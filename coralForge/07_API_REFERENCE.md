# coralForge API Reference

**Source**: `neuralSpring/src/coral_forge/` (2,684 LOC, 12 files, 8 modules)
**Convention**: All arrays are flat `&[f64]` in row-major order with explicit dimension parameters.

---

## `coral_forge::activation`

Fundamental nonlinear transforms used throughout the Evoformer and Structure Module.

### `gelu(x: f64) -> f64`

Gaussian Error Linear Unit activation. Approximation per Hendrycks & Gimpel (2016):

```
gelu(x) = 0.5 · x · (1 + tanh(√(2/π) · (x + 0.044715 · x³)))
```

Used in: Evoformer transition blocks, pairformer FFN, confidence heads.

### `gelu_vec(xs: &[f64]) -> Vec<f64>`

Elementwise GELU over a slice. Returns a new `Vec<f64>` of the same length.

### `layer_norm(x, rows, dim, gamma, beta, eps) -> Vec<f64>`

Layer normalization (Ba et al., 2016) along the last axis.

| Parameter | Type | Shape | Description |
|-----------|------|-------|-------------|
| `x` | `&[f64]` | `[rows × dim]` | Input activations |
| `rows` | `usize` | — | Number of independent normalization groups |
| `dim` | `usize` | — | Feature dimension (normalized axis) |
| `gamma` | `&[f64]` | `[dim]` | Learned scale |
| `beta` | `&[f64]` | `[dim]` | Learned bias |
| `eps` | `f64` | — | Numerical stability floor (typically 1e-5) |

Returns `[rows × dim]` normalized output.

### `softmax_rows(x, rows, cols) -> Vec<f64>`

Numerically stable row-wise softmax. For each row, subtracts the max before exponentiating.

| Parameter | Type | Shape |
|-----------|------|-------|
| `x` | `&[f64]` | `[rows × cols]` |
| `rows` | `usize` | — |
| `cols` | `usize` | — |

Returns `[rows × cols]` where each row sums to 1.0.

---

## `coral_forge::attention`

Scaled dot-product attention (Vaswani et al., 2017) with batched multi-head support.

### `sdpa_scores(query, key, batch, heads, q_len, kv_len, head_dim) -> Vec<f64>`

Computes raw attention logits: `Q @ K^T / √d_k`.

| Parameter | Type | Shape | Description |
|-----------|------|-------|-------------|
| `query` | `&[f64]` | `[B × H × Sq × D]` | Query tensor |
| `key` | `&[f64]` | `[B × H × Skv × D]` | Key tensor |
| `batch` | `usize` | — | Batch size (B) |
| `heads` | `usize` | — | Number of attention heads (H) |
| `q_len` | `usize` | — | Query sequence length (Sq) |
| `kv_len` | `usize` | — | Key/value sequence length (Skv) |
| `head_dim` | `usize` | — | Head dimension (D) |

Returns `[B × H × Sq × Skv]` unnormalized logits.

### `attention_apply(weights, value, batch, heads, q_len, kv_len, head_dim) -> Vec<f64>`

Weighted value summation: `output[b,h,q,d] = Σ_k weights[b,h,q,k] · V[b,h,k,d]`.

Returns `[B × H × Sq × D]` attended output.

### `sdpa_full(query, key, value, batch, heads, q_len, kv_len, head_dim) -> Vec<f64>`

Complete scaled dot-product attention: `softmax(QK^T / √d) @ V`.

Equivalent to `attention_apply(softmax_rows(sdpa_scores(...)), value, ...)`.

Returns `[B × H × Sq × D]`.

---

## `coral_forge::triangle`

Triangle operations unique to AlphaFold's Evoformer — the pair representation self-interaction.

### `triangle_mul_outgoing(proj_a, proj_b, n, channels) -> Vec<f64>`

Algorithm 11 (Jumper et al., 2021). Triangle multiplicative update on outgoing edges.

```
output[i,j,c] = Σ_k proj_a[i,k,c] · proj_b[j,k,c]
```

| Parameter | Type | Shape |
|-----------|------|-------|
| `proj_a` | `&[f64]` | `[N × N × C]` |
| `proj_b` | `&[f64]` | `[N × N × C]` |
| `n` | `usize` | Residue count (N) |
| `channels` | `usize` | Channel dimension (C) |

Returns `[N × N × C]`.

### `triangle_mul_incoming(proj_a, proj_b, n, channels) -> Vec<f64>`

Algorithm 12. Triangle multiplicative update on incoming edges. Transposes the summation axis relative to outgoing.

```
output[i,j,c] = Σ_k proj_a[k,i,c] · proj_b[k,j,c]
```

### `triangle_attention_scores(query, key, bias, n_rows, n_res, n_heads, head_dim) -> Vec<f64>`

Algorithms 13-14. Multi-head attention over residue pairs with pair bias.

```
scores[r,h,i,j] = Σ_d query[r,i,h,d] · key[r,j,h,d] / √d + bias[h,i,j]
```

| Parameter | Type | Shape |
|-----------|------|-------|
| `query` | `&[f64]` | `[R × N × H × D]` |
| `key` | `&[f64]` | `[R × N × H × D]` |
| `bias` | `&[f64]` | `[H × N × N]` |

Returns `[R × H × N × N]` unnormalized attention logits.

---

## `coral_forge::msa`

Multiple Sequence Alignment attention operations from the Evoformer.

### `outer_product_mean(a, b, n_seq, n_res, c_a, c_b) -> Vec<f64>`

Algorithm 10. Projects MSA information into the pair representation via outer product and mean over sequences.

```
output[i,j,ca,cb] = (1/N_seq) · Σ_s a[s,i,ca] · b[s,j,cb]
```

Returns `[N_res × N_res × c_a × c_b]`.

### `msa_row_attention_scores(query, key, pair_bias, n_seq, n_res, n_heads, head_dim) -> Vec<f64>`

Algorithm 7. MSA row-wise attention logits with pair bias from the pair representation.

Returns `[N_seq × H × N_res × N_res]`.

### `msa_row_attention(query, key, value, pair_bias, n_seq, n_res, n_heads, head_dim) -> Vec<f64>`

Full MSA row attention: scores → softmax → weighted values.

Returns `[N_seq × N_res × (H·D)]`.

### `msa_col_attention_scores(query, key, n_seq, n_res, n_heads, head_dim) -> Vec<f64>`

Algorithm 8. MSA column-wise attention logits (across sequences for each residue position). No pair bias.

Returns `[N_res × H × N_seq × N_seq]`.

### `msa_col_attention(query, key, value, n_seq, n_res, n_heads, head_dim) -> Vec<f64>`

Full MSA column attention.

Returns `[N_seq × N_res × (H·D)]`.

---

## `coral_forge::structure`

Structure Module: rigid-body frame operations and Invariant Point Attention.

### `IpaConfig`

```rust
pub struct IpaConfig {
    pub n_res: usize,      // Number of residues
    pub n_heads: usize,    // Number of attention heads
    pub head_dim: usize,   // Dimension per head (scalar)
    pub n_points: usize,   // Number of 3D query/key points per head
    pub w_l: f64,          // Weight for scalar logit term
    pub w_c: f64,          // Weight for pair bias term
    pub w_p: f64,          // Weight for point distance term
    pub gamma: f64,        // Point distance softness parameter
}
```

### `ipa_scores(q_scalar, k_scalar, pair_bias, q_points, k_points, frames, cfg) -> Vec<f64>`

Algorithm 22 attention scores. Three terms:

```
a[h,i,j] = w_L · (Q_s · K_s / √c)          — scalar logit
          + w_C · pair_bias[h,i,j]           — pair representation bias
          + w_P · (-γ/2) · Σ_p ||T_i(q_p) - T_j(k_p)||²  — 3D point distance
```

| Parameter | Type | Shape |
|-----------|------|-------|
| `q_scalar` | `&[f64]` | `[N × H × D]` |
| `k_scalar` | `&[f64]` | `[N × H × D]` |
| `pair_bias` | `&[f64]` | `[H × N × N]` |
| `q_points` | `&[f64]` | `[N × H × P × 3]` |
| `k_points` | `&[f64]` | `[N × H × P × 3]` |
| `frames` | `&[f64]` | `[N × 12]` (rotation 9 + translation 3) |
| `cfg` | `&IpaConfig` | — |

Returns `[H × N × N]` unnormalized attention logits.

### `ipa_apply(q_scalar, k_scalar, v_scalar, pair_bias, q_points, k_points, frames, cfg) -> Vec<f64>`

Full IPA: scores → softmax → weighted sum of scalar and point values.

Returns `[N × (H·D + H·P·3)]` — concatenation of scalar outputs and point outputs per residue.

### `backbone_update(delta_quats, delta_trans, current_frames, n_res) -> Vec<f64>`

Algorithm 23. Composes predicted frame updates with current frames. Each frame is `[12]` (rotation 9 + translation 3). Delta quaternions are converted to rotation matrices via `quat_to_rotation`.

Returns `[N × 12]` updated frames.

### `torsion_angles(single, weights, n_res, c_single, c_hidden) -> Vec<f64>`

Predicts 7 torsion angles (φ, ψ, ω, χ1–χ4) from the single representation via a two-layer MLP with `atan2` output.

Returns `[N × 7]` in radians.

### `quat_to_rotation(q: &[f64; 4]) -> [f64; 9]`

Unit quaternion `[w, x, y, z]` → 3×3 rotation matrix (row-major).

### `apply_frame(rot, trans, point) -> [f64; 3]`

Apply rigid-body transform: `R · p + t`.

### `invert_frame(rot, trans) -> ([f64; 9], [f64; 3])`

Invert: `R^T` and `-R^T · t`.

### `compose_frames(r1, t1, r2, t2) -> ([f64; 9], [f64; 3])`

Compose two frames: `R = R1 · R2`, `t = R1 · t2 + t1`.

---

## `coral_forge::diffusion`

AlphaFold3 diffusion process: noise schedules, forward/reverse steps, SE(3) equivariance.

### `NoiseSchedule`

```rust
pub struct NoiseSchedule {
    pub betas: Vec<f64>,     // Per-step noise (β_t)
    pub alpha_bar: Vec<f64>, // Cumulative signal retention (ᾱ_t = Π(1-β_s))
}
```

### `cosine_beta_schedule(t_steps, s) -> NoiseSchedule`

Nichol & Dhariwal (2021) cosine schedule. `s` is the offset (typically 0.008).

### `linear_beta_schedule(t_steps, beta_start, beta_end) -> NoiseSchedule`

Ho et al. (2020) linear schedule from `beta_start` to `beta_end`.

### `forward_diffusion(coords, noise, t, schedule) -> Vec<f64>`

Add noise at timestep `t`:
```
x_t = √(ᾱ_t) · x_0 + √(1 - ᾱ_t) · ε
```

### `ddpm_reverse_step(x_t, predicted_noise, z, t, schedule) -> Vec<f64>`

DDPM reverse (Ho et al., 2020):
```
x_{t-1} = (1/√α_t) · (x_t - (β_t/√(1-ᾱ_t)) · ε_θ) + σ_t · z
```
`z` is fresh Gaussian noise.

### `ddim_reverse_step(x_t, predicted_noise, t, schedule) -> (Vec<f64>, Vec<f64>)`

DDIM reverse (Song et al., 2020). Deterministic — no added noise. Returns `(x_{t-1}, predicted_x_0)`.

### `remove_center_of_mass(coords) -> (Vec<f64>, [f64; 3])`

Subtracts center of mass. Returns `(centered_coords, center)`. `coords` is `[N × 3]`.

### `se3_equivariant_noise(coords, noise, t, schedule) -> (Vec<f64>, [f64; 3])`

Applies forward diffusion then re-centers. Returns `(noisy_centered, center)`. The centering ensures SE(3) equivariance: the noise process is invariant to global translation.

### `pair_transition_ffn(pair_repr, n, d_pair, w1, b1, d_hidden, w2, b2) -> Vec<f64>`

Two-layer FFN with GELU: `GELU(x @ W1 + b1) @ W2 + b2`. Used in pairformer transition blocks.

---

## `coral_forge::pairformer`

AlphaFold3's Pairformer block with timestep conditioning.

### `sinusoidal_embedding(t: f64, d_model: usize) -> Vec<f64>`

Sinusoidal positional encoding for diffusion timestep `t`. Returns `[d_model]`.

```
emb[2i]   = sin(t / 10000^(2i/d))
emb[2i+1] = cos(t / 10000^(2i/d))
```

### `condition_pair_with_timestep(pair_repr, n, d, t_emb, w_cond, b_cond) -> Vec<f64>`

Adds timestep conditioning to the pair representation:
```
pair[i,j,:] += W_cond @ t_emb + b_cond
```

### `PairformerWeights<'a>`

All weight tensors for a single pairformer block. Borrowed references — no allocation.

| Field | Shape | Purpose |
|-------|-------|---------|
| `ln_gamma`, `ln_beta` | `[d]` | LayerNorm parameters |
| `tri_out_wa`, `tri_out_wb` | `[N×N×C]` | Triangle mul outgoing projections |
| `tri_out_wg` | `[N×N×C]` | Outgoing gate |
| `tri_in_wa`, `tri_in_wb`, `tri_in_wg` | `[N×N×C]` | Triangle mul incoming |
| `tri_attn_wq`, `tri_attn_wk`, `tri_attn_wv` | `[R×N×H×D]` | Triangle attention QKV |
| `ffn_w1`, `ffn_b1` | `[d×h]`, `[h]` | FFN layer 1 |
| `ffn_w2`, `ffn_b2` | `[h×d]`, `[d]` | FFN layer 2 |
| `cond_w`, `cond_b` | `[d_emb×d]`, `[d]` | Timestep conditioning |
| `n_heads`, `head_dim`, `d_hidden` | `usize` | Dimensions |

### `pairformer_block(pair, n, d, w, t_emb) -> Vec<f64>`

One pairformer iteration:

1. LayerNorm
2. Timestep conditioning (if `t_emb` is `Some`)
3. Triangle multiplication outgoing (Alg 11)
4. Triangle multiplication incoming (Alg 12)
5. Triangle attention (Alg 13)
6. Pair transition FFN (GELU)
7. Residual connection

Returns `[N × N × d]` updated pair representation.

---

## `coral_forge::confidence`

AlphaFold3 model confidence estimation heads.

### `plddt_head(single_repr, n_res, d, w, b) -> Vec<f64>`

Per-residue confidence (predicted LDDT). Linear projection → softmax over 50 bins → weighted sum.

Returns `[N_res]` values in [0, 1]. Higher = more confident.

### `pae_head(pair_repr, n, d, w, b, n_bins) -> (Vec<f64>, Vec<f64>)`

Predicted Aligned Error. Linear projection → softmax over `n_bins`.

Returns `(expected_pae[N×N], bin_probs[N×N×n_bins])`. Expected PAE in Angstroms.

### `pde_head(pair_repr, n, d, w, b, n_bins, max_dist) -> (Vec<f64>, Vec<f64>)`

Predicted Distance Error (new in AlphaFold3). Linear projection → softmax over distance bins.

Returns `(expected_pde[N×N], bin_probs[N×N×n_bins])`. Expected PDE in Angstroms.

### `RankingWeights`

```rust
pub struct RankingWeights {
    pub w_plddt: f64,   // pLDDT weight (default 1.0)
    pub w_pae: f64,     // PAE penalty weight (default 0.5)
    pub w_pde: f64,     // PDE penalty weight (default 0.3)
    pub max_pae: f64,   // PAE normalization ceiling (default 30.0)
    pub max_pde: f64,   // PDE normalization ceiling (default 30.0)
}
impl Default for RankingWeights  // {1.0, 0.5, 0.3, 30.0, 30.0}
```

### `ranking_score(plddt, pae_expected, pde_expected, weights) -> f64`

Global model ranking score combining all confidence metrics:

```
score = w_plddt · mean(plddt)
      - w_pae · mean(pae) / max_pae
      - w_pde · mean(pde) / max_pde
```

Returns a single f64. Higher = better model.

---

*API Reference — every function, every parameter, every shape.*
