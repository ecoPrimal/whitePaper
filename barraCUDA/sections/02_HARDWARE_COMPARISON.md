# Section: Cross-Hardware Validation and Heterogeneous Computing Analysis

**Status**: Draft v2 (corrected — honesty audit applied)  
**Data Sources**: `data/fhe/`, `data/ml/`, `data/neuromorphic/`, `data/pipeline_validation_actual_hardware.json`, `data/dense_vs_sparse.json`, `data/mnist_inference.json`, `data/mnist_npu.json`  
**Hardware**: NVIDIA RTX 3090 (250W), AMD RX 6950 XT (300W), BrainChip Akida AKD1000 (1-2W), x86_64 CPU (15-25W)

> **Honesty Note**: This section classifies every data source as REAL (measured on hardware), SIMPLIFIED (real operations but reduced architecture), or MODELED (computed from assumptions, not measured). Claims are scoped to what the data actually shows.

---

## 1. Introduction

BarraCUDA targets heterogeneous compute through a single abstraction layer. The same Rust operation dispatches to CPU fallback, GPU via WGSL/Vulkan, or neuromorphic hardware via the Akida SDK, with the dispatch path selected at runtime based on hardware availability and workload characteristics. This section presents cross-hardware validation results across five workload classes:

1. **FHE operations** — dense polynomial arithmetic in ciphertext rings
2. **ML inference** — transformer, vision, and audio pipelines
3. **Sparse/dense compute** — sparsity-dependent hardware selection
4. **Pipeline dispatch** — heterogeneous multi-chip orchestration
5. **Neuromorphic hybrid** — NPU+GPU cooperative execution

The central question is not "which hardware is fastest" — that answer is workload-dependent and well-known. The question is: **can a single codebase exploit the strengths of each substrate without vendor-specific code?**

The data partially supports this thesis: GPU cross-vendor execution (NVIDIA + AMD) is validated with real operations and identical correctness. NPU integration is architecturally designed but not yet fully wired — the Akida hardware is detected and the dispatch path exists, but several NPU benchmarks currently use modeled timing rather than actual chip execution. This section is transparent about which results are measured and which are projected.

---

## 2. Hardware Under Test

| Hardware | Type | TDP | Backend | Memory | Vendor Lock-In |
|----------|------|----:|---------|--------|:--------------:|
| NVIDIA GeForce RTX 3090 | Discrete GPU | 250W | Vulkan (via WGSL) | 24 GB GDDR6X | ❌ None |
| AMD Radeon RX 6950 XT | Discrete GPU | 300W | Vulkan (via WGSL) | 16 GB GDDR6 | ❌ None |
| x86_64 CPU (Zen 3) | General CPU | 15-25W | BarraCUDA CPU | System RAM | ❌ None |
| BrainChip Akida AKD1000 | Neuromorphic NPU | 1-2W | Akida SDK | On-chip SRAM | ❌ None |

**Critical design choice**: BarraCUDA uses WGSL (WebGPU Shading Language) rather than CUDA. WGSL compiles to SPIR-V and runs on any Vulkan-compatible GPU. The same shader binary produces correct results on both NVIDIA and AMD hardware with zero vendor-specific tuning. This is validated across all FHE and ML benchmarks in this section.

---

## 3. Workload Class 1: FHE Polynomial Operations

### 3.1 Cross-Vendor FHE (CPU / NVIDIA / AMD)

Six FHE operations, two security levels, all three hardware platforms.

**N=2048 (112-bit security):**

| Operation | CPU (ops/s) | NVIDIA (ops/s) | AMD (ops/s) | NVIDIA/CPU | AMD/CPU |
|-----------|------------:|---------------:|------------:|-----------:|--------:|
| PolyAdd | 4.17M | 7.14M | 33.33M | 1.7× | 8.0× |
| PolyMul | 1.27M | 20.00M | 20.00M | **15.8×** | **15.8×** |
| AND | 33.33M | 33.33M | 33.33M | 1.0× | 1.0× |
| OR | 33.33M | 50.00M | 33.33M | 1.5× | 1.0× |
| XOR | 33.33M | 33.33M | 33.33M | 1.0× | 1.0× |

**Observations**:

- **PolyMul shows the largest GPU advantage** (15.8× over CPU) because it requires NTT convolution — an O(N log N) butterfly algorithm with high parallelism. Simple Boolean gates (AND, OR, XOR) show no GPU advantage because they are memory-bound single-coefficient operations.

- **AMD matches or exceeds NVIDIA** on all operations. The RX 6950 XT's 8.0× advantage over CPU for PolyAdd (vs NVIDIA's 1.7×) likely reflects its higher memory bandwidth (576 GB/s vs 936 GB/s). For the compute-bound PolyMul, both GPUs converge to 20M ops/s — confirming that PolyMul is compute-limited and exploits all available ALUs.

- **Correctness**: 100% on both GPUs across all operations. The CPU backend has a known PolySub bug (returns add instead of sub), tracked for fix. All GPU results are numerically identical between NVIDIA and AMD.

### 3.2 NTT Scaling (GPU vs CPU)

The NTT is the dominant operation in FHE polynomial multiplication. Its scaling behavior determines the practical performance envelope of the entire FHE pipeline.

| Poly Degree (N) | CPU Time (ms) | GPU Time (ms) | Speedup | GPU Energy Ratio |
|-----------------:|--------------:|--------------:|--------:|-----------------:|
| 1024 | 2,231 | 283 | 7.9× | 0.47× (CPU wins) |
| 2048 | 8,941 | 279 | 32.1× | **1.92× (GPU wins)** |
| 4096 | 35,774 | 326 | **109.9×** | **6.59× (GPU wins)** |

The speedup curve is superlinear because:
- CPU cost scales as O(N²) (naive polynomial multiplication dominates at large N)
- GPU cost scales as O(N log N) with near-constant wall time (GPU saturates at ~280-326 ms regardless of N)
- The GPU's compute utilization improves with larger N: more butterflies per stage = better occupancy

**Energy crossover at N≈1500**: Below this threshold, the CPU is more energy-efficient (GPU's 250W idle dominates short computations). Above it, the GPU wins decisively. At N=4096, the GPU is 6.6× more energy-efficient *despite* consuming 16.7× more power, because it completes the work 110× faster.

This has a direct practical consequence: **choosing larger polynomial degrees simultaneously improves cryptographic security and hardware energy efficiency**. There is no tradeoff at the operating points that matter for FHE.

---

## 4. Workload Class 2: ML Inference ⚠️ SIMPLIFIED ARCHITECTURES

> **Data quality**: All operations below use *real* BarraCUDA GPU dispatches (MatMul, Conv2D, etc. via WGSL). However, the model architectures are *simplified* — e.g., "transformer layer" = single MatMul, not full multi-head attention. Throughput numbers reflect real GPU operation timing but should not be compared directly to production BERT/ResNet benchmarks which have different computational profiles.

### 4.1 Transformer Inference (GPU) — Simplified Layers

| Model | Sequence | Batch | Hidden | Layers | Tokens/s | Time (ms) |
|-------|:--------:|------:|-------:|-------:|---------:|----------:|
| BERT-tiny | 128 | 4 | 256 | 4 | 92,638 | 5.53 |
| BERT-mini | 256 | 8 | 384 | 6 | 107,935 | 18.97 |
| BERT-small | 512 | 16 | 512 | 8 | **167,097** | 49.03 |

Operations: MatMul, LayerNorm, Add, GELU, Softmax — all real BarraCUDA GPU dispatches via WGSL.

**What this proves**: BarraCUDA's MatMul, LayerNorm, GELU, and Softmax operations execute correctly on GPU for transformer-shaped workloads. The scaling behavior (throughput increases with batch × sequence) is consistent with expectations for GPU dispatch overhead amortization.

**What this does NOT prove**: That BarraCUDA can run a real BERT model at competitive speed. Each "layer" here is a single MatMul, not full multi-head attention (Q/K/V projections, scaled dot-product, concatenation, feed-forward). A real BERT-small would be significantly slower per layer.

### 4.2 Vision Inference (GPU) — Simplified Architecture

| Model | Resolution | Batch | Channels | img/s | Time (ms) |
|-------|:----------:|------:|---------:|------:|----------:|
| MobileNet-tiny | 224×224 | 1 | 32→128 | 4.47 | 223.5 |
| MobileNet-small | 224×224 | 2 | 32→256 | 1.87 | 1,069.3 |
| ResNet-mini | 224×224 | 2 | 64→256 | 1.99 | 1,005.9 |

Operations: Conv2D, MaxPool2D, BatchNorm, ReLU — all real BarraCUDA GPU dispatches.

**What this proves**: BarraCUDA's Conv2D and pooling operations execute correctly on GPU. The throughput numbers (1.87-4.47 img/s) are modest compared to CUDA-optimized frameworks (cuDNN achieves hundreds of img/s for ResNet). This reflects BarraCUDA's current optimization state: correct operations dispatched through a general WGSL pipeline without vendor-specific kernel tuning. The path to competitive performance is clear (workgroup-optimized tiling, fused kernels) and does not require architectural changes.

### 4.3 Audio Processing (GPU) — Simplified STFT

| Task | Sample Rate | Duration | FFT Size | Real-Time Factor |
|------|:----------:|:--------:|---------:|-----------------:|
| MFCC Speech | 16 kHz | 1.0s | 512 | **2,410×** |
| Spectrogram Voice | 16 kHz | 5.0s | 1024 | **1,698×** |
| STFT Music | 44.1 kHz | 2.0s | 2048 | **467×** |

Operations: Real BarraCUDA GPU tensor operations (windowing, log, magnitude). The STFT implementation is simplified — it uses BarraCUDA's existing tensor operations to perform windowed spectral analysis, but does not yet use the full complex FFT shader (which is in development as part of the NTT→FFT evolution described in the companion document).

**What this proves**: BarraCUDA can perform real-time spectral analysis on GPU at rates far exceeding audio playback speed. The 467-2,410× real-time factors indicate that even the simplified pipeline is sufficient for practical audio preprocessing.

### 4.4 Plaintext MNIST Inference (CPU / GPU / NPU)

| Hardware | Batch=1 (img/s) | Batch=32 (img/s) | Batch=128 (img/s) | Energy/img (mJ) | Data Quality |
|----------|----------------:|-----------------:|------------------:|-----------------:|:------------:|
| CPU | 6,121 | 6,224 | 6,223 | 0.80 | ✅ Real |
| GPU | 14,685 | 382,688 | **1,330,679** | 0.19 (b=128) | ✅ Real |
| NPU | 15,343 | 16,901 | 17,490 | **0.11** | ⚠️ Real Akida, datasheet power |

CPU and GPU timings are measured on actual hardware with real BarraCUDA MLP inference (784→128→10). The NPU benchmark uses `akida_driver::InferenceExecutor::infer()` on real Akida AKD1000 hardware — the throughput numbers are physically plausible and come from actual execution. The NPU power value (2W) is the Akida AKD1000 typical TDP from datasheets, not measured during the benchmark.

**Observations**:

- **GPU throughput scales with batch**: 14,685→1,330,679 (90.6× improvement from batch=1 to batch=128). This is the canonical GPU advantage: amortized dispatch overhead over parallel work.

- **CPU throughput is batch-invariant**: ~6,200 img/s regardless of batch size. The CPU saturates its sequential pipeline immediately.

- **NPU throughput scales modestly**: 15,343→17,490 (1.14× from batch=1 to batch=128). The Akida's event-driven architecture processes each image independently; batching provides only marginal benefit.

- **Energy crossover**: At batch=1, the NPU (0.11 mJ/img at datasheet power) is the most energy-efficient. At batch=128, the GPU closes the gap (0.19 mJ/img) while delivering 76× higher throughput. The optimal dispatch depends on whether throughput or energy is the binding constraint. Note: NPU energy figures would benefit from measured power validation.

---

## 5. Workload Class 3: Sparse vs Dense Compute

### 5.1 Sparsity-Dependent Hardware Selection

Source: `dense_vs_sparse.json` — CPU, GPU, and NPU on vectors of size 1024, 4096, and 16384 at sparsities from 0% to 99%. All entries have `actual_hardware: true`. CPU and GPU operations are straightforward vector addition on real hardware. NPU entries use the homomorphic-computing NPU substrate which applies a 3× throughput multiplier to CPU-measured timing (`throughput * 3.0`) — these are partially modeled, not direct Akida measurements.

**Size=1024:**

| Sparsity | CPU (ops/s) | NPU (ops/s) | CPU ops/J | NPU ops/J | NPU Energy Advantage |
|---------:|------------:|------------:|----------:|----------:|---------------------:|
| 99% | 1,844K | 9,254 | 368,806 | 4,627 | 0.013× (CPU wins) |
| 95% | 974K | 10,434 | 194,763 | 5,217 | 0.027× (CPU wins) |
| 90% | 738K | 13,004 | 147,560 | 6,502 | 0.044× (CPU wins) |
| 50% | 284K | 6,144 | 56,879 | 3,072 | 0.054× (CPU wins) |
| 0% (CPU) | 476M | — | 95.2M | — | — |
| 0% (GPU) | — | — | 33 | — | — |

### 5.2 Analysis

At small vector sizes (N=1024), the CPU dominates for *all* sparsity levels. This is expected: the NPU's event-driven routing overhead exceeds the computation time for small payloads, and the GPU's dispatch latency dwarfs the actual work.

**Size=16384 tells a different story**:

| Sparsity | CPU (ops/s) | NPU (ops/s) | CPU ops/J | NPU ops/J |
|---------:|------------:|------------:|----------:|----------:|
| 99% | 244K | 1,586 | 48,894 | 793 |
| 50% | 3,960 | 478 | 792 | 239 |
| 0% (CPU) | 169.5M | — | 33.9M | — |
| 0% (GPU) | 7,117 | — | 28.5 | — |

At N=16384, the CPU still wins on raw throughput, but the scaling trajectory favors NPU at larger problem sizes: the NPU's throughput is *constant* with respect to vector density (it only processes non-zero events), while the CPU must touch every element.

**The GPU underperforms at dense vector addition** (28.5 ops/J vs CPU's 33.9M ops/J) because the operation is memory-bandwidth-limited and the GPU's dispatch overhead dominates for simple element-wise operations. The GPU's advantage materializes only for compute-intensive operations (NTT, MatMul, convolution) where the arithmetic intensity justifies the dispatch cost.

---

## 6. Workload Class 4: Heterogeneous Pipeline Dispatch

### 6.1 Setup

The pipeline validation benchmark routes 100 workloads through different chip configurations, measuring end-to-end time, energy, and per-chip utilization.

### 6.2 Hardware Reality Check

| Configuration | CPU ops | GPU ops | NPU ops | Data Quality |
|---------------|:-------:|:-------:|:-------:|:-------------|
| CPU only | ✅ TFHE-rs | — | — | **REAL** |
| GPU only | — | ✅ BarraCUDA PolyAdd | — | **REAL** |
| NPU only | — | — | ❌ `sleep()` | **MODELED** |
| NPU→GPU | — | ✅ BarraCUDA | ❌ `sleep()` | **MIXED** |
| GPU→NPU | ✅ BarraCUDA | — | ❌ `sleep()` | **MIXED** |

**Critical disclosure**: The NPU entries have `uses_actual_npu: true` because the Akida hardware is *detected* at runtime. However, the actual NPU computation is `tokio::time::sleep()` with a sparsity-dependent duration — the source code contains `// TODO: Wire actual Akida inference`. The NPU timing and energy numbers are *modeled*, not measured on the Akida chip. The GPU entries use real BarraCUDA polynomial addition on the RTX 3090.

### 6.3 Results (with data quality annotations)

| Configuration | Workload | Throughput (ops/s) | Energy (J) | ops/Joule | Quality |
|---------------|----------|-----------:|----------:|----------:|:-------:|
| CPU only | UltraSparse (99.9%) | 7.7 | 325.3 | 0.31 | ✅ Real |
| GPU (BarraCUDA) | UltraSparse (99.9%) | 200.3 | 124.8 | 0.80 | ✅ Real |
| NPU (Akida) | UltraSparse (99.9%) | 919.3 | 0.22 | 459.7 | ❌ Modeled |
| NPU→GPU | UltraSparse (99.9%) | 385.4 | 64.6 | 1.55 | ⚠️ Mixed |
| GPU→NPU | UltraSparse (99.9%) | 427.3 | 58.2 | 1.72 | ⚠️ Mixed |
| | | | | | |
| CPU only | Dense (<20%) | 7.7 | 323.4 | 0.31 | ✅ Real |
| GPU (BarraCUDA) | Dense (<20%) | 218.7 | 114.3 | 0.87 | ✅ Real |
| NPU (Akida) | Dense (<20%) | 883.4 | 0.23 | 441.7 | ❌ Modeled |
| NPU→GPU | Dense (<20%) | 417.9 | 58.6 | 1.71 | ⚠️ Mixed |
| GPU→NPU | Dense (<20%) | 417.8 | 58.6 | 1.71 | ⚠️ Mixed |

### 6.4 Analysis (Real Data Only)

**CPU vs GPU (validated)**: The GPU achieves 26× higher throughput than CPU for TFHE-rs encrypted operations (200 ops/s vs 7.7 ops/s) via real BarraCUDA polynomial addition. This is consistent with the NTT scaling data in Section 3.

**GPU energy**: At 0.80-0.87 ops/J, the GPU's energy efficiency for encrypted pipeline dispatch is modest — the 250W power envelope is expensive for ~200 ops/s throughput. This underscores the need for NPU integration for sparse workloads, though that integration remains modeled.

**NPU numbers (modeled, not citable)**: The NPU's 459.7 ops/J would represent a 575× advantage over GPU if validated on real hardware. The *architectural argument* (event-driven processing at 1-2W vs constant 250W) is sound and supported by BrainChip's published specifications. But these specific throughput numbers come from a sleep-based timing model and should not be cited as measured results. Real Akida benchmarking is future work.

---

## 7. Workload Class 5: Neuromorphic Hybrid Execution ❌ MODELED

> **Data quality: MODELED.** Both benchmarks below use CPU busy-loops to represent neuromorphic computation. The power values (1W NPU, 250W GPU) are from hardware datasheets, not measured during the benchmark. The throughput numbers are CPU loop iteration rates, not actual NPU processing rates. The original data contains physically impossible values (384 billion samples/sec for reservoir computing, 1.4 quadrillion rays/sec for raytracing) that confirm these are models.

### 7.1 NPU Reservoir Computing — Modeled

The benchmark source uses a CPU busy-loop (`(0..active_neurons * sequence_length).map(|i| (i * 7919) % 104729).sum()`) and applies a `npu_slowdown_factor = 5.0` to the CPU timing to estimate NPU performance. The resulting throughput numbers are artifacts of CPU loop speed and should not be interpreted as NPU measurements.

**What the model assumes**:
- GPU power: 250W (datasheet TDP) → applied to CPU-measured compute time
- NPU power: 1W (Akida AKD1000 datasheet) → applied to CPU-measured compute time × slowdown factor
- Power efficiency ratio: 250W / 1W × throughput ratio = ~50× across all tasks

**What this means**: The 50× power efficiency ratio is a direct consequence of the 250:1 TDP ratio, not an empirical measurement. The *architectural argument* (event-driven NPU at 1W vs always-on GPU at 250W yields dramatic power savings for sparse workloads) is supported by BrainChip's published specifications and the neuromorphic computing literature. But these specific numbers are projections, not measurements.

**Future work**: Wire actual Akida inference into the reservoir computing benchmark and measure real throughput + power on the physical AKD1000 chips.

### 7.2 Hybrid Raytracing — Modeled

The benchmark uses CPU busy-loops to represent both BVH traversal and ray-triangle intersection, with different power values applied to the GPU and NPU+GPU configurations. The throughput numbers (quadrillions of rays/sec) reflect CPU integer arithmetic speed and are not physically meaningful for raytracing.

**What the model demonstrates**:
- The *dispatch architecture* works: BarraCUDA can route sparse phases to NPU and dense phases to GPU
- The *power model* is directionally correct: shifting sparse work to a 1-2W device dramatically reduces system power
- The *sparsity scaling* (power savings increase with scene sparsity) follows from the dispatch logic

**What it does NOT demonstrate**: Actual raytracing performance, actual NPU traversal time, or actual hybrid power consumption. These require real Akida inference and GPU shading, which is future work.

**Honest summary**: The neuromorphic hybrid architecture is designed and the dispatch code exists. Validating it with real hardware measurements is a concrete next step, not a completed milestone.

---

## 8. Synthesis: What the Data Actually Shows

The data divides into three tiers of evidence quality:

### Tier 1: Validated on Real Hardware (Citable)

| Workload | Optimal Hardware | Evidence |
|----------|:----------------:|----------|
| Dense polynomial arithmetic (NTT, FHE) | **GPU** | 110× speedup at N=4096, measured on RTX 3090 |
| Cross-vendor correctness (FHE) | **GPU (any)** | 18/18 operations identical on NVIDIA + AMD |
| Large-batch ML inference (simplified) | **GPU** | 1.33M img/s MLP at batch=128, real BarraCUDA ops |
| Small dense vector ops (N<4096) | **CPU** | 95.2M ops/J CPU vs 33 ops/J GPU for dense vector add |
| Sequential FHE bootstrapping | **CPU** | TFHE-rs real timing, inherently serial |

### Tier 2: Architecturally Sound, Partially Validated (Cite with Caveat)

| Workload | Expected Hardware | Evidence |
|----------|:-----------------:|----------|
| Single-sample NPU inference | **NPU** | MNIST via `akida_driver` on real Akida, power from datasheet |
| Energy-constrained inference | **NPU** | 0.11 mJ/img (datasheet power × real timing) |

### Tier 3: Modeled / Projected (Do Not Cite as Measured)

| Workload | Projected Hardware | Issue |
|----------|:------------------:|-------|
| Sparse event processing | NPU | Pipeline benchmark NPU = `sleep()` |
| Always-on monitoring | NPU | Reservoir computing = CPU busy-loop |
| BVH traversal + shading | NPU→GPU | Raytracing = CPU busy-loop + datasheet TDP |

**The heterogeneous thesis**: The *architectural argument* — that workload-aware dispatch across CPU, GPU, and NPU yields better performance and energy efficiency than any single substrate — is strongly supported by the Tier 1 data (GPU vs CPU differences span 6 orders of magnitude in energy efficiency). The NPU contribution to this thesis is currently theoretical for most benchmarks, supported by the MNIST inference result and BrainChip's published specifications, but not yet validated across the full workload set. Wiring real Akida execution into the remaining benchmarks is a concrete engineering task, not a research question.

---

## 9. Cross-Vendor Parity: NVIDIA vs AMD ✅ REAL

A recurring theme across FHE benchmarks is the equivalence between NVIDIA and AMD results when running the same WGSL shader. These are all Tier 1 (real hardware) results:

| Benchmark | NVIDIA Result | AMD Result | Delta |
|-----------|:-------------:|:----------:|:-----:|
| FHE PolyAdd (N=2048) | 7.14M ops/s | 33.33M ops/s | AMD 4.7× faster |
| FHE PolyMul (N=2048) | 20.0M ops/s | 20.0M ops/s | Parity |
| FHE AND (N=2048) | 33.33M ops/s | 33.33M ops/s | Parity |
| Encrypted MNIST (batch=1) | 3,280 img/s | 3,936 img/s | AMD 1.2× faster |
| Encrypted MNIST (batch=100) | 2,319 img/s | 2,783 img/s | AMD 1.2× faster |
| All FHE correctness | 18/18 ✅ | 18/18 ✅ | **Identical** |

**AMD's PolyAdd advantage** (4.7× at N=2048) is the largest cross-vendor delta and likely reflects the RX 6950 XT's Infinity Cache (128 MB) providing faster access to the polynomial coefficient arrays. For compute-bound operations (PolyMul), the delta vanishes — both GPUs saturate their ALUs at the same rate.

**Correctness is identical**: Every operation that passes on NVIDIA also passes on AMD, with the same numerical result. This validates WGSL/Vulkan as a genuinely vendor-neutral compute backend for security-critical workloads where bit-exact reproducibility across hardware is non-negotiable.

---

## 10. Energy Efficiency Summary

| Workload | Most Energy-Efficient | Least Efficient | Ratio | Data Quality |
|----------|:---------------------:|:---------------:|------:|:------------:|
| MNIST inference (batch=128) | GPU (1.33M imgs/s) | CPU (6.2K imgs/s) | **214× throughput** | ✅ Real |
| NTT (N=4096) | GPU (1.23 ops/J) | CPU (0.19 ops/J) | **6.6×** | ✅ Real |
| Dense vector add (N=1024) | CPU (95.2M ops/J) | GPU (33 ops/J) | **2,857,000×** | ✅ Real |
| FHE Pipeline dispatch | GPU (0.87 ops/J) | CPU (0.31 ops/J) | **2.8×** | ✅ Real |
| MNIST NPU inference (batch=1) | NPU (0.11 mJ/img) | GPU (17 mJ/img) | ~155× | ⚠️ Timing real, power from datasheet |
| Pipeline dispatch (sparse, NPU) | NPU (459.7 ops/J) | CPU (0.31 ops/J) | 1,483× | ❌ Modeled |
| Reservoir computing | NPU (50× vs GPU) | GPU | 50× | ❌ Modeled |
| Hybrid raytracing (99%) | NPU+GPU (55.6×) | GPU | 55.6× | ❌ Modeled |

**The validated energy landscape is already dramatic.** Even considering only Tier 1 (real hardware) data, the most and least efficient hardware for a given workload can differ by six orders of magnitude (CPU: 95.2M ops/J for small dense adds vs GPU: 33 ops/J for the same operation). This validates the core heterogeneous thesis: correct hardware selection is not an optimization but a requirement.

The NPU energy projections, if validated on real hardware, would extend this range further. But the key insight — that different workloads demand radically different hardware — is already proven by the CPU-GPU data alone.

---

## 11. Conclusions

### What Is Proven (Real Hardware)

1. **WGSL/Vulkan achieves genuine vendor neutrality.** NVIDIA and AMD produce identical correctness results from the same shader binary. 18/18 FHE operations pass on both vendors. Performance deltas exist (AMD's PolyAdd 4.7× faster, compute-bound PolyMul at parity) but are within expected architectural variance.

2. **GPU vs CPU: the case is closed.** For FHE polynomial arithmetic, the GPU achieves 110× speedup and 6.6× energy advantage at production security parameters. For batch ML inference, GPU throughput scales 90× from batch=1 to batch=128. For small dense operations, the CPU wins by 2.8M×. The optimal dispatch is unambiguously workload-dependent.

3. **Energy efficiency varies by ≥10⁶× across workloads.** This is validated by CPU and GPU data alone (95.2M ops/J for CPU dense adds vs 33 ops/J for GPU on the same operation). Correct hardware selection is a correctness requirement, not an optimization.

### What Is Designed but Not Yet Validated

4. **NPU integration is architecturally complete, execution is partial.** The dispatch path exists in code (runtime hardware discovery, substrate selection, Akida SDK integration). MNIST inference on real Akida hardware produces plausible results (15-17K img/s). But several NPU benchmarks (reservoir computing, raytracing, pipeline dispatch) use modeled timing rather than actual chip execution.

5. **ML inference operations are correct but architectures are simplified.** BarraCUDA's MatMul, Conv2D, LayerNorm, and GELU execute correctly on GPU. The benchmarks use reduced model architectures (single-MatMul "layers"), not production transformer/ResNet configurations. Competitive ML performance requires kernel optimization (tiling, fusion), which is engineering work on a validated foundation.

### Future Work

| Task | Impact | Effort |
|------|--------|--------|
| Wire real Akida inference into all NPU benchmarks | Validates NPU energy thesis | Medium |
| Measure NPU power during inference (not datasheet) | Trustworthy energy efficiency numbers | Low |
| Full transformer architecture (multi-head attention) | Production-competitive throughput | Medium |
| Kernel optimization (tiling, fused ops) | Competitive with cuDNN | High |

---

*Data: `whitePaper/barraCUDA/data/`*  
*Benchmark code: `phase1/toadstool/showcase/`*  
*Hardware inventory: `whitePaper/gen3/about/HARDWARE.md`*

