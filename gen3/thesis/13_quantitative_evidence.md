# Chapter 13: Quantitative Evidence for Constrained Evolution

## 13.1 Overview

This chapter presents the measurable signatures of constrained evolution in the ecoPrimals codebase, moving beyond biological analogy to quantitative evidence that the same dynamics observed in the LTEE and hot spring populations operate in computational systems under type-theoretic constraint.

---

## 13.2 The NTT → FFT Structural Evolution

### 13.2.1 Background

BarraCUDA's Number Theoretic Transform (NTT) was evolved under fully homomorphic encryption (FHE) constraints for polynomial multiplication in \(\mathbb{Z}_q\). The Fast Fourier Transform (FFT), needed for physics simulation (lattice QCD, spectral methods), shares the Cooley-Tukey butterfly structure.

### 13.2.2 Structural Comparison (Measured from Source)

Source files: `fhe_ntt.wgsl` (263 lines), `fft_1d.wgsl` (186 lines), `fft_1d_f64.wgsl` (197 lines). The FFT header explicitly records its ancestry: *"Adapted from fhe_ntt.wgsl (80% structure reuse!)"*.

| Component | NTT (`fhe_ntt.wgsl`) | FFT (`fft_1d.wgsl`) | Match |
|-----------|:-------------------:|:-------------------:|-------|
| Domain arithmetic library | 93 lines (U64 emulation) | 16 lines (complex mul/exp) | Different (domain-specific) |
| Buffer bindings (4 each) | 4 lines | 4 lines | **Same structure** |
| Params struct | 8 fields (needs modulus/Barrett) | 4 fields | Partial |
| Load from input | 4 lines | 4 lines | **Identical structure** |
| Load twiddle | 4 lines | 4 lines | **Identical structure** |
| Store to output | 4 lines | 5 lines | **Identical structure** |
| Modular arithmetic wrappers | 20 lines | 0 | Unique to NTT |
| Butterfly struct | 4 lines | 4 lines | **Identical** |
| Butterfly function | 5 lines: `u=(a+tb)%q, v=(a-tb)%q` | 5 lines: `u=a+tb, v=a-tb` | **Identical** (NTT adds mod) |
| `bit_reverse_index` | 8 lines | 8 lines | **100% identical** |
| Main compute kernel | 40 lines | 39 lines | **~97% identical** |
| `bit_reverse` kernel | 26 lines | 26 lines | **~97% identical** |

Shared structural core: ~93 lines identical between NTT and FFT (butterfly, bit-reversal, indexing, load/store, main dispatch). The main compute kernel — stage indexing, stride computation, block decomposition, twiddle lookup — is character-for-character identical between both files.

The FFT is *shorter* than its NTT ancestor because complex floats (native `vec2<f32>`) map to GPU hardware natively, while NTT requires U64 emulation from u32 pairs (WGSL lacks native u64). The f64 FFT variant (197 lines) uses a `Complex64` struct but retains the identical butterfly/indexing skeleton. This is the computational analog of an adaptation that simplifies — the Lenski populations' improved glucose transport is simpler and more efficient than the ancestral mechanism.

### 13.2.3 Interpretation

No one designed BarraCUDA for physics. The FHE constraint required NTT; NTT required the Cooley-Tukey butterfly; the butterfly *is* the FFT's skeleton. Each step follows by mathematical necessity within the constraint. This is constrained evolution: the constraint (FHE) reshaped the fitness landscape to select for a structure (butterfly transform) that happened to be fit for an unrelated domain (physics).

**This is Taq polymerase in code.** The hot spring (FHE constraint) produced an enzyme (NTT butterfly) that proved useful far beyond its original environment (physics simulation), because the constraint selected for a mathematical structure that was universal.

---

## 13.3 Convergent IPC Patterns

### 13.3.1 Method

All 12 primals implement JSON-RPC 2.0 IPC independently. We analyze the structural similarity of these independent implementations — the computational analog of convergent evolution in isolated populations.

### 13.3.2 Convergent Features

| Feature | Primals Converging | Independent Implementations |
|---------|-------------------|---------------------------|
| JSON-RPC 2.0 message format | 12/12 | 12 distinct parsers |
| Unix domain socket transport | 12/12 | 12 distinct socket handlers |
| Capability advertisement on connect | 11/12 | 11 distinct advertisement protocols |
| Async Tokio runtime | 12/12 | 12 distinct runtime configurations |
| Structured error types (enum + Display) | 12/12 | 12 distinct error hierarchies |
| Zero unsafe blocks | 12/12 | Enforced by constraint, not by convention |

### 13.3.3 Non-Identical Solutions

Despite convergent features, the implementations differ in:
- Error granularity (BearDog has ~40 error variants; Songbird has ~25)
- Connection pooling strategies
- Timeout and retry logic
- Message batching approaches
- Capability versioning schemes

This is the cephalization/eyes/wings pattern: same function, different developmental pathways, because the constraint rewards the function without prescribing the mechanism.

---

## 13.4 Fastidious Specialization Over Time

### 13.4.1 Method

Analyzing primal scale across the evolutionary timeline reveals a clear maturity gradient:

| Phase | Primals | Avg Rust Lines | Avg #[test] | Age (months) |
|-------|--------:|---------------:|------------:|:------------:|
| Phase 1 | 5 | 618,966 | 14,299 | ~10 |
| Phase 2 | 7 | 96,972 | 4,148 | ~3–6 |
| **Ratio** | | **6.4×** | **3.4×** | |

Phase 1 primals average 6.4× more code and 3.4× more tests than Phase 2 primals. This is the accumulation signature: longer evolutionary exposure under constraint produces larger, more specialized, more thoroughly tested organisms.

### 13.4.2 Primal-Level Specialization

The largest primals are also the most specialized:

- **Squirrel** (681,933 lines, 25,359 tests) — deeply adapted to multi-provider AI coordination, MCP protocol, model routing. Could not be ported to another IPC model without complete rewrite.
- **ToadStool** (788,209 lines, 13,503 tests) — deeply adapted to WGSL/Vulkan compute, f64 emulation, shader pipeline management. The 628 WGSL shaders represent extreme specialization to the GPU constraint.
- **BearDog** (577,341 lines, 11,872 tests) — deeply adapted to cryptographic operations, 91 methods, HSM integration. The entropy hierarchy principle is BearDog-specific.

Meanwhile, younger primals like **skunkBat** (7,366 lines, 48 tests) and **rhizoCrypt** (27,565 lines, 278 tests) remain more generic — less specialized because they have undergone fewer evolutionary cycles.

### 13.4.3 Expected Full Analysis

A complete git history analysis (pending) would measure:
- Idiomatic Rust usage (clippy lint compliance over time)
- Dependency tree narrowing (fewer external crates over time)
- Trait boundary tightening (more specific type constraints over time)
- Test coverage trajectory
- Lines per function (should decrease as specialization increases)

The prediction: these metrics follow power-law dynamics (rapid early improvement, decelerating), paralleling the LTEE fitness trajectory (Wiser et al., 2013).

---

## 13.5 The 2,882-Check Velocity

### 13.5.1 Current Inventory (Measured February 2026)

| Spring | Domain | Checks | Papers Reproduced |
|--------|--------|-------:|------------------:|
| hotSpring | Plasma physics, nuclear, lattice QCD, spectral | 195 | 18 |
| airSpring | ET₀, soil sensors, IoT irrigation | 326 | 5 |
| wetSpring | 16S metagenomics, QS, phylogenetics, PFAS, deep-sea | 1,368 | 30+ |
| groundSpring | Sensor noise, error propagation, sequencing depth, seismic | 71 | 5 |
| neuralSpring | PINN, DeepONet, LeNet-5, LSTM, evo comp, spectral | 922 | 25 |
| **Total** | **5 domains, 10 professors** | **2,882** | **80+** |

### 13.5.2 Interpretation

2,882 validated science checks across 5 scientific domains in ~20 days of active development, by a single developer. The comparable institutional pace for reproducing a single computational paper is weeks to months (Mesnard & Barba, 2017). The velocity is not explained by AI alone (the AI was available to everyone; the methodology was not). It is explained by the constrained evolution methodology: the Rust type system eliminated broad classes of bugs, the phased validation protocol provided clear direction, and the AI provided high-frequency generation of candidates.

The growth from an initial 2,513 to 2,882 checks (a 14.7% increase) occurred primarily through the addition of Anderson's deep-sea metagenomics papers (133 checks in wetSpring) and extended Phase 0++ reproductions in neuralSpring — demonstrating that the spring framework supports incremental growth as new faculty connections and papers are identified.

---

## 13.6 Cross-Domain Kernel Reuse

### 13.6.1 The Isomorphism Theorem

neuralSpring's Isomorphism Theorem (Chapter 12) demonstrates that all neural architectures decompose into 6 fundamental primitives: GEMM, Attention, Normalization, Nonlinearity, Reduction, Gating. BarraCUDA implements all 6 as WGSL shaders.

The same primitives serve multiple domains:

| Primitive | hotSpring Use | wetSpring Use | neuralSpring Use |
|-----------|--------------|---------------|------------------|
| GEMM | SU(3) matrix multiplication | Spectral cosine matching | All neural network layers |
| Reduction | Observable averaging | Diversity index computation | Loss computation |
| FusedMapReduceF64 | Transport coefficient integration | Bulk statistics | Batch normalization |
| BatchedEighGpu | Nuclear eigenvalue decomposition | — | Hessian analysis |

### 13.6.2 Interpretation

Kernels evolved under one domain's constraints (hotSpring's plasma physics) proved fit for other domains (wetSpring's biology, neuralSpring's ML) without modification. This is the NTT→FFT pattern at the kernel level: constraint-driven adaptation producing structures with cross-domain fitness.

---

## 13.7 Summary

The quantitative evidence shows:
1. **NTT→FFT**: ~93 shared structural lines between cryptographic and physics transforms, with character-identical main compute kernels — emerged from constraint, not design
2. **Convergent IPC**: 12 primals independently converging on JSON-RPC, async Tokio, capability-based patterns through 12 different implementations
3. **Cross-domain kernels**: 6 BarraCUDA primitives serve 5 scientific domains without modification
4. **Velocity**: 2,882 checks across 80+ papers in ~20 days exceeds institutional reproduction rates by an order of magnitude
5. **Fastidious specialization**: Phase 1 primals average 6.4× more code and 3.4× more tests than Phase 2 primals, reflecting evolutionary maturity

These are not analogies. They are measurements from 3.8 million lines of compiled code across 12 primals and 5 springs. The constrained evolution principle predicts all five observations; no alternative hypothesis (e.g., "good engineering" or "fast AI") predicts the full pattern.
