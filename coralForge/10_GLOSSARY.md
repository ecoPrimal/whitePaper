# coralForge Glossary

Terms and abbreviations used across the coralForge white paper series, sorted alphabetically.

---

### AlphaFold2 (AF2)
DeepMind's protein structure prediction system (Jumper et al., 2021). Introduced the Evoformer + Structure Module architecture. coralForge re-implements the core algorithms in Rust f64.

### AlphaFold3 (AF3)
Successor to AF2 (Abramson et al., 2024). Replaces the Structure Module with a diffusion-based decoder and adds the Pairformer. coralForge implements the new primitives (diffusion, pairformer, confidence heads).

### BarraCUDA
Shared Rust crate (`crates/barracuda/`) providing GPU-accelerated primitives for the ecoPrimals ecosystem. coralForge's WGSL shaders are candidates for upstream absorption into BarraCUDA.

### Backbone frames
Rigid-body transforms representing each amino acid residue's coordinate system. Stored as 12 f64 values: 3×3 rotation matrix (row-major) + 3D translation vector.

### BaselineProvenance
A struct in `neuralSpring/src/provenance.rs` that records the origin of every validation baseline: script path, commit hash, date, command, environment, seed, and expected value.

### Confidence heads
Neural network outputs that estimate prediction quality. coralForge implements three: pLDDT (per-residue), PAE (pairwise alignment error), and pDE (pairwise distance error).

### coralForge
Sovereign structure prediction engine within ecoPrimals. Named for the coral reef (living computational structure from simple organisms) and the forge (where raw materials become tools). Formerly `sovereign_folding` + `structure_module`, unified in Session 94.

### DDIM (Denoising Diffusion Implicit Models)
Song et al. (2020). A deterministic reverse process for diffusion models. Used in AlphaFold3 during inference for faster sampling.

### DDPM (Denoising Diffusion Probabilistic Models)
Ho et al. (2020). A stochastic reverse process for diffusion models. AlphaFold3 trains with DDPM; inference may use DDPM or DDIM.

### df64
Double-precision float emulation on f32 GPU cores. Uses pairs of f32 values to achieve ~50 bits of mantissa precision (vs 52 for native f64). Implemented in coralForge's WGSL shaders. Maximum observed error vs native f64: < 1e-6.

### Drift detection
The practice of re-running Python baselines and comparing to committed JSON to detect changes in numerical output. Catches NumPy upgrades, Python version changes, or seed behavior shifts.

### ecoPrimals
The overarching ecosystem of sovereign computing projects. Includes neuralSpring, wetSpring, hotSpring, RootPulse, ToadStool, and others.

### Evoformer
The core attention-based feature extraction module in AlphaFold2/3. Operates on MSA and pair representations through alternating row attention, column attention, triangle operations, and transitions. Typically 48 blocks.

### Forward diffusion
Adding noise to structure coordinates at a given timestep: `x_t = √(ᾱ_t) · x_0 + √(1 - ᾱ_t) · ε`. Part of the AlphaFold3 diffusion pipeline.

### GELU (Gaussian Error Linear Unit)
Activation function used in transformer-based architectures: `gelu(x) = 0.5 · x · (1 + tanh(√(2/π) · (x + 0.044715 · x³)))`.

### IPA (Invariant Point Attention)
AlphaFold2's SE(3)-equivariant attention mechanism (Algorithm 22). Uses 3D point distances projected through backbone frames to make attention scores geometry-aware. The key innovation that enables structure prediction.

### Isomorphism Theorem
neuralSpring's central thesis: all neural architectures decompose into 6 universal primitives (GEMM, Attention, Normalization, Nonlinearity, Reduction, Gating). coralForge provides the strongest evidence by showing AlphaFold's "novel" operations also decompose into these primitives.

### Layer normalization
Normalization technique (Ba et al., 2016) that normalizes across features for each sample independently: `y = γ · (x - μ) / √(σ² + ε) + β`.

### LTEE (Long-Term Evolution Experiment)
Richard Lenski's ongoing experiment tracking 12 populations of *Escherichia coli* through 75,000+ generations since 1988. coralForge's target application: structural analysis of evolved proteins from LTEE frozen fossil record.

### MSA (Multiple Sequence Alignment)
A matrix of related protein sequences aligned by homology. AlphaFold2/3 uses MSA information to extract co-evolutionary signals via row and column attention.

### neuralSpring
The learning layer of ecoPrimals. Implements ML surrogate models and the isomorphism theorem validation. coralForge lives within neuralSpring as `src/coral_forge/`.

### Noise schedule
The sequence of noise levels (β_t) used in diffusion models. coralForge implements two: linear (Ho et al., 2020) and cosine (Nichol & Dhariwal, 2021).

### Outer product mean
Algorithm 10 from AlphaFold2. Projects MSA information into the pair representation: `output[i,j] = mean_s(a[s,i] ⊗ b[s,j])`. The bridge between MSA and pair tracks.

### PAE (Predicted Aligned Error)
Pairwise confidence metric: estimates the error in the relative position of residue j when the structure is aligned on residue i. Output as an N×N matrix.

### Pairformer
AlphaFold3's replacement for the pair stack in the Evoformer. Adds timestep conditioning for the diffusion process. A single pairformer block: LayerNorm → conditioning → triangle mul (out + in) → triangle attention → FFN → residual.

### pDE (Predicted Distance Error)
New confidence metric in AlphaFold3. Estimates the error in predicted inter-residue distances. Output as an N×N matrix. Complements PAE.

### pLDDT (Predicted Local Distance Difference Test)
Per-residue confidence metric: softmax over 50 bins, weighted sum gives a [0, 1] score. Higher = more confident. Values > 0.7 are generally reliable.

### Primitives (6 universal)
The building blocks of the isomorphism theorem: **GEMM** (matrix multiplication), **Attention** (scaled dot-product), **Normalization** (layer/batch norm), **Nonlinearity** (GELU/ReLU), **Reduction** (mean/sum/max), **Gating** (element-wise product with sigmoid). Every coralForge operation decomposes into these.

### `require!`
Validation macro that replaces `expect()` in neuralSpring binaries. Records a named error and continues (graceful degradation) instead of panicking.

### SE(3) equivariance
Symmetry property: structure prediction should give the same result regardless of how the protein is rotated or translated in 3D space. Achieved in coralForge by centering coordinates before diffusion and using frame-projected point distances in IPA.

### Sovereign computing
The principle of owning the complete compute stack from source code to hardware. No cloud inference, no proprietary dependencies, no API keys. coralForge is sovereign: Rust source + WGSL shaders on consumer GPUs.

### Structure Module
AlphaFold2's iterative coordinate refinement. Applies IPA, backbone updates, and torsion angle prediction for 8 iterations to convert features into 3D coordinates.

### ToadStool
ecoPrimals' compute primal for GPU promotion. The hardware target for BarraCUDA-accelerated inference. coralForge's shaders will be absorbed into ToadStool for production deployment.

### Tolerances (named)
Domain-specific numerical thresholds defined as named constants in `src/tolerances/mod.rs`. Examples: `FOLDING_EPS` (1e-10), `FISHER_EPS` (1e-12), `BURGERS_IC_GUARD` (1e-14). 139+ named tolerances across neuralSpring — zero inline magic numbers.

### Torsion angles
The 7 dihedral angles per residue (φ, ψ, ω, χ1–χ4) that define side-chain conformation. Predicted from the single representation via a 2-layer MLP with `atan2` output.

### Triangle multiplication
Algorithms 11-12 from AlphaFold2. Self-interaction within the pair representation: for each residue pair (i,j), aggregate information from all residue pairs sharing one index (i,k) or (k,j). The O(N²·C) bottleneck of the Evoformer.

### Triangle attention
Algorithms 13-14 from AlphaFold2. Multi-head attention over the pair representation with pair bias. Applied along rows (starting node) and columns (ending node).

### Validate_all
neuralSpring's comprehensive validation script: runs all Rust validation binaries (185/185 in Session 94), checking both CPU and GPU results against Python baselines.

### WGSL (WebGPU Shading Language)
The shader language for WebGPU. coralForge uses WGSL for cross-platform GPU compute — the same shaders run on NVIDIA, AMD, Intel, and Apple Silicon GPUs via `wgpu`.

---

*Glossary: know the words, understand the work.*
