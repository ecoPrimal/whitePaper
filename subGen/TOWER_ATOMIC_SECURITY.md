# Tower Atomic — Transport Security Architecture

**Status**: Living document — reflects deployed BTSP implementation
**Primals**: bearDog (key material, signing), songBird (routing, mesh),
skunkBat (negotiation, cipher floor, session management)
**Performance**: 353× LAN (0.45ms vs 158ms WireGuard), 1.7× WAN sustained

---

## What Tower Atomic Replaces

WireGuard provides a single encrypted tunnel between two endpoints. Every
packet gets the same treatment — no content awareness, no capability routing,
no trust differentiation. Tower Atomic replaces this with a multi-layer,
capability-aware transport that understands *what* is being carried and
*who* is carrying it.

| Dimension | WireGuard | Tower Atomic |
|-----------|-----------|-------------|
| Routing | Point-to-point tunnel | Capability-aware mesh routing |
| Encryption | Single static key per tunnel | Per-session, bond-aware cipher selection |
| Trust model | Binary (key or no key) | Three-tier (Covalent/Metallic/Ionic) |
| Content awareness | None | Protocol-level content routing |
| Minimum cipher | Fixed | Server-configurable cipher floor |
| Platform | Kernel module | Userspace (cross-platform) |

---

## BTSP Protocol — Three Phases

### Phase 1 — Connection + Protocol Detection

When a TCP connection arrives, the server peeks at the first bytes to
determine intent:

1. **JSON-RPC probe**: Plaintext `{` — Legacy JSON-RPC client, no encryption.
   Accepted in permissive mode, rejected in enforced mode.
2. **BTSP handshake**: `BTSP` magic bytes — Client speaks the transport
   protocol. Proceeds to Phase 2.
3. **Unknown**: Neither pattern matches. Connection closed.

This peek-based detection allows a single port to serve both legacy and
BTSP clients during migration, without protocol negotiation overhead.

### Phase 2 — Mutual Identity Verification

The BTSP handshake establishes mutual identity:

1. Client sends `BTSP` + protocol version + client identity
2. Server validates identity via bearDog's `btsp.session.verify`
3. bearDog returns a handshake key (derived from `FAMILY_SEED`) if the
   client is verified, or `None` for unknown peers
4. Server registers a `SessionState` in the `SessionRegistry`

The handshake is *authentication*, not *encryption*. A verified peer with
no encryption (null cipher) is still authenticated — the server knows who
it's talking to. This separation matters: authentication gates access,
encryption protects content. They are independent.

### Phase 3 — Cipher Negotiation

After Phase 2, the client sends a `btsp.negotiate` JSON-RPC call:

```json
{
  "method": "btsp.negotiate",
  "params": {
    "session_id": "...",
    "client_nonce": "<base64>",
    "ciphers": ["chacha20-poly1305"],
    "bond_type": "Ionic"
  }
}
```

The server selects the best cipher through a four-step process:

1. **Key availability**: No handshake key → null cipher (can't encrypt
   without key material, regardless of what client offers)
2. **Strongest offered**: Select the strongest cipher from the client's
   `ciphers` array
3. **Bond-type minimum**: If `bond_type` is specified, enforce its minimum:
   - `Covalent` (genetic lineage): Any cipher, including null
   - `Metallic` (organizational): Minimum HMAC integrity
   - `Ionic` (contractual): Full AEAD encryption required
4. **Server cipher floor**: `SKUNKBAT_CIPHER_FLOOR` env var sets a
   deployment-wide minimum, independent of client preferences

If the selected cipher fails to meet either the bond-type minimum or the
server floor, negotiation falls back to null — the caller decides whether
to proceed or disconnect. This is a deliberate design choice: the
negotiation layer reports what it *can* do, the application layer decides
what it *will* do.

#### Key Derivation

When a non-null cipher is negotiated:

```
HKDF-SHA256(
  ikm = handshake_key,          // From bearDog Phase 2
  salt = client_nonce || server_nonce
)
expand(info = "btsp-session-v1-c2s") → client_to_server key (32 bytes)
expand(info = "btsp-session-v1-s2c") → server_to_client key (32 bytes)
```

Directional keys prevent reflection attacks. The server encrypts with
`s2c`, decrypts with `c2s`. The client does the inverse.

#### Wire Format

Encrypted frames: `nonce(12) || ciphertext || tag(16)`

- ChaCha20-Poly1305 AEAD
- Random nonce per frame (not counter-based — eliminates nonce-reuse risk
  at the cost of slightly larger frames)
- Minimum frame size: 28 bytes (12 nonce + 16 tag)

---

## Cipher Suites

| Suite | Wire Name | Confidentiality | Integrity | Status |
|-------|-----------|-----------------|-----------|--------|
| Null | `null` | No | No (handshake-only) | Implemented |
| HMAC-Plain | `hmac-plain` | No | HMAC-SHA256 per frame | Protocol-defined, wire TBD |
| ChaCha20-Poly1305 | `chacha20-poly1305` | Yes (AEAD) | Yes (Poly1305 tag) | Implemented |

HMAC-Plain is recognized in negotiation but not yet wired at the frame
level — it requires a separate frame codec path. When implemented, it
provides integrity verification without confidentiality, useful for
high-throughput LAN scenarios where eavesdropping risk is low but
tampering risk exists.

---

## Bond Types — Trust-Tier Enforcement

Bond types map the biological bonding metaphor to transport security
requirements:

### Covalent (Genetic Lineage)

Peers verified through bearDog's genetic lineage — same organism. Highest
trust tier. Any cipher is acceptable because identity is verified through
the strongest mechanism available (shared `FAMILY_SEED` lineage).

Example: Two gates on the same LAN mesh that share a lineage chain.

### Metallic (Organizational)

Peers within the same organizational boundary but without genetic lineage
verification. Minimum HMAC integrity required — tampering must be detectable
even if eavesdropping is considered acceptable.

Example: A collaborator gate that joins the mesh through a federations
endpoint but isn't enrolled in the genetic lineage.

### Ionic (Contractual)

Peers connected through a contractual or transactional relationship. Full
AEAD encryption required — no data crosses the boundary without
confidentiality and integrity.

Example: An external service consuming `security.advisory` via Tower HTTP
Gateway.

---

## Cipher Floor Policy

The cipher floor is a server-side enforcement mechanism independent of
client negotiation:

```
SKUNKBAT_CIPHER_FLOOR=chacha20-poly1305
```

When set, any negotiation that would result in a cipher weaker than the
floor is rejected (falls back to null, which the application layer treats
as "connection denied for sensitive operations").

This addresses the pen-test finding `s_tower_pen_cipher_downgrade`: a
malicious client cannot negotiate a weaker cipher than the deployment
mandates, regardless of what it offers in `ciphers`.

The floor is deployment-configurable, not compiled in. A LAN-only gate
might set no floor (allowing null for performance-sensitive local traffic).
A VPS-exposed gate sets `chacha20-poly1305` as floor. The code enforces
whatever the operator configures.

---

## Session Management

### Registry

Active BTSP sessions are tracked in a `SessionRegistry` (concurrent
`HashMap` behind `RwLock`):

- **Insert**: After Phase 2 verify succeeds
- **Update**: After Phase 3 negotiate completes (cipher + derived keys)
- **Remove**: On disconnect or timeout
- **Sweep**: TTL-based eviction of expired sessions

### Session State

Each session tracks:
- `created_at`: For TTL sweep
- `cipher`: Negotiated cipher suite
- `session_key`: Handshake key from bearDog (if provided)
- `phase3_keys`: Derived directional keys (encrypt + decrypt)

### Key Redaction

`SessionKeys` implements `Debug` with `[REDACTED]` fields — key material
never appears in logs, traces, or debug output.

---

## What Tower Does Not Do

Tower Atomic is a transport-layer protocol. It deliberately does not:

- **Store keys on disk**: All key material is ephemeral (session-scoped).
  Persistent identity is bearDog's responsibility.
- **Manage identity**: Identity verification is delegated to bearDog.
  Tower transports authenticated sessions, it doesn't create them.
- **Route application logic**: Content routing is songBird's responsibility.
  Tower provides the encrypted pipe, songBird decides what flows through it.
- **Detect threats**: Anomaly detection is skunkBat's responsibility.
  Tower provides the transport telemetry, skunkBat interprets it.

This separation of concerns is the Tower Atomic composition model:
`bearDog` (identity) + `songBird` (routing) + `skunkBat` (defense) =
sovereign transport stack.

---

*subGen Wave 150x — BTSP Phase 1–3 as implemented. 353× LAN, 1.7× WAN.
Cipher floor policy deployed. Bond-type enforcement live.*
