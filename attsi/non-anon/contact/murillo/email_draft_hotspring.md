# Email Drafts: hotSpring Repo to Professor Murillo

**Context**: Already had coffee, good rapport, he's returning from ignition conference. Previous emails were about neuromorphic/Akida. This is the pivot to plasma physics — sharing the hotSpring repo where we reproduced his group's work on consumer hardware. Let the repo do the talking.

---

## Option A: The Short One (recommended)

**Subject:** Sarkas on GPU — thought you'd want to see this

---

Hi Professor Murillo,

Hope the ignition conference went well! Since we talked, I've been working with Sarkas and your group's published data as part of a project I'm building.

I put together a repo that reproduces the PP Yukawa DSF study, the TTM, and the surrogate learning work from the Nature MI paper — first in the original Python, then re-executed on GPU using Rust and WGSL shaders (f64 precision, no CUDA).

The short version: 131 quantitative checks pass across all three studies. The Yukawa MD runs entirely on an RTX 4070 with 0.000% energy drift. I also found 5 silent bugs in the upstream Python code along the way.

Repo is here: https://github.com/syntheticChemistry/hotSpring

Start with `whitePaper/STUDY.md` if you want the full narrative, or `README.md` for the quick overview.

Would love to get your thoughts when you have a chance. Happy to meet up again.

Kevin
mokkevin@msu.edu

---

## Option B: The Casual One

**Subject:** Been working with Sarkas — quick update

---

Hey Professor Murillo,

Hope California was good! Quick update on what I've been up to since we grabbed coffee.

I reproduced the full DSF study (all 12 cases), the TTM, and the surrogate learning from your Nature MI paper on my workstation. Then I got the 9 PP Yukawa cases running entirely on GPU — RTX 4070, double precision WGSL shaders, no CUDA. Energy conservation is exact (0.000% drift).

Everything's documented here: https://github.com/syntheticChemistry/hotSpring

131/131 validation checks pass. Found a few upstream compatibility issues with newer NumPy/pandas versions that I documented and patched.

Let me know if you'd like to dig into any of it — happy to chat over coffee again.

Kevin

---

## Option C: The Slightly More Formal One

**Subject:** Reproduction study of Murillo Group computational physics — consumer GPU results

---

Hi Professor Murillo,

I hope the ignition conference went well. I wanted to share a project I've been working on that builds directly on your group's published work.

hotSpring is a validation study that reproduces three Murillo Group workloads — Sarkas molecular dynamics, the Two-Temperature Model, and the surrogate learning methodology from Diaw et al. (2024) — on consumer hardware (i9-12900K, RTX 4070). The study has two phases:

**Phase A (Python control):** Reproduced all published results in the original code. 86/86 quantitative checks pass. Five silent upstream bugs identified and documented (NumPy 2.x / pandas 2.x compatibility).

**Phase C (GPU molecular dynamics):** Re-executed the 9 PP Yukawa DSF cases entirely on GPU using f64 WGSL shaders (Rust + WebGPU, no CUDA). 9/9 cases pass with 0.000% energy drift. 3.7x GPU speedup at N=2000 vs CPU.

The repo is public and AGPL-3.0 licensed: https://github.com/syntheticChemistry/hotSpring

I've documented everything in `whitePaper/STUDY.md`. The physics equations are in `PHYSICS.md`. All results are reproducible from a single `cargo run` command.

I'd welcome your feedback, and I'm happy to discuss any of this in person.

Best regards,
Kevin Mok
mokkevin@msu.edu

---

## Notes for Kevin

- **Don't mention gen3, ecoPrimals, constrained evolution, or the enzyme thesis.** This email is purely about the physics reproduction. Let him engage with the science first.
- **Don't oversell the GPU speedup.** 3.7x at N=2000 is honest. The scaling argument (O(N^2) favors GPU at larger N) is in the docs if he looks.
- **The bugs are framed as compatibility issues, not criticism.** "Newer NumPy/pandas versions" is factual and neutral.
- **Code Ocean is mentioned in the repo docs but not in the email.** He'll see it if he reads STUDY.md. Let him discover it.
- **"No CUDA" is the hook for a physicist.** Every physicist knows the CUDA lock-in problem. Consumer GPU + no CUDA + f64 precision is genuinely interesting.
- **Let the repo do the heavy lifting.** 131 checks, 10 documented files, full equation reference — he can go as deep as he wants.
