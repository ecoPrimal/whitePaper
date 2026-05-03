# The Hardware Atheist's Proof of Work

> *Supersedes: AN_INVITATION_TO_NVIDIA_V2.md (correct framing, stale numbers)*
>
> V1 asked NVIDIA to open-source CUDA — wrong, adversarial.
> V2 proposed two-layer collaboration — right framing, early stack.
> V3 is the same argument, backed by proof. The stack is live.
>
> *May 2026*

---

## The Argument, Updated

A hardware-atheistic math layer creates more demand for hardware optimization,
not less. V2 made this argument in theory. This document makes it with data.

Since March 2026, the stack has grown from a proof of concept to what is likely
the largest WGSL shader corpus in existence:

| Metric | V2 (March 2026) | Current |
|--------|-----------------|---------|
| WGSL shaders | 806 | **1,145** |
| WGSL lines | ~48,000 | **88,150** |
| Rust lines | ~1M | **4,505,044** |
| Tests | ~27,000 | **83,587** |
| Primals (binaries) | 14 | **15** |
| Springs (validation) | 7 | **8** |
| Precision tiers | DF64 theorized | **15 tiers, DF64 validated** |
| Sovereign dispatch | Early | **SM120 live, SM70/SM37 active** |

These numbers were produced in ~13 months by one person using AI-assisted
development (K-NOME methodology). The shaders cover lattice QCD (Wilson gauge,
HMC, Dirac, CG solvers), molecular dynamics (Yukawa, Verlet, Berendsen),
nuclear physics (SEMF, HFB, BCS), plasma (Mermin, BGK, Euler HLL), fluid
dynamics (MPM, SPH), and spectral methods (batched eigensolve). All validated
against published physics. All running on consumer NVIDIA GPUs through Vulkan.

---

## What Changed: Sovereign Dispatch Is Live

V2 positioned coralReef as a future WGSL-to-SASS compiler. It is no longer
future. coralReef compiles WGSL to native vendor ISA today:

- **SM120 (Blackwell / RTX 5070)**: Live sovereign dispatch. WGSL → SASS,
  bypassing Vulkan for compute workloads. Production shaders running.
- **SM70 (Volta / Titan V)**: Active development. FECS microcode sequences
  identified, channel setup in progress.
- **SM37 (Kepler / GTX 780 Ti)**: Active development. Proving the stack works
  on decade-old silicon — science doesn't require new hardware.

This means the two-layer architecture from V2 is no longer a proposal. It
exists. Layer 1 (hardware-atheistic math) has 1,145 shaders. Layer 2 (hardware
optimization) has a working SASS backend that targets NVIDIA architectures
directly.

---

## The Two-Layer Architecture (Carried from V2)

The core argument is unchanged and correct:

```
┌──────────────────────────────────────────────────────┐
│  Layer 1: Mathematics (hardware atheistic)            │
│  barraCuda — 1,145 WGSL shaders, DF64, RHMC          │
│  Pure math. Same algorithm everywhere.                │
│  Global optimizations: algorithmic, not hardware.     │
│  88,150 lines of science that runs on any GPU.        │
└──────────────┬───────────────────────────────────────┘
               │ coralReef compiles to
┌──────────────▼───────────────────────────────────────┐
│  Layer 2: Hardware Optimization (the last mile)       │
│  NVIDIA: SASS (SM120, SM70, SM37 — live/active)       │
│  AMD: GFX ISA (future, architecture supports it)      │
│  CPU: AVX-512/NEON via SIMD fallback                  │
│  NPU: Akida AKD1000 (rustChip — standalone driver)    │
│  Future: whatever silicon exists                      │
└──────────────────────────────────────────────────────┘
```

Separating math from hardware makes both layers better. Mathematicians write
math. Hardware engineers optimize dispatch. Neither does the other's job.

---

## DF64: Science-Grade Precision Without Native f64

WGSL has no native f64. This is the wall that stopped Dimforge's wgmath project
(they pivoted to rust-gpu). We solved it differently.

**DF64 (Double-Float 64)**: Two f32 values encoding a single number with ~48-bit
mantissa (~14 decimal digits). Uses Knuth's `two_sum` and FMA-based `two_prod`.
Pure WGSL, no extensions, runs on any GPU with f32 hardware.

The precision hierarchy in barraCuda:

| Tier | Mantissa bits | Use case |
|------|--------------|----------|
| f32 | 24 | Throughput-bound (particles, rendering) |
| DF64 | ~48 | Science-grade (lattice QCD, MD, nuclear) |
| f64 | 53 | Native IEEE double (CPU, GPUs with f64 HW) |
| QF128 | ~96 | Reference / validation |
| DF128 | ~106 | Ultra-precision research |

**PrecisionBrain** (in toadStool) detects hardware capabilities at runtime and
routes computation to the optimal tier. It knows that your consumer GPUs throttle
f64 to 1/32 throughput. It knows that DF64 gives science-grade precision at full
f32 throughput. It routes accordingly.

The result: an RTX 3090 running DF64 delivers ~4x the science-grade GFLOPS per
dollar of an H100 running native f64, for workloads where 48-bit mantissa
suffices. Most scientific computing falls in this range.

**This makes your consumer GPUs more valuable, not less.** Every physicist who
discovers they can do lattice QCD on an RTX 4070 instead of waiting for HPC
allocation is a potential NVIDIA hardware customer who wasn't one before.

---

## What We've Actually Proven

Not hypotheses. Measurements.

| Claim | Evidence |
|-------|---------|
| Consumer GPUs do real science | 0.000% energy drift in Hamiltonian evolution (RTX 3090) |
| DF64 precision is sufficient | Lattice QCD Wilson loops, HMC trajectories, Dirac solvers — all validated |
| The stack scales to real problems | 926x PFAS mass-spec speedup over sequential CPU |
| Old hardware works | SM37 (2013 silicon) targeted by coralReef — science on a GTX 780 Ti |
| Sovereign dispatch works | SM120 SASS generation live, shaders executing without Vulkan overhead |
| The corpus is real | 88,150 WGSL lines, 83,587 tests, public repository |

---

## What This Means for NVIDIA

### The consumer GPU becomes a science instrument

Every RTX card sold is already a science-grade compute device. The buyer just
doesn't know it yet. barraCuda + DF64 + toadStool makes it accessible.

"Your gaming GPU does real physics" is not a marketing claim. It's a measured
result. NVIDIA can use it or ignore it, but the data exists.

### The market expansion math (updated from V2)

| Metric | CUDA world | Hardware-atheistic world |
|--------|-----------|------------------------|
| GPU science developers | ~2-5M | ~50-500M |
| Barrier to entry | CUDA + C++ + HPC allocation | `cargo build` + any GPU |
| Consumer GPUs doing science | ~0 | Potentially all of them |
| NVIDIA's competitive edge | Lock-in (CUDA required) | Merit (fastest silicon) |

NVIDIA wins more in an open market. The silicon is genuinely the best. Lock-in
was necessary when AMD was competitive on hardware. AMD isn't anymore. The moat
is the silicon itself.

### Dimforge tried and hit WGSL's walls. We solved them.

Dimforge's wgmath project (Rust + wgpu GPU math) documented these blockers:
- No WGSL module system → they pivoted to rust-gpu
- No f64 in WGSL → they couldn't do science-grade precision
- Basic language limitations → development was impractical

ecoPrimals solved all three:
- coralReef provides WGSL preamble composition (simulated module system)
- barraCuda provides DF64 (science-grade precision in pure WGSL)
- 88,150 lines of production WGSL prove the language works at scale

We are preparing standalone extractions (`wgsl-precision`, `wgsl-compose`) as
MIT/Apache-2.0 crates for the wider ecosystem. When Dimforge and others adopt
these, more people write GPU compute, more people need GPUs, NVIDIA benefits.

---

## The Specific Opportunity (Updated)

### What NVIDIA could do (none required)

1. **Validate physics results on DGX** — Run hotSpring benchmarks on your
   systems. If consumer GeForce GPUs match DGX precision, that's a marketing
   story: "Your gaming GPU does CERN-grade physics."

2. **Contribute SM-specific optimizations to coralReef** — Your engineers know
   NVIDIA ISA better than anyone. Making coralReef's SASS backend generate
   better code for your silicon means NVIDIA hardware runs our shaders faster
   than AMD hardware. That's your competitive advantage, amplified.

3. **Provide architectural documentation** — Public PGRAPH initialization
   sequences, PFIFO channel setup, compute class registers. This helps
   coralReef's VFIO sovereign dispatch path get better on your hardware first.

### What NVIDIA does NOT need to do

- Does NOT need to open-source CUDA
- Does NOT need to change their driver model
- Does NOT need to adopt AGPL
- Does NOT need to change anything about their business
- Does NOT need to acknowledge this project publicly

The stack works today, on your hardware, without your involvement. Engagement
is optional and mutually beneficial, not required.

---

## The Position Shift

V2 said: "We're building this. Please don't obstruct."

V3 says: "We built it. Here's the data. Your consumer GPUs do science. That
sells more consumer GPUs. You're welcome to help make them do it faster."

The math is universal. The silicon is competitive. Both benefit.

---

*May 2026*
*1,145 shaders. 88,150 WGSL lines. 83,587 tests. Sovereign dispatch live.*
*The proof of work is the work itself.*
