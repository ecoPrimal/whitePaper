# Contract Testing Thesis Sketch

**Status**: SKETCH (May 11, 2026)
**Origin**: Wave 7 semantic gate evolution (primalSpring)
**Context**: NestGate content.* transport parity gap — downstream composition
pressure exposed a gap class where methods were registered but never exercised.

## The Lesson

NestGate implemented `content.put` through `content.collections` on its primary
Unix socket dispatch path (content_handlers.rs, BLAKE3 CAS with dedup, sidecar
metadata, manifest-based collections). But `SemanticRouter`, isomorphic IPC, and
HTTP API did not route `content.*` — only `storage.*`, health, session, crypto.

primalSpring's gate validated **structural** consistency (methods registered in
the 413-method registry, health alive, deploy graphs referencing correct
capabilities) but not **semantic** correctness (methods actually serve correct
responses across all transports).

The gap reached projectNUCLEUS. `publish_sporeprint.sh` called `content.put`
through a transport path that lacked routing. "Method not found."

## The Thesis: Wire Format IS the Contract

gen4's `DEPLOY_GRAPH_COMPOSITION.md` states this explicitly (§5.2): the only
composition contract between layers is JSON-RPC 2.0 over UDS/TCP. No shared
crates. No Cargo imports from primals. The wire format is the contract.

But a contract that is never tested is a promise that is never kept.

### Corollary: Test at Every Transport Boundary

If the wire format is the contract, then every transport path that claims to
serve a method must be independently tested. NestGate had four transport paths:

| Transport | `content.*` tested? | Result |
|-----------|-------------------|--------|
| Primary `unix_socket_server/dispatch.rs` | No | Worked (but untested) |
| `SemanticRouter::call_method` | No | Method not found |
| Isomorphic IPC `UnixSocketRpcHandler` | No | Method not found |
| `nestgate-api` HTTP `NestGateRpcHandler` | No | Method not found |

**Zero** of four paths were tested. Three of four were broken.

### Corollary: Registered but Never Exercised = Technical Debt

The 413-method registry listed `content.*` as NestGate-owned. The drift check
(`check_method_strings.sh`) verified that Rust source strings matched the
registry. But no check verified that methods in the registry were **exercised**
in any scenario, test, or graph.

This is the "registered but never exercised" gap class. Wave 7's inverse drift
detector (`check_method_coverage.sh`) catches it: any registered method not
referenced in scenarios, tests, or graphs is flagged.

## Connecting to gen4 Concepts

### Novel Ferment Transcripts (NFTs)

NFTs derive value from **accumulated history** — an append-only DAG of events
sealed by the provenance trio (rhizoCrypt + loamSpine + sweetGrass) and signed
by BearDog. The contract chain is:

1. `dag.session.create` → event DAG opened
2. `dag.event.append` → vertices accumulated
3. `dag.session.complete` → Merkle root sealed
4. `spine.create` + `entry.append` → loamSpine dehydration certificate
5. `braid.create` → sweetGrass attribution braid
6. BearDog signature → integrity seal

Each step is a JSON-RPC call across a transport boundary. Each is a contract.
If any step is registered-but-never-exercised, the NFT pipeline is structurally
plausible but semantically broken — exactly the NestGate content.* pattern.

**Implication**: The contract testing thesis applies recursively to every
multi-primal pipeline. The NFT provenance chain needs end-to-end contract
tests spanning all four primals in the trio + BearDog.

### Composition Patterns

`COMPOSITION_PATTERNS.md` defines `PrimalBridge` as the composition surface:
JSON-RPC client pool with circuit breaker and graceful degradation across four
tiers (Full / Partial / Minimal / Standalone).

Each degradation tier defines a **different contract**: Full tier promises all
methods; Standalone promises none. Contract tests must cover tier transitions:

- **Tier transition tests**: What happens when NestGate drops from Full to
  Partial? Does the bridge return correct errors, or does it silently lose
  `content.*` while keeping `storage.*`?
- **Circuit breaker tests**: When a primal is unreachable, does the bridge
  correctly report SKIP (not FAIL) and degrade gracefully?

### Stadial/Interstadial Pattern

`STADIAL_INTERSTADIAL_PATTERN.md` defines the two-tier gate:

- **Tier 1 (structural)**: Build, lint, unit tests, deny lists — no external
  dependencies. Cheap. Run on every commit.
- **Tier 2 (behavioral)**: Live composition, IPC round-trips, token federation —
  requires deployed primals. Expensive. Run as gate.

Wave 7 evolves Tier 2 from health-check-only to **contract testing**: methods
are not just discoverable but provably functional across all transports.

### guideStone + Consumer-as-Verifier

`GUIDESTONE.md` establishes the "consumer-as-verifier" pattern: guideStone
artifacts carry their own validation (CHECKSUMS, `expected/`, tolerance
metadata). The consumer re-runs `./run` and verifies output against reference.

Contract testing is the **composition-level analog**: primalSpring doesn't
trust that NestGate serves `content.put` because it's registered. It verifies
by calling `content.put` and checking the response. Consumer-as-verifier at
the wire level.

## Wave 7 Implementation Map

| Wave 7 Item | gen4 Grounding | Status |
|-------------|---------------|--------|
| W7-01: `content` in `ALL_CAPS` + routing | DEPLOY_GRAPH_COMPOSITION §5.2 — capability routing IS the contract surface | **DONE** |
| W7-02: `s_nestgate_content_pipeline` scenario | COMPOSITION_PATTERNS — PrimalBridge contract test template | **DONE** |
| W7-03: Gate tests in `server_ecosystem_compose.rs` | STADIAL_INTERSTADIAL_PATTERN — Tier 2 behavioral gate | **DONE** |
| W7-04: `content_pipeline_smoke.toml` graph | DEPLOY_GRAPH_COMPOSITION — graph-as-contract | **DONE** |
| W7-06: `check_method_coverage.sh` inverse drift | NOVEL_FERMENT_TRANSCRIPTS — registered-but-unexercised = broken pipeline | **DONE** |
| W7-05: `content.resolve` for petalTongue backend | COMPOSITION_PATTERNS — degradation tier cross-primal contract | OPEN (NestGate transport parity first) |
| W7-07: NestGate transport parity verification | DEPLOY_GRAPH_COMPOSITION §5.2 — test at every transport boundary | OPEN (NestGate must wire routing) |

## Future Contract Testing Axes

### Per-Domain Contract Suites

The inverse drift detector shows 125/413 methods unexercised. Priority domains
for contract suites beyond `content.*`:

| Domain | Methods | Gap Risk | Priority |
|--------|---------|----------|----------|
| `secrets.*` | 4 | High — BearDog crypto secrets, untested in composition | HIGH |
| `bonding.*` | 4 | Medium — bond lifecycle untested end-to-end | MEDIUM |
| `spine.*` / `entry.*` | 6 | High — loamSpine certificate pipeline, NFT chain | HIGH |
| `braid.*` | 3 | Medium — sweetGrass attribution, NFT chain | MEDIUM |
| `inference.*` | 3 | Medium — squirrel AI pipeline | LOW (springs test directly) |

### Transport Parity Matrix

For every primal with multiple transport paths (NestGate has 4, others may have
2-3), a transport parity matrix should verify that all registered methods are
reachable on all claimed transports:

```
primal × method × transport → {reachable, correct_response, error_shape}
```

This is the generalization of the NestGate content.* lesson.

### NFT Pipeline Integration Test

Once provenance trio contract suites exist, compose them into an end-to-end
NFT pipeline test:

```
session.create → event.append × N → session.complete → spine.create →
entry.append(cert) → braid.create(attribution) → verify(Merkle_root, sig)
```

This validates the entire Novel Ferment Transcript chain as a composition
contract, not just individual primal methods.

---

*This sketch connects primalSpring's Wave 7 evolution to the gen4 thesis.
The wire format is the contract. The contract must be tested at every
transport boundary. Registered but never exercised is technical debt.*
