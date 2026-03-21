# baseCamp Extension Plan: Technical Learnings and Evolution

**Date:** March 21, 2026 (hotSpring Exp 071 sovereign PFIFO pipeline update + V130 + ludoSpring V23 + airSpring V0.10.0 deep debt evolution update)
**Foundation:** baseCamp papers 01–22, barraCuda v0.3.5 standalone (wgpu 28), wetSpring V130 (376+ experiments, Anderson hormesis framework), airSpring v0.10.0 (911 lib + 311 integration + 61 forge tests, 97 binaries, 87 experiments, MCP tools/list + tools/call wired in primal dispatch — 10 ecology tools discoverable by Squirrel AI, platform-agnostic IPC Transport enum (Unix + TCP, ecoBin compliant), ValidationHarness migration, 50+ inline tolerances centralized, 63 provenance baselines, zero clippy warnings pedantic+nursery, `#![forbid(unsafe_code)]`, zero C deps, `#[expect(reason)]` Rust 2024 complete), ludoSpring V23 (75 experiments, 1692 checks, 394 tests + 12 proptest + 6 IPC integration, all modules >= 90% coverage, cross-ecosystem deep debt: zero `#[allow()]`, zero-panic validation, `#![forbid(unsafe_code)]`)

---

## Sovereign GPU Command Submission: PFIFO Pipeline Cracking (hotSpring Exp 071, March 21, 2026)

**Source:** hotSpring Exp 071, coralReef coral-driver diagnostic matrix
**Connects to:** baseCamp #14 (Sovereign Compute Hardware), sovereign compute thesis

### What Was Proven

A 54-configuration diagnostic matrix systematically tests every combination of
GPU channel initialization strategies on GV100 (Titan V) via VFIO — no kernel
driver, no proprietary firmware at the command submission layer.

**6 of 10 sovereign pipeline layers are now proven working:**

| Layer | Component | Status |
|-------|-----------|--------|
| 0-1 | PCIe/VFIO + PFB/MMU (warm state) | ✅ |
| 2-3 | PFIFO Engine + Scheduler | ✅ Re-initialized from cold |
| 4-5 | Channel + PBDMA Context | ✅ 12 configs scheduler-accepted |
| 6 | MMU Page Table Translation | ❌ Single remaining blocker |
| 7-10 | GPFIFO→Commands→FECS→Shader | Blocked by Layer 6 |

### Key Technical Discovery: PFIFO Re-Initialization

After nouveau unbind, PFIFO is disabled and PBDMAs hold stale channel contexts.
A 5-phase sequence reliably re-initializes in ~25ms:

1. PMC-level PFIFO reset (bit 8 of register 0x200)
2. PFIFO soft enable (0→1 transition at 0x2200)
3. Preempt ALL active runlists via GV100_PREEMPT (0x2638)
4. Wait for INTR_RL_COMPLETE (BIT30) acknowledgment
5. Force-clear PBDMA operational and context-save registers

This produces clean PBDMA states (`STATE=0x00000000`) ready for new channels.

### Root Cause: MMU Translation Failure

The PBDMA loads the GPFIFO base address (GPU VA 0x1000) from the channel context
but returns `0xbad00200` (PBUS timeout) when attempting to fetch entries. The GPU's
internal FBHUB MMU cannot translate the 5-level page table chain (PD3→PD2→PD1→PD0→PT0)
to reach host system memory via the IOMMU.

### Sovereign Compute Implications

The diagnostic matrix proves the channel→scheduler→PBDMA pipeline works without
any proprietary firmware or kernel driver at those layers. The remaining gap is
purely a memory mapping issue — the GPU MMU needs correctly-formatted page tables
that map GPU virtual addresses to IOMMU-visible host physical addresses.

Once this works, GPFIFO command submission is sovereign: the host writes commands
into DMA buffers and the GPU executes them without any driver involvement. This
is the foundation for the full sovereign compute pipeline (FECS/GPCCS firmware
load → shader dispatch).

### Cross-Spring Relevance

The PFIFO re-initialization sequence and register map are GV100-specific but the
*pattern* — PMC domain reset, engine enable, scheduler preempt, PBDMA context
clearing — applies to any NVIDIA Volta+ GPU and conceptually to AMD's equivalent
(SDMA/IH for command submission). The diagnostic matrix approach generalizes to
any GPU where the command submission path needs reverse engineering.

---

## FHE on GPU: Modular Arithmetic Without Native u64 (S87)

**Source:** ToadStool S87 deep debt evolution (March 2, 2026)  
**Connects to:** baseCamp #07 (Sovereign WDM Simulation), sovereign compute thesis

### The Problem

Fully Homomorphic Encryption (FHE) enables privacy-preserving computation — data remains encrypted while operations are performed. NTT/INTT (Number Theoretic Transform and its inverse) are the core primitives for polynomial multiplication in lattice-based FHE schemes. Running FHE on WebGPU/WGSL unlocks sovereign, vendor-agnostic privacy-preserving computation without cloud dependencies.

WGSL (WebGPU Shading Language) has no native `u64` or `u128`. All 64-bit arithmetic must be emulated with `u32` pairs. Standard FHE moduli (12289, 65537) fit in 16 bits, but intermediate products during NTT butterfly operations can reach millions — requiring correct 64-bit modular reduction.

### The Failure Mode

The naive approach — iteratively subtracting the modulus up to 128 times — fails catastrophically for products in the millions. For modulus 12289, a product of 150 million would require ~12,000 subtractions to reduce; 128 iterations produce unreduced values that cascade through the entire NTT/INTT computation, corrupting all outputs.

### The Solution: Bit-by-Bit Modular Reduction

The bit-by-bit shift-and-reduce technique discovered during S87 provides **exact** modular reduction in O(64) iterations:

1. Treat the 64-bit value as a stream of bits (high word first, then low word).
2. Maintain an accumulator that never exceeds 2× modulus.
3. For each bit: shift accumulator left, OR in the next bit; if accumulator ≥ modulus, subtract modulus.
4. After 64 bits, the accumulator holds the exact remainder.

This is a fundamental building block for FHE on WebGPU. It generalizes to any 32-bit modulus (covering 12289, 65537, and most NTT-friendly primes). For 64-bit moduli, the same technique applies with 128 iterations — the 128-iteration fallback path in the current implementation may need this treatment if larger FHE moduli are adopted.

### Sovereign Compute Implications

- **GPU FHE enables privacy-preserving computation** without vendor lock-in. WebGPU runs on Vulkan, Metal, D3D12 — no CUDA dependency.
- **Connects to baseCamp #07**: The sovereign WDM thesis argues that consumer GPU networks can replace institutional HPC for plasma physics. FHE on the same stack extends that thesis: sovereign *private* computation on consumer hardware.
- **No cloud required**: FHE inference and training can run entirely on edge devices or distributed consumer GPU networks, preserving data locality and avoiding trust boundaries.

### Lesson for Future Work

FHE modular arithmetic on GPU is treacherous. Every 64-bit operation (multiply, add, reduce) must be carefully emulated. The bit-by-bit reduction is O(64) but exact — a small constant cost that guarantees correctness. For production FHE at scale, consider precomputed Barrett reduction or Montgomery form for larger moduli; the bit-by-bit approach remains the correct fallback when those optimizations are unavailable or when modulus varies at runtime.

---

## Track 6 Anaerobic Biogas — Learnings (V108, March 10, 2026)

**Source:** wetSpring V108, 5 Liao group papers reproduced (Exp336-346, 183 checks)
**Connects to:** baseCamp #16 (Anaerobic-Aerobic QS Phase Transition), Paper 01 (Anderson-QS)

### What Was Validated

Track 6 adds four new kinetics models to the BarraCuda math library, all validated
through the full 6-tier chain (Paper→CPU→Python→GPU→Streaming→metalForge):

| Model | Equation | Domain |
|-------|----------|--------|
| Modified Gompertz | `H(t) = P * exp(-exp((Rm*e/P)*(λ-t) + 1))` | Biogas cumulative production |
| First-order kinetics | `B(t) = B_max * (1 - exp(-k*t))` | Cumulative yield |
| Monod growth | `μ = μ_max * S / (Ks + S)` | Microbial growth rate |
| Haldane inhibition | `μ = μ_max * S / (Ks + S + S²/Ki)` | Substrate inhibition with `S_opt = √(Ks * Ki)` |

Anderson W mapping for anaerobic communities confirmed: `W_digester > W_soil`,
meaning anaerobic digester communities are more disordered than aerobic soil
communities — consistent with reduced evenness and dominance by specialist
methanogens under oxygen-absent conditions. P(QS) comparison via `norm_cdf`
shows lower signal propagation probability in anaerobic regime.

### Key Insight: Anaerobic QS Is Physics

The five reproduced papers (Yang 2016, Chen 2016, Rojas-Sossa 2017/2019,
Zhong 2016) all describe bioprocess engineering outcomes (biogas yield, community
stability, substrate inhibition) that map directly to Anderson localization
parameters. Co-digestion improves evenness → lowers W → extends QS. Substrate
inhibition reduces evenness → raises W → localizes QS. Pretreatment (AFEX)
improves substrate accessibility → changes community structure → changes W.

This is the same physics as Paper 06 (no-till) and Paper 12 (immunological
Anderson) but in a controlled industrial bioreactor. The digester is the most
instrumented and reproducible system for testing the Anderson-QS model.

### What This Enables

1. **Paper 16 Stage 1 is complete** — all computational models validated, ready
   for real NCBI community data
2. **Kinetics models are reusable** — Gompertz/Monod/Haldane apply to any
   microbial growth system (gut, fermentation, wastewater)
3. **healthSpring gut modeling** gains Monod kinetics for bacterial growth and
   Haldane for substrate inhibition in the colon
4. **airSpring soil** gains Monod for rhizosphere microbial dynamics

---

## Staged Dataset Extension Roadmap (V108+)

### Tier 0: Already Referenced, Ready to Download (~hours, <10GB)

| Dataset | Accession | Scale | Extension |
|---------|-----------|-------|-----------|
| Cold seep 16S | PRJNA315684 (170 runs) | ~5GB raw | Track 6 Gompertz + Anderson W on real anaerobic communities |
| LTEE | PRJNA294072 | ~2GB | Time-series W evolution over 60,000 generations |
| Algae pond | PRJNA488170 | ~1GB | Aerobic reference for W comparison |
| Deep-sea vent | PRJNA283159 | ~3GB | Anaerobic/microaerophilic reference |

**Action:** NestGate `data.ncbi_fetch` or sovereign HTTP fallback.

### Tier 1: Published Data from Track 6 Papers (~days, 10-50GB)

The Liao group papers reference specific datasets:

- Yang 2016: 16S amplicon data from co-digestion reactors (supplementary or SRA)
- Chen 2016: Biogas yield curves + community composition tables (journal supplementary)
- Rojas-Sossa 2017/2019: Costa Rica deployment data, AFEX treatment data

**Action:** Search NCBI SRA for Liao group BioProjects (MSU BAE). Extract
published community composition tables from supplementary materials. These
become the real-data baselines for Track 6, replacing the synthetic proxy
communities in the validators.

### Tier 2: Large-Scale Atlases (~weeks, 50GB-2TB)

| Dataset | Scale | Compute | What It Unlocks |
|---------|-------|---------|-----------------|
| EMP (Earth Microbiome Project) | ~30K samples, 14 biomes | ~20 min GPU (diversity), ~4h full | Global W atlas: every biome's disorder fingerprint |
| Tara Oceans | 243 stations | ~2h GPU | Marine W gradient: surface (aerobic) → deep (anaerobic) |
| HMP | ~4,700 samples | ~1h GPU | Human gut W: mucosal (aerobic) → lumen (anaerobic) |
| KBS LTER | 30+ years, ~200GB | ~4h CPU | Temporal W evolution under no-till |

**Action:** LAN infrastructure (10G cables) or patient sequential download. EMP
is the highest-value target — 30K samples for W distribution analysis across
all 14 EMPO biomes.

### Tier 3: Sovereign Pipeline at NCBI Scale (~months, multi-TB)

| Dataset | Scale | Compute | What It Unlocks |
|---------|-------|---------|-----------------|
| Full SRA 16S surveys | 500-2000 BioProjects | Multi-day, multi-GPU | Global QS-disorder mapping |
| Cold seep full metagenomes | 170 × ~1GB each | ~170GB, GPU-parallel | Real 299K QS gene validation |
| ADREC collaboration data | Time-series from digesters | ~50GB | Paper 16 Stage 3 predictions |

---

## QS Gene Extension Axes (V108+)

### Current State

- 299,355 QS genes across 170 metagenomes, 34 QS types (Exp144-145)
- 6 QS systems: AHL (89.8K), AI-2 (74.8K), DSF (44.9K), DPD (29.9K), AIP (44.9K), HAI (15.0K)
- Validated: QS type vs Anderson geometry, frequency-division multiplexing model

### Extension Axes

1. **Anaerobic-specific QS genes** — Cross-reference 34 QS types with
   FNR/ArcAB/Rex regulon databases. Which QS genes are oxygen-regulated?
   Core of Paper 16.
2. **Gut QS atlas** — HMP gut metagenomes contain QS genes. Map onto the
   Anderson gut lattice (healthSpring Exp032). Gut mucosal O₂ gradient
   creates spatial W variation.
3. **Soil QS stratification** — EMP soil samples stratified by depth/moisture.
   Waterlogged = anaerobic = different QS gene expression. Connects Track 4
   (soil) to Track 6 (anaerobic).
4. **Fermentation QS** — Starter cultures (kimchi, sauerkraut, kefir) have
   characterized communities. Controlled anaerobic environments with known
   composition. Public 16S data available.
5. **Time-series QS** — LTEE (PRJNA294072) has 60,000 generations of E. coli
   evolution. QS gene gain/loss over evolutionary time.

### Data Requirements

- NCBI Protein database for QS gene families
- UniProt for FNR/ArcAB/Rex regulated gene lists
- Antibiotic Resistance Gene Database (ARDB) for QS-AMR co-occurrence

---

## Compute Budget Estimates (V108 Hardware)

| Workload | Single GPU (RTX 4070) | LAN (176GB VRAM) | Bottleneck |
|----------|-----------------------|-------------------|------------|
| Track 6 (5 papers, current) | 0.03ms per run | — | Done |
| Cold seep 170 metagenomes | ~2h diversity + W | ~15 min distributed | Download |
| EMP 30K samples diversity | ~20 min | ~3 min | Download |
| EMP 30K full pipeline | ~4h | ~30 min | Download |
| Tara 243 stations | ~30 min | ~5 min | Download |
| HMP 4,700 samples | ~1h | ~10 min | Download |
| SRA 2000 BioProjects | Multi-day | ~12h | Download |
| Full cold seep metagenomes | ~8h | ~1h | Download (170GB) |

The bottleneck is always data acquisition, not compute.

---

## ludoSpring Extensions (V18, March 15, 2026)

**Source:** ludoSpring V23 — 75 experiments, 1692 checks, 394 tests + 12 proptest + 6 IPC integration, Papers 17-22 in baseCamp
**Connects to:** baseCamp #17 (Game Design as Rigorous Science), #18 (RPGPT), #19 (Games@Home), #20 (Novel Ferment Transcript), Papers 01, 12, 13, 16

### What ludoSpring Brings to the Ecosystem

ludoSpring validates 13 foundational HCI models through the Python→Rust→GPU pipeline.
The key scientific finding — that Flow state discriminates game quality while engagement
alone does not — has implications for every spring that builds interactive systems:
medical UIs (healthSpring), lab dashboards (petalTongue), scientific visualization
(all springs).

V18 evolves ludoSpring into a first-class biomeOS niche citizen per the Spring-as-Niche
Deployment Standard. The `game` capability domain (12 methods) is registered with
semantic mappings via Neural API. Deploy graphs (`ludospring_deploy.toml`,
`ludospring_gaming_niche.toml`) and niche YAML (`ludospring-game.yaml`) are ready
for `biomeos deploy`. IPC handlers include `lifecycle.status` for primal discovery,
and `capability.list` returns operation dependencies and cost estimates for the
Pathway Learner. Clean SIGTERM shutdown with domain deregistration.

V15 built the GPU dispatch and mixed hardware foundation:
Tier A WGSL compute shaders (Perlin 2D, fBm, engagement batch, DDA raycaster) with
CPU parity validation. metalForge evolved to capability-based routing (SubstrateKind,
Capability enum, route(), fallback_chain — matching sibling spring pattern). NPU→GPU
direct PCIe transfer model. toadStool JSON-RPC 2.0 dispatch client wire format.
biomeOS DeploymentGraph (5-node topology, 60Hz budget). All modules ≥ 90% test
coverage. Clippy pedantic + nursery clean. `#![forbid(unsafe_code)]` everywhere.

V10-V13 added 22 new experiments (exp045-066) proving: ingestible ruleset architecture
(RPGPT), distributed human computation (Games@Home), provenance trio integration,
extraction shooter fraud detection (12 fraud types, zone topology), composable
primal architecture (biomeOS + songbird + petalTongue via JSON-RPC 2.0), Lysogeny
open recreation catalog (6 game mechanics from open math), Novel Ferment Transcript
(full NFT lifecycle), and cross-spring provenance (BearDog signing, field sample/medical
scaffolds, cross-domain fraud unification, radiating attribution).

### Completed Extension Axes

| Extension | Springs Involved | Experiments | Checks | Status |
|-----------|-----------------|-------------|--------|--------|
| NCBI QS gene pipeline | ludoSpring + nestgate | exp041 | 12 | **DONE** |
| Tower Atomic boot | ludoSpring + biomeOS + BearDog + Songbird | exp042 | 10 | **DONE** |
| QS gene dataset (20 genera) | ludoSpring + wetSpring | exp043 | 10 | **DONE** |
| Anderson QS interactive explorer | ludoSpring + wetSpring | exp044 | 12 | **DONE** |
| RPGPT: Ruleset control systems | ludoSpring + loamSpine | exp045 | 49 | **DONE** |
| RPGPT: Text adventure DAG | ludoSpring + rhizoCrypt | exp046 | 33 | **DONE** |
| RPGPT: MTG card provenance | ludoSpring + loamSpine + sweetGrass | exp047 | 23 | **DONE** |
| Games@Home: Stack resolution folding | ludoSpring | exp048 | 36 | **DONE** |
| Games@Home: Novel data combinatorics | ludoSpring | exp049 | 33 | **DONE** |
| Games@Home: Game tree design metric | ludoSpring | exp050 | 30 | **DONE** |
| Games@Home: Distributed computation | ludoSpring | exp051 | 28 | **DONE** |
| Provenance trio integration | ludoSpring + rhizoCrypt + loamSpine + sweetGrass | exp052 | 37 | **DONE** |
| Extraction shooter fraud detection | ludoSpring + rhizoCrypt + loamSpine | exp053 | 65 | **DONE** |
| Composable raid visualization | ludoSpring + biomeOS + songbird + petalTongue (IPC) | exp054 | 40 | **DONE** |
| Lysogeny catalog (6 mechanics) | ludoSpring | exp055-060 | 237 | **DONE** |
| Fermenting (NFT lifecycle) | ludoSpring + trio | exp061 | 89 | **DONE** |
| BearDog-signed provenance chain | ludoSpring + BearDog | exp064 | 39 | **DONE** |
| Field sample provenance (wetSpring) | ludoSpring + wetSpring scaffold | exp062 | 39 | **DONE** |
| Consent-gated medical (healthSpring) | ludoSpring + healthSpring scaffold | exp063 | 35 | **DONE** |
| Cross-domain fraud unification | ludoSpring | exp065 | 74 | **DONE** |
| Radiating attribution | ludoSpring + sunCloud | exp066 | 41 | **DONE** |
| Deep audit: coverage ≥ 90% all modules | ludoSpring | 212 tests | — | **DONE (V14)** |
| GPU dispatch: Tier A WGSL shaders | ludoSpring + barraCuda (exp030) | exp030 +8 | 24 | **DONE (V15)** |
| metalForge capability routing | ludoSpring (metalForge/forge) | 9 tests | — | **DONE (V15)** |
| Mixed hardware: NPU→GPU PCIe bypass | ludoSpring (exp032) | exp032 +6 | 18 | **DONE (V15)** |
| NUCLEUS: capability routing + toadStool dispatch + biomeOS graph | ludoSpring (exp033) | exp033 +8 | 19 | **DONE (V15)** |

### Key Architectural Lessons (V10)

**Composable vs chimeric dependencies**: Infrastructure primals (biomeOS, songbird,
petalTongue) are NOT Cargo dependencies. They communicate via JSON-RPC 2.0 over Unix
sockets. Data primals (rhizoCrypt, loamSpine, sweetGrass) ARE direct Cargo dependencies
because they provide pure data structures with no runtime side effects.

**Anti-cheat = chain-of-custody**: Proven concretely in exp053 with 12 fraud types.
The same orphan-item detector catches duped loot in an extraction shooter, phantom
samples in field genomics, and phantom swords in an RPG. Same DAG, same code path.

**Fraud detection as GPU workload**: Zone adjacency and `LoS` matrices are graph
operations suitable for GPU parallelization. Batched spatial fraud analysis is a
natural candidate for barraCuda GPU dispatch.

### GPU Promotion Path

ludoSpring has 8 Tier A modules ready for GPU promotion (pure math, embarrassingly
parallel). The pipeline is:

1. **Local validation** (complete) — all 75 experiments, 394 tests + 12 proptest, ≥ 90% coverage. Tier A WGSL shaders validated (exp030: Perlin, fBm, engagement, raycaster — 24/24 GPU parity)
2. **Niche deployment** (complete, V18) — UniBin binary, deploy graphs, niche YAML, Neural API domain registration, `lifecycle.status`, operation dependencies + cost estimates, dispatch metrics
3. **ToadStool GPU dispatch** — noise, raycaster, metrics batch on GPU. Wire format validated (exp033: JSON-RPC 2.0 compute.submit). metalForge capability routing ready for absorption.
4. **coralReef shader compilation** — sovereign WGSL→native for game workloads
5. **metalForge cross-substrate** — game pipeline stages dispatched to optimal hardware
6. **Fraud batching** — spatial fraud detectors as GPU compute shaders (new from exp053)

### NUCLEUS Integration Path

ludoSpring's game loop (60Hz) maps directly to biomeOS's continuous graph execution:

1. **Tower Atomic** — BearDog+Songbird discover ludoSpring capabilities
2. **Node Atomic** — ToadStool dispatches GPU noise/raycaster workloads
3. **Nest Atomic** — NestGate stores telemetry sessions, fetches NCBI data for cross-spring experiments
4. **Full NUCLEUS** — game_logic + metrics nodes tick against live primal data at 60Hz
5. **Composable deployment** — biomeOS `DeploymentGraph` with `Continuous` coordination pattern validated in exp054

### Connection to Existing Papers

| Paper | ludoSpring Extension |
|-------|---------------------|
| 01 (Anderson-QS) | Perlin noise fields as disorder landscape for interactive QS exploration |
| 12 (Immuno-Anderson) | Fitts/Hick for medical UI; DDA for treatment adaptation |
| 13 (Sovereign Health) | Engagement for patient compliance; flow for therapy design |
| 16 (Anaerobic-Aerobic QS) | Phase transition visualization through terrain generation |
| 17 (Game Design as Science) | All 13 HCI models apply directly to RPGPT session quality measurement |
| **18 (RPGPT)** | **exp045-047 validate ruleset ingestion, session DAG, card provenance. exp053 proves anti-cheat = chain-of-custody with 12 fraud types.** |
| **19 (Games@Home)** | **exp048-051 validate stack-as-folding, novel data, game tree metrics, distributed computation isomorphism. exp054 validates composable multi-player coordination architecture.** |
| **20 (Novel Ferment)** | **exp061 validates full NFT lifecycle. exp064 proves BearDog signing. exp065 proves cross-domain fraud unification (>80% structural similarity). exp066 proves radiating attribution (conservation of shares).** |

---

## RPGPT — Sovereign RPG Engine (Paper 18, March 11, 2026)

**Source:** ludoSpring architectural sketch + provenance trio (rhizoCrypt, sweetGrass, loamSpine)
**Connects to:** baseCamp #17 (Game Design as Science), #18 (RPGPT), Papers 01, 12, 13, 16

### The Isomorphism: Anti-Cheat = Chain-of-Custody

The same DAG operation serves all domains — only vocabulary changes:

| DAG Operation | Extraction Shooter | Field Genomics | Tabletop RPG |
|---------------|-------------------|----------------|-------------|
| Session start | Player spawns with loadout | Researcher enters field site | Session begins, characters loaded from loamSpine |
| Object creation | Item spawns in world | Sample collected from soil | Sword found in dungeon chest |
| Object transform | Weapon modded with parts | DNA amplified from sample | Sword enchanted with rune |
| Object transfer | Item traded to teammate | Sample handed to lab tech | Sword gifted to party member |
| Session end | Extract from raid | Submit to BioProject | Save to loamSpine, end session |
| Audit | No item without loot vertex | No reads without sample vertex | No sword without loot vertex |

Same rhizoCrypt. Same BLAKE3 Merkle integrity. Same BearDog signing. Different application.

### Ingestible Open Rulesets

The system ingests **any** open ruleset as a loamSpine certificate — a machine-readable
constraint document the AI must respect:

| System | License | What It Provides |
|--------|---------|-----------------|
| Pathfinder 2e | ORC (irrevocable) | 3-action economy, 4 degrees of success, conditions, proficiency tiers |
| FATE Core | CC-BY | Aspects (narrative tags with mechanical weight), Fate Points, fiction-first |
| Powered by the Apocalypse | CC-BY | Moves, partial success, GM principles |
| Cypher System | Cypher Open License | Single target number, GM intrusions, effort/edge |
| Cairn / Into the Odd | CC-BY-SA | Inventory-as-HP, direct damage, minimal rules |

Combined with **any world** (original or existing), this yields:
- Lord of the Rings + Pathfinder 2e = d20 campaign in Middle-earth
- Dune + FATE Core = Aspect-driven campaign on Arrakis
- Original world + Cypher = GM-intrusion-driven campaign in custom setting

The ruleset certificate constrains the AI absolutely — if the cert says "3 actions per turn"
the AI cannot grant 4. The constraint is provably anchored in loamSpine.

### Provenance Trio Evolution Goals (Cross-Domain Benefits)

RPGPT scaffolds evolution goals that benefit all domains:

**rhizoCrypt:**
- Turn-based session mode → multi-day field campaigns (wetSpring)
- Condition tracking with decay → sample degradation modeling (field genomics)
- Branch diff/merge → protocol variant comparison (lab science)
- Phase transitions → collect/transport/process/analyze lifecycle (field genomics)

**loamSpine:**
- Machine-readable ruleset certs → experimental protocol certs (lab science)
- Character sheet certs → instrument calibration certs (lab)
- NPC personality certs → reagent property certs (chemistry)
- Lending via slice mode → shared equipment checkout (lab)

**sweetGrass:**
- Multi-agent creative attribution → multi-lab collaboration tracking
- Narrative entity extraction → hypothesis/finding entities (science)
- Session contribution rollup → experiment contribution summary
- FATE Aspects as semantic entities → any freeform-tagged annotation system

### Build Phases

1. **Ruleset-as-certificate** — PF2e/FATE/Cypher mechanics as loamSpine certs
2. **Session DAG** — Turn structure, dice rolls, conditions, phases in rhizoCrypt
3. **AI narration loop** — Squirrel reads DAG + ruleset cert; ludoSpring measures quality
4. **Attribution + economics** — sweetGrass tracks player/AI creative contributions

---

## Novel Ferment Transcript Economics (Paper 20, March 13, 2026)

**Source:** ludoSpring exp061_fermenting (89/89 checks) + provenance trio + BearDog + sunCloud
**Connects to:** baseCamp #17 (Game Design), #18 (RPGPT), #19 (Games@Home), Papers 01, 12, 13

### The Evolution from Concept to Code

| Phase | Date | What | Status |
|-------|------|------|--------|
| Ethos | Jul 2025 | `LATENT_VALUE_ECONOMY.md` — value from significance | Concept |
| Model | Jul 2025 | `SUNCLOUD_ECONOMIC_MODEL.md` — radiating attribution | Concept |
| Certificate | Jul 2025 | `LOAM_CERTIFICATE_LAYER.md` — memory-bound objects | Concept |
| scyBorg | Mar 2026 | `SCYBORG_PROVENANCE_TRIO_GUIDANCE.md` — triple copyleft | Guidance |
| Fermenting | Mar 2026 | `exp061_fermenting` — working lifecycle + trading + memory | **Validated** |
| NFT Economics | Mar 2026 | Paper 20 — sunCloud + trio + cross-domain | **Published** |

### What Was Built (exp061)

- **Certificate lifecycle**: mint, inspect, trade, loan, return, consume
- **Trading protocol**: offer, accept, reject, cancel, atomic swap (loam-spine-core)
- **Object memory**: event timeline with PROV-O export (sweet-grass-core)
- **Composable IPC**: JSON-RPC wire types for live trio deployment
- **Deployment graph**: `provenance_node_atomic.toml` (Tower + Trio)

### What Needs Building

| Component | Team | Priority | Status |
|-----------|------|----------|--------|
| BearDog signing on every operation | BearDog | High | **Model validated (exp064)** — wire format proven, needs live IPC swap |
| Radiating attribution calculator | sweetGrass + sunCloud | High | **Model validated (exp066)** — decay, role weighting, conservation proven |
| Public chain anchor entry type | loamSpine | Medium | Pending |
| Owner inventory query | loamSpine | Medium | Pending |
| Cross-session derivation links | rhizoCrypt | Medium | Pending |
| License-aware attribution notices | sweetGrass | Medium | Pending |
| Physical-digital bridge (NFC/QR) | biomeOS | Low | Pending |
| Marketplace protocol | biomeOS | Low | Pending |

### Cross-Domain Applications

Same architecture, same code, different vocabulary:

| Domain | Object | History | Anchor Trigger |
|--------|--------|---------|---------------|
| Gaming | Tournament sword | Kills, trades, cosmetics | Sale or exhibition |
| Collectibles | Trading card | Tournament play, condition | Resale |
| Science | DNA sample | Collection → lab → analysis | Custody transfer |
| Medical | Patient record | Access log, treatment chain | Regulatory audit |
| Creative | Digital artwork | Creation process, remix chain | Sale |
| Legal | Property deed | Ownership transfers, liens | Recording |

### sunCloud Activation Path

1. Object accumulates history (local, free)
2. Owner optionally anchors to public chain (32-byte hash)
3. Anchor activates radiating attribution
4. sunCloud reads sweetGrass chain, distributes proportionally
5. Every contributor in the chain receives credit forever

---

## Cross-Spring Provenance Experiments (exp062-066, March 13, 2026)

**Source:** ludoSpring V14 — 5 cross-spring provenance experiments extending NFT architecture into wetSpring and healthSpring scaffolds (deep audit: 187 tests, 93.2% coverage)
**Connects to:** baseCamp #20 (NFT Economics), #21 (Sovereign Sample Provenance), #22 (Zero-Knowledge Medical Provenance)

### What Was Built

| Experiment | Checks | What It Proves |
|-----------|--------|---------------|
| exp064: BearDog-Signed Provenance Chain | 39/39 | Ed25519 signing on every trio operation. Chain verification. Tamper detection at exact position. IPC wire format validated. |
| exp062: Field Sample Provenance | 39/39 | Full sample lifecycle (collect → publish). 6 fraud types. DAG isomorphism with extraction shooter. wetSpring scaffold. |
| exp063: Consent-Gated Medical Access | 35/35 | Patient-owned records. Consent as scoped lending. 5 fraud types. Zero-knowledge access proofs. healthSpring scaffold. |
| exp065: Cross-Domain Fraud Unification | 74/74 | Same GenericFraudDetector across gaming/science/medical. 5 generic fraud types. >80% structural similarity. |
| exp066: Radiating Attribution Calculator | 41/41 | sunCloud value distribution. Decay models. Role weighting. Conservation (shares sum to 1.0). |

**Total**: 228 new checks, 0 failures.

### The Universality Proof (exp065)

The most significant result: the fraud detectors are NOT analogies. exp065 runs the
same `GenericFraudDetector` code on identically-structured DAGs labeled with three
different vocabularies (gaming, science, medical). The detected fraud types are
identical — only the domain names change:

| Generic | Gaming (exp053) | Science (exp062) | Medical (exp063) |
|---------|----------------|-------------------|-------------------|
| OrphanObject | OrphanItem | PhantomSample | PhantomAccess |
| DuplicateIdentity | DuplicateCert | DuplicateAccession | ConsentForgery |
| UnauthorizedAction | SpeedViolation | UnauthorizedAccess | UnauthorizedAccess |
| ScopeViolation | ImpossibleKill | MislabeledSpecimen | ScopeViolation |
| BrokenChain | UnattributedLoot | BrokenColdChain | ExpiredConsent |

This validates the core thesis from Paper 18 (RPGPT): anti-cheat IS chain-of-custody.

### What Needs Building Next

| Component | Team | Priority | Experiment |
|-----------|------|----------|-----------|
| Live BearDog IPC signing | BearDog | High | Replace exp064 model signatures with live crypto.sign_ed25519 |
| wetSpring pipeline adoption | wetSpring | High | Adapt exp062 SampleType/ProcessingStep to field genomics |
| healthSpring clinical adoption | healthSpring | High | Adapt exp063 RecordType to PK/PD/microbiome/biosignal/TRT tracks |
| BearDog ZK circuit | BearDog | Medium | Full zero-knowledge proofs for exp063 access control |
| Cross-institution provenance | songbird + biomeOS | Medium | Multi-lab / multi-provider consent chains |
| FHIR/HL7 interop | healthSpring + loamSpine | Medium | Map consent certificates to FHIR resources |
| ISO 17025 compliance matrix | wetSpring + loamSpine | Medium | Formal requirement → trio operation mapping |
| Patient portal | petalTongue | Low | Consent status + access history visualization |
| Public anchor for regulatory proof | loamSpine | Low | Blockchain anchoring for ISO/HIPAA compliance |

### Connection to Existing Papers

| Paper | New Connection |
|-------|---------------|
| 04 (Sentinels) | Sample monitoring extends sentinel architecture (exp062) |
| 09 (Field Genomics) | Direct scaffold for wetSpring sample processing (exp062) |
| 12 (Immuno-Anderson) | Medical access model for immunological data (exp063) |
| 13 (Sovereign Health) | Consent/access model for clinical tracks (exp063) |
| 16 (Anaerobic-Aerobic QS) | Sample chain-of-custody for digester studies (exp062) |
| 17 (Game Design) | Same provenance patterns, different domain vocabulary (exp065) |
| 18 (RPGPT) | Anti-cheat = chain-of-custody proven computationally (exp065) |
| 20 (NFT Economics) | Every sample and record is a Novel Ferment Transcript |

---

## airSpring V0.9.0 Audit Execution Learnings (March 18, 2026)

**Source:** airSpring V0.9.0 — 87 experiments, 894 lib + 299 integration tests, comprehensive audit execution
**Connects to:** baseCamp #03 (Precision Microbiome), #06 (No-Till Anderson), #08 (NPU IoT), #12 (Immunological Anderson), #16 (Anaerobic-Aerobic QS)

### Cast Module Pattern — Upstream Absorption Candidate

airSpring built a `cast` module with 9 type-safe numeric cast helpers (`usize_f64`, `f64_usize`, `u32_usize`, `u64_usize`, `u64_f64`, etc.) that replace raw `as` casts throughout the library. Combined with `#![deny(clippy::cast_precision_loss, clippy::cast_possible_truncation, clippy::cast_sign_loss)]` in `lib.rs`, this enforces safe casting at compile time while allowing pragmatic raw casts in validation binaries via Cargo.toml `[lints]`.

**Cross-ecosystem relevance:** Every spring has the same problem. neuralSpring has `safe_cast` (S162), healthSpring has `cast_helpers`. This is a strong barraCuda upstream absorption candidate — centralize once, all springs lean on it.

### Module Refactoring Pattern — Domain-Responsibility Split

`soil_moisture.rs` (672 LOC) was refactored into 4 submodules:

| Submodule | Responsibility | LOC |
|-----------|---------------|-----|
| `topp.rs` | Topp equation (permittivity to water content) | 127 |
| `texture.rs` | USDA soil texture classification + hydraulic props | 179 |
| `saxton_rawls.rs` | Saxton and Rawls 2006 pedotransfer functions | 216 |
| `water.rs` | PAW, SWD, irrigation trigger calculations | 90 |

Public API unchanged — `mod.rs` re-exports everything. Tests stay with their code. This is the correct pattern for splitting large modules across all springs: split by domain responsibility, not just line count.

### Three-Tier Discovery Pattern — Standard for All Primals

All primal discovery now follows: (1) environment override, (2) named socket scan, (3) capability probe. This eliminates hardcoded socket paths from deployment manifests and enables zero-configuration primal discovery via biomeOS socket resolution. Applied to: coralReef (shader), Squirrel (inference), petalTongue (visualization), toadStool (compute), nestGate (data).

### Benchmark JSON Provenance — Traceable Validation

Hardcoded Python baseline values were migrated from Rust source code to benchmark JSON files with provenance metadata (`baseline_script`, `baseline_commit`, `date`, `tolerance`). This makes every validation target traceable to the exact Python run that produced it.

### CI Lint Strategy — Cargo.toml as Single Source

Cargo.toml `[lints.clippy]` should be the single source of lint configuration. CLI flags like `-W clippy::pedantic` conflict with specific `allow` overrides. airSpring's CI now uses `cargo clippy --all-targets -- -D warnings` (no `-W` flags), letting Cargo.toml control all lint levels.

### What Papers Gain

| Paper | What V0.9.0 Adds |
|-------|-----------------|
| #03 (Microbiome) | soil_moisture module now cleanly separated for orchard theta(t) extensions |
| #06 (No-Till) | Benchmark provenance pattern for all Anderson coupling expected values |
| #08 (NPU IoT) | petalTongue discovery enables real-time NPU dashboard visualization |
| #12 (Immunological) | Cast safety in GpuDiversity and CytokineBrain numerical paths |
| #16 (Anaerobic QS) | Three-tier discovery for cross-spring soil O2 zonation pipeline |

## airSpring V0.10.0 Cross-Ecosystem Absorption Learnings (March 18, 2026)

### MCP Tool Definitions — Standard Pattern for All Springs

All springs should expose typed MCP tool definitions for Squirrel AI integration.
Pattern: `McpTool` struct with `name`, `description`, `input_schema`, plus `list_tools()`
and `tool_to_method()` dispatch. airSpring exposes 10 ecology tools; wetSpring exposes 8
life science tools. The struct and test patterns are identical — candidate for upstream
promotion to `barracuda::ipc::mcp`.

### Python Baseline Provenance Registry — Structured Traceability

`provenance.rs` with `PythonBaseline` records provides compile-time-checked provenance
for every validation binary. Categories: PythonParity, GpuParity, Analytical, Published.
Canonical commit epochs prevent drift. Both airSpring (11 records) and wetSpring (14 records)
use this pattern — candidate for shared upstream type.

### Kahan Compensated Summation — Delegate to barraCuda

`barracuda::shaders::precision::cpu::kahan_sum()` provides O(1) accumulation error.
Springs should use `eco::numerics::kahan_sum()` wrappers rather than `Iterator::sum()`
for precision-critical aggregation paths.

### ecoBin deny.toml — 14 C-Dependency Bans

Template for all springs: ban openssl-sys, libz-sys, zstd-sys, curl-sys, ring, native-tls,
libgit2-sys, libssh2-sys, bzip2-sys, lzma-sys, zlib-ng-sys, libdbus-sys, libsqlite3-sys.
Plus `unlicensed = "deny"` in `[licenses]`.

### Lint Convention Clarification

- `#[expect(reason)]` ONLY where the lint is **known** to fire (compile error if not)
- `#[allow(reason)]` for blanket test module suppressions (unwrap_used, expect_used)

### API Safety: assert! → Result in Public Libraries

All public library functions that validate input should return `Result<T, Error>`, not panic.
Pattern: `wind_speed_at_2m()` evolved from `assert!` to `Result<f64, InvalidInput>`.

### NaN-Safe Float Ordering

`f64::total_cmp` replaces `partial_cmp().unwrap_or(Equal)` everywhere.

### What Papers Gain from V0.10.0

| Paper | What V0.10.0 Adds |
|-------|-----------------|
| #01 (FAO-56 ET₀) | MCP tool `airspring_et0` enables Squirrel AI to compute ET₀ interactively |
| #03 (Microbiome) | `airspring_diversity` MCP tool for ecology-aware AI interpretation |
| #04 (Water Balance) | Provenance registry tracks exact Python baseline commit for WB validation |
| #06 (No-Till) | `airspring_dual_kc` MCP tool for cover crop coefficient queries |
| #09 (Richards) | `airspring_richards` MCP tool + kahan_sum for PDE accumulation precision |
| #14 (Climate Scenarios) | `airspring_spi_drought` MCP tool for drought analysis |
