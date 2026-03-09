# Chuna Review Package — hotSpring v0.6.23

**Date**: March 8, 2026
**Author**: Kevin Mok (mokkevin@msu.edu)
**Repository**: [github.com/syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring) (AGPL-3.0)

---

## Hardware

The initial Murillo Group reproduction work (Sarkas MD, TTM, surrogate learning,
Stanton-Murillo transport) was done on **Eastgate** — an i9-12900K workstation with
an RTX 4070 (12 GB, $600). That proved consumer GPUs could do the plasma MD physics.

To extend into lattice QCD, dynamical fermions, and Chuna's gradient flow work,
I built **biomeGate** — a semi-mobile mini HPC:

| Component | biomeGate | ICER |
|-----------|-----------|------|
| CPU | Threadripper 3970X (32c/64t) | Cluster nodes |
| GPU (primary) | **RTX 3090** (24 GB, Ampere) | — |
| GPU (secondary) | **Titan V** (12 GB HBM2, native f64) | — |
| NPU | BrainChip AKD1000 (80 NPs, PCIe) | — |
| RAM | 256 GB DDR4 | — |
| Storage | 5 TB NVMe | — |
| Total cost | ~$4,000 (used parts) | $M+ institutional |
| Software | Rust + WGSL (Vulkan, no CUDA) | MILC (C), Python, Fortran |
| Access | My basement | Institutional allocation |

The Chuna paper validations run on biomeGate. The RTX 3090 handles the GPU
compute (24 GB allows 48⁴ lattices GPU-resident). The Titan V provides native
f64 cross-validation via NVK (open-source Vulkan driver, Mesa 25.1.5).

---

## What We Reproduced — Three Papers, One Binary

All three of Chuna's published papers are reproduced and validated in a single
binary (`validate_chuna_overnight`) that runs end-to-end in ~5 hours
(~4 hours for the 16⁴ lattice; 8⁴ configs + Papers 44/45 complete in ~1 hour):

```bash
cargo run --release --bin validate_chuna_overnight
```

### Paper 43: Gradient Flow Integrators (Bazavov & Chuna, arXiv:2101.05320)

**What Chuna did on ICER**: SU(3) gradient flow using LSCFRK integrators on
MILC-generated configurations. Scale setting via t₀ and w₀.

**What we did at home**:

- Implemented 5 integrators: Euler, RK2, LSCFRK3W6 (Lüscher), LSCFRK3W7
  (Chuna-recommended), LSCFRK4CK (Carpenter-Kennedy 4th-order)
- **Derived the LSCFRK3 coefficients from first principles** — a compile-time
  Rust function solves the four Taylor order conditions. Our values match the
  paper exactly. We didn't copy coefficients; we derived them.
- Convergence sweep (ε = 0.02 → 0.001): measured orders 2.06/2.08/2.11 on 8⁴
  (finite-size suppressed from nominal 3/3/4; consistent trend, passes >1.5 threshold)
- t₀ and w₀ scale extraction works on 8⁴ and 16⁴ thermalized lattices
- W7 is ~2× more efficient than W6 for w₀, confirming the paper's recommendation

**Performance**:

| Substrate | 8⁴ W7 flow (t=0→1) | Speedup |
|-----------|:------------------:|:-------:|
| CPU (single core) | 5.56s | 1× |
| GPU (RTX 3090) | 0.14s | **38.5×** |

**Extension (in progress)**: We also run gradient flow on **dynamical N_f=4
staggered** configurations (50-trajectory thermalization via adaptive Omelyan
HMC + CG solver, then W7 flow). This matches Chuna's actual MILC setup — not
just quenched configs. The adaptive step controller tunes dt based on rolling
acceptance, starting from a volume-aware heuristic. Flow monotonicity is
confirmed on dynamical backgrounds; full thermalization validation is ongoing.

### Paper 44: Conservative BGK Dielectric (Chuna & Murillo, Phys. Rev. E 111, 035206)

**What Chuna did on ICER**: Derived completed Mermin susceptibility from
multicomponent BGK. f-sum rule, DSF, conductivity under NIF hot-spot conditions.

**What we did at home**:

- Standard Mermin dielectric function (number conservation)
- Completed Mermin (number + momentum, Eq. 26 correction)
- Multi-component Mermin (electron-ion, per-species susceptibility)
- All three on CPU (Rust) and GPU (WGSL f64 shaders)

**Key results**:
- Debye screening exact to 1e-12
- DSF positivity ≥98% (standard), ≥99% (completed)
- f-sum rule converging to −πωₚ²/2
- GPU-CPU parity: L² = 5.5e-7 (standard), 100% agreement (multi-component)

**Performance**: Rust CPU is **322× faster than Python** for the kinetic-fluid
CPU reference (same algorithm, same physics).

**Bug found**: 6 instances of incorrect complex×scalar multiplication in the
WGSL shader (`vec2 * vec2` is element-wise in WGSL, not complex multiplication).
After fixing, multi-component GPU agreement went from 4% → 100%. This is a WGSL
language footgun worth documenting.

### Paper 45: Multi-Species Kinetic-Fluid Coupling (Haack, Murillo, Sagert & Chuna, J. Comput. Phys. 2024)

**What Chuna did on ICER**: Hybrid kinetic-fluid model coupling BGK and Euler
solvers in different spatial regions. Reduces cost while preserving fidelity.

**What we did at home**:

- Multi-species BGK relaxation with mass/momentum/energy conservation, H-theorem
- 1D Euler shock tube (Sod problem) with HLL Riemann solver
- Full coupled kinetic-fluid interface with 3-iteration sub-iteration convergence
- GPU shaders for collision (`bgk_relaxation_f64.wgsl`) and Euler (`euler_hll_f64.wgsl`)

**Key results**:
- BGK mass conservation: exact (Δm = 0)
- Euler mass conservation: 1.4e-15
- Sod shock front resolved (contact + shock captured)
- Interface density matching between kinetic and fluid domains
- GPU-CPU parity within 15% on interface coupling

The interface sub-iteration is physics-based (convergence tolerance 0.01), not
hand-tuned. This matters — hand-tuned thresholds aren't recoverable in future runs.

---

## Cost Comparison: ICER vs Home

| | ICER | biomeGate |
|--|------|-----------|
| Hardware | HPC cluster ($M+) | ~$4,000 (used parts) |
| Access | Institutional allocation queue | Always available |
| Software stack | MILC (C) + Python + Fortran + CUDA | Rust + WGSL (one `cargo build`) |
| Vendor lock-in | CUDA (NVIDIA only) | Vulkan (any GPU vendor) |
| Gradient flow (8⁴, W7) | MILC production | **38.5× GPU speedup**, 0.14s |
| Kinetic-fluid coupling | Python | **322× Rust speedup** |
| Full validation (3 papers) | Hours across jobs | **~5 hours, single binary** (8⁴ papers in ~1 hr) |
| Overnight run | Batch queue | Runs immediately |
| Electricity | Institutional | ~$0.10 per full run |
| Reproducibility | Depends on cluster env | `cargo run` on any Vulkan GPU |

The point is not that biomeGate is faster than ICER in absolute terms — a large
cluster with many nodes will always win on throughput. The point is that **the
same physics runs correctly on hardware anyone can buy**, with no institutional
dependencies, no vendor SDK, and no access queue.

---

## DF64: An Additional Precision Tier

Consumer GPUs (RTX 3090, 4070) have fp64:fp32 ratios of ~1:64 — the fp64 ALUs
are throttled. We use **DF64 (double-float)**: f32-pair arithmetic on the abundant
FP32 cores, delivering 14-digit precision at **9.9× the throughput of native f64**.

| Tier | Digits | Hardware | Throughput (RTX 3090) |
|------|:------:|----------|:---------------------:|
| f32 | 7 | FP32 cores (native) | ~29 TFLOPS |
| **DF64** | **14** | **FP32 cores (paired)** | **~3.2 TFLOPS** |
| f64 | 15-16 | FP64 ALU (1:64 throttle) | ~0.3 TFLOPS |

Most scientific calculations need more than 7 digits but don't require a full 16.
DF64 fills that gap, turning idle FP32 silicon into useful precision. The Titan V
(genuine 1:2 fp64) serves as ground truth for cross-validation.

We've audited 9 cancellation-prone computation families across f32/DF64/f64
(Experiment 046). The physics is stable at all precision tiers for the algorithms
we use (stable BCS v², direct asymptotic plasma W(z)).

---

## What We Extended Beyond the Papers

1. **GPU acceleration** for all three papers — none of the originals used GPU compute
2. **Multi-component Mermin** (Paper 44) — electron-ion extension, not in the original
3. **Dynamical N_f=4 staggered flow** (Paper 43) — gradient flow on dynamical configs
4. **Cross-paper validation** — single binary validates all three papers together
5. **Precision stability audit** — stable algorithms at f32/DF64/f64 (Experiment 046)
6. **322× Rust-over-Python speedup** — same algorithm, same physics, compiled language
7. **38.5× GPU speedup** for gradient flow — WGSL shader reuses HMC infrastructure

---

## How to Reproduce

```bash
git clone https://github.com/syntheticChemistry/hotSpring
cd hotSpring/barracuda

# Full validation (all 3 papers, ~5 hours; skip 16⁴ for ~1 hour)
cargo run --release --bin validate_chuna_overnight

# Individual papers
cargo run --release --bin validate_gradient_flow      # Paper 43
cargo run --release --bin validate_dielectric          # Paper 44
cargo run --release --bin validate_kinetic_fluid       # Paper 45

# Convergence benchmark (Paper 43 extension)
cargo run --release --bin bench_flow_convergence

# DSF vs MD comparison (Paper 44, against Murillo Group plasma DB)
cargo run --release --bin validate_dsf_vs_md
```

**Requirements**: Rust (stable), a Vulkan-capable GPU with `SHADER_F64`.
No CUDA toolkit, no Python, no MILC, no vendor SDK. Works on NVIDIA (proprietary
or NVK), AMD (RADV), and Intel (ANV) drivers.

---

## What We're Asking

1. **Does the physics look right?** We reproduced your three papers on consumer
   hardware. Do our convergence data, scale-setting values, dielectric curves,
   and conservation results match what you'd expect from your ICER/MILC runs?

2. **Did we derive the integrators correctly?** We solved the four Taylor order
   conditions independently. Our coefficients match your paper. Can you confirm?

3. **Is the approach viable?** Pure Rust + WGSL, dispatched through Vulkan.
   No MILC, no Fortran, no CUDA. Does this seem like a credible path for the
   physics you work on?

---

## Detailed Paper Artifacts

Each paper has a standalone baseCamp document in the repository with the full
math, equations, numerical values, data provenance, and source file listings:

| Paper | baseCamp document |
|-------|-------------------|
| 43 | `whitePaper/baseCamp/chuna_gradient_flow.md` |
| 44 | `whitePaper/baseCamp/chuna_bgk_dielectric.md` |
| 45 | `whitePaper/baseCamp/chuna_kinetic_fluid.md` |

These are the reproducible artifact equivalents of the papers — everything
needed to verify the physics, trace the data, and understand the algorithms.

---

## References

- Bazavov, A. & Chuna, T. "Efficient integration of gradient flow in lattice gauge theory and properties of low-storage commutator-free Lie group methods." arXiv:2101.05320 (2021)
- Chuna, T. & Murillo, M.S. "Conservative dielectric functions and electrical conductivities from the multicomponent Bhatnagar-Gross-Krook equation." Phys. Rev. E 111, 035206 (2024)
- Haack, J.R., Murillo, M.S., Sagert, I. & Chuna, T. "Multi-species kinetic-fluid coupling for high-energy density simulations." J. Comput. Phys. (2024)
