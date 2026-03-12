# baseCamp Extension Plan: Technical Learnings and Evolution

**Date:** March 11, 2026 (V113 update)
**Foundation:** baseCamp papers 01–16, barraCuda v0.3.5 standalone (wgpu 28), wetSpring V113 (370 experiments, 9,886+ checks, 63 papers, paper extension roadmap: EMP 28K atlas + Liao real data + KBS LTER temporal + QS gene profiling + primal pipeline + P1 framework + LAN mesh plan + NVIDIA hardware learning + PrecisionBrain bio routing + petalTongue viz + Anderson QS O₂-modulated model), airSpring v0.7.5

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

## ludoSpring Extensions (V6, March 11, 2026)

**Source:** ludoSpring V6 — 44 experiments, 410 checks, Paper 17 in baseCamp
**Connects to:** baseCamp #17 (Game Design as Rigorous Science), Papers 01, 12, 13, 16

### What ludoSpring Brings to the Ecosystem

ludoSpring validates 13 foundational HCI models through the Python→Rust→GPU pipeline.
The key scientific finding — that Flow state discriminates game quality while engagement
alone does not — has implications for every spring that builds interactive systems:
medical UIs (healthSpring), lab dashboards (petalTongue), scientific visualization
(all springs).

V6 adds 4 cross-spring experiments proving the game-science metrics generalize to
bioinformatics exploration and primal infrastructure coordination.

### Cross-Spring Extension Axes

| Extension | Springs Involved | New Experiments | Compute | Status |
|-----------|-----------------|-----------------|---------|--------|
| NCBI QS gene pipeline | ludoSpring + nestgate | exp041 (12/12) | CPU, ~80s (rate-limited) | **DONE** |
| Tower Atomic boot | ludoSpring + biomeOS + BearDog + Songbird | exp042 (10/10) | CPU only, <1s | **DONE** |
| QS gene dataset (20 genera) | ludoSpring + wetSpring | exp043 (10/10) | CPU, ~80s (rate-limited) | **DONE** |
| Anderson QS interactive explorer | ludoSpring + wetSpring | exp044 (12/12) | CPU only, <1s | **DONE** |
| Immune response as game | ludoSpring + healthSpring | exp045 | CPU only, <1s | Planned |
| Patient engagement metrics | ludoSpring + healthSpring | exp046 | CPU only, <1s | Planned |
| Phase transition visualization | ludoSpring + wetSpring | exp047 | CPU only, <1s | Planned |
| Interactive microbial landscape | ludoSpring + wetSpring | exp048 | GPU (noise fields) | Planned |
| Engagement-driven scientific viz | ludoSpring + petalTongue | exp049 | CPU only | Planned |
| Sovereign game science on consumer HW | ludoSpring + barraCuda + metalForge | exp050 | GPU benchmarks | Planned |
| **RPGPT: Ruleset-as-certificate** | ludoSpring + loamSpine | Paper 18, Phase 1 | CPU only | **Architecture defined** |
| **RPGPT: Turn-based session DAG** | ludoSpring + rhizoCrypt | Paper 18, Phase 2 | CPU only | **Architecture defined** |
| **RPGPT: AI narration loop** | ludoSpring + Squirrel + loamSpine | Paper 18, Phase 3 | CPU only | **Architecture defined** |
| **RPGPT: Creative attribution** | ludoSpring + sweetGrass + sunCloud | Paper 18, Phase 4 | CPU only | **Architecture defined** |

### GPU Promotion Path

ludoSpring has 8 Tier A modules ready for GPU promotion (pure math, embarrassingly
parallel). The pipeline is:

1. **Local validation** (current) — all 40 experiments on CPU
2. **ToadStool GPU dispatch** — noise, raycaster, metrics batch on GPU
3. **coralReef shader compilation** — sovereign WGSL→native for game workloads
4. **metalForge cross-substrate** — game pipeline stages dispatched to optimal hardware

### NUCLEUS Integration Path

ludoSpring's game loop (60Hz) maps directly to biomeOS's continuous graph execution:

1. **Tower Atomic** — BearDog+Songbird discover ludoSpring capabilities
2. **Node Atomic** — ToadStool dispatches GPU noise/raycaster workloads
3. **Nest Atomic** — NestGate stores telemetry sessions, fetches NCBI data for cross-spring experiments
4. **Full NUCLEUS** — game_logic + metrics nodes tick against live primal data at 60Hz

### Connection to Existing Papers

| Paper | ludoSpring Extension |
|-------|---------------------|
| 01 (Anderson-QS) | Perlin noise fields as disorder landscape for interactive QS exploration |
| 12 (Immuno-Anderson) | Fitts/Hick for medical UI; DDA for treatment adaptation |
| 13 (Sovereign Health) | Engagement for patient compliance; flow for therapy design |
| 16 (Anaerobic-Aerobic QS) | Phase transition visualization through terrain generation |
| 17 (Game Design as Science) | All 13 HCI models apply directly to RPGPT session quality measurement |
| **18 (RPGPT)** | **Sovereign RPG engine: ingestible rulesets, provenance-backed world state, anti-cheat = chain-of-custody** |

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
