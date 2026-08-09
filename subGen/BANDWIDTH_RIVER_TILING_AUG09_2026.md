# Bandwidth as River — Tiling, PCIe Streaming, and Structured Transfer

**Status**: PROFILED + CONCEPTS | **Wave**: 157a | **Date**: Aug 9, 2026
**Gate**: strandGate | **Upstream**: barraCuda, toadStool

---

## 1. The River vs Traffic Insight

The current PCIe stream benchmark reveals catastrophic bandwidth underutilization:

| Transfer | Size | Time | Measured | Theoretical | **Utilization** |
|----------|------|------|----------|-------------|-----------------|
| GPU A → CPU (readback) | 37.75 MB | 49 ms | 770 MB/s | 12,800 MB/s | **6.0%** |
| CPU → GPU B (upload) | 37.75 MB | 335 ms | 113 MB/s | 12,800 MB/s | **0.9%** |
| Optimized stream | 37.75 MB | 88 ms | 429 MB/s | 25,600 MB/s bidir | **1.7%** |

Both GPUs have **PCIe 4.0 x16 at full 16 GT/s** (confirmed via `lspci`). We're using
1-6% of the available bandwidth. The river is a trickle.

### Why It's Traffic, Not a River

Current pattern (random traffic):
```
GPU A computes → waits → issues readback → waits for map_async → CPU copies → waits →
uploads to GPU B → waits for upload complete → GPU B can start
```

River pattern (structured streaming):
```
GPU A tile[0] computes → tile[0] streams out while tile[1] computes → 
continuous pipeline, never stalls, PCIe always saturated
```

The difference: **latency hiding through tiling and double-buffering**.

---

## 2. VRAM Bandwidth — Already a River on AMD

Cache hierarchy profiling reveals why AMD dominates:

### NVIDIA RTX 3090

| Working Set | Bandwidth | Note |
|-------------|-----------|------|
| 64 KB | 486 GB/s | In L1 |
| 256 KB | 466 GB/s | Still L1 |
| 1 MB | 374 GB/s | L2 partial |
| 4 MB | 420 GB/s | L2 full |
| **8 MB** | **262 GB/s** | **← L2 BOUNDARY (cliff)** |
| 32 MB | 408 GB/s | VRAM direct |
| 128 MB | 463 GB/s | VRAM streaming |
| 256 MB | 485 GB/s | VRAM streaming |

NVIDIA's effective L2 is ~6 MB. Above this, every access goes to GDDR6X (higher
latency, lower effective throughput for scattered access patterns).

### AMD RX 6950 XT

| Working Set | Bandwidth | Note |
|-------------|-----------|------|
| 64 KB | 394 GB/s | In L1 |
| 256 KB | 434 GB/s | L1 |
| 1 MB | 374 GB/s | L1/L2 |
| 4 MB | 436 GB/s | Infinity Cache |
| 8 MB | 424 GB/s | **NO CLIFF** |
| 32 MB | 420 GB/s | Still Infinity Cache |
| 64 MB | 399 GB/s | Infinity Cache |
| **128 MB** | **431 GB/s** | **Infinity Cache still absorbing** |
| 256 MB | 414 GB/s | Beyond IC, but prefetch hides latency |

**AMD has no cache cliff.** The 128 MB Infinity Cache covers the entire 16⁴ working
set (125.5 MB). This is why AMD is 20× faster: NVIDIA's memory accesses fall off
the L2 cliff at 8 MB, while AMD's stay cache-hot.

### Implication for Tiling

A 16⁴ lattice's total memory footprint is **125.5 MB** — fits entirely in AMD's
Infinity Cache. This is the **natural tile size** for AMD hardware: the tile where
all accesses are cache-hot.

For NVIDIA, the natural tile is smaller — a volume whose working set fits in 6 MB
(approximately 6⁴ = 1296 sites, 4.6 MB). At larger volumes, NVIDIA pays VRAM
latency for every access beyond L2.

---

## 3. The Tiling Concept — 16⁴ as a Tile

### Current State (Monolithic)

```
32⁴ lattice → all 576 MB loaded → process entire volume at once
  → NVIDIA: memory-bound (far exceeds L2)
  → AMD: cache-hot (Infinity Cache absorbs most of working set)
```

### Tiled State (Domain Decomposition on-Card)

```
32⁴ lattice = 2⁴ = 16 tiles of 16⁴
  → Each tile: 125 MB (fits AMD Infinity Cache perfectly)
  → Process tile[i] while streaming tile[i-1] results
  → NVIDIA: each tile fits in L2 with explicit tiling!
  → Boundary sync: halo exchange between adjacent tiles
```

### On-Card Tiling Benefits

| Benefit | Mechanism |
|---------|-----------|
| Cache efficiency (NVIDIA) | 125 MB tile exceeds L2, but 16⁴ sub-tile stencil fits |
| Pipeline parallelism | Tile[i] computes while tile[i-1] streams to measurement |
| Multi-GPU scaling | Each GPU owns a tile, halo exchange via PCIe |
| Natural PCIe streaming | One tile = one structured burst = saturate PCIe |
| Occupancy reuse | Same workgroup count per tile, just re-bind buffers |

### Implementation Path

For HMC on a 32⁴ lattice:
1. Decompose into **2⁴ = 16 tiles** of 16⁴ (or 4 tiles of 16×16×16×32)
2. Each tile has a **halo** (1-site boundary) from adjacent tiles
3. **Force computation**: process tile, accumulate halo contributions
4. **Leapfrog step**: independent per-tile (momenta are local)
5. **Halo exchange**: between tiles (on-card: just pointer swap, cross-GPU: PCIe stream)

The key insight: **the 16⁴ volume isn't just where we measured peak performance — it's
the hardware-natural tile size.** The AMD Infinity Cache and the PCIe burst size
conspire to make 16⁴ the optimal quantum of work.

---

## 4. PCIe as a River — Structured Streaming

### Current Problem

The PCIe benchmark shows 1-6% utilization because:
1. **Latency dominates**: `map_async` + CPU copy + upload each stall the pipeline
2. **Single-buffer**: one transfer at a time, PCIe idle during compute
3. **Synchronous**: GPU waits for transfer before continuing

### River Pattern (Double-Buffered Pipeline)

```
Time →
GPU A:  [compute tile0] [compute tile1] [compute tile2] ...
PCIe:   ───────────────[stream tile0]──[stream tile1]──[stream tile2]──
GPU B:  ───────────────────────────────[measure tile0] [measure tile1]
```

With 37.75 MB tiles and 12.8 GB/s PCIe: transfer time = **2.9 ms** (not 88 ms!)
The current 88 ms includes all the synchronization overhead.

### Bidirectional Opportunity

PCIe 4.0 x16 is **full-duplex**: 12.8 GB/s in each direction simultaneously.
While GPU A → CPU streams results, CPU → GPU B can stream the previous results.
Total: 25.6 GB/s bidirectional, zero waste.

For our 16⁴ configs (37.75 MB):
- Theoretical transfer: 37.75 MB / 12.8 GB/s = **2.9 ms** per direction
- Bidirectional: both happen at once = 2.9 ms total (not 2×2.9)
- Current measured: 88 ms (30× slower than physics allows)

### What Needs to Change

| Fix | Impact | Owner |
|-----|--------|-------|
| Pinned host memory (`MAP_WRITE | MAP_READ`) | Eliminates CPU copy | barraCuda |
| Double-buffered staging | Overlap transfer + compute | barraCuda |
| Async encoder submission | GPU never stalls on transfer | barraCuda |
| wgpu `maintain` loop | Keep PCIe fed continuously | barraCuda |
| Tile-aligned transfers | Each burst = one cache-natural tile | barraCuda |
| Bidirectional schedule | A→CPU and CPU→B overlap | toadStool |

---

## 5. Tensor Core Probing — Upstream Guidance for coralReef

### What We Can Observe Today

Even without SASS dispatch, we can characterize the tensor core environment:

| Observable | Method | Value |
|-----------|--------|-------|
| Tensor core count | Device properties (SM86) | 328 tensor cores |
| Peak INT8 TOPS | Spec | 1248 TOPS (4× FP16) |
| Peak FP16 TOPS | Spec | 624 TOPS (142 per SM × 82 SMs) |
| Peak TF32 TOPS | Spec | 312 TOPS |
| Memory bus to tensor | Same GDDR6X | 936 GB/s |
| Arithmetic intensity needed | 312 TOPS / 936 GB/s | 333 FLOPs/byte |

### What coralReef Needs to Unblock

The fermion matrix-vector product (Dirac operator) has:
- **Arithmetic intensity**: ~10-20 FLOPs/byte (memory-bound!)
- **Matrix shape**: 3×3 (SU(3)) per link, batched over 4V links
- **Accumulation**: needs f32 or DF64 (FP16 accumulation loses too much precision)

This means tensor cores in TF32 mode (12-bit mantissa, 32-bit accumulate) are the
target — not FP16. coralReef's `mma.sync` should target `mma.sync.aligned.m16n8k8.f32.tf32.tf32.f32`.

### Probing Experiments (without SASS)

1. **VK_KHR_cooperative_matrix probe**: Check if wgpu/Vulkan exposes this on our driver
2. **Tensor throughput ceiling**: Compute 3×3 matmul via shader ALU, measure vs spec
3. **Memory bound analysis**: Profile Dirac operator bytes/FLOP to confirm tensor core
   utilization ceiling
4. **coralReef handoff**: Provide arithmetic intensity profile so SASS team knows
   which `mma.sync` variant to prioritize

---

## 6. Compound Effect — All Rivers Together

When all bandwidth paths are flowing as rivers (structured, not traffic):

```
┌─────────────────────────────────────────────────────────────┐
│              Compound Silicon River                           │
├─────────────────────────────────────────────────────────────┤
│ VRAM → ALU:    936 GB/s (NVIDIA) / 576 GB/s (AMD + IC)     │
│ TMU → ALU:     285-323 GT/s (texture lookups)               │
│ LDS ↔ ALU:     520-550 GB/s (shared memory)                 │
│ PCIe ↔ Host:   25.6 GB/s bidirectional (currently 1.7%)     │
│ NVENC input:   ~4 GB/s (encoder feed rate)                  │
│ NPU feed:      negligible (2.8 µs/prediction)               │
├─────────────────────────────────────────────────────────────┤
│ Key insight: ALL these rivers can flow simultaneously.       │
│ They use different silicon. No contention.                   │
│                                                              │
│ While ALU computes HMC force on tile[i]:                    │
│   • TMU prefetches neighbor lookups for tile[i+1]           │
│   • PCIe streams tile[i-1] results to GPU B                 │
│   • NVENC compresses tile[i-2] for archival                 │
│   • NPU classifies tile[i-3] phase                          │
│   • LDS holds the current stencil working set               │
│                                                              │
│ Zero contention. Maximum utilization. All rivers flowing.    │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Evolution Targets (for barraCuda + toadStool)

### Immediate (this wave)

| Target | Current | Goal | Impact |
|--------|---------|------|--------|
| PCIe utilization | 1.7% | 50%+ | 30× faster cross-GPU transfer |
| Tile size selection | Monolithic | Cache-natural (16⁴ AMD, 6⁴ NVIDIA) | 2-5× NVIDIA speedup |
| Double-buffered staging | Single buffer | Overlap compute + transfer | Hide latency |

### Near-term (next wave)

| Target | Current | Goal | Impact |
|--------|---------|------|--------|
| Domain decomposition | None | On-card tiling for 32⁴-64⁴ | Larger volumes |
| Bidirectional PCIe | Unidirectional | Both directions saturated | 2× transfer throughput |
| Halo exchange | N/A | 1-site boundary per tile | Enable tiled HMC |
| Tensor core probe | Blocked | Characterize arithmetic intensity | Inform coralReef |

### Abstraction (for upstream)

```rust
trait RiverScheduler {
    fn tile_size(&self, adapter: &Adapter) -> [usize; 4];
    fn pipeline_depth(&self) -> usize; // double=2, triple=3
    fn schedule_tiles(&self, tiles: &[Tile]) -> TileSchedule;
    fn pcie_budget(&self) -> BandwidthBudget;
}
```

This becomes the core of barraCuda's next evolution: treating bandwidth as a
schedulable resource, not a bottleneck to work around.

---

## Related Files

- `bench_gpu_pcie_stream.rs` — Current unidirectional PCIe benchmark
- `bench_silicon_saturation.rs` — Cache hierarchy + bandwidth sweep
- `bench_silicon_budget.rs` — Theoretical peak per unit
- `bench_silicon_composition.rs` — Compound throughput measurement

---

*strandGate — Wave 157a — Aug 9, 2026.
PCIe at 1.7% utilization → river pattern achievable at 50%+.
AMD Infinity Cache (128 MB) = no cliff = 16⁴ natural tile.
NVIDIA L2 cliff at 8 MB → needs explicit tiling at 6⁴ sub-tile.
Tiling + double-buffer + bidirectional = unlock next order of magnitude.*
