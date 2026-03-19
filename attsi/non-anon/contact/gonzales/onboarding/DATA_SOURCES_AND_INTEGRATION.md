<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# Data Sources and Integration Strategy

**Audience:** Gonzales Lab, ADDRC, Drug Discovery Program
**Purpose:** Map free/open data → validated computational models → internal
data integration. Start immediately with public data; layer internal data
as access develops.

---

## Phase 1: Public Data (Day 1 — No Approvals Needed)

### Drug Target / Binding Data

| Source | What You Get | Size | Our Use | Access |
|--------|-------------|:----:|---------|--------|
| **PubChem BioAssay** | Dose-response curves, IC50, EC50 for millions of compound-target pairs | 1.5M+ assays | Calibrate low-affinity binding models; build cross-target selectivity matrices | Free API: `ncbi.nlm.nih.gov/pcassay` |
| **ChEMBL 34** | Curated bioactivity data: 2.4M compounds, 15K targets, 20M activities | ~2 GB download | MATRIX scoring calibration; identify compounds with broad-weak profiles | Free: `ebi.ac.uk/chembl` |
| **BindingDB** | 2.8M experimentally measured binding affinities | ~1 GB | Ground truth for affinity landscape analysis; Kd/Ki distributions | Free: `bindingdb.org` |
| **DrugBank** | 14K+ drug entries with targets, pathways, PK parameters, ADMET | Free academic | Cross-species PK parameters; allometric scaling validation | Academic license |
| **ZINC20** | 1.4B purchasable compounds with predicted properties | Variable | Compound selection for virtual screens | Free: `zinc20.docking.org` |

**What we compute on Day 1:**
- IC50 distributions across JAK pathway targets (PubChem)
- Cross-reactivity matrices for known AD drugs (ChEMBL)
- Binding breadth analysis: which drug classes have broad-weak profiles (ChEMBL)

### Pharmacokinetic / Clinical Data

| Source | What You Get | Our Use | Access |
|--------|-------------|---------|--------|
| **FDA Orange Book** | Approved drug products, therapeutic equivalences | PK parameter reference, cross-species bridging | Free: `fda.gov` |
| **Drugs@FDA** | Label information, clinical pharmacology reviews | Published human PK parameters | Free: `accessdata.fda.gov` |
| **Published literature** | Gonzales G1–G6, Fajgenbaum MATRIX, Phase III trials | Already reproduced: 782/782 checks | PubMed |
| **Harman 2001 (BLSA)** | Age-related testosterone decline data | Track 4 (TRT outcomes) validation | Published |
| **Saad 2013 registry** | TRT metabolic response (n=411) | TRT outcome modeling | Published |

### Microbiome / Genomics

| Source | What You Get | Our Use | Access |
|--------|-------------|---------|--------|
| **NCBI SRA** | Raw sequencing reads (16S, shotgun metagenomes) | Anderson W computation, diversity baselines | Free: `ncbi.nlm.nih.gov/sra` |
| **HMP Phase II** | Healthy human gut microbiome profiles | Baseline gut Anderson W for colonization resistance | Free: `hmpdacc.org` |
| **EMP (Earth Microbiome Project)** | 30,000+ samples across environments | Cross-environment Anderson framework validation | Free: `earthmicrobiome.org` |
| **curatedMetagenomicData** | Curated human gut 16S and shotgun data | Disease-associated W shifts | Free: Bioconductor |

### Biosignal / Physiological

| Source | What You Get | Our Use | Access |
|--------|-------------|---------|--------|
| **MIT-BIH Arrhythmia** | 48 half-hour annotated ECG records | Beat classification templates | Free: `physionet.org` |
| **MIMIC-III** | ICU patient records + continuous biosignals | Multi-modal health assessment | Free (with credentials) |
| **PTB-XL** | 21,799 12-lead ECG records | ECG classification at scale | Free: `physionet.org` |

### Protein Structure / Receptor

| Source | What You Get | Our Use | Access |
|--------|-------------|---------|--------|
| **PDB / RCSB** | 200K+ protein structures | Target geometry for Anderson tissue models | Free: `rcsb.org` |
| **UniProt** | Protein sequences + functional annotations | IL-31RA, IL-4Rα, OSMR receptor mapping | Free: `uniprot.org` |
| **AlphaFold DB** | Predicted structures for 200M+ proteins | Target modeling where crystal structures missing | Free: `alphafold.ebi.ac.uk` |

---

## Phase 2: Internal Data (Month 1–3, Pending Access)

### ADDRC Compound Library (Lisabeth)

| Data | What It Contains | Integration Path |
|------|-----------------|-----------------|
| **8K compound dose-response** | Full 10-point curves per compound per target | Feed into affinity_landscape module → composite binding scores, Gini breadth metrics, toxicity IPR |
| **Brucella screen (2024)** | 8K compounds screened against Brucella host pathways | Proof-of-concept reanalysis: find function in "inactive" compounds |
| **GREENScreen metadata** | Compound MW, delivery route, target pathway | Input to Anderson-augmented MATRIX scoring |
| **HTS quality metrics** | Z', SSMD, signal-to-background per assay plate | Validate exp091 (HTS analysis) against real data |

**Integration workflow:**
```
GREENScreen CSV export
    → healthSpring ingest (IC50, Hill slope, Emax per compound)
    → composite_binding_score() across target panels
    → toxicity_ipr() for organ-specific risk ranking
    → hormetic_optimum() for biphasic candidates
    → Anderson-augmented MATRIX scoring
    → Ranked priority list + tissue geometry rationale
```

### Gonzales iPSC Readouts

| Data | What It Contains | Integration Path |
|------|-----------------|-----------------|
| **iPSC cytotoxicity** | Viability data for canine/feline/human iPSC lines | Validate delocalized toxicity prediction (H2) |
| **IL-31 response data** | Pruritus model readouts | Refine dose-response model parameters |
| **Barrier function assays** | TEER, permeability, cornified envelope integrity | Anderson dimensional promotion validation |
| **Cross-species readouts** | Same assay across species iPSC lines | Allometric scaling validation (H6) |

**Integration workflow:**
```
iPSC experimental readout (Excel/CSV)
    → healthSpring ingest
    → Compare predicted vs observed for low-affinity compounds
    → Refine Anderson model parameters with real tissue data
    → Generate next round of computational predictions
    → Design next experiment
```

### Future Clinical Data (Longer Term)

| Data | Context | Integration |
|------|---------|-------------|
| Companion animal clinical outcomes | Gonzales Zoetis network | Validate cross-species PK predictions |
| Human clinical trial data (if applicable) | Collaboration dependent | Population PK Monte Carlo calibration |
| Real-time biosignal data | Wearable / clinical monitor | Sovereign biosignal pipeline validation |

---

## Phase 3: Cross-Spring Data Integration

Internal data doesn't just feed healthSpring. It enriches the entire ecosystem:

```
ADDRC dose-response → healthSpring affinity landscape
    → wetSpring colonization resistance models
    → airSpring pesticide hormesis predictions
    → groundSpring uncertainty budgets

Gonzales iPSC → healthSpring tissue validation
    → wetSpring Anderson immunological framework refinement
    → neuralSpring ESN regime classifier training
```

Every spring benefits from better parameters. The public data builds the
framework; the internal data makes it precise.

---

## Data Sovereignty

All data stays local:
- Public data: downloaded once, stored on biomeGate or lab workstation
- Internal data: never leaves lab hardware
- ICER: binary runs on ICER GPU, data stays on biomeGate (NUCLEUS dispatch)
- No cloud uploads, no third-party analytics, no data governance issues
- Every computation produces a signed provenance record (BearDog Ed25519)

The lab owns its data. The computation serves the lab, not the other way around.
