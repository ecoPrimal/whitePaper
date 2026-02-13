# BarraCUDA White Paper — Section Index

**Title**: BarraCUDA: Heterogeneous Scientific Computing Through Constrained Evolution  
**Status**: Draft v1 (all sections complete, under review)  
**Date**: February 2026

---

## Paper Structure

| Section | Title | Lines | Status |
|:-------:|-------|:-----:|:------:|
| 00 | [Abstract and Introduction](00_ABSTRACT_AND_INTRODUCTION.md) | ~100 | Draft v1 |
| 01 | [FHE Validation](01_FHE_VALIDATION.md) | 265 | Draft v2 (corrected) |
| 02 | [Hardware Comparison](02_HARDWARE_COMPARISON.md) | 363 | Draft v2 (honesty audit) |
| 03 | [ToadStool Wiring Directive](03_TOADSTOOL_WIRING_DIRECTIVE.md) | 285 | Action items |
| 04 | [Control Experiments](04_CONTROL_EXPERIMENTS.md) | ~430 | Draft v4 (86/86, energy profiling, GPU data) |
| 04a | [Surrogate Open Science](04a_SURROGATE_OPEN_SCIENCE.md) | ~220 | Draft v1 (Code Ocean critique) |
| 05 | [Constrained Evolution](05_CONSTRAINED_EVOLUTION.md) | ~200 | Draft v1 |
| 06 | [Conclusion and Future Work](06_CONCLUSION.md) | ~170 | Draft v1 |

**Total**: ~1,700 lines across 7 sections

---

## Reading Order

For **reviewers**: 00 → 01 → 02 → 04 → 04a → 05 → 06 (skip 03, which is internal)

For **ToadStool team**: 03 → 02 (to understand what needs wiring)

For **control experiment details**: 04 → `hotSpring/CONTROL_EXPERIMENT_STATUS.md`

---

## Data Sources

| Data | Location | Format |
|------|----------|--------|
| FHE benchmarks | `data/fhe/` | JSON + CSV |
| ML benchmarks | `data/ml/` | JSON + CSV |
| NPU benchmarks | `data/neuromorphic/` | JSON + CSV |
| Cross-vendor validation | `data/fhe/cross_vendor/` | JSON |
| MNIST pipeline | `data/fhe/encrypted_mnist_pipeline.json` | JSON + CSV |
| Control results (comprehensive) | `../../hotSpring/control/comprehensive_control_results.json` | JSON |
| Observable validation (Sarkas) | `../../hotSpring/control/sarkas/simulations/dsf-study/results/` | JSON |
| TTM results | `../../hotSpring/control/ttm/reproduction/` | CSV + JSON |
| Surrogate results | `../../hotSpring/control/surrogate/results/` | JSON |

---

## Evidence Quality Classification

All claims in the paper are classified:

- **Tier 1 (✅ Real)**: Measured on actual hardware, operation under test executing on claimed substrate
- **Tier 2 (⚠️ Partial)**: Real execution with some modeled component (e.g., datasheet power)
- **Tier 3 (❌ Modeled)**: Computed from assumptions, explicitly labeled as such

No result labeled "validated" uses mocks, simulations, or estimated timings.

---

## Key Numbers

| Metric | Value | Source |
|--------|-------|--------|
| GPU NTT speedup (N=4096) | **110×** | §1 — measured |
| Cross-vendor correctness | **34/36** (all GPU correct) | §1 — measured |
| NTT → FFT code reuse | **80%** | §5 — source comparison |
| Control checks (all) | **86/86 pass** | §4 — measured |
| Sarkas observables | **60/60 pass** | §4 — measured |
| Upstream bugs found | **5** (3 silent) | §4 — documented |
| Force kernel hotspot | **97.2%** of exec time | §4 — profiled |
| Energy efficiency range | **10⁶×** across workloads | §2 — measured |
| BarraCUDA L1 vs Python | **478× faster**, chi2 2.27 vs 6.62 | §4 Phase B — measured |
| BarraCUDA GPU energy | **44.8× less** than Python (L1 SEMF) | §4 Phase B — measured (RAPL + nvidia-smi) |
| GPU FP64 precision | **4.55e-13 MeV** max error vs CPU | §4 Phase B — measured |
| L2 improvement (4 cycles) | **1,764× improvement** | §4 Phase B — measured |
| Math functions validated | **11** against NumPy/SciPy | §4 Phase B — production |
| External dependencies | **0** (nalgebra removed) | §4 Phase B — verified |
| NMP physical correctness | **5/5 within 2σ** | §4 Phase B — measured |

---

## GPU FP64 Handoff (NEW — February 13, 2026)

| Document | Purpose |
|----------|---------|
| [`../HOTSPRING_GPU_HANDOFF.md`](../HOTSPRING_GPU_HANDOFF.md) | **ToadStool team**: Full findings from GPU FP64 science validation, naga gotchas, precision data, evolution targets |

## Phase B Data Sources (NEW — February 13, 2026)

| Data | Location | Format |
|------|----------|--------|
| L1 validation results | `../../hotSpring/barracuda/` (run binary) | stdout + JSON |
| L2 validation results | `../../hotSpring/control/surrogate/nuclear-eos/results/barracuda_l2_evolved.json` | JSON |
| L3 validation results | `../../hotSpring/control/surrogate/nuclear-eos/results/barracuda_l3_deformed.json` | JSON |
| Public-safe writeup | `../../hotSpring/whitePaper/BARRACUDA_SCIENCE_VALIDATION.md` | Markdown |
| Evolution handoffs | `../../wateringHole/handoffs/BARRACUDA_L2_FULL_EVOLUTION_FEB13_2026.md` | Markdown |
| GPU roadmap | `../../wateringHole/handoffs/BARRACUDA_EVOLUTION_GUIDE_GPU_READY_FEB13_2026.md` | Markdown |

