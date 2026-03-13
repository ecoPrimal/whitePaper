# Graph Execution — How biomeOS Coordinates Primals

**TOML-defined graphs, coordination patterns, and execution engines**

**Date**: March 13, 2026  
**Status**: Whitepaper - Implementation Specification

---

## Overview

biomeOS orchestrates primals by executing **graphs** — declarative workflows defined in TOML. The graph executor translates semantic capability names into concrete primal invocations, respects dependency order, and supports both transactional (run-once) and continuous (fixed-timestep) coordination. All inter-primal communication uses JSON-RPC 2.0.

---

## Graph Types

### DeploymentGraph

A validated graph loaded from TOML. The `biomeos-graph` crate defines:

```toml
[graph]
id = "my-graph"
name = "My Graph"
version = "1.0.0"
coordination = "Sequential"

[graph.tick]   # Only for coordination = "Continuous"
target_hz = 60.0
max_accumulator_ms = 100.0
budget_warning_ms = 4.0

[graph.env]
VAR = "value"

[graph.outputs]
result = "node_id.output"
```

`GraphDefinition` fields: `id`, `name`, `version`, `coordination`, `tick` (optional), `env`, `nodes`, `outputs`.

### GraphNode

Each node is an execution unit with:

| Field | Purpose |
|-------|---------|
| `id` | Unique identifier within the graph |
| `name` | Human-readable label |
| `capability` | Semantic capability to invoke (e.g., `dag.dehydrate`) |
| `depends_on` | DAG edges — node IDs that must complete first |
| `feedback_to` | For Continuous: output feeds this node on the *next* tick |
| `budget_ms` | Per-node time budget; exceeded → reuse previous output |
| `env` | Node-scoped environment overrides |

---

## Coordination Patterns

`CoordinationPattern` (biomeos-graph) defines how nodes execute:

| Pattern | Behavior | Use case |
|---------|----------|----------|
| **Sequential** | Nodes one-at-a-time in dependency order | Deploy graphs, commit workflows |
| **Parallel** | Independent nodes run concurrently | Bulk operations |
| **ConditionalDag** | DAG with conditional branching | Workflows with if/else |
| **Pipeline** | Streaming: output of one feeds input of next | Data processing |
| **Continuous** | Fixed-timestep loop at target Hz (e.g. 60 Hz) | Game engines, dashboards |

Sequential, Parallel, ConditionalDag, and Pipeline are **run-to-completion**. The graph executes once and terminates. Continuous runs indefinitely until the session is stopped.

---

## Execution Engine

### biomeos-atomic-deploy: GraphExecutor

For transactional graphs (deployment, commit workflows):

1. **Topological sort** — Kahn's algorithm on `depends_on` edges yields execution phases.
2. **Phases** — Nodes in the same phase have no dependencies on each other; they run in parallel.
3. **Parallel within phases** — Semaphore limits concurrency (default 3).
4. **Rollback / checkpoint** — On failure, if `rollback_on_failure` is set, the executor rolls back completed nodes.

Used by `provenance_trio_deploy.toml`, `rootpulse_commit.toml`, and similar deployment/workflow graphs.

### biomeos-graph: ContinuousExecutor

For continuous graphs (game loops, live dashboards):

1. **TickClock** — Accumulator pattern: real elapsed time accumulates; each tick consumes a fixed `1/target_hz` slice. `max_accumulator_ms` caps catch-up to avoid spiral-of-death.
2. **SessionState** — Lifecycle: `Starting` → `Running` → `Paused` / `Stopping` → `Stopped`.
3. **Feedback edges** — `feedback_to` connects a node's output to another node's input on the *next* tick. Excluded from within-tick topological sort.
4. **Per-node budget** — If a node exceeds `budget_ms`, the previous tick's output is reused; a warning is logged.
5. **Output cache** — Node outputs are cached for feedback consumers and budget-overrun fallback.

---

## Example TOML Graphs

### provenance_trio_deploy.toml

Deploys the RootPulse provenance stack (LoamSpine, rhizoCrypt, sweetGrass) atop Tower. Five logical phases:

1. **Verify tower** — `verify-beardog` → `verify-songbird`
2. **Start LoamSpine** — `start-loamspine` → `health-loamspine`
3. **Start rhizoCrypt** — `start-rhizocrypt` → `health-rhizocrypt`
4. **Start sweetGrass** — `start-sweetgrass` → `health-sweetgrass`
5. **Register capabilities** — `register-loamspine-caps`, `register-rhizocrypt-caps`, `register-sweetgrass-caps` (parallel within phase)

Nodes use `[nodes.operation]` (`health_check`, `primal.launch`, `register_capabilities`) and `[nodes.config]` (`primal_name`, `timeout_secs`, `mode`).

### rootpulse_commit.toml

RootPulse commit workflow. Six phases:

1. **Health** — `check_rhizocrypt`, `check_loamspine` (parallel)
2. **Dehydrate** — rhizoCrypt `dag.dehydrate`
3. **Sign** — BearDog `crypto.sign`
4. **Store** — NestGate `storage.store`
5. **Commit** — LoamSpine `commit.session`
6. **Attribute** — sweetGrass `provenance.create_braid` (optional)

Uses `capability_call` with semantic names like `dag.dehydrate`, `commit.session`; the executor resolves these via the capability registry.

### game_engine_tick.toml

60 Hz continuous game loop. Five nodes:

```
input → game-logic → physics → scene → render
         ↑______________|
         feedback_to (next tick)
```

- `input` (1 ms) — Poll sensors
- `game-logic` (4 ms) — Rules, DDA; receives `feedback_to` from physics
- `physics` (4 ms) — Collision, integration; `feedback_to = "game-logic"`
- `scene` (3 ms) — Build render list
- `render` (4 ms) — Submit to GPU

`[graph.tick]`: `target_hz = 60`, `max_accumulator_ms = 100`, `budget_warning_ms = 4`.

---

## Capability Routing

`capability_registry.toml` maps semantic capability names to primal-specific methods. The executor discovers primal endpoints at runtime (socket paths, ports) and translates capability calls into JSON-RPC invocations.

Examples:

| Capability | Provider | Method |
|------------|----------|--------|
| `dag.dehydrate` | rhizocrypt | `dehydrate` |
| `commit.session` | loamspine | `session.commit` |
| `crypto.sign` | beardog | `ed25519_sign` |
| `provenance.create_braid` | sweetgrass | `sweetgrass.createBraid` |

Graphs reference capabilities by name; the registry and runtime discovery determine which primal and method to call.

---

## JSON-RPC Wire Protocol

All inter-primal communication uses **JSON-RPC 2.0**. The executor:

1. Resolves a capability (e.g., `dag.dehydrate`) to a provider primal and method via the registry.
2. Discovers the primal's endpoint (Unix socket or TCP) at runtime.
3. Builds a JSON-RPC request: `{"jsonrpc":"2.0","method":"dehydrate","params":{...},"id":1}`.
4. Sends the request, awaits the response, and passes the result to dependent nodes.

Primals are agnostic to who invokes them; they expose JSON-RPC methods, and biomeOS routes capability calls to the correct primal based on configuration and discovery.

---

## Summary

| Component | Crate | Role |
|-----------|-------|------|
| Graph parsing | biomeos-graph | TOML → DeploymentGraph, topological sort |
| Transactional execution | biomeos-atomic-deploy | GraphExecutor: phases, parallel, rollback |
| Continuous execution | biomeos-graph | ContinuousExecutor: TickClock, SessionState, feedback, budget |
| Capability routing | biomeos-atomic-deploy + config | capability_registry.toml → primal method |
| Wire protocol | All | JSON-RPC 2.0 |

---

*"The graph is the contract. Primals fulfill it."*
