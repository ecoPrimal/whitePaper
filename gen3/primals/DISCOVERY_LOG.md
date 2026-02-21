# Discovery Log — How We Found What We Needed

## What This Is

The primals and springs didn't follow a roadmap. They followed a methodology that could be called **capability hunting**: analyze a need, probe the environment for capabilities that aren't advertised, experiment until you understand what's actually there. Then use it.

This is the opposite of the monolithic SDK approach, where a vendor (NVIDIA/CUDA, Intel/oneAPI) decides what your hardware can do and you write code within those boundaries. In capability hunting, the hardware's actual capabilities are the starting point, and you discover the boundaries empirically.

This document logs the key discoveries that shaped the system. These are not design decisions — they're findings.

---

## Timeline Context

| Period | Focus | What Was Happening |
|--------|-------|-------------------|
| Months 1–8 | Primals | BearDog, NestGate, Songbird, Squirrel, ToadStool, biomeOS evolving under Pure Rust constraint. BarraCUDA growing from ML primitives through FHE to 628 shaders. No science validation yet. |
| Month 9 | ToadStool + BarraCUDA maturation | Shader-first architecture solidified. GPU dispatch, f64 pipeline, mixed-substrate (GPU/NPU/CPU). Still no springs. |
| Months 9–10 (~2 weeks of spring work) | Springs | hotSpring, airSpring, wetSpring, groundSpring, neuralSpring. 2,882 checks across 80+ papers. All on single-machine hardware — not the full NUCLEUS basement HPC. |

The springs are the youngest part of the system. ToadStool/BarraCUDA had months of independent evolution before the springs existed. The springs then became the selection pressure that drove specific shader development — the scientific needs pulled BarraCUDA's evolution in directions the ML/FHE origins wouldn't have reached.

**The full basement HPC via NUCLEUS is not deployed yet.** All 2,882 science checks run on a single machine (RTX 4070, AKD1000 NPU, consumer hardware). The distributed deployment remains future work.

---

## Discovery 1: Consumer GPUs Are Science Chips (f64 via Vulkan)

### The Need

Computational plasma physics (hotSpring) requires f64 (double-precision) arithmetic. Molecular dynamics energy conservation, nuclear EOS fitting, lattice QCD plaquettes — all require 64-bit floating point. This is why institutional HPC uses NVIDIA A100/H100 ($10K–$30K): they have full f64 throughput.

### The Assumption

Consumer GPUs (RTX 4070, $600) have f64 at 1:64 throughput on CUDA — effectively useless for science. NVIDIA segments its product line: consumer chips do gaming (f32), compute chips do science (f64). This is pricing segmentation, not hardware limitation — the silicon often has the same f64 units, but CUDA throttles them.

### The Discovery

A Titan V was ordered on the assumption that a compute-class GPU was necessary for f64 science. While setting up the f64 pipeline for the Titan via Vulkan/WGSL (the Pure Rust constraint had already eliminated CUDA), we discovered:

**Vulkan's `SHADER_F64` extension exposes native f64 hardware on consumer GPUs at 1:2 throughput — not 1:64.**

The RTX 4070's f64 units exist in the silicon. CUDA throttles them to 1:64 to protect the compute-class product line. Vulkan doesn't. The `SHADER_F64` extension lets WGSL shaders use `f64` types that compile to native hardware double-precision instructions.

### The Implication

The $600 RTX 4070 does real science. Yukawa MD with 0.000% energy drift over 80,000 steps. Nuclear EOS with χ²/datum = 2.27. Lattice QCD plaquettes matching strong-coupling expansion. All at f64 precision, on a consumer GPU, through Vulkan — because the Pure Rust constraint eliminated CUDA and forced us to look.

**This is Taq polymerase again.** The constraint (no CUDA) forced exploration of an unfamiliar environment (Vulkan). The unfamiliar environment contained a capability (native f64 on consumer silicon) that the conventional approach (CUDA) actively hides. The constraint didn't just find a workaround — it found something better.

The Titan V is still useful (full f64 throughput is 1:1, not 1:2), but the discovery that consumer chips are viable for science at 1:2 changes the economics of computational science.

---

## Discovery 2: NTT → FFT Structural Identity

### The Need

hotSpring's PPPM electrostatics method requires FFT for charge mesh computation. BarraCUDA had NTT (Number Theoretic Transform) from the FHE work.

### The Discovery

The NTT's Cooley-Tukey butterfly structure IS the FFT's skeleton. The main compute kernel — stage indexing, stride computation, block decomposition, twiddle lookup — is character-for-character identical. See `fhe_ntt.wgsl` (263 lines) vs `fft_1d.wgsl` (186 lines).

The FFT is shorter because complex floats (`vec2<f32>`) map to GPU hardware natively, while NTT uses U64 emulation from u32 pairs (WGSL lacks native u64). The adaptation simplified the organism.

### The Implication

No one designed BarraCUDA for physics. The FHE constraint selected for the Cooley-Tukey butterfly — a mathematical structure that was universal. Switching from modular arithmetic to complex arithmetic preserved 80%+ of the code. The cryptographic constraint accidentally produced the physics engine.

---

## Discovery 3: Mixed-Substrate Pipelines (GPU → NPU → CPU)

### The Need

hotSpring's lattice QCD phase detection could benefit from neuromorphic inference — classify lattice configurations as confined/deconfined using an Echo State Network on the AKD1000 NPU.

### The Discovery

`hotSpring/metalForge/` contains the mixed-substrate experiments. The pipeline:

1. **GPU** (BarraCUDA): Generate lattice configurations, compute observables
2. **NPU** (AKD1000): ESN reservoir computing for phase classification
3. **CPU**: Validation and statistical analysis

The NPU achieves 9,017× less energy than equivalent CPU inference for the phase classification task. The quantization cascade (f64 → f32 → int8 → int4) tracks precision loss at each stage.

### The Implication

Capability hunting across substrate boundaries. The AKD1000 NPU ($300) was probed for what it could actually do — not what Akida's SDK advertised. The mixed pipeline emerged from asking "what if the phase detection step runs on the NPU?" and experimenting until the answer was clear.

This is the methodology: analyze a need (phase classification), identify a candidate capability (NPU inference), experiment (ESN on AKD1000), measure (9,017× energy reduction), and validate (100% test accuracy, f32 parity within 2.8e-7).

---

## Discovery 4: WGSL Shader-First Architecture

### The Need

BarraCUDA needed to be vendor-agnostic (no CUDA, no ROCm, no oneAPI). The Pure Rust constraint eliminated all C-based GPU frameworks.

### The Discovery

`wgpu` (Rust bindings for the WebGPU specification) compiles WGSL shaders to Vulkan SPIR-V, Metal MSL, or DirectX HLSL. A single WGSL shader runs identically on NVIDIA, AMD, and Intel GPUs.

The shader-first architecture means: write the math in WGSL, dispatch from Rust, validate on any GPU. The 628 shaders represent 48,698 lines of portable GPU code that doesn't depend on any vendor's proprietary toolchain.

### The Implication

By eliminating CUDA at the constraint level (Pure Rust directive), we were forced to discover that WebGPU/WGSL — originally designed for browser-based graphics — is a viable scientific computing platform. The f64 extension, storage buffers, and compute shader workgroups provide everything needed for MD, lattice QCD, spectral methods, and ML inference.

---

## Discovery 5: Convergent IPC Without Specification

### The Need

12 primals needed to communicate. JSON-RPC 2.0 over Unix sockets was an early choice for BearDog. No specification document mandated it for other primals.

### The Discovery

All 12 primals independently converged on:
- JSON-RPC 2.0 message format
- Unix domain socket transport
- Async Tokio runtime
- 4-tier socket discovery
- Capability advertisement on connect
- Structured error types (enum + Display)

This wasn't copied from a template. Each primal's IPC was written independently, solving the same problem under the same constraint (Rust + async + Unix sockets). The convergence is visible in the code: 12 different JSON-RPC parsers, 12 different socket handlers, 12 different error hierarchies — all structurally identical, all independently evolved.

### The Implication

This is what made the constrained evolution thesis visible. The convergence across 12 independent codebases, without a shared design document, is the computational analog of cephalization or camera eyes — independent lineages arriving at the same solution because the physics of the environment (memory safety, type contracts, IPC latency) rewards these structures.

---

## The Methodology: Capability Hunting vs. Monolithic SDKs

### Monolithic Approach (CUDA/PyTorch/TensorFlow)

1. Accept vendor's definition of hardware capability
2. Write code within SDK boundaries
3. Scale by buying more of the same vendor's hardware
4. Inefficiency is siloed inside the monolith — hidden by scale

### Capability Hunting Approach (ecoPrimals)

1. Analyze a specific need (f64 for MD, FFT for PPPM, NPU for classification)
2. Probe the hardware for actual capabilities (Vulkan `SHADER_F64`, AKD1000 ESN performance)
3. Experiment until you understand what's really there
4. Build the minimal shader/pipeline for the need
5. Validate against published science (springs)

The monolithic approach scales by adding resources. Capability hunting scales by understanding resources. The difference: a monolithic system that can't do f64 on a consumer GPU buys a $30,000 A100. A capability hunter discovers that the $600 GPU already has the hardware and uses Vulkan to access it.

This is resource hunting in the ecological sense: organisms don't build food — they find it, by probing their environment and adapting to what's available. The constraint (no CUDA, Pure Rust) forced us to probe the environment (Vulkan/WGSL) and discover resources (f64 on consumer GPUs) that the conventional approach would never have found.
