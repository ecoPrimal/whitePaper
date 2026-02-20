# gen3/data/ — Reproduction Studies, Faculty Profiles, and Evolution Evidence

**Status**: Active — 5 springs producing validated science  
**Last Updated**: February 20, 2026

---

## Purpose

This directory contains the evidence behind the gen3/ papers: reproduction plans, faculty profiles, benchmark data, and gap analyses. Every claim in `SPRING_CATALOG.md` and `PRIMAL_CATALOG.md` traces back to runnable experiments in the public spring repositories.

The two-phase validation approach:

1. **Phase A**: Reproduce published work using original tools (Python/NumPy/SciPy/PyTorch) to validate correctness and establish a baseline.
2. **Phase B+**: Re-execute the same computation on **BarraCUDA** — ToadStool's Pure Rust GPU compute engine (165+ ops, 226+ WGSL shaders) that runs on any GPU vendor without CUDA, ROCm, or vendor SDK.

Phase A → Phase B comparison is itself a research contribution: can Pure Rust + WGSL match or exceed Python + CUDA for real scientific workloads? Answer: yes — 478x throughput at L1, 1,077x spectral cosine matching, 43-78x fused ML inference pipeline.

---

## Documents

### Faculty & Spring Connections

**`FACULTY_SPRING_PROFILES.md`** — Master reference mapping 9 professors to springs and candidate papers for reproduction. Each profile includes: connection to author, key research themes, candidate papers with spring relevance, BarraCUDA kernel coverage, and reproduction priority tiers. Covers Murillo (hotSpring), Dong (airSpring), Waters/Cahill/Smallwood/Jones (wetSpring), Dolson/Liu/Bazavov (neuralSpring/groundSpring), and Kachkovskiy (hotSpring/groundSpring/neuralSpring). 60+ candidate papers ranked across 3 tiers.

### Reproduction Plans

**`MURILLO_REPRODUCTION_PLAN.md`** — Detailed plan for reproducing Murillo Group computational physics. Documents the Phase A → Phase C pipeline that produced hotSpring's 195/195 checks: Sarkas MD (60 observable checks across 12 DSF cases), TTM (6/6 equilibration), surrogate learning (15/15 benchmark functions), nuclear EOS (full AME2020 dataset, 2,042 nuclei). Phase C GPU MD runs on a $600 RTX 4070 for $0.044 — 1,000-10,000x cheaper than institutional HPC.

**Status**: Phase A COMPLETE (86/86), Phase C GPU MD COMPLETE (9/9 PP Yukawa at N=10,000), Phase F COMPLETE (195/195 total). Stanton-Murillo transport partially validated. Lattice QCD infrastructure (SU(3), HMC, Dirac CG) built and validated (12/12).

### Infrastructure

**`MISE_EN_PLACE.md`** — Pre-NUCLEUS infrastructure setup. Catalogs repositories, Python dependencies, data sources, storage locations, and hardware assignments for the reproduction studies. Originally written when the springs were planned; now serves as the historical record of how the infrastructure was prepared.

### Gap Analysis

**`BARRACUDA_SCIENTIFIC_COMPUTE_GAPS.md`** — Gap analysis from examining BarraCUDA through a computational physics lens rather than ML/AI/FHE. Documents what scientific computing reveals as evolution targets: complex number arithmetic, complex FFT, periodic boundary conditions, physics force kernels, ODE/PDE solvers, eigendecomposition, and sparse matrix operations.

Key finding: ML-driven evolution already covered ~60-70% of scientific computing needs because the underlying math is shared. The springs confirmed this — the 6 isomorphic primitives (GEMM, Attention, Normalization, Nonlinearity, Reduction, Gating) serve physics, biology, chemistry, and geophysics, not just neural networks.

Remaining P0-P1 gaps (driven by faculty extension papers):
- FFT (Bazavov lattice QCD, groundSpring spectral reconstruction)
- ODE solver (Waters c-di-GMP signaling dynamics)
- Lanczos eigensolve + SpMV (Kachkovskiy spectral theory)
- HMM Viterbi (Liu comparative genomics)
- Evolutionary optimization (Dolson counterdiabatic evolution)

### Benchmarks

**`HOTSPRING_PHASE_B_EVIDENCE.md`** — Phase B technical results: BarraCUDA vs Python/SciPy numbers for nuclear EOS computation. 478x L1 throughput, 44.8x energy reduction. GPU FP64 validated to 4.55e-13 MeV precision.

**`neuromorphic_benchmark_datasheet_v1.md`** — BrainChip Akida neuromorphic benchmark results. Shared with Professor Murillo early 2026. k-mer filtering 2.3x faster and 53x more power-efficient vs CPU.

---

## Current Science Production (February 20, 2026)

| Spring | Experiments | Checks | Papers Reproduced | Domain |
|--------|-----------|--------|------------------|--------|
| hotSpring | 6 phases | 195 | 4 published + lattice QCD infra | Plasma physics, nuclear structure |
| airSpring | 4 + Rust + cross-val | 326 | 3 published + real data pipeline | ET₀, soil moisture, IoT |
| wetSpring | 42 experiments | 1,116 | 8 pipelines + 4 BioProject benchmarks | 16S, LC-MS, PFAS, GPU pipeline |
| groundSpring | 5 experiments | 71 | 5 noise characterization baselines | Sensors, weather, seismic, microbiome |
| neuralSpring | 10 + Rust + GPU | 805 | 5 published (PINN, DeepONet, LeNet-5, LSTM, quantized) | ML primitives, scholarly reproduction |
| **Total** | | **2,513** | **20+** | **6 scientific domains** |

All spring repositories are public under AGPL-3.0. No institutional access required. No proprietary software. Runs on consumer hardware purchased from Newegg and Facebook Marketplace.

---

## Relationship to gen3/ Papers

- `SPRING_CATALOG.md` claims specific check counts → the spring repos contain the runnable experiments
- `PRIMAL_CATALOG.md` claims specific benchmark numbers → `HOTSPRING_PHASE_B_EVIDENCE.md` provides the raw data
- `CONSTRAINED_EVOLUTION_FORMAL.md` claims constraints drive fitness → 2,513 checks across 5 domains are the evidence
- `ECOSYSTEM_ARCHITECTURE.md` describes hardware-aware workload distribution → the springs validate that different hardware performs differently on the same workloads
- `FACULTY_SPRING_PROFILES.md` maps professors to candidate papers → the spring `specs/PAPER_REVIEW_QUEUE.md` files track reproduction status
