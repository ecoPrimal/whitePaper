# Sub-Thesis 15: Self-Routing Precision Brain for Heterogeneous GPU Compute

**Date:** March 11, 2026 (original); **Updated March 30, 2026** (15-tier expansion)
**Status:** **Validated + 15-Tier Continuum Implemented** — barraCuda v0.3.11, 4,307 tests, 15 `PrecisionTier` variants (Binary→DF128), 13 `Precision` variants with per-tier WGSL `op_preamble`, 15 `PhysicsDomain` variants (including Inference/Training/Hashing), per-tier tolerances, coralReef strategy mapping for all tiers. Original 4-tier validation (hotSpring v0.6.28, Kokkos benchmark, NVVM poisoning guard) remains valid as a subset. **Exp 053**: Live Kokkos parity benchmark validates precision routing in production — DF64 transcendental poisoning bug discovered and fixed. 12.4× gap vs Kokkos-CUDA dominated by 1:32 f64 rate; safe DF64 exp path is the single biggest unlock. QF128 (Bailey quad-double on f32) now provides ~96-bit mantissa on GPUs with no f64 hardware.
**Domain:** GPU computing, precision engineering, hardware discovery
**Novelty:** Data-driven self-routing precision brain that discovers hardware
capabilities at startup, routes physics workloads to optimal precision tier
per-domain, and survives driver-level device poisoning — without static
heuristics or vendor-specific codepaths
**Cross-Spring:** hotSpring (precision profiling, physics domains) ×
barraCuda (precision tiers, shader compilation) × toadStool (hardware
discovery, GPU dispatch)

---

## Abstract

GPUs provide a wide spectrum of numerical precision, from 1-bit binary masks
to ~104-bit double-double floating point. barraCuda defines a **15-tier
precision continuum** that spans this spectrum:

```
Scale-down (throughput):  Binary → Int2 → Q4 → Q8 → FP8-E5M2 → FP8-E4M3 → BF16 → F16 → TF32
Baseline:                 F32 (universal, all GPUs)
Scale-up (precision):     DF64 → F64 → F64Precise → QF128 → DF128
```

Each GPU model, each driver, and each shader type exhibits different behavior
across these tiers. Static routing tables are fragile — driver updates, shader
complexity, and transcendental function support all change the picture.

We demonstrate a **self-routing precision brain** that:

1. **Probes** the GPU at startup with minimal test shaders across all 15
   precision tiers (safest to riskiest order)
2. **Records** which tiers compile, dispatch, and produce correct results
   per `HardwareCalibration` with `TierCapability[15]`
3. **Routes** 15 physics domains (including Inference, Training, Hashing) to
   the best available tier based on domain requirements (precision floor, FMA
   sensitivity, throughput bounds) combined with measured hardware capabilities
4. **Survives** driver failure modes including NVIDIA NVVM device poisoning
5. **Cascades** gracefully — if the optimal tier is unavailable, falls back
   to the next-best tier automatically

The brain is portable — it depends only on `PrecisionTier` and
`HardwareCalibration`, both fundamental barraCuda abstractions. Dropping it
into any spring gives that spring automatic precision routing for the hardware
it's running on. Scale-down tiers (Binary through BF16) are universally
available on any GPU with f32 cores.

### Extended Precision Without f64 Hardware

QF128 (Bailey quad-double on f32) provides ~96-bit mantissa using only f32
arithmetic. This is barraCuda's answer to precision requirements on consumer
GPUs that lack f64 hardware or have severe f64 throttling (1:64 rate).

## Discovery: NVVM Device Poisoning

The RTX 3090's proprietary NVIDIA driver routes WGSL through naga → SPIR-V
→ NVVM for compilation. The NVVM compiler cannot handle f64 transcendental
functions (`exp`, `log`) in DF64 or F64Precise modes. A single failed
compilation permanently invalidates the entire wgpu device — all subsequent
buffer creation, dispatch, and readback operations fail with
`"Buffer is invalid"`.

This is not a wgpu bug or a barraCuda bug — it is a fundamental limitation
of the NVIDIA proprietary driver's NVVM backend. NVK (Mesa's open-source
NVIDIA driver) handles all tiers correctly, including DF64 transcendentals.

### Implications for Sovereign Computing

1. **Driver diversity is a security feature**: A single driver bug should
   not kill a compute pipeline. The brain's ability to detect and route
   around this failure demonstrates why sovereignty requires probing, not
   assuming.
2. **NVK is the correct long-term path**: NVK handles all precision tiers
   correctly. The proprietary driver's NVVM limitation is a barrier to
   full DF64 transcendental throughput on consumer NVIDIA GPUs.
3. **coralReef bypass**: The sovereign WGSL→native compilation path may
   bypass the NVVM issue entirely by compiling directly to SASS/GFX,
   never touching NVVM.

## Architecture

### Three-Layer Design

```
Layer 1: HardwareCalibration
  Probe each of 15 tiers with minimal shaders
  Record compile/dispatch/accuracy per tier
  Infer transcendental safety from driver identity
  Output: TierCapability[15] + flags
  Universal tiers (Binary→BF16) always marked safe

Layer 2: PrecisionBrain
  Consume calibration data
  Build route_table[15] for all PhysicsDomains
  O(1) lookup: domain → tier
  Compile method dispatches: compile_shader (f32/sub-f32),
    compile_shader_f64 (f64/DF128), compile_shader_df64 (DF64)
  coralReef strategy string selection per tier

Layer 3: Physics Pipeline
  Call brain.route(domain) → tier
  Call brain.compile(domain, source) → pipeline
  Never touch compilation directly
```

### Probe Order

Universal tiers (Binary, Int2, Q4, Q8, FP8, BF16) are always available —
they compute in f32. Hardware-dependent tiers probe in order:
F16 (needs `SHADER_F16`) → F32 → DF64 → F64 → F64Precise → QF128 → DF128
(safest to riskiest). If any probe poisons the device, subsequent probes
are skipped and those tiers are marked as unavailable.

### F64 Throttle Detection

```
ratio = f64_dispatch_us / f32_dispatch_us
if ratio > 8.0: card has 1:64 FP64:FP32 ratio (consumer)
```

When F64 is severely throttled and DF64 is available, throughput-bound
workloads route to DF64 for higher throughput.

## Results

### Heterogeneous Pair Profile

| Metric | Titan V (GV100, NVK) | RTX 3090 (GA102, proprietary) |
|--------|------|------|
| FP64 cores | 2560 | 82 |
| FP32 cores | 5120 | 10496 |
| VRAM | 12 GB HBM2 | 24 GB GDDR6X |
| PCIe | 3.0 x16 | 4.0 x16 |
| F64 | ✓ full | ✓ full |
| DF64 | ✓ full | △ arith only |
| F64Precise | ✓ full | △ arith only |
| Brain role | Precision oracle | Throughput engine |

### Dual-Card Cooperative Patterns

The two GPUs complement each other:

- **Split compute**: 3090 runs throughput work, Titan V validates precision
- **Redundant compute**: Both run identical trajectories, difference measures numerical noise
- **PCIe bridge**: 1.7 ms for 512KB roundtrip (1.2 GB/s effective)

## Connection to Constrained Evolution

The precision brain embodies the constrained evolution principle: it does
not assume what hardware can do — it probes, records, and routes. When
dropped into a new spring on unknown hardware, it discovers capabilities
and builds an optimal routing table. This is the same pattern as NVK
discovery, NPU capability probing, and the absorption cycle — sovereignty
through self-knowledge, not external authority.

## 15-Tier Precision Table

| # | Tier | Mantissa | Storage | Direction | Universal? |
|---|------|----------|---------|-----------|------------|
| 1 | Binary | 1-bit | 1-bit packed | Scale-down | Yes |
| 2 | Int2 | 2-bit | 2-bit packed | Scale-down | Yes |
| 3 | Q4 | ~3.5-bit | 4-bit block | Scale-down | Yes |
| 4 | Q8 | ~7-bit | 8-bit block | Scale-down | Yes |
| 5 | FP8-E5M2 | 2-bit | 8-bit IEEE | Scale-down | Yes |
| 6 | FP8-E4M3 | 3-bit | 8-bit IEEE | Scale-down | Yes |
| 7 | BF16 | 7-bit | 16-bit | Scale-down | Yes |
| 8 | F16 | 10-bit | 16-bit IEEE | Scale-down | f16 or f32 |
| 9 | TF32 | 10-bit | 32-bit internal | Scale-down | Tensor cores |
| 10 | F32 | 23-bit | 32-bit IEEE | Baseline | Yes |
| 11 | DF64 | ~48-bit | 2×f32 | Scale-up | Yes |
| 12 | F64 | 52-bit | 64-bit IEEE | Scale-up | f64 required |
| 13 | F64Precise | 52-bit | 64-bit IEEE | Scale-up | f64 + FMA |
| 14 | QF128 | ~96-bit | 4×f32 | Scale-up | Yes |
| 15 | DF128 | ~104-bit | 2×f64 | Scale-up | f64 required |

## References

1. hotSpring Experiment 049: Precision Brain + Heterogeneous GPU Evaluation
2. barraCuda `crates/barracuda/src/device/hardware_calibration.rs` — safe per-tier probe (15 tiers)
3. barraCuda `crates/barracuda/src/device/precision_brain.rs` — self-routing brain (15 domains)
4. barraCuda `crates/barracuda/src/device/precision_tier.rs` — `PrecisionTier` enum (15 variants)
5. barraCuda `specs/PRECISION_TIERS_SPECIFICATION.md` — full 15-tier specification
6. hotSpring wateringHole handoff: `HOTSPRING_V0625_PRECISION_BRAIN_NVVM_POISONING_HANDOFF_MAR10_2026.md`
7. wateringHole handoff: `BARRACUDA_V0311_15TIER_PRECISION_CONTINUUM_HANDOFF_MAR30_2026.md`
