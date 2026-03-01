# Nautilus — Evolutionary Reservoir Computing & Brain Architecture

**Where bingo boards become brains: evolutionary reservoirs, neuromorphic deployment, and multi-substrate orchestration.**

---

## Overview

Nautilus is the adaptive intelligence layer of the ecoPrimals compute pipeline. It combines three systems into a unified brain architecture:

1. **Nautilus Shell** — Evolutionary reservoir computing using BingoCube bingo boards as structured random projections. Populations of boards evolve under column-range constraints; generations replace temporal recurrence; the accumulated history forms a serializable, transferable "shell."

2. **ESN Integration** — Echo State Networks deployed on BrainChip AKD1000 neuromorphic hardware (15 production heads) and in software simulation. The NPU runs at 30 mW continuous, handles adaptive steering, phase prediction, CG cost estimation, and anomaly detection.

3. **Brain Architecture** — A 4-layer concurrent pipeline treating biomeGate as a brain: RTX 3090 (motor cortex), Titan V (pre-motor), CPU/256 GB (cortex), AKD1000 NPU (cerebellum). The NPU coordinates all layers, interrupting only on anomalies.

**Status**: March 1, 2026 — Nautilus Shell validated (31 tests, 5 examples, 5.3% LOO, 2.6% blind prediction). Brain architecture validated through Exp 028-030. AKD1000 int4 export validated (quantization MSE = 0.004).

**Crate**: `bingocube-nautilus` (`primalTools/bingoCube/nautilus/`)
**License**: AGPL-3.0-only

---

## Document Series

### Design & Origins

| # | Document | Description |
|---|----------|-------------|
| 00 | [00_INTRODUCTION.md](00_INTRODUCTION.md) | Origin story, design philosophy, the bingo-to-brain pipeline |
| 01 | [01_ARCHITECTURE.md](01_ARCHITECTURE.md) | Nautilus Shell: boards as reservoirs, evolution as time, shells as memory |

### Systems

| # | Document | Description |
|---|----------|-------------|
| 02 | [02_ESN_INTEGRATION.md](02_ESN_INTEGRATION.md) | NPU ESN heads, Gen 1/Gen 2 evolution, sim vs hardware, cross-chip transfer |
| 03 | [03_BRAIN_ARCHITECTURE.md](03_BRAIN_ARCHITECTURE.md) | 4-layer concurrent brain: motor, pre-motor, cortex, cerebellum |
| 04 | [04_DRIFT_AND_EDGES.md](04_DRIFT_AND_EDGES.md) | Drift monitor, edge seeding, concept edge detection |
| 05 | [05_AKD1000_DEPLOYMENT.md](05_AKD1000_DEPLOYMENT.md) | Hardware mapping, int4 quantization, export/import pipeline |

### Validation & Evolution

| # | Document | Description |
|---|----------|-------------|
| 06 | [06_VALIDATION.md](06_VALIDATION.md) | Test results, full brain rehearsal, live predictions, state persistence |
| 07 | [07_ROADMAP.md](07_ROADMAP.md) | Evolution plans, LTEE library vision, multi-spring deployment |

---

## Reading Order

**For a reservoir computing researcher**: 01 (architecture) → 04 (drift/edges) → 06 (validation) → 05 (AKD1000) → 07 (roadmap)

**For a neuromorphic engineer**: 05 (AKD1000) → 02 (ESN heads) → 01 (architecture) → 06 (validation)

**For a systems architect**: 03 (brain architecture) → 02 (ESN integration) → 04 (drift/edges) → 07 (roadmap)

**For a physicist using the pipeline**: 00 (introduction) → 01 (architecture) → 06 (validation) → 03 (brain)

**For a biologist / LTEE researcher**: 00 (introduction) → 04 (drift/edges) → 07 (roadmap, LTEE vision)

---

## Quick Numbers

| Metric | Value |
|--------|-------|
| Nautilus Shell unit tests | 31 |
| Examples | 5 (lifecycle, prediction, QCD transfer, brain rehearsal, live Exp 029) |
| LOO generalization error | 5.3% on CG cost prediction |
| Blind Exp 029 prediction | 2.6% CG error (never trained on dynamical data) |
| Quenched→dynamical transfer | 540× cost reduction |
| AKD1000 quantization MSE | 0.004 |
| State persistence | Bit-perfect (delta < 10⁻¹⁶) |
| Serialized shell size | ~23 KB (16 boards, 20 generations, 2 targets) |
| NPU production heads | 11 active + 4 proxy = 15 total |
| Hardware power draw | 30 mW continuous (NPU cerebellum) |
| Brain layers | 4 (3090 + Titan V + CPU + NPU) |

---

## Cross-References

| Document | Location |
|----------|----------|
| baseCamp Paper 11 | `gen3/baseCamp/11_bingocube_nautilus_shell.md` |
| Thesis §3.4.6 | `gen3/thesis/03_theoretical_framework.md` |
| Brain Architecture Spec | `hotSpring/specs/BIOMEGATE_BRAIN_ARCHITECTURE.md` |
| Exp 028 (Brain Pipeline) | `hotSpring/experiments/028_BRAIN_CONCURRENT_PIPELINE.md` |
| Exp 029 (NPU Steering) | `hotSpring/experiments/029_NPU_STEERING_PRODUCTION.md` |
| Exp 030 (Adaptive Fix) | `hotSpring/experiments/030_ADAPTIVE_STEERING_PRODUCTION.md` |
| toadStool Handoff | `hotSpring/wateringHole/handoffs/HOTSPRING_NAUTILUS_EVOLUTION_TOADSTOOL_HANDOFF_MAR01_2026.md` |
| Crate source | `primalTools/bingoCube/nautilus/` |
