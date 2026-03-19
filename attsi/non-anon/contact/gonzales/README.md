# Andrea J. Gonzales, PhD — Contact & Work Log

**Position:** Assistant Professor, Pharmacology & Toxicology, MSU (2025–present)
**Previous:** Zoetis (18 years — Senior Research Fellow, Veterinary Medicine R&D)
**Lab:** Gonzales Comparative Pharmacology Lab, MSU
**Department:** https://phmtox.msu.edu/
**Domain:** Comparative pharmacology, JAK inhibitors, anti-cytokine mAbs, atopic dermatitis, One Health drug development

---

## Interview

**Date:** March 2026
**Role:** Research Associate III (Molecular Biology)
**Lab:** Gonzales Lab, Dept. of Pharmacology & Toxicology, MSU
**Focus:** iPSC-derived skin models, drug screening, molecular biology assays

---

## ecoPrimals Connection — Paper 12: Immunological Anderson

Gonzales's published work is the **primary experimental foundation** for baseCamp Paper 12
(Immunological Anderson Localization in Cytokine Signaling). Her canine AD research
provides the biological data that maps onto the Anderson framework.

**All 6 Gonzales papers are fully reproduced and three-tier validated.**

### What we've built from her work:

#### airSpring (Exp 066-069, 94/94):
- `CytokineBrain` (bingocube-nautilus) — evolutionary reservoir for AD flare prediction
  using IL-31/IL-4/IL-13 time series from G3/G4
- Tissue diversity → Anderson W mapping — McCandless/G6 cell-type heterogeneity
- Barrier state model — VG θ(h) applied to skin permeability, dimensional promotion
- Cross-species comparison — One Health bridge: Apoquel↔tofacitinib, Cytopoint↔nemolizumab
- metalForge workloads: `tissue_diversity` (GPU), `cytokine_brain` (CPU), `ad_flare_classifier` (NPU)

#### wetSpring — Immunological Anderson Framework (Exp273-279, 157/157):
- Anderson lattice with skin-layer geometry: 2D epidermis + 3D dermis (22/22)
- Barrier disruption: dimensional promotion, P06↔P12 duality proof (15/15)
- Cell-type heterogeneity sweep: 6 disease profiles, W_c detection (11/11)
- CPU parity, GPU (RTX 4070), ToadStool streaming, metalForge (109/109)

#### wetSpring — Gonzales Paper Reproductions (Exp280-286, 202/202):
- **G2 IC50 dose-response (Exp280, 35/35):** Hill equation for 6 cytokines (JAK1=10nM through IL-13=249nM), JAK selectivity profile, Anderson barrier mapping W = ln(IC50) × 4
- **G4 PK decay (Exp281, 19/19):** dose-duration regression (R²=1.0, exact fit — prior intercept bug corrected), exponential decay, pruritus time-series (oclacitinib vs prednisolone vs placebo), three-compartment cell model
- **G1 IL-31 serum (Exp282, 15/15):** AD/healthy fold-change=9.7× (Cohen's d=5.43), dose-response scratching bouts (Hill R²=0.876), receptor→lattice, Anderson spectral, cross-species
- **CPU parity (Exp283, 43/43):** Hill bit-exact, exponential regression perfect on clean data, diversity metrics match textbook to 1e-12
- **GPU validation (Exp284, 17/17):** Shannon, Simpson, Pielou, Bray-Curtis on RTX 4070
- **ToadStool streaming (Exp285, 37/37):** batched GPU pipeline, 50K-element batch parity
- **metalForge cross-substrate (Exp286, 36/36):** full CPU↔GPU + NUCLEUS atomics

### What she has that complements our computational work:

- Empirical cytokine data (IL-31 pruritus scores, dose-response curves)
- iPSC-derived skin models across species (canine, feline, human)
- Plate-based screening infrastructure
- Drug discovery pipeline and regulatory expertise
- 18 years of Zoetis data and institutional knowledge
- Wet-lab capacity to physically validate Anderson predictions

### What we bring:

- Anderson localization spatial modeling (no one else has this for immunology)
- Fajgenbaum drug repurposing bridge (MATRIX geometry scoring)
- GPU/NPU-accelerated diversity + regime classification
- Automated bioinformatics pipelines (NCBI, metagenomics)
- Cross-spring validation infrastructure (286 experiments, 7,579+ checks, 1,088 tests)
- Full three-tier portability chain: CPU → GPU → streaming → metalForge
- Published data already reproduced computationally — her lab data can refine parameters
- **Public repos she can verify:** all spring experiments are AGPL-3.0 on GitHub

### Potential collaboration areas:

1. **iPSC validation of Anderson predictions** — her iPSC skin models can test whether cytokine propagation distances match lattice predictions
2. **Receptor mapping** — NCBI Protein search for IL-31RA/IL-4Rα/OSMR expression → empirical lattice site occupancy
3. **Drug screening with Anderson geometry** — Fajgenbaum-augmented scoring applied to her plate-based screening data
4. **Cross-species validation** — canine (thin epidermis, Lz=3) vs human (thick epidermis, Lz=5) Anderson barrier predictions

---

## Publication Catalog

### Gonzales-Authored (G1–G6)

| # | Citation | Key Data | wetSpring Status |
|---|----------|----------|:----------------:|
| G1 | Gonzales AJ et al. (2013) "Interleukin-31: its role in canine pruritus and naturally occurring canine atopic dermatitis." *Vet Dermatol* 24:48-53 | IL-31 elevated in AD dog serum; IV IL-31 induces pruritus in beagles | **Exp282 DONE** (15/15) — serum levels, dose-response, receptor→lattice, Anderson spectral |
| G2 | Gonzales AJ et al. (2014) "Oclacitinib (APOQUEL) is a novel JAK inhibitor with activity against cytokines involved in allergy." *J Vet Pharmacol Ther* 37:317-324 | JAK1 IC50 = 10 nM; blocks IL-2, IL-4, IL-6, IL-13, IL-31 (IC50 36-249 nM) | **Exp280 DONE** (35/35) — Hill dose-response for all 6 cytokines, JAK selectivity, Anderson barrier map |
| G3 | Gonzales AJ et al. (2016) "IL-31-induced pruritus in dogs: a novel experimental model." *Vet Dermatol* 27:34-e10 | Standardized IL-31 pruritus model; oclacitinib > prednisolone/dexamethasone at 1,6,11,16 hr | **Exp281 DONE** (19/19, D04) — pruritus time-series, treatment comparison |
| G4 | Fleck TJ,...,Gonzales AJ (2021) "Onset and duration of action of lokivetmab in IL-31 induced pruritus." *Vet Dermatol* 32:681-e182 | Cytopoint: 3 hr onset, dose-dependent duration (14/28/42 days at 0.125/0.5/2.0 mg/kg) | **Exp281 DONE** (19/19, D01-D03) — dose-duration regression (R²=1.0, exact fit), exponential decay |
| G5 | Gonzales AJ et al. (2024) "Oclacitinib is a selective JAK1 inhibitor with efficacy in canine flea allergic dermatitis." *J Vet Pharmacol Ther* 47:447-453 | JAK1 selectivity confirmed in FAD model | **Exp280 DONE** (35/35, D03) — JAK1 selectivity in cross-disease context |
| G6 | McCandless EE, Rugg CA, Fici GJ et al. (2014) "Allergen-induced production of IL-31 by canine Th2 cells and identification of immune, skin, and neuronal target cells." *Vet Immunol Immunopathol* 157:42-48 | IL-31 produced by Th2 cells; target cells = immune, skin, neuronal | **Exp281 DONE** (19/19, D05) — three-compartment cell model, Pielou per compartment |

### Companion Literature

| # | Citation | Relevance |
|---|----------|-----------|
| F1 | Fajgenbaum DC et al. (2019) "Identifying and targeting pathogenic PI3K/AKT/mTOR signaling in IL-6 blockade–refractory iMCD." *J Clin Invest* | Pathway-based drug repurposing; mTOR cross-talks with JAK/STAT |
| F2 | Every Cure / MATRIX — ARPA-H $48.3M (2024) | 4,000 drugs × 18,000 diseases = 75M pairs scored |
| D1 | Simpson et al. (2020) "Dupilumab Phase 3 trials." *N Engl J Med* | Human anti-IL-4Rα for AD — cross-species validation |
| D2 | Silverberg et al. (2023) "JAK inhibitors in AD." *J Am Acad Dermatol* | Human equivalents of Apoquel |
| N1 | Oetjen et al. (2023) "Sensory neurons co-opt immune cells." *Cell* | IL-4/IL-13 directly sensitize sensory neurons |
| N2 | Cohen et al. (2022) "Neuro-immune interactions in AD." *Sci Immunol* | Bidirectional neuron-immune communication in skin |

---

## Career Timeline

| Year | Role | Organization |
|------|------|-------------|
| ~2007–2025 | Senior Research Fellow → Principal Scientist (Vet Med R&D) | Zoetis (Kalamazoo, MI) |
| 2025–present | Assistant Professor, Pharmacology & Toxicology | Michigan State University |

Key contributions at Zoetis:
- Co-developed oclacitinib (Apoquel) — first JAK inhibitor for veterinary use
- Co-developed lokivetmab (Cytopoint) — first anti-cytokine mAb for veterinary use
- Established IL-31 pruritus model in beagles (standardized experimental platform)
- Published canine→human translation data supporting human drug development

---

## Repurposing Targets (Anderson-Filtered)

From Paper 12 §3.3 — drugs scored by pathway match × tissue geometry:

| Drug (Original Use) | Pathway | Anderson Score | Repurposing Logic |
|---------------------|---------|:--------------:|-------------------|
| Rapamycin/sirolimus (transplant) | mTOR (PI3K/AKT cross-talk) | HIGH | Fajgenbaum proved efficacy in cytokine storms |
| Tofacitinib (RA) | JAK1/JAK3 | HIGH | Human equivalent of Apoquel |
| Tanezumab (OA pain) | Anti-NGF mAb | HIGH | NGF elevated in AD skin |
| Trametinib (melanoma) | MEK/ERK (downstream IL-31RA) | MODERATE | ERK activated by IL-31 |
| Crisaborole (mild AD) | PDE4 | LOW→MOD | Limited by 2D barrier penetration |
| Nemolizumab (prurigo nodularis) | Anti-IL-31RA mAb | HIGH | Human equivalent of Cytopoint |

---

## Public Spring Repositories (Referenceable)

All spring repos are public under AGPL-3.0. These are what the `computational_brief.md` points to.

| Repository | URL | Gonzales Experiments | Checks |
|------------|-----|----------------------|:------:|
| wetSpring | https://github.com/syntheticChemistry/wetSpring | Exp 273–286 (Anderson framework + G1–G6 reproductions) | 359/359 |
| airSpring | https://github.com/syntheticChemistry/airSpring | Exp 066–069 (CytokineBrain, tissue diversity, barrier, cross-species) | 94/94 |
| neuralSpring | https://github.com/syntheticChemistry/neuralSpring | nS-601–605 (dose-response, PK, tissue lattice, MATRIX) | 329/329 |
| groundSpring | https://github.com/syntheticChemistry/groundSpring | Exp 008, 012, 015, 018 (Anderson spectral, transport, uncertainty) | 236+ |
| hotSpring | https://github.com/syntheticChemistry/hotSpring | (not directly Gonzales — plasma physics, lattice QCD) | 664+ |

**Total Gonzales-specific checks across springs: 782/782**

---

## Documents

| File | Purpose | When to Send |
|------|---------|:------------:|
| `email_post_interview.md` | Draft thank-you email with notes on tone, context, and strategy. | **Now** (first contact post-interview) |
| `computational_brief.md` | **Sendable** — technical brief summarizing our computational modeling of her published data. Covers dose-response, PK decay, pruritus model, 3D tissue lattice, Fajgenbaum MATRIX, and public repo links. | **Attach to thank-you email** |
| `spring_validation_brief.md` | **Sendable** — detailed validation evidence: what was reproduced from G1–G6, what was extended (Anderson framework, CytokineBrain, Fajgenbaum MATRIX), four-tier validation chain across wetSpring + neuralSpring + airSpring. Shows the 782/782 check breakdown. | Second conversation (if she engages) |
| `../hotspring_evolution_brief.md` | **Sendable** — general-audience brief showing the full pipeline evolution (CERN → Python → Rust CPU → BarraCUDA GPU → Brain architecture). Demonstrates scale, speed, and infrastructure maturity. Not Gonzales-specific — can be sent to anyone. | If she asks about infrastructure |

---

## neuralSpring Session 107 — Extended Implementation (March 2, 2026)

Deepened the computational implementation with three areas:

**Gonzales modeling (nS-601/602/603):** Generalized Hill dose-response for all
6 cytokines, exponential PK decay, lokivetmab log-linear regression (exact fit,
R² = 1.0 — prior 1.7-day bias was an intercept bug, now corrected), pruritus
time-series treatment decay model.

**3D tissue lattice (nS-604):** Three-compartment disorder analysis
(immune/skin/neural), multi-layer Anderson Hamiltonian, level spacing ratio
from sorted eigenvalues, barrier promotion spectral sweep (2D→3D).

**Fajgenbaum MATRIX (nS-605):** 6 drug candidates scored with
pathway × geometry × disorder. Tofacitinib #1, Trametinib #5 (pathway mismatch).
Crisaborole geometry improves with chronic barrier breach. Integrated
dose-response × MATRIX end-to-end chain.

**Validation:** Python 48/48, Rust 240/240, 27 unit tests — all PASS.

---

## Interaction Log

| Date | Type | Notes |
|------|------|-------|
| March 2026 | Job interview | RA III Molecular Biology, Gonzales Lab, MSU Pharmacology & Toxicology. Focus: iPSC-derived skin models, drug screening, molecular biology assays. |
| March 2026 | Interview outcome | **Went great.** She appreciates the data science / analytics dimension. Introduced me to Erika Lisabeth (Director, ADDRC) in MSU Drug Discovery. This connects our Fajgenbaum MATRIX scoring directly to institutional HTS infrastructure. |
| March 2026 | Sent data draft | Sent `computational_brief.md` before the interview. She has now seen the computational modeling of her published data. |
| March 2026 | Lisabeth introduction | Gonzales introduced me to Lisabeth in person. Had the specificity/binding conversation that became Track 9 (low-affinity binding, hormesis). See `contact/lisabeth/` for details. |
| March 2026 | Post-interview | Track 9 built: exp097 (affinity landscape), exp098 (toxicity), exp099 (hormesis), exp111 (causal terrarium). 65+ tests, 76 validation checks. 8 testable experimental hypotheses ready for grant writing. See `healthSpring/work/EXPERIMENTAL_HYPOTHESES.md`. |

### MSU Drug Discovery Connection (via Gonzales referral)

Gonzales referred me to the MSU Drug Discovery program, specifically:

**Erika Lisabeth, PhD** — Director, ADDRC (Assay Development and Drug Repurposing Core)
- Same department: Pharmacology & Toxicology, MSU
- https://drugdiscovery.msu.edu/about-us/people/erika-lisabeth-ph-d.aspx
- UCSD PhD (chemistry/biochemistry), Sanford Burnham Prebys postdoc
- Domain: HTS assay development, drug repurposing, chemical probes
- Equipment: plate readers, high-content microscopes, liquid-handling robots, GREENScreen informatics
- Published: screened 8,000+ small molecules for Brucella host-cellular pathways (2024)
- Research: EphA3 receptor tyrosine kinase (cancer), NF-κB degradation pathway

**The pipeline this creates:**

```
Anderson-augmented MATRIX scores (nS-605)
    → ADDRC high-throughput screening (Lisabeth, 8,000+ compound library)
    → iPSC skin model validation (Gonzales, canine/feline/human)
    → Medicinal chemistry optimization (Ellsworth, MSU Drug Discovery)
```

This is exactly the computation → screening → validation workflow described
in `computational_brief.md` and `spring_validation_brief.md`, but now with
institutional infrastructure behind it. The ADDRC is literally a drug
repurposing core — our nS-605 Fajgenbaum MATRIX extension was built for
this use case.

**Also in MSU Drug Discovery:**

| Person | Role | Relevance |
|--------|------|-----------|
| **Richard Neubig, MD PhD** | Prof Emeritus, Director Drug Discovery Program | GPCR signaling, Rho/MRTF/SRF inhibitors for **skin fibrosis** and melanoma. Founded UMich Center for Chemical Genomics, established MSU Drug Discovery. Skin fibrosis connects to AD barrier models. |
| **Edmund Ellsworth, PhD** | Interim Director Drug Discovery, Director Medicinal Chemistry | Synthetic/heterocyclic chemistry, niclosamide delivery, terpene biosynthesis. Medicinal chemistry optimization downstream of HTS hits. |
