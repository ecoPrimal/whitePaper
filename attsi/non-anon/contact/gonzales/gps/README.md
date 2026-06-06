# GPS Platform — Sovereign Rebuild (`tideGlass`)

**Project name**: `tideGlass` (cross-spring biological current parser)
**Source**: [zenodo.org/records/17653393](https://zenodo.org/records/17653393)
**Paper**: "Deep learning-based screening and design of novel therapeutics that reverse disease-associated transcriptional phenotype"
**Lab**: Bin Chen Lab, Michigan State University
**Assigned by**: Andrea Gonzales (June 5, 2026)
**Introduction to PI**: Gonzales → Bin Chen (offered, pending)
**License**: Apache 2.0 (GitHub) / GPL-3.0 (Zenodo) — discrepancy to resolve
**Zenodo artifact**: 713 MB (v5) / 840 MB (v6)
**GitHub**: [github.com/Bin-Chen-Lab/GPS](https://github.com/Bin-Chen-Lab/GPS)
**Web portal**: [apps.octad.org/GPS/](http://apps.octad.org/GPS/)
**Published**: Cell (2026) — [Full text](https://www.cell.com/cell/fulltext/S0092-8674(26)00223-0)
**Org**: `protoKarya` (first project)
**Platform**: `tideGlass` (GPS rebuild = first lens)
**Status**: Phase 0 — Archaeology

---

## What This Is

The first project of the `protoKarya` GitHub organization. A gen5 product target.

Unlike the gen4 springs (wetSpring, hotSpring, etc.) which evolved internally from
baseCamp experiments, this is an **external scientific codebase assigned by a collaborator**
to be rebuilt as a functional lithoSpore and pseudoSpore. The pattern:

```
gen4 springs: our experiments → validate → elevate to primals → products
gen5 GPS:     their codebase → revalidate → rebuild sovereign → pseudoSpore/lithoSpore
```

**Papers are validation targets. All else is authority. Rebuild from true scratch.**

We do not fork. We do not patch. We do not upgrade Python 2 to 3 and call it done.
We read the methods as a specification, fetch raw data from primary sources, implement
from the mathematics, train from scratch, and compare our outputs against their claims.

This forces novel system evolution the ecosystem would otherwise miss — gene expression
prediction from chemical structures, multi-objective compound optimization, collaborative
noise cleaning. These are capabilities none of the existing springs have.

Gonzales offered to introduce us to Bin Chen (the PI). This is real, directed, functional
work with the domain expert at the end to review. Not a toy. Not a portfolio piece.
Science.

---

## The Platform (Three Modules)

### 1. RCL — Robust Collaborative Learning

**Purpose**: Clean noisy drug-induced gene expression profiles from LINCS/L1000.
**Problem it solves**: LINCS profiles are noisy (batch effects, cell line variance, temporal drift). RCL trains multiple networks that teach each other to ignore noise.
**Technical**: Multi-network co-training with fuzzy membership and forget-rate scheduling.
**Legacy state**: Python 2, specific conda env (`py27`), hardcoded paths.

### 2. GPS4Drug — Structure → Expression → Screening

**Purpose**: Given a chemical structure (SMILES), predict what gene expression changes it induces. Then screen compound libraries for molecules that *reverse* a disease signature.
**Problem it solves**: Traditional screening is experimental (expensive, slow). This predicts expression from structure alone — virtual screen millions of compounds in hours.
**Technical**: Deep learning (chemical structure encoder → expression predictor). Inference on large libraries. Reversal scoring against disease signatures.
**Legacy state**: Mixed Python 2/3, model checkpoints, web portal integration.

### 3. MolSearch — Multi-Objective Compound Optimization

**Purpose**: Given a lead compound, optimize it for multiple objectives simultaneously (potency, selectivity, drug-likeness, synthetic accessibility).
**Problem it solves**: Lead optimization is traditionally iterative medicinal chemistry. MCTS explores chemical space computationally.
**Technical**: Monte Carlo Tree Search with Structure-Gene-Activity Relationships (SGAR). Multi-objective reward function.
**Legacy state**: 518 MB (largest module). Python, likely heavy model weights.

---

## The Rebuild Plan

### Phase 0: Archaeology (Week 1-2)

- [ ] Download full Zenodo artifact (713 MB)
- [ ] Inventory all files, dependencies, environments
- [ ] Map `gps_env.yml` — identify Python 2 vs 3 boundaries
- [ ] Identify Fortran components (if any in the compute chain)
- [ ] Trace data dependencies: what LINCS data, what GEO data, what model weights
- [ ] Read the paper lineage (what does this build on? OCTAD? L1000CDS2?)
- [ ] Document the full dependency graph

### Phase 1: Reproduce (Week 2-4)

- [ ] Stand up RCL on VCAP_t1 (their example case)
- [ ] Match published cleaned expression profiles
- [ ] Stand up GPS4Drug inference
- [ ] Reproduce figure data from `data_for_GPS_figures.zip` (151 MB)
- [ ] Stand up MolSearch
- [ ] Reproduce HCC lead optimization (IC50 4 µM → 0.5 µM claim)
- [ ] Document every reproduction failure and workaround

### Phase 2: Validate (Week 4-6)

- [ ] Cross-validate RCL output against raw LINCS data
- [ ] Validate GPS4Drug predictions against ChEMBL experimental data
- [ ] Validate MolSearch optimization against known SAR
- [ ] Quantify: how much of the claimed performance is real vs artifact of the pipeline?
- [ ] Write validation report (guideStone format: check count, pass/fail, evidence)

### Phase 3: Rebuild Sovereign (Week 6-12)

- [ ] RCL: Python 2 → modern Python (or Rust if performance-critical)
- [ ] GPS4Drug: Clean inference pipeline, remove dead code, sovereign data fetch
- [ ] MolSearch: MCTS in modern framework (potentially Rust for speed)
- [ ] All three: NestGate-compatible data ingestion, BLAKE3 provenance
- [ ] Remove pinned nonsense, eliminate dead environments
- [ ] Test suite: automated checks for every reproduction target

### Phase 4: Package (Week 12+)

- [ ] pseudoSpore: self-verifying artifact with all modules, data, and validation
- [ ] lithoSpore: USB-deployable version (exFAT, platform launchers, HTML output)
- [ ] guideStone modules: one per component (RCL, GPS4Drug, MolSearch)
- [ ] Extend to NF: screen against NF Data Portal transcriptomic signatures
- [ ] Cross-species: Anderson-augmented predictions (tissue geometry modulates reversal)

---

## Why This Is a gen5 Product

| gen4 pattern | gen5 GPS pattern |
|-------------|-----------------|
| Internal experiment drives development | External collaborator assigns the target |
| Validate against published papers | Validate against *their* codebase |
| Build from scratch in Rust | Rebuild from legacy (Python 2 → sovereign) |
| Spring creates the product | Product forces spring evolution |
| Output: validated pipeline | Output: pseudoSpore a PI can hand to a foundation |

The GPS rebuild will force evolution in:

| Area | What GPS Demands | Current State |
|------|-----------------|---------------|
| **Chemical structure encoding** | SMILES → learned representation | Not in any spring |
| **Gene expression prediction** | Structure → expression profile | wetSpring has expression analysis, not prediction |
| **Collaborative noise cleaning** | Multi-network co-training | neuralSpring has ML, not this specific pattern |
| **MCTS for chemistry** | Tree search in chemical space | Not in any spring |
| **LINCS L1000 ingestion** | 1.3M drug perturbation profiles | Not in PUBLIC_DATA_SYSTEMS.md yet |
| **Reversal scoring** | Disease signature → reverse screen | healthSpring has MATRIX, not reversal scoring |

Every one of these is a capability gap that the ecosystem would not have discovered without an external collaborator's codebase forcing the issue. This is gen5 working as designed.

---

## Data Dependencies

| Dataset | Role in GPS | Scale | Access | Trust Tier |
|---------|-------------|-------|--------|-----------|
| **LINCS L1000** | Drug perturbation signatures (core training data) | 1.3M profiles, ~50 GB | clue.io (free) | T1 — NIH-funded instrument data |
| **GEO disease signatures** | Disease expression targets for reversal scoring | Variable per disease | NCBI GEO (free) | T1 — depositor data |
| **ChEMBL** | Compound structures + activity (validation) | 2.4M compounds | EBI (free) | T2 — curated |
| **PubChem** | Compound structures (screening libraries) | 115M+ | NCBI (free) | T1 — depositor |
| **ZINC** | Purchasable compound library | 750M+ | zinc.docking.org | T1 — computed |
| **DrugBank** | Approved drug profiles | 14K+ | drugbank.com (academic free) | T2 — curated |
| **NF Data Portal** | NF disease signatures (extension target) | 108M data points | nf.synapse.org | T2 — curated |
| **TCGA** | Pan-cancer expression (NF1 subset) | 9,125 samples | GDC | T1/T2 mixed |

### Data to add to PUBLIC_DATA_SYSTEMS.md

- **LINCS L1000** (clue.io) — 1.3M drug perturbation profiles. T1. Critical for GPS.
- **ZINC** (zinc.docking.org) — 750M+ purchasable compounds. T1. Screening library.
- **OCTAD** (octad.org) — Open Cancer TherApeutic Discovery. T2. GPS predecessor/data source.

---

## The 10-Year Lineage

Andrea mentioned this represents 10+ years of work. The paper trail likely includes:

1. **OCTAD** (Open Cancer TherApeutic Discovery) — earlier platform from same lab
2. **L1000CDS2** (LINCS Cloud-based Drug Signature Search) — Ma'ayan Lab, precursor concept
3. **Connectivity Map** (Broad Institute) — original reversal hypothesis (Lamb et al. 2006)
4. **LINCS program** (NIH Common Fund, 2010-2020) — generated the perturbation data
5. **GPS manuscript chain** — likely multiple earlier versions, preprints, conference papers

Tracing this lineage is part of Phase 0. The rebuild doesn't just reproduce the latest code — it validates the intellectual chain that produced it.

---

## Connection to Ecosystem Products

```
GPS4Drug (expression prediction)
    → healthSpring MATRIX (drug repurposing scoring)
    → Anderson geometry (tissue-specific propagation)
    = Three complementary angles on drug repurposing

GPS4Drug screens: "This compound reverses NF signature"
MATRIX scores:    "This compound has pathway + geometry match for NF"
Anderson predicts: "In nerve sheath tissue (d_eff=2.4), the drug signal reaches targets"

All three agree → high-confidence candidate for validation
Any one disagrees → investigate why (could reveal biology)
```

---

## The lithoSpore / pseudoSpore Vision

The GPS lithoSpore is a USB drive Andrea can hand to:
- A foundation reviewer (CTF NDU) — "Here's the drug screening platform, it validates itself"
- A grad student — "Type `./validate`, see what passes, then screen your disease"
- A collaborator at another institution — "No environment setup, no dead dependencies"

The GPS pseudoSpore ships after every significant milestone:
- v0.1: RCL reproduced, expression profiles match
- v0.2: GPS4Drug inference reproduced, screening validated
- v0.3: MolSearch reproduced, HCC lead optimization confirmed
- v1.0: Full sovereign rebuild, NF extension, cross-species Anderson augmentation

Each version self-verifies. Each version is a concrete demonstration of progress.

---

## Cross-References

- `gonzales/gps/LINEAGE.md` — **full temporal chain**, papers, data, code repos, validation targets
- `gonzales/gps/DATA_MANIFEST.md` — every file, source, hash, download instruction
- `gonzales/README.md` — meeting outcomes, relationship arc
- `gen5/collaborators/GONZALES_NF.md` — gen5 collaborator status
- `gen5/products/NF_CASE_STUDY.md` — how GPS feeds the NF product composition
- `gen5/foundations/PUBLIC_DATA_SYSTEMS.md` — data systems catalog (LINCS, ZINC, OCTAD added)
- `ABG/ABG_discord_gps_june2026.md` — Discord post connecting GPS to ABG interests
- `gonzales/onboarding/PRE_GRANT_PIPELINE.md` — GPS as pre-grant engine
- `hotSpring control/gromacs_fel/` — analogous rebuild pattern (GROMACS + PLUMED parity)
- `wetSpring experiments/` — analogous reproduction pattern (380+ experiments)

---

## Project Structure (this folder)

```
gonzales/gps/
├── README.md          ← you are here (overview + rebuild plan)
├── LINEAGE.md         ← 20-year temporal chain, all papers, all data, all code
├── DATA_MANIFEST.md   ← download manifest with hashes and fetch commands
├── phase0/            ← (future) archaeology notes, dependency inventory
├── phase1/            ← (future) reproduction logs, match/fail records
├── phase2/            ← (future) validation reports, guideStone checks
├── phase3/            ← (future) sovereign rebuild source (→ protoKarya repo)
└── phase4/            ← (future) lithoSpore packaging, pseudoSpore releases
```

---

*10 years of work. Python 2. Fortran. Pinned nonsense. A web portal barely alive. The grad students left. The code is dying. But the science is real — published in Cell, validated in mice, 20 years of chain behind it. We bring it back as science that runs. That's what protoKarya does.*
