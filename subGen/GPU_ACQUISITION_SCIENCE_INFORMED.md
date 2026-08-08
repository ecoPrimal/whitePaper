# GPU Acquisition Guide — Science-Informed Hardware Selection

**Status**: ACTIVE | **Wave**: 157a | **Date**: Aug 8, 2026
**Gate**: strandGate (primary compute), ecosystem-wide applicability
**Audience**: Hardware acquisition, gate operators, overwatch
**Prerequisite**: SILICON_TIER_ROUTING.md, SILICON_INVENTORY.md

---

## Thesis

Our experiments now generate *empirical hardware selection criteria*. Instead of
buying GPUs based on marketing specs or gaming benchmarks, we buy based on measured
QCD physics throughput across the silicon tier hierarchy. The precision continuum
(f64 → DF64 → f32 → f16 → int8) maps directly to GPU architecture choices.

**Key insight**: For Lattice QCD consumer-GPU work, the metrics that matter are:

1. **DF64 throughput** (TFLOPS) — bulk physics compute
2. **Native FP64 ratio** — precision oracle operations
3. **Memory bandwidth** (GB/s) — lattice streaming
4. **VRAM capacity** (GB) — lattice volume ceiling
5. **ROP/atomic throughput** — force accumulation pattern
6. **Power efficiency** (DF64 TFLOPS/watt) — sustained operation cost
7. **Tensor cores** (optional) — SU(3) matmul acceleration path

Gaming benchmarks (FPS at 4K) are *weakly correlated* with these metrics.

---

## Measured Baseline — strandGate Current Fleet

| Metric | RTX 3090 | RX 6950 XT | Winner |
|--------|----------|------------|--------|
| DF64 throughput | 18.1 TFLOPS | **24.1 TFLOPS** | AMD (+33%) |
| Native FP64 | 0.56 TFLOPS | **1.48 TFLOPS** | AMD (+164%) |
| FP64:FP32 ratio | 1:64 | **1:16** | AMD |
| Memory BW | **936 GB/s** | 576 GB/s | NVIDIA (+63%) |
| VRAM | **24 GB** | 16 GB | NVIDIA |
| ROP atomics | 16.0 Gatom/s | **117.7 Gatom/s** | AMD (+635%) |
| ALU+TMU composition | **2.80×** | 1.95× | NVIDIA |
| TDP | 350W | 335W | ~parity |
| DF64/watt | 51.7 GF/W | **71.9 GF/W** | AMD (+39%) |
| Tensor cores | 328 (71 TF32 TFLOPS) | None | NVIDIA |

**Surprise finding**: AMD RDNA 2 is the superior DF64 silicon for our workloads.
The 1:16 FP64 ratio means the error-correction step in Dekker arithmetic runs
at native speed rather than being bottlenecked by 1:64 throughput.

---

## GPU Architecture Tiers for QCD

### Tier S — HBM2/HBM3 Cards (Native FP64 Monsters)

These cards have full-rate FP64 (1:2 ratio). They eliminate the need for DF64
entirely — native f64 at throughput that exceeds our DF64 emulation.

| Card | FP64 TFLOPS | FP64:FP32 | VRAM | HBM BW | TDP | Used Price (eBay, Aug 2026) |
|------|-------------|-----------|------|--------|-----|---------------------------|
| **NVIDIA Tesla V100 (16GB)** | 7.0 | 1:2 | 16 GB HBM2 | 900 GB/s | 250W | $150-250 |
| **NVIDIA Tesla V100 (32GB)** | 7.0 | 1:2 | 32 GB HBM2 | 900 GB/s | 250W | $250-400 |
| **NVIDIA Titan V** | 7.5 | 1:2 | 12 GB HBM2 | 653 GB/s | 250W | $400-600 |
| **NVIDIA A100 (40GB)** | 9.7 | 1:2 | 40 GB HBM2e | 1555 GB/s | 250W | $2000-3000 |
| **NVIDIA A100 (80GB)** | 9.7 | 1:2 | 80 GB HBM2e | 2039 GB/s | 300W | $4000-6000 |
| **AMD MI50 (16GB)** | 6.6 | 1:4 | 16 GB HBM2 | 1024 GB/s | 300W | $100-200 |
| **AMD MI100** | 11.5 | 1:2 | 32 GB HBM2 | 1229 GB/s | 300W | $300-500 |

**Recommendation for strandGate**: **Tesla V100 32GB** ($250-400 on eBay).

Why:
- 7.0 native FP64 TFLOPS = **12.5× our current RTX 3090 FP64** (0.56)
- Eliminates DF64 overhead entirely — pure f64 at throughput
- 32 GB HBM2 handles 32⁴ SU(3) easily
- 900 GB/s HBM2 bandwidth (~parity with RTX 3090 GDDR6X)
- 250W TDP = fits existing PSU
- PCIe x16 Gen 3 — strandGate has the slot
- **Serves as precision validation oracle**: run identical physics in native f64,
  compare against DF64 results → quantifies DF64 precision loss empirically

**Role**: Precision oracle + large-volume HMC where DF64 precision is borderline.

**Caveat**: V100 lacks consumer display outputs. Headless compute only. Needs
`nvidia-fabricmanager` or basic nvidia driver in compute-only mode. No gaming,
no display — pure science silicon.

### Tier A — Consumer Cards with Good FP64 Ratio (AMD RDNA 2/3)

AMD consumer cards have 1:16 FP64 ratio — 4× better than NVIDIA consumer (1:64).
This makes them superior DF64 machines.

| Card | DF64 est. TFLOPS | FP64:FP32 | VRAM | BW | TDP | Used Price |
|------|------------------|-----------|------|-----|-----|-----------|
| **RX 6950 XT** (current) | 24.1 (measured) | 1:16 | 16 GB | 576 GB/s | 335W | $350-450 |
| **RX 6900 XT** | ~22 | 1:16 | 16 GB | 512 GB/s | 300W | $280-380 |
| **RX 7900 XTX** (RDNA 3) | ~28-32 | 1:16 | 24 GB | 960 GB/s | 355W | $650-800 |
| **RX 7900 XT** (RDNA 3) | ~24-28 | 1:16 | 20 GB | 800 GB/s | 315W | $500-650 |
| **Radeon Pro W7900** | ~30 | 1:16 | 48 GB | 864 GB/s | 295W | $1500+ |
| **RX 9070 XT** (RDNA 4) | ~30-35 | TBD | 16 GB | ~700 GB/s | 300W | $550 new |

**Recommendation**: **RX 7900 XTX** ($650-800 used) if VRAM ceiling is the
bottleneck. 24 GB at 960 GB/s with AMD's 1:16 ratio. Expect ~28-32 DF64 TFLOPS
(extrapolating from our 6950 XT measurements).

**Alternative budget play**: Second **RX 6900 XT** ($280-380) for pure independent
trajectory parallelism. Same architecture as our 6950 XT, proven driver path.

### Tier B — NVIDIA Consumer (High VRAM, Tensor Cores)

NVIDIA consumer cards have 1:64 FP64 ratio — poor for native f64, but compensated
by massive FP32 ALU count (good for DF64) and tensor cores (future SU(3) path).

| Card | DF64 est. TFLOPS | VRAM | BW | Tensor | TDP | Used Price |
|------|------------------|------|-----|--------|-----|-----------|
| **RTX 3090** (current) | 18.1 (measured) | 24 GB | 936 GB/s | 328 (Ampere) | 350W | $600-800 |
| **RTX 3090 Ti** | ~19-20 | 24 GB | 1008 GB/s | 336 (Ampere) | 450W | $650-850 |
| **RTX 4090** | ~25-30 | 24 GB | 1008 GB/s | 512 (Ada) | 450W | $1400-1700 |
| **RTX 4080 Super** | ~18-22 | 16 GB | 736 GB/s | 320 (Ada) | 320W | $800-1000 |
| **Titan RTX** | ~12-15 | 24 GB | 672 GB/s | 576 (Turing) | 280W | $500-700 |
| **RTX A6000** | ~20-25 | 48 GB | 768 GB/s | 336 (Ampere) | 300W | $2000-3000 |

**Recommendation**: Don't buy more NVIDIA consumer for DF64 — we already have the
3090 and AMD is better at this workload. NVIDIA's value is in **tensor cores**
(future coralReef SASS path) and **VRAM capacity** (A6000's 48 GB for 48⁴ lattices).

### Tier C — Budget / Retired HBM2 Cards

These are the "retiring HBM2 cards" — former datacenter GPUs now available cheap:

| Card | FP64 | VRAM | BW | TDP | Used Price | Notes |
|------|------|------|-----|-----|-----------|-------|
| **Tesla P100 (16GB)** | 4.7 | 16 GB HBM2 | 732 GB/s | 250W | $80-150 | Pascal. No Tensor. Good FP64. |
| **Tesla P100 (12GB)** | 4.7 | 12 GB HBM2 | 549 GB/s | 250W | $50-100 | Same die, less VRAM. |
| **AMD MI50 (16GB)** | 6.6 | 16 GB HBM2 | 1024 GB/s | 300W | $100-200 | Vega 20. ROCm required. |
| **Tesla K80** (dual-die) | 2×1.87 | 2×12 GB GDDR5 | 2×240 GB/s | 300W | $30-60 | Kepler. Ancient but cheap. |
| **Titan V** | 7.5 | 12 GB HBM2 | 653 GB/s | 250W | $400-600 | Volta. Full tensor + FP64. |

**Best value**: **Tesla P100 16GB at $80-150**. That's 4.7 native FP64 TFLOPS for
the price of a dinner. It's 8.4× our RTX 3090's FP64, and it has HBM2 bandwidth.
The only catch: Pascal (2016), no tensor cores, compute-only (no display).

**Best overall retired**: **Tesla V100 32GB** as discussed in Tier S.

---

## Radeon M150 — What Is It?

The "Radeon M150" likely refers to a rebranded mobile/OEM Radeon from the GCN era
(R5 M230/M255 class or similar). These are:
- Very low power (15-35W)
- GCN 1.0/2.0 era
- 2-4 GB GDDR5
- Negligible compute (<1 TFLOPS FP32)

**Verdict**: Not useful for QCD compute. Possibly useful as a display adapter to
free a compute GPU from display duty (so the 3090 or 6950 XT can run headless).

---

## Science-Informed Acquisition Priority

Based on measured workload characteristics:

### Priority 1: Precision Oracle (V100 32GB) — $250-400

**Why first**: Our arXiv paper claims DF64 achieves sufficient precision for QCD.
A V100 running identical physics in native f64 provides the ground-truth comparison.
This is a publication-quality validation: "DF64 on RTX 3090 agrees with native f64
on V100 to N significant digits across M configurations."

**What it unlocks**:
- Empirical DF64 precision quantification (the paper's missing systematic error bar)
- Large-volume HMC without DF64 overhead (32⁴ SU(3) at full f64 speed)
- Tensor core experiments (V100 has 1st-gen tensor cores: FP16 accumulate to FP32)
- Establishes the "precision oracle" role in the silicon tier hierarchy

### Priority 2: Second AMD Card (RX 6900 XT) — $280-380

**Why second**: Independent trajectory parallelism. Each GPU runs its own Markov
chain — no inter-GPU communication needed for RHMC. A second AMD card at 1:16
FP64 ratio gives us ~22 additional DF64 TFLOPS for $300.

**What it unlocks**:
- 3× independent trajectory generation (3090 + 6950 XT + 6900 XT)
- Faster thermalization of the remaining 12 SU(N>3) configs
- AMD DF64 is already our fastest path — more of the same proven silicon

### Priority 3: Budget Tesla (P100 16GB) — $80-150

**Why third**: Cheapest path to native FP64 compute. At $100, the P100 gives us
4.7 TFLOPS native f64 — useful for small-lattice precision validation and as a
"canary" card (if P100 and V100 agree but 3090 DF64 disagrees, we know DF64 is
the problem).

**What it unlocks**:
- Cross-generation FP64 validation (Pascal vs Volta vs Ampere)
- Cheap redundancy for precision-critical computations
- Training ground for multi-GPU dispatch without risking expensive cards

### Priority 4: VRAM Ceiling Breaker (RX 7900 XTX or A6000) — $650-3000

**Why fourth**: Only needed if physics demands lattice volumes beyond 32⁴ SU(3).
At 24 GB (7900 XTX) or 48 GB (A6000), we can push to 48⁴ or 64⁴ lattices.
Current experiments fit in 16-24 GB — this becomes relevant for SU(8) at large
volumes or continuum-limit extrapolation studies.

### Priority 5: Tensor Core Activation (RTX 4090 or A100) — $1400+

**Why last**: Tensor cores for SU(3) matmul via coralReef SASS is powerful but
requires cross-spring development (WGSL → HMMA lowering). The silicon is idle
until the software path exists. Buy this only after coralReef tensor integration
is operational.

---

## eBay Profiling Criteria

When searching for used GPUs, profile by these criteria (in order):

```
MUST HAVE:
  □ PCIe x16 Gen 3+ (strandGate slots are Gen 4)
  □ TDP ≤ 350W per card (PSU budget: 1600W total, ~4 cards max)
  □ Linux driver support (nvidia or amdgpu, not ancient fglrx)
  □ ECC memory NOT required (we use algorithmic error detection via DF64)

STRONG PREFERENCE:
  □ FP64:FP32 ≥ 1:16 (AMD) or 1:2 (datacenter NVIDIA)
  □ ≥ 16 GB VRAM (32⁴ SU(3) requires ~8 GB, margin for SU(N>3))
  □ HBM2 bandwidth ≥ 700 GB/s (or GDDR6X ≥ 800 GB/s)
  □ Passive/blower cooling (tower case has good airflow)

NICE TO HAVE:
  □ Tensor cores (future SU(3) matmul path)
  □ 2-slot form factor (more cards per chassis)
  □ NVLink connector (future multi-GPU domain decomposition)

AVOID:
  ✗ Mining cards with no video output AND no driver support
  ✗ GTX 10-series (1:32 FP64, no DF64 advantage)
  ✗ RTX 20-series consumer (1:32 FP64, worse than 30-series)
  ✗ AMD Polaris/Fiji (GCN 4/3 — ancient driver, no vulkan compute)
  ✗ Intel Arc (no f64 shader support in wgpu currently)
```

---

## Multi-Card Configuration Scenarios

### Scenario A: Precision Lab ($400-700 additional)

```
strandGate current:  RTX 3090 (DF64) + RX 6950 XT (DF64) + AKD1000 (NPU)
Add:                 Tesla V100 32GB (FP64 oracle) + P100 16GB (FP64 canary)
Total FP64:          7.0 + 4.7 + 1.48 + 0.56 = 13.74 native TFLOPS
Total DF64:          18.1 + 24.1 = 42.2 TFLOPS
Role split:          V100/P100 = precision validation | 3090/6950 = throughput
```

### Scenario B: Throughput Maximizer ($700-1100 additional)

```
strandGate current:  RTX 3090 + RX 6950 XT + AKD1000
Add:                 V100 32GB (oracle) + RX 6900 XT (DF64 #2)
Total DF64:          18.1 + 24.1 + ~22 = 64.2 TFLOPS
Independent chains:  4 simultaneous Markov chains
Thermalization:      12 remaining configs in ~2 hours vs ~8 hours
```

### Scenario C: Full Arsenal ($1200-1800 additional)

```
strandGate current:  RTX 3090 + RX 6950 XT + AKD1000
Add:                 V100 32GB + RX 6900 XT + P100 16GB
Total native FP64:   7.0 + 4.7 + 1.48 + 0.56 = 13.74 TFLOPS
Total DF64:          18.1 + 24.1 + ~22 = 64.2 TFLOPS
Total VRAM:          24 + 16 + 32 + 16 + 16 = 104 GB
Cards:               5 GPUs + 1 NPU (6 silicon substrates)
```

---

## Power Budget

strandGate PSU: 1600W (assumed Dual EPYC platform)

| Component | TDP | Actual Draw (est.) |
|-----------|-----|-------------------|
| 2× EPYC 7452 | 2×155W = 310W | ~250W typical |
| RTX 3090 | 350W | ~300W under compute |
| RX 6950 XT | 335W | ~280W under compute |
| System (RAM, NVMe, fans) | ~80W | ~80W |
| **Subtotal (current)** | **~910W typical** | |
| Headroom for additional GPU | **~690W** | |

Two additional 250W cards (V100 + P100) = 500W → fits with 190W headroom.
Three additional cards pushes close to limit — would need sequential workloads
or power management via toadStool GlowPlug quota system.

---

## Cross-Gate Distribution

Not all cards belong on strandGate. The ecosystem repurposing principle applies:

| Card | Best Gate | Rationale |
|------|-----------|-----------|
| Tesla V100 32GB | strandGate | Precision oracle for hotQCD paper |
| RX 6900 XT | strandGate | DF64 throughput, proven AMD path |
| Tesla P100 16GB | strandGate or ironGate | Cheap FP64, validation canary |
| Titan (Kepler/Pascal) | biomeGate | Already has Titan V pair, VFIO-managed |
| RX 7900 XTX | strandGate (if VRAM-limited) | Only if 32⁴ is insufficient |
| Budget Radeon | Any gate needing display | Free display GPU from compute duty |

---

## The Science-Hardware Feedback Loop

```
    Measure workload characteristics
              │
              ▼
    Identify bottleneck (DF64 speed? FP64 precision? VRAM? BW?)
              │
              ▼
    Select GPU architecture that addresses bottleneck
              │
              ▼
    Profile new card on identical physics (controlled variable)
              │
              ▼
    Publish comparison in paper (Table: card × metric × physics)
              │
              ▼
    Inform next acquisition (loop)
```

Every GPU purchase produces a paper figure. Every paper figure justifies the next
GPU purchase. The science and hardware co-evolve.

---

*subGen Wave 157a — Science-informed GPU acquisition guide. Key findings: AMD RDNA 2
dominates DF64 workloads (24.1 vs 18.1 TFLOPS, +33%). Tesla V100 at $250-400 is
the highest-value acquisition for precision validation. Budget P100 at $80-150 is
the cheapest path to native FP64. eBay profiling criteria: FP64 ratio ≥ 1:16,
VRAM ≥ 16 GB, HBM2+ bandwidth, ≤350W TDP. Total recommended investment for
Scenario C (full arsenal): $1200-1800 for 5 GPUs + NPU across 6 silicon substrates.*
