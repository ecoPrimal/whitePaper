# Thomas (TC) Chuna — Outreach & Validation Review

**Referred by**: Professor Michael Murillo (coffee, March 4, 2026)
**Purpose**: Demonstrate that all three of Chuna's published papers can be
reproduced and extended on a $600 consumer GPU — no ICER, no MILC, no vendor SDK.
Ask him to validate our results against his production runs.

---

## Context

Murillo suggested that Chuna is the person to prepare a review package for.
Chuna authored or co-authored all three papers we reproduced in hotSpring's
Chuna validation suite:

| Paper | Citation | ICER → Home |
|-------|----------|-------------|
| 43 | Bazavov & Chuna, arXiv:2101.05320 (2021) | SU(3) gradient flow with LSCFRK integrators — reproduced in Rust + WGSL |
| 44 | Chuna & Murillo, Phys. Rev. E 111, 035206 (2024) | Conservative BGK dielectric + completed Mermin — CPU + GPU |
| 45 | Haack, Murillo, Sagert & Chuna, J. Comput. Phys. (2024) | Multi-species kinetic-fluid coupling — full GPU pipeline |

**Result**: **41/41 automated validation checks pass** on consumer hardware
(RTX 4070 / Titan V, biomeGate). Zero institutional dependencies.

---

## What We're Asking

1. **Validate our physics**: Do our Rust/WGSL results match his ICER/MILC
   production numbers? We have convergence data, scale-setting results,
   dielectric function curves, and kinetic-fluid coupling profiles.

2. **Review our integrators**: We derived the LSCFRK3 coefficients from first
   principles via `const fn derive_lscfrk3(c2, c3)` — solving the four Taylor
   order conditions at compile time. This is the same math as his paper but
   done without referencing his code. Does our derivation agree?

3. **Comment on the approach**: The entire pipeline is Rust + WGSL shaders
   dispatched through Vulkan (wgpu). No CUDA, no MILC, no Fortran. Does this
   seem viable for the physics he works on?

## What We're NOT Asking

- We're not asking him to endorse ecoPrimals, constrained evolution, or the
  broader project
- We're not asking for collaboration (yet) — just independent validation
- We're not asking him to learn Rust — we provide results, not code reviews

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — outreach plan |
| `review_package.md` | Technical review package: what we achieved, how, results |
| `email_draft_chuna.md` | Draft email for first contact |

## Timeline

- **Week of March 8**: Finalize review package, overnight validation run
- **Week of March 10**: Send email (via Murillo introduction or direct)
- **Response**: Allow 1-2 weeks — he's a PhD student with his own work

## Tone

Lead with respect for his publications. He wrote the papers; we reproduced
them. Frame as: "We found your work, we reproduced it, here's what we got —
does this look right?" Not: "We did your thesis on a laptop."

The technical audience is one person who knows this physics deeply. Be
precise, cite his equations, show our numbers next to what he would expect.
