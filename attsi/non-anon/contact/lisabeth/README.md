# Erika Lisabeth, PhD — ADDRC Director, MSU Pharmacology & Toxicology

**URL:** https://drugdiscovery.msu.edu/about-us/people/erika-lisabeth-ph-d.aspx
**Domain:** HTS assay development, drug repurposing, chemical probes, EphA3 RTK, NF-κB
**Department:** Pharmacology & Toxicology, MSU (same as Gonzales)
**Facility:** Assay Development and Drug Repurposing Core (ADDRC)
**Equipment:** Plate readers, high-content microscopes, liquid-handling robots,
GREENScreen informatics, 8,000+ compound library
**PhD:** Chemistry/Biochemistry, UC San Diego; Postdoc: Sanford Burnham Prebys

---

## Connection

Referred by Andrea Gonzales during RA III interview (March 2026). Gonzales
brought me to meet her and the Drug Discovery team after the interview.

## Meeting (March 2026)

Met in person via Gonzales introduction. The conversation that matters:

**The binding question:** She described how HTS screens work — dose-response
curves, Z' quality metrics, SSMD hit classification, the standard workflow.
Compounds that don't hit hard enough against a specific target get classified
"inactive" and discarded. The whole pipeline optimizes for strong, specific
binding.

This is where the low-affinity idea crystallized: **what if the compounds
we discard as inactive are actually functional in a different mode?** Not
as single-target scalpels but as distributed, weak, combinatorial binders
that work through coincidence detection.

The conversation was about specificity vs breadth. She knows the data —
she's been running these screens. The question is whether her existing
dose-response data (which she already HAS for 8,000 compounds) can be
reanalyzed through a different lens.

## What She Has That We Need

1. **Full dose-response curves** for 8,000+ compounds — not just hit/miss,
   but the entire affinity landscape including the low-affinity tail
2. **GREENScreen informatics** — structured data management for compound
   metadata and screening results
3. **Liquid-handling robots** — capacity for custom assay configurations
   (extended dose-response, sub-IC50 concentrations)
4. **Lisabeth Brucella screen (2024)** — 8,000+ small molecules screened
   against Brucella host-cellular pathways. This is real HTS data with full
   dose-response that can serve as proof-of-concept
5. **EphA3 kinase expertise** — receptor tyrosine kinase work (cancer
   relevance for multi-target binding hypothesis)

## What We Bring to ADDRC

1. **Computational triage** — Anderson-augmented MATRIX scores rank 8K
   compounds before they touch a plate reader ($0.01 vs $210K/pipeline)
2. **Low-affinity analysis** — models that find value in "inactive"
   compounds (exp097: 26× selectivity from weak binders)
3. **Toxicity prediction** — Anderson IPR predicts organ-specific toxicity
   from binding distribution (exp098)
4. **Hormesis detection** — extended dose-response model detects biphasic
   effects invisible to standard analysis (exp099)
5. **Automated data science** — statistical analysis, dose-response fitting,
   Z' calculation, SSMD — all sovereign, all reproducible

## The Pitch

Your 8,000-compound library already contains the data. Every dose-response
curve you've run includes the low-affinity tail. Our computational models
predict that the compounds you're currently discarding as "inactive" include:
- Cancer-selective multi-target binders (coincidence detection)
- Hidden immunomodulators (distributed weak binding)
- Hormetic agents (beneficial at sub-IC50 doses)

We're not asking you to run new screens. We're asking to look at existing
data through a new lens. The experiments to test our predictions use your
existing infrastructure.

## Relevant Spring Work

| Artifact | Location | What It Shows |
|----------|----------|---------------|
| ADDRC HTS analysis (exp091) | healthSpring | Z', SSMD, hit classification |
| Compound library IC50 (exp092) | healthSpring | 8K batch processing |
| Low-affinity selectivity (exp097) | healthSpring | 26× selectivity |
| Toxicity landscape (exp098) | healthSpring | Anderson toxicity IPR |
| Hormesis framework (exp099) | healthSpring | Biphasic dose-response |
| Causal terrarium (exp111) | healthSpring | Molecular → ecosystem chain |
| MATRIX + Anderson (exp090) | healthSpring | Drug repurposing with geometry |
| Drug Discovery Pipeline | attsi/non-anon/publicRelease/ | Full architecture doc |

## Papers to Look For

- Lisabeth et al. (2024) — Brucella host-cellular pathways (8,000+ small
  molecule screen). This is the proof-of-concept dataset.
- EphA3 kinase mutation work (postdoc era) — receptor tyrosine kinase
  relevant to multi-target binding

## ecoPrimals Connection

- **gen3 baseCamp Paper 12**: Anderson immunological signaling → ADDRC pipeline
- **gen3 baseCamp Paper 14**: Anderson hormesis → low-affinity binding → ADDRC data
- **healthSpring baseCamp gonzales/**: Full pipeline doc
- **healthSpring baseCamp fajgenbaum/**: MATRIX comparison (ADDRC as wet-lab front end)

## Grant Alignment

| Mechanism | Title (short) | Lisabeth Role |
|-----------|---------------|---------------|
| NCI R21 | Low-affinity cancer selectivity | ADDRC data + screen design |
| NIGMS R21 | Hormetic dose-response | Extended dose-response protocol |
| NIAID R21 | Hidden immunomodulators | Compound selection from existing library |
| NIAMS R01 | Anderson-augmented MATRIX | ADDRC 8K library screening |

See `healthSpring/work/EXPERIMENTAL_HYPOTHESES.md` for full details.

## Documents

- `computational_brief.md` — Technical brief for Lisabeth audience
- `binding_landscape_brief.md` — The specific low-affinity binding analysis

## Status

**Meeting happened** (March 2026, in person via Gonzales). She knows
the computational angle. Next: share the binding landscape analysis and
discuss reanalyzing existing ADDRC dose-response data.

## Next Steps

1. Share `computational_brief.md` with the ADDRC-specific binding analysis
2. Discuss access to existing dose-response data (even summary statistics)
3. Propose extended dose-response protocol (add sub-IC50 concentrations)
4. Identify pilot compound set for low-affinity validation
5. Co-develop R21 proposal (NCI or NIGMS)
