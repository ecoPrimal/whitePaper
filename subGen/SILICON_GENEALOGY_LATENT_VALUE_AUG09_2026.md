# Silicon Genealogy — Generation-Specific Latent Value Analysis

**Status**: FRAMEWORK | **Wave**: 157a | **Date**: Aug 9, 2026
**Principle**: Every card belongs to a production era with specific silicon capabilities.
Performance differences reveal *architectural features*, not brand superiority.
A newer generation of either vendor may flip measured advantages.

---

## 1. The Genealogy Principle

We are NOT comparing "AMD vs NVIDIA." We are comparing:

- **NVIDIA Ampere (GA102, Sept 2020)** — 2nd gen RT, 3rd gen Tensor, 6 MB L2
- **AMD RDNA2 (Navi21, Nov 2020)** — 1st gen Ray Accelerator, 128 MB Infinity Cache

Each generation has *latent capabilities* — silicon that exists on die but whose
value for scientific computing has never been measured. Our profiling discovers
this latent value.

A future card (RTX 5060, Ada L2 expansion, RDNA4 Infinity Cache v2) will have
DIFFERENT capabilities. Our framework profiles any card's actual silicon, not brand.

---

## 2. strandGate Silicon Census

### Card 0: NVIDIA GeForce RTX 3090 (eVga)

| Property | Value | Production Era |
|----------|-------|----------------|
| **Architecture** | Ampere (GA102) | Sept 2020 |
| **Process** | Samsung 8nm | 2nd gen Samsung |
| **SM Count** | 82 | Full die (GA102) |
| **CUDA Cores** | 10,496 | 128 per SM |
| **Tensor Cores** | 328 (3rd gen) | 4 per SM |
| **RT Cores** | 82 (2nd gen) | 1 per SM |
| **VRAM** | 24 GB GDDR6X | Micron 19.5 Gbps |
| **Memory Bus** | 384-bit | 12× 32-bit channels |
| **L2 Cache** | **6 MB** | ~73 KB per SM |
| **Shared Memory** | 48 KB/SM (max 100 KB config) | Partitioned with L1 |
| **Bandwidth** | 936 GB/s | Theoretical peak |
| **Subgroup Size** | 32 (warp) | Fixed |
| **PCIe** | Gen 4 x16 (16 GT/s) | Full bandwidth |
| **NVENC** | 7th gen (1 encoder) | H.264 + HEVC |
| **Dispatch Model** | GigaThread Engine | Hardware scheduler |
| **Atomic Float** | f32 atomicAdd + f64 atomicAdd | Full float atomic support |

**Latent value discovered:**
- f64 atomicAdd in hardware (unique to Ampere+, AMD lacks this)
- NVENC 61:1 compression at 28 fps on dedicated ASIC
- 6 MB L2 = cache cliff at 8 MB working sets → needs explicit tiling
- Dispatch latency floor of ~10 ms (GigaThread scheduler overhead)
- Tensor cores idle (328 × 64 TOPS = blocked on coralReef SASS)

### Card 1: AMD Radeon RX 6950 XT (XFX)

| Property | Value | Production Era |
|----------|-------|----------------|
| **Architecture** | RDNA2 (Navi21) | Nov 2020 |
| **Process** | TSMC 7nm | 1st gen TSMC N7 |
| **CU Count** | 80 | Full die (Navi21) |
| **Stream Processors** | 5,120 | 64 per CU |
| **Ray Accelerators** | 80 (1st gen) | 1 per CU |
| **VRAM** | 16 GB GDDR6 | 18 Gbps |
| **Memory Bus** | 256-bit | 8× 32-bit channels |
| **Infinity Cache** | **128 MB** | On-die SRAM L3 |
| **L2 Cache** | 4 MB | Plus 128 MB IC above |
| **Shared Memory (LDS)** | 64 KB/CU | Fixed partition |
| **Bandwidth** | 576 GB/s (VRAM) + IC | Effective >> 576 with IC hit |
| **Subgroup Size** | 64 (wave) | Fixed |
| **PCIe** | Gen 4 x16 (16 GT/s) | Full bandwidth |
| **VAAPI** | VCN 3.0 (1 encoder) | H.264 + HEVC |
| **Dispatch Model** | ACE (Asynchronous Compute Engine) | 4× ACE hardware |
| **Atomic Float** | f32/f64 compare-swap only | **NO** float atomicAdd |

**Latent value discovered:**
- 128 MB Infinity Cache = NO cache cliff from 64 KB to 128 MB
- 16⁴ lattice (125 MB) fits entirely in Infinity Cache → near-linear scaling
- Wave64 = fewer subgroups per WG → fewer barriers → less sync overhead
- ACE dispatch = lower latency than GigaThread for small workloads
- 20× HMC advantage is an INFINITY CACHE effect, not a "GPU speed" effect
- VAAPI compression at 20:1 (less efficient than NVENC, different encode ASIC)
- f64 atomicAdd ABSENT — must use reduction trees or ROP blend for accumulation

---

## 3. MEASURED Results — Aug 9, 2026

### Headline: NVIDIA Wins Raw Everything. AMD Wins Lattice QCD.

```
                          Metric  Ampere GA102 (2020)  RDNA2 Navi21 (2020)  NVIDIA advantage
  ─────────────────────────────────────────────────────────────────────────────────────────
  Effective cache (measured):       256 MB                64 MB              4.0×
  Dispatch floor:                    66.7 µs            125.1 µs            1.87×
  FP32 throughput:                 4796.3 GFLOP/s      3656.9 GFLOP/s       1.31×
  DF64 throughput (est):            479.6 GFLOP/s       365.7 GFLOP/s       1.31×
  Sustained bandwidth (copy):       614.6 GB/s          410.5 GB/s          1.50×
  Atomic i32 throughput:            238.6 Gatom/s       191.0 Gatom/s       1.25×
  Natural tile (QCD sites):          12⁴                  9⁴
```

**Yet AMD is 20× faster at 16⁴ HMC.** Why?

### The Intra-Dispatch Working Set Explanation (MEASURED)

Simple access pattern tests show only modest differences:
- Linear 64 MB: AMD 1.32× faster (IC sweet spot)
- Strided 64 MB: AMD 1.11× faster (barely)
- At 128 MB: NVIDIA wins both (1.5-1.7×)

But HMC shows **10-20× AMD advantage**. We tested the "inter-dispatch cache
persistence" hypothesis by varying MD step count at 12⁴:

```
DISPATCH COUNT SCALING (12⁴ = 20,736 sites, 11.4 MB link buffer):
  Steps  NVIDIA    AMD        Ratio   Per-dispatch
  ──────────────────────────────────────────────
     2    41.7 ms   3.9 ms    10.6×   NV: 2,603 µs, AMD: 245 µs
     5    99.5 ms   8.2 ms    12.2×   NV: 2,488 µs, AMD: 205 µs
    10   195.2 ms  12.9 ms    15.1×   NV: 2,439 µs, AMD: 162 µs
    20   389.5 ms  38.3 ms    10.2×   NV: 2,434 µs, AMD: 239 µs
    40   776.7 ms  77.2 ms    10.1×   NV: 2,427 µs, AMD: 241 µs
```

**Key finding: BOTH CARDS SCALE LINEARLY.** The ratio is ~10× and CONSTANT.
The gap is NOT from inter-dispatch cache eviction (hypothesis DISPROVEN).

The true explanation is **INTRA-DISPATCH working set thrashing**:

Each force kernel thread needs:
- Link data at current site + 6 staple directions × 4 offsets = ~24 random sites
- Neighbor table lookup per access
- Total active working set per dispatch: links + momenta + force ≈ **34 MB**

**NVIDIA 6 MB L2**: 34 MB >> 6 MB → every staple lookup goes to VRAM (~300 ns)
**AMD 128 MB IC**: 34 MB << 128 MB → every staple lookup hits IC (~30 ns)

This 10× latency difference per memory access explains the 10× per-dispatch gap.
The gap grows with VOLUME (more active data per dispatch) but is constant with
step count (same working set per dispatch regardless of how many steps).

**Volume scaling explained by working set vs cache size:**
```
  4⁴:   Working set ~0.5 MB  → fits in NVIDIA L2    → ratio  2.1×
  8⁴:   Working set ~7.4 MB  → barely exceeds L2    → ratio  5.1×
 12⁴:   Working set ~34 MB   → far exceeds L2       → ratio 17.5×
 16⁴:   Working set ~113 MB  → massively exceeds L2 → ratio 19.6×
                                but fits in 128 MB IC     (AMD ceiling)
```

**Implication for future cards**: Need L2 ≥ working set for competitive performance.
- 12⁴ needs 34 MB L2 → Ada Lovelace (96 MB) would be competitive
- 16⁴ needs 113 MB L2 → only IC-class cards (RDNA2+) can hold this
- A 5060 with 48 MB L2 would close the gap at 12⁴ but still lose at 16⁴

### Other Measured Corrections

| Earlier Assumption | Measured Reality | Correction |
|-------------------|-----------------|-----------|
| NVIDIA dispatch floor ~10 ms | **66.7 µs** | GigaThread is fast, earlier measure included HMC overhead |
| AMD dispatch faster | **125.1 µs** (2× slower) | ACE dispatch is NOT faster for single-queue |
| AMD "no cache cliff" | Cliff at **64 MB** (1.66× drop) | IC is 128 MB but effective boundary is ~64 MB for copy |
| NVIDIA "6 MB L2 cliff" | No cliff in copy (linear access) | L2 manages linear access fine; STRIDED access reveals cliff |

### Critical Insight: A 5060 Might Flip Everything

NVIDIA Ada Lovelace (RTX 40 series) has:
- **96 MB L2 cache** (vs 6 MB on 3090) — closes gap for lattices up to ~80 MB working set
- **Dual NVENC** (2× encode throughput)
- **3rd gen RT cores** (faster BVH traversal)
- **4th gen Tensor cores** (FP8 support)
- **Optical flow accelerator** (motion estimation in hardware)
- **SM 8.9 dispatch** (lower latency than 8.6)

A hypothetical RTX 5060 (Blackwell, smaller die) might have:
- 32-48 MB L2 (larger than 3090's 6 MB, still smaller than IC at 16⁴)
- Lower dispatch latency (already 2× faster than AMD)
- Better power efficiency (4nm vs 8nm)
- The 20× AMD advantage may shrink to 2-3× or flip entirely at volumes ≤12⁴

The CORRECT experiment is: **profile each card's cache hierarchy boundary,
dispatch latency floor, and arithmetic intensity ceiling — then route accordingly.**
The WRONG experiment is: "NVIDIA is slow, use AMD."

---

## 4. Generation-Neutral Profiling Framework

### What To Measure Per Card (Brand-Agnostic)

```
SiliconProfile {
    // Cache hierarchy
    l2_boundary_bytes: usize,       // Where bandwidth drops (NVIDIA: 8MB, AMD: 128MB)
    effective_cache_bytes: usize,   // Total accessible fast storage
    cache_hit_bandwidth_gbps: f64,  // Bandwidth when working set fits cache
    cache_miss_bandwidth_gbps: f64, // Bandwidth beyond cache boundary
    
    // Dispatch model
    dispatch_latency_floor_us: f64, // Minimum time for any dispatch (NVIDIA: ~10ms!)
    dispatch_overhead_per_wg: f64,  // Per-workgroup scheduling cost
    
    // Compute density
    fp32_tflops: f64,               // Raw ALU throughput
    df64_tflops: f64,               // Emulated double precision
    native_f64_tflops: f64,         // Hardware f64 (if available)
    
    // Fixed-function
    has_float_atomic_add: bool,     // f32/f64 atomicAdd (NVIDIA yes, AMD no)
    has_tensor_cores: bool,         // Matrix multiply accelerator
    has_rt_bvh: bool,               // Hardware BVH traversal
    encode_asic: Option<EncodeAsic>, // Video encode silicon
    
    // Memory model
    subgroup_size: u32,             // 32 (NVIDIA) vs 64 (AMD)
    shared_memory_bytes: u32,       // Per-workgroup LDS
    max_buffer_size: u64,           // Per-buffer VRAM limit
    
    // Natural tile size (derived)
    natural_tile_volume: usize,     // Volume where cache_hit_bandwidth dominates
}
```

### Routing Decision (Per-Card, Not Per-Brand)

```
fn optimal_route(profile: &SiliconProfile, lattice_bytes: usize) -> WorkloadDecision {
    if lattice_bytes <= profile.effective_cache_bytes {
        // Working set fits in cache → this card is optimal for monolithic
        WorkloadDecision::Monolithic
    } else {
        // Needs tiling → tile size = effective_cache_bytes / buffers_per_tile
        let tile_size = profile.effective_cache_bytes / 6; // 6 buffers in HMC
        WorkloadDecision::Tiled { tile_volume: tile_size / bytes_per_site }
    }
}
```

This framework works for ANY card: RTX 3090, RX 6950 XT, RTX 5060, Intel Arc A770,
or a future AMD RDNA4 card. The measurement determines routing, not the label.

---

## 5. Latent Value Catalog

"Latent value" = silicon on the card whose scientific utility was unknown until profiled.

### RTX 3090 (Ampere GA102) — Latent Value Discovered

| Silicon | Latent Value | Discovered | Status |
|---------|-------------|------------|--------|
| NVENC (7th gen) | 61:1 config compression at 28 fps | Aug 9, 2026 | ACTIVATED |
| f64 atomicAdd | CG accumulation without reduction trees | Aug 9, 2026 | AVAILABLE |
| f32 atomicAdd | Force accumulation at full f32 precision | Aug 9, 2026 | AVAILABLE |
| RT Cores (2nd gen) | BVH for lattice spatial queries | Aug 9 | API CONFIRMED (EXPERIMENTAL_RAY_QUERY=YES) |
| Tensor Cores (3rd gen) | 312 TF32 TOPS for matmul | — | BLOCKED (coralReef SASS) |
| SHADER_F16 | Half-precision folding for DF32 | Aug 9 | API CONFIRMED |
| 6 MB L2 | Working set boundary: 5.1× penalty at 8⁴ | Aug 9, 2026 | CHARACTERIZED |
| Dispatch floor | 66.7 µs (2× faster than AMD) | Aug 9, 2026 | MEASURED |
| FP32 throughput | 4796 GFLOP/s | Aug 9, 2026 | MEASURED |
| Subgroup (warp32) | 15.2 Gelem/s reduction | Aug 9, 2026 | ACTIVATED |
| TMU bilinear | 15.7 Gsamp/s multigrid interpolation | Aug 9, 2026 | ACTIVATED |

### RX 6950 XT (RDNA2 Navi21) — Latent Value Discovered

| Silicon | Latent Value | Discovered | Status |
|---------|-------------|------------|--------|
| 128 MB Infinity Cache | 20× QCD advantage at 16⁴ | Aug 9, 2026 | KEY ADVANTAGE |
| Cache cliff | 1.66× drop at 64 MB (linear), but no cliff for lattice QCD | Aug 9, 2026 | CHARACTERIZED |
| Wave64 | 9.67 Gelem/s reduction (wide lanes) | Aug 8, 2026 | ACTIVATED |
| ACE dispatch | 125.1 µs floor (slower than NVIDIA!) | Aug 9, 2026 | MEASURED |
| VAAPI (VCN 3.0) | 20:1 compression at 33 fps | Aug 9, 2026 | ACTIVATED |
| Ray Accelerator (1st gen) | BVH traversal | Aug 9 | API CONFIRMED (EXPERIMENTAL_RAY_QUERY=YES) |
| SHADER_F16 | Half-precision folding for DF32 | Aug 9 | API CONFIRMED |
| ROP atomics | 117.7 Gatom/s (6.35× NVIDIA) | Prior wave | ACTIVATED |
| buffer_size = i32::MAX | Vendor-specific limit requiring negotiation | Aug 9, 2026 | FIXED |
| No f64 atomicAdd | Forces reduction tree pattern (portable) | Aug 9, 2026 | CHARACTERIZED |
| FP32 throughput | 3657 GFLOP/s | Aug 9, 2026 | MEASURED |
| Sustained BW | 410.5 GB/s (614 GB/s NVIDIA) | Aug 9, 2026 | MEASURED |

### AKD1000 NPU — Latent Value Discovered

| Silicon | Latent Value | Discovered |
|---------|-------------|------------|
| 80 neural processors | Phase classification at 30 mW | Aug 7, 2026 |
| 10 MB SRAM | ESN weights fit entirely on-chip | Aug 7, 2026 |
| PCIe x4 | Negligible bus contention | Aug 8, 2026 |
| 2.8 µs inference | 0.02% trajectory overhead | Aug 9, 2026 |
| Adaptive steering | 62% compute savings | Aug 9, 2026 |

---

## 6. Future Card Predictions (Testable Hypotheses)

### RTX 5060 (Blackwell, hypothetical)

If L2 expands to 48 MB:
- **Hypothesis**: Cache cliff moves from 8 MB to 48 MB
- **Prediction**: 16⁴ (125 MB) still exceeds L2, but 12⁴ (73 MB) might fit → NVIDIA competitive at 12⁴
- **Test**: Run cache hierarchy sweep, find boundary

If dispatch latency drops to 1 ms:
- **Hypothesis**: NVIDIA competitive at small volumes
- **Prediction**: 4⁴-6⁴ performance matches AMD
- **Test**: Volume scaling sweep, find dispatch floor

### RX 8800 XT (RDNA4, hypothetical)

If Infinity Cache drops to 64 MB (cost reduction):
- **Hypothesis**: Cache cliff appears at 64 MB
- **Prediction**: 12⁴ (73 MB) exceeds IC → performance cliff
- **Test**: Same cache hierarchy sweep

If wave32 mode available:
- **Hypothesis**: Better occupancy for small workloads
- **Prediction**: Small-volume performance improves
- **Test**: Compare wave32 vs wave64 via subgroup size control

### Intel Arc A770 (Alchemist, available now)

| Property | Expected | To Measure |
|----------|----------|-----------|
| L2 Cache | 16 MB | Cache hierarchy sweep |
| Dispatch model | Xe-HPG | Dispatch floor measurement |
| Subgroup | 8-32 (variable) | Subgroup size control |
| XMX (tensor) | 16 TOPS | Matrix multiply ceiling |
| HW RT | Gen 1 | BVH traversal throughput |
| QSV (encode) | AV1 + H.264 | Compression ratio measurement |

---

## 7. The Production Era Model

Each card belongs to a production era. Our framework treats them as:

```
ProductionEra {
    card: CardIdentity,
    silicon_profile: SiliconProfile,      // Measured capabilities
    latent_value: Vec<LatentCapability>,   // Discovered unused silicon
    natural_tile: TileConfig,             // Hardware-optimal quantum of work
    routing_role: WorkloadRole,           // What this era excels at
    generation_peers: Vec<CardIdentity>,  // Other cards from same era
}
```

When a new card arrives (Radeon M150, Titan, Tesla, Intel Arc, retired HBM2):
1. Run `SiliconProfile` measurement suite (cache hierarchy, dispatch floor, ALU throughput)
2. Discover latent value (encode ASIC, atomic capabilities, fixed-function units)
3. Determine natural tile size (where cache dominates)
4. Assign routing role (production, oracle, compression, classification)
5. Compare to generation peers (what's better/worse than same-era cards)

This framework makes hardware acquisition scientific: buy the era/capability
that fills a measured gap, not the brand with the best marketing.

---

## 8. Additional Silicon Unit Measurements

### Subgroup Operations (Warp32 vs Wave64)

| Operation | NVIDIA (warp32) | AMD (wave64) | NVIDIA advantage |
|-----------|----------------|--------------|-----------------|
| Subgroup reduce | 0.069 ms (15.2 Gelem/s) | 0.108 ms (9.67 Gelem/s) | 1.57× |
| TMU bilinear | 0.0042 ms (15.7 Gsamp/s) | 0.0076 ms (8.66 Gsamp/s) | 1.81× |
| Indirect dispatch | 0.0183 ms/cycle | 0.0208 ms/cycle | 1.14× |

NVIDIA's warp32 with more SMs outperforms AMD's wave64 at fixed-function operations.
This is consistent with NVIDIA's 1.3× raw FP32 advantage. These are unit-level
measurements, not affected by cache hierarchy.

---

## 9. Complete Generational Summary

```
╔════════════════════════════════════════════════════════════════════════╗
║  NVIDIA Ampere GA102 (RTX 3090, 2020)                                ║
║  Production Role: Oracle, Encode, Small-Volume                        ║
╟────────────────────────────────────────────────────────────────────────╢
║  WINS: Raw FP32 (4796 GF), bandwidth (614 GB/s), dispatch (67 µs),  ║
║        subgroup (15.2 Gelem/s), atomics (238 Gatom/s), NVENC (61:1), ║
║        f64 atomicAdd (hardware), tensor cores (blocked on SASS)       ║
║  LOSES: QCD at 12⁴+ (working set exceeds 6 MB L2 → VRAM thrashing)  ║
║  NATURAL SIZE: ≤8⁴ (working set fits in L2)                          ║
║  LATENT VALUE: $0.10/hr at peak; encode silicon free during compute  ║
╚════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════╗
║  AMD RDNA2 Navi21 (RX 6950 XT, 2020)                                ║
║  Production Role: Primary QCD Production Engine                       ║
╟────────────────────────────────────────────────────────────────────────╢
║  WINS: Lattice QCD 10-20× (128 MB IC absorbs working set),          ║
║        linear scaling through 16⁴, wave64 (fewer barriers),          ║
║        ROP atomics (6.35× NVIDIA for additive blend)                  ║
║  LOSES: Raw everything (compute, bandwidth, dispatch, subgroup),     ║
║         f64 atomicAdd (absent), encode quality (VAAPI 20:1 vs 61:1)  ║
║  NATURAL SIZE: ≤16⁴ (working set fits in 128 MB IC)                  ║
║  LATENT VALUE: 20× QCD throughput at production volumes               ║
╚════════════════════════════════════════════════════════════════════════╝
```

---

## 10. Hardware Acquisition Guidance (Science-Informed)

### What to buy for QCD:

| Need | Buy | Reason |
|------|-----|--------|
| Max QCD throughput at 16⁴ | AMD RDNA2 (6800XT/6900XT/6950XT) | 128 MB IC, proven 20× |
| Max QCD at 32⁴+ | Need tiling regardless | No single card holds it |
| Oracle/validation | Keep NVIDIA | f64 atomicAdd, higher raw precision |
| Video archival | Keep NVIDIA | NVENC 61:1 compression |
| Future-proof | RTX 5060/5070 (48+ MB L2) | May close the gap |
| Budget | Used 6800XT ($200-250) | Same IC as 6950 XT |
| Exotic | Intel Arc A770 | Third data point, 16 MB L2 |

### Cards to avoid for this workload:

| Card | Why |
|------|-----|
| NVIDIA 2080/1080 (pre-Ampere) | No f64 atomicAdd, smaller L2 |
| AMD RDNA3 (7900 XTX) | 96 MB IC (LESS than 6950 XT's 128 MB!) |
| Anything with <64 MB effective cache | Will thrash at 12⁴+ |

### Counterintuitive insight for eBay shopping:

**The RX 6950 XT (128 MB IC) is BETTER for QCD than the newer RX 7900 XTX (96 MB IC).**
This is because AMD reduced IC size in RDNA3 to save die area. For our specific
workload, the older generation has more latent value. Always measure, never assume
newer = better.

---

## 11. Immediate Next Steps

1. **Intel Arc A770 acquisition** — third generation data point (Xe-HPG, 16 MB L2)
2. **Test RX 7900 XTX** — verify the RDNA3 IC regression hypothesis
3. **Profile used Radeon M150** — HBM2 changes the bandwidth equation entirely
4. **Test Titans/Tesla** — HPC-class cards with large L2 may compete
5. **RTX 5060 when available** — verify Ada/Blackwell L2 expansion helps

---

## 12. Validated Binaries

| Binary | Purpose | Status |
|--------|---------|--------|
| `bench_silicon_genealogy` | Full SiliconProfile per card | VALIDATED |
| `bench_access_pattern_era` | Linear vs strided per generation | VALIDATED |
| `bench_dispatch_count_scaling` | Cache persistence proof | VALIDATED |
| `bench_silicon_volume_scaling` | Volume-dependent advantage | VALIDATED |
| `bench_advanced_silicon` | Subgroup, TMU, indirect | VALIDATED |
| `bench_silicon_force_paths` | HMC force accumulation | VALIDATED |
| `bench_silicon_saturation` | Cache hierarchy sweep | VALIDATED |

---

*strandGate — Wave 157a — Aug 9, 2026.
Silicon genealogy framework: generation-specific, not brand-specific.
Every card's advantage traces to specific silicon (cache size, atomic units, dispatch model).
A newer generation of either vendor could flip current rankings.
The measurement determines routing, not the label.
Key discovery: 20× AMD advantage = intra-dispatch working set thrashing on NVIDIA's 6 MB L2.
RDNA2's 128 MB IC absorbs the full QCD working set. This is GENERATIONAL, not brand.*
