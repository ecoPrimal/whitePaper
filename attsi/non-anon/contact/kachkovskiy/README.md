# Ilya Kachkovskiy — Outreach & GPU Spectral Computing

**Faculty**: Ilya Kachkovskiy, Assistant Professor, Department of Mathematics, MSU
**Website**: https://users.math.msu.edu/users/ikachkov/
**Email**: ikachkov@msu.edu | Room C300, Wells Hall
**NSF**: DMS-1758326 "Spectral theory of periodic and quasiperiodic quantum systems"
**Connection**: Sold the NucBox M6 on Facebook Marketplace; brief GPU conversation; noticed equations on his whiteboard
**Hardware**: Known to have an RTX 5080

---

## Context

Kachkovskiy is the mathematician whose work underpins the Anderson localization
framework that runs through the entire ecoPrimals thesis. His spectral theory
sits between Murillo's plasma physics and Bazavov's lattice QCD — he proves the
eigenvalue mathematics they both use. His co-author network is extraordinary:
Jean Bourgain (Fields Medalist), Svetlana Jitomirskaya (Dannie Heineman Prize),
Nikolay Filonov (Steklov Institute).

We bought a NucBox M6 mini PC from him on Facebook Marketplace. Brief
conversation about GPUs. He has an RTX 5080, which means he does numerical
computation — likely eigenvalue problems, lattice diagonalization, localization
studies. He's a mathematician who computes.

---

## What We've Already Built With His Math

Anderson localization and spectral theory are the most deeply validated
primitives in the entire ecosystem. Four springs consume his mathematics:

| Spring | Experiments | Checks | What |
|--------|:-----------:|:------:|------|
| hotSpring | Papers 14-22 | **45/45** | Anderson 1D/2D/3D, Hofstadter butterfly, Almost-Mathieu, Lanczos, GPU SpMV + Lanczos |
| groundSpring | Exp 008, 009, 012, 018 | **44+** | Anderson localization, Almost-Mathieu, spin chain transport, band edge |
| wetSpring | Exp107 + 113-149 | **312+** | Spectral cross-spring bridge → QS biology, 28-biome atlas, NPU classifier |
| neuralSpring | Papers 022-023 | **16/16** | Spectral commutativity, Anderson localization |
| **Total** | | **417+** | Across 4 springs, 30+ experiments |

### Papers Reproduced (his domain)

| # | Paper | Citation | Where |
|---|-------|----------|-------|
| 1 | Anderson (1958) | "Absence of diffusion in certain random lattices" | hotSpring |
| 2 | Aubry & André (1980) | "Analyticity breaking and Anderson localization" | hotSpring |
| 3 | Jitomirskaya (1999) | "Metal-insulator transition for the almost Mathieu operator" | hotSpring |
| 4 | Herman (1983) | "Une méthode pour minorer les exposants de Lyapunov" — γ = ln|λ| | hotSpring |
| 5 | Lanczos (1950) | Iteration method — eigenvalue solver | hotSpring |
| 6 | Abrahams et al. (1979) | "Scaling theory of localization" — GOE→Poisson | hotSpring |
| 7 | Slevin & Ohtsuki (1999) | "Critical exponent for the Anderson transition" — 3D mobility edge | hotSpring |
| 8 | Hofstadter (1976) | "Energy levels and wave functions" — butterfly, Cantor spectrum | hotSpring |
| 9 | Avila & Jitomirskaya (2009) | "The Ten Martini Problem" | hotSpring |
| 10 | Kachkovskiy & Safarov (2016) | Spectral commutativity | neuralSpring |
| 11 | Bourgain & Kachkovskiy (2018) | "Anderson localization for two interacting quasiperiodic particles" GAFA | wetSpring, groundSpring, neuralSpring |

### GPU-Validated Spectral Primitives (in barraCuda)

| Primitive | Precision | Hardware | Status |
|-----------|-----------|----------|--------|
| Lanczos eigenvalue solver | f64 | RTX 4070 | **Validated** (6/6, 1e-15 parity) |
| Sparse matrix-vector product (CSR SpMV) | f64 | RTX 4070 | **Validated** (8/8, 1.78e-15) |
| Anderson 3D disorder sweep | f64 | RTX 4070 | **Validated** (10/10) |
| Hofstadter butterfly (Harper equation) | f64 | RTX 4070 | **Validated** (10/10) |
| Almost-Mathieu Lyapunov exponent | f64 | RTX 4070 | **Validated** |
| DF64 extended precision Anderson | DF64 | Titan V | **Validated** (14-digit) |

---

## What He Likely Does With a 5080

Kachkovskiy is a spectral theorist who proves localization results. His
computational workflow probably looks like:

1. **Large Anderson lattices** — diagonalize random tight-binding Hamiltonians
   at increasing L to study finite-size scaling of localization length. Python
   (NumPy/SciPy) on CPU, or possibly Julia. L=100-1000 in 1D, L=20-50 in 2D/3D.

2. **Almost-Mathieu eigenvalue statistics** — compute eigenvalues of the Harper
   operator at irrational α, study spectral measure (Cantor set structure),
   Lyapunov exponents. Sweep over coupling λ and frequency α.

3. **Two-particle localization** — his Bourgain paper. Numerically verify
   localization for two interacting quasiperiodic particles. This is
   computationally expensive: Hilbert space is L² for two particles.

4. **Spin chain transport** — Kachkovskiy (2016 CMP). Time evolution of
   quasiperiodic XY spin chains, measuring transport exponents. Requires
   matrix exponentiation or Chebyshev expansion.

5. **Band edge computation** — Filonov & Kachkovskiy (2018 Acta Math). 2D
   periodic operators, spectral band structure. Numerical verification of
   analytic predictions.

**Pain points** (likely):
- Python/SciPy sparse eigensolvers are CPU-bound — the 5080 sits idle
- Large 2D/3D Anderson lattices (L=50+) take hours on CPU
- Two-particle Hilbert space grows as L², making GPU essential
- No easy path from NumPy sparse to GPU without CUDA or CuPy vendor lock-in

---

## What ecoPrimals Enables For Him

### Immediate (today, validated)

| Capability | His Workflow | ecoPrimals Version |
|-----------|-------------|-------------------|
| GPU Lanczos eigensolve | SciPy CPU `eigsh` | barraCuda `Lanczos` — f64, RTX 4070, 1e-15 parity |
| GPU SpMV (CSR) | SciPy CPU `sparse.dot` | barraCuda `SpMV` — f64, validated 1.78e-15 |
| Anderson 1D/2D/3D sweep | Python loop over disorder W | barraCuda GPU sweep — embarrassingly parallel |
| Hofstadter butterfly | Python Harper diagonalization | barraCuda GPU — full butterfly in seconds |
| Almost-Mathieu Lyapunov | Transfer matrix product (slow in Python) | barraCuda GPU — parallel over energy grid |
| DF64 extended precision | Limited by float64 | 14-digit DF64 via WGSL on any GPU |

### Near-term (write phase)

| Capability | His Need | What We'd Build |
|-----------|----------|----------------|
| Two-particle Anderson | L² Hilbert space, huge matrices | GPU Lanczos on 2-particle Hamiltonian |
| Spin chain dynamics | Matrix exponential / Chebyshev | GPU time evolution shader |
| 2D band edge | Periodic operator eigenvalues | Floquet-Bloch GPU sweep over Brillouin zone |
| Large-L 3D Anderson | L=50+ requires GPU or cluster | barraCuda 3D — runs on his 5080, no cluster |

### The pitch (unstated)

His 5080 has 16GB VRAM and native f64. With barraCuda:
- 3D Anderson at L=50: fits in ~2GB, runs in minutes instead of hours
- Hofstadter at L=10,000: full butterfly resolution unachievable on CPU
- Two-particle at L=200: ~6GB, feasible on 5080, impossible on CPU in Python
- No CUDA, no CuPy, no vendor lock-in — compiles from source, runs anywhere

---

## Outreach Strategy

This one is different from Chuna. Chuna is a PhD student we reached through
Murillo. Kachkovskiy is a professor we bought a computer from. The connection
is personal but thin.

### Approach

1. **Don't email cold.** The NucBox purchase is the connection. Reference it.
   "I'm the guy who bought the NucBox — I noticed the equations on your
   whiteboard." This is memorable and human.

2. **Lead with his math, not our infrastructure.** "I've been implementing
   Anderson localization and Hofstadter butterflies on consumer GPUs. Your
   Bourgain paper is one of the things I validated."

3. **Show the GPU angle.** He has a 5080. He computes. The value proposition
   is: "the eigenvalue solvers you use in Python/SciPy now run on your GPU
   at f64 precision, vendor-agnostic, no CUDA."

4. **Don't oversell biology.** He's a pure mathematician. The QS-disorder
   bridge is our application — don't lead with it. If he's curious about
   where Anderson localization shows up in biology, he'll ask.

5. **Offer a concrete artifact.** "Here's the Hofstadter butterfly computed
   on an RTX 4070 in 3 seconds. Here's your Bourgain-Kachkovskiy two-particle
   localization running on GPU. Want to try it on your 5080?"

### What We're Asking

- Does our GPU Lanczos reproduce correct eigenvalue statistics for Anderson?
- Does the Hofstadter butterfly match his expectations at high resolution?
- Would GPU-accelerated spectral tools be useful for his research?
- Can he point us to numerical benchmarks we should match?

### What We're NOT Asking

- No endorsement of ecoPrimals or constrained evolution
- No collaboration commitment
- No code review (unless he wants to)
- No biology pitch

---

## Outreach Readiness

### Ready Now
- 11 papers reproduced, 417+ checks passing
- GPU Lanczos validated to machine precision (1e-15)
- Hofstadter butterfly in ~3s on RTX 4070
- Public repos with `cargo run` binaries
- Cross-spring absorption cycle demonstrated

### Not Ready (blocks compelling demo)
- GPU Lanczos only validated to N=144 — his lattices are 1000+
- No SciPy `eigsh` comparison benchmark — can't answer "faster than what I use?"
- No two-particle Anderson GPU — his Bourgain paper headline
- No large-N scaling curves — can't show where GPU dominates CPU

### Minimum Viable Demo (before contact)
1. GPU Lanczos at N=10000+ with timing
2. SciPy `eigsh` comparison on same hardware
3. Hofstadter butterfly visualization (have this)
4. Anderson 3D mobility edge on GPU at L=20+

**Evolution handoff**: `wateringHole/handoffs/SPECTRAL_GPU_CROSS_SPRING_KACHKOVSKIY_EVOLUTION_HANDOFF_MAR10_2026.md`

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — outreach plan and work inventory |
| `review_package.md` | Technical review: spectral primitives, GPU benchmarks, validation data |
| `email_draft.md` | Draft email for first contact |

## Timeline

- **Pre-contact**: Close P0/P1 gaps from evolution handoff (SciPy benchmark, large-N GPU Lanczos)
- **Contact**: Email or in-person (Wells Hall is on campus)
- **Tone**: "I bought your NucBox. I've been running your math on GPUs. Want to see?"
