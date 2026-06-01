# RootPulse Case Study — Neural API in Action

**Provenance trio end-to-end with real execution traces**

**Date**: March 13, 2026 (revised May 14, 2026 — Barrick Lab convergence)
**Status**: Whitepaper - Case Study

---

## The Provenance Trio

Three primals compose the RootPulse version-control niche. Each has a distinct temporal and structural model:

| Primal | Version | Tests | Model |
|--------|---------|-------|-------|
| rhizoCrypt | v0.13.0-dev | 862 | Ephemeral DAG, dehydration, slices |
| LoamSpine | v0.8.0 | 700 | Permanent linear history, certificates |
| sweetGrass | v0.7.3 | 746 | W3C PROV-O attribution, braids |

rhizoCrypt holds the mutable present (session DAG). LoamSpine holds the immutable past (append-only spine). sweetGrass adds semantic attribution (who contributed what). The Neural API orchestrates them via capability calls and graph execution.

---

## Deployment Graph

`provenance_trio_deploy.toml` orchestrates startup in dependency order:

```
Tower verification (BearDog, Songbird)
    → LoamSpine (permanence)
    → rhizoCrypt (ephemeral DAG)
    → sweetGrass (attribution)
    → capability registration
```

LoamSpine must start first; rhizoCrypt and sweetGrass dehydrate and anchor to it. Tower provides discovery and signing.

---

## The RootPulse Commit Workflow (rootpulse_commit.toml)

The 6-phase workflow collapses ephemeral session state into permanent history. Real JSON-RPC traces from a March 13, 2026 run:

### Phase 1 — Health

```json
{"jsonrpc":"2.0","method":"system.health","params":{},"id":1}
→ {"healthy":true,"state":"running","active_sessions":1}
```

### Phase 2 — Dehydrate

Session created via `dag.session.create`. Events appended via `dag.event.append`: SessionStart, DataCreate, DataModify, AgentAction, SessionEnd. Then `dag.dehydrate` computes the Merkle tree and extracts the frontier:

```json
{"method":"dag.dehydrate","params":{"session_id":"..."}}
→ {"merkle_root":"b4af34d8aa1a96426e9908164cf3168bddb15dee0da461152be9185eba7a5ac8",...}
```

### Phase 3 — Sign

BearDog `crypto.sign` via Unix socket. Ed25519 signature over the dehydration summary.

### Phase 4 — Store

NestGate `storage.store` persists payload. Skipped in minimal config (no NestGate).

### Phase 5 — Commit

```json
{"capability":"commit","operation":"session","args":{"summary":{...},"content_hash":"..."}}
→ {"accepted":true,"commit_id":"17f721c7...","entry_index":1}
```

### Phase 6 — Attribute

sweetGrass `contribution.recordDehydration` creates the braid. `braid.create` emits W3C PROV-O entity for semantic attribution.

The graph uses `coordination = "Sequential"`. Each phase depends on the previous output. Phase 5 (commit) depends on both Phase 4 (store) and Phase 1 (health); when NestGate is skipped, the store node is short-circuited and content_hash falls back to merkle_root.

---

## Type Alignment

The wire format flows cleanly across primals:

- **DehydrationSummary** (rhizoCrypt) matches **PermanentStorageCommitRequest** (LoamSpine). Merkle root, frontier, event hashes map 1:1.
- sweetGrass has a richer format (braids, agent roles, contribution weights). Extra fields are optional; defaults suffice for minimal attribution.

No schema translation layer. The trio was designed for this handoff.

---

## E2E Test Infrastructure

biomeOS provides `provenance_trio_e2e.rs` with five integration tests:

1. Graph parsing (provenance_trio_deploy, rootpulse_commit)
2. Health checks for all trio primals
3. Capability registration verification (dag, permanent_storage, attribution)
4. Full RootPulse commit flow (create session → dehydrate → sign → store → commit → attribute → verify)
5. Graph execution via `graph.execute(rootpulse_commit)`

Tests are gated behind `#[ignore]` for CI; they require Tower, rhizoCrypt, LoamSpine, sweetGrass, and optionally NestGate.

---

## Cross-Spring Validation

ludoSpring exp052 ran 37 provenance trio integration checks: **37/37 passed**. Validates:

- Game session DAG creation, vertex append, frontier tracking (rhizoCrypt)
- Ruleset/card certificate minting, ownership (LoamSpine)
- Game action braids, PROV-O attribution, agent linking (sweetGrass)
- biomeOS graph topology, budget fit, dependency satisfaction
- Cross-primal round-trip: game action → vertex → certificate → braid

---

## What Neural API Learns

Over time, the Pathway Learner would discover:

- **rhizoCrypt → LoamSpine dehydration is always sequential**. The commit depends on the merkle root; no parallelization.
- **sweetGrass attribution can run in parallel with NestGate storage**. Both consume the signed summary; no data dependency between them.
- **BearDog signing is the latency bottleneck**. Ed25519 via Unix socket dominates phase latency. Pre-warming or batching could help.

These patterns are not programmed. They emerge from observing execution traces. RootPulse provides signal at human pace (~100 commits/day). The game engine niche (08_NICHE_API_PATTERNS.md) provides 50,000x more signal at 60 Hz.

---

## Relationship to Series

This document fills the slot described in README.md as "09_ROOTPULSE_CASE_STUDY.md — First transactional niche". It grounds the conceptual framework from 00_INTRODUCTION.md (three-layer architecture) and 06_BIOMEOS_IMPLEMENTATION.md (graph execution, metrics, Pathway Learner) in a real end-to-end run. The provenance trio is the first niche to execute fully via Neural API graphs.

---

---

## May 2026 Addendum: Barrick Lab Convergence

### Updated Trio State

| Primal | Version | Tests | Key Evolution |
|--------|---------|------:|--------------|
| rhizoCrypt | v0.13.0+ | 1,637+ | `dag.session.get` enriched with agents/genesis/frontier |
| LoamSpine | v0.8.0+ | 1,442+ | Immutable record with witness-bearing commits |
| sweetGrass | v0.7.3+ | 1,522 | JH-0 gate + port 9850 canonical |

All three at zero debt. BTSP AEAD 3/3. MethodGate 3/3.

### Barrick Lab Tool Convergence

The Barrick Lab software list (https://barricklab.org/twiki/bin/view/Lab/SoftwareList)
has been handed to lithoSpore. These tools map directly onto the RootPulse
provenance pattern:

| Barrick Tool | Pipeline | lithoSpore Module | Provenance Flow |
|-------------|----------|-------------------|----------------|
| **breseq** | C++/Python → mutation calls | Module 6 (ltee-breseq) | breseq output → `nest.store` → Merkle proof |
| **pLannotate** | Python → plasmid annotation | New candidate | Annotation → `nest.store` → attribution braid |
| **OSTIR** | Python → translation rates | Module 5 (biobricks) | Rate data → `nest.store` → reproducibility record |
| **EFM Calculator** | Python/Django → failure modes | Module 3 (clonal) | Hypermutable sites → `nest.store` → validation target |
| **CryptKeeper** | Python → burden prediction | New candidate | Burden data → `nest.store` → comparison baseline |

Each tool produces scientific data that flows through the same provenance
trio commit pattern: compute → dehydrate → sign → store → commit → attribute.
The Python/R pipelines are Tier 1 baselines; Rust lithoSpore modules are
Tier 2 reproductions validated against them.

**petalTongue visualization target**: Barrick tools have published figures
(mutation frequency plots, fitness trajectories, phylogenetic trees).
These become concrete render targets for petalTongue's grammar of graphics,
served from NestGate content, with provenance braids from sweetGrass.

### Atomic Signal for Barrick Pipelines

The full Barrick pipeline maps to a signal composition:

```
node.compute (Rust reproduction)
  → nest.store (provenance commit via trio)
    → petalTongue.visualize (figure generation)
```

This is `node.compute` + `nest.commit` — two atomic signals composing
the entire scientific reproduction pipeline. The 427-method surface
collapses to 2 signals for any Barrick reproduction.

---

*"The provenance trio is not three services. It is one temporal collapse — ephemeral to permanent — orchestrated by graphs that learn."*
