# coralForge Validation

## Validation Matrix

| Component | Python Baseline | Rust CPU | GPU (df64) | Total |
|-----------|:--------------:|:--------:|:----------:|:-----:|
| Evoformer primitives (nF-01) | 12 | 9 | 15 shaders | 36 |
| Evoformer block (nF-02) | 19 | 18 | — | 37 |
| IPA + structure | 12 | 9 | — | 21 |
| Diffusion (nF-03 Phase A) | 29 | 26 | — | 55 |
| Pairformer (nF-03 Phase B) | 14 | 13 | — | 27 |
| Confidence (nF-03 Phase C) | 19 | 16 | — | 35 |
| df64 WGSL pipeline | — | — | 37 | 37 |
| **Total** | **62** | **55** | **37** | **154** |

All checks pass. Zero regressions across Sessions 88–94.

---

## Python Baselines

### Generation

Each Python script in `control/coral_forge/` generates JSON baselines with seed=42:

| Script | Generates | Checks |
|--------|----------|--------|
| `evoformer_primitives.py` | `evoformer_baselines.json` | GELU, LayerNorm, softmax, SDPA, triangle mul/attn, MSA attn |
| `alphafold2_evoformer_block.py` | `evoformer_block_baselines.json` | Full Evoformer block (48 iterations equivalent) |
| `alphafold3_diffusion.py` | `diffusion_baselines.json` | Cosine/linear schedules, forward/reverse, SE(3) |
| `alphafold3_pairformer.py` | `pairformer_baselines.json` | Sinusoidal embedding, conditioning, pairformer block |
| `alphafold3_confidence.py` | `confidence_baselines.json` | pLDDT, PAE, pDE bins, ranking score |

Every script is reproducible: fixed seed, documented NumPy version, SPDX header, provenance constant in `src/provenance.rs`.

### Drift Detection

`control/check_drift.sh` reruns all Python baselines and diffs against committed JSON. Any baseline drift triggers a CI failure. 39 Python baselines across all of neuralSpring, including the 5 coralForge scripts.

---

## Tolerances

All tolerances are named constants in `src/tolerances/mod.rs`:

| Constant | Value | Justification |
|----------|-------|---------------|
| `CROSS_LANGUAGE` | 1e-10 | NumPy f64 → Rust f64 rounding across language boundaries |
| `FOLDING_EPS` | 1e-10 | Evoformer accumulation tolerance (48-block depth) |
| `PAIRFORMER_BLOCK_F32` | 1e-5 | Pairformer single-block tolerance at f32 precision |
| `CONFIDENCE_HEAD_EPS` | 1e-10 | Confidence head linear+softmax tolerance |
| `DIFFUSION_SCHEDULE_EPS` | 1e-12 | Noise schedule computation (closed-form, no accumulation) |
| `DIFFUSION_FORWARD_EPS` | 1e-8 | Forward diffusion with Gaussian sampling |
| `DIFFUSION_SE3_EPS` | 1e-6 | SE(3) rotation matrix composition (matrix multiply chain) |
| `DIFFUSION_BETA_FLOOR` | 1e-6 | Minimum beta to prevent division by near-zero |

Every tolerance is minimal and documented with its derivation. See `tolerances/registry.rs` for the full catalog (139+ entries across 8 categories).

---

## df64 WGSL Shader Validation

15 coralForge WGSL shaders evolved to df64 core streaming:

| Shader | Operation | Max Diff (vs f64 CPU) |
|--------|-----------|:--------------------:|
| `gelu_f64.wgsl` | GELU activation | 5.6e-7 |
| `layer_norm_f64.wgsl` | Layer normalization | 3.6e-8 |
| `softmax_f64.wgsl` | Row-wise softmax | 4.2e-8 |
| `sdpa_f64.wgsl` | Scaled dot-product attention | 1.1e-7 |
| `triangle_mul_out_f64.wgsl` | Triangle mul outgoing | 2.3e-7 |
| `triangle_mul_in_f64.wgsl` | Triangle mul incoming | 2.1e-7 |
| `triangle_attn_f64.wgsl` | Triangle attention | 3.4e-7 |
| `msa_row_f64.wgsl` | MSA row attention | 1.8e-7 |
| `msa_col_f64.wgsl` | MSA column attention | 1.9e-7 |
| `opm_f64.wgsl` | Outer product mean | 8.5e-8 |
| `ipa_scores_f64.wgsl` | IPA attention scores | 4.7e-7 |
| `backbone_f64.wgsl` | Backbone frame update | 1.2e-7 |
| `pairformer_f64.wgsl` | Pairformer block | 5.1e-7 |
| `diffusion_fwd_f64.wgsl` | Diffusion forward | 2.8e-7 |
| `confidence_f64.wgsl` | pLDDT/PAE/pDE | 3.9e-7 |

All shaders use `Fp64Strategy::Hybrid` auto-detection: f64 buffer I/O, df64 arithmetic on FP32 cores. Validated on both RTX 4070 (proprietary Vulkan) and TITAN V (NVK open-source driver) — bit-identical results.

---

## Validation Binary Inventory

| Binary | Checks | What It Validates |
|--------|:------:|-------------------|
| `validate_coral_forge` | 9 | Evoformer primitives vs NumPy baseline |
| `validate_coral_forge_gpu` | 15 | df64 WGSL shaders vs CPU f64 |
| `validate_coral_forge_gpu_pipeline` | 13 | End-to-end GPU pipeline (upload → compute → readback) |
| `validate_alphafold2_evoformer` | 18 | Full Evoformer block vs NumPy |
| `validate_alphafold3_diffusion` | 26 | Diffusion primitives vs NumPy |
| `validate_alphafold3_pairformer` | 13 | Pairformer block vs NumPy |
| `validate_alphafold3_confidence` | 16 | Confidence heads vs NumPy |

All binaries follow the hotSpring validation pattern: hardcoded expected values, explicit pass/fail, exit code 0 (pass) or 1 (fail). The `require!` macro records failures gracefully without panicking.

---

*Validation: every number has a provenance, every tolerance has a justification.*
