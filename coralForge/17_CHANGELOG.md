# coralForge Changelog

All notable changes to coralForge, tracked per neuralSpring session.

Format follows [Keep a Changelog](https://keepachangelog.com/). Dates are the session dates. Versions are neuralSpring session numbers until Phase F (standalone release), when semantic versioning begins.

---

## [Unreleased] — Phase C: BarraCUDA Integration

### Planned

- Replace hand-written GEMM loops with `barracuda::tensor::matmul`
- Rayon parallelism for batch/head outer loops
- Buffer reuse and allocation pooling
- Benchmark suite with criterion

---

## [Session 94] — 2026-02-28

### Changed

- **coralForge rename**: `sovereign_folding/` + `structure_module/` → unified `coral_forge/` with `structure/` submodule
- Updated 25+ source files, 3 validation binaries, Cargo.toml, control scripts, specs, docs
- RPC capability names (`science.structure_module`) remain stable for protocol compatibility

### Added

- 5 new domain tolerance constants: `FISHER_EPS`, `BURGERS_IC_GUARD`, `DP_EQUALITY_EPS`, `SINGLETON_FREQ_EPS`, `PHENOTYPE_TIE_EPS`
- `safe_idx()` bounds checking in `cpu_fallback.rs` for activator indices
- Documentation for all 34 `BaselineProvenance` constants (Clippy `doc_markdown` warnings resolved)

### Fixed

- 24 `.expect()` calls in GPU validation binaries → graceful `require!(h, ...)` error recording
- Clippy `doc_markdown` warnings for `DeepONet` and `SATé` in doc comments

### Metrics

- 197 binaries | 685 lib tests | 9 integration | 139+ named tolerances
- 0 clippy pedantic warnings | 0 doc warnings
- 154 coralForge checks (62 Python + 55 Rust + 37 GPU)

---

## [Session 93] — 2026-02-28

### Added

- **AlphaFold3 Phase C confidence heads**: `plddt_head`, `pae_head`, `pde_head`, `ranking_score`
- `RankingWeights` struct with `Default` implementation
- Python baseline: `control/coral_forge/alphafold3_confidence.py` (19 checks)
- Validation binary: `validate_coral_forge_confidence`

### Changed

- Deep debt evolution: magic number elimination across production code
- `expect()` → `require!()` migration started in validation binaries

---

## [Session 92] — 2026-02-28

### Added

- **AlphaFold3 Pairformer**: `sinusoidal_embedding`, `condition_pair_with_timestep`, `pairformer_block`
- `PairformerWeights` struct for zero-allocation weight passing
- Python baseline: `control/coral_forge/alphafold3_pairformer.py` (14 checks)
- Pairformer df64 WGSL shader (`pairformer_f64.wgsl`)

### Changed

- Refactored `pair_transition_ffn` from standalone to shared by diffusion and pairformer modules

---

## [Session 91] — 2026-02-27

### Added

- **AlphaFold3 diffusion**: `cosine_beta_schedule`, `linear_beta_schedule`, `forward_diffusion`, `ddpm_reverse_step`, `ddim_reverse_step`, `remove_center_of_mass`, `se3_equivariant_noise`
- `NoiseSchedule` struct
- Python baseline: `control/coral_forge/alphafold3_diffusion.py` (29 checks)
- 5 diffusion df64 WGSL shaders

---

## [Session 90] — 2026-02-27

### Added

- **Evoformer block integration**: Full Evoformer block combining all Phase A primitives
- Python baseline: `control/coral_forge/alphafold2_evoformer_block.py` (19 checks)
- Validation binary: `validate_coral_forge_evoformer_block`
- 5 GPU shaders for combined Evoformer operations

---

## [Session 89] — 2026-02-26

### Added

- **Torsion angle prediction**: `torsion_angles` function (7 angles per residue via 2-layer MLP + atan2)
- **Backbone update**: Frame composition from predicted quaternion/translation updates

---

## [Session 88] — 2026-02-26

### Added

- **Invariant Point Attention**: `ipa_scores`, `ipa_apply` with `IpaConfig`
- **Frame operations**: `quat_to_rotation`, `apply_frame`, `invert_frame`, `compose_frames`
- `structure/` submodule created with `ipa.rs`, `backbone.rs`, `frame.rs`
- IPA df64 WGSL shader (`ipa_scores_f64.wgsl`)

---

## [Session 87] — 2026-02-25

### Added

- **MSA attention**: `msa_row_attention`, `msa_col_attention` (full attention with weighted value summation)
- **MSA attention scores**: `msa_row_attention_scores` (with pair bias), `msa_col_attention_scores`
- MSA row attention df64 WGSL shader

---

## [Session 86] — 2026-02-25

### Added

- **Outer product mean**: `outer_product_mean` (Algorithm 10)
- **Triangle attention**: `triangle_attention_scores` (Algorithms 13-14 with pair bias)
- OPM and triangle attention df64 WGSL shaders

---

## [Session 85] — 2026-02-24

### Added

- **Initial coralForge module**: `src/coral_forge/mod.rs` created (as `sovereign_folding`)
- **Activation primitives**: `gelu`, `gelu_vec`, `layer_norm`, `softmax_rows`
- **Attention primitives**: `sdpa_scores`, `attention_apply`, `sdpa_full`
- **Triangle multiplication**: `triangle_mul_outgoing`, `triangle_mul_incoming` (Algorithms 11-12)
- Python baseline: `control/coral_forge/evoformer_primitives.py` (12 checks)
- First 3 df64 WGSL shaders (GELU, LayerNorm, softmax)

---

## [Pre-Session 85] — Design Phase

### Documented

- AlphaFold2/3 algorithm survey and feasibility assessment
- Isomorphism theorem connection identified (all AF operations decompose into 6 primitives)
- BarraCUDA integration strategy planned
- LTEE structural analysis use case defined
- Module structure designed

---

*Changelog: what changed, when, and why — the fossil record of coralForge's evolution.*
