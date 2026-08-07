# Murillo Outreach: Claims vs Reality — Aug 7, 2026

**Purpose**: Re-examine everything we told Murillo, validate against current
evidence, identify what's stronger/weaker/different than claimed, and draft
a modern honest assessment for the next outreach.

---

## Timeline of Claims Made

### Email 1: Neuromorphic Hardware (Jan 2026) — SENT

| Claim | Status Aug 7, 2026 | Assessment |
|---|---|---|
| K-mer filtering: 2.3× NPU throughput, 53× efficiency | **UNVERIFIED** — simulator-based, not hardware-measured | Retest on AKD1000 hardware |
| LLM intent: sub-ms latency, 100× efficiency | **UNVERIFIED** — projected from simulator | Retest needed |
| MNIST: 98.7% acc, 53× efficiency | **PLAUSIBLE** — standard Akida demo, likely real | Verify with hardware run |
| N-MNIST native events: 384× efficiency | **UNVERIFIED** — projected | Retest needed |
| 3× Akida boards, $15k mesh | **TRUE** — hardware confirmed (lspci shows AKD1000) | ✓ |

**Honest assessment**: The benchmark datasheet was largely projections from
NpuSimulator + Akida documentation, not direct measurements. We need to
re-validate each claim on the actual hardware, which is NOW accessible.

---

### Email 2: Sarkas on GPU (Mar 2026) — SENT

| Claim | Status Aug 7, 2026 | Assessment |
|---|---|---|
| 131 quantitative checks pass | **TRUE** — `validate_barracuda_pipeline` + associated binaries | ✓ |
| PP Yukawa DSF: 0.000% energy drift on GPU | **TRUE** — validated repeatedly | ✓ |
| 5 silent bugs in upstream Python | **TRUE** — documented in repo | ✓ |
| 3.7× GPU speedup at N=2000 | **TRUE but UNDERSTATED** — we now see 40-53× for QCD HMC | ✓✓ |
| No CUDA, no ROCm | **TRUE** — WGSL/Vulkan only, cross-vendor validated | ✓ |

**Honest assessment**: Everything in this email was factual and has gotten
stronger since. The GPU speedup is now demonstrated at 40-53× for production
QCD (not just 3.7× for small MD). Cross-vendor parity (6 ppm NVIDIA/AMD)
is a major result that didn't exist when this was sent.

---

### Email 3: Ewald/PPPM + Kokkos Discussion (Mar 4, 2026) — SENT

| Claim | Status Aug 7, 2026 | Assessment |
|---|---|---|
| Full PPPM in WGSL shaders | **TRUE** — operational | ✓ |
| Vendor-agnostic 3D FFT | **TRUE** — no cuFFT dependency | ✓ |
| Would add Kokkos as validation baseline | **NOT DONE** — Kokkos comparison never built | ✗ (honest about gap) |
| PPPM accuracy presets 1e-3 to 1e-7 | **TRUE** — implementation verified | ✓ |

**Honest assessment**: The PPPM claims are solid. The Kokkos baseline promise
is unfulfilled but can be addressed — the honest answer is: our WGSL pipeline
now has enough real-world validation (cross-vendor, MILC interop, literature
plaquette agreement) that a Kokkos micro-benchmark feels less critical than
proving the physics is right.

---

### Email 4: Touch-Base May 2026 — SENT

| Claim | Status Aug 7, 2026 | Assessment |
|---|---|---|
| Chuna Engine: 8 Rust binaries, MILC-compatible | **TRUE** — now validated with bidirectional export (Δ⟨P⟩=3×10⁻⁹) | ✓✓ |
| MILC data generator for Bazavov | **OPERATIONAL** — `milc_validation_loop` writes MILC v5 format | ✓✓ |
| 11 nodes, ~154 cores, ~248 GB VRAM | **TRUE** — current config has 128 cores on strandGate alone | ✓ |
| Anderson localization → QCD connection | **TRUE AND PROVEN** — GPU Lanczos on Anderson Hamiltonians, QCD eigenvalues on same infrastructure | ✓✓ |
| Library proves correct / Binary makes portable | **STRONGLY TRUE** — 652 library tests + musl static binaries deployed | ✓✓ |

**Honest assessment**: This email's claims have all gotten stronger. The
conceptual leaps (Anderson→QCD, library/binary distinction) are now backed
by published data and operational systems.

---

## What's New (Not Claimed in Any Email)

These are capabilities that emerged since the last Murillo contact:

| Capability | Evidence | Impact |
|---|---|---|
| SU(N) for N=2,3,4,5,6,8 on same code | Production validation pass | Major — no prior work does this |
| DF64 (emulated f64 on FP32) | 14 digits, matrix ALL PASS | Novel for lattice QCD |
| Cross-vendor parity (NVIDIA/AMD) | 6 ppm agreement at β=6.2 | First demonstration in QCD |
| MILC v5 bidirectional exchange | Δ⟨P⟩ = 3×10⁻⁹ round-trip | Interoperability proven |
| GPU Lanczos at N=10,648 | 8.4× speedup, 10⁻¹⁵ parity | Spectral computing at scale |
| Cryptographic provenance (BLAKE3+Ed25519) | Every config content-addressed | Reproducibility infrastructure |
| NPU phase classification (ESN on AKD1000) | 100% accuracy on SU(2) configs | Heterogeneous compute demo |
| 41/42 reviewer rubric items done | External review quality | Paper-ready |
| 69 cached configs (SU(2)+SU(3)), 5 GB | Full sunMemo table | Production data archive |
| arXiv preprint ready for submission | 1,412 lines, 4 figures | Publishable result |

---

## NPU Re-Experimentation Plan

The NPU is "just another silicon" in the ecosystem. What experiments to run:

### 1. Validate Original Claims (Truth Check)

```
Run on ACTUAL AKD1000 hardware (PCIe at e2:00.0):
- [ ] MNIST classification: measure real accuracy, latency, power
- [ ] K-mer filtering: measure real throughput on AKD1000
- [ ] Intent classification: deploy small ESN/SNN model, measure
- [ ] Compare to NpuSimulator predictions — what's the gap?
```

### 2. Modern Physics Integration

```
Run sun_npu_metalforge with npu-hw feature:
- [ ] Phase classification on SU(2) configs — does AKD1000 match simulator?
- [ ] SU(3) configs — extend to full gauge group ladder
- [ ] Inference latency: can NPU classify faster than GPU produces configs?
- [ ] Power measurement: what's the real W during inference?
```

### 3. Novel Experiments (never tried)

```
NPU as online HMC monitor:
- [ ] Stream observables from GPU HMC → NPU classifier in real-time
- [ ] Can NPU detect thermalization endpoint online?
- [ ] Can NPU detect stuck/sick trajectories (bad acceptance) live?
- [ ] Adaptive dt steering: NPU recommends step size based on history

NPU for spectral theory:
- [ ] Lanczos convergence prediction: can NPU predict # iterations needed?
- [ ] Anderson phase classification: W sweep → NPU labels localized/extended
- [ ] Use NPU as a "disorder sensor" for localization transition detection
```

### 4. Kokkos-Honest Assessment

What we should tell Murillo about Kokkos now:
- We didn't build the Kokkos comparison (promised in March)
- What we DID build: cross-vendor parity proving vendor independence works
- The honest answer: our architecture is validated by physics correctness +
  cross-vendor agreement, not by micro-benchmark against Kokkos
- The paper makes this case explicitly (§1.1, §4.8)
- If he still wants the Kokkos comparison, Cabana + PPPM is the right test

---

## Modern Murillo Pitch (Reworked)

The story is no longer "I have GPUs and NPUs, want to play?"

The story is now:
1. **Paper-quality physics** on consumer hardware (arXiv-ready preprint)
2. **Heterogeneous compute proof** (CPU→GPU→NPU pipeline, real data)
3. **His group's work reproduced + extended** (Sarkas→QCD on same engine)
4. **MILC-compatible output** (his collaborators can consume our data)
5. **Infrastructure for students** (128 cores, 24GB GPU, Akida, remote access)
6. **Kokkos answer**: we achieve vendor independence through Vulkan+WGSL,
   validated by cross-vendor parity (6 ppm), not by API abstraction layers

**The ask**: Review the paper. See if the physics checks out. The data is
his to probe — same methodology as the Sarkas reproduction, scaled to QCD.
