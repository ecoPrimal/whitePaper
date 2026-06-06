# tideGlass — lithoSpore Deployment Design

**Date**: June 6, 2026
**Status**: Design sketch (for ecosystem to build from)
**Pattern source**: `sporeGarden/lithoSpore` (LTEE instance, 7/7 PASS, deployed to Barrick Lab)
**Target**: GPS sovereign rebuild → NUCLEUS lithoSpore (USB-deployable, self-verifying)
**Org**: `protoKarya`
**Domain expert**: Bin Chen (PI, MSU) — introduction via Andrea Gonzales
**Niche**: Transcriptomic drug discovery (gene expression reversal → therapeutic compounds)

---

## The Niche Deployment Question

lithoSpore evolved to reproduce microbial evolution (LTEE). The chassis is
domain-agnostic — `litho-core` carries no LTEE science. The question: **what
happens when we deploy this biology into a completely different niche?**

LTEE lithoSpore:
- 7 modules, 75 checks, 7 papers
- Data: mutation tables, allele frequencies, fitness measurements (~200 MB)
- Math: curve fitting, fixation probability, model selection
- Domain: microbial evolution over 82,500 generations

tideGlass lithoSpore:
- 7 modules, ~120 checks (estimated), 6 papers
- Data: gene expression profiles, chemical structures, model weights (~15 GB)
- Math: deep learning, MCTS, multi-objective optimization, correlation analysis
- Domain: drug discovery via transcriptomic reversal over 20 years of science

The niche is radically different. The chassis should work unchanged. If it
doesn't, the gaps reveal what `litho-core` is missing. That's the value of
deploying in new soil — the biology tells you what organs it still needs.

---

## Module Registry (scope.toml sketch)

```toml
[guidestone]
name = "tideglass-guidestone"
version = "0.1.0"
target = "GPS Platform — Bin Chen Lab, MSU"
created = "2026-06-06"
standard = "TARGETED_GUIDESTONE_STANDARD v1.0"
targets_file = "data/targets/gps_validation_targets.toml"
graph_file = "graphs/tideglass_guidestone.toml"

# --- Contributing Springs ---

[[spring]]
name = "healthSpring"
contributes = [
    "Hill dose-response (IC50 validation)",
    "MATRIX scoring (Fajgenbaum framework)",
    "Anderson geometry (tissue propagation)",
    "Population PK Monte Carlo (compound distribution)",
    "ChEMBL bioactivity pipeline (Exp093)",
    "ADDRC HTS pipeline (Exp091)",
]
modules = ["gps-screening", "gps-mcts", "gps-nf-extension"]
papers = ["Chen2017", "Zeng2021", "Xing2026"]

[[spring]]
name = "wetSpring"
contributes = [
    "ChEMBL data fetch (handle_chembl_fetch)",
    "PubChem data fetch (handle_pubchem_fetch)",
    "NCBI GEO fetch (L1000 profiles)",
    "NestGate content-addressing",
    "Provenance trio (session + step + completion)",
]
modules = ["gps-rcl", "gps-prediction", "gps-screening"]
papers = ["Subramanian2017"]

[[spring]]
name = "neuralSpring"
contributes = [
    "Deep learning model training infrastructure",
    "Multi-network co-training (RCL pattern)",
    "SMILES encoding → learned representation",
    "Model checkpoint BLAKE3 verification",
]
modules = ["gps-rcl", "gps-prediction"]
papers = ["Xing2026"]

[[spring]]
name = "hotSpring"
contributes = [
    "Anderson disorder (tissue geometry for drug propagation)",
    "Conformational energy landscapes (compound flexibility)",
]
modules = ["gps-nf-extension"]
papers = ["Anderson analogy"]

# --- Seven Science Modules ---

[[module]]
name = "rges_correlation"
binary = "tideglass-rges"
data_dir = "artifact/data/chen_2017_rges"
expected = "validation/expected/module1_rges.json"
tier1_notebook = "notebooks/module1_rges/rges_correlation.py"
paper = "Chen 2017, Nature Communications"
claim = "RGES correlates with IC50 (r=0.52, P=2.3e-3 in MCF7)"

[[module]]
name = "rcl_noise_cleaning"
binary = "tideglass-rcl"
data_dir = "artifact/data/lincs_vcap_t1"
expected = "validation/expected/module2_rcl.json"
tier1_notebook = "notebooks/module2_rcl/rcl_vcap_cleaning.py"
paper = "Xing 2026, Cell (RCL component)"
claim = "RCL improves VCAP_t1 profile signal-to-noise vs raw LINCS"

[[module]]
name = "expression_prediction"
binary = "tideglass-gps4drug"
data_dir = "artifact/data/gps4drug_heldout"
expected = "validation/expected/module3_prediction.json"
tier1_notebook = "notebooks/module3_prediction/gps4drug_heldout.py"
paper = "Xing 2026, Cell (GPS4Drug component)"
claim = "GPS4Drug predicts expression from structure (R² on held-out test set)"

[[module]]
name = "reversal_screening"
binary = "tideglass-screen"
data_dir = "artifact/data/zinc_hcc_screen"
expected = "validation/expected/module4_screening.json"
tier1_notebook = "notebooks/module4_screening/zinc_reversal_screen.py"
paper = "Xing 2026, Cell (screening validation)"
claim = "ZINC screening recovers known HCC actives (enrichment AUC)"

[[module]]
name = "mcts_optimization"
binary = "tideglass-molsearch"
data_dir = "artifact/data/molsearch_hcc"
expected = "validation/expected/module5_mcts.json"
tier1_notebook = "notebooks/module5_mcts/molsearch_hcc_lead.py"
paper = "Xing 2026, Cell (MolSearch component)"
claim = "MCTS optimizes HCC lead (IC50 4μM → 0.5μM, selectivity maintained)"

[[module]]
name = "octad_parity"
binary = "tideglass-octad"
data_dir = "artifact/data/octad_hcc_baseline"
expected = "validation/expected/module6_octad.json"
tier1_notebook = "notebooks/module6_octad/octad_parity.py"
paper = "Zeng 2021, Nature Protocols"
claim = "GPS screening exceeds OCTAD repurposing for HCC targets"

[[module]]
name = "nf_extension"
binary = "tideglass-nf"
data_dir = "artifact/data/nf_disease_signatures"
expected = "validation/expected/module7_nf.json"
tier1_notebook = "notebooks/module7_nf/nf_reversal_screen.py"
paper = "Novel (no prior publication)"
claim = "GPS reversal scoring identifies candidates for NF1-driven tumors"

# --- Primals (Tier 3, optional) ---

[[primal]]
name = "rhizoCrypt"
tier = 3
required = false
purpose = "DAG provenance chain for each module execution"

[[primal]]
name = "loamSpine"
tier = 3
required = false
purpose = "Certificate chain for model weight verification"

[[primal]]
name = "sweetGrass"
tier = 3
required = false
purpose = "Attribution braid (6 papers, LINCS program, ChEMBL, NF Data Portal)"

[[primal]]
name = "toadStool"
tier = 3
required = false
purpose = "GPU dispatch for RCL training + MCTS tree search + population PK"

[[primal]]
name = "nestGate"
tier = 2
required = false
purpose = "Content-addressed data fetch (LINCS, ChEMBL, PubChem, ZINC)"

# --- Foundation Threads ---

[[foundation_thread]]
id = "03"
name = "Immunology / Drug Discovery"
datasets = ["lincs_l1000", "chembl_jak_panel", "nf_data_portal"]

[[foundation_thread]]
id = "07"
name = "Anderson Framework"
datasets = ["anderson_tissue_geometry"]
notes = "d_eff for nerve sheath (NF) and liver (HCC) tissue"

# --- Source ---

[source]
repo = "git@github.com:protoKarya/tideGlass.git"
repo_https = "https://github.com/protoKarya/tideGlass.git"
branch = "main"
ecosystem_repo = "git@github.com:sporeGarden/ecoPrimals.git"
ecosystem_repo_https = "https://github.com/sporeGarden/ecoPrimals.git"
rust_toolchain = "stable"
rust_target = "x86_64-unknown-linux-musl"
license = "AGPL-3.0-or-later"
```

---

## What litho-core Needs (Niche Pressure)

Deploying in the GPS niche will reveal gaps in the domain-agnostic chassis.
Predicted pressures:

| Pressure | LTEE (existing) | tideGlass (new) | litho-core Gap |
|----------|----------------|----------------|----------------|
| **Data size** | ~200 MB (tables, frequencies) | ~15 GB (L1000 profiles, model weights) | Streaming validation — can't load all data into memory |
| **Model weights** | None (all analytical math) | ~500 MB per module (trained neural networks) | Weight verification protocol — BLAKE3 of checkpoints |
| **Training** | None (reproduction is analytical) | Full model training from scratch | Long-running validation (hours, not seconds) |
| **Chemical structures** | None | SMILES, Morgan fingerprints, molecular graphs | Structural representation handling |
| **GPU requirement** | Optional (Tier 3 dispatch) | Effectively required (training without GPU = weeks) | GPU as Tier 2 requirement (not just Tier 3) |
| **Multi-step pipeline** | Each module is atomic | RCL output → GPS4Drug input → screening → MCTS | Module dependency chains |
| **External API** | NCBI fetch (one-shot) | LINCS, ChEMBL, PubChem, ZINC (complex queries) | Pagination + rate limiting in fetch |
| **Tolerance types** | Absolute/relative (deterministic) | Statistical (R², AUC, correlation) | Statistical tolerance framework |
| **Reproduction time** | Minutes (all modules) | Days-weeks (training from scratch) | Validation timeout / checkpoint resume |

### Predicted Evolution Points

1. **`litho-core::tolerance`** needs statistical tolerance types (R², P-value, AUC, enrichment)
2. **`litho-core::data`** needs streaming/chunked validation for large GCTx files
3. **`litho-core::discovery`** needs GPU as capability (not just dispatch primal)
4. **Module dependency graph** — modules that depend on prior module outputs
5. **Checkpoint resume** — `litho validate --resume` for multi-hour training runs
6. **Model weight provenance** — BLAKE3 chain from training data → weights → predictions

These are capabilities lithoSpore would eventually need anyway. tideGlass forces
them to evolve now, in a real-world niche, under domain expert review.

---

## Three-Tier Architecture (tideGlass Instance)

| Tier | What Runs | Requirements | Provenance |
|------|-----------|--------------|-----------|
| **1 (Python)** | Reference GPS code (cleaned from Zenodo). Runs RCL, GPS4Drug inference, MolSearch. Produces baseline outputs. | Python 3.10+, PyTorch, RDKit | — |
| **2 (Rust/Python)** | Sovereign reimplementation. Initially Python-only with parity checks, then Rust acceleration for scoring/MCTS. Model training stays Python (PyTorch). | Python 3.10+, PyTorch, Rust (for scoring) | BLAKE3 on inputs/outputs |
| **3 (Primal)** | Tier 2 science + NUCLEUS provenance trio + NestGate data fetch + barraCuda GPU dispatch | NUCLEUS running + primals | DAG + spine + braid |

### Why Tier 2 Stays Partially Python

Unlike LTEE where all math can be implemented in pure Rust (curve fitting, statistics),
GPS4Drug's core is a neural network. The neural network doesn't move to Rust — it stays
in Python/PyTorch. What moves to Rust:

- RGES scoring (enrichment statistics — fast, parallelizable)
- MCTS tree search (MolSearch — Rust is natural for tree algorithms)
- Molecular fingerprints (Morgan fingerprints — bit operations)
- Validation harness (all check logic in Rust via litho-core)
- Data loading (GCTx parsing — Rust for speed on 23 GB files)

The "late stage evolution to primals" the user described:
```
Phase 0-2: Pure Python (reproduction + validation)
Phase 3:   Python + Rust scoring (RGES, fingerprints, MCTS in Rust)
Phase 4:   Python (model) + Rust (everything else) = lithoSpore-ready
```

---

## USB Layout (tideGlass Hypogeal Cotyledon)

```
USB (32 GB minimum, 64 GB recommended)
├── .biomeos-spore                      # Spore identity marker
├── validate                            # Entry point (platform-detecting launcher)
├── validate.exe                        # Windows entry point
├── biomeOS/
│   └── tower.toml                      # Ecosystem identity
├── tier1/                              # Python reference
│   ├── requirements.txt                # Pinned deps (pytorch, rdkit, cmapPy, etc.)
│   ├── module1_rges/
│   ├── module2_rcl/
│   ├── module3_prediction/
│   ├── module4_screening/
│   ├── module5_mcts/
│   ├── module6_octad/
│   └── module7_nf/
├── tier2/                              # Rust + Python sovereign
│   ├── tideglass                       # musl-static binary (Linux)
│   ├── tideglass.exe                   # Windows binary
│   ├── models/                         # Trained model weights (BLAKE3-verified)
│   │   ├── rcl_networks.pt
│   │   ├── gps4drug_encoder.pt
│   │   └── gps4drug_predictor.pt
│   └── scoring/                        # Rust-accelerated scoring
│       └── rges_mcts                   # musl-static
├── data/                               # All bundled data (~10 GB)
│   ├── lincs_core/                     # L1000 Level 5 subset (9 core cell lines)
│   ├── chen_2017/                      # RGES validation dataset
│   ├── gps_figures/                    # Figure reproduction data
│   ├── zinc_subset/                    # Screened compound library
│   ├── chembl_rules/                   # MolSearch transformation rules
│   ├── nf_signatures/                  # NF disease signatures
│   └── checksums.blake3               # BLAKE3 manifest
├── validation/
│   ├── expected/                       # 7 module expected outputs
│   └── results/                        # Generated on each run
├── provenance/
│   ├── ferment_transcript.json         # Build provenance
│   ├── paper_chain.toml                # 6 paper validation targets
│   └── braids/                         # Upstream spring braids
├── figures/                            # Publication-quality outputs
├── scope.toml                          # Birth certificate
├── liveSpore.json                      # Deployment history (append-only)
└── README.html                         # Rendered documentation (offline browsable)
```

---

## Validation Targets (What Each Module Proves)

### Module 1: RGES Correlation (Chen 2017)

| Check | Target | Tolerance |
|-------|--------|-----------|
| Pearson r (RGES vs IC50, MCF7) | 0.52 | ±0.05 (stat) |
| P-value | 2.3e-3 | < 0.01 |
| Pyrvinium pamoate in top predictions | True | Boolean |
| 4/4 validated compounds predicted | ≥ 3/4 | Count |

### Module 2: RCL Noise Cleaning (Xing 2026)

| Check | Target | Tolerance |
|-------|--------|-----------|
| VCAP_t1 signal-to-noise improvement | > baseline | Ratio > 1.0 |
| Profile correlation with ground truth | > 0.8 | Pearson r |
| Training convergence | < 100 epochs | Count |

### Module 3: Expression Prediction (Xing 2026)

| Check | Target | Tolerance |
|-------|--------|-----------|
| Held-out R² (structure → expression) | Within 5% of reported | Relative |
| Known drug expression match | Top-10 recovery | Rank |
| Cell-line specificity preserved | Per-line correlation > 0.7 | Pearson r |

### Module 4: Reversal Screening (Xing 2026)

| Check | Target | Tolerance |
|-------|--------|-----------|
| Known HCC actives recovered from ZINC | Enrichment AUC > 0.7 | AUC |
| Top-100 overlap with published screen | > 60% | Percentage |
| Negative controls excluded | < 5% false positive | Rate |

### Module 5: MCTS Optimization (Xing 2026)

| Check | Target | Tolerance |
|-------|--------|-----------|
| HCC lead IC50 improvement | 4μM → ≤ 1μM | IC50 nM |
| Selectivity maintained | Selectivity index > 5 | Ratio |
| Drug-likeness (QED) preserved | > 0.5 | Score |
| Synthetic accessibility (SA) | < 5 | Score |

### Module 6: OCTAD Parity (Zeng 2021)

| Check | Target | Tolerance |
|-------|--------|-----------|
| HCC drug rankings match OCTAD | Spearman ρ > 0.6 | Correlation |
| GPS exceeds OCTAD enrichment | GPS AUC > OCTAD AUC | Comparison |
| Known therapeutics in top-50 | ≥ 3 known drugs | Count |

### Module 7: NF Extension (Novel)

| Check | Target | Tolerance |
|-------|--------|-----------|
| NF1 signature reversal candidates identified | > 0 | Count |
| Known MEK inhibitors in top-100 | Selumetinib ranked | Boolean |
| Anderson geometry modulates ranking | Different ranking with/without | Boolean |
| Cross-validated against NF Data Portal | Overlap with portal compounds | Percentage |

---

## Pseudospore Release Schedule

| Version | Content | Gate |
|---------|---------|------|
| v0.1.0 | Module 1 (RGES) reproduced | Correlation matches within tolerance |
| v0.2.0 | Module 2 (RCL) reproduced | Profile quality improvement confirmed |
| v0.3.0 | Module 3 (GPS4Drug) reproduced | Expression prediction R² within 5% |
| v0.4.0 | Module 4 (screening) reproduced | ZINC enrichment validated |
| v0.5.0 | Module 5 (MolSearch) reproduced | HCC lead optimization confirmed |
| v0.6.0 | Module 6 (OCTAD parity) | GPS exceeds OCTAD baseline |
| v0.7.0 | Module 7 (NF extension) | Novel NF candidates identified |
| v1.0.0 | **Full lithoSpore** | All 7 PASS, USB deploys, self-verifies |

Each pseudoSpore is a milestone deliverable. Each can be handed to Gonzales/Bin Chen.
Each proves progress. The lithoSpore is the terminal artifact — the grad student who
built it left, but the science lives on a USB drive.

---

## What This Tells Us About the Chassis

If lithoSpore is truly domain-agnostic, then `litho-core` should handle tideGlass
with minimal modification. Every modification needed is a **chassis evolution** that
benefits all future deployments.

| If tideGlass needs... | litho-core evolves... | Benefits... |
|----------------------|----------------------|-------------|
| Statistical tolerances | `tolerance::Statistical` (R², P, AUC) | Any ML/stat module |
| Large data streaming | `data::StreamingManifest` | Any genomics/imaging module |
| Module dependencies | `scope::DependencyGraph` | Any multi-step pipeline |
| Model weight verification | `provenance::WeightChain` | Any ML deployment |
| Checkpoint resume | `validation::CheckpointResume` | Any long-running validation |
| Chemical structure handling | `data::MolecularFormat` (SMILES, SDF) | Any chemistry module |

This is the gen5 pattern in action: external niche forces internal evolution
that the ecosystem couldn't have discovered on its own.

---

## Repository Structure (protoKarya/tideGlass)

```
tideGlass/
├── Cargo.toml                    # Workspace (reuses litho-core as dependency)
├── crates/
│   ├── tideglass-rges/           # Module 1: RGES correlation
│   ├── tideglass-rcl/            # Module 2: RCL noise cleaning
│   ├── tideglass-gps4drug/       # Module 3: expression prediction
│   ├── tideglass-screen/         # Module 4: reversal screening
│   ├── tideglass-molsearch/      # Module 5: MCTS optimization
│   ├── tideglass-octad/          # Module 6: OCTAD parity
│   ├── tideglass-nf/             # Module 7: NF extension
│   └── tideglass-cli/            # Unified CLI (reuses litho-core harness)
├── artifact/
│   ├── scope.toml                # Birth certificate (above)
│   ├── data.toml                 # Data manifest (from DATA_MANIFEST.md)
│   └── tolerances.toml           # Named tolerances
├── data/
│   ├── sources/                  # Data source manifests
│   └── targets/                  # Validation targets (quantitative claims)
├── notebooks/                    # Tier 1 Python baselines (7 modules)
├── validation/expected/          # Reference outputs
├── papers/                       # Paper registry (6 DOIs + reading order)
├── lineage/                      # Temporal chain (from LINEAGE.md)
├── provenance/braids/            # Upstream ferment transcript braids
├── figures/                      # Publication-quality outputs
├── profiles/                     # Domain profile (transcriptomic-reversal.toml)
├── pseudospores/                 # Ingested pseudoSpore registry
├── graphs/                       # Tier 3 deploy graphs
├── workloads/                    # NUCLEUS workload TOMLs
├── scripts/                      # Data download, container build
└── docs/                         # Architecture, gaps, niche pressure analysis
```

---

## The Delivery

Andrea Gonzales can hand Bin Chen a USB drive.

On it:
- His platform, rebuilt from scratch
- Every claim in his Cell paper, validated or refuted
- The 20-year chain from Lamb 2006, computationally verified
- An NF extension he hasn't tried yet
- Self-verifying: `./validate` reports PASS/FAIL
- Portable: no Docker, no conda, no internet
- Living: `liveSpore.json` tracks every deployment

That's what `tideGlass` is. The glass shaped by the drift. The instrument
that reads the biological current. Deployed as a lithoSpore into a niche
no one in the ecosystem has inhabited before. Whatever organs it needs to
grow there — those become capabilities for every future deployment.

---

*The LTEE lithoSpore proved the chassis works for microbial evolution.
The tideGlass lithoSpore proves it works for drug discovery. If the same
chassis validates both — from 82,500 bacterial generations to 20 years of
deep learning — then it validates anything. That's the prize.*
