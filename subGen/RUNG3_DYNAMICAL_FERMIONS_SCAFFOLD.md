# Rung 3 — Dynamical Fermions on Consumer GPUs via WebGPU/WGSL

**Status**: Code complete, data generation pending
**Target**: arXiv hep-lat (2nd preprint in the program)
**Dependency**: Rung 1-2 published + MILC comparison framework (Chuna)

---

## Abstract (Draft)

We extend our vendor-agnostic lattice QCD engine to include dynamical fermions
using the Rational Hybrid Monte Carlo (RHMC) algorithm with staggered quarks.
The multi-shift conjugate gradient solver and pseudofermion action are implemented
entirely in WGSL, executing on any Vulkan-capable GPU without CUDA or ROCm
dependencies. We demonstrate Nf=2 dynamical generation on consumer hardware
(NVIDIA RTX 3060 Ti, AMD RX 7900 XTX) and validate against the MILC code
at matching parameters. Hasenbusch mass preconditioning provides 3-5x
acceleration at physical-mass-like parameters. DF64 emulated double precision
ensures solver convergence to ε < 10⁻¹² residual, validated against native
FP64 reference paths.

---

## Section Outline

### 1. Introduction
- Motivation: full QCD (not just gauge) on sovereign hardware
- Our contribution: first vendor-agnostic dynamical fermion generation in WebGPU
- Position relative to MILC/openQCD/Grid (Fortran/C++/CUDA vs. WGSL)

### 2. Theoretical Framework
- Staggered Dirac operator: D_st = ½ Σ_μ η_μ(n) [U_μ(n)δ_{n+μ,m} - U†_μ(n-μ)δ_{n-μ,m}]
- Pseudofermion action: S_pf = φ† (D†D)^{-Nf/4} φ
- RHMC rational approximation: (D†D)^{-α} ≈ α₀ + Σ αₖ/(D†D + βₖ)
- Multi-shift CG: solve (D†D + σₖ)xₖ = b simultaneously
- Hasenbusch decomposition: separate UV/IR modes
- Force derivation: ∂S_pf/∂U for each pole

### 3. GPU Implementation
- **§3.1 Dirac operator kernel**: Stencil pattern, gauge-link loading, even-odd preconditioning
- **§3.2 Multi-shift CG**: 8-pole simultaneous solve, convergence monitoring per pole
- **§3.3 Pseudofermion force**: Gauge-covariant derivative, force accumulation via ROP atomics
- **§3.4 Memory management**: Per-pole solution vectors, precision folding for spinor storage
- **§3.5 Silicon offloading**: ROP force accumulation, TMU prolongation, subgroup reductions
- **§3.6 DF64 solver precision**: Double-single representation, solver convergence guarantee

### 4. Validation
- **§4.1 Free-field Dirac spectrum**: Compare eigenvalues vs analytic result
- **§4.2 Solver convergence**: CG iteration count vs mass, volume, condition number
- **§4.3 MILC comparison**: Same parameters, same configs → Δ < ε
- **§4.4 Reversibility**: Integrate forward-reverse, check ΔH
- **§4.5 Acceptance rate vs step size**: Creutz equality, optimal δτ
- **§4.6 Plaquette vs quark mass**: Physical expectation (lighter quarks → smaller ⟨P⟩)

### 5. Results
- **§5.1 Nf=2 plaquette vs β**: Table of results, comparison to published
- **§5.2 Pion correlator and effective mass**: mπ vs m_quark scan
- **§5.3 Performance**: Traj/sec vs volume, solver time breakdown
- **§5.4 Cross-GPU agreement**: AMD vs NVIDIA at same parameters
- **§5.5 Hasenbusch speedup**: CG iterations saved, total time comparison

### 6. Discussion
- Vendor-agnostic dynamical QCD: implications for accessibility
- DF64 vs FP64 for solvers: when is ε < 10⁻¹² enough?
- Cost comparison: consumer GPU full-QCD vs HPC allocation
- Silicon offloading at Rung 3: force computation benefits from ROP at higher N

### 7. Conclusion and Outlook
- Summary of achievements (first WebGPU dynamical fermion code)
- Path to Nf=2+1 (Rung 4) and physical point
- Implications for lattice QCD democratization

---

## Data Generation Plan

| Ensemble | Lattice | β | am | N_traj | Hardware | ETA |
|----------|---------|---|-----|--------|----------|-----|
| Nf2_8_60_01 | 8⁴ | 6.0 | 0.1 | 1000 | RTX 3060 Ti | Near-term |
| Nf2_8_60_005 | 8⁴ | 6.0 | 0.05 | 1000 | RTX 3060 Ti | Near-term |
| Nf2_8_60_001 | 8⁴ | 6.0 | 0.01 | 1000 | RTX 3060 Ti | Near-term |
| Nf2_12_60_01 | 12⁴ | 6.0 | 0.1 | 500 | RTX 3060 Ti | After 8⁴ |
| Nf2_16_60_01 | 16⁴ | 6.0 | 0.1 | 500 | RX 7900 XTX | After 12⁴ |
| Nf2_16_60_005 | 16⁴ | 6.0 | 0.05 | 500 | RX 7900 XTX | After 12⁴ |
| Nf2_32_60_01 | 32⁴ | 6.0 | 0.1 | 200 | Multi-GPU | After capacity |

---

## MILC Comparison Protocol

For Chuna's requirement:

1. Export our thermalized configs in ILDG format
2. Run MILC spectroscopy on the same configs
3. Compare: our measured values vs MILC measured values on same gauge field
4. Report: Δ/σ for each observable
5. Additionally: run MILC HMC generation at matching params, compare ⟨P⟩ ensembles

---

## pseudoSpore: `hotspring-qcd-sun-v3.0.0-rung3`

Contents:
- All Nf=2 configs (.lat + .milc export)
- Solver convergence logs per trajectory
- Observable measurements (plaquette, pion correlator, meson masses)
- Source code (tagged release)
- MILC comparison tables
- BLAKE3 DAG + Ed25519 signature

---

## Silicon Continuum at Rung 3

The solver-dominated workload benefits differently from silicon offloading:

| Phase | ALU | ROP | TMU | Subgroup | NPU |
|-------|-----|-----|-----|----------|-----|
| CG iterations (solve) | 90% | — | — | 10% (dot) | — |
| Force (gauge + ferm) | 60% | 15% (atomic) | — | 25% (reduce) | — |
| Multigrid precondition | 40% | — | 40% (interp) | 20% (smooth) | — |
| Phase classification | — | — | — | — | 100% |
| Acceptance filter | — | — | — | — | ESN |

DF64 precision folding at Rung 3: store spinors in f16 for VRAM, promote to DF64
for solver arithmetic. 4x VRAM savings on spinor storage enables larger volumes.

---

*Scaffold only. Data generation begins after Rung 1-2 reviewer send and MILC
comparison framework is confirmed with Chuna.*
