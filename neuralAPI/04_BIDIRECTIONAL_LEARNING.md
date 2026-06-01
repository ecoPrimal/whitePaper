# Bidirectional Learning — Forward Execution, Backward Feedback

**How the Neural API learns from every graph execution**

**Date**: May 14, 2026
**Status**: Architecture Specification
**Depends on**: MetricsCollector (Phase 2 COMPLETE), PathwayLearner (Phase 3 PARTIAL)

---

## Overview

Static orchestration executes the same way every time. Neural API
orchestration executes, observes, and adapts. The mechanism is
**bidirectional learning**: forward passes execute graphs over primals;
backward passes feed execution metrics into the PathwayLearner, which
modifies future graph execution.

```
Forward (execution):
  Signal → Graph → Nodes → Primal calls → Result

Backward (learning):
  Result → Metrics → PathwayLearner → Graph optimization → Signal
```

The two passes form a closed loop. Each execution makes the next one
better.

---

## Forward Pass: Graph Execution

The forward pass is documented in `03_GRAPH_EXECUTION.md`. The key
points relevant to learning:

1. **Every node produces timing data** — start time, end time, success/failure
2. **Every edge carries data** — the output of node N becomes the input of node N+1
3. **Every graph has a coordination pattern** — Sequential, Parallel, ConditionalDag, Pipeline, Continuous

The MetricsCollector (Phase 2, COMPLETE) already captures this data:

| Metric | Source | Storage |
|--------|--------|---------|
| Per-node latency | GraphExecutor / ContinuousExecutor | redb (persistent) + in-memory |
| Per-graph latency | GraphExecutor | redb |
| Co-occurrence | Edge traversals | In-memory HashMap |
| Success/failure rate | Node execution result | redb |
| Budget violations | ContinuousExecutor budget checks | In-memory counter |

---

## Backward Pass: Learning

The backward pass is the gap. The PathwayLearner struct exists in
`biomeos-graph/src/pathway_learner.rs` with detection algorithms
(Parallelize, Prewarm, Batch, Cache, Reorder) but is not wired
into the execution path.

### What the PathwayLearner needs to receive

After each graph execution, the PathwayLearner should receive:

```rust
struct ExecutionTrace {
    graph_id: String,
    coordination: CoordinationPattern,
    nodes: Vec<NodeTrace>,
    total_duration: Duration,
    success: bool,
    timestamp: Instant,
}

struct NodeTrace {
    node_id: String,
    capability: String,
    primal: String,
    duration: Duration,
    success: bool,
    depends_on: Vec<String>,
    output_size_bytes: usize,
}
```

### What the PathwayLearner does with it

1. **Accumulates traces** — stores the last N executions of each graph
2. **Detects patterns** — statistical analysis over accumulated traces
3. **Generates suggestions** — optimization proposals with confidence scores
4. **Tracks effectiveness** — measures whether applied optimizations actually helped

### Pattern Detection Algorithms

Five detection algorithms, ordered by complexity:

**Parallelize**: Find sequential nodes with no data dependency between them.
If nodes A and B are sequential but A's output is not B's input, they can
run in parallel. Confidence increases with number of observations.

**Prewarm**: Find primals that are always invoked within 100ms of graph start.
Pre-connect their sockets before the graph executes. Saves connection
establishment latency (~2-5ms per primal on UDS).

**Batch**: Find graphs that are frequently invoked in quick succession
(e.g., 10 `nest.store` calls within 1 second). Batch the inner primal
calls (e.g., one `spine.commit` with 10 entries instead of 10 commits).

**Cache**: Find nodes whose output is deterministic given the same input.
Cache results keyed by input hash. Most useful for `shader.compile`
(same WGSL → same SPIR-V every time).

**Reorder**: Find execution orders that consistently produce lower total
latency. If node A (5ms) and node B (50ms) are independent, running B
first lets A overlap with B's tail. Reordering within phases can reduce
wall-clock time.

---

## The Feedback Loop

### Transactional graphs (RootPulse, deploy graphs)

Signal frequency: human-paced (~100/day for active use)

```
Execution 1-10:    Baseline measurements
Execution 11-50:   Pattern detection (Parallelize, Prewarm)
Execution 51-100:  Suggestions generated (with confidence scores)
Execution 101+:    Optimizations applied if user/spring accepts
```

### Continuous graphs (game engine, dashboards)

Signal frequency: clock-paced (60 Hz = 5.184M frames/day)

```
Tick 1-100:        Baseline measurements (~1.7 seconds at 60 Hz)
Tick 101-1000:     Budget violation patterns detected
Tick 1001-10000:   Node reordering and parallelization discovered
Tick 10001+:       Steady-state optimization (re-evaluate periodically)
```

Continuous graphs provide 50,000x more learning signal per day than
transactional graphs. This is why the game engine is the richest
learning environment.

### Atomic signals (Tower/Node/Nest/NUCLEUS)

Signal graphs are small (3-5 nodes) and frequently invoked. They
converge quickly:

```
Signal 1-5:    Baseline (e.g., tower.publish = sign→announce→audit)
Signal 6-20:   Discover announce and audit can parallelize
Signal 21+:    Optimized graph: sign → (announce || audit)
```

---

## Feedback to Primals

The backward pass doesn't only optimize biomeOS. It can feed information
back to primals:

### Passive feedback (log scraping)

biomeOS already collects `tracing` logs from primals. Structured log
fields (`operation`, `latency_ms`, `success`) are metric sources that
require zero primal changes. All 13 primals already use `tracing`.

### Active feedback (metrics socket)

Primals that opt in can report via `BIOMEOS_METRICS_SOCKET`:

```json
{"primal":"beardog","operation":"crypto.sign","latency_ms":3.2,"success":true}
```

This gives biomeOS real-time per-operation metrics without log parsing.
No primal currently implements this — it is the Phase 4 deliverable.

### Reverse suggestions

biomeOS can expose `neural_api.suggest` to tell primals about their
own performance in composition:

```json
{"suggestion":"prewarm","primal":"beardog","reason":"always invoked within 50ms of tower.publish, pre-connect saves 3ms"}
```

Primals can ignore suggestions. The system is advisory, not prescriptive.

---

## Dark Forest Compliance in Learning

The learning loop must respect Dark Forest invariants:

1. **No metric leakage** — execution traces stay local to the tower.
   Federated learning (Phase 5) would share aggregate patterns, not
   raw traces.

2. **BTSP on metric transport** — if primals report via metrics socket,
   the socket uses BTSP AEAD. No cleartext metric data.

3. **Audit trail** — skunkBat logs optimization applications. If biomeOS
   reorders a graph, the reordering is an auditable event.

4. **No external dependencies** — the PathwayLearner uses local storage
   (redb) and in-memory statistics. No cloud, no phone-home.

---

## Implementation Status

| Component | Status | Gap |
|-----------|--------|-----|
| MetricsCollector (redb) | COMPLETE | — |
| MetricsCollector (in-memory) | COMPLETE | — |
| PathwayLearner struct | EXISTS | Not wired into execution |
| Detection algorithms | EXISTS | Parallelize, Prewarm, Batch, Cache, Reorder coded but untested |
| ExecutionTrace struct | NOT STARTED | Needs definition + plumbing |
| Metrics socket (BIOMEOS_METRICS_SOCKET) | NOT STARTED | Phase 4 |
| Reverse suggestions | NOT STARTED | Phase 4 |
| Dark Forest compliance for metrics | NOT STARTED | Phase 4 |

### Activation path

1. Define `ExecutionTrace` and `NodeTrace` structs in `biomeos-graph`
2. Hook GraphExecutor to emit traces after each execution
3. Hook ContinuousExecutor to emit traces per tick (sampled, not every tick)
4. Wire PathwayLearner to consume traces and update its internal state
5. Expose `neural_api.suggest_optimizations` JSON-RPC method
6. Add primalSpring scenario `s_neural_learning` to validate the loop structurally

---

*"The best optimization is the one the system discovers for itself."*
