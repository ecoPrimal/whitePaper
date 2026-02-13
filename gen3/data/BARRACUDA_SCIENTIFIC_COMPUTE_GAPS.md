# BarraCUDA: Scientific Computing Gap Analysis

**Status**: Discovery document  
**Purpose**: Map what computational physics reveals as new evolution targets for BarraCUDA  
**Context**: First analysis of BarraCUDA through the lens of scientific computing (Sarkas MD, surrogate learning, TTM, ABM) rather than ML/AI/FHE  
**Last Updated**: February 7, 2026

---

## The Discovery

BarraCUDA evolved under three selective pressures: **machine learning**, **fully homomorphic encryption**, and **universal GPU portability**. This analysis is the first time we've looked at it through the lens of **computational physics** - specifically, what would it take to run Sarkas molecular dynamics, the Two-Temperature Model, surrogate learning, and agent-based epidemiology entirely on BarraCUDA.

The finding: **ML-driven evolution covered ~60-70% of what scientific computing needs**, because the underlying math is shared. The remaining 30-40% is genuinely new territory - and it's illuminating to see exactly where the gap is.

---

## What Already Exists (And Why)

These BarraCUDA ops exist because ML needed them, but they serve scientific computing directly:

| Scientific Need | BarraCUDA Op | Why ML Built It |
|----------------|-------------|-----------------|
| Coulomb screening (erfc) | `erfc.wgsl`, `erf.wgsl` | GELU activation uses erf |
| Pairwise forces | `pairwise_distance.wgsl`, `cdist.wgsl` | Contrastive learning, triplet loss |
| Radial distribution g(r) | `histc.wgsl`, `bincount.wgsl` | Data analysis, histogram equalization |
| Neighbor lists | `sort.wgsl`, `argsort.wgsl`, `searchsorted.wgsl` | Top-k sampling, beam search |
| Tensor contractions | `einsum.wgsl` | Attention, tensor networks |
| Double-precision math | `matmul_fp64.wgsl`, `u64_emu.wgsl` | FHE requires large integer precision |
| Energy/pressure sums | `sum_reduce.wgsl`, `mean_reduce.wgsl` | Loss computation, gradient accumulation |
| Statistical diagnostics | `std_reduce.wgsl`, `variance_reduce.wgsl` | Batch normalization, running statistics |
| Windowed spectral analysis | `stft.wgsl`, `istft.wgsl`, `spectrogram.wgsl` | Audio processing |
| Agent communication | `message_passing.wgsl`, GNN stack | Graph neural networks |
| Integration steps | Basic arithmetic via `unified_math.rs` | Any numeric computation |
| Gamma function | `lgamma.wgsl` | Statistical distributions |
| Trig functions (all) | sin, cos, tan, asin, acos, atan, sinh, cosh, etc. | Positional encoding, rotation |
| Matrix decomposition | `inverse.wgsl`, `determinant.wgsl`, `matrix_power.wgsl` | Normalizing flows, covariance |
| Cumulative sums | `cumsum.wgsl`, `cumprod.wgsl`, `prefix_sum.wgsl` | Scan operations, CDF computation |
| Spatial transforms | `affine_grid.wgsl`, `grid_sample.wgsl` | Image warping, spatial transformers |
| Window functions | `window_function.wgsl` | STFT windowing (Hann, Hamming, etc.) |

**The convergence is real.** ML and physics share the same mathematical substrate. BarraCUDA didn't know it was building a scientific computing engine, but that's what constrained evolution produces - the same ops emerge because the same math is needed.

---

## Critical Gaps: What Physics Reveals

### 1. Complex Number Arithmetic

**Priority**: CRITICAL (blocks FFT, blocks most of computational physics)

**What's missing**: BarraCUDA operates entirely in real-valued arithmetic. Physics needs native complex numbers (a + bi).

**Operations needed**:

| Op | Formula | Use Case |
|----|---------|----------|
| Complex add | (a+bi) + (c+di) = (a+c) + (b+d)i | FFT butterfly |
| Complex mul | (a+bi)(c+di) = (ac-bd) + (ad+bc)i | FFT twiddle factors, wave functions |
| Complex div | (a+bi)/(c+di) | Transfer functions, impedance |
| Complex conjugate | conj(a+bi) = a-bi | Correlation, power spectrum |
| Complex magnitude | |a+bi| = sqrt(a²+b²) | Amplitude, structure factors |
| Complex exp | exp(a+bi) = exp(a)(cos(b)+i·sin(b)) | Euler's formula, Fourier basis |
| Complex sqrt | sqrt(a+bi) | Wave propagation, Green's functions |
| Real/Imaginary extraction | Re(z), Im(z) | Phase analysis |

**Implementation approach**: Store complex as `vec2<f32>` (or `vec2<f64>` via u64 emulation). Each complex shader wraps two reals. This is how CUDA cuFFT works internally.

**Why ML didn't need it**: Neural networks operate in real-valued space. The closest ML gets to complex math is the STFT/ISTFT pipeline, which likely handles complex internally but doesn't expose it as a general primitive.

---

### 2. Complex FFT / IFFT

**Priority**: CRITICAL (blocks PPPM/Ewald summation, blocks structure factors, blocks correlation functions)

**What's missing**: A full complex-to-complex Fast Fourier Transform.

**What exists**:
- `fhe_ntt.wgsl` / `fhe_intt.wgsl` - Number Theoretic Transform (FFT over finite fields, integer domain)
- `stft.wgsl` / `istft.wgsl` - Short-Time Fourier Transform (windowed, overlapping, for audio)

**What's needed**:
- 1D complex FFT (Cooley-Tukey radix-2/radix-4)
- 2D complex FFT (row-column decomposition)
- 3D complex FFT (for PPPM - the critical physics case)
- Inverse FFT (IFFT)
- Real-to-complex FFT (r2c, half-complex optimization)

**Why this is the #1 gap**: PPPM (Particle-Particle Particle-Mesh) is the standard algorithm for long-range Coulomb forces in MD. It splits forces into short-range (real space, direct pairwise) and long-range (reciprocal space, via 3D FFT). Without FFT, you can only do direct O(N²) force calculation, which limits particle count. With FFT, PPPM gives O(N log N).

**Evolution path**: The NTT butterfly structure is isomorphic to FFT. The difference is:
- NTT: modular arithmetic over integers, roots of unity in a finite field
- FFT: floating-point arithmetic over complex numbers, roots of unity on the unit circle

The shader architecture (butterfly pattern, twiddle factors, bit-reversal permutation) already exists in `fhe_ntt.wgsl`. Adapting it to complex float should be a direct evolution, not a ground-up rewrite. **NTT is FFT's sibling - they share the same skeleton.**

---

### 3. Periodic Boundary Conditions (PBC)

**Priority**: HIGH (required for any MD simulation in a periodic box)

**What's missing**: MD simulations occur in periodic boxes where particles that exit one side re-enter from the other. All distance calculations must use the **minimum image convention**.

**Operations needed**:

| Op | Description |
|----|-------------|
| Coordinate wrapping | `pos = pos - floor(pos / box_size) * box_size` |
| Minimum image distance | `dr = dr - round(dr / box_size) * box_size` |
| Periodic pairwise distance | `cdist` variant with PBC |

**Implementation**: A thin wrapper around existing distance ops. The minimum image convention is just a modular operation on the displacement vector. Could be a flag on `pairwise_distance.wgsl` / `cdist.wgsl` rather than a separate shader.

**Why ML didn't need it**: ML operates in unbounded feature spaces. The concept of a periodic simulation box is physics-specific.

---

### 4. Physics-Specific Force Kernels

**Priority**: HIGH (core of MD simulation)

**What's missing**: Specialized shaders for common interparticle potentials with force and energy computation.

| Potential | Formula | Use Case |
|-----------|---------|----------|
| Coulomb | V(r) = q₁q₂ / (4πε₀r) | Charged particles |
| Yukawa / screened Coulomb | V(r) = q₁q₂ exp(-κr) / (4πε₀r) | Dusty plasmas, DLVO theory |
| Lennard-Jones | V(r) = 4ε[(σ/r)¹² - (σ/r)⁶] | Neutral atoms, soft matter |
| Morse | V(r) = D[1 - exp(-a(r-r₀))]² | Molecular bonds |
| Born-Mayer | V(r) = A·exp(-r/ρ) | Short-range repulsion |

Each needs: potential V(r), force F(r) = -dV/dr, virial contribution for pressure.

**Implementation approach**: These are composable from existing ops (exp, pow, reciprocal, etc.). The shader would be a fused kernel: take particle pair, compute distance (with PBC), evaluate potential + force, accumulate. One dispatch per pair, massive parallelism.

**Why ML didn't need it**: ML doesn't compute physics potentials. But the constituent math (exp, pow, reciprocal, sqrt) already exists.

---

### 5. Bessel Functions (J_n, Y_n, I_n, K_n)

**Priority**: MEDIUM-HIGH (needed for TTM cylindrical coordinates, wave physics)

**What's missing**: Bessel functions of the first kind (J), second kind (Y), modified first kind (I), and modified second kind (K).

**Why they matter**:
- **TTM**: The Two-Temperature Model evolves temperatures in **cylindrical coordinates**. Cylindrical coordinate solutions to diffusion/wave equations are expressed in Bessel functions. Without them, you can't do the TTM on BarraCUDA.
- **FMM3D alternative**: The Fast Multipole Method uses spherical harmonics and Bessel functions for multipole expansions. If we want to replace FMM3D (Fortran), we need these.
- **Electromagnetic wave propagation**: Bessel functions describe waveguide modes, antenna patterns, scattering cross-sections.

**Implementation**: Series expansion or polynomial approximation (Abramowitz & Stegun, DLMF). SciPy uses Cephes library (C) for these. A WGSL implementation would use rational polynomial approximations.

**Why ML didn't need it**: ML has no concept of cylindrical/spherical coordinate systems.

---

### 6. Spherical Harmonics Y_l^m

**Priority**: MEDIUM (needed for multipole expansions, FMM replacement)

**What's missing**: Spherical harmonic functions and associated Legendre polynomials.

**Use cases**:
- Multipole expansion of Coulomb potential (replace FMM3D Fortran)
- Angular momentum decomposition
- Gravitational potential modeling
- 3D rotational invariant features (potential ML crossover: SE(3) equivariant networks)

**Note**: This has a potential ML/physics crossover. Equivariant neural networks (used in molecular property prediction) use spherical harmonics. If BarraCUDA gets these, it serves both physics and next-gen ML architectures.

---

### 7. ODE/PDE Solvers

**Priority**: MEDIUM (needed for TTM, general physics simulation)

**What's missing**: Explicit time-stepping schemes on GPU.

| Solver | Type | Use Case |
|--------|------|----------|
| RK4 | Fixed-step ODE | General physics integration |
| RK45 (Dormand-Prince) | Adaptive ODE | Variable timestep |
| Velocity-Verlet | Symplectic | MD time integration (energy conservation) |
| Leapfrog | Symplectic | N-body simulation |
| Finite difference stencils | PDE | Heat equation, diffusion, TTM |
| Crank-Nicolson | Implicit PDE | Stable diffusion |

**Implementation approach**: These are patterns over existing arithmetic. A Velocity-Verlet shader is: `v += 0.5*F/m*dt; x += v*dt; recompute F; v += 0.5*F/m*dt`. The structure is simple; the value is having it as a reusable shader.

**Why ML didn't need it**: Neural networks train via backpropagation (gradient descent), not forward-time integration. The closest ML equivalent is Neural ODEs, which is a niche architecture.

---

### 8. Scientific Interpolation

**Priority**: MEDIUM (needed for EOS tables, force interpolation)

**What exists**: `interpolate.wgsl`, `interpolate_nearest.wgsl` - but these are image-domain (bilinear/bicubic for upsampling).

**What's needed**:
- 1D cubic spline interpolation (for EOS tables, potential tabulation)
- Chebyshev interpolation (for spectral methods)
- Polynomial interpolation (Lagrange, Newton)
- Lookup table with interpolation (physics uses tabulated functions extensively)

**Why ML's version isn't enough**: ML interpolation assumes regular grids (pixel coordinates). Physics interpolation needs irregular grids (e.g., non-uniform temperature/density points in an EOS table).

---

### 9. Eigenvalue Decomposition

**Priority**: MEDIUM (needed for normal modes, stability analysis, PCA of trajectories)

**What exists**: `inverse.wgsl`, `determinant.wgsl`, `matrix_power.wgsl` - matrix operations exist.

**What's needed**:
- Eigenvalue computation (symmetric and general)
- Eigenvector computation
- SVD (singular value decomposition)
- QR decomposition

**Why they matter**: Normal mode analysis of crystal structures, stability analysis of equilibria, principal component analysis of simulation trajectories. Also critical for iterative solvers (Lanczos, GMRES).

---

### 10. High-Quality PRNG

**Priority**: MEDIUM (needed for Monte Carlo, Langevin thermostat, initial conditions)

**What exists**: Random ops for dropout, augmentation (random_crop, random_rotation, etc.).

**What may be needed**: Scientific computing demands specific PRNG quality:
- Long period (>2⁶⁴)
- Uniform distribution guarantees
- Reproducibility across hardware (same seed → same sequence on NVIDIA and AMD)
- Parallel-safe (independent streams per thread)
- Common choices: PCG, xoshiro256**, Mersenne Twister

**Why ML's version may not suffice**: ML random ops need "good enough" randomness for dropout masks. Physics needs statistically rigorous randomness for Monte Carlo integration where subtle correlations in the PRNG can bias thermodynamic averages.

---

### 11. Sparse Matrix Operations

**Priority**: LOW-MEDIUM (needed for HNC, large linear systems)

**What exists**: `sparse_matmul_quantized.rs` - quantized sparse matmul for ML inference.

**What's needed**:
- General sparse matrix-vector multiply (SpMV)
- Sparse matrix-matrix multiply (SpGEMM)
- Conjugate gradient solver
- Preconditioned iterative solvers

**Use case**: The Ornstein-Zernike equation (HNC approximation from Murillo's BIM_HNC) involves solving integral equations that reduce to sparse linear systems. Also relevant for finite element methods.

---

## Unexpected Synergies

The gap analysis revealed operations that serve *both* physics and future ML architectures:

| Operation | Physics Use | ML Use |
|-----------|------------|--------|
| Spherical harmonics | Multipole expansion, FMM | SE(3)-equivariant neural networks |
| Complex FFT | PPPM, structure factors | Complex-valued neural networks |
| Bessel functions | Cylindrical PDE solutions | Bessel-basis neural potentials |
| Eigendecomposition | Normal modes, stability | Spectral graph convolutions |
| ODE solvers | Time integration | Neural ODEs (continuous-depth networks) |
| Sparse operations | Integral equations | Sparse transformers, mixture of experts |
| High-quality PRNG | Monte Carlo sampling | Diffusion models, stochastic depth |

**These aren't just physics additions - they're the next frontier of ML compute too.** BarraCUDA evolving these capabilities would serve both domains simultaneously.

---

## The Evolution Path: NTT → FFT as a Case Study

The most instructive gap is the FFT. Here's why:

BarraCUDA already has NTT (Number Theoretic Transform) for FHE:
- Butterfly computation pattern ✓
- Twiddle factor application ✓
- Bit-reversal permutation ✓
- Forward and inverse transforms ✓
- GPU-parallel dispatch ✓

NTT operates over integers modulo a prime. FFT operates over complex floats on the unit circle. The **algorithm is identical** - the **arithmetic domain** is different.

This is exactly the constrained evolution pattern: the FHE constraint produced NTT, which contains the structural DNA for FFT. The structure evolved for one purpose (encrypted computation) and can be adapted for another (physics simulation) because the underlying mathematical structure is invariant.

To get FFT from NTT:
1. Replace modular integer arithmetic with complex float arithmetic
2. Replace roots of unity mod p with roots of unity on the unit circle: exp(-2πi·k/N)
3. Keep the butterfly structure, the bit-reversal, the recursive decomposition

**The NTT shader is the FFT shader's ancestor.** This is covalent evolution in the BarraCUDA codebase.

---

## Summary: What to Evolve

### Must Have (Phase B Blockers)

| # | Gap | Effort | Dependencies |
|---|-----|--------|-------------|
| 1 | Complex number type/arithmetic | Medium | None - foundational |
| 2 | Complex FFT (1D, 2D, 3D) | Medium-High | Complex arithmetic, NTT structure |
| 3 | Periodic boundary conditions | Low | Existing distance ops |
| 4 | Force kernels (Coulomb, Yukawa, LJ) | Low-Medium | PBC, existing math |

### Should Have (Full Scientific Computing)

| # | Gap | Effort | Dependencies |
|---|-----|--------|-------------|
| 5 | Bessel functions | Medium | Series/polynomial approximation |
| 6 | ODE/PDE solvers (Verlet, RK4, FD stencils) | Medium | Basic arithmetic |
| 7 | Scientific interpolation (spline, Chebyshev) | Low-Medium | None |
| 8 | High-quality PRNG | Medium | None |

### Nice to Have (Extended Capability)

| # | Gap | Effort | Dependencies |
|---|-----|--------|-------------|
| 9 | Spherical harmonics | Medium-High | Bessel, Legendre polynomials |
| 10 | Eigendecomposition / SVD | High | Linear algebra foundations |
| 11 | Sparse matrix operations | High | New data structure support |

### Total New Shaders Estimated: ~25-40

Added to the existing 226+, this would bring BarraCUDA to ~260+ WGSL shaders covering ML, FHE, **and** scientific computing. A universal compute engine.

---

**This is constrained evolution observed in real time. The ML/FHE pressure produced ops that accidentally cover 60-70% of physics. The remaining gaps are specific, identifiable, and in many cases (FFT from NTT, force kernels from distance ops) the ancestral structure already exists. The physics constraint doesn't require starting over - it requires evolving what's already there.**
