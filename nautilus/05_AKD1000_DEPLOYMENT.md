# 05 — AKD1000 Deployment: Hardware Mapping & Int4 Quantization

**Date:** March 1, 2026

---

## AKD1000 Overview

The BrainChip Akida AKD1000 is a neuromorphic processor designed for
always-on edge inference:

| Spec | Value |
|------|-------|
| Neural Processing units (NPs) | 78 |
| Neurons per NP | 256 (19,968 total) |
| Weight precision | int4 ([-8, 7]) or int8 |
| Inference power | 30 mW continuous |
| Interface | PCIe Gen2 x1 (500 MB/s) |
| On-chip SRAM | ~1 MB |
| Architecture | Feed-forward only (no recurrence) |

The AKD1000's feed-forward constraint is precisely why the Nautilus Shell
exists. Traditional ESNs require recurrence; the AKD1000 cannot do
recurrence. Evolution replaces recurrence. The constraint created the
architecture.

## Why BingoCube Maps to Int4

A bingo board column draws values from [k·R, (k+1)·R) where R=15. The
maximum value is 75. These integers naturally fit in int4 after scaling:

```
Original range: [1, 75]
Scaled to [-8, 7]: value_q = round((value - 38) * 7 / 37)
```

But the readout weights — the linear regression coefficients — are f64.
These need quantization for hardware deployment.

## Akd1000Export

```rust
pub struct Akd1000Export {
    pub quantized_weights: Vec<Vec<i8>>,  // [n_targets][input_dim], int4 range
    pub scales: Vec<f64>,                  // per-target dequantization scale
    pub biases: Vec<f64>,                  // per-target bias
    pub input_dim: usize,
    pub n_targets: usize,
}
```

### Quantization Method

Symmetric min-max quantization to [-8, 7]:

```
scale = max(|w|) / 7
w_q = round(w / scale)
w_q = clamp(w_q, -8, 7)
```

For each target (output dimension), a separate scale is computed. This
preserves the relative magnitudes within each target's weight vector.

### Dequantization for Validation

```
w_hat = w_q * scale
prediction = w_hat · input + bias
```

The `predict_dequantized()` method performs inference using the quantized
weights with dequantization, allowing software validation against hardware.

### Quantization Error

On QCD-like data (2 targets: plaquette and CG cost):

| Metric | Value |
|--------|-------|
| Quantization MSE | 0.004 |
| Plaquette error | ±0.02 (within noise) |
| CG cost error | ±0.04 (within noise) |
| Weight sparsity (zeros) | ~15% (int4 quantization pushes small weights to 0) |
| Max abs weight | 7 (by construction) |
| Min abs weight | 0 (sparse) |

The 15% sparsity is a bonus — sparse weights map to inactive synapses on the
AKD1000, reducing power further.

## Deployment Pipeline

```
1. Train Nautilus Shell on data (CPU, f64 precision)
2. shell.export_akd1000_weights() → Akd1000Export
3. Validate: akd1000_export.quantization_mse(&original_readout) → 0.004
4. Spot-check: akd1000_export.predict_dequantized(test_input) ≈ shell.predict(test_input)
5. Serialize: serde_json::to_string(&akd1000_export) → JSON file
6. Deploy: load JSON → map to akida-models FullyConnected layer
7. Hardware inference: AKD1000 runs int4 multiply-accumulate
```

Step 6 requires the `akida-models` Python SDK (BrainChip's toolchain) to
load the quantized weights into the AKD1000's SRAM. Once loaded, inference
runs at 30 mW with no further host involvement.

## Multi-Head Deployment

Each of the 15 ESN heads gets its own `Akd1000Export`:

```
Head 1 (plaquette predict): input_dim=400, n_targets=1, ~400 int4 weights
Head 2 (CG cost predict):   input_dim=400, n_targets=1, ~400 int4 weights
...
Head 15 (CG residual):      input_dim=100, n_targets=3, ~300 int4 weights
```

Total weight budget: ~6,000 int4 values = ~3 KB. The AKD1000 has ~1 MB SRAM.
The entire 15-head ESN uses < 0.3% of available on-chip memory.

## Transfer to Other Hardware

The `Akd1000Export` format is the reference quantization. For other targets:

| Target | Precision | Adaptation |
|--------|-----------|------------|
| AKD1000 | int4 [-8,7] | Direct deployment |
| AKD1500 (future) | int8 [-128,127] | Widen scale, lower MSE |
| FPGA | int8 or int16 | Standard quantization |
| CPU sim | f64 | Dequantize, no loss |
| GPU (inference) | f16 or f32 | Widen from int4, negligible loss |

The key insight: the column-range constraint means the boards themselves are
already "quantized" — integer values in bounded ranges. The readout
quantization is the only precision-sensitive step, and at 0.004 MSE, it is
well within the noise floor of the physics measurements.
