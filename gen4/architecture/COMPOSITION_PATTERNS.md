# Composition Patterns

**How Primals Become Invisible Infrastructure in gen4 Products**

**Date**: March 24, 2026
**Lineage**: esotericWebb V4 → gen3/ECOSYSTEM_ARCHITECTURE → gen3/baseCamp/18 (RPGPT)

---

## The Composition Thesis

gen3 proved primals compute correctly. gen4 composes them into products
where the consumer never sees a primal. The consumer sees a game, a
health dashboard, a field genomics kit. The primals are the plumbing.

This document captures the composition patterns discovered while
building esotericWebb V4 — the first gen4 product. These patterns are
not theoretical; they run in production Rust code with 166 tests.

---

## I. The Dual Surface

Every gen4 product has two interaction surfaces:

```
┌─────────────────────────────────────────────┐
│              Creator Surface                │
│  (YAML content, TOML config, CLI tools)     │
│                                             │
│  "I write rooms, NPCs, abilities, rules."   │
│  "I run validate, preview, graph."          │
│  "I never touch Rust."                      │
├─────────────────────────────────────────────┤
│             Developer Surface               │
│  (Rust crate, PrimalBridge, deploy graphs)  │
│                                             │
│  "I extend the engine."                     │
│  "I add new scene types, new primals."      │
│  "I write Rust."                            │
└─────────────────────────────────────────────┘
```

The creator surface is what makes gen4 a barrier-lowering generation.
The developer surface is what makes gen4 extensible. Both consume the
same primal infrastructure, but through different interfaces.

esotericWebb's dual surface:

| Surface | Tool | Purpose |
|---------|------|---------|
| Creator | `esotericwebb new-world` | Scaffold a world from templates |
| Creator | `esotericwebb validate` | Lint content YAML against rulesets |
| Creator | `esotericwebb preview` | Run text-mode playthrough |
| Creator | `esotericwebb graph` | Visualize narrative DAG |
| Creator | `esotericwebb export` | Package for distribution |
| Developer | `PrimalBridge` | Wire new primals via JSON-RPC |
| Developer | `GameSession::act()` | Extend the composition pipeline |
| Developer | Deploy graph TOML | Define primal topology |

---

## II. The PrimalBridge Pattern

### Core Principle

A gen4 product communicates with primals exclusively via JSON-RPC 2.0
over TCP (or Unix domain sockets). It never imports a primal crate. It
never links a primal binary. The bridge is the only contact surface.

### Bridge Architecture

```
gen4 product (esotericWebb)
    │
    ├── PrimalBridge
    │     ├── connection pool (TCP/UDS per primal)
    │     ├── capability cache (discovered via Songbird)
    │     ├── retry + circuit breaker per method
    │     └── graceful degradation (sensible defaults)
    │
    └── plasmidBin/ (deployed primal binaries)
          ├── rhizoCrypt (dag.*)
          ├── loamSpine (certificate.*)
          ├── sweetGrass (attribution.*)
          ├── Squirrel (ai.*)
          ├── petalTongue (visualization.*, interaction.*)
          ├── ludoSpring (game.*)
          ├── toadStool (compute.*)
          └── nestGate (storage.*)
```

### Bridge Methods

The SEMANTIC_METHOD_NAMING_STANDARD governs all method names:

```
{domain}.{resource}.{action}
```

Examples from esotericWebb V4:

| Method | Domain | What it does |
|--------|--------|-------------|
| `game.evaluate_flow` | ludoSpring | Evaluate flow state from metrics |
| `game.npc_dialogue` | ludoSpring | Generate NPC dialogue with rules |
| `game.narrate_action` | ludoSpring | Narrate player action with style |
| `game.voice_check` | ludoSpring | Voice detection check for NPC |
| `game.push_scene` | ludoSpring | Push scene state to game engine |
| `game.begin_session` | ludoSpring | Start game session |
| `game.complete_session` | ludoSpring | End game session |
| `ai.chat` | Squirrel | Narration fallback / general AI |
| `ai.summarize` | Squirrel | Summarize narrative state |
| `visualization.render.scene` | petalTongue | Render scene to display |
| `interaction.poll` | petalTongue | Poll for player input |
| `dag.session.create` | rhizoCrypt | Create provenance session |
| `dag.event.append` | rhizoCrypt | Append event to session DAG |
| `dag.session.complete` | rhizoCrypt | Complete and seal session |
| `dag.frontier.get` | rhizoCrypt | Get current frontier vertices |
| `dag.merkle.root` | rhizoCrypt | Compute Merkle root of session |
| `dag.query.vertices` | rhizoCrypt | Query vertices by predicate |
| `certificate.mint` | loamSpine | Mint personality/ownership cert |
| `compute.dispatch.submit` | toadStool | Submit GPU compute job |
| `storage.store` | nestGate | Store key-value pair |
| `storage.retrieve` | nestGate | Retrieve value by key |
| `attribution.record` | sweetGrass | Record attribution braid |

23 methods across 8 domains. Every method degrades gracefully — if the
primal is unreachable, the bridge returns a sensible default. The
product never crashes because a primal is absent.

---

## III. Graceful Degradation (The Resilience Pattern)

### The Rule

**No primal is required. Every primal is beneficial.**

A gen4 product must run — with reduced capability — even if zero
primals are available. This means every bridge call has a fallback:

```
[attempt ludoSpring game.narrate_action]
    ↓ success? → use ludoSpring narration
    ↓ fail?
[attempt Squirrel ai.chat as fallback]
    ↓ success? → use AI narration
    ↓ fail?
[use local template narration]
    ↓ always succeeds → product continues
```

### Degradation Tiers

| Tier | Available primals | Product capability |
|------|-------------------|-------------------|
| Full | All 8 domains | Rich narration, provenance, attribution, flow, rendering |
| Partial | ludoSpring + rhizoCrypt | Game science + provenance, local rendering, template AI |
| Minimal | rhizoCrypt only | Provenance tracking, everything else templated |
| Standalone | None | Pure local operation, YAML-driven, text-mode |

The standalone tier is critical: it means a creator can develop content
on a laptop with no network, no primals, no GPU. The primals enrich the
experience; they don't gatekeep it.

### Circuit Breaker

Each bridge method tracks consecutive failures. After N failures
(configurable, default 3), the circuit opens and the bridge stops
attempting that method for a cooldown period. This prevents cascade
failures where a single unresponsive primal blocks the entire
composition pipeline.

---

## IV. Deploy Graph Pattern

### The Problem

Primals have dependencies. rhizoCrypt needs to be running before
esotericWebb can create a session. Squirrel needs to be running before
esotericWebb can request narration. Some primals need other primals
(Songbird discovers others, BearDog authenticates).

### The Solution

Deploy graphs are TOML files that declare the primal topology:

```toml
[primals.rhizoCrypt]
binary = "plasmidBin/rhizoCrypt/rhizo_crypt"
port = 9100
capabilities = ["dag.session", "dag.event", "dag.merkle"]
depends_on = []

[primals.loamSpine]
binary = "plasmidBin/loamSpine/loam_spine"
port = 9101
capabilities = ["certificate.mint"]
depends_on = ["rhizoCrypt"]

[primals.sweetGrass]
binary = "plasmidBin/sweetGrass/sweet_grass"
port = 9102
capabilities = ["attribution.record"]
depends_on = ["rhizoCrypt", "loamSpine"]

[primals.squirrel]
binary = "plasmidBin/squirrel/squirrel"
port = 9200
capabilities = ["ai.chat", "ai.summarize"]
depends_on = []

[primals.ludoSpring]
binary = "plasmidBin/ludoSpring/ludo_spring"
port = 9300
capabilities = ["game.evaluate_flow", "game.npc_dialogue"]
depends_on = []
```

### PrimalLauncher

The `PrimalLauncher` reads the deploy graph, topologically sorts by
`depends_on`, spawns binaries in wave order, polls TCP readiness, and
injects live connections into the `PrimalBridge`. This is the NUCLEUS
composition model from gen3 instantiated outside a spring.

### Wave Ordering

```
Wave 0: [rhizoCrypt, squirrel, ludoSpring]  (no dependencies)
Wave 1: [loamSpine]                          (depends on rhizoCrypt)
Wave 2: [sweetGrass]                         (depends on rhizoCrypt + loamSpine)
```

Each wave waits for the previous wave's TCP readiness before launching.
Timeout per primal is configurable. If a primal fails to start, the
bridge marks it as unavailable and proceeds — graceful degradation
handles the rest.

---

## V. The Composition Pipeline (`GameSession::act()`)

The heart of esotericWebb is the `act()` method — the composition
pipeline that fires on every player action. This is the pattern for
how gen4 products orchestrate primals:

```
Player action arrives
    │
    ├── 1. ludoSpring: narrate the action (style, voice, world state)
    │     └── fallback: Squirrel ai.chat
    │           └── fallback: local template
    │
    ├── 2. ludoSpring: NPC dialogue (personality cert, knowledge, trust)
    │     └── fallback: template dialogue
    │
    ├── 3. ludoSpring: evaluate flow (engagement, DDA, pacing)
    │     └── fallback: default flow state
    │
    ├── 4. petalTongue: render scene (visual output)
    │     └── fallback: text-mode rendering
    │
    ├── 5. rhizoCrypt: append event to session DAG
    │     └── fallback: local event log
    │
    └── Result: PrimalEnrichment
          ├── narration (text, voice, style)
          ├── npc_dialogue (text, detection hints)
          ├── flow_state (engagement, pacing, DDA adjustment)
          ├── render_result (scene output)
          └── provenance (vertex hash, DAG position)
```

### PrimalEnrichment

The `PrimalEnrichment` struct captures the results of the full
composition. It is a single data object that downstream systems consume.
The game loop doesn't need to know which primals contributed — it gets
a `PrimalEnrichment` and uses whatever fields are populated.

This is the composition result pattern: many primals in, one enrichment
out. The product sees the enrichment, not the primals.

---

## VI. Capability Discovery (Songbird Pattern)

In gen3, primals are wired by configuration. In gen4, primals can be
**discovered by capability**:

1. Product broadcasts: "I need `dag.session.create`"
2. Songbird queries the local biome for primals advertising that
   capability
3. Songbird returns the primal's TCP endpoint
4. PrimalBridge connects and verifies via capability handshake

This means a gen4 product doesn't need to know *which* primal provides
a capability — only that the capability exists somewhere in the biome.
If rhizoCrypt v2 replaces rhizoCrypt v1 with the same capability
surface, the product doesn't change.

The CAPABILITY_BASED_DISCOVERY_STANDARD governs this: primals advertise
capabilities via JSON-RPC `system.capabilities` response. The bridge
matches requested capabilities to available primals.

---

## VII. The Tiered Narration Pattern

esotericWebb discovered a pattern for AI narration that generalizes to
any gen4 product using natural language:

### Tier 1: Domain-Specific Engine (ludoSpring)

The game science engine has context: it knows the ruleset, the NPC
personality certs, the flow state, the narrative phase. Its narration
is contextually rich and rule-constrained.

### Tier 2: General AI (Squirrel)

If the domain engine is unavailable, the general AI model can generate
narration from a prompt. Less context-aware, but still dynamic. Squirrel
routes to the best available model (local or remote, sovereign first).

### Tier 3: Local Templates

If all AI is unavailable, the product falls back to authored templates
— YAML-defined text patterns with variable substitution. Functional,
not dynamic, but the product never stops.

This three-tier pattern (domain → general → template) applies to any
capability: rendering (petalTongue → terminal → text), attribution
(sweetGrass → local log → none), storage (nestGate → filesystem →
memory).

---

## VIII. The Zero-Import Principle

A gen4 product has zero Cargo dependencies on primal crates. It does
not `use rhizo_crypt::*`. It does not link `libsquirrel.so`. The only
interface is JSON-RPC over TCP.

This gives gen4 products several properties:

1. **Language independence**: A gen4 product could be written in Python,
   Go, or TypeScript. The bridge is JSON over TCP.
2. **Version independence**: Primal upgrades don't require product
   recompilation.
3. **Deployment independence**: The product and its primals can run on
   different machines.
4. **License independence**: The product's license is its own. The
   primals' AGPL license applies to the primals, not the product (see
   scyBorg exception protocol).

---

## IX. Pattern Summary

| Pattern | What | Why |
|---------|------|-----|
| Dual surface | Rust + YAML | Barrier lowering for creators |
| PrimalBridge | JSON-RPC TCP client pool | Zero-import composition |
| Graceful degradation | Retry → fallback → default | No primal is required |
| Deploy graph | TOML topology + wave ordering | Dependency-aware spawning |
| Composition pipeline | act() → PrimalEnrichment | Many primals in, one result out |
| Capability discovery | Songbird broadcast | Primal-agnostic wiring |
| Tiered narration | Domain → general → template | Progressive enhancement |
| Circuit breaker | Failure tracking per method | Cascade prevention |

These patterns are not esotericWebb-specific. They are the gen4
composition vocabulary. Any sporeGarden product that consumes primals
will use some or all of these patterns.

---

*The primals do the hard work. The bridge hides the seams. The product
does the creative work. The creator never knows.*
