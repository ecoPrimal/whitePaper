<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# Gonzales Lab — Computational Onboarding Package

**Author:** Kevin Mok (mokkevin@msu.edu)
**Position:** Research Assistant III — Gonzales Lab, Dept. of Pharmacology & Toxicology
**Date:** March 19, 2026
**For:** Dr. Andrea Gonzales (Professor, Director of MSU Drug Discovery Program)
**Purpose:** What I bring to the lab on Day 1, and what we can build together.

---

## Executive Summary

I bring a validated computational pipeline — tested against 782 of Dr.
Gonzales's published data points — that replaces $210K/year of commercial
pharmacometric software (NONMEM, Monolix, WinNonlin) with free, open-source
code. The pipeline has 809 automated tests, 83 validated experiments, and
8 grant-ready hypotheses designed around existing ADDRC infrastructure.

I also bring biomeGate, a multi-GPU workstation (96 GB total GPU memory,
native 64-bit precision) that can serve as a lab compute resource for
pilot experiments and live demonstrations.

**The computational work is ready before the bench work starts.**

---

## 1. For Dr. Gonzales — What This Means for the Lab

### What's Already Built From Your Published Data

All 6 Gonzales papers (G1–G6) have been computationally reproduced across
three separate code repositories. Total: **782/782 validation checks pass.**

| Paper | What Was Modeled | Checks |
|-------|------------------|:------:|
| G1 (IL-31 pruritus, 2013) | Serum levels, dose-response scratching, receptor lattice | 15/15 |
| G2 (Oclacitinib IC50, 2014) | Hill dose-response for 6 cytokines, JAK selectivity, Anderson barrier | 35/35 |
| G3 (IL-31 pruritus model, 2016) | Time-series pruritus, treatment comparison | 19/19 |
| G4 (Lokivetmab PK, 2021) | Dose-duration regression (R²=1.0), exponential decay | 19/19 |
| G5 (Oclacitinib FAD, 2024) | JAK1 selectivity cross-disease | included |
| G6 (IL-31 cell targets, 2014) | Three-compartment tissue model (immune + skin + neural) | 19/19 |
| **Total across repositories** | Anderson framework, GPU validation | **782/782** |

### What I Replace on the Software Side

| Commercial Tool | Annual Cost | What healthSpring Provides | Status |
|-----------------|:----------:|----------------------------|:------:|
| NONMEM | $2,000/yr | Population PK (FOCE, 30-subject) | Validated |
| Monolix | $1,500/yr | SAEM estimation | Validated |
| WinNonlin | $3,000/yr | NCA (λz, AUC∞, MRT, CL, Vss) | Validated |
| SAS/R/Python infra | $500–5K/yr | All statistical computing | Built in |
| CRO population PK | $50K–200K/program | Population PK Monte Carlo (100K patients) | Validated |
| **Total per pipeline** | **$75K–$210K** | **~$0.01** (GPU electricity) | **Now** |

### What I Do at the Bench

The bench is the job. The computation makes the bench more productive.

| Bench Capability | Experience | Relevance to Position |
|-----------------|-----------|----------------------|
| BSL2 cell culture, aseptic technique | 5 years MSUBI (bacteria, fungi, mycobacteria, GMOs) | Ready for iPSC culture and eukaryotic cell lines |
| Plate-based screening and phenotypic assays | MSUBI enzyme kinetics, HPLC, mass spec, viable cell counts | Drug screening assays, immunoassays |
| Molecular biology | DNA/RNA extraction, PCR, selective media, microscopy | Molecular mechanisms of atopic disease |
| Fermentation and bioprocess | Flask-to-10L bioreactors, BSL2, media prep | Culture maintenance, growth optimization |
| High-throughput sequencing and bioinformatics | Sandia National Labs (algae toxin effects, microbial interactions) | Data analysis, mechanism identification |
| Environmental chemistry | MSU PFAS Research Lab (EPA SOPs, biomolecular methods) | Rigorous protocol compliance |
| Statistical analysis and ML | MS Data Science (4.0 GPA), Python, R, SQL | Data interpretation, presentation, computational analysis |

**What I want to learn from this lab:** Eukaryotic cell culture (iPSC-derived
skin models, mammalian systems), neuro-immune interaction assays, transgenic
mouse models. My bench experience is prokaryotic and fungal — the discipline
transfers, the biological system is new and is what I'm here to learn.

**Why the computation matters at the bench:** When computation is near-free,
the scarce resource is the person who can design the right experiment, run
it correctly, and interpret the result. The computation tells us which 20
compounds out of 8,000 to test first. The bench scientist runs those 20
assays, measures the actual cytokine response, and determines whether the
prediction held. That cycle — predict, test, refine — is faster and cheaper
than screening blind. But it requires someone at the bench who understands
both the biology and the data.

---

## 2. For Dr. Lisabeth (ADDRC) — How Computation Plugs Into HTS

### The Pipeline

```
healthSpring MATRIX scoring (8,000 compounds, ~1 second on GPU)
    → Ranked compound list with tissue geometry rationale
    → ADDRC HTS screens top candidates
    → Gonzales iPSC validates hits
    → Ellsworth med chem optimizes leads
    → Feedback loop refines Anderson model
```

### What Changes for ADDRC

1. **Computational triage before screening** — rank 8K compounds by
   Anderson-augmented MATRIX score. Screen the top 100, not the full library.
   Save reagents, save time, improve hit rate.

2. **Reanalyze "inactive" compounds** — existing dose-response data contains
   compounds classified inactive (IC50 > 10 µM, SSMD < 1) that our models
   predict are functional as low-affinity multi-target binders. No new
   screening needed.

3. **Extended dose-response** — add 4 sub-IC50 concentrations to existing
   10-point curves. Detect hormetic responses invisible to standard HTS.
   Marginal cost per compound.

4. **Automated data science** — Z' calculation, SSMD, dose-response fitting,
   IC50 determination, cross-compound comparison. Fully automated,
   reproducible, free.

### Data We'd Need From ADDRC

| Data | Format | Use | Sensitivity |
|------|--------|-----|-------------|
| Dose-response summary | CSV (IC50, Hill, Emax per compound) | Binding landscape analysis | Low (summary stats) |
| Brucella screen (2024) | GREENScreen export | Proof-of-concept reanalysis | Published |
| Target panel metadata | Compound → target mapping | Multi-target scoring | Low |
| Full dose-response curves | 10-point response data | Full affinity landscape | Medium |

Everything runs locally. No cloud. No data leaves the lab.

---

## 3. For the Drug Discovery Program — Grants

### Ready to Write Now (Near-Term)

| # | Hypothesis | Mechanism | Budget | PI Lead |
|---|------------|-----------|:------:|---------|
| H1 | "Inactive" compounds show cancer selectivity via coincidence detection | NCI R21 | $275K/2yr | Gonzales (Lisabeth co-I) |
| H3 | Hormetic dose-response detectable at sub-IC50 | NIGMS R21 | $275K/2yr | Gonzales (Lisabeth co-I) |
| H6 | Cross-species PK translation without commercial software | NIGMS supp / FDA | $150K/2yr | Gonzales |
| H8 | Hidden immunomodulators in HTS "inactive" compounds | NIAID R21 | $275K/2yr | Gonzales (Lisabeth co-I) |

### Needs Pilot Data First (Medium-Term)

| # | Hypothesis | Mechanism | Budget | PI Lead |
|---|------------|-----------|:------:|---------|
| H2 | Delocalized toxicity advantage (distributed binding) | NIGMS R01 | $1.25M/5yr | Gonzales |
| H4 | Anderson-augmented MATRIX reranks drug candidates | NIAMS R01 | $1.25M/5yr | Gonzales |
| H5 | Probiotic colonization resistance via diverse weak adhesion | NIDDK R21 / USDA | $275K/2yr | Gonzales |

### Long-Term

| # | Hypothesis | Mechanism | Budget |
|---|------------|-----------|:------:|
| H7 | Stress pathway hierarchy predicts drug sensitivity | NIGMS R01 | $1.25M/5yr |

### Total Addressable Grant Funding

Near-term R21s (H1, H3, H6, H8): **$975K**
Medium-term R01s (H2, H4): **$2.5M**
Full portfolio (all 8): **$5.775M over 5 years**

All proposals use **existing ADDRC infrastructure** — the computational
triage is free, and wet-lab validation uses existing equipment.

See `healthSpring/work/EXPERIMENTAL_HYPOTHESES.md` for full details on each.

### The Pre-Grant Pipeline

Every hypothesis can be explored computationally **before any grant
money is requested**. Open data + free software + biomeGate = zero-cost
preliminary results. The traditional pipeline (propose → fund → experiment →
analyze) becomes: **compute → predict → propose with data → fund → validate**.

Grant reviewers see preliminary results, not promises. Time to first insight
drops from years to weeks. Cost to university: zero.

See `onboarding/PRE_GRANT_PIPELINE.md` for the full rationale.

### Cross-Species Causal Engine

Why does cat skin ≠ dog skin ≠ human skin? Anderson localization predicts
species-specific drug responses from measurable tissue geometry: epidermal
thickness, follicle density, cell-type diversity. This is the causal
engine that makes Gonzales's comparative pharmacology generalizable — not
empirical scaling, but physics-based prediction.

See `onboarding/CROSS_SPECIES_CAUSAL_MODEL.md` for the full model and
testable predictions.

---

## 4. Free / Open-Source Data Starting Points

These are immediately usable — no institutional access, no IRB, no MTA.

### Drug Discovery & Pharmacology

| Source | What | How We Use It | URL |
|--------|------|---------------|-----|
| PubChem BioAssay | Dose-response data for millions of compounds | Binding landscape analysis, IC50 distributions | pubchem.ncbi.nlm.nih.gov |
| ChEMBL | Curated drug-target data (2.4M compounds, 15K targets) | MATRIX scoring, cross-target binding profiles | ebi.ac.uk/chembl |
| DrugBank | 14K+ drug entries with targets, pathways, ADMET | Drug repurposing candidates, PK parameters | drugbank.com (free academic) |
| BindingDB | 2.8M binding affinities | Low-affinity landscape calibration | bindingdb.org |
| PDB | 200K+ protein structures | Target geometry for Anderson tissue models | rcsb.org |
| UniProt | Protein sequences + annotations | Receptor distribution mapping | uniprot.org |
| FDA Orange Book | Approved drug products with therapeutic equivalence | Cross-species reference parameters | fda.gov/drugs |

### Microbiome & Genomics

| Source | What | How We Use It | URL |
|--------|------|---------------|-----|
| NCBI SRA | Raw sequencing reads (16S, shotgun, etc.) | 16S diversity, Anderson W computation | ncbi.nlm.nih.gov/sra |
| NCBI BioProject | Organized sequencing studies | Benchmarking, community validation | ncbi.nlm.nih.gov/bioproject |
| Zenodo | Open datasets with DOIs | Provenance-tracked reference data | zenodo.org |
| HMP (Human Microbiome Project) | Healthy gut community data | Baseline gut diversity for Anderson models | hmpdacc.org |
| MIMIC-III (PhysioNet) | ICU patient records + biosignals | ECG, HRV, biosignal validation | physionet.org |
| MIT-BIH (PhysioNet) | Arrhythmia database | Beat classification templates | physionet.org |

### Tissue Geometry & Cross-Species Biology

| Source | What | How We Use It | URL |
|--------|------|---------------|-----|
| Human Protein Atlas | Tissue-specific protein expression + histology | Receptor density maps per tissue per species | proteinatlas.org |
| Cell×Gene (CZI) | Single-cell RNA-seq atlases, multi-species | Cell-type diversity → Anderson W per species per tissue | cellxgene.cziscience.com |
| Tabula Sapiens / Muris | Human + mouse single-cell reference atlases | Cross-species cell composition comparison → d_eff | tabula-sapiens-portal.ds.czbiohub.org |
| GTEx | Gene expression across 54 human tissue types | Cell-type diversity (Pielou W) per tissue | gtexportal.org |
| Published histomorphometry | Epidermal thickness, follicle density per species | Anderson d_eff per species — the causal bridge | Literature review |

### How Internal Data Layers On Top

```
PUBLIC DATA                    INTERNAL DATA
─────────────                  ──────────────
PubChem IC50 distributions     ADDRC 8K compound dose-response
    → calibrates models    →       → refines models with real data
                                   → validates computational predictions
ChEMBL cross-target profiles   Gonzales iPSC readouts
    → builds scoring matrix →      → validates scoring in live cells

HMP gut diversity baselines    Future clinical microbiome data
    → establishes normal W  →      → measures treatment-specific W shifts

MIT-BIH arrhythmia templates   Future patient ECG data
    → trains classifiers    →      → monitors real patients
```

The public data builds and validates the framework. Internal data refines
the parameters and closes the prediction → validation loop. The same code,
the same models — just better parameters from real measurements.

---

## 5. Cost Savings on ICER

MSU's ICER (Institute for Cyber-Enabled Research) provides V100/A100 GPU
access. Our pipeline runs on ICER with zero environment setup.

### How It Works

The pipeline compiles into a single executable with zero external
dependencies — no Python environments, no CUDA toolkit, no module
loads on ICER. Build once on any Linux machine, copy to ICER, run.
Setup time: under 10 minutes. No IT tickets, no environment conflicts.

### Comparison: Commercial vs ICER + Our Pipeline

| Task | Commercial | ICER + Python | ICER + Our Pipeline |
|------|:----------:|:-------------:|:-----------------:|
| Population PK (100K patients) | $50K–200K (CRO) | $5–20 (ICER GPU-hr) | **< $0.01** (biomeGate or ICER) |
| 16S pipeline (1,000 samples) | $5K–15K (QIIME2 + analyst) | $2–5 (ICER CPU) | **~$0.10** (GPU) |
| Compound scoring (8K compounds) | Commercial + analyst (weeks) | Not available | **< 1 second** on any GPU |
| PK software (NONMEM + Monolix + WinNonlin) | $6,500/yr license | $0 (R/Python) | **$0** (open source) |

### What ICER Accelerates

| Workload | Consumer GPU | ICER A100 | Speedup |
|----------|:-----------:|:---------:|:-------:|
| Population PK Monte Carlo (1M patients) | ~5 sec | ~0.6 sec | 8× |
| Anderson spectral sweep (10K lattices) | ~30 sec | ~4 sec | 8× |
| Lattice QCD 32⁴ production | ~8 hr | ~1 hr | 8× |
| Michigan Crop Water Atlas | ~1 hr | ~8 min | 8× |

ICER gives us scale for production runs. biomeGate gives us zero-queue
iteration for daily work. Both run the same code, produce the same results.

---

## 6. biomeGate — Lab HPC on Campus

### What biomeGate Is

A multi-GPU workstation I built and own. Portable to campus.

| Component | Spec |
|-----------|------|
| **CPU** | AMD Threadripper 3970X (32 cores / 64 threads) |
| **RAM** | 256 GB DDR4 ECC |
| **Primary GPU** | NVIDIA RTX 5060 (8 GB, consumer shader) |
| **Work GPUs** | 2× NVIDIA Titan V (12 GB HBM2 each, native f64) |
| **Work GPUs** | 2× AMD MI50 (32 GB HBM2 each, native f64) |
| **NPU** | BrainChip AKD1000 (neuromorphic, 1.4 µJ/inference) |
| **Storage** | 2 TB NVMe |
| **Network** | 10 GbE |
| **Total GPU VRAM** | **96 GB** (12+12+32+32+8) |

### Why Titan V and MI50 Matter

The Titan V provides full-speed 64-bit floating point — 6.9 TFLOPS,
matching data-center GPUs but at consumer prices. The MI50 (AMD) provides
comparable 64-bit performance (6.7 TFLOPS) on different hardware.

Together they prove **cross-vendor reproducibility**: the same computation
on NVIDIA and AMD hardware produces identical results. This matters for
grant reviewers who ask "can anyone reproduce this?"

### What biomeGate Enables in the Lab

1. **Zero-queue computation** — run 50 parameter sweeps before lunch.
   No ICER queue. No scheduling. No waiting.

2. **Hardware demonstrations** — show collaborators (Lisabeth, Neubig,
   Ellsworth) live Anderson-augmented MATRIX scoring on real compound data.
   Seeing the pipeline run in seconds is more compelling than any slide deck.

3. **Pilot experiments** — before writing the grant, run the pilot. Feed
   ADDRC dose-response data into the binding landscape analysis. Show
   results same day. The pilot IS the preliminary data for the R21.

4. **Cross-vendor validation** — prove that results are vendor-agnostic.
   Same computation, same result on NVIDIA (Titan V) and AMD (MI50).
   Reviewers love reproducibility evidence.

5. **Data stays local** — ADDRC compound data never leaves the lab.
   biomeGate sits in the lab, under lab control. No cloud uploads, no
   third-party data processing.

6. **Neuromorphic edge prototype** — the AKD1000 processor runs
   biosignal classifiers at 1.4 µJ per inference. Demo: real-time ECG
   beat classification on coin-cell power. Relevant for wearable
   monitoring grants (NIBIB, FDA).

### biomeGate on Campus — Logistics

- **Physical:** One desktop-sized workstation. Standard power (two 120V
  outlets). Standard Ethernet (lab jack or departmental WiFi).
- **Setup:** 30 minutes (plug in, run `cargo test --workspace`).
- **Access:** My machine, lab use. Can network with Gonzales lab
  workstations and ADDRC machines for distributed computation.
- **ICER integration:** Heavy jobs dispatch to ICER A100s; results
  return to biomeGate. Best of both worlds.

---

## 7. Pilot Experiments — What We Can Run Immediately

These require zero internal data. They use only public data and our
existing validated models.

### Week 1: Demonstrate Capability

| Experiment | Time | What It Shows | Who Sees It |
|------------|:----:|---------------|-------------|
| Run all 809 healthSpring tests on biomeGate | 2 min | Everything passes on lab hardware | Gonzales |
| Hill dose-response for G2 oclacitinib data | 0.04 ms | Your published data, reproduced | Gonzales |
| Lokivetmab PK prediction at new dose levels | 0.1 ms | Testable prediction from published data | Gonzales |
| Anderson-augmented MATRIX for 6 candidates | < 1 sec | Drug ranking with tissue geometry | Gonzales, Lisabeth |
| Low-affinity selectivity demo (exp097) | 2 sec | 26× selectivity from "inactive" compounds | Lisabeth, Neubig |

### Week 2–4: Pilot with Public Data

| Experiment | Data Source | What We Learn | Grant Seed |
|------------|------------|---------------|------------|
| PubChem binding landscape for AD targets | PubChem BioAssay | Calibrate low-affinity model against real IC50 distributions | H1 (NCI R21) |
| ChEMBL cross-reactivity matrix | ChEMBL 34 | Which drug classes show broad-weak binding profiles | H1, H8 |
| HMP gut diversity baseline | HMP Phase II | Establish normal Anderson W for colonization resistance | H5 (NIDDK R21) |
| MIT-BIH arrhythmia on AKD1000 NPU | MIT-BIH | Real-time beat classification at microwatt power | Biosignal grant |
| DrugBank PK parameters for cross-species | DrugBank | Validate allometric scaling predictions | H6 (NIGMS supp) |

### Month 2–3: Pilot with ADDRC Data (Pending Access)

| Experiment | Internal Data | What We Learn | Grant Seed |
|------------|--------------|---------------|------------|
| Reanalyze Brucella screen low-affinity tail | Lisabeth 2024 screen | Proof-of-concept: function in "inactive" compounds | H1, H8 |
| Full 8K compound MATRIX scoring | ADDRC compound metadata | Ranked candidates with Anderson geometry | H4 (NIAMS R01) |
| Extended dose-response on select compounds | ADDRC + 4 sub-IC50 points | Hormesis detection | H3 (NIGMS R21) |
| iPSC cytotoxicity: broad-weak vs narrow-strong | Gonzales iPSC | Validate delocalized toxicity advantage | H2 (NIGMS R01) |

---

## 8. Document Index — What to Share With Whom

### For Gonzales (PI)

| Document | Location | When |
|----------|----------|------|
| Computational brief (her data modeled) | `contact/gonzales/computational_brief.md` | Sent |
| Validation brief (782/782 checks) | `contact/gonzales/spring_validation_brief.md` | If she asks |
| Cost comparison ($210K → $0.01) | `baseCamp/gonzales/cost_access_methods.md` | Meeting |
| Pre-grant pipeline (zero-cost science) | `onboarding/PRE_GRANT_PIPELINE.md` | Day 1 discussion |
| Cross-species causal model | `onboarding/CROSS_SPECIES_CAUSAL_MODEL.md` | Day 1 discussion |
| This onboarding package | This file | Day 1 |

### For Lisabeth (ADDRC)

| Document | Location | When |
|----------|----------|------|
| ADDRC computational brief | `contact/lisabeth/computational_brief.md` | Next meeting |
| Binding landscape analysis | `contact/lisabeth/binding_landscape_brief.md` | Next meeting |
| Drug Discovery Pipeline | `publicRelease/DRUG_DISCOVERY_PIPELINE.md` | If she asks |
| Cross-species causal model | `onboarding/CROSS_SPECIES_CAUSAL_MODEL.md` | ADDRC + tissue geometry |

### For Drug Discovery Program (Neubig, Ellsworth)

| Document | Location | When |
|----------|----------|------|
| Drug Discovery Pipeline | `publicRelease/DRUG_DISCOVERY_PIPELINE.md` | Group meeting |
| Grant Technical Appendix | `publicRelease/GRANT_TECHNICAL_APPENDIX.md` | Grant writing |
| MSU Asset Acceleration | `publicRelease/MSU_ASSET_ACCELERATION.md` | Department talk |
| Pre-grant pipeline rationale | `onboarding/PRE_GRANT_PIPELINE.md` | Department talk |

### For Grant Applications

| Document | Location | When |
|----------|----------|------|
| Experimental Hypotheses (8 proposals) | `healthSpring/work/EXPERIMENTAL_HYPOTHESES.md` | Grant writing |
| Grant Technical Appendix | `publicRelease/GRANT_TECHNICAL_APPENDIX.md` | Technical section |
| Hardware Cost Analysis | `sporePrint/technical/HARDWARE_COST_ANALYSIS.md` | Budget justification |
| Cross-species causal model | `onboarding/CROSS_SPECIES_CAUSAL_MODEL.md` | R01 preliminary data |
| Pre-grant pipeline | `onboarding/PRE_GRANT_PIPELINE.md` | Broader impacts / innovation |

### For Other MSU Labs and Collaborators

This package is also designed as a collaboration resource. When the Drug
Discovery Program reaches out to other departments — Vet Med, Chemistry,
BMB, MGI (the three incoming Global Impact faculty hires) — these
documents explain what the computational pipeline does for their data:

| MSU Team | What We Offer | Document to Share |
|----------|--------------|-------------------|
| Vet Med (cross-species AD) | Cross-species causal model from tissue geometry | `CROSS_SPECIES_CAUSAL_MODEL.md` |
| Chemistry (med chem, compound design) | Computational triage of compound libraries | `PRE_GRANT_PIPELINE.md` |
| BMB (protein structure, receptor biology) | Anderson-augmented target scoring | `DRUG_DISCOVERY_PIPELINE.md` |
| MGI (microbiome, immunology) | Gut Anderson W, colonization resistance models | `DATA_SOURCES_AND_INTEGRATION.md` |
| ICER (HPC infrastructure) | Zero-dependency binaries, GPU validation | `COST_AND_COMPUTE_BRIEF.md` |
| Any PI with dose-response data | Binding landscape reanalysis for free | `PRE_GRANT_PIPELINE.md` |

The computation is free. The data is public. What's valuable is the
expertise to connect them — to design the right experiment, run it at the
bench, and interpret the result in the context of the causal model. Every
collaboration we build produces data that feeds back into the pipeline,
making the next prediction better and the next experiment more targeted.

---

## 9. What I Need From the Lab

| Need | From | Timeline |
|------|------|----------|
| Desk + power outlet for biomeGate | Gonzales | Day 1 |
| Lab network access (Ethernet or WiFi) | IT | Week 1 |
| Introduction to ADDRC team | Gonzales/Lisabeth | Week 1-2 |
| ADDRC compound metadata (CSV) | Lisabeth | Month 1 |
| Brucella screen dataset | Lisabeth | Month 1 |
| iPSC cell lines for pilot validation | Gonzales | Month 2-3 |
| ICER account (if not existing) | ICER enrollment | Week 1 |

---

## The Bottom Line

I walk in as a bench scientist with 5+ years of BSL2 lab experience,
ready to learn eukaryotic cell culture, iPSC models, and neuro-immune
assays. I want to work with transgenic mice, dissect tissue, and run
the experiments that test real biological questions.

I also walk in with:
- A validated computational pipeline (809 tests, 782 Gonzales-specific checks)
- $0 replacement for $210K/year of commercial software
- biomeGate (96 GB GPU VRAM) as a lab compute resource
- 8 grant-ready hypotheses totaling $5.775M in addressable funding
- Public data pipelines that generate preliminary data while the lab spins up

The computation is near-free. The expertise is valuable. A bench scientist
who can design computationally-informed experiments, run them, and interpret
the results across species is more productive than either capability alone.

Every pilot experiment, every piece of preliminary data, every collaboration
with another MSU team exists to generate the funding and the scientific
questions that keep me at the bench, working with the biological systems
that matter.
