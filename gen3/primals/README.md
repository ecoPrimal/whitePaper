# The Primals

## What This Is

This is the work. The thesis came later — the primals came first.

This directory documents each primal individually: what it does, why it exists, how it evolved, and how it connects to the others. The thesis (`gen3/thesis/`) formalizes the methodology that emerged from building them. This directory documents the building itself.

---

## The Evolution: gen1 → gen2 → gen3

### gen1 — The AI Swarm (Latency and Downtime Theory)

The original idea was simple: **fault tolerance over perfect uptime** as a competitive advantage for independent scientific compute.

The insight was that 99.999% uptime costs $13,300/year in redundant hardware, enterprise licensing, and 24×7 operations — money that could buy GPUs and NVMe instead. If you accept 2–10 minutes of downtime per day and build software that handles it gracefully, you can build a multi-node HPC cluster for under $11,000.

Two software systems carried the idea:

1. **NestGate** — Rust-based storage management. ZFS, tiered storage (cold/warm/hot/cache), NFS/SMB. The data layer.
2. **Squirrel** — Fault-tolerant compute orchestration. MCP, circuit breakers, checkpoint/restart, "ant-model" orchestration. The brain.

These are the original primals, before the word "primal" existed. NestGate held the data; Squirrel coordinated the work. Everything else grew from the problems they couldn't solve alone.

The hardware: Stackgate (MCP orchestrator), Northgate (GPU), Southgate (storage), Swiftgate (edge), Nestgate (cold archive). Five machines, named for compass directions around a basement. Explicit uptime targets per node: Stackgate 95%, Northgate 80%, Nestgate 90%. Downtime was a parameter, not a failure mode.

### gen2 — ecoPrimals (Autonomy Scarcity)

Building NestGate and Squirrel exposed a deeper problem: **autonomy scarcity**. The hardware bottleneck (gen1) was solvable with money. The control bottleneck — who owns your data, who sees your traffic, who can revoke your compute — was structural.

The AI Swarm became ecoPrimals. Two systems became eight composable primitives:

| Primal | Domain | Why It Split Off |
|--------|--------|------------------|
| **NestGate** | Storage | Original. Still the data layer. |
| **Squirrel** | AI coordination | Original. Evolved from HPC orchestration to AI-native MCP. |
| **BearDog** | Cryptography | Every primal needed crypto. Embedding it in each was duplicating code and trust surface. Split out as a dedicated service. |
| **Songbird** | Networking | NestGate and Squirrel each had ad-hoc networking. TLS, discovery, NAT traversal needed one owner. |
| **ToadStool** | Compute | Squirrel orchestrated work but didn't own the GPU. ToadStool became the hardware-aware compute engine. |
| **biomeOS** | Orchestration | Someone had to start and coordinate all the primals. biomeOS is the conductor. |
| **sweetGrass** | Attribution | If sovereign systems produce work, who gets credit? PROV-O provenance tracking. |
| **rhizoCrypt** | Working memory | Content-addressed ephemeral DAG for session state. The scratch pad. |

Gen2 also introduced the philosophical framing: **sovereignty-first**, AGPL as a trust protocol, "bring-your-own-AI", rejection of intermediaries between people and their data.

### gen3 — Constrained Evolution (The Discovery)

Building 8+ primals under a single constraint set (Pure Rust, JSON-RPC IPC, capability-based routing) produced something unexpected: **the primals converged on the same patterns independently**.

All primals implemented JSON-RPC 2.0 parsers independently. All used async Tokio. All converged on capability advertisement. All had zero unsafe blocks. The convergence wasn't planned — it was driven by the constraint.

This looked like evolution. Specifically, it looked like what happens when you put 12 bacterial populations under identical selective pressure: they find different paths to the same fitness.

That observation became the constrained evolution thesis. But the thesis is theory; the primals are the experiment.

Gen3 added four more primals to complete the ecosystem:

| Primal | Domain | Why |
|--------|--------|-----|
| **LoamSpine** | Permanent ledger | rhizoCrypt is ephemeral; LoamSpine is permanent. Together they implement the "philosophy of forgetting." |
| **petalTongue** | Representation/UI | Multi-modal interface: desktop (egui), terminal (ratatui), web (axum). |
| **skunkBat** | Defense | Threat detection without content inspection. Metadata-only security. |
| **sourDough** | Scaffolding | The starter culture. Core traits every primal must implement. |

Total: **12 primals** across two phases.

### Timeline

The primals are months old. The springs are weeks old. ToadStool and BarraCUDA evolved independently for ~8 months before the first spring existed. The springs then became the selection pressure that drove BarraCUDA's evolution toward specific scientific capabilities — f64 shaders, Yukawa force kernels, FFT from NTT, lattice QCD observables. The springs validated what the primals could do; the primals didn't know they could do science until the springs asked.

The full basement HPC via NUCLEUS is not deployed yet. All 2,882 science checks run on a single machine with a $600 consumer GPU. See [DISCOVERY_LOG.md](DISCOVERY_LOG.md) for how capability hunting — rather than monolithic SDKs — drove the key technical discoveries.

---

## The Twelve Primals at a Glance

| # | Primal | Phase | Domain | Rust Lines | Tests | Profile |
|--:|--------|:-----:|--------|----------:|------:|---------|
| 1 | [BearDog](01_beardog.md) | 1 | Cryptography | 577,341 | 11,872 | Foundation |
| 2 | [NestGate](02_nestgate.md) | 1 | Storage | 645,445 | 14,807 | Foundation |
| 3 | [Songbird](03_songbird.md) | 1 | Networking | 401,900 | 7,314 | Foundation |
| 4 | [Squirrel](04_squirrel.md) | 1 | AI Coordination | 681,933 | 25,359 | Foundation |
| 5 | [ToadStool](05_toadstool.md) | 1 | Compute (+ BarraCUDA) | 788,209 | 13,503 | Foundation |
| 6 | [biomeOS](06_biomeos.md) | 2 | Orchestration | 321,534 | 14,179 | Foundation |
| 7 | [petalTongue](07_petaltongue.md) | 2 | Representation / UI | 160,970 | 6,186 | Post-NUCLEUS |
| 8 | [sourDough](08_sourdough.md) | 2 | Scaffolding | 50,746 | 3,622 | Post-NUCLEUS |
| 9 | [sweetGrass](09_sweetgrass.md) | 2 | Attribution | 66,168 | 3,769 | Post-NUCLEUS |
| 10 | [LoamSpine](10_loamspine.md) | 2 | Permanence | 44,453 | 1,952 | Post-NUCLEUS |
| 11 | [rhizoCrypt](11_rhizocrypt.md) | 2 | Working Memory | 27,565 | 278 | Post-NUCLEUS |
| 12 | [skunkBat](12_skunkbat.md) | 2 | Defense | 7,366 | 48 | Post-NUCLEUS |

**Totals**: 3,773,630 Rust lines, 102,889 #[test] annotations.

---

## How They Interact

See [INTERACTIONS.md](INTERACTIONS.md) for the full coordination model.

Short version: every primal is a self-contained Rust binary that exposes **primitives** (atomic operations) via JSON-RPC 2.0 over Unix sockets. No primal imports another's code. Coordination happens at runtime through **biomeOS**, which maintains a capability registry and routes requests semantically.

The startup order matters:

```
BearDog → Songbird → ToadStool → NestGate → Squirrel → biomeOS → (everything else)
```

BearDog must be first because everything needs crypto. Songbird must be second because everything needs networking/discovery. ToadStool and NestGate provide compute and storage. Squirrel provides AI. biomeOS orchestrates the whole thing.

---

## NUCLEUS Atomics

Primals compose into larger units called **atomics**:

| Atomic | Components | What It Provides | Status |
|--------|------------|------------------|--------|
| **Tower** | BearDog + Songbird | Pure Rust HTTPS, zero C dependencies | **Deployed** — running on all gates + NUCs |
| **Node** | Tower + ToadStool | Tower + GPU/CPU/NPU compute | In progress |
| **Nest** | Tower + NestGate | Tower + content-addressed storage | In progress |
| **Full NUCLEUS** | Tower + Node + Nest + Squirrel | Complete sovereign stack | Future — requires Node + Nest |

### How Tower Atomic Was Discovered

~November 2025, ToadStool and Songbird managed basic distributed workloads on LAN — plaintext, no encryption. Then an audit of Songbird's TLS dependencies revealed: the `ring` crate wraps BoringSSL (C code). Any Rust project using `ring` for TLS has a hidden C dependency. The Pure Rust constraint was broken.

Tower Atomic was the solution: delegate all crypto to BearDog (which uses Pure Rust `RustCrypto` crates, no C) via JSON-RPC over Unix sockets. Songbird handles the TLS state machine; BearDog handles the math. Pure Rust HTTPS, onion routing, Dark Forest beacons — all via primal composition, zero C.

### What Tower Has Achieved

- **USB-to-Pixel cross-network handshake**: x86_64 LiveSpore (desktop LAN) ↔ aarch64 Pixel 8a (mobile hotspot), paired through `api.nestgate.io` Cloudflare tunnel → Tower:3492. Encrypted BirdSong beacons, lineage-verified, Tower never sees plaintext.
- **4-tier NAT traversal**: LAN → direct punch → coordinated punch → relay. Self-hosted, no rented TURN servers.
- **NUC federation**: Intel NUC nodes running Tower validated for always-on relay/discovery.
- **Cross-arch deployment**: Same protocol on x86_64 and aarch64 binaries.

### What Node + Nest Will Unlock

Node and Nest atomics will allow the basement HPC to become a covalent NUCLEUS mesh — machines bonded by family seed (SoloKey FIDO2), each running atomics matched to their hardware. Distributed springs: lattice QCD on Strandgate's dual EPYC, MD on Eastgate's RTX 4070, coordinated by biomeOS plasmodium.

---

## Reading Order

**If you're new to ecoPrimals**: Read this README, then BearDog (the simplest to understand), then Songbird (networking), then ToadStool (compute + BarraCUDA), then biomeOS (how they all fit together).

**If you're evaluating the architecture**: Start with [INTERACTIONS.md](INTERACTIONS.md), then read the foundation primals (1–6).

**If you want the discovery story**: Read [DISCOVERY_LOG.md](DISCOVERY_LOG.md) — how the f64-on-consumer-GPU discovery happened, how NTT became FFT, how mixed GPU/NPU/CPU pipelines emerged from capability hunting rather than SDK compliance.

**If you want the history**: Read gen1's AI Swarm whitepaper (`gen1/Draft/draft.md`), then gen2's ecoPrimals protocol (`gen2/EcoPrimals_Whitepaper_Draft.md`), then this directory.

**If you want the science**: Go to the springs (hotSpring, wetSpring, etc.) or the thesis (`gen3/thesis/`). The primals are infrastructure; the springs are what the infrastructure computes.
