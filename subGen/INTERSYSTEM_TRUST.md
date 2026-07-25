# Intersystem Trust — How Primals Discover, Verify, and Communicate

**Status**: Living document — reflects deployed IPC and trust model
**Protocol**: JSON-RPC 2.0 over UDS / TCP
**Discovery**: Capability-based via songBird mesh
**Identity**: Genetic lineage via bearDog

---

## First Principle: Self-Knowledge Only

Every primal has self-knowledge and discovers other primals at runtime.
No primal imports another primal's crate. No primal hardcodes another
primal's address, port, or socket path. The only shared artifact is the
JSON-RPC 2.0 wire format.

This constraint is not aspirational — it is enforced:

- `cargo deny` bans cross-primal crate dependencies
- CI validates that no primal's `Cargo.toml` references another primal
- Integration tests use mock RPC servers, not imported primal code
- The `zero-import` principle is documented in gen4's `COMPOSITION_PATTERNS.md`

The practical consequence: any primal can be replaced, upgraded, or removed
without touching any other primal's source code. The ecosystem is loosely
coupled at the source level and tightly composed at the wire level.

---

## Discovery — Capability Routing

### How a Primal Finds Another

1. A primal needs a capability (e.g., `lineage-verification`)
2. It queries songBird's mesh: `discovery.find_by_capability`
3. songBird returns the endpoint (UDS socket path or TCP `host:port`) of
   whatever primal currently announces that capability
4. The requesting primal connects and speaks JSON-RPC 2.0

The key insight: the requesting primal doesn't know *who* provides the
capability. It knows *what* it needs. Today `lineage-verification` is
provided by bearDog. Tomorrow it could be provided by a different primal,
or by a federated peer on another gate. The requesting primal's code
doesn't change.

### Capability Registry

Each primal publishes a `capability_registry.toml` that biomeOS reads at
deployment:

```toml
[primal]
name = "skunkbat"
protocol = "jsonrpc-2.0"
transport = ["uds", "tcp"]

[domains.security]
methods = ["scan", "detect", "respond", "metrics", "audit_log", "advisory"]

[consumed]
capabilities = ["lineage-verification", "federation", "discovery"]
```

This is a static declaration of what a primal *offers* and what it
*consumes*. It is not a runtime contract — it's a deployment manifest
that helps biomeOS build the capability graph before any primal starts.

### Environment-Based Discovery

When songBird mesh discovery isn't available (bootstrap, standalone
testing), primals fall back to environment variables:

- `LINEAGE_ENDPOINT` → bearDog TCP endpoint
- `BIOMEOS_SOCKET_DIR` → directory containing capability-named UDS sockets
  (e.g., `lineage-verification.sock`)

The `CapabilityClient` abstraction handles both paths: try UDS first
(lowest latency, strongest isolation), fall back to TCP, fall back to
"capability unavailable" with conservative defaults.

---

## Identity — Genetic Lineage

### The Trust Problem

In a mesh of gates, not every peer is equally trusted. A gate on the same
LAN switch shares physical infrastructure. A gate across the WAN shares
organizational membership. A collaborator gate shares only a contractual
relationship.

WireGuard treats all these the same: you have the key or you don't.
Tower Atomic differentiates them through *genetic lineage*.

### Lineage Verification

bearDog maintains a lineage chain — a directed graph of enrollment
relationships:

```
root → genome-alpha → gate-01
root → genome-alpha → gate-02
root → genome-beta  → collaborator-gate
```

When skunkBat needs to verify a peer, it calls `lineage.verify` on
whatever primal announces the `lineage-verification` capability:

```json
{
  "method": "lineage.verify",
  "params": { "peer_id": "gate-02" }
}
→ { "is_family": true, "lineage_chain": ["root", "genome-alpha", "gate-02"] }
```

The lineage chain determines the bond type:
- **Covalent**: Same lineage chain (same genome)
- **Metallic**: Different genome, same root
- **Ionic**: No shared lineage (contractual relationship)

### Graceful Degradation

When the lineage provider is unreachable:
- `is_family` returns `Err` (not `false` — the distinction matters)
- The caller treats unverified peers conservatively
- The system continues operating in degraded mode
- An `UnknownLineage` threat is raised if configured

No primal panics or blocks on lineage verification failure. The design
assumes the verification provider may be temporarily unavailable and
handles that as a normal operational condition.

---

## Communication — JSON-RPC 2.0

### Wire Format

Every inter-primal call is a JSON-RPC 2.0 message over newline-delimited
JSON (one JSON object per line):

```json
{"jsonrpc":"2.0","method":"security.scan","params":{"source":"10.0.0.1"},"id":1}
```

Response:
```json
{"jsonrpc":"2.0","result":{"threats":[],"scanned":true},"id":1}
```

Error:
```json
{"jsonrpc":"2.0","error":{"code":-32001,"message":"PERMISSION_DENIED"},"id":1}
```

### Transport Parity

Every method must work identically over UDS and TCP. This is not a
guideline — it is a tested invariant. The `TransportEndpoint` trait
abstracts the transport:

```rust
pub trait TransportEndpoint: Send + Sync {
    fn serve(&self, handler: impl ConnectionHandler) -> impl Future;
}
```

UDS and TCP are both `TransportEndpoint` implementations. The server
code doesn't know which transport it's using. This is how skunkBat runs
on Android (TCP-only, SELinux denies UDS) and Linux (UDS + TCP) from the
same binary.

### Error Codes

Ecosystem-standard error codes:

| Code | Name | Meaning |
|------|------|---------|
| -32700 | Parse error | Invalid JSON |
| -32600 | Invalid request | Missing jsonrpc/method |
| -32601 | Method not found | Unknown method |
| -32602 | Invalid params | Wrong parameter types |
| -32603 | Internal error | Server-side failure |
| -32000 | Unauthorized | Invalid token signature |
| -32001 | Permission denied | Missing capability token |

---

## Trust Composition

The full trust flow for a cross-gate capability call:

```
1. Caller discovers provider via songBird mesh
2. TCP connection established (Layer 0: network binding)
3. BTSP Phase 1: protocol detection (Layer 1: transport)
4. BTSP Phase 2: mutual identity via bearDog (genetic lineage)
5. BTSP Phase 3: cipher negotiation (bond type → cipher minimum)
6. MethodGate: capability token check (Layer 2: authorization)
7. Dispatch: method execution
8. Audit: event recorded (Layer 6: audit trail)
```

Each step can fail independently. A connection that passes identity
verification (step 4) but fails MethodGate (step 6) is a verified
peer attempting an unauthorized operation — logged differently than
an unknown peer (step 4 failure).

The trust model is not binary. It is a spectrum: from fully trusted
(covalent bond + BTSP + valid token) to completely untrusted (unknown
peer + no BTSP + no token). The system's response is proportional
to the trust level established.

---

## Capability Announcement vs. Trust-on-First-Use

Current state: capability announcements are accepted on first contact.
If a primal announces `lineage-verification`, the mesh registers it
without independent verification that the primal actually provides
that capability correctly.

This is a known P2 gap (Wave 150x):
- **Capability announcement validation**: Trust-on-first-use needs
  verification — can the announced capability actually be consumed?
- **Capability revocation**: No mesh-wide revocation mechanism yet.
  If a primal is compromised, its capabilities remain registered until
  the primal is restarted or manually deregistered.

These are not blocking for current deployment (LAN mesh with physical
access control) but will need to be addressed for WAN federation.

---

*subGen Wave 150x — Self-knowledge only, capability routing, genetic
lineage, JSON-RPC 2.0, trust spectrum.*
