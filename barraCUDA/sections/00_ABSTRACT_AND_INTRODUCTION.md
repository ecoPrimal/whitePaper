# BarraCUDA: Heterogeneous Scientific Computing Through Constrained Evolution

**Status**: Draft v1  
**Authors**: ecoPrimals Team  
**Date**: February 2026

---

## Abstract

We present BarraCUDA, a GPU-accelerated compute engine implemented in Rust and WGSL
(WebGPU Shading Language) that demonstrates how code structures evolved under one
set of constraints — Fully Homomorphic Encryption — naturally transfer to a different
domain: computational physics. BarraCUDA achieves vendor-neutral execution across
NVIDIA and AMD GPUs from a single shader binary, with 110× GPU speedup for the core
NTT operation and validated cross-vendor correctness (34/36 FHE operations correct,
all GPU operations correct). Heterogeneous dispatch to BrainChip Akida neuromorphic
hardware enables 200× energy efficiency gains for sparse workloads.

We validate BarraCUDA's scientific computing potential through **control experiments**
reproducing published Murillo Group results: 12 molecular dynamics cases (9 Yukawa
+ 3 Coulomb) validated against the Dense Plasma Properties Database across 5
observables (60/60 checks pass), Two-Temperature Model simulations for 3 noble gas
species, and optimizer-directed surrogate learning benchmarks (15/15 pass). These
control experiments establish 81 quantitative acceptance criteria for the GPU
re-implementation phase.

The central finding is that the NTT shader (263 lines, evolved for FHE) shares 80%
structural identity with the FFT shader (186 lines, needed for physics) — the
Cooley-Tukey butterfly, bit-reversal permutation, and stage-wise dispatch are
character-for-character identical. Only the arithmetic domain changes (modular
integers → complex floats). This provides concrete evidence that mathematical
convergence across domains is not coincidental but structural.

---

## 1. Introduction

### 1.1 The Problem

Scientific computing in Python faces a reproducibility crisis that is structural,
not incidental. Published codes depend on specific library version combinations
(NumPy, pandas, Numba, pyfftw) that break silently across major releases. JIT
compilers change semantics without warning. Multi-threaded I/O introduces data
corruption in production code. Root-finder convergence depends on undocumented
initial conditions.

We discovered this empirically: reproducing three published computational physics
codes required **5 separate patches** to work on current Python stacks, three of
which were **silent failures** — the code ran, produced output, and gave no error,
while the actual data was NaN or corrupt. Only explicit dump-level verification
caught them.

This is not a critique of the authors or their software. It is a structural property
of the Python scientific ecosystem, where the boundary between "works" and "silently
produces garbage" is invisible without exhaustive validation.

### 1.2 The Thesis: Constrained Evolution

BarraCUDA was not designed as a scientific computing platform. It was evolved under
two constraints:

1. **Fully Homomorphic Encryption**: Polynomial ring arithmetic (NTT, modular
   multiplication) on encrypted data, requiring 64-bit precision emulation in WGSL's
   32-bit integer domain.

2. **Heterogeneous hardware**: Vendor-neutral GPU execution via WGSL/Vulkan,
   neuromorphic dispatch to BrainChip Akida, with runtime hardware discovery.

Under these constraints, BarraCUDA accumulated 226+ Rust operations and 15 WGSL
shaders. When we audited these against the requirements of computational physics
(molecular dynamics, plasma transport, wave phenomena), we found **~65% coverage**
was already present — not by design but by mathematical necessity.

The NTT → FFT evolution is the clearest example. The Cooley-Tukey butterfly
algorithm is shared between FHE (polynomial multiplication in Z_q) and physics
(spectral analysis in ℂ). The NTT shader's indexing logic, workgroup dispatch,
and bit-reversal permutation transfer verbatim. Only 3 function calls change
(from modular arithmetic to complex arithmetic). This is constrained evolution
observed in code — the constraint (FHE) produced a structure (butterfly transform)
that adapts to an unrelated domain (physics) with 80% code reuse.

### 1.3 This Paper

This paper presents:

- **Section 1 (FHE Validation)**: Real GPU-measured FHE primitive performance,
  cross-vendor correctness, and honest characterization of what the MNIST pipeline
  does and does not yet prove. Long-term FHE applications are gated on NUCLEUS
  ecosystem deployment, not BarraCUDA capability.

- **Section 2 (Hardware Comparison)**: Cross-hardware validation across CPU, NVIDIA
  GPU, AMD GPU, and BrainChip Akida NPU. All data is classified by evidence quality
  (Tier 1: real hardware, Tier 2: partially validated, Tier 3: modeled). Energy
  efficiency varies by 10⁶× across workloads on validated hardware alone.

- **Section 3 (ToadStool Wiring Directive)**: Engineering action items for converting
  remaining modeled benchmarks to real hardware execution. Included for transparency.

- **Section 4 (Control Experiments)**: Reproduction of published Murillo Group
  computational physics results in their original Python implementations. 86/86
  quantitative checks pass across molecular dynamics (Sarkas), plasma transport
  (Two-Temperature Model), surrogate learning, and nuclear EOS validation.
  Phase B BarraCUDA results include GPU FP64 validation (sub-ULP precision),
  478× throughput improvement at L1, and energy profiling showing 44.8× less
  energy consumption on GPU vs Python. These establish the ground truth
  for BarraCUDA Phase B re-implementation.

- **Section 5 (Constrained Evolution)**: Side-by-side code comparison of the NTT
  (FHE ancestor) and FFT (physics descendant) shaders, with quantitative analysis
  of structural reuse (80%) and domain-specific changes (20%).

- **Section 6 (Conclusion)**: Assessment of current capabilities, honest gaps, and
  the 22-30 week roadmap from current state to full scientific computing coverage.

### 1.4 Methodology

All claims are scoped to what the data shows:

- **"Validated"** means measured on real hardware with the operation under test
  actually executing on the claimed substrate (GPU via WGSL/Vulkan, NPU via Akida
  SDK, CPU via native Rust).

- **"Modeled"** means computed from assumptions (datasheet TDP, throughput
  multipliers, sleep-based timing). These are explicitly labeled throughout.

- **"Silent failure"** means the code ran to completion without error but produced
  incorrect data (NaN, corrupted dumps, wrong results). These were discovered through
  our validation pipeline, not through the upstream code's own error handling.

No mock backends, no simulated operations, no estimated timings for any result
labeled "validated." Results labeled "modeled" are presented with full disclosure
of the modeling assumptions.

---

*Sections 1-6 follow.*

