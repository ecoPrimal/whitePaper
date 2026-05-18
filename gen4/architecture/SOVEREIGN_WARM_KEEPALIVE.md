# Sovereign Warm Keepalive

**183ms GPU initialization on sovereign hardware — no vendor driver, no kernel module, no ACR re-boot**

**Date**: May 18, 2026
**Lineage**: gen3/baseCamp/14 → Exp 206 (Falcon ACR DMA) → Exp 207 (Boot Abstraction) → **Exp 208** (Warm Keepalive)
**Status**: Proven — dual Titan V (GV100), validated across power cycles and daemon restarts
**Cross-Spring**: hotSpring × toadStool (cylinder + ember)

---

## The Result

A sovereign GPU compute pipeline initializes NVIDIA Titan V hardware in
**183ms** with `compute_ready: true`. No vendor driver. No kernel module
beyond VFIO. No userspace stack beyond our Rust daemon. The GPU's own
boot ROM firmware is preserved and reused — the 3.7s ACR (Authenticated
Code Runner) re-boot that dominated the warm pipeline is eliminated entirely.

| Scenario | Pipeline Time | compute_ready |
|----------|-------------|---------------|
| Cold (no boot ROM training) | 14s | false |
| Cold (early-exit) | 200ms | false |
| Warm (pre-falcon fix) | 3.9s | true |
| **Warm (falcon preservation)** | **183ms** | **true** |

The 76× speedup over cold and 21× over pre-falcon warm is not a software
optimization in the traditional sense. It is the result of understanding
which hardware state survives which boundaries and not destroying it.

---

## Why This Matters for gen4

gen4 products — esotericWebb, helixVision, coralForge — compose primals
into tools. Those tools need GPU compute. If GPU initialization takes 14
seconds (or even 3.9 seconds), every daemon restart, every live-patch,
every deployment becomes a latency event that breaks the composition
illusion. At 183ms, GPU initialization is invisible. The primal layer
disappears, which is the gen4 thesis.

For the biomeOS trajectory, this is the first proof that sovereign
hardware management can match or exceed the responsiveness of vendor
driver stacks. The NVIDIA proprietary driver achieves similar latency
because it never loses falcon state — it keeps the GPU initialized
across the kernel module's lifetime. We achieve the same by preserving
FECS firmware across VFIO device opens and daemon restarts via systemd
FileDescriptorStore.

---

## Architecture

### The Hardware Line

Cold boot is a power-on reset. The boot ROM on the GPU board trains
HBM2 memory using sequences burned into the VBIOS. This is the same
wall NVIDIA's proprietary driver faces. No software — not theirs, not
ours — can train HBM2 from a cold GPU. Only the boot ROM can, triggered
by board-level voltage regulator sequencing.

This means cold boot requires a full machine power cycle. This is an
acceptable, well-defined hardware constraint — not a software limitation.

### The Warm Pipeline

After the boot ROM runs (at machine power-on), the GPU is "warm": HBM2 is
trained, PRAMIN (privileged RAM interface) is live, and PMC engines are
partially initialized. The sovereign init pipeline then:

```
identity_probe   →  Read BOOT0, identify GPU generation
pmc_enable       →  Enable all PMC engine domains
pgraph_reset     →  Reset PGRAPH engine (shader/graphics subsystem)
cg_sweep         →  Sweep clock gating registers
pri_recovery     →  PRI (programmable register interface) recovery
boot_state_probe →  Classify warm/cold via PRAMIN sentinel + PMC popcount
memory_training  →  HBM2/GDDR training (skipped if warm)
falcon_boot      →  Load FECS/GPCCS firmware via ACR HS DMA boot
gr_init          →  GR (graphics) engine initialization
verify           →  Final state verification
```

Before the falcon warm preservation fix, the warm pipeline took **3.9s**
— with falcon_boot's ACR DMA consuming 94.5% of that time.

### The Root Cause: Self-Inflicted Falcon Death

The pipeline's `pgraph_reset` stage toggles PMC_ENABLE bit 12, resetting
the entire PGRAPH engine. This kills FECS (Falcon Engine Control
Subsystem) and GPCCS (GPC Control and Status) firmware. The subsequent
`boot_state_probe` then finds the falcon cold — because the pipeline
just killed it. `falcon_boot` then runs a full ACR HS DMA boot (3.7s)
to reload firmware that was alive 200ms earlier.

On the **second** `sovereign.init` call, this cycle repeats: boot the
falcon, then kill it on the next call's pgraph_reset, then re-boot it.

### The Fix: Early Falcon Probe

An early falcon state probe runs **before** `pgraph_reset`. It reads
FECS registers directly from BAR0:

| Register | What It Tells Us |
|----------|-----------------|
| `CPUCTL` (0x409100) | Halted, HRESET, running state |
| `CPUCTL_ALIAS` (0x409130) | CPU control alias (non-secure view) |
| `PC` (0x409110) | Program counter — where the falcon is executing |
| `MAILBOX0` (0x409040) | OS-firmware handshake register |

The detection logic classifies falcon state into four categories:

- **Cold**: CPUCTL halted, no meaningful PC → run pgraph_reset normally
- **WarmPreserved**: CPUCTL halted, not in HRESET → skip pgraph_reset
- **WarmRunning**: CPUCTL in HRESET, PC >= 0x40 → skip pgraph_reset
- **Inconsistent**: Unexpected register combination → run pgraph_reset (safe fallback)

The PC threshold (>= 0x40) distinguishes genuine running firmware from
Function Level Reset (FLR) artifacts. After VFIO device re-open (which
triggers FLR), the PC register can retain a small residual value
(0x00–0x10) from the boot ROM. Genuine ACR-loaded firmware operates at
PC 0x80+ (code section entry points). The threshold filters false
positives without rejecting real firmware state.

### After the Fix

When the falcon is detected as `WarmRunning`:

1. `pgraph_reset` is **skipped** (preserving FECS/GPCCS)
2. `boot_state_probe` finds falcon warm (PGRAPH wasn't reset)
3. `falcon_boot` returns immediately ("warm-running")
4. `gr_init` skips (PGRAPH already initialized)
5. CG sweep + PRI recovery still run (they don't affect falcons)

The warm pipeline becomes:

| Stage | Time (µs) | Fraction |
|-------|----------|----------|
| identity_probe | 11,000 | 6.0% |
| pmc_enable | 73,000 | 40.3% |
| pri_recovery | 85,000 | 46.3% |
| verify | 12,000 | 6.5% |
| **TOTAL** | **183,000** | |

### Persistence Across Daemon Restarts

The systemd FileDescriptorStore integration ensures warm state survives
daemon restarts:

1. On SIGTERM: `store_anchors()` sends 4 VFIO file descriptors (2 device + 2 iommufd) to systemd via `sd_notify` + `SCM_RIGHTS`
2. systemd holds the fds while the process exits
3. On restart: `retrieve_anchors()` recovers fds from `LISTEN_FDS`
4. `VfioAnchor` reconstructed from stored fds — GPU never lost its VFIO binding

Because the VFIO device fds are preserved, no Function Level Reset
occurs. The falcon firmware continues running at PC=0xB0+. The next
`sovereign.init` call detects `WarmRunning` and completes in 183ms.

This enables zero-downtime live patching: copy new binary, `systemctl
restart`, new daemon picks up warm GPUs. The user (or the composition
layer) never sees a cold start.

---

## Validation Evidence

### Power Cycle Validation

Full machine power cycle → boot ROM trains HBM2 → toadstool starts:

| Card | 1st sovereign.init | Falcon State | Pipeline |
|------|-------------------|-------------|----------|
| Titan V #1 (0000:02:00.0) | 185ms | WarmRunning (PC=0xB0) | pgraph_reset skipped, falcon_boot skipped |
| Titan V #2 (0000:49:00.0) | 188ms | WarmRunning (PC=0xB9) | pgraph_reset skipped, falcon_boot skipped |

The boot ROM leaves FECS running. The first `sovereign.init` after power
cycle detects this and achieves full 183ms initialization with no ACR
boot needed.

### Daemon Restart Validation

After `systemctl restart toadstool-ember`:

- `sovereign.warm_status`: 2 anchors held, both warm, fd_store_capable
- `sovereign.init` card #1: 183ms, falcon=WarmRunning
- `sovereign.init` card #2: 183ms, falcon=WarmRunning

### Twin-Card Consistency

Both Titan Vs produce near-identical timings (183ms ± 5ms), confirming
that the measurement is deterministic and the optimization is
hardware-independent within the GV100 generation.

---

## What This Enables

### For toadStool

The `sovereign.init` RPC is now fast enough to be called speculatively.
A composition graph can probe GPU readiness at daemon startup without
blocking. The cold early-exit path (200ms, `compute_ready: false`)
tells the caller the GPU needs a power cycle. The warm path (183ms,
`compute_ready: true`) delivers a ready compute surface.

### For coralReef / barraCuda

GPU dispatch latency is no longer dominated by initialization. The
triangle architecture (coralReef ↔ toadStool ↔ barraCuda) can treat
GPU readiness as an O(200ms) event rather than an O(14s) event. This
changes the economics of GPU sharing between primals.

### For Cross-Platform Testing

The techniques are architecture-specific in implementation but
pattern-universal:

- **Falcon warm detection** applies to all NVIDIA GPUs with HS-secure falcons (Maxwell+)
- **FLR PC threshold** must be calibrated per architecture (code section offsets vary)
- **pgraph_reset skip** must be validated per generation (engine reset semantics differ)
- **systemd fd store** is Linux-specific; other platforms need equivalent fd persistence

The wateringHole handoff below provides the information needed for
primals teams to test on other hardware.

---

## Files Changed (toadStool)

| File | Change |
|------|--------|
| `cylinder/src/vfio/sovereign_init.rs` | Early falcon probe before pgraph_reset, conditional skip |
| `cylinder/src/vfio/sovereign_strategy.rs` | `detect_falcon_warm_state()` — CPUCTL/PC register classification, FLR threshold |
| `cylinder/src/vfio/sovereign_types.rs` | `skip_cold_memory_training` on `SovereignInitOptions` |
| `server/src/pure_jsonrpc/handler/dispatch/mod.rs` | `sovereign.warm_status` RPC, cold early-exit flag, anchor logging |
| `server/src/pure_jsonrpc/handler/mod.rs` | Route `sovereign.warm_status` |
| `server/src/pure_jsonrpc/handler/core/mod.rs` | Register `sovereign.warm_status` in method list |

---

## The Science Ladder Position

```
Exp 164: Sovereign GPU dispatch proven (WGSL→SM70 SASS)
Exp 197: sovereign.init RPC wired (warm/cold detection)
Exp 198: Vendor-agnostic BootPipeline (Kepler/Volta/Vega)
Exp 206: Falcon ACR DMA boot solved (3.7s)
Exp 207: Boot state abstraction + twin-card profiling (3.9s warm)
Exp 208: Warm keepalive proven (183ms warm, fd store, falcon preservation)
         ← YOU ARE HERE
```

The next frontier is either:
1. **pmc_enable optimization** (73ms, 40% of remaining time — can we detect already-enabled engines?)
2. **Cross-generation validation** (Maxwell, Pascal, Turing, Ampere falcon behavior)
3. **AMD equivalent** (Vega/RDNA falcon-less architecture has different warm semantics)

---

*Cold boot is a hardware line. Warm boot is a software choice. We chose 183ms.*
