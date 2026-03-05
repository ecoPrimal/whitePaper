# Email: Post-Coffee Follow-Up (March 4, 2026)

**Context**: Second coffee meeting, Tuesday March 4. He asked two sharp questions:
(1) How does hotSpring/BarraCuda handle Ewald summation for long-range interactions?
(2) Have we looked at Kokkos from Sandia for performance portability?
Both are exactly the questions a serious computational physicist should ask.
The repo is already shared. Previous emails covered quenched QCD (Feb 27)
and dynamical QCD progress (Feb 28).

---

## Email (DRAFT — send tonight or tomorrow morning)

**Subject:** Re: Following up — Ewald and Kokkos

---

Hi Professor Murillo,

Thanks again for coffee today — those were exactly the right questions to ask, and I want to give you proper answers.

**Ewald / PPPM:**

We have a full PPPM implementation in BarraCuda. The standard Ewald splitting — erfc-damped short-range in real space, FFT-based k-space solve for the long-range part — with B-spline charge spreading (order 4–7), precomputed Green's function with influence correction, and gradient-based force interpolation back to particles. Self-energy and dipole corrections included.

The entire pipeline is in WGSL shaders — `charge_spread_f64.wgsl`, `greens_apply.wgsl`, `force_interpolation_f64.wgsl`, `erfc_forces.wgsl`, `bspline_f64.wgsl` — so it runs on any Vulkan GPU without a vendor SDK. The Sarkas DSF Yukawa cases you published already run through the PPPM path. References are Essmann et al. JCP 103 (1995) for the smooth PME algorithm and Deserno & Holm JCP 109 (1998) for accuracy analysis. Accuracy presets go from 1e-3 to 1e-7 relative force error.

The GPU PPPM orchestration (charge spread → forward FFT → Green's multiply → inverse FFT → force interpolation → short-range correction) is fully pipelined. The 3D FFT uses our own WGSL implementation rather than cuFFT, which is the main reason it's vendor-agnostic.

**Kokkos:**

Honestly, I hadn't studied Kokkos in depth before you mentioned it — and I should have. It's the most serious prior art for what we're doing on the portability side.

The fundamental architectural difference: Kokkos provides C++ template abstractions (`parallel_for`, `parallel_reduce`, `parallel_scan`) that get compiled against a specific backend — CUDA, HIP, SYCL, OpenMP. The user code is portable, but you still need the vendor SDK installed at compile time (CUDA toolkit for NVIDIA, ROCm for AMD, oneAPI for Intel). Our approach writes the compute kernels directly in WGSL and dispatches through WebGPU/Vulkan at runtime. The only requirement is a Vulkan driver — no SDK, no toolkit, no compile-time backend selection.

The tradeoff is clear: Kokkos has a decade of production use in DOE codes (LAMMPS, Trilinos, ExaWind), established optimizations for specific hardware, and a large community. We have architectural sovereignty and the ability to run the same binary on any vendor's GPU without recompilation. For the MD workloads specifically, Cabana (the particle library built on Kokkos) would be the closest comparison point.

What I'd like to do is add Kokkos/Cabana as a validation baseline alongside Python — reproduce a subset of the same physics using Kokkos, measure performance, and use that as the competitive benchmark for our WGSL pipeline. Python validates correctness; Kokkos validates that we're competitive with production HPC tooling. That feels like the honest way to evaluate the approach rather than only comparing against Python.

I'll read the Edwards et al. JPDC 2014 paper and the Trott et al. CiSE 2022 update this week. If there are specific Kokkos patterns or benchmarks you think would be most informative, I'd welcome the pointer.

Thanks for pushing on this — these are the questions that make the work better.

Kevin
mokkevin@msu.edu

---

## Notes

- Don't mention ecoPrimals, constrained evolution, or the broader project architecture
- Honest about not having studied Kokkos — he'll respect that more than pretending
- Frame Kokkos as a validation target, not a competitor — this is the correct framing
- The PPPM answer is strong and factual — he can verify all of this in the repo
- Mentioning Cabana shows we understand the specific comparison point for MD
- Asking for his pointers keeps the conversation open and shows respect for his domain knowledge
- The "Python validates correctness, Kokkos validates competitiveness" framing is the key insight
