# baseCamp: Independent Explorations Alongside the Constrained Evolution Thesis

**Date:** March 5, 2026 (standalone barraCuda v0.3.1, wetSpring V96, hotSpring v0.6.17+, neuralSpring V82, groundSpring V76)
**Author:** Kevin Mok (BS Microbiology, MSU 2018; MS Data Science, MSU 2025)

---

## What This Is

These are independent scientific explorations that arose from applying the
ecoPrimals technology (barraCuda, toadStool, wetSpring, neuralSpring, hotSpring,
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
| 01 | Anderson Localization as QS Null Hypothesis | Physics × Microbiology | Exp107-156 (3,100+ checks), Exp170-182 (321 checks) | 3D geometry is necessary and sufficient for QS in diverse communities; 3 genuine NP solutions found; W_c = 16.26 ± 0.95 quantified | **Validated** — 197 experiments, full three-tier |
| 02 | Extending the Frozen Fossil Record | Evolutionary Biology | Builds on Ch. 14 + Anderson anomaly catalog (Exp143) | Constrained evolution predictions for LTEE, permafrost, vent archives, agricultural time series | Proposal — predictions quantified |
| 03 | Precision Microbiome for Tree Crops | Agricultural Microbiology | Extension of Anderson model + Track 4 soil QS (Exp170-178) | Soil biome geometry guides inoculant design; rhizosphere W ≈ 6.7 (extended regime) | Proposal — Track 4 validates framework |
| 04 | Microbial Sentinels | Environmental Biosensing | Exp114-119, 123, 124, **193-195** (NPU), PFAS/algae | Community shifts as early-warning biosensors; **NPU validated on real AKD1000** (18.8K Hz, coin-cell 11 years, online evolution 136 gen/sec, PUF fingerprint) | **Validated on Live Hardware** — Pure Rust driver, Phase C sovereign |
| 05 | Cross-Species Signaling in Symbiotic Systems | Symbiotic Ecology | Exp142, 144-146 (cold seep + luxR phylogeny) | Mixed-species QS in lichen, rhizobia, coral; 299K QS genes across 170 metagenomes; eavesdropper enrichment confirmed | **Validated** — cold seep + phylogeny complete |
| 06 | Anderson Localization as the Mechanism Behind No-Till Soil Health | Soil Microbial Ecology × Physics | Track 4: Exp170-182 (321 checks), 9 papers, full three-tier | Tillage = dimensional collapse of QS-active 3D pore network; CPU + GPU + metalForge validated | **Validated** — Track 4 complete |
| 07 | Sovereign Warm Dense Matter Simulation on Consumer GPU | Plasma Physics × Distributed Computing | hotSpring Tier 4 + neuralSpring surrogates + groundSpring uncertainty | WDM transport on $600 GPU; deconfinement at β_c=5.69 on $1,500 GPU; **11-head NPU GPU conductor** (Exp 023) | **Validated** — hotSpring v0.6.15 |
| 08 | Neuromorphic Edge Intelligence for Sovereign Agricultural IoT | Agricultural IoT × Neuromorphic Computing | airSpring Exp 028-029 (88 checks) + wetSpring NPU driver | NPU inference at 0.0009% of active cycle energy; 10.7× more efficient than cloud; 1-min cadence unlocked; multi-crop hot-swap | **Validated on Live Hardware** — AKD1000, streaming + evolution + power budget. airSpring v0.6.9: 852 lib + 1133 integration tests, f64-canonical universal precision (6 ops via compile_shader_universal), deep debt audit, sovereignty hardened |
| 09 | Sovereign Field Genomics — Nanopore + NPU | Environmental Genomics × Edge Inference | wetSpring Exp193-195 (NPU) + Exp184-185 (16S) + planned Exp196-202 | MinION sequencing + AKD1000 classification + BarraCUDA 16S pipeline = autonomous field sentinel. NPU-driven adaptive sampling (37x read-rate headroom). No cloud, no Python. | **Architecture defined** — all compute components validated, awaiting sequencer hardware |
| 10 | First Dynamical QCD Production on Consumer GPU | Lattice QCD × Neuromorphic Computing | hotSpring Exp 024 (8⁴ dynamical, 1,031+ traj, 17 β points), Exp 028-031 | First NPU-steered dynamical fermion QCD scan. Smooth crossover confirmed. β_c ~ 5.5. NPU expanded 4-seed scan to 17 points. CG–disorder correlation validates Anderson proxy. **Exp 031: NPU controls dt/n_md with mid-beta adaptation, targeting 70% acceptance.** | **Complete + Evolving** — 17 β points, Exp 031 adds NPU parameter control. |
| 11 | The Nautilus Shell — Evolutionary Reservoir Computing from Bingo Boards | Reservoir Computing × Neuromorphic × Evolutionary Algorithms | primalTools/bingoCube/nautilus/ (31 tests, 5 examples); **ToadStool S80**: barracuda::nautilus (7 files, 22 tests, 8 JSON-RPC methods) | Bingo boards as structured random projections; evolutionary generations replace temporal recurrence for feed-forward hardware; nautilus shell = layered evolutionary history, portable between instances. Column-range-preserving crossover maps natively to AKD1000 int4. Self-regulating drift monitor + edge seeding. AKD1000 int4 weight export. Quenched→dynamical transfer: 540× cost reduction. | **Validated** — 5.3% LOO CG error, 2.6% blind prediction on Exp 029, 31 tests. **S80**: Standalone absorption into ToadStool/BarraCUDA (7 files, 22 tests, 8 ai.nautilus.* JSON-RPC methods). |
| 12 | Anderson Localization in Immunological Signaling — Cytokine Propagation, Drug Geometry, and the Fajgenbaum Repurposing Bridge | Immunology × Condensed Matter Physics × Pharmacology × Drug Repurposing | Proposed: wetSpring Exp270-274, neuralSpring ESN/LSTM, groundSpring Exp008/012/015/018 | Cytokine (IL-31/IL-4/IL-13) propagation through inflamed skin tissue follows Anderson localization; AD barrier disruption = dimensional promotion (inverse of Paper 06 tillage collapse); Fajgenbaum MATRIX drug-disease scoring gains geometry dimension via Anderson transport; **groundSpring** provides 2D/3D spectral validation (Exp 008), cytokine transport modeling (Exp 012), uncertainty bridge (Exp 015), band edge for epidermal periodicity (Exp 018), ConceptEdge for AD flare detection, DriftAction for treatment steering | **Proposal** — literature grounded, Gonzales catalog (6 papers) + Fajgenbaum catalog complete, pathway mapping complete, 5 wetSpring experiments designed. Source: Dr. Andrea J. Gonzales (Zoetis → MSU Pharmacology & Toxicology, 2025) |

## Reading Order

**For a microbiologist**: 01 (Anderson-QS, the headline result) → 05 (cross-species) → 03 (bioag) → 06 (no-till)

**For an immunologist or pharmacologist**: 12 (immunological Anderson — cytokine propagation, Fajgenbaum bridge) → 01 (Anderson-QS foundation) → 05 (cross-species signaling) → 04 (sentinels — ESN regime classification)

**For an ecologist**: 05 (symbiotic signaling) → 02 (LTEE extensions) → 04 (sentinels) → 06 (no-till)

**For a soil scientist or agronomist**: 06 (no-till Anderson mechanism) → 03 (tree crop inoculants) → 01 (underlying physics)

**For a physicist**: 01 (Anderson applied to biology) → 06 (dynamic Anderson with time series) → the wetSpring experiment docs (Exp107-143)

**For a plasma physicist**: 07 (sovereign WDM on consumer GPU) → 10 (dynamical QCD production) → 01 (Anderson framework) → the hotSpring paper queue (Tier 0–4)

**For a PhD committee**: 01 (demonstrates novel contribution) → 06 (applied to 60-year dataset) → 07 (WDM + distributed compute) → 02 (connects to LTEE proposal) → 03-05 (breadth) → 08 (NPU edge deployment)

**For an agricultural engineer**: 08 (NPU edge IoT) → 09 (field genomics) → 06 (no-till physics) → 03 (bioag microbiome) → 04 (sentinel monitoring)

**For a field genomics researcher**: 09 (field genomics) → 04 (sentinel concept) → 01 (Anderson detection signal) → 08 (NPU agricultural IoT) → the wetSpring experiment docs (Exp193-195, planned Exp196-202)

**For a reservoir computing researcher**: 11 (nautilus shell — evolutionary reservoir from bingo boards) → 10 (ESN-steered dynamical QCD) → 07 (NPU brain architecture) → 04 (sentinels, NPU edge deployment)

**For an immunologist or veterinary pharmacologist**: 12 (Anderson in immunological signaling) → 01 (underlying Anderson-QS physics) → 06 (dimensional collapse/promotion duality) → 05 (cross-species signaling)

**For a drug repurposing researcher**: 12 §3 (Fajgenbaum bridge — geometry-aware scoring) → 12 §2 (Anderson mapping) → 01 (framework) → 04 (sentinels as diagnostic analog)

## Connection to the Main Thesis

Paper 11 (Nautilus Shell) provides direct computational evidence for the
constrained evolution framework (thesis Ch. 3). The column-range constraint
on bingo boards reshapes the fitness landscape of the reservoir, producing
specialized boards that predict QCD observables at 5.3% LOO error —
structures that would not emerge from unconstrained neural architecture
search. The N_e·s drift monitor implements Anderson's drift boundary
(thesis §3.2.3) computationally, and edge seeding implements directed
mutagenesis where constraint identifies regions of qualitative physics
change. The Nautilus Shell is also the computational machinery needed for
the LTEE library vision (Paper 02): populations under constraint, with
drift monitoring, fitness tracking, and concept edge detection.

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

- **wetSpring**: Anderson QS, 16S pipeline, DADA2, taxonomy, NPU live, field genomics architecture, bio brain (8,300+ checks, 281 experiments, 1,261 lib+forge tests, 285 binaries, 47 CPU + 45 GPU bio modules, Phase 96, standalone `barraCuda` v0.3.1, 150+ primitives consumed, 164 named tolerances, 94.69% line coverage, zero local WGSL, zero TODO/FIXME/HACK in 453 source files. `classify_quantized` evolved to `Option<usize>` (no silent fallbacks). Capability-based IPC discovery. Platform-agnostic benchmarks. `vault` feature-gated. Python baseline environment pinned. Chuna papers queued to hotSpring (43-45) and neuralSpring (26).)
- **neuralSpring**: ML primitives (LSTM, HMM, transfer learning, spectral analysis,
  ESN reservoir computing), 26 papers + 5 WDM surrogates validated at 4,100+ checks,
  880 lib tests, 238 binaries, 139+ named tolerances, 46 upstream rewires to
  barraCuda delegates. barraCuda v0.3.1 standalone (`../barraCuda/crates/barracuda`).
  Session 124: airSpring V069 naming rewire (`ToadStool`=dispatch, `BarraCUDA`=math),
  HMM forward chain absorbed to `HmmBatchForwardF64` ComputeDispatch (single-dispatch
  f64 log-domain GPU, fallback to per-step Tensor), Paper 026 Chuna LSTM glucose
  prediction (Py 5/5 + Rs 8/8 + bC 4/4 + gT 4/4). Zero clippy warnings
  (pedantic+nursery, all-features). 217/217 validate\_all. V82 handoff.
  Cross-spring provenance mapped: hotSpring precision → wetSpring bio → neuralSpring
  domain → barraCuda fused ops → consumed by all Springs
- **hotSpring**: MD simulation, nuclear EOS, lattice QCD, transport, 4-layer brain architecture (711 tests, 84 binaries, 62 WGSL shaders, 0 clippy warnings, 0 files >1000 lines). **25 papers** (Papers 43-45 added March 5: Chuna gradient flow integrators, conservative dielectric functions, kinetic-fluid coupling).
- **airSpring**: FAO-56 ET₀ (8 methods), Priestley-Taylor, Thornthwaite, GDD, Saxton-Rawls
  pedotransfer, water balance, Richards PDE, isotherms, yield response, scheduling, lysimeter,
  sensitivity, SCS-CN runoff, Green-Ampt infiltration, Anderson coupling, diversity indices,
  100-station Michigan Crop Water Atlas, NUCLEUS primal (30 capabilities), metalForge dispatch,
  AirSpringBrain (Nautilus evolutionary reservoir: ET₀/soil/crop heads), MonitoredAtlasStream
  (DriftMonitor regime change detection), Paper 12 immunological Anderson (tissue diversity +
  CytokineBrain + barrier state + cross-species), 6 local WGSL compute shaders
  (`local_elementwise.wgsl`: SCS-CN, Stewart yield, Makkink, Turc, Hamon, Blaney-Criddle)
  via `gpu::local_dispatch::LocalElementwise` (wgpu direct, f32 precision).
  **v0.6.8 (March 3, 2026)**: Rewired to standalone barraCuda 0.3.1. 1237 Python +
  846 lib + 62 forge tests + 86 binaries, 77 experiments. 1132 total workspace tests.
  25 Tier A + 6 GPU-local modules (ops 0-13 + local ops 0-5 + uncertainty stack),
  27 metalForge workloads, NUCLEUS mesh routing (Exp 076: 60/60). 94.91% line coverage.
  Capability-based discovery (no hardcoded primal names). `to_toadstool()` → `to_barracuda()`.
  146/146 cross-spring evolution benchmark + 32/32 Exp 077 provenance.
  ToadStool S93 sync, barraCuda 0.3.1 standalone. Zero clippy pedantic warnings, cargo-deny clean.
- **groundSpring**: Uncertainty quantification, noise labels, spectral theory (Anderson, Almost-Mathieu, band edge), transport, quasispecies, rare biosphere, jackknife, freeze-out, spectral recon, WDM precision/convergence/vendor-parity, NPU Anderson regime classification, mixed-hardware pipeline dispatch (`PCIe` topology, NUCLEUS atomics, fallback chains) (33 experiments, 376/376 Rust checks + 187 metalForge checks, 10 domains, 790 workspace tests; live hardware: RTX 4070, Titan V, AKD1000 NPU; 2.2× GPU speedup). V76: structural evolution (domain-split GPU tier binary, NUCLEUS shared utilities, observation-gap benchmark parity chain, deep debt zero). barraCuda v0.3.1, toadStool S93 fully synchronized, clippy pedantic CI, 13-tier named tolerance architecture (`tol::` module, `eps::` module), zero bare tolerance literals, full validation benchmark (28/28 binaries, −10% with barraCuda CPU delegation), cross-spring provenance documented. 97.25% library line coverage. 81 active delegations (47 CPU + 34 GPU). 28/28 mathematical parity. biomeOS Neural API + NestGate data pipelines (NCBI, NOAA, IRIS). All files < 1000 lines, zero unsafe, zero production mocks, zero `unwrap()` in production, zero TODO/FIXME in Rust source

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

## Cross-Spring Provenance (standalone barraCuda v0.3.1)

**Validated March 3, 2026** — all springs rewired to standalone `barraCuda`:

```
┌─ hotSpring v0.6.17 ─ spectral (Anderson, Lanczos, level statistics), 4-layer brain
├─ neuralSpring V80 ── spectral phase (Bulk/EdgeOfChaos/Chaotic), shared validation helpers
├─ wetSpring V95 ───── diversity, Bray-Curtis, rarefaction, NMF, ridge
├─ groundSpring V74 ── Kimura fixation, error threshold, jackknife, 13-tier tolerance architecture, clippy pedantic CI, full validation benchmark
├─ airSpring v0.6.9 ── regression, moving window, hydrology (FAO-56 ET₀), f64 canonical universal precision
├─ wateringHole V69 ── Boltzmann sampling (Metropolis-Hastings MCMC)
├─ bingoCube/nautilus ─ NautilusBrain → BioNautilusBrain (concept edge, drift)
└─ multi-spring ────── special functions, bootstrap, correlation
```

All 767+ `barraCuda` WGSL shaders are f64-canonical with f16/f32/f64/Df64
precision dispatch per hardware. `barraCuda` is the standalone math primal
(WHAT to compute); `toadStool` handles hardware dispatch (WHERE and HOW).
Springs depend on `barraCuda` directly for math. Cross-spring evolution is
bidirectional: each spring's innovations flow through `barraCuda` and benefit
all springs.

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

Paper 12 (Immuno-Anderson)
 wetSpring (Anderson spectral,
   cytokine lattice Exp270-274)
 neuralSpring (ESN regime,
   LSTM dose-response, IC50)
 groundSpring (transport,
   uncertainty bridge,
   spectral validation)
```

**What each spring contributes:**

| Spring | Contributes To | Key Primitives |
|--------|---------------|----------------|
| wetSpring | 01, 03, 04, 05, 06 | Anderson QS, diversity, Bray-Curtis, FASTA, NCBI, NPU int8 |
| hotSpring | 01, 07 | Spectral theory (Lanczos, Anderson 3D), GPU MD, lattice QCD |
| airSpring | 03, 06, **08**, **12** | FAO-56 ET₀, soil moisture, Richards PDE, **NPU int8 eco classifiers, IoT sensor pipeline**, GpuDiversity (tissue W), CytokineBrain (AD flare prediction), barrier state (VG analogue), cross-species Anderson |
| neuralSpring | 01, 02, 04, 05, 06, 07 | ESN/LSTM anomaly detection, WDM surrogates, HMM, transfer learning |
| groundSpring | **01, 02, 03, 04, 05, 06, 07, 08, 09, 12** | Spectral theory validation (Anderson, Almost-Mathieu, band edge, transport), uncertainty budgets, sensor noise calibration, rare biosphere, jackknife error bars, freeze-out inverse, spectral recon, drift vs selection, quasispecies threshold, WDM precision/convergence/vendor-parity, **NPU Anderson regime classification (AKD1000)**, metalForge cross-substrate validation, **immunological Anderson mapping (Exp 008/012/015/018 → cytokine propagation)** |

groundSpring now contributes to ALL 10 active baseCamp papers (01-09, 12) —
reflecting the expansion from 5 experiments (sensor noise only) to 33 experiments
across 10 scientific domains including live NPU hardware. The spectral theory experiments (008, 009,
012, 018) validate the Anderson framework underlying papers 01, 05, and 06.
The Bazavov experiments (019-021) connect directly to paper 07's lattice QCD
science. The evolutionary biology experiments (014, 016, 017) serve papers 02
and 04. The WDM experiments (025-027) provide the uncertainty budget for paper
07's consumer GPU claims. Exp 028 (NPU Anderson classification on AKD1000)
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
| 07/10 | WDM transport S(q,ω); **Dynamical QCD 32⁴ production** (Exp 024 8⁴ complete, Exp 025-027 scale-up); 4D Anderson + Wegner proxy pipeline | hotSpring × neuralSpring × **groundSpring** (spectral reconstruction + freeze-out + jackknife for lattice QCD observables; NPU GPU-conductor validation; Anderson CG proxy) |
| 08 | High-cadence NPU pipeline + field integration | airSpring (sensor + water balance) × wetSpring (NPU driver + ESN) × neuralSpring (LSTM time series) × **groundSpring** (NPU DMA validation, cross-substrate parity proof, uncertainty budget) |
| 09 | Nanopore + NPU field genomics end-to-end | wetSpring (16S + NPU + PFAS ML + alignment) × airSpring (soil sensors) × neuralSpring (ESN/LSTM) × **groundSpring** (rare biosphere + uncertainty + **metalForge cross-substrate dispatch validation**) |
| 11 | Live data stream prediction via Nautilus Shell | primalTools/bingoCube × hotSpring (trajectory data, NPU brain) × neuralSpring (ESN baseline comparison) × **groundSpring** (uncertainty budget for evolutionary vs recurrent reservoir) |
| 12 | Skin-layer Anderson lattice (2D epidermis + 3D dermis), barrier disruption dimensional promotion, Gonzales cytokine data ingestion, Fajgenbaum geometry-aware drug scoring | wetSpring (Anderson spectral Exp270-274) × neuralSpring (ESN regime classifier, LSTM dose-response) × **airSpring** (GpuDiversity: Pielou evenness as tissue disorder W; CytokineBrain: Nautilus reservoir for AD flare prediction; DriftMonitor: regime change detection in cytokine time series; Paper 06 dimensional promotion/collapse duality) × **groundSpring** (Exp 008 2D/3D spectral, Exp 012 cytokine transport, Exp 015 uncertainty bridge, Exp 018 band edge for epidermal periodicity; ConceptEdge for AD flare detection; DriftAction for treatment response steering) |

## Future Contributions

### Immediate (S80+)

- **Nautilus Absorption (DONE S80)**: `barracuda::nautilus` absorbed from
  bingoCube — 7 files, 22 tests, CPU-only. 8 `ai.nautilus.*` JSON-RPC
  methods in ToadStool daemon. Feature-gated `nautilus` in CLI.
- **BatchedEncoder (DONE S80)**: Fused multi-op GPU pipeline — single
  `queue.submit()` for MLP/Transformer forward passes.
- **Batch Nelder-Mead GPU (DONE S80)**: N parallel optimizations via
  batched simplex shaders. Available for isotherm fitting, multi-start
  optimization.
- **GpuDriverProfile Workarounds (DONE S80)**: Taylor-series sin/cos
  preamble for NVK driver. `asin`/`acos` protected.
- **ComputeDispatch at 95/250 (S80)**: 19 more ops migrated.

### Immediate (V63 — DONE)

- **Brain Architecture Integration (DONE V63)**: DriftAction, ConceptEdge,
  MultiHeadUncertainty from hotSpring/Nautilus. detect_concept_edges returns
  structured edges with drift action recommendations. seed_around_edges for
  focused phase boundary exploration.
- **NUCLEUS Capability Registration (DONE V63)**: 7 science.* capabilities
  registered/deregistered via biomeos::register_capabilities().
- **Hardcoded Primal Elimination (DONE V63)**: All primal names removed from
  routing and display labels. Capability-based discovery only.
- **Configurable Timeouts (DONE V63)**: biomeos connect/read timeouts via
  env vars.
- **Paper 12 Integration (DONE V63)**: Anderson immunological signaling
  mapped to groundSpring experiments 008/012/015/018.

### Previous Immediate (V61 — DONE)

- **Mixed-Hardware Pipeline Dispatch (DONE V61)**: groundSpring V61 adds `PCIe`
  topology modeling, multi-stage pipeline dispatch, NUCLEUS atomic types
  (Tower/Node/Nest/Full), and fallback chains. Infrastructure for NPU→GPU
  P2P bypass and mixed-substrate streaming. 42/42 validation checks, 120
  metalForge tests.
- **NPU Live (DONE)**: 3 ESN classifiers validated on real AKD1000 hardware
  (Exp193-195). Online evolution at 136 gen/sec, PUF fingerprinting (6.34 bits),
  12.9K Hz temporal streaming. Coin-cell viable (1.4 µJ/infer).
- **Field Genomics Architecture (DONE)**: Sub-thesis 06 defines MinION +
  AKD1000 + BarraCUDA for autonomous environmental sentinels. Experiments
  196-202 planned pending sequencer hardware.
- **Data Type Profiling (DONE)**: Comprehensive catalog of biological data
  types in `wetSpring/specs/DATA_TYPES.md` for NestGate evolution.
- **DF64 Anderson**: Extended precision (f64-pair) for large Anderson
  lattices (L=14-20). Phase 1 validated at f64 (Exp187); Phase 2 will
  use DF64 shaders from hotSpring.

### Immediate (V62 — DONE)

- **ToadStool S79 Catch-Up (DONE)**: Full rewire to `ToadStool` S79
  (`f97fc2ae`). Pollster dependency eliminated — all async bridging now
  uses `barracuda::device::test_pool::tokio_block_on`. GPU device
  initialization upgraded to `WgpuDevice::new_f64_capable()` with
  automatic fallback to `WgpuDevice::new()`. DF64 precision strategy
  wired end-to-end.
- **Shader Cleanup (DONE)**: 2 redundant local WGSL shaders
  (`mc_et0_propagate.wgsl`, `batched_multinomial.wgsl`) removed — both
  absorbed into ToadStool's f64-canonical bio shader library. Only 2
  unique Anderson Lyapunov shaders retained in metalForge.
- **Cross-Spring Shader Lineage (DONE)**: Full provenance documented in
  V62 handoff — tracing shader contributions across hotSpring (precision),
  wetSpring (bio), neuralSpring (domain), airSpring (hydrology), and
  groundSpring (spectral) through ToadStool's unified shader library.
- **License Harmonization (DONE)**: All `Cargo.toml` SPDX identifiers
  updated to `AGPL-3.0-only` for consistency with workspace root.
- **Validation (DONE)**: 710 workspace tests, 23/23 cross-spring
  benchmark, 39/39 GPU tier, 13/13 Titan V + RTX 4070 validation.
  Zero clippy warnings (pedantic + nursery), zero unsafe.

### Immediate (airSpring v0.6.1 — DONE)

- **ToadStool S79 Absorption (DONE)**: airSpring v0.6.1 absorbs ToadStool S79
  modernization — `libc`→`rustix`, `async-trait`→AFIT, universal f64 precision,
  `pollster`→`test_pool`. 7 new GPU orchestrators wired: `BatchedVanGenuchten`
  (ops 9-10: soil hydraulics θ(h)/K(h)), `BatchedThornthwaite` (op 11),
  `BatchedGdd` (op 12), `BatchedPedotransfer` (op 13), `GpuJackknife`,
  `GpuBootstrap`, `GpuDiversity` (Shannon/Simpson/Pielou). All with CPU
  fallbacks and unit tests. 25 Tier A GPU modules total (up from 15).
- **Cross-Spring Provenance Tracking (DONE)**: `ShaderProvenance` entries
  added for all new GPU modules — tracking origin across hotSpring (precision
  shaders), wetSpring (bio diversity), groundSpring (uncertainty stack),
  and airSpring (hydrology/ecology). `bench_cross_spring_evolution` binary
  extended with S79 ops 9-13 and GPU uncertainty benchmarks.
- **Validation (DONE)**: 737 lib tests, 94.15% llvm-cov coverage, zero
  clippy warnings (pedantic + nursery), `cargo doc` clean. Cross-spring
  evolution benchmark and GPU uncertainty stack fully exercised.
- **Directly enables**: Paper 06 (GPU van Genuchten for soil hydraulics at
  scale), Paper 03 (GPU pedotransfer for inoculant trial design), Paper 08
  (GPU uncertainty for NPU edge confidence intervals).

### Immediate (airSpring v0.6.4 — DONE)

- **GPU Multi-Field Pipeline (DONE)**: `SeasonalPipeline::run_multi_field()`
  dispatches Stage 3 (WB) to GPU per-day across M fields via `gpu_step()`.
  6.8M field-days/s at atlas scale (50 stations × 153 days). `MultiFieldResult`
  tracks GPU dispatch count for instrumentation.
- **CPU Parity Benchmark (DONE)**: 9 domains validated against Python, 34/34 PASS.
  13,000× Rust-vs-Python at atlas scale. Key throughputs: ET₀ 10M/s, Kc 1.9B/s,
  WB 162M days/s, seasonal pipeline 59K seasons/s.
- **Pure GPU End-to-End (DONE)**: All 4 stages on GPU (ET₀+Kc+WB+Yield), 46/46 PASS.
  19.7× GPU dispatch reduction for 20 fields. CPU↔GPU parity within 2mm seasonal.
- **metalForge 7-Stage Cross-System (DONE)**: Weather(CPU) → ET₀(GPU) → Kc(GPU) →
  WB(GPU) → Yield(GPU) → CropStress(NPU) → Validation(CPU). 66/66 PASS. GPU→NPU
  via PCIe P2P bypass. GPU stages 2-5 stay on device (zero CPU round-trips).
- **Validation (DONE)**: 815 lib tests (at v0.6.4), 82 binaries, 72 experiments,
  zero clippy pedantic warnings, all provenance documented.
- **Directly enables**: Paper 06 (atlas-scale multi-field GPU for no-till vs tilled
  comparison), Paper 08 (NPU edge with GPU-computed uncertainty intervals),
  Paper 12 (tissue diversity GPU + CytokineBrain streaming pipeline).

### Immediate (airSpring v0.6.6 — DONE)

- **Cross-Spring Rewire (DONE)**: `BrentGpu` wired into VG inverse (θ→h on GPU),
  `RichardsGpu` wired into Richards PDE (GPU Picard+CN+Thomas solver).
  68/68 cross-spring provenance validation — all 5 springs verified.
- **ToadStool S87 Sync (DONE)**: Absorbed `StatefulPipeline`, `BatchedStatefulF64`,
  `BrentGpu`, `RichardsGpu`, `BatchedNelderMeadGpu`, `nautilus`, `L-BFGS`,
  `anderson_4d`. Tier B→A promotions for water balance and isotherm.
- **Cross-Spring Evolution Benchmark (DONE)**: 138/138 PASS across S80-S87
  primitives. 68/68 rewire PASS across 5 springs.
- **Validation (DONE)**: 815 lib tests, 83 binaries, 73 experiments, zero clippy
  pedantic warnings, all provenance documented.
- **Directly enables**: Fused `SeasonalPipelineF64` adoption, batched multi-column
  Richards GPU, Green-Ampt/pedotransfer GPU shaders.

### Immediate (airSpring v0.6.8 — DONE)

- **Local GPU Compute Evolution (DONE)**: 6 element-wise ecological operations now
  run on GPU via `local_elementwise.wgsl` (f32 WGSL compute shader dispatched through
  wgpu directly). Operations: SCS-CN runoff (op=0), Stewart yield (op=1), Makkink ET₀
  (op=2), Turc ET₀ (op=3), Hamon PET (op=4), Blaney-Criddle (op=5).
- **`gpu::local_dispatch::LocalElementwise` (DONE)**: New wgpu dispatch engine —
  compiles shader, manages buffers, handles f64↔f32 conversion. Demonstrates the
  "write locally → absorb upstream → lean" cycle at the shader level.
- **metalForge Workload Expansion (DONE)**: 27 ecological workloads (21 existing +
  6 new with `ShaderOrigin::Local`). ToadStool absorption converts to `::Absorbed`.
- **NUCLEUS Mesh Routing (DONE)**: Exp 076 validates full NUCLEUS pipeline —
  capability-based dispatch, PCIe P2P bypass, Tower/Node/Nest atomics, multi-node
  cross-hop routing. 60/60 PASS.
- **ToadStool Absorption Handoff (DONE)**: V051 handoff documents proposed ops 14-19
  for `batched_elementwise_f64.wgsl`, precision characteristics, helper function
  mapping to existing df64 transcendentals. V053 consolidates absorption guide with
  cross-spring evolution intelligence, GPU driver insights, and performance data.
- **Exp 077 Cross-Spring Provenance (DONE)**: CPU↔GPU benchmark with 5-spring shader
  provenance tracking. Validates precision lineage (hotSpring→all), uncertainty stack,
  seasonal pipeline parity. 32/32 PASS.
- **Validation (DONE)**: 846 lib tests, 86 binaries, 77 experiments, zero clippy
  pedantic warnings. 146/146 cross-spring evolution benchmark + 32/32 provenance.
- **Directly enables**: ToadStool f64 absorption of 6 local ops (tightens tolerances
  by 6+ orders of magnitude), fused seasonal pipeline, full GPU-first workload chain.

### Immediate (airSpring v0.6.9 — DONE)

- **f64-Canonical Universal Precision (DONE)**: Evolved `local_elementwise.wgsl` (f32)
  to `local_elementwise_f64.wgsl` (f64 canonical) compiled via `compile_shader_universal()`.
  F64 native on pro GPUs (Titan V), F32 downcast on consumer GPUs (RTX 4070). "Math is
  universal, precision is silicon."
- **Deep Debt Audit (3 rounds — DONE)**: Provenance normalization (47 benchmark JSONs →
  `_provenance` key), `json_f64_required` structured failure (exit(1) not panic),
  `SubmitParams` refactor for wgpu dispatch, env-configurable RPC timeout
  (`BIOMEOS_RPC_TIMEOUT_SECS`), `bench_cpu_vs_python` multi-file refactor, BarraCuda
  `variance`/`std_dev` primitive wiring (zero local math duplication), streaming JSON I/O,
  all `#[allow]` annotations with reason strings.
- **Cross-Spring Evolution Benchmark (DONE)**: Exp 078 validates universal precision
  evolution across 6 f64-canonical ops, confirming `compile_shader_universal()` correctness.
- **Validation (DONE)**: 852 lib + 33 integration + 62 forge tests (947 total), 86 binaries,
  78 experiments, 95.66% line coverage, zero clippy pedantic+nursery warnings, zero unsafe,
  zero mocks in production. All provenance normalized with commit-level traceability.
- **Directly enables**: BarraCuda absorption of 6 f64-canonical local ops (ready for
  `batched_elementwise_f64` ops 14-19), cross-spring `compile_shader_universal()` pattern.

### Medium-term

- **`SeasonalPipelineF64` adoption**: Move from per-stage dispatch to fused upstream
  seasonal GPU pipeline (ET₀→Kc→WB→stress in one shader).
- **Batched Richards GPU**: M soil columns in one dispatch (amortize per-field overhead).
- **Green-Ampt + SCS-CN GPU**: Coupled runoff-infiltration on GPU for watershed-scale.
- **Pedotransfer GPU**: Saxton-Rawls θs/θr/Ks from texture (embarrassingly parallel).
- **Multi-GPU field parallelism**: Use upstream `multi_gpu` for horizontal scaling.
- **NCBI sovereign scaling**: Multi-BioProject sovereign pipeline
  via NestGate JSON-RPC, replacing all institutional API dependencies.
- **Cross-spring shared tolerances**: wetSpring's 86 named tolerance
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
  math operational (4,748+ checks). Experiments 196-202 planned.
