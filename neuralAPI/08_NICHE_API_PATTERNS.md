# Niche API Patterns — The Game Engine as First Continuous Niche

**From transactional coordination to real-time orchestration**

**Date**: March 10, 2026
**Status**: Whitepaper - Architectural Design

---

## The Niche Spectrum

Niches are Layer 3 abstractions — domain-specific coordination patterns that
compose primals into capabilities no single primal provides. The Neural API
whitepaper (00_INTRODUCTION.md) describes three example niches: RootPulse
(version control), Hive (CI/CD), and Reef (deployment).

All three share a characteristic: they are **transactional**. A user triggers
an operation (commit, build, deploy), the primal graph executes, and the
operation completes. The graph runs once per trigger.

But the full niche spectrum includes a second, harder class: **continuous**
niches. These run indefinitely, ticking at a fixed frequency, where each
tick's output feeds the next tick's input. The canonical example is a game
engine — but the pattern applies to any real-time system: live monitoring,
streaming simulation, collaborative editing, or live performance.

```
Niche Spectrum

Transactional                              Continuous
     │                                          │
     ▼                                          ▼
  RootPulse    Hive    Reef    Dashboard    Game Engine
  (commit)    (build)  (deploy) (1 Hz)      (60 Hz)

  ◄──── biomeOS supports today ────►  ◄── needs evolution ──►
```

This document specifies the continuous niche pattern and proposes the game
engine as the first implementation, because it forces the hardest variant
of the problem and makes every easier variant a special case.

---

## Why the Game Engine First

### The virtuous difficulty argument

RootPulse's commit workflow involves 6 primals executing in ~50ms, triggered
by a human action. The game engine involves 7+ primals executing in ~16.67ms,
triggered by a clock, 60 times per second, indefinitely.

Solving the hard problem first yields a system where:

- A 1 Hz dashboard is a game engine at 1/60th speed.
- A batch pipeline is a game engine that runs exactly one tick.
- RootPulse's real-time collaboration is a game engine with commit semantics
  instead of physics.

If biomeOS can orchestrate a game at 60 Hz with real-time budgets, partial
failure recovery, and feedback loops, it can orchestrate anything.

### The learning argument

The Neural API's core innovation is bidirectional learning: observe execution,
discover patterns, optimize automatically. Learning requires a tight feedback
loop. RootPulse provides signal at human pace — maybe 100 commits per day.
A game engine provides signal at 60 Hz — 5.184 million frames per day.

The game engine gives the Neural API's Pathway Learner a dataset 50,000x
richer than RootPulse, per day. It can discover that "running audio 2ms ahead
of visual reduces perceived latency" in an afternoon, not a quarter.

---

## Continuous Coordination Mode

### Current coordination modes

biomeOS supports four coordination patterns (biomeos-graph/src/parser.rs):

| Mode | Behavior | Use case |
|------|----------|----------|
| Sequential | Phases in dependency order, each completes | Deploy graphs |
| Parallel | Independent nodes run concurrently | Bulk operations |
| ConditionalDAG | Branch based on node outputs | Conditional workflows |
| Pipeline | Streaming: output of one feeds input of next | Data processing |

All four are **run-to-completion**. The graph executes once and terminates.

### The fifth mode: Continuous

```toml
[graph]
id = "mycorrhizal_explorer"
coordination = "Continuous"

[graph.tick]
target_hz = 60
max_accumulator_ms = 250
budget_warning_ms = 14
```

Continuous coordination adds:

1. **Tick clock**: biomeOS maintains a fixed-timestep clock. Each tick, the
   graph's dependency order is re-executed with the previous tick's outputs
   as inputs.

2. **Budget awareness**: Each node reports execution time. If a node exceeds
   its budget, biomeOS can:
   - Use the previous tick's output (staleness tolerance)
   - Reduce the node's quality (e.g., skip physics substeps)
   - Log a budget violation for the Pathway Learner

3. **Feedback edges**: Standard graphs are DAGs (acyclic). Continuous graphs
   allow marked "next-tick" edges where a node's output becomes another
   node's input in the *next* tick, not the current one. This enables:
   - Input → game logic → render → (next tick) → input reads previous state
   - Metrics → DDA → (next tick) → game logic uses adjusted difficulty

4. **Partial execution**: If a tick runs over budget, completed nodes' outputs
   are used; incomplete nodes reuse their previous output. The frame still
   renders.

5. **Niche lifecycle**: Continuous niches have sessions with start, pause,
   resume, and stop semantics. biomeOS manages the session state.

```
Tick N:
  input ──► game_logic ──► physics ──► scene ──┬──► render
                                                ├──► audio
                                                └──► metrics
                                                       │
                                               (next-tick edge)
                                                       │
Tick N+1:                                              ▼
  input ──► game_logic ◄── difficulty_adjustment ◄── metrics
```

---

## The Game Engine Niche

### Primal composition

```
┌─────────────────────────────────────────────────────────┐
│              Niche: Game Engine                          │
│              coordination = "Continuous"                 │
│              tick_hz = 60                                │
│                                                         │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐          │
│  │ Chimera:  │  │ Chimera:  │  │ Chimera:  │          │
│  │ Senses    │  │ Simulator │  │ Brain     │          │
│  │           │  │           │  │           │          │
│  │ petal     │  │ barraCuda │  │ ludoSpr.  │          │
│  │ Tongue    │  │ toadStool │  │ neural    │          │
│  │ (scene,   │  │ (physics, │  │ Spring    │          │
│  │  audio,   │  │  collision│  │ (game     │          │
│  │  haptic,  │  │  render)  │  │  logic,   │          │
│  │  braille, │  │           │  │  DDA,     │          │
│  │  interact)│  │           │  │  PCG)     │          │
│  └───────────┘  └───────────┘  └───────────┘          │
│                                                         │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐          │
│  │ Optional: │  │ Optional: │  │ Optional: │          │
│  │ Science   │  │ Network   │  │ Storage   │          │
│  │           │  │           │  │           │          │
│  │ wetSpring │  │ Songbird  │  │ NestGate  │          │
│  │ hotSpring │  │ (multi-   │  │ (world    │          │
│  │ (domain   │  │  player)  │  │  persist) │          │
│  │  physics) │  │           │  │           │          │
│  └───────────┘  └───────────┘  └───────────┘          │
└─────────────────────────────────────────────────────────┘
```

### Node definitions

```toml
[graph]
id = "game_engine_niche"
coordination = "Continuous"

[graph.tick]
target_hz = 60
max_accumulator_ms = 250
budget_warning_ms = 14

# ── Input ──
[[nodes]]
id = "input"
output = "sensor_events"
capabilities = ["interaction"]
budget_ms = 1
[nodes.primal]
by_capability = "visualization"

# ── Game Logic ──
[[nodes]]
id = "game_logic"
depends_on = ["input"]
output = "game_state"
capabilities = ["game"]
budget_ms = 3
[nodes.primal]
by_capability = "game"

# ── Physics ──
[[nodes]]
id = "physics"
depends_on = ["game_logic"]
output = "physics_state"
capabilities = ["compute"]
budget_ms = 4
[nodes.primal]
by_capability = "compute"

# ── Scene Update ──
[[nodes]]
id = "scene"
depends_on = ["physics", "game_logic"]
output = "render_plan"
capabilities = ["visualization"]
budget_ms = 2
[nodes.primal]
by_capability = "visualization"

# ── Render ──
[[nodes]]
id = "render"
depends_on = ["scene"]
output = "frame"
capabilities = ["compute"]
budget_ms = 6
[nodes.primal]
by_capability = "compute"

# ── Audio ──
[[nodes]]
id = "audio"
depends_on = ["scene"]
output = "audio_buffer"
capabilities = ["visualization"]
budget_ms = 2
[nodes.primal]
by_capability = "visualization"

# ── Metrics (next-tick feedback) ──
[[nodes]]
id = "metrics"
depends_on = ["input", "game_logic"]
output = "engagement"
capabilities = ["game"]
budget_ms = 1
feedback_to = ["game_logic"]
[nodes.primal]
by_capability = "game"
```

### Comparison with RootPulse

| Dimension | RootPulse | Game Engine |
|-----------|-----------|-------------|
| Trigger | User action | Clock (60 Hz) |
| Duration | Milliseconds | Indefinite session |
| Primals (required) | rhizoCrypt, LoamSpine, NestGate, BearDog | petalTongue, barraCuda, toadStool, ludoSpring |
| Primals (optional) | SweetGrass, Songbird, Squirrel | Springs, Songbird, NestGate |
| State model | DAG present → linear past | Tick buffer → replay history |
| Budget constraint | Human patience (~200ms) | Frame deadline (16.67ms) |
| Learning signal | ~100 ops/day | ~5M frames/day |
| Coordination | Sequential, DAG | Continuous with feedback edges |
| Failure mode | Retry or abort | Use previous output, degrade gracefully |

### Temporal mapping

RootPulse's two-tier temporal model (rhizoCrypt DAG present / LoamSpine
linear past) has a direct analogue in the game engine:

| RootPulse | Game Engine | Shared concept |
|-----------|-------------|----------------|
| rhizoCrypt ephemeral session | Current tick's working state | Mutable present |
| LoamSpine append-only history | Replay buffer / recorded session | Immutable past |
| Dehydration (ephemeral → permanent) | Session end → save game | State crystallization |
| Merkle proof of inclusion | Frame hash for deterministic replay | Cryptographic integrity |
| SweetGrass attribution | Engagement tracking per player | Semantic provenance |
| BearDog signing | Anti-cheat (signed state) | Trust |

---

## Neural API Learning in Continuous Niches

### Forward pass (execution)

Each tick:
1. biomeOS triggers the graph
2. Nodes execute in dependency order
3. Outputs flow to dependent nodes
4. Frame completes or budget exceeded

### Backward pass (learning)

The Pathway Learner observes:

| Signal | Source | What it learns |
|--------|--------|---------------|
| Node latency | Every node, every tick | Budget allocation optimization |
| Budget violations | Nodes exceeding budget_ms | Which nodes need offloading |
| Frame drops | Ticks where accumulator > 2×dt | System is overloaded |
| Engagement metrics | ludoSpring metrics node | Which configurations keep players in flow |
| Accessibility scores | ludoSpring accessibility node | Which modality configurations work |
| Staleness | Nodes reusing previous output | Where quality is degrading |

### Emergent optimizations

After observing thousands of frames:

```
Day 1:   physics=4ms, render=6ms, audio=2ms  → 12ms total, 4ms slack
Day 30:  Learned: audio can start 2ms before render completes
         New total: 10ms, 6ms slack → enable physics substeps
Day 90:  Learned: player explores slowly → reduce tick to 30Hz when idle
         Power savings: 50% during exploration, 60Hz during action
Day 180: Learned: blind player profile → skip render, boost audio budget
         Audio gets 14ms budget, spatial accuracy doubles
```

These optimizations are NOT programmed. They emerge from the Pathway Learner
observing the tight feedback loop.

---

## Implementation Requirements for biomeOS

### Graph parser extension

Add `Continuous` to `CoordinationPattern` enum in
`biomeos-graph/src/parser.rs`:

```rust
match coord_str.as_str() {
    "Sequential" => Ok(CoordinationPattern::Sequential),
    "Parallel" => Ok(CoordinationPattern::Parallel),
    "ConditionalDAG" => Ok(CoordinationPattern::ConditionalDAG),
    "Pipeline" => Ok(CoordinationPattern::Pipeline),
    "Continuous" => Ok(CoordinationPattern::Continuous),
    other => Err(...)
}
```

### Tick-aware executor

The `neural_executor.rs` needs a continuous execution loop:

```rust
pub struct ContinuousExecutor {
    graph: PrimalGraph,
    clock: TickClock,       // from ludoSpring's game_loop pattern
    node_cache: HashMap<NodeId, NodeOutput>,  // previous tick's outputs
    metrics: MetricsCollector,
}

impl ContinuousExecutor {
    pub async fn run_session(&mut self) {
        loop {
            let dt = self.clock.begin_frame();
            while self.clock.should_tick() {
                self.execute_tick().await;
                self.clock.consume_tick();
            }
        }
    }

    async fn execute_tick(&mut self) {
        let phases = topological_sort(&self.graph);
        for phase in phases {
            let results = join_all(phase.nodes.iter().map(|node| {
                self.execute_node_with_budget(node)
            })).await;
            // Cache outputs for next tick's feedback edges
            for (node_id, output) in results {
                self.node_cache.insert(node_id, output);
            }
        }
    }

    async fn execute_node_with_budget(&self, node: &GraphNode) -> NodeOutput {
        let budget = Duration::from_millis(node.budget_ms);
        match timeout(budget, self.execute_node(node)).await {
            Ok(output) => output,
            Err(_) => {
                self.metrics.record_budget_violation(node.id);
                // Use previous tick's output
                self.node_cache.get(&node.id).cloned()
                    .unwrap_or_default()
            }
        }
    }
}
```

### Feedback edge support

Allow `feedback_to` in graph node definitions. During topological sort,
feedback edges are excluded (they connect tick N to tick N+1, not within
a single tick). The executor reads feedback outputs from `node_cache`.

### Session lifecycle

```rust
pub enum SessionState {
    Starting,   // Primals spawning, resources allocated
    Running,    // Ticking
    Paused,     // Clock frozen, primals idle
    Stopping,   // Graceful shutdown, state saved
    Stopped,    // Session ended
}
```

### Niche manifest

Following the RootPulse niche pattern (`niches/rootpulse/rootpulse-niche.yaml`),
the game engine niche needs a manifest:

```toml
# niches/game-engine.toml

[niche]
name = "game-engine"
version = "0.1.0"
type = "continuous"
description = "Real-time game engine via primal coordination"

[[primals]]
binary = "petaltongue"
provides = ["visualization", "interaction", "scene_graph"]
requires = ["discovery"]

[[primals]]
binary = "toadstool"
provides = ["compute", "3d_render", "audio_device"]
requires = ["security"]

[[primals]]
binary = "ludospring"
provides = ["game", "ludology", "procedural_generation"]
requires = ["discovery"]

[[primals]]
binary = "barracuda"
provides = ["compute", "collision", "spatial_audio"]
optional = true

[[graphs]]
name = "deploy"
path = "../graphs/game_engine_deploy.toml"
default = true

[[graphs]]
name = "tick"
path = "../graphs/game_engine_tick.toml"
coordination = "Continuous"
```

---

## Generalization: All Continuous Niches

The game engine pattern generalizes to any real-time coordination:

| Niche | Tick rate | Primals | Domain |
|-------|-----------|---------|--------|
| Game engine | 60 Hz | petalTongue, toadStool, ludoSpring, barraCuda | Interactive simulation |
| Live dashboard | 1 Hz | petalTongue, springs | Monitoring |
| Streaming simulation | 10 Hz | barraCuda, springs, petalTongue | Science |
| Collaborative editing | 30 Hz | rhizoCrypt, petalTongue, Songbird | Real-time co-authoring |
| Live performance | 44100 Hz | petalTongue (audio), barraCuda (DSP) | Music/sound art |
| Biosignal monitoring | 250 Hz | healthSpring, petalTongue | Clinical |

The game engine is the hardest (highest tick rate with the most primals and
strictest budget). Solving it first means every other continuous niche is
a configuration change, not an architecture change.

---

## Relationship to Existing Whitepaper Series

This document fills the slot described in the README.md table of contents
as "08_NICHE_API_PATTERNS.md — Building high-level APIs". It extends the
conceptual framework from 00_INTRODUCTION.md (three-layer architecture) and
06_BIOMEOS_IMPLEMENTATION.md (graph execution model) with the continuous
coordination pattern.

The next document in the series, 09_ROOTPULSE_CASE_STUDY.md, describes the
first transactional niche. This document describes the first continuous niche.
Together they cover the full niche spectrum.

---

*"The game engine is not a new primal. It is what primals do together,
60 times per second."*
