# coralForge — Sovereign Structure Prediction

**Where structure prediction becomes sovereign: no cloud, no proprietary inference, no Python at runtime.**

---

## Overview

coralForge is the sovereign structure prediction engine within the ecoPrimals ecosystem. It implements AlphaFold2 and AlphaFold3 primitives in pure Rust f64, validated against NumPy baselines, and accelerated via BarraCUDA/ToadStool WGSL shaders on consumer GPUs.

The name connects the coral reef — a living computational structure assembled from simple organisms — with the forge, where raw materials become tools. A sequencer on a dive boat. A MinION in a farm field. Structure prediction that belongs to the scientist, not the cloud.

**Status**: February 28, 2026 — Evoformer, IPA, diffusion, pairformer, and confidence heads implemented and validated. 62/62 Python + 55/55 Rust + 37/37 GPU = **154 checks**. 15 df64 WGSL shaders evolved. All quality gates green. 2,684 LOC across 12 source files, 8 modules, 40 public API items.

**White Paper**: 20 documents covering design, implementation, validation, evolution, benchmarks, security, and community guidance.

**License**: AGPL-3.0-or-later

---

## Document Series

### Design & Architecture

| # | Document | Description |
|---|----------|-------------|
| 00 | [00_INTRODUCTION.md](00_INTRODUCTION.md) | What coralForge is and why it exists |
| 01 | [01_ARCHITECTURE.md](01_ARCHITECTURE.md) | Evoformer → IPA → Diffusion → Confidence pipeline |
| 02 | [02_ISOMORPHISM.md](02_ISOMORPHISM.md) | How structure prediction decomposes into the 6 universal primitives |
| 15 | [15_DESIGN_DECISIONS.md](15_DESIGN_DECISIONS.md) | Architectural choices: what, why, and what was rejected |

### Implementation & Validation

| # | Document | Description |
|---|----------|-------------|
| 03 | [03_IMPLEMENTATION.md](03_IMPLEMENTATION.md) | Rust module structure, f64 reference implementations, testing strategy |
| 04 | [04_VALIDATION.md](04_VALIDATION.md) | Python baselines, tolerances, GPU shader evolution, df64 streaming |
| 07 | [07_API_REFERENCE.md](07_API_REFERENCE.md) | Complete public API: every function, parameter, and shape |
| 08 | [08_DATA_PROVENANCE.md](08_DATA_PROVENANCE.md) | Baseline origins, algorithm references, drift detection |
| 14 | [14_TESTING.md](14_TESTING.md) | Three-tier validation: unit → binary → GPU |

### Evolution & Applications

| # | Document | Description |
|---|----------|-------------|
| 05 | [05_EVOLUTION.md](05_EVOLUTION.md) | Roadmap: MSA databases → end-to-end inference → LTEE analysis |
| 06 | [06_LTEE_APPLICATION.md](06_LTEE_APPLICATION.md) | Using coralForge for LTEE wet lab genetic structure analysis |
| 13 | [13_ROADMAP.md](13_ROADMAP.md) | Phase-gated roadmap with milestones and release criteria |

### Project & Community

| # | Document | Description |
|---|----------|-------------|
| 09 | [09_BENCHMARKS.md](09_BENCHMARKS.md) | CPU/GPU benchmarks, projected inference times, memory analysis |
| 10 | [10_GLOSSARY.md](10_GLOSSARY.md) | Terms and abbreviations used across the white paper |
| 11 | [11_CONTRIBUTING.md](11_CONTRIBUTING.md) | How to add primitives, evolve shaders, and pass quality gates |
| 12 | [12_DEPENDENCIES.md](12_DEPENDENCIES.md) | Zero C/C++ dependencies — the full audit |
| 16 | [16_SECURITY.md](16_SECURITY.md) | Threat model, data sovereignty, and supply chain analysis |
| 17 | [17_CHANGELOG.md](17_CHANGELOG.md) | Session-by-session evolution history |
| 18 | [18_QUICKSTART.md](18_QUICKSTART.md) | Clone → build → validate in 5 minutes |
| 19 | [19_FAQ.md](19_FAQ.md) | Frequently asked questions |

---

## Reading Order

**For a biologist**: 00 (what it is) → 06 (LTEE application) → 05 (what's coming) → 10 (glossary)

**For a computational scientist**: 00 → 01 (architecture) → 07 (API) → 03 (implementation) → 09 (benchmarks)

**For the ToadStool/BarraCUDA team**: 01 (architecture) → 04 (validation) → 12 (dependencies) → 13 (roadmap)

**For the thesis committee**: 00 → 02 (isomorphism) → 06 (biological validation) → 15 (design decisions)

**For a new contributor**: 00 → 11 (contributing) → 14 (testing) → 07 (API) → 10 (glossary)

**For security review**: 16 (security) → 12 (dependencies) → 08 (provenance)

---

## Connection to the Thesis

coralForge connects to the constrained evolution thesis at three levels:

1. **The Isomorphism Theorem** (Ch. 12): Structure prediction decomposes into the same 6 primitives as language models, vision models, and physics surrogates. This is the strongest evidence that the primitive decomposition is universal, not domain-specific.

2. **Biological Validation** (Ch. 14): coralForge enables sovereign structure prediction on LTEE samples — analyzing how protein structures evolve under glucose-minimal constraint across 75,000+ generations. This closes the loop between computational and biological constrained evolution.

3. **baseCamp Paper 02** (LTEE Extensions): coralForge provides the structural analysis component for the LTEE frozen fossil record proposal. Predict protein fold changes, detect convergent structural solutions across populations, and correlate structural evolution with fitness trajectories.

---

## The Pipeline

```
Frozen LTEE sample → DNA extraction → sequencing → wetSpring 16S/WGS
     → gene calling → coralForge structure prediction → structural evolution analysis
          → Anderson-QS correlation → constrained evolution validation
```

Each step runs on sovereign hardware. No cloud. No proprietary tools. The scientist owns every bit.

---

## Quick Start

```bash
git clone git@github.com:ecoPrimals/neuralSpring.git
cd neuralSpring && cargo build --release
cargo run --release --bin validate_coral_forge          # 12/12 checks
cargo run --release --bin validate_coral_forge_gpu      # 22/22 checks (needs GPU)
```

Full details: [18_QUICKSTART.md](18_QUICKSTART.md)

---

## Quick Links

| Resource | Location |
|----------|----------|
| Source code | `neuralSpring/src/coral_forge/` |
| Python baselines | `neuralSpring/control/coral_forge/` |
| BarraCUDA requirements | `neuralSpring/coral_forge/BARRACUDA_FOLDING_REQUIREMENTS.md` |
| MSA database plan | `neuralSpring/coral_forge/MSA_DATABASE_PLAN.md` |
| AlphaFold3 assessment | `neuralSpring/specs/NF03_ALPHAFOLD3_ASSESSMENT.md` |
| Validation handoff | `neuralSpring/wateringHole/handoffs/` (V62) |
| df64 WGSL shaders | `neuralSpring/metalForge/shaders/` |
| Thesis Ch. 12 | `gen3/thesis/12_results_neuralspring.md` |
| Thesis Ch. 14 | `gen3/thesis/14_biological_validation.md` |
| baseCamp 02 | `gen3/baseCamp/02_ltee_extensions.md` |
| FAQ | [19_FAQ.md](19_FAQ.md) |

---

*coralForge — structure prediction that belongs to the scientist.*
*20 documents. 154 checks. Zero cloud. Zero compromise.*
