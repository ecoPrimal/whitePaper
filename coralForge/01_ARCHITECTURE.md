# coralForge Architecture

## The Two Pipelines

coralForge implements primitives for both AlphaFold2 and AlphaFold3. They share the Evoformer core but diverge at the structure prediction stage.

### AlphaFold2 (Jumper et al., 2021)

```
Input Features
    ├── MSA representation [N_seq × N_res × c_m]
    └── Pair representation [N_res × N_res × c_z]
        │
        ▼
┌─────────────────────────────┐
│     Evoformer × 48 blocks    │
│                              │
│  MSA row attention (Alg 7)   │  ← weighted by pair bias
│  MSA column attention (Alg 8)│
│  Outer product mean (Alg 10) │  ← MSA → pair channel
│  Triangle mul outgoing (11)  │  ← pair ⊗ pair → pair
│  Triangle mul incoming (12)  │
│  Triangle attention (13-14)  │  ← attention over triangles
│  Pair transition (FFN)       │
│                              │
└──────────────┬───────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Structure Module × 8 iter  │
│                              │
│  IPA (Algorithm 22)          │  ← attention with 3D geometry
│  Backbone update             │  ← rigid-body frame update
│  Torsion angles              │  ← side-chain prediction
│                              │
└──────────────┬───────────────┘
               │
               ▼
        3D Coordinates + pLDDT confidence
```

### AlphaFold3 (Abramson et al., 2024)

```
Input Features
    ├── MSA representation
    └── Pair representation
        │
        ▼
┌─────────────────────────────┐
│   MSA Module (simplified)    │  ← attention + outer product
└──────────────┬───────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Pairformer × 48 blocks     │
│                              │
│  Sinusoidal timestep embed   │  ← conditioning signal
│  Triangle mul outgoing/in    │
│  Triangle attention          │
│  Pair transition (FFN)       │
│                              │
└──────────────┬───────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Diffusion Module × T steps  │
│                              │
│  Forward: x_t = α_t·x_0 +   │
│           σ_t·ε             │
│  Reverse: DDPM or DDIM      │
│  SE(3) equivariant noise    │
│                              │
└──────────────┬───────────────┘
               │
               ▼
        3D Coordinates
               │
               ▼
┌─────────────────────────────┐
│   Confidence Heads           │
│                              │
│  pLDDT  (per-residue)       │
│  PAE    (pairwise aligned)  │
│  pDE    (pairwise distance) │  ← new in AF3
│  Ranking score (global)     │
│                              │
└──────────────┘
```

---

## Module Map

### `coral_forge/` — Top-Level Modules

| File | Algorithms | What It Computes |
|------|-----------|------------------|
| `activation.rs` | — | GELU, LayerNorm, softmax (row-wise) |
| `attention.rs` | 1, 22 (partial) | Scaled dot-product attention: scores and full SDPA |
| `triangle.rs` | 11, 12, 13, 14 | Triangle multiplication (outgoing/incoming), triangle attention with pair bias |
| `msa.rs` | 7, 8, 10 | MSA row attention, MSA column attention, outer product mean |
| `pairformer.rs` | — (AF3) | Sinusoidal timestep embedding, pairformer block with conditioning |
| `diffusion.rs` | — (AF3) | Cosine/linear noise schedules, forward diffusion, DDPM/DDIM reverse, SE(3)-equivariant rotation noise |
| `confidence.rs` | — (AF3) | pLDDT, PAE, pDE confidence heads, ranking score |

### `coral_forge/structure/` — Structure Prediction

| File | Algorithms | What It Computes |
|------|-----------|------------------|
| `ipa.rs` | 22 | Invariant Point Attention: query/key/value projections + geometric distance terms + pair bias |
| `backbone.rs` | 23 | Rigid-body frame update: translations via attention output |
| `frame.rs` | — | Rotation matrix representation, frame composition |
| `mod.rs` | — | Re-exports: `IpaConfig`, `ipa_scores`, `backbone_update`, `torsion_angles` |

---

## Key Design Decisions

### Pure f64 Throughout

All arithmetic uses `f64`. This is intentional:

1. **Reference correctness**: f64 provides machine-epsilon accuracy for validating against NumPy baselines
2. **Tolerance justification**: When we eventually quantize to f32 or bf16 for GPU inference, we can measure exactly how much precision is lost and whether it matters for each operation
3. **df64 shader bridge**: The 15 WGSL shaders use df64 core streaming (f64 I/O, df64 arithmetic on FP32 cores), achieving ~14-digit precision on consumer GPUs

### Flat Row-Major Arrays

All matrices are `Vec<f64>` with explicit dimensions, not nested `Vec<Vec<f64>>`. This is critical for GPU buffer compatibility — BarraCUDA expects flat buffers, and the flat layout enables zero-copy upload to GPU storage buffers.

### Compositional Primitives

Every operation composes from the 6 universal primitives:

| coralForge Operation | Primitive Decomposition |
|---------------------|------------------------|
| Triangle multiplication | Batched outer product (GEMM) + elementwise sigmoid (Gating) + sum (Reduction) |
| Triangle attention | Attention with pair bias mask (Attention + Normalization) |
| IPA | Standard attention + geometric L2 distance (Attention + Reduction) |
| Diffusion forward | Elementwise scale + add (Nonlinearity) |
| pLDDT | Linear projection (GEMM) + softmax (Normalization) + weighted sum (Reduction) |

This decomposition is the empirical proof that the isomorphism theorem extends to structure prediction.

---

## BarraCUDA Absorption Path

The primitives map directly to existing or planned BarraCUDA operations:

| coralForge Primitive | BarraCUDA Equivalent | Status |
|---------------------|---------------------|--------|
| GELU | `Tensor::gelu()` | Available |
| LayerNorm | `Tensor::layer_norm_wgsl()` | Available |
| Softmax | `Tensor::softmax_dim()` | Available |
| SDPA | `ops::mha::MultiHeadAttention` | Available (S-03b resolved) |
| MatMul | `Tensor::matmul()` | Available |
| Triangle mul | Batched GEMM + elementwise | Compose from existing |
| Triangle attn | MHA with custom mask | Needs mask API |
| IPA | MHA + L2 distance | Compose from PairwiseL2Gpu + MHA |
| Diffusion step | Elementwise + scalar schedule | Compose from existing |
| Confidence | Linear + softmax + reduce | Compose from existing |

**Key insight**: Only 1 new BarraCUDA primitive is needed (attention with custom mask). Everything else composes from existing operations. This validates the claim that the 6-primitive library is sufficient.

---

*Architecture: from algorithms to flat buffers to WGSL shaders.*
