# coralForge — Frequently Asked Questions

---

## General

### What is coralForge?

coralForge is a sovereign protein structure prediction engine. It re-implements AlphaFold2 and AlphaFold3 primitives in pure Rust f64, validates them against NumPy baselines, and accelerates them via WGSL shaders on consumer GPUs. The goal: predict protein structures on hardware you own, with code you can read, and no data leaving your machine.

### Why not just use AlphaFold Server?

AlphaFold Server requires uploading your protein sequence to Google's servers. For unpublished research sequences, clinical data under HIPAA/GDPR, or sensitive biosecurity work, this is unacceptable. coralForge runs entirely on local hardware.

### Why not use ColabFold?

ColabFold runs on Google Colab (cloud) or locally with CUDA (NVIDIA-only). coralForge uses WGSL via WebGPU, which runs on NVIDIA, AMD, Intel, and Apple Silicon GPUs. No vendor lock-in. ColabFold also uses PyTorch at runtime — coralForge uses no Python at runtime.

### Can coralForge predict structures today?

Not yet. coralForge has validated all the *primitives* (attention, triangle operations, diffusion, IPA, confidence) against reference implementations. End-to-end inference (sequence → structure) is Phase D on the roadmap. See [13_ROADMAP.md](13_ROADMAP.md).

### When will end-to-end inference be ready?

Estimated Phase D (Sessions 106–130). No fixed date — phases gate on correctness, not deadlines. See the [roadmap](13_ROADMAP.md) for milestone details.

---

## Technical

### Why pure f64 instead of f32?

coralForge is first and foremost a *reference* implementation. f64 eliminates precision-related debugging — if a test fails, it is an algorithm bug, not a precision issue. f32 inference will come in Phase D+ as an optimization, validated against the f64 reference.

### Why flat arrays instead of ndarray?

Three reasons: (1) flat `&[f64]` maps directly to GPU buffer uploads with zero conversion, (2) explicit indexing (`x[i * cols + j]`) is trivially verifiable against paper pseudocode, and (3) no external dependency — ndarray optionally links to BLAS (C/C++), which would break the pure-Rust guarantee. See [DD-02 in 15_DESIGN_DECISIONS.md](15_DESIGN_DECISIONS.md).

### What is df64?

Double-float emulation using pairs of f32 values on GPU. Provides ~50 bits of mantissa precision (vs 52 for native f64) while running at f32 throughput. Most consumer GPUs process native f64 at 1/64 the rate of f32 — df64 is roughly 16× faster than native f64 on the same hardware. Maximum observed error vs CPU f64: < 1e-6.

### Why WGSL instead of CUDA?

WGSL (WebGPU Shading Language) runs on all GPU vendors via the wgpu library (pure Rust). CUDA is proprietary and NVIDIA-only. For sovereign computing, vendor lock-in is unacceptable. The performance cost of WGSL vs CUDA is minimal for the O(N²) operations in structure prediction.

### How does coralForge relate to neuralSpring?

coralForge lives inside neuralSpring as the `src/coral_forge/` module. neuralSpring provides the shared infrastructure: validation harness, tolerance constants, provenance tracking, quality gates. Phase F will extract coralForge into a standalone crate.

### How does coralForge relate to BarraCUDA?

BarraCUDA is the shared GPU acceleration crate. coralForge currently uses its own hand-written WGSL shaders. Phase C will integrate BarraCUDA's CPU primitives (matmul, etc.), and the coralForge shaders are candidates for upstream absorption into BarraCUDA.

### What are the 6 universal primitives?

GEMM (matrix multiplication), Attention (scaled dot-product), Normalization (layer/batch norm), Nonlinearity (GELU/ReLU), Reduction (mean/sum/max), and Gating (element-wise product with sigmoid). coralForge demonstrates that AlphaFold's "novel" operations (triangle multiplication, IPA, diffusion) all decompose into these 6 primitives. This supports neuralSpring's isomorphism theorem.

---

## LTEE Application

### What is the LTEE?

The Long-Term Evolution Experiment, run by Richard Lenski at Michigan State University since 1988. Twelve populations of *Escherichia coli* have been propagated daily for 75,000+ generations under glucose-minimal constraint. Frozen samples from every 500 generations create a "fossil record" of bacterial evolution.

### How will coralForge be used for LTEE analysis?

coralForge will predict protein structures for evolved *E. coli* genes, then compare structures across populations and time points. Key questions: Do independently evolved populations converge on the same structural solutions? Is structural evolution gradual or punctuated? What structural precursors enabled the Cit+ innovation in population Ara-3? See [06_LTEE_APPLICATION.md](06_LTEE_APPLICATION.md).

### Do I need wet lab access?

For the initial analysis, no — LTEE genome sequences are publicly available via GenBank. For the full pipeline (frozen stock → sequencing → analysis), wet lab access is needed. The complete wet-to-dry pipeline is documented in [06_LTEE_APPLICATION.md](06_LTEE_APPLICATION.md).

---

## Building and Running

### What are the system requirements?

Rust 1.82+ (stable). That's it for CPU validation. For GPU validation, any GPU with Vulkan, Metal, or DirectX 12 support. No CUDA needed. See [18_QUICKSTART.md](18_QUICKSTART.md).

### Does it work on macOS/Windows?

The Rust code is platform-independent. WGSL shaders run via wgpu, which supports macOS (Metal), Windows (DX12/Vulkan), and Linux (Vulkan). Validation has been performed on Linux (Pop!_OS 22.04); other platforms are expected to work but not yet CI-tested.

### How long does the full validation take?

About 2 minutes for all 185 neuralSpring validation binaries on an i9-12900K. The coralForge subset (5 CPU + 2 GPU binaries) takes about 30 seconds.

### How do I regenerate the Python baselines?

`pip install numpy==2.2.6`, then run each script in `control/coral_forge/`. See [18_QUICKSTART.md](18_QUICKSTART.md). Python is only needed for baseline generation, never at runtime.

---

## Contributing

### How do I add a new primitive?

Write the Python baseline first, then the Rust implementation, then a validation binary, then provenance. Full walkthrough in [11_CONTRIBUTING.md](11_CONTRIBUTING.md).

### What quality gates must pass?

`cargo fmt`, `clippy --pedantic`, `cargo test`, `cargo doc` (zero warnings), and `validate_all.sh` (185/185). All five. No exceptions.

### Can I use unsafe code?

No. Zero `unsafe` blocks in coralForge source. The BarraCUDA integration layer may use `unsafe` internally, but coralForge's own code does not.

---

## Licensing

### What license is coralForge under?

AGPL-3.0-or-later. You can use, modify, and distribute coralForge freely. If you distribute a modified version (including as a web service), you must release your modifications under the same license.

### Can I use coralForge for commercial work?

Yes, as long as you comply with the AGPL-3.0 terms. If you modify coralForge and deploy it as a service (e.g., a structure prediction API), you must release your modifications.

### Are the baselines copyrighted?

The baseline *algorithms* are from published papers (Jumper et al. 2021, Abramson et al. 2024). The baseline *implementations* (Python scripts and Rust code) are original work under AGPL-3.0-or-later.

---

*FAQ: if the answer isn't here, it's in one of the 18 other documents.*
