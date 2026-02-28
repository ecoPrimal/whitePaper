# Neuromorphic Compute Partnership — Open Outreach

**Date:** February 27, 2026
**Project:** ecoPrimals / hotSpring + wetSpring
**License:** AGPL-3.0-or-later
**Repository:** [github.com/syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring)

---

## What This Is

This directory contains a standing technical brief for neuromorphic hardware
manufacturers. It documents what we have built, what we have measured, and
what we are looking for — with enough data for an engineering team to evaluate
whether collaboration benefits both sides.

Everything referenced here is published under AGPL-3.0. The repository is
public. The benchmarks are reproducible. The findings are version-controlled.

---

## The Offer

We operate a multi-substrate scientific computing pipeline that validates
computational physics (lattice QCD, molecular dynamics, nuclear structure,
spectral theory) on consumer hardware. Our stack is pure Rust with WGSL GPU
shaders — vendor-agnostic by construction.

We have integrated a BrainChip AKD1000 neuromorphic processor as a
coprocessor substrate alongside NVIDIA GPUs (RTX 3090, Titan V). The NPU
runs echo state network inference for adaptive steering of physics simulations,
operating at microwatt power while GPUs handle the heavy compute.

**What we give:**
- Public, AGPL-3.0 benchmarks on your hardware running real science (not toy demos)
- Rust bindings and driver-level integration into a production validation suite
- 664 passing tests, zero clippy warnings, provenance-traced physical constants
- Continuous evolution — every release that touches your substrate produces new public data
- Documentation quality that serves as de facto technical writing for your platform
- Hardware integration roadmap: on-board GPU co-location, chiplet architectures, edge nodes, custom PCB design
- Sovereign Rust driver development — your hardware gets kernel-independent Linux support

**What you can give:**
- Evaluation hardware (dev board, reference design, or engineering sample)
- Technical contact for driver/SDK questions during integration

**What you get:**
- The only public scientific computing validation suite for your architecture
- Novel use case beyond vision/keyword: adaptive QCD steering, transport prediction, anomaly detection
- Rust ecosystem development (your SDK is likely Python/C++ only)
- A living, version-controlled benchmark that keeps producing results
- A Rust PCIe driver that outlives your vendor kernel module's supported versions
- Hardware integration R&D: custom board designs, chip-level integration studies

---

## Contents

| Document | Description |
|----------|-------------|
| [`TECHNICAL_BRIEF.md`](TECHNICAL_BRIEF.md) | Full technical findings: architecture, benchmarks, 10 SDK assumptions overturned, AKD1500 analysis, near-future NPU extension roadmap across 5 scientific domains, hardware integration vision (on-board NPU, modular chiplet, edge nodes, custom PCB), Exp 022 production results, and what we want to test next |
| [`BENCHMARK_DATASHEET.md`](BENCHMARK_DATASHEET.md) | Raw benchmark numbers: latency, throughput, power, precision parity, three-substrate production results (Exp 015 + Exp 022 live NPU), AKD1500 projected performance |
| [`AKD1500-Datasheet-1.2.pdf`](AKD1500-Datasheet-1.2.pdf) | BrainChip AKD1500 datasheet (reference) |

---

## Current Hardware

| Substrate | Device | Role | Status |
|-----------|--------|------|--------|
| Primary GPU | NVIDIA RTX 3090 (24 GB) | DF64 production HMC | ✅ Production |
| Compute GPU | NVIDIA Titan V ×2 (12 GB each) | Native f64 oracle | ✅ Validated |
| NPU | BrainChip AKD1000 (PCIe) | ESN adaptive steering | ✅ Integrated (hotSpring SDK) |
| NPU | BrainChip AKD1000 (PCIe) | ESN classifiers, online evolution | ✅ **Live via Pure Rust driver** (wetSpring V60) |
| CPU | AMD Threadripper 3970X (32C/64T) | Orchestration + reference | ✅ Baseline |
| CPU | Intel i9-12900K | wetSpring NPU host | ✅ Production (Exp193-195) |

Full hardware inventory: [`whitePaper/gen3/about/HARDWARE.md`](../../gen3/about/HARDWARE.md)

---

## Repository Structure (relevant paths)

```
hotSpring/
├── barracuda/                    ← 76 validation binaries, 664 tests, v0.6.14
│   ├── src/bin/                  ← includes validate_three_substrate, production_mixed_pipeline
│   ├── src/md/npu_hw.rs          ← AKD1000 Rust hardware adapter
│   ├── src/md/reservoir.rs       ← ESN + NpuSimulator + cross-run learning
│   └── src/discovery.rs          ← capability-based NPU probe (sysfs + akida-driver)
├── metalForge/
│   ├── forge/src/probe.rs        ← PCIe vendor-ID scan (0x1e7c), substrate abstraction
│   └── npu/akida/                ← HARDWARE.md, BEYOND_SDK.md, EXPLORATION.md, scripts/
├── experiments/                  ← 22 experiment journals (001-022)
│   ├── 015_MIXED_PIPELINE_BENCHMARK.md   ← three-substrate validation (3 β)
│   ├── 022_MIXED_PIPELINE_NPU_PRODUCTION.md ← live NPU production (10 β, 5,978 NPU calls)
│   └── 016_CROSS_SPRING_EVOLUTION_MAP.md ← full shader flow map
└── wateringHole/handoffs/        ← cross-project evolution record
```

---

## Contact

Available for technical discussion. Preferred format: email with link to
this directory. All correspondence regarding hardware partnerships is
conducted in the open — findings will be published.

---

## Evolution History

The earlier documents in `whitePaper/outreach/` (2025) reflect the
philosophical foundations of this project. This directory represents the
grounded, data-driven evolution of that vision: we built the system,
measured the hardware, published the results, and now seek to expand
the substrate diversity.

### V60 Update (February 26, 2026): Pure Rust NPU — Phase C Sovereign Driver

wetSpring now runs 3 ESN classifiers (QS phase, bloom sentinel, Anderson
disorder) on a **live AKD1000** via ToadStool's pure Rust `akida-driver`.
Zero Python, zero C++, zero vendor SDK in the data path.

Key measurements on real silicon:
- **18.8K Hz** inference throughput via DMA
- **37 MB/s** reservoir weight loading to 10 MB SRAM
- **86 µs** online readout switching (weight mutation — 3 classifiers hot-swapped)
- **136 gen/sec** online evolutionary learning on hardware
- **12.9K Hz** temporal streaming with p99=76 µs latency
- **1.4 µJ/inference** → coin-cell CR2032 lasts **11 years** at 1 Hz
- **6.34 bits** byte entropy from SRAM PUF fingerprint

This is the first published scientific computing validation of an AKD1000
using a non-vendor driver. The Rust `akida-driver` achieves kernel-independent
hardware access — answering the AKD1500 datasheet's "no plans for updates"
Linux kernel support policy with a sovereign alternative.

### Exp 022 Update (February 27, 2026): First Live NPU Lattice QCD Production Run

hotSpring completed a full 32⁴ quenched SU(3) β-scan with the AKD1000
running ESN adaptive steering in real-time via PCIe. 10 NPU-steered β
points, 5,900 measurement trajectories, 5,978 NPU calls. ESN weights
bootstrapped from prior runs (cross-run learning). 63% thermalization
savings. Susceptibility peak χ=32.41 at β=5.7797 confirming the
deconfinement transition. Same wall time as previous non-NPU run (14h)
but 2.5× more measurement statistics.
