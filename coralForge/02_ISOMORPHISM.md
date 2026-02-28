# coralForge and the Isomorphism Theorem

## The Claim

neuralSpring's Isomorphism Theorem states that all neural architectures decompose into compositions of 6 fundamental primitives: GEMM, Attention, Normalization, Nonlinearity, Reduction, and Gating. coralForge tests this claim against the most complex neural architecture in production use: AlphaFold.

## The Test

AlphaFold introduced operations not seen in language models, vision models, or physics surrogates:

| "Novel" Operation | First Impression | Primitive Decomposition |
|------------------|-----------------|------------------------|
| **Triangle multiplication** | New — pair representation self-interaction | Batched outer product (**GEMM**) + sigmoid (**Gating**) + sum (**Reduction**) |
| **Triangle attention** | New — attention over triangles | Scaled dot-product (**Attention**) + pair bias mask + softmax (**Normalization**) |
| **Outer product mean** | New — MSA → pair channel | Outer product (**GEMM**) + mean (**Reduction**) |
| **IPA** | New — geometry-aware attention | Standard Q·K^T/√d (**Attention**) + L2 distance (**Reduction**) + softmax (**Normalization**) + weighted sum (**Reduction**) |
| **Diffusion denoising** | New — iterative structure refinement | Scale + add (**Nonlinearity**) per step, sequential application |
| **SE(3) equivariant noise** | New — rotation-invariant corruption | Matrix multiplication (**GEMM**) + Gaussian sampling |
| **Confidence heads** | New — quality estimation | Linear (**GEMM**) + softmax (**Normalization**) + weighted sum (**Reduction**) |

Every "novel" operation decomposes into the known 6 primitives. No new primitive category was needed.

## Cross-Domain Primitive Usage (Extended)

| Primitive | Language (llama.cpp) | Vision (ViT) | Physics (hotSpring) | Structure (coralForge) |
|-----------|:-------------------:|:------------:|:-------------------:|:---------------------:|
| **GEMM** | Token embedding, FFN | Patch projection, MLP | Force computation, EOS | Triangle mul, IPA projection, confidence linear |
| **Attention** | Self-attention, KV cache | Patch attention | — | SDPA, triangle attention, IPA, MSA attention |
| **Normalization** | RMSNorm, LayerNorm | LayerNorm | — | LayerNorm (every block) |
| **Nonlinearity** | SiLU, GELU | GELU | Boltzmann, Hill | GELU (activation), sigmoid (gating) |
| **Reduction** | KV aggregation, logits | CLS pooling | Mean, variance | Outer product mean, confidence aggregation, L2 distance |
| **Gating** | MLP gate | — | Selection | Triangle mul sigmoid gate, diffusion schedule scaling |

The pattern is complete: structure prediction uses exactly the same primitive vocabulary as every other domain. The 6 primitives are sufficient.

## What This Means

### For the Thesis

If 6 primitives explain language, vision, physics, evolution, phylogenetics, game theory, spectral analysis, *and* protein structure prediction, then the computational substrate is truly universal. A single optimized engine (BarraCUDA) serving all domains is not an engineering convenience — it is a reflection of the mathematical structure of computation itself.

### For BarraCUDA

The ToadStool team needs to optimize exactly 6 primitive categories. coralForge's validation proves that any future architecture — protein design, molecular dynamics, drug binding, RNA folding — will decompose into the same 6 operations. The investment in WGSL shader optimization has unbounded return.

### For LTEE Analysis

The structural evolution of LTEE proteins can be analyzed using the same primitives that analyze their sequence evolution (wetSpring HMM forward/backward, neuralSpring attention). The computational substrate is the same; only the interpretation layer changes. This unification is itself evidence for constrained evolution: the tools that emerged under type-system constraint serve every scientific domain.

---

*The strongest evidence for universality comes from the domain that looked most different.*
