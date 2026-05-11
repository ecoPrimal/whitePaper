# Eaves / Woldring Lab — Paper Review & Spring Integration Targets

**Purpose**: Identify Woldring Lab papers to reproduce/validate in springs, computational gaps we can fill, and synergy opportunities.

---

## WOLDRING LAB PAPERS

---

### Paper E1: Woldring et al. — "A gradient of sitewise diversity promotes evolutionary fitness" (*Biochemistry* 2017)

**What they found:**
- Studied a three-helix bundle protein scaffold for binder discovery
- Sitewise diversity gradient (not uniform randomization) produces better libraries
- Evolutionary fitness of library members increases when diversity is structured

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| wetSpring | Anderson disorder analogy: sitewise diversity = Anderson W at each lattice site. Structured diversity = correlated disorder (Exp 151). Predicts which library positions tolerate randomization vs which need conservation | Theory: protein_library_Anderson |
| neuralSpring | ML prediction of binding affinity from sequence diversity profile | New Exp: library_binding_ML |
| coralForge | Structure prediction for top/bottom library members; structural basis for diversity tolerance | New Exp: library_structure |

**Computational gap we fill:**
- Anderson framework maps directly: protein positions = lattice sites, amino acid diversity = disorder W
- Positions with high structural constraint = low W (extended regime, conserved)
- Positions tolerating randomization = high W (localized regime, variable)
- This predicts which positions to diversify without exhaustive experimental screening

---

### Paper E2: Mardikoraem & Woldring 2025 — "HOLIgraph" (*J Cheminformatics*)

**What they found:**
- Heterogeneous OATP-ligand interaction graph neural network
- Predicts inhibitors of OATP1B1 (drug transporter)
- Graph neural network approach to protein-ligand interactions

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| neuralSpring | GNN for protein-ligand prediction — extends ML capabilities | New Exp: GNN_protein_ligand |
| coralForge | Structure prediction for OATP1B1 variants; docking validation | New Exp: OATP_structure |
| healthSpring | Drug transporter modeling connects to PK/PD Track 1 (OATPs affect drug bioavailability) | Extension of healthSpring PK/PD |

**Computational gap we fill:**
- GPU-accelerated GNN inference via barraCuda
- Sovereign structure prediction for OATP variants (no cloud dependency)
- Integration with healthSpring PK/PD models (transporter kinetics → drug levels)
- OATPs are gatekeepers for drug absorption — this bridges protein engineering and pharmacology

---

### Paper E3: Dolgikh, Schulte & Woldring 2025 — "Tuning Yeast Glycosylation for FLS2" (bioRxiv preprint)

**What they found:**
- Engineered yeast glycosylation near FLS2-flg22 binding interface
- Enabled functional yeast surface display under ER stress
- Plant immunity receptor engineered for high-throughput screening

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| coralForge | Structural modeling of glycosylation site effects on FLS2 binding | New Exp: FLS2_glycosylation |
| neuralSpring | ML prediction of glycosylation effects on binding affinity | New Exp: glycosylation_binding_ML |
| airSpring | Plant immunity receptor (FLS2 detects bacterial flagellin) — connects to agricultural microbiome sentinel work (Paper 04) | Theory: plant_immunity_sentinel |

**Computational gap we fill:**
- Glycosylation modeling is computationally expensive — GPU acceleration matters
- FLS2 is a plant innate immunity receptor → bridges to our agricultural springs
- Predicting glycosylation effects on binding without experimental iteration saves weeks per construct

---

### Paper E4: Woldring Lab — "Screening macrocyclic peptide libraries by yeast display" (bioRxiv 2024)

**What they found:**
- Yeast display for macrocyclic peptide screening
- Control over selection process and affinity ranking
- High-throughput binder discovery

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| neuralSpring | ML ranking of binders from sequence features; transfer learning from linear → cyclic peptides | New Exp: macrocyclic_ranking |
| coralForge | Structure prediction for cyclic peptides bound to targets | New Exp: cyclic_peptide_structure |
| healthSpring | Drug discovery pipeline connection: cyclic peptides → ADDRC library → Gonzales validation | Cross-contact bridge |

**Computational gap we fill:**
- Cyclic peptide structure prediction is harder than linear — conformational sampling is expensive
- ML ranking before synthesis prioritizes the most promising candidates
- Connects to Gonzales/ADDRC drug discovery pipeline for AD therapeutics

---

### Paper E5: Woldring Lab — "Single-Cell B-cell Sequencing for Natively-paired scFab Yeast Surface Display Libraries" (2023)

**What they found:**
- Single-cell B-cell sequencing to generate natively-paired antibody fragment libraries
- Yeast surface display for functional screening of native immune repertoires

**Spring targets:**
| Spring | What to Reproduce | Experiment |
|--------|-------------------|------------|
| wetSpring | Single-cell sequencing analysis pipeline (sovereign, Rust-based) | New Exp: scFab_pipeline |
| neuralSpring | Antibody pairing prediction from single-cell data; ML for VH/VL pairing | New Exp: antibody_pairing_ML |
| coralForge | Structure prediction for scFab fragments; paratope modeling | New Exp: scFab_structure |

**Computational gap we fill:**
- Single-cell sequencing generates massive data — GPU acceleration for alignment and clustering
- Native pairing prediction (which VH goes with which VL) is an unsolved ML problem
- Sovereign pipeline avoids cloud sequencing analysis dependency

---

## WOLDRING LAB METHODS CHAPTERS (2022)

Three book chapters establish their computational methodology:

### M1: Machine Learning-Driven Library Design
- ML for protein library design — directly overlaps neuralSpring capabilities
- Opportunity: benchmark our LSTM/ESN architectures against their published approaches

### M2: Site-Wise Diversification
- Computational methods for deciding which positions to diversify
- Opportunity: Anderson disorder framework as alternative/complementary prediction method

### M3: Ancestral Sequence Reconstruction for Directed Evolution
- ASR to identify ancestrally stable scaffolds for engineering
- Opportunity: coralForge structural comparison of ancestral vs modern sequences

---

## CONNECTION TO OTHER CONTACTS

### Eaves/Woldring ↔ Barrick
| Connection | Woldring/Eaves Side | Barrick Side | Our Bridge |
|-----------|--------------------|--------------|----|
| Directed evolution | Yeast display = engineered directed evolution | LTEE = natural directed evolution (82K gen) | Anderson framework: same fitness landscape physics, different timescales |
| Protein engineering | Protein library design, structure-function | Insect symbiont engineering (RNAi, chromosomal edits) | coralForge structure prediction for both |
| ML for biology | HOLIgraph (GNN for protein-ligand) | breseq (deterministic mutation calling) | neuralSpring: unified ML stack for genomics + proteomics |
| Constrained evolution | Library screening: structured diversity under selection | LTEE: 12 populations under identical constraint | baseCamp Paper 02 + library Anderson model |
| Synthetic biology | Yeast display circuit engineering | BioBrick burden, constructability limits | Anderson disorder theory for genetic circuit burden |

### Eaves/Woldring ↔ Gonzales
| Connection | Woldring/Eaves Side | Gonzales Side | Our Bridge |
|-----------|--------------------|--------------|----|
| Drug discovery | Macrocyclic peptides, protein binder engineering | ADDRC screening, iPSC validation for AD | healthSpring drug discovery pipeline |
| Drug transporters | OATP1B1 prediction (HOLIgraph) | Drug absorption/bioavailability for AD therapeutics | healthSpring PK/PD models |
| High-throughput screening | Yeast display libraries | iPSC-derived keratinocytes | neuralSpring ML for hit prediction |
| Plant immunity | FLS2 receptor engineering | One Health: environment → skin → disease | airSpring sentinel framework |

---

## REPRODUCTION PRIORITY QUEUE

### Tier 1 — High impact, Zoom call conversation starters
1. **HOLIgraph (E2)** → neuralSpring (GNN) + healthSpring (PK/PD) — most recent, most computational
2. **Library diversity (E1)** → wetSpring (Anderson disorder in protein libraries) — foundational, connects theory

### Tier 2 — Demo-ready for lab mates
3. **Macrocyclic peptides (E4)** → coralForge structure + neuralSpring ML ranking
4. **scFab libraries (E5)** → wetSpring sovereign pipeline + coralForge paratope modeling

### Tier 3 — Longer-term collaboration
5. **FLS2 glycosylation (E3)** → coralForge structural + airSpring plant immunity
6. **Methods chapters (M1-M3)** → benchmark neuralSpring ML against published approaches

---

## WHAT TO DISCUSS ON ZOOM

### For Joelle directly
- Anderson disorder framework for sitewise library diversity (Paper E1) — novel angle on her existing work
- GPU-accelerated structure prediction via coralForge — relevant to any protein engineering lab
- Reproducible pipelines in Rust vs Python notebooks — reliability for dissertation work

### For lab mates (via Joelle)
- HOLIgraph GNN: can we run inference faster on ironGate GPUs?
- Macrocyclic peptide screening: ML pre-ranking before yeast display
- Single-cell sequencing analysis: sovereign pipeline for scFab data
- General compute bottlenecks: what takes too long on their current hardware?

### For Woldring (faculty connection)
- Anderson localization as unified theory for directed evolution fitness landscapes
- coralForge as structural complement to their sequence-based approaches
- ironGate as departmental compute resource for protein engineering
