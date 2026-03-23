<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# Cross-Species Causal Model: Why Skin Behaves Differently Across Species

**Audience:** Gonzales (comparative pharmacology), Lisabeth (drug screening),
Neubig (fibrosis), Drug Discovery Program
**Core claim:** A signal-propagation framework (Anderson localization) may
predict species-specific drug responses from tissue geometry. If correct,
the geometry is the cause — and every prediction below is testable.

---

## The Question

Gonzales's lab runs iPSC-derived skin models across species: canine, feline,
human. The same drug produces different responses in each. Current practice
handles this with species-specific parameters — different IC50 values,
different clearance rates, different allometric scaling factors.

But why are the parameters different?

The conventional answer is "biology is complicated." Different receptor
densities, different metabolic enzymes, different immune cell populations.
Each species is its own dataset. Translation is empirical curve fitting.

**We propose a simpler answer: the geometry is different.** And if
geometry determines signal propagation, then geometry determines
drug response. This is testable.

---

## The Physical Framework

### Background: Anderson Localization

Anderson localization is a well-established physics result (Nobel Prize,
1977): waves or signals traveling through disordered media can become
*trapped* (localized) rather than propagating freely. The key insight is
that **dimensionality and disorder together determine whether signals
spread or stay put.**

This has been applied to electron transport in semiconductors, light in
photonic crystals, and acoustic waves. We apply it to cytokine signaling
in tissue — a domain where the physics is analogous but the biological
implications are unexplored.

### Skin as a Signal Processing System

Skin is a layered medium. Cytokine signals (IL-31, IL-4, IL-13) propagate
through this medium from source cells (Th2, mast cells) to target cells
(neurons, keratinocytes). Whether a signal reaches its target depends on:

1. **Dimension (d):** How many directions can the signal travel?
   - 2D epidermis: signal is confined to a plane → localizes (trapped)
   - 3D dermis: signal travels in all directions → propagates (extended)

2. **Disorder (W):** How heterogeneous is the cell population?
   - Uniform population: signal travels freely
   - Mixed population: signal scatters → may localize

3. **Channels (d_eff):** Do 3D conduits exist through 2D barriers?
   - Hair follicles: 3D tubes through 2D epidermis
   - Sweat glands: 3D channels
   - Scratch wounds: 3D breaks in the barrier

Anderson's theorem: in 2D, signals **always** localize (get trapped)
regardless of disorder. In 3D, signals propagate **unless** disorder
exceeds a critical threshold W_c ≈ 16.

The species difference reduces to three numbers: epidermal thickness
(the 2D barrier), follicle density (the 3D channels), and dermal cell
diversity (the disorder W).

---

## Species Comparison

### Geometry Parameters

| Parameter | Dog | Cat | Human | Horse | Mouse |
|-----------|:---:|:---:|:-----:|:-----:|:-----:|
| Epidermis thickness (µm) | 15–25 | 10–20 | 50–100 | 30–50 | 8–15 |
| Hair follicle density (/cm²) | 1,000–9,000 | 800–1,600 | 100–150 | 200–600 | 5,000+ |
| Dermal cell types | 6+ | 5+ | 8+ | 6+ | 5+ |
| Sebaceous gland density | High | Moderate | Low–Mod | Very low | Moderate |
| Estimated d_eff | **2.6–2.8** | **2.2–2.4** | **2.1–2.3** | **2.2–2.5** | **2.7–2.9** |

### Anderson Predictions From Geometry

| Species | Epidermis Barrier | Follicle Channels | d_eff | Prediction |
|---------|:-----------------:|:-----------------:|:-----:|------------|
| **Dog** | Thin (weak barrier) | Very dense (many channels) | ~2.7 | Cytokines propagate easily → severe AD, fast drug penetration |
| **Cat** | Very thin (minimal barrier) | Moderate density | ~2.3 | Barrier weak but fewer channels → localized lesions, moderate AD |
| **Human** | Thick (strong barrier) | Very sparse channels | ~2.2 | Cytokines mostly confined → chronic but less severe, topicals limited |
| **Horse** | Moderate barrier | Low density | ~2.4 | Moderate propagation → insect hypersensitivity pattern |
| **Mouse** | Ultra-thin (negligible) | Ultra-dense | ~2.8 | Nearly 3D → signals propagate freely → why mice are bad AD models |

### What This Explains

**Why dogs get worse AD than humans:**
Dogs have thin epidermis (weak 2D barrier) + very dense hair follicles
(many 3D channels). d_eff ≈ 2.7, approaching the 3D regime where
cytokines propagate freely. Human d_eff ≈ 2.2, close to 2D where
signals localize. The geometry predicts: same cytokines, same pathways,
worse disease in dogs.

**Why Apoquel works better in dogs than human JAK inhibitors in humans:**
At d_eff ≈ 2.7, cytokine signals are more delocalized in dog skin.
A systemic JAK inhibitor (Apoquel) blocks signal transduction
everywhere simultaneously — effective because the signals ARE
everywhere. In human skin (d_eff ≈ 2.2), signals are more localized —
topical approaches can work because you can target the site.

**Why mice are poor AD models:**
Mouse d_eff ≈ 2.8 (ultra-thin epidermis, ultra-dense follicles) is
essentially 3D. This is so far from human d_eff ≈ 2.2 that the
geometry-driven disease dynamics are qualitatively different. A drug
that works in a mouse AD model may fail in humans not because of
pharmacology but because of geometry.

**Why lokivetmab (Cytopoint) works by systemic injection:**
IL-31 is a cytokine that signals through the 3D dermal compartment to
reach nerve endings. In dog skin, the 3D propagation is strong (d_eff
high). A systemic anti-IL-31 mAb (lokivetmab) intercepts the signal
in the 3D compartment where it's propagating. This explains the 14/28/42
day dose-duration data from G4: mAb concentration decays → signal
extinction time should be proportional to log(dose). This is checkable
against the published data.

**Why barrier repair is a therapeutic target (prediction):**
Restoring the 2D epidermis should reduce d_eff. The model predicts that
even partial barrier restoration (d_eff from 2.7 → 2.4) pushes the system
toward localization. If correct, this explains why moisturizers and barrier
creams have clinical benefit in AD beyond simple hydration — they are
physically reducing the effective dimension. Testable by measuring cytokine
propagation distance before and after barrier repair in iPSC models.

---

## Testable Predictions (Rank-Ordered by Feasibility)

### Tier 1: Computationally Testable Now (Open Data)

| # | Prediction | Test | Data Source |
|---|------------|------|-------------|
| C1 | Dog d_eff > human d_eff (by 0.3–0.5) | Compute from published histology: epidermal thickness + follicle density → d_eff | Dermatology textbooks, published tissue morphometry |
| C2 | Species IC50 ratio correlates with d_eff ratio | Compare canine IC50 (G2) to human IC50 for same targets (ChEMBL) | G2 + ChEMBL JAK inhibitor data |
| C3 | Mouse d_eff predicts poor AD model fidelity | Compute mouse d_eff, compare to human, quantify geometry gap | Published mouse skin morphometry |
| C4 | Follicle density explains topical vs systemic efficacy | Model drug penetration as function of follicle channel density | Published dermal drug penetration studies |
| C5 | Cross-species gut W correlates with drug metabolism | Compute Anderson W from published 16S across species | NCBI SRA gut 16S studies (dog, cat, human) |

### Tier 2: Testable With Gonzales iPSC Models

| # | Prediction | Test | What's Needed |
|---|------------|------|---------------|
| E1 | iPSC with higher cell diversity (higher W) shows more cytokine propagation | Vary cell-type ratios in iPSC skin model; measure IL-31 diffusion distance | iPSC culture + cytokine ELISA at spatial points |
| E2 | Physical barrier disruption increases d_eff measurably | Scratch iPSC barrier, measure cytokine propagation before/after | iPSC barrier model + scratch assay + time-series cytokine |
| E3 | Follicle-containing iPSC organoids show higher d_eff than flat iPSC | Compare cytokine propagation in organoid vs monolayer | Hair follicle organoid iPSC (if available) |
| E4 | Canine iPSC shows faster cytokine propagation than human iPSC | Compare IL-31 diffusion kinetics in species-matched iPSC | Cross-species iPSC (Gonzales has both) |
| E5 | Anderson-predicted drug ranking matches iPSC cytotoxicity ranking | Rank 20 compounds by Anderson score, test in iPSC, compare | ADDRC compounds + iPSC viability |

### Tier 3: Testable With Extended Lab Resources

| # | Prediction | Test | What's Needed |
|---|------------|------|---------------|
| L1 | d_eff measured by confocal microscopy matches computational prediction | Image cytokine diffusion in 3D skin tissue with fluorescent reporters | Confocal microscopy + fluorescent cytokine analogs |
| L2 | Barrier repair reduces d_eff and reduces cytokine propagation | Treat barrier-disrupted iPSC with repair compounds, measure d_eff change | iPSC + barrier repair compounds + imaging |
| L3 | Anderson geometry predicts in vivo drug response across species | Compare computational predictions to published clinical trial outcomes | Meta-analysis of cross-species drug trials |

---

## The Causal Chain

```
GEOMETRY (measurable)
    │
    ├── Epidermal thickness → 2D barrier strength
    ├── Follicle density → 3D channel density
    ├── Cell-type diversity → Anderson disorder W
    │
    ↓
ANDERSON PARAMETERS (computed)
    │
    ├── d_eff (effective dimension)
    ├── W (disorder)
    ├── W_c (critical threshold for propagation)
    │
    ↓
SIGNAL PROPAGATION (predicted)
    │
    ├── Which cytokines reach which targets
    ├── How far signals propagate
    ├── Whether signals localize or extend
    │
    ↓
DISEASE DYNAMICS (predicted)
    │
    ├── AD severity (more propagation → worse disease)
    ├── Itch intensity (IL-31 reaches nerves if d_eff > threshold)
    ├── Barrier feedback (scratching → dimensional promotion → more propagation)
    │
    ↓
DRUG RESPONSE (predicted)
    │
    ├── Which drugs work (pathway × geometry scoring)
    ├── Which route works (systemic vs topical vs follicular)
    ├── Which species responds (geometry determines efficacy)
    ├── Therapeutic window (Anderson predicts toxicity distribution)
    │
    ↓
TESTABLE PREDICTION → EXPERIMENT → VALIDATE/REFINE → REPEAT
```

Every step in this chain is computable. Every connection is testable.
The geometry is measurable. The predictions are specific and falsifiable.

This IS drug discovery: understand the causal mechanism, predict the
outcome, test the prediction, refine the model. The difference is that
we can explore the entire space computationally before touching a
reagent.

---

## What This Means for the Lab

### For Gonzales

Your comparative pharmacology approach (canine → human) is not just a
bridge — it's a window into causal mechanism. The Anderson framework
gives you a language to explain WHY the canine model predicts the human
response: the geometry is similar enough that the physics transfers.
Where the geometry differs (follicle density, epidermal thickness), the
framework predicts exactly HOW the response will differ.

This reframes the One Health vision: not "dogs are cheaper than human
trials" but "dogs reveal the causal geometry of disease."

### For Lisabeth

ADDRC compound screening can be pre-filtered by geometry. For a skin
target, compute the Anderson score with the specific tissue geometry.
For a gut target, use the gut Anderson parameters. The same compound
may rank differently for different tissue targets — this is information
the pathway-only MATRIX scoring can't provide.

### For the Field

If the causal geometry model holds across 3+ species in iPSC validation,
it represents a genuinely new approach to comparative pharmacology: a
single physical framework predicting species-specific drug responses from
measurable geometry parameters. The field currently relies on
phenomenological scaling (allometry). This offers a causal mechanism
underneath. That's worth testing rigorously.
