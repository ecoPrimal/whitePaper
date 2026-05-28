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

## Meeting — Scheduled ~Tuesday, June 3, 2026

Reply sent (`email_reply_meeting_may2026.md`): Tuesday proposed, flexible through Thursday.

### Three Threads to Cover

| Thread | Source | Key Message |
|--------|--------|-------------|
| Compound registration / AI super user | May 23 email, pseudoSpore | pseudoSpore pattern → dose-response/screening artifacts with built-in validation |
| NF data mining | Meeting email | Pre-grant pipeline as operating model — public data, zero lab cost, validated preliminary data |
| Core science (still valid) | computational_brief, 782/782 | Anderson framework, MATRIX scoring, PTP/JAK-STAT connection |

### Questions for Andrea

1. NF project: what dataset, what foundation, what timeline/deliverables?
2. Compound registration system: what platform (or greenfield?), what data types first?
3. Where does the data/AI role sit in the hiring sequence (3rd/4th)?
4. Does Lisabeth/ADDRC connect to either thread?

---

## Next Steps

1. ✅ Send reply expressing patience + flexibility + computational contribution (email_reply_patience.md)
2. ✅ Andrea replied May 23 — RA III filled, new data management/AI role floated
3. ✅ **Reply to May 23 email** — v5 SENT (`email_reply_data_ai_role_v5.md`). Two-level AI (tool-building + lab Jarvis), ABG + PTP connection, lithoSpore concept, opportunity-not-outcome framing, AGPL licensing, around all summer.
4. ✅ **pseudoSpore follow-up** — SENT (`email_spore_followup_may2026.md`). Attached pseudoSpore as AI workflow example + artifact pattern. Shows compound registration angle directly.
5. ✅ **Meeting reply** — SENT (`email_reply_meeting_may2026.md`). Tuesday proposed, NF interest expressed, independent researcher framing.
6. **Tuesday meeting**: demonstrate how existing infra maps to compound registration + AI pattern detection + NF data mining
7. Keep Barrick position as parallel track — these are complementary, not competing
8. Paper 12 + MATRIX drug repurposing + the PTP/kinase-phosphatase work from ABG all strengthen the case
9. The ABG PTP cancer project (Mark) is isomorphic to Gonzales's work — kinase-phosphatase balance in disease. This is additional evidence of domain fluency
