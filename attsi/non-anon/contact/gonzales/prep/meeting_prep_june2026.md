# Meeting Prep — Gonzales Lab, ~Tuesday June 3, 2026

**Format**: In-person or call (her office, per her invitation)
**Context**: Post-RA III, post-pseudoSpore follow-up. Three active threads.

---

## The Three Threads

### Thread 1: NF Data Mining Project

Andrea mentioned a neurofibromatosis data mining project tied to a foundation. This is the highest-leverage thread — it maps directly to the pre-grant pipeline and is the first multi-product composition for an external PI.

**What to learn:**
- What foundation? (Likely CTF — Children's Tumor Foundation)
- What dataset? (NF Data Portal / Synapse? Pluto.bio? Internal?)
- What deliverables does the foundation expect?
- What timeline? (NDU is typically 2-year awards)
- What biological questions? (Tumor subtyping? Drug targets? Biomarkers?)
- Is this her project or inherited/shared?

**What to offer:**
- The pre-grant pipeline in action — public NF data, open tools, validated computational results before a dollar is spent
- The pseudoSpore pattern applied to NF: self-verifying data packages for foundation applications
- GPU compute (biomeGate) for gene expression analysis and drug repurposing scoring
- Existing validated base: 782/782 on her published JAK/STAT work, same signaling biology

**What NOT to lead with:**
- Product names (helixVision, initioChem) — speak in terms of what they do
- Infrastructure details (primals, deploy graphs, PrimalBridge)
- The gen5 framing — that's internal architecture language

**How to frame it:**
"I've been building validated computational pipelines for drug discovery — the same ones that reproduced your oclacitinib data. NF1 is RAS/MAPK, which cross-talks with the JAK/STAT biology I've been modeling from your papers. If the foundation wants gene expression mining, drug repurposing candidates, or structural analysis, I can produce that computationally before the lab spends a dollar — and the output self-validates."

### Thread 2: Compound Registration / Data Management / AI

Andrea's May 23 email explicitly asked about a "super user for compound registration and data management system" with AI-driven pattern assessment.

**What to learn:**
- Is this a specific software platform (or greenfield)?
- What data types come first? (Compound metadata, screening results, PK data?)
- Who would Kevin interact with? (Lisabeth/ADDRC, other lab members, IT?)
- Is this a funded position or still conceptual?
- Timeline for this role vs. other hires?

**What to offer:**
- The pseudoSpore pattern IS compound registration: structured data + provenance + automated validation
- AI-accelerated bookkeeping: metadata extraction, cross-checking, quality assurance — as demonstrated by the attached artifact
- The existing ecosystem already handles the data management patterns her lab needs (content-addressed storage, provenance DAGs, attribution chains)

**How to frame it:**
"The artifact I sent you is essentially what compound registration looks like when you build it right — every data field is pipeline-derived, not hand-authored, and the whole thing validates itself. The same pattern handles dose-response curves, screening results, compound metadata. AI does the bookkeeping; the human stays on the science."

### Thread 3: Core Science (Background — Don't Lead)

The 782/782 validation, Anderson framework, MATRIX scoring, and PTP/JAK-STAT connection remain the foundation of credibility. Don't present this as a pitch — let it emerge naturally if she asks about the computational work.

**If she asks "how does the modeling work?":**
- Point to G2 oclacitinib IC50 (Hill dose-response, 6 pathways, all reproduced)
- Point to G4 lokivetmab PK (dose-duration regression, R²=1.0)
- MATRIX scoring: `pathway_match × tissue_geometry × disorder_factor` — tofacitinib ranks #1, confirmed by clinical evidence
- "Everything is published and AGPL. Your lab can run it right now."

---

## What to Bring

### On Laptop (ready to show, not present unprompted)

1. **pseudoSpore contents** — `scope.toml`, a few figures, the `validate` output
2. **computational_brief.md** — the Anderson framework applied to G1-G6
3. **lab.primals.eco** — live notebooks (if WiFi available)
4. **GitHub repos** — syntheticChemistry/wetSpring, healthSpring

### Physical

- Nothing. This is a conversation, not a presentation. Let her drive.

### Mental Model

Kevin is an independent researcher who got interested in her science because it's genuinely good biology, built validated tools around it, and now sees the NF project as a natural extension of work he's already doing. He wants to be in the lab long-term but is not contingent on a hire. The tools exist either way. Her expertise shapes where they point.

---

## Tone Calibration

| Do | Don't |
|----|-------|
| Let her talk about NF first — learn before you pitch | Don't walk in with a slide deck |
| Ask specific biological questions about NF | Don't talk about primals, springs, or gen5 |
| Frame computation as serving her science | Don't frame her science as validating your tools |
| Show the pseudoSpore only if she asks to see an example | Don't demo anything unsolicited |
| Express genuine interest in the NF biology | Don't treat this as a job interview |
| Mention you're available all summer | Don't pressure on hiring timeline |
| Reference the pre-grant pipeline concept | Don't use the phrase "pre-grant pipeline" |

---

## Key One-Liners

- "NF1 and JAK/STAT aren't separate problems — your oclacitinib work already models the signaling cross-talk that matters in NF tumors."
- "I can produce validated gene expression analysis and drug repurposing candidates computationally before the lab spends a dollar."
- "The artifact I sent you is what that output looks like — it validates itself. Same pattern works for compound registration data."
- "I'm building this regardless. Your input on where the biological questions are makes the tools better."
- "What does the foundation want to see in the preliminary data?"

---

## Possible Outcomes

| Outcome | Next Step |
|---------|-----------|
| She confirms NF project details and wants computational support | Begin NF Data Portal data ingestion, draft CTF NDU outline |
| She's more interested in compound registration role | Map pseudoSpore pattern to her specific data management needs |
| Both threads advance | Parallel track: NF preliminary data + compound registration prototype |
| She's noncommittal | Leave door open, continue building independently, follow up with a concrete NF result |
| She has a different project entirely | Adapt — the ecosystem is domain-agnostic |

---

## Timeline Context

- Andrea is building a lab from scratch — she needs wins, not complexity
- The compound registration hire is likely 3rd or 4th in sequence
- NF project may have a shorter timeline if foundation has a deadline
- Kevin is available all summer with no competing commitments
- ABG and Barrick tracks are parallel, not competing

---

## Cross-References

- `../correspondence/email_reply_meeting_may2026.md` — the reply that set up this meeting
- `../correspondence/email_spore_followup_may2026.md` — the pseudoSpore she's already received
- `../correspondence/email_reply_data_ai_role_v5.md` — the v5 reply already sent (two-level AI, ABG, lithoSpore)
- `computational_brief.md` — Anderson framework technical summary
- `interview_talking_points_mar2026.md` — March interview prep (still valid for background)
- `onboarding/PRE_GRANT_PIPELINE.md` — the operational model for NF
- `onboarding/LAB_ONBOARDING_PACKAGE.md` — full lab integration plan
- `gen5/products/NF_CASE_STUDY.md` — internal product composition mapping (don't share)
