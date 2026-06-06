# tideGlass Viability: GPS Preprint vs Ecosystem Capabilities

**Date**: June 6, 2026
**Status**: Assessment complete — **VIABLE**
**Reuse ratio**: ~70% existing infrastructure, ~30% novel science
**Verdict**: The ecosystem can absorb, revalidate, and redeploy GPS as a lithoSpore

---

## The Preprint's Toolchain (What Bin Chen Lab Used)

The GPS Cell 2026 paper runs on a legacy stack accumulated over 10 years:

| Tool | Role in GPS | Version State |
|------|-------------|---------------|
| **Python 2/3 mixed** | Core logic, data processing | `py27` conda env still required for RCL |
| **PyTorch** | Deep learning (RCL co-training, GPS4Drug encoder/predictor) | Modern, pinned version |
| **RDKit** | Molecular fingerprints, SMILES parsing, descriptors | Modern |
| **scikit-learn** | Baseline ML comparisons, preprocessing | Modern |
| **cmapPy** | Reading GCTx files (L1000 HDF5 format) | Python-only |
| **Fortran** | BLAS/LAPACK via scipy/numpy | Hidden dependency |
| **Docker** | Containerized inference | `binchengroup/gpsimage`, `binchengroup/molsearch` |
| **Flask/Django** | Web portal at `apps.octad.org/GPS/` | Barely alive |
| **ChEMBL REST API** | Compound data queries | Active (EBI) |
| **Hardcoded paths** | Data, environments, outputs | Absolute paths, non-portable |

**Total external dependencies**: ~40+ Python packages, 2 Docker images, 1 web portal,
3 external APIs, 1 Fortran runtime, 2 conda environments.

---

## What We Already Have (Ecosystem Inventory)

### healthSpring — Drug Discovery Track (Track 7, COMPLETE)

| Capability | Function/Module | Checks | Status |
|-----------|----------------|--------|--------|
| Hill dose-response | `hill_dose_response()` | 18 | Rust + WGSL GPU |
| Pathway selectivity | `pathway_selectivity_score()` | 15 | Rust (Exp090) |
| Selectivity index | `selectivity_index()` | 21 | Rust (Exp093) |
| Panel scoring | `score_panel()` with `TissueContext` | 14 | Rust |
| MATRIX scoring | Fajgenbaum framework + Anderson geometry | 15 | Rust (Exp090) |
| ADDRC HTS pipeline | Z'-factor, SSMD, hit scoring | 14 | Rust (Exp091) |
| Batch IC50 | Multi-compound profiling | 14 | Rust (Exp092) |
| ChEMBL JAK panel | Bioactivity fetch + parse + validate | 21 | Rust (Exp093) |
| GPU shaders | 6 WGSL: Hill, diversity, popPK, MM, SCFA, beat | 42 parity | Live |
| Population PK Monte Carlo | 100K virtual patients/second on GPU | — | GPU live |

**Total**: 1,021 Rust tests, 95 experiments, 57 validation scenarios.

### wetSpring — Data Fetch Infrastructure (Active Rust Code)

```rust
// Already wired in barracuda/src/ipc/handlers/data_fetch.rs:
pub fn handle_chembl_fetch(params: &Value) -> Result<Value, RpcError>
pub fn handle_pubchem_fetch(params: &Value) -> Result<Value, RpcError>
// + NCBI E-utilities, NestGate content-addressing, provenance trio
```

Every fetch: session → step → BLAKE3 hash → Merkle root → completion.
tideGlass L1000/GEO ingestion follows this exact pattern.

### barraCuda Primal — GPU Compute

| Resource | Spec | Available |
|----------|------|-----------|
| Titan V (x2) | 12 GB HBM2 each, 5,120 CUDA cores | Yes |
| MI50 (x2) | 16 GB HBM2 each, 3,840 stream processors | Yes |
| RTX 5060 | 16 GB GDDR7 | Yes |
| Total VRAM | 96 GB across 5 GPUs | Yes |
| WGSL dispatch | `toadStool` streaming, `metalForge` multi-device | Operational |

GPS4Drug training on 96 GB distributed VRAM is well within capacity.
RCL co-training (multiple small networks) fits on any single GPU.

### lithoSpore — Deployment Chassis (7/7 PASS)

- `litho-core`: Domain-agnostic (validation, tolerance, provenance, discovery, braid)
- `pseudospore-core`: Format spec (BLAKE3 manifest, braid envelope)
- Three tiers: Python (Tier 1) → Rust (Tier 2) → Primal IPC (Tier 3)
- `litho assemble`: USB assembly pipeline (data + binaries + runtime)
- `litho parity`: Cross-tier validation (Python ↔ Rust math stability)
- 199 unit/integration tests + 10 chaos/fault-injection tests

### projectNUCLEUS — Deployment Infrastructure

- 13/13 primals deployed and healthy, zero debt
- Tower/Node/Nest atomics operational
- NestGate content pipeline: 8 `content.*` methods on 4 transports
- Provenance trio: rhizoCrypt DAG → loamSpine ledger → sweetGrass braid
- `nucleus-deploy spore` — pseudoSpore emission from workloads
- Agent composition (Squirrel `signal_plan` → biomeOS `signal.dispatch`)
- 247 Rust tests (darkforest 140, tunnelKeeper 48, nucleus-deploy 47, nucleus-primals 12)

### projectFOUNDATION — Validation Pipeline

- `foundation-fetch` crate: Source fetching + BLAKE3 hashing
- `foundation-validate` crate: Pipeline execution + structured reporting
- `foundation-publish` crate: Domain profiles + gallery generation
- `nucleus-spore-ingest.toml` workload: Spore ingestion pattern
- Thread linkage: TOML-based lineage tracking across spring contributions

---

## Viability Mapping: GPS Module → Ecosystem Component

### Module 1: RCL (Robust Collaborative Learning)

| GPS Needs | Ecosystem Has | Gap |
|-----------|--------------|-----|
| L1000 GCTx data loading | NestGate fetch pattern | **GCTx parser** (HDF5 streaming) |
| Multi-network PyTorch training | neuralSpring ML patterns | **None** — PyTorch stays |
| GPU for co-training | barraCuda multi-GPU (96 GB VRAM) | **None** — dispatch exists |
| Profile quality metrics | litho-core validation harness | **Statistical tolerances** (R², SNR) |

### Module 2: GPS4Drug (Structure → Expression Prediction)

| GPS Needs | Ecosystem Has | Gap |
|-----------|--------------|-----|
| SMILES → molecular representation | — | **SMILES encoder** (Rust or Python) |
| Morgan fingerprints | — | **Fingerprint generator** (well-specified) |
| Deep learning predictor | neuralSpring patterns | **None** — PyTorch stays |
| Held-out test validation | litho-core `ValidationHarness` | **None** |
| Large compound library handling | NestGate content-addressing | **Streaming** for 750M+ ZINC |

### Module 3: Reversal Screening

| GPS Needs | Ecosystem Has | Gap |
|-----------|--------------|-----|
| RGES enrichment scoring | `score_panel()`, `pathway_selectivity_score()` | **RGES statistic** (KS-like, low effort) |
| Disease signature matching | healthSpring MATRIX | **None** — extends existing |
| Batch scoring on GPU | 6 WGSL shaders, `population_pk_f64.wgsl` pattern | **RGES shader** |
| ChEMBL compound data | `handle_chembl_fetch()` in wetSpring | **None** |
| Anderson tissue geometry | `TissueContext`, validated in Exp090 | **None** |

### Module 4: MolSearch (MCTS Multi-Objective Optimization)

| GPS Needs | Ecosystem Has | Gap |
|-----------|--------------|-----|
| Monte Carlo Tree Search | — | **Rust MCTS** (tree algorithms natural in Rust) |
| ChEMBL transformation rules | — | **SQLite ingestion** (1.5 GB chemblDB3) |
| Multi-objective reward | `selectivity_index()`, `hill_dose_response()` | **Composite reward** (extends existing) |
| Structure enumeration | — | **Chemical move generator** (from rules DB) |
| GPU tree evaluation | barraCuda + toadStool dispatch | **MCTS evaluation shader** |

### Module 5-7: RGES Correlation, OCTAD Parity, NF Extension

These are **validation and application** modules — they compose the above
capabilities, they don't require new infrastructure. They use:
- Existing scoring math
- Existing data fetch
- Existing validation harness
- Existing USB packaging

---

## The Gaps (What Must Be Built)

### Novel (no ecosystem precedent)

| Gap | Difficulty | Spring Owner | Approach |
|-----|-----------|-------------|----------|
| **SMILES parser + Morgan FP** | Medium | healthSpring | Rust crate (algorithm is well-specified: ECFP/Morgan radius 2-4) |
| **GCTx/HDF5 streaming** | Low-Medium | wetSpring | `hdf5-rust` crate exists, add streaming slice access |
| **MCTS in chemical space** | Medium | healthSpring | Rust tree search + SQLite rule lookup |
| **Chemical move generator** | Medium | healthSpring | Enumerate valid chemical transformations from rule DB |

### Extensions (builds on existing patterns)

| Gap | Difficulty | Spring Owner | Approach |
|-----|-----------|-------------|----------|
| **RGES scoring** | Low | healthSpring | KS-like enrichment statistic, extends `score_panel()` |
| **L1000 ingestion** | Low | wetSpring | New NestGate manifest entry, follows existing fetch pattern |
| **Statistical tolerances** | Low | lithoSpore | Add `R²`, `AUC`, `Correlation` to `litho-core::tolerance` |
| **Module dependencies** | Low | lithoSpore | Add `depends_on` field to `scope.toml` `[[module]]` |
| **Model weight provenance** | Low | lithoSpore | BLAKE3 chain on checkpoints, extends existing braid |
| **Checkpoint resume** | Low | lithoSpore | `litho validate --resume` with state file |

### Not Needed (stays in Python)

| Component | Why Not Rust | Validation Strategy |
|-----------|-------------|---------------------|
| GPS4Drug neural network | PyTorch ecosystem, GPU kernels | Tier 1 notebook, harness wraps outputs |
| RCL co-training loop | PyTorch, complex training logic | Tier 1 notebook, validate output quality |
| Model architecture code | Not compute-bound at inference | Python inference, Rust validates results |

---

## The Pattern: Spring Shader → barraCuda Consolidation

**Historical precedent** (what already happened):

```
gen3: healthSpring has inline GPU code → shaders in ecoPrimal/shaders/
gen4: All GPU dispatch consolidated → barraCuda primal owns hardware
now:  Springs call compute.dispatch via IPC → never touch GPU directly
```

**tideGlass follows the same trajectory**:

```
Phase 0-2: Standalone Python/PyTorch (training + inference)
Phase 3:   Python model + Rust scoring → scoring via compute.dispatch
Phase 4:   Full NUCLEUS → tideglass-nf requests screening via IPC
```

Each phase is a pseudoSpore release. Each is a valid stopping point.
The lithoSpore only requires Phase 2 (Python + validation harness).
Phase 3-4 are late-stage primal evolution — the "just as Python and
primals as a late stage evolution" the user described.

---

## Verdict: VIABLE

| Question | Answer |
|----------|--------|
| Can we reproduce the GPS paper? | **Yes** — PyTorch stays, data is public, methods are specified |
| Can we validate claims? | **Yes** — litho-core harness wraps Python outputs |
| Can we extend to NF? | **Yes** — healthSpring MATRIX + Anderson already validated |
| Can we package as lithoSpore? | **Yes** — chassis is domain-agnostic, scope.toml maps directly |
| Can we GPU-accelerate? | **Yes** — 96 GB VRAM, WGSL shader pattern proven, barraCuda dispatch live |
| Can we provenance-track? | **Yes** — trio (DAG + spine + braid) already operational |
| Can we do this without rewriting PyTorch? | **Yes** — Tier 1 notebooks handle NN, Rust handles scoring + validation |
| Does the chassis need modification? | **Minimal** — statistical tolerances + module deps + streaming |
| Is 70% reuse realistic? | **Yes** — infrastructure (fetch, GPU, validate, package, deploy, provenance) all exist |

### Risk Assessment

| Risk | Likelihood | Mitigation |
|------|-----------|-----------|
| GPS code won't run (dead deps) | High | Docker images exist as reference; rebuild from paper methods |
| L1000 data too large for USB | Medium | Core subset (9 cell lines) fits 5 GB; full is 23 GB (64 GB USB) |
| Model training diverges from published | Medium | Compare against their Zenodo figure data; acceptable R² tolerance |
| MCTS rules DB format undocumented | Low | SQLite is self-describing; schema inferable from code |
| Bin Chen disagrees with approach | Low | We validate HIS claims — agreement is finding the same numbers |

---

## Timeline Estimate

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| 0 (Archaeology) | 1-2 weeks | Dependency inventory, data downloaded, code inventoried |
| 1 (Reproduce) | 2-4 weeks | 7 pseudoSpores (one per module as it reproduces) |
| 2 (Validate) | 2-4 weeks | Validation report (discrepancies documented) |
| 3 (Rebuild) | 4-8 weeks | Sovereign Rust scoring + MCTS, Python model training validated |
| 4 (Package) | 2-4 weeks | Full lithoSpore on USB, self-verifying |
| **Total** | ~12-20 weeks | USB drive Andrea can hand to Bin Chen |

This is solo work on biomeGate. Team involvement (math validator, chemist)
shortens Phase 2-3 significantly.

---

## Cross-References

- `gonzales/gps/README.md` — project overview
- `gonzales/gps/LINEAGE.md` — 20-year temporal chain
- `gonzales/gps/DATA_MANIFEST.md` — every file + fetch commands
- `gonzales/gps/LITHO_DESIGN.md` — lithoSpore deployment architecture
- `healthSpring/specs/PAPER_REVIEW_QUEUE.md` — Track 7 (Drug Discovery) complete
- `healthSpring/ecoPrimal/src/discovery/` — existing scoring infrastructure
- `wetSpring/barracuda/src/ipc/handlers/data_fetch.rs` — ChEMBL/PubChem fetch
- `lithoSpore/artifact/scope.toml` — chassis pattern (LTEE instance)
- `projectNUCLEUS/README.md` — deployment infrastructure

---

*The ecosystem didn't evolve for this. It evolved for microbial evolution,
molecular dynamics, pharmacokinetics, environmental chemistry, and game engines.
But the patterns it grew — fetch, validate, score, dispatch, package, deploy —
are general enough to absorb drug discovery transcriptomics. That's what
domain-agnostic infrastructure means: you build it for one niche, and it
works in another. The 70% reuse number isn't optimism. It's architecture.*
