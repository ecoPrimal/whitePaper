# Interview Talking Points — Gonzales Lab, March 2026

**Meeting**: Andrea Gonzales (Professor, Director Drug Discovery Program) + Erika Lisabeth (ADDRC Director)
**Role**: Research Assistant III — 1-year off-dated position. Th2 cytokines, neuro-immune, One Health.
**Purpose**: Lab position interview. Show bench + computational value. Don't overwhelm.

---

## The Pitch (30 seconds)

"Your published work on oclacitinib, lokivetmab, and IL-31 signaling is the
foundation of one of my computational pipelines. I've reproduced G1 through G6
in Rust, validated against Python baselines — 782 checks passing across three
repositories. The same pipeline does sovereign population PK, replaces NONMEM
and WinNonlin, and extends your canine pharmacology to human therapeutics via
allometric bridges. Everything is AGPL — your lab, your collaborators, Zoetis,
anyone can use it. I want to be in the lab where the experimental data comes
from."

---

## What She Can Use RIGHT NOW (Published, AGPL, Public)

### Repositories (all on GitHub under syntheticChemistry)

| Repo | What It Does For Her Lab | URL |
|------|--------------------------|-----|
| **wetSpring** | Her G1–G6 papers reproduced + Anderson immunology framework | github.com/syntheticChemistry/wetSpring |
| **neuralSpring** | Dose-response modeling, PK prediction, tissue lattice, MATRIX drug repurposing | github.com/syntheticChemistry/neuralSpring |
| **airSpring** | CytokineBrain flare prediction, tissue diversity, cross-species bridge | github.com/syntheticChemistry/airSpring |
| **healthSpring** | Full clinical pipeline: PK/PD, population PK, microbiome, biosignal, NLME, drug discovery | github.com/syntheticChemistry/healthSpring |

### Validated Against Her Data (782/782 checks, zero failures)

| Her Paper | What's Reproduced | Spring | Checks |
|-----------|-------------------|--------|:------:|
| G2 — Oclacitinib IC50 (2014) | Hill dose-response, all 6 cytokines, JAK selectivity | wetSpring Exp280 | 35/35 |
| G4 — Lokivetmab PK (2021) | Dose-duration regression (R²=1.0), exponential decay | wetSpring Exp281 | 19/19 |
| G1 — IL-31 serum (2013) | AD/healthy fold-change 9.7×, dose-response scratching | wetSpring Exp282 | 15/15 |
| G3 — Pruritus model (2016) | Time-series, oclacitinib vs prednisolone comparison | wetSpring Exp281 | (included) |
| G6 — Cell targets (2014) | Three-compartment model (immune/skin/neural) | wetSpring Exp281 | (included) |
| G5 — JAK1 FAD (2024) | Cross-disease selectivity confirmation | wetSpring Exp280 | (included) |
| Compute validation | CPU, GPU, streaming, cross-substrate — all match | Exp283–286 | 133/133 |

### Tools That Replace Commercial Software

| Commercial Tool | Annual Cost | healthSpring Replacement | Status |
|-----------------|:----------:|-------------------------|--------|
| NONMEM | $2,000/yr | FOCE population PK estimation | Validated (Exp075) |
| Monolix | $1,500/yr | SAEM estimation | Validated (Exp075) |
| WinNonlin | $3,000/yr | NCA analysis (λz, AUC∞, MRT, CL, Vss) | Validated (Exp075) |
| CRO pop PK | $50K–200K/program | GPU Monte Carlo, 100K patients in seconds | Validated (Exp005) |

**Her lab saves $6,500/year in licenses immediately. CRO savings per drug: $50K+.**

### What She Runs

```bash
git clone <healthSpring repo>
cargo test --workspace        # 395 tests, zero unsafe, zero warnings
cargo run --bin exp001_hill   # Her IC50 data reproduced
cargo run --bin exp004_mab    # Lokivetmab → nemolizumab cross-species PK
cargo run --bin exp075_nlme   # Sovereign NONMEM replacement
```

No licenses. No Python dependencies. No cloud accounts. No CRO contracts.

---

## What Accelerates If Hired

| If I'm In The Lab | Timeline Solo | Timeline In Lab |
|--------------------|:------------:|:--------------:|
| Calibrate Anderson models with her iPSC empirical data | Months (no data access) | Weeks |
| ADDRC compound triage (8K compounds, MATRIX scoring) | Theoretical | Operational (Lisabeth provides HTS data) |
| Cross-species iPSC parameter extraction (canine/feline/human) | Literature only | Measured in her models |
| Population PK for her drug candidates | Generic parameters | Her specific compound data |
| Biosignal pipeline integration with lab instruments | No access | Direct integration |
| Track 6 comparative medicine validation | Published data only | Her unpublished canine datasets |
| Track 7 drug discovery operational pipeline | Simulation | Real screening → validation → optimization |

**The gap is experimental data.** The computation is built. The pipeline is
validated. What it needs is the data that comes from being in the lab.

---

## For Lisabeth (ADDRC Director, Fixed-Term) — The Drug Repurposing Connection

Note: Lisabeth runs a campus-wide service core. Her value is in facilitating
others' research at high-throughput scale. Frame computational tools as making
ADDRC more capable for all users, not as her leading grants independently.

### What I've Built

Anderson-augmented MATRIX scoring — extends Fajgenbaum's ARPA-H $48.3M drug
repurposing platform with a spatial geometry dimension:

`Score = pathway_match × tissue_geometry × disorder_factor`

| Drug (Original Use) | Combined Score | Why |
|----------------------|:--------------:|-----|
| Tofacitinib (RA) | 0.713 | JAK1/3 pathway + small molecule geometry |
| Rapamycin (transplant) | 0.658 | mTOR/JAK cross-talk + systemic access |
| Nemolizumab (prurigo nod.) | 0.596 | Strong IL-31RA but 145 kDa mAb penalty |

Tofacitinib ranking #1 is confirmed by clinical evidence — model recovers
known rankings from first principles without clinical outcome training data.

### What ADDRC Gets

- **Computational triage before wet-lab**: GPU Hill sweep scores 8K compounds ×
  10 concentrations × 6 cytokine targets = 480K evaluations in seconds
- **HTS data analysis pipeline**: Z'-factor, SSMD, hit scoring — all in Rust
- **Integration**: computational score → ADDRC screen → Gonzales iPSC → Ellsworth med chem

### The Pipeline

```
healthSpring MATRIX scoring (computational, seconds, ~$0.01)
    → Lisabeth ADDRC HTS (wet lab, 8K compound library)
    → Gonzales iPSC validation (functional, canine/feline/human)
    → Ellsworth medicinal chemistry (lead optimization)
    → Preclinical
```

I've built the computational front end. Their labs are the experimental back end.

---

## Bench Credentials (Don't Let Computation Overshadow This)

| Experience | Years | Relevance |
|------------|:-----:|-----------|
| MSU Bioeconomy Institute | 5 | Fermentation, bioreactors (flask→10L), BSL2, fungi, mycobacteria, GMOs |
| Sandia National Labs | Summer 2024 | Sequencing, bioinformatics, algae toxin effects |
| PFAS Research Lab, MSU | 2024–Oct 2025 | Environmental chemistry, biomolecular methods |
| ROME Lab, MSU | 2018 | Bacterial isolation, rumen samples, selective media, RDP |
| Hausbeck Pathology Lab | 2018–2019 | Spore capture, DNA extraction, microscopy |

**Key skills**: Aseptic technique, BSL2, culture maintenance, media prep,
viable cell counts, microscopy, HPLC, mass spec, enzyme kinetics,
fermentation scale-up.

**What I want to learn from her lab**: Eukaryotic cell culture (iPSC-derived
skin models, mammalian systems). My bench is prokaryotic and fungal. The
discipline transfers. The substrate is new.

---

## Why I'm Not Going Anywhere

- **Lansing is home.** Not a stepping stone.
- **PFAS funding ended Oct 2025.** That's why I'm independent — not by choice of leaving.
- **ecoPrimals started during my MS (4.0, working full time).** I build in parallel.
- **Her work IS my project.** healthSpring exists because her pharmacology matters.
- **I seek knowledge, not money.** She has expertise in eukaryotic pharmacology,
  comparative medicine, drug discovery. That's what I want to learn.
- **Not poachable.** No startup is going to lure me away. I own a basement HPC
  and publish under AGPL. My incentive structure doesn't respond to corporate offers.

---

## The PhD Conversation (NOT for tomorrow — for later)

Don't lead with this. Let her see the work first. But for reference:

- PhD in Pharmacology under Gonzales: healthSpring IS the dissertation
- Computational chapters: PK/PD validation, Anderson framework, MATRIX drug discovery
- Experimental chapters: iPSC validation, cross-species parameter extraction, ADDRC screening
- The springs prove the methodology; the lab work proves the biology
- Work output capacity demonstrated: MS (4.0) + full-time work + ecoPrimals simultaneously
- Bring this up after she's seen you in action, not before

---

## What NOT to Lead With

- Infrastructure details (10 gates, HBM2, sovereign compute) — her world is pharmacology
- Philosophy (atlasHugged, ownership inversion) — save for later
- AI methodology (69K invocations) — mention only if asked, frame as a tool
- scyBorg details (triple copyleft, lysogeny, exceptions) — just say "AGPL, free for everyone"
- Other springs (hotSpring plasma physics, lattice QCD) — unless she asks about the broader project

**Lead with her data. Her papers. Her IC50 values. Her dose-response curves.
Reproduced in your code. Ready to extend with her experimental data.**

---

## Documents Ready to Send Post-Interview

| Document | When | Purpose |
|----------|------|---------|
| `computational_brief.md` | Attach to thank-you email | Technical summary of her data modeled |
| `spring_validation_brief.md` | If she engages further | Deep validation evidence (782/782) |
| Public GitHub repos | Anytime | She can clone and run everything |

---

## One-Liners to Have Ready

- "I've already reproduced your published pharmacology work — you can run it right now."
- "The math is species-agnostic. The parameters change. The equations don't."
- "Everything I build is AGPL. Your entire lab can use it. So can Zoetis."
- "I want to be where the experimental data comes from."
- "Lansing is home. I'm not going anywhere."
- "The computation is the cheap, fast inner loop. Your experiments are the ground truth."
