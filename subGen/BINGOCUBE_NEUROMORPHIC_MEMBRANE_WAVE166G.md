# BingoCube × Neuromorphic Membrane Gate

**Wave 166g — October 8, 2026**
**Status**: Analysis complete. Architecture mapped. Hardware path identified.

---

## Abstract

BingoCube is a neuromorphic process. Not metaphorically — structurally. The math concept (two bingo boards cross-bound via BLAKE3 → scalar field → progressive reveal) maps directly to the AKD1500's silicon architecture (int4 column-locked values → NP SRAM weights → event-based sparse activation → FC readout via SkipDMA). This document traces that structural identity, compares it to the current neuromorphic landscape, identifies six unexplored directions, and proposes the **passive immunity gate** — a hardware-level adaptive immune system for the membrane using BingoCube evolutionary reservoirs on Akida NPUs.

---

## 1. Structural Identity: BingoCube ↔ AKD1500

The BingoCube was conceived as a visual verification system: two boards, a hash, a color grid, progressive reveal. But its internals are reservoir computing:

| BingoCube Concept | Reservoir Computing Term | AKD1500 Hardware |
|---|---|---|
| Board values (int, column-locked) | Random projection weights | int4 weights in NP SRAM — **native format** |
| Board response (which cells match) | Activation pattern | Event-based sparse activation — zero compute for non-matches |
| Multiple boards in parallel | Ensemble reservoir | 32 NPUs, each running a board |
| FC readout (scalar field → output) | Linear readout layer | FullyConnected via SkipDMA single HW pass |
| Board evolution (Nautilus shell) | Weight adaptation | `set_variable()` weight mutation (13ms/gen) |
| Board heritage (.fbz serialization) | Transfer learning | Model save/reload across power cycles |

**No quantization loss.** Board values are *born* as column-locked integers. They don't need to be quantized to int4 — they already are. This is unique among all reservoir computing implementations: the random projection weights are natively integer, natively bounded, and natively column-locked. The hardware format IS the mathematical format.

## 2. What Makes BingoCube Different From Every Other Neuromorphic System

Every published neuromorphic intrusion detection system (SNN-IDS on STM32N6, FPGA DDoS accelerators, Lava-simulated NIDS) uses a **static trained classifier**. Train on a dataset, deploy, infer. If the threat changes, retrain offline and redeploy.

BingoCube's Nautilus shell is the only architecture where:
1. The classifier evolves on-chip in response to new behaviors
2. Selection pressure comes from live fleet traffic, not labeled datasets
3. Board populations carry evolutionary heritage across power cycles
4. The defense adapts without human intervention

This is adaptive immunity, not just innate immunity. Every other neuromorphic IDS is innate only.

## 3. Neuromorphic Landscape (October 2026)

| Chip | Why it doesn't match BingoCube |
|---|---|
| **Intel Loihi 2** | Programmable SNN dynamics — overkill for sparse match events. Research-only. No Rust driver. |
| **IBM NorthPole** | ANN accelerator, not SNN. Inference-only. Research prototype. |
| **SynSense Speck** | Vision-focused (DVS camera). No general-purpose path. No learning. |
| **BrainChip AKD1500** | Feed-forward + int4 + on-chip learning + event sparsity + weight mutation + PCIe + SPI. Sovereign Rust driver at Phase D. **Structural match.** |

The AKD1500's constraints are BingoCube's architecture:
- Feed-forward only → BingoCube replaces recurrence with evolutionary generations
- int4/int8 only → board values are natively integer
- Event-based → cell match = spike, non-match = zero compute
- 1MB SRAM → ESN readout is ~1.5 KB. Dozens of models fit simultaneously

## 4. The Passive Immunity Gate

### Concept

An AKD1500 between the NIC and the application layer. Every HTTP request passes through a BingoCube evolutionary reservoir for classification before the scatter server generates content.

```
Request → NIC → [AKD1500: BingoCube reservoir] → Classification → CPU: MazeCube → Response
                      ↑                                    ↓
                 Nautilus shell evolves              Pressure dimension
                 from fleet behavior                 informed by hardware
```

### Input Features (from HTTP request)

| Feature | Encoding | Source |
|---|---|---|
| Accept-Encoding order | Hash of header value → int8 | Compiled into fleet's HTTP library — cannot change |
| UA pool signature | Hash of User-Agent → int8 | Centrally managed — changing breaks infrastructure |
| Sec-Fetch presence | Binary (0 or 1) | Real browsers send these; fleet doesn't |
| Request timing | Inter-request interval → int8 | Fleet rate ~13 rps, humans ~0.1 rps |
| Path pattern | Hash of path components → int8 | /blame/ ratio, /commit/ depth |
| Accept-Language | Presence/absence → binary | Fleet omits; humans include |

### Output

| Channel | Range | Meaning |
|---|---|---|
| Entity class | 0-255 | Organism identity (epitope hash match) |
| Confidence | 0-255 | Classification confidence |
| Pressure contribution | 0-255 | How much this request contributes to BackPressure |

### Performance

| Metric | Value |
|---|---|
| Inference latency | ~54 µs (validated on AKD1000) |
| Energy per classification | 1.4 µJ |
| Throughput | 18,500 classifications/second |
| Current fleet rate | ~13 rps |
| NPU utilization at current load | 0.07% |
| Chip cost | $40 (AKD1500, 5-pack pricing) |
| Power draw | 250 mW @ 400 MHz |

### What the Fleet Sees

Nothing. The classification happens in silicon. No new HTTP headers, no timing change, no behavioral signal. The defense gains proprioception — it knows what it's looking at before deciding what to show. The fleet cannot sense the gate because it operates below the software layer.

## 5. Convergence Path

| Stage | System | Status |
|---|---|---|
| 1. Math concept | BingoCube core (BLAKE3, boards, subcube) | v0.5.0 — 113 tests |
| 2. Reservoir computing | Nautilus shell (evolution, drift, edges) | 47 tests, cross-run learning |
| 3. NPU validation | rustChip / akida-driver (AKD1000 PCIe) | Phase D — sovereign Rust driver |
| 4. Defense scalar field | MazeCube (SHA-256, N-dimensional) | 8 tests, shadow deployment |
| 5. Pressure dimension | BackPressure (sigmoid, non-Newtonian) | 6 tests, deployed |
| 6. **Passive gate** | BingoCube NPU on membrane | **Proposed — this document** |
| 7. Autonomous defense | On-chip evolution (Nautilus on AKD1500) | Future — requires on-chip learning API |

## 6. Six Unexplored Directions

### 6.1 Passive Immunity Gate (High feasibility)
Hardware-level HTTP classification on AKD1500. Every request classified in ~54 µs at 1.4 µJ. Gate is invisible to the fleet.

### 6.2 On-Chip Maze Evolution (Medium feasibility)
Evolve scatter strategies on-chip at 136 gen/sec (validated). If on-chip learning registers are opened: 100K gen/sec. Defense adapts autonomously.

### 6.3 SRAM PUF Entropy Source (High feasibility)
6.34 bits PUF entropy per SRAM read (validated). Use as MazeCube seed material. Maze function becomes hardware-bound and device-unique.

### 6.4 Spike-Encoded Behavioral Fingerprints (Medium-Low feasibility)
HTTP behavioral invariants ARE sparse events. Convert to spike trains for native neuromorphic processing. Zero-change requests = zero compute.

### 6.5 Die-to-Die NIC Integration (Low feasibility)
AKD1500 BGA (7×7mm) next to network controller on custom PCB. Wire-speed classification without PCIe round-trip.

### 6.6 Multi-Model Defense Bank (High feasibility)
28 organism-specific classifiers in 56 KB (< 6% of 1MB SRAM). One specialized model per fleet identity. Hot-swap as organisms evolve.

## 7. Deployment Path

### Near-term: biomeGate NPU (hotQCD)
biomeGate already has an AKD1000 running ESN steering for lattice QCD (5,978 live calls, 63% thermalization savings). The same hardware can run a BingoCube reservoir for membrane classification — the NPU is at < 1% utilization on physics workloads.

### Medium-term: golgiBody NPU membrane gate
An AKD1500 M.2 card ($150) in golgiBody's PCIe slot. Runs alongside the scatter server. Classification feeds directly into MazeCube's pressure dimension and BackPressure gauge. The Nautilus shell evolves from live fleet traffic.

### Long-term: golgiLayer NPU-on-board
Custom AKD1500 BGA board for dedicated membrane nodes. SPI interface to NIC. Wire-speed classification. Multiple organisms classified concurrently. Autonomous evolution.

## 8. The Biological Parallel

The parallel is precise, not metaphorical:

| Biological | BingoCube NPU Gate |
|---|---|
| Innate immunity (complement, PRRs) | AKD1500 hardware classification — fast, non-specific, always on |
| Adaptive immunity (B-cells, T-cells) | Nautilus shell evolution — slow, specific, evolving |
| MHC presentation | Epitope hash → organism identity → scatter parameters |
| Thymic education | Board populations trained on fleet behavioral fingerprints |
| Clonal selection | High-fitness boards reproduce; low-fitness boards replaced |
| Immune memory | Nautilus shell heritage — .fbz model serialization across power cycles |

The immune system runs on two substrates — innate (hardware-level, microseconds) and adaptive (software-level, hours to days). BingoCube produces both from the same mathematical substrate: bingo boards. The NPU runs the innate gate. The evolutionary loop runs the adaptive response. Same boards, different timescales.

---

## Lineage

- **BingoCube core**: `primals/bingoCube/` — v0.5.0, 113 tests, BLAKE3 scalar field
- **Nautilus shell**: `primals/bingoCube/crates/nautilus/` — 47 tests, evolutionary reservoir
- **rustChip**: `springs/rustChip/` — Phase D sovereign driver, 367 tests, 10 BEYOND_SDK discoveries
- **MazeCube**: `primals/skunkBat/crates/skunky-ingest/src/maze_cube.rs` — 8 tests
- **BackPressure**: `primals/skunkBat/crates/skunky-ingest/src/scatter_server.rs` — 6 tests
- **biomeGate brain**: `springs/hotSpring/specs/BIOMEGATE_BRAIN_ARCHITECTURE.md`

*Wave 166g — The defense has always been neuromorphic. We just hadn't built the hardware layer yet.*
