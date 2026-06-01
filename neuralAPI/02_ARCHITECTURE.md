# Atomic Decomposition Architecture — Tower/Node/Nest/NUCLEUS as Addressable Units

**The composition collapse: from 427 methods to atomic compositions**

**Date**: June 1, 2026 (updated Wave 66 — Phase A complete)
**Status**: Architecture Specification — Phase A implemented, Phases B-D remain
**Depends on**: Phase 32 atomic model, Dark Forest Glacial Gate, biomeOS v3.50+
**Vocabulary**: `gen5/foundations/FUNCTIONAL_PATTERN_CONVERGENCE.md`

> **Note on terminology**: This document uses "signal" and "composition"
> interchangeably at the code level — the API method is `signal.dispatch()`,
> but the operation is biomeOS **composition dispatch**: decomposing a
> high-level operation into a graph of primal capability calls. See
> `FUNCTIONAL_PATTERN_CONVERGENCE.md` for the canonical vocabulary.

---

## The Problem: Combinatorial Surface

The ecoPrimals ecosystem has evolved to 13 primals exposing 427 registered
capability methods across 15 domains. Each spring must understand:

- Which primal owns which capability domain
- How to route calls through `CompositionContext`
- Which primals must coordinate for compound operations
- How to handle partial availability (optional primals)
- Dark Forest security invariants (BTSP, ports, metadata)

This produces an N×M surface where N springs each manage M primal
connections. At 8 springs × 13 primals = 104 connection edges, each
potentially involving multiple methods. The routing table in
`primalSpring/ecoPrimal/src/composition/routing.rs` already maps
40+ method prefixes to 15 capability domains.

**This surface does not scale.** Every new primal, method, or spring
multiplies the edges. Every new emergent system (RootPulse, RPGPT,
Barrick pipelines) adds another coordination pattern that each spring
must learn.

---

## The Solution: Atomic Composition Layer

Insert a **decomposition layer** between springs and individual primals.
Springs address **composition tiers** (Tower, Node, Nest, NUCLEUS), not
individual primals. biomeOS's Neural API decomposes atomic compositions
into the correct sequence of primal-level capability calls.

```
BEFORE (direct routing):

  spring ──► routing table ──► bearDog
  spring ──► routing table ──► songbird
  spring ──► routing table ──► skunkBat
  spring ──► routing table ──► toadStool
  spring ──► routing table ──► ...

AFTER (atomic signals):

  spring ──► "tower.publish" ──► Neural API ──┬──► bearDog.crypto.sign
                                              ├──► songbird.beacon.announce
                                              └──► skunkBat.audit.log_event
```

The spring sends one signal. biomeOS executes a small graph. The spring
gets back a composed result.

---

## Phase 32 Atomic Tiers

Each tier is a stable composition that has been validated across the
entire ecosystem. The Phase 32 model is canonical in
`plasmidBin/manifest.toml` under `[atomics.*]`.

### Tier 1: Tower (electron)

**Trust boundary** — the minimal composition for authenticated operation.

| Primal | Role | Key Methods |
|--------|------|------------|
| bearDog | Crypto, identity, TLS, BTSP | `crypto.sign`, `btsp.negotiate`, `tls.handshake`, `identity.resolve` |
| songbird | Discovery, network, relay | `beacon.announce`, `discovery.find`, `relay.establish`, `mesh.join` |
| skunkBat | Defense, audit, threat detection | `audit.log_event`, `defense.verify_lineage`, `threat.assess`, `recon.scan` |

**Dark Forest compliance**: The Tower is the enforcement point for all
5 pillars of the Dark Forest Glacial Gate. Zero metadata leakage (bearDog
strips binaries, songbird encrypts beacons), zero port exposure (UDS-only
default), songbird as sole network surface, BTSP crypto integrity, and
skunkBat audit coverage.

**Tower signals**:

| Signal | Decomposition Graph | Coordination |
|--------|-------------------|:------------:|
| `tower.authenticate` | btsp.negotiate → defense.verify_lineage | Sequential |
| `tower.publish` | crypto.sign → beacon.announce → audit.log_event | Sequential |
| `tower.discover` | discovery.find → crypto.verify_peer → audit.log_event | Sequential |
| `tower.secure_channel` | tls.handshake → relay.establish → threat.assess | Sequential |
| `tower.health` | health.liveness (all 3, parallel) | Parallel |

### Tier 2: Node (proton)

**Compute substrate** — Tower + the compute trio.

| Primal | Role | Key Methods |
|--------|------|------------|
| Tower (3) | Trust boundary | (inherited) |
| toadStool | GPU/CPU dispatch, orchestration | `compute.dispatch`, `workload.validate`, `toadstool.list_workloads` |
| barraCuda | Math engine, tensors, shaders | `tensor.matmul`, `stats.mean`, `linalg.solve`, `spectral.fft` |
| coralReef | Shader compilation, SPIR-V | `shader.compile`, `shader.compile.gemm`, `shader.compile.module` |

**Node signals**:

| Signal | Decomposition Graph | Coordination |
|--------|-------------------|:------------:|
| `node.compute` | tower.authenticate → compute.dispatch → shader.compile → tensor.execute | Sequential |
| `node.validate` | workload.validate → validate.result | Sequential |
| `node.compile` | shader.compile → (cache in nestGate if Nest available) | Sequential |
| `node.health` | tower.health + compute trio health (parallel) | Parallel |

### Tier 3: Nest (neutron)

**Storage + provenance** — Tower + the provenance trio + NestGate.

| Primal | Role | Key Methods |
|--------|------|------------|
| Tower (3) | Trust boundary | (inherited) |
| nestGate | Content-addressed storage | `content.put`, `content.get`, `storage.store` |
| rhizoCrypt | Ephemeral DAG, sessions | `dag.session.create`, `dag.dehydrate`, `dag.event.append` |
| loamSpine | Immutable linear history | `spine.commit`, `proof.verify`, `entry.get` |
| sweetGrass | Attribution, PROV-O braids | `braid.create`, `provenance.query`, `contribution.record` |

**Nest signals**:

| Signal | Decomposition Graph | Coordination |
|--------|-------------------|:------------:|
| `nest.store` | tower.authenticate → content.put → dag.event.append → spine.commit → braid.create | Sequential |
| `nest.retrieve` | content.get → dag.session.get → provenance.query | Parallel |
| `nest.verify` | proof.verify → crypto.verify → provenance.validate | Sequential |
| `nest.commit` | dag.dehydrate → crypto.sign → content.put → spine.commit → braid.create | Sequential (RootPulse flow) |
| `nest.health` | tower.health + provenance trio + nestGate health (parallel) | Parallel |

### Tier 4: NUCLEUS (atom)

**Full composition** — Node + Nest (10 unique primals).

| Signal | Decomposition |
|--------|--------------|
| `nucleus.deploy` | graph.execute over the full atomic deploy graph |
| `nucleus.status` | biomeos.spring_status + topology.get + per-primal health |
| `nucleus.provision` | tower.authenticate → node.health → nest.health → graph.deploy |

### Meta-Tier

**Cross-atomic** — biomeOS + squirrel + petalTongue. These operate at
all levels and don't form a strict tier; they are the orchestration,
AI, and UI surfaces that wrap atomic operations. Unlike foundation
tiers, meta-tier signals *compose* other signals rather than decomposing
into direct primal calls.

| Primal | Role | Key Methods |
|--------|------|------------|
| biomeOS | Orchestration, graph execution | `graph.execute`, `capability.call`, `composition.reload` |
| squirrel | AI coordination, inference, agentic planning | `ai.query`, `ai.complete`, `squirrel.context.push`, `mcp.tools.list` |
| petalTongue | UI, visualization, interaction capture | `visualization.render`, `visualization.session.create`, `interaction.poll` |

**Meta-tier signals**:

| Signal | Decomposition Graph | Coordination |
|--------|-------------------|:------------:|
| `meta.observe` | visualization.session.create → squirrel.context.push → graph.list | Sequential |
| `meta.intent` | interaction.poll → ai.query → graph.execute | Sequential |
| `meta.render` | graph.status → ai.complete → viz.render | Sequential |
| `meta.health` | health.liveness (all 3, parallel) | Parallel |

---

## Meta-Tier Signal Layer: Agentic Composition Collapse

The meta-tier signal layer solves a problem that foundation signals
alone cannot: **making the signal surface machine-legible for agentic
AI**. An LLM agent (squirrel) cannot reason effectively over 427
methods across 13 primals. But it *can* reason over ~12 atomic signals
across 4 tiers plus meta. The composition collapse creates a tool-use
schema that squirrel can ingest and plan over.

### The Ecological Loop

The meta-tier signals define a complementary cycle:

```
  Intent (forward):     petalTongue → squirrel → biomeOS → primals
  Render (backward):    primals → biomeOS → squirrel → petalTongue

  User says: "publish my analysis"
  petalTongue:  captures intent, sends structured action
  squirrel:     reads signal_tools.toml, plans [tower.publish, nest.store]
  biomeOS:      executes tower.publish graph (3 primal calls)
                executes nest.store graph (4 primal calls)
  squirrel:     summarizes "Published with provenance CID abc..."
  petalTongue:  renders narrative + dashboard to user
```

**Collapse ratio**: User says 1 thing. petalTongue sends 1 intent.
squirrel plans 2 signals. biomeOS executes 7 primal calls.
The user never names a primal.

### Signal Tool Schema

The key enabler is `config/signal_tools.toml` — a TOML file that maps
every atomic signal into a tool-use schema squirrel can ingest via
`squirrel.context.push`. Each tool entry includes:

- `name`: tier.signal identifier matching `[signals.*]` in the registry
- `tier`: atomic tier (tower/node/nest/meta)
- `description`: human/LLM-readable summary for reasoning
- `parameters`: named inputs with types
- `returns`: description of composed output
- `primals`: which primals participate (squirrel never calls these directly)

This schema is effectively an MCP tool manifest. squirrel already owns
`mcp.tools.list` — the signal tool schema can be surfaced through
that existing interface, providing agentic capabilities without
inventing a new protocol.

### `signal_plan()` and `execute_plan()`

`CompositionContext` provides two new methods for agentic dispatch:

- **`signal_plan(intent, context)`**: Sends user intent to squirrel's
  `ai.query` with the signal tool schema context. squirrel returns an
  ordered list of (tier, signal, params) tuples.

- **`execute_plan(plan)`**: Takes squirrel's plan and dispatches each
  step sequentially through `signal()`. Collects results into a JSON
  array. On failure, returns partial results up to the failing step.

Springs that want full agentic behavior call:
```
let plan = ctx.signal_plan("publish my analysis", context)?;
let results = ctx.execute_plan(&plan)?;
ctx.signal("meta", "render", results)?;
```

Springs that want direct signal dispatch still call:
```
ctx.signal("tower", "publish", payload)?;
```

Both paths go through the same graph executor in biomeOS.

### What This Unlocks

- **squirrel becomes agentic**: it can plan multi-signal workflows
  from user intent using the signal tool schema
- **petalTongue becomes semantic**: it captures intent, not raw
  method calls
- **biomeOS stays mechanical**: it executes graphs, doesn't need
  to understand intent
- **Springs get simpler**: they call `signal("meta", "intent", ...)`
  for anything complex
- **MCP convergence**: the signal tool schema is an MCP tool manifest
  in TOML form

---

## Signal Dispatch Mechanism

### How `capability.call("tower", "publish", payload)` works

1. **Spring** calls `NeuralBridge::capability_call("tower", "publish", &payload)`.

2. **NeuralBridge** sends JSON-RPC to biomeOS:
   ```json
   {"jsonrpc":"2.0","method":"capability.call","params":{
     "capability":"tower","operation":"publish","args":{...}
   },"id":1}
   ```

3. **NeuralRouter** in biomeOS checks the signal registry:
   - `tower.publish` maps to graph `tower_publish.toml`
   - This is a **signal**, not a single-method dispatch

4. **GraphExecutor** loads and executes `tower_publish.toml`:
   ```toml
   [graph]
   id = "tower_publish"
   coordination = "Sequential"

   [[graph.nodes]]
   id = "sign"
   capability = "crypto.sign"
   depends_on = []

   [[graph.nodes]]
   id = "announce"
   capability = "beacon.announce"
   depends_on = ["sign"]

   [[graph.nodes]]
   id = "audit"
   capability = "audit.log_event"
   depends_on = ["announce"]
   ```

5. **Result** flows back to the spring as a single composed response.

### Fallback to direct dispatch

If a `capability.call` targets a non-atomic capability (e.g.,
`"tensor"`, `"storage"`), the NeuralRouter falls through to
direct single-method dispatch as it does today. Atomic signals
are an additive layer, not a replacement for direct routing.

---

## Signal Graph Requirements

Each atomic signal is backed by a small TOML graph. Requirements:

1. **Nodes reference capabilities, not primals** — the graph says
   `capability = "crypto.sign"`, not `primal = "beardog"`. The router
   resolves at runtime.

2. **Data flows between nodes** — `depends_on` edges carry the previous
   node's output as the next node's input. The graph executor manages
   the `ExecutionContext`.

3. **Dark Forest compliant** — signal graphs inherit the Dark Forest
   invariants: BTSP on every edge, no cleartext fallback, skunkBat
   audit on every composition.

4. **Optional nodes** — a signal graph can mark nodes as optional
   (e.g., `nest.store` can skip `braid.create` if sweetGrass is
   unavailable). Optional nodes that fail are logged, not fatal.

5. **Composable** — `nest.commit` can internally call `tower.authenticate`
   as a subgraph, inheriting its BTSP state.

---

## Decomposition vs Composition

The atomic model has always described **composition** — how primals
combine into larger units. The Neural API adds **decomposition** — how
high-level operations break down into primal-level calls.

```
                     COMPOSITION (bottom-up)
                     how primals build into units

   bearDog ──┐
   songbird ──┼── Tower ──┐
   skunkBat ──┘           │
                          ├── NUCLEUS
   toadStool ──┐          │
   barraCuda ──┼── Node ──┤
   coralReef ──┘          │
                          │
   nestGate ────┐         │
   rhizoCrypt ──┼── Nest ─┘
   loamSpine ───┤
   sweetGrass ──┘


                     DECOMPOSITION (top-down)
                     how signals break into calls

   nucleus.deploy ──┐
                    ├── tower.authenticate ──┬── btsp.negotiate
                    │                        └── defense.verify_lineage
                    ├── node.compute ──┬── compute.dispatch
                    │                  ├── shader.compile
                    │                  └── tensor.execute
                    └── nest.store ──┬── content.put
                                    ├── dag.event.append
                                    ├── spine.commit
                                    └── braid.create
```

Both directions use the same atomic model. Composition tells you what
runs together. Decomposition tells you what happens when you invoke
the unit.

---

## Coverage Metrics

### Signal coverage target

The 427 registered methods fall into these capability domains:

| Domain | Owner | Methods | Atomic Tier |
|--------|-------|--------:|:-----------:|
| security | bearDog | 45 | Tower |
| discovery | songbird | 38 | Tower |
| defense | skunkBat | 12 | Tower |
| compute | toadStool | 18 | Node |
| tensor | barraCuda | 89 | Node |
| shader | coralReef | 15 | Node |
| storage/content | nestGate | 22 | Nest |
| dag | rhizoCrypt | 28 | Nest |
| ledger | loamSpine | 19 | Nest |
| commit/attribution | sweetGrass | 16 | Nest |
| orchestration | biomeOS | 42 | Meta |
| ai/inference | squirrel | 14 | Meta |
| visualization | petalTongue | 11 | Meta |
| tool (primalSpring) | primalSpring | 48 | Coordination |
| other (springs) | various | 30 | Domain-specific |

**Goal**: Define atomic signals that cover the 10-15 most common
composition patterns. Springs that need the remaining methods can
still call capability domains directly. The signals are a convenience
layer, not a restriction.

### Validation via primalSpring

New scenario `s_atomic_signals` (proposed) would validate:

- Every defined signal graph parses and resolves to valid capabilities
- Signal decompositions cover the declared primals in their tier
- Signal results compose correctly (output of node N feeds node N+1)
- Dark Forest invariants hold for every signal path
- Fallback to direct dispatch works for non-signal capabilities

---

## Relationship to Existing Infrastructure

| Component | What It Does Today | What Signals Add |
|-----------|-------------------|-----------------|
| `routing.rs` | Maps capabilities → primals | Unchanged — signals are an upper layer |
| `NeuralBridge` | Client to biomeOS neural-api socket | Unchanged — signals are just capability.call with tier names |
| `CompositionContext` | Per-domain `call()` method | New: `signal("tower", "publish", ...)` method |
| `EmergentSystem` | RootPulse, RPGPT graph names | Signals are finer-grained — below emergent systems |
| `capability_registry.toml` | 427 method → owner mapping | New: `[signals]` section mapping signal names → graph files |
| `s_routing_consistency` | Validates method → domain → primal | Extended: also validates signal → graph → capabilities |

---

## Bootstrap Paradox and Two-Phase Startup

### The Problem

The atomic signal layer assumes biomeOS is running to execute graphs.
But biomeOS is *itself* a composition that depends on Tower primals for
discovery (songbird), crypto identity (bearDog), and audit (skunkBat).
This is the **bootstrap paradox**: you need Tower to run graphs, but
the graph infrastructure lives in biomeOS which needs Tower to start.

The cellMembrane deployment (a fieldMouse Tower on external VPS
substrate) exposed real consequences of this paradox:

- `bootstrap_gate.sh` uses **inline `sleep 2`** between primal starts
  instead of health-probed dependency ordering
- `deploy_gate.sh` generates shell scripts with hardcoded sleep
  intervals that fail on slower hosts
- `nucleus_launcher.sh` has rich ordering and Phase 5 songbird registry
  seeding, but Tower bootstrap doesn't use any of it
- Family seed generation falls back to `/dev/urandom` — acceptable
  for isolation, but breaks fleet enrollment assumptions

### Resolution: Two-Phase Bootstrap

The `tower.bootstrap` signal (`graphs/signals/tower_bootstrap.toml`)
defines a declarative two-phase cold-start sequence:

**Phase 1 — Static startup (no biomeOS)**

```
beardog_identity   [order 1, spawn, no dependencies]
  └─► crypto.identity, btsp.handshake

songbird_discovery [order 2, spawn, depends on beardog_identity]
  └─► ipc.register, discovery.announce

skunkbat_audit     [order 3, spawn, depends on beardog_identity]
  └─► security.audit_event, defense.status
```

bearDog is the **root node** — it has no dependencies because it
provides the crypto substrate that everything else requires. songbird
and skunkBat both depend on bearDog but are independent of each other;
a future optimization could parallelize their startup.

Phase 1 requires no biomeOS, no graph executor, no signal dispatch.
A minimal bootstrap binary (or even a shell script) can parse
`tower_bootstrap.toml` and spawn primals in dependency order, replacing
`sleep 2` with health-probe readiness checks against each primal's
`health.liveness` method.

**Phase 2 — Graph-driven expansion (biomeOS available)**

```
biomeos_discover   [order 4, optional, depends on songbird_discovery]
  └─► graph.list, topology.rescan

registry_seed      [order 5, optional, depends on biomeos_discover]
  └─► ipc.register (seeds all Tower primals into biomeOS's view)

health_verify      [order 6, optional, depends on registry_seed]
  └─► health.liveness (composed Tower health check)
```

Once Tower is running, biomeOS can discover it via songbird and seed
the registry. From this point forward, all operations use the signal
layer. The Phase 2 nodes are marked `required = false` because a
Tower can operate indefinitely without biomeOS (the cellMembrane
deployment does exactly this).

### Primal Role Sharing

The two-phase model reveals an important architectural property:
**a single Tower can serve multiple compositions simultaneously**.

The IPC layer already supports this — `discover_by_capability("discovery")`
finds whatever socket provides that capability, regardless of which
composition "owns" the primal. bearDog is the same bearDog whether
it's serving a Tower, a Node, a Nest, or all three at once.

This is visible in the signal layer where skunkBat, a Tower primal,
participates in `meta.deploy` — a meta-tier signal. skunkBat doesn't
"leave" the Tower to serve the meta-tier; it provides its `defense`
capability to any composition that requests it.

**Implications for deployment**:

- A NUCLEUS doesn't need 10 primal processes — it needs Tower (3)
  + compute trio (3) + provenance trio (4) + nestGate (1), but Tower
  is shared, not duplicated
- A fieldMouse deployment runs one Tower and layers compositions on
  top as resources allow
- Fleet enrollment via songbird mesh means a running Tower can
  discover and enroll new deployments, seeding their identity via
  bearDog's `crypto.family_seed`

### Lessons from cellMembrane / fieldMouse

| Lesson | Shell Script Problem | Graph-Driven Solution |
|--------|---------------------|----------------------|
| Startup ordering | `sleep 2` between primals | `depends_on` edges with health probes |
| Dependency declaration | Implicit in script order | Explicit in graph TOML |
| Optional components | Not supported | `required = false` on Phase 2 nodes |
| Fleet enrollment | Manual `/dev/urandom` seeds | bearDog `crypto.family_seed` via songbird mesh |
| Health verification | Hoped for the best | `tower.health` signal post-bootstrap |
| Documentation | Comments in bash | Parseable, validatable TOML graph |

### Stadial Goals

The interstadial `tower.bootstrap` signal creates the documentation
and validation infrastructure. Full resolution of the bootstrap
paradox requires stadial work:

- **biomeOS bootstrap mode**: A minimal biomeOS mode that can execute
  `tower.bootstrap` graphs without needing Tower to already exist
- **Primal multiplexing in CompositionContext**: Adding a composition
  dimension so `ctx.call("security", ...)` routes to the correct
  bearDog instance by composition scope
- **Fleet enrollment via songbird mesh**: A running Tower discovers
  and enrolls new fieldMouse deployments via songbird federation
- **projectNUCLEUS convergence**: Replace `nucleus_launcher.sh` with
  graph-driven deployment using the signal layer

---

## Implementation Path

### Phase A: Composition Definition (primalSpring) — COMPLETE

1. ~~Define Tower/Node/Nest/Meta/Ecosystem composition graphs~~ — **32 graphs** in `graphs/signals/`
2. ~~Add `[signals]` section to `capability_registry.toml`~~ — all 6 tiers registered
3. ~~Add `s_atomic_signals` scenario~~ — validates all 32 graphs structurally
4. ~~Add `CompositionContext::signal()` method~~ — dispatches to orchestration via capability.call
5. ~~Create `config/signal_tools.toml`~~ — tool-use schema for squirrel's agentic planning
6. ~~Add `s_meta_tier_signals` scenario~~ — validates meta-tier intent loop, routing, tool schema coverage
7. ~~Add `signal_plan()` + `execute_plan()` to CompositionContext~~ — agentic dispatch methods
8. ~~Define agentic sync compositions~~ — `sync_diverge`, `sync_resolve`, `sync_resolve_crossgate`

### Phase B: Composition Dispatch (biomeOS)

1. Extend NeuralRouter to recognize signal-tier capabilities (`tower`, `node`, `nest`, `nucleus`, `meta`)
2. On signal dispatch, load and execute the corresponding graph instead of single-method routing
3. Compose graph results into a single response
4. Wire `signal_tools.toml` into squirrel's `mcp.tools.list` response

### Phase C: Composition Adoption (springs)

1. Springs can migrate gradually: `call("security", "crypto.sign", ...)` still works
2. New code prefers `signal("tower", "publish", ...)` where applicable
3. Agentic flows use `signal_plan()` + `execute_plan()` for multi-signal orchestration
4. petalTongue captures intent as structured actions, not raw API calls

### Phase D: Composition Learning (biomeOS)

1. PathwayLearner observes signal execution traces
2. Discovers parallelization within signal graphs (e.g., `nest.store` can parallelize sweetGrass + nestGate)
3. Suggests and applies optimizations automatically
4. Squirrel learns to optimize signal plans from execution results

---

*"The atom is not 13 primals. It is one composition, decomposed. And the*
*agent sees not 427 methods, but 32 tools."*
