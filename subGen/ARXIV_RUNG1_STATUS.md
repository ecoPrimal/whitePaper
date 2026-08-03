# arXiv Rung 1 — SU(2) Preprint Status

**Status**: **BLOCKED** — plaquette ×4 normalization must be resolved first
**Wave**: post-155n | **Date**: Aug 2, 2026 (updated)
**Paper**: `LATTICE_QCD_CONSUMER_GPU_ARXIV.md` (this directory)
**LaTeX**: `lattice_qcd_consumer_gpu.tex` (this directory)

---

## Title

**Toward Vendor-Agnostic Lattice QCD on Consumer GPUs: SU(2) Hybrid Monte
Carlo with DF64 WebGPU/WGSL and Cryptographic Provenance**

---

## What Rung 1 Proves

1. Non-Abelian gauge HMC executes through WebGPU/WGSL
2. DF64 is accurate for SU(2) observables (~9 digits accumulated)
3. Common WGSL source produces identical physics on NVIDIA and AMD
4. The deterministic GPU MD path is separable from the faulty stochastic path
5. Complete trajectories carry independently verifiable provenance

This is SU(2) lattice gauge theory, not lattice QCD. The title says
"Toward" — the completed result is SU(2), the intended system is lattice QCD.

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
| 4.2 PRNG Discovery | Three-path isolation, cpu_mom validation | DONE |
| 4.5 Vendor Neutrality | WGSL→PTX/GCN compilation pipeline | DONE |
| 5 Reproducibility | pseudoSpore artifact description | DONE |

---

## Experiment Queue (reordered — normalization first)

**CRITICAL**: Do NOT run items 4-8 until items 1-3 are resolved.

| # | Experiment | Priority | Owner | Blocks |
|---|-----------|----------|-------|--------|
| 1 | **Resolve plaquette ×4 normalization** | **BLOCKER** | hotSpring | Everything |
| 2 | Action–force finite-difference test | **BLOCKER** | hotSpring | Submission |
| 3 | Short β-scan (1.8–2.5) vs published SU(2) data | **BLOCKER** | hotSpring | Submission |
| 4 | Reversibility + ΔH scaling | HIGH | hotSpring | Submission |
| 5 | Multiple seeds + longer chains | HIGH | hotSpring | Submission |
| 6 | PRNG distribution characterization | MEDIUM | hotSpring | Submission |
| 7 | 12⁴/16⁴ full production | MEDIUM | hotSpring | Paper completeness |
| 8 | pseudoSpore version freeze | MEDIUM | Node Atomic | Section 5 |

The ×4 discrepancy: reported ⟨P⟩ ≈ 0.15 at β=2.3, published SU(2) is
≈ 0.60. Exactly 4×. May be measurement normalization (extra 1/N² or 1/4)
or action coupling convention (effective β/4). See paper Appendix B for
diagnostic protocol.

Full experiment specs: `wateringHole/handoffs/HOTSPRING_RUNG1_EXPERIMENT_QUEUE.md`
Normalization AAR: `wateringHole/aars/SPOREPRINT_PLAQUETTE_NORMALIZATION_AAR.md`

---

## Submission Path

```
hotSpring runs experiment queue
    ↓
sporePrint integrates data into markdown draft
    ↓
sporePrint regenerates LaTeX (tectonic build)
    ↓
Final hype compliance review
    ↓
arXiv hep-lat submission (cross-list cs.DC)
    ↓
ORCID: 0009-0004-2141-0321
```

---

## 6-Rung Ladder (future papers)

| Rung | Title Pattern | Status |
|------|--------------|--------|
| 1 | SU(2) HMC with DF64 WebGPU/WGSL | **This paper** |
| 2 | SU(3) Pure Gauge on Consumer GPUs | In development |
| 3 | Quenched QCD with DF64 Dirac Operator | Planned |
| 4 | Dynamical QCD on Consumer GPUs | Planned |
| 5 | (2+1)-Flavor QCD on Sovereign Hardware | Planned |
| 6 | Finite-Temperature QCD on Consumer GPUs | Planned |

Full roadmap: `wateringHole/handoffs/OVERWATCH_LATTICE_QCD_LADDER.md`

---

## Key Lesson

An AI review confirmed the pattern seen throughout ecoPrimals development:
**the code is real, the comparisons are hype.** Every self-contained,
falsifiable claim checked out. Every scoping claim (calling SU(2) "lattice
QCD," claiming 16⁴ production without data) needed correction. The fix:
name what you proved, not what you intend to prove.

---

*subGen Wave post-155n — Rung 1 preprint under validation. The SU(2)
result is strong. Experiment queue is the critical path to arXiv.*
