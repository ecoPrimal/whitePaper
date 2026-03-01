# baseCamp: Independent Explorations Alongside the Constrained Evolution Thesis

**Date:** March 1, 2026
**Author:** Kevin Mok (BS Microbiology, MSU 2018; MS Data Science, MSU 2025)

---

## What This Is

These are independent scientific explorations that arose from applying the
ecoPrimals technology (BarraCuda, ToadStool, wetSpring, neuralSpring, hotSpring,
airSpring, groundSpring) to questions driven by curiosity and bench experience
rather than the specifics of the constrained evolution thesis. They are companion
papers, not thesis chapters.

Each document stands alone as a potential publication. Together they demonstrate
that the technology built for sovereign scientific computing produces real,
publishable science across multiple domains — from condensed matter physics
applied to microbiology, to agricultural biome engineering, to environmental
biosensing.

## How These Relate to the Main Thesis

The constrained evolution thesis (`thesis/03_theoretical_framework.md`) argues
that environmental constraints reshape fitness landscapes and drive
specialization. These baseCamp explorations are the scientific fruit of that
methodology: they were produced using the same constrained tools (Rust, GPU
via BarraCuda, validated against published papers) and they organically
connect back to constrained evolution where the biology demands it — but the
connection is never forced.

```
                    Main Thesis
            (Constrained Evolution)
                    │
        ┌───────────┼───────────┐
        │           │           │
     Theory      System    Validation
   (Chs 3-4)   (Chs 5-6)  (Chs 7-12)
                    │
            ────────┴────────
            │               │
      Spring Papers    baseCamp Papers
      (reproduce)      (explore)
```

Spring papers reproduce published work to validate the infrastructure.
baseCamp papers use that validated infrastructure to explore new science.

## The Papers

| # | Title | Domain | wetSpring Experiments | Key Finding | Status |
|---|-------|--------|---------------------|-------------|--------|
| 01 | Anderson Localization as QS Null Hypothesis | Physics × Microbiology | Exp107-156 (3,100+ checks), Exp170-182 (321 checks), Exp216-220 (130+ checks), **Exp251-255** (172 checks), **Exp256** (35 checks) | 3D geometry is necessary and sufficient for QS in diverse communities; 3 genuine NP solutions found; W_c = 16.26 ± 0.95 quantified; 26-domain CPU proof + 21-domain GPU portability + streaming + cross-substrate; **V86: EMP Atlas 30K proves at scale, NUCLEUS deployed, Genomic Vault organ model; cross-spring evolution validated (23/23 across 5 Springs)** | **Validated** — 260+ experiments, 50/50 three-tier |
| 02 | Extending the Frozen Fossil Record | Evolutionary Biology | Builds on Ch. 14 + Anderson anomaly catalog (Exp143) | Constrained evolution predictions for LTEE, permafrost, vent archives, agricultural time series | Proposal — predictions quantified |
| 03 | Precision Microbiome for Tree Crops | Agricultural Microbiology | Extension of Anderson model + Track 4 soil QS (Exp170-178) | Soil biome geometry guides inoculant design; rhizosphere W ≈ 6.7 (extended regime) | Proposal — Track 4 validates framework |
| 04 | Microbial Sentinels | Environmental Biosensing | Exp114-119, 123, 124, **193-195** (NPU), PFAS/algae | Community shifts as early-warning biosensors; **NPU validated on real AKD1000** (18.8K Hz, coin-cell 11 years, online evolution 136 gen/sec, PUF fingerprint) | **Validated on Live Hardware** — Pure Rust driver, Phase C sovereign |
| 05 | Cross-Species Signaling in Symbiotic Systems | Symbiotic Ecology | Exp142, 144-146 (cold seep + luxR phylogeny) | Mixed-species QS in lichen, rhizobia, coral; 299K QS genes across 170 metagenomes; eavesdropper enrichment confirmed | **Validated** — cold seep + phylogeny complete |
| 06 | Anderson Localization as the Mechanism Behind No-Till Soil Health | Soil Microbial Ecology × Physics | Track 4: Exp170-182 (321 checks), 9 papers + 10 Python baselines, full three-tier + airSpring Exp 047 GPU portability | Tillage = dimensional collapse of QS-active 3D pore network; **V86: NUCLEUS pipeline for field data, EMP Atlas confirms soil biomes, Genomic Vault for LTER soil DNA** | **Validated** — Track 4 complete, 50/50 three-tier |
| 07 | Sovereign Warm Dense Matter Simulation on Consumer GPU | Plasma Physics × Distributed Computing | hotSpring Tier 4 + neuralSpring surrogates + groundSpring uncertainty | WDM transport on $600 GPU; deconfinement at β_c=5.69 on $1,500 GPU; **11-head NPU GPU conductor** (Exp 023) | **Validated** — hotSpring v0.6.15 |
| 08 | Neuromorphic Edge Intelligence for Sovereign Agricultural IoT | Agricultural IoT × Neuromorphic Computing | airSpring Exp 028-029 (88+ checks) + Exp 047 GPU portability + wetSpring NPU driver | NPU inference at 0.0009% of active cycle energy; 10.7× more efficient than cloud; 1-min cadence unlocked; multi-crop hot-swap; GPU math portability proven (46/46 all 13 modules) | **Validated on Live Hardware** — AKD1000, streaming + evolution + power budget + ESN GPU conductor + GPU portability |
| 09 | Sovereign Field Genomics — Nanopore + NPU | Environmental Genomics × Edge Inference | wetSpring Exp193-195 (NPU) + Exp184-185 (16S) + Exp259 (vault) + planned Exp196-202 | MinION + AKD1000 + BarraCUDA = autonomous field sentinel. NPU-driven adaptive sampling (37x headroom). **V86: Genomic Vault organ model for MinION data sovereignty, NUCLEUS deployed (all 6 primals READY)** | **Architecture defined** — awaiting MinION hardware |
| 10 | First Dynamical QCD Production on Consumer GPU | Lattice QCD × Neuromorphic Computing | hotSpring Exp 024 (8⁴ dynamical, 1,031+ traj, 17 β points), Exp 025-027 | First NPU-steered dynamical fermion QCD scan. Smooth crossover confirmed (no first-order jump). β_c ~ 5.5 (shifted from quenched 5.692). NPU expanded 4-seed scan to 17 points. CG–disorder correlation validates Anderson proxy. 4D Wegner block model proposed. | **Complete** — 17 β points measured, smooth crossover confirmed, β_c ~ 5.5. Adaptive steering bug fixed in Exp 030. |
| 11 | The Nautilus Shell — Evolutionary Reservoir Computing from Bingo Boards | Reservoir Computing × Neuromorphic × Evolutionary Algorithms | primalTools/bingoCube/nautilus/ (31 tests, 5 examples) | Bingo boards as structured random projections; evolutionary generations replace temporal recurrence for feed-forward hardware; nautilus shell = layered evolutionary history, portable between instances. Column-range-preserving crossover maps natively to AKD1000 int4. Self-regulating drift monitor + edge seeding. AKD1000 int4 weight export. Quenched→dynamical transfer: 540× cost reduction. | **Validated** — 5.3% LOO CG error, 2.6% blind prediction on Exp 029, 31 tests, full brain rehearsal (save/restore/transfer/merge/AKD1000) |

## Reading Order

**For a microbiologist**: 01 (Anderson-QS, the headline result) → 05 (cross-species) → 03 (bioag) → 06 (no-till)

**For an ecologist**: 05 (symbiotic signaling) → 02 (LTEE extensions) → 04 (sentinels) → 06 (no-till)

**For a soil scientist or agronomist**: 06 (no-till Anderson mechanism) → 03 (tree crop inoculants) → 01 (underlying physics)

**For a physicist**: 01 (Anderson applied to biology) → 06 (dynamic Anderson with time series) → the wetSpring experiment docs (Exp107-143)

**For a plasma physicist**: 07 (sovereign WDM on consumer GPU) → 01 (Anderson framework) → the hotSpring paper queue (Tier 0–4)

**For a PhD committee**: 01 (demonstrates novel contribution) → 06 (applied to 60-year dataset) → 07 (WDM + distributed compute) → 02 (connects to LTEE proposal) → 03-05 (breadth) → 08 (NPU edge deployment)

**For an agricultural engineer**: 08 (NPU edge IoT) → 09 (field genomics) → 06 (no-till physics) → 03 (bioag microbiome) → 04 (sentinel monitoring)

**For a field genomics researcher**: 09 (field genomics) → 04 (sentinel concept) → 01 (Anderson detection signal) → 08 (NPU agricultural IoT) → the wetSpring experiment docs (Exp193-195, planned Exp196-202)

**For a structural biologist**: 10 (coralForge) → 02 (LTEE extensions) → 01 (Anderson-QS) → the `coralForge/` white paper series

**For the LTEE sequencing proposal**: 02 (LTEE extensions) → 10 (coralForge structural analysis) → Ch. 14 (biological validation) → 01 (Anderson-QS predictions)

## Bench Experience Behind These Papers

These explorations draw directly on the author's lab experience:

- **Bioeconomy Institute (5 years)**: Fermentation, bioreactors, BSL2 work with
  fungi, mycobacteria, anaerobes, GMOs. Informed Sub-thesis 03 (bioag) and 05
  (mixed systems).
- **Pivot Bio project**: Soybean root isolate as N-fixation probiotic. Directly
  informed the rhizosphere QS predictions in Sub-thesis 01 and 03.
- **Sandia National Lab**: Bacterial toxins on raceway algae, high-throughput
  sequencing. Informed Sub-thesis 04 (sentinel microbes, algal bloom prediction).
- **PFAS Research Lab (MSU)**: Forever chemicals in environmental samples.
  Informed Sub-thesis 04 (contamination biosensing).
- **Microbial Ecology Lab (undergrad)**: Rumen bacteria isolation, RDP analysis.
  Informed the diversity-disorder mapping in Sub-thesis 01.

## Data and Reproducibility

Experimental data is generated by Spring binaries (public, AGPL-3.0).
NCBI queries use the Entrez E-utilities API (via NestGate `NCBILiveProvider`).
Springs contributing validated infrastructure:

- **wetSpring**: Anderson QS, 16S pipeline, DADA2, taxonomy, NPU live, field genomics architecture, biomeOS IPC science primal, drug repurposing (Track 3), no-till soil QS (Track 4), Genomic Vault organ model (consent/provenance/encrypted storage), V86 ToadStool S70+++ rewire (6,656+ checks, 60 NPU on AKD1000, 260+ experiments, 52/52 papers, 50/50 three-tier, 1,247 tests, 97 named tolerances with provenance, 93 ToadStool primitives, 0 local WGSL, 0 unsafe code, 0 todo!/unimplemented!(), clippy pedantic CLEAN, 33.4× Rust vs Python, EMP Atlas 30K, NUCLEUS deployed — all 6 primals READY). Cross-spring evolution validated (23/23 checks across 5 Springs). ESN bridge to ToadStool esn_v2 enables bio multi-head classifiers. Deep debt elimination: all modules under 652 lines, 0 magic numbers, 0 unsafe, 0 mocks in production. New specs: `CROSS_SPRING_EVOLUTION.md` documents full shader lineage.
- **neuralSpring**: ML primitives (LSTM, HMM, transfer learning, spectral analysis,
  ESN reservoir computing), 25 papers + 5 WDM surrogates + coralForge (nF-01/02/03 AlphaFold3) + 3 pub experiments validated
  at 3,500+ checks, 685 lib tests, 216 binaries, **200/200 validators (all green)**,
  139+ named tolerances, 44 upstream rewires + 130+ barracuda import sites.
  **83.6× faster** than Python/NumPy (geomean, 11 domains; fastest 1104×).
  coralForge: sovereign structure prediction engine — Evoformer, IPA, diffusion, pairformer, confidence heads.
  S97d: ToadStool S70+++ cross-spring evolution validation (matmul_ref, SimpleMlp).
  S98: coralForge nF-03 GPU tier closed — AlphaFold3 diffusion + Pairformer GPU Tensor validators (26/26), pure GPU pipeline expanded (24/24), cross-spring evolution benchmark expanded (40/40).
  S99: NUCLEUS Tower validated on Eastgate. Primal handoffs: NestGate V1 (data acquisition), biomeOS V1 (NUCLEUS integration), Songbird V1 (networking). nS-01 Paper A real-data pipeline: weight\_loader.rs (safetensors, f16/bf16/f32→f64), validate\_weight\_spectral\_real 12/12 PASS. V66 ToadStool handoff.
  S95: +3 WDM GPU Tensor validators (transport, ESN, S(q,ω)) + AlphaFold3 confidence GPU validator.
  CPU→GPU portability proven (9/9, 7 domains). Phase 4 WGSL shader validation (22/22),
  ToadStool streaming spectral pipeline (28/28), NUCLEUS compute dispatch (39/39),
  ToadStool absorption readiness (294/294). Session 89: **dispatch parity 30/30
  (CPU↔GPU math identical for 26 operations), mixed-hardware dispatch 47/47 (NPU
  substrate + PCIe bridge + NUCLEUS atomics)**, 47 GPU-promoted Dispatcher ops
  (+3: HillGateGpu, MultiObjFitnessGpu, SwarmNnGpu wired to upstream BarraCUDA).
  42 metalForge WGSL shaders. 16 barracuda submodules exercised
- **hotSpring**: MD simulation, nuclear EOS, lattice QCD, transport, 11-head NPU GPU conductor (664+ tests, 80+ binaries, 62 WGSL shaders)
- **airSpring**: 8 ET₀ methods (PM, PT, HG, Makkink, Turc, Hamon, Thornthwaite, Blaney-Criddle),
  ensemble, bias correction, water balance, Richards PDE, isotherms, yield, scheduling,
  lysimeter, sensitivity, GDD, Saxton-Rawls pedotransfer, SCS Curve Number runoff,
  Green-Ampt infiltration, coupled runoff-infiltration (292/292), VG inverse (84/84),
  full-season WB audit (34/34), climate scenario analysis (46/46), 80yr decade analysis
  (102/102), NASS yield validation (99/99), Shannon H' diversity gradient (63/63),
  100-station Michigan Crop Water Atlas, CPU↔GPU parity, GPU math portability
  (13 modules, 46/46), metalForge mixed hardware dispatch, Titan V GPU live dispatch,
  Anderson cross-spring coupling, NCBI 16S soil-moisture coupling, ToadStool S70+ fully
  rewired,   NUCLEUS primal (16 capabilities, JSON-RPC, 28/28 cross-primal pipeline),
  ecology domain in biomeOS capability registry, capability.call neural-api routing,
  cross-primal forwarding (ToadStool, BearDog, Songbird), primal discovery,
  ecology.full_pipeline (ET₀→WB→yield single-call), biomeOS graph executor
  capability_call wired (fixes all science pipeline graphs)
  (v0.5.9: 1237 Python + 817 Rust lib tests + 1498 atlas checks, 73 binaries,
  63 experiments, 44/44 cross-spring evolution benchmark, Richards PDE rewired to
  `barracuda::linalg::tridiagonal_solve`, configurable `RichardsConfig`, shared `biomeos`
  module, `lifecycle.health` wateringHole-compliant, zero mocks in production,
  capability-based discovery everywhere, 17 Tier A + 7 Tier B GPU orchestrators,
  seasonal pipeline GPU Stages 1-2 + streaming (GpuPipelined/GpuFused), GPU stats
  (neuralSpring S69), atlas stream, MC ET₀ GPU path,
  `validate_pure_gpu` 16/16, `validate_gpu_math` 46/46,
  `validate_gpu_rewire_benchmark` 26/26, `validate_climate_scenario` 46/46,
  `validate_atlas_decade` 102/102, `validate_nass_real` 99/99,
  `validate_ncbi_diversity` 63/63, `validate_nucleus` 29/29,
  `validate_nucleus_pipeline` 28/28 (cross-primal: ecology domain, neural-api routing,
  ToadStool/BearDog forwarding, primal discovery, 7 discovered primals),
  metalForge 18 workloads + cross-system routing (GPU+NPU+CPU) 29/29 + 21/21 PASS,
  Titan V 24/24, 5 live substrates, 14.5× Rust vs Python (21/21 parity),
  35/35 cross-spring benchmarks, 42+ named constants, zero dead code, zero unsafe,
  zero mocks, zero todo, capability-based GPU discovery, pure Rust data providers
  (OpenMeteo + USDA NASS via ureq), `airspring_primal` NUCLEUS integration,
  biomeOS ecology domain + capability_call graph execution,
  ToadStool S70+++: ops 5-8 GPU-first, streaming pipeline, climate scenario)
- **groundSpring**: Uncertainty quantification, noise labels, spectral theory (Anderson 1D/2D/3D, Almost-Mathieu, band edge, Lanczos sparse eigensolver), transport, quasispecies, rare biosphere, jackknife, freeze-out (+ decomposed chi2 analysis), spectral recon, WDM precision/convergence/vendor-parity, ESN regime classification, nonlinear regression, NPU Anderson regime classification, **biomeOS Neural API live** (Tower + Node + Squirrel validated), **NestGate data pipelines** (NCBI, NOAA GHCND, IRIS FDSN), Hargreaves ET₀ + crop coefficient + soil water balance (airSpring cross-spring), Brent root-finder band edge refinement (32 experiments, 347/347 Rust validation checks — 292 core + 55 NUCLEUS, 613 workspace tests, 10 domains; live hardware: RTX 4070, Titan V, AKD1000 NPU; **61 active barracuda delegations (38 CPU + 19 GPU + 4 cross-spring S59+)**, 1 evolution candidate; V58: cross-spring evolution — ESN (wetSpring), Lanczos (hotSpring), 2D/3D Anderson eigenvalues (hotSpring), chi2 decomposed (hotSpring nuclear), disorder sweep; deep-debt completion — zero unsafe, zero mocks, zero production unwrap, FAMILY_ID evolution, DRY refactoring; NUCLEUS integration — biomeOS `capability_call` semantic routing, NestGate data providers, 4 NUCLEUS experiments (Exp 029–032); 19 metalForge workloads, 5+ substrates, architecture-aware GPU routing; ToadStool S70+++; clippy::pedantic clean, zero warnings all feature modes)

Every experiment can be reproduced with the corresponding Spring's binaries:

```bash
# wetSpring experiments (Anderson QS, 16S, metagenomics)
cd wetSpring/barracuda && cargo run --release --features gpu --bin <binary_name>

# neuralSpring experiments (ML, spectral, surrogates)
cd neuralSpring && cargo run --release --bin <binary_name>

# hotSpring experiments (MD, nuclear EOS, lattice QCD)
cd hotSpring && cargo run --release --features gpu --bin <binary_name>
```

No proprietary data. No restricted access. No institutional dependencies.

## Cross-Spring Coordination

baseCamp papers are where springs meet. Each paper draws from multiple springs,
and future work on any spring is guided by what the baseCamp science needs.
This makes baseCamp the indirect coordination layer for the ecosystem.

```
                         baseCamp Papers
                              │
    ┌─────────────────────────┼─────────────────────────┐
    │                         │                         │
Paper 01 (Anderson QS)  Paper 06 (No-Till)         Paper 07 (WDM)
 wetSpring              wetSpring                   hotSpring
 hotSpring (spectral)   airSpring (ET₀)             neuralSpring (surrogates)
 groundSpring (spectral groundSpring (uncertainty   groundSpring (freeze-out
   theory validation)     bridge, rare biosphere)     inverse, spectral recon,
 neuralSpring (ESN)     neuralSpring (LSTM)           jackknife error bars)
    │                         │                         │
    │                         │                         │
Paper 04 (Sentinels)   Paper 03 (BioAg)           Paper 05 (Cross-Species)
 wetSpring (NPU)        wetSpring (Anderson)        wetSpring (metagenomes)
 neuralSpring (ESN)     airSpring (soil moisture)   neuralSpring (HMM)
 hotSpring (Akida)      groundSpring (sensor        groundSpring (transport,
 groundSpring (sensor     calibration, rare           band edge, quasispecies)
   noise, uncertainty)    biosphere, jackknife)
                              │
                        Paper 02 (LTEE)
                         wetSpring (16S)
                         neuralSpring (HMM, ESN)
                         groundSpring (drift vs
                           selection, quasispecies,
                           rare biosphere, jackknife)

Paper 08 (NPU Ag IoT)  Paper 09 (Field Genomics)
 airSpring (sensors)     wetSpring (16S, NPU, PFAS,
 wetSpring (NPU driver)    alignment, Anderson QS)
 neuralSpring (LSTM)     airSpring (soil sensors)
                         neuralSpring (ESN/LSTM)
                         groundSpring (rare biosphere,
                           uncertainty budgets)
                         hotSpring (akida-driver)
```

**What each spring contributes:**

| Spring | Contributes To | Key Primitives |
|--------|---------------|----------------|
| wetSpring | 01, 03, 04, 05, 06 | Anderson QS, diversity, Bray-Curtis, FASTA, NCBI, NPU int8 |
| hotSpring | 01, 07 | Spectral theory (Lanczos, Anderson 3D), GPU MD, lattice QCD |
| airSpring | 03, 06, **08** | FAO-56 ET₀ (8 methods incl. Blaney-Criddle), SCS-CN runoff, Green-Ampt infiltration, soil moisture, Richards PDE, **NPU int8 eco classifiers, IoT sensor pipeline**, GPU orchestrators (17 Tier A + 7 Tier B + streaming pipeline + GPU stats), GPU math portability (13 modules, 46/46), metalForge cross-system dispatch (18 workloads, GPU+NPU+CPU), Anderson cross-spring coupling, climate scenario analysis, 14.5× Rust vs Python (21/21 parity), **NUCLEUS primal (16 capabilities, ecology domain, cross-primal forwarding, 28/28 pipeline)** |
| neuralSpring | 01, 02, 04, 05, 06, 07 | ESN/LSTM anomaly detection, WDM surrogates, HMM, transfer learning |
| groundSpring | **01, 02, 03, 04, 05, 06, 07, 08, 09** | Spectral theory validation (Anderson, Almost-Mathieu, band edge, transport), uncertainty budgets, sensor noise calibration, rare biosphere, jackknife error bars, freeze-out inverse, spectral recon, drift vs selection, quasispecies threshold, WDM precision/convergence/vendor-parity, **NPU Anderson regime classification (AKD1000)**, metalForge cross-substrate validation |

groundSpring now contributes to ALL 9 baseCamp papers — reflecting the expansion
from 5 experiments (sensor noise only) to 32 experiments across 10 scientific
domains including live NPU hardware and NUCLEUS primal interaction. The spectral theory experiments (008, 009,
012, 018) validate the Anderson framework underlying papers 01, 05, and 06.
Full NUCLEUS is now operational on Eastgate with all 6 primals (BearDog, Songbird,
ToadStool, NestGate, Squirrel, Neural API), enabling end-to-end primal
orchestration and data acquisition for baseCamp paper extensions.
The Bazavov experiments (019-021) connect directly to paper 07's lattice QCD
science. The evolutionary biology experiments (014, 016, 017) serve papers 02
and 04. The cross-spring uncertainty experiments (022-024) validate the
no-till Anderson pipeline: ET₀→ξ propagation (Exp 022), no-till vs tilled
16S diversity loss (Exp 023), and aggregate stability noise floors (Exp 024),
directly supporting paper 06. The WDM experiments (025-027) provide the
uncertainty budget for paper 07's consumer GPU claims. Exp 028 (NPU Anderson classification on AKD1000)
directly validates the edge deployment architecture for papers 04, 08, and 09.
The metalForge cross-substrate validation (CPU + GPU + NPU parity on Anderson
localization) proves the mathematical portability that the entire baseCamp
program depends on.

**What each paper needs next (guides spring evolution):**

| Paper | Open Question | Springs Involved |
|-------|--------------|-----------------|
| 01 | DF64 Anderson at L=14-20 (large lattice, higher precision) | wetSpring × hotSpring × **groundSpring** (spectral validation at extended precision) |
| 02 | LTEE frozen fossil sequencing + sdiA expression | wetSpring × neuralSpring × **groundSpring** (drift vs selection quantification, jackknife error bars) |
| 03 | Pistachio/almond field inoculant trial design | wetSpring × airSpring × **groundSpring** (sensor calibration + rare biosphere monitoring of inoculant persistence) |
| 04 | Real-time HAB sentinel deployment (edge NPU) — **LIVE on AKD1000** | wetSpring × hotSpring (Akida) × **groundSpring** (uncertainty budget for detection threshold calibration, **NPU Anderson classification validated on live AKD1000 Exp 028**). V60: 3 ESN classifiers live, online evolution, PUF fingerprint, temporal streaming |
| 05 | Cross-kingdom metagenome 170-sample QS gene scan | wetSpring × neuralSpring × **groundSpring** (transport models for mycorrhizal relay) |
| 06 | Brandt farm real soil time series → r(t) prediction | wetSpring × airSpring × neuralSpring × **groundSpring** (uncertainty bridge: sensor → ξ → r) |
| 07 | WDM transport S(q,ω) at 10 densities; **Exp 023 full-pipeline production run** | hotSpring × neuralSpring × **groundSpring** (spectral reconstruction + freeze-out + jackknife for lattice QCD observables; NPU GPU-conductor validation) |
| 08 | High-cadence NPU pipeline + field integration | airSpring (sensor + water balance) × wetSpring (NPU driver + ESN) × neuralSpring (LSTM time series) × **groundSpring** (NPU DMA validation, cross-substrate parity proof, uncertainty budget) |
| 09 | Nanopore + NPU field genomics end-to-end | wetSpring (16S + NPU + PFAS ML + alignment) × airSpring (soil sensors) × neuralSpring (ESN/LSTM) × **groundSpring** (rare biosphere + uncertainty + **metalForge cross-substrate dispatch validation**) |

## Future Contributions

### Immediate (V81 + airSpring v0.5.8 — DONE)

- **airSpring Pipeline Coupling + Inverse Problems (DONE, v0.5.6)**: 3 new coupled
  experiments — SCS-CN + Green-Ampt rainfall partitioning (292/292), VG inverse via
  Brent root-finding (84/84), full-season WB audit (34/34). Validates that validated
  modules compose correctly for end-to-end pipelines.
- **airSpring GPU Evolution Pipeline (DONE, v0.5.6)**: 4 ops GPU-first rewired
  (Hargreaves op=6, Kc climate op=7, dual Kc op=8, sensor cal op=5) with
  CPU fallback → GPU auto-activate on ToadStool absorption. Seasonal pipeline
  (ET₀→Kc→WB→Yield chained). Atlas stream for multi-year regional ET₀.
  MC ET₀ GPU path. `validate_pure_gpu` (16/16), `validate_dispatch` (29/29).
- **airSpring Science Extensions + Streaming (DONE, v0.5.7)**: Exp 058 Climate
  Scenario Analysis (46/46 PASS, CMIP6-style offsets on FAO-56 chain). Streaming
  pipeline backends (GpuPipelined, GpuFused). GPU stats module (neuralSpring S69).
  21/21 CPU parity (14.5× speedup). Technical debt: zero magic numbers (Turc
  constants promoted), zero unsafe, zero mocks, zero todo.
  68 binaries, 58 experiments, 641 lib tests.
- **V66 Deep Audit + Dispatch Evolution (DONE)**: Byte-native FASTQ I/O,
  bytemuck nanopore, streaming APIs (mzML/MS2/FASTQ), safe env (`temp_env`),
  tolerance centralization (92 constants), `total_cmp` migration. Dispatch
  evolution Exp213 (49/49), NUCLEUS V8 Exp214 (49/49), CPU vs GPU v5 Exp215
  (built, awaiting GPU). Total: 216 experiments, 5,251+ checks, ALL PASS.
- **V67 Experiment Buildout + Evolution (DONE)**: 10 new Python baselines
  (Track 4 soil papers + NPU spectral triage), Exp216 (47-domain CPU proof),
  Exp217 (Python-vs-Rust benchmark), Exp218 (42-module GPU portability),
  Exp219 (unidirectional streaming pipeline), Exp220 (cross-substrate dispatch
  V67 + BandwidthTier). 11 extension papers promoted to three-tier (50/50).
  Total: 221 experiments, 5,421+ checks, 1,081+ tests, ALL PASS.
- **biomeOS IPC Integration (DONE)**: Science primal server with JSON-RPC 2.0,
  Songbird registration, Neural API metrics, GPU-aware dispatch routing via
  lazy `OnceLock<GpuF64>` + dispatch threshold. Exp203-208, 321 checks PASS.
- **Cross-Spring Modern Rewiring (DONE, V64)**: `Fp64Strategy` and
  `optimal_precision()` wired in `GpuF64`, 6 GPU modules migrated to
  `submit_and_poll()` for device-lost resilience. Exp210 cross-spring
  evolution benchmark (24/24 PASS, 5-spring provenance).
- **Progression Benchmark (DONE, V65)**: Full Python → CPU → GPU → streaming
  → metalForge progression on unified workload. Exp211 (16/16 PASS). Rust/CPU
  27× faster than Python, chained GPU GEMM, metalForge workload-aware routing.
- **Comprehensive Green Sweep (DONE)**: Full pipeline validated from Python
  baselines (27× speedup) through metalForge cross-substrate. 216 experiments,
  5,251+ checks, 1,073+ tests, ALL PASS.
- **NPU Live (DONE)**: 3 ESN classifiers validated on real AKD1000 hardware
  (Exp193-195). Online evolution at 136 gen/sec, PUF fingerprinting (6.34 bits),
  12.9K Hz temporal streaming. Coin-cell viable (1.4 µJ/infer).
- **Field Genomics Architecture (DONE)**: Sub-thesis 06 defines MinION +
  AKD1000 + BarraCUDA for autonomous environmental sentinels. Experiments
  196-202 planned pending sequencer hardware.
- **V72-V75 Five-Tier Chain + ComputeDispatch (DONE)**: Exp224-228 five-tier
  validation chain (paper math → CPU → GPU → streaming → metalForge). V75:
  ComputeDispatch builder adopted in 6 GPU modules, BatchedMultinomialGpu +
  DiversityFusionGpu for rarefaction, PairwiseL2Gpu + FstVariance new modules.
  82 primitives consumed. 229 experiments, 5,743+ checks, 1,148 tests.
- **V76 Deep Codebase Audit + Evolution (DONE)**: Comprehensive audit of
  linting, formatting, clippy pedantic, coverage, unsafe code, sovereignty,
  dependency health, file sizes, mocks, tolerance provenance. Workspace
  configuration unified. 14 new named tolerances. 62 new metalForge/forge
  tests (73% → 84% coverage). Zero unsafe, zero todo, zero mocks in
  production. 97 named tolerances with full provenance. 95.86% line coverage.
- **V80 Extended Evolution Chain (DONE)**: 19 domains × 4 tiers. CPU v17
  (+chimera, +DADA2, +alignment, +ESN, +GBM, +DTL, +clock, +RF), GPU v9
  (16 GPU workloads), Streaming v7 (6-stage ToadStool), metalForge v11
  (23-workload catalog: 16 GPU + 3 NPU + 4 CPU). Exp239-242, 114 checks.
- **V81 CPU↔GPU Parity + Dispatch + PCIe + NUCLEUS (DONE)**: CPU vs GPU v6
  (22 domains head-to-head, math truly portable), ToadStool Dispatch v2
  (streaming overhead proof, GpuPipelineSession pre-warmed), PCIe Bypass
  (NPU→GPU direct, bandwidth-aware routing, mixed pipeline topology),
  NUCLEUS v2 (49 workloads, Tower+Nest+Node extended, biomeOS sovereign
  fallback). Exp243-246, 144 checks. 247 experiments, 6,273+ checks total.

### Medium-term

- **NUCLEUS local deployment (DONE)**: biomeOS Tower + Node running on Eastgate.
  airSpring registered as ecology primal (16 capabilities), capability.call routing
  via neural-api, cross-primal forwarding to ToadStool/BearDog/Songbird.
  capability_call node type wired in graph executor (fixes all science pipeline graphs).
  7 primals discovered, 28/28 cross-primal pipeline validation (Exp 063).
  ecology domain added to biomeOS capability_registry.toml + capability_domains.rs.
  airspring_ecology_pipeline.toml graph defined (weather → ET₀ → WB → yield).
- **NestGate NCBI integration**: NestGate's `NCBILiveProvider` (E-utilities:
  ESearch, ESummary, EFetch) for sovereign data acquisition. Content-addressed
  storage (BLAKE3) for reference databases (SILVA, RefSeq, NCBI nt). SRA
  toolkit integration for bulk FASTQ download is the missing piece.
  Next: NestGate Unix socket NUCLEUS integration (currently HTTP standalone).
- **GPU Lanczos kernel**: `barracuda::spectral::lanczos` is CPU-bound (~457ms
  for L=8). A WGSL Lanczos would eliminate this bottleneck for Anderson spectral.
- **DF64 Anderson**: Extended precision (f64-pair) for large Anderson
  lattices (L=14-20). Phase 2 will use DF64 shaders from hotSpring.
- **Cross-spring shared tolerances**: wetSpring's 92 named tolerance
  constants (with provenance) as a pattern for all springs.

### Long-term

- **metalForge cross-substrate**: GPU→NPU→CPU dispatch for heterogeneous
  workloads. NPU handles streaming sentinel inference while GPU handles
  batch Anderson spectral analysis.
- **LTEE validation**: Sequencing data from Lenski's frozen fossil record
  to test constrained evolution predictions (Paper 02).
- **Field deployment**: Sentinel microbe prototype using Akida NPU for
  real-time HAB prediction (Paper 04).
- **Field genomics (Paper 09)**: MinION nanopore sequencer as a new
  metalForge substrate class (SEQ). Sovereign Rust pipeline from raw
  signal to classified community state: MinION → BarraCUDA 16S → AKD1000
  NPU classification → adaptive sampling feedback. Target deployments:
  Great Lakes HAB monitoring (Saginaw Bay / Lake Erie), soil health
  sentinel for no-till monitoring, AMR wastewater surveillance, PFAS
  dual-mode detection. NPU-driven adaptive sampling provides 37x headroom
  over MinION read generation. New BarraCUDA modules: `io::nanopore`
  (FAST5/POD5 reader), `bio::basecall` (signal → base). All downstream
  math operational (5,061+ checks). Experiments 196-202 planned.
