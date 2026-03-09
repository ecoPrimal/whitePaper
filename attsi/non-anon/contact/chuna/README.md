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
| `README.md` | This file — outreach plan |
| `review_package.md` | Internal reference (full technical detail) |
| `email_draft_chuna.md` | Draft email for first contact (Murillo CC'd) |
| **hotSpring/`CHUNA_REVIEW.md`** | **External-facing data sheet** (what Chuna sees in the repo) |
| **hotSpring/`whitePaper/baseCamp/chuna_*.md`** | **Per-paper detailed artifacts** (math, data, reproduction) |

## Timeline

- **March 6-8**: Review package finalized, overnight validation runs, baseCamp artifacts created
- **March 8**: `CHUNA_REVIEW.md` placed in hotSpring repo, email draft with inline data sheet
- **Week of March 10**: Send email via Murillo introduction (CC'd)
- **Response**: Allow 1-2 weeks — he's a PhD student with his own work

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
