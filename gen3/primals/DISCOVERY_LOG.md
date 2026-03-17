# Discovery Log — How We Found What We Needed

## What This Is

The primals and springs didn't follow a roadmap. They followed a methodology that could be called **capability hunting**: analyze a need, probe the environment for capabilities that aren't advertised, experiment until you understand what's actually there. Then use it.

This is the opposite of the monolithic SDK approach, where a vendor (NVIDIA/CUDA, Intel/oneAPI) decides what your hardware can do and you write code within those boundaries. In capability hunting, the hardware's actual capabilities are the starting point, and you discover the boundaries empirically.

This document logs the key discoveries that shaped the system. These are not design decisions — they're findings.

---

## Timeline Context

| Period | Focus | What Was Happening |
|--------|-------|-------------------|
| Months 1–8 | Primals | BearDog, NestGate, Songbird, Squirrel, ToadStool, biomeOS evolving under Pure Rust constraint. BarraCuda growing from ML primitives through FHE to 628 shaders. No science validation yet. |
| Month 9 | ToadStool + BarraCuda maturation | Shader-first architecture solidified. GPU dispatch, f64 pipeline, mixed-substrate (GPU/NPU/CPU). Still no springs. |
| Months 9–10 (~2 weeks of spring work) | Springs | hotSpring, airSpring, wetSpring, groundSpring, neuralSpring. 2,882 checks across 80+ papers. All on single-machine hardware — not the full NUCLEUS basement HPC. |

The springs are the youngest part of the system. ToadStool/BarraCuda had months of independent evolution before the springs existed. The springs then became the selection pressure that drove specific shader development — the scientific needs pulled BarraCuda's evolution in directions the ML/FHE origins wouldn't have reached.

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

hotSpring's PPPM electrostatics method requires FFT for charge mesh computation. BarraCuda had NTT (Number Theoretic Transform) from the FHE work.

### The Discovery

The NTT's Cooley-Tukey butterfly structure IS the FFT's skeleton. The main compute kernel — stage indexing, stride computation, block decomposition, twiddle lookup — is character-for-character identical. See `fhe_ntt.wgsl` (263 lines) vs `fft_1d.wgsl` (186 lines).

The FFT is shorter because complex floats (`vec2<f32>`) map to GPU hardware natively, while NTT uses U64 emulation from u32 pairs (WGSL lacks native u64). The adaptation simplified the organism.

### The Implication

No one designed BarraCuda for physics. The FHE constraint selected for the Cooley-Tukey butterfly — a mathematical structure that was universal. Switching from modular arithmetic to complex arithmetic preserved 80%+ of the code. The cryptographic constraint accidentally produced the physics engine.

---

## Discovery 3: Mixed-Substrate Pipelines (GPU → NPU → CPU)

### The Need

hotSpring's lattice QCD phase detection could benefit from neuromorphic inference — classify lattice configurations as confined/deconfined using an Echo State Network on the AKD1000 NPU.

### The Discovery

`hotSpring/metalForge/` contains the mixed-substrate experiments. The pipeline:

1. **GPU** (BarraCuda): Generate lattice configurations, compute observables
2. **NPU** (AKD1000): ESN reservoir computing for phase classification
3. **CPU**: Validation and statistical analysis

The NPU achieves 9,017× less energy than equivalent CPU inference for the phase classification task. The quantization cascade (f64 → f32 → int8 → int4) tracks precision loss at each stage.

### The Implication

Capability hunting across substrate boundaries. The AKD1000 NPU ($300) was probed for what it could actually do — not what Akida's SDK advertised. The mixed pipeline emerged from asking "what if the phase detection step runs on the NPU?" and experimenting until the answer was clear.

This is the methodology: analyze a need (phase classification), identify a candidate capability (NPU inference), experiment (ESN on AKD1000), measure (9,017× energy reduction), and validate (100% test accuracy, f32 parity within 2.8e-7).

---

## Discovery 4: WGSL Shader-First Architecture

### The Need

BarraCuda needed to be vendor-agnostic (no CUDA, no ROCm, no oneAPI). The Pure Rust constraint eliminated all C-based GPU frameworks.

### The Discovery

`wgpu` (Rust bindings for the WebGPU specification) compiles WGSL shaders to Vulkan SPIR-V, Metal MSL, or DirectX HLSL. A single WGSL shader runs identically on NVIDIA, AMD, and Intel GPUs.

The shader-first architecture means: write the math in WGSL, dispatch from Rust, validate on any GPU. The 628 shaders represent 48,698 lines of portable GPU code that doesn't depend on any vendor's proprietary toolchain.

### The Implication

By eliminating CUDA at the constraint level (Pure Rust directive), we were forced to discover that WebGPU/WGSL — originally designed for browser-based graphics — is a viable scientific computing platform. The f64 extension, storage buffers, and compute shader workgroups provide everything needed for MD, lattice QCD, spectral methods, and ML inference.

---

## Discovery 5: The `ring` C Dependency and Tower Atomic

### The Need

TLS for secure communication between machines. Every networking library in Rust uses the `ring` crate for TLS handshakes, key exchange, and hashing.

### The Discovery

`ring` wraps BoringSSL — Google's fork of OpenSSL. It's C code. Any Rust project that uses `ring` for TLS has a C dependency hiding inside what looks like a Rust dependency. The Pure Rust constraint was dead on arrival.

This was found when Songbird's TLS implementation was audited for C dependencies. The audit showed: `ring` → BoringSSL → C compiler required → Pure Rust violated.

### The Solution: Tower Atomic

Instead of embedding crypto in Songbird (which would require `ring`), all cryptographic operations were delegated to BearDog via JSON-RPC over Unix sockets. BearDog uses `RustCrypto` crates — Pure Rust implementations of the same algorithms, no C. Songbird handles the TLS state machine and protocol logic, calling BearDog for every crypto operation.

The composition pattern:
```
HTTPS request → Songbird (protocol) → BearDog (crypto) → Response
```

Neither primal can do HTTPS alone. Together, they do it with zero C dependencies, zero unsafe blocks. This is the Tower Atomic — the foundational composition that every other atomic builds on.

### The Implication

The constraint didn't just find an alternative to `ring`. It forced a separation of concerns (protocol vs. crypto) that turned out to be architecturally superior. Songbird can upgrade its protocol handling without touching crypto. BearDog can upgrade its crypto algorithms without touching networking. The IPC boundary is a clean evolutionary interface between two independent lineages.

This is also why the convergent IPC pattern matters (Discovery 6 below): the JSON-RPC socket interface that Tower Atomic depends on was already present in every primal. The composition pattern was available because the constraint environment had already selected for it.

---

## Discovery 6: Convergent IPC Without Specification

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

## Discovery 7: Cross-Network Handshake (USB ↔ Pixel via nestgate.io)

### The Need

Two devices on completely separate networks needed to find each other and establish a cryptographic handshake: a USB LiveSpore on a desktop LAN and a Pixel 8a on its own mobile hotspot. No shared subnet, no port forwarding, no VPN.

### The Discovery

The Tower's rendezvous endpoint (`/api/v1/rendezvous/beacon`) combined with the BirdSong beacon protocol and the nestgate.io Cloudflare tunnel solved it:

1. Both devices POST encrypted BirdSong beacons to `api.nestgate.io` (Cloudflare QUIC tunnel → Tower:3492 in the basement)
2. Tower verifies lineage via BearDog (same `.family.seed` → same lineage hash)
3. Tower matches peers and returns connection info (STUN address, NAT type)
4. The 4-tier NAT traversal strategy negotiates a direct connection

The Tower never sees plaintext. Beacons are ChaCha20-Poly1305 encrypted. Slots expire in 5 minutes. The rendezvous is a blind matchmaker.

### The Implication

This is cross-architecture (x86_64 ↔ aarch64), cross-network (LAN ↔ mobile hotspot), with end-to-end encryption, on sovereign infrastructure (your domain, your tunnel, your machine). No rented TURN servers, no WebRTC relay services, no third-party signaling.

The same mechanism scales to the full basement HPC mesh: any device with the family seed can find any other device through the Tower, regardless of network topology. This is the bootstrap for NUCLEUS — the discovery and trust layer that allows covalent bonding across machines that can't see each other at the network level.

---

## Discovery 8: DF64 Core Streaming (FP32 Cores for Science)

### The Need

Consumer GPUs have f64 at 1:64 throughput (both CUDA and Vulkan). The Titan V has 1:2. But consumer GPUs have 5,000-10,000 FP32 cores sitting idle during f64 workloads.

### The Discovery

Double-float (DF64) arithmetic represents each f64 value as a pair of f32 values, computed on the FP32 cores. On an RTX 3090: **3.24 TFLOPS at 14-digit precision** — 9.9× the throughput of the same chip's native f64. The gauge force, plaquette, and kinetic energy shaders in lattice QCD HMC were converted to DF64. Result: 32⁴ production β-scan in **7.1 hours** (vs 13.6h FP64-only), with identical physics (deconfinement at β_c=5.69, matching known 5.692).

### The Implication

The hardware constraint (consumer GPU with throttled f64) forced exploration of double-float arithmetic. The FP32 cores were always there — they were just being used for the wrong thing. DF64 is the Taq analog for GPU precision: the capability existed in the silicon, hidden by the vendor's product segmentation. The constraint (Pure Rust, no CUDA) meant we needed to understand the hardware at the shader level, which made DF64 obvious once we looked.

---

## Discovery 9: Cross-Substrate ESN — GPU as Reservoir Computer

### The Need

The Echo State Network (ESN) was running on CPU (f64) and NPU (int4). Could a GPU run the reservoir update directly, and when would it make sense?

### The Discovery

The ESN WGSL shaders (`esn_reservoir_update.wgsl`, `esn_readout.wgsl`) already existed but had never been dispatched to GPU. Building the `GpuEsn` pipeline required adding f32 buffer management to `GpuF64` and handling a critical recurrent-network constraint: per-step GPU submit is mandatory (naive encoder batching fails because state at step t depends on step t-1).

**Scaling crossover at RS ≈ 512.** Below this, CPU wins (GPU dispatch overhead ~40μs + 3.5ms/step dominates). Above, GPU parallel matrix-vector wins: 8.2× at RS=1024. NPU streaming is 1000× faster than GPU for single-step inference (2.8μs vs 3,170μs).

### The Implication

Each substrate has a fitness niche:
- **NPU**: streaming inference (2.8μs/step, 30mW)
- **CPU**: small reservoirs and precision-critical readout
- **GPU**: large reservoirs (RS≥512) where parallelism overcomes dispatch overhead

This is ecological niche partitioning applied to silicon. The capability hunting methodology discovered the crossover point by measuring, not by design. No vendor SDK would have told us "use the NPU for RS<200, GPU for RS>512" — that emerged from the experiment.

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
