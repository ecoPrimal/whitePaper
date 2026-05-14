# Jeffrey Barrick & Richard Lenski — Contact Notes

**Name**: Jeffrey E. Barrick, PhD
**Title**: Hannah Distinguished Professor
**Department**: Microbiology, Genetics & Immunology + Entomology (joint)
**Institution**: Michigan State University (returned Nov 2025 from UT Austin)
**Email**: barlab contact via barricklab.org
**Lab Website**: https://barricklab.org/
**LTEE Website**: https://the-ltee.org/
**GitHub**: https://github.com/barricklab
**Substack**: https://barricklab.substack.com/

**Richard E. Lenski**
**Title**: John A. Hannah Distinguished Professor Emeritus
**Department**: Microbiology & Molecular Genetics, MSU
**Role**: Founder of the LTEE (1988), now emeritus; Barrick is successor/director
**Blog**: https://telliamedrevisited.wordpress.com/

---

## Context

Applied to Research Assistant II position in the Barrick and Lenski Labs (posting 1124446, closed May 12, 2026).

### Interview Timeline
- **May 11, 2026** — Initial Zoom with Barrick ✅ (went well)
- **May 13, 2026** — Invited to **in-person interview** to meet lab + Rich Lenski
  - Options: **Fri 5/15**, **Mon 5/18**, or **Tue 5/19** (11:30 AM – 4:00 PM)
  - Format: Lab tour → Lunch with PhD students/postdocs → One-on-one/small group meetings → Final meeting with Barrick
  - This is the **guideStone USB opportunity** — bring the LTEE artifact

Position manages lab operations and LTEE, characterizes evolving populations, uses synthetic biology and computation.

---

## Barrick — Career Arc

- PhD: Biochemistry (computational/molecular)
- Postdoc: With Lenski at MSU — applied whole-genome sequencing to LTEE (~2005)
- Faculty: University of Texas at Austin (2010–2025), built independent lab, 10 PhDs graduated
- Current: Hannah Distinguished Professor, MSU (returned Nov 2025)
- Brought LTEE back to MSU from UT Austin — restarted Sept 10, 2025 at 82,000 generations
- Brought 5 PhD students and 2 postdocs from UT Austin
- Recent: "Phages use contingency loci as a bet-hedging strategy" (2025, with C.M. Waters)

---

## Four Research Pillars

### 1. LTEE — Long-Term Evolution Experiment
- 12 populations of *E. coli*, started 1988, now **82,500+ generations** (late 2025)
- Daily serial transfers (1% into fresh glucose minimal medium, ~6.67 gen/day)
- Frozen fossil record every 500 generations at –80°C
- Key findings: power-law fitness (no asymptote), parallel evolution, Ara-3 citrate innovation, genome streamlining, hypermutator lineages
- Barrick applied WGS to LTEE, built breseq, maintains experiment
- Recent: DFE (Distribution of Fitness Effects) paper accepted in *Science* (2024) — collaboration Baym/Tenaillon + Couce teams
- Reached 80,000 generations Aug 7, 2024 — "both a new Olympic Record and World Record"

### 2. breseq — Computational Genomics Pipeline
- Command-line tool (C++ and R) for mutation identification from resequencing data
- Predicts: SNPs, indels, large deletions, new junctions in haploid microbial genomes (<10-20 Mb)
- Open source: GPL-2.0, GitHub (barricklab/breseq), v0.39.0 (July 2024)
- LTEE-Ecoli repo: curated mutation database with interactive web interface
- Used worldwide for evolution experiments, strain QC, pathogen tracking

### 3. Insect Symbiont Engineering
- **Honey bee**: Bee microbiome toolkit (BTK), engineered *Snodgrassella alvi* for symbiont-mediated RNAi, gene knockdown in bees, protection from viral pathogens/parasites
- **Aphid**: Engineering *Serratia symbiotica*, maternal transmission, related to *Buchnera* endosymbionts
- 29 *Buchnera* genomes published 2024 (*Scientific Data*)
- One-step chromosomal engineering without exogenous recombinase (2024, *mBio*)

### 4. Synthetic Biology Reliability
- BioBrick burden study (2024, *Nature Communications*): 301 plasmids, 19.6% burdensome
- Engineering naturally transformable bacteria (*Acinetobacter baylyi*)
- Preventing evolutionary failure via cellular differentiation

---

## Key Publications

### LTEE Core
| Year | Citation | Key Finding |
|------|----------|-------------|
| 2009 | Barrick et al. "Genome evolution and adaptation in a long-term experiment with *E. coli*" *Nature* | First comprehensive WGS of LTEE populations |
| 2016 | Tenaillon et al. "Tempo and mode of genome evolution in a 50,000-generation experiment" *Nature* | Parallel and contingent molecular evolution at scale |
| 2017 | Good et al. "The dynamics of molecular evolution over 60,000 generations" *Nature* | Fitness dynamics, mutation trajectories, clonal interference |
| 2013 | Wiser et al. "Long-term dynamics of adaptation in asexual populations" *Science* | Power-law fitness trajectory — no asymptote |
| 2008 | Blount et al. "Historical contingency and the evolution of a key innovation in an experimental population of *E. coli*" *PNAS* | Citrate innovation in Ara-3 required potentiating mutations |
| 2012 | Blount et al. "Genomic analysis of a key innovation..." *Nature* | Molecular basis of citrate utilization |

### breseq & Computation
| Year | Citation | Key Finding |
|------|----------|-------------|
| 2014 | Deatherage & Barrick "Identification of mutations using breseq" *Methods Mol Biol* | Standard reference for breseq pipeline |
| 2010 | Barrick & Lenski "Genome-wide mutational diversity in an evolving population" *Cold Spring Harb Symp* | Mutation diversity across LTEE populations |

### Insect Symbionts
| Year | Citation | Key Finding |
|------|----------|-------------|
| 2024 | Leonard et al. "One-step genome engineering in bee gut bacterial symbionts" *mBio* | Chromosomal engineering without exogenous recombinase |
| 2024 | "Twenty-nine newly sequenced genomes...Buchnera" *Scientific Data* | Comprehensive *Buchnera* genome dataset |

### Synthetic Biology
| Year | Citation | Key Finding |
|------|----------|-------------|
| 2024 | "Measuring the burden of hundreds of BioBricks..." *Nature Communications* | 19.6% burdensome, evolutionary limit on constructability |

### Recent (2024-2025)
| Year | Citation | Key Finding |
|------|----------|-------------|
| 2025 | Barrick & Waters "Phages use contingency loci as a bet-hedging strategy" *bioRxiv* | Hypermutable phage DNA regions for host evasion |
| 2024 | Baym/Tenaillon/Couce "DFE evolution in LTEE" *Science* | Distribution of fitness effects changes over evolutionary time |
| 2024 | "Twenty-nine newly sequenced genomes...Buchnera" *Scientific Data* | Comprehensive aphid endosymbiont genome dataset |

---

## Connection to Our Work

### baseCamp Paper 02 — LTEE Extensions (DIRECT)
- Makes specific, falsifiable Anderson-QS predictions for LTEE populations
- Proposes biofilm vs planktonic LTEE growth to test sdiA expression
- E. coli sdiA = eavesdropper QS receptor (no synthase) — Anderson predicts geometry-dependent response
- wetSpring + neuralSpring + groundSpring pipeline for LTEE analysis
- References their literature correctly (Lenski, Wiser, Blount, Tenaillon)

### baseCamp Paper 01 — Anderson-QS (FOUNDATIONAL)
- Core framework: microbial signaling governed by spatial geometry × diversity
- 3D = QS active, 2D = QS fails — universal across life domains
- sdiA eavesdropper enrichment confirmed in NCBI data (Exp142)
- Directly testable with LTEE strains in biofilm vs planktonic conditions

### baseCamp Paper 05 — Cross-Species Signaling
- Multi-species QS in symbiotic systems (lichen, rhizobia, coral)
- Directly relevant to insect symbiont engineering:
  - Bee gut = 3D biofilm → QS predicted active
  - Aphid bacteriome = near-monoculture (*Buchnera*) → low W, deep extended regime
  - Anderson predicts engineered symbionts must maintain 3D geometry for coordinated gene expression

### baseCamp Paper 04 — Sentinels
- ESN regime classifier for community monitoring
- Could classify evolutionary regimes in LTEE populations from genomic features
- Same architecture classifies pre-citrate vs post-citrate Ara-3

### baseCamp Paper 16 — Anaerobic-Aerobic QS
- MSUBI fermentation experience → Anderson framework for bioreactors
- LTEE is aerobic, but biofilm experiments would create microaerobic zones
- Gut symbionts (bee, aphid) span aerobic/anaerobic

---

## Spring Opportunities — What Their Lab Needs

### wetSpring
| Their Need | Our Capability | Spring Module |
|-----------|---------------|---------------|
| 16S/WGS analysis of LTEE populations | Sovereign 16S/DADA2/taxonomy pipeline | wetSpring Exp001-070 |
| QS gene annotation across evolving populations | HMM profiles for QS genes | wetSpring Exp140-142 |
| Diversity/evenness tracking over 82K generations | Anderson disorder mapping from community data | wetSpring Exp127-143 |
| Metagenome analysis of insect gut symbionts | NCBI sovereign pipeline, Bray-Curtis GPU | wetSpring Exp184-185 |
| Strain collection database management | NestGate data pipelines | wetSpring NestGate NCBI |

### neuralSpring
| Their Need | Our Capability | Spring Module |
|-----------|---------------|---------------|
| Mutation trajectory analysis | LSTM time-series prediction (R²=0.98) | neuralSpring nW-03 |
| Evolutionary regime classification | ESN classifier (96.5% accuracy) | neuralSpring nW-05 |
| Introgression/HGT detection in symbionts | HMM/PhyloNet-HMM | neuralSpring Papers 016-018 |
| ML for synthetic biology burden prediction | Transfer learning framework | neuralSpring Exp 004 |
| breseq enhancement / complementary analysis | Spectral analysis of mutation spectra | neuralSpring spectral primitives |

### groundSpring
| Their Need | Our Capability | Spring Module |
|-----------|---------------|---------------|
| Drift vs selection quantification in LTEE | Wright-Fisher fixation probability, Kimura neutral theory | groundSpring Exp 014 |
| Error bars on population genomic measurements | Jackknife estimation (subpercent precision) | groundSpring Exp 019 |
| Rare mutant lineage detection thresholds | Rare biosphere signal detection | groundSpring Exp 016 |
| Quasispecies threshold for LTEE mutation rates | Eigen error threshold | groundSpring Exp 017 |
| Sequencing depth requirements for frozen fossils | Rarefaction curves + saturation analysis | groundSpring Exp 004 |

### hotSpring / coralReef
| Their Need | Our Capability | Spring Module |
|-----------|---------------|---------------|
| Protein structure tracking across 82K generations | coralForge: AlphaFold2/3 primitives (154 checks) | coralForge LTEE application |
| Structural evolution of key mutations (citrate) | Sovereign structure prediction pipeline | coralForge 06_LTEE_APPLICATION.md |
| GPU-accelerated phylogenetic analysis | GPU spectral methods, Lanczos eigensolves | hotSpring spectral theory |

### airSpring
| Their Need | Our Capability | Spring Module |
|-----------|---------------|---------------|
| Agricultural soil microbiome connections | FAO-56 water balance, soil QS framework | airSpring + Paper 06 |
| Field deployment of microbial sentinels | NPU edge inference for community monitoring | airSpring NPU pipeline |

### healthSpring
| Their Need | Our Capability | Spring Module |
|-----------|---------------|---------------|
| Bee/aphid gut as microbiome model | Anderson gut lattice, anaerobic QS | healthSpring Exp032 |
| Symbiont PK/PD (engineered gene expression levels) | Hill dose-response, PK modeling | healthSpring Track 1 |

### Infrastructure
| Their Need | Our Capability | Module |
|-----------|---------------|--------|
| Reproducible computational pipelines | Rust-based validated binaries with provenance | All springs |
| GPU-accelerated genomics | barraCuda standalone math primal | barraCuda v0.3.7 |
| Strain collection database | NestGate content-addressed storage | NestGate |
| Lab data management + visualization | petalTongue dashboards | petalTongue |
| Secure multi-user compute | ironGate JupyterHub with tier isolation | projectNUCLEUS |

---

## Synergy: Computation They Don't Have

### 1. Anderson Framework for LTEE
Nobody has applied Anderson localization to LTEE populations. The predictions are specific:
- sdiA expression should differ in biofilm (3D) vs planktonic (shaken flask)
- W_eff = W_base / occupancy → planktonic dilution suppresses QS
- Testable with existing strains, standard reporter assays

### 2. Sovereign Bioinformatics
breseq is C++ and R — mature but not GPU-accelerated. We bring:
- GPU-accelerated diversity analysis (barraCuda)
- Sovereign NCBI pipeline (no institutional API dependencies)
- Validated Rust pipelines with provenance tracking

### 3. Structure Prediction for Evolutionary Analysis
coralForge can track how protein structures change across 82,000 generations:
- Predict structures for ancestral vs evolved alleles
- Map structural consequences of key mutations (citrate pathway)
- Compare across replicates to identify structural convergence

### 4. Edge Deployment for Field Applications
Insect symbiont monitoring in field conditions:
- NPU inference for real-time community classification
- Sentinel architecture for hive health monitoring
- MinION + AKD1000 for field genomics

### 5. ML for Evolutionary Dynamics
Beyond breseq's deterministic mutation calling:
- ESN regime classification for identifying evolutionary transitions
- LSTM prediction of mutation accumulation trajectories
- Transfer learning across LTEE replicates (constrained evolution prediction)

---

## Papers to Reproduce / Validate in Springs

### Priority 1: LTEE Core (wetSpring + neuralSpring + groundSpring)
1. **Wiser et al. 2013** — Power-law fitness dynamics. Reproduce power-law fit, validate with groundSpring jackknife error bars
2. **Tenaillon et al. 2016** — Tempo and mode at 50K generations. Mutation accumulation patterns, parallel evolution scoring
3. **Good et al. 2017** — Molecular evolution at 60K generations. Allele frequency trajectories, clonal interference dynamics
4. **Blount et al. 2008/2012** — Citrate innovation. Historical contingency analysis, potentiating mutation detection

### Priority 2: breseq Validation (wetSpring)
5. **Deatherage & Barrick 2014** — breseq pipeline. Compare our Rust 16S/WGS pipeline against breseq output on same datasets
6. **Barrick & Lenski 2010** — Mutation diversity. Reproduce diversity metrics with Anderson framework overlay

### Priority 3: Insect Symbionts (wetSpring + healthSpring)
7. **Leonard et al. 2024** — Bee gut engineering. Map engineered symbiont QS potential via Anderson geometry
8. **Buchnera genomes 2024** — 29 genomes. Structural analysis via coralForge, diversity analysis via wetSpring

### Priority 4: Synthetic Biology (neuralSpring)
9. **BioBrick burden 2024** — 301 plasmids. ML prediction of burden from sequence features, Anderson disorder as burden proxy

---

## Next Steps

1. ✅ Interview prep document created (whitePaper/interview_prep_barrick_lenski_RA2.md)
2. ✅ Contact file created
3. ✅ Initial Zoom interview with Barrick (May 11) — went well
4. 🔄 **In-person interview** — schedule one of: Fri 5/15, Mon 5/18, Tue 5/19
5. 🔄 **Build LTEE guideStone USB** for in-person interview (see gen4/architecture/GUIDESTONE_LTEE.md)
6. ⏳ Meet Rich Lenski at in-person interview
7. ⏳ If hired: Begin LTEE Paper 02 validation with real LTEE data
8. ⏳ Propose Anderson-QS experiments using LTEE strains
9. ⏳ Integrate breseq output into wetSpring analysis pipeline
