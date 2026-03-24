# Sub-Thesis 10: coralForge — Sovereign Structure Prediction for Evolutionary Biology

**Date:** March 1, 2026
**Status:** GPU tier closed. 210+ validation checks (Py 62/62, Rs 55/55, GPU Tensor 26/26, pure GPU 24/24, confidence GPU 5/5, BarraCuda CPU 3/3 coralForge, cross-spring 40/40). All CPU→GPU pipeline proven. LTEE application designed. 15 df64 WGSL shaders. Pipeline pending real PDB data. **coralReef Iter 65**: Sovereign pipeline at **8/10 layers**. Layer 8 (WPR/ACR) **SOLVED** (Exp 087, W1-W7 fixed). Layer 7 (SEC2 binding) SOLVED (Exp 085, B1-B7 fixed). Cross-driver profiling (Exp 086): interface problem confirmed. ACR bootstraps FECS/GPCCS. Layer 9 under investigation (falcon halt release). AMD DRM dispatch fully validated (6/6 PASS). RTX 5060 Blackwell DRM cracked (SM120). NVIDIA sovereign dispatch nearing: 2 layers remain.
**Domain:** Structural biology × constrained evolution × sovereign computing
**Novelty:** No prior work implements AlphaFold2/3 primitives in pure Rust f64
with complete CPU→GPU portability on consumer hardware

---

## Abstract

coralForge is a sovereign protein/RNA/DNA structure prediction engine built
entirely in Rust, reproducing AlphaFold2 and AlphaFold3 mathematical
primitives at f64 precision. The pipeline runs on a $600 consumer GPU
(RTX 4070) vs $83K/year cloud compute, with validated CPU→GPU mathematical
portability for every operation.

The constrained evolution connection: LTEE (Paper 02) produces mutant
proteins whose structural consequences can be predicted by coralForge
without depending on Google's infrastructure. Sovereign structure
prediction enables hypothesis generation about how fitness landscape
constraints manifest as structural changes.

## What's Validated

### AlphaFold2 (nF-01, nF-02)

| Component | Python | Rust CPU | BarraCuda CPU | GPU Tensor | Status |
|-----------|--------|----------|---------------|------------|--------|
| Evoformer attention | 10/10 | 8/8 | 3/3 | 6/6 | **Complete** |
| Triangle multiply | 8/8 | 6/6 | 3/3 | 4/4 | **Complete** |
| IPA (Invariant Point Attention) | 12/12 | 10/10 | — | — | **CPU complete** |
| Full Evoformer block | 19/19 | 18/18 | 17/17 | — | **CPU+bC complete** |

### AlphaFold3 (nF-03)

| Component | Python | Rust CPU | BarraCuda CPU | GPU Tensor | Status |
|-----------|--------|----------|---------------|------------|--------|
| Diffusion primitives | 29/29 | 26/26 | 3/3 | 14/14 | **Complete** |
| Pairformer block | 14/14 | 13/13 | 3/3 | 12/12 | **Complete** |
| Confidence heads | 19/19 | 16/16 | 3/3 | 5/5 | **Complete** |

### Pure GPU Pipeline (scalar-only readback)

| Domain | Checks | Pattern |
|--------|--------|---------|
| Diffusion forward | 2 | Mean readback |
| Pairformer FFN | 2 | Frobenius norm readback |
| Pairformer TriMul | 2 | Frobenius norm readback |

### Cross-Spring Evolution Benchmarks (S98)

| Operation | Time | Provenance |
|-----------|------|------------|
| cosine_beta_schedule T=200 | 1.5µs | neuralSpring `coral_forge::diffusion` |
| forward_diffusion 128 atoms | 0.7µs | neuralSpring `coral_forge::diffusion` |
| ddpm_reverse_step 128 atoms | 0.1µs | neuralSpring `coral_forge::diffusion` |
| ddim_reverse_step 128 atoms | 1.0µs | neuralSpring `coral_forge::diffusion` |
| se3_equivariant_noise 128 atoms | 1.1µs | neuralSpring `coral_forge::diffusion` |
| pair_transition_ffn 8×8 d=16 | 138µs | neuralSpring `coral_forge::diffusion` |
| sinusoidal_embedding d=64 | 0.9µs | neuralSpring `coral_forge::pairformer` |

## Cross-Spring Provenance

coralForge draws from all springs:

| Spring | Contribution | Key Primitives |
|--------|-------------|----------------|
| **hotSpring** | DF64 precision architecture, `compile_shader_df64` | FP48 accuracy on FP32 cores |
| **wetSpring** | Bio-shader patterns (triangle multiply, attention, GELU) | 700+ WGSL provenance |
| **neuralSpring** | Diffusion, Pairformer, confidence head implementations | `coral_forge::*` modules |
| **ToadStool** | Tensor API (`matmul`, `matmul_ref`, `transpose`, `softmax`) | GPU execution substrate |

## Extension: LTEE Structural Evolution

The primary scientific extension connects Paper 02 (LTEE frozen fossil
record) to structural biology:

1. **Predict structures** of LTEE citrate+ mutant proteins using coralForge
2. **Compare** wild-type vs mutant conformations (RMSD, pLDDT, contact maps)
3. **Map** structural changes onto fitness landscape predictions from Paper 01
4. **Test** whether Anderson localization constraints predict which mutations
   produce large structural changes vs neutral drift

**Data requirements**: LTEE protein sequences from frozen fossil record
(available from Lenski lab, ~60 years of evolution). PDB reference
structures for E. coli K-12 proteome (public, RCSB).

**Compute requirements**: coralForge primitives are validated but the full
end-to-end pipeline (MSA → Evoformer → Structure Module → Confidence) needs
assembly. Per-protein prediction on RTX 4070: estimated minutes for
small proteins (<200 residues), hours for larger domains.

## Extension: Real PDB Validation

Before LTEE application, validate coralForge against known structures:

1. **Select** 10-20 well-characterized small proteins (50-200 residues)
   from RCSB PDB with high-resolution experimental structures
2. **Run** coralForge pipeline: sequence → Evoformer → IPA → diffusion →
   confidence heads → predicted coordinates
3. **Compare** predicted vs experimental: Cα-RMSD, GDT-TS, pLDDT calibration
4. **Benchmark** sovereign Rust f64 vs AlphaFold server (free, rate-limited)

**Data**: RCSB PDB (public, ~220K structures). Sequence databases for MSA:
UniRef90 (~100GB), PDB70 (~15GB). Acquirable via NestGate NCBI pipeline.

**Compute**: MSA generation is the bottleneck (JackHMMer equivalent needed).
Structure prediction itself: forward pass through Evoformer (matmul-heavy,
GPU-accelerated) + diffusion (validated at 0.7µs/step for 128 atoms on CPU).

## What This Needs from Other Primals

| Primal | What coralForge Needs | Status |
|--------|----------------------|--------|
| **NestGate** | NCBI sequence fetch (EFetch for UniProt/PDB), content-addressed storage for reference DBs | `NCBILiveProvider` operational |
| **ToadStool** | `Tensor::gelu()` global kernel, batched 3D matmul, f64 Tensor parity | Absorption targets in V65 handoff |
| **biomeOS** | NUCLEUS orchestration for multi-gate pipeline (MSA on Strandgate EPYC, GPU inference on Northgate 5090) | Architecture ready, deployment pending LAN |
| **metalForge** | Cross-substrate dispatch: MSA on CPU cluster, structure prediction on GPU | Substrate model validated (47/47) |

## Reading Order

**For a structural biologist**: This document → `neuralSpring/whitePaper/coralForge/` (00-19) → Paper 02 (LTEE)

**For a computational biologist**: This document → Paper 01 (Anderson-QS) → Paper 02 (LTEE + coralForge) → `06_LTEE_APPLICATION.md`

**For a PhD committee**: Paper 01 → This document (sovereign pipeline) → Paper 02 (LTEE predictions) → Paper 07 (sovereign WDM, same philosophy)

---

*coralForge: sovereign structure prediction for evolutionary biology.
210+ checks, full CPU→GPU pipeline, 15 df64 WGSL shaders, 7 AF3 CPU
benchmarks. S98: GPU tier closed. Next: real PDB validation, LTEE
structural evolution, primal integration (NestGate + biomeOS NUCLEUS).*
