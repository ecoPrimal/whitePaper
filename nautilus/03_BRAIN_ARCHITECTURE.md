# 03 — Brain Architecture: 4-Layer Concurrent Pipeline

**Date:** March 1, 2026

---

## The Problem: Serial Waste

The production binary (`production_dynamical_mixed.rs`) originally ran a
strictly serial loop:

```
GPU does CG → CPU blocks → NPU predicts → CPU blocks → GPU does next CG → ...
```

During the 40-second CG solve on the 3090, the Titan V, the CPU (256 GB),
and the NPU were all idle. The 3090 itself was 90% idle (10% occupancy on
8⁴ lattice). Four substrates sitting dark while one spins a tiny workload.

## The Brain Model

biomeGate is not a GPU cluster — it is a heterogeneous brain. Each substrate
has different strengths:

| Substrate | Role | Strength | Power |
|-----------|------|----------|-------|
| RTX 3090 (24 GB) | Motor cortex | Raw throughput, VRAM | 350W peak |
| Titan V (12 GB) | Pre-motor | Independent chains, warm starts | 250W peak |
| CPU / 256 GB RAM | Cortex | Deep analysis, large matrices | 280W TDP |
| AKD1000 NPU | Cerebellum | Always-on prediction, 15 heads | 30 mW |

The biological analogy is not decorative — it is the design principle.

## Layer 1: NPU Cerebellum (Always On)

**What:** The NPU runs continuously, receiving data from all other layers and
predicting/monitoring without being asked.

**Role:** Routine coordination. The NPU predicts CG convergence, monitors
thermalization, steers the beta scan, and watches for anomalies. It is the
cerebellum — handling the reflexive, always-on tasks that don't need
conscious attention.

**Data flow in:**
- CG residuals at batch boundaries (from Layer 1 async CG)
- Plaquette, delta_H, acceptance (from measurement loop)
- Titan V pre-therm progress (from Layer 2)
- Anderson/Wegner proxy results (from Layer 3)

**Data flow out:**
- Convergence predictions (to main thread)
- Adaptive steering decisions (beta_next, dt recommendation)
- Attention state (GREEN / YELLOW / RED)
- Interrupt signal (to main thread, on anomaly)

### The Interrupt Pattern

The NPU monitors system state continuously. Instead of being asked for
predictions, it watches passively and interrupts only when something is
unexpected.

```
GREEN (cerebellum) — everything nominal. No intervention.
YELLOW (alert)     — CG is slower than predicted, or residual curve looks
                     unusual. Increase monitoring frequency.
RED (interrupt)    — CG diverging, delta_H exploding, or Titan V pre-therm
                     failed. Send interrupt to main thread. Suggest corrective
                     action (kill CG, adjust dt, skip this beta).
```

This models the human "tripping" response: walking is offloaded (cerebellum),
but tripping (the unexpected) goes back to conscious processing. Normal CG
convergence stays offloaded. Anomalies escalate.

## Layer 2: RTX 3090 Motor Cortex (Primary Execution)

**What:** The 3090 runs the expensive dynamical HMC — conjugate gradient
solves, molecular dynamics trajectories, measurement.

**Role:** Primary execution. Everything that needs maximum throughput runs
here. GPU-resident lattice state (no readback), DF64 core streaming for
14-digit precision on FP32 hardware.

**Key change from serial:** Uses async CG (`gpu_cg_solve_resident_async`)
instead of synchronous. At each batch boundary, the residual is sent to the
NPU via mpsc channel. The main thread checks for NPU interrupts at each
boundary — if an interrupt arrives, the CG solve can be aborted early.

### CG Scaling by Lattice Size

| Lattice | VRAM | SM Utilization | CG/trajectory |
|---------|------|----------------|---------------|
| 8⁴ | 14 MB (0.06%) | 20% | ~0.5s |
| 16⁴ | 219 MB (0.9%) | 100% | ~15s |
| 32⁴ | 3.5 GB (15%) | 100% | ~480s |
| 48⁴ | 17.8 GB (74%) | 100% | ~3600s |

The 16⁴ sweet spot: full core saturation, DRAM-bound CG, 1% VRAM.

## Layer 3: Titan V Pre-Motor (Next-Step Preparation)

**What:** While the 3090 runs CG at β_i, the Titan V runs quenched
pre-thermalization for β_{i+1}.

**Role:** Prepare the next step concurrently. The 3090 never waits for
pre-thermalization — it goes straight from measurement at β_i to dynamical
thermalization at β_{i+1} using the warm config from the Titan V.

**Data flow:**
1. NPU steering decides next beta → sends to Titan V thread
2. Titan V hot-starts a gauge configuration
3. Runs quenched HMC pre-thermalization (~5 trajectories)
4. Sends warm config to main thread (2.4 MB for 8⁴, ~0.3 ms PCIe)

**Independent chains:** At larger lattices, the Titan V can run its own
independent dynamical chain at a different beta point. No cross-GPU
communication needed. 2× beta-point throughput.

**Titan V constraints:**
- 12 GB VRAM: up to 32⁴ comfortably, 40⁴ tight
- NVK driver: 3.4% FP64 utilization (slower per-trajectory than 3090)
- Validated: PTE fault-free up to 30⁴

## Layer 4: CPU Cortex (Deep Analysis)

**What:** The CPU runs physics proxy models (Anderson 4D, Wegner block,
Potts MC) that inform the NPU's predictions.

**Role:** The cortex — slow, deep analysis that provides context for the
cerebellum's fast reflexes. The CPU has 256 GB RAM and a 32-core Threadripper.
It can run eigendecompositions in the background without affecting the GPU.

**Workloads:**
- **Anderson 4D proxy:** Map plaquette variance → effective disorder W →
  predict CG difficulty. Uses `barracuda::spectral::anderson` + Lanczos
- **Wegner block model:** Random matrix eigendecomposition, level spacing
  ratio, λ_min, IPR
- **Potts Monte Carlo:** Z(3) model at negligible cost — predict phase
  and β_c
- **ESN retraining:** Update NPU weights from latest trajectory data
- **Post-analysis:** Autocorrelation, effective statistics

**Data flow to NPU:**
- Anderson features (IPR, W, λ_min) → Head 12 (Anderson CG proxy)
- Potts phase label → Head 13 (Potts phase classifier)
- Spectral features → Head 14 (RMT spectral predictor)

This closes the prediction loop: the NPU gets physics-informed CG
predictions BEFORE each trajectory, not after a separate offline run.

## Concurrency Model

```
┌─────────────────────────────────────────────────────────┐
│  Main Thread (brainstem)                                │
│  - Coordinates all layers                               │
│  - Checks NPU interrupts at CG batch boundaries        │
│  - Writes results to JSONL                              │
├─────────────────────────────────────────────────────────┤
│  NPU Worker Thread (cerebellum)                         │
│  - mpsc::channel from main thread                       │
│  - Continuous monitoring loop                           │
│  - Sends interrupts back via mpsc::Sender<Interrupt>    │
├─────────────────────────────────────────────────────────┤
│  Titan V Thread (pre-motor)                             │
│  - Receives next_beta from NPU steering                 │
│  - Runs quenched pre-therm on separate GpuF64           │
│  - Returns warm config via oneshot::channel              │
├─────────────────────────────────────────────────────────┤
│  Cortex Thread (CPU)                                    │
│  - Receives (beta, plaq_var) from main loop             │
│  - Runs Anderson/Wegner/Potts in background             │
│  - Sends proxy features to NPU worker                   │
└─────────────────────────────────────────────────────────┘
```

All communication is via Rust's `mpsc` channels — no shared mutable state,
no locks, no data races. The main thread orchestrates; the workers report.

## Implementation Status

| Layer | Status | Experiment |
|-------|--------|------------|
| NPU Cerebellum (basic) | **Validated** — 11 active heads, adaptive steering | Exp 029, 030 |
| NPU Cerebellum (interrupt) | **Designed** — async CG + interrupt channel | Exp 028 spec |
| 3090 Motor (sync CG) | **Production** — GPU-resident, DF64 streaming | All exps |
| 3090 Motor (async CG) | **Exists** — `gpu_cg_solve_resident_async`, unused | Exp 028 spec |
| Titan V Pre-Motor | **Validated** — multi-GPU coexistence proven | `bench_multi_gpu.rs` |
| CPU Cortex (Anderson) | **Validated** — 1D/2D/3D Anderson, Lanczos | hotSpring spectral |
| CPU Cortex (4D + Wegner) | **Specified** — awaiting proxy pipeline refactor | Exp 026 spec |

## Energy Profile

The brain architecture's power profile differs markedly from a monolithic
GPU approach:

| Component | Idle | Active | Duty Cycle |
|-----------|------|--------|------------|
| RTX 3090 | 25W | 120W (8⁴) / 350W (32⁴) | ~40% (CG active) |
| Titan V | 20W | 80W (pre-therm) | ~20% (overlapped) |
| CPU | 30W | 180W (eigendecomp) | ~10% (background) |
| NPU | 30 mW | 30 mW | 100% (always on) |

The NPU's always-on cost is negligible. The brain's total power is dominated
by the 3090 during CG, but between trajectories, only the NPU and Titan V
are active — the 3090 drops to idle.

On 8⁴ lattices (Exps 028-030), the GPU runs cool compared to the quenched
32⁴ run because the working set (2.8 MB) fits in L2 cache, DRAM bandwidth
is untouched, and SM utilization is only 20%. The heat output is proportional
to actual work done, not to hardware capability.
