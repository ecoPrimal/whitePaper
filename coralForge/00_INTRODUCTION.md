# coralForge: Sovereign Structure Prediction

## What coralForge Is

coralForge is a sovereign structure prediction engine — pure Rust f64 reference implementations of the algorithms behind AlphaFold2 (Jumper et al., 2021) and AlphaFold3 (Abramson et al., 2024), validated against NumPy baselines and accelerated via BarraCUDA/ToadStool WGSL shaders on consumer GPUs.

It is not a reimplementation of AlphaFold. It is the computational substrate that makes sovereign structure prediction *possible* — the same relationship that BarraCUDA has to CUDA, or that the springs have to their Python counterparts. coralForge implements the primitives. The pipeline emerges from composing them.

## Why It Exists

Three motivations, each sufficient alone:

### 1. The Isomorphism Proof

neuralSpring's core thesis is that all neural architectures decompose into 6 fundamental primitives (GEMM, Attention, Normalization, Nonlinearity, Reduction, Gating). Structure prediction is the strongest test of this claim because:

- AlphaFold uses **triangle operations** that appear in no other architecture — or do they? Triangle multiplication is a specialized form of batched outer product + elementwise gating. Triangle attention is attention with a pair bias mask. The "novel" operations decompose into known primitives.
- **IPA (Invariant Point Attention)** adds geometric distance terms to standard attention — but the core is still Q·K^T/√d → softmax → V, with extra features in the query/key/value projection.
- **Diffusion** (AlphaFold3) is the same DDPM/DDIM formalism used in image generation — cosine/linear noise schedules, forward corruption, reverse denoising.

If the 6 primitives explain structure prediction, the isomorphism theorem holds across *all* domains the ecosystem will ever need.

### 2. Sovereign Science

AlphaFold inference currently requires:

| Dependency | Problem |
|-----------|---------|
| Python runtime | Startup overhead, GIL, deployment complexity |
| PyTorch/JAX | 2+ GB frameworks with CUDA dependency |
| NVIDIA GPU | Vendor lock-in via CUDA |
| Cloud API | Data leaves the lab; rate limits; availability risk |
| MSA databases | 3+ TB downloads from centralized servers |

coralForge removes every one of these. Pure Rust binary. BarraCUDA WGSL shaders run on any Vulkan GPU (NVIDIA, AMD, Intel, even llvmpipe CPU). No cloud. The scientist's data never leaves their hardware.

This matters especially for:
- **Field genomics**: MinION sequencer + laptop + coralForge = structure prediction at the collection site
- **BSL-3/4 work**: Air-gapped labs cannot use cloud APIs
- **Resource-limited settings**: A single consumer GPU ($600 RTX 4070) runs the full pipeline
- **Data sovereignty**: AGPL-3.0 ensures the code stays open; the scientist owns every computation

### 3. The LTEE Connection

The Lenski Long-Term Evolution Experiment (LTEE) at Michigan State University maintains 75,000+ generations of *E. coli* in frozen fossil records. Chapter 14 of the thesis proposes sequencing these samples to validate the constrained evolution framework.

coralForge enables a critical analysis layer: **how do protein structures evolve under sustained environmental constraint?** Given whole-genome sequences from LTEE timepoints, coralForge can predict the 3D structure of every protein at every generation, revealing:

- Which structural folds are conserved across 75,000 generations of glucose-minimal constraint
- Whether convergent structural solutions appear across the 12 replicate populations
- How structural evolution correlates with the power-law fitness dynamics Wiser et al. (2013) documented
- Whether the Ara-3 citrate innovation (Blount et al., 2008, 2012) has a detectable structural precursor

This is the bridge between computational and biological constrained evolution — and coralForge makes it sovereign.

---

## The Name

**Coral**: Living structures assembled from simple polyps. A coral reef is a computational structure — each organism performs simple operations, and the emergent architecture is greater than the sum. The Rust crab connection is a bonus.

**Forge**: Where raw material becomes tools. coralForge takes the 6 universal primitives and forges them into structure prediction.

The working name was "sovereignFold." We dropped "fold" because coralForge isn't limited to protein folding — it handles any molecular structure prediction (protein, RNA, DNA, ligands, ions), and the pipeline extends to any dataset where structural evolution is interesting. The LTEE is the first target, but coral reefs, soil microbiomes, and extremophile populations are all on the roadmap.

Gabe Newell can carry a mini sequencer when he goes exploration diving. The structures predicted on his dive boat belong to science, not to a cloud API.

---

## Current State

| Component | Status | Checks |
|-----------|--------|--------|
| Evoformer primitives (gelu, layernorm, softmax, SDPA, triangle, MSA attention) | Validated | Py 12, Rs 9 |
| IPA (Invariant Point Attention) | Validated | Py 12, Rs 9 |
| Backbone frames + torsion angles | Validated | Py 12, Rs 9 |
| AlphaFold3 diffusion (DDPM, DDIM, SE(3)) | Validated | Py 29, Rs 26 |
| AlphaFold3 pairformer (conditioning, triangle, FFN) | Validated | Py 14, Rs 13 |
| AlphaFold3 confidence (pLDDT, PAE, pDE, ranking) | Validated | Py 19, Rs 16 |
| df64 WGSL shaders (15 shaders) | Validated on RTX 4070 + TITAN V | 37/37 GPU |
| **Total** | | **Py 62 + Rs 55 + GPU 37 = 154** |

### Quality

- Zero unsafe code (`#![forbid(unsafe_code)]`)
- Zero production mocks
- Zero inline magic numbers (all tolerances named and justified)
- 0 clippy pedantic warnings, 0 doc warnings
- Every `BaselineProvenance` constant documented
- Full provenance: script, commit, date, command, seed for every baseline

### Evolution Path

```
NumPy baseline → Rust CPU → BarraCUDA CPU → df64 WGSL → sovereign pipeline
    ✓ done        ✓ done     (next)         ✓ done      (target)
```

---

*coralForge is where neuralSpring's isomorphism theorem meets biology.*
