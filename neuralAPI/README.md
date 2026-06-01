# Neural API Architecture — Adaptive Multi-Layer Orchestration

**Status**: Whitepaper Series (Phase 32 revision — partially implemented)
**Updated**: May 14, 2026
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

### The Composition Collapse

The ecoPrimals ecosystem has grown to **427 registered capability methods**
across **13 primals** and **15 capability domains**. This is powerful but
produces a combinatorial surface that individual springs must navigate.

The Neural API's deepest goal is **composition collapse**: reducing
that surface from hundreds of individual method calls to a small set of
**atomic signals** — operations addressed to composition tiers
(Tower, Node, Nest, NUCLEUS) that biomeOS decomposes into the correct
primal-level calls internally.

```
TODAY (427 methods, 13 primals):
  spring → ctx.call("security", "crypto.sign", ...) → bearDog
  spring → ctx.call("discovery", "beacon.announce", ...) → songbird
  spring → ctx.call("defense", "audit.log_event", ...) → skunkBat

COLLAPSED (atomic signals):
  spring → neural_api.signal("tower", "publish", payload)
  biomeOS decomposes: sign → announce → audit_log
  spring never names individual primals
```

This is not abstraction for abstraction's sake. It is the path from
"8 springs each managing 13 primal connections" to "8 springs each
speaking 4 atomic tiers." See `02_ARCHITECTURE.md` for the full
decomposition layer specification.

---

## Document Series

### Conceptual Foundation

1. **[00_INTRODUCTION.md](./00_INTRODUCTION.md)** — What is Neural API?
2. **[01_PHILOSOPHY.md](./01_PHILOSOPHY.md)** — Why emergence over engineering?
3. **[02_ARCHITECTURE.md](./02_ARCHITECTURE.md)** — Atomic decomposition layer (Tower/Node/Nest/NUCLEUS)

### Technical Deep Dives

4. **[03_GRAPH_EXECUTION.md](./03_GRAPH_EXECUTION.md)** — Graph coordination patterns (Sequential, Parallel, ConditionalDag, Pipeline, Continuous)
5. **[04_BIDIRECTIONAL_LEARNING.md](./04_BIDIRECTIONAL_LEARNING.md)** — Forward execution, backward learning
6. **[05_PATHWAY_OPTIMIZATION.md](./05_PATHWAY_OPTIMIZATION.md)** — Usage tracking, pattern discovery, signal collapse metrics

### Implementation Guides

7. **[06_BIOMEOS_IMPLEMENTATION.md](./06_BIOMEOS_IMPLEMENTATION.md)** — biomeOS graph executor, pathway learner, optimization engine
8. **[07_PRIMAL_REQUIREMENTS.md](./07_PRIMAL_REQUIREMENTS.md)** — 13/13 primals: metrics, capabilities, Dark Forest compliance
9. **[08_NICHE_API_PATTERNS.md](./08_NICHE_API_PATTERNS.md)** — Transactional vs continuous niches, game engine at 60 Hz

### Practical Application

10. **[09_ROOTPULSE_CASE_STUDY.md](./09_ROOTPULSE_CASE_STUDY.md)** — First transactional niche (version control) + Barrick Lab convergence
11. **[10_ROADMAP.md](./10_ROADMAP.md)** — Atomic signal activation path

---

## Emergent Systems via Neural API

The same graph execution engine powers radically different systems.
biomeOS doesn't need domain knowledge — it executes capability graphs:

| Emergent System | Coordination | Atomic Tier | Springs/Primals | Graph |
|-----------------|:------------:|:-----------:|-----------------|-------|
| **RootPulse** (version control) | Sequential | Nest | rhizoCrypt + loamSpine + sweetGrass + BearDog + NestGate | `rootpulse_commit.toml` |
| **RPGPT** (sovereign RPG engine) | Continuous + Sequential | NUCLEUS | ludoSpring + rhizoCrypt + loamSpine + sweetGrass + BearDog + Squirrel + petalTongue | `game_engine_tick.toml` + provenance at session boundaries |
| **AlphaFold-class** (protein folding) | Pipeline | Node | neuralSpring (evoformer) + hotSpring (physics) + wetSpring (sequence) + toadStool (GPU) | `neuralspring_spectral_pipeline.toml` |
| **Cross-spring ecology** | Sequential | Node | airSpring (ET0) + wetSpring (diversity) + neuralSpring (spectral) | `cross_spring_ecology.toml` |
| **Surgical VR** | Continuous | NUCLEUS | healthSpring + petalTongue + ludoSpring | `surgical_vr_deploy.toml` |
| **Barrick pipelines** | Pipeline | Nest + Node | breseq output + lithoSpore validation + NestGate storage + petalTongue visualization | (planned — Barrick Lab tool convergence) |

The Neural API doesn't distinguish these. A game session and a protein
folding run are both "graphs of capability calls with timing constraints."

---

## Phase 32 Atomic Model — The Decomposition Substrate

The Neural API's composition collapse depends on the Phase 32 atomic model.
Each tier is a stable, well-tested unit that biomeOS can address as a single
entity:

| Tier | Primals | Particle | Role |
|------|---------|:--------:|------|
| **Tower** | bearDog + songbird + skunkBat | electron | Trust boundary — crypto + discovery + defense |
| **Node** | Tower + toadStool + barraCuda + coralReef | proton | Compute substrate — dispatch + execute + compile |
| **Nest** | Tower + nestGate + rhizoCrypt + loamSpine + sweetGrass | neutron | Storage + provenance — content-addressed data + lineage |
| **NUCLEUS** | Node + Nest (10 unique primals) | atom | Full composition |
| **Meta-Tier** | biomeOS + squirrel + petalTongue | — | Cross-atomic: orchestration + AI + UI |

When a spring sends `signal("tower", "authenticate", payload)`, biomeOS
decomposes it into `bearDog.btsp.negotiate` → `skunkBat.defense.verify_lineage`
and returns the composed result. The spring never knows which primals ran.

### Atomic Signal Vocabulary (Goals)

| Atomic Signal | Tier | Decomposition |
|--------------|:----:|--------------|
| `tower.authenticate` | Tower | bearDog `btsp.negotiate` → skunkBat `defense.verify_lineage` |
| `tower.publish` | Tower | bearDog `crypto.sign` → songbird `beacon.announce` → skunkBat `audit.log_event` |
| `tower.discover` | Tower | songbird `discovery.find` → bearDog `crypto.verify_peer` |
| `tower.secure_channel` | Tower | bearDog `tls.handshake` → songbird `relay.establish` → skunkBat `threat.assess` |
| `node.compute` | Node | toadStool `compute.dispatch` → coralReef `shader.compile` → barraCuda `tensor.matmul` |
| `node.validate` | Node | toadStool `workload.validate` → barraCuda `validate.result` |
| `nest.store` | Nest | nestGate `content.put` → rhizoCrypt `dag.event.append` → loamSpine `spine.commit` → sweetGrass `braid.create` |
| `nest.retrieve` | Nest | nestGate `content.get` → rhizoCrypt `dag.session.get` → sweetGrass `provenance.query` |
| `nest.verify` | Nest | loamSpine `proof.verify` → bearDog `crypto.verify` → sweetGrass `provenance.validate` |
| `nucleus.deploy` | NUCLEUS | biomeOS `graph.execute` (full atomic graph) |
| `nucleus.status` | NUCLEUS | biomeOS `biomeos.spring_status` + topology + health |

This vocabulary collapses the 427-method surface into ~20 atomic signals
that cover the most common composition patterns. Springs that need
fine-grained control can still call individual capability domains directly.

---

## gen4 Context — Neural API as the Kernel Substrate

The Neural API's domain-agnostic graph execution is what enables gen4 products
to exist. A game engine, a science pipeline, and a health dashboard are all
"graphs of capability calls" — the Neural API doesn't distinguish them. This
makes the Neural API the kernel substrate for a sovereign operating system.

### gen4 Products Built on Neural API

| Product | Coordination Pattern | Atomic Tier | Graph |
|---------|---------------------|:-----------:|-------|
| esotericWebb | Deploy graphs + session pipeline | NUCLEUS | `webb_*.toml` (6 atomic tiers) |
| helixVision | Pipeline + sequential | Nest + Node | Genomics deploy graphs |
| RPGPT Engine | Continuous + transactional | NUCLEUS | `game_engine_tick.toml` |
| Cross-spring ecology | Sequential | Node | `cross_spring_ecology.toml` |
| Barrick validation | Pipeline | Nest | lithoSpore module graphs |

---

## Implementation Status (May 14, 2026)

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
| **Capability routing** | Implemented | `biomeos-core` registry + `biomeos-atomic-deploy` NeuralRouter (320+ translations, 27 domains) |
| **tarpc forwarding** | Implemented | JSON-RPC primary, tarpc escalation with fallback |
| **RootPulse graphs** | Implemented | commit, branch, merge, diff, federate |
| **Game engine graph** | Implemented | `game_engine_tick.toml` (60 Hz, feedback edges) |
| **MetricsCollector** | Implemented | redb-backed (biomeos-graph) + in-memory (biomeos-core) |
| **NeuralBridge (primalSpring)** | Implemented | `ecoPrimal/src/ipc/neural_bridge.rs` — capability.call, graph.deploy, topology.rescan |
| **Token forwarding** | Implemented | v3.50: `_bearer_token` propagation through all capability paths |
| **MethodGate / BTSP** | Implemented | 13/13 authenticated, JH-0/JH-2 resource envelope |
| **Dark Forest compliance** | Structural | 5-pillar gate validated by `s_dark_forest_gate` scenario |
| **PathwayLearner** | Code exists | **Not wired into execution path** |
| **Atomic signal vocabulary** | Designed | Needs graph definitions + Neural API route registration |
| **Bidirectional feedback** | Not started | Spec written (04_BIDIRECTIONAL_LEARNING.md) |
| **Pattern discovery** | Not started | Spec written (05_PATHWAY_OPTIMIZATION.md) |

### Critical gaps for atomic signal activation

1. **Atomic signal → graph dispatch** — `capability.call("tower", "publish", ...)` must trigger a graph execution (e.g., `tower_publish.toml`), not a single-method dispatch. The NeuralRouter needs a "signal" tier above individual capabilities.
2. **Unified graph schema** — `[[nodes]]` (Neural API server) vs `[[graph.nodes]]` (ContinuousExecutor). Must unify.
3. **Continuous execution via JSON-RPC** — ContinuousExecutor only runs via `biomeos continuous` CLI. Need `graph.start_continuous`, `graph.pause`, `graph.resume`, `graph.stop`.
4. **ConditionalDag not implemented** — real branching needed for RPGPT and complex pipelines.
5. **PathwayLearner disconnected** — exists but doesn't receive execution metrics or feed back into scheduling.
6. **Mixed coordination** — continuous ticks with transactional subgraphs at session boundaries.

---

## Ecosystem Context (May 14, 2026)

- **13 primals** — all BTSP Phase 3 AEAD authenticated, MethodGate 13/13, zero debt
- **427 registered capability methods** — 313 exercised (73.3%)
- **8 springs** — all Tier 4 IPC-first, all eukaryotic UniBin
- **123 deploy graphs** across ecosystem (78 in primalSpring)
- **13,760+ tests** across the river delta
- **Dark Forest Glacial Gate** — 5-pillar security standard formalized
- **biomeOS v3.50** — 7,924 tests, 320+ translations, 27 domains, token forwarding, MethodGate
- **primalSpring v0.9.25** — 29 validation scenarios, 651+ tests, NeuralBridge client
- **Phase**: Interstadial — sovereignty pre-wire, shadow runs executing

---

## Quick Start

**For biomeOS developers**: [06_BIOMEOS_IMPLEMENTATION.md](./06_BIOMEOS_IMPLEMENTATION.md) then [03_GRAPH_EXECUTION.md](./03_GRAPH_EXECUTION.md)

**For primal/spring teams**: [07_PRIMAL_REQUIREMENTS.md](./07_PRIMAL_REQUIREMENTS.md) then [02_ARCHITECTURE.md](./02_ARCHITECTURE.md)

**For niche developers**: [08_NICHE_API_PATTERNS.md](./08_NICHE_API_PATTERNS.md) then [09_ROOTPULSE_CASE_STUDY.md](./09_ROOTPULSE_CASE_STUDY.md)

---

## Related Work

- **[RootPulse](../RootPulse/)** — First transactional niche (version control via primal coordination)
- **biomeOS v3.50** — 7,924 tests, 320+ translations, token forwarding, MethodGate JH-0/JH-2
- **primalSpring v0.9.25** — `NeuralBridge`, `EmergentSystem::RootPulse`, 29 validation scenarios
- **[Dark Forest Glacial Gate](../../springs/primalSpring/specs/DARK_FOREST_GLACIAL_GATE.md)** — 5-pillar security invariant standard
- **[Barrick Lab Software](https://barricklab.org/twiki/bin/view/Lab/SoftwareList)** — breseq, pLannotate, OSTIR, EFM Calculator → lithoSpore Rust reproduction targets

---

## Next Steps — Atomic Signal Activation

1. **Define Tower signal graphs** — `tower_publish.toml`, `tower_authenticate.toml`, `tower_discover.toml`
2. **Wire signal→graph dispatch in NeuralRouter** — `capability.call("tower", ...)` triggers graph execution
3. **Implement ConditionalDag** — real conditional branching
4. **Wire PathwayLearner** — record metrics per execution, surface suggestions
5. **Expose continuous execution via JSON-RPC** — session management methods
6. **Mixed coordination** — transactional subgraphs within continuous graphs

---

*"Intelligence emerges not from complexity, but from the right kind of simplicity, repeated and refined."*
