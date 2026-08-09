# Rung 5 — Finite-Temperature QCD and the QCD Crossover on Consumer GPUs

**Status**: Infrastructure ready (asymmetric lattices work), data pending
**Target**: arXiv hep-lat + Physical Review D
**Dependency**: Rung 4 validated (Nf=2+1 at physical-ish pion mass)

---

## Abstract (Draft)

We present the first finite-temperature QCD calculation performed entirely on
consumer GPUs using vendor-agnostic WebGPU/WGSL compute. Using (2+1)-flavor
QCD with staggered fermions on Ns³×Nτ lattices, we scan across the QCD
crossover temperature by varying β at fixed Nτ = {6, 8, 10, 12}. We measure
the chiral condensate, Polyakov loop, chiral susceptibility, and trace anomaly,
demonstrating that consumer hardware can reproduce the essential thermodynamic
features of the QCD transition at T_c ≈ 155 MeV. Multi-GPU pipeline parallelism
and silicon offloading enable 32³×8 and 48³×12 ensembles on hardware costing
less than $5,000.

---

## Section Outline

### 1. Introduction
- QCD thermodynamics: deconfinement, chiral symmetry restoration
- The crossover at physical quark masses (T_c ≈ 155 MeV)
- State of the art: HotQCD, Wuppertal-Budapest, Bielefeld
- Our contribution: reproduce on sovereign hardware, open and verifiable

### 2. Finite-Temperature Lattice Setup
- Temperature: T = 1/(a·Nτ)
- Fixed-Nτ approach: vary β to scan T at given physical scale
- Zero-temperature companions: same β on Ns⁴ for subtraction
- Continuum limit: compare Nτ = 6, 8, 10, 12

### 3. Observables
- **§3.1 Polyakov loop**: ⟨L⟩ = (1/V) Tr Π_{τ=1}^{Nτ} U₄(x,τ)
- **§3.2 Chiral condensate**: ⟨ψ̄ψ⟩ via stochastic estimator (random source trick)
- **§3.3 Chiral susceptibility**: χ_disc = ∂²ln Z / ∂m²
- **§3.4 Trace anomaly**: (ε-3p)/T⁴ via anisotropy derivative method
- **§3.5 Pressure**: p/T⁴ via integral method
- **§3.6 Speed of sound**: c²_s = dp/dε

### 4. GPU Implementation for Finite-T
- **§4.1 Asymmetric lattice kernels**: Ns³×Nτ → different loop bounds
- **§4.2 Polyakov loop GPU kernel**: Ordered product along temporal direction
- **§4.3 Stochastic estimator on GPU**: Random source + CG solve
- **§4.4 Gradient flow for scale setting**: Same as Rung 4 but on finite-T configs
- **§4.5 Multi-Nτ scheduling**: Batch different Nτ values across GPUs
- **§4.6 Silicon offloading at finite-T**: Smaller Nτ → less temporal stencil → more ROP benefit

### 5. Results
- **§5.1 Polyakov loop vs T**: Crossover signal
- **§5.2 Chiral condensate vs T**: Symmetry restoration
- **§5.3 Susceptibility peak**: T_c determination
- **§5.4 Equation of state**: p/T⁴, ε/T⁴, s/T⁴, c²_s
- **§5.5 Continuum extrapolation**: Nτ → ∞ limit
- **§5.6 Comparison to HotQCD/WB**: Our values vs published

### 6. Discussion
- Accuracy: what Nτ achieves what precision?
- Cost per temperature point: consumer GPU vs HPC allocation
- Open thermodynamics: all data in pseudoSpore, reproducible
- Applications: neutron star EOS input, heavy-ion collision comparison

### 7. Conclusion
- Summary: QCD crossover on consumer hardware
- Limitations: quenched artifacts at small Nτ, continuum extrapolation quality
- Future: Columbia plot exploration, imaginary chemical potential

---

## Data Generation Plan

### Temperature scan at Nτ = 8 (primary)

| Ensemble | Lattice | β range | T/T_c range | N_traj each |
|----------|---------|---------|-------------|-------------|
| FT_32x8_scan | 32³×8 | 5.6-6.8 (20 pts) | 0.7-2.5 | 500 |
| FT_0T_32x32_companion | 32⁴ | matching β | T=0 | 200 |

### Continuum extrapolation

| Nτ | Lattice | Points | Purpose |
|----|---------|--------|---------|
| 6 | 24³×6 | 15 | Coarse |
| 8 | 32³×8 | 20 | Primary |
| 10 | 40³×10 | 15 | Fine |
| 12 | 48³×12 | 10 | Finest (multi-GPU) |

---

## Hardware Budget for Finite-T

The advantage of finite-T: the temporal direction is SHORT (Nτ = 6-12), so total
sites are much smaller than Ns⁴ symmetric lattices at the same spatial volume.

| Lattice | Sites | VRAM (est) | Traj time (est) | Hardware |
|---------|-------|------------|------------------|----------|
| 24³×6 | 82,944 | 0.4 GB | ~5 s | Any 4 GB card |
| 32³×8 | 262,144 | 1.5 GB | ~20 s | Any 8 GB card |
| 40³×10 | 640,000 | 4 GB | ~90 s | 8+ GB card |
| 48³×12 | 1,327,104 | 8 GB | ~5 min | 12+ GB card |

This means finite-T is CHEAPER than symmetric Nf=2+1 — it's the natural first
target for "exceeding labs" because volume ∝ Ns³·Nτ rather than L⁴.

---

## Comparison Targets

| Observable | HotQCD (2014) | Our target | Agreement needed |
|------------|--------------|------------|-----------------|
| T_c | 154±9 MeV | Within 10% | Demonstrates crossover |
| Δ⟨ψ̄ψ⟩/T² | Fig 3 of 1407.6387 | Qualitative match | Chiral restoration signal |
| p/T⁴ at 2T_c | ~3.5 (SB ~5.2) | Within 20% | Correct magnitude |
| c²_s minimum | ~0.15 near T_c | Qualitative dip | Softening signal |

---

## pseudoSpore: `hotspring-qcd-sun-v5.0.0-rung5`

Contents:
- All finite-T configs at multiple Nτ (ILDG format)
- Zero-temperature companion configs
- Observable measurements: Polyakov, chiral condensate, susceptibility
- Equation of state tables (with errors)
- Continuum extrapolation fits
- Comparison tables vs HotQCD/WB published values
- Source code (tagged release)

---

## Why Finite-T Matters for the PI Reviewers

- **Bazavov**: Co-author on HotQCD equation of state papers. Will immediately see
  whether our T_c and EOS match. This is his domain — sovereign reproduction of
  his published results validates the entire stack.
- **Murillo**: MILC collaboration member. Finite-T is where MILC has extensive data.
  A cross-check of our code against MILC thermodynamic ensembles is a strong claim.
- **Chuna**: Can load our finite-T configs into MILC spectroscopy tools and verify
  the screening masses independently.

---

*Scaffold only. Production requires Rung 4 completion (Nf=2+1 at lower pion mass).
Finite-T is the most cost-effective path to "exceeding labs" because the
temporal compression reduces total lattice sites by 4-8x compared to symmetric
volumes.*
