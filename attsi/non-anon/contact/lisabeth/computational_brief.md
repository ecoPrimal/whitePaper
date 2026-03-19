<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# Computational Brief: Binding Landscape Analysis for ADDRC

**For:** Erika Lisabeth (ADDRC Director, MSU Pharmacology & Toxicology)
**From:** Kevin Mok (mokkevin@msu.edu)
**Date:** March 2026
**Repos:** https://github.com/syntheticChemistry/healthSpring (AGPL-3.0)

---

## What This Is

A computational framework that reanalyzes HTS dose-response data to find
value in compounds classified as "inactive." Instead of optimizing for
strong, specific binding (the standard HTS pipeline), we model the full
affinity landscape — including the low-affinity tail that current analysis
discards.

Everything described here is implemented, tested, and reproducible.

---

## The Core Idea: Computation Before Experiment

Traditional pipeline:
```
Screen 8,000 compounds → analyze hits → discard inactives → pursue leads
```

Our addition:
```
Existing dose-response data → computational binding landscape →
identify low-affinity compounds with interesting profiles →
design targeted validation assays → test predictions
```

The computation doesn't replace the screen. It extracts additional value
from data you already have.

---

## What We Found Computationally

### 1. Weak Binders Can Be Selective

A compound with IC50 = 20 µM against 15 cancer markers and IC50 = 200 µM
against 4 normal markers achieves a **26× selectivity ratio** through
coincidence detection — many weak signals summing only where targets
co-localize on cancer cells.

This compound would be classified "inactive" in a standard HTS screen.

**Module:** `healthSpring/ecoPrimal/src/discovery/affinity_landscape.rs`
**Experiment:** exp097 (26 validation checks, all pass)

### 2. Distributed Binding Is Less Toxic

At equivalent total systemic exposure, compounds that bind weakly across
many tissues produce less organ-specific damage than compounds that bind
strongly in one tissue. The physics: per-tissue burden stays below repair
capacity, and clearance remains in the linear kinetics regime.

We quantify this using the Anderson Inverse Participation Ratio (IPR):
- Distributed binder: IPR = 0.003 (spread across tissues)
- Concentrated binder: IPR = 0.695 (one tissue bears the load)

**Module:** `healthSpring/ecoPrimal/src/toxicology.rs`
**Experiment:** exp098 (12 validation checks, all pass)

### 3. Some Compounds Have Biphasic Dose-Response (Hormesis)

At sub-IC50 concentrations, certain compounds upregulate cellular stress
response pathways (HSP70, SOD, p53-mediated repair) — producing a net
benefit before the damage curve overtakes the repair curve at higher doses.

Standard HTS misses this because it doesn't test at sub-IC50 doses.
Our model predicts which compounds should show hormetic behavior based on
their Hill parameters and the target cell's stress pathway profile.

**Module:** `healthSpring/ecoPrimal/src/toxicology.rs` (hormesis functions)
**Experiment:** exp099 (18 validation checks, all pass)

### 4. Full Causal Chain: Molecular → Cellular → Tissue → Organism → Population

We built a mechanistic simulation that traces how molecular binding events
propagate through cellular stress pathways, integrate into tissue-level
fitness, and ultimately reshape population dynamics. The biphasic
dose-response curve emerges from the model — it's not fitted, it's
predicted.

**Module:** `healthSpring/ecoPrimal/src/simulation.rs`
**Experiment:** exp111 (20 validation checks, all pass)

---

## What This Means for ADDRC

### Immediate Opportunity

Your 8,000-compound library already has full dose-response data. Our
models can:

1. **Compute composite binding scores** — find compounds with interesting
   low-affinity profiles across multiple targets
2. **Predict toxicity distribution** — rank compounds by organ-specific
   risk using Anderson IPR
3. **Identify hormetic candidates** — flag compounds likely to show
   biphasic effects at sub-IC50 doses
4. **Prioritize validation experiments** — computational triage tells you
   which compounds are worth testing in extended assays

### What We'd Need

- Access to existing dose-response summary data (IC50, Hill slope, Emax
  per compound per target) — even anonymized or aggregated
- The Brucella screen dataset (Lisabeth 2024) as a proof-of-concept
- Input on which target panels would be most informative for the
  low-affinity hypothesis

### What We Don't Need

- New screening runs (reanalyze existing data first)
- Proprietary compound identifiers (summary statistics are sufficient)
- Cloud infrastructure (everything runs on a laptop)

---

## Testable Predictions

These are the hypotheses we can test with ADDRC infrastructure:

| # | Prediction | Test | Data Needed |
|---|------------|------|-------------|
| H1 | "Inactive" compounds include cancer-selective multi-target binders | Cytotoxicity on cancer vs normal iPSC lines for computationally ranked compounds | Existing dose-response + Gonzales iPSC |
| H2 | Distributed binders produce less organ-specific toxicity | Multi-tissue cytotoxicity panel for matched compound pairs | ADDRC compounds + 4+ cell lines |
| H3 | Biphasic dose-response detectable at sub-IC50 concentrations | Extended dose-response (add 4 sub-IC50 points) + stress pathway reporters | Existing ADDRC compounds + qPCR panel |
| H4 | Anderson geometry scoring reranks drug candidates | Compare standard vs Anderson-augmented MATRIX for AD | ADDRC compound metadata + Gonzales iPSC |
| H8 | "Inactive" compounds include immune modulators | Cytokine panel (IL-6, TNF-α, IL-10, IFN-γ) for computationally ranked compounds | ADDRC inactives + PBMC/THP-1 assay |

---

## Technical Details

All code is public (AGPL-3.0), runs on consumer hardware, produces
deterministic output with full provenance.

```bash
git clone https://github.com/syntheticChemistry/healthSpring
cd healthSpring

# Run the binding landscape analysis
cargo run --release --bin exp097_affinity_landscape

# Run the toxicity landscape analysis
cargo run --release --bin exp098_toxicity_landscape

# Run the hormesis analysis
cargo run --release --bin exp099_hormesis

# Run the full causal chain
cargo run --release --bin exp111_causal_terrarium

# All exit 0 — every assertion passes
```

Total: 809 tests, 83 experiments, 53 Python baselines, zero warnings.

---

## Grant Opportunities (Joint)

| Mechanism | Focus | Budget |
|-----------|-------|--------|
| NCI R21 | Low-affinity cancer selectivity from existing HTS | $275K/2yr |
| NIGMS R21 | Hormetic dose-response prediction from HTS data | $275K/2yr |
| NIAID R21 | Hidden immunomodulators in "inactive" compounds | $275K/2yr |
| NIAMS R01 | Anderson-augmented drug repurposing (with Gonzales) | $1.25M/5yr |

All proposals use existing ADDRC infrastructure — the computational
triage is free, and the wet-lab validation uses existing equipment and
compound libraries.
