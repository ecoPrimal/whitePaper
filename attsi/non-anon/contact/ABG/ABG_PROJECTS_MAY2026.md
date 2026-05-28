# ABG Chosen Projects — May 2026

**Date**: May 21, 2026
**Source**: ABG Discord project proposals
**Purpose**: Ingest for FOUNDATION thread linkage and NUCLEUS workload targets. Upstream dissemination across springs.

---

## Project 1: Chloroquine Resistance Evolution via pfaat1 (Tamison)

**Paper**: Amambua-Ngwa et al. 2023, *Nature Microbiology* 8:1213–1226
**DOI**: 10.1038/s41564-023-01377-z
**License**: CC-BY 4.0 (Open Access)
**Code**: github.com/emilyli0325/CQ.AAT1.git, github.com/kbuttons/CQ.AAT1.progeny.git
**Data**: NCBI SRA / ENA (600 P. falciparum genomes, Gambia 1984–2014, MalariaGEN release 6)

### Summary

Longitudinal genomic analysis of 600 *P. falciparum* genomes from Gambia (1984–2014) reveals that a second digestive vacuole transporter, pfAAT1 (putative amino acid transporter), co-evolved with pfCRT during chloroquine resistance evolution. pfaat1 S258L rose from 0% to 97% in parallel with pfcrt K76T. Genetic crosses in humanized mice + CRISPR-Cas9 editing confirm: S258L potentiates CQ resistance (+1.5x IC50) but at fitness cost; F313S (common in SE Asia) partially restores fitness while reducing resistance. Epistatic interaction between the two loci. Convergent evolution of S258L in Africa vs SE Asia (independent origins).

### Key Methods Reproduced/Reproducible

- Population genomics: hapFLK selection scans, IBD (isoRelate), LD decay, allele frequency trajectories
- QTL mapping: bulk segregant analysis (BSA) from genetic crosses in humanized mice
- Gene editing: CRISPR-Cas9 allelic replacements, IC50 dose-response curves
- Fitness: pairwise competition assays, selection coefficient estimation
- Structural: AlphaFold + I-TASSER modeling of pfAAT1, transmembrane topology (TOPCONS)
- Yeast heterologous expression: doubling time under CQ stress

### Spring Mapping

| Spring | Touchpoints |
|--------|------------|
| **wetSpring** | 600 WGS pipeline (BWA mem, GATK HaplotypeCaller, vcftools), allele frequency calculation, IBD analysis, haplotype networks, MSN construction |
| **groundSpring** | Selection coefficient estimation (s=0.18 pfaat1, s=0.11 pfcrt), FST, hapFLK significance, Fisher's exact for linkage, Pearson correlation of allele frequencies |
| **neuralSpring** | Time-series allele trajectory modeling (1984→2014), regime detection (pre/post CQ withdrawal 2004), convergent evolution scoring |
| **hotSpring** | AlphaFold/I-TASSER structural modeling, transmembrane helix analysis, RMSD superposition (2.5A over 327 residues) |
| **healthSpring** | IC50 dose-response modeling (4-parameter curve), competitive fitness assays, SYBR Green fluorescence assay |

### Validation Targets

- [ ] Reproduce allele frequency trajectories for pfaat1 S258L and pfcrt K76T (Fig 1a)
- [ ] Reproduce selection coefficient estimates (s=0.18, s=0.11) from frequency data
- [ ] Reproduce IBD peaks at pfaat1 and pfcrt (Fig 1c)
- [ ] Reproduce LD correlation between pfcrt CVIET and pfaat1 S258L (R²=0.65 WAF, R²=0.44 all Africa)
- [ ] Reproduce IC50 fold-changes from CRISPR edits (1.5x for S258L)
- [ ] Reproduce fitness measurements from competition assays (Fig 5c)
- [ ] Reproduce BSA QTL peaks at chr 6 and chr 7 (Fig 3)

### Anderson-QS Connection

The digestive vacuole is a bounded 3D compartment (~1-2 um). Two transporters in the same membrane (pfCRT and pfAAT1) create a coupled transport system where amino acid flux and drug flux compete. This is a molecular-scale Anderson localization problem: the "disorder" is the mutation landscape of two interacting transporters, and the "localization" is whether drug accumulates in the vacuole or escapes. The epistatic interaction (S258L + F313S) is a two-locus fitness landscape with geometry-dependent transport physics.

---

## Project 2: PTP Expression in Cancer Metastasis (Mark)

**PI**: Mark (ABG member, NIH-funded lab working on protein tyrosine phosphatases)
**Collaborators**: rosīe, OneMoreChemist
**Timeline**: Semester to year
**Status**: Proposal stage, defining scope

### Summary

Screen expression levels of the ~100+ protein tyrosine phosphatases (PTPs) in aggressive cancers and metastases using public transcriptomic and proteomic datasets. Goal: identify which PTPs are overexpressed in metastases, potentially revealing new drug targets (migrastatics). Starting with colorectal cancer (CRC) based on existing PTPRD links, expanding to blood cancers, ovarian, breast. Secondary interest in phospho-site relative abundances across cancer stages.

### Key Methods

- Transcriptomic analysis: RNA-seq differential expression, pathway enrichment
- Proteomic analysis: phosphoproteomics, phospho-site abundance mapping
- Dataset curation: GEO/SRA/ENA mining, metadata standardization
- Tools mentioned: TNMplot for initial screening

### Spring Mapping

| Spring | Touchpoints |
|--------|------------|
| **wetSpring** | RNA-seq pipeline (alignment, quantification, normalization, DE analysis), GEO/SRA dataset retrieval, batch effect correction across studies |
| **healthSpring** | Cancer biology domain (PTP family, metastasis markers, migrastatic targets), PK/PD modeling of PTP inhibitors |
| **neuralSpring** | ML for expression pattern classification across cancer types, feature selection for PTP panel |
| **groundSpring** | Statistical rigor for multi-dataset meta-analysis, multiple testing correction, effect size estimation |

### Validation Targets

- [ ] Automated GEO/SRA query and metadata extraction for PTP + cancer datasets
- [ ] Cross-study normalization pipeline for RNA-seq data from different labs
- [ ] Differential expression of PTP family members in CRC (metastatic vs primary)
- [ ] Phospho-site abundance correlation with PTP expression levels

### Notes

OneMoreChemist flagged proteomics interest — phospho-site relative abundances across cancer stages. This is the deeper analysis: not just which PTPs are expressed, but whether the phosphoproteome shows downstream effects of PTP activity changes. Computational bottleneck is likely cross-study normalization (different platforms, library prep, sequencing depth).

---

## Project 3: Conformational Energy Landscapes for CAZyme Docking (Alistaire)

**Lead**: Alistaire
**Timeline**: Ongoing, reviewing methods
**Status**: **pseudoSpore v1.7.0 delivered May 28** — 8 modules, 190 checks PASS, GuideStone-grade. Derivation Anchoring v1.0 (zero magic numbers). Automated artifact detection (cross-landscape, binding distance, KS test). Awaiting Alistaire review before AutoDock correlation phase.
**Product**: **initioChem** (`gardens/initioChem/`, `git@github.com:sporeGarden/initioChem.git`) — interactive 3D FEL explorer being seeded as the user-facing tool for this work.

### Summary

Validate whether molecular docking (AutoDock Vina) can substitute for resource-intensive conformational energy landscapes when studying monosaccharide ring conformations in carbohydrate-active enzyme (CAZyme) active sites. Preliminary results show that catalytic itinerary conformations are better binders in Vina. Now generating full energy landscapes (MD/MM level, not full QM/MM since only pre/post-transition state conformations are needed) for comparison.

**Reference**: Davies et al. 2015, JACS (esp. Fig 10 — conformational free energy landscapes of carbohydrate substrates)

### Key Methods

- Molecular docking: AutoDock Vina, monosaccharide ring conformations
- Energy landscapes: MD/MM simulations (sufficient for pre/post-transition state)
- Ring conformation generation: computational ring pucker sampling
- Structural analysis: Glycosyl Hydrolase family representative selection

### Spring Mapping

| Spring | Touchpoints |
|--------|------------|
| **hotSpring** | Molecular dynamics simulations, energy landscape generation, conformational sampling, GPU-accelerated force field evaluation |
| **groundSpring** | Statistical comparison of docking scores vs energy landscape minima, correlation and agreement metrics |
| **neuralSpring** | ML surrogate models for energy landscape prediction from docking scores |

### Validation Targets

- [x] Reproduce Iglesias-Fernández 2015 FEL — ⁴C₁/boat/¹C₄ basins, barriers 38–53 kJ/mol (free xylose) ← **v1.6.1 PASS**
- [x] Enzyme-bound barrier lowering (1–5 kJ/mol) consistent with two-fold catalytic itinerary ← **v1.6.1 PASS**
- [x] 2D Stoddart diagram: conformational selection visible in enzyme-bound landscape ← **v1.6.1 PASS**
- [x] Method controls: alanine dipeptide Ramachandran + chignolin OPES folding ← **v1.6.1 PASS**
- [x] PLUMED-NEST validation: 8 targets ingested (2 PASS, 6 profiled) ← **v1.6.1 PASS**
- [ ] Docking score vs energy landscape correlation for representative GH families (Tier 3 — after FEL review)
- [ ] Ring conformation generator validation against known pucker coordinates
- [ ] Epimer baselines: lyxose/glucose/mannose/galactose (Tier 1 — next)
- [ ] 2D24 −2/+1 subsite distortion propagation (Tier 1 — next)
- [ ] GH11 inverting xylanase comparison (Tier 2)

### Deliverables

| Version | Date | Files | Checks | Status |
|---------|------|-------|--------|--------|
| v0.6.0 | May 24 | 41 | ~20 | Prototype. Atom index errors + lyxose contamination found by Alistaire |
| v1.6.1 | May 27 | 76 | 71 PASS | Pipeline-derived. All v0.6.0 issues fixed + machine-verified. Self-verifying |
| v1.7.0 | May 28 | 190+ | 190 PASS | GuideStone-grade. 16 FEL landscapes. Derivation Anchoring. Automated artifact detection. Phase 0 self-consistency. Zero magic numbers. |

### Notes

Alistaire correctly identified that MD/MM is sufficient for pre/post-transition states (no need for QM/MM which is required for transition state characterization). This scoping decision reduces compute requirements significantly. The WGSL shader library in barraCuda includes force field kernels (Coulomb, Yukawa, LJ, Morse, Born-Mayer) that are directly relevant to the MD energy calculations.

---

## Project 4: Global Salmon RNA-seq Meta-Analysis (bake3011)

**Lead**: bake3011
**Collaborators**: Metaniche
**Timeline**: 4–6 months
**Status**: Proposal stage, dataset screening starting next week

### Summary

Identify and compare publicly available salmon RNA-seq datasets from different geographical regions worldwide. Detect region-associated gene expression patterns linked to immune response, environmental adaptation, parasite resistance, and aquaculture stress. Build a curated metadata resource. Species: Atlantic salmon (*Salmo salar*), coho, Chinook, sockeye. Tissues: gill, skin, liver, muscle, blood, immune.

### Candidate Datasets Identified

| Accession | Species | Focus |
|-----------|---------|-------|
| GSE166686 | Atlantic salmon | Gill scRNA-seq, smoltification |
| GSE269132 | Atlantic + coho | Sea lice response comparison |
| GSE166760 | Atlantic salmon | Amoebic gill disease |
| SRP124522 | Chinook salmon | Multi-tissue transcriptome, Canada |

### References

- Bari et al. 2025, BMC Genomics — meta-analysis of rainbow trout RNA-seq (stress responses)
- Beemelmanns et al. 2021, BMC Genomics — Atlantic salmon heat + hypoxia
- Christensen et al. 2020, PLOS ONE — sockeye salmon genome/transcriptome
- He et al. 2018, Ecol Evol — Atlantic salmon competition transcriptomics
- Jeffries et al. 2014, Evol Appl — Pacific salmon high temperature
- Krasnov et al. 2021, Front Immunol — Atlantic salmon pathogen/stress transcriptomics

### Key Methods

- Dataset curation: GEO/SRA/ENA search, metadata standardization
- RNA-seq analysis: QC, alignment (reference genomes per species), gene-level quantification, normalization
- Cross-study analysis: batch correction, differential expression, pathway enrichment
- Geographic analysis: region-associated expression signatures

### Spring Mapping

| Spring | Touchpoints |
|--------|------------|
| **wetSpring** | RNA-seq pipeline (NCBI/SRA retrieval, alignment, quantification, normalization), batch correction across studies/labs, 16S-style taxonomy if microbiome component |
| **airSpring** | Environmental data integration (temperature, salinity correlations with expression), aquaculture environmental monitoring |
| **groundSpring** | Cross-study normalization statistics, confound identification (lab vs geography), meta-analysis effect sizes |
| **neuralSpring** | Geographic clustering from expression data, unsupervised pattern detection across regions |

### Validation Targets

- [ ] Automated SRA retrieval and metadata extraction for salmon RNA-seq
- [ ] Cross-study normalization pipeline handling different species, tissues, conditions
- [ ] Batch effect detection and correction (Metaniche correctly flagged this risk)
- [ ] Geographic expression signature identification controlling for species/tissue/lab confounds

### Notes

rosīe correctly noted that a dataset catalogue alone is not a novel result — the analysis needs to go deeper. Metaniche flagged the batch effect confound (lab differences vs geographic differences). bake3011 acknowledged the ChatGPT-generated proposal needs work. The computational challenge is real: cross-study RNA-seq normalization across species, tissues, and platforms is a hard problem. Restricting to one species + one tissue initially (Metaniche's suggestion) is the right move.

---

## Upstream Dissemination Map

```
ABG Project                    Primary Spring    Secondary Springs
─────────────────────────────────────────────────────────────────
1. CQ resistance (pfaat1)      wetSpring         groundSpring, hotSpring, healthSpring, neuralSpring
2. PTP cancer metastasis       wetSpring         healthSpring, groundSpring, neuralSpring
3. CAZyme energy landscapes    hotSpring         groundSpring, neuralSpring
4. Salmon RNA-seq geography    wetSpring         airSpring, groundSpring, neuralSpring
```

### For wateringHole Handoff

These four projects provide immediate validation targets for:
- **wetSpring**: RNA-seq/WGS pipelines, SRA retrieval, cross-study normalization (Projects 1, 2, 4)
- **hotSpring**: MD/MM energy landscapes, force field evaluation, structural modeling (Projects 1, 3)
- **groundSpring**: Selection coefficients, meta-analysis statistics, batch correction (all 4)
- **healthSpring**: Cancer transcriptomics, PK/PD, dose-response curves (Projects 1, 2)
- **neuralSpring**: Time-series modeling, ML surrogates, pattern detection (all 4)

### For FOUNDATION Thread Linkage

| Project | Foundation Thread |
|---------|------------------|
| CQ resistance | Thread 4 (Environmental Genomics), Thread 7 (Anderson Framework) |
| PTP metastasis | Thread 1 (Whole-Cell Modeling), Thread 5 (Health/Disease) |
| CAZyme landscapes | Thread 2 (Plasma/QCD — energy landscape methods), Thread 7 (Anderson) |
| Salmon geography | Thread 4 (Environmental Genomics), Thread 3 (Agriculture/Ecology) |

### For NUCLEUS Workload Catalog

Each project should generate workload TOMLs for toadStool dispatch:
- `workloads/wetspring/wetspring-abg-cq-resistance.toml`
- `workloads/wetspring/wetspring-abg-ptp-cancer.toml`
- `workloads/hotspring/hotspring-abg-cazyme-landscape.toml`
- `workloads/wetspring/wetspring-abg-salmon-rnaseq.toml`

---

## Compute Placement & Gate Assignment

**Cluster status**: Pre-covalent. Gates are standalone towers, not yet meshed. 10G backbone hardware acquired (switch + NICs) but cables pending. ironGate is the active ABG gate. Other towers are available hardware that can be brought online per project.

**westGate NAS**: Late-stage. HDDs are being pulled to provide storage for other towers. Not available as a centralized NAS for these projects. Local NVMe on the assigned gate handles storage.

**Reference**: Full hardware inventory in `whitePaper/gen3/about/HARDWARE.md`.

### Project Resource Needs + Gate Assignment

| | **P1: CQ/pfaat1** | **P2: PTP Cancer** | **P3: CAZyme FEL** | **P4: Salmon RNA-seq** |
|---|---|---|---|---|
| **Lead** | Tamison | Mark | Alistaire | bake3011 |
| **CPU cores** | 4–8 | 2–4 | 4–8 (docking), 16+ (MD) | 8–16 (STAR) |
| **RAM** | 8 GB | 8 GB | 16 GB (MD) | 32–64 GB (STAR index) |
| **GPU** | No | No | **Yes** (force field eval) | No |
| **Storage** | ~5 GB (VCFs) | ~10 GB (TCGA counts) | ~50 GB (trajectories) | ~500 GB+ (FASTQs) |
| **Network** | Moderate (download once) | Light | Light | Heavy (bulk SRA download) |
| **Proposed gate** | **ironGate** | **ironGate** | **biomeGate** | **strandGate** |
| **Gate hardware** | i9-14900K, RTX 5070, 96GB DDR5, 3.6TB NVMe | (same — co-hosted) | TR 3970X, Titan V HBM2, MI50 HBM2, 256GB, 5TB NVMe | Dual EPYC 7452 (64c/128t), 256GB ECC, 18TB NVMe |
| **Why this gate** | Light workload. 23MB genome fits easily. CPU stats alongside normal dev | Light workload. Pre-processed TCGA counts, no alignment | **Only GPU-heavy project**. Titan V FP64 (7.4 TFLOPS) + MI50 FP64 (6.6 TFLOPS) for MD force evaluation. Dual-vendor WGSL parity | 64-core EPYC for parallel STAR alignment of 3GB salmon genome. 256GB ECC holds STAR index. 18TB NVMe stages FASTQs |
| **barraCuda role** | `stats.*` (FST, correlation), `genomics` (HMM/IBD), `health` (IC50 curves) | `stats.*` (DE, ANOVA, survival), `ml.*` (classifiers), `linalg.*` (PCA) | `ops/md` (Yukawa, PPPM, LJ, Coulomb, VV integrator). **GROMACS parity showcase** | `stats.*` (batch correction, DE), `linalg.*` (PCA/SVD), `ml.*` (geographic classification) |
| **Spring** | wetSpring (primary) | healthSpring (primary) | hotSpring (primary) | wetSpring (primary) |

### Placement Logic

**ironGate hosts all small**: Projects 1 and 2 are light compute. The 23MB *P. falciparum* genome and pre-processed TCGA counts never stress 96GB/24-core. Both run alongside normal development. No additional tower needed.

**Larger projects get their own tower:**

- **Project 3 → biomeGate**: The only project requiring GPU-hours. Metadynamics FEL = inner-loop force evaluation (Coulomb + LJ + bonded) at every MD timestep, 12–48 hours per enzyme system. biomeGate's Titan V HBM2 (7.4 TFLOPS FP64) and MI50 HBM2 (6.6 TFLOPS FP64) are purpose-built. Dual-vendor validates barraCuda's "same WGSL shader, different silicon" on a real scientific workload — the **GROMACS parity showcase**.

- **Project 4 → strandGate**: STAR alignment of 200+ salmon RNA-seq samples against a 3GB genome is CPU-parallel and RAM-hungry (STAR index ~30GB). strandGate's 64 cores and 256GB ECC are the natural substrate. 18TB all-NVMe stages the ~500GB of FASTQs locally — no NAS dependency.

### Available Metal (towers not yet assigned)

These towers can absorb overflow or take on project work if the primary gates are loaded:

| Gate | CPU | GPU | RAM | Storage | Potential role |
|------|-----|-----|-----|---------|---------------|
| **eastGate** | i9-12900, RTX 4070, Akida NPU | 32GB DDR5 | 2TB NVMe | Utility compute, neuromorphic. Could run P1/P2 overflow |
| **southGate** | Ryzen 5800X3D, RTX 4060 + 3090 slot | 128GB DDR4 | 5TB NVMe | Gaming + compute. 128GB makes it a P4 alternate |
| **northGate** | Ryzen 9 9950X3D, RTX 5090 32GB | 96GB DDR5 | 5TB NVMe | Strongest single GPU. P3 alternate if biomeGate is loaded |
| **swiftGate** | Ryzen 5800X, RTX 3070 FE | 64GB DDR4 | NVMe | Mobile/compact. Batch overflow |
| **kinGate** | i7-6700K, RTX 3070 | 32GB DDR4 | NVMe | Staging/utility |
| **flockGate** | i9-13900K, RTX 3070 Ti | 64GB DDR5 | 2TB NVMe | Remote. Latency-tolerant batch |
| **blueGate** | TBD, no GPU | 128GB DDR4 | 2TB NVMe | Windows. Cross-platform testing |

### barraCuda as GROMACS Alternative (Project 3)

```
GROMACS:                          barraCuda:
  CUDA kernels (NVIDIA only)        WGSL shaders (any GPU vendor)
  + OpenMM/OpenCL (partial)         + NagaExecutor (CPU fallback)
  + PLUMED (metadynamics bias)      + spring-layer metadynamics (to build)
  + PME (long-range electrostatics) + PPPM (same algorithm class)
  = Runs on: NVIDIA HPC only        = Runs on: Titan V, MI50, RTX, Apple, Intel, CPU
```

Existing barraCuda shaders mapping to GROMACS nonbonded kernels:
- `yukawa_*.wgsl` → screened Coulomb (generalized LJ+Coulomb)
- `pppm_*.wgsl` → particle-mesh electrostatics (PME equivalent)
- `rop_force_accum.wgsl` → force accumulation
- `vv_integrator.wgsl` → velocity Verlet time stepping
- `cell_list_*.wgsl` → neighbor search

The metadynamics bias (PLUMED's role — adaptive Gaussians on collective variables) needs spring-layer implementation. The expensive inner loop (force evaluation per timestep) is already covered by existing shaders.

### Workload TOMLs

```
workloads/wetspring/wetspring-abg-cq-resistance.toml       → ironGate
workloads/healthspring/healthspring-abg-ptp-cancer.toml     → ironGate
workloads/hotspring/hotspring-abg-cazyme-landscape.toml     → biomeGate
workloads/wetspring/wetspring-abg-salmon-rnaseq.toml        → strandGate
```
