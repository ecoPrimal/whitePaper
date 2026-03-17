# Neural API — Quick Reference

**Updated**: March 15, 2026

---

## What Is It?

**Neural API** is biomeOS's orchestration layer. It executes graphs of
capability calls over autonomous primals, learns from execution traces,
and evolves coordination strategies. Complex systems emerge as graphs:

- **RootPulse** (version control) = Sequential graph over provenance trio
- **RPGPT** (sovereign RPG engine) = Continuous 60 Hz graph over ludoSpring + provenance + Squirrel
- **AlphaFold-class** (protein folding) = Pipeline graph over neuralSpring + hotSpring + wetSpring

biomeOS doesn't know what these systems are. It only knows graphs.

---

## Three Layers

```
Layer 3: Emergent Systems (RootPulse, RPGPT, AlphaFold, Surgical VR)
         | (graphs)
Layer 2: biomeOS (graph execution + capability routing + learning)
         | (JSON-RPC 2.0)
Layer 1: Primals & Springs (capabilities via niche.rs self-knowledge)
```

---

## Five Coordination Patterns

| Pattern | Use Case | Status |
|---------|----------|--------|
| **Sequential** | RootPulse commit (A -> B -> C) | Implemented |
| **Parallel** | Independent capability calls | Implemented |
| **ConditionalDag** | RPGPT (if AI available, use Squirrel) | Parsed, not executed |
| **Pipeline** | Streaming (telemetry, pharmacology) | Parsed, not executed |
| **Continuous** | Game engine at 60 Hz | Implemented (CLI only) |

---

## Implementation Status (March 15, 2026)

| Phase | Status |
|-------|--------|
| Graph execution (Sequential, Parallel, Continuous) | Implemented |
| Capability routing (124 translations, 12 domains) | Implemented |
| RootPulse transactional flow | Validated end-to-end |
| Game engine continuous flow | Implemented (ContinuousExecutor) |
| MetricsCollector | Implemented (redb + in-memory) |
| PathwayLearner | Code exists, not wired |
| ConditionalDag execution | Not implemented |
| Continuous via Neural API JSON-RPC | Not implemented (CLI only) |
| Bidirectional feedback | Not started |
| Pattern discovery | Research phase |

---

## For Each Role

### biomeOS developers
Build: unified graph schema, continuous via JSON-RPC, ConditionalDag, PathwayLearner wiring

### Primal/Spring teams
Provide: `niche.rs` self-knowledge, `health.check`, `capability.list`, structured `tracing` logging
5/7 springs already have `niche.rs` (airSpring, groundSpring, wetSpring, neuralSpring, ludoSpring)

### Niche/Emergent System developers
Use: TOML graph definitions, capability-based node resolution, `fallback = "skip"` for optional deps
Study: `rootpulse_commit.toml` (transactional), `game_engine_tick.toml` (continuous)

---

## Read More

- **[README.md](./README.md)** — Full index and status
- **[03_GRAPH_EXECUTION.md](./03_GRAPH_EXECUTION.md)** — Graph patterns
- **[08_NICHE_API_PATTERNS.md](./08_NICHE_API_PATTERNS.md)** — Continuous niches
- **[09_ROOTPULSE_CASE_STUDY.md](./09_ROOTPULSE_CASE_STUDY.md)** — Working example
- **[10_ROADMAP.md](./10_ROADMAP.md)** — Implementation plan
