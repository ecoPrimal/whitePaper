# Thomas (TC) Chuna — Profile

**Role**: PhD Student, Physics & Computational Mathematics, Science & Engineering (CMSE), MSU
**Lab**: Murillo Group — https://murillogroupmsu.com/thomas-chuna/
**Referred by**: Professor Michael Murillo (coffee, March 4, 2026)
**Purpose**: Murillo suggested Chuna is the person to prepare a review package
for — he would evaluate our spring evolution and WGSL shader pipeline.

---

## Why Chuna Is the Right Reviewer

Chuna sits at the exact intersection of our work:

1. **Lattice QCD + Lie group integrators** — co-authored with Bazavov on
   gradient flow integration on SU(3) manifolds using MILC. He knows the
   physics our hotSpring lattice QCD reproduces, and he contributed code
   to the production MILC codebase.

2. **Plasma MD + kinetic theory** — published with Murillo on dielectric
   functions, conductivities, and the dynamic structure factor (DSF). The
   DSF is exactly what our Sarkas reproduction validates. He understands
   the physics at the equation level.

3. **ML closures + hybrid models** — neural network moment closures for
   BGK kinetic equations, kinetic-fluid coupling for HED simulations. This
   overlaps directly with neuralSpring (ESN reservoir computing, surrogate
   learning) and the brain architecture (NPU steering).

4. **HPC + numerical methods** — ICER cluster experience, low-storage
   Runge-Kutta, structure-preserving integrators. He can evaluate whether
   our WGSL shader implementations are numerically sound.

He's a PhD student (not faculty), which means he has the time and incentive
to actually read code. He works in Murillo's lab, so Murillo can vouch for
the context. And his dual math/physics background means he can evaluate both
the mathematics and the physics.

---

## Education

- **PhD (in progress)**: Physics & CMSE, Michigan State University (2021–present)
- **MS**: Physics, Michigan State University (lattice QCD / MILC)
- **BS (dual)**: Mathematics + Physics
  - Math: Matrix representations of mapping class groups
  - Physics: High-precision beta decay experiment at NSCL (National
    Superconducting Cyclotron Laboratory, MSU)

---

## Publications

### 1. Gradient Flow Integration on SU(3) — with Bazavov (2021)

**"Efficient integration of gradient flow in lattice gauge theory and
properties of low-storage commutator-free Lie group methods"**
- Bazavov, A. & Chuna, T.
- arXiv: [2101.05320](https://arxiv.org/abs/2101.05320) [hep-lat]
- Published January 2021

Examines three-stage third-order explicit Runge-Kutta Lie group integrators
for SU(3) gradient flow. Demonstrates relation to 2N-storage classical RK
methods. Proposes coefficient tuning for optimal performance. Studies two
fourth-order low-storage alternatives.

**Relevance to us**: Our hotSpring HMC integrator uses Omelyan (4th-order
symplectic) on the SU(3) manifold. Chuna literally wrote the paper on
optimizing these integrators for MILC. He can evaluate whether our Rust/WGSL
implementation is numerically competitive with the production MILC code.

### 2. Conservative Dielectric Functions — with Murillo (2024)

**"Conservative dielectric functions and electrical conductivities from the
multicomponent Bhatnagar-Gross-Krook equation"**
- Chuna, T. & Murillo, M.S.
- arXiv: [2405.07871](https://arxiv.org/abs/2405.07871) [physics.plasm-ph]
- Published: Phys. Rev. E 111, 035206 (2025)

Derives a "completed Mermin" susceptibility from multicomponent BGK that
conserves number and momentum, satisfies the f-sum rule. Applies to DSF
shape under NIF hot-spot conditions (carbon-contaminated DT plasma). New
non-Drude conductivity model. Shows Drude-Smith parameter violates local
number conservation.

**Relevance to us**: The DSF is the central observable in our Sarkas Yukawa
reproduction. Chuna's paper extends the theory beyond what Sarkas computes.
He can evaluate whether our GPU DSF calculations are physically meaningful
and whether our PPPM implementation handles the long-range interactions
correctly.

### 3. Multi-Species Kinetic-Fluid Coupling — with Sagert, Murillo, Haack (2024)

**"Multi-species kinetic-fluid coupling for high-energy density simulations"**
- Chuna, T., Sagert, I., Murillo, M.S., & Haack, J.R.
- Journal of Computational Physics, May 2024
- DOE OSTI: [2368912](https://www.osti.gov/pages/biblio/2368912)

Hybrid model coupling kinetic and hydrodynamic simulations in different
spatial regions. Example: kinetic TH gas region + hydrodynamic CD foam
region. Reduces computational cost while preserving fidelity.

**Relevance to us**: Direct parallel to our brain architecture — different
hardware substrates (GPU, CPU, NPU) handle different computational domains
simultaneously. The multi-fidelity concept (cheap proxy + expensive full
solve) is the same pattern.

---

## Technical Skills (Inferred from Publications + Lab Page)

| Skill | Evidence |
|-------|----------|
| Lattice QCD | MILC contributor, gradient flow integrators, anisotropic lattices |
| Lie group integration | Bazavov & Chuna (2021) — RK on SU(3) manifold |
| Kinetic theory | BGK equation, Chapman-Enskog, moment closures |
| Plasma physics | Dielectric functions, DSF, Yukawa/screened Coulomb |
| HPC | ICER cluster, MILC production runs |
| ML for physics | Neural network moment closures (Murillo Lab) |
| Hybrid methods | Kinetic-fluid coupling, multi-scale |
| Numerical analysis | Structure-preserving integrators, ODE solvers |

**Languages/tools (likely)**: C (MILC), Python, Fortran (HPC tradition),
possibly C++ (Kokkos ecosystem). Unclear if Rust/WGSL experience — probably not.

---

## What He Can Evaluate

| Our Component | His Expertise | Depth |
|---------------|---------------|-------|
| hotSpring lattice QCD (HMC, β-scan) | Literally his thesis area | Deep — wrote MILC integrators |
| hotSpring Sarkas MD (Yukawa, DSF, PPPM) | His advisor's group code | Deep — published on DSF theory |
| BarraCuda WGSL shaders (f64, DF64) | Numerical methods, SU(3) manifold | Can evaluate numerics; WGSL syntax is new |
| Brain architecture (NPU steering) | ML closures, hybrid models | Conceptual overlap; hardware is new |
| Spring evolution pattern (Python→Rust→GPU) | HPC pipeline experience | Can evaluate methodology |
| Kokkos comparison | HPC background (MILC, ICER) | Likely familiar with Kokkos ecosystem |

---

## What to Include in the Review Package

Given his background, the package should emphasize:

1. **hotSpring**: The Sarkas reproduction (his group's code), lattice QCD
   β-scan (his thesis domain), and the PPPM implementation (his DSF work)
2. **BarraCuda shaders**: The SU(3) HMC shaders specifically — he can
   compare against MILC's production integrators
3. **Validation methodology**: The three-tier pattern (Python→Rust→GPU)
   with provenance tracking — he'll appreciate the rigor
4. **DF64 precision**: The Dekker double-float approach — he can evaluate
   whether 14-digit precision is sufficient for the physics
5. **Performance data**: Wall times, FLOPS, energy costs — he can compare
   against MILC/ICER numbers he knows firsthand

**Do NOT lead with**: ecoPrimals architecture, primal sovereignty, BiomeOS,
NestGate, or the broader ecosystem. Lead with the physics he knows and let
him discover the infrastructure.

---

## Funding Context

From his publications:
- DOE DE-SC0023164
- NSF-2309655, NSF-2008004
- DOD SMART Scholarship (Science, Mathematics, and Research for
  Transformation)

The SMART scholarship means he's funded by DOD and will likely return to
a DOD lab after graduation. This is relevant — DOD labs (Sandia, LANL, LLNL)
are exactly where Kokkos lives.

---

*Profile compiled March 4, 2026. Source: Murillo Group lab page, arXiv,
OSTI, web search. Referred by Professor Murillo during second coffee meeting.*
