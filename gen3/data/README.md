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

**Current state**: One developer, one gate at a time, running experiments sequentially. This is the baseline — what constrained evolution produces on a single RTX 4070 in a basement.

---

## What NUCLEUS Unlocks

The 2,513 checks above were produced on single gates, running one experiment at a time. NUCLEUS changes the economics by composing the basement HPC into a coordinated mesh.

### The Hardware (Today)

| Gate | CPU | GPU | RAM | Role |
|------|-----|-----|-----|------|
| Northgate | i9-14900K | RTX 5090 | 192GB DDR5 | Flagship AI/LLM |
| Southgate | 5800X3D | RTX 3090 | 128GB DDR4 | Heavy compute |
| Eastgate | i9-12900 | RTX 4070 + Akida NPU | 32GB DDR5 | Utility + neuromorphic |
| Strandgate | Dual EPYC 7452 (64 cores) | RTX 3090 + RX 6950 XT + 2x Akida | 256GB ECC DDR4 | Bioinformatics |
| Westgate | i7-4771 | RTX 2070 Super | 32GB DDR3 | 76TB ZFS cold storage |
| + 4 more towers | Mixed | Mixed | 288GB total | Staging, flock, expansion |

**Aggregate**: 100+ CPU cores, ~128GB GPU VRAM (NVIDIA + AMD), ~1TB system RAM, ~100TB storage, 3x Akida NPU (160 NPUs), 10G backbone. ~$15K total investment.

### Covalent Bonding: The Basement as a Supercomputer

With NUCLEUS deployed, each gate runs its own NUCLEUS atomic composition. biomeOS coordinates the mesh. The bonding model (see `ECOSYSTEM_ARCHITECTURE.md` §4) determines how gates share capabilities:

- **Covalent bonding** (family gates): Full genetic trust. Workloads flow freely across gates. Strandgate's 64 cores handle CPU-bound bioinformatics while Northgate's RTX 5090 handles GPU-bound ML. Westgate's 76TB ZFS stores everything. No human orchestration — biomeOS routes workloads to hardware that matches.

- **What this means for the springs**: Instead of running one experiment per gate, all 5 springs run simultaneously across the mesh. hotSpring's Yukawa MD on Northgate's 5090. wetSpring's 16S pipeline on Strandgate's EPYC. neuralSpring's LSTM training on Southgate's 3090. groundSpring's Monte Carlo on Eastgate's 4070. All writing to Westgate's ZFS. The BarraCUDA WGSL shaders run identically on NVIDIA and AMD — validated on both in the mesh.

### Ionic Bonding: Others Join

The bonding model supports **ionic bonding** — contract-scoped access for external collaborators. A professor's lab GPU contributes compute under a metered contract. They get access to specific capabilities (e.g., run BarraCUDA lattice QCD on their parameter sweep) but not to the family's genetic lineage or storage. Usage is auditable. Access is scoped.

Scenario: Murillo's group has persoanl GPUs. Bazavov's group has personal GPUs. Kachkovskiy has a RTX 5080 GPU. If each runs a NUCLEUS with ionic bonding to the basement mesh:

- Murillo's gates run Sarkas parameter sweeps across the Γ-κ grid
- Bazavov's gates run lattice QCD temperature scans
- Kachkovskiy's gates run Anderson localization eigenvalue computations
- The basement mesh coordinates, stores results, and provides the BarraCUDA kernel library

Each group maintains sovereignty over their hardware. The mesh is voluntary. The science is shared. The compute cost is split. AGPL-3.0 ensures all improvements flow back.

### Metallic Bonding: MSU Turns ICER Into a Lattice

MSU's Institute for Cyber-Enabled Research (ICER) runs a traditional HPC: identical nodes, centralized scheduler, homogeneous workloads. In the NUCLEUS bonding model, this is **metallic bonding** — an electron sea of delocalized compute. Sub-specialized. Efficient for throughput. No sovereignty per node.

If ICER deployed NUCLEUS atomics on its nodes, every idle GPU on campus becomes a BarraCUDA compute node. The WGSL shaders are vendor-agnostic — they run on whatever GPU ICER has. The lattice QCD workloads that currently require CERN's HPC or Fermilab's allocation could run on Michigan State's campus GPU fleet.

The math:

- CERN's LHCC computing: ~1M CPU cores, ~50K GPUs, $1B+ infrastructure
- MSU ICER: ~20K cores, ~200 GPUs, ~$50M infrastructure
- Basement mesh: 100 cores, 8 GPUs, $15K
- BarraCUDA cost per hotSpring paper: **$0.01-0.10**

NUCLEUS doesn't make the basement as fast as CERN. It makes the *science-per-dollar* comparable, because the constraint isn't raw FLOPS — it's whether the compute produces correct, reproducible, published-quality results. 2,513 checks say it does.

The path from a basement in Lansing to a distributed physics computing network:

```
Basement (covalent)
  └──→ Faculty labs join (ionic)
        └──→ ICER deploys NUCLEUS (metallic)
              └──→ Other universities join (ionic/metallic)
                    └──→ Distributed science mesh
```

Each step is additive. Each step preserves sovereignty. Each step uses the same BarraCUDA kernels validated by the springs. The 2,513 checks don't need to be re-run — they're the acceptance tests for every new node that joins.

---

## Relationship to gen3/ Papers

- `SPRING_CATALOG.md` claims specific check counts → the spring repos contain the runnable experiments
- `PRIMAL_CATALOG.md` claims specific benchmark numbers → `HOTSPRING_PHASE_B_EVIDENCE.md` provides the raw data
- `CONSTRAINED_EVOLUTION_FORMAL.md` claims constraints drive fitness → 2,513 checks across 5 domains are the evidence
- `ECOSYSTEM_ARCHITECTURE.md` describes hardware-aware workload distribution → the springs validate that different hardware performs differently on the same workloads
- `FACULTY_SPRING_PROFILES.md` maps professors to candidate papers → the spring `specs/PAPER_REVIEW_QUEUE.md` files track reproduction status
