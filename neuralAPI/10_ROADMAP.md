# Neural API Implementation Roadmap

**Updated**: March 15, 2026
**Original**: January 4, 2026

---

## Overview

This roadmap tracks the path from static orchestration to adaptive
orchestration. Phases 1-2 are largely complete. Phase 3 has code but
lacks integration. Phases 4-5 remain planned.

---

## Phase Status

```
Phase 1: Graph Execution        COMPLETE   (biomeos-graph, biomeos-atomic-deploy)
Phase 2: Metrics Collection     COMPLETE   (MetricsCollector, redb-backed)
Phase 3: Pathway Learning       PARTIAL    (PathwayLearner exists, not wired)
Phase 4: Bidirectional Feedback PLANNED    (spec only)
Phase 5: Self-Evolution         RESEARCH   (not started)
```

---

## Phase 1: Graph Execution — COMPLETE

**Delivered** (biomeOS v2.39-v2.41):

- `DeploymentGraph` and `GraphNode` TOML parsing (`biomeos-graph`)
- Sequential, Parallel coordination via Kahn's topological sort
- `ContinuousExecutor` with TickClock, feedback edges, session lifecycle
- `GraphExecutor` for transactional graphs (`biomeos-atomic-deploy`)
- Capability routing via `NeuralRouter` with tarpc escalation
- RootPulse graphs: commit, branch, merge, diff, federate
- Game engine graph: `game_engine_tick.toml` (60 Hz, feedback edges)
- 55 deploy/workflow graphs in `biomeOS/graphs/`

**Remaining (v2.42)**:

- [ ] Unify `[[nodes]]` and `[[graph.nodes]]` schema
- [ ] Expose continuous execution via Neural API JSON-RPC methods
- [ ] Implement ConditionalDag branching (currently executes as Sequential)
- [ ] Implement Pipeline streaming (currently executes as Sequential)
- [ ] Support mixed coordination (continuous ticks + transactional subgraphs)
- [ ] Tick-level `fallback = "skip"` for optional primal nodes

---

## Phase 2: Metrics Collection — COMPLETE

**Delivered**:

- `MetricsCollector` in `biomeos-graph` (redb-backed, per-graph and per-node)
- `MetricsCollector` in `biomeos-core` (in-memory pathway-learning metrics)
- `NeuralRouter` tracks `log_metric` and `get_metrics` per capability call
- `GraphEventBroadcaster` for session state changes

**Remaining (v2.42)**:

- [ ] Wire graph execution metrics into PathwayLearner's store
- [ ] Persist NeuralRouter metrics (currently in-memory, lost on restart)

---

## Phase 3: Pathway Learning — PARTIAL

**Delivered**:

- `PathwayLearner` struct in `biomeos-graph/src/pathway_learner.rs`
- Detection algorithms: Parallelize, Prewarm, Batch, Cache, Reorder
- Optimization suggestion API

**Remaining (v2.42)**:

- [ ] Hook PathwayLearner into GraphExecutor (record per-execution metrics)
- [ ] Hook PathwayLearner into ContinuousExecutor (record per-tick metrics)
- [ ] Surface suggestions via `neural_api.suggest_optimizations` JSON-RPC
- [ ] Apply optimizations to live graphs (reorder nodes, parallelize independent calls)
- [ ] Track optimization effectiveness over time

---

## Phase 4: Bidirectional Feedback — PLANNED

**Goal**: Enable learning from niche APIs back to primals and biomeOS.

### Deliverables

1. **Primal Metrics API** — Standard format for primals to report operation metrics
   to biomeOS. Springs already emit structured `tracing` logs; this adds a
   formal metrics socket (`BIOMEOS_METRICS_SOCKET`).

2. **Niche API Framework** — `NicheAPI` trait for emergent systems. RootPulse,
   RPGPT, and cross-spring pipelines implement this trait. biomeOS learns
   domain-specific patterns (e.g., "dehydration is always sequential",
   "NestGate and sweetGrass can parallelize").

3. **Feedback Loop** — Primals report metrics -> biomeOS aggregates and learns
   -> graph execution adapts -> users see improvements.

### Prerequisites

- Phase 3 PathwayLearner fully wired
- At least 3 springs enhanced with formal metrics reporting
- RootPulse or game engine niche running end-to-end

---

## Phase 5: Self-Evolution — RESEARCH

**Goal**: Discover novel coordination patterns automatically.

### Research Questions

1. Can biomeOS discover novel patterns from execution traces?
2. Can learning be shared across towers via Songbird federation?
3. How to balance exploration vs exploitation in graph scheduling?

### Approach

- Pattern clustering from execution traces
- Genetic algorithm optimization of graph topology
- Multi-tower federated learning via Songbird

---

## Validation Targets

### Transactional (RootPulse)

The provenance trio commit flow is validated end-to-end (March 13, 2026).
37/37 cross-spring checks via ludoSpring exp052. biomeOS E2E tests cover
graph parsing, health checks, capability registration, full commit flow,
and `graph.execute(rootpulse_commit)`.

### Continuous (Game Engine)

`game_engine_tick.toml` runs via `biomeos continuous` CLI with 60 Hz
TickClock, feedback edges, and per-node budget enforcement. Next step:
expose via Neural API JSON-RPC for programmatic session management.

### Cross-Spring (Ecology Pipeline)

`cross_spring_ecology.toml` chains airSpring ET0 -> wetSpring diversity ->
neuralSpring spectral analysis. Sequential coordination with capability
routing. Validated in spring-local experiments.

### Emergent (RPGPT)

ludoSpring V18 is building a sovereign RPG engine that composes 7+
primals via biomeOS graphs. This is the hardest composition test:
continuous ticks (60 Hz), transactional provenance (session boundaries),
conditional AI narration (Squirrel availability), and real-time
visualization (petalTongue). The RPGPT project will validate or expose
every remaining gap in the Neural API.

---

## Spring Niche Readiness (March 15, 2026)

| Spring | Version | niche.rs | Deploy Graph | Capability Registry |
|--------|---------|:--------:|:------------:|:-------------------:|
| hotSpring | v0.6.31 | No | Yes | Partial (no physics domain) |
| groundSpring | V105 | Yes | Yes | Missing (no measurement domain) |
| neuralSpring | S154 | Yes | Yes | Yes (22 capabilities) |
| wetSpring | V119 | Yes | Yes | Yes (15 domains, 20 methods) |
| airSpring | v0.8.2 | Yes | Yes | Yes (41 capabilities) |
| healthSpring | V25 | No | Yes | Partial (missing Track 6+7) |
| ludoSpring | V18 | Yes | Yes | Yes (8 game methods) |

All 7 springs have deploy graphs. 5/7 have `niche.rs` self-knowledge.
The capability registry needs `measurement.*` (groundSpring) and
`physics.*` (hotSpring) domains added.

---

## Timeline (Revised)

### Completed (Q1 2026)

- Phase 1: Graph execution (Sequential, Parallel, Continuous)
- Phase 2: Metrics collection (redb-backed, in-memory)
- RootPulse end-to-end validation
- 7 spring deploy graphs
- 124 capability translations across 12 domains

### In Progress (March-April 2026)

- Phase 1 completion: unified schema, continuous via API, ConditionalDag
- Phase 3 wiring: PathwayLearner into execution path
- Capability registry gaps: measurement, physics, healthSpring Track 6+7
- ludoSpring RPGPT composition validation

### Planned (Q2 2026)

- Phase 4: Bidirectional feedback
- Phase 5: Self-evolution research
- Multi-tower federation testing
- Additional emergent systems (AlphaFold-class, surgical VR)
