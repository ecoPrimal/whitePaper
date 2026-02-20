# ecoPrimals Spring Catalog: Status, Science, and Evolution

**Status**: Working paper
**Lineage**: Science validation companion to `PRIMAL_CATALOG.md`
**Last Updated**: February 12, 2026
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

### 1.1 hotSpring — Computational Plasma Physics

**Domain**: Dense plasmas, nuclear structure, molecular dynamics, surrogate learning
**Grade**: Most mature spring — Phase A through F complete
**Checks**: 195/195 quantitative checks pass
**Faculty**: Michael Murillo (CMSE, MSU — MSDS professor), Alexei Bazavov (CMSE + Physics, MSU — master's professor), Ilya Kachkovskiy (Math, MSU — spectral theory)
**Repository**: git@github.com:syntheticChemistry/hotSpring.git
**License**: AGPL-3.0

**What it validates**: hotSpring proves BarraCUDA can do first-principles computational physics on a consumer GPU. Sarkas Yukawa MD runs at paper parity (N=10,000, 80k production steps) on a $600 RTX 4070 for $0.044 in electricity — roughly 1,000-10,000x cheaper than institutional HPC allocations. The full AME2020 nuclear dataset (2,042 nuclei, 39x the published paper) runs on a single consumer GPU.

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| A (Python control) | Sarkas MD, TTM, surrogates, nuclear EOS | 86/86 | 5 silent upstream bugs found and fixed |
| B (BarraCUDA GPU) | Nuclear EOS L1/L2 | Validated | 478x speedup, 44.8x energy reduction |
| C (GPU MD) | Yukawa MD N=2,000 | 9/9 | 0.000% energy drift, 149-259 steps/s |
| D (f64 + scaling) | N=10,000 native WGSL | Validated | 5.3 min per case, native builtins |
| E (Paper parity) | N=10,000, 80k steps | 9/9 | 3.66 hours total, $0.044 electricity |
| F (Full nuclear EOS) | 2,042 nuclei AME2020 | 195 total | Consumer GPU does nuclear structure |

**Papers reproduced**: Sarkas Yukawa OCP, TTM, Diaw et al. (2024) Nat Mach Intel surrogate learning, SEMF→HFB nuclear EOS on full AME2020.

**Papers queued**: Bazavov [HotQCD] (2014) QCD EOS, Polyakov loop (2016), muon g-2 HVP (2025). See `hotSpring/specs/PAPER_REVIEW_QUEUE.md`.

**BarraCUDA kernels validated**: Yukawa force, Velocity Verlet, cell-list, thermostats, GEMM, BatchedEighGpu, FusedMapReduce, PPPM Ewald, SSF.

**BarraCUDA gaps identified**: FFT (momentum-space), complex f64 arithmetic, SU(3) matrix ops, Lanczos eigensolve + SpMV (Kachkovskiy spectral theory).

**Participates in**: ToadStool validation (primary GPU science driver), gen3 constrained evolution evidence.

---

### 1.2 airSpring — Precision Agriculture & Irrigation

**Domain**: Evapotranspiration, soil moisture sensing, IoT irrigation scheduling
**Grade**: Full Python→Rust→cross-validation pipeline complete
**Checks**: 142/142 Python + 101/101 Rust + 53/53 cross-validation = 296 total
**Faculty**: Younsuk Dong (BAE, MSU — new lab 2026)
**Repository**: git@github.com:syntheticChemistry/airSpring.git
**License**: AGPL-3.0

**What it validates**: airSpring proves BarraCUDA's Rust crate can replace the Python/Excel toolchain for precision agriculture. FAO-56 Penman-Monteith ET₀ computed in Rust matches Python to 1e-5 tolerance across 53 cross-validated values. Real data from 4 Michigan stations (918 station-days) achieves R²=0.967 against Open-Meteo's independent computation.

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| 0 (Python control) | FAO-56, Dong 2020 soil, Dong 2024 IoT, water balance | 142/142 | Paper examples matched exactly |
| 0+ (Real data) | 4 Michigan stations, 918 station-days | R²=0.967 | Open-Meteo ERA5 validates open data approach |
| 1 (Rust) | 5 validation binaries, 106 unit tests | 101/101 | Hargreaves ET₀, 10-crop Kc, sensor calibration |
| 2 (Cross-validation) | Python↔Rust value comparison | 53/53 | All values match within 1e-5 |

**Papers reproduced**: Allen et al. (1998) FAO-56 Chapters 2/4/8, Dong et al. (2020) soil sensor calibration, Dong et al. (2024) IoT irrigation pipeline.

**Papers queued**: Dong IoT field network, FAO-56 Chapter 7 dual Kc, regional ET₀ intercomparison. See `airSpring/specs/PAPER_REVIEW_QUEUE.md`.

**BarraCUDA kernels validated (Rust, pre-GPU)**: ET₀ Penman-Monteith, Hargreaves, Topp equation, SoilWatch 10 calibration, water balance.

**BarraCUDA gaps identified**: Richards equation PDE solver, crop growth model, batch ET₀ GPU dispatch (template ready).

**Participates in**: ToadStool validation (Rust science crate), Penny Irrigation (real-world application target).

---

### 1.3 wetSpring — Life Science & Analytical Chemistry

**Domain**: 16S metagenomics, LC-MS feature extraction, PFAS screening, microbial ecology
**Grade**: Most modules — 30 sovereign Rust modules, 1 runtime dependency
**Checks**: 135/135 CPU + 38/38 GPU = 173/173 total
**Faculty**: Christopher Waters (MMG, MSU — undergrad professor), Kevin Liu (CMSE, MSU — master's professor), Jesse Cahill & Chuck Smallwood (Sandia), A. Daniel Jones (BMB/Chemistry, MSU — PFAS job)
**Repository**: git@github.com:syntheticChemistry/wetSpring.git
**License**: AGPL-3.0

**What it validates**: wetSpring proves BarraCUDA can replace the Galaxy/QIIME2/Python bioinformatics stack with sovereign Rust. The complete 16S pipeline (FASTQ→quality→merge→derep→DADA2→chimera→taxonomy→diversity→UniFrac) runs in Rust with 1 runtime dependency (flate2 for gzip). GPU spectral cosine matching achieves **1,077x speedup** over CPU. The sovereign XML parser eliminates `quick-xml`; the sovereign FASTQ parser eliminates `needletail`.

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| 1 (Galaxy/Python) | 8 experiments in Galaxy/QIIME2/Python | Baselined | Published pipeline reproduced |
| 2 (Rust CPU) | 7 validation binaries, 30 modules, 284 tests | 135/135 | Sovereign bioinformatics in Rust |
| 3 (GPU) | 11 ToadStool primitives, f64 precision | 38/38 | 1,077x spectral cosine speedup |

**Pipelines validated**: Complete 16S (Galaxy/QIIME2 → Rust), LC-MS features (asari → Rust), PFAS screening (FindPFAS → Rust).

**Papers queued**: 22 candidates across 3 tracks — Waters c-di-GMP/QS (Track 1), Liu comparative genomics (Track 1b), Jones PFAS (Track 2). See `wetSpring/specs/PAPER_REVIEW_QUEUE.md`.

**BarraCUDA kernels validated**: FusedMapReduceF64, BrayCurtisF64, BatchedEighGpu, GemmF64, VarianceF64, CorrelationF64, CovarianceF64, WeightedDotF64.

**BarraCUDA gaps identified**: ODE solver (c-di-GMP dynamics), Gillespie stochastic sim, HMM Viterbi, Smith-Waterman alignment, phylogenetic likelihood.

**Key discovery**: `log_f64` bug in ToadStool — coefficients halved, causing ~1e-3 precision instead of ~1e-15. Found during Shannon entropy validation, fixed immediately in ToadStool core.

**Participates in**: ToadStool validation (GPU science, bug discovery), biomeOS (microbiome health monitoring), Squirrel (learned classifiers).

---

### 1.4 groundSpring — Measurement Noise & Uncertainty

**Domain**: Sensor noise characterization, inverse problems, error propagation, sensing systems
**Grade**: Phase 0 complete across 4 scientific domains
**Checks**: 71/71 quantitative checks pass
**Faculty**: Alexei Bazavov (CMSE + Physics, MSU), Christopher Waters (MMG, MSU), Kevin Liu (CMSE, MSU), Emily Dolson (CSE, MSU), Ilya Kachkovskiy (Math, MSU — Anderson localization)
**Repository**: git@github.com:syntheticChemistry/groundSpring.git
**License**: AGPL-3.0

**What it validates**: groundSpring establishes the uncertainty budget for every other spring. It decomposes measurement error into correctable bias and irreducible noise, quantifies which inputs dominate output uncertainty, and demonstrates how noise propagates through inverse problems. The framework — decompose, identify dominant source, quantify noise floor — is universal across domains.

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| 0 (Python) | 5 experiments across 4 domains | 71/71 | Unified noise characterization framework |

**Experiment catalog**:

| # | Domain | Checks | Key Finding |
|---|--------|--------|-------------|
| 001 | Agricultural sensors | 32/32 | EC5 bias-dominated (77%); site calibration removes most error |
| 002 | Meteorology (ERA5 vs station) | 5/5 | Representation noise dominates model-observation gap |
| 003 | ET₀ uncertainty (FAO-56) | 8/8 | Humidity dominates at 66% of total variance |
| 004 | Microbiome sequencing depth | 16/16 | Genus saturation at 5,000 reads; phyla robust at 100 reads |
| 005 | Seismic source inversion | 10/10 | ±2km horizontal, ±8.5km depth from ±0.5s noise |

**Papers queued**: 18 candidates — Bazavov spectral reconstruction, Waters biological signal specificity, Liu RAWR resampling, Kachkovskiy Anderson localization. See `groundSpring/specs/PAPER_REVIEW_QUEUE.md`.

**BarraCUDA gaps identified**: FFT (shared with hotSpring), Gillespie (shared with wetSpring), jackknife/bootstrap, regularized inversion, Lanczos eigensolve + SpMV (shared with hotSpring, needed for Kachkovskiy spectral methods).

**Cross-spring impact**: groundSpring Exp 003 told airSpring that humidity sensors matter most. Exp 004 told wetSpring that 5,000 reads is the genus saturation depth. Exp 001 told neuralSpring how much sensor noise to expect in transfer learning.

**Participates in**: All springs (provides uncertainty quantification), neuralSpring (noise labels for training robustness).

---

### 1.5 neuralSpring — Machine Learning Primitives & Isomorphic Patterns

**Domain**: Neural surrogates, transformers, sequence models, transfer learning, scholarly reproduction
**Grade**: Phase 0 + Phase 0+ complete with 5 published paper reproductions
**Checks**: 48/48 synthetic + 27/27 scholarly = 75/75 total
**Faculty**: Emily Dolson (CSE, MSU — master's professor), Kevin Liu (CMSE, MSU — master's professor), Christopher Waters (MMG, MSU — undergrad professor), Alexei Bazavov (CMSE + Physics, MSU), Ilya Kachkovskiy (Math, MSU — spectral/optimization landscape)
**Repository**: git@github.com:syntheticChemistry/neuralSpring.git
**License**: AGPL-3.0

**What it validates**: neuralSpring proves the **Isomorphism Theorem** — all neural architectures decompose into 6 fundamental primitives (GEMM, Attention, Normalization, Nonlinearity, Reduction, Gating), and BarraCUDA's WGSL shader library covers all 6. Phase 0+ extends this by reproducing 5 published studies (Raissi PINNs, Lu DeepONet, LeCun LeNet-5, LSTM on real ERA5 data, quantized inference), demonstrating that the validated primitives produce correct results on real scientific problems.

**Phase inventory**:

| Phase | What | Checks | Key Result |
|-------|------|--------|------------|
| 0 (Synthetic) | 5 experiments: surrogate, transformer, LSTM, transfer, isomorphic | 48/48 | 6 primitives explain all architectures |
| 0+ (Scholarly) | 5 published studies reproduced | 27/27 | PINN, DeepONet, LeNet-5, ERA5 LSTM, quantized inference |

**Studies reproduced**:

| Study | Paper | Result |
|-------|-------|--------|
| PINN Burgers | Raissi et al. (2019) J Comp Physics | L2 error 5.1% (Adam-only; paper: 0.06% with L-BFGS) |
| DeepONet | Lu et al. (2021) Nat Mach Intel | 1.2% mean L2 on operator learning |
| LeNet-5 MNIST | LeCun et al. (1998) | 98.89% accuracy (paper: ~99%) |
| LSTM ERA5 | Real Open-Meteo data | NSE=0.849, RMSE=3.46°C on 4 years Michigan |
| Quantized inference | INT8/INT4 methodology | INT8: 0.017% loss, INT4: 0.79% loss |

**Papers queued**: 11 candidates — Dolson counterdiabatic evolution (Nature Physics 2020), Liu PhyloNet-HMM, Waters cooperation game theory. See `neuralSpring/specs/PAPER_REVIEW_QUEUE.md`.

**BarraCUDA primitives validated**: GEMM, Attention, LayerNorm, BatchNorm, RMSNorm, ReLU, GELU, Conv2d, MaxPool, LSTM cell, autograd, quantized GEMV (Q4/Q8), MSE loss, Adam optimizer.

**BarraCUDA gaps identified**: Evolutionary optimization (GA/ES), HMM Viterbi, Gillespie simulation, L-BFGS optimizer, Lanczos eigensolve + SpMV (Kachkovskiy spectral, Hessian analysis).

**Critical gen3 connection**: Dolson's Iram et al. (2020) Nature Physics on counterdiabatic driving of evolution is the closest published analog to `CONSTRAINED_EVOLUTION_FORMAL.md`. Reproducing it would externally validate the ecoPrimals methodology.

**Participates in**: biomeOS PathwayLearner (validated ML primitives), Squirrel (quantized inference), NUCLEUS (isomorphic kernel sharing), all springs (surrogates, transfer learning).

---

## 2. The Spring Network

### 2.1 By the Numbers

| Metric | Value |
|--------|-------|
| Total springs | 5 |
| Total quantitative checks | 610+ passing |
| Scientific domains covered | Physics, agriculture, biology, chemistry, geophysics, ML |
| Papers reproduced | 15+ (published, peer-reviewed) |
| Papers queued for review | 57 candidates across all springs |
| Faculty connected | 9 professors (MSU + Sandia) |
| BarraCUDA kernels validated by springs | 25+ distinct GPU primitives |
| BarraCUDA bugs found by springs | 6 (5 upstream in Sarkas, 1 in ToadStool log_f64) |
| Languages | Python (Phase 0), Rust (Phase 1+), WGSL shaders (Phase 2+) |
| License | AGPL-3.0 (all springs, no exceptions) |
| Institutional access required | Zero |
| Proprietary software required | Zero |

### 2.2 Cross-Spring Data Flow

```
groundSpring (uncertainty)
    │
    ├──→ airSpring: "humidity dominates ET₀ uncertainty at 66%"
    ├──→ wetSpring: "genus saturation at 5,000 reads"
    ├──→ neuralSpring: "expect 0.004-0.021 m³/m³ sensor noise floor"
    └──→ hotSpring: "inverse problem depth poorly constrained"

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

wetSpring (biology + chemistry)
    │
    ├──→ ToadStool: "log_f64 bug found and fixed"
    ├──→ airSpring: "kriging spatial interpolation module"
    └──→ groundSpring: "sequencing noise calibrates rarefaction"
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

Full profiles: `data/FACULTY_SPRING_PROFILES.md`

### 2.5 BarraCUDA Gap Summary (Across All Springs)

| Gap | Requesting Springs | Priority | Faculty Driver | Impact |
|-----|-------------------|----------|---------------|--------|
| FFT | hotSpring (lattice QCD), groundSpring (spectral recon), wetSpring (signal) | P0 | Bazavov | Unlocks Bazavov extension + spectral methods |
| ODE solver (RK4) | wetSpring (c-di-GMP), groundSpring (bifurcation) | P0 | Waters | Unlocks signaling dynamics |
| Lanczos eigensolve | hotSpring (Dirac spectrum), groundSpring (Anderson localization), neuralSpring (Hessian) | P1 | Kachkovskiy | Unlocks spectral theory, sparse eigenvalue problems |
| SpMV (sparse matrix-vector) | hotSpring (lattice gauge), groundSpring (spectral), neuralSpring (sparse attention) | P1 | Kachkovskiy | Foundation for Lanczos + sparse computation |
| HMM Viterbi | neuralSpring (PhyloNet-HMM), wetSpring (metagenomics) | P1 | Liu | Unlocks comparative genomics |
| Evolutionary optimization | neuralSpring (counterdiabatic), groundSpring (Dolson) | P1 | Dolson | Unlocks constrained evolution validation |
| Smith-Waterman alignment | wetSpring (genomics), neuralSpring (sequence models) | P1 | Liu | Unlocks large-scale sequence analysis |
| Gillespie simulation | wetSpring (quorum sensing), groundSpring (biological noise) | P1 | Waters | Unlocks stochastic biology |
| Matrix exponentiation | hotSpring (SU(3) HMC), groundSpring (transport) | P2 | Kachkovskiy, Bazavov | General exp(A) for time evolution |
| L-BFGS optimizer | neuralSpring (PINN improvement) | P2 | Raissi | Closes PINN error gap (5.1% → ~0.06%) |

---

## 3. The Evidence

The springs answer a question the primals alone cannot: **does this infrastructure produce correct science?**

The primals prove that Rust can build a sovereign computing ecosystem. The springs prove that sovereign computing can reproduce published, peer-reviewed science — and in some cases, do it faster, cheaper, and more transparently than the institutional tools it replaces.

**Claim**: Open data can replace institutional access.
**Evidence**: airSpring achieves R²=0.967 across 918 station-days using only free, open APIs (Open-Meteo, NOAA CDO). No institutional weather station access required.

**Claim**: Consumer GPUs can do real science.
**Evidence**: hotSpring runs paper-parity Yukawa MD (N=10,000, 80k steps) on a $600 RTX 4070 for $0.044. The same computation costs $50-500 on institutional HPC.

**Claim**: Sovereign Rust can replace the Python scientific stack.
**Evidence**: wetSpring's 30 Rust modules with 1 runtime dependency cover the complete 16S pipeline. airSpring's Rust crate matches Python to 1e-5 across 53 cross-validated values.

**Claim**: BarraCUDA's 6 isomorphic primitives serve all domains.
**Evidence**: neuralSpring proves GEMM + Attention + Normalization + Nonlinearity + Reduction + Gating explain LLaMA, OpenFold, ResNet, ViT, MLP surrogates, and LSTM weather models. All 6 are WGSL shaders in BarraCUDA.

**Claim**: Science validation improves the infrastructure.
**Evidence**: wetSpring found and fixed the `log_f64` bug in ToadStool. hotSpring found and fixed 5 silent bugs in Sarkas upstream. groundSpring identified humidity as the bottleneck for ET₀ accuracy. Each discovery fed back into the system.

---

**Every check count in this catalog is measured, not estimated. Every paper reproduction runs on consumer hardware with no institutional access. Every spring is AGPL-3.0. The science is open because the methodology demands it.**
