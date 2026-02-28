# coralForge Testing Strategy

## Three-Tier Validation

coralForge uses a three-tier testing strategy. Each tier catches different classes of bugs, and all three must pass before any change is accepted.

```
                  ┌─────────────────────────┐
     Tier 3       │  GPU Validation (df64)   │  37 checks
                  │  Max diff < 1e-6 vs CPU  │
                  └───────────┬───────────────┘
                              │
                  ┌───────────▼───────────────┐
     Tier 2       │  Rust Validation Binaries  │  55 checks
                  │  f64 vs Python baselines   │
                  └───────────┬───────────────┘
                              │
                  ┌───────────▼───────────────┐
     Tier 1       │  Rust Unit Tests (#[test]) │  62 checks
                  │  Small cases, edge cases   │
                  └───────────────────────────┘
```

---

## Tier 1: Unit Tests

Each module contains `#[cfg(test)] mod tests` with small, hand-verifiable cases.

### Purpose

- Catch implementation bugs immediately during development
- Test edge cases (empty inputs, single-element, zero weights)
- Verify mathematical properties (softmax sums to 1, rotation matrices are orthogonal)

### Running

```bash
cargo test -p neuralspring -- coral_forge
```

### What unit tests cover

| Module | Tests | Focus |
|--------|:-----:|-------|
| `activation` | 8 | GELU symmetry, LayerNorm invariance, softmax normalization |
| `attention` | 6 | Score scaling, causal masking, identity attention |
| `triangle` | 5 | Outgoing/incoming symmetry, pair bias additivity |
| `msa` | 6 | Row/column attention shapes, OPM symmetry |
| `diffusion` | 8 | Schedule monotonicity, forward/reverse roundtrip, COM removal |
| `pairformer` | 5 | Embedding orthogonality, conditioning linearity, residual |
| `confidence` | 6 | pLDDT range [0,1], PAE non-negative, ranking monotonicity |
| `structure/ipa` | 6 | SE(3) equivariance, score symmetry, point distance |
| `structure/backbone` | 4 | Frame composition associativity, quaternion normalization |
| `structure/frame` | 8 | Rotation orthogonality, inversion roundtrip, compose associativity |

### Writing unit tests

```rust
#[test]
fn test_softmax_rows_sum_to_one() {
    let x = vec![1.0, 2.0, 3.0, 4.0, 5.0, 6.0];
    let result = softmax_rows(&x, 2, 3);
    let row1_sum: f64 = result[0..3].iter().sum();
    let row2_sum: f64 = result[3..6].iter().sum();
    assert!((row1_sum - 1.0).abs() < 1e-14);
    assert!((row2_sum - 1.0).abs() < 1e-14);
}
```

---

## Tier 2: Validation Binaries

Standalone binaries that compare Rust f64 output against committed Python NumPy baselines.

### Purpose

- Cross-language validation: if Rust and Python agree, the algorithm is likely correct
- Regression detection: any code change that alters output is caught
- Tolerance documentation: explicit named constants for every comparison

### Binaries

| Binary | Baselines | Checks | Tests |
|--------|-----------|:------:|-------|
| `validate_coral_forge` | `evoformer_baselines.json` | 12 | Evoformer primitives |
| `validate_coral_forge_evoformer_block` | `evoformer_block_baselines.json` | 19 | Full Evoformer block |
| `validate_coral_forge_diffusion` | `diffusion_baselines.json` | 12 | Diffusion pipeline |
| `validate_coral_forge_pairformer` | `pairformer_baselines.json` | 6 | Pairformer block |
| `validate_coral_forge_confidence` | `confidence_baselines.json` | 6 | Confidence heads |
| **Total** | **5 baseline files** | **55** | |

### Running

```bash
# Individual binary:
cargo run --bin validate_coral_forge

# All coralForge binaries:
cargo run --bin validate_coral_forge
cargo run --bin validate_coral_forge_evoformer_block
cargo run --bin validate_coral_forge_diffusion
cargo run --bin validate_coral_forge_pairformer
cargo run --bin validate_coral_forge_confidence

# Or via the validate_all script:
bash control/validate_all.sh
```

### The `require!` macro

Validation binaries use `require!` instead of `assert!` or `.expect()`:

```rust
require!(h, (got - expected).abs() < FOLDING_EPS,
    "triangle_mul_outgoing[{i}]: got {got:.15e}, expected {expected:.15e}, \
     diff {:.2e}", (got - expected).abs());
```

`require!` records the failure in the `ValidationHarness` and continues. This means a single validation run reports *all* failures, not just the first. The harness prints a summary at the end with pass/fail counts.

### Tolerance constants

Every comparison uses a named tolerance from `src/tolerances/mod.rs`:

| Constant | Value | Domain |
|----------|:-----:|--------|
| `FOLDING_EPS` | 1e-10 | General f64 folding comparisons |
| `DIFFUSION_NOISE_FLOOR` | 1e-12 | Noise schedule numerical floor |
| `FISHER_EPS` | 1e-12 | Fisher information comparisons |
| `BURGERS_IC_GUARD` | 1e-14 | Initial condition precision |
| `DP_EQUALITY_EPS` | 1e-14 | Dynamic programming equality |
| `SINGLETON_FREQ_EPS` | 1e-15 | Frequency comparison near zero |
| `PHENOTYPE_TIE_EPS` | 1e-12 | Fitness tie-breaking |

---

## Tier 3: GPU Validation

df64 WGSL shaders running on the GPU, compared against Rust CPU f64 output.

### Purpose

- Verify that the df64 emulation on f32 cores produces results within tolerance
- Catch GPU-specific bugs (thread divergence, atomic contention, precision loss)
- Establish the precision boundary between CPU and GPU paths

### Binaries

| Binary | Shaders | Checks | Max Diff |
|--------|:-------:|:------:|:--------:|
| `validate_coral_forge_gpu` | 10 | 22 | < 1e-6 |
| `validate_coral_forge_gpu_pipeline` | 5 | 15 | < 1e-6 |
| **Total** | **15** | **37** | |

### Running

```bash
# Requires GPU (will skip gracefully if no GPU detected):
cargo run --bin validate_coral_forge_gpu
cargo run --bin validate_coral_forge_gpu_pipeline
```

### df64 Tolerance

GPU checks use a wider tolerance than CPU checks because df64 emulates f64 using pairs of f32:

```
CPU vs Python:  ≤ 1e-10 (FOLDING_EPS)
GPU vs CPU:     ≤ 1e-6  (df64 precision ceiling)
GPU vs Python:  ≤ 1e-6  (transitive)
```

The 1e-6 ceiling comes from df64 providing ~50 bits of mantissa vs f64's 52 bits. In practice, most shaders achieve max diff < 1e-7.

### Shader Inventory

| # | Shader | Operation |
|:-:|--------|-----------|
| 1 | `gelu_f64.wgsl` | GELU activation |
| 2 | `layer_norm_f64.wgsl` | Layer normalization |
| 3 | `softmax_f64.wgsl` | Row-wise softmax |
| 4 | `sdpa_f64.wgsl` | Scaled dot-product attention |
| 5 | `triangle_mul_out_f64.wgsl` | Triangle mul outgoing |
| 6 | `triangle_mul_in_f64.wgsl` | Triangle mul incoming |
| 7 | `triangle_attn_f64.wgsl` | Triangle attention |
| 8 | `msa_row_attn_f64.wgsl` | MSA row attention |
| 9 | `opm_f64.wgsl` | Outer product mean |
| 10 | `ipa_scores_f64.wgsl` | IPA score computation |
| 11 | `forward_diff_f64.wgsl` | Forward diffusion |
| 12 | `ddpm_rev_f64.wgsl` | DDPM reverse step |
| 13 | `se3_noise_f64.wgsl` | SE(3) equivariant noise |
| 14 | `pairformer_f64.wgsl` | Pairformer block |
| 15 | `pair_ffn_f64.wgsl` | Pair transition FFN |

---

## Validation Matrix

Summary of all checks across all three tiers:

```
                      Python   Rust    GPU     Total
                      (Tier 1) (Tier 2) (Tier 3)
Evoformer primitives    12      12       10       34
Evoformer block         19      19        5       43
Diffusion               12      12       10       34
Pairformer               6       6        7       19
Confidence              13       6        5       24
                       ───     ───      ───     ───
Total                   62      55       37      154
```

---

## Continuous Integration

The full validation suite runs as part of neuralSpring's quality gates:

```bash
# The complete gate sequence:
cargo fmt --check
cargo clippy --all-targets -- -D warnings -W clippy::pedantic
cargo test
cargo doc --no-deps 2>&1 | grep warning  # must be empty
bash control/validate_all.sh              # 185/185 binaries pass
```

`validate_all.sh` runs all 185 validation binaries (not just coralForge), ensuring that coralForge changes don't break other modules.

---

## Adding New Tests

### Tier 1 (unit test)

Add to the module's `#[cfg(test)]` block. Use small inputs you can verify by hand.

### Tier 2 (validation binary)

1. Write the Python baseline script → JSON
2. Create `src/bin/validate_coral_forge_[name].rs`
3. Use `require!` macro for all checks
4. Add `BaselineProvenance` constant
5. Add to `validate_all.sh`

### Tier 3 (GPU shader)

1. Write/evolve the WGSL shader in `metalForge/shaders/`
2. Add GPU checks to `validate_coral_forge_gpu` or create a new GPU binary
3. Compare against the Tier 2 Rust output (not Python directly)
4. Document max diff in the shader header

---

*Testing: three tiers, three languages, one truth.*
