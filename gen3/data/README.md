# gen3/data/ - Benchmark Data and Reproduction Studies

**Status**: Framework established, data collection in progress  
**Last Updated**: February 7, 2026

---

## Purpose

This directory contains benchmark data from the ecoPrimals ecosystem and reproduction studies of published computational research. Every reproduction study follows a two-phase approach:

1. **Phase A**: Reproduce the original work using the original tools (Python/NumPy/Numba) to validate correctness and establish a baseline.
2. **Phase B**: Re-execute the same computation on **BarraCUDA** - ToadStool's Pure Rust GPU compute engine (165+ ops, 226+ WGSL shaders) that runs on any GPU vendor without CUDA, ROCm, or any vendor SDK.

The Phase A → Phase B comparison is itself a research contribution: can Pure Rust + WGSL match or exceed Python + CUDA for real scientific workloads?

---

## Directory Structure

### `toadstool-benchmarks/` (In Progress)

Benchmark data from ToadStool's universal compute framework, running across the heterogeneous HPC mesh. ToadStool is actively running NPU and GPU workloads and writing FHE (fully homomorphic encryption) benchmarks as of February 2026.

**Planned contents**:
- NPU vs GPU vs CPU comparison data (CSV/JSON) from live workloads
- BarraCUDA tensor operation benchmarks across NVIDIA (RTX 3090, RTX 4070, RTX 5090) and AMD (RX 6950 XT)
- BrainChip Akida neuromorphic benchmarks (k-mer filtering, intent classification, image classification)
- Power efficiency measurements across substrates
- Cross-substrate validation (same math, different hardware, identical results)

**Source**: Phase 1 neuromorphic benchmark datasheet already shared with Professor Murillo (see `neuromorphic_benchmark_datasheet_v1.md`).

### `murillo-group-reproduction/` (Planned)

Two-phase reproduction studies of published work from the Murillo Group at MSU. Phase A validates correctness using the original Python tools. Phase B re-executes the same physics on BarraCUDA's vendor-agnostic Pure Rust GPU compute layer. Three studies planned: Sarkas molecular dynamics, surrogate learning (Nature Machine Intelligence 2024, data on Zenodo + Code Ocean), and agent-based infectious disease modeling.

See `MURILLO_REPRODUCTION_PLAN.md` for detailed kernel-to-shader mappings and the full two-phase design.

---

### `MISE_EN_PLACE.md`

Infrastructure setup document. Catalogs every repository, Python dependency, data source, storage location, and hardware assignment needed for the reproduction studies and benchmark data collection. This is the pre-NUCLEUS preparation checklist - everything gathered and organized so we're ready to execute when NUCLEUS is stable and Westgate's Nest Atomic is managing cold data.

**Contents**:
- Sarkas: installation, conda env, FFTW3/FMM3D external deps
- Surrogate learning: Zenodo datasets, Code Ocean capsule, mystic optimizer
- Two-Temperature Model: repo structure, Python deps
- Additional Murillo Group repos (BIM_HNC, Thomas-Fermi, Teaching_Content)
- ToadStool benchmark data format and storage plan
- BarraCUDA op inventory and kernel-to-shader mapping (Phase B)
- Westgate ZFS storage architecture and access patterns
- Python environment strategy (per-gate conda envs for Phase A)
- Three-tier checklist: pre-NUCLEUS, Phase A (Python), Phase B (BarraCUDA)

### `BARRACUDA_SCIENTIFIC_COMPUTE_GAPS.md`

Gap analysis from the first examination of BarraCUDA through a computational physics lens rather than ML/AI/FHE. Documents what scientific computing reveals as new evolution targets: complex number arithmetic, complex FFT (evolutionarily related to the existing NTT for FHE), periodic boundary conditions, physics force kernels, Bessel functions, ODE/PDE solvers, scientific interpolation, eigendecomposition, and high-quality PRNG. Also documents the unexpected finding that ML-driven evolution already covers ~60-70% of scientific computing needs because the underlying math is shared. Estimates ~25-40 new shaders needed to make BarraCUDA a universal scientific compute engine.

---

## Relationship to gen3/ Papers

The `PRIMAL_CATALOG.md` claims specific benchmark numbers. This directory provides the raw data behind those claims. The `ECOSYSTEM_ARCHITECTURE.md` describes hardware-aware workload distribution. This directory provides the evidence that different hardware actually performs differently on the same workloads, validating the heterogeneity principle.

---

## Status: Mise en Place

This work is blocked on NUCLEUS stability. The reproduction studies require Westgate's Nest Atomic for cold data storage, the 10G backbone for data transfer, and biomeOS for workload coordination. Until then, we're in preparation mode: gathering ingredients, documenting procedures, validating individual components. See `MISE_EN_PLACE.md` for the full pre-NUCLEUS checklist.
