# ecoPrimals Spring Catalog: Status, Science, and Evolution

**Status**: Working paper
**Lineage**: Science validation companion to `PRIMAL_CATALOG.md`
**Last Updated**: March 1, 2026
**License**: AGPL-3.0 — All springs are aggressively open science

---

## Abstract

This document catalogs every spring in the ecoPrimals ecosystem as of February 2026. Where the Primal Catalog (§`PRIMAL_CATALOG.md`) documents the Rust infrastructure that was built, this catalog documents the **scientific validation** that proves the infrastructure computes real physics, biology, chemistry, and mathematics correctly.

The springs exist because BarraCUDA's claim — "Pure Rust GPU compute can replace the Python scientific stack" — requires evidence from every scientific domain the ecosystem intends to serve. Each spring takes published, peer-reviewed work and asks: can we reproduce it? First in Python (the original tool). Then in Rust. Then on GPU. If the answers are yes, the science is validated and the BarraCUDA kernel is proven.

The springs are organized into two tiers:

- **Established Springs** (§1): Complete Phase 0 validation with passing quantitative checks. Each has Python baselines, whitePaper documentation, specs directories, and either Rust ports or GPU validation. These springs have been handed off to sub-teams for continued evolution.

- **The Spring Network** (§2): How springs connect to each other, to the primals, and to the faculty network that grounds them in published science.

---

## 1. The Springs

---

### 1.1 hotSpring — Computational Plasma Physics, Lattice QCD, Spectral Theory

**Domain**: Dense plasmas, nuclear structure, molecular dynamics, lattice QCD, spectral theory, neuromorphic computing
**Grade**: Most mature spring — Phase A through F complete, 21 experiments, 39/39 validation suites
**Checks**: 197+ quantitative checks pass (~697 tests, 78 binaries, 62 WGSL shaders)
**Faculty**: Michael Murillo (CMSE, MSU — MSDS professor), Alexei Bazavov (CMSE + Physics, MSU — master's professor), Ilya Kachkovskiy (Math, MSU — spectral theory), Rika Anderson (Biology, Carleton — *Sulfolobus* in Yellowstone hot springs, Taq corollary)
**Repository**: git@github.com:syntheticChemistry/hotSpring.git
**License**: AGPL-3.0

**What it validates**: hotSpring proves BarraCUDA can do first-principles computational physics on consumer hardware. Sarkas Yukawa MD runs at paper parity (N=10,000, 80k production steps) on a $600 RTX 4070 for $0.044 in electricity. The full AME2020 nuclear dataset (2,042 nuclei, 39x the published paper) runs on a single consumer GPU. Lattice QCD production β-scans (32⁴, 12 temperatures) resolve the deconfinement transition on a $500 RTX 3090 for $0.58. A $300 Akida NPU runs ESN inference at 2.8μs/step — 1000× faster than GPU for streaming workloads. GPU ESN dispatch via WGSL crosses over CPU at reservoir size ≈512 (8.2× faster at 1024).

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| A (Python control) | Sarkas MD, TTM, surrogates, nuclear EOS | 86/86 | 5 silent upstream bugs found and fixed |
| B (BarraCUDA GPU) | Nuclear EOS L1/L2 | Validated | 478× speedup, 44.8× energy reduction |
| C (GPU MD) | Yukawa MD N=2,000 | 9/9 | 0.000% energy drift, 149-259 steps/s |
| D (f64 + scaling) | N=10,000 native WGSL | Validated | 5.3 min per case, native builtins |
| E (Paper parity) | N=10,000, 80k steps | 9/9 | 3.66 hours total, $0.044 electricity |
| F (Full nuclear EOS) | 2,042 nuclei AME2020 | 9/9 | Consumer GPU does nuclear structure |
| Lattice QCD | SU(3) HMC + dynamical fermion + GPU streaming | 39/39 suites | 32⁴ β-scan, χ=40.1 at β=5.69 |
| Spectral | Anderson, Hofstadter, Lanczos | 45/45 | GPU SpMV + Lanczos validated |
| NPU | metalForge cross-substrate ESN + characterization | 48/48 | 10 SDK assumptions overturned, 2.8μs streaming |
| DF64 | FP32-core double precision | Validated | 3.24 TFLOPS, 9.9× native f64 throughput |

**Papers reproduced**: Sarkas Yukawa OCP, TTM, Diaw et al. (2024) surrogate learning, SEMF→HFB nuclear EOS on full AME2020, Stanton-Murillo transport (Green-Kubo), Murillo-Weisheit screened Coulomb (Sturm bisection), HotQCD EOS tables, SU(3) pure gauge Wilson action, dynamical fermion QCD (pseudofermion HMC), Abelian Higgs U(1), Anderson localization (1D/2D/3D), Hofstadter butterfly, Kachkovskiy spectral theory.

**Papers queued**: muon g-2 HVP (2025), WDM & ignition (Papers 32-42). See `hotSpring/specs/PAPER_REVIEW_QUEUE.md`.

**BarraCUDA kernels validated**: Yukawa force, Velocity Verlet, cell-list, thermostats, GEMM, BatchedEighGpu, FusedMapReduce, PPPM Ewald, SSF, SU(3) HMC (gauge force, plaquette, KE — all DF64), staggered Dirac, CG solver (GPU-resident), complex f64, Lanczos, SpMV, ESN reservoir update + readout.

**BarraCUDA gaps closed** (since Feb 20): ~~FFT~~ (done), ~~complex f64~~ (done), ~~SU(3) matrix ops~~ (done), ~~Lanczos eigensolve + SpMV~~ (done). GPU-resident CG reduces readback by 15,360×. DF64 core streaming delivers 14-digit precision on FP32 cores. Bidirectional streaming pipeline dispatches 90%+ to GPU with async readback.

**metalForge (NPU + cross-substrate)**: 21 experiments including NPU characterization campaign (6 pipeline placements, Akida feedback report drafted), cross-substrate ESN comparison (CPU/GPU/NPU), streaming pipeline topology with substrate routing. NPU achieves 9,017× less energy for transport predictions. GPU can function as ESN reservoir (crossover at RS≈512). See `hotSpring/metalForge/` and `hotSpring/whitePaper/baseCamp/neuromorphic_silicon.md`.

**Participates in**: ToadStool validation (primary GPU science driver), gen3 constrained evolution evidence, metalForge hardware exploration.

---

### 1.2 airSpring — Precision Agriculture & Irrigation

**Domain**: Evapotranspiration, soil moisture sensing, IoT irrigation scheduling
**Grade**: Full Python→Rust→GPU→NPU→metalForge pipeline complete
**Checks**: 1109 Python + 651 Rust + 1393 atlas + 75 cross-val = 4,153+ total
**Faculty**: Younsuk Dong (BAE, MSU — new lab 2026)
**Repository**: git@github.com:syntheticChemistry/airSpring.git
**License**: AGPL-3.0

**What it validates**: airSpring (v0.5.1) proves BarraCuda's Rust crate can replace the Python/Excel toolchain for precision agriculture. 45 experiments across 7 ET₀ methods, Richards PDE, soil hydraulics, yield response, Anderson coupling, NPU edge inference, and metalForge mixed hardware. Rust is 25.9× faster than Python (8/8 parity). Titan V GPU live dispatch (24/24 PASS, 0.04% seasonal parity). AKD1000 NPU live (95/95 checks). 100 Michigan stations, 15,300 station-days, R²=0.967 against Open-Meteo.

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| 0 (Python control) | FAO-56, Dong 2020 soil, Dong 2024 IoT, water balance | 142/142 | Paper examples matched exactly |
| 0+ (Real data) | 4 Michigan stations, 918 station-days | R²=0.967 | Open-Meteo ERA5 validates open data approach |
| 1 (Rust) | 7 binaries, 233 tests (161 unit + 72 integration) | 119/119 | Hargreaves ET₀, 10-crop Kc, sensor calibration |
| 2 (Cross-validation) | Python↔Rust value comparison | 65/65 | All values match within 1e-5 |

**Papers reproduced**: Allen et al. (1998) FAO-56 Chapters 2/4/8, Dong et al. (2020) soil sensor calibration, Dong et al. (2024) IoT irrigation pipeline.

**Papers complete**: 45 experiments validated. See `airSpring/specs/PAPER_REVIEW_QUEUE.md`.

**BarraCUDA kernels validated (Rust, pre-GPU)**: ET₀ Penman-Monteith, Hargreaves, Topp equation, SoilWatch 10 calibration, water balance.

**BarraCUDA gaps identified**: Richards equation PDE solver, crop growth model, batch ET₀ GPU dispatch (template ready).

**Participates in**: ToadStool validation (Rust science crate), Penny Irrigation (real-world application target).

---

### 1.3 wetSpring — Life Science & Analytical Chemistry

**Domain**: 16S metagenomics, LC-MS feature extraction, PFAS screening, microbial ecology
**Grade**: V86 — 30 sovereign Rust modules, 1 runtime dependency
**Checks**: 5,421+ validation checks (1,578 GPU) across 260+ experiments. 1,247 Rust tests, 92 named tolerances, 189 binaries (174 validate + 15 benchmark). 52/52 papers, 50/50 three-tier. ToadStool S68, 79 primitives consumed. 10 new Python baselines (Track 4 soil + NPU spectral). Cross-spring evolution validated (23/23 checks across 5 Springs). ESN bridge to ToadStool esn_v2 (BioEsn + multi-head). Deep debt elimination: all modules under 652 lines, 0 magic numbers, 0 unsafe, 0 mocks in production. Specs: `CROSS_SPRING_EVOLUTION.md`.
**Faculty**: Christopher Waters (MMG, MSU — undergrad professor), Kevin Liu (CMSE, MSU — master's professor), Jesse Cahill & Chuck Smallwood (Sandia), A. Daniel Jones (BMB/Chemistry, MSU — PFAS job), Rika Anderson (Biology, Carleton — vent metagenomics, pangenomics, phage ecology)
**Repository**: git@github.com:syntheticChemistry/wetSpring.git
**License**: AGPL-3.0

**What it validates**: wetSpring proves BarraCUDA can replace the Galaxy/QIIME2/Python bioinformatics stack with sovereign Rust. The complete 16S pipeline (FASTQ→quality→merge→derep→DADA2→chimera→taxonomy→diversity→UniFrac) runs in Rust with 1 runtime dependency (flate2 for gzip). GPU spectral cosine matching achieves **1,077x speedup** over CPU. The sovereign XML parser eliminates `quick-xml`; the sovereign FASTQ parser eliminates `needletail`.

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| 1-2 (Galaxy→Rust) | 16S + LC-MS + PFAS pipelines, 30 modules | 135/135 | Sovereign bioinformatics in Rust |
| 3 (GPU) | 11 ToadStool primitives, f64 precision | 38/38 | 1,077x spectral cosine speedup |
| 4 (Sovereign 16S) | DADA2 + chimera + taxonomy + UniFrac | 37/37 | Complete 16S in Rust |
| 5 (Paper parity) | Real NCBI data + VOC peaks | 51/51 | Algae pond + Reese 2019 match |
| 6 (Public benchmark) | 4 BioProjects vs paper ground truth | 202/202 | 22 samples, all match |
| 7 (GPU pipeline) | Full DADA2 + chimera + taxonomy on GPU | 88/88 | 10 samples, QF WGSL, streaming |
| V53-V58 | Anderson QS, Track 4 soil, drug repurposing, cross-spring S68 | 3,043+ | 52/52 papers, 79 primitives, 0 local WGSL |
| V59 | Science extensions + three-tier controls | 1,094+ | NCBI sovereign, cold seep, dynamic W(t), NPU sentinel, Exp190-192 |
| V66-V67 | Deep audit + experiment buildout + evolution | 733+ | 50/50 three-tier, BandwidthTier, ComputeDispatch, 10 Python baselines, Exp216-220 |
| V86 | Cross-Spring Evolution & Deep Debt (March 1, 2026) | Exp260-262 | Cross-spring validation 23/23 across 5 Springs; ESN bridge to ToadStool esn_v2 (BioEsn + multi-head); 4 module refactors, 11 new tests (1,247 total); 75 files changed, -4,753 net lines (deep debt elimination) |

**Pipelines validated**: Complete 16S (Galaxy/QIIME2 → Rust → GPU), LC-MS features (asari → Rust), PFAS screening (FindPFAS → Rust), public data benchmark (4 BioProjects, 22 samples, all match paper ground truth), real NCBI sovereign pipeline (EFetch/SRA → FASTA → diversity → Anderson), cold seep metagenome classification, dynamic Anderson W(t) perturbation models.

**Papers reproduced**: 52/52 across 4 tracks — Waters c-di-GMP/QS (Track 1), Liu comparative genomics (Track 1b), deep-sea metagenomics (Track 1c), Jones PFAS (Track 2). 50/50 three-tier eligible papers have full CPU + GPU + metalForge validation (11 extension papers promoted in V67). See `wetSpring/specs/PAPER_REVIEW_QUEUE.md`.

**BarraCUDA primitives consumed**: 79 via ToadStool S68 `compile_shader_universal` — including FusedMapReduceF64, BrayCurtisF64, BatchedEighGpu, GemmF64, anderson_3d, lanczos, lanczos_eigenvalues, level_spacing_ratio, and all diversity/spectral primitives. Zero local WGSL, zero local derivative/regression math.

**BarraCUDA gaps resolved by wetSpring**: ODE solver (bistable, capacitor, qs_ode), Gillespie stochastic sim, HMM Viterbi (phylohmm), Smith-Waterman alignment.

**Key discovery**: `log_f64` bug in ToadStool — coefficients halved, causing ~1e-3 precision instead of ~1e-15. Found during Shannon entropy validation, fixed immediately in ToadStool core.

**Participates in**: ToadStool validation (GPU science, bug discovery, 79 primitives consumed), biomeOS (microbiome health monitoring, science graph), Squirrel (learned classifiers), NestGate (NCBI JSON-RPC integration).

---

### 1.4 groundSpring — Measurement Noise & Uncertainty

**Domain**: Sensor noise characterization, inverse problems, error propagation, sensing systems, spectral theory, quasispecies, rare biosphere, jackknife, freeze-out
**Grade**: Phase 0 + Phase 1 (Rust) complete across 8 scientific domains
**Checks**: 236/236 Rust validation checks (all PASS), 280 Rust tests, 21/21 mathematical parity (Python == Rust)
**Faculty**: Alexei Bazavov (CMSE + Physics, MSU), Christopher Waters (MMG, MSU), Kevin Liu (CMSE, MSU), Emily Dolson (CSE, MSU), Ilya Kachkovskiy (Math, MSU — Anderson localization, Almost-Mathieu, transport, band edge), Rika Anderson (Biology, Carleton — stochastic vs deterministic evolution, drift, uncertainty bridge, rare biosphere)
**Repository**: git@github.com:syntheticChemistry/groundSpring.git
**License**: AGPL-3.0

**What it validates**: groundSpring establishes the uncertainty budget for every other spring. It decomposes measurement error into correctable bias and irreducible noise, quantifies which inputs dominate output uncertainty, and demonstrates how noise propagates through inverse problems. The framework — decompose, identify dominant source, quantify noise floor — is universal across domains. Phase 1 adds spectral theory (Anderson, Almost-Mathieu, band edge), transport, quasispecies, rare biosphere, jackknife, freeze-out, and spectral reconstruction.

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| 0 (Python) | 5 experiments across 4 domains | 71/71 | Unified noise characterization framework |
| 1 (Rust) | 21 experiments across 8 domains, dual-mode CI | 236/236 | 24 library modules, 27 barracuda delegations (22 CPU + 5 GPU) |

**Experiment catalog**:

| # | Domain | Checks | Key Finding |
|---|--------|--------|-------------|
| 001 | Agricultural sensors | 36 | EC5 bias-dominated (77%); site calibration removes most error |
| 002 | ERA5 observation gap | 13 | Representation noise dominates model-observation gap |
| 003 | FAO-56 ET₀ error propagation | 15 | Humidity dominates at 66% of total variance |
| 004 | Sequencing noise rarefaction | 15 | Genus saturation at 5,000 reads; phyla robust at 100 reads |
| 005 | Seismic source inversion | 9 | ±2km horizontal, ±8.5km depth from ±0.5s noise |
| 006 | Signal specificity | 12 | Waters bistable, multi-signal QS |
| 007 | RAWR resampling | 11 | Liu resampling convergence |
| 008 | Anderson localization | 8 | Kachkovskiy 1D/2D/3D |
| 009 | Almost-Mathieu localization | 8 | Kachkovskiy spectral theory |
| 010 | Bistable switching | 9 | Waters ODE dynamics |
| 011 | Multi-signal QS | 8 | Waters quorum sensing |
| 012 | Spin chain transport | 18 | Kachkovskiy transport |
| 013 | Resampling convergence | 8 | Liu RAWR |
| 014 | Drift vs selection | 7 | R. Anderson evolution |
| 015 | Uncertainty bridge | 8 | R. Anderson |
| 016 | Rare biosphere | 10 | R. Anderson |
| 017 | Quasispecies threshold | 6 | Dolson |
| 018 | Band edge structure | 10 | Kachkovskiy |
| 019 | Jackknife estimation | 9 | Bazavov |
| 020 | Freeze-out inverse | 8 | Bazavov |
| 021 | Spectral reconstruction | 8 | Bazavov |

**Papers completed**: Waters (signal specificity, bistable, multi-signal QS), Liu (RAWR, resampling convergence), Kachkovskiy (Anderson, Almost-Mathieu, transport, band edge), Dolson (quasispecies), R. Anderson (drift, uncertainty bridge, rare biosphere), Bazavov (jackknife, freeze-out, spectral recon).

**Papers queued**: Remaining candidates. See `groundSpring/specs/PAPER_REVIEW_QUEUE.md`.

**BarraCUDA gaps NOW**: FFT (resolved in hotSpring), batched_multinomial (Tier C), eigenvector solver (Tier C), grid search GPU (now implemented CPU). Most gaps resolved. **Cholesky solve batch** is the main NEW gap.

**Cross-spring impact**: groundSpring Exp 003 told airSpring that humidity sensors matter most. Exp 004 told wetSpring that 5,000 reads is the genus saturation depth. Exp 001 told neuralSpring how much sensor noise to expect in transfer learning. Spectral theory (Anderson, Almost-Mathieu, band edge) shared with hotSpring and wetSpring. Transport, quasispecies, rare biosphere feed wetSpring and neuralSpring. **Bazavov experiments (019-021) connect directly to hotSpring lattice QCD**: freeze-out inverse validates thermodynamic observable extraction, spectral reconstruction validates ill-posed inversion from Euclidean correlators, and jackknife provides the standard error estimation used in every lattice QCD publication. Combined pipeline: hotSpring (GPU simulation) → groundSpring (inverse problem + error bars) → neuralSpring (surrogate acceleration).

**baseCamp coordination**: groundSpring now contributes to ALL 7 baseCamp papers. The spectral theory experiments (008, 009, 012, 018) validate the Anderson framework underlying papers 01, 05, 06. The Bazavov experiments (019-021) serve paper 07 (WDM/lattice QCD). The evolutionary biology experiments (014, 016, 017) serve papers 02, 04. The sensor noise experiments (001-005) serve papers 03, 04, 06. This makes groundSpring the only spring that contributes to every baseCamp paper — reflecting its role as the universal uncertainty quantification layer.

**Evolution path**:

| Phase | Target | Status |
|-------|--------|--------|
| 0 (Python) | 21 experiments, ~211 Python checks | Complete |
| 1 (Rust CPU) | 236/236 Rust checks, 280 tests, 21/21 parity | Complete |
| 2a (BarraCUDA CPU) | Pure Rust math faster than Python, 27 delegations (22 CPU + 5 GPU) | Delegation inventory ready; ToadStool absorbing |
| 2b (BarraCUDA GPU) | GPU implementations match CPU exactly | Pending ToadStool absorption |
| 3 (metalForge) | Cross-substrate dispatch (GPU → NPU → CPU) | Architecture defined |

**Participates in**: All springs (provides uncertainty quantification), all 7 baseCamp papers, neuralSpring (noise labels for training robustness), hotSpring (spectral primitives + lattice QCD inverse problems), wetSpring (quasispecies, rare biosphere, Anderson validation).

---

### 1.5 neuralSpring — Machine Learning Primitives, Isomorphic Patterns & Sovereign Structure Prediction

**Domain**: Neural surrogates, transformers, sequence models, transfer learning, scholarly reproduction, structure prediction (coralForge)
**Grade**: Phase 0 → 0+ → 0++ → Rust → BarraCUDA CPU → GPU Tensor → metalForge WGSL → Pipeline → Cross-dispatch → Mixed-hardware → Multi-GPU → coralForge. **Most complete validation pipeline of any spring.**
**Checks**: 282/282 Python + 2918+ Rust+GPU = **3,200+ total** (685 lib + 9 integration + 43 forge tests, 197 binaries, 185/185 validate\_all)
**Faculty**: Emily Dolson (CSE, MSU — master's professor), Kevin Liu (CMSE, MSU — master's professor), Christopher Waters (MMG, MSU — undergrad professor), Alexei Bazavov (CMSE + Physics, MSU), Ilya Kachkovskiy (Math, MSU — spectral/optimization landscape), Rika Anderson (Biology, Carleton — pangenomics, constrained evolution empirics)
**Repository**: git@github.com:syntheticChemistry/neuralSpring.git
**License**: AGPL-3.0

**What it validates**: neuralSpring proves the **Isomorphism Theorem** — all neural architectures decompose into 6 fundamental primitives (GEMM, Attention, Normalization, Nonlinearity, Reduction, Gating), and BarraCUDA's WGSL shader library covers all 6. Phase 0++ extended to 15 papers across 4 faculty groups and 5 disciplines. **coralForge** is the sovereign structure prediction engine — pure Rust f64 implementations of AlphaFold2/AlphaFold3 primitives (Evoformer, IPA, diffusion, pairformer, confidence), validated against NumPy baselines and accelerated via BarraCUDA/ToadStool. Pure Rust is **83.6× faster** than Python/NumPy (geomean, 11 domains).

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| 0 (Synthetic) | 5 experiments: surrogate, transformer, LSTM, transfer, isomorphic | 48/48 | 6 primitives explain all architectures |
| 0+ (Scholarly) | 5 published studies reproduced | 31/31 | PINN, DeepONet, LeNet-5, ERA5 LSTM, quantized inference |
| 0++ (Extended) | 15 papers across 4 faculty, 5 disciplines | 127/127 | Evolutionary, phylogenetic, game theory, spectral, population genetics |
| 1a (Rust) | 40 modules + gpu\_ops/ + gpu\_dispatch | 685 lib + 9 integration + 43 forge | 197 validation/bench binaries |
| 2 (bC CPU) | BarraCUDA CPU ports — 24/25 papers (96%) | 203 | Machine-precision Rust math |
| 3 (GPU Tensor) | 23/25 papers (92%), metalForge 15/25, pipeline 15/25 | 272+ | CPU→GPU portability proven |
| 4 (Dispatch) | 47 CPU→GPU ops, dispatch parity 30/30, mixed-hardware 47/47 | 124+ | ~97% math on GPU |
| 5 (Multi-GPU) | RTX 4070 + TITAN V (NVK) — 384/384 bit-identical | 384 | Architecture-independent |
| coralForge | AlphaFold2/3 Evoformer, IPA, diffusion, pairformer, confidence | 62 Py + 55 Rs | Sovereign structure prediction |
| WDM | 5 warm dense matter surrogates | 186/186 | Physics surrogates validated |
| baseCamp | 5 biophysical AI sub-theses | 128/128 | GPU pure 5/5 |

**Studies reproduced**: All 25 papers from Phase 0++ + 5 Phase 0/0+ studies + 5 WDM surrogates + 3 publication experiments + coralForge nF-01/02/03 (AlphaFold2 Evoformer + AlphaFold3 diffusion/pairformer/confidence).

**BarraCUDA primitives validated**: 130+ import sites across 20+ submodules. 47 GPU-promoted dispatch ops (7 domain files). 44 upstream rewires. 21/21 WGSL shaders absorbed + 15 coralForge df64 shaders. 42 metalForge WGSL shaders. All gaps from original audit closed: HMM Viterbi (done), Gillespie (done), Lanczos (done via hotSpring lineage), pairwise distance (PairwiseL2Gpu), LogSumExp (upstream).

**BarraCUDA gaps remaining**: None critical. L-BFGS optimizer and compute_graph (lazy execution) are future Phase 5 items. All 17 shortcomings (S-01..S-17) resolved upstream.

**Critical gen3 connection**: Dolson's Iram et al. (2020) Nature Physics on counterdiabatic driving of evolution — **reproduced and validated** (Paper 011). coralForge extends the isomorphism to protein structure prediction: the same 6 primitives that serve language models serve AlphaFold.

**Participates in**: biomeOS PathwayLearner (validated ML primitives), Squirrel (quantized inference), NUCLEUS (isomorphic kernel sharing), all springs (surrogates, transfer learning), coralForge sovereign protein pipeline.

---

## 2. The Spring Network

### 2.1 By the Numbers

| Metric | Value |
|--------|-------|
| Total springs | 5 |
| Total quantitative checks | **11,161+** passing |
| Scientific domains covered | Physics, agriculture, biology, chemistry, geophysics, ML, neuromorphic computing |
| Papers reproduced | 70+ (published, peer-reviewed, across all springs) |
| Papers queued for review | 60+ candidates across all springs |
| Faculty connected | 10 professors (MSU + Sandia + Carleton) across 7 departments |
| BarraCUDA kernels validated by springs | 79+ distinct GPU/NPU primitives (wetSpring alone consumes 79 via ToadStool S68) |
| BarraCUDA bugs found by springs | 6 (5 upstream in Sarkas, 1 in ToadStool log_f64) |
| Rust validation checks | 1,008 (wetSpring) + 2,250+ (neuralSpring) + 4,153+ (airSpring) + ~697 (hotSpring) + 236 (groundSpring) |
| WGSL shaders | 700+ cross-spring via ToadStool S68 universal precision |
| Languages | Python (Phase 0), Rust (Phase 1+), WGSL shaders (Phase 2+) |
| License | AGPL-3.0 (all springs, no exceptions) |
| Institutional access required | Zero |
| Proprietary software required | Zero |
| Time from first spring to 11,161+ checks | ~27 days |

### 2.2 Cross-Spring Data Flow

```
groundSpring (uncertainty + spectral + quasispecies — 21 experiments, 236/236 checks, 8 domains)
    │
    ├──→ airSpring: "humidity dominates ET₀ uncertainty at 66%"
    ├──→ wetSpring: "genus saturation at 5,000 reads; quasispecies, rare biosphere"
    ├──→ neuralSpring: "expect 0.004-0.021 m³/m³ sensor noise floor; noise labels"
    ├──→ hotSpring: "inverse problem depth poorly constrained; Anderson, Almost-Mathieu, band edge spectral primitives"
    └──→ ToadStool: "27 barracuda delegations (22 CPU + 5 GPU)"

neuralSpring (ML primitives)
    │
    ├──→ airSpring: "MLP surrogate replaces FAO-56 at R²=0.999"
    ├──→ airSpring: "transfer learning bridges Michigan→NM with 200 samples"
    ├──→ hotSpring: "isomorphic GEMM serves plasma and nuclear"
    ├──→ wetSpring: "LSTM validates lstm_cell.wgsl on real weather"
    └──→ biomeOS: "PathwayLearner uses validated attention primitives"

hotSpring (GPU compute patterns)
    │
    ├──→ airSpring: "f64 GPU dispatch batching pattern"
    ├──→ wetSpring: "FusedMapReduceF64 pattern for bulk statistics"
    └──→ ToadStool: "195 acceptance checks, 6 bugs found"

wetSpring (biology + chemistry — 4,688+ checks, 197 experiments, 52/52 papers)
    │
    ├──→ ToadStool: "log_f64 bug found and fixed; 79 primitives consumed; three-tier validated (CPU→GPU→metalForge)"
    ├──→ ToadStool: "Anderson spectral primitives (anderson_3d, lanczos, level_spacing_ratio) validated at f64"
    ├──→ ToadStool: "Typed NCBI errors (Error::Ncbi) for sovereign data acquisition"
    ├──→ airSpring: "kriging spatial interpolation; dynamic Anderson W(t) models soil moisture coupling"
    ├──→ hotSpring: "Anderson localization applied to biology — shared spectral primitives, W_c determination"
    ├──→ neuralSpring: "ESN/LSTM anomaly detection for sentinel microbes; NPU int8 quantization validated"
    └──→ groundSpring: "sequencing noise calibrates rarefaction; 86 named tolerances with provenance"
```

### 2.3 Spring → Primal Connections

| Spring | Primarily Validates | Also Feeds |
|--------|-------------------|------------|
| hotSpring | ToadStool/BarraCUDA (GPU MD, nuclear EOS) | gen3 (constrained evolution evidence) |
| airSpring | ToadStool/BarraCUDA (Rust science crate) | Penny Irrigation (real-world application) |
| wetSpring | ToadStool/BarraCUDA (GPU diversity, spectral) | biomeOS (microbiome monitoring), Squirrel (classifiers) |
| groundSpring | All springs (uncertainty budget) | neuralSpring (noise labels for training) |
| neuralSpring | ToadStool/BarraCUDA (ML kernels) | biomeOS (PathwayLearner), Squirrel (inference), NUCLEUS (optimization) |

### 2.4 Faculty → Spring Mapping

| Professor | Department | Connection | Springs |
|-----------|-----------|-----------|---------|
| Michael Murillo | CMSE, MSU | MSDS professor | hotSpring |
| Younsuk Dong | BAE, MSU | New lab 2026 | airSpring |
| Christopher Waters | MMG, MSU | Undergrad professor | wetSpring, groundSpring, neuralSpring |
| Kevin Liu | CMSE, MSU | Master's professor | wetSpring, groundSpring, neuralSpring |
| Alexei Bazavov | CMSE + Physics, MSU | Master's professor | hotSpring, groundSpring, neuralSpring |
| Emily Dolson | CSE, MSU | Master's professor | neuralSpring, groundSpring |
| Ilya Kachkovskiy | Math, MSU | Sold NucBox M6 (FB Marketplace) | hotSpring, groundSpring, neuralSpring |
| Jesse Cahill | Sandia (Bioscience) | Time at Sandia | wetSpring |
| Chuck Smallwood | Sandia (Bioscience) | Time at Sandia | wetSpring |
| A. Daniel Jones | BMB/Chemistry, MSU | PFAS job | wetSpring |
| Rika Anderson | Biology, Carleton College | Literature search | hotSpring, wetSpring, groundSpring, neuralSpring |

Full profiles: `data/FACULTY_SPRING_PROFILES.md`

### 2.5 BarraCUDA Gap Summary (Across All Springs)

| Gap | Requesting Springs | Priority | Faculty Driver | Status |
|-----|-------------------|----------|---------------|--------|
| FFT | hotSpring (lattice QCD), groundSpring (spectral recon), wetSpring (signal) | P0 | Bazavov | **Resolved** — hotSpring |
| ODE solver (RK4) | wetSpring (c-di-GMP), groundSpring (bifurcation) | P0 | Waters | **Resolved** — wetSpring bistable, capacitor, qs_ode validated |
| Lanczos eigensolve | hotSpring (Dirac spectrum), groundSpring (Anderson), neuralSpring (Hessian) | P1 | Kachkovskiy | **Resolved** — wetSpring + hotSpring: `lanczos`, `lanczos_eigenvalues` validated (CPU + GPU) |
| SpMV (sparse matrix-vector) | hotSpring (lattice gauge), groundSpring (spectral), neuralSpring (sparse) | P1 | Kachkovskiy | **Resolved** — implemented for Lanczos + Anderson 3D |
| HMM Viterbi | neuralSpring (PhyloNet-HMM), wetSpring (metagenomics) | P1 | Liu | **Resolved** — wetSpring `phylohmm` module validated |
| Evolutionary optimization | neuralSpring (counterdiabatic), groundSpring (Dolson) | P1 | Dolson | Open — unlocks constrained evolution validation |
| Smith-Waterman alignment | wetSpring (genomics), neuralSpring (sequence models) | P1 | Liu | **Resolved** — wetSpring Exp028 validated |
| Gillespie simulation | wetSpring (quorum sensing), groundSpring (biological noise) | P1 | Waters | **Resolved** — wetSpring stochastic modules validated |
| Matrix exponentiation | hotSpring (SU(3) HMC), groundSpring (transport) | P2 | Kachkovskiy, Bazavov | Open — general exp(A) for time evolution |
| L-BFGS optimizer | neuralSpring (PINN improvement) | P2 | Raissi | Open — closes PINN error gap (5.1% → ~0.06%) |
| Cholesky solve batch | groundSpring (jackknife, spectral recon) | P1 | Bazavov | Open — main NEW gap |

---

## 3. The Evidence

The springs answer a question the primals alone cannot: **does this infrastructure produce correct science?**

The primals prove that Rust can build a sovereign computing ecosystem. The springs prove that sovereign computing can reproduce published, peer-reviewed science — and in some cases, do it faster, cheaper, and more transparently than the institutional tools it replaces.

**Claim**: Open data can replace institutional access.
**Evidence**: airSpring achieves R²=0.967 across 15,300 station-days (100 Michigan stations) using only free, open APIs (Open-Meteo, NOAA CDO). No institutional weather station access required.

**Claim**: Consumer GPUs can do real science.
**Evidence**: hotSpring runs paper-parity Yukawa MD (N=10,000, 80k steps) on a $600 RTX 4070 for $0.044. The same computation costs $50-500 on institutional HPC.

**Claim**: Sovereign Rust can replace the Python scientific stack.
**Evidence**: wetSpring's 30 Rust modules with 1 runtime dependency cover the complete 16S pipeline with 4,688+ checks across 197 experiments, 52/52 papers reproduced, and 39/39 three-tier validated (CPU→GPU→metalForge). airSpring's 45 experiments produce 4,153+ checks; Rust is 25.9× faster than Python with 8/8 numerical parity. 75/75 cross-validation match at 1e-5.

**Claim**: BarraCUDA's 6 isomorphic primitives serve all domains.
**Evidence**: neuralSpring proves GEMM + Attention + Normalization + Nonlinearity + Reduction + Gating explain LLaMA, OpenFold, ResNet, ViT, MLP surrogates, and LSTM weather models. All 6 are WGSL shaders in BarraCUDA.

**Claim**: Science validation improves the infrastructure.
**Evidence**: wetSpring found and fixed the `log_f64` bug in ToadStool. hotSpring found and fixed 5 silent bugs in Sarkas upstream. groundSpring identified humidity as the bottleneck for ET₀ accuracy. Each discovery fed back into the system.

---

**Every check count in this catalog is measured, not estimated. Every paper reproduction runs on consumer hardware with no institutional access. Every spring is AGPL-3.0 and publicly available on GitHub. The science is open because the methodology demands it. 11,161+ checks across 5 domains in 27 days — the constrained evolution methodology works. 7 of 11 BarraCUDA gaps have been resolved by the springs themselves (ODE, Lanczos, SpMV, HMM, Smith-Waterman, Gillespie, FFT). A $300 NPU runs ESN inference at 2.8μs/step. A $600 GPU runs the same ESN at 8.2× CPU speed when the reservoir is large enough. The silicon does what the silicon does — we just had to look.**
