# Andrea Gonzales — NF Data Mining & Drug Discovery Collaboration

**Status**: Engaged — GPS platform assigned (June 5), product composition mapped, CTF NDU aligned
**Collaborator**: Andrea J. Gonzales, PhD, Assistant Professor, Pharmacology & Toxicology, MSU
**Products**: helixVision + healthSpring + initioChem + coralForge (multi-product composition)
**Springs Fed**: wetSpring, healthSpring, neuralSpring, hotSpring
**Domain**: Drug discovery transcriptomics (GPS platform), neurofibromatosis data mining, One Health cross-species
**Funding**: CTF NF Data Utilization Award (NDU) — up to $125K total ($50K Y1 + $75K Y2)
**Date**: June 6, 2026 (updated post-meeting)

---

## The Relationship Arc

| Date | Event | Status Change |
|------|-------|---------------|
| Spring 2026 | Applied for RA III position | theory → contacted |
| March 2026 | First interview (made second round) | contacted |
| March 2026 | Sent computational_brief.md (782/782) + onboarding package | contacted |
| May 13, 2026 | Andrea update: hiring sequence, patience requested | contacted |
| May 23, 2026 | Andrea: RA III filled, new data/AI role floated, meeting invited | contacted → engaged |
| May 2026 | Reply v5 sent (AI workflow, ABG, lithoSpore) | engaged |
| May 2026 | pseudoSpore follow-up sent (artifact demo) | engaged |
| May 2026 | Andrea mentions NF data mining project | engaged |
| May 2026 | Meeting reply sent (Tuesday proposed) | engaged |
| **June 5, 2026** | **In-person meeting: GPS platform assigned, One Health discussion** | **engaged → producing** |

---

## Two Active Threads

### Thread 0: GPS Platform Rebuild — `tideGlass` (Primary Deliverable)

Andrea assigned Kevin the **GPS platform** (Bin Chen Lab, MSU) for rebuild as a pseudoSpore. This is the first concrete deliverable — not speculative, not waiting for a hire.

**Platform name**: `tideGlass` (cross-spring biological current parser)
**Org**: `protoKarya` (first project, first lens)
**Introduction**: Gonzales → Bin Chen (offered, pending)

**Source**: [zenodo.org/records/17653393](https://zenodo.org/records/17653393) — "Deep learning-based screening and design of novel therapeutics that reverse disease-associated transcriptional phenotype" — Cell (2026)

**What GPS does**: Predicts drug-induced gene expression changes from chemical structures (SMILES → expression profile), then screens for compounds that *reverse* disease transcriptomic signatures. Three modules:
- **RCL**: Robust Collaborative Learning — cleans noisy drug-induced profiles
- **GPS4Drug**: Structure → expression prediction + virtual screening
- **MolSearch**: Multi-objective lead optimization via MCTS

**Technical state**: Python 2, Fortran, pinned dependencies, 713 MB on Zenodo, web portal at `apps.octad.org/GPS/`. 10+ years of accumulated legacy code.

**pseudoSpore target**: Full lineage trace → reproduce every figure → rebuild sovereign → package with automated validation checks. Same pattern as hotSpring compChem GuideStone.

**Data dependencies (all public)**: LINCS L1000 (1.3M drug perturbation profiles), GEO disease signatures, ChEMBL/PubChem compounds.

**Connection to NF**: Screen compound libraries against NF transcriptomic signatures from the NF Data Portal. The GPS reversal scoring + Anderson tissue geometry + healthSpring MATRIX = three complementary angles on the same drug repurposing question.

### Thread 1: NF Data Mining Project

Andrea mentioned a neurofibromatosis data mining project tied to a foundation (likely CTF — Children's Tumor Foundation). This is the first multi-product composition for an external PI.

**The Biological Connection**: NF1 loss = hyperactive RAS/MAPK. Andrea studies JAK/STAT via oclacitinib. NF1 tumors have hyperactivated STAT3. Same signaling biology, different disease context.

**Product Composition**:

| Product | Role | Existing Validation |
|---------|------|-------------------|
| helixVision | Gene expression from NF Data Portal | wetSpring 6,656+ checks |
| healthSpring | MATRIX drug repurposing (MEK, JAK, mTOR inhibitors) | healthSpring 233/233 |
| initioChem | MEK inhibitor conformational dynamics | hotSpring 190/190 |
| coralForge | NF1 variant structural impact | neuralSpring 154 checks |

**Data Sources**:
- NF Data Portal / Synapse (gene expression, genomic variants, drug screening)
- Pluto.bio NF datasets (~108M data points, 12 datasets)
- PubChem / ChEMBL (compound activity for RAS/MAPK, JAK/STAT targets)
- ADDRC 8K compound library (Lisabeth access)

**Grant Alignment**: CTF NF Data Utilization Award (NDU) — up to $125K total ($50K Year 1 bioinformatics via Pluto.bio, $75K Year 2 in vitro validation). Andrea as PI, Kevin as computational infrastructure. CTF covers Pluto platform access.

**Full case study**: `gen5/products/NF_CASE_STUDY.md`

### Thread 2: Compound Registration / Data Management / AI

Andrea's May 23 email explicitly floated a "super user for compound registration and data management system" with AI-driven pattern assessment. The ecoPrimals stack maps directly:

| Ecosystem Component | Lab Equivalent |
|--------------------|---------------|
| NestGate (content-addressed storage) | Compound registry |
| rhizoCrypt (provenance DAG) | Audit trail for screening results |
| sweetGrass (attribution) | Data lineage (compound → assay → result) |
| neuralSpring ML | AI pattern detection across compound library |
| barraCuda stats | Dose-response, IC50, PK modeling |
| pseudoSpore pattern | Self-verifying data packages for every experiment |

---

## What Andrea Brings

| Contribution | Detail |
|-------------|--------|
| **Faculty PI status** | Required for CTF NDU and federal grants |
| **JAK/STAT domain expertise** | Published G1-G6 (782/782 validated), oclacitinib, lokivetmab, IL-31 |
| **ADDRC access** | 8K compound library through Lisabeth (MSU Drug Discovery Program) |
| **iPSC models** | Functional validation (canine, feline, human skin models) |
| **Wet lab capacity** | Year 2 in vitro confirmation of computational predictions |
| **NF project direction** | Foundation relationship, dataset selection, biological questions |
| **Hiring authority** | Potential data/AI role in her lab (3rd/4th hire in sequence) |

## What the Ecosystem Brings

| Contribution | Detail |
|-------------|--------|
| **Validated computation** | 782/782 on her published data, 12,510+ ecosystem-wide |
| **Multi-product composition** | helixVision + healthSpring + initioChem + coralForge |
| **GPU compute** | biomeGate (Threadripper 3970X, 256 GB RAM, Titan V ×2, MI50 ×2, RTX 5060) |
| **Self-verifying artifacts** | pseudoSpore pattern for NF preliminary data |
| **Data management infrastructure** | NestGate, rhizoCrypt, sweetGrass — compound registration pattern |
| **Zero cost to university** | All AGPL-3.0, all sovereign |
| **Pre-grant pipeline** | Computational preliminary data before a dollar is spent |

---

## New Spring Validation Targets (from Gonzales Collaboration)

Andrea's NF work will create validation targets the ecosystem has never seen:

| Result | Spring Fed | Validation Target |
|--------|-----------|-------------------|
| NF gene expression signatures | wetSpring | Differential expression in NF1 tumors |
| RAS/MAPK pathway enrichment | wetSpring | Pathway analysis on NF Data Portal data |
| NF drug repurposing MATRIX scores | healthSpring | MEK/JAK/mTOR inhibitor ranking |
| NF compound screening results | healthSpring | ADDRC HTS on NF-relevant targets |
| Neurofibromin structural variants | neuralSpring | NF1 mutation structural impact |
| MEK inhibitor binding dynamics | hotSpring | Selumetinib/trametinib FEL landscapes |

---

## New Public Data Systems (from Gonzales Collaboration)

| System | Purpose | Ingestion Status |
|--------|---------|-----------------|
| NF Data Portal / Synapse | Gene expression, genomic variants, drug screening | Not started |
| Pluto.bio NF datasets | Gene expression, pathway analysis | Not started |
| CTF Foundation datasets | Curated NF research data | Not started |
| CTF NF Challenge data | Scientific challenge benchmarks | Survey |

All cataloged in `gen5/foundations/PUBLIC_DATA_SYSTEMS.md`.

---

## Synapse Challenge Connection

The Children's Tumor Foundation sponsors NF-related computational challenges on Synapse. If Andrea's NF project aligns with an active or upcoming CTF challenge:

1. The preliminary data produced for her NDU application can also serve as a challenge submission
2. The challenge evaluation provides external domain-expert validation of the computational methods
3. The foundation sees the same tools and results from two directions — grant application and challenge submission

This is the gen5 evolution profile: challenge participation and collaborator science production reinforce each other.

---

## The gen5 Pattern

### One Health / Cross-Species (Meeting June 5)

Andrea and Kevin discussed the interconnected models problem as systems evolve toward "One Health":

- Dog skin is used as a model for human pruritus because apoquel already targets the kinase in dogs
- Animal models for humans is a tactic of the bench to overcome the lack of human subjects — not because dogs are a better model
- Better approach: examine the dog model in dogs, cat model in cats — trace **underlying causal mechanisms**
- This is the Anderson framework stated in pharmacology language: tissue geometry (d_eff) determines signal propagation, not species identity

**GPS + Anderson synthesis**: GPS tells you WHAT compound reverses the disease signature. Anderson tells you WHERE the drug signal will propagate in a given tissue geometry. Together they bypass species-extrapolation entirely — you predict species-specific drug responses from causal mechanisms.

Gonzales is the canonical gen5 collaborator: a faculty PI with a specific biological question, foundation funding, and institutional access that the ecosystem doesn't have. The cycle:

```
Andrea brings NF biological question + ADDRC access + PI authority
    → Products compose for her domain (helixVision + healthSpring + initioChem + coralForge)
    → Data ingested from NF Data Portal, PubChem, ChEMBL
    → Computational preliminary data produced (pseudoSpore for NF)
    → Andrea uses results for CTF NDU application
    → If funded: Year 1 bioinformatics → Year 2 wet lab validation
    → Results feed back as new spring validation targets
    → Ecosystem strengthens from external demand
    → Next collaborator (Barrick, Murillo, Chuna) benefits from expanded springs
```

---

## Cross-References

- `gen5/products/NF_CASE_STUDY.md` — full product composition mapping
- `gen4/thesis/THE_GEN5_TRANSITION.md` — the architectural pattern
- `attsi/non-anon/contact/gonzales/README.md` — full contact profile
- `attsi/non-anon/contact/gonzales/meeting_prep_june2026.md` — Tuesday meeting prep
- `attsi/non-anon/contact/gonzales/computational_brief.md` — Anderson framework on her data
- `attsi/non-anon/contact/gonzales/onboarding/PRE_GRANT_PIPELINE.md` — the operational model
- `gen5/foundations/PUBLIC_DATA_SYSTEMS.md` — NF data systems catalog
- `gen5/thesis/SCIENTIFIC_CHALLENGES.md` — CTF challenge alignment

---

*Andrea didn't apply to the ecosystem. She invited it to her science. The NF project isn't a demo — it's her research question answered by tools that happen to be sovereign, validated, and open. If the ecosystem can't serve her biology, the architecture is wrong. If it can, gen5 is real.*
