# RootPulse Coordination Patterns

**biomeOS Deployment and Workflow Graphs**

**Version**: 1.0.0-concept  
**Date**: December 27, 2025  
**Status**: Implementation Specification

---

## Overview

RootPulse workflows are expressed as biomeOS deployment and workflow graphs in TOML. These graphs define the coordination patterns between primals — how rhizoCrypt, LoamSpine, NestGate, BearDog, and sweetGrass orchestrate to produce version control behavior. The graphs are declarative: nodes declare dependencies, outputs, and capability requirements; biomeOS executes them.

---

## The Three Graph Types

### 1. Deploy Graph (provenance_trio_deploy.toml)

Sequential startup of the RootPulse provenance stack atop Tower (BearDog + Songbird):

1. **Tower verification** — health checks for BearDog and Songbird
2. **LoamSpine** — permanence layer; must start first (rhizoCrypt and sweetGrass dehydrate/anchor to it)
3. **rhizoCrypt** — ephemeral DAG; connects to LoamSpine for dehydration, BearDog for signing
4. **sweetGrass** — attribution; connects to LoamSpine for anchoring
5. **Capability registration** — registers `permanent_storage`, `dag`, `dehydration`, `attribution`, etc. with the biomeOS registry

### 2. Workflow Graph (rootpulse_commit.toml)

Sequential 6-phase commit workflow with `coordination = "Sequential"`:

1. **Health** — verify rhizoCrypt and LoamSpine
2. **Dehydrate** — rhizoCrypt produces DehydrationSummary from ephemeral session
3. **Sign** — BearDog cryptographically signs the summary
4. **Store** — NestGate persists content to content-addressed storage
5. **Commit** — LoamSpine appends to permanent linear history
6. **Attribute** — sweetGrass creates provenance braid (optional)

### 3. Pipeline Graph (provenance_pipeline.toml)

Streaming pipeline for continuous provenance. Same phases as rootpulse_commit but parameterized by `SESSION_ID` and `EXPERIMENT_ID` for any Spring experiment. Reusable across niches: Spring produces results → rhizoCrypt captures → dehydrate → LoamSpine permanence → sweetGrass attribution.

---

## Coordination Patterns Used

### Sequential (rootpulse_commit.toml)

Each phase depends on the previous. Phase outputs feed as inputs to the next:

```
dehydrate_session output (DehydrationSummary) → sign_commit input
sign_commit output (signed_summary) → store_content input
store_content output (content_stored) → commit_permanent input
```

### Parallel (within phases)

- **Health checks** — `check_rhizocrypt` and `check_loamspine` have no `depends_on`; they run in parallel

### Conditional (branching)

- **Phase 6 (sweetGrass attribute)** — optional; workflow succeeds even if attribution is unavailable

---

## Node Dependencies (rootpulse_commit.toml)

```
check_rhizocrypt ──┐
                   ├──► dehydrate_session ──► sign_commit ──► store_content ──┐
check_loamspine ───┘                                                          │
                                                                              ├──► commit_permanent ──► create_attribution
                                                                              │
check_loamspine ──────────────────────────────────────────────────────────────┘
```

- `check_rhizocrypt`, `check_loamspine` — parallel (no dependencies)
- `dehydrate_session` — depends_on `check_rhizocrypt`
- `sign_commit` — depends_on `dehydrate_session`
- `store_content` — depends_on `sign_commit`
- `commit_permanent` — depends_on `store_content` AND `check_loamspine`
- `create_attribution` — depends_on `commit_permanent`

---

## Capability Translation

biomeOS routes capability calls through its registry. Semantic names map to primal methods:

| Capability | Provider | Method |
|------------|----------|--------|
| `dag.dehydrate` | rhizoCrypt | `dehydrate` |
| `commit.session` | LoamSpine | `session.commit` |
| `provenance.create_braid` | sweetGrass | `sweetgrass.createBraid` |
| `crypto.sign` | BearDog | `ed25519_sign` |

Callers invoke `capability_call` with semantic names; biomeOS resolves provider, method, and transport. NestGate uses direct `rpc_call` with `storage.store` for content persistence.

---

## Future: Continuous Coordination for Game Sessions

The **ContinuousGraph** pattern is already implemented in biomeOS. `game_engine_tick.toml` defines a 60 Hz tick-based coordination:

```
input → game_logic → physics → scene → render
         ▲_______________│
         (feedback: physics → game_logic)
```

- **Per-node budgets** — each node has `budget_ms`; exceeded ticks reuse previous output and emit a warning
- **Feedback edges** — `physics` feeds back to `game_logic` for collision-driven decisions; `scene` feeds to `render` for interpolation
- **Target 60 Hz** — `target_hz = 60.0`, `max_accumulator_ms = 100.0`

This pattern can extend to RootPulse game sessions: continuous provenance capture at tick boundaries, with the same dehydration → sign → store → commit pipeline triggered on session boundaries.

---

## Next Reading

1. [03_PRIMAL_COMPOSITION.md](./03_PRIMAL_COMPOSITION.md) — How primals coordinate
2. [04_BIOME_DEPLOYMENT.md](./04_BIOME_DEPLOYMENT.md) — BiomeOS orchestration
3. [02_ARCHITECTURE.md](./02_ARCHITECTURE.md) — System design
