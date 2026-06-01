# Pathway Optimization — Pattern Discovery and Signal Collapse Metrics

**How Neural API discovers novel coordination patterns and measures composition efficiency**

**Date**: May 14, 2026
**Status**: Architecture Specification (Research + Design)
**Depends on**: PathwayLearner (Phase 3), Bidirectional Learning (Phase 4)

---

## Overview

Pathway optimization sits above bidirectional learning. Where learning
observes individual executions, optimization discovers **patterns across
executions** and **measures the effectiveness of composition collapse**.

Three concerns:

1. **Pattern discovery** — find recurring coordination shapes in execution traces
2. **Signal collapse metrics** — measure how effectively atomic signals reduce surface complexity
3. **Cross-graph optimization** — find common subgraphs across different signal and emergent system graphs

---

## Pattern Discovery

### What patterns look like

A pattern is a recurring subgraph shape with consistent timing characteristics.

**Example: "sign-then-announce" pattern**

Across hundreds of executions of different graphs (`tower.publish`,
`rootpulse_commit`, `nest.store`), the PathwayLearner observes:

```
beardog.crypto.sign (3ms avg) → songbird.beacon.announce (2ms avg)
```

This pair always appears together, always in this order, with consistent
latency. It is a **pattern**: "signed announcement."

### Discovery algorithms

**Frequent Subgraph Mining**: Given N execution traces, find subgraphs
that appear in at least K traces. Standard algorithms (gSpan, FSG) work
on small graphs (3-10 nodes). Signal graphs are small enough for exact
enumeration.

**Temporal Clustering**: Group executions by timing profile. If 80% of
`nest.store` executions show `braid.create` at <1ms (because sweetGrass
is local and fast) but 20% show it at >50ms (because sweetGrass is
remote or busy), these are two distinct operational modes. The optimizer
can specialize graphs for each mode.

**Co-occurrence Analysis**: Track which capabilities are always invoked
together. If `crypto.sign` and `audit.log_event` have co-occurrence
0.95+ across all graphs, they are candidates for a fused operation or
pre-connected socket pair.

### What patterns enable

Once discovered, patterns enable:

1. **Pre-connection** — if A always follows B, pre-connect A's socket while B runs
2. **Batching** — if the same subgraph runs N times in quick succession, batch it
3. **Specialization** — generate optimized code paths for common patterns
4. **Prediction** — if a spring calls `tower.authenticate`, predict that `nest.store` follows 60% of the time and pre-warm the Nest tier

---

## Signal Collapse Metrics

### The composition surface

Define the **composition surface** as the number of distinct IPC calls
a spring makes per unit of work. Before atomic signals:

```
Surface(spring) = Σ (primal calls per operation × operations per unit of work)
```

For a spring performing a "store with provenance" operation today:

```
1. ctx.call("security", "crypto.sign", ...)         → bearDog
2. ctx.call("storage", "content.put", ...)           → nestGate
3. ctx.call("dag", "dag.event.append", ...)          → rhizoCrypt
4. ctx.call("ledger", "spine.commit", ...)           → loamSpine
5. ctx.call("commit", "braid.create", ...)           → sweetGrass
6. ctx.call("defense", "audit.log_event", ...)       → skunkBat

Surface = 6 calls to 6 primals
```

With `nest.store` signal:

```
1. neural_api.signal("nest", "store", payload)       → biomeOS → 6 primals

Surface = 1 call to 1 endpoint
```

### Collapse ratio

```
Collapse_Ratio = Surface_before / Surface_after
```

For `nest.store`: 6/1 = 6x collapse.

**Ecosystem-wide target**: measure the average collapse ratio across
all springs and all operations. Goal: ≥ 3x for common operations.

### Metrics to track

| Metric | Definition | Target |
|--------|-----------|--------|
| **Signal coverage** | % of spring operations expressible as atomic signals | ≥ 60% |
| **Collapse ratio** | Average surface reduction per signal | ≥ 3x |
| **Signal latency overhead** | Extra time from signal dispatch vs direct calls | < 5ms per signal |
| **Learning convergence** | Executions needed before PathwayLearner suggests first optimization | < 50 executions |
| **Optimization effectiveness** | Measured speedup of applied optimizations | ≥ 15% when suggested |

### Per-spring measurement

Each spring can report its composition surface:

| Spring | Operations/session | Surface (direct) | Surface (signals) | Collapse |
|--------|------------------:|------------------:|-------------------:|---------:|
| hotSpring | ~20 | ~60 calls | ~15 signals | 4x |
| wetSpring | ~15 | ~45 calls | ~12 signals | 3.75x |
| healthSpring | ~25 | ~75 calls | ~18 signals | 4.2x |
| ludoSpring | ~60/sec (continuous) | ~180 calls/sec | ~30 signals/sec | 6x |
| groundSpring | ~10 | ~30 calls | ~10 signals | 3x |

(Projected values — actual measurement requires signal activation.)

---

## Cross-Graph Optimization

### Common subgraph extraction

Multiple emergent systems share subgraphs:

```
RootPulse commit:   health → dehydrate → SIGN → store → commit → attribute
Deploy pipeline:    validate → build → SIGN → harvest → compose → verify
Barrick validation: fetch → compute → SIGN → store → verify → visualize
```

`SIGN` (bearDog crypto.sign with BTSP token) appears in all three. The
optimizer can:

1. **Identify** the common subgraph (`crypto.sign` with `_bearer_token` propagation)
2. **Cache** the BTSP connection state across graphs in the same session
3. **Pre-warm** bearDog's socket whenever any of these graphs is likely to run

### Emergent system interaction patterns

The four `EmergentSystem` variants in primalSpring (`RootPulse`, `Rpgpt`,
`CoralForge`, `CrossSpringEcology`) each have required graphs. Cross-graph
analysis can discover:

- **RootPulse + RPGPT**: game session commit uses rootpulse_commit at session
  boundaries. Pre-warm the provenance trio when a game session starts.
- **CoralForge + CrossSpringEcology**: both use the Node tier for compute.
  Schedule them to avoid GPU contention (sequential, not parallel).
- **RootPulse + Barrick**: lithoSpore validation produces provenance artifacts
  that flow through RootPulse commit. Fuse the store→commit→attribute subgraph.

---

## Optimization Application

### Safety model

Optimizations are **suggestions**, not mandates:

1. PathwayLearner generates a suggestion with a confidence score
2. If confidence > threshold (default 0.8), the optimization is auto-applied
3. If confidence < threshold, the optimization is logged for human review
4. Applied optimizations are tracked: if performance degrades, they are reverted

### Rollback

Every optimization stores:
- The original graph (before optimization)
- The optimized graph (after optimization)
- The timestamp and confidence score
- Performance measurements before and after

If the optimized graph performs worse over the next N executions
(measured by latency regression > 10%), the optimization is automatically
rolled back and marked as ineffective.

### Audit

Per Dark Forest standards, every optimization application is:
1. Logged by skunkBat as an audit event
2. Recorded in the MetricsCollector with before/after data
3. Reversible — no destructive optimization

---

## Research Phase: Self-Evolution (Phase 5)

Beyond optimization of known graphs, Phase 5 explores:

### Novel pattern discovery

Can biomeOS discover coordination patterns that no human designed?

Example: after observing 1M game engine ticks, the PathwayLearner
notices that audio processing can start 2ms before the render node
completes, because the audio output for tick N depends on game state
from tick N-1 (available via feedback edge), not tick N. A human would
need to analyze the dependency graph carefully to spot this. The
PathwayLearner discovers it statistically.

### Federated learning

Can optimization knowledge transfer between towers?

If Tower A discovers that `nest.store` benefits from parallelizing
sweetGrass + nestGate, can it share this discovery with Tower B
without leaking execution traces? Possible approach: share the
**graph topology** optimization (which nodes can parallelize) without
sharing the **data** (what was stored).

Federated learning depends on Songbird mesh and BTSP mutual authentication.
It is stadial-phase work.

### Evolutionary search

Can biomeOS explore novel graph topologies via mutation?

Given a seed graph (e.g., `tower_publish.toml`), generate N mutant
graphs (reorder nodes, add/remove edges, change coordination pattern),
execute all N, and select the best performer. This is a genetic algorithm
applied to coordination patterns.

Constraint: mutations must preserve data dependencies. You can't run
`spine.commit` before `dag.dehydrate` — the commit needs the merkle root.
The dependency graph constrains the search space.

---

## Relationship to Atomic Signals

Pathway optimization is what makes atomic signals better over time.

| Layer | What | Who |
|-------|------|-----|
| Atomic signal definition | Static graph per signal | Human (primalSpring) |
| Signal execution | Run the graph | biomeOS GraphExecutor |
| Signal learning | Observe execution metrics | PathwayLearner |
| Signal optimization | Modify graph for better performance | PathwayLearner + human review |
| Signal evolution | Discover novel signal topologies | Phase 5 research |

The human defines the initial signal. The system improves it.

---

*"The river finds its own path. We just define the mountain."*
