# baseCamp Domain Paper Targets — Journal Submission Strategy

**Purpose:** Identify target journals, co-authors, and submission requirements
for the three highest-readiness baseCamp papers.
**Date:** August 25, 2026

---

## Priority 1: Paper 01 — Anderson Localization as QS Null Hypothesis

### Validation Evidence
- 198 experiments, 3,700+ checks (all PASS)
- W_c = 16.26 ± 0.95 (finite-size scaling)
- 28/28 biomes QS-active in 3D, 0/28 in 2D/1D
- EMP Atlas: 30,002 synthetic samples across 14 EMPO biome categories (55ms)
- V110: O₂-modulated W model (r=0.851)
- Python bit-identical parity (15 domains)
- Three genuine NP solutions identified (V. cholerae, M. xanthus, Dictyostelium)

### Novelty Claim
No prior work applies Anderson localization to quorum sensing (confirmed via
literature search, February 2026). First quantitative null hypothesis for QS
based on physical geometry.

### Target Journals (ranked)

| Journal | Impact | Fit | Notes |
|---------|--------|-----|-------|
| **Nature Communications** | ~17 | Excellent — cross-domain physics×biology | Requires experimental validation (wet lab) |
| **ISME Journal** | ~11 | Core audience — microbial ecology | Strong computational papers accepted |
| **mBio** | ~7 | ASM flagship — broad microbiology | Open access, good for first pub |
| **Physical Review E** | ~2.5 | Physics audience — Anderson community | Would establish cross-domain credibility |
| **PLOS Computational Biology** | ~4 | Computational methods | Lower bar, open access |

### Recommended Path
**mBio** (first) or **ISME Journal** — strongest fit for computational
microbial ecology with physics framework. Nature Communications requires
wet-lab validation that doesn't exist yet.

### Faculty Anchors / Potential Co-Authors

| Person | Affiliation | Contribution | Status |
|--------|-------------|-------------|--------|
| Christopher Waters | MSU Microbiology | QS domain expert; 7 papers reproduced | Not contacted for co-authorship |
| Ilya Kachkovskiy | MSU Mathematics | Anderson math; 11 papers reproduced | Not contacted |
| Emily Dolson | MSU CSE | Constrained evolution / NP framing | Not contacted |
| Rika Anderson | Carleton College | Extremophile population genomics | Not contacted |

### Pre-Submission Gaps
- [ ] Contact Waters for domain review and potential co-authorship
- [ ] Contact Kachkovskiy for mathematical review
- [ ] Run 299K QS gene cold-seep validation (proposed §6.1, data available)
- [ ] Format in target journal style
- [ ] Write cover letter
- [ ] Prepare supplementary materials (experiment IDs, reproduction scripts)

---

## Priority 2: Paper 06 — No-Till Anderson (Dimensional Collapse)

### Validation Evidence
- Track 4 complete: 9 papers reproduced, 321 checks (all PASS)
- Dynamic W(t) models (Exp186)
- airSpring: GPU van Genuchten, pedotransfer, Anderson coupling (55+95 checks)
- groundSpring: ET₀→Anderson propagation, no-till vs tilled 16S (H'=3.88 vs 1.57)
- EMP Atlas confirms Anderson-QS across soil biomes

### Novelty Claim
First application of Anderson localization to explain the mechanism behind
no-till soil health benefits. Tillage = dimensional collapse of 3D pore
network → QS suppression → microbial community disruption.

### Target Journals (ranked)

| Journal | Impact | Fit | Notes |
|---------|--------|-----|-------|
| **Nature Communications** | ~17 | Strong — Martínez-García/Feng precedent | Requires field data validation |
| **Soil Biology & Biochemistry** | ~9 | Core soil science audience | Computational papers published |
| **ISME Journal** | ~11 | Microbial ecology → soil intersection | Good secondary target |
| **Agronomy Journal** | ~2 | Applied agriculture | Lower bar, broad readership |
| **Geoderma** | ~6 | Soil science, global readership | Physics-soil crossover |

### Recommended Path
**Soil Biology & Biochemistry** — core audience, computational papers
accepted, field-data validation would strengthen but isn't required for
a computational/theoretical contribution.

### Faculty Anchors / Potential Co-Authors

| Person | Affiliation | Contribution | Status |
|--------|-------------|-------------|--------|
| Younsuk Dong | MSU BAE | airSpring/irrigation; 3,123+ checks, FAO-56 | Active collaborator |
| OSU Soil Fertility Lab | Ohio State | 60-year Triplett-Van Doren experiment data | Data is public |
| David Brandt legacy | Carroll, Ohio | 50-year natural experiment (Islam 2014) | Data is public |

### Pre-Submission Gaps
- [ ] Pull real LTER/field 16S data via NestGate (OSU/Brandt)
- [ ] Run Exp D: Process OSU 16S through sovereign pipeline
- [ ] Validate coupled moisture-geometry model θ(t)→d_eff(t)→r(t) on field data
- [ ] Format in target journal style
- [ ] Contact Dong for co-authorship confirmation

---

## Priority 3: Paper 12 — Immunological Anderson + Fajgenbaum Bridge

### Validation Evidence
- wetSpring: 359/359 checks (Exp273-286)
- neuralSpring: 329/329 checks (nS-601-605)
- airSpring: 94/94 checks (Exp066-069)
- groundSpring: cross-validated
- Gonzales G1-G6: 782/782 reproductions
- nS-605 Anderson-augmented MATRIX scores: 6 drug candidates
- W↔P(QS) correlation r=-0.924

### Novelty Claim
First application of Anderson localization to cytokine propagation in
inflamed tissue. AD barrier disruption = dimensional promotion (inverse
of Paper 06 tillage collapse). Fajgenbaum MATRIX gains geometry dimension
via Anderson transport.

### Target Journals (ranked)

| Journal | Impact | Fit | Notes |
|---------|--------|-----|-------|
| **Science Translational Medicine** | ~18 | Translational drug discovery | Requires wet-lab validation |
| **Journal of Investigative Dermatology** | ~7 | Core dermatology | Strong computational+immunological |
| **Drug Discovery Today** | ~7 | Drug discovery methodology | Computational papers welcome |
| **Veterinary Dermatology** | ~2 | Canine foundation (Gonzales domain) | Lower impact but core audience |
| **Cell Reports Medicine** | ~14 | Broad biomedical | High bar |

### Recommended Path
**Drug Discovery Today** or **Journal of Investigative Dermatology** first.
Science Translational Medicine requires ADDRC wet-lab validation (nS-605
compound screening) which hasn't happened yet.

### Faculty Anchors / Potential Co-Authors

| Person | Affiliation | Contribution | Status |
|--------|-------------|-------------|--------|
| Andrea J. Gonzales | MSU Pharm/Tox | Primary domain expert, G1-G6 data | ACTIVE — GPS assigned Jun 5 |
| Erika Lisabeth | MSU ADDRC | HTS 8K compound library | Referenced, not engaged |
| Richard Neubig | MSU Drug Discovery | Rho/skin fibrosis cross-talk | Open question |
| David Fajgenbaum | UPenn / Every Cure | MATRIX paradigm | External validation target |

### Pre-Submission Gaps
- [ ] Secure Gonzales co-authorship (active relationship)
- [ ] Confirm Gonzales ORCID
- [ ] Schedule ADDRC screening of nS-605 top candidates with Lisabeth
- [ ] Resolve Rho/MRTF/SRF ↔ JAK/STAT cross-talk question with Neubig
- [ ] Format in target journal style
- [ ] Prepare supplementary data (experiment IDs, check counts)

---

## Cross-Cutting Submission Decisions

### Sovereign Science vs. Traditional Journal

Per `SOVEREIGN_SCIENCE.md`, ecoPrimals favors open publication with named
review over traditional journal gatekeeping. Options:

| Path | Pros | Cons |
|------|------|------|
| **Traditional journal** | Impact factor, citation, credibility for grants | Slow (6-18 months), paywall, format constraints |
| **arXiv preprint + journal** | Speed + credibility | Two rounds of formatting |
| **sporePrint + named review** | Full sovereignty, immediate, verifiable | No impact factor, no institutional recognition |
| **JOSS (software papers)** | Open, quick, citable DOI | Only for software, not science claims |

### Recommended Hybrid
1. Post preprint to arXiv (or bioRxiv for biology papers)
2. Submit to target journal simultaneously
3. Link sporePrint evidence page in preprint
4. pseudoSpore artifact available for reviewer validation

This gives speed (preprint), credibility (journal), and sovereignty
(sporePrint + pseudoSpore).

---

## Priority Order

| Priority | Paper | Journal target | Key blocker | Timeline |
|----------|-------|---------------|-------------|----------|
| **0** | arXiv QCD (not baseCamp) | hep-lat | LaTeX assembly | Weeks |
| **1** | Paper 01 (Anderson QS) | mBio / ISME | Faculty contact | 2-3 months |
| **2** | Paper 06 (No-Till) | Soil Biol & Biochem | Field data pull | 3-4 months |
| **3** | Paper 12 (Immuno Anderson) | Drug Disc Today / JID | ADDRC screening | 6-12 months |

---

*The arXiv QCD preprint is the beachhead. It proves Kevin Mok publishes
real science. Papers 01, 06, and 12 follow in order of readiness.
Each publication becomes a credential that opens the next policy door.*
