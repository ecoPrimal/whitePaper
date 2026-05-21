# Project 2: PTP Expression in Cancer / Migrastatics

## Upstream Validation Research Package

**Project Lead**: Mark (ABG)
**Collaborators**: OneMoreChemist, rosie
**Funded by**: NIH (Mark's lab — PTP involvement in metastasis)
**Timeline**: Semester to year
**Focus cancer**: Colorectal (CRC) first, then breast/ovarian, blood cancers

---

## Core Question

Which protein tyrosine phosphatases (PTPs) are differentially expressed — particularly overexpressed — in metastatic or aggressive cancers, and which represent viable next-generation therapeutic targets (migrastatics)?

### Sub-questions (from Discord thread)

1. Screen all ~38 classical PTPs in a focused cancer type (CRC) — Mark's preferred approach
2. Correlate phospho-site abundances across cancer stages — OneMoreChemist's interest
3. Identify novel targets beyond established ones for next grant cycle — Mark's strategic need

---

## Gene Set Definition

### Classical PTPs (38 genes — the target family)

**Receptor-type (21 genes)**:
PTPRA, PTPRB, PTPRC (CD45), PTPRD, PTPRE, PTPRF (LAR), PTPRG, PTPRH (SAP-1), PTPRJ (DEP-1), PTPRK, PTPRM, PTPRN (IA-2), PTPRN2 (IA-2β), PTPRO, PTPRQ, PTPRR, PTPRS, PTPRT, PTPRU, PTPRZ1, DUSP

**Non-receptor-type (17 genes — PTPN family)**:
PTPN1 (PTP1B), PTPN2 (TC-PTP), PTPN3 (PTPH1), PTPN4 (PTP-MEG1), PTPN5 (STEP), PTPN6 (SHP-1), PTPN7 (HePTP), PTPN9 (PTP-MEG2), PTPN11 (SHP-2), PTPN12 (PTP-PEST), PTPN13 (PTP-BAS), PTPN14, PTPN18 (BDP1), PTPN20, PTPN21, PTPN22 (LYP), PTPN23 (HD-PTP)

### Reference

- Alonso et al. 2004, *Cell* 117:699–711 — "Protein tyrosine phosphatases in the human genome" (107 PTPs total)
- Julien et al. 2011 — Classification framework

---

## Datasets

### Transcriptomics

| Source | Dataset | Samples | Access |
|--------|---------|---------|--------|
| TCGA-COAD | Colon adenocarcinoma RNA-seq | ~480 tumor + 41 normal | GDC portal |
| TCGA-READ | Rectal adenocarcinoma RNA-seq | ~170 tumor + 10 normal | GDC portal |
| GTEx | Normal colon tissue RNA-seq | ~370 transverse colon, ~370 sigmoid colon | GTEx portal |
| TNMplot | Integrated TCGA+GTEx+GEO (56,938 samples) | 22 tissue types, N/T/M | tnmplot.com |
| TCGA-BRCA | Breast invasive carcinoma | ~1,100 tumor + 113 normal | GDC portal |
| TCGA-OV | Ovarian serous cystadenocarcinoma | ~300 tumor | GDC portal |
| TCGA-LAML | Acute myeloid leukemia | ~170 samples | GDC portal |
| TCGA-DLBC | Diffuse large B-cell lymphoma | ~48 samples | GDC portal |

### Proteomics / Phosphoproteomics

| Source | Dataset | Samples | Key Data |
|--------|---------|---------|----------|
| CPTAC-COAD (2019) | Colon cancer multi-omic | 97 tumor, 100 normal | 19,147 phosphosites (log2 MS1) |
| LinkedOmics CPTAC-pancan-COAD | Integrated phospho + proteo + RNA | Same cohort | Direct download available |
| ProteomeXchange PXD005353 | CRC cell lines + patients | 65 cell lines, 90 patients | Pharmacoproteomics |
| ProteomeXchange PXD002089 | TCGA-matched proteomics | 95 tumor | MS2-based quantification |

### Pre-existing Pan-Cancer PTP Analyses

| Paper | DOI | Key contribution |
|-------|-----|-----------------|
| Li et al. 2022 (Front Immunol) | 10.3389/fimmu.2022.976996 | Pan-cancer PTP expression, GRN, PTPscore, drug sensitivity |
| Xu et al. 2024 (Sci Rep) | 10.1038/s41598-024-74037-9 | PTPN6/SHP-1 pan-cancer prognostic + immune analysis |
| He et al. 2022 (Math Biosci Eng) | 10.3934/mbe.2022251 | PTPRD pan-cancer prognostic + immune analysis |

---

## Code Repositories and Tools

### Data Access & Analysis

| Tool | Source | Purpose |
|------|--------|---------|
| TCGAbiolinks | github.com/bioinformaticsfmrp/tcgabiolinks | TCGA data query, download, prepare |
| DESeq2 | Bioconductor | Differential expression analysis |
| edgeR | Bioconductor | Alternative DE analysis |
| limma-voom | Bioconductor | Normalization + DE for RNA-seq |
| TCGAquantify | github.com/luisabatti/TCGAquantify | TCGA-specific DE wrapper |
| AndrewGarven/DifferentialExpression | GitHub | Simplified TCGA DE pipeline |
| nedaghohabi/TCGA-RNA-seq | GitHub | CRC-specific TCGA pipeline |

### Specialized Tools

| Tool | Source | Purpose |
|------|--------|---------|
| TNMplot | tnmplot.com / github.com/4ronB/tnmplot | N vs T vs M expression comparison, initial screening |
| cBioPortal | cbioportal.org | Mutation, expression, survival queries |
| TIMER2.0 | timer.cistrome.org | Tumor immune infiltrate + gene correlation |
| GEPIA2 | gepia2.cancer-pku.cn | Gene expression profiling, survival analysis |
| Kaplan-Meier Plotter | kmplot.com | Survival analysis for gene expression cutoffs |
| LinkedOmics | linkedomics.org | Multi-omic integration, kinase-substrate enrichment |
| PhosphoSitePlus | phosphosite.org | Curated phosphorylation site annotations |
| NetworKIN | networkin.info | Kinase-substrate prediction |

### GitHub Repos with CRC Proteomics Analysis

| Repo | Content |
|------|---------|
| Jasonmbg/CPTAC-Colon | CPTAC colon cancer proteogenomic analysis in R |

---

## PTPRD in CRC (OneMoreChemist's Lead)

### Established Evidence

- PTPRD is a haploinsufficient tumor suppressor on chr 9p23-24.3
- Frequently deleted/mutated in CRC (heterozygous loss sufficient for tumorigenesis)
- PTPRD suppresses colon cancer cell migration via CD44 regulation (Spandidos 2011)
- PTPRT + PTPRD mutations predict bevacizumab resistance in metastatic CRC (Cancers 2018)
- Somatic mutations at ~10% in CRC (COSMIC database)

### Key Papers

| Paper | Year | Key finding |
|-------|------|-------------|
| Veeriah et al. (Oncotarget) | 2015 | PTPRD as haploinsufficient tumor suppressor |
| Basso et al. (Cancers) | 2018 | PTPRT/PTPRD mutations predict bevacizumab resistance in mCRC |
| Spandidos-Publications (Exp Ther Med) | 2011 | PTPRD suppresses CRC migration via CD44 |
| He et al. (Math Biosci Eng) | 2022 | PTPRD pan-cancer prognostic and immune analysis |

---

## Migrastatics Context (Mark's Funded Work)

### Background

- Migrastatics = drugs targeting cancer cell migration/invasion (anti-metastatic)
- Mark's lab develops migrastatics targeting a specific PTP (likely receptor-type)
- Goal: identify additional PTP targets for next grant from expression data
- Preclinical pipeline established (Gandalovicova et al. 2021, Br J Cancer)

### Clinical-Stage PTP Inhibitors

| Compound | Target | Stage | Indication |
|----------|--------|-------|------------|
| ABBV-CLS-484 | PTP1B + PTPN2 | Phase I/II | Solid tumors (immuno-oncology) |
| Trodusquemine | PTP1B | Preclinical | Various (allosteric inhibitor) |

---

## Reproducibility Analysis Plan

### Phase 1: CRC Screen (all PTPs in one cancer)

1. Download TCGA-COAD + TCGA-READ RNA-seq counts via TCGAbiolinks
2. Download GTEx normal colon for expanded normal panel
3. Run DESeq2 on 38 classical PTP genes: tumor vs normal
4. Stage-stratify: I/II vs III/IV (or by TNM stage)
5. Survival analysis: high vs low expression for each PTP (Kaplan-Meier, Cox regression)
6. Quick screen via TNMplot for all 38 PTPs in CRC (N vs T vs M)

### Phase 2: Phosphoproteomics Layer

1. Download CPTAC-COAD phosphoproteomics from LinkedOmics
2. Extract phospho-sites on PTP family substrates
3. Correlate PTP mRNA expression with substrate phosphorylation levels
4. Compare phospho-site abundances across cancer stages (OneMoreChemist's proposal)

### Phase 3: Cross-cancer Expansion

1. Repeat Phase 1 screen for BRCA, OV, LAML
2. Identify PTPs consistently dysregulated across Mark's priority cancers
3. Cross-reference with mutation data (cBioPortal) for loss-of-function enrichment
4. Rank novel targets by: expression fold-change × mutation frequency × survival impact

---

## Spring-Specific Validation Targets

### healthSpring

- [ ] Pan-PTP differential expression in TCGA-COAD (DESeq2 / limma-voom)
- [ ] Survival analysis for 38 classical PTPs in CRC (Cox PH, log-rank)
- [ ] TNMplot automated screening for N/T/M differences
- [ ] PTPRD mutation and expression analysis in CRC (cBioPortal integration)

### groundSpring

- [ ] CPTAC phosphoproteomics: PTP substrate phospho-site quantification
- [ ] Kinase-substrate enrichment analysis (KSEA) for PTP loss-of-function impact
- [ ] Multi-omic integration: mRNA-protein-phospho correlation per PTP
- [ ] Stage-dependent phosphorylation trajectories

### neuralSpring

- [ ] Feature importance ranking: which PTPs best predict metastatic status?
- [ ] Clustering of PTP expression profiles to identify cancer subtypes
- [ ] Network analysis: PTP co-expression modules in CRC

### wetSpring

- [ ] RNA-seq quantification pipeline (STAR/Salmon → counts → DE)
- [ ] Proteomics/phosphoproteomics data processing (MaxQuant/DIA-NN output → R)

---

## FOUNDATION Thread Linkage

- **Environmental Genomics**: Cancer transcriptomics as environmental response to tumor microenvironment
- **Whole-Cell Modeling**: Phosphoproteomics as readout of cell-wide signaling state
- **Anderson Framework**: Tumor microenvironment as bounded vs diffuse signaling geometry (solid tumor = 3D bounded; circulating tumor cells = 2D planktonic; metastatic niche = re-bounded)
