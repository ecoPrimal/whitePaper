# From CERN to Consumer GPU — Lattice QCD in Pure Rust

**Author:** Kevin Mok, syntheticChemistry / Michigan State University
**Date:** March 2026
**Repository:** [github.com/syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring) (AGPL-3.0)

---

## Summary

In 10 days (February 18–28, 2026), a single developer built a lattice QCD
pipeline from scratch in Pure Rust — reproducing quenched SU(3)
deconfinement on a 32⁴ lattice (β_c = 5.69, matching literature to three
significant figures), then extending to dynamical fermion QCD with NPU
adaptive steering on consumer hardware costing ~$0.60/run.

The pipeline evolved through five stages, each building on the last:

| Stage | What | Key Result |
|-------|------|------------|
| 1. CERN-class physics | Reproduce Bazavov/HotQCD lattice QCD | Same physics, $3.5M machine → $1,500 GPU |
| 2. Python baseline | Sarkas MD, nuclear EOS in Python | 86/86 checks, 5 upstream bugs found |
| 3. Rust CPU | Pure Rust port, zero Python runtime | 15.7× faster than Python |
| 4. Rust GPU (BarraCUDA) | WGSL shaders via Vulkan, vendor-agnostic | 478× speedup, 44.8× less energy |
| 5. Brain architecture | NPU + dual GPU + CPU concurrent pipeline | 2.5× more useful statistics at same cost |

No CUDA. No Fortran. No Python runtime. No vendor lock-in. The same WGSL
shaders run on NVIDIA, AMD, and Intel GPUs.

---

## The Five Stages

### Stage 1: The Physics — What CERN Runs

Lattice QCD simulates the strong nuclear force by discretizing spacetime
onto a lattice and evolving the gauge field with Hybrid Monte Carlo (HMC).
The deconfinement phase transition — where quarks become free at high
temperature — is detected by a peak in the plaquette susceptibility χ at
the critical coupling β_c.

This is traditionally done on purpose-built supercomputers:

| Machine | Year | FP64 | Cost | This calculation |
|---------|------|:----:|:----:|:----------------:|
| QCDSP (Columbia) | 1998 | 0.6 TFLOPS | $3.5M | ~7 hours |
| QCDOC | 2004 | 10 TFLOPS | $5M | ~25 min |
| BlueGene/L (1 rack) | 2005 | 0.46 TFLOPS | $1.5M | ~11 hours |
| **RTX 3090 (this work)** | **2026** | **3.24 TFLOPS** | **$1,500** | **14.2 hours** |

The physics is identical — the susceptibility peak at β = 5.69 matches the
known β_c ≈ 5.692 to three significant figures. The cost is 2,300× lower.

### Stage 2: Python Baseline (Phase A)

Every physics domain starts with a Python reproduction of published work.
For hotSpring, this meant reproducing the Murillo Group's Sarkas molecular
dynamics suite, two-temperature models, surrogate learning, and nuclear
equation of state calculations.

| Domain | Papers | Checks | Key Finding |
|--------|:------:|:------:|-------------|
| Yukawa MD (Sarkas) | 6 | 60/60 | 0.000% energy drift at N=10,000 |
| Nuclear structure (AME2020) | 6 | 86/86 | 2,042 nuclei, L1/L2/L3 models |
| Spectral theory | 4 | 45/45 | Anderson, Hofstadter, Lanczos |
| Lattice QCD | 6 | 39/39 | β_c = 5.69, SU(3) pure gauge |

5 upstream bugs were found and fixed during Python reproduction — the
independent validation caught numerical issues in existing published code.

**Benchmark:** Nuclear EOS L1 in Python: 1,143 μs/eval, 5,648 J total energy.

### Stage 3: Rust CPU — The Standard Pipeline

The Python baselines are ported to Pure Rust: zero runtime dependencies,
no Python, no C FFI, no nalgebra. The Rust implementations must match
Python outputs to full floating-point precision (bit-exact where possible,
1e-12 tolerance otherwise).

**Benchmark:** Nuclear EOS L1 in Rust CPU: 72.7 μs/eval — **15.7× faster
than Python**, same numerical results.

This is the "standard pipeline" — the Pure Rust CPU tier. It's the
portable, auditable, reproducible layer that runs anywhere Rust compiles.
Every GPU and NPU result is validated against it.

### Stage 4: BarraCUDA GPU — Vendor-Agnostic Acceleration

BarraCUDA is a GPU compute engine built on WGSL shaders dispatched via
Vulkan through `wgpu`. No CUDA, no ROCm, no vendor SDK. The same shader
binary runs on NVIDIA, AMD, and Intel GPUs.

| | Python | Rust CPU | BarraCUDA GPU |
|--|:------:|:--------:|:-------------:|
| **L1 Nuclear EOS** | 1,143 μs/eval | 72.7 μs/eval | **39.7 μs/eval** |
| **Speedup vs Python** | 1× | 15.7× | **28.8×** |
| **Energy** | 5,648 J | 360 J | **126 J** |
| **Energy reduction** | 1× | 15.7× | **44.8×** |

For Yukawa MD at N=10,000 (80,000 steps), the full GPU run completes in
3.66 hours at $0.044 in electricity — with 0.000% energy drift.

#### DF64: Unlocking FP32 Cores for Double Precision

Consumer NVIDIA GPUs throttle native f64 to 1:64 of f32 throughput. The
RTX 3090 has 10,496 FP32 cores but only 164 FP64 units. BarraCUDA's DF64
(double-float, Dekker 1971) uses the FP32 cores for f64-equivalent math:

| | Native f64 | DF64 on FP32 Cores |
|--|:----------:|:------------------:|
| **Throughput** | 0.33 TFLOPS | **3.24 TFLOPS** |
| **Precision** | ~16 digits | ~14 digits |
| **Speedup** | 1× | **9.9×** |
| **HMC trajectory (32⁴)** | 15.5 s | **7.6 s** |

The 2-digit precision loss has no measurable effect on any physics
observable — plaquette, Polyakov loop, susceptibility, acceptance rate, and
energy conservation are statistically identical.

#### Standard Pipeline vs BarraCUDA GPU

| Aspect | Standard (Rust CPU) | BarraCUDA GPU |
|--------|:-------------------:|:-------------:|
| **Language** | Pure Rust | Rust + WGSL shaders |
| **Execution** | Any CPU | GPU via wgpu/Vulkan |
| **Precision** | f64 native | f64 native or DF64 hybrid |
| **Vendor lock-in** | None | **None** (NVIDIA, AMD, Intel) |
| **CUDA required** | No | **No** |
| **Fortran required** | No | No |
| **Auditability** | Full source | Full source + shaders |
| **Cost (lattice QCD)** | Hours | **Minutes** (at scale) |
| **Validated on** | All platforms | RTX 3090, RTX 4070, Titan V |

Both tiers produce identical physics. The standard pipeline is the
verification layer — portable, auditable, bit-exact. BarraCUDA is the
acceleration layer — same math, 10–480× faster, vendor-agnostic.

### Stage 5: Brain Architecture — NPU-Steered Concurrent Pipeline

The final stage treats the workstation as a heterogeneous brain — four
hardware layers running concurrently, each handling a different cognitive
function:

```
┌─────────────────────────────────────────────────────┐
│                biomeGate Brain                      │
│                                                     │
│  CPU (256 GB, 32-core)     Titan V (12 GB HBM2)    │
│  "Prefrontal Cortex"       "Pre-motor Cortex"       │
│  Anderson 3D proxy          Quenched pre-therm for  │
│  Z(3) Potts MC              NEXT β while 3090 runs  │
│         │                   current β               │
│         ▼                          │                │
│  ┌─────────────────────────────────────────┐        │
│  │  NPU (BrainChip AKD1000) — "Cerebellum"│        │
│  │  15-head ESN: steering, monitoring,     │        │
│  │  CG residual stream, phase detection    │        │
│  │  341 μs inference, ~30 mW              │        │
│  └─────────────────┬───────────────────────┘        │
│                    │ interrupts                      │
│                    ▼                                 │
│  ┌─────────────────────────────────────────┐        │
│  │  RTX 3090 (24 GB) — "Motor Cortex"     │        │
│  │  Full dynamical HMC with CG solver     │        │
│  │  Streams residuals to NPU every N iters │        │
│  └─────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────┘
```

The NPU determines where the GPU spends its next 42 minutes of compute at
a cost ratio of 1.4 ms / 2,520,000 ms = 0.00006%.

---

## Production Results

### Quenched SU(3): 32⁴ Lattice (Runs 1–2)

Two production-scale β-scans on 1,048,576 lattice sites:

| | Run 1 (native f64) | Run 2 (DF64 + NPU) |
|--|:---:|:---:|
| **β points** | 12 (uniform grid) | 10 (3 seed + 7 NPU-steered) |
| **Total measurements** | 2,400 | **5,900** |
| **Thermalization saved** | 0% | **63%** |
| **Wall time** | 13.6 hours | 14.2 hours |
| **Electricity** | $0.58 | $0.61 |
| **β_c** | 5.69 | 5.69 |
| **Peak χ** | 52.87 | 32.41 |

Same wall time. Same cost. Run 2 produces **2.5× more measurement
statistics** in the transition region while saving 63% of thermalization
compute — because the NPU detects convergence early and steers the GPU to
spend time on measurements instead.

### Dynamical Fermion QCD: 8⁴ Lattice (Run 3)

First dynamical fermion production scan on consumer GPU. Staggered quarks
(N_f = 1, m = 0.1) with Conjugate Gradient solver. NPU-steered.

| Metric | Value |
|--------|-------|
| Lattice | 8⁴ (4,096 sites) |
| β points | 17 (4 seed + **13 NPU-inserted**) |
| Total trajectories | 1,071 |
| Wall time | 11.96 hours |
| Acceptance | 56.6% |
| Electricity | ~$0.50 |
| Transition type | **Smooth crossover** (no first-order jump) |
| β_c shift | ~5.0–5.5 (down from quenched 5.692) |

The NPU expanded a 4-point seed scan to 17 points autonomously, using a
"bracket and fill" strategy it learned from quenched training data — it
was never explicitly programmed to bracket. The plaquette curve shows a
smooth crossover, confirming the expected qualitative change from adding
dynamical quarks.

### NPU Performance

| Function | Accuracy | Latency | Energy vs CPU |
|----------|:--------:|:-------:|:-------------:|
| Thermalization detection | 87.5% | 341 μs | 9,017× less |
| Rejection prediction | 80.4% | 341 μs | 9,017× less |
| Phase classification | 100% (n ≥ 10) | 341 μs | 9,017× less |
| β_c regression | ε = 0.0098 | 341 μs | 9,017× less |
| Adaptive β steering | 13/17 points steered | 341 μs | 9,017× less |

Total NPU overhead across the entire dynamical run: **~0.35 seconds** out
of 11.5 hours of GPU compute (0.00085%).

---

## Development Velocity

| Date | Event | Lattice |
|------|-------|---------|
| Feb 18 | Quenched Run 1 (native f64) — β_c = 5.69 | 32⁴ |
| Feb 20 | Quenched Run 2 (DF64 + NPU) — 2.5× more stats | 32⁴ |
| Feb 24 | Dynamical HMC first attempt — CG too slow | 32⁴ |
| Feb 25 | Fermion force fix — first dynamical trajectories | 8⁴ |
| Feb 26 | dt/n_md parameter sweep — stability mapped | 8⁴ |
| Feb 27 | Production launched — 17 β points overnight | 8⁴ |
| **Feb 28** | **Production complete** — 1,071 trajectories | **8⁴** |
| Feb 28 | Physics proxy pipeline — 171 training points in 67 s | — |
| Feb 28 | Brain architecture implemented and validated | 8⁴ |
| Mar 1 | NPU parameter control — closed-loop dt/n_md adaptation | 8⁴ |

**Quenched → dynamical: 7 days. Dynamical → brain architecture: 1 day.**

---

## The Pipeline Applied Across Domains

The same BarraCUDA pipeline (Python baseline → Rust CPU → Rust GPU → NPU)
is not specific to lattice QCD. It has been validated across multiple
scientific domains within the public spring repositories:

| Spring | Domain | Papers | Checks | Key Result |
|--------|--------|:------:|:------:|------------|
| [hotSpring](https://github.com/syntheticChemistry/hotSpring) | Plasma physics, lattice QCD, spectral theory, NPU | 22 | 700+ | 32⁴ β_c = 5.69, dynamical QCD |
| [wetSpring](https://github.com/syntheticChemistry/wetSpring) | Life science, analytical chemistry | 30+ | 7,083+ | 1,077× GPU speedup (spectral cosine) |
| [airSpring](https://github.com/syntheticChemistry/airSpring) | Precision agriculture, biophysics | 20+ | 3,123+ | CytokineBrain reservoir computing |
| [neuralSpring](https://github.com/syntheticChemistry/neuralSpring) | ML primitives, structure prediction | 10+ | 3,200+ | 83.6× faster than Python (geomean) |
| [groundSpring](https://github.com/syntheticChemistry/groundSpring) | Measurement noise, uncertainty | 10+ | 236+ | Anderson spectral, transport |
| **Total** | | **70+** | **14,300+** | |

Every spring follows the same pattern: reproduce published work in Python,
port to Rust, validate on GPU, add NPU where applicable. The lattice QCD
progression described above is one instance of a general methodology.

---

## Software Stack

| Layer | Technology |
|-------|-----------|
| Language | Rust (stable, zero runtime dependencies) |
| GPU dispatch | wgpu + Vulkan (vendor-agnostic WGSL shaders) |
| Shaders | 628 WGSL files, 48,698 lines (BarraCUDA) |
| NPU driver | BrainChip AKD1000 via PCIe → Rust adapter |
| Precision | f64 native + DF64 hybrid (Dekker 1971) |
| License | AGPL-3.0 |

### Hardware

| Component | Role | Cost |
|-----------|------|:----:|
| RTX 3090 (24 GB) | Primary GPU — HMC, MD, spectral | $1,500 |
| RTX 4070 (12 GB) | Validation GPU — MD, diversity | $600 |
| Titan V (12 GB HBM2) | Pre-motor — quenched pre-therm | $800 (used) |
| BrainChip AKD1000 (×3) | NPU — ESN inference, steering | $300 ea |
| CPU (32-core, 256 GB) | Proxy pipeline, coordination | — |
| **Total system** | | **~$4,500** |

For reference, QCDSP cost $3.5M in 1998 for equivalent physics.

---

## What This Demonstrates

1. **The standard pipeline (Pure Rust CPU) is the verification layer.**
   Portable, auditable, bit-exact against Python. Runs anywhere.

2. **BarraCUDA GPU is the acceleration layer.** Same math, 10–480× faster,
   vendor-agnostic. No CUDA lock-in.

3. **The NPU is the intelligence layer.** 341 μs inference steers hours of
   GPU compute. 9,017× less energy than CPU for the same predictions.

4. **The brain architecture composes all three.** CPU (cheap proxies), dual
   GPU (concurrent simulation), and NPU (real-time steering) run
   simultaneously — each layer informs the one above it.

5. **Development velocity is real.** Quenched to dynamical QCD in 7 days.
   Dynamical to brain architecture in 1 day. All public, all reproducible.

---

**Kevin Mok**
Michigan State University
[syntheticChemistry](https://github.com/syntheticChemistry) on GitHub
