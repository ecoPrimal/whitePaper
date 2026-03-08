# Email Draft: First Contact with TC Chuna

**Context**: Murillo referred us during coffee (March 4, 2026). He said
Chuna is the person who would evaluate our work. Chuna authored/co-authored
all three papers we reproduced. The repo is public. Lead with his physics,
not our infrastructure.

---

## Option A: Direct Introduction (recommended if Murillo makes the intro)

**Subject:** Reproducing your gradient flow and dielectric work — Murillo suggested I reach out

---

Hi Thomas,

I'm Kevin Mok — Professor Murillo suggested I get in touch with you. I'm
finishing my MS in Data Science at MSU and I've been building a Rust + GPU
pipeline for computational physics as a personal project.

Over the past couple weeks I've been reproducing your published work:

- **arXiv:2101.05320** (gradient flow): Implemented the full LSCFRK family
  on SU(3) lattices — W6, W7, and CK4. I derived the 3-stage 3rd-order
  coefficients from the Taylor order conditions independently (compile-time
  derivation in Rust) and they match your published values. Five integrators
  validated, convergence scaling matches the paper, and I've extended to
  dynamical N_f=4 staggered configurations (50-trajectory thermalization +
  W7 flow).

- **Phys. Rev. E 111, 035206** (dielectric): Standard Mermin, completed
  Mermin (Eq. 26 correction), and a multi-component extension for
  electron-ion plasmas. The f-sum rule, Debye screening, DSF positivity,
  and passive medium compliance all validate. GPU shader implementation
  runs at f64 precision.

- **J. Comput. Phys. (2024)** (kinetic-fluid): Three-phase validation —
  BGK relaxation with conservation laws, Sod shock tube via HLL Riemann
  solver, and the full coupled kinetic-fluid interface. The interface uses
  a sub-iteration convergence loop for density matching (not hand-tuned).
  GPU pipeline for the collision and Euler stages.

All three papers pass **41 automated validation checks** on a consumer
RTX 4070 — no ICER, no MILC, no CUDA. Pure Rust and WGSL shaders
dispatched through Vulkan. The repo is public:

  https://github.com/syntheticChemistry/hotSpring

The relevant binary is `validate_chuna_overnight`, which runs all three
papers end-to-end. The code is in `barracuda/src/`.

I'd welcome any feedback on whether the physics looks right — especially
the gradient flow convergence data and the completed Mermin dielectric.
You know this math far better than I do.

Happy to meet on campus or over Zoom if that's easier.

Kevin Mok
mokkevin@msu.edu

---

## Option B: Cold Email (if Murillo doesn't make intro)

**Subject:** Your gradient flow integrators — reproduced in Rust/GPU

---

Hi Thomas,

I'm a grad student in CMSE finishing my MS in Data Science. I've been
building a GPU physics pipeline as a personal project, and I recently
reproduced three of your papers — the LSCFRK gradient flow integrators
(arXiv:2101.05320), the conservative BGK dielectric (Phys. Rev. E 111,
035206), and the kinetic-fluid coupling (J. Comput. Phys. 2024).

Professor Murillo mentioned your name when I showed him the lattice QCD
and plasma work I've been running on consumer hardware. He thought you'd
be the right person to evaluate whether the physics is correct.

All three papers pass 41 automated checks on an RTX 4070 using Rust +
WGSL shaders (no MILC, no CUDA). I derived the LSCFRK3 coefficients
independently from the order conditions and extended the gradient flow
to dynamical N_f=4 staggered configurations.

Repo: https://github.com/syntheticChemistry/hotSpring

I'd genuinely appreciate your feedback on the results — especially
anything that looks wrong or suspicious. Happy to meet whenever works.

Kevin
mokkevin@msu.edu

---

## Notes

- **Lead with his papers, not our infrastructure**. He doesn't care about
  ecoPrimals or primal evolution. He cares about gradient flow coefficients,
  f-sum rules, and conservation laws.

- **Don't oversell**. "I reproduced your work and I'd like your feedback"
  is more effective than "I replaced ICER with a $600 GPU." He'll see the
  hardware comparison in the repo.

- **Be specific about the physics**. Mentioning Eq. 26 (completed Mermin),
  the LSCFRK derivation, and the sub-iteration coupling shows we actually
  read his papers, not just ran his code.

- **Mention the independent derivation**. The fact that we derived the
  integrator coefficients from scratch (not copied from his code or MILC)
  is the strongest credibility signal. He'll want to verify this.

- **The extension to dynamical flow is the hook**. His paper used MILC on
  ICER for this. We did it on a consumer GPU. That's the part he'll want
  to look at most closely.

- **Option A is strongly preferred** if Murillo will make the introduction.
  A cold email from a random grad student about "I reproduced your thesis
  work" could come across wrong without context.

- **Allow him time**. He's a PhD student. 1-2 weeks for a response is normal.
  One follow-up after 2 weeks is fine; more than that is pushy.

- **Don't attach PDFs or data**. Point to the repo. Let him explore at his
  own pace. The `validate_chuna_overnight` binary is the single entry point.

- **If he runs the code**: He'll need Rust (stable) and a Vulkan GPU with
  SHADER_F64. If he only has CUDA GPUs, the code still works — wgpu routes
  through the Vulkan layer on NVIDIA proprietary drivers. No additional
  setup needed.
