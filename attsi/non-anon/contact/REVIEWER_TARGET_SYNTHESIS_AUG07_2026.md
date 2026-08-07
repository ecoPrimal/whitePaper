# Reviewer Target Synthesis — Three Domains, One System

**Date**: Aug 7, 2026 | **Wave**: 156  
**Status**: All three reviewers identified, two engaged, one pending first contact

---

## The Three Reviewers

| Reviewer | Domain | Affiliation | Connection | Status |
|---|---|---|---|---|
| **Michael Murillo** | Plasma physics, computational methods, reservoir computing | MSU (Professor) | Former instructor (AML), met for coffee, ongoing | ENGAGED — pre-submission review requested |
| **Thomas "TC" Chuna** | Lattice QCD algorithms, HMC, dynamical fermions | LANL (PhD student via Murillo) | Through Murillo, package delivered, ongoing | ENGAGED — arXiv review email drafted |
| **Ilya Kachkovskiy** | Spectral theory, Anderson localization, quasiperiodic operators | MSU (Asst. Prof., Mathematics) | NucBox purchase, in-person connection | PENDING — demo-ready, needs first outreach |

### What Each Validates

| Reviewer | Validates | System Component |
|---|---|---|
| Murillo | Computational methodology, DF64, GPU scaling, broader impact | barraCuda + hotSpring infrastructure |
| Chuna | HMC correctness, integrator diagnostics, MILC interop, fermion path | hotSpring lattice QCD engine |
| Kachkovskiy | Spectral primitives, Lanczos, Anderson localization, precision mathematics | barraCuda spectral + DF64 precision layer |

Together they cover the full stack: **precision arithmetic** (Kachkovskiy) → **physics engine** (Chuna) → **computational infrastructure** (Murillo).

---

## What Each Reviewer Can USE

### Murillo — Computational Infrastructure Consumer

| Capability | His Interest | How He Uses It |
|---|---|---|
| GPU heterogeneous compute | Reservoir computing, ESN on NPU | BrainChip Akida phase classification |
| Power efficiency benchmarks | Green computing, $/FLOP | 100× power efficiency data |
| Cross-vendor portability | Vendor independence | Same shaders on NVIDIA/AMD/Intel |
| Provenance chain | Reproducibility | BLAKE3 DAG for any computation |

**What to give him**: The arXiv preprint + access to the live system. He validates methodology and framing.

### Chuna — Lattice QCD Engine User

| Capability | His Interest | How He Uses It |
|---|---|---|
| SU(N) HMC engine | His PhD work (dynamical QCD at LANL) | Run configs, validate against MILC |
| MILC format I/O | Standard in his field | Import/export configurations |
| Omelyan integrator | Standard in his code | Compare ΔH, acceptance |
| GPU-accelerated CG solver | His daily tool | Benchmark against MILC/QUDA |
| Creutz ratios, Wilson loops | Standard observables | Cross-validate measurements |

**What to give him**: MILC-compatible config files + the `validate_production_qcd` binary. He validates physics correctness. If he can load our configs in MILC and get matching plaquettes, that's the strongest possible validation.

### Kachkovskiy — Spectral Primitive Consumer

| Capability | His Interest | How He Uses It |
|---|---|---|
| GPU Lanczos eigensolve | His daily research tool | Replace SciPy eigsh on his 5080 |
| Anderson 3D mobility edge | Foundation of his field | GPU at L=50+ (impossible in Python) |
| Hofstadter butterfly | Classic result in his area | High-res in seconds |
| Two-particle localization | His Bourgain paper | L² Hilbert space on GPU |
| DF64 extended precision | Small eigenvalue spacing | 14-digit precision where f64 fails |

**What to give him**: The `validate_spectral` binaries + API access. He validates mathematical correctness and can immediately benefit in his own research.

---

## The sunMemo Reshape

The SU(N) memo table (cached thermalized configurations) should be structured to serve all three:

| Component | Murillo's View | Chuna's View | Kachkovskiy's View |
|---|---|---|---|
| Config memo table | "Reproducibility infrastructure" | "Production gauge configs for measurement" | "Precomputed spectra for eigenvalue studies" |
| Precision tiers | "Performance-accuracy tradeoff study" | "DF64 vs f64 plaquette agreement" | "Extended precision for degenerate eigenvalues" |
| Cross-vendor | "Portability proof" | "MILC-compatible across hardware" | "Same eigenvalues on any GPU" |
| Provenance | "Computational audit trail" | "Configuration metadata for ILDG/MILC" | "Reproducible numerical experiments" |

### sunMemo Structure for Reviewer Access

```
configs/
├── su2/           → Kachkovskiy can use for spectral studies
├── su3/           → Chuna validates against MILC
├── su4-su8/       → Large-N scaling (all three)
├── milc_export/   → Direct MILC format for Chuna/Bazavov
└── spectral/      → Eigenvalue data for Kachkovskiy
```

---

## The MILC/Chuna Engine Connection

Chuna's path to validation:

```
1. hotSpring generates SU(3) config at β=6.0, 16⁴
2. Export via milc.rs → MILC v5 binary format
3. Chuna loads in MILC code → computes plaquette
4. Compare: must match to <0.01%
5. Reverse: Chuna exports MILC config → hotSpring reads → computes plaquette
```

This is the **strongest possible validation** for the lattice QCD paper — not "we reproduced published numbers" but "we read each other's files and get the same answer."

**Status**: `milc.rs` reader/writer is implemented and compiles. Needs a real MILC config to test against (from Chuna or NERSC archive).

---

## The Math/Silicon Puzzle — How It Fits Together

```
                    SILICON LAYER
                    ┌─────────────────────────────────┐
                    │  barraCuda (GPU compute substrate)│
                    │  DF64 · SpMV · Lanczos · WGSL   │
                    └──────────┬──────────────────────┘
                               │
          ┌────────────────────┼────────────────────────┐
          │                    │                         │
    SPECTRAL               GAUGE               INFRASTRUCTURE
    (Kachkovskiy)          (Chuna)              (Murillo)
    ┌──────────┐      ┌──────────────┐      ┌──────────────┐
    │ Anderson │      │ SU(N) HMC    │      │ Cross-vendor │
    │ Hofstadter│     │ Wilson action │      │ Provenance   │
    │ Lanczos  │      │ Omelyan      │      │ NPU/ESN      │
    │ DF64 prec│      │ MILC interop │      │ Power eff.   │
    └──────────┘      └──────────────┘      └──────────────┘
          │                    │                         │
          └────────────────────┼────────────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │  hotSpring (physics) │
                    │  Validation Spring   │
                    └─────────────────────┘
```

All three domains share:
- **DF64 precision** — Kachkovskiy needs it for eigenvalue problems, Chuna for plaquettes, Murillo validates the methodology
- **GPU acceleration** — All three benefit from consumer GPU, no CUDA
- **Provenance** — All three can independently verify results
- **Cross-vendor** — Same computation, different hardware, same answer

---

## Kachkovskiy Gap Analysis (Pending Contact)

### Ready Now

| Item | Status |
|---|---|
| 11 papers in his domain reproduced | ✅ 417+ checks passing |
| GPU Lanczos to machine precision | ✅ 1e-15 parity |
| Hofstadter butterfly in 3s | ✅ |
| Anderson 3D mobility edge | ✅ W_c = 16.26 ± 0.95 |
| His Bourgain paper validated (single-particle) | ✅ |
| Email draft written | ✅ |
| Review package written | ✅ |

### Gaps Before Contact

| Gap | Priority | Effort | Why |
|---|---|---|---|
| GPU Lanczos at N=10,000+ | P0 | 1-2 days | His lattices are large — must show scaling |
| SciPy `eigsh` comparison benchmark | P0 | 4 hrs | Must answer "faster than what I use?" |
| Two-particle Anderson on GPU | P1 | 1 week | His Bourgain paper headline — L=200 on 5080 |
| Large-N scaling curves (N vs time) | P1 | 1 day | Show where GPU dominates CPU |
| In-person demo (Hofstadter on laptop) | P0 | 0 | Already possible — just needs scheduling |

### Outreach Trigger

Contact Kachkovskiy when:
1. GPU Lanczos runs at N=10,000+ with timing data
2. SciPy comparison shows clear GPU advantage
3. Can demo two-particle Anderson at L≥100

Or: just go to Wells Hall with the Hofstadter butterfly on a laptop. The in-person demo is the hook.

---

## Unified Review Package Strategy

Each reviewer gets a **customized package** from the same system:

| Reviewer | Package Contents |
|---|---|
| **Murillo** | Preprint PDF + neuromorphic datasheet + cost analysis + provenance walkthrough |
| **Chuna** | Preprint PDF + MILC config exchange protocol + `validate_production_qcd` binary + HMC diagnostic data |
| **Kachkovskiy** | Spectral review package (already written) + GPU Lanczos benchmarks + Hofstadter demo + Anderson 3D data |

### What We Ask Each

| Reviewer | Question |
|---|---|
| Murillo | "Is the computational methodology sound? Is DF64 novel? Is the cost argument credible?" |
| Chuna | "Do the plaquettes match? Is the HMC correctly implemented? Can you read our configs in MILC?" |
| Kachkovskiy | "Are the eigenvalues correct? Does GPU Lanczos give you correct Anderson statistics? Would this be useful for your research?" |

---

## Next Actions

| Action | Owner | Timeline |
|---|---|---|
| Send Chuna the arXiv preprint review email | Kevin | Ready now (email drafted) |
| Send Murillo the preprint for methodology review | Kevin | Ready now |
| Close Kachkovskiy P0 gaps (GPU Lanczos N=10k, SciPy comparison) | hotSpring | 1-2 days |
| Demo Hofstadter at Wells Hall (in-person) | Kevin | When on campus |
| Generate MILC export of 16⁴ β=6.0 config for Chuna | hotSpring | Today (code exists) |
| Acquire real MILC config from NERSC or Chuna for import test | Kevin/Chuna | After Chuna responds |

---

## The Endgame

Three domain experts using the system for their own work:
- Murillo references it in computational methodology discussions
- Chuna exchanges configs with it as part of his LANL workflow
- Kachkovskiy runs GPU eigensolves on his 5080 for his papers

The paper is the receipt. The system is the product.
