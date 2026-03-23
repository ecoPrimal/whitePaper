<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# The Binding Landscape: Why "Inactive" Compounds May Be Active

**For:** Erika Lisabeth (ADDRC Director)
**Context:** This brief extends the specificity/binding conversation from
our meeting (March 2026, introduced by Gonzales).

---

## The Problem We Discussed

Standard HTS analysis optimizes for one thing: strong, specific binding.
A compound hits a target hard (IC50 < 1 µM, SSMD > 3), or it's classified
inactive. This is the right approach when you want a scalpel — a drug that
precisely modulates one target.

But the immune system doesn't work that way. Immune recognition operates
through many weak, distributed interactions. Gut colonization resistance
comes from many bacteria weakly adhering to epithelium, not one strain
strongly attached. Cancer cells are distinguished from normal cells by
having *more* surface markers, not *different* ones — suggesting that
distributed detection (many weak signals summing) may outperform
targeted detection (one strong signal).

## What the HTS Data Contains

Every dose-response curve in the ADDRC library is a window into the full
affinity landscape. The standard analysis extracts one number: IC50 (or
"inactive" if IC50 is too high). But that curve contains much more:

```
                    What standard HTS sees
                    ↓
Response |         ┌──────────┐
         |        /            \
         |       /              \
         |      /                ← IC50 (the one number)
         |     /
         |    /← This part is "inactive" but contains real binding data
         |   /
         |  /
         |_/________________________________
              Low dose            High dose
```

The low-affinity tail (left side) is real data. It represents compounds
that do bind, just weakly. The question is whether that weak binding is
*functional* in biological contexts that don't require strong specificity.

## Three Modes of Low-Affinity Function

### 1. Coincidence Detection (Cancer Selectivity)

Cancer cells express many markers at moderate levels. Normal cells express
few markers at high levels. A compound with weak affinity for many markers
generates a composite binding score that:
- Is HIGH on cancer cells (many weak signals sum)
- Is LOW on normal cells (few weak signals, each below threshold)

Our model shows **26× selectivity** from a compound with IC50 = 20 µM —
a compound your screen would classify as inactive.

The math (fractional occupancy × coincidence detection):

| Target Profile | # Markers | Per-marker Occupancy | Composite Score |
|----------------|:---------:|:--------------------:|:---------------:|
| Cancer cell (15 markers) | 15 | ~5% each | 0.519 |
| Normal cell (4 markers) | 4 | ~1% each | 0.020 |
| **Selectivity ratio** | | | **26×** |

### 2. Distributed Toxicity (Safety Advantage)

At equivalent total systemic exposure, a weak distributed binder produces
less organ-specific toxicity than a strong concentrated binder. The
physics:

- **Concentrated:** Most binding in liver → hepatic burden exceeds repair
  capacity → tissue damage → clearance saturates (nonlinear elimination)
- **Distributed:** Binding spread across 10+ tissues → each tissue at
  <10% of repair capacity → no tissue damage → clearance stays linear

We measure this with the Anderson Inverse Participation Ratio (IPR):
- IPR = 0.003 → perfectly distributed (safe)
- IPR = 0.695 → highly concentrated (single-organ risk)

### 3. Hormetic Dose-Response (Sub-IC50 Benefit)

At concentrations below IC50, some compounds activate cellular stress
repair pathways (HSP70 chaperone, SOD antioxidant, p53 checkpoint, mTOR
nutrient sensing) faster than they cause damage. The result: a biphasic
curve where low doses *improve* cellular fitness.

```
Fitness |    ____
        |   /    \
        |  / ← Hormetic peak (cell is stronger)
        | /      \
1.0 ----/         \
        |          \
        |           \ ← Toxic decline
        |            \
        |_____________\___
        Low dose         High dose
```

Standard HTS can't detect this because it doesn't test sub-IC50 doses.
Our model predicts which compounds should show hormesis based on their
Hill parameters.

## What We're Proposing

### Phase 1: Computational Reanalysis (No Wet Lab Needed)

Take existing ADDRC dose-response data and compute:
- Composite binding scores across target panels
- Toxicity IPR for binding distribution prediction
- Hormesis candidates from Hill parameter analysis
- Anderson-augmented MATRIX scores with tissue geometry

**Timeline:** 2-4 weeks given data access
**Cost:** $0 (computational)

### Phase 2: Targeted Validation (Minimal Wet Lab)

For top computationally ranked compounds:
- Test cytotoxicity on cancer vs normal iPSC lines (Gonzales)
- Extended dose-response at sub-IC50 concentrations
- Stress pathway qPCR panel (HSP70, SOD, p53)
- Multi-tissue cytotoxicity panel (4+ cell lines)

**Timeline:** 3-6 months
**Cost:** Standard ADDRC assay costs (no new equipment)

### Phase 3: Grant Proposal

Joint R21 (NCI or NIGMS) based on Phase 1-2 results:
- Computational discovery from existing HTS data
- Validation using existing ADDRC infrastructure
- Novel paradigm: the "inactive" compounds as candidates

**Timeline:** Submit within 6 months of Phase 2 results

## Why This Is Different

| Traditional HTS | This Approach |
|-----------------|---------------|
| Discard compounds below IC50 threshold | Analyze the full affinity landscape |
| One number per compound (IC50) | Composite score across target panels |
| Toxicity tested per organ | Anderson IPR predicts distribution |
| Monotonic dose-response assumed | Biphasic (hormetic) models included |
| New screens required | Reanalyze existing data first |
| $210K commercial software stack | $0 open-source Rust (AGPL-3.0, public) |

## The Data We'd Need to Start

1. **Summary dose-response data** — IC50, Hill slope, Emax per compound
   per target for the 8K library (even anonymized)
2. **Brucella screen dataset** — your 2024 paper's 8K compound screen as
   a proof-of-concept dataset
3. **Target panel metadata** — which targets are in which screens

We don't need compound identifiers, proprietary structures, or cloud
access. Summary statistics run locally on a laptop.

---

*All computational work: healthSpring V39, 809 tests, 83 experiments.
Public repository: https://github.com/syntheticChemistry/healthSpring*
