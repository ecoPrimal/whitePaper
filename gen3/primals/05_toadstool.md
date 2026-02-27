# ToadStool — Sovereign Compute (+ BarraCUDA)

## Identity

| Field | Value |
|-------|-------|
| Phase | 1 (Foundation) |
| Domain | GPU/CPU/NPU compute, hardware discovery, BarraCUDA math engine |
| Rust lines | 788,209 |
| Tests | 13,503 |
| Crates | 50+ |
| WGSL shaders (BarraCUDA) | 628 |
| WGSL lines | 48,698 |
| AGPL-3.0 | Yes |

## What It Is

ToadStool is the compute layer. Hardware discovery (GPU, NPU, CPU via sysfs/PCIe), workload dispatch, and the home of **BarraCUDA** — the vendor-agnostic GPU math engine that is the single largest subsystem in ecoPrimals.

ToadStool owns the hardware. BarraCUDA owns the math. Together they provide scientific computing on any GPU (NVIDIA, AMD, Intel) via WGSL/Vulkan, without CUDA dependency.

## Why It Exists

In gen1, Squirrel handled both job scheduling and compute execution. As the GPU workloads grew more complex (molecular dynamics, lattice QCD, neural network inference), the compute layer needed its own primal.

ToadStool was split from Squirrel to own the hardware-specific concerns: GPU detection, driver compatibility, memory management, workload queuing. Squirrel kept the AI-specific logic (model routing, MCP); ToadStool took the "run this computation on that hardware" responsibility.

## BarraCUDA — The Math Engine

BarraCUDA is **not a separate primal**. It is a crate within ToadStool — the largest crate, with 792 Rust source files and 628 WGSL shaders.

### What BarraCUDA Does

BarraCUDA provides mathematical operations as WGSL shader pipelines:

| Domain | Operations | Spring Validation |
|--------|-----------|-------------------|
| Linear algebra | GEMM, eigensolvers, SVD, LU, QR | hotSpring, neuralSpring |
| FFT/NTT | Complex FFT (f32, f64), NTT (FHE) | hotSpring (PPPM) |
| Physics | Yukawa force, Velocity Verlet, PBC | hotSpring (MD) |
| Statistics | Reduction, histogram, moments | wetSpring, groundSpring |
| ML | Attention, LayerNorm, LSTM cell, ReLU | neuralSpring |
| Special functions | erfc, Bessel, Gamma | hotSpring, wetSpring |

### The NTT → FFT Evolution

BarraCUDA's NTT (Number Theoretic Transform) was evolved for fully homomorphic encryption — polynomial multiplication in Z_q. When hotSpring needed FFT for plasma physics (PPPM electrostatics), the NTT's Cooley-Tukey butterfly structure turned out to be the FFT's skeleton. The main compute kernel — stage indexing, stride computation, block decomposition, twiddle lookup — is character-for-character identical between `fhe_ntt.wgsl` (263 lines) and `fft_1d.wgsl` (186 lines).

No one designed BarraCUDA for physics. The cryptographic constraint selected for a mathematical structure that was universal.

### Vendor-Agnostic Design

BarraCUDA uses WGSL (WebGPU Shading Language) compiled through `wgpu` to Vulkan, Metal, or DirectX 12. The same shader runs on:

- NVIDIA (GeForce, Quadro, Tesla)
- AMD (Radeon, Instinct)
- Intel (Arc, integrated)

### The f64 Discovery

A Titan V was ordered on the assumption that consumer GPUs can't do double-precision science — NVIDIA's CUDA throttles consumer f64 to 1:64 throughput. While setting up the f64 pipeline for the Titan via Vulkan (CUDA was already eliminated by the Pure Rust constraint), we discovered: **Vulkan's `SHADER_F64` extension exposes native f64 on consumer GPUs at 1:2 throughput**.

The RTX 4070's f64 hardware exists in the silicon. CUDA throttles it to protect the compute-class product line. Vulkan doesn't. The $600 consumer GPU does real science: Yukawa MD with 0.000% energy drift, nuclear EOS with χ²/datum = 2.27, lattice QCD plaquettes — all at f64 precision.

The constraint (no CUDA) forced exploration of Vulkan, which revealed a capability the conventional approach actively hides. See [DISCOVERY_LOG.md](DISCOVERY_LOG.md) for the full story.

On hardware without native f64, BarraCUDA provides u64 emulation from u32 pairs (used in NTT for FHE).

## How It Connects

```
biomeOS ──compute.dispatch──▶ ToadStool
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
              ┌─────▼─────┐ ┌───▼────┐  ┌────▼────┐
              │BarraCUDA  │ │ Ollama │  │GPU Queue│
              │(628 WGSL) │ │(models)│  │(jobs)   │
              └───────────┘ └────────┘  └─────────┘

BearDog: security for job submission
Songbird: registration via ipc.register
NestGate: model storage
Squirrel: AI model inference requests
```

### Key Relationships

- **Squirrel** submits AI inference workloads to ToadStool for GPU execution
- **biomeOS** monitors ToadStool as part of the Node Atomic
- **BearDog** authenticates compute job submissions
- **NestGate** stores model weights that ToadStool loads for inference
- **Springs** (hotSpring, wetSpring, neuralSpring) validate BarraCUDA's kernels against published science

## Internal Architecture

50+ crates, the most of any primal:

**BarraCUDA core:**
- `barracuda` — Main crate: 628 WGSL shaders, Rust dispatch, pipeline management
- `barracuda-linalg` — Linear algebra ops (GEMM, eigensolvers)
- `barracuda-numerical` — FFT, NTT, integration, interpolation
- `barracuda-special` — Special functions (erfc, Bessel, Gamma)
- `barracuda-stats` — Statistical operations (reduction, moments)
- `barracuda-optimize` — Optimization (gradient descent, surrogate)
- `barracuda-pde` — PDE solvers (finite difference, spectral)

**ToadStool infrastructure:**
- `toadstool-core` — Hardware discovery, device management
- `toadstool-server` — JSON-RPC + tarpc server
- `toadstool-gpu` — GPU-specific runtime (wgpu, pipeline caching)
- `toadstool-neuromorphic` — NPU support (AKD1000, **live hardware validated**)
  - `akida-driver` — Pure Rust driver for BrainChip AKD1000/AKD1500 (Phase C sovereign: zero SDK)
  - wetSpring V60 (Feb 2026): 18.8K Hz inference, 37 MB/s DMA, online evolution at 136 gen/sec
- `toadstool-distributed` — Multi-node compute dispatch

## What Makes It Interesting

ToadStool is the largest primal by total Rust lines (788,209) because BarraCUDA is inside it. The 628 WGSL shaders represent ~49,000 lines of GPU code that runs identically on any vendor's hardware.

The springs are ToadStool's acceptance tests. hotSpring proves the physics kernels work (0.000% energy drift in Yukawa MD). wetSpring proves the biology kernels work (926× GPU speedup for spectral cosine). neuralSpring proves the ML kernels work (76.6× fused pipeline speedup for transformers). Every validated check is evidence that BarraCUDA's constrained evolution produced correct scientific computing.

The Ollama integration means ToadStool can serve both scientific compute (BarraCUDA) and AI inference (LLM) on the same GPU, with workload scheduling to avoid contention.
