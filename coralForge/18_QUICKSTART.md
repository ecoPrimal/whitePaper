# coralForge Quickstart

Get coralForge running from source in under 5 minutes. No Python required for validation — only Rust.

---

## Prerequisites

| Requirement | Version | Check |
|-------------|:-------:|-------|
| Rust (stable) | 1.82+ | `rustc --version` |
| Cargo | 1.82+ | `cargo --version` |
| GPU (optional) | Any Vulkan/Metal/DX12 | `vulkaninfo` or skip GPU tests |

No Python, no CUDA, no conda, no Docker. Just Rust.

---

## Clone and Build

```bash
git clone git@github.com:ecoPrimals/neuralSpring.git
cd neuralSpring
cargo build --release
```

Build time: ~3 minutes on first compile (2,684 LOC in coralForge, ~65,000 LOC total in neuralSpring).

---

## Run Validation

### CPU validation (no GPU required)

```bash
# Evoformer primitives (GELU, softmax, attention, triangle, MSA, IPA):
cargo run --release --bin validate_coral_forge

# Full Evoformer block:
cargo run --release --bin validate_coral_forge_evoformer_block

# AlphaFold3 diffusion:
cargo run --release --bin validate_coral_forge_diffusion

# AlphaFold3 pairformer:
cargo run --release --bin validate_coral_forge_pairformer

# AlphaFold3 confidence heads:
cargo run --release --bin validate_coral_forge_confidence
```

Expected output:

```
═══ coralForge Evoformer Primitives ═══
✓ gelu_basic .......................... PASS
✓ layer_norm_2x3 ..................... PASS
✓ softmax_rows_basic ................. PASS
...
═══ 12/12 checks passed ═══
```

### GPU validation (requires GPU)

```bash
cargo run --release --bin validate_coral_forge_gpu
cargo run --release --bin validate_coral_forge_gpu_pipeline
```

If no GPU is detected, these binaries skip gracefully with a message.

### Full validation suite

```bash
bash control/validate_all.sh
```

Runs all 185 neuralSpring validation binaries, including the coralForge subset. Takes ~2 minutes.

---

## Run Unit Tests

```bash
# coralForge tests only:
cargo test -- coral_forge

# All neuralSpring tests:
cargo test
```

---

## Explore the Code

```
src/coral_forge/
├── mod.rs              ← Start here: module root with all public re-exports
├── activation.rs       ← GELU, LayerNorm, softmax (simplest primitives)
├── attention.rs        ← Scaled dot-product attention
├── triangle.rs         ← Triangle multiplication + attention (AlphaFold-specific)
├── msa.rs              ← MSA row/column attention + outer product mean
├── diffusion.rs        ← Noise schedules, forward/reverse diffusion steps
├── pairformer.rs       ← Pairformer block with timestep conditioning
├── confidence.rs       ← pLDDT, PAE, pDE confidence estimation
└── structure/
    ├── mod.rs           ← Structure module root
    ├── ipa.rs           ← Invariant Point Attention (the key innovation)
    ├── backbone.rs      ← Backbone frame updates + torsion angles
    └── frame.rs         ← Rigid-body frame operations (rotate, translate, compose)
```

**Suggested reading order for the source**: `activation.rs` (simplest) → `attention.rs` → `triangle.rs` → `msa.rs` → `structure/frame.rs` → `structure/ipa.rs` → `diffusion.rs` → `pairformer.rs` → `confidence.rs` (most complex).

---

## Explore the Baselines

```bash
# Regenerate Python baselines (requires Python 3.10+, NumPy 2.2.6):
pip install numpy==2.2.6
python3 control/coral_forge/evoformer_primitives.py
python3 control/coral_forge/alphafold2_evoformer_block.py
python3 control/coral_forge/alphafold3_diffusion.py
python3 control/coral_forge/alphafold3_pairformer.py
python3 control/coral_forge/alphafold3_confidence.py

# Check for drift against committed baselines:
bash control/check_drift.sh
```

---

## Quality Gates

Before submitting any change:

```bash
cargo fmt --check                                          # formatting
cargo clippy --all-targets -- -D warnings -W clippy::pedantic  # lints
cargo test                                                 # unit tests
cargo doc --no-deps 2>&1 | grep warning                   # doc warnings (must be empty)
bash control/validate_all.sh                               # full validation
```

All five must pass. See [11_CONTRIBUTING.md](11_CONTRIBUTING.md) for details.

---

## Where to Go Next

| Goal | Document |
|------|----------|
| Understand the architecture | [01_ARCHITECTURE.md](01_ARCHITECTURE.md) |
| Read the API docs | [07_API_REFERENCE.md](07_API_REFERENCE.md) |
| Add a new primitive | [11_CONTRIBUTING.md](11_CONTRIBUTING.md) |
| Understand the testing strategy | [14_TESTING.md](14_TESTING.md) |
| See the roadmap | [13_ROADMAP.md](13_ROADMAP.md) |
| Learn the terminology | [10_GLOSSARY.md](10_GLOSSARY.md) |

---

*Quickstart: clone, build, validate. Five minutes to truth.*
