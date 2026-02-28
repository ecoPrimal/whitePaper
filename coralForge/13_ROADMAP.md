# coralForge Roadmap

## Release Philosophy

coralForge evolves through phases with strict gate criteria. No phase begins until the previous phase's gates are green. No shortcuts, no technical debt carried forward.

---

## Phase Map

```
Phase A ─── Phase B ─── Phase C ─── Phase D ─── Phase E ─── Phase F
Evoformer   AF3 Ext     BarraCUDA   Inference   LTEE        Open
Primitives  Primitives  Integration Pipeline    Analysis    Release
  ✓ DONE     ✓ DONE     ► NEXT      planned     planned     planned
```

---

## Phase A: Evoformer Primitives (COMPLETE)

**Sessions 85–89** | **Status: Done**

Implemented the core AlphaFold2 Evoformer from published algorithms.

### Deliverables

| Primitive | Algorithm | LOC | Checks |
|-----------|:---------:|:---:|:------:|
| GELU, LayerNorm, Softmax | — | 173 | 12 |
| SDPA (scores, apply, full) | — | 134 | 8 |
| Triangle mul outgoing | 11 | 55 | 6 |
| Triangle mul incoming | 12 | 48 | 6 |
| Triangle attention scores | 13-14 | 92 | 4 |
| MSA row attention (with pair bias) | 7 | 82 | 6 |
| MSA column attention | 8 | 64 | 4 |
| Outer product mean | 10 | 48 | 4 |
| IPA scores + apply | 22 | 307 | 8 |
| Backbone update | 23 | 141 | 3 |
| Torsion angles | — | 166 | 3 |
| Frame operations | — | 168 | 8 |

### Gate Criteria (all met)

- [x] Every primitive has a Python NumPy baseline
- [x] Every primitive passes Rust unit tests
- [x] Validation binary checks all against baselines
- [x] Zero clippy warnings (pedantic)
- [x] Zero doc warnings
- [x] BaselineProvenance for every baseline file

---

## Phase B: AlphaFold3 Extended Primitives (COMPLETE)

**Sessions 90–94** | **Status: Done**

Added AlphaFold3's diffusion decoder, pairformer, and confidence heads.

### Deliverables

| Primitive | Source | LOC | Checks |
|-----------|--------|:---:|:------:|
| Noise schedules (cosine, linear) | Ho/Nichol | 52 | 4 |
| Forward diffusion | Ho 2020 | 22 | 2 |
| DDPM reverse step | Ho 2020 | 33 | 4 |
| DDIM reverse step | Song 2020 | 41 | 4 |
| SE(3) equivariant noise | Abramson 2024 | 22 | 4 |
| Center-of-mass removal | — | 25 | 2 |
| Pair transition FFN | — | 40 | 2 |
| Sinusoidal embedding | Vaswani 2017 | 24 | 2 |
| Timestep conditioning | Abramson 2024 | 34 | 2 |
| Pairformer block | Abramson 2024 | 95 | 6 |
| pLDDT head | Jumper 2021 | 23 | 3 |
| PAE head | Jumper 2021 | 51 | 3 |
| pDE head | Abramson 2024 | 49 | 3 |
| Ranking score | Abramson 2024 | 36 | 2 |

### Gate Criteria (all met)

- [x] 5 Python baseline scripts, 62/62 Python checks
- [x] 55/55 Rust validation checks
- [x] 37/37 GPU (df64 WGSL) validation checks
- [x] 15 df64 WGSL shaders, all max diff < 1e-6
- [x] coralForge rename complete (sovereign_folding → coral_forge)
- [x] 139+ named tolerances, zero inline magic numbers
- [x] 24 expect() → require!() in validation binaries
- [x] All 34 BaselineProvenance constants documented

---

## Phase C: BarraCUDA Integration (NEXT)

**Target: Sessions 95–105** | **Status: Planning**

Replace hand-written loops with BarraCUDA CPU primitives for the performance-critical path.

### Milestones

| # | Milestone | Description | Gate |
|:-:|-----------|-------------|------|
| C.1 | GEMM integration | `triangle_mul_*` → `barracuda::tensor::matmul` | All triangle checks pass |
| C.2 | Attention integration | `sdpa_*` → `barracuda::attention::scaled_dot_product` | All attention checks pass |
| C.3 | LayerNorm integration | `layer_norm` → `barracuda::norm::layer_norm` | All norm checks pass |
| C.4 | Rayon parallelism | Outer loops over batch/head dimensions | Wall time ≤ 50% of Phase B |
| C.5 | Memory optimization | Buffer reuse, allocation pooling | Peak memory ≤ 1.5× theoretical |
| C.6 | Integration test | Full pairformer block via BarraCUDA | Bit-for-bit match with Phase B |

### Dependencies

```
C.1 ──→ C.2 ──→ C.6
 │              ↗
 └── C.3 ──── C.4 ──→ C.5
```

C.1 (GEMM) must land first because triangle multiplication is the bottleneck. C.4 (Rayon) requires C.1-C.3 to be stable.

### Gate Criteria

- [ ] All 154 existing checks still pass (no regression)
- [ ] BarraCUDA CPU path reproduces f64 reference within tolerance
- [ ] Wall-clock time for pairformer block ≤ 5ms at N=32 (currently ~18ms)
- [ ] No new `unsafe` blocks
- [ ] Memory usage profiled and documented

---

## Phase D: Inference Pipeline (PLANNED)

**Target: Sessions 106–130** | **Status: Design**

Build the end-to-end structure prediction pipeline: sequence in → coordinates out.

### Milestones

| # | Milestone | Description | Gate |
|:-:|-----------|-------------|------|
| D.1 | FASTA parser | Read protein sequences | Unit tests for common formats |
| D.2 | MSA search | Local HHblits/MMseqs2 interface | MSA generated for test sequences |
| D.3 | Feature extraction | MSA → input features (Alg 1-4) | Features match OpenFold reference |
| D.4 | Evoformer stack | 48-block Evoformer loop | Shape checks at each block |
| D.5 | Structure Module | 8-iteration IPA + backbone | Backbone frames converge |
| D.6 | AF3 diffusion path | Pairformer + DDPM/DDIM | Denoised coordinates |
| D.7 | Recycling | 3× recycling with gradient stop | Convergence check |
| D.8 | Output formatting | PDB/mmCIF coordinate output | Valid files pass PDB validation |
| D.9 | Weight loading | Load trained AF2/AF3 weights | Shapes match, forward pass runs |
| D.10 | End-to-end test | Predict known structure (T1024) | LDDT > 0.7 |

### Dependencies

```
D.1 ──→ D.3 ──→ D.4 ──→ D.5 ──→ D.7 ──→ D.10
              ↗        ↘     ↗
D.2 ────┘     D.6 ────┘
                        ↘
                    D.8 ──→ D.10
                    D.9 ──→ D.10
```

### Key Decisions (deferred)

- **MSA strategy**: HMMER reimplementation vs MMseqs2 subprocess vs precomputed
- **Weight source**: AlphaFold2 (publicly released) vs AF3 (not released as of Feb 2026)
- **Memory tiling**: Pair representation chunking for proteins > 500 residues
- **Recycling**: Whether to implement gradient-based or input-based recycling

### Gate Criteria

- [ ] Predicts at least one known structure to LDDT > 0.7
- [ ] Full pipeline runs on RTX 4070 (12 GB) for proteins ≤ 300 residues
- [ ] No cloud, no external API, no Python at runtime
- [ ] All existing 154+ checks still pass
- [ ] Pipeline documented with timing breakdown

---

## Phase E: LTEE Structural Analysis (PLANNED)

**Target: Sessions 131–160** | **Status: Concept**

Apply coralForge to LTEE frozen fossil record for biological validation of constrained evolution.

### Milestones

| # | Milestone | Description | Gate |
|:-:|-----------|-------------|------|
| E.1 | Gene panel | Define 50-gene target panel from LTEE literature | Panel documented, literature citations |
| E.2 | Sequence acquisition | Obtain LTEE gene sequences (public GenBank) | Sequences downloaded, verified |
| E.3 | Structure prediction | Predict structures for ancestral + evolved variants | Coordinates generated, pLDDT > 0.7 |
| E.4 | Structural comparison | RMSD, TM-score, LDDT between ancestor/evolved | Comparison metrics computed |
| E.5 | Convergence analysis | Cross-population structural convergence | Statistical tests, figures |
| E.6 | Temporal dynamics | Structure change vs generation time | Trajectory plots |
| E.7 | Citrate precursor | Ara-3 Cit+ structural precursor analysis | Structural pathway documented |
| E.8 | Publication draft | Results formatted for journal submission | Draft complete |

### Science Questions

1. **Structural convergence**: Do independently evolved populations find the same structural solutions?
2. **Trajectory dynamics**: Is structural evolution gradual or punctuated?
3. **Hitchhiker analysis**: Do neutral structural changes correlate with linked beneficial mutations?
4. **Fastidiousness**: Does genome streamlining under glucose-minimal constraint simplify fold space?
5. **Citrate innovation**: What structural precursors enabled the Ara-3 citrate phenotype?

### Gate Criteria

- [ ] At least 20 gene structures predicted with pLDDT > 0.7
- [ ] Cross-population comparison for at least 5 genes
- [ ] Statistical significance established for convergence claims
- [ ] All analyses reproducible from committed scripts
- [ ] Results connect to thesis Chapter 14 biological validation

---

## Phase F: Open Release (PLANNED)

**Target: Sessions 161+** | **Status: Vision**

Release coralForge as a standalone crate for the broader research community.

### Milestones

| # | Milestone | Description | Gate |
|:-:|-----------|-------------|------|
| F.1 | Crate extraction | Separate `coral_forge` crate from neuralSpring | Builds independently |
| F.2 | API stabilization | Review and freeze public API | Semver 0.1.0 |
| F.3 | Documentation | docs.rs-ready documentation | `cargo doc` complete |
| F.4 | Examples | Runnable examples for key use cases | Examples compile and run |
| F.5 | Benchmarks | Criterion benchmarks for all primitives | Benchmark suite passes |
| F.6 | CI/CD | GitHub Actions for fmt/clippy/test/doc | All gates green |
| F.7 | crates.io | Publish to crates.io | Published, installable |
| F.8 | Paper | Companion paper for coralForge | Submitted |

### Release Criteria

- [ ] Zero `unsafe`
- [ ] Zero `unwrap()` / `expect()` in library code
- [ ] 100% public API documented
- [ ] All primitives benchmarked
- [ ] MSRV (minimum supported Rust version) documented
- [ ] AGPL-3.0-or-later license applied
- [ ] No Python at runtime
- [ ] No C/C++ dependencies
- [ ] README with quick-start example
- [ ] CHANGELOG following Keep a Changelog

---

## Timeline Summary

| Phase | Sessions | Duration (est.) | Status |
|:-----:|:--------:|:--------------:|:------:|
| A | 85–89 | 5 sessions | **Done** |
| B | 90–94 | 5 sessions | **Done** |
| C | 95–105 | 10 sessions | **Next** |
| D | 106–130 | 25 sessions | Planned |
| E | 131–160 | 30 sessions | Planned |
| F | 161+ | 20+ sessions | Vision |

Total estimated: ~95 sessions from current state to open release. Phases A+B took 10 sessions, so the pace is established.

---

*Roadmap: every phase has gates, every gate has criteria, every criterion is measurable.*
