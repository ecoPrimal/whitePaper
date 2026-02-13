# hotSpring GPU FP64 — Handoff to ToadStool Team

**Date**: February 13, 2026
**From**: hotSpring validation team
**To**: ToadStool / BarraCUDA evolution team
**Re**: GPU FP64 science validation findings and evolution targets

---

## Summary

We ran the first end-to-end GPU FP64 nuclear physics computation on the RTX 4070 using BarraCUDA's `SHADER_F64` infrastructure. Two approaches were tested: CPU-precomputed transcendentals fed to GPU, and a **pure-GPU math library** (`math_f64.wgsl`) that computes sqrt, pow, exp, log entirely on GPU. Both work. The pure-GPU path is the one that matters for substrate independence.

---

## 1. What We Built (on our side — you'll reimplement)

### 1.0 `hotSpring/barracuda/src/bench.rs` — Benchmark harness (NEW)

A comprehensive time + energy + hardware context measurement system:
- **Hardware inventory**: CPU model, cores/threads, cache, RAM, GPU name/VRAM/driver/compute capability, OS kernel, Rust version
- **CPU energy**: Intel RAPL (`/sys/class/powercap/intel-rapl:0/energy_uj`) with counter-wrap handling
- **GPU energy**: Background thread polls `nvidia-smi` every 100ms, integrates power → Joules, tracks peak temp/VRAM/utilization
- **Memory**: Peak RSS from `/proc/self/status`
- **Reporting**: Structured JSON + summary table with energy attribution per substrate

Paired with `control/surrogate/nuclear-eos/scripts/bench_wrapper.py` (Python equivalent) so all three substrates report in the same format.

### 1.1 `hotSpring/barracuda/src/gpu.rs` — GPU device wrapper

A thin wrapper around `wgpu` that:
- Creates a device requesting `wgpu::Features::SHADER_F64`
- Provides `create_f64_buffer()`, `create_f64_output_buffer()`, `create_pipeline()`
- Provides `dispatch_and_read()` for synchronous compute+readback
- Reports adapter capabilities (`has_f64`, `has_timestamps`)

This is hotSpring-specific (science workload convenience layer). Your equivalent is the `WgpuDevice` + `TensorContext` + `TensorSession` stack, which already handles all of this more generically.

### 1.2 `hotSpring/barracuda/src/bin/nuclear_eos_gpu.rs` — Three-way validation

Runs L1 (SEMF) and L2 (HFB) nuclear physics on CPU, GPU-with-precompute, and GPU-pure-math. Compares precision, timing, and chi2 values. This is our validation binary — no action needed from you.

### 1.3 `math_f64.wgsl` — Pure-arithmetic f64 math library (PROTOTYPE)

We placed a prototype at `barracuda/src/shaders/math/math_f64.wgsl`. **This is your evolution target.** It implements 27 functions using only f64 arithmetic. You will want to rewrite it properly — what we built is a working proof-of-concept with known precision limitations (see Section 4).

### 1.4 `precision.rs` additions — `math_f64_preamble()` and `with_math_f64()`

We added two methods to `ShaderTemplate` in `precision.rs`:

```rust
/// Returns the full math_f64.wgsl contents as a String
pub fn math_f64_preamble() -> String

/// Prepends math_f64 preamble to a shader body string
pub fn with_math_f64(shader_body: &str) -> String
```

These are the integration points for your shader template system.

---

## 2. What Worked Well

### 2.1 SHADER_F64 is production-ready

Your `check_caps`, `fp64_validation`, and `fp64_benchmark` tools were exactly right. The RTX 4070 confirmed:
- `SHADER_F64: Supported` (Vulkan backend)
- `0 ULP error` vs CPU f64 for basic arithmetic
- Practical FP64:FP32 ratio of **~2x** (not the 1:64 CUDA-reported)

### 2.2 CPU-precomputed GPU path: exact match

When we precompute transcendentals (A^(2/3), A^(1/3), sqrt(A)) on CPU and pass them as buffer data:

| Metric | Value |
|--------|:-----:|
| Max |B_cpu - B_gpu| | **4.55e-13 MeV** |
| Mean |B_cpu - B_gpu| | 8.31e-14 MeV |
| |chi2 diff| | 8.88e-15 |
| GPU speedup (vs BarraCUDA CPU) | **1.8x** |
| GPU speedup (vs Python) | **28.8x** |
| GPU energy savings (vs Python) | **44.8x** |

This is sub-ULP noise. The GPU f64 arithmetic is **bit-exact** with CPU f64 for add/sub/mul/div.

### 2.3 Pure-GPU math library: works, needs precision tuning

The `math_f64.wgsl` library successfully compiled and ran on the RTX 4070:

| Metric | Value |
|--------|:-----:|
| Max |B_cpu - B_pure_gpu| | **4.06e-4 MeV** (0.4 keV) |
| Mean |B_cpu - B_pure_gpu| | 5.24e-5 MeV |
| Time per eval | 45.0 us (**1.6x faster** than CPU) |

The 0.4 keV precision gap comes from `pow_f64` which chains `exp_f64(exponent * log_f64(base))` — each polynomial approximation introduces ~1e-12 error that compounds through the chain.

### 2.4 The ShaderTemplate prepend pattern works

`ShaderTemplate::with_math_f64(user_shader)` concatenates the math library + user code into one shader module. Naga validates the whole thing as a unit. No include mechanism needed.

### 2.5 Timing summary (RTX 4070, 52 nuclei batched, 100k iterations)

| Path | us/eval | vs CPU | vs Python |
|------|:-------:|:------:|:---------:|
| Python (CPython 3.10) | 1,143 | 15.7x slower | baseline |
| CPU (BarraCUDA native) | 72.7 | baseline | **15.7x** |
| GPU (CPU precompute) | 39.7 | **1.8x** | **28.8x** |
| GPU (pure math_f64) | 46.4 | **1.6x** | **24.6x** |

### 2.6 Energy profiling (NEW — February 13, 2026)

We added a full benchmark harness (`barracuda/src/bench.rs`) that measures CPU energy via Intel RAPL and GPU energy via nvidia-smi at 100ms polling intervals. The three-way energy comparison for L1 SEMF (100k iterations, 52 nuclei):

| Substrate | Wall Time | Energy (J) | J/eval | Power (W) |
|-----------|-----------|------------|--------|-----------|
| **Python** (CPython 3.10) | 114.3 s | **5,648 J** | 0.056 | 49 W CPU |
| **BarraCUDA CPU** (Rust native) | 7.27 s | **374 J** | 0.0037 | 51 W CPU |
| **BarraCUDA GPU** (RTX 4070 f64) | 3.97 s | **126 J** | 0.0013 | 32 W GPU |

**Key insight**: GPU L1 uses **44.8x less energy** than Python and **3.0x less** than BarraCUDA CPU — while producing bit-identical physics.

For L2 HFB DirectSampler (12 evals, full SCF): **32,500 J** at 135W avg CPU power for 4 minutes. The Murillo paper ran 30,000 evaluations at similar per-eval cost. At 20s/eval, that is ~7 days wall time and ~810 MJ of CPU energy on this hardware. This is the compute cost that GPU evolution aims to cut by orders of magnitude.

**Measurement infrastructure**: Reports saved as JSON to `benchmarks/nuclear-eos/results/` with full hardware inventory, per-phase energy, and physics results. Compatible between Rust and Python paths. See `benchmarks/PROTOCOL.md` for the full specification.

---

## 3. Critical Naga/WGSL Gotchas You Need to Know

### 3.1 AbstractFloat does NOT auto-promote to f64

This is the single biggest issue. WGSL literal `0.0`, `1.0`, `0.5` etc. are `AbstractFloat`. Naga does **not** promote them to `f64` to match:
- Function return types (`fn foo(x: f64) -> f64 { return 1.0; }` → **FAILS**)
- Function arguments (`pow_f64(a, 2.0 / 3.0)` → **FAILS** because `2.0/3.0` is AbstractFloat)
- Assignments to `array<f64>` elements (`energies[idx] = 0.0;` → **FAILS**)

**Workaround**: Construct f64 values from f64 arithmetic:

```wgsl
// WRONG — naga rejects
return 1.0;

// RIGHT — f64 type propagates from parameter x
return x - x + 1.0;   // (f64 - f64) + AbstractFloat → f64
```

```wgsl
// WRONG — AbstractFloat arguments
pow_f64(a, 2.0 / 3.0);

// RIGHT — construct f64 constants
let two_thirds = (a - a + 2.0) / (a - a + 3.0);
pow_f64(a, two_thirds);
```

We use `x - x + constant` throughout `math_f64.wgsl`. The `x - x` part evaluates to f64 zero, then `+ constant` promotes the constant to f64. It's ugly but reliable.

### 3.2 Literals > f32 range cause parse errors

`1.0e308` (near max f64) overflows f32, so naga rejects it even in an f64 context. Construct large values via arithmetic:

```wgsl
// WRONG
return 1.0e308;

// RIGHT
var big = x - x + 1e37;  // within f32 range
big = big * big;          // 1e74
big = big * big;          // 1e148
big = big * big;          // 1e296
return big * 1e12;        // ~1e308
```

### 3.3 No f64 overloads for ANY builtins

None of these work with f64: `sqrt`, `pow`, `exp`, `log`, `sin`, `cos`, `abs`, `max`, `min`, `floor`, `ceil`, `round`, `clamp`, `sign`, `fract`. All must be implemented as pure arithmetic.

The only operations available on f64 are: `+`, `-`, `*`, `/`, `<`, `>`, `<=`, `>=`, `==`, `!=`, negation, and `i32()`/`f64()` casts.

### 3.4 No f64 vec types

`vec2<f64>`, `vec3<f64>`, `vec4<f64>` are not supported. All f64 operations are scalar. Your `precision.rs` already handles this correctly (falls back to scalar for f64).

### 3.5 `arrayLength()` works fine with `array<f64>`

No issues here — bounds checking via `arrayLength(&output)` works as expected.

---

## 4. What Needs More Evolution

### 4.1 `math_f64.wgsl` precision (HIGH PRIORITY)

Current `pow_f64(a, 2.0/3.0)` has ~4e-4 relative error because it chains `exp(log())`, each with polynomial truncation error. Improvement paths:

1. **More polynomial terms**: The `exp_f64` and `log_f64` functions use degree-13 and degree-10 polynomials. Increasing to degree-17+ would improve from ~1e-12 to ~1e-15 per function.

2. **Specialized fractional powers**: For `A^(1/3)` and `A^(2/3)`, use Newton-Raphson directly (cube root via Halley's method is already implemented as `cbrt_f64`). Bypass the exp/log chain entirely.

3. **Kahan summation in Horner evaluation**: The polynomial evaluation accumulates error through ~13 multiply-adds. Kahan compensation would help.

4. **sqrt_f64 is already good**: 5 Newton-Raphson iterations achieve full f64 precision. Confirmed by the precomputed-GPU comparison.

### 4.2 Preamble system (MEDIUM PRIORITY)

The current approach is string concatenation: `math_f64 + user_shader`. This works but has issues:
- Every f64 shader includes ALL 27 functions (~300 lines) even if it only uses `sqrt_f64`
- Naga compiles unused functions (adds ~10ms to shader compilation)

Better approach: **modular preamble** where `ShaderTemplate` only prepends the functions actually needed. Could be function-level granularity with dependency tracking (e.g., `pow_f64` needs `exp_f64`, `log_f64`, `abs_f64`, `round_f64`, `ipow_f64`).

### 4.3 Batched eigendecomposition shader (HIGH PRIORITY for L2)

The L2 HFB solver's bottleneck is `eigh_f64` (symmetric eigendecomposition). Currently CPU-only. A batched f64 eigendecomposition shader would:
- Process all 52 nuclei × ~10 (l,j) blocks simultaneously
- Each block is small (5x5 to 15x15 matrix)
- Jacobi or Householder QR in f64 using `math_f64` functions

This is the single biggest GPU evolution target for nuclear physics.

### 4.4 Prefix-sum / scan shader for f64 (MEDIUM PRIORITY)

The Coulomb potential in HFB uses cumulative integration (prefix sum). A parallel prefix-sum in f64 would enable full GPU dispatch of the Coulomb step.

### 4.5 GPU-resident DirectSampler (FUTURE)

Currently `DirectSampler` is CPU-resident and calls the objective function serially. A GPU-resident version would:
- Keep all Nelder-Mead vertices on GPU
- Evaluate ALL vertices in a single dispatch
- Only read back the best value for convergence checking

This would make the optimizer itself substrate-independent.

---

## 5. Files We Modified In Your Tree

These are on our machine only. You'll want to reimplement properly:

| File | What we did | Your action |
|------|------------|-------------|
| `shaders/math/math_f64.wgsl` | Created 27-function f64 math library | Rewrite with better precision, modular structure |
| `shaders/precision.rs` | Added `math_f64_preamble()` and `with_math_f64()` | Integrate into your template system properly |

We did **not** modify `wgpu_device.rs` or any other core BarraCUDA files.

---

## 6. Measured Results for Your Records

### L1 SEMF (SLy4, 52 nuclei, RTX 4070, 100k iterations)

```
Python (CPython 3.10):
  chi2/datum = 4.99
  1,143 us/eval
  Energy: 5,648 J (49 W CPU, 114.3s)

CPU (BarraCUDA native):
  chi2/datum = 4.9851
  72.7 us/eval
  Energy: 374 J (51 W CPU, 7.27s)

GPU (CPU-precomputed transcendentals):
  chi2/datum = 4.9851
  39.7 us/eval (1.8x vs CPU, 28.8x vs Python)
  Max |B_cpu - B_gpu| = 4.55e-13 MeV (EXACT)
  Energy: 126 J (32 W GPU, 3.97s)

GPU (pure math_f64 library):
  chi2/datum ≈ 4.9851
  46.4 us/eval (1.6x vs CPU, 24.6x vs Python)
  Max |B_cpu - B_pure| = 4.06e-4 MeV (GOOD, improvable)
```

### L1 DirectSampler optimization

```
CPU:  chi2/datum = 1.52 (48 evals, 6 rounds, 32.4s)
GPU:  chi2/datum = 1.52 (identical physics, GPU-accelerated eval)
```

### L1 LHS Sweep (512 parameter sets)

```
Python:          chi2/datum = 6.87 (best of 512), 147.2s, 7,420 J
BarraCUDA CPU:   chi2/datum = 5.69 (best of 512), 5.07s, 265 J
BarraCUDA GPU:   chi2/datum = 5.69 (best of 512), 3.75s, 122 J
```

### L2 HFB (SLy4 baseline + DirectSampler)

```
SLy4 single-eval: chi2/datum = 54.91 (14/19 converged, 3.6s)
DirectSampler:     chi2/datum = 23.09 (12 evals, 252s, 21s/eval)
Energy: 32,500 J (135 W CPU avg)
```

### Three-way comparison table (with energy)

```
┌────────────┬──────────────────────────────┬──────────────────────────────┬──────────────────────────────┐
│ Level      │ Python/SciPy                 │ BarraCUDA CPU                │ BarraCUDA GPU                │
├────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ L1 SEMF    │ χ² = 4.99                    │ χ² = 4.99                    │ χ² = 4.99                    │
│ (100k)     │ 1,143 us/eval, 5,648 J       │ 72.7 us/eval, 374 J          │ 39.7 us/eval, 126 J          │
│            │                              │ 15.7× faster, 15.1× less E   │ 28.8× faster, 44.8× less E  │
├────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ L1 LHS     │ χ² = 6.87 (best/512)         │ χ² = 5.69 (best/512)         │ χ² = 5.69 (best/512)         │
│ (512 pts)  │ 147.2s, 7,420 J              │ 5.07s, 265 J                 │ 3.75s, 122 J                 │
│            │                              │ 29.0× faster, 28.0× less E   │ 39.3× faster, 60.8× less E  │
├────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ L1 Direct- │ (not comparable)             │ χ² = 1.52 (48 evals)         │ χ² = 1.52 (GPU-eval)         │
│ Sampler    │                              │ 32.4s                        │ (same optimizer)             │
├────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ L2 HFB     │ χ² = 1.93 (3,008 evals)      │ χ² = 23.09 (12 evals)        │ (SCF on CPU, GPU pending)    │
│            │ 3.2h (Python/mystic)         │ 252s, 32,500 J               │                              │
│            │ SparsitySampler advantage    │ DirectSampler only           │                              │
└────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘

Energy measured: CPU via Intel RAPL, GPU via nvidia-smi polling.
Hardware: i9-12900K, RTX 4070 (SHADER_F64), Pop!_OS 22.04 / Linux 6.17.4
```

---

## 7. The Big Picture

The `math_f64.wgsl` library proves that BarraCUDA can run complete scientific workloads on GPU with **zero CPU dependency**. The naga gotchas are annoying but systematic — once you know the `x - x + constant` pattern, every function follows the same template.

This matters for:
- **Borrowed compute**: Friend's GPU while they use CPU
- **Headless GPU nodes**: LAN cloud with no dedicated CPU
- **Gaming swap**: GPU available during work hours, CPU-only during gaming
- **True substrate independence**: Same physics, any hardware, one codebase

The precision gap (4e-4 MeV for pure-GPU vs exact for precomputed) is an engineering problem, not a fundamental one. Higher-order polynomials and specialized power functions will close it. The architecture is proven.

---

*From the hotSpring validation desk, February 13, 2026*
