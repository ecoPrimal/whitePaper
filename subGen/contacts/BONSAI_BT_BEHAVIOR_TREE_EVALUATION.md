# Bonsai-BT: Behavior Tree Evaluation for Neural API

**Source**: Reddit discovery (public)
**Date**: Aug 2026
**Repo**: https://github.com/Sollimann/bonsai
**Crate**: `bonsai-bt` v0.13.0 (~790 stars, 207 commits, active development)
**License**: MIT
**Relevance**: Neural API execution semantics, squirrel agent orchestration

---

## Core Insight

Bonsai-BT provides **deterministic orchestration over nondeterministic actions**. The fundamental object is `Behavior<A>` where `A` is application-defined. The engine supplies composition: `Sequence`, `Select`, `If`, `Invert`, loops, `WhenAll`, `WhenAny`, `Race`, `After`, plus reactive/memoryless variants.

The key architectural contribution to ecoPrimals:

```
LLM = proposes
BT  = constrains
Primal = executes
SweetGrass = witnesses
BearDog = attributes
Songbird = coordinates
```

This separates **reasoning** from **execution control** — the tree isn't the agent, it decides *when/why* the agent calls capabilities.

---

## Architectural Fit: biomeOS Neural API Primitive

Behavior trees belong **inside biomeOS as a native execution semantic**, not as a separate layer above or below it.

### Two Complementary Graph Forms

The Neural API already has capability/data graphs (TOML-defined compositions). Bonsai adds a second form:

**Capability Graph** (existing): What capabilities must be composed?

```
sign → store → attribute → sync
```

**Behavior/Control Graph** (new): Under what conditions, in what order, with what fallback?

```
Sequence
├── identity.available?
├── Select
│   ├── local.compute
│   ├── mesh.compute
│   └── cpu.fallback
├── validate
└── commit
```

These nest — a behavior-tree leaf can invoke an entire capability graph.

### Critical Design Constraint

**Bonsai leaves must never know primal names.** They use Neural API signals:

```
compute.execute    (not ToadStool.submit)
crypto.sign        (not BearDog.sign)
storage.put        (not NestGate.put)
provenance.commit  (not SweetGrass.braid)
```

This makes trees **portable** — serialized on westGate, executable on any gate. biomeOS resolves the capability to whichever primal currently advertises it.

---

## Key Properties

### Stateful vs Reactive Execution

Bonsai distinguishes `.memory(true)` (resume running child) from `.memory(false)` (recheck prerequisites every tick). Highly relevant to distributed systems:

```
Sequence(memoryless)
├── NetworkAvailable?
├── NodeAuthenticated?
├── NodeHealthy?
├── CapacityAvailable?
└── ExecuteJob
```

Reactive policy encoded as structure rather than prompt instructions.

### Lightweight Runtime

Core crate has minimal deps (optional `serde`, `serde_json`, `petgraph`, `tungstenite`). No async runtime dragged in. Long-running work dispatched externally, reported back to tree. Compatible with existing biomeOS/songBird dispatch.

### Python Bindings

Thin binding over Rust implementation — same semantics, not a reimplementation. Enables `Rust primal ⟷ Python experiment` with shared behavior semantics without Python becoming architectural.

### Serializable Trees

With `serde` feature, `Behavior<A>` serializes. Trees could become ecosystem artifacts:

```
Behavior
├── definition + hash + version + author
├── required signals
├── constraints
└── provenance (sweetGrass-witnessed)
```

Squirrel transmits inspectable, signed execution topology rather than imperative "do X."

---

## PathwayLearner Integration

Behavior trees give the existing PathwayLearner explicit decision boundaries:

```
Select
├── LocalGPU      [32 ms, 4.1 J, success]
├── MeshGPU       [91 ms, unavailable]
└── CPU           [840 ms]
```

Learning changes policy preference without owning execution semantics. Probabilistic optimization inside deterministic constraints.

---

## Provenance Integration

SweetGrass records per-tick:

```
tree_hash, tree_version, tick, node
input_hash, action, action_result
model/version, seed, result_hash
timestamp, primal_identity
```

Nondeterminism (LLM calls) becomes an explicit leaf node in a deterministic execution graph. Replayable control flow with recorded nondeterministic boundaries.

---

## Proposed Neural API Vocabulary Extension

```
behavior.validate    behavior.load
behavior.execute     behavior.tick
behavior.status      behavior.pause
behavior.resume      behavior.cancel
behavior.inspect     behavior.replay
```

Tree leaves call existing atomic signals — no new namespace collision.

---

## Coordination Triad Mapping

```
quorumSignal  = SENSE
Behavior      = DECIDE    ← missing explicit layer
capability    = ACT
rootPulse     = REMEMBER
waterFall     = PROPAGATE
PathwayLearner = ADAPT
```

Behavior is the missing decision layer between sensing and acting.

---

## Maturity Assessment

- 207 commits, ~790 stars, v0.13.0
- Active development: typed ports, richer blackboard, pre/postconditions in open issues (May-June 2026)
- Real usage: Utah Robotics Lunabotics 2026 rover autonomy stack
- What's NOT sophisticated yet: typed dataflow between nodes, advanced decorator semantics

**Decision**: Fork bonsai-bt into ecoPrimals as a new meta-primal (DECIDE layer). AGPL3 + scyBorg triple license. sourDough scaffold. Full primal subsystem with Neural API capabilities, provenance integration, and PathwayLearner wiring. See `BONSAI_INGESTION_PLAN.md` for full pipeline.

---

## Implementation Path

1. **Evaluate**: Add `bonsai-bt` as optional dep in biomeOS, prototype a single behavior tree executing existing Neural API signals
2. **Validate**: Can a serialized tree from one gate execute on another using capability resolution?
3. **Integrate**: Wire `behavior.*` methods into Neural API translation registry
4. **Evolve**: Let PathwayLearner observe behavior-tree decision boundaries
5. **Publish**: Document the capability graph + behavior graph duality as architectural contribution

---

---

## Codebase Assessment (Aug 2026)

| Metric | Value |
|--------|-------|
| Created | May 23, 2022 |
| Latest version | 0.13.0 |
| MSRV | 1.80.0 |
| Stars | 876 / Forks: 37 |
| Commits | 207 |
| Core LOC | 5,284 Rust |
| Test LOC | 2,087 (39% ratio) |
| Workspace total | 7,477 LOC |
| Default deps | **0** (zero runtime dependencies) |
| With `visualize` | 4 (petgraph, serde, serde_json, tungstenite) |
| Behavior node types | 16 |
| Public Rust exports | ~36 |
| Python exports | 26 |
| Rust tests | 106 |
| Python tests | 106 |
| `unsafe` usage | **0** |
| Contributors | 10 (primary: Kristoffer Rakstad Solberg ~85%, secondary: Anmol Kathail — Python/visualizer) |
| License | **MIT** |
| Coverage | ~70-75% (Codecov) |
| Clippy | `-D warnings` enforced in pre-commit |

### Project Timeline

```
2022 Q2   Created. v0.3.x–v0.4.x (graphviz, reset_bt)
2023 Q4   Blackboard generics (v0.6.0)
2024 Q4   Serde made optional (v0.8)
2025 Q1   Major API break: tick/blackboard (v0.9.0)
2026 Q1   Race primitive (v0.11.0)
2026 Q2   Live visualizer (v0.12.0), Python bindings, reactive composites (v0.13.0)
```

### Production Users

- Utah Robotics Lunabotics 2026 rover autonomy (3rd of 50 NASA competition)
- Titanfall 2 / Northstar mod NPC AI (catornot/bp-ort)
- AnotherlandServer MMORPG NPC behaviors

### Up to ecoPrimals Standards?

**Strengths**: Zero-dep core, zero unsafe, clippy enforced, deterministic sync tick, MIT license, generic blackboard maps to Neural API state, reactive composites for distributed preemption.

**Gaps**: 0.x semver (expect breaking changes), serde coupled to `visualize` feature (no standalone serialization), no typed blackboard ports (open issue #61), small bus factor (1+1 maintainers), no CONTRIBUTING.md, release automation incomplete (v0.13 not tagged on GitHub).

### Decision: Fork → Full Primal Subsystem

**Fork and evolve** into an ecoPrimals meta-primal. The core is clean and small enough (5,284 LOC) to fully ingest and evolve. AGPL3 + scyBorg triple license. sourDough scaffold into standard primal workspace. Core BT improvements offered back upstream (MIT). Ecosystem-specific types (EcoAction, EcoBlackboard, provenance) stay in fork.

This is a one-human project recognizing another. Small enough to fully understand, clean enough to build on, production-proven enough to trust as foundation.

See `BONSAI_INGESTION_PLAN.md` for full pipeline: Phase 0 (ingest + review) → Phase 1 (sourDough scaffold) → Phase 2 (ecosystem evolution) → Phase 3 (Neural API capabilities) → Phase 4 (protocol compliance) → Phase 5 (meta-primal integration).

---

*Public contact. Source: Reddit/GitHub. No prior relationship with maintainer (Kristoffer Rakstad Solberg). Evaluated for architectural fit with Neural API and squirrel agent orchestration.*
