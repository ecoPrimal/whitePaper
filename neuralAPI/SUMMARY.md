# Neural API — Quick Reference

**Updated**: May 14, 2026

---

## What Is It?

**Neural API** is biomeOS's orchestration layer. It executes graphs of
capability calls over autonomous primals, learns from execution traces,
and evolves coordination strategies. Complex systems emerge as graphs:

- **RootPulse** (version control) = Sequential graph over provenance trio
- **RPGPT** (sovereign RPG engine) = Continuous 60 Hz graph over ludoSpring + provenance + Squirrel
- **AlphaFold-class** (protein folding) = Pipeline graph over neuralSpring + hotSpring + wetSpring
- **Barrick pipelines** = `node.compute` + `nest.commit` signal composition

biomeOS doesn't know what these systems are. It only knows graphs.

---

## Three Layers + Atomic Signals

```
Layer 3: Emergent Systems (RootPulse, RPGPT, AlphaFold, Barrick validation)
         | (atomic signals: tower.publish, nest.store, node.compute)
Layer 2: biomeOS (graph execution + capability routing + learning)
         | (JSON-RPC 2.0, BTSP AEAD, 320+ translations)
Layer 1: 13 Primals & 8 Springs (427 methods, Dark Forest compliant)
```

## Four Atomic Tiers (Phase 32)

| Tier | Primals | Role |
|------|---------|------|
| **Tower** | bearDog + songbird + skunkBat | Trust boundary |
| **Node** | Tower + toadStool + barraCuda + coralReef | Compute substrate |
| **Nest** | Tower + nestGate + rhizoCrypt + loamSpine + sweetGrass | Storage + provenance |
| **NUCLEUS** | Node + Nest (10 unique + 3 meta) | Full composition |

Springs send atomic signals (e.g., `tower.publish`). biomeOS decomposes
them into primal-level capability calls via small TOML graphs.

---

## Five Coordination Patterns

| Pattern | Use Case | Status |
|---------|----------|--------|
| **Sequential** | RootPulse commit (A → B → C) | Implemented |
| **Parallel** | Independent capability calls | Implemented |
| **ConditionalDag** | RPGPT (if AI available, use Squirrel) | Parsed, not executed |
| **Pipeline** | Streaming (telemetry, pharmacology) | Parsed, not executed |
| **Continuous** | Game engine at 60 Hz | Implemented (CLI only) |

---

## Implementation Status (May 14, 2026)

| Phase | Status |
|-------|--------|
| Graph execution (Sequential, Parallel, Continuous) | **COMPLETE** |
| Capability routing (320+ translations, 27 domains) | **COMPLETE** |
| MetricsCollector (redb + in-memory) | **COMPLETE** |
| Token forwarding (`_bearer_token` propagation) | **COMPLETE** (v3.50) |
| MethodGate / BTSP (13/13 authenticated) | **COMPLETE** |
| NeuralBridge (primalSpring client) | **COMPLETE** |
| Dark Forest Glacial Gate | **STRUCTURAL** (primalSpring validated) |
| RootPulse transactional flow | Validated end-to-end |
| Game engine continuous flow | Implemented (ContinuousExecutor) |
| PathwayLearner | Code exists, **not wired** |
| Atomic signal vocabulary | **DESIGNED** (02_ARCHITECTURE.md) |
| Atomic signal dispatch | Not implemented |
| ConditionalDag execution | Not implemented |
| Continuous via JSON-RPC | Not implemented (CLI only) |
| Bidirectional feedback | Specified (04_BIDIRECTIONAL_LEARNING.md) |
| Pattern discovery | Specified (05_PATHWAY_OPTIMIZATION.md) |

---

## For Each Role

### biomeOS developers
Build: unified graph schema, signal dispatch in NeuralRouter, continuous via JSON-RPC, ConditionalDag, PathwayLearner wiring

### Primal/Spring teams
Provide: `niche.rs` self-knowledge, `health.check`, `capability.list`, structured `tracing` logging, Dark Forest compliance
All 8 springs have deploy graphs and capability registry sync. 13/13 primals at zero debt.

### Niche/Emergent System developers
Use: atomic signals for common patterns, TOML graph definitions for custom coordination, `fallback = "skip"` for optional deps
Study: `rootpulse_commit.toml` (transactional), `game_engine_tick.toml` (continuous), `02_ARCHITECTURE.md` (signal vocabulary)

---

## Read More

- **[README.md](./README.md)** — Full index, ecosystem context, signal vocabulary
- **[02_ARCHITECTURE.md](./02_ARCHITECTURE.md)** — Atomic decomposition layer
- **[03_GRAPH_EXECUTION.md](./03_GRAPH_EXECUTION.md)** — Graph patterns
- **[04_BIDIRECTIONAL_LEARNING.md](./04_BIDIRECTIONAL_LEARNING.md)** — Feedback loop
- **[05_PATHWAY_OPTIMIZATION.md](./05_PATHWAY_OPTIMIZATION.md)** — Pattern discovery
- **[08_NICHE_API_PATTERNS.md](./08_NICHE_API_PATTERNS.md)** — Continuous niches
- **[09_ROOTPULSE_CASE_STUDY.md](./09_ROOTPULSE_CASE_STUDY.md)** — Working example + Barrick convergence
- **[10_ROADMAP.md](./10_ROADMAP.md)** — Atomic signal activation path
