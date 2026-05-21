# Project 4: Salmon RNA-seq Geographic Patterns

## Upstream Validation Research Package

**Project Lead**: bake3011 (ABG)
**Collaborators**: Metaniche, rosie
**Timeline**: 4–6 months
**Focus**: Atlantic salmon (*Salmo salar*) primarily; potential expansion to coho, Chinook, sockeye
**Approach**: Meta-analysis of public RNA-seq datasets across global geographic regions

---

## Core Question

Do salmon from different geographic regions (North Atlantic, North Pacific, Europe, Canada, Chile, Australia/Tasmania, Asia) show region-associated transcriptomic signatures, and can these be separated from confounding technical/biological variables?

### Narrowing (from Discord feedback)

- rosie: Dataset catalogue alone is not a novel result — need deeper expression analysis
- Metaniche: Risk of batch effects mimicking geographic signal → restrict to one species + one tissue initially
- Consensus: Start with Atlantic salmon (*S. salar*) gill tissue, then expand

---

## Reference Genomes

### Atlantic Salmon

| Assembly | Year | Source | Notes |
|----------|------|--------|-------|
| Ssal_v3.1 | 2021 | NCBI GCF_905237065.1 | **Current best** — long-read, improved duplicate resolution |
| ICSASG_v2 | 2015 | NCBI GCF_000233375.1 | Legacy assembly, many older datasets aligned to this |
| Ensembl Release 115 | 2025 | ensembl.org/Salmo_salar | Gene models, Ssal_v3.1 based |

### Other Salmonids

| Species | Assembly | NCBI |
|---------|----------|------|
| Chinook (*O. tshawytscha*) | Otsh_v2.0 | GCF_018296145.1 |
| Coho (*O. kisutch*) | Okis_V2 | GCF_002021735.2 |
| Sockeye (*O. nerka*) | — | Christensen et al. 2020, PLOS ONE |
| Rainbow trout (*O. mykiss*) | Omyk_1.0 | GCF_013265735.2 |

---

## Candidate Datasets

### Tier 1: Directly cited by bake3011

| GEO/SRA | Species | Tissue | Condition | Region | Samples | Citation |
|---------|---------|--------|-----------|--------|---------|----------|
| GSE166686 | Atlantic salmon | Gill (snRNA-seq) | Smoltification | Scotland | ~24 | West et al. 2021, Front Immunol |
| GSE269132 | Atlantic + Coho | Skin, fin (snRNA-seq) | Sea lice response | Scotland/Edinburgh | ~48 | Salisbury et al. 2024, BMC Biol |
| GSE166760 | Atlantic salmon | Gill | Amoebic gill disease (AGD) | Australia/Tasmania | ~30 | Multiple AGD studies |
| SRP124522 | Chinook salmon | Multi-tissue | Baseline | Canada (BC) | Variable | Christensen et al. 2020 |

### Tier 2: High-value geographic datasets to screen

| Region | Condition | Search terms | Expected repositories |
|--------|-----------|-------------|----------------------|
| Norway | Aquaculture stress, temperature | "Salmo salar RNA-seq Norway" | GEO, ENA |
| Chile | Sea lice (C. rogercresseyi), ISA | "salmon RNA-seq Chile" | GEO, ENA |
| Canada | Multi-tissue baseline, wild populations | "salmon RNA-seq Canada" | GEO, SRA |
| Scotland/Ireland | Sea lice (L. salmonis), AGD | "salmon RNA-seq Scotland" | GEO, ENA |
| Tasmania | AGD, aquaculture disease | "salmon RNA-seq Tasmania Australia" | GEO |
| Iceland | Wild, landlocked vs anadromous | "salmon RNA-seq Iceland" | GEO |

### Tier 3: Centralized Resources

| Resource | URL | Content |
|----------|-----|---------|
| SalmoBase | salmobase.org | Genome browser + Aqua-FAANG functional annotations |
| Aqua-FAANG | aqua-faang.eu | Multi-tissue RNA-seq, ChIP-seq, ATAC-seq body/dev maps |
| ICES (Int'l Council for Exploration of the Sea) | ices.dk | Wild salmon survey data (non-seq, but geographic metadata) |

---

## Software Stack

### Dataset Discovery & Metadata

| Tool | Source | Purpose |
|------|--------|---------|
| GEOquery | Bioconductor | Programmatic GEO dataset search and metadata retrieval |
| SRAdb / pysradb | Bioconductor / PyPI | SRA metadata mining |
| ffq | github.com/pachterlab/ffq | Fast metadata fetch from SRA/GEO/ENA |
| rentrez | CRAN | R interface to NCBI Entrez API |
| ENA Browser API | ebi.ac.uk/ena | European Nucleotide Archive programmatic access |

### Alignment & Quantification

| Tool | Source | Purpose |
|------|--------|---------|
| Salmon (quant) | combine-lab.github.io/salmon | Quasi-mapping pseudoalignment, fast quantification |
| STAR | github.com/alexdobin/STAR | Splice-aware alignment |
| fastp / Trim Galore | — | Adapter trimming, quality control |
| MultiQC | multiqc.info | Aggregate QC across samples |
| nf-core/rnaseq | nf-co.re/rnaseq | Full Nextflow pipeline (STAR-Salmon, RSEM, HISAT2 options) |
| nf-core/rnaseqmeta | github.com/hossainlab/nf-core-rnaseqmeta | Meta-analysis pipeline with batch correction |

### Normalization & Batch Correction

| Tool | Source | Purpose |
|------|--------|---------|
| DESeq2 (vst) | Bioconductor | Variance stabilizing transform + normalization |
| edgeR (TMM) | Bioconductor | Trimmed mean of M-values normalization |
| ComBat / ComBat-seq | sva package (Bioconductor) | Empirical Bayes batch correction for known batches |
| limma (removeBatchEffect) | Bioconductor | Linear model batch correction |
| RUVSeq | Bioconductor | Remove unwanted variation using control genes |
| Harmony | github.com/immunogenomics/harmony | Fast batch correction for scRNA-seq (applicable to snRNA-seq datasets) |

### Differential Expression & Pathway Analysis

| Tool | Source | Purpose |
|------|--------|---------|
| DESeq2 | Bioconductor | Differential expression (primary) |
| limma-voom | Bioconductor | DE for heterogeneous designs |
| clusterProfiler | Bioconductor | GO/KEGG enrichment |
| GSEA (fgsea) | Bioconductor | Gene set enrichment |
| MetaVolcanoR | CRAN | Meta-analysis volcano plots |
| metaRNASeq | Bioconductor | Combining p-values across RNA-seq studies |

### Visualization

| Tool | Purpose |
|------|---------|
| ggplot2 | Core plotting |
| ComplexHeatmap | Expression heatmaps with annotations |
| PCAtools | PCA with batch/region coloring |
| pheatmap | Quick clustered heatmaps |

---

## Key Papers (Dependency Chain)

### Directly Cited by bake3011

| Paper | Year | Key contribution |
|-------|------|-----------------|
| Bari et al., BMC Genomics | 2025 | Rainbow trout RNA-seq meta-analysis (4 datasets) — **methodology template** |
| Beemelmanns et al., BMC Genomics | 2021 | Atlantic salmon heat + hypoxia transcriptomic responses |
| Christensen et al., PLOS ONE | 2020 | Sockeye salmon genome + population-defining regions |
| He et al., Ecol Evol | 2018 | Atlantic salmon transcriptome response to competition with non-native species |
| Jeffries et al., Evol Appl | 2014 | Pacific salmon high water temperature transcriptomic responses |
| Krasnov et al., Front Immunol | 2021 | Atlantic salmon pathogen/stress response meta-analysis (127 experiments, 6,440 arrays) |

### Additional High-Value References

| Paper | Year | System | Relevance |
|-------|------|--------|-----------|
| West et al., Front Immunol | 2021 | Atlantic salmon gill snRNA-seq (GSE166686) | Cell-type-resolved smoltification |
| Salisbury et al., BMC Biol | 2024 | Atlantic vs coho sea lice snRNA-seq | Immune resistance mechanisms |
| Lien et al., Nature | 2016 | Atlantic salmon genome (ICSASG_v2) | Reference genome paper |
| Macqueen et al., BMC Genomics | 2017 | Salmonid whole genome duplication | Interpreting paralogous genes in DE |
| Krasnov et al., Front Immunol | 2021 | Salmonid immune gene atlas | Reference gene sets for immune signatures |

---

## Confound Management Strategy

### Major Confounds

| Confound | Source | Mitigation |
|----------|--------|------------|
| Lab / sequencing batch | Different labs, platforms, years | ComBat-seq on known batch labels |
| Species | S. salar vs O. kisutch vs O. tshawytscha | Start single-species (S. salar only) |
| Tissue | Gill, skin, liver, muscle, blood | Start single-tissue (gill) |
| Developmental stage | Smolt, parr, adult, spawning | Filter metadata, match stages |
| Experimental condition | Healthy, infected, stressed | Start with controls/healthy only |
| Reference genome version | ICSASG_v2 vs Ssal_v3.1 | Re-align all to Ssal_v3.1 uniformly |
| Whole-genome duplication | Salmonid Ss4R paralogs | Use OHNOLOG-aware gene models |

### Quality Filters for Dataset Inclusion

- Minimum 3 biological replicates per condition
- Raw FASTQ available (not just processed counts)
- Clear geographic provenance in metadata
- Single-species (Atlantic salmon initially)
- Single-tissue (gill initially)
- Sequencing depth > 10M reads per sample

---

## Reproducibility Analysis Plan

### Phase 1: Dataset Catalogue (weeks 1–3)

1. Search GEO/SRA/ENA for Atlantic salmon RNA-seq datasets
2. Screen by metadata quality: species, tissue, geography, condition, accession, read count
3. Build standardized inventory table (CSV/TSV):
   - Columns: accession, species, region, country, ocean_basin, tissue, condition, sequencing_type, platform, sample_size, read_length, paired/single, download_links, publication DOI
4. Identify well-represented vs underrepresented regions
5. Prioritize control/healthy gill samples from 3+ geographic regions

### Phase 2: Uniform Processing (weeks 3–6)

1. Download raw FASTQs via SRA toolkit / ENA
2. Quality check: fastp / FastQC
3. Align to Ssal_v3.1 genome using STAR (or pseudoalign with Salmon for speed)
4. Quantify at gene level (Salmon quant or featureCounts)
5. Aggregate into unified count matrix
6. QC: PCA colored by study, region, tissue — assess batch structure

### Phase 3: Batch Correction & DE (weeks 6–10)

1. Apply ComBat-seq (or limma removeBatchEffect) with study as batch variable
2. Verify batch correction: re-PCA, check that geographic signal remains while batch signal decreases
3. Differential expression: region-to-region comparisons (DESeq2, ~region + batch)
4. Identify geography-associated DE genes
5. GO/KEGG pathway enrichment on regional DE gene sets

### Phase 4: Signature Discovery (weeks 10–16)

1. Weighted gene co-expression network analysis (WGCNA) to find region-associated modules
2. Classify modules by biological function: immune, osmoregulation, stress, metabolism
3. Cross-reference with known salmon immune gene atlas (Krasnov 2021)
4. Test for enrichment of: parasite resistance genes, temperature response, salinity adaptation
5. Compare geographic signatures against known environmental gradients (temperature, parasite pressure)

### Phase 5: Reporting (weeks 16–20)

1. Finalize curated dataset catalogue as supplementary table
2. Publication-quality figures: PCA, heatmaps, volcano plots, WGCNA module-geography associations
3. Identify high-quality dataset shortlist for future meta-analysis

---

## Spring-Specific Validation Targets

### wetSpring

- [ ] SRA/GEO/ENA metadata mining for Atlantic salmon gill RNA-seq
- [ ] Uniform STAR/Salmon alignment to Ssal_v3.1
- [ ] Gene-level quantification and count matrix assembly
- [ ] fastp QC + MultiQC aggregation

### groundSpring

- [ ] ComBat-seq batch correction across studies
- [ ] DESeq2 differential expression: region-to-region comparisons
- [ ] WGCNA module discovery with geographic covariates
- [ ] Statistical framework for separating batch from biology

### neuralSpring

- [ ] Unsupervised clustering of samples by expression profile
- [ ] Classification: can geographic origin be predicted from transcriptome?
- [ ] Feature selection: minimal gene set distinguishing regions

### airSpring

- [ ] PCA visualizations colored by study, region, tissue
- [ ] Heatmaps of region-specific DE genes
- [ ] Geographic maps overlaid with expression signatures

### ludoSpring

- [ ] Dataset catalogue as structured metadata resource
- [ ] Reproducible Nextflow/Snakemake pipeline for the full analysis

---

## FOUNDATION Thread Linkage

- **Environmental Genomics**: Core domain — transcriptomic response to geographic/environmental pressures
- **Anderson Framework**: Aquaculture pens as bounded 3D geometry (high-density, recirculating water); wild river systems as linear flow geometry; open-ocean migration as dispersed 2D. These different environmental geometries predict different pathogen exposure patterns and immune gene expression profiles. The geographic signal in transcriptomics may partly reflect geometry-driven selection.
