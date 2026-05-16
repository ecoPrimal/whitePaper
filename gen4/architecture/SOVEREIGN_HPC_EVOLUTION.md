# Sovereign HPC Evolution — From Basement Cluster to Gram-Negative Organism

**Date**: May 15, 2026
**Status**: Active evolution — 10G backbone imminent, HBM2 fleet expanding
**Lineage**: gen1 hardware acquisition → gen3 cluster inventory → gen4 membrane composition
**Relates to**: `CELLMEMBRANE_FIELDMOUSE_ARCHITECTURE.md`, `SOVEREIGN_COMPUTE_TRIO_SKETCH.md`,
`BIOMEOS_OS_TRAJECTORY.md`, `NUCLEUS_SOVEREIGNTY_ARCHITECTURE.md`

---

## The Question This Document Answers

gen3 `about/HARDWARE.md` inventories the hardware — what we own, where it
sits, what it can do. This document answers a different question:

> **How does sovereign hardware compose into a living organism through
> the cell membrane model?**

The hardware inventory is static. The composition is dynamic. A Titan V
in a PCIe slot is a card. A Titan V dispatched through coralReef's
sovereign compiler, coordinated by toadStool, connected via 10G backbone
to a provenance pipeline anchored by the trio — that is an organ in an
organism.

---

## The Three-Layer Membrane Model (Gram-Negative Architecture)

Gram-positive bacteria have one membrane. Gram-negative bacteria have
two: an **outer membrane** facing the environment, an **inner membrane**
protecting the cytoplasm, and a **periplasmic space** between them where
critical biochemistry happens (protein folding, signal transduction,
toxin export).

Our infrastructure follows the gram-negative pattern:

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXTRACELLULAR (Internet)                       │
│  DNS registrar · GitHub Pages CDN · Cloudflare edge · browsers   │
└──────────────────────────────┬──────────────────────────────────┘
                               │ ionic (scoped tokens, TLS)
┌──────────────────────────────▼──────────────────────────────────┐
│              OUTER MEMBRANE (VPS — covalent to gate)              │
│  Caddy TLS :443 · Songbird TURN :3478 · RustDesk :21115-17      │
│  BearDog crypto :9100 · SkunkBat audit :9140                     │
│  membrane.primals.eco (Let's Encrypt E8, 68ms TTFB)              │
└──────────────────────────────┬──────────────────────────────────┘
                               │ routing decisions, telemetry
┌──────────────────────────────▼──────────────────────────────────┐
│                 PERIPLASM (Routing + Bonding Logic)               │
│  routing_config.toml · membrane_telemetry.sh (15-min cron)       │
│  shadow_run_orchestrator.sh · membrane_7day.toml                 │
│  Content-aware routing: static→cache, auth→gate, large→P2P      │
│  Trust classification: covalent/ionic/metallic/weak              │
└──────────────────────────────┬──────────────────────────────────┘
                               │ covalent (SSH, tunnel, owned)
┌──────────────────────────────▼──────────────────────────────────┐
│            INNER MEMBRANE (Gate Network Boundary)                 │
│  UFW deny-default · iptables owner-match DROP · hidepid=2        │
│  cloudflared tunnel · JupyterHub :8000 (PAM + BTSP dual-auth)    │
│  13 primals on 127.0.0.1 · MethodGate enforced                   │
└──────────────────────────────┬──────────────────────────────────┘
                               │ full trust (family seed, 10G)
┌──────────────────────────────▼──────────────────────────────────┐
│           INTRACELLULAR (Covalent HPC Mesh — the compute)        │
│                                                                   │
│  ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌─────────┐           │
│  │ironGate │  │northGate│  │strandGate│  │biomeGate│           │
│  │i9-14900K│  │9950X3D  │  │Dual EPYC │  │TR 3970X │           │
│  │96GB DDR5│  │RTX 5090 │  │256GB ECC │  │HBM2 test│           │
│  └────┬────┘  └────┬────┘  └─────┬────┘  └────┬────┘           │
│       └─────────────┴─────────────┴─────────────┘                │
│                    10G BACKBONE (pending cables)                   │
│                                                                   │
│  + southGate (128GB) + eastGate (Akida NPU) + westGate (76TB)    │
│  + swiftGate + flockGate + kinGate + blueGate + 3x Intel NUC     │
└─────────────────────────────────────────────────────────────────┘
```

### Why Gram-Negative, Not Gram-Positive

A gram-positive organism (single membrane) would be: gate directly
facing the internet, one firewall, done. This is how most self-hosted
infrastructure works. It's fragile — one misconfiguration exposes
everything.

The gram-negative model adds a **sacrificial outer membrane** (the VPS)
that can be destroyed and reprovisioned without affecting intracellular
state. The periplasm (routing logic, telemetry) enables sophisticated
decisions about what crosses each boundary. The inner membrane (UFW,
iptables, hidepid) is the last defense.

The biological advantage: gram-negative bacteria are resistant to many
antibiotics because the outer membrane blocks penetration, and the
periplasm contains enzymes (beta-lactamases) that destroy threats before
they reach the inner membrane. Our periplasm contains SkunkBat audit,
content-aware routing, and BTSP token validation — same function.

---

## Bonding at Each Layer

The bonding model (covalent/ionic/metallic/weak) maps directly to
membrane permeability:

| Boundary | Bond Type | What Crosses | Trust Level |
|----------|-----------|--------------|-------------|
| Intra ↔ Intra (gates) | **Covalent** | Everything — full primal RPC, blob replication, workload dispatch | Shared family seed, 10G wire speed |
| Intra ↔ VPS | **Covalent** | SSH, deploy scripts, content sync, health probes | Same owner, key-based |
| VPS ↔ External (ABG) | **Ionic** | Scoped access — BTSP tokens, content serving, relay traffic | Metered, per-request auth |
| VPS ↔ External (public) | **Weak** | Read-only content — sporePrint pages, health endpoints | Zero trust, observe-only |
| Gate ↔ External (tunnel) | **Ionic** | JupyterHub sessions, API calls (via Cloudflare Access + PAM) | Gated, session-scoped |

### The Ionic Surface

ABG collaborators interact with the organism through the **ionic
surface** — the outer membrane's public-facing APIs. They receive
scoped capability tokens (BearDog ionic: Ed25519-signed, expiry, JTI)
that grant access to specific resources:

- Notebook execution (JupyterHub via tunnel)
- Content viewing (sporePrint via Caddy)
- Compute dispatch (toadStool via biomeOS, future)
- Remote desktop (RustDesk, scoped to session)

The ionic surface is the **value proposition**: sovereign compute
offered to collaborators without compromising intracellular sovereignty.
The covalent mesh does the work; the ionic surface shares the results.

### The Third Layer (gram-negative expansion)

A single VPS is gram-positive-plus (outer membrane exists but is
singular). True gram-negative architecture requires **multiple outer
membrane nodes** forming a contiguous boundary:

```
                  Internet (extracellular)
                 /          |          \
         VPS-NYC       VPS-EU       VPS-West
        (current)    (future)      (future)
              \          |          /
               \         |         /
                 ┌───────────────┐
                 │  PERIPLASM    │ ← distributed routing
                 │  (Songbird    │    + federated telemetry
                 │   federation) │
                 └───────┬───────┘
                         │ covalent
                 ┌───────▼───────┐
                 │ GATE CLUSTER  │
                 │ (10G backbone)│
                 └───────────────┘
```

Each VPS runs Tower atomic (BearDog + SkunkBat), Songbird relay, and
Caddy TLS. They federate via Songbird's BirdSong protocol — encrypted
UDP discovery within the genetic lineage. The periplasm becomes a
distributed consensus layer: which VPS serves which request, where
content is cached, how load distributes.

This maps to real biology: gram-negative outer membrane is not a single
lipid bilayer — it contains **porins** (selective channels) and
**lipopolysaccharide** (immune evasion). Each VPS is a porin; the
routing logic is the LPS.

---

## What We Have (May 2026 Inventory)

### Intracellular Compute

| Resource | Quantity | Notes |
|----------|----------|-------|
| Towers | 11 | northGate through blueGate |
| CPU cores | 154+ | Celeron through dual EPYC 7452 |
| System RAM | ~1.0 TB | DDR3 through DDR5-4800 |
| GPU VRAM (total) | ~248 GB | Display + work tier combined |
| HBM2 | 56 GB | 2x Titan V (24 GB) + 2x MI50 (32 GB) |
| HBM2 FP64 | ~28 TFLOPS | sovereign via coralReef (sm_70 + gfx906) |
| NPU | 3x Akida AKD1000 | Sovereign Rust driver, 18.8K Hz inference |
| Cold storage | 76 TB | ZFS on westGate |
| NVMe (aggregate) | ~46 TB | Across all gates |
| GPU vendors | NVIDIA + AMD | barraCuda WGSL validated on both |
| GPU architectures | Kepler → Blackwell (NVIDIA), Vega 20 + RDNA 2 (AMD) | 7 generations |

### Networking

| Component | Status | Impact |
|-----------|--------|--------|
| 10G switch | **Acquired** | Backbone hub |
| 10G NICs x4 | **Installed** | northGate, southGate, eastGate, westGate |
| 10G cables (Cat6a/DAC) | **Pending** (~$50-100) | The only blocker |
| 1G mesh (remaining gates) | Active | biomeGate, strandGate, others on 1G |
| NUC M6 point-to-point | Active | USB-C ethernet to ironGate (10.99.0.0/30) |
| VPS ↔ Gate | SSH over internet | ~15ms RTT (NYC to Michigan) |

### Outer Membrane (VPS)

| Resource | Value |
|----------|-------|
| Provider | DigitalOcean nyc1 |
| Cost | $12/month (2 GB RAM, 1 vCPU) |
| IP | 157.230.3.183 |
| Services | 6 (Songbird TURN, RustDesk hbbs/hbbr, BearDog, SkunkBat, Caddy TLS) |
| TLS surface | `membrane.primals.eco` (Let's Encrypt E8, auto-renewal) |
| Content cache | 19 MB sporePrint (synced from gate NestGate cache) |
| RAM free | 1.7 GB |
| Disk | 14% used |

### Sovereignty Proofs (May 15, 2026)

| Proof | Result |
|-------|--------|
| BearDog TLS vs Cloudflare | 3ms vs 120ms (40x sovereign advantage) |
| HTTP content parity | VPS 68ms TTFB vs GitHub Pages 89ms (**PASS**) |
| TLS content parity | membrane.primals.eco 130ms vs primals.eco 96ms (within 35%) |
| ACME cert automation | End-to-end working (http-01 challenge, 4s to cert) |
| NAT relay reachability | 100% (10/10 UDP probes) |
| Uptime (both channels) | 100% |
| Continuous telemetry | 15-min cron, 7-day rolling summary, permanent shadow |

---

## Evolution Path

### Tier 1: 10G Backbone Activation (immediate — ~$50 in cables)

The switch is acquired. The NICs are installed. The only blocker is
physical cable runs between the four primary towers.

**What changes at 10G**:

| Workload | At 1G | At 10G | Improvement |
|----------|-------|--------|-------------|
| NestGate blob replication (5 GB FASTQ) | 40s | 4s | 10x |
| toadStool workload shuffle (100 MB state) | 0.8s | 0.08s | 10x |
| Songbird cross-gate federation | ~125 MB/s ceiling | ~1.2 GB/s | Wire speed |
| provenance pipeline (BLAKE3 hash streaming) | Bottlenecked at NIC | Bottlenecked at NVMe | Unblocked |
| Plasmodium collective model sync | Latency-bound | Latency-bound (10G doesn't help latency) | Neutral |

**Configuration changes**:
- MTU 9000 (jumbo frames) on 10G interfaces
- Dedicated VLAN for inter-gate covalent traffic
- Songbird auto-discovers 10G peers via BirdSong (larger payloads)
- NestGate content-addressed replication leverages full bandwidth

**What this enables**: The covalent mesh becomes a single logical machine
for data-intensive workloads. strandGate's 256 GB ECC + dual EPYC runs
the CPU-bound bioinformatics; northGate's RTX 5090 runs the GPU shaders;
westGate's 76 TB ZFS stores the results — all at wire speed.

### Tier 2: HBM2 Fleet Expansion (access-dependent)

The sovereign compute pipeline (coralReef compiler → toadStool dispatch)
already targets two HBM2 architectures: Volta `sm_70` and Vega 20
`gfx906`. Expanding the fleet requires zero new compiler work for cards
sharing these targets.

**Priority acquisitions** (from `gen3/about/HBM2_WATCHLIST.md`):

| Card | HBM2 | FP64 | Target | Price | New Compiler Work |
|------|------|------|--------|-------|-------------------|
| MI60 | 32 GB | 7.4 TFLOPS | gfx906 (same as MI50) | ~$550 | Zero |
| V100 16GB PCIe | 16 GB | 7.0 TFLOPS | sm_70 (same as Titan V) | ~$400 | Zero |
| P100 16GB PCIe | 16 GB | 5.3 TFLOPS | sm_60 (new, simpler) | ~$350 | Moderate |

**After all Tier 1 acquired**: 7 HBM2 cards, 120 GB aggregate, ~48
TFLOPS FP64, under $2K total investment. For comparison: one A100 80GB
costs $10K+ and delivers 19.5 TFLOPS FP64. The sovereign fleet delivers
2.5x the FP64 throughput at 1/5 the cost, across vendor-orphaned silicon
that the sovereign compiler pipeline rescues.

**Access factors**:
- NVIDIA R535 LTS driver EOL: **June 2026** (imminent — expect Volta price drops)
- MI100 ROCm drop: watch ROCm release notes for gfx908 deprecation
- Cooling: 3D-printed blowers proven on MI50, same STLs fit MI60
- PCIe slots: biomeGate has 3-slot practical limit (expandable with risers)
- Budget: $550 for MI60, $400 for V100 — individually accessible

### Tier 3: Blackwell Pro / Next-Gen HPC (future)

The mesh already contains two Blackwell devices:
- northGate: RTX 5090 (32 GB GDDR7, SM120)
- ironGate: RTX 5070 (12 GB GDDR7, SM120)

These validate coralReef's SM120 target at consumer ratios (1:64 FP64).
A Blackwell Pro (B200/B100) would provide:
- Native FP64 at datacenter ratios (1:2 or 1:4)
- 80-192 GB HBM3e (single card exceeds entire current fleet)
- NVLink for multi-GPU coherent memory

**Access factors**: $10K+ new, server chassis required, 300-700W TDP,
secondary market years away. The sovereign compute trio must first prove
E2E dispatch on current hardware before justifying this investment.

**The honest assessment**: The HBM2 fleet at $2K delivers more aggregate
FP64 than a single B200 at $30K. The Blackwell advantage is memory
bandwidth (HBM3e at 8 TB/s vs HBM2 at ~1 TB/s) and single-card VRAM
(192 GB vs 32 GB max). For our workloads (lattice QCD sweeps,
bioinformatics pipelines, LTEE simulations), the embarrassingly-parallel
HBM2 fleet is likely the better investment until a single workload
demands >32 GB contiguous GPU memory.

### Tier 4: Multi-VPS Mesh (gram-negative expansion)

Multiple VPS nodes in different geographies, each running Tower
composition, forming a contiguous outer membrane:

| VPS | Location | Purpose |
|-----|----------|---------|
| membrane-nyc (current) | DigitalOcean NYC1 | Primary relay + TLS surface |
| membrane-eu (future) | Hetzner/OVH EU | EU latency for EU collaborators |
| membrane-west (future) | DO SFO/LAX | West coast latency |

Each VPS costs ~$12/month. The aggregate membrane cost is ~$36/month
for global coverage — less than a single Cloudflare Pro subscription.

**What this enables**:
- Geographic load balancing (Songbird routes to nearest outer membrane)
- Redundancy (one VPS down, others absorb)
- DNS anycast potential (authoritative NS on multiple VPS)
- Content edge caching (sporePrint cached at each geo)

---

## The Compute Trio in Membrane Context

The sovereign compute trio (coralReef + toadStool + barraCuda) is the
computational engine inside the intracellular space. Its relationship
to the membrane model:

```
External request (ionic): "run lattice QCD β=6.0"
  → Outer membrane (VPS): TLS terminates, token validated
  → Periplasm: routing classifies as compute workload → gate
  → Inner membrane: tunnel carries to JupyterHub/biomeOS
  → Intracellular: biomeOS dispatches via deploy graph
    → barraCuda (WHAT): defines the physics — Yukawa potential, HMC
    → coralReef (HOW): compiles WGSL → SM70 binary for Titan V
    → toadStool (WHERE): dispatches to biomeGate's Titan V via VFIO
    → Result streams back through membranes
  → Periplasm: telemetry records latency, SkunkBat audits
  → Outer membrane: response served to collaborator
```

The compute trio never touches a membrane. It operates purely inside the
cell. The membrane infrastructure (VPS, routing, telemetry) is a
different concern entirely — this is the Layer 1/Layer 3 separation from
`SOVEREIGN_COMPOSITION_EVOLUTION.md` made operational.

---

## What ABG Gets (Ionic Compute Sharing)

The entire infrastructure exists to serve one purpose: offer sovereign
compute to ABG collaborators through ionic bonding. What they experience:

| Capability | How It Works | Membrane Path |
|-----------|-------------|---------------|
| Run notebooks | JupyterHub → Python/R kernels | Tunnel → inner membrane → gate |
| Submit workloads | toadStool dispatch via TOML spec | Tunnel → biomeOS → compute trio |
| View results | sporePrint at primals.eco/lab | Outer membrane → Caddy → NestGate cache |
| Access remote desktop | RustDesk → gate display | Outer membrane → TURN → RustDesk relay |
| Verify provenance | sweetGrass braid inspection | Tunnel → loamSpine → braid API |

**What they never see**: The gate hardware, the 10G backbone, the HBM2
cards, the deploy graphs, the primal ports, the family seed. Ionic
bonding is selective permeability — they get the capability without the
mechanism.

---

## Relationship to Other Documents

| Document | What It Covers | How This Doc Extends It |
|----------|---------------|------------------------|
| `gen3/about/HARDWARE.md` | Static inventory | Composes into membrane layers |
| `gen3/about/HBM2_WATCHLIST.md` | Acquisition targets | Places in evolution timeline |
| `CELLMEMBRANE_FIELDMOUSE_ARCHITECTURE.md` | VPS deployment | One node in outer membrane |
| `SOVEREIGN_COMPUTE_TRIO_SKETCH.md` | GPU dispatch model | Engine inside intracellular |
| `BIOMEOS_OS_TRAJECTORY.md` | OS vision (Layer 0) | Hardware layer of future OS |
| `NUCLEUS_SOVEREIGNTY_ARCHITECTURE.md` | Sovereignty evolution | Membrane model operationalized |
| `SOVEREIGN_COMPOSITION_EVOLUTION.md` | Layer separation | Hardware as Layer 3 infrastructure |
| `projectNUCLEUS/gates/` | Gate TOML configs | Machine-readable nodes in mesh |
| `projectNUCLEUS/deploy/nucleus_config.sh` | Runtime config | Periplasm routing + membrane params |

---

## The Living Organism Analogy (Complete)

```
gen1:  Acquired organelles (hardware)          → cards in boxes
gen2:  Organelles learned to communicate       → JSON-RPC, IPC
gen3:  Proved each organelle works correctly   → 12,510+ checks
gen4:  Organelles composed into organs         → products, compositions
Now:   Organism growing its membrane           → VPS, routing, telemetry
Next:  10G nervous system connects organs      → backbone activation
Then:  More mitochondria (HBM2 fleet)          → compute capacity
Later: Multi-cell organism (VPS mesh)          → geographic distribution
Final: Fully autonomous organism               → zero external dependencies
```

The 10G backbone is the **nervous system** — it doesn't add compute, it
connects compute. A brain without nerves is isolated tissue. A cluster
without 10G is isolated gates. The cables are the cheapest, highest-ROI
evolution step available: $50 transforms isolated gates into a unified
computational organism.

---

*11 towers, 4 HBM2 cards, 3 NPUs, 1 VPS outer membrane, 1 organism forming.
The cables are $50. The membrane is live. The rest is patience and
secondary markets.*
