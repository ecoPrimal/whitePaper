# Neuromorphic Compute Partnership — Open Outreach

**Date:** February 25, 2026
**Project:** ecoPrimals / hotSpring
**License:** AGPL-3.0-only
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

**What we ask:**
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
| [`TECHNICAL_BRIEF.md`](TECHNICAL_BRIEF.md) | Full technical findings: architecture, benchmarks, 10 SDK assumptions overturned, AKD1500 analysis, near-future NPU extension roadmap across 5 scientific domains, hardware integration vision (on-board NPU, modular chiplet, edge nodes, custom PCB), and what we want to test next |
| [`BENCHMARK_DATASHEET.md`](BENCHMARK_DATASHEET.md) | Raw benchmark numbers: latency, throughput, power, precision parity, three-substrate production results, AKD1500 projected performance |
| [`AKD1500-Datasheet-1.2.pdf`](AKD1500-Datasheet-1.2.pdf) | BrainChip AKD1500 datasheet (reference) |

---

## Current Hardware

| Substrate | Device | Role | Status |
|-----------|--------|------|--------|
| Primary GPU | NVIDIA RTX 3090 (24 GB) | DF64 production HMC | ✅ Production |
| Compute GPU | NVIDIA Titan V ×2 (12 GB each) | Native f64 oracle | ✅ Validated |
| NPU | BrainChip AKD1000 (PCIe) | ESN adaptive steering | ✅ Integrated |
| CPU | AMD Threadripper 3970X (32C/64T) | Orchestration + reference | ✅ Baseline |

Full hardware inventory: [`whitePaper/gen3/about/HARDWARE.md`](../../gen3/about/HARDWARE.md)

---

## Repository Structure (relevant paths)

```
hotSpring/
├── barracuda/                    ← 76 validation binaries, 664 tests, v0.6.14
│   ├── src/bin/                  ← includes validate_three_substrate, validate_titan_oracle
│   ├── src/md/npu_hw.rs          ← AKD1000 Rust hardware adapter
│   ├── src/md/reservoir.rs       ← ESN + NpuSimulator
│   └── src/discovery.rs          ← capability-based NPU probe (sysfs + akida-driver)
├── metalForge/
│   ├── forge/src/probe.rs        ← PCIe vendor-ID scan (0x1e7c), substrate abstraction
│   └── npu/akida/                ← HARDWARE.md, BEYOND_SDK.md, EXPLORATION.md, scripts/
├── experiments/                  ← 17 experiment journals (001-017)
│   ├── 015_MIXED_PIPELINE_BENCHMARK.md   ← three-substrate production run
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
