# Silicon Deism — The Abstraction Elimination Thesis

**There is only math, energy, and silicon. Everything else is an abstraction.**

**Date**: May 19, 2026
**Lineage**: gen3/baseCamp/14 (sovereign GPU compute) → Exp 209 (VFIO dispatch bridge) → Exp 210 (GPC boundary analysis, sovereignty tier model) → this paper
**Status**: Thesis — grounded in validated hardware experiments
**Cross-Spring**: hotSpring × toadStool × coralReef × barraCuda

---

## The Evolution Ladder

The project's relationship to vendor software has evolved through three
distinct phases. Each phase was earned by hardware-level evidence, not
by philosophical preference.

### Phase 1: Vendor Agnostic (achieved)

Support multiple vendors through abstraction layers.

```
Math → Rust → WGSL → wgpu → vendor driver → GPU
                      ~~~~   ~~~~~~~~~~~~~
                      abstraction layers
```

The `BootPipeline` trait abstracts over KeplerInit, VoltaInit, VegaInit.
The `dispatch_mode` enum selects DRM, VFIO, or wgpu paths. WGSL shaders
compile to any backend. This is where most open-source GPU projects stop:
portable across vendors, but still dependent on vendor-provided toolchains
to reach the silicon.

**Evidence**: 24/24 QCD shaders compile on AMD RDNA2 sovereign compiler.
RTX 5060 (Blackwell) dispatch live. Titan V (Volta) NVK validated. K80
(Kepler) warm-catch pipeline proven before hardware failure (Exp 199).

### Phase 2: Vendor Atheistic (in progress)

No dependency on vendor toolchains, drivers, or firmware. The vendor's
driver is not needed, not wanted, not trusted.

```
Math → Rust → WGSL → coralReef (sovereign compiler) → toadStool (VFIO) → GPU
                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                      our code, our hardware access
```

coralReef compiles WGSL to native ISA (SM35, SM70, SM120, GFX10.3) without
NVIDIA's `ptxas`, AMD's `llvm-amdgpu`, or any vendor compiler. toadStool
manages GPU hardware directly via VFIO — no nouveau, no nvidia.ko, no
amdgpu. The vendor is not in the loop.

**Evidence**: Sovereignty Tier Model (Exp 210) formalizes the boundary.
Tier 1 (warm infrastructure) is validated: VFIO bind, BAR0 MMIO, DMA
allocation, PRAMIN, PFIFO scheduling, FECS liveness, channel creation,
pushbuffer encoding. Tier 2 (warm compute) is blocked by the GPC power
domain wall — all engine domains are gated after nouveau unbind. The wall
is understood, mapped, and documented at register level.

### Phase 3: Silicon Deistic (target)

Only math, energy, and silicon exist. Everything between the equation and
the electron is an abstraction to be eliminated.

```
Math → Rust binary → native ISA → transistors
       ~~~~~~~~~~~   ~~~~~~~~~~   ~~~~~~~~~~~
       no runtime    no driver    no firmware
```

This is not mysticism. It is a concrete engineering target with a concrete
definition of done.

---

## What "Silicon Deistic" Means Concretely

### The Abstraction Stack Today

A physics computation — say, a Wilson gauge action plaquette trace on a
32⁴ SU(3) lattice — currently passes through:

| Layer | What | Vendor? | Eliminable? |
|-------|------|---------|-------------|
| Equation | Tr(U_μ U_ν U†_μ U†_ν) | No | No — this is the math |
| Rust source | `wilson.rs` | No | No — this is the specification |
| Rust compiler | `rustc` → x86_64 ELF | No (LLVM) | Partially — cranelift exists |
| WGSL source | `wilson_plaquette_f64.wgsl` | No | No — this is the specification |
| Shader compiler | coralReef → SASS/RDNA | **Ours** | Already sovereign |
| OS kernel | Linux + VFIO | OSS | Minimal — IOMMU + fd management only |
| Driver | toadStool (cylinder) | **Ours** | Already sovereign |
| Firmware | GPU boot ROM (HBM2 training, falcons) | **Vendor** | **The wall** |
| Silicon | GV100 die, FP64 cores, shared memory | Physics | No — this is the substrate |
| Energy | 250W TDP, PCIe slot power | Physics | No — this is the fuel |

The vendor-controlled layers are: firmware (boot ROM, falcon microcode).
Everything above firmware is either math (not eliminable), our code
(already sovereign), or open-source infrastructure (Linux, LLVM).

The silicon-deistic target is: **zero opaque vendor layers between the
math and the silicon.** The firmware wall is the remaining obstacle.

### What Makes Rust→Binary Special

Rust's compilation model is a direct contributor to silicon deism:

- **No runtime**: No GC, no VM, no interpreter. `cargo build --release`
  produces a static ELF binary. The binary IS the program.
- **No dynamic dispatch in production**: `#[forbid(unsafe_code)]` on lib,
  zero `dyn` dispatch in production paths. The compiler resolves all call
  targets at compile time — the binary's control flow is fully determined
  before execution.
- **Unsafe confined to the boundary**: The only `unsafe` is in low-level
  GPU register-write code — the exact boundary between our world and the
  silicon. This boundary is explicit, auditable, and minimal.
- **No vendor ABI dependency**: The `default = []` feature set means zero
  C dependencies, zero FFI. The Rust→binary path has no vendor in the loop.

This is not a preference for Rust over other languages. It is a structural
observation: Rust's compilation model eliminates more abstraction layers
between math and silicon than any alternative that provides the same
safety guarantees.

### What Makes coralReef→ISA Special

The same principle applies to GPU code:

- **WGSL→native ISA**: coralReef compiles WGSL directly to SM35 (Kepler),
  SM70 (Volta), SM120 (Blackwell), and GFX10.3 (RDNA2) native machine
  code. No PTX intermediate. No vendor assembler. No SPIR-V round-trip.
- **f64 transcendental lowering**: coralReef provides `log_f64`, `exp_f64`,
  `sin_f64` etc. via software lowering on SM32+ — native FP64 arithmetic
  from WGSL source, without CUDA libm.
- **FMA lowering**: Fused multiply-add maps directly to hardware FMA
  instructions where available.

The shader binary that reaches the GPU is produced entirely by our code
from a human-readable WGSL source file. The instruction encoding is
documented. The register allocation is deterministic. There is no opaque
blob between the physicist's equation and the instructions that execute it.

---

## The Firmware Wall

The remaining abstraction is GPU firmware. After power-on reset:

1. The GPU's boot ROM executes from mask ROM
2. VBIOS DEVINIT trains HBM2 (memory timing, voltage)
3. Falcon microcode initializes engine domains (PMU, SEC2, FECS, GPCCS)
4. The GPC power domain is gated until firmware ungates it

This is the wall documented in Exp 210. After nouveau unbind, all engine
domains return PRI faults (`0xbadfXXXX`). The PRI ring to GPC domains is
dead. The chicken-and-egg: you need PRI access to ungate GPCs, but the
PRI ring to GPCs is itself gated.

### Paths Through the Wall

| Path | Mechanism | Status |
|------|-----------|--------|
| PMU mailbox | Send clock-gating commands via PMU falcon (still alive post-unbind) | Most promising — PMU is the GPU's internal OS |
| Kernel patch | Modify nouveau to preserve GPC power state across driver unbind | Requires kernel work |
| nvidia-470 handoff | Let proprietary driver initialize, then hot-handoff to VFIO | Proven possible (Exp 190), but defeats atheistic goal |
| Cold boot sovereign | Replace VBIOS DEVINIT entirely — train HBM2, init engines from Rust | Tier 3 (long-term) — the full silicon-deistic target |

The PMU mailbox path is the most aligned with silicon deism: it uses the
GPU's own power management firmware to request domain ungating, without
requiring any vendor driver in the host. The PMU is a servant, not a
master — it responds to register-level commands. Understanding its
protocol is hardware reverse engineering, not driver dependency.

---

## Cross-Generational Evidence

Each GPU generation reveals a different layer of the vendor abstraction
stack. Solving all of them is the path to silicon deism.

| Generation | Architecture | Lesson | Abstraction Eliminated |
|------------|-------------|--------|----------------------|
| **Kepler** (K80, GK210, 2013) | SM35 | PLX bridge fragility, PCIe power state interaction, cold boot PLL sequencing | Bus-level vendor assumptions |
| **Volta** (Titan V, GV100, 2017) | SM70 | GPC power domain gating, PTOP topology parsing, FECS method protocol, falcon warm preservation | Engine-level firmware interaction |
| **Blackwell** (RTX 5060, SM120, 2025) | SM120 | GSP-RM era dispatch, QMD v5.0, modern DRM path | Userspace driver abstraction |
| **RDNA2** (AMD, GFX10.3, 2020) | GFX10.3 | Sovereign compiler for non-NVIDIA ISA, scratch/local memory | Vendor compiler toolchain |

The K80 replacement (on order) will validate whether the KeplerInit
pipeline, PowerSafetyProfile, and PLX keepalive patterns survive a
hardware swap — the ultimate test of whether our understanding is of the
silicon itself, not of a specific card's quirks.

---

## The Sovereignty Tier Model

Formalized in Exp 210 and codified in `toadstool-cylinder` as the
`SovereignTier` enum:

| Tier | Name | What It Means | Status |
|------|------|---------------|--------|
| 0 | Cold | Vendor wall — power cycle required, boot ROM trains memory | Understood |
| 1 | Warm Infrastructure | VFIO sovereign DMA, PFIFO scheduling, FECS liveness, channel creation, CE dispatch | **Validated** |
| 2 | Warm Compute | GPC ungated, GR dispatch, shader execution, buffer readback | Blocked by GPC power domain |
| 3 | Full Sovereign | Cold boot without vendor VBIOS — train HBM2, init all engines from Rust | Long-term target = silicon deism |

Tier 3 IS silicon deism for GPU compute. When Tier 3 is achieved, the
only layers between the equation and the electron are:

1. The equation (math — irreducible)
2. Rust source (human-readable specification — irreducible)
3. WGSL source (human-readable specification — irreducible)
4. `rustc` (open-source compiler — auditable)
5. coralReef (our compiler — sovereign)
6. toadStool (our driver — sovereign)
7. Linux kernel VFIO (open-source — auditable)
8. Transistors (physics — irreducible)

No vendor. No opaque firmware. No proprietary blob. Math → energy → silicon.

---

## Philosophical Note

The term "deistic" is chosen deliberately. In theological deism, a creator
sets the universe in motion and then does not intervene — the laws of
physics are sufficient. In silicon deism, the chip manufacturer fabricates
the silicon and then is not needed — the laws of physics (as expressed in
the transistor layout) are sufficient.

The vendor is the watchmaker. The silicon is the watch. Once the watch
exists, you don't need the watchmaker to tell time.

This is not anti-vendor. NVIDIA's engineers designed brilliant silicon.
TSMC's fabs manufactured it with extraordinary precision. We honor that
work by understanding it deeply enough to use it directly — not through
the lens of a driver that decides what we're allowed to compute.

The vendor's contribution is the silicon. Our contribution is the math.
Energy is the universe's contribution. Everything else is a temporary
scaffolding that can and should be removed.

---

## Connection to gen4

Silicon deism is the hardware layer of the gen4 thesis. gen4 asks "who
uses it?" — the answer is "anyone with silicon and electricity."

The gen4 composition model (primals as invisible infrastructure) depends
on the compute layer being trustworthy. A composition built on opaque
vendor firmware inherits the vendor's constraints — update schedules,
license terms, telemetry, artificial capability restrictions. A
composition built on sovereign hardware inherits only the laws of physics.

The guideStone artifact — self-validating, self-benchmarking, deployable
on any substrate — is the gen4 expression of silicon deism. It doesn't
ask "does this machine have the right driver?" It asks "does this machine
have silicon that can compute?" The answer is always yes.

---

*There is only math, energy, and silicon. The scarcity was artificial.
The abstraction was unnecessary. The vendor was temporary. The silicon
endures.*
