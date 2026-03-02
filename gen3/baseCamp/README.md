# baseCamp: Independent Explorations Alongside the Constrained Evolution Thesis

**Date:** March 2, 2026 (updated S80)
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
| 01 | Anderson Localization as QS Null Hypothesis | Physics × Microbiology | Exp107-156 (3,100+ checks), Exp170-182 (321 checks) | 3D geometry is necessary and sufficient for QS in diverse communities; 3 genuine NP solutions found; W_c = 16.26 ± 0.95 quantified | **Validated** — 197 experiments, full three-tier |
| 02 | Extending the Frozen Fossil Record | Evolutionary Biology | Builds on Ch. 14 + Anderson anomaly catalog (Exp143) | Constrained evolution predictions for LTEE, permafrost, vent archives, agricultural time series | Proposal — predictions quantified |
| 03 | Precision Microbiome for Tree Crops | Agricultural Microbiology | Extension of Anderson model + Track 4 soil QS (Exp170-178) | Soil biome geometry guides inoculant design; rhizosphere W ≈ 6.7 (extended regime) | Proposal — Track 4 validates framework |
| 04 | Microbial Sentinels | Environmental Biosensing | Exp114-119, 123, 124, **193-195** (NPU), PFAS/algae | Community shifts as early-warning biosensors; **NPU validated on real AKD1000** (18.8K Hz, coin-cell 11 years, online evolution 136 gen/sec, PUF fingerprint) | **Validated on Live Hardware** — Pure Rust driver, Phase C sovereign |
| 05 | Cross-Species Signaling in Symbiotic Systems | Symbiotic Ecology | Exp142, 144-146 (cold seep + luxR phylogeny) | Mixed-species QS in lichen, rhizobia, coral; 299K QS genes across 170 metagenomes; eavesdropper enrichment confirmed | **Validated** — cold seep + phylogeny complete |
| 06 | Anderson Localization as the Mechanism Behind No-Till Soil Health | Soil Microbial Ecology × Physics | Track 4: Exp170-182 (321 checks), 9 papers, full three-tier | Tillage = dimensional collapse of QS-active 3D pore network; CPU + GPU + metalForge validated | **Validated** — Track 4 complete |
| 07 | Sovereign Warm Dense Matter Simulation on Consumer GPU | Plasma Physics × Distributed Computing | hotSpring Tier 4 + neuralSpring surrogates + groundSpring uncertainty | WDM transport on $600 GPU; deconfinement at β_c=5.69 on $1,500 GPU; **11-head NPU GPU conductor** (Exp 023) | **Validated** — hotSpring v0.6.15 |
| 08 | Neuromorphic Edge Intelligence for Sovereign Agricultural IoT | Agricultural IoT × Neuromorphic Computing | airSpring Exp 028-029 (88 checks) + wetSpring NPU driver | NPU inference at 0.0009% of active cycle energy; 10.7× more efficient than cloud; 1-min cadence unlocked; multi-crop hot-swap | **Validated on Live Hardware** — AKD1000, streaming + evolution + power budget |
| 09 | Sovereign Field Genomics — Nanopore + NPU | Environmental Genomics × Edge Inference | wetSpring Exp193-195 (NPU) + Exp184-185 (16S) + planned Exp196-202 | MinION sequencing + AKD1000 classification + BarraCUDA 16S pipeline = autonomous field sentinel. NPU-driven adaptive sampling (37x read-rate headroom). No cloud, no Python. | **Architecture defined** — all compute components validated, awaiting sequencer hardware |
| 10 | First Dynamical QCD Production on Consumer GPU | Lattice QCD × Neuromorphic Computing | hotSpring Exp 024 (8⁴ dynamical, 1,031+ traj, 17 β points), Exp 028-031 | First NPU-steered dynamical fermion QCD scan. Smooth crossover confirmed. β_c ~ 5.5. NPU expanded 4-seed scan to 17 points. CG–disorder correlation validates Anderson proxy. **Exp 031: NPU controls dt/n_md with mid-beta adaptation, targeting 70% acceptance.** | **Complete + Evolving** — 17 β points, Exp 031 adds NPU parameter control. |
| 11 | The Nautilus Shell — Evolutionary Reservoir Computing from Bingo Boards | Reservoir Computing × Neuromorphic × Evolutionary Algorithms | primalTools/bingoCube/nautilus/ (31 tests, 5 examples); **ToadStool S80**: barracuda::nautilus (7 files, 22 tests, 8 JSON-RPC methods) | Bingo boards as structured random projections; evolutionary generations replace temporal recurrence for feed-forward hardware; nautilus shell = layered evolutionary history, portable between instances. Column-range-preserving crossover maps natively to AKD1000 int4. Self-regulating drift monitor + edge seeding. AKD1000 int4 weight export. Quenched→dynamical transfer: 540× cost reduction. | **Validated** — 5.3% LOO CG error, 2.6% blind prediction on Exp 029, 31 tests. **S80**: Standalone absorption into ToadStool/BarraCUDA (7 files, 22 tests, 8 ai.nautilus.* JSON-RPC methods). |

## Reading Order

**For a microbiologist**: 01 (Anderson-QS, the headline result) → 05 (cross-species) → 03 (bioag) → 06 (no-till)

**For an ecologist**: 05 (symbiotic signaling) → 02 (LTEE extensions) → 04 (sentinels) → 06 (no-till)

**For a soil scientist or agronomist**: 06 (no-till Anderson mechanism) → 03 (tree crop inoculants) → 01 (underlying physics)

**For a physicist**: 01 (Anderson applied to biology) → 06 (dynamic Anderson with time series) → the wetSpring experiment docs (Exp107-143)

**For a plasma physicist**: 07 (sovereign WDM on consumer GPU) → 10 (dynamical QCD production) → 01 (Anderson framework) → the hotSpring paper queue (Tier 0–4)

**For a PhD committee**: 01 (demonstrates novel contribution) → 06 (applied to 60-year dataset) → 07 (WDM + distributed compute) → 02 (connects to LTEE proposal) → 03-05 (breadth) → 08 (NPU edge deployment)

**For an agricultural engineer**: 08 (NPU edge IoT) → 09 (field genomics) → 06 (no-till physics) → 03 (bioag microbiome) → 04 (sentinel monitoring)

**For a field genomics researcher**: 09 (field genomics) → 04 (sentinel concept) → 01 (Anderson detection signal) → 08 (NPU agricultural IoT) → the wetSpring experiment docs (Exp193-195, planned Exp196-202)

**For a reservoir computing researcher**: 11 (nautilus shell — evolutionary reservoir from bingo boards) → 10 (ESN-steered dynamical QCD) → 07 (NPU brain architecture) → 04 (sentinels, NPU edge deployment)

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

- **wetSpring**: Anderson QS, 16S pipeline, DADA2, taxonomy, NPU live, field genomics architecture (4,748+ checks, 60 NPU on AKD1000)
- **neuralSpring**: ML primitives (LSTM, HMM, transfer learning, spectral analysis,
  ESN reservoir computing), 25 papers + 5 WDM surrogates validated at 2,450+ checks,
  623 lib tests, 172 binaries, 156/156 validators, 129+ named tolerances, 39 functions
  rewired to BarraCUDA. Session 87: WDM queue closed (nW-01..nW-05 — MLP, LSTM
  reservoir, ESN classifier), reservoir computing validated for sequence regression
  and regime classification
- **hotSpring**: MD simulation, nuclear EOS, lattice QCD, transport, 4-layer brain architecture (~700 tests, 84 binaries, 62 WGSL shaders)
- **airSpring**: FAO-56 ET₀, Priestley-Taylor, Thornthwaite, GDD, Saxton-Rawls pedotransfer,
  water balance, Richards PDE, isotherms, yield response, scheduling, lysimeter, sensitivity,
  100-station Michigan Crop Water Atlas
  (v0.4.8: 594 Python + 491 Rust tests + 570 validation + 1393 atlas checks, 27 binaries,
  97.45% coverage, 11 Tier A GPU modules)
- **groundSpring**: Uncertainty quantification, noise labels, spectral theory (Anderson, Almost-Mathieu, band edge), transport, quasispecies, rare biosphere, jackknife, freeze-out, spectral recon, WDM precision/convergence/vendor-parity, NPU Anderson regime classification (28 experiments, 288/288 Rust checks + 31 metalForge checks, 9 domains; live hardware: RTX 4070, Titan V, AKD1000 NPU; 2.2× GPU speedup)

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
| airSpring | 03, 06, **08** | FAO-56 ET₀, soil moisture, Richards PDE, **NPU int8 eco classifiers, IoT sensor pipeline** |
| neuralSpring | 01, 02, 04, 05, 06, 07 | ESN/LSTM anomaly detection, WDM surrogates, HMM, transfer learning |
| groundSpring | **01, 02, 03, 04, 05, 06, 07, 08, 09** | Spectral theory validation (Anderson, Almost-Mathieu, band edge, transport), uncertainty budgets, sensor noise calibration, rare biosphere, jackknife error bars, freeze-out inverse, spectral recon, drift vs selection, quasispecies threshold, WDM precision/convergence/vendor-parity, **NPU Anderson regime classification (AKD1000)**, metalForge cross-substrate validation |

groundSpring now contributes to ALL 9 baseCamp papers — reflecting the expansion
from 5 experiments (sensor noise only) to 28 experiments across 9 scientific
domains including live NPU hardware. The spectral theory experiments (008, 009,
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

### Previous Immediate (V60 → V61)

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

### Medium-term

- **BarraCUDA CPU vs GPU validation**: groundSpring pipeline infrastructure
  enables systematic BarraCUDA CPU ↔ GPU parity testing across all 61
  delegated functions. Foundation for ToadStool compute dispatch evolution.
- **Pure GPU workload**: End-to-end Anderson spectral analysis on GPU
  without CPU round-trips — the final validation of the BarraCuda
  evolution path.
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
