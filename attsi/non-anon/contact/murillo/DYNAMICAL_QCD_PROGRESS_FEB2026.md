# Dynamical QCD Progress Report — February 2026

**Author:** Kevin Mok (mokkevin@msu.edu)
**Repository:** [github.com/syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring) (AGPL-3.0)
**Date:** February 28, 2026
**Depends on:** LATTICE_QCD_RESULTS_FEB2026 (quenched baseline)

---

## Summary

The quenched SU(3) runs described in the previous data sheet (Runs 1–2)
simulated pure gluons — no quarks. This report covers the next step:
**dynamical fermion QCD**, where virtual quark loops are included in the
simulation and react back on the gluon field.

The dynamical run is currently in production on an 8⁴ lattice. A
multi-physics proxy pipeline using Anderson localization and Z(3) Potts
models has been built and validated to extend the NPU's predictive
capabilities for future runs at 16⁴ and 32⁴.

| | Quenched (Runs 1–2) | Dynamical (Run 3, in progress) |
|--|:-------------------:|:------------------------------:|
| **Lattice** | 32⁴ | 8⁴ (validation → 16⁴ → 32⁴) |
| **Physics** | Pure gauge (no quarks) | Full QCD with staggered quarks |
| **Force** | Wilson gauge only | Gauge + fermion force (CG solver) |
| **Cost / trajectory** | 7.6 s (DF64) | ~40 s (+ CG solver, 8⁴) |
| **NPU heads** | 6 | 14 (expanded with physics proxies) |
| **β points** | 10–12 | 15 (NPU-steered) |
| **Status** | Complete | 15/15 β points, 966 trajectories |

---

## 1. What Changed: Quenched → Dynamical

### The physics

Quenched QCD treats the gluon field as if quarks don't exist. The
partition function is Z = ∫ DU exp(−S_gauge[U]). This is the
approximation used in Runs 1 and 2.

Dynamical QCD adds the fermion determinant: Z = ∫ DU det(M[U])
exp(−S_gauge[U]). The matrix M is the Dirac operator — it describes how
quarks propagate through the gluon field. The determinant det(M) captures
the back-reaction of virtual quark-antiquark pairs on the gluon field.

This changes the physics qualitatively:

- **Quenched:** The deconfinement transition is first-order (sharp jump).
- **Dynamical:** Quark loops screen the gluon interaction, softening the
  transition into a smooth crossover. No sharp jump, just a broad peak.
- **β_c shifts lower:** The critical coupling moves because fermions
  contribute additional attractive forces at the scale where confinement
  sets in.

### The computational cost

The fermion determinant cannot be computed directly (the matrix M is
enormous). Instead, it is evaluated stochastically using pseudofermion
fields and a Conjugate Gradient (CG) solver — an iterative algorithm
that solves the linear system (M†M + m²)x = b at every step of the
molecular dynamics trajectory.

For the 8⁴ lattice, CG requires ~55,000 iterations per trajectory.
Each iteration performs a sparse matrix-vector multiply across the full
lattice. This is the dominant cost: a single trajectory takes ~40 seconds
compared to ~7.6 seconds for quenched at 32⁴ with DF64. The CG solver
is why dynamical QCD is historically 10–100× more expensive than
quenched.

### Why we scaled down

The previous quenched runs used a 32⁴ lattice (1,048,576 sites). For
dynamical fermions, the CG solver cost scales with volume and condition
number. At 32⁴ with dynamical fermions, a single trajectory is estimated
at 8–15 minutes. A 15-point β scan with 65 measurements per point would
take 5–10 days.

We validated on 8⁴ first (4,096 sites) to:

1. Confirm the fermion force implementation is correct
2. Verify CG convergence across the full β range
3. Establish NPU adaptive steering for dynamical trajectories
4. Measure real scaling factors before committing to long runs

The path is: **8⁴ validate → 16⁴ scale → 32⁴ production**. Each step
uses measured data from the previous step to predict the next.

---

## 2. Production Run: 8⁴ Dynamical — Current Results

### Run parameters

| Parameter | Value |
|-----------|-------|
| Lattice | 8⁴ (4,096 sites) |
| Gauge action | Wilson SU(3) |
| Fermions | Staggered (1 flavor, m = 0.1) |
| Integrator | Omelyan leapfrog, dt = 0.01, n_md = 100 |
| GPU | RTX 3090 (DF64 hybrid) |
| NPU | BrainChip AKD1000 (14-head ESN) |

### Results by β point (15 points, 966 trajectories)

| β | n | Acc% | ⟨P⟩ | ⟨\|ΔH\|⟩ | ⟨CG⟩ | Wall/traj |
|--------|-----|------|--------|---------|---------|-----------|
| 4.4416 | 56 | 54% | 0.3285 | 0.753 | 55,045 | 41 s |
| 4.4969 | 65 | 45% | 0.3356 | 0.744 | 55,783 | 42 s |
| 4.5535 | 65 | 54% | 0.3426 | 0.729 | 55,769 | 52 s |
| 4.6116 | 65 | 54% | 0.3470 | 0.740 | 55,753 | 42 s |
| 4.6711 | 65 | 48% | 0.3546 | 0.727 | 55,649 | 41 s |
| 4.7321 | 65 | 48% | 0.3629 | 0.706 | 55,401 | 41 s |
| 4.7946 | 65 | 59% | 0.3702 | 0.696 | 55,051 | 41 s |
| 4.8603 | 65 | 51% | 0.3765 | 0.693 | 54,652 | 40 s |
| 4.9293 | 65 | 49% | 0.3891 | 0.658 | 54,431 | 40 s |
| 5.0000 | 65 | 54% | 0.4020 | 0.636 | 54,399 | 40 s |
| 5.5000 | 65 | 71% | 0.5146 | 0.371 | 51,422 | 37 s |
| 5.6900 | 65 | 79% | 0.5415 | 0.321 | 50,562 | 36 s |
| 6.0000 | 65 | 79% | 0.5711 | 0.285 | 46,848 | 34 s |
| 6.0673 | 65 | 77% | 0.5809 | 0.268 | 50,401 | 37 s |
| 6.1314 | 65 | 82% | 0.5883 | 0.249 | 46,079 | 34 s |

**Totals:** 966 trajectories, 10.6 hours wall time, 60% overall acceptance.

### Key observations

1. **Plaquette rises monotonically** from ⟨P⟩ = 0.329 at β = 4.44 to
   ⟨P⟩ = 0.588 at β = 6.13 — consistent with asymptotic freedom.

2. **No sharp jump** — the plaquette transition is smooth, confirming
   the crossover behavior expected for dynamical fermions (contrast with
   the quenched first-order transition).

3. **Acceptance improves at weak coupling** — from ~50% in the confined
   region to ~80% at β > 5.69, reflecting the better-conditioned Dirac
   operator at weak coupling.

4. **CG iterations decrease at weak coupling** — from ~55,000 at β ≈ 4.5
   to ~46,000 at β ≈ 6.1. The Dirac operator condition number improves as
   gauge fluctuations decrease, exactly as predicted by the Anderson
   localization analogy (less disorder → fewer localized modes → faster
   CG convergence).

5. **β_c has shifted** — the quenched critical coupling was 5.692. The
   dynamical plaquette shows the steepest gradient around β ≈ 5.0–5.5,
   consistent with the expected downward shift from fermion backreaction.

---

## 3. NPU Adaptive Steering: What It Means

### The problem it solves

A traditional lattice QCD scan is a uniform grid: pick 10–15 β values
evenly spaced, run 200 trajectories at each, wait for the answer. This
wastes most of the compute budget in boring regions where nothing
interesting happens (deep confined, deep deconfined) while under-sampling
the transition region where the physics changes rapidly.

### What the NPU does

The BrainChip AKD1000 runs an Echo State Network (ESN) — a recurrent
neural network where the internal "reservoir" of neurons has fixed random
connections, and only the output layer is trained. This is the same
reservoir computing principle from your Applied ML course, now running on
dedicated neuromorphic silicon.

The ESN observes each trajectory's results (plaquette, acceptance,
|ΔH|, CG iterations) and produces 14 simultaneous predictions through
separate readout heads. The inference takes 341 µs and costs ~30 mW —
essentially free compared to the 40-second, 370-watt GPU trajectory it
informs.

### The 14 NPU heads

| Head | Name | When | What it predicts |
|------|------|------|-----------------|
| 1 | β Priority | Before scan | Which β point to measure next |
| 2 | Parameter Suggestion | Before trajectory | Optimal dt and n_md |
| 3 | CG Estimate | Before trajectory | Expected CG iterations |
| 4 | Quenched Length | Before dynamical | How many pre-thermalization steps needed |
| 5 | Quench Therm Detector | During quenched phase | Has the quenched pre-phase converged? |
| 6 | Dynamical Therm Detector | During dynamical | Has the Markov chain thermalized? |
| 7 | Rejection Predictor | During trajectory | Will this trajectory be accepted? |
| 8 | Phase Classifier | After trajectory | Confined / transition / deconfined |
| 9 | Quality Score | After trajectory | Is the measurement statistically useful? |
| 10 | Anomaly Detector | After trajectory | Flag unusual trajectories |
| 11 | Adaptive Steering | After batch | Insert new β points in under-sampled gaps |
| 12 | RMT Spectral | Before trajectory | Predicted smallest eigenvalue (λ_min) |
| 13 | Potts Phase | Before trajectory | Phase transition prediction from Z(3) proxy |
| 14 | Anderson CG | Before trajectory | CG cost prediction from disorder proxy |

Heads 1–11 were active in the quenched runs and are now running for
dynamical. Heads 12–14 are new — trained from the physics proxy pipeline
described in Section 5.

### What "adaptive steering" means, concretely

In the quenched Run 2, the NPU steered 7 of 10 β points adaptively.
Instead of a uniform grid, it concentrated measurements in the
transition region (β ≈ 5.4–5.8) where the susceptibility peak lives. The
result: 2.5× more statistics in the interesting region at the same total
wall time.

For the dynamical run, the NPU steered the full 15-point scan. The
first 3 points were seeded (β = 5.0, 5.5, 5.69). After seeing the
plaquette and acceptance data from those seeds, the NPU recommended the
next β point to fill the largest gap in the physics. It continued
inserting points — including pulling the scan down to β ≈ 4.44 where it
detected the transition onset was earlier than expected for dynamical
fermions.

The steering cycle per β point:

```
GPU finishes 65 trajectories at β_i
    ↓ (plaquette, acceptance, CG data → NPU)
NPU Head 1 scores all candidate β values     [341 µs]
NPU Head 11 identifies the largest physics gap [341 µs]
NPU Head 2 suggests dt and n_md for β_{i+1}   [341 µs]
NPU Head 3 predicts CG iterations at β_{i+1}  [341 µs]
    ↓
GPU starts trajectories at β_{i+1}
```

Total NPU overhead per scan point: ~1.4 ms. Total GPU time per scan
point: ~43 minutes. The NPU is making real-time decisions that determine
where the GPU spends its next 43 minutes of compute, at a cost ratio of
1.4 ms / 2,600,000 ms = 0.00005%.

---

## 4. Evolution Timeline: What Scaled Down and Why

| Date | Event | Lattice | Key finding |
|------|-------|---------|-------------|
| Feb 18 | Quenched Run 1 (native f64) | 32⁴ | β_c = 5.69, matches literature |
| Feb 20 | Quenched Run 2 (DF64 + NPU) | 32⁴ | 2.5× more stats, 63% therm saved |
| Feb 24 | Dynamical HMC first attempt | 32⁴ | CG too slow, |ΔH| diverging |
| Feb 25 | Fermion force fix | 8⁴ | Momentum kick sign error found and fixed |
| Feb 25 | Dynamical validation | 8⁴ | First successful dynamical trajectories |
| Feb 26 | dt/n_md parameter sweep (Exp 024) | 8⁴ | Mapped stability region for Omelyan |
| Feb 27 | 8⁴ production run launched | 8⁴ | 15 β points, NPU-steered, overnight |
| Feb 28 | Production run complete | 8⁴ | 966 trajectories, 10.6 hours, 60% acc |
| Feb 28 | Physics proxy pipeline (Exp 025) | — | Anderson + Potts training data generated |
| **Next** | **16⁴ validation** | **16⁴** | **Scale test before full production** |
| **Next** | **32⁴ dynamical production** | **32⁴** | **Full-volume dynamical QCD** |

The scale-down from 32⁴ to 8⁴ was driven by the CG solver cost. In
quenched QCD, there is no CG solver — the molecular dynamics force comes
only from the gauge field, which is a local computation. Adding dynamical
fermions introduces a global linear solve at every MD step. The CG cost
scales as O(V × κ), where V is the lattice volume and κ is the condition
number of the Dirac operator.

At 32⁴ (V = 1,048,576), the CG solver would dominate the trajectory
by a factor of ~256× compared to 8⁴ (V = 4,096). The strategy is to
validate physics and NPU steering at small volume, then scale up with
measured parameters rather than guessing.

---

## 5. Future: Multi-Physics Proxy Pipeline

### The problem

The CG solver is the bottleneck of dynamical QCD. The number of CG
iterations depends on the condition number of the Dirac operator, which
depends on the gauge field configuration, which depends on β and the
simulation history. We want to predict CG difficulty before committing
GPU cycles to a trajectory.

### The insight

The QCD Dirac operator has the same mathematical structure as the
Anderson Hamiltonian from condensed matter physics:

| | Anderson Hamiltonian | QCD Dirac Operator |
|--|---------------------|-------------------|
| **Matrix structure** | Hopping + random on-site energy | Hopping + gauge link matrices |
| **Disorder** | Random potential (W) | Gauge field fluctuations |
| **Localization** | Electron wavefunctions localize | Quark modes localize |
| **Critical behavior** | Metal-insulator transition at W_c | Deconfinement transition at β_c |
| **Spectral diagnostic** | Level spacing ratio ⟨r⟩ | Same — maps directly |
| **Solver impact** | Condition number → CG difficulty | Same relationship |

This connection is well-established theoretically (Kovács & Pittler 2010,
Giordano et al. 2013–2026). What is new here is using it computationally:
**run the Anderson model first as a cheap proxy, predict CG difficulty,
and feed the prediction to the NPU before the GPU starts.**

The Anderson Hamiltonian is dramatically cheaper to solve because it has
no gauge structure (scalar hopping vs. SU(3) matrix hopping) and no spin
degrees of freedom. A full eigendecomposition of the 8³ Anderson model
takes ~200 ms on CPU. The equivalent QCD Dirac problem takes minutes.

### Similarly: Z(3) Potts model for phase prediction

The deconfinement phase transition in SU(3) gauge theory belongs to the
same universality class as the Z(3) Potts model (Svetitsky & Yaffe 1982).
A Potts Monte Carlo simulation at the corresponding coupling predicts
whether a given β value is in the confined phase, near the transition, or
deconfined — at a cost of milliseconds.

### What we built (Experiment 025)

A proxy pipeline (`barracuda/src/bin/gpu_physics_proxy.rs`) that runs:

1. **Anderson 3D** — 7 disorder strengths × 3 seeds × 3 lattice sizes
   = 63 eigendecompositions → level spacing ratio, smallest eigenvalue,
   bandwidth, localization diagnostics
2. **Z(3) Potts MC** — 12 β values × 3 lattice sizes = 36 Monte Carlo
   runs → magnetization, susceptibility, energy, phase classification

**Results:** 171 training data points generated in 67 seconds on CPU.
This data trains NPU Heads 12–14 (RMT Spectral, Potts Phase, Anderson
CG). The predictions from these heads will be available before each GPU
trajectory begins, at zero additional GPU cost.

### The multi-fidelity stack

```
Layer 0 (free):    NPU inference — 14 predictions in 341 µs, 30 mW
Layer 1 (cheap):   Anderson 3D + Potts MC — seconds on CPU
Layer 2 (moderate): Quenched HMC pre-thermalization — minutes on GPU
Layer 3 (expensive): Full dynamical HMC with CG solver — minutes/trajectory on GPU
```

Each layer informs the one above it. The NPU sits at the bottom,
synthesizing information from all layers into real-time steering
decisions. The cheaper layers (Anderson, Potts) run on the CPU or Titan V
while the expensive layer (dynamical HMC) runs on the RTX 3090. No
hardware sits idle; no layer duplicates work.

---

## 6. Hardware Utilization and Scaling Plan

### Current state (8⁴ on 3090)

| Resource | Used | Available | Utilization |
|----------|------|-----------|-------------|
| VRAM | 13.7 MB | 24 GB | 0.06% |
| SM cores | 16 workgroups | 82 SMs | ~20% |
| Titan V | Idle | 12 GB HBM2 | 0% |

### Scaling roadmap

| Lattice | VRAM (est.) | CG/traj | Wall/traj | GPU util |
|---------|-------------|---------|-----------|----------|
| 8⁴ | 14 MB | 55,000 | 40 s | 20% |
| 16⁴ | 220 MB | ~114,000 | 2–5 min | ~50% |
| 32⁴ | 3.5 GB | ~228,000 | 8–15 min | ~80% |
| 48⁴ | 18 GB | ~400,000 | 30–60 min | ~95% |

The RTX 3090 has 24 GB VRAM and 936 GB/s memory bandwidth. We are
currently using less than 1% of both. Scaling to 32⁴ brings utilization
to production levels; 48⁴ would saturate the card.

The Titan V (12 GB HBM2, 653 GB/s) can run independent 8⁴ or 16⁴
chains simultaneously, doubling β-point throughput. The physics proxy
pipeline (Anderson + Potts) runs on CPU, keeping both GPUs free for HMC.

---

## 7. Comparison: Quenched → Dynamical at a Glance

### For context: what got harder, what got smarter

| Aspect | Quenched (32⁴) | Dynamical (8⁴) | At scale (32⁴ dynamical) |
|--------|:--------------:|:--------------:|:------------------------:|
| Trajectories | 6,640 | 966 | Target: ~1,000 |
| Wall time | 14.2 h | 10.6 h | Est: 100–250 h |
| Cost per trajectory | 7.6 s | 40 s | 8–15 min |
| CG iterations | 0 | 55,000 | ~228,000 |
| NPU heads | 6 | 14 | 14 |
| NPU overhead | 0.016% | 0.001% | <0.001% |
| Adaptive steering | Yes (7/10 β steered) | Yes (12/15 β steered) | Yes |
| Physics proxies | None | Anderson + Potts (171 data points) | Full pipeline |
| Phase transition | First-order (sharp) | Crossover (smooth) | Crossover |
| β_c | 5.692 (literature match) | ~5.0–5.5 (shifted lower) | To be measured |

---

## 8. What This Means for the Coffee

The previous data sheet showed we could reproduce known quenched QCD
results on consumer hardware at $0.60/run, with NPU adaptive steering
providing 2.5× more useful statistics at the same cost.

This update shows we are now running full dynamical QCD — the real thing,
with quarks — on the same hardware. The CG solver is the new bottleneck,
and we have built a multi-physics proxy system (Anderson localization +
Potts model) that predicts CG difficulty before each trajectory,
expanding the NPU from 6 heads to 14. The proxies run on CPU at zero GPU
cost, generating 171 training points in 67 seconds.

The scaling path from 8⁴ to 32⁴ is clear and data-driven: each step
uses measured parameters from the previous step to predict the next.
The 32⁴ dynamical production run is estimated at 100–250 GPU-hours on
the RTX 3090, costing approximately $5–12 in electricity.

For reference, this same calculation on QCDSP in 1998 would have
required a $3.5M purpose-built machine. The physics is identical.

---

*Full data, code, experiment journals, and all 25 experiment documents
available at [github.com/syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring).*
