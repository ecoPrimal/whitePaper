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

**Recommendation**: Investigate making behavior-tree semantics a first-class biomeOS Neural API primitive. Initially embed `bonsai-bt`, let experience determine whether the ecosystem needs its own generalized representation. Do not make ecoPrimals structurally dependent on the exact API yet.

---

## Implementation Path

1. **Evaluate**: Add `bonsai-bt` as optional dep in biomeOS, prototype a single behavior tree executing existing Neural API signals
2. **Validate**: Can a serialized tree from one gate execute on another using capability resolution?
3. **Integrate**: Wire `behavior.*` methods into Neural API translation registry
4. **Evolve**: Let PathwayLearner observe behavior-tree decision boundaries
5. **Publish**: Document the capability graph + behavior graph duality as architectural contribution

---

*Public contact. Source: Reddit/GitHub. No prior relationship with maintainer (Kristoffer Sollimann). Evaluated for architectural fit with Neural API and squirrel agent orchestration.*
