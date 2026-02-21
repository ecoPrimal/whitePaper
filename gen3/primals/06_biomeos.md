# biomeOS — Autonomous Orchestration

## Identity

| Field | Value |
|-------|-------|
| Phase | 2 (Foundation) |
| Domain | Orchestration, Neural API, NUCLEUS composition, federation |
| Rust lines | 321,534 |
| Tests | 14,179 |
| Crates | 26 |
| AGPL-3.0 | Yes |

## What It Is

biomeOS is the conductor. It starts the other primals in the correct order, maintains a capability registry, routes requests semantically, composes primals into atomics (Tower, Node, Nest, NUCLEUS), and manages the lifecycle of the entire ecosystem.

If BearDog is the immune system and Songbird is the nervous system, biomeOS is the endocrine system: it coordinates all the organs without micromanaging any of them.

## Why It Exists

In gen2, the ecoPrimals whitepaper described "composable primitives" but left coordination implicit. As the primal count grew from 2 (gen1) to 8 (gen2) to 12 (gen3), explicit orchestration became necessary. Who starts first? How does a new primal discover existing ones? What happens when a primal crashes? biomeOS answers these questions.

The name comes from gen2's "biome" concept: a packaged ecosystem defined by a `biome.yaml` manifest, analogous to a biological biome where organisms interact through defined ecological relationships.

## Key Capabilities

### Neural API

124 semantic capability translations. Callers don't address primals by name — they request capabilities:

```
capability.call("crypto.sign", { message: "..." })    → routes to BearDog
capability.call("ai.chat", { prompt: "..." })          → routes to Squirrel
capability.call("store.blob", { data: "..." })         → routes to NestGate
capability.call("compute.matrix_mul", { a, b })        → routes to ToadStool
```

biomeOS discovers which primal provides each capability, routes the request, and returns the result. The caller never knows (or cares) which primal handled it.

### NUCLEUS Composition

biomeOS composes primals into atomics and validates their health:

| Atomic | Composition | biomeOS Responsibility |
|--------|------------|----------------------|
| Tower | BearDog + Songbird | Verify crypto + networking healthy |
| Node | Tower + ToadStool | Verify compute available |
| Nest | Tower + NestGate | Verify storage available |
| Full NUCLEUS | Tower + Node + Nest + Squirrel | All capabilities green |

### Lifecycle Management

Startup order: `BearDog → Songbird → ToadStool → NestGate → Squirrel → biomeOS`

biomeOS starts last because it depends on all foundation primals. Once running, it monitors health, handles crashes (auto-resurrection), and can start/stop post-NUCLEUS primals on demand.

### AI Bridge

The AI Bridge routes AI requests from Squirrel through Songbird to cloud providers:

```
Application → biomeOS → Squirrel → Songbird → {OpenAI | Anthropic | Ollama}
```

This chain ensures that AI requests go through crypto (BearDog → Songbird) and routing (Squirrel) before leaving the machine.

### Plasmodium Collective

For multi-machine deployments, biomeOS instances can form a "plasmodium" — a collective that coordinates across machines. Agent operations: meld (combine), split (distribute), mix (redistribute). This enables NUCLEUS to scale from one basement server to a distributed mesh.

## How It Connects

```
          ┌──────────────────────────────┐
          │           biomeOS            │
          │    (Neural API + NUCLEUS)    │
          └──────────┬───────────────────┘
     ┌───────────────┼───────────────────┐
     │       │       │       │           │
  BearDog  Song  ToadStool NestGate  Squirrel
  (crypto) (net)  (compute) (store)   (AI)
     │       │       │       │           │
     └───────┴───────┴───────┴───────────┘
              Foundation Primals
                    │
     ┌──────────────┼──────────────┐
     │    │    │    │    │    │    │
   petal sourdgh sweet loam rhizo skunk
   Tongue       Grass Spine Crypt  Bat
              Post-NUCLEUS Primals
```

### Key Relationships

- **All primals** register capabilities with biomeOS
- **BearDog** is always started first; biomeOS verifies its health before proceeding
- **Songbird** provides the discovery and networking substrate that biomeOS uses
- **ToadStool** and **NestGate** are composed into Node and Nest atomics
- **Squirrel** is the last foundation primal started, completing NUCLEUS

## Internal Architecture

26 crates:

- `biomeos-core` — Main lifecycle, capability registry
- `biomeos-types` — Shared type definitions
- `biomeos-nucleus` — NUCLEUS composition and health monitoring
- `biomeos-atomic-deploy` — Tower/Node/Nest deployment
- `biomeos-graph` — Neural API capability graph (124 translations)
- `biomeos-spore` — Plasmodium collective (multi-machine)
- `biomeos-genomebin-v3` — Deployment packaging

## What's Been Deployed

### USB-to-Pixel Handshake (Cross-Network, Cross-Architecture)

biomeOS orchestrated the first cross-network cryptographic handshake: a USB LiveSpore (x86_64, desktop LAN) and a Pixel 8a (aarch64, mobile hotspot) paired through the Tower's rendezvous endpoint via `api.nestgate.io`.

The flow:
- `pixel8a-deploy/` contains the mobile deployment scripts (`start_nucleus_mobile.sh`, `test_nat_traversal.sh`)
- `livespore-usb/` contains cross-arch binaries (x86_64 and aarch64) with deploy scripts
- `crates/biomeos-api/src/handlers/rendezvous.rs` implements the blind matchmaker — POST/check beacon, lineage verification, 5-minute TTL slots
- `crates/biomeos-spore/src/dark_forest.rs` implements BirdSong beacon encryption (ChaCha20-Poly1305, `birdsong-broadcast-v1` context)
- `crates/biomeos-core/src/connection_strategy.rs` implements 4-tier NAT traversal (LAN → punch → coordinated → relay)

The E2E test (`crates/biomeos-api/tests/sovereign_mesh_e2e.rs`) covers the full Pixel-USB-Tower handshake with cryptographic mock BearDog, beacon posting, lineage matching, and encrypted data transfer.

### nestgate.io Tunnel

`api.nestgate.io` runs as a Cloudflare tunnel to Tower:3492 in the basement. Any device on any network can reach the Tower through HTTPS. The Pixel on a mobile hotspot, a NUC on a coffee shop WiFi, a gate at a friend's house — all reach the same rendezvous point through the tunnel. This is sovereign infrastructure: your domain, your tunnel, your machine.

### NUC Federation

Intel NUC nodes running Tower Atomic have been validated in the federation — discovery, beacon exchange, and capability registration through biomeOS. These are the always-on relay/discovery nodes described in the hardware inventory.

## What Makes It Interesting

biomeOS is the only primal in Phase 2 that is classified as "Foundation." It was added later than the Phase 1 primals but is architecturally fundamental — nothing works without orchestration.

The 124 semantic capability translations in the Neural API represent the ecosystem's API surface. Any application that speaks JSON-RPC can access any primal's capability without knowing which primal implements it. This decoupling is what makes hot-swapping primals possible: biomeOS can route `crypto.sign` to a different implementation without the caller noticing.
