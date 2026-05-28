# NF Case Study — First Multi-Product Composition for External Science

**The Gonzales Neurofibromatosis Data Mining Project as gen5 Proof Case**

**Date**: May 28, 2026
**Author**: Kevin Mok (BS Microbiology, MSU 2018; MS Data Science, MSU 2025)
**Status**: Engaged — meeting scheduled, product composition mapped
**License**: scyBorg triple — AGPL-3.0-or-later (code), ORC (system mechanics), CC-BY-SA 4.0 (this document)
**Lineage**: gen3/baseCamp (wetSpring, healthSpring, neuralSpring) → gen4/products (helixVision, initioChem, blueFish) → gen5 (this document)

---

## Why This Project Matters

The NF data mining project is not one product solving one problem. It is the first instance where multiple gen4 products compose to serve an external domain expert's scientific question — and the deliverable is her science, not an infrastructure demo.

This makes it the gen5 proof case: the moment the ecosystem demonstrates that someone else's science comes out the other end.

---

## The Biological Question

### Neurofibromatosis Type 1 (NF1)

NF1 is caused by loss-of-function mutations in the NF1 gene, which encodes neurofibromin — a RAS-GAP (GTPase-activating protein). Loss of neurofibromin means hyperactive RAS/MAPK signaling, driving tumor formation: neurofibromas (benign), plexiform neurofibromas (can transform), and malignant peripheral nerve sheath tumors (MPNST).

### The JAK/STAT Connection

Andrea Gonzales already studies JAK/STAT signaling through her oclacitinib work (782/782 checks across G1-G6, wetSpring Exp 273-286). NF1 tumors exhibit hyperactivated STAT3. This is not a domain shift — it is the same signaling biology extended to a rare disease:

| Her Published Work | NF Extension |
|-------------------|--------------|
| Oclacitinib JAK1 selectivity (G2, G5) | JAK/STAT hyperactivation in NF1 tumors |
| IL-31 dose-response (G1) | Cytokine signaling in neurofibroma microenvironment |
| Three-compartment model: immune/skin/neural (G6) | NF1 affects all three compartments |
| Anderson localization of cytokine propagation | RAS/MAPK propagation through NF1 tissue geometry |

The Fajgenbaum MATRIX with Anderson geometry extension applies directly to NF drug repurposing.

### Key Pathways

- **RAS/MAPK**: Primary driver. NF1 loss → hyperactive RAS → uncontrolled proliferation. MEK inhibitors (selumetinib, trametinib) are current therapeutic focus.
- **JAK/STAT**: Secondary/connected. STAT3 hyperactivation in NF tumors. JAK inhibitors may have synergistic potential.
- **PI3K/mTOR**: Cross-talk with RAS. mTOR inhibitors (rapamycin, everolimus) under investigation.

---

## Data Sources

### NF Data Portal (Synapse)

The Children's Tumor Foundation (CTF) NF Data Portal on Synapse.org hosts curated datasets for neurofibromatosis research:

- Gene expression datasets (bulk RNA-seq, single-cell)
- Genomic variants (WGS/WES of NF1 tumors)
- Drug screening data (compound libraries against NF cell lines)
- Clinical data (de-identified patient records)

### Pluto.bio NF Datasets

~108M data points across 12 datasets — gene expression, drug response, pathway analysis. Publicly browsable.

### Compound Data

- **PubChem / ChEMBL**: Compound activity data for RAS/MAPK and JAK/STAT targets
- **ADDRC 8K compound library**: Direct screening access through Lisabeth/MSU Drug Discovery Program
- **DrugBank**: Approved drug profiles for repurposing candidates

---

## Product Composition

This is the first project requiring multiple gen4 products working together. No single product is sufficient.

### helixVision — Gene Expression Analysis

**Role**: Primary genomics pipeline for NF data mining.

- Ingest NF Data Portal gene expression datasets (bulk + single-cell)
- Differential expression analysis: NF1 tumor vs. normal tissue
- Pathway enrichment: RAS/MAPK, JAK/STAT, PI3K/mTOR
- Community profiling of tumor microenvironment
- ESN anomaly detection for outlier identification

**Springs consumed**: wetSpring (6,656+ checks), neuralSpring/coralForge (154 checks)

### healthSpring — Drug Repurposing

**Role**: MATRIX scoring for NF drug candidates.

- Anderson-augmented MATRIX: `Score = pathway_match × tissue_geometry × disorder_factor`
- Dose-response modeling for MEK inhibitors, JAK inhibitors, mTOR inhibitors
- Population PK extrapolation from published NF clinical trials
- Cross-disease comparison: AD (her published work) vs. NF (new domain)

**Springs consumed**: healthSpring (233/233 checks), groundSpring (statistics/uncertainty)

### initioChem — Conformational Dynamics

**Role**: FEL exploration for NF-relevant drug targets.

- Neurofibromin structure: RAS-GAP domain, variant effects on catalytic activity
- MEK inhibitor binding landscapes: selumetinib, trametinib conformational dynamics
- Cross-target comparison with CAZyme FEL pipeline (already validated, 190/190)

**Springs consumed**: hotSpring (500+ checks, Exp 220 FEL pipeline)

### coralForge — Structure Prediction

**Role**: NF1 variant structural impact.

- AlphaFold2/3 predictions for NF1 mutation effects on neurofibromin structure
- RAS-GAP interface disruption modeling
- Structural basis for LOF classification

**Springs consumed**: neuralSpring (154 checks — 62 Python + 55 Rust + 37 GPU)

---

## The Composition Map

```
NF Data Portal (Synapse)          PubChem / ChEMBL          ADDRC Library
    │                                  │                         │
    ▼                                  ▼                         ▼
helixVision                      healthSpring               healthSpring
(gene expression,                (MATRIX scoring,           (HTS computational
 pathway enrichment,              dose-response,             triage, 8K compounds)
 tumor microenvironment)          population PK)
    │                                  │                         │
    │    coralForge                    │                         │
    │    (NF1 variant structure,       │                         │
    │     RAS-GAP modeling)            │                         │
    │         │                        │                         │
    │    initioChem                    │                         │
    │    (MEK inhibitor FEL,           │                         │
    │     neurofibromin dynamics)      │                         │
    │         │                        │                         │
    ▼         ▼                        ▼                         ▼
    └─────────┴────────────────────────┴─────────────────────────┘
                                  │
                                  ▼
                    pseudoSpore (NF preliminary data)
                    ├── Gene expression analysis results
                    ├── Drug repurposing MATRIX scores
                    ├── Structural variant analysis
                    ├── Conformational dynamics
                    ├── Cross-disease comparison (AD → NF)
                    └── Self-verifying, foundation-ready
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              CTF NDU Grant   Andrea's     New Spring
              Prelim Data    NF Science   Validation Targets
```

---

## Grant Alignment

### Children's Tumor Foundation — NF Data Utilization Award (NDU)

Total budget: up to **$125K** over two years. Indirect costs capped at 10%.

- **Year 1** (up to $50K): Data exploration and bioinformatics analysis via Pluto.bio platform — gene expression mining, pathway enrichment, drug repurposing scoring, computational preliminary data. CTF provides Pluto platform access for the duration of the award.
- **Year 2** (up to $75K): In vitro validation of pathways, targets, or biomarkers identified in Year 1 — iPSC models, ADDRC compound screening, wet lab confirmation of computational predictions.

### Role Split

| Role | Person | Contribution |
|------|--------|-------------|
| **PI** | Andrea Gonzales | Domain expertise (JAK/STAT, drug discovery), ADDRC access, grant authority, wet lab validation |
| **Computational infrastructure** | Kevin Mok | Validated pipelines, GPU compute (biomeGate), data management, self-verifying artifacts, zero cost to university |

### What Andrea Brings

- Faculty PI status (required for CTF NDU)
- Published expertise in JAK/STAT signaling (G1-G6, 782/782 validated)
- ADDRC compound library access (8K compounds through Lisabeth)
- iPSC models for functional validation
- Wet lab capacity for Year 2 confirmation
- Domain perspective on NF biology and signaling cross-talk

### What the Ecosystem Brings

- Validated computational pipelines across 5 springs
- GPU compute (biomeGate: Threadripper 3970X, 256 GB RAM, Titan V ×2, MI50 ×2, RTX 5060)
- AI-accelerated pipeline coordination
- Self-verifying artifact packaging (pseudoSpore pattern)
- Data management and provenance (NestGate, rhizoCrypt, sweetGrass)
- Zero cost to university — all AGPL-3.0, all sovereign

---

## What This Proves About gen5

### Multi-product composition is necessary

NF cannot be served by helixVision alone. The biological question spans genomics (helixVision), pharmacology (healthSpring), structural biology (coralForge), and dynamics (initioChem). gen5 science demands products that compose with each other, not just products that compose primals.

### External data ingestion changes the game

gen3/gen4 reproduced published papers. gen5 ingests data the ecosystem has never seen — NF Data Portal datasets, CTF curated collections, Andrea's unpublished screening results. The springs must handle data they weren't trained on.

### The collaborator owns the science

The pseudoSpore produced for NF is Andrea's preliminary data. It goes into her CTF NDU application. She is the PI. The ecosystem provided the computation; she provides the science and the authority. This is the gen5 success metric: the science belongs to the collaborator.

### The feedback loop creates new validation targets

Andrea's NF results become new spring validation checks:
- NF gene expression analysis → new wetSpring validation targets
- NF drug repurposing scores → new healthSpring validation targets
- NF structural variants → new neuralSpring validation targets
- NF conformational dynamics → new hotSpring validation targets

The ecosystem gains validation targets it could never have generated internally.

---

## Connection to Existing Validated Work

The NF project does not start from zero. It builds on 782/782 checks already passing against Andrea's published work:

| Existing Validation | NF Extension |
|-------------------|--------------|
| wetSpring Exp 273-286: G1-G6 reproduced (359/359) | Same pipeline, NF gene expression datasets |
| neuralSpring nS-601-605: modeling + MATRIX (329/329) | MATRIX scoring extended to NF drug targets |
| airSpring: CytokineBrain cross-species (94/94) | Cytokine signaling in NF microenvironment |
| healthSpring: PK/PD, population PK (233/233) | Population PK for NF drug candidates |
| hotSpring Exp 220: CAZyme FEL (190/190) | FEL pipeline applied to MEK inhibitor dynamics |

Total existing foundation: **782/782** (Andrea's published data) + **190/190** (FEL pipeline) + **6,656+** (genomics pipeline) + **500+** (MD pipeline) = a validated computational base spanning every domain the NF project touches.

---

## Cross-References

- `gen5/collaborators/GONZALES_NF.md` — relationship context and collaboration status
- `gen4/thesis/THE_GEN5_TRANSITION.md` — the architectural pattern this instantiates
- `gen4/products/HELIX_VISION.md` — primary genomics product
- `gen4/products/INITIOCHEM.md` — conformational dynamics product
- `gen4/products/BLUEFISH.md` — analytical chemistry product (PFAS bridge)
- `attsi/non-anon/contact/gonzales/onboarding/PRE_GRANT_PIPELINE.md` — the operational model
- `attsi/non-anon/contact/gonzales/computational_brief.md` — Anderson framework applied to her data
- `attsi/non-anon/contact/gonzales/onboarding/LAB_ONBOARDING_PACKAGE.md` — full lab integration plan

---

*The NF project is not a collaboration proposal. It is a proof of concept for the gen5 operating model — where the ecosystem's validated computation serves an external scientist's question, the deliverable is science she owns, and the feedback makes the ecosystem stronger than it was before she arrived.*
