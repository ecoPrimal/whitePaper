# Project 1: CQ Resistance Evolution via pfaat1

## Upstream Validation Research Package

**Paper**: Amambua-Ngwa et al. 2023, *Nature Microbiology* 8:1213–1226
**DOI**: 10.1038/s41564-023-01377-z
**Preprint**: bioRxiv 10.1101/2022.05.26.493611
**License**: CC-BY 4.0

---

## Code Repositories

| Repo | Owner | Language | Content |
|------|-------|----------|---------|
| [emilyli0325/CQ.AAT1](https://github.com/emilyli0325/CQ.AAT1) | Xue Li (Texas Biomed) | R | Population genomics analysis: hapFLK, IBD, allele frequencies, LD, haplotype networks |
| [kbuttons/CQ.AAT1.progeny](https://github.com/kbuttons/CQ.AAT1.progeny) | Katrina Button-Simons (Notre Dame) | R | Progeny characterization, linkage analysis, CQ IC50 analysis |
| [MPB-mrcg](https://github.com/MPB-mrcg) | Alfred Amambua-Ngwa (MRC Gambia) | R | Gambian population genomics (related repos: Pf_balancing_selection, Mali geo-temp popgen) |
| [emilyli0325/P01-cloned.progeny](https://github.com/emilyli0325/P01-cloned.progeny) | Xue Li | Data | Filtered SNP calls for cloned progeny of multiple P. falciparum genetic crosses |
| [emilyli0325/BSA_lifecycle](https://github.com/emilyli0325/BSA_lifecycle) | Xue Li | R, Shell | BSA and genetic mapping across P. falciparum life cycle |

---

## Datasets

### Primary: MalariaGEN Pf6 (7,000 genomes)

- **Source**: https://www.malariagen.net/data_package/catalogue-genetic-variation-p-falciparum-v6-0/
- **Publication**: MalariaGEN et al. 2021, Wellcome Open Research 6:42
- **Samples**: 7,113 samples from 73 locations across 28 countries
- **QC pass**: 5,970 samples (FWS > 0.90 for monoclonal)
- **Variants**: 6M+ SNPs and indels
- **Format**: VCF per chromosome, zarr genotype format
- **Explorer**: https://www.malariagen.net/apps/pf6
- **Subset used in paper**: 4,051 monoclonal samples (FWS > 0.90, >50% genotyped)
  - WAF: 1,233 | EAF: 415 | CAF: 170 | ESEA: 994 | WSEA: 998 | SA: 37 | SM: 37 | PO: 167

### Primary: Gambian Longitudinal (600 genomes, 1984–2014)

- **Samples**: 321 isolates after QC (134 from 1984, 13 from 1990, 34 from 2001, 75 from 2008, 65 from 2014)
- **Sites**: Farafenni (central Gambia) and Serrekunda (coastal Gambia)
- **Variants after QC**: 16,385 biallelic SNPs (VQSLOD >= 2, MQ > 30, >= 5 reads/allele, MAF > 2%, missingness < 10%)
- **Sequencing**: Illumina HiSeq, paired-end, selective WGA for 1984/2001 samples
- **Accessions**: Listed in Supplementary Table 1 of the paper (SRA/ENA)
- **2008/2014 data from**: Amambua-Ngwa et al. 2018 (Sci Rep) and 2012 (PLoS Genet)

### Genetic Cross: 3D7 x NHP4026

- **Parents**: 3D7 (CQ-sensitive, African origin) x NHP4026 (CQ-resistant, Thailand-Myanmar border, 2007)
- **Cross method**: FRG NOD huHep mice (human-liver chimeric) + Anopheles stephensi mosquitoes
- **Pools**: 2 independent biological replicates, ~2,800 estimated recombinants each
- **CQ treatment**: 0, 50, 100, 250 nM for 48h or 96h
- **Progeny**: 155 clonal progeny (100 CQ-selected, 55 control); 109 unique recombinants
- **Sequencing**: Illumina NovaSeq S4 / HiSeq X, >100x coverage (bulk), 25x (clones)
- **Accessions**: Listed in Supplementary Table 4

### Reference Genome

- **Assembly**: *P. falciparum* 3D7, PlasmoDB release 46
- **Source**: https://plasmodb.org (current releases at veupathdb.org)
- **NCBI**: GCA_000002765
- **Genome**: ~23 Mb, 14 chromosomes
- **Annotation**: snpEff v4.3 with 3D7 release 46

---

## Software Stack

### Alignment & Variant Calling

| Tool | Version | Purpose |
|------|---------|---------|
| BWA mem | — | Read alignment to 3D7 reference |
| Picard tools | v2.0.1 | Sort, dedup, BAM processing |
| GATK HaplotypeCaller | v3.7 | Variant calling (per-sample gVCF) |
| GATK GenotypeGVCFs | v3.7 | Joint genotyping |
| bcftools | — | VCF merging |
| vcftools | — | VCF filtering |
| snpEff | v4.3 | Variant annotation |
| PLINK | — | Allele frequency calculation |

### Population Genomics

| Tool | Source | Purpose |
|------|--------|---------|
| hapFLK | v2.1 (PyPI) / INRA Forge | Haplotype-based selection scans (FLK + hapFLK tests) |
| isoRelate | github.com/bahlolab/isoRelate | IBD detection in haploid organisms (HMM-based) |
| hierfstat | CRAN | Weir & Cockerham FST |
| vcflib (pFST) | — | Likelihood ratio test for allele frequency differences |
| metaseq | CRAN | Fisher method for combined P-values |
| poppr | CRAN | MSN construction, genetic distance |
| igraph | CRAN | Relatedness networks (IBD > 90%) |
| ggplot2 | CRAN | Visualization |

### QTL Mapping

| Tool | Source | Purpose |
|------|--------|---------|
| QTLseqr | github.com/bmansfeld/QTLseqr (MSU) | G' statistic, BSA, confidence intervals |

### CRISPR / Phenotyping

| Tool | Purpose |
|------|---------|
| GraphPad Prism 8 | IC50 4-parameter curve fitting |
| Guava easyCyte HT (Luminex) | Flow cytometry for parasitemia/stage |
| rhAmp SNP Assay (IDT) | Competition allele frequency tracking |

### Structural Biology

| Tool | Purpose |
|------|---------|
| AlphaFold | 3D structure prediction of pfAAT1 |
| I-TASSER | Alternative structure prediction |
| TOPCONS | Transmembrane helix topology prediction |
| PyMol v2.3.0 | Structure visualization and mutagenesis |
| PDBeFold | Structural superposition (RMSD) |

---

## Key Numerical Results to Reproduce

### Allele Frequency Trajectories (Fig 1a)

| Locus | 1984 | 1990 | 2001 | 2008 | 2014 |
|-------|------|------|------|------|------|
| pfaat1 S258L | 0% | present | — | — | 97% |
| pfcrt K76T | 0% | present | — | — | 88% |

### Selection Coefficients (Extended Data Fig 1)

| Locus | s (per generation) | Basis |
|-------|-------------------|-------|
| pfaat1 S258L | 0.18 | 1990→2001 frequency change |
| pfcrt K76T | 0.11 | 1990→2001 frequency change |

Assuming 6-month generation time (mosquito to mosquito), estimated from 1990 and 2001 timepoints (before CQ monotherapy stopped in 2004).

### Allele Frequency Correlation (Extended Data Fig 4)

| Population | R² (CVIET vs S258L) | P |
|-----------|---------------------|---|
| West Africa | 0.65 | 0.0017 |
| All Africa | 0.44 | 0.0021 |

### IC50 Fold Changes (Fig 5b, CRISPR edits in NHP4026 background)

| pfaat1 allele | CQ IC50 relative to ancestral (258S/313F) |
|---------------|------------------------------------------|
| 258L/313F | ~1.5x increase (highest resistance) |
| 258L/313S (NHP4026) | moderate increase |
| 258S/313S | ~ancestral |
| 258S/313F (ancestral) | baseline |

### Fitness (Fig 5c, competition vs NHP4026)

| pfaat1 allele | Relative fitness |
|---------------|-----------------|
| 258L/313F | lowest (high fitness cost) |
| 258L/313S (NHP4026) | ~1.0 (reference) |
| 258S/313S | ~NHP4026 |
| 258S/313F (ancestral) | highest fitness |

### Structural (Extended Data Fig 9)

- 11 transmembrane helices in pfAAT1 (vs 10 in pfCRT)
- AlphaFold vs I-TASSER RMSD: 2.4–2.8 A over 303–327 of 440 aligned residues
- S258L on helix 3, F313S on helix 5, Q454E on helix 8, K541N in loop 9-10
- N-terminal residues 1-166 excluded (low confidence)

### QTL (Fig 3)

- Chr 7 QTL: contains pfcrt (expected)
- Chr 6 QTL: 1,013 kb to 1,283 kb (270 kb), 60 genes, pfaat1 at peak
- G' threshold: 20
- Progeny linkage: Fisher's exact, Bonferroni-corrected

---

## Reproducibility Tiers

### Tier 1 (Python baseline)

Reproduce using standard Python/R bioinformatics stack:
1. Allele frequency calculation from VCF (plink equivalent)
2. Selection coefficient estimation (linear model on log allele ratio)
3. FST calculation (Weir & Cockerham)
4. Correlation of pfcrt CVIET vs pfaat1 S258L frequencies
5. IC50 4-parameter curve fitting
6. Competition assay selection coefficient fitting

### Tier 2 (Rust binary validation)

Elevate to compiled binary with cross-tier parity:
1. VCF parsing and allele frequency extraction
2. FST computation
3. Selection coefficient estimation
4. IBD detection (HMM — isoRelate equivalent)
5. hapFLK selection scan (requires kinship matrix computation)
6. BSA G' statistic and QTL confidence intervals
7. MSN construction from genetic distance matrix

### Tier 3 (NUCLEUS provenance)

Full provenance chain on Tier 2 outputs:
- BLAKE3 hash on input VCFs and reference genome
- rhizoCrypt DAG for analysis session
- loamSpine ledger for permanent results
- sweetGrass braid for attribution

---

## Spring-Specific Validation Targets

### wetSpring

- [ ] BWA mem alignment of P. falciparum reads to 3D7 reference
- [ ] GATK HaplotypeCaller variant calling pipeline
- [ ] VCF filtering (VQSLOD, MQ, depth, MAF, missingness)
- [ ] Allele frequency extraction from VCF
- [ ] FWS complexity of infection estimation
- [ ] IBD detection via HMM (isoRelate-equivalent)
- [ ] Haplotype network construction (MSN via genetic distance)

### groundSpring

- [ ] Selection coefficient estimation from temporal allele frequency data
- [ ] Weir & Cockerham FST
- [ ] hapFLK selection scan with hierarchical population structure
- [ ] Fisher's exact test for inter-chromosomal linkage
- [ ] Pearson correlation of allele frequencies across populations
- [ ] BH multiple testing correction
- [ ] G' statistic for BSA QTL mapping
- [ ] Li's method for QTL confidence intervals

### neuralSpring

- [ ] Time-series modeling of allele frequency trajectories (1984→2014)
- [ ] Regime detection: pre-CQ-withdrawal vs post-2004 dynamics
- [ ] Convergent evolution scoring (independent origins of S258L in Africa vs SE Asia)

### hotSpring

- [ ] AlphaFold structure prediction for pfAAT1
- [ ] I-TASSER structure prediction for comparison
- [ ] Transmembrane helix topology prediction (TOPCONS equivalent)
- [ ] RMSD superposition between models
- [ ] Mutagenesis impact analysis (S258L, F313S, Q454E, K541N)

### healthSpring

- [ ] IC50 dose-response curve fitting (4-parameter logistic)
- [ ] Batch correction for IC50 data (ANOVA with load date)
- [ ] Competitive fitness assay analysis (log allele ratio vs time)
- [ ] Meta-analysis with random effects for combined fitness estimates

---

## Related Papers (Dependency Chain)

### Direct Dependencies (cited, data/methods reused)

| Ref | Paper | Relevance |
|-----|-------|-----------|
| 5,6 | Su et al. 1997 (Cell), Wellems et al. 1991 (PNAS) | Original pfcrt mapping |
| 16 | Nwakanma et al. 2014 (J Infect Dis) | Gambia 25-year drug resistance genomics |
| 17 | Amambua-Ngwa et al. 2019 (Science) | P. falciparum sub-Saharan Africa subpopulations |
| 18 | Henden et al. 2018 (PLoS Genet) | isoRelate method and global IBD analysis |
| 20 | Band et al. 2022 (Nature) | Strongest inter-chromosomal LD between pfcrt and pfaat1 |
| 21 | MalariaGEN 2021 (Wellcome Open Res) | Pf6 dataset (7,000 genomes) |
| 23,24 | Vaughan et al. 2015 (Nat Methods), Vendrely et al. 2020 (Trends Parasitol) | Humanized mouse genetic cross methodology |
| 25 | Brenneman et al. 2022 (iScience) | Optimized BSA for P. falciparum |
| 28 | Modrzynska et al. 2012 (BMC Genomics) | pcaat1 T162E in rodent malaria CQ resistance |
| 56 | Mansfeld & Grumet 2018 (Plant Genome) | QTLseqr package |

### Broader Context (Anderson-QS connection)

| Topic | Connection |
|-------|-----------|
| Digestive vacuole as bounded compartment | 1-2 um membrane-enclosed space — 3D bounded geometry |
| Coupled transporters (pfCRT + pfAAT1) | Competing drug/amino acid flux through same membrane |
| Epistasis (S258L + F313S) | Two-locus fitness landscape with transport physics |
| Regional dynamics (Africa vs SE Asia) | Different evolutionary solutions to same selective pressure |
| Fitness-resistance tradeoff | Anderson disorder: resistance mutations increase "disorder" in transport function |
