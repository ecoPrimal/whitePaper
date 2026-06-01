# RootPulse — Emergent Version Control

**Universal temporal tracking through primal coordination**

**Updated**: June 1, 2026 (Wave 66)
**Vocabulary**: `gen5/foundations/FUNCTIONAL_PATTERN_CONVERGENCE.md`

---

## White Paper Series

RootPulse is not a primal. It is a coordination pattern — a set of TOML
composition graphs that biomeOS dispatches over existing primals. Version
control, game session provenance, scientific experiment tracking, and RPG
session DAGs all use the same temporal primitives with different graph
topologies.

RootPulse is the ACTION domain of the coordination triad (qS SENSE /
wF SYNC / rP ACTION). Where waterFall propagates state across gates,
RootPulse creates the versioned artifacts that waterFall carries. The
provenance trio (rhizoCrypt, loamSpine, sweetGrass) provides the recording
substrate for both.

### Documents

**Core Concepts**

1. **[00_INTRODUCTION.md](./00_INTRODUCTION.md)** — What is RootPulse?
2. **[01_PHILOSOPHY.md](./01_PHILOSOPHY.md)** — Emergence vs monoliths
3. **[02_ARCHITECTURE.md](./02_ARCHITECTURE.md)** — Technical design
4. **[04_DAG_VS_LINEAR.md](./04_DAG_VS_LINEAR.md)** — Two-tier temporal architecture

**Primal Coordination**

5. **[03_PRIMAL_COMPOSITION.md](./03_PRIMAL_COMPOSITION.md)** — How primals work together
6. **[06_COORDINATION_PATTERNS.md](./06_COORDINATION_PATTERNS.md)** — Deploy and workflow graph definitions

**Features**

7. **[08_SEMANTIC_ATTRIBUTION.md](./08_SEMANTIC_ATTRIBUTION.md)** — SweetGrass integration (three-layer model)
8. **[12_API_REFERENCE.md](./12_API_REFERENCE.md)** — JSON-RPC API reference

---

## RootPulse is NOT a Primal

Pulse is what primals DO together, not what they ARE.

Six existing primals compose the temporal coordination stack:

| Primal | Role | Version | Tests |
|--------|------|---------|------:|
| **rhizoCrypt** | Ephemeral DAG (present/future) | v0.13.0 | 862 |
| **LoamSpine** | Immutable history (past) | v0.8.0 | 700 |
| **sweetGrass** | Semantic attribution | v0.7.3 | 746 |
| **NestGate** | Content-addressed storage | Production | — |
| **BearDog** | Cryptographic signing | v0.15.0 | — |
| **Songbird** | Federated discovery | v3.6 | — |

biomeOS executes graphs over these primals. The graphs define
coordination patterns. No new primal needed.

---

## Two-Tier Temporal Architecture

- **rhizoCrypt (DAG)** — The present/future: branching, lock-free, 10-100x faster than Git staging
- **LoamSpine (Linear)** — The past: immutable, provable, append-only
- **Dehydration** — Temporal collapse from DAG to linear (flexible timescales)
- **Anchors** — Multiple orderings: crypto, atomic, causal, consensus

See [04_DAG_VS_LINEAR.md](./04_DAG_VS_LINEAR.md) for the deep dive.

---

## Composition Graphs (biomeOS)

All RootPulse operations are TOML composition graphs dispatched by biomeOS:

| Graph | Coordination | Phases |
|-------|:------------:|--------|
| `rootpulse_commit.toml` | Sequential | Health -> Dehydrate -> Sign -> Store -> Commit -> Attribute |
| `rootpulse_branch.toml` | Sequential | Validate -> Create session -> Create spine -> Attribute |
| `rootpulse_merge.toml` | Sequential | Health -> Dehydrate -> Sign -> Merge commit -> Seal -> Attribute |
| `rootpulse_diff.toml` | Sequential | Health -> Get commits -> Compare Merkle -> Diff provenance |
| `rootpulse_federate.toml` | Sequential | Discover -> Exchange tips -> Fetch -> Verify -> Append -> Attribute |

All graphs use capability-based routing (`dag.dehydrate` -> rhizoCrypt,
`commit.session` -> LoamSpine, `provenance.create_braid` -> sweetGrass,
`crypto.sign` -> BearDog). No primal names in the graphs.

---

## Beyond Version Control

The same temporal primitives serve any domain where events need
sequencing, signing, attribution, and permanence:

| Domain | Pattern | Graph | Who |
|--------|---------|-------|-----|
| Code commits | VCS | `rootpulse_commit.toml` | RootPulse |
| Game sessions | Frame | `game_engine_tick.toml` + provenance at session boundaries | ludoSpring RPGPT |
| Scientific experiments | Scientific | `provenance_pipeline.toml` | wetSpring, groundSpring |
| Field samples | Collection | Custom sequential | wetSpring (exp062) |
| Medical records | Consent-gated | Custom sequential | healthSpring (exp063) |
| Art/music creation | Moments | Custom sequential | sweetGrass attribution |
| RPG campaigns | Session DAG | Continuous + transactional | ludoSpring RPGPT |

ludoSpring's RPGPT engine (Paper 18) treats game sessions as rhizoCrypt
DAGs: turns, rolls, conditions, and branches are vertices. Rulesets are
LoamSpine certificates. Player/AI attribution flows through sweetGrass.
Anti-cheat reduces to chain-of-custody verification — the same pattern
that tracks sample lineage in field genomics. Same primals, same graphs,
different vocabulary.

---

## gen4 Context — RootPulse as Conceptual Bridge

RootPulse is the conceptual engine behind the gen3→gen4 transition. It proves
that complex systems emerge from primal coordination — the same 6 primals
with different TOML graphs produce version control, game session tracking,
sample provenance, and medical records. This emergence proof is what makes
gen4 possible: if temporal coordination emerges, so can game engines, science
pipelines, and eventually a sovereign operating system.

### gen4 Products That Use RootPulse Patterns

| Product | RootPulse Pattern | What Emerges |
|---------|-------------------|-------------|
| esotericWebb | Session DAG + provenance lifecycle | Game session tracking with attribution |
| helixVision | Sample → analysis → publication provenance | Field-to-publication chain-of-custody for genomic samples |
| RPGPT Engine | Continuous + transactional | Campaign history with anti-cheat as chain-of-custody |

### RootPulse → biomeOS OS Trajectory

The temporal coordination that RootPulse provides is what an OS filesystem
needs: version history, provenance, branching, federation. In the biomeOS OS
trajectory (`gen4/architecture/BIOMEOS_OS_TRAJECTORY.md`), RootPulse patterns
become the filesystem layer — files don't just exist, they have provenance.

See `gen4/` for the full gen4 documentation (22 working papers).

---

## Implementation Status (June 1, 2026)

| Component | Status |
|-----------|--------|
| Provenance trio (rhizoCrypt + LoamSpine + sweetGrass) | Production ready (2,308+ tests combined) |
| 6-phase commit composition | Validated end-to-end |
| Composition graphs (commit, branch, merge, diff, federate) | All defined in `primalSpring/graphs/signals/` |
| Capability routing | 320+ translations across 27 domains |
| E2E tests (`provenance_trio_e2e.rs`) | 5 integration tests |
| Cross-spring validation (ludoSpring exp052) | 37/37 checks passed |
| Cross-domain provenance (exp062-066) | 228/228 checks (gaming, science, medical) |
| `CompositionContext::signal("nest", "commit", ...)` | Implemented — dispatches to composition graph |
| Agentic sync (wF + rP + trio) | **Wave 66** — `sync_resolve.toml` uses trio for provenance recording |
| Phase A composition definition | **Complete** — 32 graphs including 5 rootPulse compositions |
| `rootpulse` CLI frontend | Not yet implemented |
| NestGate <-> LoamSpine content integration | Needs implementation |

### What RootPulse needs from biomeOS (Phase B)

1. **Composition dispatch in NeuralRouter** — Phase B of the composition
   layer: NeuralRouter recognizes composition-tier capabilities and loads
   the corresponding graph instead of direct single-method routing.

2. **Continuous + transactional mixed mode** — RPGPT needs 60 Hz game
   ticks (continuous) with provenance commits at session boundaries
   (transactional). Currently these are separate execution paths.

3. **Continuous execution via Neural API** — `graph.start_continuous`,
   `graph.pause`, `graph.resume`, `graph.stop` JSON-RPC methods so
   game sessions can be managed programmatically, not just via CLI.

4. **ConditionalDag** — RPGPT needs conditional flows: if squirrel AI
   is available, use AI narration; else use template narration.

---

## Core Principles

1. **Emergence over monoliths** — Complex systems arise from simple coordination
2. **Composition over creation** — Reuse temporal primitives, don't rebuild
3. **Sovereignty** — You own your code, your history, your infrastructure
4. **Provenance** — Cryptographic proofs, not just trust
5. **Attribution** — Semantic contributions, not line counts
6. **Federation** — Distributed by design, no central authority

---

## Related Work

- **[FUNCTIONAL_PATTERN_CONVERGENCE.md](../gen5/foundations/FUNCTIONAL_PATTERN_CONVERGENCE.md)** — The Two Threes (canonical triad/trio vocabulary)
- **[Neural API](../neuralAPI/)** — biomeOS composition dispatch layer
- **[waterFall](../waterFall/)** — Temporal ecosystem sync (SYNC domain of the triad)
- **[waterFall/09_AGENTIC_SYNC.md](../waterFall/09_AGENTIC_SYNC.md)** — Agentic sync — fullest triad + trio composition
- **[ludoSpring](../../ludoSpring/)** — RPGPT composition, exp052 trio validation

### Primal Repositories
- **rhizoCrypt** — Ephemeral DAG workspace (provenance trio)
- **loamSpine** — Immutable linear history (provenance trio)
- **sweetGrass** — Semantic attribution (provenance trio)
- **bearDog** — Cryptographic primitives
- **nestGate** — Content-addressed storage
- **songbird** — Federated discovery

### Fossil Record

The `whitePaper_RootPulse/` subdirectory contains a gen4-era version of this
documentation (December 2025). It is retained as fossil record — the parent
`RootPulse/` directory is the living document.

---

## License

Part of the ecoPrimals ecosystem. AGPL-3.0-or-later.
See individual primal licenses for details.

