# coralForge Implementation

## Source Structure

All coralForge code lives in `neuralSpring/src/coral_forge/`:

```
coral_forge/
├── mod.rs              # Module root: re-exports, doc comments, evolution path
├── activation.rs       # GELU, LayerNorm, softmax_rows
├── attention.rs        # sdpa_scores, sdpa_full (scaled dot-product attention)
├── triangle.rs         # triangle_mul_outgoing, triangle_mul_incoming, triangle_attention_scores
├── msa.rs              # msa_row_attention, msa_col_attention, outer_product_mean
├── pairformer.rs       # sinusoidal_embedding, pairformer_block (AlphaFold3)
├── diffusion.rs        # cosine/linear schedules, forward/reverse diffusion, SE(3) noise
├── confidence.rs       # pLDDT, PAE, pDE, ranking_score (AlphaFold3)
└── structure/
    ├── mod.rs          # Re-exports: IpaConfig, ipa_scores, backbone_update, torsion_angles
    ├── ipa.rs          # Invariant Point Attention (Algorithm 22)
    ├── backbone.rs     # Rigid-body frame update (Algorithm 23)
    └── frame.rs        # Rotation matrix representation, frame composition
```

**12 files, ~2,500 LOC total.** Every file is under the 1000 LOC limit. No file has more than one responsibility.

## Design Principles

### Pure f64 Arithmetic

Every computation uses `f64`. No `f32` anywhere in the library. Rationale:

- NumPy baselines are f64 — matching types eliminates one source of tolerance
- f64 makes tolerance analysis tractable: any deviation from the baseline is algorithmic, not precision-related
- The df64 WGSL shaders demonstrate that f64 *input/output* with df64 *compute* achieves ~14 digits on FP32 GPU cores

### Flat Row-Major Layout

All matrices are `&[f64]` with explicit `(rows, cols)` dimensions:

```rust
pub fn layer_norm(x: &[f64], rows: usize, cols: usize, eps: f64) -> Vec<f64>
```

Not `Vec<Vec<f64>>`. Not `ndarray::Array2`. Flat slices because:

1. **GPU buffer ready**: BarraCUDA `create_buffer_f64()` takes `&[f64]`
2. **Cache friendly**: row-major layout matches the computation order
3. **Zero allocation**: operations that can work in-place do so

### No Trait Abstractions

coralForge primitives are standalone functions, not methods on a tensor type. This is deliberate:

```rust
// This:
let scores = sdpa_scores(q, k, q_rows, q_cols, k_rows);

// Not this:
let scores = q.attention(k);
```

Why: the functions are validation reference implementations. Adding trait abstractions would create a second thing to validate (the abstraction itself) without adding correctness. When these primitives graduate to BarraCUDA, they will use the `Tensor` API — but the reference implementations stay simple.

### Provenance on Every Baseline

Every Python baseline has a `BaselineProvenance` constant in `src/provenance.rs`:

```rust
pub const CORAL_FORGE_PROVENANCE: BaselineProvenance = BaselineProvenance {
    label: "nF-01 Phase B: Evoformer primitive baselines",
    script: "control/coral_forge/evoformer_primitives.py",
    commit: BASELINE_COMMIT,
    date: "2026-02-16",
    command: "python3 control/coral_forge/evoformer_primitives.py",
    environment: "Python 3.10.12, NumPy 2.2.6, seed=42",
    value: 1.0,
    unit: "baselines generated → evoformer_baselines.json",
};
```

This means anyone can reproduce every baseline by running the exact command with the exact environment.

## Testing Strategy

### Three Tiers

1. **Unit tests** (`#[cfg(test)]` in each module): Analytical known-values. "LayerNorm of a constant vector is zero." "Softmax rows sum to 1.0." "GELU(0) = 0."

2. **Validation binaries** (`src/bin/validate_coral_forge*.rs`): Compare Rust output against NumPy baselines loaded from JSON. Tolerances are named constants from `tolerances/mod.rs`.

3. **GPU validation** (`validate_coral_forge_gpu*.rs`): Same math on df64 WGSL shaders. Proves GPU produces identical results to CPU f64.

### Error Handling

Validation binaries use the `require!` macro instead of `.expect()`:

```rust
let buf = require!(h, gpu.create_buffer_f64(&data), "create input buffer");
```

If the GPU allocation fails, the harness records the failure and continues — no panic, no abort. The exit code reflects the overall pass/fail.

## Key Algorithms

### Triangle Multiplication (Algorithms 11-12)

The signature operation of the Evoformer. Given a pair representation `z[i,j]`, compute interactions via a third index `k`:

```
z_out[i,j] = Σ_k gate(z[i,k]) · proj(z[k,j])    (outgoing)
z_out[i,j] = Σ_k gate(z[k,j]) · proj(z[i,k])    (incoming)
```

This is a batched outer product with sigmoid gating — pure GEMM + Gating + Reduction.

### Invariant Point Attention (Algorithm 22)

Standard attention augmented with 3D geometric information:

1. Project pair representation into Q, K, V
2. Compute standard attention logits: Q·K^T/√d
3. Add pair bias from the pair representation
4. Add geometric distance term: -γ/2 · Σ_p ||T_i(q_p) - T_j(k_p)||²
5. Softmax → weighted sum of values

The geometric term makes IPA equivariant to rigid-body transformations — rotating the entire protein doesn't change the attention weights. This decomposes into Attention + L2 distance (Reduction) + frame application (GEMM).

### Diffusion (AlphaFold3)

DDPM forward process:
```
x_t = √(ᾱ_t) · x_0 + √(1 - ᾱ_t) · ε,    ε ~ N(0, I)
```

DDIM reverse (deterministic):
```
x_{t-1} = √(ᾱ_{t-1}) · x̂_0 + √(1 - ᾱ_{t-1}) · ε_θ(x_t, t)
```

SE(3) equivariant noise: rotation matrices sampled from SO(3) via Rodrigues' formula, applied to coordinate frames. The noise respects the protein's rigid-body symmetry.

---

*Implementation: simple functions, flat arrays, full provenance.*
