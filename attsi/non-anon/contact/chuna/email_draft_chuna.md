# Email Draft: First Contact with TC Chuna

**Context**: Murillo referred us during coffee (March 4, 2026). He said
Chuna is the person who would evaluate our work. Chuna authored/co-authored
all three papers we reproduced. The repo is public. Murillo will be CC'd.

Lead with his physics, not our infrastructure. The story: his work runs
correctly, fast, and cheap — on hardware anyone can buy. This is the
application of a system we built. We're asking him to verify the physics.

---

## Option A: Introduction via Murillo (recommended)

**Subject:** Reproducing your gradient flow and dielectric work — Murillo suggested I reach out

**CC:** Murillo

---

Hi Thomas,

I'm Kevin Mok — Professor Murillo suggested I get in touch with you. I
finished my MS in Data Science at MSU last May (Murillo's CMSE 890 was
my last semester). Before that I did a BS in Microbiology here, and I
spent five years in a bench lab at the Bioeconomy Institute. I've been
building a computational physics pipeline in Rust in my basement since
graduation — consumer GPUs, no cloud, no cluster.

I reproduced all three of your published papers on a home workstation
I built from used parts. Here's what I got:

**Paper 43 — Gradient Flow (arXiv:2101.05320)**

| | Result |
|--|--------|
| Integrators | W6, W7, CK4 — LSCFRK3 coefficients derived from first principles (compile-time Rust, not copied) |
| Convergence | ε = 0.02 → 0.001, measured orders 2.06/2.08/2.11 on 8⁴ (finite-size suppressed) |
| Plaquette | β=6.0 ⟨P⟩ = 0.5929 (literature ~0.594) |
| GPU speedup | **38.5×** (RTX 3090 vs single-core CPU, 8⁴ W7 flow) |
| Extension | Dynamical N_f=4 staggered flow (adaptive Omelyan HMC) — in progress |

**Paper 44 — Conservative BGK Dielectric (Phys. Rev. E 111, 035206)**

| | Result |
|--|--------|
| Scope | Standard, completed (Eq. 26), multi-component Mermin (electron-ion) |
| Debye screening | Exact to 1e-12 |
| DSF positivity | ≥99% (completed Mermin) |
| f-sum rule | Converging to −πωₚ²/2 |
| GPU-CPU parity | L² = 5.5e-7 |
| DSF vs MD | Completed Mermin within 0.8% of MD peak (Murillo Group plasma DB, κ=2 Γ=31) |
| Speedup | **322× Rust over Python**, same algorithm |

**Paper 45 — Kinetic-Fluid Coupling (J. Comput. Phys. 2024)**

| | Result |
|--|--------|
| Scope | BGK relaxation + Euler/HLL + coupled interface (3-iteration sub-iteration) |
| BGK mass conservation | Exact (Δm = 0) |
| Euler mass conservation | 1.4e-15 |
| H-theorem | Entropy monotonically non-decreasing |
| Interface | Physics-based convergence, not hand-tuned |

**Hardware & Cost**

| | ICER | My basement |
|--|------|-------------|
| Hardware | HPC cluster | RTX 3090 + Titan V, Threadripper 3970X, ~$4K used parts |
| Full validation (3 papers) | Batch queue | ~5 hours, single binary, ~$0.10 electricity |
| Software | MILC (C) + Python + Fortran + CUDA | Rust + WGSL (`cargo build`), Vulkan — no vendor SDK |

Everything is in two public repos — the validation application and the
compute engine:

  https://github.com/syntheticChemistry/hotSpring  (validation)
  https://github.com/ecoPrimals/barraCuda          (compute engine — pulled automatically)

To run it:

```
cd hotSpring/barracuda
cargo run --release --bin validate_chuna_overnight
```

The review document is `CHUNA_REVIEW.md` at the repo root — it has all
the numbers above plus links to detailed per-paper artifacts in
`whitePaper/baseCamp/` (full math, equations, data provenance, source
file listings, reproduction instructions).

I'd welcome your feedback on whether the physics looks right. You and
Professor Bazavov know this math far better than I do. If the results
check out, it means anyone with a Vulkan GPU and `cargo` can reproduce
this science at home.

Happy to meet on campus or over Zoom whenever works.

Kevin Mok
mokkevin@msu.edu

---

## Option B: Cold Email (fallback if Murillo doesn't make intro directly)

**Subject:** Your gradient flow integrators — reproduced on a home GPU

**CC:** Murillo

---

Hi Thomas,

I'm Kevin Mok — I finished my MS in Data Science at MSU last May
(Professor Murillo's CMSE 890 was my last semester). I've been building
a Rust + GPU pipeline for computational physics in my basement since
graduation.

I reproduced three of your papers — the LSCFRK gradient flow integrators
(arXiv:2101.05320), the conservative BGK dielectric (Phys. Rev. E 111,
035206), and the kinetic-fluid coupling (J. Comput. Phys. 2024) — on
a home workstation (RTX 3090 + Titan V, Threadripper 3970X, ~$4K in
used parts). Murillo's name came up because I'd already reproduced his
group's Sarkas MD and transport work — he said you're the person to
evaluate the gradient flow and dielectric results.

Quick numbers: 38.5× GPU speedup on gradient flow, 322× Rust over
Python on the kinetic-fluid coupling, Debye screening exact to 1e-12,
completed Mermin DSF within 0.8% of MD. The LSCFRK3 coefficients were
derived independently from the order conditions — not copied from MILC
or the paper.

Repo: https://github.com/syntheticChemistry/hotSpring
Engine: https://github.com/ecoPrimals/barraCuda (pulled automatically by cargo)
Review: `CHUNA_REVIEW.md` at the repo root (data sheet + links to
per-paper baseCamp artifacts with full math and reproduction steps)

I'd genuinely appreciate your feedback — especially anything that looks
wrong or suspicious. If it passes your review, anyone with a GPU can
do this science at home. No cluster, no vendor SDK, ~$0.10 per run.

Happy to meet whenever works.

Kevin
mokkevin@msu.edu

---

## Notes

- **Murillo is CC'd**. He gave us the referral. Having him on the thread
  adds credibility and context. He's seen the earlier Murillo Group
  reproduction work (Sarkas, TTM, transport — on the RTX 4070).

- **Bazavov is co-author on Paper 43**. Mentioning him by name shows
  we know the faculty network and adds weight — he's MSU CMSE faculty.

- **"I finished my MS"** — degree was awarded May 2, 2025 (3.916 GPA).
  This is post-graduation independent work, not a class project.

- **Lead with his papers, not the infrastructure**. He cares about
  gradient flow coefficients, f-sum rules, and conservation laws — not
  about Rust vs C or our internal architecture.

- **The inline data sheet is the pitch**. He can scan the tables in
  30 seconds and know whether this is worth his time. Everything else
  is in baseCamp if he wants to dig.

- **The independent derivation is the strongest signal**. We derived the
  integrator coefficients from scratch — compile-time Rust, solvable order
  conditions. He'll want to verify this.

- **The dynamical flow extension is the hook**. His paper is primarily
  quenched + MILC for dynamical. We did dynamical on a home GPU. That's
  the part he'll look at most closely.

- **The cost story speaks for itself**. Don't oversell "I replaced ICER."
  Just state the hardware, the price, and the electricity cost. He'll
  draw the conclusion.

- **DF64 is in CHUNA_REVIEW.md** as an additional precision tier. Don't
  lead with it in the email — it's a technical detail he'll discover if
  he digs in. The email should be about his physics, not our precision
  architecture.

- **Option A is strongly preferred** since Murillo is making the
  introduction and will be CC'd.

- **Allow him time**. He's a PhD student. 1-2 weeks for a response is
  normal. One follow-up after 2 weeks is fine; more than that is pushy.

- **Don't attach PDFs or data**. Point to the repo. Let him explore at
  his own pace. `validate_chuna_overnight` is the single entry point.
  `CHUNA_REVIEW.md` is the data sheet. `whitePaper/baseCamp/chuna_*.md`
  is where he digs.

- **If he runs the code**: Rust (stable) + a Vulkan GPU with SHADER_F64.
  On NVIDIA, the proprietary driver's Vulkan layer works. No extra setup.
