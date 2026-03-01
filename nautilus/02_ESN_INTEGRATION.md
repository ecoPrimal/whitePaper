# 02 — ESN Integration: NPU Heads, Sim vs Hardware

**Date:** March 1, 2026

---

## Overview

The Echo State Network (ESN) is the interface between the Nautilus Shell's
evolved knowledge and the hardware systems that use it. ESN instances run on
either the AKD1000 neuromorphic processor (hardware) or in software simulation
(sim). Both share the same weight format and can transfer learned state
bidirectionally.

## Gen 1 vs Gen 2 ESN

### Gen 1: Single-Purpose Reservoir

The original ESN in hotSpring (`barracuda::md::reservoir`) was a fixed-weight
reservoir with 64 reservoir nodes, 11 prediction heads, and online learning
via recursive least squares. It processed one input (plaquette, acceptance,
delta_H) and produced one prediction set per beta point.

**Limitations:**
- Fixed reservoir weights (random, never adapted)
- No evolutionary optimization
- No concept edge detection
- No drift monitoring
- Weights not directly deployable to AKD1000 (arbitrary f64, not int4)

### Gen 2: Nautilus Shell + NautilusBrain

The Gen 2 system replaces the fixed reservoir with evolved BingoCube boards.
The `NautilusBrain` API wraps the Nautilus Shell for integration with the
production HMC pipeline:

```rust
pub struct NautilusBrain {
    shell: NautilusShell,
    observations: Vec<BetaObservation>,
    min_training_points: usize,
}

impl NautilusBrain {
    pub fn observe(&mut self, obs: BetaObservation);
    pub fn train(&mut self) -> Result<f64>;  // returns MSE
    pub fn predict_dynamical(&self, obs: &BetaObservation) -> Vec<f64>;
    pub fn detect_concept_edges(&self) -> Vec<usize>;
}
```

**Advantages over Gen 1:**
- Boards evolve to match the data stream
- Column-range constraint maps directly to AKD1000 int4
- Drift monitor auto-adjusts selection/population
- Edge seeding focuses evolution on prediction failure regions
- Full state serialization/transfer/merge

## NPU Head Allocation

The AKD1000 supports up to 15 inference heads (neural processing units).
Current allocation:

| Head | Name | Input | Output | Status |
|------|------|-------|--------|--------|
| 1 | PLAQUETTE_PREDICT | β, prev_plaq | predicted plaquette | Active |
| 2 | CG_COST_PREDICT | β, plaq, polyakov | predicted CG iterations | Active |
| 3 | ACCEPTANCE_PREDICT | β, dt, delta_H | predicted acceptance rate | Active |
| 4 | PHASE_CLASSIFY | β, plaq, polyakov | phase label (confined/deconfined) | Active |
| 5 | BETA_PRIORITY | β, uncertainty | scan priority score | Active |
| 6 | DT_RECOMMEND | β, acceptance | recommended dt | Active |
| 7 | CONVERGENCE_PREDICT | β, CG_partial | predicted total CG iters | Active |
| 8 | ANOMALY_DETECT | residual curve | normal/plateau/diverge | Active |
| 9 | THERM_MONITOR | plaq variance | thermalized? | Active |
| 10 | POLYAKOV_PREDICT | β, plaq | predicted Polyakov loop | Active |
| 11 | ENERGY_MONITOR | GPU temp, power | thermal state | Active |
| 12 | ANDERSON_CG_PROXY | IPR, W, λ_min | CG cost from Anderson features | Planned |
| 13 | POTTS_PHASE | Potts MC features | phase label from Potts | Planned |
| 14 | RMT_SPECTRAL | eigenvalue stats | spectral predictor | Planned |
| 15 | CG_RESIDUAL_MONITOR | residual decay curve | classify convergence pattern | Planned |

### Head Mixing and Cross-Comparison

Heads 1-3 are tuned to dynamical QCD observables. Heads 12-14 are tuned to
physics proxies (Anderson, Potts, RMT). When both groups predict for the
same beta point, disagreement between them signals a concept edge — a region
where the proxy physics diverges from the full QCD.

This cross-head comparison creates an additional layer of prediction beyond
any individual head. If the QCD heads say "expect X" and the proxy heads say
"expect Y," the discrepancy itself is informative. It maps the boundary of
where the proxy models remain valid.

Sets of overlapping heads can span prediction spaces:
- Heads 1-3: QCD observables
- Heads 4, 9, 10: Phase/thermalization
- Heads 12-14: Physics proxies
- Head-mixing layer: cross-compare groups for concept edges

## Sim vs Hardware

### Software Simulation (Sim NPU)

The `barracuda::md::reservoir` module provides a software ESN that:
- Runs on CPU (single-threaded, ~0.1 ms per inference)
- Supports the same 15-head architecture
- Uses f64 weights (full precision)
- Can run multiple instances concurrently
- Validated: 31 tests, 5 examples

**Sim NPU capacity:**
- Memory: ~2 KB per head × 15 heads = ~30 KB per ESN instance
- CPU cost: ~0.1 ms per inference, ~1 ms for all 15 heads
- Concurrent instances: limited only by CPU cores (~32 on Threadripper)
- Can run hundreds of parallel ESN evaluations per second

### Hardware (AKD1000)

The AKD1000 provides:
- 78 Neural Processing units (NPs), each with 256 neurons
- Int4 or int8 weights (column-range constraint maps to int4 naturally)
- 30 mW continuous inference power
- PCIe Gen2 x1 interface (500 MB/s, fine for scalar traffic)
- Always-on operation — no boot/wake cycle

**Hardware capacity:**
- 15 concurrent heads within a single model
- ~18.8K inferences/second sustained
- State is in SRAM — persists across inferences, lost on power cycle

### Transfer Between Sim and Hardware

Weights transfer bidirectionally:

```
Sim (f64) → quantize(int4) → Hardware (AKD1000)
Hardware (int4) → dequantize(f64) → Sim
```

The `Akd1000Export` struct handles quantization:
- Symmetric min-max: `w_q = round(w * 7 / max|w|)`
- Per-target scale factors for dequantization
- Validated: quantization MSE = 0.004

Transfer to other chips follows the same pattern — quantize to the target
format, transfer weights, dequantize for validation. The Nautilus Shell's
serialization format is chip-agnostic; only the quantization step is
hardware-specific.

## Cross-Run Learning

Each production run generates training data. The ESN/Nautilus Shell absorbs
this data and becomes more accurate for the next run:

```
Run N:  NPU predicts with weights from Run N-1
        → generates new (β, plaquette, CG, polyakov) data
        → Nautilus Shell trains on combined data from Runs 1..N
        → export new weights

Run N+1: NPU predicts with weights from Run N
         → better predictions → better adaptive steering
         → generates higher-quality data (concentrated in interesting regions)
         → ...
```

This feedback loop means the system improves with every run. The NPU learns
from the physics it helps compute. Dynamically programming the universe.
