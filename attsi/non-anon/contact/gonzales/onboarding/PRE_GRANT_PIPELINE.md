<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# The Pre-Grant Pipeline: Open Data, Open Systems, Zero University Cost

**Audience:** Gonzales, Lisabeth, Drug Discovery Program, grant reviewers
**Core idea:** Run the entire computational discovery pipeline — from question
to testable hypothesis to preliminary data — on open data and free software
before the university spends a dollar.

---

## The Proposition

Before we ask for grant money, we prove the approach works. Before we touch
a plate reader or an iPSC line, we extract every insight that public data
can give us. Before we spend a single reagent, we know exactly which
compounds to test and why.

This is not "do the computation after the experiment." This is computation
**as the experiment** — at zero cost, at zero risk, producing real
preliminary data that makes the grant application undeniable.

### What Zero-Cost Means

| Resource | Cost | Who Provides |
|----------|:----:|:------------:|
| Software (computational pipeline) | $0 | Open source (AGPL-3.0) |
| Hardware (biomeGate in lab) | $0 to university | I bring it |
| ICER GPU access | $0 (existing allocation) | MSU provides |
| Public data (PubChem, ChEMBL, etc.) | $0 | Federal investment |
| Researcher time | Already hired | RA III position |
| **Total cost to university** | **$0** | |

The entire pre-grant pipeline runs on resources that already exist. The
university takes no financial risk. The output is real preliminary data
that funds the wet-lab work.

---

## Why This Changes Drug Discovery

### The Traditional Pipeline

```
1. Write grant proposal (6-12 months, speculative)
2. Get funding (if lucky: 10-20% success rate)
3. Screen compounds (6 months, $50K-200K reagents)
4. Analyze results (months, $6K-20K software licenses)
5. Identify hits (maybe 50 compounds out of 8,000)
6. Validate hits in cell models (6 months, $20K-50K)
7. Write paper
8. Write next grant
```

**Time to first insight: 2-3 years. Cost: $300K-500K. Risk: high.**

### The Pre-Grant Pipeline

```
1. Download public data (Day 1)
2. Compute binding landscapes across targets (Week 1)
3. Predict which compounds to test and why (Week 2)
4. Identify species-specific causal mechanisms (Week 3)
5. Generate preliminary data (Month 1)
6. Write grant WITH preliminary results (Month 2-3)
7. Get funding (higher success: you already have data)
8. Run the wet-lab experiments the computation designed (efficient)
```

**Time to first insight: 2-3 weeks. Cost: covered by the table above.**

The wet lab doesn't disappear — it gets better. Every experiment is
designed by the computation. Every compound is chosen for a reason.
Every result feeds back into the model. The wet lab validates
predictions instead of fishing for hits.

---

## The Causal Question: Why Does Cat Skin ≠ Dog Skin ≠ Human Skin?

This is the question that makes everything else work. And it's the kind of
question computation can explore before any wet-lab time is spent.

### Background: Anderson Localization

Anderson localization (Nobel Prize, 1977) is a physics result: signals
traveling through disordered media can become trapped rather than
propagating freely. Whether trapping occurs depends on two things —
**dimensionality** (2D vs 3D) and **disorder** (how heterogeneous the
medium is). In 2D, signals always localize. In 3D, they propagate unless
disorder exceeds a critical threshold.

We apply this to biological tissue: cytokine signals propagating through
skin. The dimensionality and disorder of the tissue determine whether
inflammatory signals spread or stay localized — which determines disease
severity and drug response.

### What We Know

Gonzales's lab works across species — canine, feline, human iPSC models.
The same diseases (atopic dermatitis, allergic response, pruritus) present
differently across species. The same drugs work differently. Current
pharmacology describes this with species-specific parameters:

- Different IC50 values per species
- Different clearance rates (allometric scaling CL ∝ BW^0.75)
- Different volumes of distribution
- Different tissue binding

This is **phenomenological** — it describes WHAT differs, not WHY.

### What Anderson Predicts (Causal)

The Anderson framework says: the **geometry** of the tissue determines
signal propagation. The parameters differ BECAUSE the geometry differs.

| Tissue Property | Cat | Dog | Human | Anderson Consequence |
|-----------------|-----|-----|-------|---------------------|
| Epidermis thickness | ~15 µm | ~25 µm | ~75 µm | Thicker barrier → stronger 2D localization → more cytokine confinement |
| Dermal cell diversity | Moderate | High (Th2-dominant) | Very high | Higher diversity W → signals propagate more in 3D dermis |
| Hair follicle density | ~800/cm² | ~1500/cm² | ~100/cm² | Follicles = dimensional promotion channels through epidermis |
| Sebaceous gland distribution | Concentrated | Distributed | Mixed | Affects drug penetration geometry |
| Nerve ending density | High | Very high | Moderate | IL-31 → nerve → itch pathway architecture |
| d_eff (effective dimension) | ~2.3 | ~2.7 | ~2.2 | Higher d_eff → more propagation → more AD severity |

**The prediction:** Dogs get worse atopic dermatitis than cats or humans
because their skin geometry (thin epidermis + high follicle density + high
dermal diversity) creates more 3D propagation channels for cytokines.
Hair follicles are dimensional promotion channels — each one is a 3D tube
through the 2D epidermal barrier.

This is testable — and if it holds, it offers a causal framework for the
comparative pharmacology data that currently relies on species-specific
curve fitting.

### What We Can Compute Today (Open Data)

| Analysis | Data Source | What It Reveals |
|----------|-----------|-----------------|
| Cross-species skin cell composition | Published histology (literature) | Pielou evenness → Anderson W per species |
| Hair follicle geometry modeling | Dermatology textbooks + measurements | d_eff per species |
| IL-31RA receptor distribution | UniProt + NCBI Gene Expression | Receptor lattice occupancy per compartment |
| Cross-species IC50 comparison | G2 (canine) + published human JAK IC50 | Barrier height mapping per species |
| Lokivetmab vs nemolizumab PK | G4 (canine) + published human mAb PK | Allometric scaling accuracy |
| Three-compartment W per species | G6 (canine) + published human tissue data | Cross-compartment variance predicts AD severity |

### What This Means for Drug Discovery

If skin geometry CAUSES the different drug responses, then:

1. **You can predict drug efficacy from tissue geometry** — before any
   screening. Measure the Anderson parameters of the target tissue, compute
   which drugs will propagate to their targets.

2. **Species translation becomes physics** — not empirical curve fitting.
   Change the geometry parameters (epidermal thickness, follicle density,
   cell diversity), and the model predicts the species-specific response.

3. **iPSC models can be designed by the computation** — instead of just
   growing iPSC cells and testing drugs, grow iPSC tissues with specific
   geometries and test whether the Anderson predictions hold. This is
   **causal validation**.

4. **New therapeutic modalities emerge** — if follicles are propagation
   channels, then follicle-targeted delivery changes the effective
   dimension. Anderson predicts which delivery routes are optimal for
   which skin conditions.

---

## The Range Expansion

### What Open Data Gives Us That Internal Data Can't

Internal lab data is deep but narrow — a few species, a few drug classes,
a few tissue types. Open data is broad:

| Dimension | Internal Data | Open Data |
|-----------|:------------:|:---------:|
| Species | 3 (dog, cat, human) | 50+ (veterinary + wildlife + model organisms) |
| Drug targets | JAK/cytokine pathway | 15K+ targets (ChEMBL) |
| Compounds | ADDRC 8K library | 115M+ (PubChem) |
| Tissue types | Skin (iPSC) | All tissues with published histology |
| Microbiome | Future lab samples | 300K+ samples (NCBI SRA) |
| Protein structures | Target of interest | 200K+ (PDB) + 200M+ (AlphaFold) |

The computation generates hypotheses across this space. The lab tests
the most promising ones. See `DATA_SOURCES_AND_INTEGRATION.md` for
the full catalog with URLs and access instructions.

### Pre-Grant Experiments by Expansion Axis

**Cross-species expansion (open data):**

| Experiment | Species | Data Source | Question |
|------------|---------|-------------|----------|
| Skin geometry → Anderson W | Dog, cat, human, horse, rat, mouse | Published histology | Which species has highest d_eff? |
| Follicle density → dimensional promotion | Dog, cat, human | Dermatology literature | Do follicles predict AD severity? |
| Sebaceous distribution → drug penetration | Dog, cat, human | Published skin models | Does geometry predict topical efficacy? |
| Cross-species IC50 → barrier height | Dog, cat, human | ChEMBL + G2 | Is the IC50 difference geometry-driven? |
| Gut microbiome W per species | Dog, cat, human | NCBI SRA (gut 16S) | Do gut Anderson parameters correlate with drug metabolism? |

**Cross-target expansion (open data):**

| Experiment | Targets | Data Source | Question |
|------------|---------|-------------|----------|
| Full JAK/STAT binding landscape | JAK1, JAK2, JAK3, TYK2 | PubChem BioAssay | Which JAK subtypes have the broadest low-affinity binder pools? |
| Cytokine receptor cross-reactivity | IL-31RA, IL-4Rα, OSMR | ChEMBL | Do any compounds hit all three weakly? |
| Rho/MRTF/SRF overlap | Neubig targets | ChEMBL | Do fibrosis pathway compounds show AD cross-reactivity? |
| EphA3 binding landscape | Lisabeth target | PubChem + BindingDB | Low-affinity EphA3 binders as cancer selectivity candidates? |

**Cross-disease expansion (open data):**

| Experiment | Disease | Connection | Question |
|------------|---------|------------|----------|
| AD → psoriasis Anderson comparison | Psoriasis | Same tissue, different immune axis | Does geometry distinguish AD from psoriasis? |
| AD → asthma barrier disruption | Asthma | Epithelial barrier disease (lung vs skin) | Is lung epithelium Anderson-equivalent to skin epidermis? |
| AD → IBD gut barrier | IBD | Epithelial barrier disease (gut vs skin) | Does Anderson W correlate with barrier disease severity? |
| AD → food allergy immunomodulation | Food allergy | Hygiene hypothesis, immune calibration | Can hormesis models predict oral tolerance? |

---

## The Data Extraction Advantage

### More Signal From the Same Experiments

Traditional HTS extracts one number per compound: IC50 (or "inactive").
Our pipeline extracts from the same dose-response curve:

| Traditional Extraction | Our Extraction |
|----------------------|----------------|
| IC50 (one number) | IC50 (one number) |
| | Hill slope (cooperativity) |
| | Emax (maximum effect) |
| | Composite binding score (across targets) |
| | Binding breadth (Gini coefficient) |
| | Toxicity IPR (organ-specific risk) |
| | Hormetic zone boundaries (sub-IC50 benefit) |
| | Anderson barrier height (W from IC50) |
| | Cross-reactivity profile (against all targets) |
| | MATRIX score (with tissue geometry) |
| | **10× more information from the same experiment** |

### How Internal Data Layers On Top

The public data calibrates the models. The internal data sharpens them:

```
PUBLIC DATA (broad, calibration)
────────────────────────────────
PubChem: 115M compounds × IC50
ChEMBL: 2.4M × 15K targets
BindingDB: 2.8M binding affinities
HMP: 300+ healthy gut microbiomes
Published histology: skin geometry per species
    │
    ↓ Models calibrated on public data
    │
INTERNAL DATA (deep, refinement)
────────────────────────────────
ADDRC: 8K compounds × full dose-response
Gonzales iPSC: species-specific viability
Lab microbiome: actual patient/animal communities
Real tissue imaging: actual d_eff measurements
    │
    ↓ Models refined with internal data
    │
PREDICTIONS (testable, specific)
────────────────────────────────
"This compound (ADDRC #4721) should show 3.2× wider therapeutic
window in human iPSC vs canine iPSC because human epidermal d_eff
is 0.5 lower, confining the toxic signal more effectively."
```

That prediction is generated computationally. Testing it costs one iPSC
experiment. If it holds, it's the preliminary data for an R01.

---

## The Pipeline as Grant Engine

### How Pre-Grant Data Feeds Grant Success

| Pre-Grant Result | Grant It Enables | Reviewer Reaction |
|-----------------|-----------------|-------------------|
| PubChem binding landscape shows 2,400 broad-weak JAK binders in public data | NCI R21 (H1) | "They already identified candidates from public data" |
| ChEMBL cross-reactivity reveals drug class with hidden immunomodulation | NIAID R21 (H8) | "Computational evidence is compelling" |
| Cross-species Anderson W predicts dog > human AD severity from geometry alone | NIGMS R01 (H2) | "This is a novel causal framework" |
| DrugBank allometric scaling matches published human PK within 15% | NIGMS supp (H6) | "Open-source replacement validated" |
| Hormesis model correctly predicts 8/10 known hormetic responses from literature | NIGMS R21 (H3) | "Model is already validated on external data" |

Reviewers see: **preliminary data generated before funding was requested**,
from a validated pipeline, with testable predictions that the proposed
experiments will evaluate. The grant doesn't ask "can we build this?" — it
asks "should we fund the validation of predictions we already have?"

### Yearly Output Trajectory

| Period | Activity | Output |
|--------|----------|--------|
| **Month 0-3** | Pre-grant pipeline on open data | 5-10 computational pilot studies, preliminary data |
| **Month 3-6** | Write R21 proposals (2-3) | Proposals with computational preliminary data |
| **Month 6-9** | First ADDRC data access → refined predictions | Brucella reanalysis, 8K compound scoring |
| **Month 9-12** | iPSC pilot experiments validating predictions | Wet-lab data confirming/refining computational models |
| **Year 1-2** | R21 funding → expanded validation | Funded wet-lab experiments, model refinement |
| **Year 2-3** | R01 proposals with validated pipeline | Large-scale proposals with published pilot results |

---

## Why This Is the Core of Drug Discovery

Drug discovery is pattern recognition across an impossibly large space:
millions of compounds × thousands of targets × hundreds of tissues ×
dozens of species × infinite disease states.

Traditional drug discovery explores this space experimentally — one
compound at a time, one tissue at a time, one species at a time.
It's expensive, slow, and misses most of the space.

The pre-grant pipeline inverts this: **explore the space computationally,
then experiment only where the computation says to look.** The space is
the same. The coverage is vastly larger. The marginal cost of each
additional hypothesis is near zero.

The Anderson framework gives us the causal engine: tissue geometry
determines signal propagation. Change the geometry (different species,
different tissue, different disease state), and the model predicts what
changes. The model doesn't replace the experiment — it tells you which
experiment to run next.

That's the core of what we're proposing: **computation decides what to
ask, the bench decides what's true.**

When computation is near-free, what's valuable is the expertise — the
bench scientist who can run the experiment the computation designed, in
the tissue system the model identified, and interpret the result in the
context of the causal framework. Every pilot on open data, every
connection with another MSU lab, every piece of preliminary data exists
to fund the wet-lab work that answers the real biological questions.

This package is also a collaboration tool. Any PI at MSU with
dose-response data, tissue models, or compound libraries can plug into
this pipeline. The computation runs their data for free. What we get
back is experimental validation, new parameters for the models, and
co-investigator relationships that strengthen grant proposals. The Drug
Discovery Program grows by making other labs more productive.

---

## Document Map

**In this folder (onboarding/):**

| Document | What It Contains |
|----------|-----------------|
| This document | The pre-grant pipeline rationale |
| Lab Onboarding Package | Master Day 1 document — start here |
| Data Sources & Integration | Detailed catalog of open data with URLs |
| Cost & Compute Brief | biomeGate + ICER specs and cost analysis |
| Pilot Experiments | 14 specific pilot experiments with timeline |
| Cross-Species Causal Model | The geometry → drug response framework |

**Also relevant (in parent directories):**

| Document | What It Contains |
|----------|-----------------|
| Gonzales computational brief | Technical brief for Dr. Gonzales |
| Gonzales validation brief | 782/782 checks against published data |
| Lisabeth computational brief | ADDRC-focused brief for Dr. Lisabeth |
| Lisabeth binding landscape brief | Low-affinity binding analysis for ADDRC |
| Experimental Hypotheses | 8 grant-ready proposals with budgets |
