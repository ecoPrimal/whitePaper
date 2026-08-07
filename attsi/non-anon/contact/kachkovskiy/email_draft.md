# Email: First Contact with Ilya Kachkovskiy — SENT

**Context**: Bought a NucBox M6 from him on Facebook Marketplace. Brief
conversation about GPUs. He has an RTX 5080. He noticed equations on his
whiteboard. The connection is personal but thin — warm it with a specific,
concrete offering.

---

## Option A: In-Person (Wells Hall — preferred)

Stop by C300 Wells Hall during office hours. Bring a laptop with the
Hofstadter butterfly visualization or Anderson 3D output. The conversation:

"Hey — I'm Kevin, I bought the NucBox from you last year. I've been
running Anderson localization and Hofstadter butterflies on consumer GPUs
as part of a personal project. Your Bourgain paper is one of the things
I validated. Wanted to show you what it looks like — 3D mobility edge,
Lanczos eigenvalues, the whole butterfly, all on a $600 GPU. No CUDA."

If he's interested, hand him the repo URL and let him explore. If he has
5 minutes, show the butterfly rendering on screen. If he has 20 minutes,
walk through the Herman formula verification.

---

## Option B: Email

**Subject:** Anderson localization on consumer GPU — you sold me a NucBox

---

Hi Professor Kachkovskiy,

I'm Kevin Mok — you sold me a NucBox M6 on Marketplace a while back. I'm
finishing up in CMSE (MS Data Science, May 2025) and I've been building a
GPU pipeline for scientific computing as a personal project.

I've been implementing spectral theory on consumer GPUs — Anderson
localization (1D/2D/3D), the Almost-Mathieu operator, Hofstadter butterfly,
and Lanczos eigensolves. Your co-authored paper with Bourgain (GAFA 2018)
on two-particle quasiperiodic localization is one of the things I
validated, along with the foundational papers in the field (Anderson 1958,
Jitomirskaya 1999, Herman 1983, Aubry-André, Slevin-Ohtsuki).

Some results:
- 3D Anderson mobility edge at W_c = 16.26 ± 0.95 (matches Slevin-Ohtsuki)
- Herman formula γ = ln|λ| verified to 4 decimal places
- GPU Lanczos eigenvalues agree with CPU to 10⁻¹⁵ (machine precision)
- N=10,648 sites (22³ Anderson 3D): GPU Lanczos 8ms vs CPU 64ms (8.4× speedup)
- Full Hofstadter butterfly in ~3 seconds on RTX 3090
- Scaling: GPU advantage grows with N — ready for your L² Hilbert spaces

Everything is Rust + WGSL shaders — no CUDA, no LAPACK, no Python. Runs
on any Vulkan GPU. Repo is public:

  https://github.com/syntheticChemistry/hotSpring

The spectral validation binaries are `validate_spectral`,
`validate_anderson_3d`, `validate_hofstadter`, and `validate_gpu_lanczos`.

I know you have a 5080 — these tools would run well on it. The two-particle
Hilbert space from the Bourgain paper (L² dimension) is the natural GPU
target. Happy to walk through any of it if you're curious.

Kevin Mok
mokkevin@msu.edu

---

## Notes

- **NucBox reference is the hook.** It's memorable, personal, and establishes
  he's a real person Kachkovskiy has met, not a cold emailer.
- **Lead with his Bourgain paper.** That's his most computationally intensive
  work and the one where GPU matters most.
- **Show numbers.** W_c = 16.26, γ = ln|λ| to 4 decimals, 1e-15 Lanczos
  parity — these are things he can evaluate instantly.
- **5080 mention is the value proposition.** He bought a 5080 for a reason.
  We're offering to make it useful for his research without CUDA.
- **Don't mention biology.** He's a pure mathematician. Anderson localization
  in gut microbiomes is our application, not his interest. If he asks, great.
- **In-person is strongly preferred.** He's on campus. A 5-minute hallway
  demo of the Hofstadter butterfly is worth more than any email.
- **The two-particle pitch.** His Bourgain paper is the computationally hardest
  thing in his portfolio. L² Hilbert space at L=200 is 40,000×40,000 — doable
  on a 5080 with GPU Lanczos, impossible in Python/SciPy in reasonable time.
  This is where GPU spectral computing actually changes what he can compute.
- **Fresh data (Aug 7, 2026).** bench_lanczos_scaling now validates up to
  N=10,648. The 8.4× speedup at this size is conservative — with more Lanczos
  iterations (k=200+) or larger N, the GPU advantage will grow because SpMV
  dominates and GPU parallelism scales. His two-particle problem at L=200
  (N=40,000) should see 20-40× GPU advantage.
