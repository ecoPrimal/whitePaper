# Esoteric Webb

**The First gen4 Product: A CRPG Engine as Primal Composition**

**Date**: March 24, 2026
**Status**: V4 — Live primal composition wired into game loop
**Repository**: sporeGarden/esotericWebb
**Lineage**: gen3/baseCamp/17 (Game Science) + gen3/baseCamp/18 (RPGPT) → gen4

---

## What It Is

esotericWebb is a sovereign CRPG (Computer Role-Playing Game) engine
that consumes ecoPrimals infrastructure as invisible plumbing. It is
not a spring — it does not reproduce published science. It is a
**product** — something a creator uses to build interactive narrative
worlds.

It is the first project where the primals are infrastructure, not the
subject. This makes it the gen3→gen4 boundary artifact.

---

## Vital Statistics (V4, March 24, 2026)

| | |
|---|---|
| **Version** | V4 |
| **Tests** | 166 |
| **Rust files** | 32 (~8.5k LOC) |
| **Experiments** | 5 (exp001–exp005) |
| **MSRV** | 1.87 (edition 2024) |
| **License** | AGPL-3.0 + ORC + CC-BY-SA 4.0 (scyBorg trio) |
| **Unsafe** | `#![forbid(unsafe_code)]` |
| **C deps** | Zero (ecoBin compliant) |
| **Bridge methods** | 23 (all domains, all degrading) |
| **Primals consumed** | 8 domains |
| **Clippy** | pedantic + nursery, zero warnings |

---

## The V1–V4 Arc

### V1: Foundation (early March 2026)

Core data structures: `WorldState`, `NarrativeGraph`, `GameSession`.
YAML content loading. Text-mode game loop. Experiment harness. 40+
tests. The engine ran standalone with zero primals.

### V2: Bridge Construction (mid March 2026)

`PrimalBridge` with JSON-RPC client stubs for all 8 domains. Graceful
degradation (retry + circuit breaker + sensible defaults). 80+ tests.
The engine could talk to primals but all calls degraded to defaults.

### V3: Content Pipeline (mid-late March 2026)

YAML content authoring spec. NPC personality certs with knowledge
bounds, trust gates, lie tables. Ability system with stat interactions.
Ruleset validation. CLI tools (validate, preview, graph). 120+ tests.
The engine could ingest creator content and run standalone previews.

### V4: Live Composition (March 24, 2026)

Full primal wiring in `GameSession::act()`:

- **ludoSpring** (game science): narration, NPC dialogue, flow
  evaluation, voice checks, scene push, session lifecycle
- **Squirrel** (AI): narration fallback, summarization
- **petalTongue** (visualization): scene rendering, input polling
- **rhizoCrypt** (provenance): DAG session create → event append →
  session complete → frontier/merkle queries

All with tiered degradation. 166 tests. Five numbered experiments
validating bridge resilience, composition pipeline, and provenance
lifecycle.

---

## Architecture

```
esotericWebb/
├── webb/                     # Core engine crate
│   └── src/
│       ├── lib.rs            # Public API + GameSession
│       ├── autoplay.rs       # Heuristic autoplay
│       ├── bridge.rs         # PrimalBridge (JSON-RPC composition)
│       ├── combat.rs         # Tactical combat system
│       ├── content.rs        # YAML content loading
│       ├── director.rs       # GameDirector (narrative flow)
│       ├── enrichment.rs     # PrimalEnrichment (composition result)
│       ├── experiment.rs     # Shared validation harness
│       ├── graph.rs          # NarrativeGraph (DAG topology)
│       ├── state.rs          # WorldState (combinatorial state)
│       └── ipc/              # IPC subsystem
│           ├── client.rs     # JSON-RPC client
│           ├── listener.rs   # IPC listener
│           ├── protocol.rs   # Wire protocol
│           └── transport.rs  # TCP/UDS transport
├── specs/                    # Design specifications
│   ├── BOUNDED_INFINITE_ARCHITECTURE.md
│   ├── CONTENT_AUTHORING_SPEC.md
│   ├── CREATOR_PROFILES_AND_SYSTEM_DESIGN.md
│   ├── DESIGN_PRINCIPLES.md
│   ├── EXPERIMENT_SPEC.md
│   └── IPC_PRIMAL_WIRING.md
├── experiments/              # Numbered validation experiments
│   ├── exp001_bridge_basic/
│   ├── exp002_flow/
│   ├── exp003_content_pipeline/
│   ├── exp004_autoplay/
│   └── exp005_primal_composition/
├── content/                  # Example YAML content
├── wateringHole/             # Handoffs and guidance
└── deploy/                   # Deploy graph TOML files
```

---

## What esotericWebb Proved

### 1. Primals Can Be Invisible

The game loop (`GameSession::act()`) composes 8 primal domains into a
single `PrimalEnrichment` result. The player never knows. The creator
doesn't need to know. The primals are the plumbing.

### 2. Graceful Degradation Works

Every bridge call has a fallback chain. The engine runs standalone (no
primals) for content development. It runs partially (some primals) for
testing. It runs fully (all primals) for production. Same code path,
different capability levels.

### 3. The Dual Surface Works

Creators write YAML. Developers write Rust. Both produce the same
game world. The `validate` command checks creator content without
running the engine. The `preview` command runs it in text mode without
primals. The barrier is low for creators, deep for developers.

### 4. Bounded Infinite Stories Are Buildable

The `NarrativeGraph` + `WorldState` + predicate system creates the
combinatorial state space described in BOUNDED_INFINITE_STORIES.md.
8 rooms × 5 NPCs × 8 abilities × 4 arc phases × continuous trust ×
flags = a state space no author could enumerate.

### 5. Provenance as Infrastructure Is Viable

The rhizoCrypt integration (DAG session create → event append →
session complete) runs inside the game loop. Every player action is a
DAG vertex. Every playthrough is traceable. The provenance overhead
is negligible because the DAG operations are append-only and
non-blocking.

---

## Patterns Extracted for Other Products

These patterns were discovered building esotericWebb and are documented
in gen4/architecture/COMPOSITION_PATTERNS.md:

1. **PrimalBridge** — JSON-RPC client pool with per-method degradation
2. **Deploy graph** — TOML topology with wave-ordered spawning
3. **PrimalEnrichment** — Many primals in, one data structure out
4. **Tiered narration** — Domain engine → general AI → local template
5. **Circuit breaker** — Consecutive failure tracking per method
6. **Capability discovery** — Songbird broadcast for primal-agnostic wiring
7. **Zero-import principle** — No primal crate dependencies

---

## Evolution Roadmap

### V5 (planned): Deep Composition

- Live NPC personality certs from loamSpine (currently bridge-ready)
- sweetGrass attribution braids in game loop
- toadStool GPU dispatch for compute-heavy scenes
- nestGate persistence for save games

### V6 (planned): Creator Tools

- GUI content editor (petalTongue-powered)
- Content pack format for distribution
- Community sharing via Songbird discovery
- Template worlds for common genres

### V7 (planned): Federation

- Multi-machine deployment (GPU server + local client)
- Collaborative world building (multiple creators, attribution)
- Player-to-player world sharing with provenance

---

## The Name

"Esoteric Webb" references Cliche Studio's *Esoteric Ebb* (successor
to Disco Elysium) and the interconnected web of primals that compose
beneath the surface. The "Webb" spelling evokes both the web of
connections and the James Webb Space Telescope — an instrument that
sees deeper into structure than anything before it.

The naming follows the ecosystem's biological vocabulary while honoring
the creative lineage that inspired it.

---

*esotericWebb is not the point. The point is what someone builds with
esotericWebb — a world they care about, traced from first playtest to
thousandth playthrough, attributed from creator to player, remembered
by infrastructure that was never visible.*
