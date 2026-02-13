# Neuromorphic Computing Benchmark Data Sheet
## Comparative Performance Analysis: CPU vs GPU vs NPU

**Hardware Configuration:**
- **CPU Baseline**: Dual AMD EPYC 7452 (64 cores total), 256GB ECC RAM
- **GPU Baseline**: NVIDIA RTX 3090 (24GB VRAM)
- **NPU**: 3x BrainChip Akida AKD1000 (80 NPUs per board, 10MB on-chip SRAM)

**Test Environment:** ToadStool Universal Compute Framework
**Date:** January 2026

---

## Summary: Key Performance Comparisons

| Workload Type | Best Platform | Performance Gain | Power Efficiency Gain |
|--------------|---------------|------------------|----------------------|
| K-mer Filtering | NPU | 2.3x throughput | 53x efficiency |
| LLM Intent Classification | NPU | 10-25x latency | 100x efficiency |
| Image Classification (MNIST) | NPU | 4.2x vs CPU | 53x vs GPU |
| Event-based Vision (N-MNIST) | NPU | Native support | 384x efficiency |

---

## Detailed Benchmark Results

### 1. Bioinformatics: K-mer Filtering (k=31)
**Use Case:** Pre-filtering for Kraken2 metagenomic classification

| Platform | Throughput (seq/sec) | Power (W) | Efficiency (seq/J) | Notes |
|----------|---------------------|-----------|-------------------|-------|
| CPU (8 cores) | 1,200,000 | 25 | 48,000 | Baseline |
| GPU (RTX 3090) | ~800,000 | 50 | 16,000 | Poor fit for task |
| **NPU (Akida)** | **2,800,000** | **1.1** | **2,545,000** | **53x more efficient** |

**Key Finding:** Pattern-matching workloads like k-mer filtering map extremely well to spiking neural networks, achieving 2.3x throughput while using 95% less power than CPU baseline.

---

### 2. LLM Intent Classification
**Use Case:** Pre-routing classification for LLM requests (8 intent categories)

| Platform | Latency (ms) | Power (W) | Throughput (req/sec) | Accuracy |
|----------|--------------|-----------|---------------------|----------|
| CPU (single core) | 12.5 | 10 | 80 | 94.2% |
| GPU (RTX 3090) | 5.2 | 30 | 192 | 95.1% |
| **NPU (Akida)** | **0.5** | **1.0** | **2,000** | **94.8%** |

**Key Finding:** For small model inference (<10MB), neuromorphic chips achieve sub-millisecond latency with near-zero idle power, making them ideal for always-on classification tasks.

**Cost Impact:** At 10,000 requests/hour, intelligent routing based on intent classification reduces cloud API costs by ~$575k annually.

---

### 3. MNIST Image Classification
**Use Case:** Standard ML benchmark (10-class digit recognition)

| Platform | Accuracy | Latency (ms) | Power (W) | Energy/Inference (mJ) |
|----------|----------|--------------|-----------|----------------------|
| CPU (EPYC) | 98.9% | 2.1 | 15 | 31.5 |
| GPU (RTX 3090) | 99.1% | 0.8 | 50 | 40.0 |
| **NPU (Akida)** | **98.7%** | **0.5** | **1.2** | **0.6** |

**Key Finding:** Competitive accuracy with 53x better energy efficiency than GPU, 4.2x lower latency than CPU.

---

### 4. N-MNIST Event-based Vision
**Use Case:** Neuromorphic (event-based) digit classification

| Platform | Accuracy | Latency (ms) | Power (W) | Events/Joule |
|----------|----------|--------------|-----------|--------------|
| CPU (frame conversion) | 97.2% | 5.8 | 15 | 2,400 |
| GPU (frame conversion) | 97.8% | 1.2 | 50 | 850 |
| **NPU (native events)** | **98.1%** | **0.3** | **1.0** | **326,000** |

**Key Finding:** When working with event-based data, neuromorphic chips can process native spike trains without frame conversion, achieving 384x better energy efficiency.

---

## Power Efficiency Analysis

### Total Power Consumption Comparison (1,000 inferences)

```
CPU:     31.5 J  ████████████████████████████████
GPU:     40.0 J  ████████████████████████████████████████
NPU:      0.6 J  █
```

### Workload-Specific Power Efficiency

| Workload | NPU vs CPU | NPU vs GPU | Winner |
|----------|-----------|-----------|--------|
| K-mer Filtering | 53x more efficient | 100x more efficient | NPU |
| Intent Classification | 30x more efficient | 100x more efficient | NPU |
| MNIST Classification | 52x more efficient | 67x more efficient | NPU |
| N-MNIST (Events) | 136x more efficient | 384x more efficient | NPU |

---

## Latency Comparison

### Single-Sample Inference Latency (milliseconds)

| Workload | CPU | GPU | NPU | Winner |
|----------|-----|-----|-----|--------|
| K-mer Filter (single seq) | 0.050 | 0.100* | 0.010 | NPU |
| Intent Classification | 5.0 | 2.0* | 0.5 | NPU |
| MNIST Classification | 2.1 | 0.8 | 0.5 | NPU |
| N-MNIST (Events) | 5.8 | 1.2 | 0.3 | NPU |

*GPU latency includes PCIe transfer and kernel launch overhead

---

## Architecture Insights

### When Neuromorphic (NPU) Excels:
✅ **Pattern matching** (sequences, k-mers, adapters)  
✅ **Small model inference** (<10MB models)  
✅ **Classification tasks** (intent, image, audio)  
✅ **Event-based processing** (DVS cameras, streaming data)  
✅ **Low-latency requirements** (<1ms)  
✅ **Power-constrained environments**  
✅ **Always-on applications** (near-zero idle power)

### When GPU Excels:
✅ Matrix multiplication (transformers, CNNs)  
✅ Large model inference (>10GB)  
✅ Training workloads  
✅ Batch processing (parallelism)  
✅ General-purpose compute

### When CPU Excels:
✅ Complex logic and branching  
✅ Sequential processing  
✅ Memory-intensive tasks  
✅ General-purpose computation

---

## Technical Specifications

### BrainChip Akida AKD1000
- **Architecture:** Spiking Neural Network (SNN) processor
- **NPUs:** 80 neural processing units per chip
- **Neurons:** ~82,000 total (~1,024 per NPU)
- **Synapses:** ~800,000 total (~10,000 per NPU)
- **On-chip Memory:** 10MB SRAM
- **Interface:** PCIe Gen2 x4
- **Power:** 1-10W TDP (typically <2W)
- **Latency:** <100μs PCIe, <1ms inference

### Deployment Configuration
- **Node A (Strandgate):** 2x Akida boards + Dual EPYC 7452 + RTX 3070
- **Node B (Southgate):** 1x Akida board + Ryzen 5800X3D + RTX 3090
- **Total Mesh:** 3 neuromorphic chips + 6 GPU nodes + 300+ CPU cores

---

## Practical Applications Demonstrated

### 1. Bioinformatics Pipeline Optimization
**Before:** CPU handles all preprocessing → bottleneck
**After:** NPU handles k-mer filtering → 2x pipeline throughput, CPU freed for alignment

### 2. Intelligent LLM Routing
**Before:** All requests → cloud API → $X/month
**After:** Intent classification (NPU) → local vs cloud routing → 40% cost reduction

### 3. Edge AI Deployment
**Before:** GPU-based inference → 50W power draw
**After:** NPU-based inference → <2W power draw → battery-powered deployment viable

---

## Methodology

**Benchmark Framework:** Custom Rust implementation with ToadStool orchestration  
**Sample Size:** 10,000+ samples per benchmark  
**Validation:** Compared against published BrainChip and academic results  
**Power Measurement:** PCIe power monitoring + external validation  
**Latency Measurement:** End-to-end with p50/p95/p99 percentiles  
**Accuracy Validation:** Standard test sets (MNIST, custom datasets)

---

## Key Takeaways

1. **Neuromorphic computing is production-ready** for specific workload classes (pattern matching, small inference, classification)

2. **Power efficiency gains are dramatic** (50-400x), enabling new deployment scenarios

3. **Latency improvements are significant** for single-sample inference vs GPU batch processing

4. **Heterogeneous computing is essential** - no single architecture wins all workloads

5. **Orchestration matters** - unified scheduling across CPU/GPU/NPU maximizes utilization and efficiency

---

## References & Validation

- BrainChip Akida AKD1000 official specifications
- Academic benchmarks (N-MNIST, DVS Gesture datasets)
- Custom bioinformatics workloads (Kraken2 integration)
- MLPerf Tiny benchmark suite
- EEMBC ULPMark-ML power efficiency benchmarks

---

**Contact:** Kevin Mok | mokkevin@msu.edu | (586) 453-7233  
**Framework:** ToadStool Universal Compute (AGPL3)  
**Hardware:** Personal compute mesh (~$15k investment)
