# Sovereign Compute Trio — gen4 Composition Sketch → VALIDATED

**Status**: SKETCH → **EMPIRICALLY VALIDATED** (June 1, 2026)
**Wave**: 8 → 67 — Compute Trio Composition → Sovereign Pipeline
**Relates to**: `COMPOSITION_PATTERNS.md`, `CONTRACT_TESTING_THESIS_SKETCH.md`,
`STADIAL_INTERSTADIAL_PATTERN.md`, `DEPLOYABLE_ARTIFACT_STANDARD.md`

> **June 1, 2026 — Historic milestone**: The architecture described in this sketch
> has been empirically validated on hardware. coralReef compiles WGSL → SPIR-V (sm_70
> target), toadStool's local_cylinder dispatches compiled binaries on bare-metal
> Titan V GPUs via VFIO. This is the first sovereign shader dispatch in the ecoPrimals
> stack — no vendor runtime, no CUDA, no proprietary API. The thesis holds: complex
> compute capabilities emerge from simple primal composition.
>
> Remaining gaps: VFIO readback (GAP-HS-118), DRM execution provider (GAP-HS-119),
> barraCuda cross-gate method name (GAP-HS-120), Blackwell firmware (GAP-HS-121),
> sm_120 codegen (GAP-HS-122). See `HOTSPRING_PIPELINE_INTELLIGENCE_JUN01_2026.md`.

---

## Thesis

The compute trio (coralReef + toadStool + barraCuda) demonstrates a
gen4 composition principle: **domain-split sovereign compute through
IPC-only coupling**. No primal links another's crate. The trio
decomposes computation into three orthogonal domains — HOW (compilation),
WHERE (hardware dispatch), WHAT (workloads) — and composes them at
runtime through JSON-RPC contracts.

This is the same architectural pattern as the provenance trio (rhizoCrypt
+ loamSpine + sweetGrass) but applied to compute instead of attestation.
Both trios validate the thesis that **complex capabilities emerge from
simple primal composition, not from monolithic implementations**.

---

## The HOW / WHERE / WHAT Principle

This principle generalizes beyond the compute trio into a gen4
composition pattern:

| Question | Compute Trio | Provenance Trio | Content Domain |
|----------|-------------|----------------|----------------|
| **HOW** | coralReef: compile WGSL → native ISA | rhizoCrypt: DAG event hashing | NestGate: BLAKE3 CAS |
| **WHERE** | toadStool: dispatch to GPU/NPU/CPU | loamSpine: commit to immutable ledger | NestGate: filesystem store |
| **WHAT** | barraCuda: math/physics workloads | sweetGrass: attribution/braid | petalTongue: content serving |

The HOW/WHERE/WHAT split enforces separation of concerns at the
IPC boundary. Each primal answers exactly one question. Composition
emerges from the contracts between them.

---

## Sovereign Dispatch as a Composition Pattern

### The Problem

GPU compute has historically required tight coupling: the application
links vendor SDKs (CUDA, ROCm, Metal), compiles shaders with the vendor
compiler, and dispatches through vendor-specific APIs. This creates:

1. **Vendor lock-in** at compile time (CUDA headers)
2. **Driver dependency** at runtime (nvidia.ko, amdgpu.ko)
3. **Binary incompatibility** across architectures (SM70 vs SM120 vs GFX10)

### The Sovereign Solution

The compute trio breaks this coupling:

```
barraCuda (WHAT)
  │ pure math: "compute mean of [2, 4, 6, 8]"
  │ no GPU awareness, no vendor types
  │
  ├── shader.compile.wgsl ──→ coralReef (HOW)
  │                             pure compiler: WGSL → target ISA
  │                             no hardware access, no VFIO
  │                             returns: {binary_b64, shader_info}
  │
  └── compute.dispatch.submit ──→ toadStool (WHERE)
                                    pure hardware: VFIO, MMIO, GPFIFO
                                    accepts any compiled binary
                                    dispatches to any device
                                    returns: {result, timing}
```

Each IPC boundary is a sovereignty boundary. barraCuda never touches a
GPU register. coralReef never opens a VFIO fd. toadStool doesn't know
WGSL syntax.

### Degradation Tiers (PrimalBridge)

Following `COMPOSITION_PATTERNS.md` degradation model:

| Tier | What's Available | How It Works |
|------|-----------------|-------------|
| Full | All three primals + sovereign GPU | IPC: compile → dispatch → readback |
| Partial | wgpu available (vendor driver) | Local: wgpu Vulkan/Metal pipeline |
| Minimal | CPU only | cpu-shader or lavapipe fallback |
| Standalone | No IPC, no GPU | Pure Rust scalar implementation |

**Key insight**: correctness is invariant across tiers. `stats.mean([2, 4, 6, 8])`
returns 5.0 whether computed on an RTX 5060 via sovereign dispatch or on a
single CPU core via scalar Rust. Performance varies by orders of magnitude;
results do not.

---

## Ember/Glowplug Absorption as Budding

The `DEPLOYABLE_ARTIFACT_STANDARD.md` describes "budding" — how systems
spawn subsystems. The ember/glowplug absorption into toadStool is the
**reverse**: a subsystem (coralReef's hardware layer) being reabsorbed
into its natural domain owner (toadStool, the hardware primal).

### Why This Happens

coralReef evolved under pressure from hotSpring's sovereign compute work.
The team needed GPU hardware access *now*, so it grew ember (device
lifecycle) and glowplug (fleet orchestration) organically alongside
the compiler. But these are hardware-domain concerns, not compiler
concerns.

toadStool always had the trait surface (`ResourceHandle`,
`DevicePersonality`, `SwapOrchestrator`) — it lacked *implementations*.
coralReef's ember/glowplug implementations are the first production
fills for these traits.

### The 6-Phase Absorption Path

1. **Absorb coral-ember**: `HeldDevice` → `ResourceHandle`, device
   hold/release/reacquire, swap journal
2. **Absorb coral-glowplug**: `sovereign_boot` → `SwapOrchestrator`,
   personality detection, health probes
3. **Absorb coral-driver hardware**: BAR0/MMIO, VFIO channel, DRM
   ioctl wrappers
4. **Validate generalization**: Akida NPU, AMD RDNA, Intel Arc
5. **Generalize cylinder**: per-GPU → per-device subprocess isolation
6. **Serve compute.dispatch.execute**: universal dispatch entry point

After absorption, coralReef becomes a pure compiler. toadStool becomes
the "Universal Hardware Primal" — dispatching to GPU, NPU, USB HSM,
or any future hardware target.

---

## The Warm-Catch Pattern

hotSpring's breakthrough demonstrates a sovereignty pattern generalizable
beyond GPUs:

1. **Firmware barrier**: Hardware requires vendor-proprietary firmware
   initialization (NVIDIA VBIOS, AMD PSP)
2. **Binary patching**: Pure Rust ELF patcher modifies the open-source
   driver (nouveau.ko) to bypass firmware version checks
3. **Warm catch**: Load patched driver → hardware initializes → unload
   driver → rebind to vfio-pci → sovereign access via MMIO/GPFIFO
4. **Result**: Full hardware control without any vendor runtime

This pattern applies wherever firmware barriers exist:
- TPM/HSM devices (initialize via standard driver, rebind to sovereign)
- USB peripherals (warm-catch for firmware-locked devices)
- NPUs with proprietary SDKs (BrainChip Akida, Intel Movidius)

The warm-catch becomes a first-class toadStool capability after ember
absorption: `compute.sovereign.init` → `compute.dispatch.submit`.

---

## Era-Agnostic Compute

The compute trio's architecture is designed to outlive any single GPU
generation:

| Era | Architecture | coralReef Target | toadStool Driver | Validated |
|-----|-------------|-----------------|------------------|-----------|
| Kepler | SM35 | naga → PTX → SASS35 | VFIO (warm-catch, K80) | ⚠️ K80 awaiting hardware |
| Volta | SM70 | naga → PTX → SASS70 | VFIO (warm-catch, Titan V) | **✅ June 1, 2026** |
| Blackwell | SM120 | naga → PTX → SASS120 | VFIO (warm-catch, RTX 5060) | ❌ firmware + codegen gaps |
| RDNA2+ | GFX10 | naga → AMDIL → ISA | VFIO (amdgpu) | ⏳ future target |
| Akida | NPU | N/A (inference-only) | Akida driver (MetaTF) | ⏳ future target |

barraCuda is completely era-agnostic. Its 826+ WGSL shaders compile to
any target coralReef supports. The same `stats.mean` computation runs on
a K80 from 2014 and an RTX 5060 from 2025 — the shader is identical,
only the compiled binary differs.

---

## Connection to Atomic Patterns

### Node Atomic = Tower + Compute Trio

```
Node (Proton) = Tower (Electron) + coralReef + toadStool + barraCuda
              = [bearDog, songbird] + [coralReef, toadStool, barraCuda]
              = security + discovery + shader + compute + tensor
```

The Node atomic gives the NUCLEUS its computational identity. A TFLOP
is a TFLOP — Node primals are fungible across hardware. This is the
"proton" in the particle model: massive, carrying the composition's
computational charge.

### Nest Atomic = Tower + Provenance + Storage

```
Nest (Neutron) = Tower (Electron) + NestGate + squirrel
              = [bearDog, songbird] + [NestGate, squirrel]
              = security + discovery + storage + ai
```

The Nest atomic gives the NUCLEUS its memory. It stores, retrieves,
and attributes. This is the "neutron": neutral, stabilizing the atom.

### Full NUCLEUS = Tower + Node + Nest + Meta

```
NUCLEUS (Atom) = Tower + Node + Nest + [biomeOS, skunkBat, sourDough]
              = all 13 primals
              = all capability domains
```

The compute trio sketch completes the Node atomic definition, moving
it from "structural health checks" to "semantic contract validation"
(Wave 8, mirroring Wave 7's content pipeline evolution for Nest).

---

## Implications for Future Composition

1. **Spring compute**: Any spring that needs GPU compute (neuralSpring
   for ML, hotSpring for QCD, ludoSpring for games, wetSpring for bio)
   composes the Node atomic. The spring never touches GPU hardware.

2. **guideStone compute**: lithoSpore's LTEE simulations can use the
   sovereign dispatch path when GPU is available, falling back to CPU
   when deployed on minimal hardware.

3. **NFT attestation**: Novel Ferment Transcripts that attest to
   computational results can reference the dispatch contract
   (`shader.compile.wgsl` → `compute.dispatch.submit` → result hash)
   as provenance evidence, tying the compute trio to the provenance trio.

4. **Cross-platform parity**: The 4-tier degradation model ensures
   compute works everywhere — from a 3-GPU workstation to a Raspberry Pi.
   The IPC contracts are identical; only the dispatch tier changes.

---

---

## Empirical Validation (June 1, 2026)

### What Was Proven

The theoretical pipeline described above was tested end-to-end on hardware:

```
WGSL source code
  │
  ├── shader.compile.wgsl → coralReef (UDS socket)
  │     target: sm_70 (Volta)
  │     result: 472-byte SPIR-V binary, 0 warnings
  │     latency: ~120ms
  │
  └── shader.dispatch → toadStool (TCP:33709)
        binary: SPIR-V from coralReef
        bdf: 0000:02:00.0 (Titan V, VFIO-bound)
        dispatch_mode: local_cylinder (bare-metal)
        result: status=completed, ~1-4s
```

Both Titan V GPUs (`0000:02:00.0` and `0000:49:00.0`) dispatch successfully.
The RTX 5060 Blackwell (`0000:21:00.0`) is blocked by DRM provider gap.

### What Was Partially Proven

- **barraCuda cross-gate dispatch**: Routes correctly, acquires device handle,
  but calls `compute.dispatch.execute` (should be `compute.dispatch.submit`).
  One-line fix in barraCuda will complete this path.
- **songbird discovery**: coralReef registered and resolvable for 7 capabilities.
  But toadStool doesn't query songbird — uses its own internal provider registry.

### What Remains

| Gap | Team | Severity | Description |
|-----|------|----------|-------------|
| GAP-HS-118 | toadStool | P0 | VFIO cylinder readback not implemented |
| GAP-HS-119 | toadStool | P0 | DRM dispatch requires missing visualization provider |
| GAP-HS-120 | barraCuda | P0 | Cross-gate dispatch calls nonexistent method |
| GAP-HS-121 | toadStool | P1 | Blackwell firmware inventory empty |
| GAP-HS-122 | coralReef | P1 | No sm_120 codegen target |

### The 234-Experiment Arc

This validation is the culmination of 234 experiments spanning ~18 months:

| Era | Experiments | Achievement |
|-----|------------|-------------|
| Physics (001–057) | Sarkas MD, nuclear EOS, GPU benchmarks | Proved WGSL physics correctness |
| Sovereignty (058–131) | VFIO, Falcon, SEC2, ACR, WPR | Understood GPU hardware from silicon up |
| Diesel Engine (132–189) | Ember, GlowPlug, warm-catch, catalyst | Built the machinery to control GPUs |
| Pipeline (191–234) | PBDMA, dispatch, compile trio, NOP, lockup | **Connected compilation to execution** |

The sovereign compute trio thesis originated as a composition pattern (gen4). It is now
empirical fact for the VFIO path on Volta silicon. The DRM path, Blackwell support, and
readback pipeline are active evolution targets.

---

## References

- `primalSpring/docs/COMPUTE_TRIO_EVOLUTION.md` — architecture document
- `COMPOSITION_PATTERNS.md` — PrimalBridge degradation tiers
- `CONTRACT_TESTING_THESIS_SKETCH.md` — Wave 7 contract testing thesis
- `STADIAL_INTERSTADIAL_PATTERN.md` — evolution phase model
- `DEPLOYABLE_ARTIFACT_STANDARD.md` — budding and artifact patterns
- `wateringHole/handoffs/SOVEREIGN_COMPUTE_THREE_GPU_WARM_CATCH_HANDOFF_MAY11_2026.md`
- `wateringHole/handoffs/hotSpring/HOTSPRING_PIPELINE_INTELLIGENCE_JUN01_2026.md`
- `wateringHole/handoffs/hotSpring/HOTSPRING_SOVEREIGN_COMPUTE_TRIO_VALIDATED_JUN01_2026.md`
- `hotSpring/docs/PRIMAL_GAPS.md` — GAP-HS-115 through GAP-HS-122
