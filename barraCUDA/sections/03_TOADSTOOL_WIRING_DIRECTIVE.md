# ToadStool Wiring Directive: Complete Real Hardware Integration

**To**: ToadStool Team  
**From**: ecoPrimals / White Paper Review  
**Date**: February 7, 2026  
**Priority**: IMMEDIATE  
**Status**: Action Required

---

## Context

The white paper audit of Sections 01 (FHE Validation) and 02 (Hardware Comparison) revealed a consistent pattern: BarraCUDA's **core primitive operations are real and validated**, but several **showcase benchmarks use `sleep()`, CPU busy-loops, or throughput multipliers** instead of actual hardware execution. This directive tells you exactly what needs to be wired, what needs to be deleted, and what gets deprioritized.

**Key policy change**: FHE scheme-level work (BFV/CKKS encryption, encrypted training) is **pinned to NUCLEUS deployment** — BearDog owns the ciphertext layer. ToadStool should redirect that effort to **completing real hardware wiring across CPU, GPU, and NPU**.

---

## Inventory: What's Real vs What's Faking

### ✅ REAL — Do Not Touch (Validated in White Paper)

| Component | Evidence | File |
|-----------|----------|------|
| FHE NTT/INTT on GPU | 110× speedup measured | `crates/barracuda/src/ops/fhe_ntt.wgsl` |
| FHE PolyAdd/Mul/Sub | Cross-vendor correct | `crates/barracuda/src/ops/fhe_poly_*.wgsl` |
| Complex mul/exp | Euler's identity verified | `crates/barracuda/src/ops/complex/` |
| FFT 1D/2D/3D | Evolved from NTT | `crates/barracuda/src/ops/fft/` |
| MD force kernels | Coulomb, Yukawa, LJ, Morse, Born-Mayer | `crates/barracuda/src/ops/md/forces/` |
| PBC distance | Minimum image convention | `crates/barracuda/src/ops/md/pbc.wgsl` |
| LeNet5 GPU demo | Real OpenCL execution | `showcase/gpu-universal/ml-inference/src/bin/lenet5_demo.rs` |
| wgpu executor | Real Vulkan compute | `showcase/gpu-universal/ml-inference/src/wgpu_executor.rs` |
| MNIST NPU inference | Real `akida_driver` calls | `showcase/barracuda-validation/benchmarks/mnist/mnist_npu.rs` |
| K-mer NPU | Real `akida_driver` calls | `showcase/barracuda-validation/benchmarks/genomics/kmer_npu.rs` |
| Cross-platform FHE | CPU TFHE-rs + GPU BarraCUDA | `showcase/barracuda-validation/benchmarks/universal/cross_platform_homomorphic.rs` |
| Transformer inference | Real MatMul/LayerNorm on GPU | `showcase/whitePaper/benchmarks/transformer_inference.rs` |

### ❌ FAKING — Needs Real Wiring or Deletion

Sorted by priority (NPU first — you have 2× Akida chips sitting on the tower).

---

## PRIORITY 1: NPU Wiring (2× Akida AKD1000 Available)

You already have the pattern working in `mnist_npu.rs` and `kmer_npu.rs`. Both use `akida_driver::InferenceExecutor::infer()` on real hardware. Apply this pattern to the remaining NPU benchmarks.

### 1.1 Pipeline Dispatch NPU — `tokio::time::sleep()`

**File**: `showcase/homomorphic-computing/examples/pipeline_validation_actual_hardware.rs`  
**Lines**: 406-411

```rust
// CURRENT (fake):
// TODO: Wire actual Akida inference
for _ in 0..iterations {
    let events = (iterations as f32 * (1.0 - sparsity)) as u64;
    tokio::time::sleep(tokio::time::Duration::from_micros(events)).await;
}
```

**Fix**: Replace with `akida_driver` inference call. Use same pattern as `mnist_npu.rs`:
```rust
let config = InferenceConfig::new(vec![input_size], vec![output_size], 1, 1);
let executor = InferenceExecutor::new(config);
for _ in 0..iterations {
    let _ = executor.infer(&events, &mut device)?;
}
```

**Also fix**: Lines 427-428 (NPU→GPU pipeline) and 464-465 (GPU→NPU pipeline) — same `sleep()` pattern.

**Impact**: Converts pipeline dispatch from ❌ Modeled to ✅ Real. This is the single highest-value fix for the white paper.

### 1.2 Reservoir Computing NPU — CPU Busy-Loop

**File**: `showcase/whitePaper/benchmarks/npu_reservoir_computing.rs`  
**Lines**: 196-205

```rust
// CURRENT (fake):
// Simulate sparse event-driven processing
let sparsity = 0.1;
let active_neurons = (reservoir_size as f32 * sparsity) as usize;
for _ in 0..iterations {
    let _work: u64 = (0..active_neurons * sequence_length)
        .map(|i| (i as u64 * 7919) % 104729)
        .sum();
}
```

**Problem**: This produces throughput numbers of 384 billion samples/sec (physically impossible). The numbers are CPU loop iteration rates.

**Fix**: Deploy an actual SNN reservoir model to Akida. You already have the conversion pipeline documented in `showcase/neuromorphic/BENCHMARKS.md`. Train a small reservoir network in Python/Keras, convert with `quantize_model()` + `convert_to_akida()`, save as `.akd`, load via `akida_driver`.

**Effort**: Medium. Requires Python model training step, then Rust integration via existing `akida_driver`.

### 1.3 Hybrid Raytracing NPU — CPU Busy-Loop

**File**: `showcase/whitePaper/benchmarks/hybrid_raytracing.rs`

**Problem**: Both BVH traversal and shading are CPU busy-loops. Throughput numbers (1.4 quadrillion rays/sec) are physically impossible.

**Fix**: Deploy a sparse BVH-traversal SNN to Akida for the traversal phase. The GPU shading phase should use real BarraCUDA operations (you already have the matmul/texture ops). This is the most complex NPU wiring task.

**Effort**: High. May want to defer to after 1.1 and 1.2 are done.

### 1.4 Dense vs Sparse NPU — Throughput Multiplier

**File**: `showcase/akida-characterization/benchmarks/dense_vs_sparse.rs`  
**Also**: `showcase/homomorphic-computing/src/substrates/npu.rs` line 207

```rust
// CURRENT (modeled):
let throughput = (total_ops as f64 / duration_secs) * 3.0;  // ← 3× multiplier!
```

**Fix**: Replace with actual `akida_driver` sparse event processing. Feed sparse vectors as spike events, measure real throughput.

### 1.5 Power Measurement — Use Real Akida Telemetry

**File**: `showcase/homomorphic-computing/src/measurement/power.rs`  
**Lines**: 270-281

```rust
// TODO: Use actual Akida detection from showcase/neuromorphic
// TODO: Use actual Akida API for power measurement
```

**Fix**: BrainChip Akida SDK provides `device.power_consumption()` or equivalent. Wire it. This converts all NPU energy numbers from ❌ Datasheet to ✅ Measured.

---

## PRIORITY 2: GPU Cleanup — Delete Fakes, Wire Remaining

### 2.1 DELETE: Fake GPU Demos

These files claim GPU execution but use `sleep()` or `forward_cpu()`:

| File | Problem | Action |
|------|---------|--------|
| `gpu-universal/ml-inference/src/bin/real_cuda_vs_barracuda.rs` | `thread::sleep()` pretending to be GPU | **DELETE** |
| `gpu-universal/ml-inference/src/bin/vendor_agnostic_demo.rs` | `forward_cpu()` claiming GPU | **DELETE** |
| `gpu-universal/ml-inference/src/bin/cuda_vs_barracuda_benchmark.rs` | Suspected CPU fallback | **AUDIT → DELETE if fake** |

These were identified in your own `HONEST_SHOWCASE_AUDIT_JAN12_2026.md`. You already know they're fake. Just delete them and point scripts to `lenet5_demo.rs`.

### 2.2 Wire: Cross-Platform MLP

**File**: `showcase/barracuda-validation/benchmarks/universal/cross_platform_mlp.rs` line 92

```rust
// TODO: Implement actual WGSL compute shader version
println!("   NOTE: GPU shader integration pending - using CPU fallback");
```

**Fix**: Use `WgpuDevice::new()` + BarraCUDA `MatMul` ops (same pattern as `transformer_inference.rs`).

### 2.3 Wire: FHE Operation Validation

**File**: `showcase/whitePaper/benchmarks/fhe_operation_validation.rs` line 194

```rust
// TODO: Replace with actual BarraCUDA FHE operation
```

**Fix**: Use `FhePolyAdd::new().execute()`, `FheNtt::new().execute()`, etc. These ops already exist and are validated.

### 2.4 Wire: GPU Power Measurement

**File**: `showcase/homomorphic-computing/src/substrates/gpu.rs` line 526

```rust
// TODO: Integrate with nvidia-smi or similar for actual measurement
Some(150.0)
```

**Fix**: Shell out to `nvidia-smi --query-gpu=power.draw --format=csv,noheader,nounits` or use NVML bindings. The RTX 3090 supports real-time power queries.

---

## PRIORITY 3: ML Architecture Completion

These benchmarks use real BarraCUDA GPU ops but simplified model architectures. Complete them:

### 3.1 Transformer → Full Multi-Head Attention

**File**: `showcase/whitePaper/benchmarks/transformer_inference.rs`  
**Current**: Single MatMul per "layer"  
**Target**: Q/K/V projections → scaled dot-product attention → concatenation → feed-forward  
**Ops needed**: All exist (MatMul, Softmax, LayerNorm, GELU, Add). Just compose them correctly.

### 3.2 Audio STFT → Real FFT Shader

**File**: `showcase/whitePaper/benchmarks/audio_processing.rs`  
**Current**: Simplified spectral analysis using tensor ops  
**Target**: Use `fft_1d.wgsl` (already implemented!) for real STFT  
**This should be trivial** — the FFT shader exists, just wire it into the audio pipeline.

### 3.3 Vision → Full Conv Pipeline

**File**: `showcase/whitePaper/benchmarks/vision_inference.rs`  
**Current**: Simplified Conv2D architecture  
**Target**: Full MobileNet/ResNet layer composition  
**Ops needed**: Conv2D, MaxPool2D, BatchNorm, ReLU — all exist.

---

## DEPRIORITIZE: Pin to NUCLEUS

These items are **explicitly deferred** until NUCLEUS enables BearDog↔ToadStool composition:

| Item | Owner | Gate |
|------|-------|------|
| BFV encryption/decryption | BearDog | NUCLEUS deployment |
| CKKS encryption/decryption | BearDog | NUCLEUS deployment |
| End-to-end encrypted training | BearDog + ToadStool | NUCLEUS deployment |
| End-to-end encrypted inference | BearDog + ToadStool | NUCLEUS deployment |
| Inter-primal coordination demos | All primals | NUCLEUS deployment |

**Files to leave as-is** (placeholder implementations, correctly marked):
- `homomorphic-computing/src/schemes/bfv.rs` — "TODO: Implement actual BFV"
- `homomorphic-computing/src/schemes/ckks.rs` — "TODO: Implement actual CKKS"
- `showcase/inter-primal/01-beardog-encrypted-workload/src/main.rs` — sleep-based demo
- `showcase/inter-primal/03-nestgate-persistent-results/src/main.rs` — sleep-based demo
- `showcase/inter-primal/04-songbird-distributed-coordination/src/main.rs` — sleep-based demo

These are **architecturally correct placeholders** waiting for NUCLEUS. Do not waste time implementing them now.

---

## Suggested Execution Order

```
Week 1-2:  PRIORITY 2.1  — Delete fake GPU demos (30 minutes)
           PRIORITY 1.1  — Wire pipeline dispatch NPU (1-2 days)
           PRIORITY 1.5  — Wire Akida power measurement (1 day)
           PRIORITY 2.3  — Wire FHE operation validation (1 day)

Week 3-4:  PRIORITY 1.2  — Wire reservoir computing NPU (3-5 days, needs Python SNN training)
           PRIORITY 1.4  — Wire dense/sparse NPU (1-2 days)
           PRIORITY 2.2  — Wire cross-platform MLP GPU (1 day)
           PRIORITY 2.4  — Wire GPU power measurement (2 hours)

Week 5-6:  PRIORITY 3.2  — Audio STFT with real FFT shader (1-2 days)
           PRIORITY 3.1  — Full transformer architecture (3-5 days)
           PRIORITY 3.3  — Full vision pipeline (2-3 days)

Week 7+:   PRIORITY 1.3  — Hybrid raytracing NPU (5-7 days, complex)
```

**Total estimate**: 6-8 weeks to convert all ❌ to ✅.

---

## Success Criteria

After this directive is complete:

- [ ] **Zero `sleep()` calls in any benchmark that reports hardware performance**
- [ ] **Zero throughput multipliers** (no `* 3.0`, no `* 0.6`)
- [ ] **Zero CPU busy-loops claiming NPU performance**
- [ ] **All NPU benchmarks use `akida_driver::InferenceExecutor::infer()`**
- [ ] **All GPU benchmarks use real BarraCUDA WGSL dispatch**
- [ ] **Power measurement from hardware telemetry, not datasheets**
- [ ] **Fake GPU demos deleted, scripts updated**
- [ ] **ML architectures complete (multi-head attention, real FFT STFT, full Conv pipeline)**

When these criteria are met, every number in the white paper's hardware comparison section can be cited without caveat.

---

## What This Enables

Once wiring is complete, the white paper can honestly state:

> "BarraCUDA dispatches FHE, ML, and scientific compute workloads to CPU, NVIDIA GPU, AMD GPU, and BrainChip Akida NPU from a single Rust codebase. All performance and energy measurements are from actual hardware execution. No simulations, no mocks, no multipliers."

That is the sentence we are working toward. Everything in this directive exists to make that sentence true.

---

*Generated from white paper audit of Sections 01-02.*  
*Data sources: benchmark source code inspection, `HONEST_SHOWCASE_AUDIT_JAN12_2026.md`, JSON data file analysis.*

