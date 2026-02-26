# Sub-Thesis 07: Sovereign Warm Dense Matter Simulation on Consumer GPU

**Date:** February 26, 2026
**Status:** **Validated** — hotSpring v0.6.14 completes all plasma MD and lattice QCD reproduction. 60/60 Sarkas observable checks (N=10k, 80k steps, $0.044). Deconfinement phase transition at β_c=5.69 on RTX 3090 (32⁴, 13.6h, $0.58). DF64 core streaming delivers 9.9× native f64 throughput. Transport coefficients D*, η*, λ* via GPU Green-Kubo. 664 hotSpring tests, 39/39 validation suites
**Domain:** Plasma physics, computational science, distributed computing
**Novelty:** No prior work demonstrates full WDM transport coefficient
reproduction on consumer GPU via vendor-agnostic shaders; no prior work
frames distributed consumer GPU networks as alternatives to institutional
HPC for plasma physics
**Cross-Spring:** hotSpring (MD + transport + lattice QCD) × neuralSpring
(surrogate learning + LSTM) × groundSpring (uncertainty propagation)

---

## Abstract

We demonstrate that warm dense matter (WDM) — the plasma regime central
to inertial confinement fusion (ICF), planetary interiors, and stellar
evolution — can be simulated on consumer GPU hardware using the BarraCUDA
compute stack. The 70-author "Roadmap for warm dense matter physics"
(Murillo et al., arXiv:2505.02494, revised Feb 13, 2026) identifies
computational accessibility as a critical bottleneck: state-of-the-art
codes require institutional HPC allocations, creating artificial scarcity
in who can do WDM science.

We propose that hotSpring's validated pipeline — Yukawa MD (9/9 GPU),
Green-Kubo transport (13/13), nuclear EOS (195/195), screened Coulomb
(23/23), and lattice QCD (full GPU pipeline) — already contains the
primitives needed for WDM simulation at modest system sizes. The gap is
not capability but scale, and scale is a distribution problem, not an
algorithm problem.

We frame this as the **GPU-as-hot-water-heater** thesis: every consumer
GPU running WGSL shaders through open Vulkan drivers can contribute to
WDM computation while its waste heat serves domestic purposes. A network
of 1,000 idle consumer GPUs, each contributing 1 GPU-hour/day, provides
365,000 GPU-hours/year — equivalent to a mid-tier institutional HPC
allocation — at zero marginal compute cost and with waste heat as a
useful byproduct.

---

## 1. The Problem: WDM Computation Is Artificially Scarce

### 1.1 What Is Warm Dense Matter?

WDM occupies the regime between cold condensed matter and hot classical
plasma: temperatures of 10⁴–10⁸ K, densities of 0.1–100 g/cm³. At these
conditions, neither cold-matter approximations (band theory, perturbation
theory) nor hot-plasma approximations (Debye-Hückel, ideal gas) apply.
The electrons are partially degenerate, ions are strongly coupled, and
quantum effects coexist with classical dynamics.

WDM matters because it describes:
- **ICF fuel**: the deuterium-tritium capsule during NIF implosion
- **Planetary cores**: Jupiter, Saturn, super-Earths
- **Stellar interiors**: white dwarf envelopes, brown dwarfs
- **Astrophysical shocks**: supernovae, neutron star mergers

### 1.2 The Computational Bottleneck

The WDM roadmap (arXiv:2505.02494) identifies several open computational
challenges:
1. **Transport coefficients** at WDM conditions (partially ionized,
   strongly coupled) — extending Stanton-Murillo (2016) beyond the
   classical regime
2. **Equation of state** for mixtures under compression — beyond SEMF/HFB
3. **Dynamic structure factor S(q,ω)** — the key experimental diagnostic
   for X-ray Thomson scattering (XRTS) at NIF
4. **Orbital-free DFT** for large-scale WDM simulations
5. **Wavepacket MD** for quantum ion dynamics

Current state: these calculations require institutional HPC (Frontier,
Summit, Perlmutter). A typical WDM transport calculation uses 4–8 GPUs
for days. Allocation proposals take months. Results are published behind
paywalls.

### 1.3 The Sovereign Alternative

hotSpring has already reproduced Stanton-Murillo transport on a single
RTX 4070 at ~$0.02 compute cost. The Yukawa MD pipeline runs at 34.7×
CPU speed on GPU. The lattice QCD pipeline achieves 40× CPU speed with
streaming GPU HMC. The nuclear EOS pipeline covers 195 nuclei.

The question is not whether consumer GPU can do WDM physics — hotSpring
has already proven it can for classical plasma. The question is whether
the extensions to WDM conditions (partial ionization, quantum effects,
higher temperatures) are tractable on the same hardware.

---

## 2. What hotSpring Already Has

### 2.1 Validated Primitives

| Primitive | hotSpring Paper | Checks | WDM Extension |
|-----------|----------------|--------|---------------|
| Yukawa MD (all-pairs + cell-list) | Paper 1 | 9/9 GPU | Extend to screened potentials with partial ionization |
| Green-Kubo transport (D*, η*, λ*) | Paper 5 | 13/13 | Extend to WDM conditions (higher T, Z*) |
| Nuclear EOS (SEMF→HFB) | Paper 4 | 195/195 | Use as cold-curve input for WDM EOS |
| Screened Coulomb eigensolve | Paper 6 | 23/23 | Yukawa screening at WDM parameters |
| FFT (1D + 3D, f64) | ToadStool | 14/14 GPU | Required for S(q,ω) computation |
| Lattice QCD HMC | Papers 8-12 | Full GPU | Monte Carlo sampling methodology |
| Streaming GPU dispatch | Paper 10+ | 9/9 | Zero CPU→GPU transfer architecture |

### 2.2 The FFT Gap Is Closed

ToadStool commit `1ffe8b1a` delivered `Fft1DF64` and `Fft3DF64` with
roundtrip validation to 1e-10 on RTX 3090. This was THE major blocker
for S(q,ω) computation. With FFT available, the dynamic structure factor
becomes:

```
S(q,ω) = (1/N) |∫ Σ_j exp(iq·r_j(t)) exp(-iωt) dt|²
```

which is a spatial Fourier transform (over particle positions) followed
by a temporal Fourier transform (over MD trajectory). Both transforms now
run on GPU.

### 2.3 What's Missing

| Gap | Effort | Priority |
|-----|--------|----------|
| Partial ionization model (Z* from Thomas-Fermi or average-atom) | Medium | P1 |
| Electron-ion coupling (two-temperature model extension) | Medium | P1 |
| Wavepacket evolution (quantum ion dynamics) | High | P3 |
| Orbital-free kinetic energy functional | High | P3 |
| Multi-component mixture EOS | Medium | P2 |

---

## 3. The GPU-as-Hot-Water-Heater Thesis

### 3.1 The Core Argument

A consumer GPU running WDM simulations at 200W produces:
- **Useful computation**: ~10 TFLOPS f64 sustained
- **Waste heat**: 200W thermal output

In a residential setting, this waste heat can offset space heating or
water heating costs. A GPU mining cryptocurrency wastes energy on proof
of meaningless work. A GPU running WDM simulations wastes energy on
proof of meaningful work — the same Joules produce both heat and science.

### 3.2 The Economics

| Resource | Institutional HPC | Consumer GPU Network |
|----------|-------------------|---------------------|
| Hardware | $600M (Frontier) | $600/node × N nodes |
| Allocation | Competitive proposal (months) | Volunteer (immediate) |
| Energy | Grid power at industrial rate | Residential, offset by heating |
| Access | Credential-gated | Open (AGPL-3.0) |
| Results | Journal paywall | Public domain |
| Vendor lock | CUDA (NVIDIA-only) | WGSL/Vulkan (any GPU) |

### 3.3 Why WGSL/Vulkan Matters

BarraCUDA's WGSL shaders run on any GPU exposing Vulkan with
SHADER_F64. This includes:
- NVIDIA (RTX 2070 through 5090, Titan V)
- AMD (RX 6000+, MI-series)
- Intel (Arc A-series)
- Qualcomm (Adreno, via Android Vulkan)
- Apple (via MoltenVK translation layer)

CUDA locks WDM computation to NVIDIA. WGSL liberates it. The same
physics shader runs identically on a $300 used RTX 2070 and a $2000
RTX 5090 — only the speed changes, not the math.

### 3.4 Distributed Architecture

The NUCLEUS mesh (biomeOS + BearDog + Songbird) provides:
- **Task distribution**: BOINC-style work units, but with covalent trust
- **Verification**: deterministic MD trajectories verify via hash
- **Aggregation**: independent parameter sweeps combine trivially
- **Fault tolerance**: any node can fail; work units redistribute

WDM transport calculations are embarrassingly parallel across the
(κ, Γ, T) parameter space. Each point is an independent MD run. A
network of 100 GPUs can sweep 100 parameter points simultaneously.

---

## 4. Experimental Design

### 4.1 Phase 1: Reproduce FPEOS on Consumer GPU

**Target**: Militzer's First-Principles Equation of State database
(Berkeley, open C++/Python code). Reproduce EOS tables for hydrogen,
helium, and carbon at WDM conditions.

**Method**: Port average-atom + MD pipeline to BarraCUDA. Validate
against published FPEOS tables. Measure accuracy vs compute cost.

**Success criterion**: Agreement with FPEOS tables to within published
uncertainties, running on a single RTX 4070.

### 4.2 Phase 2: WDM Transport Coefficients

**Target**: Extend Stanton-Murillo (Paper 5) to WDM conditions.

**Method**: Run Yukawa MD at elevated temperatures (T > 10 eV) with
density-dependent screening. Compute Green-Kubo transport. Compare
to published DFT-MD values from the roadmap comparison studies.

**Success criterion**: D*, η*, λ* within 50% of DFT-MD for at least
3 (ρ, T) points in the WDM regime.

### 4.3 Phase 3: Dynamic Structure Factor

**Target**: Compute S(q,ω) from MD trajectories for comparison with
NIF XRTS experimental data.

**Method**: Spatial FFT of particle positions → intermediate scattering
function F(q,t) → temporal FFT → S(q,ω). All on GPU via validated
FFT primitives.

**Success criterion**: S(q,ω) peak positions and widths match published
MD results for hydrogen at WDM conditions.

### 4.4 Phase 4: Distributed Parameter Sweep

**Target**: Full (ρ, T) sweep of transport coefficients using the
NUCLEUS mesh (2 GPUs initially, scaling to N).

**Method**: biomeOS distributes MD work units across available GPUs.
Each GPU runs an independent (κ, Γ) point. Results aggregate into a
transport table.

**Success criterion**: Linear scaling of throughput with GPU count.
Deterministic verification of all results via trajectory hash.

---

## 5. Connection to NIF and the Ignition Era

### 5.1 NIF Context

The National Ignition Facility achieved fusion energy gain in December
2022, with 6 subsequent successful shots reaching peak gain of 2.3× at
5.2 MJ (as of the Feb 2026 NIF/JLF User Groups Meeting). This has
created unprecedented demand for WDM simulation to design future targets,
understand capsule physics, and optimize implosion conditions.

### 5.2 Murillo's Role

Michael Murillo (MSU, Computational Mathematics, Science, & Engineering)
co-authored the WDM roadmap (arXiv:2505.02494) and has published
extensively on transport coefficients in dense plasma. His Stanton-Murillo
(2016) transport paper is hotSpring Paper 5 — the first complete
reproduction in our pipeline. His screened Coulomb work is Paper 6.

hotSpring was built to validate BarraCUDA against Murillo's published
results. Extending to WDM conditions is the natural next step — using
the same infrastructure, the same validation methodology, the same
consumer hardware.

### 5.3 What This Proves

If a single graduate student with a $600 GPU can reproduce WDM transport
coefficients that currently require institutional HPC allocations, it
demonstrates that:

1. **The computation is not the bottleneck** — the algorithm is
2. **Access to physics is artificially scarce** — not technically scarce
3. **Open-source GPU stacks can do real science** — not just benchmarks
4. **Distributed consumer GPU networks are viable** — not just theoretical

---

## 6. Connection to Other baseCamp Sub-Theses

| Sub-Thesis | Connection |
|-----------|------------|
| 01 (Anderson QS) | Anderson localization is spectral theory; WDM uses same eigensolve primitives |
| 02 (Frozen Fossil) | Constrained evolution under extreme thermal constraint (WDM is the ultimate thermal constraint) |
| 03 (Bioag) | Distributed sensing → distributed computing; same NUCLEUS infrastructure |
| 04 (Sentinel) | WDM diagnostics (XRTS) are a form of environmental sensing under extreme conditions |
| 05 (Cross-species) | Multi-component plasma mixtures are the physics analog of multi-species communities |
| 06 (No-till) | Both apply physics principles (Anderson, transport) to applied problems using consumer compute |

### 6.1 neuralSpring Integration

neuralSpring contributes validated ML surrogates and spectral analysis directly
to WDM science:

- **WDM surrogates** (nW-01 through nW-05): MLP surrogate models for EOS
  interpolation — the Diaw surrogate (Paper P20) is already validated.
  Remaining queue: pair correlation functions, transport coefficients,
  dynamic structure factor, dense hydrogen opacity
- **Spectral analysis**: neuralSpring's `eigh_f64` eigendecomposition and
  `spectral_entropy` (rewired to `barracuda::stats::shannon_from_frequencies`
  in Session 81) apply directly to plasma eigenmode analysis
- **Session 81 status**: 129+ named tolerances, 39 BarraCUDA rewires,
  full PyTorch deterministic seeding for reproducible surrogate training

---

## 7. Reproduction Targets

See `hotSpring/specs/PAPER_REVIEW_QUEUE.md` Tier 4 for the full list
of WDM reproduction targets (Papers 32-42).

### Priority Order

1. **Paper 33 (atoMEC)**: Average-atom model — ideal Phase 0 Python control
2. **Paper 32 (FPEOS)**: EOS tables — data validation, interpolation
3. **Paper 35 (WDM transport)**: Extend Stanton-Murillo to WDM conditions
4. **Paper 38 (S(q,ω))**: Dynamic structure factor — FFT + MD
5. **Paper 36 (Dragon OF-DFT)**: Orbital-free DFT — new primitive
6. **Paper 40 (XRTS diagnostics)**: Model-free temperature extraction

---

## 8. Cost Projection

| Phase | Hardware | Time | Cost |
|-------|----------|------|------|
| Phase 1 (FPEOS reproduction) | 1× RTX 4070 | ~1 week | ~$2 |
| Phase 2 (WDM transport) | 1× RTX 4070 | ~2 weeks | ~$5 |
| Phase 3 (S(q,ω)) | 1× RTX 4070 | ~1 week | ~$2 |
| Phase 4 (distributed sweep) | 2× GPU (NUCLEUS) | ~1 month | ~$10 |
| **Total** | | ~2 months | **~$19** |

Compare to institutional WDM allocation: ~100,000 GPU-hours at ~$1/GPU-hr
= $100,000. Even at 100× less accuracy, the cost ratio is 5,000:1.

---

## 9. The Broader Vision

This sub-thesis is not about competing with Frontier. It is about proving
that the mathematical workflow is correct, portable, and accessible. If
the physics runs correctly on one consumer GPU, it runs correctly on any
consumer GPU. If it runs on any consumer GPU, it runs on every idle GPU.
If it runs on every idle GPU, WDM simulation becomes a public utility
rather than an institutional privilege.

The shaders are the mathematics. The GPU is the substrate. The heat is
the byproduct. The science is the point.
