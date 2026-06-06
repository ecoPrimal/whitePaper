# tideGlass — Temporal Lineage & Validation Chain

**Platform**: `tideGlass` (cross-spring biological current parser)
**First lens**: GPS rebuild (transcriptomic reversal)
**First project of**: `protoKarya` (GitHub org, sporeGarden gen5)
**Rebuild philosophy**: Papers are validation targets. All else is authority. Rebuild from true scratch.
**Domain expert review**: Bin Chen (PI, MSU) — introduction via Andrea Gonzales
**Spring target**: healthSpring (new spring-level validation team in time)
**Terminal artifact**: NUCLEUS lithoSpore (self-verifying, USB-deployable, portable)

---

## The 20-Year Chain

The GPS platform did not appear from nothing. It sits at the end of a 20-year intellectual
chain, each link building on the last. We treat every paper in this chain as a
**validation target** — not as truth, but as a claim to reproduce or refute.

```
2006 ━━━ THE HYPOTHESIS
│
│   Lamb et al. "The Connectivity Map"
│   Science 313(5795):1929-1935
│   DOI: 10.1126/science.1132939
│
│   Claim: If a drug induces gene expression OPPOSITE to a disease
│   signature, that drug is a therapeutic candidate.
│   Scale: 164 compounds × 3 cell lines (MCF7, PC3, HL60)
│   Method: Pattern matching (KS-like enrichment scoring)
│   Validation: HDAC inhibitors cluster, gedunin→HSP90, sirolimus→dexamethasone
│
│   STATUS: Foundational hypothesis. Still holds. GPS extends it from
│   matching known drugs to PREDICTING unknown compounds.
│
2010 ━━━ THE DATA PROGRAM
│
│   NIH LINCS Program (Library of Integrated Network-based Cellular Signatures)
│   Common Fund, 2010-2020, ~$150M total investment
│   6 Data & Signature Generation Centers + 1 Coordination Center
│
│   Goal: 1000× scale-up of CMap
│   Technology: L1000 assay (Luminex bead, 978 landmark genes, $2/sample)
│   Output: 3,000,000+ profiles by program end
│
│   STATUS: Program complete. Data is PUBLIC. This is our primary source.
│
2016 ━━━ THE SEARCH ENGINE
│
│   Duan et al. "L1000CDS2: LINCS L1000 characteristic direction
│   signatures search engine"
│   npj Systems Biology and Applications 2:16015
│   DOI: 10.1038/npjsba.2016.15
│   Lab: Avi Ma'ayan, Mount Sinai
│
│   Claim: Characteristic Direction method improves signal/noise over MODZ.
│   Scale: 22,000+ signatures searched in <4 seconds
│   Innovation: Cosine similarity search, drug target prediction from signatures
│   Applied: 670 disease signatures screened, 22 endogenous ligands matched
│   Portal: https://maayanlab.cloud/L1000CDS2/
│
│   STATUS: Still running. GPS supersedes this with learned prediction
│   (predicts expression from structure, rather than just searching existing).
│
2017 ━━━ THE METRIC
│
│   Chen et al. "Reversal of cancer gene expression correlates with
│   drug efficacy and reveals therapeutic targets"
│   Nature Communications 8:16022
│   DOI: 10.1038/ncomms16022
│   Lab: Bin Chen, UCSF (Atul Butte Lab)
│
│   Claim: RGES (Reversal Gene Expression Score) correlates with IC50.
│   Scale: 66,000 compound profiles × 12M activity measurements
│   Data: LINCS L1000 + ChEMBL + CCLE + TCGA
│   Validation: 4 novel liver cancer compounds predicted and validated in vitro.
│   Pyrvinium pamoate validated in vivo (xenograft mouse model).
│   Code: github.com/Bin-Chen-Lab/RGES
│
│   STATUS: THIS IS THE DIRECT INTELLECTUAL ANCESTOR OF GPS.
│   The RGES paper proves the reversal correlation. GPS extends it by
│   PREDICTING what a compound's expression signature would be, without
│   ever having measured it.
│
│   VALIDATION TARGET: Reproduce RGES correlation (r=0.52, P=2.3×10⁻³
│   in MCF7). Reproduce pyrvinium pamoate prediction.
│
2017 ━━━ THE DATASET
│
│   Subramanian et al. "A Next Generation Connectivity Map: L1000
│   Platform and the First 1,000,000 Profiles"
│   Cell 171(6):1437-1452.e17
│   DOI: 10.1016/j.cell.2017.10.049
│   Lab: Todd Golub / Aravind Subramanian, Broad Institute
│
│   Scale: 1,319,138 L1000 profiles
│   Perturbagens: 42,080 (19,811 compounds, 18,493 shRNAs, 3,462 cDNAs, 314 biologics)
│   Signatures: 473,647 (after replicate consolidation)
│   Cell lines: 77 (9 core cancer lines in "Touchstone" reference)
│   GEO: GSE92742 (Phase 1) + GSE70138 (Phase 2, ongoing through 2020)
│
│   STATUS: This IS the training data for GPS. All public. All fetchable.
│
2021 ━━━ THE PLATFORM PREDECESSOR
│
│   Zeng et al. "OCTAD: an open workspace for virtually screening
│   therapeutics targeting precise cancer patient groups using gene
│   expression features"
│   Nature Protocols 16:728-753
│   DOI: 10.1038/s41596-020-00430-z
│   Lab: Bin Chen, Michigan State University
│
│   Scale: 19,127 patient samples × 50+ cancer types × 12,442 compounds
│   Innovation: Deep-learning reference tissue selection, R/Bioconductor package
│   Code: github.com/Bin-Chen-Lab/octad (R, Bioconductor)
│   Portal: http://octad.org
│   Method: Signature creation → drug reversal scoring → in silico validation
│
│   STATUS: GPS is the SUCCESSOR. OCTAD does repurposing (search existing drugs).
│   GPS does discovery (predict NEW compounds). Same lab, same philosophy,
│   fundamentally more powerful.
│
│   VALIDATION TARGET: Reproduce OCTAD's HCC repurposing results as
│   baseline before showing GPS exceeds them.
│
2016→2026 ━━━ GPS DEVELOPMENT (10 YEARS)
│
│   Bin Chen LinkedIn post (2026):
│   "March 2016, AlphaGo defeated Lee Sedol in Go... from day one...
│    3 years validation → 1 year submission. A long [road]... made it."
│
│   Development timeline:
│   2016: Project initiated after AlphaGo (deep learning is ready)
│   2016-2019: RCL development (collaborative noise cleaning)
│   2019-2022: GPS4Drug core model (structure → expression)
│   2022-2024: MolSearch development (illidanlab, Jiayu Zhou)
│   2023-2025: HCC + IPF experimental validation (3 years)
│   2025 Nov: Zenodo v5 deposit (712.7 MB)
│   2026: Published in Cell
│
│   Team: Jing Xing (lead), Mingdian Tan, Dmitry Leshchiner,
│   Mengying Sun, Mohamed Abdelgied
│   Supervised by: Jiayu Zhou, Mei-Sze Chua, Xiaopeng Li
│   Institutions: MSU, UMich, Stanford, Corewell Health
│   Dedicated to: Atul Butte (Chen's late mentor, UCSF)
│
2025 ━━━ THE DEPOSIT
│
│   Zenodo Record 17653393 (v5, November 2025)
│   Total: 712.7 MB
│   License: Apache 2.0 (per GitHub), GPL-3.0 (per Zenodo — discrepancy to resolve)
│
│   Updated: Zenodo Record 17956238 (v6, with figure_code.zip)
│   Total: 840.3 MB
│
2026 ━━━ THE PUBLICATION
│
│   Xing et al. "Deep-learning-based de novo discovery and design of
│   therapeutics that reverse disease-associated transcriptional phenotypes"
│   Cell (2026)
│   DOI: 10.1016/j.cell.2026.02.023 (S0092-8674(26)00223-0)
│
│   Three modules:
│   1. RCL — Robust Collaborative Learning (noise cleaning)
│   2. GPS4Drug — Structure → Expression → Screening
│   3. MolSearch — Multi-Objective Compound Optimization (MCTS)
│
│   Validated in:
│   - HCC (hepatocellular carcinoma): designed compound, IC50 0.5 µM
│   - IPF (idiopathic pulmonary fibrosis): repurposing + novel compounds
│   - Single-cell: reversal across multiple cell types
│
│   VALIDATION TARGETS (from the paper):
│   - RCL improves VCAP profile quality (measured vs baseline)
│   - GPS4Drug predicts expression from structure (R² against held-out)
│   - Screening recovers known actives from ZINC (enrichment)
│   - MolSearch optimizes HCC lead (IC50 4 µM → 0.5 µM, selectivity maintained)
│   - IPF reversal score predicts efficacy
│
2026 Jun ━━━ THE ASSIGNMENT
│
│   Andrea Gonzales assigns rebuild to sporeGarden ecosystem.
│   Offers introduction to Bin Chen (PI).
│   Target: Sovereign rebuild → pseudoSpore → lithoSpore
│   Extension: NF disease signatures (neurofibromatosis)
│   Org: protoKarya (first project)
```

---

## Code Repositories (Complete Map)

| Repo | Language | Created | Last Push | Role | Rebuild Status |
|------|----------|---------|-----------|------|---------------|
| `Bin-Chen-Lab/RGES` | R | ~2017 | — | Original RGES method | Validation target only |
| `Bin-Chen-Lab/octad` | R | Oct 2017 | Mar 2026 | Cancer repurposing platform | Validation target only |
| `Bin-Chen-Lab/GPS` | Python 2/3 | ~2023 | 2026 | Full GPS platform | **PRIMARY REBUILD TARGET** |
| `illidanlab/MolSearch` | Python | ~2022 | — | MCTS optimization (Jiayu Zhou) | MolSearch component source |
| Docker: `binchengroup/gpsimage` | — | — | — | GPS4Drugs container | Reference (black box) |
| Docker: `binchengroup/molsearch` | — | — | — | MolSearch container | Reference (black box) |

### The Docker Problem

They containerized it. That's not sovereignty — that's freezing the mess. A Docker image
"works" but:
- You can't verify what it does
- You can't extend it
- You can't run it without Docker
- You can't hand it to a reviewer who doesn't have Docker
- The pinned dependencies will rot (already have — Python 2)

The lithoSpore replaces this pattern entirely.

---

## Data Inventory (Full Manifest)

### Tier 1: Required for Reproduction

| Source | Dataset | GEO/URL | Size | Format | What GPS Uses It For |
|--------|---------|---------|------|--------|---------------------|
| **Broad/LINCS** | L1000 Level 5, Phase 1 | GSE92742 | **23 GB** | GCTx | Training data (473,647 signatures × 12,328 genes) |
| **Broad/LINCS** | L1000 Level 5, Phase 2 | GSE70138 | **5 GB** | GCTx | Extended training (118,050 signatures) |
| **Zenodo** | GPS artifact v5 | 17653393 | **713 MB** | ZIP | Code + models + figure data |
| **Zenodo** | GPS artifact v6 | 17956238 | **840 MB** | ZIP | + figure reproduction code |
| **Figshare** | ChEMBL transformation rules | chemblDB3.sqlitdb | **1.5 GB** | SQLite | MolSearch reaction templates |
| **ZINC** | Screened compound subset | zinc.docking.org | **~5 GB** | SMILES/SDF | Virtual screening library |

**Tier 1 Total: ~35 GB**

### Tier 2: Required for Full Validation

| Source | Dataset | URL | Size | Format | Purpose |
|--------|---------|-----|------|--------|---------|
| **Bioconductor** | OCTAD database | octad.counts.and.tpm.h5 | **~6 GB** | HDF5 | 19,127 patient samples for cross-validation |
| **ChEMBL** | Activity database | chembl.gitbook.io | **~3 GB** | SQLite/PostgreSQL | Compound activity validation |
| **TCGA** | HCC + IPF expression | GDC portal | **~2 GB** | TSV/HDF5 | Disease signature validation |
| **CCLE** | Cancer cell line profiles | DepMap portal | **~1 GB** | CSV | Cell line mapping |
| **Enamine** | HTS compound library | enamine.net | **~2 GB** | SMILES | Extended screening |

**Tier 2 Total: ~14 GB**

### Tier 3: Full Archaeology (Ground Truth Revalidation)

| Source | Dataset | GEO | Size | Format | Purpose |
|--------|---------|-----|------|--------|---------|
| **Broad/LINCS** | L1000 Level 1 (raw) | GSE70138 | **223 GB** | LXB (binary) | Raw fluorescence — proves Level 5 is correct |
| **Broad/LINCS** | L1000 Level 2 (expression) | GSE92742 | **~15 GB** | GCTx | Pre-normalization expression |
| **Broad/LINCS** | L1000 Level 3 (inferred) | GSE92742 | **~30 GB** | GCTx | Full 12,328 gene inference |

**Tier 3 Total: ~268 GB**

### Storage Budget

| What | Size | Media |
|------|------|-------|
| Tier 1 (reproduction) | 35 GB | Any USB 64 GB |
| Tier 1 + 2 (full validation) | 49 GB | USB 64 GB (tight) or 128 GB |
| Tier 1 + 2 + 3 (archaeology) | 317 GB | USB 512 GB or NVMe |
| + NF Extension data | +5 GB | NF Data Portal signatures |
| **biomeGate working space** | **~500 GB** | NVMe array (have it) |

The user has confirmed: room for the data. biomeGate (256 GB RAM, 96 GB VRAM) handles
all compute. No cloud dependency.

---

## Papers as Validation Targets

We do NOT read papers as truth. We read them as **claims to reproduce or refute**.

### Paper 1: Lamb 2006 (CMap)

| Claim | How We Validate | Pass Criterion |
|-------|----------------|----------------|
| HDAC inhibitors cluster by expression | Reproduce clustering on L1000 | Same grouping with updated data |
| Gedunin is HSP90 inhibitor | Check mechanism literature | Confirmed by others since 2006 |
| Negative connectivity = therapeutic | Statistical test on known drug-disease pairs | Enrichment above random |

### Paper 2: Chen 2017 (RGES)

| Claim | How We Validate | Pass Criterion |
|-------|----------------|----------------|
| RGES correlates with IC50 | Reproduce correlation analysis | r ≥ 0.4, P < 0.01 (they report r=0.52) |
| 4 predicted HCC compounds active | Check ChEMBL/PubChem for confirmation | At least 3/4 confirmed |
| Pyrvinium pamoate shrinks xenografts | Literature confirmation | Published in vivo validation |
| Landmark genes outperform full genome | Reproduce comparison | Confirm or refute |

### Paper 3: Zeng 2021 (OCTAD)

| Claim | How We Validate | Pass Criterion |
|-------|----------------|----------------|
| Deep learning selects better reference tissue | Reproduce tissue selection for HCC | Match or exceed manual selection |
| sRGES pipeline produces actionable hits | Run OCTAD R package on HCC | Same top compounds ± noise |
| 19,127 samples cover 50+ cancer types | Verify against TCGA/GEO counts | Confirm sample provenance |

### Paper 4: Xing 2026 (GPS)

| Claim | How We Validate | Pass Criterion |
|-------|----------------|----------------|
| RCL improves profile quality | Reproduce VCAP_t1 cleaning | Measured signal/noise improvement |
| GPS4Drug predicts expression from structure | Held-out test set correlation | R² within 5% of reported |
| ZINC screening recovers known actives | Reproduce enrichment analysis | AUC within 10% of reported |
| HCC compound design (IC50 0.5 µM) | Chemical feasibility check + literature | Structure is synthesizable, IC50 plausible |
| IPF reversal across cell types | Reproduce single-cell analysis | Same cell populations respond |
| MolSearch improves multiple objectives | Reproduce MCTS on HCC lead | Pareto front matches or extends |

---

## The protoKarya Org

`protoKarya` is the GitHub organization for gen5 external-facing validated science.

| Property | Value |
|----------|-------|
| Org name | `protoKarya` |
| Platform | `tideGlass` — cross-spring biological current parser |
| First lens | GPS Sovereign Rebuild (transcriptomic reversal) |
| License | AGPL-3.0 (code) + CC-BY-SA (documentation) |
| Relationship to sporeGarden | External publication face of validated gen5 products |
| Team model | Start solo → spring-level math validation team → full NUCLEUS |

### What Is tideGlass

The motion is the reality. The tool is what parses it.

Every spring has a biological current — gene expression flowing, proteins folding,
communities shifting, drugs distributing. `tideGlass` is the instrument that reads
any of these currents. The GPS rebuild is the first lens ground into the glass
(transcriptomic flow → reversal compounds). Future lenses:

| Lens | Current Parsed | Spring |
|------|---------------|--------|
| GPS rebuild | Transcriptomic perturbation flow | healthSpring |
| PK/PD flow | Drug concentration dynamics | healthSpring |
| Community dynamics | Microbial population shifts | wetSpring |
| Conformational space | Protein folding trajectories | hotSpring |
| Contaminant transport | PFAS/chemical migration | groundSpring |
| Environmental time series | Atmospheric/hydrological flow | airSpring |

The glass is shaped by the drift. The current trains the model that reads the current.

### Why a New Org

- `sporeGarden` is the internal ecosystem (primals, springs, infrastructure)
- `protoKarya` is where validated science goes public
- Separation means: a reviewer sees clean, reproducible science — not infrastructure complexity
- Bin Chen sees: a competent rebuild of his platform, not our internal tooling
- Grant reviewers see: a portfolio of validated computational work

### The Team Evolution

```
Phase 0 (now):        Solo. Archaeology + reproduction.
Phase 1 (months):     Spring-level validation. One mathematician for RCL proofs.
Phase 2 (6-12 mo):    Full team. Chemist for MolSearch SAR. Biologist for NF extension.
Phase 3 (lithoSpore): NUCLEUS packaging. USB-deployable. Foundation-ready.
```

---

## Rebuild Philosophy

### What "From True Scratch" Means

We do NOT:
- Fork their repo and fix bugs
- Upgrade Python 2 → 3 and call it done
- Trust their model weights without reproducing training
- Accept their Docker images as working

We DO:
- Read the paper's methods section as a specification
- Download raw data from primary sources (GEO, not Zenodo)
- Implement each algorithm from the mathematical description
- Train models from scratch on verified data
- Compare our outputs against their published results
- Document every discrepancy (theirs could be wrong too)
- Package the validated result as a self-verifying pseudoSpore

### The Authority Model

```
AUTHORITY (what we trust to start):
├── L1000 raw data (NIH instrument output, T1)
├── ChEMBL measured activities (depositor data, T1)
├── TCGA patient expression (depositor data, T1)
├── Chemical structure databases (ZINC, PubChem — computed/depositor, T1)
└── Published IC50 measurements (experimental, T1)

VALIDATION TARGETS (what we reproduce):
├── Lamb 2006 — reversal hypothesis (proven by 20 years of follow-up)
├── Chen 2017 — RGES correlation (reproduce the statistic)
├── Zeng 2021 — OCTAD pipeline (reproduce drug rankings)
└── Xing 2026 — GPS predictions (reproduce all claims)

REBUILD OUTPUTS (what we produce):
├── Cleaned L1000 profiles (via our RCL implementation)
├── Trained GPS model (from scratch, on verified data)
├── Screening results (ZINC library, NF extension)
├── Validation reports (guideStone format)
└── lithoSpore (self-verifying USB artifact)
```

### Why This Works With Bin Chen

Gonzales offered the introduction. What Bin Chen sees:

1. Someone who READ his paper chain back to 2006
2. Someone who REPRODUCED his results independently
3. Someone who found and documented where the code was dying
4. Someone who made it portable and self-verifying
5. Someone who extended it to NF (a disease he hasn't targeted yet)

This isn't criticism of his work — it's the highest form of engagement. We validate,
we extend, we make it immortal. A PI whose platform becomes a verified lithoSpore
has something no grant can buy: proof that the work was real enough to survive
independent reconstruction.

---

## Connection to NF (The Extension)

After validating GPS on its published targets (HCC, IPF), the extension:

1. **Fetch NF disease signatures** from NF Data Portal (Synapse)
2. **Compute RGES** for all LINCS-profiled compounds against NF signatures
3. **Screen ZINC** with GPS4Drug for novel NF reversal candidates
4. **Optimize leads** with MolSearch (target NF1-specific objectives)
5. **Cross-reference** with Anderson geometry (nerve sheath tissue, d_eff=2.4)
6. **Validate** against known NF therapeutics (MEK inhibitors, selumetinib)

This connects directly to the CTF NDU grant target and Andrea's domain expertise.

---

## File Checksums (Verification Anchors)

These are the MD5 hashes from Zenodo. Our rebuild verifies against these, then
produces BLAKE3 hashes for the pseudoSpore chain.

```
# Zenodo v5 (record 17653393)
c612db1387b1375fe6f395da9139f631  [file 1]
4e0aa3c27edb952f9ecc0f0ddf0179a1  [file 2]
73be3c9c3b86a20bcecb059fde9f2fa5  [file 3]
86d3f3a95c324c9479bd8986968f4327  [file 4]
30744d7dcc70490f79a1ce16ff5162de  [file 5]
4b04fc59f0e1ef57c3f24ba8e4891207  [file 6]
a9f1c26b77220fcb9590a06e23c72777  [file 7]

# Zenodo v6 (record 17956238) — adds figure_code.zip
0a85c5a760c2ddca3cd1860cbaa57369  [file 1]
65fc67c7865db46ea4b1ea3d26aaa684  [file 2]
73be3c9c3b86a20bcecb059fde9f2fa5  [file 3 — same as v5]
86d3f3a95c324c9479bd8986968f4327  [file 4 — same as v5]
a48077c310d8608200c3dae693c15eca  [file 5]
0c2f5ae5fd0088bae456e97983d69a35  [file 6]
a9f1c26b77220fcb9590a06e23c72777  [file 7 — same as v5]
```

File-to-hash mapping will be resolved during Phase 0 download.

---

## Links (Complete)

### Papers
- [Lamb 2006 — Connectivity Map](https://doi.org/10.1126/science.1132939) | [PDF](https://assets.clue.io/Lamb_2006.pdf)
- [Duan 2016 — L1000CDS2](https://doi.org/10.1038/npjsba.2016.15)
- [Subramanian 2017 — L1000 Platform](https://doi.org/10.1016/j.cell.2017.10.049)
- [Chen 2017 — RGES](https://doi.org/10.1038/ncomms16022)
- [Zeng 2021 — OCTAD](https://doi.org/10.1038/s41596-020-00430-z)
- [Xing 2026 — GPS](https://www.cell.com/cell/fulltext/S0092-8674(26)00223-0)

### Data
- [LINCS L1000 Phase 1 (GSE92742)](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742)
- [LINCS L1000 Phase 2 (GSE70138)](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE70138)
- [CLUE Portal](https://clue.io)
- [GPS Zenodo v5](https://zenodo.org/records/17653393)
- [GPS Zenodo v6](https://zenodo.org/records/17956238)
- [OCTAD Database](https://experimenthub.bioconductor.org/fetch/7327)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)
- [ZINC](https://zinc.docking.org)
- [NF Data Portal](https://nf.synapse.org)
- [TCGA GDC](https://portal.gdc.cancer.gov)

### Code
- [GPS GitHub](https://github.com/Bin-Chen-Lab/GPS)
- [OCTAD GitHub](https://github.com/Bin-Chen-Lab/octad)
- [RGES GitHub](https://github.com/Bin-Chen-Lab/RGES)
- [MolSearch GitHub](https://github.com/illidanlab/MolSearch)
- [GPS4Drugs Docker](https://hub.docker.com/repository/docker/binchengroup/gpsimage)
- [MolSearch Docker](https://hub.docker.com/repository/docker/binchengroup/molsearch)

### Portals
- [GPS Web Portal](http://apps.octad.org/GPS/)
- [OCTAD Web Portal](http://octad.org)
- [L1000CDS2](https://maayanlab.cloud/L1000CDS2/)
- [L1000FWD](https://maayanlab.cloud/L1000FWD/)
- [SigCom LINCS](https://maayanlab.cloud/sigcom-lincs/)

---

*The grad students who built this are gone. The Python 2 environments are rotting.
The Docker images are black boxes. The web portal runs on a server someone will
eventually turn off. But the science is real — 20 years of it, validated in mice,
published in Cell. We take the science. We verify it. We make it immortal.
That's what protoKarya does.*
