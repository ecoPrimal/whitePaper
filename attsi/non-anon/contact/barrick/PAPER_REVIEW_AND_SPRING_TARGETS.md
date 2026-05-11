# Barrick/Lenski + Eaves/Woldring — Paper Review & Spring Integration Targets

**Purpose**: Identify papers to reproduce/validate in springs, computational gaps we can fill, and synergy opportunities for both contacts.

---

## PART A: BARRICK / LENSKI PAPERS

---

### Paper B1: Barrick et al. 2009 — "Genome evolution and adaptation" (*Nature*)

**What they found:**
- Genomic and adaptive evolution are **decoupled**: adaptation decelerated but genomic change stayed clock-like for 20K generations
- Beneficial substitutions were surprisingly uniform over time
- Later, elevated mutation rate evolved → hundreds of additional neutral mutations
- Key specific mutation: 1-bp insertion upstream of *glmUS* (cell-wall biosynthesis), +5% fitness, swept 500–1,500 generations, unique to one population

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| groundSpring | Clock-like mutation rate → jackknife confidence intervals, drift vs selection classification of each mutation | New Exp: LTEE_mutation_clock |
| neuralSpring | LSTM time-series prediction of mutation accumulation curves; ESN regime classifier for mutation-rate shift detection | New Exp: LTEE_mutation_trajectory |
| wetSpring | Reproduce diversity metrics (Shannon, Pielou) from published OTU-like data; Anderson disorder mapping for each population | Extension of Exp140-142 |

**Computational gap we fill:**
- They identified beneficial vs neutral mutations via population genetics. Our groundSpring Exp 014 (drift vs selection, Wright-Fisher) and Exp 017 (quasispecies threshold) provide independent quantitative classification
- ESN regime classifier (nW-05) can detect the mutation-rate transition automatically from allele frequency time series

---

### Paper B2: Wiser, Ribeck & Lenski 2013 — "Long-term dynamics of adaptation" (*Science*)

**What they found:**
- Fitness follows **power law** W(t) = (1 + αt)^β, not an asymptote
- Power law predicted 20K→50K fitness accurately; asymptotic model failed
- Theoretical derivation from **clonal interference + diminishing-returns epistasis**
- Estimated beneficial mutation rate and epistasis strength

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| groundSpring | Power-law fit with jackknife error bars (Exp 019); compare against asymptotic model using AIC/BIC | New Exp: LTEE_power_law_fitness |
| neuralSpring | LSTM prediction: train on 0-20K, predict 20K-50K, compare to power law; ESN regime detection at any inflection points | New Exp: LTEE_fitness_prediction |
| hotSpring | Population genetic parameters → Anderson disorder analogy: beneficial mutation rate maps to lattice hopping parameter | Theory connection to Paper 01 |

**Computational gap we fill:**
- Their fit was least-squares. We provide: (1) jackknife uncertainty, (2) ML prediction as independent validation, (3) Bayesian model comparison (power-law vs asymptotic vs hyperbolic), (4) cross-replicate transfer learning (train on 6 populations, predict other 6)

---

### Paper B3: Good et al. 2017 — "Dynamics of molecular evolution over 60,000 generations" (*Nature*)

**What they found:**
- Whole-genome metagenomic sequencing at 500-generation intervals across all 12 populations
- **Allele frequency trajectories** reconstructed — mutations tracked from emergence to fixation/loss
- Multiple beneficial variants competing simultaneously (clonal interference)
- Long-term **quasi-stable coexistence** of competing clades in most populations
- **Epistasis and historical contingency** altered selection strength on different genes over time

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| neuralSpring | LSTM for allele frequency trajectory prediction; HMM for clade state detection (hidden states = competing clades); ESN for regime classification (sweep vs interference vs coexistence) | New Exp: LTEE_allele_dynamics |
| groundSpring | Jackknife on allele frequency estimates; rare biosphere detection (Exp 016) for emerging low-frequency variants; quasispecies threshold for when clonal interference dominates | New Exp: LTEE_clonal_interference |
| wetSpring | Anderson framework: competing clades = multi-species community. Pielou evenness of clade frequencies → disorder W → do clades that maintain 3D biofilm structure show different evolutionary dynamics? | Theory extension of Paper 02 |

**Computational gap we fill:**
- This is their most data-rich paper. The allele trajectory data is perfect for:
  1. LSTM sequence prediction (neuralSpring nW-03 architecture)
  2. HMM hidden-state inference for clade dynamics (neuralSpring Papers 016-018)
  3. ESN real-time regime detection (clonal sweep vs interference vs coexistence)
  4. Transfer learning across 12 populations (constrained evolution prediction)
- The data is available on NCBI (BioProject) — our sovereign NCBI pipeline can ingest it

---

### Paper B4: Blount et al. 2008, 2012 — Citrate Innovation in Ara-3

**What they found:**
- One of 12 populations (Ara-3) evolved ability to grow on citrate — a key innovation
- Required **potentiating mutations** (historical contingency)
- Molecular basis: tandem duplication placed *citT* (citrate transporter) under an aerobic promoter
- Only possible after prior mutations restructured the genome region

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| coralForge | Structural prediction of ancestral vs mutant CitT protein; structural consequences of the tandem duplication | New Exp: LTEE_citrate_structure |
| groundSpring | Probability of potentiating mutation cascade: rare event statistics, Poisson process modeling | New Exp: LTEE_contingency_probability |
| neuralSpring | Detect pre-potentiating mutations from allele trajectories (early warning of innovation) | Extension of LTEE_allele_dynamics |

**Computational gap we fill:**
- coralForge can predict how the structural change from the tandem duplication affects CitT function
- groundSpring rare event statistics (Exp 016) quantify exactly how improbable the innovation was
- The "early warning" detection of pre-potentiating mutations is a perfect ESN application

---

### Paper B5: Leonard et al. 2024 — "One-step genome engineering in bee gut symbionts" (*mBio*)

**What they found:**
- Chromosomal gene deletions and insertions in *S. alvi*, *S. communis*, *B. apis*
- No exogenous recombination machinery needed — uses natural recombination
- Enables functional studies of symbiont genes in the bee gut

**Spring targets:**
| Spring | What to Reproduce/Connect | Experiment |
|--------|--------------------------|------------|
| wetSpring | Anderson-QS prediction: bee gut is 3D biofilm → engineered symbionts maintain QS-active geometry → coordinated RNAi expression depends on spatial structure | Extension of Paper 05 |
| healthSpring | Symbiont-mediated gene expression as PK/PD problem: dose (colonization density) → response (RNAi knockdown level) modeled as Hill equation | New Exp: symbiont_PKPD |
| coralForge | Structure prediction for engineered symbiont proteins; stability assessment of insertions | New Exp: symbiont_stability |

**Computational gap we fill:**
- Anderson geometry predictions for when engineered symbionts will/won't coordinate gene expression
- PK/PD modeling of symbiont colonization → gene expression → host phenotype cascade
- Nobody else is modeling the spatial biology of engineered gut symbionts

---

### Paper B6: "Measuring the burden of hundreds of BioBricks" 2024 (*Nature Communications*)

**What they found:**
- 301 BioBrick plasmids tested for metabolic burden
- 19.6% were burdensome (depleting gene expression resources)
- No BioBrick reduced growth >45% — evolutionary limit on constructability
- Aligns with population genetic models

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| neuralSpring | ML prediction of burden from sequence features (GC content, codon usage, promoter strength, etc.) | New Exp: BioBrick_burden_ML |
| groundSpring | Anderson disorder analogy: burden = disorder introduced into cellular gene expression landscape. Predict constructability limit from Anderson W_c | Theory: BioBrick_Anderson |

**Computational gap we fill:**
- ML prediction of burden before building the construct (save experimental effort)
- Anderson framework provides a physical theory for WHY there's a constructability limit — gene expression resources scatter through the disordered plasmid landscape

---

### Paper B7: Tenaillon et al. 2016 — "Tempo and mode of genome evolution" (*Nature*)

**What they found:**
- 264 complete genomes across 12 populations at 50,000 generations
- Most fixed mutations **beneficial** in populations with ancestral mutation rate
- Fraction of beneficial mutations **declined** as fitness increased (diminishing returns)
- Neutral mutations accumulated at constant rate
- Nonsynonymous, intergenic, insertions, and deletions **overrepresented** → selection signature
- Data publicly available on NCBI BioProject + breseq on GitHub

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| wetSpring | Download 264 genomes from NCBI BioProject via sovereign pipeline; reproduce mutation accumulation curves per population | New Exp: LTEE_264_genomes |
| groundSpring | Beneficial vs neutral mutation classification with confidence intervals; diminishing returns epistasis quantification | New Exp: LTEE_epistasis_quantification |
| neuralSpring | ML detection of parallel evolution (same genes mutated independently across populations); transfer learning for mutation category prediction | New Exp: LTEE_parallel_evolution |

**Computational gap we fill:**
- 264 genomes × breseq → our Rust pipeline can reproduce and extend
- GPU-accelerated phylogenetic analysis for all 12 population trees simultaneously
- Anderson disorder mapping: nonsynonymous enrichment = "selection lattice" with disorder

---

### Paper B8: Barrick & Waters 2025 — "Phages use contingency loci as bet-hedging" (bioRxiv)

**What they found:**
- Bacteriophage genomes contain contingency loci (hypermutable DNA regions)
- Widespread across phage genomes, encoded in all functional gene classes (T2, T4, T6, T7)
- Generate genetic diversity to evade host defenses — bet-hedging strategy

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| wetSpring | HMM identification of contingency loci across phage genomes; compare hypermutable region detection methods | New Exp: phage_contingency_loci |
| groundSpring | Mutation rate heterogeneity across genome positions; bet-hedging as mixed strategy Nash equilibrium | Theory: phage_bet_hedging_stats |
| neuralSpring | ML prediction of contingency loci from sequence features; Anderson disorder: hypermutable = high W positions | New Exp: phage_contingency_ML |

**Computational gap we fill:**
- Contingency loci detection via HMM (neuralSpring Papers 016-018 architecture)
- Anderson framework: contingency loci = intentional high-disorder positions in the phage genome lattice
- Connects to LTEE: phage-host coevolution may drive some LTEE mutation dynamics

---

### Paper B9: DFE Evolution in LTEE 2024 (*Science*, Baym/Tenaillon/Couce collaboration)

**What they found:**
- Distribution of fitness effects (DFE) changes over evolutionary time
- Loss-of-function mutations studied across LTEE populations
- Merged complementary studies from two research teams

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| groundSpring | DFE fitting: exponential, gamma, lognormal distributions; track DFE parameter changes over time with jackknife CI | New Exp: LTEE_DFE_dynamics |
| neuralSpring | LSTM prediction of DFE parameters at generation t+1 from history; ESN detection of DFE regime shifts | New Exp: DFE_prediction |
| hotSpring | Fisher's geometric model → Anderson lattice analogy: DFE as eigenvalue distribution of random Hamiltonian | Theory: DFE_Anderson_RMT |

**Computational gap we fill:**
- Random Matrix Theory connection: DFE eigenvalue distributions are formally related to Anderson model spectra
- This is deep theoretical territory — Wigner-Dyson → DFE shape, Marchenko-Pastur → epistasis effects
- Nobody has made this connection explicit for experimental evolution data

---

## PART B: CROSS-CONTACT SYNERGIES

> **Eaves/Woldring papers reviewed separately**: see `../eaves/PAPER_REVIEW_AND_SPRING_TARGETS.md`

### Barrick ↔ Woldring/Eaves
| Connection | Barrick Side | Woldring/Eaves Side | Our Bridge |
|-----------|-------------|--------------------|----|
| Directed evolution | LTEE = natural directed evolution (82K gen) | Yeast display = engineered directed evolution | Anderson framework: same fitness landscape physics, different timescales |
| Protein engineering | Insect symbiont engineering (RNAi, chromosomal edits) | Protein library design, structure-function | coralForge structure prediction for both |
| ML for biology | breseq (deterministic mutation calling) | HOLIgraph (GNN for protein-ligand) | neuralSpring: unified ML stack for genomics + proteomics |
| Constrained evolution | LTEE: 12 populations under identical constraint | Library screening: structured diversity under selection | baseCamp Paper 02 + library Anderson model |
| Synthetic biology | BioBrick burden, constructability limits | Yeast display circuit engineering | Anderson disorder theory for genetic circuit burden |

### Barrick ↔ Gonzales (existing contact)
| Connection | Barrick | Gonzales | Our Bridge |
|-----------|---------|---------|-----------|
| Drug discovery | BioBrick burden prediction → constructability | ADDRC screening → iPSC validation | neuralSpring ML pipeline |
| Microbiome | Bee/aphid gut symbionts | Skin microbiome in AD | Anderson-QS framework (Papers 01, 05, 12) |
| Engineering | Symbiont-mediated gene expression | iPSC-derived tissue models | healthSpring PK/PD modeling |

---

## PART C: REPRODUCTION PRIORITY QUEUE (Barrick/Lenski only)

### Tier 1 — Reproduce Now (high impact, data publicly available)
1. **Wiser 2013 power-law fitness** → groundSpring (jackknife + model comparison)
2. **Good 2017 allele trajectories** → neuralSpring (LSTM + ESN + HMM)
3. **Barrick 2009 mutation clock** → groundSpring (drift vs selection) + neuralSpring (regime detection)
4. **Tenaillon 2016 — 264 genomes** → wetSpring (sovereign NCBI ingest) + neuralSpring (parallel evolution detection)

### Tier 2 — Reproduce with Lab Access / Recent Data
5. **DFE evolution 2024 (Science)** → groundSpring (DFE fitting) + hotSpring (RMT connection)
6. **Blount 2008/2012 citrate** → coralForge (structural) + groundSpring (rare events)
7. **BioBrick burden 2024** → neuralSpring (ML prediction)
8. **Bee gut RNAi 2022/2024** → wetSpring (Anderson-QS) + healthSpring (PK/PD)
9. **Phage contingency loci 2025** → wetSpring (HMM detection) + neuralSpring (ML prediction)

### Tier 3 — Long-Term Theoretical
10. Anderson-QS predictions for LTEE biofilm experiments (Paper 02)
11. Anderson disorder theory for constructability limits (BioBrick)
12. Cross-species Anderson for insect gut symbionts (Paper 05 extension)
13. Random Matrix Theory ↔ DFE ↔ Anderson localization connection
14. Phage bet-hedging as Anderson intentional-disorder strategy

> **Eaves/Woldring reproduction queue**: see `../eaves/PAPER_REVIEW_AND_SPRING_TARGETS.md`
