# Neural API Implementation Roadmap

**Updated**: June 1, 2026
**Original**: January 4, 2026
**Vocabulary**: `gen5/foundations/FUNCTIONAL_PATTERN_CONVERGENCE.md`

---

## Overview

This roadmap tracks the path from static orchestration to adaptive
orchestration with atomic composition dispatch. Phases 1-2 are complete.
Phase 3 has code but lacks integration. Phase 3.5A (composition definition)
is complete — 32 composition graphs defined and validated. Phases 3.5B-D
and Phases 4-5 remain.

---

## Phase Status

```
Phase 1:   Graph Execution            COMPLETE   (biomeos-graph, biomeos-atomic-deploy)
Phase 2:   Metrics Collection         COMPLETE   (MetricsCollector, redb-backed)
Phase 3:   Pathway Learning           PARTIAL    (PathwayLearner exists, not wired)
Phase 3.5A: Composition Definition    COMPLETE   (32 graphs, s_atomic_signals, signal_tools.toml)
Phase 3.5B: Composition Dispatch      DESIGNED   (NeuralRouter tier recognition)
Phase 3.5C: Composition Adoption      DESIGNED   (spring migration path)
Phase 3.5D: Composition Learning      DESIGNED   (PathwayLearner + composition traces)
Phase 4:   Bidirectional Feedback     SPECIFIED  (04_BIDIRECTIONAL_LEARNING.md)
Phase 5:   Self-Evolution             RESEARCH   (05_PATHWAY_OPTIMIZATION.md)
```

---

## Phase 1: Graph Execution — COMPLETE

**Delivered** (biomeOS v2.39–v3.50):

- `DeploymentGraph` and `GraphNode` TOML parsing (`biomeos-graph`)
- Sequential, Parallel coordination via Kahn's topological sort
- `ContinuousExecutor` with TickClock, feedback edges, session lifecycle
- `GraphExecutor` for transactional graphs (`biomeos-atomic-deploy`)
- Capability routing via `NeuralRouter` with tarpc escalation (320+ translations, 27 domains)
- RootPulse graphs: commit, branch, merge, diff, federate
- Game engine graph: `game_engine_tick.toml` (60 Hz, feedback edges)
- 55+ deploy/workflow graphs in biomeOS
- Token forwarding: `_bearer_token` propagation through all capability paths (v3.50)
- MethodGate: JH-0/JH-2 resource envelope + `auth.check` compatibility

**Remaining (Phase 1 completion)**:

- [ ] Unify `[[nodes]]` and `[[graph.nodes]]` schema
- [ ] Expose continuous execution via Neural API JSON-RPC methods (`graph.start_continuous`, etc.)
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

**Remaining**:

- [ ] Wire graph execution metrics into PathwayLearner's store
- [ ] Persist NeuralRouter metrics (currently in-memory, lost on restart)

---

## Phase 3: Pathway Learning — PARTIAL

**Delivered**:

- `PathwayLearner` struct in `biomeos-graph/src/pathway_learner.rs`
- Detection algorithms: Parallelize, Prewarm, Batch, Cache, Reorder
- Optimization suggestion API

**Remaining**:

- [ ] Hook PathwayLearner into GraphExecutor (record per-execution metrics)
- [ ] Hook PathwayLearner into ContinuousExecutor (record per-tick metrics)
- [ ] Surface suggestions via `neural_api.suggest_optimizations` JSON-RPC
- [ ] Apply optimizations to live graphs (reorder nodes, parallelize independent calls)
- [ ] Track optimization effectiveness over time

---

## Phase 3.5: Atomic Composition Layer

**Composition collapse architecture** from `02_ARCHITECTURE.md`. Phase A
is complete. Phases B-D remain.

### Phase A: Composition Definition (primalSpring) — COMPLETE

All deliverables shipped:

- [x] Tower composition graphs: `tower_publish.toml`, `tower_authenticate.toml`,
  `tower_discover.toml`, `tower_health.toml`, `tower_bootstrap.toml`
- [x] Node composition graphs: `node_compute.toml`
- [x] Nest composition graphs: `nest_store.toml`, `nest_commit.toml`,
  `nest_retrieve.toml`, `nest_ingest_spore.toml`
- [x] Meta composition graphs: `meta_observe.toml`, `meta_intent.toml`,
  `meta_render.toml`, `meta_health.toml`, `meta_deploy.toml`
- [x] Ecosystem composition graphs: `ecosystem_pull.toml`, `ecosystem_push.toml`,
  `ecosystem_check.toml`
- [x] RootPulse compositions: `rootpulse_commit.toml`, `rootpulse_branch.toml`,
  `rootpulse_merge.toml`, `rootpulse_diff.toml`, `rootpulse_federate.toml`
- [x] Impulse/potential compositions: `impulse_post.toml`, `impulse_post_signed.toml`,
  `impulse_ack.toml`, `potential_sense.toml`, `potential_check.toml`
- [x] Context compositions: `context_weave_anchored.toml`
- [x] Agentic sync compositions: `sync_diverge.toml`, `sync_resolve.toml`,
  `sync_resolve_crossgate.toml`
- [x] `[signals]` section in `capability_registry.toml` — all tiers registered
- [x] `s_atomic_signals` validation scenario — validates all 32 graphs
- [x] `s_meta_tier_signals` validation scenario — validates tool schemas and routing
- [x] `config/signal_tools.toml` — tool-use schema for squirrel agentic planning
- [x] `CompositionContext::signal()` method — dispatches to orchestration
- [x] `signal_plan()` + `execute_plan()` — agentic dispatch methods

**Totals**: 32 composition graphs across 6 tiers (Tower/Node/Nest/NUCLEUS/meta/ecosystem).

### Phase B: Composition Dispatch (biomeOS)

- [ ] Extend NeuralRouter to recognize composition-tier capabilities (`tower`, `node`, `nest`, `nucleus`, `meta`)
- [ ] On composition dispatch, load and execute the corresponding graph
- [ ] Compose graph results into a single response
- [ ] Wire `signal_tools.toml` into squirrel's `mcp.tools.list` response

### Phase C: Composition Adoption (springs)

- [ ] Springs migrate gradually: `call("security", "crypto.sign", ...)` still works
- [ ] New code prefers `signal("tower", "publish", ...)` for compound operations
- [ ] Agentic flows use `signal_plan()` + `execute_plan()` for multi-composition orchestration
- [ ] petalTongue captures intent as structured actions, not raw API calls

### Phase D: Composition Learning (biomeOS)

- [ ] PathwayLearner observes composition execution traces
- [ ] Discovers parallelization within composition graphs
- [ ] Suggests and applies optimizations automatically

### Prerequisites

- Phase 1 completion (unified graph schema) — compositions are graphs
- Phase 3 wiring (PathwayLearner) — compositions need learning to optimize

### Success criteria

- `tower.publish` composition executes correctly: sign → announce → audit
- `nest.store` composition executes correctly: 5-node provenance flow
- Collapse ratio measured: >= 3x for common operations
- primalSpring `s_atomic_signals` scenario passes — **DONE**

---

## Phase 4: Bidirectional Feedback — SPECIFIED

**Goal**: Enable learning from niche APIs back to primals and biomeOS.

See `04_BIDIRECTIONAL_LEARNING.md` for full specification.

### Deliverables

1. **ExecutionTrace struct** — define and plumb through GraphExecutor
2. **Metrics socket** — `BIOMEOS_METRICS_SOCKET` for active primal reporting
3. **Reverse suggestions** — `neural_api.suggest` to tell primals about composition performance
4. **NicheAPI trait** — formal interface for emergent systems to declare their coordination needs
5. **Dark Forest compliance** — BTSP on metric transport, skunkBat audit of optimizations

### Prerequisites

- Phase 3 PathwayLearner fully wired
- Phase 3.5 signal graphs providing learning signal
- At least 3 springs enhanced with formal metrics reporting
- RootPulse or game engine niche running end-to-end

---

## Phase 5: Self-Evolution — RESEARCH

**Goal**: Discover novel coordination patterns automatically.

See `05_PATHWAY_OPTIMIZATION.md` for full specification.

### Research Questions

1. Can biomeOS discover novel patterns from execution traces?
2. Can learning be shared across towers via Songbird federation?
3. How to balance exploration vs exploitation in graph scheduling?
4. Can evolutionary search over graph topologies find better signal decompositions?

### Prerequisites

- Phase 4 fully operational
- Continuous niche (game engine) running at scale for rich learning signal
- Multiple towers in federation (Songbird mesh)

---

## Validation Targets

### Transactional (RootPulse)

The provenance trio commit flow is validated end-to-end. 37/37 cross-spring
checks via ludoSpring exp052. biomeOS E2E tests cover graph parsing,
health checks, capability registration, full commit flow, and
`graph.execute(rootpulse_commit)`. The atomic signal `nest.commit`
would wrap this flow.

### Continuous (Game Engine)

`game_engine_tick.toml` runs via `biomeos continuous` CLI with 60 Hz
TickClock, feedback edges, and per-node budget enforcement. Next step:
expose via Neural API JSON-RPC for programmatic session management.

### Cross-Spring (Ecology Pipeline)

`cross_spring_ecology.toml` chains airSpring ET0 → wetSpring diversity →
neuralSpring spectral analysis. Sequential coordination with capability
routing. Validated in spring-local experiments.

### Scientific Reproduction (Barrick)

Barrick Lab tools (breseq, pLannotate, OSTIR, EFM Calculator, CryptKeeper)
map to `node.compute` + `nest.commit` signal composition. Python/R
pipelines are Tier 1 baselines; Rust lithoSpore modules reproduce them
as Tier 2, validated via the provenance trio.

### Emergent (RPGPT)

ludoSpring builds a sovereign RPG engine composing 7+ primals via
biomeOS graphs. Hardest composition test: continuous ticks (60 Hz),
transactional provenance (session boundaries), conditional AI narration
(Squirrel availability), real-time visualization (petalTongue).

---

## Spring Niche Readiness (May 14, 2026)

| Spring | Version | Tests | Deploy Graphs | Dark Forest | Atomic Tier |
|--------|---------|------:|:-------------:|:-----------:|:-----------:|
| hotSpring | V168+ | 1,042 | 5 | PENDING | Node |
| neuralSpring | V160 | 1,453 | 4 | PENDING | Node |
| wetSpring | V168 | 1,962 | 7 | PENDING | Nest |
| airSpring | v0.10.0 | 1,389 | 7 | PENDING | Node |
| groundSpring | V142 | 1,123 | 6 | PENDING | Node |
| healthSpring | V64n | 1,018 | 7 | PENDING | NUCLEUS |
| ludoSpring | V71 | 862 | 12 | PENDING | NUCLEUS |
| primalSpring | v0.9.25 | 651+ | 78 | DONE | Coordination |

All 8 springs have deploy graphs. 8/8 Tier 4 IPC-first. 10/10 foundation
threads active. Dark Forest adoption pending for 7 springs.

---

## Timeline (Revised June 1, 2026)

### Completed (Q1 2026)

- Phase 1: Graph execution (Sequential, Parallel, Continuous)
- Phase 2: Metrics collection (redb-backed, in-memory)
- RootPulse end-to-end validation
- 8 spring deploy graphs + 55 biomeOS graphs
- 320+ capability translations across 27 domains

### Completed (Q2 2026)

- Phase 3.5A: 32 composition graphs defined across 6 tiers
- `s_atomic_signals` + `s_meta_tier_signals` validation scenarios
- `signal_tools.toml` tool-use schema for squirrel
- `CompositionContext::signal()`, `signal_plan()`, `execute_plan()`
- Agentic sync compositions: `sync_diverge`, `sync_resolve`, `sync_resolve_crossgate`
- Dark Forest Glacial Gate: formalized, primalSpring validated, 7 springs pending

### In Progress (June 2026)

- Phase 1 completion: unified schema, continuous via API, ConditionalDag
- Phase 3 wiring: PathwayLearner into execution path
- Phase 3.5B design: NeuralRouter composition-tier recognition

### Next (Q2-Q3 2026)

- Phase 3.5B implementation: NeuralRouter composition dispatch
- Phase 3 completion: PathwayLearner wired, suggestions surfaced
- Phase 4: Bidirectional feedback, metrics socket, NicheAPI trait
- Barrick pipeline activation via composition dispatch

### Planned (Q3-Q4 2026)

- Phase 5: Self-evolution research
- Multi-tower federation testing (Songbird mesh)
- Full stadial deployment with composition dispatch
- Additional emergent systems (AlphaFold-class, surgical VR)

---

*"The atom is not 13 primals. It is one composition, decomposed."*
