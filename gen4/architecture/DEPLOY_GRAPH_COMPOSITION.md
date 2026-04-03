# Deploy Graph Composition — The gen4 Deployment Surface

**Date:** April 3, 2026
**Status:** Active
**Lineage:** gen3 Paper 26 (methodology) -> gen4 (deployment surface)
**License:** AGPL-3.0-or-later

---

## What This Document Is

gen3 Paper 26 documents the *science* of primal composition — typed deploy graphs,
validation experiments, gap discovery. This document describes the *deployment
surface* that science enables: how deploy graphs become the interface between
infrastructure (primals) and products (gardens), and how the BYOB schema becomes
the contract that makes gen4 products possible.

---

## 1. Deploy Graphs as Product Interface

### 1.1 The gen3 -> gen4 Transition

In gen3, deploy graphs are test fixtures. primalSpring validates that biomeOS
can boot Tower + Nest + Node. ludoSpring validates that 12 primals compose for
game science. The graphs exist to prove the infrastructure works.

In gen4, deploy graphs are **the product interface**. esotericWebb's
`PrimalLauncher` reads TOML deploy graphs, topologically sorts dependencies,
spawns binaries, polls for readiness, and injects live connections into the
`PrimalBridge`. The graph IS the deployment — not a test of deployment.

### 1.2 The BYOB Schema

"Bring Your Own Binaries" — the BYOB deploy graph schema standardized in
`wateringHole/BYOB_DEPLOY_GRAPH_SCHEMA.md`:

```toml
[graph]
name = "my_product"
description = "What this composition does"

[[graph.node]]
name = "biomeOS"
binary = "biomeos"
order = 0
required = true
capabilities = ["lifecycle.register", "graph.execute"]

[[graph.node]]
name = "rhizoCrypt"
binary = "rhizocrypt"
order = 1
depends_on = ["biomeOS"]
health_method = "health.check"
by_capability = "dag.session.create"
capabilities = ["dag.session.create", "dag.event.append"]
```

Every gen4 product ships a BYOB deploy graph. The graph declares *what* the
product needs (capabilities, dependencies, startup order). biomeOS handles
*how* to schedule, route, and monitor execution.

### 1.3 Topological Waves

Nodes group into waves by dependency depth. Wave 0 boots first (biomeOS), wave 1
boots after wave 0 is healthy, etc. This is the same `topological_waves()`
algorithm that ludoSpring and primalSpring independently implement — proving the
schema is self-consistent without shared code.

---

## 2. Session-as-Primal — Ephemeral biomeOS Citizens

### 2.1 The Pattern

sourDough's `PrimalLifecycle` traits scaffold ephemeral primals. biomeOS manages
their lifecycle (spawn, health, teardown). rhizoCrypt DAGs outlive runtime.

In gen4 terms: a game session is an ephemeral primal. An NPC is an ephemeral
primal. A multiplayer match is an ephemeral primal. A mod is an ephemeral
primal. Each has:

- A biomeOS identity (registered, discoverable, health-checked)
- A rhizoCrypt DAG (actions traced, content-addressed)
- A loamSpine certificate (session state anchored at milestones)
- A sweetGrass attribution chain (who created what)

### 2.2 Why This Matters for gen4

The session-as-primal pattern means gen4 products do not need custom session
management. biomeOS already knows how to manage entities. sourDough already
knows how to scaffold them. The provenance trio already knows how to trace
them.

A CRPG session, a genomics pipeline run, a health dashboard viewing session,
and a creative studio project are all ephemeral primals — different domains,
same infrastructure, same lifecycle.

---

## 3. Proto Sketch Taxonomy

### 3.1 How Springs Feed Gardens

Springs validate compositions and produce proto deploy graph sketches for
gardens to absorb. The taxonomy:

```
primalSpring
    |-- proto graphs for springs (structural: Tower, Nest, Node, NUCLEUS)
    |
ludoSpring
    |-- proto graphs for gardens (domain: save, session, narration, viz, render)
    |
esotericWebb (garden)
    |-- absorbs both, adapts to product context, evolves independently
```

### 3.2 What a Proto Sketch Contains

Each proto sketch is a TOML file with:
- Graph structure (nodes, dependencies, capabilities)
- Comments linking back to the validating experiment
- Addresses marking which gaps the sketch resolves
- Suggested adaptations for the absorbing product

The garden reads the sketch, understands the validated pattern, adapts it
to their product needs, and ships it as a production deploy graph.

### 3.3 The Seven Garden Patterns

ludoSpring V18 provides seven domain patterns for esotericWebb:

| Pattern | What the garden gets |
|---------|---------------------|
| Sovereign Save | Save files as signed provenance chains |
| Session-as-Primal | Game sessions as ephemeral biomeOS citizens |
| Attributed Narration | AI text with provable ORC/CC-BY-SA attribution |
| Science Overlay | Live flow/DDA dashboard during gameplay |
| Sovereign Render | Hardware-aware GPU pipeline |
| Multiplayer Provenance | Multi-gate sessions with shared DAGs |
| Creative Studio | Visual content authoring with certified packs |

Plus 2 validation patterns (sovereign save validation, full composition
validation).

---

## 4. The Ecosystem Evolution Map

### 4.1 Composition as Discovery

Every composition experiment is a gap discovery tool. When ludoSpring
validates "sovereign save" (exp073), it discovers that rhizoCrypt needs UDS
support, loamSpine needs stable startup, and biomeOS needs graph executor
endpoints. These are not failures — they are the ecosystem's evolution tasks.

### 4.2 Per-Layer Task Distribution

The evolution map (`ludoSpring/specs/ECOSYSTEM_EVOLUTION_MAP.md`) distributes
tasks to their natural owners:

**Primals (upstream):** Implement missing capabilities. biomeOS absorbs
`[[graph.node]]` ingestion. Squirrel adds NPC cert constraints. petalTongue
adds dialogue scenes. Provenance trio completes UDS/stability work.

**Springs (midstream):** Validate new primal capabilities. Produce updated
proto sketches. Discover new gaps. Refine the BYOB schema.

**Gardens (downstream):** Absorb proto sketches. Ship products. Report
usability gaps that feed back into spring experiments.

**Cross-cutting (wateringHole):** Standardize schemas. Document protocols.
Maintain the BYOB deploy graph specification.

### 4.3 The Feedback Loop

```
primalSpring (structural validation)
       |
       v
ludoSpring (domain composition, gap discovery)
       |
       v
esotericWebb (product absorption, usability feedback)
       |
       v
wateringHole (schema refinement, protocol standards)
       |
       v
biomeOS + primals (capability evolution)
       |
       v
primalSpring (validate new capabilities)
       ... (repeat)
```

This is the gen4 flywheel. Each revolution produces:
- More validated compositions
- More evolved primals
- More capable products
- More refined standards

---

## 5. The Sovereignty Guarantee

### 5.1 No Shared Crates

The BYOB schema is a wateringHole standard — a document, not a dependency.
biomeOS, primalSpring, ludoSpring, and esotericWebb each parse it independently.
This guarantees:

- A primal version bump never breaks a garden build
- A spring experiment never pollutes primal code
- A garden can ship without waiting for spring releases

### 5.2 IPC as the Only Interface

All composition happens over JSON-RPC 2.0 (Unix sockets or TCP). There are
no Cargo `[dependencies]` between layers for composition logic. The wire
format IS the contract.

### 5.3 Independent Evolution Timelines

biomeOS can add graph executors while ludoSpring experiments with new
compositions while esotericWebb ships a playable demo. No coordination
required beyond wateringHole handoffs.

---

## 6. Relationship to Other gen4 Papers

| Paper | Relationship |
|-------|-------------|
| COMPOSITION_PATTERNS.md | PrimalBridge patterns (gen4 consumer perspective) |
| CREATIVE_SURFACE_ARCHITECTURE.md | sporeGarden org model (where gardens live) |
| BIOMEOS_OS_TRAJECTORY.md | biomeOS as OS (where deploy graphs lead) |
| ESOTERIC_WEBB.md | First garden (where proto sketches land) |
| gen3 Paper 26 | The science behind this deployment surface |
| gen3 Paper 23 | NUCLEUS model (the structural foundation) |

---

## 7. What This Enables

Deploy graph composition is the mechanism that makes the gen3 -> gen4 transition
concrete. It answers: "how does validated science become a product someone uses
without knowing about primals?"

The answer: through a TOML file that declares capabilities, a launcher that
spawns binaries, a bridge that injects connections, and a runtime that
orchestrates everything via IPC. The developer writes a deploy graph. The
infrastructure handles the rest.

This is the GarageBand moment for sovereign computing: the complexity
disappears behind a declarative surface. The primals are the instruments.
The deploy graph is the sheet music. The product is the song.

---

*gen3 proved the instruments are in tune. gen4 asks: what music will people
make with them? The deploy graph is how they start playing.*
