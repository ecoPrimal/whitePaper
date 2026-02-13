# Section: Conclusion and Future Work

**Status**: Draft v1  
**Date**: February 2026

---

## 1. What Is Established

### 1.1 Validated Claims (Tier 1 — Real Hardware)

| Claim | Evidence | Section |
|-------|----------|:-------:|
| FHE primitives execute correctly on GPU | 34/36 ops correct (all GPU ops correct), NVIDIA + AMD | §1 |
| GPU NTT achieves 110× speedup at N=4096 | Measured on RTX 3090, 100 iterations | §1 |
| Cross-vendor GPU parity via WGSL/Vulkan | 18/18 operations identical on NVIDIA + AMD | §2 |
| GPU batch ML throughput scales 90× (b=1→128) | MNIST MLP, real BarraCUDA MatMul | §2 |
| Energy efficiency varies by ≥10⁶× across workloads | CPU dense add (95.2M ops/J) vs GPU same op (33 ops/J) | §2 |
| NTT → FFT shares 80% structural identity | Side-by-side code comparison, bit-reversal identical | §5 |
| Sarkas MD: 60/60 observable checks pass | 5 obs × 12 cases, DSF validated vs Dense Plasma DB | §4 |
| TTM: 3/3 species equilibrate (0D) | Argon, Xenon, Helium reach |Te-Ti| < 0.001 K | §4 |
| TTM: 3/3 species produce valid radial profiles (1D) | Te monotonic, FWHM expands, zero NaN | §4 |
| Surrogate: 15/15 benchmarks pass | mystic finds global min on all 5 functions | §4 |
| Physics surrogate from MD: LOO error ±0.090 decades | RBF trained on 12 validated cases, 900,000× speedup | §4 |
| Code Ocean is gated (not open science) | Sign-up denied, nuclear EOS wraps restricted LANL data | §4 |
| Python scientific stack requires patching | 5 bugs found: NumPy 2.x, pandas 2.x, Numba 0.60, Saha IO | §4 |

### 1.2 Partially Validated (Tier 2 — Cite with Caveat)

| Claim | Status | Gap |
|-------|--------|-----|
| NPU achieves 200× energy efficiency for inference | MNIST on real Akida, power from datasheet | Need measured power |
| FHE operation overhead is 41-10,000× | Real GPU timing, but not yet end-to-end encrypted | Need ciphertext encoding |
| TTM hydro completes full simulation | 3/3 run, Zbar diverges at r=0 after partial completion | Need solver tuning |

### 1.3 Not Yet Validated (Tier 3 — Future Work)

| Claim | Status | Dependency |
|-------|--------|------------|
| NPU sparse processing advantage | Modeled (sleep/busy-loop) | ToadStool Akida wiring |
| End-to-end encrypted ML | FHE primitives ready, composition missing | NUCLEUS + BearDog |
| BarraCUDA reproduces Sarkas physics | Python control established, GPU phase not started | Phase B implementation |
| Full-scale MD (N=10,000) | N=2,000 validated, N=10,000 needs 32GB+ RAM | Strandgate execution |

---

## 2. Key Findings

### 2.1 The Python Scientific Stack Is Fragile

The 5 upstream bugs discovered during control experiments were not edge cases. They
affect standard operations (polynomial indexing, DataFrame aggregation, JIT
compilation, root-finding initialization, data file I/O) across 3 unrelated
codebases (Sarkas, TTM, Saha data). Three of these were **silent failures** — the
code produced output without error, and the output was wrong.

This is a structural problem. Python's dynamic typing, implicit coercion, and
lazy deprecation model mean that code that works on Python 3.8 + NumPy 1.21 +
Numba 0.53 may silently produce garbage on Python 3.12 + NumPy 2.1 + Numba 0.60.
The canonical workaround — pinning exact environments — is unsustainable for
long-lived scientific software.

BarraCUDA's Rust/WGSL stack addresses this at the language level: static typing
prevents implicit coercion, the borrow checker prevents data races, and WGSL
shaders compile to SPIR-V with deterministic semantics. The 97.2% profiling
hotspot (one force kernel function) means the correctness guarantee applies to
the code that matters most.

### 2.2 Constrained Evolution Produces Reusable Structure

The NTT → FFT evolution (80% code reuse, 20% domain-specific change) is not a
one-off result. The pattern extends across BarraCUDA's operation set:

- `erf.wgsl` (ML activation) → Coulomb screening integral (same series expansion)
- `cdist.wgsl` (contrastive learning) → MD pairwise forces (same spatial pattern)
- `histc.rs` (data analysis) → RDF binning (same accumulation kernel)
- `stft.rs` (audio) → DSF computation (same windowed spectral analysis)

Each of these pairs shares the same computational pattern for different physical
reasons. The convergence is mathematical, not accidental.

### 2.3 81 Quantitative Checks Provide Phase B Acceptance Criteria

The control experiments did not just validate the upstream codes — they produced
concrete numerical targets for BarraCUDA's GPU re-implementation:

- DSF peak frequencies within 10% of reference database
- Energy drift < 2% per simulation
- RDF first peak within ±0.05 a_ws
- Diffusion coefficient within 10% (Green-Kubo)
- Te=Ti equilibrium within 1 K
- FWHM expansion within 5%
- Surrogate optimization gap within 10%

These criteria are not arbitrary thresholds. They are the values actually achieved
by the Python codes on the same physics. Meeting them on GPU proves numerical
equivalence.

### 2.4 "Reproducible" Science Has Access Gates

The surrogate learning control experiment revealed a second class of reproducibility
failure: **published "open" results behind gated infrastructure**. The Diaw et al.
(2024) paper links to a Code Ocean capsule for the nuclear EOS objective function.
Code Ocean requires institutional-approved sign-up (denied on our system). The
objective function itself wraps Los Alamos National Laboratory nuclear simulation data.

This is distinct from the Python version-drift problem:
- **Python fragility** (§4.1): The code exists but breaks on current libraries
- **Access gating** (this finding): The code exists but isn't downloadable

Both undermine the promise of "reproducible computational science." The convergence
data in Zenodo proves the method works (χ² → 9×10⁻⁶), but independent verification
requires institutional access. Our circumvention took two forms:

1. **Physics surrogate from validated MD data**: RBF trained on 12 Sarkas cases,
   producing 900,000× speedup with LOO cross-validation.
2. **Nuclear EOS from first principles**: Skyrme EDF → nuclear matter → SEMF → χ²
   against AME2020, implemented in 300 lines of Python (no HFBTHO, no Fortran, no
   permissions). Surrogate learning on the 10D Skyrme landscape demonstrated learning
   (score 2.5 → 1.4 over 30 rounds, best χ²/datum = 17.73). See §4a.5.

---

## 3. Roadmap

### 3.1 Near-Term (Eastgate — No NUCLEUS Required)

| Item | Status | Blocks |
|------|--------|--------|
| Code Ocean capsule download | **Blocked** (gated access, sign-up denied) | Nuclear EOS callable |
| Nuclear EOS surrogate reproduction | **Done** — rebuilt from scratch (Skyrme→SEMF, 300 lines Python) | See §4a.5 |
| Nuclear EOS full convergence | Needs more evals (6000/30000 used, 10D is sparse) | Compute time |
| TTM Zbar solver tuning | Low priority | Full hydro completion |

### 3.2 Cross-Gate (After NUCLEUS Stabilizes)

| Item | Gate | Blocks |
|------|------|--------|
| Full-scale DSF (N=10,000) | Strandgate (32GB+) | Production MD data |
| Cross-gate benchmark protocol | 10G backbone | Publication data |
| GPU surrogate training | Northgate (GPU) | ML reproduction |

### 3.3 ToadStool Wiring (Section 3 Action Items)

| Priority | Task | Effort | Impact |
|:--------:|------|--------|--------|
| 1 | Wire real Akida inference into pipeline dispatch | 1-2 days | Converts NPU from modeled → real |
| 1 | Wire Akida power telemetry | 1 day | Converts energy from datasheet → measured |
| 2 | Delete fake GPU demos (sleep-based) | 30 min | Removes misleading data |
| 2 | Wire GPU power measurement (nvidia-smi) | 2 hours | Measured GPU energy |
| 3 | Full transformer architecture | 3-5 days | Production-competitive ML |
| 3 | Audio STFT with real FFT shader | 1-2 days | Validates FFT evolution |

### 3.4 BarraCUDA Phase B (22-30 Weeks Total)

| Phase | Content | Duration | Milestone |
|:-----:|---------|:--------:|-----------|
| 1 | Complex arithmetic (10 ops) + FFT suite (5 shaders) | 8-12 weeks | FFT(IFFT(x))=x, PPPM unblocked |
| 2 | PBC, force kernels, integrators, Bessel | 6-8 weeks | Sarkas MD runs on GPU |
| 3 | Spherical harmonics, eigenvalue, sparse, PRNG | 8-10 weeks | Advanced physics |

---

## 4. Honest Assessment

BarraCUDA is not yet a scientific computing platform. It is a validated ML/FHE
compute engine with measured cross-vendor GPU performance, honest documentation of
what works and what doesn't, and a concrete evolution path to physics.

What makes the evolution path credible:

1. **The NTT → FFT example is real code**, not a design document. Both shaders exist,
   compile, and execute. The 80% structural reuse is measured, not projected.

2. **The control experiments found real problems** in real physics codes. Five bugs in
   three codebases, three of which were silent. This is the problem space BarraCUDA
   addresses.

3. **81 quantitative checks establish falsifiable acceptance criteria**. Phase B
   either reproduces these numbers on GPU or it doesn't. There is no ambiguity.

4. **The honest gaps are documented**. NPU benchmarks that use sleep() are labeled
   "modeled." ML architectures that are simplified are labeled "simplified." FHE
   operations that don't yet compose into end-to-end encryption are labeled "future
   work." No claim exceeds the evidence.

The work is not complete. It is honestly reported.

---

*Data archives:*  
*Control results: `hotSpring/control/comprehensive_control_results.json`*  
*Observable validation: `hotSpring/control/sarkas/simulations/dsf-study/results/all_observables_validation.json`*  
*Benchmark data: `whitePaper/barraCUDA/data/`*

