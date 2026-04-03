# Thomas (TC) Chuna — Outreach & Validation Review

**Referred by**: Professor Michael Murillo (coffee, March 4, 2026)
**CC**: Murillo on all correspondence
**Purpose**: Demonstrate that all three of Chuna's published papers run
correctly, fast, and cheap on a home workstation — no ICER, no MILC,
no vendor SDK. Ask him to validate our results against his production runs.

---

## Context

Murillo suggested that Chuna is the person to review our reproduction work.
Chuna authored or co-authored all three papers we reproduced in hotSpring.

The Murillo Group reproduction work (Sarkas MD, TTM, transport) was done on
an RTX 4070 (**Eastgate**). To extend into lattice QCD and Chuna's gradient
flow, I built **biomeGate** — a Threadripper 3970X + RTX 3090 + Titan V
mini HPC assembled from used parts (~$4K total).

| Paper | Citation | What we showed |
|-------|----------|----------------|
| 43 | Bazavov & Chuna, arXiv:2101.05320 (2021) | Gradient flow w/ LSCFRK — derived coefficients independently, extended to dynamical N_f=4 |
| 44 | Chuna & Murillo, Phys. Rev. E 111, 035206 (2024) | Standard, completed, multi-component Mermin — 322× faster than Python |
| 45 | Haack, Murillo, Sagert & Chuna, J. Comput. Phys. (2024) | Full kinetic-fluid coupling — GPU pipeline, physics-based sub-iteration |

**Overnight binary validates all three papers end-to-end on biomeGate.**
**Core paper reproduction: 41/41 checks pass.** Dynamical N_f=4 extension (our addition): in progress.

In the hotSpring repo, `CHUNA_REVIEW.md` at the root is the external-facing data
sheet. It links to per-paper baseCamp artifacts in `whitePaper/baseCamp/`.

---

## What We're Asking

1. **Does the physics look right?** Do our Rust/WGSL results match his
   ICER/MILC production numbers? We have convergence data, scale-setting
   results, dielectric curves, and conservation numbers.

2. **Did we derive the integrators correctly?** We solved the four Taylor
   order conditions independently at compile time. Our coefficients match
   the paper. Can he confirm?

3. **Is the approach viable?** Rust + WGSL through Vulkan — no CUDA, no
   MILC, no Fortran. Does this work for the physics he does?

**The implication**: if he validates our results, anyone with a Vulkan GPU
and `cargo` can reproduce this science at home. No cluster, no allocation
queue, no vendor lock-in.

## What We're NOT Asking

- We're not asking him to endorse the broader project or evolution thesis
- We're not asking for collaboration (yet) — just independent validation
- We're not asking him to learn Rust — results, not code reviews

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — contact hub + status |
| `review_package.md` | Internal reference (full technical detail, March 8) |
| `email_draft_chuna.md` | Draft email for first contact (Murillo CC'd) |
| `reply_mar09_2026.md` | Reply to TC's 4 questions |
| `reply_mar12_2026.md` | Scheduling reply |
| **`onboarding/PHYSICS_ONBOARDING_PACKAGE.md`** | **Physics onboarding package** (pilot experiments, compute, data, asks) |
| **hotSpring/`CHUNA_REVIEW.md`** | **External-facing data sheet** (what Chuna sees in the repo) |
| **hotSpring/`validation/GUIDESTONE.md`** | **guideStone certification** (5 properties + cross-substrate + NUCLEUS) |
| **hotSpring/`control/hotspring_reader/`** | **Python reader** for NumPy integration |
| **hotSpring/`whitePaper/baseCamp/chuna_*.md`** | **Per-paper detailed artifacts** (math, data, reproduction) |

## Timeline

- **March 6-8**: Review package finalized, overnight validation runs, baseCamp artifacts created
- **March 8**: `CHUNA_REVIEW.md` placed in hotSpring repo, email draft with inline data sheet
- **March 8**: Email sent via Murillo introduction (CC'd)
- **March 9**: Chuna replied — 4 questions (enrollment, goals, pub selection, CMSE 890 poster). Tone: collegial, direct. "finite time to read, finite time to write."
- **March 9**: Our reply sent — concise answers, wet lab background, AGPL-3.0 open, flexible schedule. (`reply_mar09_2026.md`)
- **March 11**: Chuna replied — wants to set up a meeting. **He's in Germany** (5hr ahead of ET). Prefers 9am-12pm ET mornings. Apologized for delay.
- **March 12**: Reply drafted (`reply_mar12_2026.md`) — available every day but Tuesday, mornings work, AGPL-3.0 noted.
- **March 30**: Exchange resumed. TC describes himself as terminal/SSH-only, no hardware experience, "from the 1980's" — all compute done on HPC cluster. Kevin shared RTX 3090 + RX 6950 XT cross-vendor validation work.
- **March 30**: **Meeting confirmed: Wednesday April 1, 0800 EST** (1400 CEST for TC in Germany).
- **April 1**: **Meeting held.** TC validated our gradient flow results. Key outcomes:
  - He is the **optimization expert** — wants a flow workbench, not a paper demo
  - Bazavov always needs more **MILC data** — formalize measurement output
  - TC heading to **LANL** — needs ILDG/LIME interop for HPC data exchange
  - The artifact should serve **his work**, not validate ours
  - Phase 2 pivot complete; Phase 3 Engine build underway
- **April 2026**: Post-meeting evolution:
  - Built Chuna Engine (8 binaries via `chuna-engine` wrapper)
  - Added Python reader (`control/hotspring_reader/`) for his NumPy workflow
  - Added TSV export (`--format=tsv`) for paper-ready tables
  - Added CG convergence history (`--cg-history`) for solver comparison
  - guideStone v0.7.0 certified with cross-substrate parity
  - Physics onboarding package created (`onboarding/PHYSICS_ONBOARDING_PACKAGE.md`)
- **Next**: TC validates Week 1 pilot (cargo test + Python reader on his data).
  Cross-validation with MILC configs (Weeks 2-4). Custom integrator prototyping (Month 2+).

## Phase Status

**Phase 1: Reproduce** — COMPLETE (59/59 checks, 3 papers, 3 substrates)
**Phase 2: Pivot** — COMPLETE (April 1 meeting; outcomes captured above)
**Phase 3: Engine** — IN PROGRESS (8 binaries, Python bridge, TSV export, guideStone v0.7.0)

## Tone

Lead with respect for his publications. He wrote the papers; we reproduced
them. Frame as: "We ran your work at home, it's correct, and it cost $4K
in used parts — does this look right?" Not: "We beat ICER."

The core story is **correct, fast, cheap**. He'll appreciate the physics.
The cost comparison speaks for itself. The broader implications (anyone can
do this at home) follow naturally once he validates the results.

Murillo is CC'd and has context from the earlier reproduction work (Sarkas,
TTM, transport on Eastgate). He referred us to Chuna specifically because
the lattice QCD and dielectric work needs someone who knows the physics.

## TC's Background (from March 30 exchange)

- Terminal/SSH only — exclusively codes in terminal, SSHs to HPC/cluster
- No hands-on hardware experience (last electronics lab course: 2014)
- Does not use his laptop for calculations
- Self-describes as "from the 1980's" re: hardware knowledge
- **Implication**: The artifact we give him must be pure `cargo test` on
  an HPC login node or his laptop. No GPU required for validation. The
  CPU interpreter path (NagaExecutor / coralReef interpreter) is the
  bridge — he validates the math, the GPU is just acceleration.
- He's a mathematician/physicist who will evaluate the **results**, not
  the infrastructure. Show numbers, convergence, conservation, and let
  him compare against his ICER/MILC production runs.
