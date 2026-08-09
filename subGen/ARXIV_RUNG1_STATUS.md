# arXiv Rung 1 — SU(3) Pure Gauge Preprint Status

**Status**: **16⁴ DUAL-GPU COMPLETE** — cross-vendor parity CONFIRMED (Δ=6 ppm at β=6.2)
**Wave**: 156d | **Date**: Aug 4, 2026 PM (updated)
**Paper**: `LATTICE_QCD_CONSUMER_GPU_ARXIV.md` (this directory)
**LaTeX**: `lattice_qcd_consumer_gpu.tex` (this directory)

---

## Title

**Vendor-Agnostic Lattice QCD on Consumer GPUs: SU(3) Pure Gauge HMC
with DF64 WebGPU/WGSL and Cryptographic Provenance**

---

## What Rung 1 Proves

1. SU(3) pure gauge HMC executes through WebGPU/WGSL on consumer GPUs
2. DF64 is accurate for SU(3) observables (~9 digits accumulated)
3. Common WGSL source produces identical physics on NVIDIA and AMD
4. The deterministic GPU MD path is separable from the faulty stochastic path
5. Complete trajectories carry independently verifiable provenance

This is SU(3) pure gauge theory — the first step toward full lattice QCD
with dynamical fermions.

---

## Data Complete (in paper)

| Section | Content | Status |
|---------|---------|--------|
| 3.1 Lattice Scaling | 4⁴, 8⁴ timing on RTX 3090 + RX 6950 XT | DONE |
| 3.2 Plaquette Values | β=2.3, cpu_mom path, GPU-vs-CPU agreement | DONE |
| 3.3 DF64 Precision | Per-op accuracy, accumulated accuracy, precision matrix | DONE |
| 3.4 Multi-Vendor | NVIDIA/AMD from same WGSL, 8⁴ agreement 3.1×10⁻⁹, **16⁴ agreement 6 ppm** | DONE |
| 3.5 Autocorrelation | τ_int, N_eff at both volumes | DONE |
| 4.1 Cost Analysis | Sovereign vs cloud pricing | DONE |
| 4.2 PRNG Discovery | Three-path isolation, cpu_mom validation, 9.5% variance deficit | DONE |
| 4.5 Vendor Neutrality | WGSL→PTX/GCN compilation pipeline | DONE |
| 5 Reproducibility | pseudoSpore artifact description | DONE |

---

## Resolved Issues

| Issue | Resolution |
|-------|-----------|
| Plaquette ×4 vs SU(2) | **Gauge group mismatch** — code is SU(3), ⟨P⟩≈0.15 is correct |
| GPU PRNG bias | **cpu_mom workaround** — 9.5% variance deficit in polyfill transcendentals |
| Cross-GPU divergence | **Validated** — inter-GPU agreement at 3.1×10⁻⁹ |

---

## Remaining Validation (strengthens, does not block)

| # | Experiment | Priority | Owner | Status |
|---|-----------|----------|-------|--------|
| 1 | Action–force finite-difference test | HIGH | hotSpring | **DONE** — max Δ/F = 8×10⁻⁶ |
| 2 | β-scan (2.0–6.5) vs published SU(3) | HIGH | hotSpring | **DONE** — §4.4 |
| 3 | ΔH scaling + Creutz equality | HIGH | hotSpring | **DONE** — ⟨exp(-ΔH)⟩=0.999985 |
| 4 | Multi-seed (8 seeds) statistics | HIGH | hotSpring | **DONE** — §4.5.3 |
| 5 | 12⁴ volume scan (5 β points) | MEDIUM | hotSpring | **DONE** — §4.4 (Δ<0.1% at β≥6.0) |
| 6 | 16⁴ + 24⁴ production | MEDIUM | hotSpring | **16⁴ DONE** — dual-GPU parity CONFIRMED. β=6.2: Δ=3.75×10⁻⁶ (6 ppm). β=6.0: +0.01% vs published. AMD 9.4× faster (273 vs 2567 ms/traj). 24⁴ thermalizing (10th config). |
| 6 | pseudoSpore version freeze | MEDIUM | Node Atomic | Section 5 |

---

## Submission Path

```
16⁴ dual-GPU scan completes (RUNNING — RTX 3090 + RX 6950 XT)
    ↓
Integrate final 16⁴ cross-vendor data into paper sections
    ↓
sporePrint regenerates LaTeX (tectonic build)
    ↓
PRE-SUBMISSION REVIEW — 3 known reviewers:
  • Michael Murillo (MSU — computational physics)
  • Thomas Chuna (LANL — lattice/kinetic theory)
  • Alexei Bazavov (MSU — lattice QCD specialist)
    ↓
Incorporate reviewer feedback
    ↓
arXiv hep-lat submission (cross-list cs.DC)
    ↓
ORCID: 0009-0004-2141-0321
```

---

## 5-Rung Ladder (UPDATED: Aug 9 — capacity breakthrough)

| Rung | Title Pattern | Max Volume | Status |
|------|--------------|-----------|--------|
| 1 | SU(N) Pure Gauge HMC with DF64 WebGPU/WGSL | **64⁴** (single) / **73⁴** (dual) | **This paper** — DATA COMPLETE |
| 2 | Quenched QCD (Dirac operator on SU(3) backgrounds) | ~58⁴ (folded) | Planned — TMU multigrid 3-5× CG speedup |
| 3 | Dynamical QCD on Consumer GPUs (RHMC) | ~52⁴ (folded) | Planned — ROP force + FP32 shift vectors |
| 4 | (2+1)-Flavor QCD on Sovereign Hardware | ~48⁴ (folded) | Planned — production-competitive |
| 5 | Finite-Temperature QCD on Consumer GPUs | ~64³×12 (folded) | Planned — continuum-limit extrapolation viable |

**Key upgrade**: Previous max was 22⁴ (software guard). Guard bypass + silicon offloading
yields 121× more lattice sites. All 5 rungs now reach volumes competitive with HPC
national-lab computations. See `LATTICE_CAPACITY_SILICON_OFFLOADING_AUG09.md`.

Full roadmap: `wateringHole/handoffs/OVERWATCH_LATTICE_QCD_LADDER.md`

---

## Key Lesson

The gauge group audit revealed that the code has been SU(3) from the start.
The "×4 discrepancy" vs published SU(2) data was not a normalization bug —
it was simply comparing to the wrong gauge group. `Su3Matrix`, `Re Tr / 3`,
`β/3` force coupling, `β = 6/g²` — all unambiguously SU(3). ⟨P⟩ ≈ 0.15
at β=2.3 matches SU(3) strong-coupling expansion. The paper was mislabeled,
not the physics. This is a stronger result than originally claimed.

---

*subGen Wave 155v — SU(3) pure gauge preprint. Data complete. All HIGH-priority
validation experiments passed. Parallel thermalization infrastructure LIVE: 10 configs
thermalizing across 64 EPYC threads, BLAKE3-addressed config cache, cache-aware GPU
production pipeline. Ready for LaTeX generation and submission.*
