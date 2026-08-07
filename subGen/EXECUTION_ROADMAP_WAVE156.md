# Execution Roadmap — Wave 156+

**Date**: Aug 7, 2026  
**Scope**: From "science complete" to "reviewers using the system"  
**Gate**: strandGate  
**Philosophy**: Paper is ancillary. System is the deliverable. Reviewers are users.

---

## Current State (validated Aug 7, 2026)

- SU(N) engine: N=2,3,4,5,6,8 — all pass production validation
- DF64 precision: 14 digits, matrix ALL PASS on RTX 3090 + RX 6950 XT
- GPU HMC: 40–53× speedup on consumer cards
- Literature match: β=6.0/6.2 to 0.01% (Necco-Sommer, Bali)
- Cross-vendor: 6 ppm NVIDIA/AMD agreement
- MILC reader/writer: implemented, compiles, needs external config test
- Rubric: 40/42 done (3 remaining are upstream)
- 25,200 LOC deprecated code fossilized
- Ecosystem cascaded (23/24 repos synced)
- 4 primals rebuilt and deployed from fresh musl builds

---

## Three Execution Tracks

### Track A: MILC Validation Loop (Chuna/Bazavov target)

**Goal**: Bidirectional config exchange with the MILC collaboration code.

```
Phase 1: Export (we → them)
├── Generate production SU(3) config at β=6.0, 16⁴, 1000 trajectories
├── Export via milc.rs → MILC v5 binary (big-endian, CRC32)
├── Compute plaquette header value
├── Package as: config file + plaquette + provenance hash
└── Deliverable: a file Chuna can `su3_gauge_read` in MILC code

Phase 2: Import (them → us)
├── Acquire public MILC config (NERSC gauge archive or from Chuna)
├── Read via milc.rs → internal Lattice representation
├── Compute plaquette, compare to MILC-reported value
├── Report: Δ⟨P⟩ < 10⁻⁶ (or diagnose discrepancy)
└── Deliverable: proven interoperability

Phase 3: Round-trip (full circle)
├── Export our config → MILC format
├── Read it back → compare bitwise to original
├── Repeat with MILC-generated config
└── Deliverable: CRC32 checksum match on both paths
```

**Binary**: `milc_validation_loop` (new, needs writing)  
**Dependency**: `src/lattice/milc.rs` (implemented, compiles)  
**Timeline**: 1 day code, 1 day validation

---

### Track B: Spectral Scaling (Kachkovskiy target)

**Goal**: GPU Lanczos at N=10,000+ with SciPy comparison timing.

```
Phase 1: Large-N Lanczos
├── Anderson 3D tight-binding at L=22 (N=10,648 sites)
├── GPU Lanczos: 50 eigenvalues on RTX 3090
├── CPU Lanczos: same matrix, same eigenvalue count
├── Time both, report speedup
└── Deliverable: "GPU Lanczos at N=10k in X seconds vs CPU Y seconds"

Phase 2: SciPy Comparison
├── Export same sparse matrix (CSR) to NPZ format
├── Python script: scipy.sparse.linalg.eigsh(H, k=50)
├── Time on same hardware (EPYC 7452)
├── Report: eigenvalue parity + speedup
└── Deliverable: "GPU Lanczos is Z× faster than SciPy eigsh"

Phase 3: Two-Particle (stretch)
├── Two-particle Anderson Hamiltonian at L=100 (N=10,000 = L²)
├── Interaction term: V(x₁,x₂) = U δ(x₁-x₂)
├── GPU Lanczos on 10k×10k sparse matrix
├── Identify localization transition as function of U/W
└── Deliverable: Bourgain-Kachkovskiy validation on GPU
```

**Binary**: extend `validate_gpu_lanczos` or new `bench_lanczos_scaling`  
**Dependency**: `barracuda::spectral::lanczos` (validated to N=1000)  
**Timeline**: 2 days for Phase 1-2, 1 week for Phase 3

---

### Track C: sunMemo Reshape + Production Campaigns

**Goal**: Config memo table structured for reviewer access, large-N statistics.

```
Phase 1: Memo Structure
├── Organize ~/.local/share/hotspring/configs/ by gauge group
├── Add MILC export path for all SU(3) configs
├── Add eigenvalue metadata for spectral configs
├── Index file with: β, V, N_traj, ⟨P⟩, provenance hash
└── Deliverable: queryable config archive

Phase 2: SU(N≥4) Thermalization
├── SU(4) at β=10.0, 12⁴: 500 trajectories (CPU-bound, ~days)
├── SU(5) at β=16.0, 8⁴: 500 trajectories
├── SU(6) at β=24.0, 8⁴: 500 trajectories
├── SU(8) at β=40.0, 8⁴: 200 trajectories
└── Deliverable: large-N plaquette table with statistics

Phase 3: 32⁴ Production
├── SU(3) at β=6.0, 32⁴: 200 trajectories (GPU, ~hours)
├── SU(3) at β=6.2, 32⁴: 200 trajectories
├── Measure full observable battery on each
└── Deliverable: large-volume data for continuum-limit evidence
```

**Binary**: `arxiv_thermalize_sun` (exists), `arxiv_measure_battery` (exists)  
**Timeline**: Days to weeks (thermalization-bound)

---

## Optimization Targets (from profiling, Aug 7)

Execute in parallel with validation tracks:

| Target | Impact | Approach | Priority |
|---|---|---|---|
| SU3 matmul → cooperative matrix | 5–10× matmul kernel | WMMA via wgpu cooperative_matrix extension | P2 (high impact, high effort) |
| DF64 compensated summation in hot loops | Better precision, no cost | Wire `df64_compensated_sum.wgsl` into force/plaquette | P1 (low effort) |
| AMD DF64 routing preference | Better precision on AMD | PrecisionBrain route DF64 reductions to AMD when available | P2 |
| PRNG → TMU LUT | 2× heat bath throughput | Texture sampling for Box-Muller transcendentals | P3 (blocked on wgpu texture compute) |
| Tiled dispatch for 16⁴+ | Recover 53×→40× plateau | Workgroup tiling strategy for large volumes | P2 |

---

## Reviewer Delivery Schedule

| Reviewer | Package | Trigger | Channel |
|---|---|---|---|
| **Chuna** | Preprint PDF + MILC config + `validate_production_qcd` + HMC data | Email ready now | Email (LANL) |
| **Murillo** | Preprint PDF + neuromorphic datasheet + cost/provenance walkthrough | Email ready now | Email/coffee (MSU) |
| **Kachkovskiy** | Spectral review package + GPU Lanczos N=10k benchmark | After Track B Phase 1-2 | In-person (Wells Hall) |

---

## Evolution Path (Rung 2 Preparation)

While reviewers evaluate Rung 1, prepare Rung 2 infrastructure:

| Component | Status | Next Step |
|---|---|---|
| Staggered Dirac operator (GPU) | Shader exists (`dirac_stencil`) | Production validation |
| Multi-shift CG solver | Implemented (`resident_cg.rs`) | Unidirectional path hardening |
| RHMC rational approximation | Code exists (`gpu_rhmc.rs`) | Connect to resident CG |
| Pseudofermion generation | Implemented | Validate against CPU reference |
| Fermion force | Implemented (`pf_force` kernel) | Profile + optimize |

**Rung 2 milestone**: Generate one Nf=4 dynamical config at β=5.5, 8⁴, confirm plaquette shift from quenched value.

---

## Success Criteria

| Milestone | Definition of Done |
|---|---|
| MILC interop proven | Bidirectional config exchange, Δ⟨P⟩ < 10⁻⁶ |
| Kachkovskiy engaged | In-person demo completed, feedback received |
| Chuna validates | Loads our MILC config, confirms plaquette |
| Large-N table complete | SU(4,5,6,8) plaquettes with jackknife errors |
| 32⁴ production | 200+ trajectories measured, observables in paper |
| Rung 2 first config | One dynamical fermion trajectory completes |
| Paper submitted | arXiv hep-lat, after reviewer feedback incorporated |

---

## Priority Stack (what to execute NOW)

```
TODAY:
1. Write hotSpring specs/ (this doc's execution plans as technical specs)
2. Generate MILC export of existing 16⁴ β=6.0 config
3. Start GPU Lanczos N=10k benchmark

THIS WEEK:
4. Complete MILC validation loop (round-trip test)
5. Complete SciPy comparison benchmark
6. Wire compensated summation into force kernel
7. Start SU(4) thermalization campaign

NEXT WEEK:
8. Package for Chuna (MILC config + preprint)
9. Package for Murillo (preprint + methodology review)
10. Two-particle Anderson L=100 on GPU (Kachkovskiy stretch)
```
