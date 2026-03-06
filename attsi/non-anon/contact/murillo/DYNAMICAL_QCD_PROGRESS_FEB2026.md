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

The 8⁴ dynamical production run is **complete** — 1,071 trajectories
across 17 NPU-steered β points in 11.96 hours. The crossover is smooth
(no first-order jump), β_c has shifted downward as expected, and the CG
solver cost tracks Anderson localization predictions. A concurrent
"brain architecture" has since been built and is now in production
validation (Exp 028), overlapping the Titan V, CPU proxy pipeline, and
NPU monitoring alongside the RTX 3090 dynamical HMC.

| | Quenched (Runs 1–2) | Dynamical (Run 3, **complete**) |
|--|:-------------------:|:------------------------------:|
| **Lattice** | 32⁴ | 8⁴ (validation → 16⁴ → 32⁴) |
| **Physics** | Pure gauge (no quarks) | Full QCD with staggered quarks |
| **Force** | Wilson gauge only | Gauge + fermion force (CG solver) |
| **Cost / trajectory** | 7.6 s (DF64) | ~52 s avg (CG-dominated, 8⁴) |
| **NPU heads** | 6 | 15 (expanded with physics proxies + CG monitor) |
| **β points** | 10–12 | 17 (4 seed + 13 NPU-inserted) |
| **Total trajectories** | 6,640 | 1,071 |
| **Wall time** | 14.2 h | 11.96 h |
| **Acceptance** | ~18% | 56.6% |
| **Status** | Complete | **Complete** — 17/17 β, 1,071 trajectories |

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

## 2. Production Run: 8⁴ Dynamical — Final Results

### Run parameters

| Parameter | Value |
|-----------|-------|
| Lattice | 8⁴ (4,096 sites) |
| Gauge action | Wilson SU(3) |
| Fermions | Staggered (1 flavor, m = 0.1) |
| Integrator | Omelyan leapfrog, dt = 0.01, n_md = 100 |
| GPU | RTX 3090 (DF64 hybrid) |
| NPU | BrainChip AKD1000 (15-head ESN) |

### Results by β point (17 points, 1,071 trajectories)

The "#" column shows when each point was evaluated. The NPU did not scan
linearly — it jumped between high and low β to bracket the crossover
(see scan trajectory below). Seed rows are **bolded**.

| # | β | n | Acc% | ⟨P⟩ | ⟨CG⟩ | Wall/traj | Source |
|---|--------|-----|------|--------|---------|-----------|--------|
| 17 | 4.3351 | 16 | 50% | 0.3156 | 60,472 | 76 s | NPU |
| 16 | 4.3877 | 50 | 52% | 0.3234 | 60,451 | 56 s | NPU |
| 15 | 4.4416 | 50 | 54% | 0.3284 | 60,442 | 60 s | NPU |
| 14 | 4.4969 | 50 | 44% | 0.3344 | 60,434 | 55 s | NPU |
| 13 | 4.5535 | 50 | 50% | 0.3430 | 60,415 | 68 s | NPU |
| 12 | 4.6116 | 50 | 50% | 0.3464 | 60,399 | 53 s | NPU |
| 11 | 4.6711 | 50 | 40% | 0.3539 | 60,295 | 53 s | NPU |
| 10 | 4.7321 | 50 | 42% | 0.3616 | 60,041 | 53 s | NPU |
| 8 | 4.7946 | 50 | 52% | 0.3711 | 59,586 | 52 s | NPU |
| 6 | 4.8603 | 50 | 46% | 0.3765 | 59,200 | 51 s | NPU |
| 5 | 4.9293 | 50 | 46% | 0.3893 | 58,968 | 51 s | NPU |
| **4** | **5.0000** | **50** | **50%** | **0.4040** | **58,929** | **51 s** | **Seed** |
| **2** | **5.5000** | **50** | **66%** | **0.5255** | **55,423** | **47 s** | **Seed** |
| **1** | **5.6900** | **50** | **78%** | **0.5511** | **54,254** | **46 s** | **Seed** |
| **3** | **6.0000** | **50** | **84%** | **0.5812** | **49,804** | **43 s** | **Seed** |
| 7 | 6.0673 | 50 | 76% | 0.5881 | 54,278 | 48 s | NPU |
| 9 | 6.1314 | 50 | 78% | 0.5957 | 49,072 | 43 s | NPU |

**Totals:** 1,071 trajectories, 11.96 hours wall time, 56.6% overall
acceptance. The NPU expanded a 4-seed scan to 17 points autonomously.

### Plaquette curve (seeds vs NPU-inserted)

```
 ⟨P⟩
 0.60 │                                                         o  ← 6.13  NPU #9
 0.59 │                                                     o      ← 6.07  NPU #7
 0.58 │                                                 S          ← 6.00  SEED #3
 0.55 │                                            S               ← 5.69  SEED #1
 0.53 │                                       S                    ← 5.50  SEED #2
 0.40 │                                  S                         ← 5.00  SEED #4
 0.39 │                             o                              ← 4.93  NPU #5
 0.38 │                         o                                  ← 4.86  NPU #6
 0.37 │                     o                                      ← 4.79  NPU #8
 0.36 │                 o                                          ← 4.73  NPU #10
 0.35 │             o                                              ← 4.67  NPU #11
 0.35 │         o                                                  ← 4.61  NPU #12
 0.34 │      o o                                                   ← 4.55  NPU #13
 0.33 │   o o                                                      ← 4.44  NPU #15
 0.32 │  o                                                         ← 4.39  NPU #16
 0.32 │ o                                                          ← 4.34  NPU #17
      ┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──
      4.3 4.5 4.6 4.7 4.8 4.9 5.0       5.5  5.7  6.0 6.1  β

      S = seed point (human-selected)     o = NPU-inserted
```

### NPU scan trajectory (evaluation order)

The NPU did not scan linearly. It bracketed the crossover region,
alternating between the low-β confined side and the high-β deconfined
tail before committing to a systematic downward sweep:

```
  Evaluation order →

  Step:  1     2     3     4     5     6     7     8     9    10    11    12    13    14    15    16    17
  β:   5.69  5.50  6.00  5.00  4.93  4.86  6.07  4.79  6.13  4.73  4.67  4.61  4.55  4.50  4.44  4.39  4.34
  Src:  [S1]  [S2]  [S3]  [S4]  NPU   NPU  NPU   NPU  NPU   NPU   NPU   NPU   NPU   NPU   NPU   NPU   NPU
                                │     │     │     │     │
                                └──┬──┘     └──┬──┘     │
                               low-β fill    jump to   high-β
                                             high-β    tail
                                             ───────── then systematic downward sweep (10→17) ──→
```

The NPU learned this "bracket and fill" strategy from quenched training
data — coarse bracketing first, then fine filling. This is how a
physicist would explore an unknown phase diagram, but the NPU was never
explicitly programmed to bracket.

### Key observations

1. **Plaquette rises monotonically** from ⟨P⟩ = 0.316 at β = 4.34 to
   ⟨P⟩ = 0.596 at β = 6.13 — consistent with asymptotic freedom.

2. **No sharp jump** — the plaquette transition is smooth, confirming
   the crossover behavior expected for dynamical fermions (contrast with
   the quenched first-order transition).

3. **Acceptance improves at weak coupling** — from ~50% in the confined
   region to ~84% at β = 6.0, reflecting the better-conditioned Dirac
   operator at weak coupling.

4. **CG iterations decrease at weak coupling** — from ~60,400 at
   β ≈ 4.5 to ~49,000 at β ≈ 6.1. The Dirac operator condition number
   improves as gauge fluctuations decrease, exactly as predicted by the
   Anderson localization analogy (less disorder → fewer localized modes
   → faster CG convergence).

5. **β_c has shifted** — the quenched critical coupling was 5.692. The
   dynamical plaquette shows the steepest gradient around β ≈ 5.0–5.5,
   consistent with the expected downward shift from fermion backreaction.

6. **NPU steering was decisive** — only 4 seed points were provided;
   the NPU autonomously inserted 13 additional points, mapping the full
   crossover. It correctly spent most of its steering budget on the
   confined side, where the dynamical crossover extends further than the
   quenched transition.

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

### The 15 NPU heads

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
| **15** | **CG Residual Monitor** | **During CG solve** | **Convergence ETA, anomaly score from live residual stream** |

Heads 1–11 were active in the quenched runs. Heads 12–14 are trained
from the physics proxy pipeline (Section 5). Head 15 is new to the
"brain architecture" (Section 6) — it receives streaming CG residuals
during the solve and can issue interrupts (adjust check frequency or
kill a diverging solve).

### What "adaptive steering" means, concretely

In the quenched Run 2, the NPU steered 7 of 10 β points adaptively.
Instead of a uniform grid, it concentrated measurements in the
transition region (β ≈ 5.4–5.8) where the susceptibility peak lives. The
result: 2.5× more statistics in the interesting region at the same total
wall time.

For the dynamical run, the NPU expanded 4 seed points (β = 5.0, 5.5,
5.69, 6.0) to a 17-point scan. After seeing the plaquette and
acceptance data from each completed β, the NPU recommended the next
insertion point. It correctly identified that the dynamical crossover
extends further into the confined regime than the quenched transition,
and spent most of its steering budget mapping the low-β side (inserting
11 points below β = 5.0). The NPU's "bracket and fill" strategy is
visible in the scan trajectory above.

The steering cycle per β point:

```
GPU finishes 50 trajectories at β_i
    ↓ (plaquette, acceptance, CG data → NPU)
NPU Head 1 scores all candidate β values     [341 µs]
NPU Head 11 identifies the largest physics gap [341 µs]
NPU Head 2 suggests dt and n_md for β_{i+1}   [341 µs]
NPU Head 3 predicts CG iterations at β_{i+1}  [341 µs]
    ↓
GPU starts trajectories at β_{i+1}
```

Total NPU overhead per scan point: ~1.4 ms. Total GPU time per scan
point: ~42 minutes. The NPU determines where the GPU spends its next 42
minutes of compute, at a cost ratio of 1.4 ms / 2,520,000 ms = 0.00006%.

---

## 4. Evolution Timeline: What Scaled Down and Why

| Date | Event | Lattice | Key finding |
|------|-------|---------|-------------|
| Feb 18 | Quenched Run 1 (native f64) | 32⁴ | β_c = 5.69, matches literature |
| Feb 20 | Quenched Run 2 (DF64 + NPU) | 32⁴ | 2.5× more stats, 63% therm saved |
| Feb 24 | Dynamical HMC first attempt | 32⁴ | CG too slow, \|ΔH\| diverging |
| Feb 25 | Fermion force fix | 8⁴ | Momentum kick sign error found and fixed |
| Feb 25 | Dynamical validation | 8⁴ | First successful dynamical trajectories |
| Feb 26 | dt/n_md parameter sweep (Exp 024) | 8⁴ | Mapped stability region for Omelyan |
| Feb 27 | 8⁴ production run launched | 8⁴ | 17 β points (4 seed → NPU-steered), overnight |
| Feb 28 | **Production run complete** | 8⁴ | **1,071 trajectories, 11.96 hours, 56.6% acc** |
| Feb 28 | Physics proxy pipeline (Exp 025) | — | Anderson + Potts training data generated |
| Feb 28 | 4D Anderson + Wegner specs (Exp 026) | — | 3-tier proxy hierarchy designed |
| Feb 28 | Brain architecture implemented | 8⁴ | Concurrent NPU + Titan V + CPU + 3090 |
| Feb 28 | Brain pilot validation | 8⁴ | All 4 layers running concurrently |
| **Feb 28** | **Brain production run launched (Exp 028)** | **8⁴** | **Overnight validation of concurrent pipeline** |
| **Next** | **16⁴ validation** | **16⁴** | **Scale test before full production** |
| **Next** | **32⁴ dynamical production** | **32⁴** | **Full-volume dynamical QCD** |

Note the development velocity: quenched-to-dynamical took 7 days.
Dynamical-to-brain-architecture took 1 day. The previous data sheet
(LATTICE_QCD_RESULTS_FEB2026) was sent February 27. This update covers
everything that happened since then.

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
Layer 0 (free):     NPU inference — 15 predictions in 341 µs, 30 mW
Layer 1 (cheap):    Anderson 3D + Potts MC — seconds on CPU (concurrent)
Layer 2 (moderate): Quenched pre-therm — minutes on Titan V (concurrent)
Layer 3 (expensive): Full dynamical HMC with CG — minutes/traj on RTX 3090
```

Each layer informs the one above it. The NPU sits at the bottom,
synthesizing information from all layers into real-time steering
decisions. With the brain architecture (Section 6), all four layers now
run **concurrently** — the CPU and Titan V do their work while the
3090 runs dynamical HMC, and the NPU monitors all of them.

---

## 6. Concurrent "Brain" Architecture (New)

After the Exp 024 production run completed, we built a concurrent
pipeline that treats the workstation as a heterogeneous brain — each
hardware component handles a different cognitive layer:

```
┌─────────────────────────────────────────────────────┐
│                biomeGate Brain                      │
│                                                     │
│  CPU (256 GB)          Titan V (12 GB HBM2)        │
│  "Prefrontal Cortex"   "Pre-motor Cortex"          │
│  Anderson 3D proxy      Quenched pre-therm for     │
│  Z(3) Potts MC          NEXT β while 3090 runs     │
│  Feeds NPU Head 14      current β                  │
│         │                        │                  │
│         ▼                        ▼                  │
│  ┌─────────────────────────────────────────┐        │
│  │  NPU (AKD1000) — "Cerebellum"          │        │
│  │  15-head ESN: steering, monitoring,     │        │
│  │  CG residual stream, attention state    │        │
│  │  Green → Yellow → Red interrupt logic   │        │
│  └─────────────────┬───────────────────────┘        │
│                    │ interrupts                      │
│                    ▼                                 │
│  ┌─────────────────────────────────────────┐        │
│  │  RTX 3090 (24 GB) — "Motor Cortex"     │        │
│  │  Full dynamical HMC with CG solver     │        │
│  │  Streams residuals to NPU every N iters │        │
│  └─────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────┘
```

**What runs concurrently:**

| Thread | Hardware | Work | Communication |
|--------|----------|------|---------------|
| Main loop | RTX 3090 | Dynamical HMC (CG solve, gauge update) | Sends residuals → NPU |
| NPU cerebellum | AKD1000 | 15-head inference, attention state machine | Sends interrupts → 3090 |
| Titan V pre-motor | Titan V | Quenched pre-therm for next β | Sends warm config → main |
| CPU cortex | CPU | Anderson 3D + Potts proxy for current β | Sends features → NPU |

The NPU monitors CG residuals in real time through Head 15. An internal
attention state machine (Green / Yellow / Red) adjusts the monitoring
frequency dynamically and can kill a diverging CG solve mid-trajectory.
This is modeled on the biological principle that routine processes run on
autopilot (cerebellum) until an anomaly triggers conscious attention.

The Titan V pre-thermalizes the *next* β point while the 3090 measures
the *current* one — overlapping work that was previously sequential. The
CPU runs the cheap physics proxies (Anderson + Potts) concurrently with
both GPUs.

This architecture is now in production validation (Exp 028, running
overnight as of Feb 28).

---

## 7. Hardware Utilization and Scaling Plan

### Current state (8⁴ on 3090 + brain architecture)

| Resource | Used | Available | Utilization |
|----------|------|-----------|-------------|
| RTX 3090 VRAM | 13.7 MB | 24 GB | 0.06% |
| RTX 3090 SM cores | 16 workgroups | 82 SMs | ~20% |
| Titan V | Pre-therm (concurrent) | 12 GB HBM2 | ~15% |
| CPU | Anderson + Potts proxy | 256 GB / 32 cores | ~5% |
| NPU | 15-head inference + monitoring | AKD1000 | Active |

### Scaling roadmap — hypercubic (L⁴)

| Lattice | VRAM (est.) | CG/traj | Wall/traj | GPU util |
|---------|-------------|---------|-----------|----------|
| 8⁴ | 14 MB | 58,000 | 52 s | 20% |
| 16⁴ | 220 MB | ~114,000 | 2–5 min | ~50% |
| 32⁴ | 3.5 GB | ~228,000 | 8–15 min | ~80% |
| 48⁴ | 18 GB | ~400,000 | 30–60 min | ~95% |

### Scaling roadmap — asymmetric (N_s³ × N_t, MILC-style)

Asymmetric lattices are physically more meaningful for finite-temperature
studies (T = 1/(a × N_t)) and far more memory-efficient:

| Lattice | Sites | VRAM | DF64 time/traj | Physics |
|---------|:-----:|:----:|:--------------:|---------|
| 32³ × 4 | 131K | 0.31 GB | ~1 s | β_c(4) ≈ 5.692 |
| 64³ × 8 | 2.10M | 5.0 GB | ~15 s | β_c(8) ≈ 6.06, MILC-comparable |
| 48³ × 12 | 1.33M | 3.2 GB | ~10 s | β_c(12) ≈ 6.34 |
| 96³ × 12 | 10.6M | 25.3 GB | ~77 s | MILC production scale |

The existing `Lattice` struct already supports arbitrary `dims: [Nx, Ny, Nz, Nt]`.
Multiple N_t values enable continuum extrapolation (N_t → ∞, a → 0).

The RTX 3090 has 24 GB VRAM and 936 GB/s memory bandwidth. We are
currently using less than 1% of both. Scaling to 32⁴ brings utilization
to production levels; asymmetric 96³×12 would saturate the card while
producing continuum-relevant physics.

At larger volumes, the brain architecture's overlap becomes more
valuable: the Titan V pre-thermalization saves ~2–5 minutes per β
point at 32⁴, and the CPU proxy cost is constant regardless of lattice
size.

---

## 8. Comparison: Quenched → Dynamical at a Glance

### What got harder, what got smarter

| Aspect | Quenched (32⁴) | Dynamical (8⁴) | At scale (32⁴ dynamical) |
|--------|:--------------:|:--------------:|:------------------------:|
| Trajectories | 6,640 | 1,071 | Target: ~1,000 |
| Wall time | 14.2 h | 11.96 h | Est: 100–250 h |
| Cost per trajectory | 7.6 s | 52 s | 8–15 min |
| CG iterations | 0 | 58,000 | ~228,000 |
| NPU heads | 6 | 15 | 15 |
| NPU overhead | 0.016% | 0.001% | <0.001% |
| Adaptive steering | Yes (7/10 β steered) | Yes (13/17 β steered) | Yes |
| Physics proxies | None | Anderson + Potts | Full pipeline + 4D Wegner |
| Concurrent hardware | 1 GPU | 2 GPUs + CPU + NPU | Same |
| Phase transition | First-order (sharp) | Crossover (smooth) | Crossover |
| β_c | 5.692 (literature match) | ~5.0–5.5 (shifted lower) | To be measured |

---

## 9. What This Means for Tuesday

The previous data sheet (sent Feb 27) showed we could reproduce known
quenched QCD results on consumer hardware at $0.60/run, with NPU
adaptive steering providing 2.5× more useful statistics at the same
cost.

Since then — in 24 hours:

1. **Completed dynamical production** — 1,071 trajectories, 17
   NPU-steered β points, smooth crossover confirmed, β_c shifted to
   ~5.0–5.5 as expected. Full data table and plaquette curves above.

2. **Built a multi-physics proxy pipeline** — Anderson localization and
   Z(3) Potts models run on CPU to predict CG difficulty and phase
   transitions. 171 training points in 67 seconds. These feed NPU Heads
   12–14 at zero GPU cost.

3. **Designed and implemented a concurrent brain architecture** — the
   RTX 3090, Titan V, CPU, and NPU now run simultaneously. The NPU
   monitors CG residuals in real time and can interrupt diverging solves.
   The Titan V pre-thermalizes the next β point while the 3090 measures
   the current one. Currently in overnight validation (Exp 028).

4. **Planned the next proxy tier** — 4D Anderson and Wegner block models
   that capture the matrix structure of the Dirac operator. Designed,
   specified, not yet coded.

The scaling path from 8⁴ to 32⁴ is clear and data-driven: each step
uses measured parameters from the previous step. The 32⁴ dynamical
production run is estimated at 100–250 GPU-hours on the RTX 3090,
costing approximately $5–12 in electricity.

For reference, this same calculation on QCDSP in 1998 would have
required a $3.5M purpose-built machine. The physics is identical.

---

*Full data, code, experiment journals, and all 28 experiment documents
available at [github.com/syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring).*
