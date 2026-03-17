# Neural API Architecture — Adaptive Multi-Layer Orchestration

**Status**: Whitepaper Series (partially implemented)
**Updated**: March 15, 2026
**Original**: January 4, 2026
**Authors**: ecoPrimals Architecture Team

---

## Overview

The **Neural API** is the orchestration layer of biomeOS. It executes
capability graphs over autonomous primals, learns from execution traces,
and evolves coordination strategies over time. Complex systems — version
control (RootPulse), sovereign RPG engines (RPGPT), protein folding
pipelines, cross-spring scientific workflows — emerge as graphs over
the Neural API. biomeOS doesn't know what these systems are; it only
knows how to execute capability graphs and learn from them.

```
Traditional:  Request -> Route -> Execute -> Response
Neural:       Request -> Learn -> Optimize -> Execute -> Feedback -> Adapt
                         ^                               |
                         +-------------------------------+
```

### The Core Insight

Every spring becomes a BYOB niche: self-describing via `niche.rs`,
discoverable via capability routing, deployable via a TOML graph.
Complex systems like RootPulse and RPGPT are not primals — they are
coordination patterns that emerge from graph execution over existing
capabilities. The Neural API is what makes emergence possible.

---

## Document Series

### Conceptual Foundation

1. **[00_INTRODUCTION.md](./00_INTRODUCTION.md)** — What is Neural API?
2. **[01_PHILOSOPHY.md](./01_PHILOSOPHY.md)** — Why emergence over engineering?
3. **[02_ARCHITECTURE.md](./02_ARCHITECTURE.md)** — Technical layer design

### Technical Deep Dives

4. **[03_GRAPH_EXECUTION.md](./03_GRAPH_EXECUTION.md)** — Graph coordination patterns (Sequential, Parallel, ConditionalDag, Pipeline, Continuous)
5. **[04_BIDIRECTIONAL_LEARNING.md](./04_BIDIRECTIONAL_LEARNING.md)** — Forward execution, backward learning
6. **[05_PATHWAY_OPTIMIZATION.md](./05_PATHWAY_OPTIMIZATION.md)** — Usage tracking, pattern discovery, optimization

### Implementation Guides

7. **[06_BIOMEOS_IMPLEMENTATION.md](./06_BIOMEOS_IMPLEMENTATION.md)** — biomeOS graph executor, pathway learner, optimization engine
8. **[07_PRIMAL_REQUIREMENTS.md](./07_PRIMAL_REQUIREMENTS.md)** — Metrics reporting, capability declaration, `niche.rs` convention
9. **[08_NICHE_API_PATTERNS.md](./08_NICHE_API_PATTERNS.md)** — Transactional vs continuous niches, game engine at 60 Hz

### Practical Application

10. **[09_ROOTPULSE_CASE_STUDY.md](./09_ROOTPULSE_CASE_STUDY.md)** — First transactional niche (version control)
11. **[10_ROADMAP.md](./10_ROADMAP.md)** — Implementation timeline and phase tracking

---

## Emergent Systems via Neural API

The same graph execution engine powers radically different systems.
biomeOS doesn't need domain knowledge — it executes capability graphs:

| Emergent System | Coordination | Springs/Primals | Graph |
|-----------------|:------------:|-----------------|-------|
| **RootPulse** (version control) | Sequential | rhizoCrypt + loamSpine + sweetGrass + BearDog + NestGate | `rootpulse_commit.toml` |
| **RPGPT** (sovereign RPG engine) | Continuous + Sequential | ludoSpring + rhizoCrypt + loamSpine + sweetGrass + BearDog + Squirrel + petalTongue | `game_engine_tick.toml` + provenance at session boundaries |
| **AlphaFold-class** (protein folding) | Pipeline | neuralSpring (evoformer) + hotSpring (physics) + wetSpring (sequence) + toadStool (GPU) | `neuralspring_spectral_pipeline.toml` |
| **Cross-spring ecology** | Sequential | airSpring (ET0) + wetSpring (diversity) + neuralSpring (spectral) | `cross_spring_ecology.toml` |
| **Surgical VR** | Continuous | healthSpring + petalTongue + ludoSpring | `surgical_vr_deploy.toml` |

The Neural API doesn't distinguish these. A game session and a protein
folding run are both "graphs of capability calls with timing constraints."

---

## Quick Start

**For biomeOS developers**: [06_BIOMEOS_IMPLEMENTATION.md](./06_BIOMEOS_IMPLEMENTATION.md) then [03_GRAPH_EXECUTION.md](./03_GRAPH_EXECUTION.md)

**For primal/spring teams**: [07_PRIMAL_REQUIREMENTS.md](./07_PRIMAL_REQUIREMENTS.md) then [09_ROOTPULSE_CASE_STUDY.md](./09_ROOTPULSE_CASE_STUDY.md)

**For niche developers**: [08_NICHE_API_PATTERNS.md](./08_NICHE_API_PATTERNS.md) then [03_GRAPH_EXECUTION.md](./03_GRAPH_EXECUTION.md)

---

## Implementation Status (March 15, 2026)

| Component | Status | Location |
|-----------|--------|----------|
| **Graph parsing (TOML)** | Implemented | `biomeos-graph` crate |
| **Sequential execution** | Implemented | `biomeos-atomic-deploy` GraphExecutor |
| **Parallel execution** | Implemented | Topological sort + wave-based |
| **ConditionalDag** | Parsed only | Executes as Sequential — needs real branching |
| **Pipeline (streaming)** | Parsed only | Executes as Sequential — needs streaming |
| **Continuous (60 Hz)** | Implemented | `biomeos-graph` ContinuousExecutor |
| **Feedback edges** | Implemented | `feedback_to` + `feedback_map` |
| **Session lifecycle** | Implemented | Starting/Running/Paused/Stopping/Stopped |
| **Capability routing** | Implemented | `biomeos-core` registry + `biomeos-atomic-deploy` NeuralRouter |
| **tarpc forwarding** | Implemented | JSON-RPC primary, tarpc escalation with fallback |
| **RootPulse graphs** | Implemented | commit, branch, merge, diff, federate |
| **Game engine graph** | Implemented | `game_engine_tick.toml` (60 Hz, feedback edges) |
| **MetricsCollector** | Implemented | redb-backed (biomeos-graph) + in-memory (biomeos-core) |
| **PathwayLearner** | Code exists | **Not wired into execution path** |
| **Bidirectional feedback** | Not started | Spec only |
| **Pattern discovery** | Not started | Research phase |

### Critical gaps for ludoSpring RPGPT and cross-spring composition

1. **Dual graph schema** — `[[nodes]]` (Neural API server) vs `[[graph.nodes]]` (ContinuousExecutor). Must unify so `neural_api.execute_graph` handles both.
2. **No continuous execution via JSON-RPC** — ContinuousExecutor only runs via `biomeos continuous` CLI. Need `graph.start_continuous`, `graph.pause`, `graph.resume`, `graph.stop` methods.
3. **ConditionalDag not implemented** — RPGPT needs conditional flows (AI availability, ruleset validation). Currently executes like Sequential.
4. **PathwayLearner disconnected** — Exists but doesn't receive execution metrics or feed back into graph scheduling.
5. **Mixed coordination** — RPGPT needs continuous ticks (game loop) with transactional subgraphs at session boundaries (provenance commit). Currently these are separate execution modes.

---

## Related Work

- **[RootPulse](../RootPulse/)** — First transactional niche (version control via primal coordination)
- **[biomeOS v2.41](../../phase2/biomeOS/)** — 5,017 tests, 77.61% coverage, 124 capability translations
- **[Capability Registry](../../phase2/biomeOS/config/capability_registry.toml)** — 12 domains, 120+ translations

---

## Next Steps (v2.42)

1. **Unify graph schema** — single format for transactional and continuous graphs
2. **Expose continuous execution via Neural API** — JSON-RPC session management
3. **Implement ConditionalDag** — real conditional branching
4. **Wire PathwayLearner** — record metrics per execution, surface suggestions
5. **Write missing chapters** — 02_ARCHITECTURE.md, 04_BIDIRECTIONAL_LEARNING.md, 05_PATHWAY_OPTIMIZATION.md
6. **Tick-level fallback** — optional primals can skip per-tick without killing the graph
7. **Mixed coordination** — transactional subgraphs within continuous graphs

---

*"Intelligence emerges not from complexity, but from the right kind of simplicity, repeated and refined."*

