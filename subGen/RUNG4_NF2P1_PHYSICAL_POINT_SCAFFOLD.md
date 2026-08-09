# Rung 4 — Nf=2+1 QCD Toward the Physical Point on Consumer GPUs

**Status**: Code paths implemented, production data pending
**Target**: arXiv hep-lat + journal submission
**Dependency**: Rung 3 validated (Nf=2 dynamical confirmed)

---

## Abstract (Draft)

We present the first (2+1)-flavor QCD configuration generation on consumer
GPUs using vendor-agnostic WebGPU/WGSL compute. Two degenerate light quarks
and one strange quark are simulated using the Rational Hybrid Monte Carlo
algorithm with independent rational approximations for each sector. Scale
setting via the gradient flow parameter w₀ enables controlled approach to the
physical pion mass. We demonstrate that consumer hardware (total cost < $3,000)
can generate ensembles at m_π ≈ 300 MeV on 16⁴-24⁴ volumes, directly
competitive with early HPC lattice QCD ensembles from the 2000s but at
1/100th the hardware cost.

---

## Section Outline

### 1. Introduction
- Context: physical-point QCD is the gold standard
- Our program: progressive mass reduction on sovereign hardware
- Historical comparison: what lattice sizes/masses were state-of-art at each era
- Our contribution: first Nf=2+1 on consumer GPU via vendor-agnostic shader

### 2. Formulation
- Two-sector RHMC: det(D†D)^{1/2}_light × det(D†D)^{1/4}_strange
- Independent rational approximations (different spectral ranges)
- Mass preconditioning for both sectors
- Multiple timescale integration: gauge (coarse), strange (medium), light (fine)
- Metropolis test over combined action

### 3. Scale Setting and Tuning
- Wilson flow: ∂_t V_μ = -∂S/∂V_μ · V_μ
- w₀ definition: t² ⟨E(t)⟩ |_{t=w₀²} = 0.3
- Line of constant physics: adjust β, am_l, am_s to keep m_π/f_π fixed
- Stout smearing for improved chiral properties

### 4. GPU Implementation Details
- **§4.1 Two-sector force computation**: Interleaved solves, buffer management
- **§4.2 Gradient flow on GPU**: Flow integration kernel, observable measurement
- **§4.3 Memory pressure at Nf=2+1**: Two sets of pseudofermion vectors
- **§4.4 Precision folding for Nf=2+1**: f16 storage + DF64 solve saves 50% VRAM
- **§4.5 Multi-GPU pipeline**: Light sector on card A, strange on card B
- **§4.6 Silicon offloading budget**: Larger fraction to solvers → different silicon profile

### 5. Results
- **§5.1 Scale setting**: w₀/a vs β
- **§5.2 Pion mass progression**: m_π from heavy (600 MeV) toward light (300 MeV)
- **§5.3 Strange quark tuning**: m_K / m_π ratio
- **§5.4 Topological charge**: Q² sampling and autocorrelation
- **§5.5 Performance**: Traj/sec vs volume at Nf=2+1 (compared to Nf=2)
- **§5.6 Cost analysis**: $/config at various pion masses

### 6. Comparison to Published Ensembles
- MILC HISQ ensembles at similar parameters
- BMW collaboration (stout-smeared Wilson clover)
- HotQCD (HISQ thermodynamic ensembles)
- Our advantage: sovereign, verifiable, vendor-agnostic, accessible

### 7. Conclusion
- Nf=2+1 on consumer hardware: reality vs aspiration
- Path to physical point (m_π = 135 MeV): volume requirements
- Federation: other gates contribute compute via pseudoSpore sharing

---

## Data Generation Plan

| Ensemble | Lattice | β | am_l | am_s | m_π (est) | N_traj |
|----------|---------|---|------|------|-----------|--------|
| Nf2p1_8_600 | 8⁴ | 5.6 | 0.1 | 0.3 | ~600 MeV | 500 |
| Nf2p1_12_450 | 12⁴ | 5.8 | 0.05 | 0.2 | ~450 MeV | 500 |
| Nf2p1_16_350 | 16⁴ | 6.0 | 0.02 | 0.1 | ~350 MeV | 500 |
| Nf2p1_24_300 | 24⁴ | 6.2 | 0.01 | 0.08 | ~300 MeV | 300 |
| Nf2p1_32_250 | 32⁴ | 6.4 | 0.005 | 0.06 | ~250 MeV | 200 |

---

## Hardware Requirements

At Nf=2+1 with light quarks, memory and solver time dominate:

| Volume | VRAM (Nf=2+1, folded) | Traj time (est) | Cards needed |
|--------|----------------------|------------------|--------------|
| 8⁴ | 0.5 GB | ~2 s | 1 (any) |
| 12⁴ | 2 GB | ~15 s | 1 (any) |
| 16⁴ | 6 GB | ~90 s | 1 (8 GB+) |
| 24⁴ | 20 GB | ~10 min | 1 (24 GB) or 2 (12 GB) |
| 32⁴ | 48 GB | ~45 min | 2-3 cards (PCIe stream) |

Silicon offloading at Rung 4 gives 30-40% time savings via ROP force +
TMU prolongation + subgroup reduction. DF64 precision folding for spinors
reduces VRAM by 4x (f16 storage), making 24⁴ feasible on a single 24 GB card.

---

## pseudoSpore: `hotspring-qcd-sun-v4.0.0-rung4`

Contents:
- All Nf=2+1 configs (multiple masses) in ILDG format
- Gradient flow measurements (w₀ per ensemble)
- Hadron correlators (pion, kaon, proton)
- Scale setting analysis + line of constant physics data
- Source code (tagged release)
- MILC/HotQCD comparison where applicable

---

*Scaffold only. Production begins after Rung 3 validation and Rung 1-2
reviewer acceptance.*
