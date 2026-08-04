# GPU Scaling Hypothesis — Maximum Lattice Sizes Per Card Per Rung

**Status**: HYPOTHESIS (validated at Rung 1, projected for Rungs 2-5)
**Wave**: 155q | **Date**: Aug 3, 2026
**Gate**: strandGate (RTX 3090 24GB + RX 6950 XT 16GB)

---

## Thesis

Every rung of the lattice QCD program fits comfortably in consumer GPU VRAM
at production-relevant lattice sizes (16⁴ to 32⁴). Memory is not the
bottleneck — CG iteration count and wall-clock time are the practical limits.
The same WGSL shaders scale from Rung 1 through Rung 5 without architectural
changes.

---

## Per-Site Memory Costs

### Rung 1: SU(3) Pure Gauge (VALIDATED)

| Buffer | Contents | Bytes/site |
|--------|----------|-----------|
| Link field U | 4 dirs × 18 reals (3×3 complex) | 576 |
| Backup links | Metropolis reject rollback | 576 |
| Momenta P | su(3) algebra, same layout | 576 |
| Force F | gauge force accumulator | 576 |
| Plaquette output | 1 double per site | 8 |
| KE output | 4 doubles (per link) | 32 |
| Neighbors | 8 × u32 (±μ for μ=0..3) | 32 |
| **Total** | | **2,376** |

### Rung 2: Quenched QCD (Dirac on Fixed Backgrounds)

Adds staggered fermion fields and CG workspace to Rung 1 buffers.

| Buffer | Contents | Bytes/site |
|--------|----------|-----------|
| Gauge (Rung 1) | all gauge buffers | 2,376 |
| Fermion ψ | 3 complex = 6 doubles | 48 |
| Result D·ψ | 3 complex | 48 |
| CG vectors (r, p, Ap, x) | 4 × 48 | 192 |
| **Total** | | **2,664** |

### Rung 3: Dynamical Nf=2 RHMC (Full QCD)

Multi-shift CG requires one solution vector per pole of the rational
approximation. Standard: 8 poles for det(D†D)^{1/4}.

| Buffer | Contents | Bytes/site |
|--------|----------|-----------|
| Gauge (Rung 1) | all gauge buffers | 2,376 |
| Pseudofermion φ | source field | 48 |
| Multi-shift vectors | 8 poles × 48 | 384 |
| CG workspace | r, p, Ap, scalars | 192 |
| **Total (no Hasenbusch)** | | **3,000** |
| **Total (2-level Hasenbusch)** | +φ₂ + CG₂ | **3,500** |

Hasenbusch mass preconditioning splits the fermion determinant into
heavy and light parts, reducing CG iterations by 2-3× at the cost of
one extra pseudofermion field + CG workspace.

### Rung 4: Nf=2+1 (Light u,d + Strange s)

Two independent fermion sectors, each with its own rational approximation:

| Buffer | Contents | Bytes/site |
|--------|----------|-----------|
| Gauge (Rung 1) | all gauge buffers | 2,376 |
| Light sector | φ + 8 poles × 48 + CG | 624 |
| Strange sector | φ + 8 poles × 48 + CG | 624 |
| **Total** | | **3,624** |

With Hasenbusch on the light sector: ~4,100 bytes/site.

### Rung 5: Finite Temperature (Ns³ × Nt)

Same per-site cost as the relevant flavor content. The key advantage is
asymmetric geometry: Nt ≪ Ns enables much larger spatial volumes at fixed
total site count.

Example: 32³ × 8 = 262,144 sites vs 16⁴ = 65,536 sites.
At Nf=2+1 cost: 32³×8 uses 262,144 × 3,624 ≈ 950 MB.

---

## Maximum Lattice Sizes Per Card

### RTX 3090 (24 GB, usable ~22 GB after driver/OS)

| Rung | Physics | Max L⁴ | Sites | VRAM Used | Feasible |
|------|---------|--------|-------|-----------|----------|
| 1 | SU(3) pure gauge | **48⁴** | 5,308,416 | 12.6 GB | YES |
| 1 | (absolute max) | 56⁴ | 9,834,496 | 23.4 GB | TIGHT |
| 2 | Quenched Dirac | **44⁴** | 3,748,096 | 10.0 GB | YES |
| 3 | Nf=2 RHMC | **40⁴** | 2,560,000 | 7.7 GB | YES |
| 3 | (with Hasenbusch) | **38⁴** | 2,085,136 | 7.3 GB | YES |
| 4 | Nf=2+1 | **36⁴** | 1,679,616 | 6.1 GB | YES |
| 5 | Finite-T Nf=2+1 | **48³×12** | 1,327,104 | 4.8 GB | YES |
| 5 | (stretch) | **64³×8** | 2,097,152 | 7.6 GB | YES |

### RX 6950 XT (16 GB, usable ~14 GB)

| Rung | Physics | Max L⁴ | Sites | VRAM Used | Feasible |
|------|---------|--------|-------|-----------|----------|
| 1 | SU(3) pure gauge | **40⁴** | 2,560,000 | 6.1 GB | YES |
| 1 | (absolute max) | 48⁴ | 5,308,416 | 12.6 GB | YES |
| 2 | Quenched Dirac | **40⁴** | 2,560,000 | 6.8 GB | YES |
| 3 | Nf=2 RHMC | **36⁴** | 1,679,616 | 5.0 GB | YES |
| 3 | (with Hasenbusch) | **32⁴** | 1,048,576 | 3.7 GB | YES |
| 4 | Nf=2+1 | **32⁴** | 1,048,576 | 3.8 GB | YES |
| 5 | Finite-T Nf=2+1 | **40³×10** | 640,000 | 2.3 GB | YES |
| 5 | (stretch) | **48³×8** | 884,736 | 3.2 GB | YES |

### Key Insight

Even at the most memory-hungry rung (Nf=2+1 with Hasenbusch), both cards
can run **32⁴** lattices — a size where meaningful continuum extrapolations
begin and published comparison data is abundant.

---

## Wall Time Estimates

Based on measured throughput at 8⁴ on RX 6950 XT (15.6 ms/traj for pure gauge)
and assuming linear volume scaling for force computation:

### Pure Gauge (Rung 1)

| Lattice | Volume | ms/traj (est.) | 1000 traj | 5000 traj |
|---------|--------|----------------|-----------|-----------|
| 8⁴ | 4,096 | 15.6 (measured) | 16 s | 78 s |
| 12⁴ | 20,736 | ~80 | 80 s | 6.5 min |
| 16⁴ | 65,536 | ~250 | 4.2 min | 21 min |
| 24⁴ | 331,776 | ~1,300 | 22 min | 1.8 hr |
| 32⁴ | 1,048,576 | ~4,000 | 67 min | 5.6 hr |
| 40⁴ | 2,560,000 | ~10,000 | 2.8 hr | 14 hr |
| 48⁴ | 5,308,416 | ~20,000 | 5.6 hr | 28 hr |

### Nf=2 RHMC (Rung 3)

CG-dominated. Each trajectory requires O(100-500) CG iterations (mass-dependent),
each iteration applying the Dirac operator twice (D and D†). The multi-shift CG
solves all 8 poles simultaneously, so overhead is ~5-6× pure gauge (without
Hasenbusch) or ~3-4× (with Hasenbusch).

| Lattice | Volume | ms/traj (no Has.) | ms/traj (Has.) | 1000 traj (Has.) |
|---------|--------|-------------------|----------------|------------------|
| 12⁴ | 20,736 | ~450 | ~280 | 4.7 min |
| 16⁴ | 65,536 | ~1,400 | ~900 | 15 min |
| 24⁴ | 331,776 | ~7,500 | ~4,500 | 75 min |
| 32⁴ | 1,048,576 | ~23,000 | ~14,000 | 3.9 hr |

### Nf=2+1 (Rung 4)

Two sectors: ~1.5× the cost of Nf=2 (strange quark is heavier → fewer CG
iterations, roughly half the cost of the light sector).

| Lattice | ms/traj (est.) | 1000 traj |
|---------|----------------|-----------|
| 16⁴ | ~1,400 | 23 min |
| 24⁴ | ~7,000 | 1.9 hr |
| 32⁴ | ~21,000 | 5.8 hr |

### Finite Temperature (Rung 5)

Asymmetric lattices are cheaper per trajectory (smaller total volume):

| Geometry | Volume | ms/traj (Nf=2+1 est.) | 1000 traj |
|----------|--------|------------------------|-----------|
| 16³×8 | 32,768 | ~700 | 12 min |
| 24³×8 | 110,592 | ~2,400 | 40 min |
| 32³×8 | 262,144 | ~5,600 | 93 min |
| 32³×12 | 393,216 | ~8,400 | 2.3 hr |
| 48³×12 | 1,327,104 | ~28,000 | 7.8 hr |

---

## Production Campaign Plan

### Rung 1 (This Paper) — IN PROGRESS

| Volume | β range | Trajectories | Status |
|--------|---------|-------------|--------|
| 4⁴, 8⁴ | 2.0–6.5 | 100-500 | **DONE** (CPU+GPU validated) |
| 12⁴ | 5.7–6.2 | 1000 | **IN PROGRESS** (GPU, overnight) |
| 16⁴ | 5.9–6.2 | 2000 | **IN PROGRESS** (GPU, overnight) |
| 24⁴ | 6.0 | 1000 | **IN PROGRESS** (GPU, overnight) |
| 32⁴ | 6.0 | 1000 | NEXT (GPU-only, ~7 hr) |

### Rung 2 (Next Paper) — Validate Dirac

| Task | Volume | Published Comparison | Estimated Time |
|------|--------|---------------------|----------------|
| Pion correlator (quenched) | 16⁴ | Bali 2000, MILC | ~30 min |
| Meson spectrum (quenched) | 24⁴ | CP-PACS 2001 | ~2 hr |
| Polyakov loop susceptibility | 16³×8 | Karsch 1994 | ~15 min |

### Rung 3 (Third Paper) — Dynamical Fermions

| Task | Volume | Published Comparison | Estimated Time |
|------|--------|---------------------|----------------|
| Nf=2 plaquette vs β | 16⁴ | MILC, HotQCD | ~25 min/point |
| Nf=2 pion mass vs am | 16⁴ | MILC | ~25 min/point |
| Deconfinement Tc (Nf=2) | 16³×8 | Karsch, Laermann | ~12 min/point |

### Rung 4 — Physical QCD

| Task | Volume | Published Comparison | Estimated Time |
|------|--------|---------------------|----------------|
| Nf=2+1 EOS | 24³×8 | HotQCD, Wuppertal-Budapest | ~40 min/point |
| Light hadron spectrum | 24⁴ | BMW, MILC | ~2 hr/mass |
| Scale setting (w₀) | 24⁴ | BMW 2014 | ~2 hr |

### Rung 5 — Finite Temperature

| Task | Volume | Published Comparison | Estimated Time |
|------|--------|---------------------|----------------|
| Tc/√σ | 32³×8,10,12 | Bazavov 2012 | ~6 hr total |
| Pressure p(T)/T⁴ | 32³×8..16 | HotQCD 2014 | ~12 hr total |
| Chiral condensate vs T | 24³×6,8,10 | Ding 2019 | ~4 hr total |

---

## Existing Infrastructure

All 5 rungs have working code paths in `hotSpring/barracuda/src/lattice/`:

| Rung | Component | Files | CPU | GPU WGSL |
|------|-----------|-------|-----|----------|
| 1 | Wilson action + force | `wilson.rs` | VALIDATED | VALIDATED |
| 1 | HMC (Omelyan 2MN) | `hmc.rs` | VALIDATED | VALIDATED |
| 1 | Plaquette measurement | `wilson.rs` | VALIDATED | VALIDATED |
| 2 | Staggered Dirac | `dirac.rs` | Implemented | `dirac_staggered_f64.wgsl` |
| 2 | D†D squared operator | `dirac.rs` | Implemented | Implemented |
| 2 | CG solver | `cg.rs` | Implemented | `gpu_hmc/resident_cg*.rs` |
| 3 | Pseudofermion action | `pseudofermion/action.rs` | Implemented | Implemented |
| 3 | Pseudofermion force | `pseudofermion/dynamics.rs` | Implemented | `pseudofermion_force_f64.wgsl` |
| 3 | RHMC rational approx | `rhmc/mod.rs` | Implemented | — |
| 3 | Multi-shift CG | `rhmc/multishift_cg.rs` | Implemented | `gpu_hmc/true_multishift_cg/` |
| 3 | Hasenbusch splitting | `pseudofermion/hasenbusch.rs` | Implemented | `gpu_hmc/hasenbusch.rs` |
| 4 | Nf=2+1 config | `rhmc/mod.rs` (`nf2p1()`) | Implemented | Implemented |
| 4 | Nf=1,2,3,4 configs | `rhmc/mod.rs` | Implemented | Implemented |
| 5 | Asymmetric lattice | `wilson.rs` (arbitrary dims) | Ready | Ready |
| 5 | Polyakov loop | `wilson.rs` | Implemented | Implemented |

**The path from Rung 1 → Rung 5 is implemented. What remains is validation
(running, measuring, comparing to published data) — not implementation.**

---

## SU(2) Gauge Theory (Condensed Matter / Electroweak)

SU(2) links are 2×2 complex (8 reals vs 18 for SU(3)), cutting gauge memory
by 2.25×. Momenta are 3 Pauli generators (vs 8 Gell-Mann for SU(3)).

| Rung | SU(2) bytes/site | Max on RTX 3090 | Max on RX 6950 XT |
|------|-----------------|----------------|-------------------|
| 1 | ~1,056 | **64⁴** (16.8M, 17.7 GB) | **56⁴** (9.8M, 10.4 GB) |
| 3 (Nf=2) | ~1,500 | **56⁴** (9.8M, 14.7 GB) | **48⁴** (5.3M, 8.0 GB) |

SU(2) is relevant for:
- Electroweak sector simulations
- Condensed matter (lattice gauge theory in 2+1D)
- Methodological validation (cheaper, faster iteration)
- Some BSM (beyond Standard Model) scenarios

---

## Convergence Targets (What "Functional" Means)

For each rung, the minimum lattice size where results are physically meaningful:

| Rung | Minimum L/a | Why | Our Target |
|------|-------------|-----|------------|
| 1 | 12 | Finite-volume effects < 2% for β > 5.7 | 12–32 |
| 2 | 16 | Pion correlator needs L > 2/m_π | 16–24 |
| 3 | 16 | m_π L > 4 for chiral extrapolation | 16–24 |
| 4 | 20 | Light quark mass needs larger volume | 24–32 |
| 5 | Ns/Nt > 3 | Spatial/temporal aspect ratio | 32³×8 to 48³×12 |

All targets are comfortably within the VRAM budget of both cards.

---

## Summary

> **Both consumer GPUs on strandGate can run publication-relevant lattice QCD
> at all 5 rungs without memory constraints.** The practical limit is wall-clock
> time (hours to days for large volumes with dynamical fermions), not VRAM.
> The entire Rung 1→5 code path is implemented; each rung requires validation
> against published data, not new implementation.

The silicon deism thesis extends cleanly: the same WGSL shaders that produce
correct SU(3) pure gauge physics on both NVIDIA and AMD at Rung 1 will compute
Dirac operators, pseudofermion forces, and RHMC trajectories at Rungs 2-5
without modification. The math is the same; only the problem size changes.

---

*subGen Wave 155q — GPU Scaling Hypothesis. Memory budget analysis for Rungs 1-5.
Both cards fit 32⁴ Nf=2+1 (Rung 4) comfortably. All infrastructure implemented.
Validation campaigns estimated: Rung 2 (~hours), Rung 3 (~days), Rung 4 (~days),
Rung 5 (~days). Path to publication at each rung is clear.*
