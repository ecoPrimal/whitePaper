# arXiv Rung 1 — SU(3) Pure Gauge Preprint Status

**Status**: **DATA COMPLETE** — gauge group audit resolved, production data validated
**Wave**: 155n | **Date**: Aug 3, 2026 (updated)
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
| 3.4 Multi-Vendor | NVIDIA/AMD from same WGSL, cross-GPU agreement 3.1×10⁻⁹ | DONE |
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
| 5 | 12⁴ and 16⁴ volume scan | MEDIUM | hotSpring | TODO |
| 3 | Reversibility + ΔH scaling | MEDIUM | hotSpring | Submission rigor |
| 4 | Multiple seeds + longer chains | MEDIUM | hotSpring | Statistics rigor |
| 5 | 12⁴/16⁴ full production | MEDIUM | hotSpring | Volume range |
| 6 | pseudoSpore version freeze | MEDIUM | Node Atomic | Section 5 |

---

## Submission Path

```
Remaining validation experiments (β-scan, action-force test) ← DONE
    ↓
sporePrint integrates final data into markdown draft
    ↓
sporePrint regenerates LaTeX (tectonic build)
    ↓
Final compliance review
    ↓
arXiv hep-lat submission (cross-list cs.DC)
    ↓
ORCID: 0009-0004-2141-0321
```

---

## 5-Rung Ladder

| Rung | Title Pattern | Status |
|------|--------------|--------|
| 1 | SU(3) Pure Gauge HMC with DF64 WebGPU/WGSL | **This paper** — DATA COMPLETE |
| 2 | Quenched QCD (Dirac operator on SU(3) backgrounds) | Planned |
| 3 | Dynamical QCD on Consumer GPUs (RHMC) | Planned |
| 4 | (2+1)-Flavor QCD on Sovereign Hardware | Planned |
| 5 | Finite-Temperature QCD on Consumer GPUs | Planned |

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

*subGen Wave 155n — SU(3) pure gauge preprint. Data complete. All HIGH-priority
validation experiments passed. Ready for LaTeX generation and submission.*
