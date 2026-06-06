# Andrea Gonzales — Contact Notes

**Name**: Andrea J. Gonzales, PhD
**Title**: Assistant Professor
**Department**: Pharmacology & Toxicology, MSU
**Position Applied**: Research Assistant III (posting r3.md)
**Focus**: Atopic dermatitis, Th2 cytokines (IL-4/IL-13/IL-31), neuro-immune interactions, One Health, iPSC models

---

## Interview Timeline

- **Applied**: Spring 2026 (posting closed ~April 15, 2026)
- **First interview**: Completed (made second round)
- **Second round status**: On hold as of May 13, 2026
- **RA III position**: Filled — went to drug screening researcher (May 23, 2026)
- **New lead**: Compound registration / data management / AI super user (May 23, 2026)

---

## Latest Communication — May 23, 2026

Andrea emailed directly with update + new opportunity:

1. **RA III position filled** — offered to a researcher with drug screening experience for sponsored research grant
2. **Still hiring** — additional positions coming once new hires are running
3. **New role floated**: "super user for compound registration and data management system" that will:
   - House all drug discovery program data
   - Allow AI-driven pattern assessment across compounds
4. **Explicitly asked if Kevin is interested** in this role
5. **Invited a meeting**: "Feel free to set up some time if you'd still like to keep discussions going"
6. Tone: warm, proactive, offering something specific

### What This Means

- The RA III (bench screener) went to someone with direct screening experience — expected
- She's now offering something that may be a **better fit** for Kevin's actual skillset
- "Compound registration and data management system + AI tools" is exactly:
  - Data infrastructure (ecoPrimals pattern)
  - Scientific data management (structured compound/assay data)
  - ML/AI pattern recognition (neuralSpring, barraCuda)
  - Drug discovery pipeline integration (Fajgenbaum MATRIX, ADDRC screening)
- She's inviting continued conversation — this is not a soft close, it's an active lead
- The role is likely **3rd or 4th hire** in her sequence (after antibody engineer + screener)

### Strategic Assessment

**This role maps directly to what Kevin already builds.** The ecoPrimals ecosystem IS a compound registration and data management system with AI pattern assessment — just for a different domain. The translation:

| ecoPrimals concept | Gonzales lab equivalent |
|---|---|
| NestGate (content-addressed storage) | Compound registry (structured chemical/assay data) |
| rhizoCrypt (provenance DAG) | Audit trail for screening results |
| sweetGrass (attribution) | Data lineage (which compound, which assay, which result) |
| neuralSpring ML | AI pattern detection across compound library |
| barraCuda stats | Dose-response, IC50, PK modeling |
| healthSpring validation | Drug discovery pipeline validation |
| lab.primals.eco | Data access surface for lab members |

---

## Previous Communication — May 13, 2026

Andrea provided a detailed update:

1. **First hire (antibody engineer)** — offer given, filled
2. **Second hire** — deciding between a **screener for an animal health company** vs **her own research position**
   - Meeting with the animal health company May 14 to understand their timeline
   - The company screener may need to come before her own research hire to attract funding
3. **Total positions**: Plans to post for **4 positions** before end of 2026
4. **Kevin's interest** (her own research) may be **3rd in hiring order** due to funding strategy
5. Tone: appreciative, transparent, asking for patience

---

## Connection to Our Work

See detailed notes in:
- `focus/research_notes_r3.md` — lab background, drug discovery pipeline, MSU ADDRC
- `focus/literature_review_r3.md` — Th2 cytokines, AD, neuro-immune, One Health
- `CV/research_assistant_iii_*` — tailored resume and cover letter
- baseCamp Paper 12 (immunological Anderson) — directly targets her research

---

## Strategy Shift — From Applicant to Meta-Colleague

Rather than waiting passively, position as an active collaborator whose work is already supporting her domain:

### What We Offer Now (No Hire Required)
1. **baseCamp Paper 12** — Anderson localization applied to her published IL-31/oclacitinib data (G1-G6). Validated: wetSpring Exp273-286 (359/359), neuralSpring nS-601-605 (329/329). This is citable work that extends her research computationally.
2. **Fajgenbaum MATRIX bridge** — geometry-aware drug repurposing scoring. Adds spatial dimension to pathway-based drug-disease matching. Directly relevant to ADDRC screening pipeline.
3. **Compute access** — lab.primals.eco for her lab or ADDRC collaborators. JupyterHub, no install, remote.
4. **Pre-grant pipeline** — computational validation that supports future grant applications (R01, R21, ARPA-H). Anderson-augmented MATRIX scores → ADDRC HTS (8,000+ compounds) → iPSC validation.

### Public & Citable Resources
- **primals.eco** — research papers and validated pipelines (175+ papers reproduced)
- **lab.primals.eco** — live computational environment (browsable, no login)
- **github.com/sporeGarden/projectNUCLEUS** — open source infrastructure
- **github.com/syntheticChemistry/wetSpring** — the genomics/biology spring (Paper 12 lives here)
- **github.com/syntheticChemistry/neuralSpring** — ML pipelines (Hill dose-response, PK, ESN regime classification)

### Key Message in Reply
- Patient and flexible on role — animal health screener, her own research, or anything she sees fit
- Already building computational tools that directly touch her science
- Work is public, citable, and available for collaboration without a hire
- Open to direction — "point me somewhere useful"

---

## NF Data Mining Project — gen5 Proof Case

Andrea floated a **neurofibromatosis (NF) patient data mining project** tied to a foundation (likely Children's Tumor Foundation). This is the first multi-product composition for an external PI — the gen5 proof case.

### The Biological Connection

NF1 = loss of neurofibromin = hyperactive RAS/MAPK. Andrea already studies JAK/STAT via oclacitinib (782/782 checks). NF1 tumors exhibit hyperactivated STAT3. This is the same signaling biology extended to a rare disease — not a domain shift.

### Product Composition

| Product | Role in NF Project |
|---------|-------------------|
| **helixVision** | Gene expression mining from NF Data Portal (Synapse) |
| **healthSpring** | MATRIX drug repurposing scoring (MEK, JAK, mTOR inhibitors) |
| **initioChem** | Conformational dynamics of MEK inhibitor binding |
| **coralForge** | NF1 variant structural impact prediction |

### Grant Alignment

- **Children's Tumor Foundation NF Data Utilization Award (NDU)**: up to $125K total ($50K Y1 + $75K Y2), 10% indirect cap
  - Year 1 (up to $50K): Bioinformatics analysis via Pluto.bio (computational preliminary data). CTF covers Pluto platform access.
  - Year 2 (up to $75K): In vitro validation (iPSC, ADDRC screening)
- Andrea = PI, Kevin = computational infrastructure

### Data Sources

- NF Data Portal / Synapse (gene expression, genomic variants, drug screening)
- Pluto.bio NF datasets (~108M data points, 12 datasets)
- PubChem / ChEMBL (compound activity for RAS/MAPK, JAK/STAT targets)
- ADDRC 8K compound library (Lisabeth access)

### Ecosystem Documentation

- `gen5/products/NF_CASE_STUDY.md` — full product composition mapping
- `gen5/collaborators/GONZALES_NF.md` — collaborator status tracking
- `gen4/thesis/THE_GEN5_TRANSITION.md` — the architectural pattern this instantiates

---

## Meeting — June 5, 2026 (In-Person, Her Office)

### Outcome

Andrea gave Kevin a concrete task: rebuild the **GPS platform** (Bin Chen Lab, MSU) as a pseudoSpore. This is a deep learning drug discovery platform that predicts gene expression changes from chemical structures and screens compounds that reverse disease-associated transcriptomic signatures.

**Paper**: [zenodo.org/records/17653393](https://zenodo.org/records/17653393) — "Deep learning-based screening and design of novel therapeutics that reverse disease-associated transcriptional phenotype" (Bin Chen Lab, MSU)

**The platform (GPS)** has three components:
1. **RCL** — Robust Collaborative Learning to improve drug-induced gene expression profile quality
2. **GPS4Drug** — Predict drug-induced gene expression from chemical structures, run drug screening
3. **MolSearch** — Multi-objective compound optimization (Monte Carlo Tree Search)

**Technical reality**: 10+ years of accumulated code — Python 2, Fortran, pinned dependencies. Web portal at `apps.octad.org/GPS/`. Total artifact ~713 MB on Zenodo. This is exactly the kind of legacy scientific code that the pseudoSpore/guideStone pattern is built to resolve.

**The plan**: Go through the lineage of the paper, rebuild entirely so it is transmissible as a pseudoSpore. Sovereign, validated, reproducible — not pinned to dead Python 2 environments.

### One Health / Cross-Species Discussion

The meeting led to substantive conversation about interconnected models as systems evolve toward "One Health":

- **Dog skin as model for human pruritus** — dog skin already has apoquel (oclacitinib) targeting the kinase. Normally we use animal models for human diseases, but this leaves massive gaps and bad assumptions.
- **Kevin's position** (aligns with Anderson framework): Rather than applying animal models to humans, examine the dog model in dogs and the cat model in cats. This allows tracing of underlying **causal mechanisms** rather than forcing cross-species extrapolation.
- **The insight**: Animal models for humans is a tactic of the bench to overcome the lack of humans to experiment on — not because dogs are a better model. The computation can expose where the models diverge and WHY (geometry, tissue architecture, receptor distribution — Anderson's `d_eff`).

This directly validates the `CROSS_SPECIES_CAUSAL_MODEL.md` in the onboarding package. Andrea is thinking about the same problems the Anderson framework addresses.

### What This Changes

| Before meeting | After meeting |
|----------------|---------------|
| Waiting for a role to develop | Actively working on a deliverable she assigned |
| NF data mining was speculative | GPS platform rebuild is concrete, scoped, demonstrable |
| Cross-species was a theoretical pitch | She's thinking about One Health problems and agrees with the approach |
| "I can help" | "She asked me to help" |

### Active Threads (Post-Meeting)

1. **GPS Platform Rebuild** — pseudoSpore target. Go through paper lineage, reproduce, rebuild sovereign. Primary deliverable.
2. **NF Data Mining** — still alive, tied to CTF NDU. GPS platform connects (screen compounds against NF transcriptomic signatures).
3. **One Health / Cross-Species** — Anderson framework maps directly. Not a separate project — it's the causal engine underlying both the GPS work and the NF work.

---

## Next Steps

1. ✅ Send reply expressing patience + flexibility + computational contribution (email_reply_patience.md)
2. ✅ Andrea replied May 23 — RA III filled, new data management/AI role floated
3. ✅ **Reply to May 23 email** — v5 SENT (`email_reply_data_ai_role_v5.md`).
4. ✅ **pseudoSpore follow-up** — SENT (`email_spore_followup_may2026.md`).
5. ✅ **Meeting reply** — SENT (`email_reply_meeting_may2026.md`).
6. ✅ **June 5 meeting** — GPS paper assigned, One Health discussion, NF confirmed.
7. **NOW**: Begin GPS platform analysis — paper lineage, dependency audit, reproduction plan.
8. **THEN**: Package as pseudoSpore — sovereign, validated, Python 2/Fortran → Rust/modern Python.
9. **PARALLEL**: NF data mining using GPS as the screening engine against NF transcriptomic signatures.
10. Keep Barrick position as parallel track — these are complementary, not competing
