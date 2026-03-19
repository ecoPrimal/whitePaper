<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# Pilot Experiments — Immediate Computational Work for Gonzales Lab

**Purpose:** Experiments that can run on Day 1 (public data) through Month 3
(internal data), producing preliminary results for grant proposals.

---

## Tier 1: Day 1 — Demonstrate Capability (Public Data Only)

These require zero institutional data. Run on biomeGate in the lab.

### P01: Reproduce Gonzales Catalog Live

**What:** Run the full 782-check validation suite on biomeGate in front of
Gonzales. Her published data, reproduced in real time.

**Command:** `cargo test --workspace` (healthSpring, 809 tests, ~2 min)

**Output:** All checks pass. Screen shows her IC50 values, PK curves, and
tissue lattice — computed in milliseconds.

**Value:** Establishes credibility. "I reproduced everything you published
before I walked in the door."

### P02: PubChem Binding Landscape for JAK Targets

**What:** Download all PubChem BioAssay dose-response data for JAK1, JAK2,
JAK3, IL-4Rα, IL-31RA. Compute the full affinity landscape including the
low-affinity tail.

**Data:** PubChem BioAssay REST API (free, no account needed)

**Analysis:**
1. Extract IC50 distributions across 5 JAK/cytokine targets
2. Compute composite_binding_score for each compound across all targets
3. Identify compounds with broad-weak profiles (Gini < 0.3, composite > 0.1)
4. Compare with known oclacitinib profile (G2 reference)

**Output:** Distribution plot of binding breadth. List of compounds that
show "oclacitinib-like" broad profiles at lower affinity. These are the
candidates standard HTS would discard.

**Grant seed:** H1 (NCI R21) — "Inactive" compounds with multi-target profiles

### P03: ChEMBL Cross-Reactivity Matrix for AD Drug Classes

**What:** Build a cross-reactivity matrix for all compounds in ChEMBL that
hit any JAK/STAT pathway target. Identify clusters of broad-weak binders.

**Data:** ChEMBL 34 download (free, ~2 GB)

**Analysis:**
1. Query all bioactivity records for JAK1/JAK2/JAK3/TYK2/IL-4Rα/IL-31RA
2. Build cross_reactivity_matrix (compound × target) from IC50 values
3. Cluster compounds by binding profile similarity
4. Identify the "broad-weak" cluster vs "narrow-strong" cluster
5. Compute low_affinity_selectivity for each cluster

**Output:** Matrix visualization. Cluster analysis. Evidence that broad-weak
binding is a real phenomenon in existing drug-target data.

**Grant seed:** H1, H4 — computational evidence for reranking

### P04: DrugBank Cross-Species PK Validation

**What:** Extract PK parameters from DrugBank for drugs with both canine and
human data. Run healthSpring's allometric scaling model. Compare predicted
human PK to published human PK.

**Data:** DrugBank academic download (free with academic license)

**Analysis:**
1. Extract CL, Vd, t½ for compounds with canine + human data
2. Predict human PK using CL_human = CL_dog × (BW_human/BW_dog)^0.75
3. Compare predictions to published human values
4. Quantify prediction error (target ≤30%)

**Output:** Scatter plot: predicted vs actual human PK. Quantified error.
Evidence that the allometric bridge works without commercial software.

**Grant seed:** H6 (NIGMS supplement / FDA Critical Path)

### P05: MIT-BIH Arrhythmia on AKD1000 NPU

**What:** Run healthSpring's beat classification (exp082) on MIT-BIH data
through biomeGate's AKD1000 neuromorphic processor.

**Data:** MIT-BIH Arrhythmia Database (free from PhysioNet)

**Analysis:**
1. Load annotated ECG records
2. Classify beats: Normal, PVC, PAC, BBB
3. Compare NPU classification to annotation gold standard
4. Measure: power (µJ/inference), latency (ms), accuracy

**Output:** NPU accuracy + power measurements. Evidence for wearable
clinical monitoring at coin-cell power.

**Grant seed:** Biosignal / wearable monitoring grant (NIBIB, FDA)

---

## Tier 2: Week 2–4 — Build Preliminary Results (Public Data)

### P06: HMP Gut Diversity Baseline

**What:** Compute Anderson W (disorder parameter) for 300+ healthy human gut
samples from the Human Microbiome Project. Establish what "normal" looks like.

**Data:** HMP Phase II 16S data (free from hmpdacc.org)

**Analysis:**
1. Run wetSpring 16S pipeline on HMP samples
2. Compute Shannon diversity, Pielou evenness, Anderson W per sample
3. Establish distribution of healthy W values
4. Map W to colonization resistance score (healthSpring exp012)

**Output:** Distribution of healthy gut W. Threshold below which
colonization resistance breaks down. Baseline for clinical comparison.

**Grant seed:** H5 (NIDDK R21 / USDA) — probiotic colonization resistance

### P07: BindingDB Low-Affinity Landscape

**What:** Download binding affinity data from BindingDB for all targets in
the Gonzales cytokine panel. Characterize the full affinity distribution
including the µM and mM ranges.

**Data:** BindingDB download (free, ~1 GB)

**Analysis:**
1. Extract Kd, Ki, IC50 for IL-31RA, IL-4Rα, JAK1, JAK2, JAK3
2. Plot full affinity distributions (pM → mM range)
3. Quantify fraction of binders in low-affinity regime (>10 µM)
4. Compute theoretical coincidence detection selectivity at each affinity level

**Output:** Evidence that the low-affinity tail is large and potentially
functional. Quantified selectivity predictions at different affinity thresholds.

**Grant seed:** H1, H8 — scope of the opportunity

### P08: Hormesis Literature Calibration

**What:** Collect published biphasic dose-response data (hormesis examples)
from the literature. Fit the mechanistic hormesis model from exp099.
Validate that the model predicts known hormetic responses.

**Data:** Published dose-response curves from hormesis literature
(Calabrese & Baldwin, 2003; Mattson, 2008; reviews in Dose-Response journal)

**Analysis:**
1. Extract dose-response data from 10+ published hormesis examples
2. Fit biphasic_dose_response model to each
3. Extract stress pathway parameters (HSP, SOD thresholds)
4. Predict: which cell types / compound classes should show hormesis
5. Compare predictions to published hormesis catalog

**Output:** Model validation across diverse biological examples. Confidence
that the model can predict hormesis in ADDRC compounds.

**Grant seed:** H3 (NIGMS R21) — preliminary evidence for prediction capability

---

## Tier 3: Month 1–3 — Internal Data Integration (Pending Access)

### P09: ADDRC Brucella Screen Reanalysis

**What:** Reanalyze Lisabeth's 2024 Brucella screen using the binding
landscape framework. Find function in compounds classified "inactive."

**Data:** Lisabeth 2024 screen data (pending access)

**Analysis:**
1. Ingest full dose-response data (8K compounds × targets)
2. Compute composite binding scores across Brucella targets
3. Identify "inactive" compounds with interesting low-affinity profiles
4. Predict which inactives should show immunomodulatory activity
5. Compare predictions with any known activity data

**Output:** Ranked list of "inactive" compounds predicted to be functional.
The proof-of-concept for the entire low-affinity hypothesis.

**Grant seed:** H1, H8 — this IS the pilot data for the R21

### P10: ADDRC Full 8K Compound MATRIX Scoring

**What:** Run Anderson-augmented MATRIX scoring on the full ADDRC compound
library for AD targets.

**Data:** ADDRC compound metadata + GREENScreen (pending access)

**Analysis:**
1. Score 8K compounds against AD target panel (JAK/cytokine pathway)
2. Apply Anderson tissue geometry scoring
3. Compare standard ranking vs Anderson-augmented ranking
4. Identify compounds where ranking changes >50 positions
5. Select top 20 for iPSC validation

**Output:** Ranked compound list with geometry rationale. Compounds for
Gonzales iPSC validation. The bridge from computation to wet lab.

**Grant seed:** H4 (NIAMS R01)

### P11: Extended Dose-Response (Hormesis Detection)

**What:** Run ADDRC compounds at extended dose-response (standard 10-point
+ 4 sub-IC50 concentrations). Detect biphasic responses.

**Data:** ADDRC compounds + custom dose-response protocol (wet lab, pending)

**Analysis:**
1. Select 20 compounds predicted by exp099 to show hormesis
2. Select 20 compounds predicted NOT to show hormesis (control)
3. Run extended dose-response (14 points)
4. Fit biphasic model + monotonic model to each
5. Compare: predicted hormetic show biphasic; predicted non-hormetic don't

**Output:** Validation of hormesis prediction. Data for NIGMS R21.

**Grant seed:** H3 (NIGMS R21) — experimental validation of computational prediction

### P12: iPSC Cancer Selectivity Test

**What:** Test computationally ranked low-affinity compounds in Gonzales
iPSC model. Compare cytotoxicity on cancer-like vs normal cells.

**Data:** Gonzales iPSC cell lines + P09/P10 ranked compounds

**Analysis:**
1. Select top 10 computationally ranked low-affinity compounds
2. Select 10 standard high-affinity hits (control)
3. Test cytotoxicity on cancer-like and normal iPSC lines
4. Compare therapeutic windows
5. Validate: low-affinity compounds show wider therapeutic windows

**Output:** Experimental evidence for the low-affinity hypothesis. Data for
NCI R21.

**Grant seed:** H1 (NCI R21) — experimental validation

---

## Timeline Summary

```
Week 1:   P01 (reproduce G1-G6 live)
          P02 (PubChem binding landscape)
          P05 (NPU arrhythmia demo)

Week 2-4: P03 (ChEMBL cross-reactivity)
          P04 (DrugBank cross-species PK)
          P06 (HMP gut baseline)
          P07 (BindingDB low-affinity landscape)
          P08 (Hormesis literature calibration)

Month 1:  P09 (Brucella screen reanalysis) — needs ADDRC data
          P10 (Full 8K compound scoring) — needs ADDRC data

Month 2:  P11 (Extended dose-response) — needs wet lab
          P12 (iPSC selectivity test) — needs wet lab

Month 3:  Compile pilot results → Write R21 proposals
```

### Grant Submission Timeline

| Grant | Pilot Data From | Target Submission |
|-------|----------------|:-----------------:|
| H1 (NCI R21) | P02, P03, P09, P12 | Month 4-5 |
| H3 (NIGMS R21) | P08, P11 | Month 4-5 |
| H6 (NIGMS supp) | P04 | Month 2-3 |
| H8 (NIAID R21) | P09 | Month 3-4 |
| H4 (NIAMS R01) | P10, P12 | Month 6-8 |

---

## What Success Looks Like

**Month 1:** biomeGate running in the lab. 782/782 checks pass on lab
hardware. PubChem and ChEMBL pilot analyses complete. Lisabeth provides
Brucella screen data. First reanalysis results in hand.

**Month 3:** ADDRC compounds scored. Extended dose-response pilot running.
iPSC selectivity test designed. Two R21 proposals in draft.

**Month 6:** Two R21s submitted. iPSC pilot data supports computational
predictions. Anderson-augmented MATRIX reranking validated.

**Year 1:** R21 funding supports expanded wet-lab validation. biomeGate +
ICER running full pipeline. Internal data refines models beyond public
calibration. Gonzales Lab is the computational pharmacology lab at MSU.
