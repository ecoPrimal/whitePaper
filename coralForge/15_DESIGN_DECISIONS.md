# coralForge Design Decisions

Every significant architectural choice in coralForge was made deliberately. This document records what was decided, why, and what was rejected.

---

## DD-01: Pure f64 Arithmetic

**Decision**: All computations use Rust `f64`. No `f32` anywhere in the reference implementation.

**Why**: coralForge is a *validation* implementation. Its purpose is to prove the algorithms are correctly understood and implemented. Precision eliminates an entire class of debugging — you never have to wonder if a test failure is a precision issue or a real bug.

**Rejected alternative**: Mixed precision (f32 for speed, f64 for sensitive operations). This makes debugging harder: "is this a precision bug or an algorithm bug?" becomes a constant question.

**Future**: Phase D+ may add an f32 inference mode for speed. The f64 path remains as the ground-truth reference.

---

## DD-02: Flat Row-Major Arrays

**Decision**: All tensors are `&[f64]` slices with explicit dimension parameters. Row-major layout.

**Why**:
1. **GPU compatibility**: Flat arrays map directly to GPU buffer uploads with zero conversion
2. **Transparency**: Indexing is explicit — `x[i * cols + j]` — making it trivial to verify against paper pseudocode
3. **No framework dependency**: No ndarray, no nalgebra, no custom tensor type
4. **Cache-friendly**: Row-major matches Rust's default memory layout and is optimal for row-wise operations (softmax, layer norm)

**Rejected alternative**: ndarray (`Array2<f64>`, `Array4<f64>`). Adds a dependency, hides indexing behind traits, and complicates the BLAS-free guarantee. Would also require `.as_slice()` conversions for GPU upload.

**Trade-off**: Manual shape checking (`assert_eq!(x.len(), n * d)`) instead of compile-time guarantees. Acceptable for a reference implementation where clarity > safety.

---

## DD-03: No Trait Abstractions

**Decision**: coralForge uses no traits, no generics over numeric types, no operator overloading. Every function takes concrete `f64` slices.

**Why**: This is a *reference* implementation meant to be read alongside the paper. A reader should be able to open `triangle.rs` and compare line-by-line with Algorithm 11 in the AlphaFold2 supplement. Generics and traits add indirection that breaks this direct correspondence.

**Rejected alternative**: `trait Tensor<T: Float>` with blanket impls for f32/f64. This is the right choice for a *production* library, not a *reference* implementation.

**Future**: Phase F (open release) may introduce a `Float` trait for f32/f64 generic support. The f64 concrete implementations become the trait's test suite.

---

## DD-04: Separate Python Baselines

**Decision**: Every Rust primitive has a corresponding Python NumPy script that generates expected outputs. These baselines are committed as JSON.

**Why**:
1. **Cross-language validation**: If two independent implementations (Python and Rust) agree, the algorithm is almost certainly correct
2. **Deterministic**: Fixed seed (42), pinned NumPy version (2.2.6)
3. **Auditable**: Anyone can re-run the Python script and verify the JSON
4. **No PyTorch/JAX**: NumPy is the simplest possible reference, with no hidden framework optimizations

**Rejected alternative**: Using PyTorch or OpenFold as the baseline. These have their own bugs, framework-specific numerics (fused kernels, TF32 by default on NVIDIA), and massive dependencies. NumPy is the closest thing to "the paper implemented directly."

**Trade-off**: Writing baselines twice (Python and Rust) is effort. But the cross-language validation has already caught 3 real bugs that unit tests missed.

---

## DD-05: ValidationHarness + `require!`

**Decision**: Validation binaries use a custom `ValidationHarness` with `require!` macro instead of Rust's built-in `assert!` or `#[test]`.

**Why**: A single validation run should report *all* failures, not crash at the first one. This is critical for a 55-check validation binary — you want to see the full picture, not play whack-a-mole.

**How**: `require!(h, condition, message)` records a failure in the harness and continues. `h.finish()` prints a summary and exits with code 0 (all pass) or 1 (any failures).

**Rejected alternative**: `#[test]` functions with `assert!`. These abort at the first failure and require `cargo test` infrastructure. Standalone binaries are simpler, faster, and produce cleaner output for CI.

---

## DD-06: Named Tolerances

**Decision**: Every numerical comparison uses a named constant from `src/tolerances/mod.rs`. No bare floating-point literals in comparisons.

**Why**:
1. **Traceability**: When a test uses `FOLDING_EPS`, you know exactly what tolerance it expects and can search for all uses
2. **Central management**: Changing a tolerance requires changing one constant, not grep-and-replace across binaries
3. **Domain documentation**: `FISHER_EPS` tells you this tolerance is about Fisher information; `1e-12` tells you nothing

**Rejected alternative**: Inline `1e-10` everywhere. This was the original approach in Sessions 40–84. Eliminating inline magic numbers was a key deep-debt resolution in Sessions 92–94.

---

## DD-07: df64 WGSL Shaders

**Decision**: GPU shaders use df64 (double-float emulation via pairs of f32) in WGSL, not native f64 or f32.

**Why**:
1. **Consumer GPU support**: Most consumer GPUs (RTX 4070, etc.) have 1/64 rate for native f64. df64 on f32 cores is 30–50× faster than native f64 on the same hardware.
2. **Precision**: df64 provides ~50 bits of mantissa, which is sufficient for structure prediction (max diff < 1e-6 vs CPU f64).
3. **Cross-platform**: WGSL + wgpu runs on NVIDIA, AMD, Intel, and Apple Silicon. No CUDA lock-in.
4. **Sovereign**: No proprietary SDK needed. wgpu is pure Rust.

**Rejected alternatives**:
- **Native f64 on GPU**: Too slow on consumer hardware (1/64 throughput on NVIDIA, unsupported on many AMD GPUs)
- **f32 directly**: Insufficient precision for IPA point distances and diffusion noise schedules. Would require extensive numerical analysis to prove correctness.
- **CUDA**: Proprietary, NVIDIA-only, requires nvcc toolchain. Antithetical to sovereign computing.

**Trade-off**: df64 operations cost 2× the register pressure and ~4× the ALU operations of f32. This is acceptable because the alternative (native f64 at 1/64 rate) is far worse.

---

## DD-08: coralForge as a Module, Not a Crate

**Decision**: coralForge lives as `src/coral_forge/` inside neuralSpring, not as a separate crate.

**Why**:
1. **Shared infrastructure**: Uses neuralSpring's `ValidationHarness`, `require!` macro, tolerances, and provenance system
2. **Co-evolution**: coralForge primitives validate the same 6-primitive isomorphism thesis that neuralSpring's other modules demonstrate
3. **Single build**: One `cargo build`, one `cargo test`, one `validate_all.sh` for the entire project
4. **ToadStool integration**: BarraCUDA imports from neuralSpring; a separate crate would add dependency management overhead

**Future**: Phase F (open release) extracts coralForge into its own crate. The module boundaries are already clean — `mod.rs` re-exports everything, and the module has no dependencies on other neuralSpring modules except `tolerances` and `provenance`.

---

## DD-09: AlphaFold2 Before AlphaFold3

**Decision**: Implement AlphaFold2 primitives first (Phase A), then add AlphaFold3 extensions (Phase B).

**Why**:
1. **Incremental validation**: AF2 has more reference implementations (OpenFold, ColabFold) to validate against
2. **Shared primitives**: ~60% of AF2 primitives are reused in AF3 (attention, triangle ops, layer norm)
3. **Published weights**: AF2 model weights are publicly available; AF3 weights are not (as of Feb 2026)
4. **Thesis connection**: The isomorphism theorem demonstration works with AF2 alone. AF3 strengthens it but isn't required.

**Rejected alternative**: Jump straight to AF3. Higher risk — less reference material, no public weights, and the diffusion framework adds complexity before the basics are validated.

---

## DD-10: Explicit Dimension Parameters

**Decision**: Every function takes explicit `n`, `d`, `heads`, `head_dim` etc. as separate `usize` parameters alongside the flat array.

**Why**:
1. **Self-documenting**: Function signatures tell you exactly what shape the input should be
2. **No hidden state**: No global configuration, no builder pattern, no struct with fields you have to set before calling
3. **Paper correspondence**: AlphaFold's pseudocode uses explicit dimensions (N_res, N_seq, c_m, etc.) — our function signatures mirror this

**Rejected alternative**: A `TensorView` struct that wraps `&[f64]` with shape metadata. This is cleaner but adds indirection and doesn't match the paper's pseudocode style.

**Exception**: `IpaConfig` and `PairformerWeights` bundle parameters into structs because these functions take 8-15 parameters. The threshold is ~6 parameters — below that, explicit arguments; above that, a config struct.

---

## DD-11: No Unsafe Code

**Decision**: Zero `unsafe` blocks in coralForge. No raw pointer arithmetic, no `transmute`, no `get_unchecked`.

**Why**: For a reference implementation, correctness is infinitely more important than performance. Bounds-checked indexing catches bugs. The performance cost is negligible relative to the O(N²) algorithmic cost.

**Future**: Phase C (BarraCUDA integration) may introduce `unsafe` in hot loops through the BarraCUDA crate. The coralForge *source* remains safe; the `unsafe` lives in the shared acceleration layer.

---

## DD-12: Committed JSON Baselines

**Decision**: Python baseline outputs are committed as JSON files in `control/coral_forge/`. They are not regenerated during CI.

**Why**:
1. **Reproducibility**: The JSON is the source of truth. If NumPy changes behavior, the drift check catches it.
2. **Offline validation**: Rust validation runs without Python installed. The JSON is included via `include_str!`.
3. **Auditability**: Anyone can inspect the expected values directly in the repository.
4. **Determinism**: The committed JSON captures a specific NumPy version + seed + platform result.

**Rejected alternative**: Regenerate baselines in CI. This makes CI dependent on Python, introduces nondeterminism (different NumPy versions), and masks drift.

---

*Decisions: every choice is a trade-off. Document both sides.*
