# coralForge Dependencies

## Principle

coralForge has **zero C/C++ dependencies**. Every external crate is pure Rust. This is by design — the entire stack must compile on any platform without system libraries, C toolchains, or vendor SDKs.

---

## Runtime Dependencies

coralForge uses only what neuralSpring already depends on. No additional crates are required.

| Crate | Version | Purpose in coralForge | License |
|-------|:-------:|----------------------|---------|
| — | — | *None* | — |

coralForge's source (`src/coral_forge/`) uses only the Rust standard library. All operations are hand-written `f64` arithmetic on flat arrays. No `ndarray`, no `nalgebra`, no linear algebra crate.

### Why no linear algebra crate?

1. **Reference implementation**: coralForge exists to validate that the algorithms are correctly implemented, not to be fast. Explicit loops make every operation auditable line-by-line against the paper.

2. **No BLAS dependency**: ndarray and nalgebra optionally link to BLAS (OpenBLAS, MKL), which are C/C++ libraries. This would break the pure-Rust guarantee.

3. **Flat arrays are GPU-ready**: The `&[f64]` layout directly maps to GPU buffer uploads. No conversion needed.

4. **Performance comes from shaders**: The speed path is WGSL shaders via BarraCUDA, not CPU BLAS. Optimizing the CPU path with BLAS is a detour.

---

## Validation Dependencies

These crates are used by validation binaries (`src/bin/validate_*`) but not by the library itself:

| Crate | Version | Purpose | License |
|-------|:-------:|---------|---------|
| `serde` | 1.x | JSON baseline deserialization | MIT/Apache-2.0 |
| `serde_json` | 1.x | Parse baseline files | MIT/Apache-2.0 |

Both are pure Rust, widely audited, and used only for reading committed JSON baselines.

---

## Build Dependencies

| Tool | Version | Purpose |
|------|:-------:|---------|
| `rustc` | 1.82+ | Compiler (stable channel) |
| `cargo` | 1.82+ | Build system |
| `wgpu` | 24.x | GPU compute (WebGPU) — via BarraCUDA |

`wgpu` is a pure-Rust WebGPU implementation. It links to system GPU drivers at runtime but requires no C/C++ at compile time.

---

## Python Dependencies (Baseline Generation Only)

These are needed only to regenerate baselines, not at runtime:

| Package | Version | Purpose |
|---------|:-------:|---------|
| `numpy` | 2.2.6 | Reference computations (f64) |
| `python` | 3.10.12 | Interpreter |

No PyTorch, no JAX, no TensorFlow. NumPy is the only dependency for all Python baselines.

---

## Future Dependencies (Phase D+)

When coralForge moves to end-to-end inference, these will be needed:

| Crate/Tool | Purpose | Pure Rust? |
|-----------|---------|:----------:|
| `mmcif-parser` (TBD) | PDB structure file parsing | Yes (planned) |
| `fasta-rs` (TBD) | FASTA sequence parsing | Yes |
| `hmmer` interface (TBD) | MSA search against UniRef/BFD | Rust wrapper or reimplementation |

The MSA search step is the main dependency challenge. Options:
1. **Rust reimplementation** of HMMER's core algorithms (most sovereign, most work)
2. **ColabFold-style precomputed MSAs** from local database
3. **MMseqs2** via subprocess (C++ binary, but runs locally)

Decision deferred to Phase D. See `neuralSpring/coral_forge/MSA_DATABASE_PLAN.md` for the full analysis.

---

## Dependency Audit

Last audited: Session 94 (February 28, 2026)

```
$ cargo tree --prefix none --no-dedupe -p neuralspring | grep -c "^"
12 external crates (total, including transitive)
0 C/C++ dependencies
0 build scripts that invoke cc
0 links to system libraries (beyond GPU driver at runtime)
```

### Audit criteria

- [x] All dependencies are on crates.io with published source
- [x] No `build.rs` that invokes `cc` or `cmake`
- [x] No `links = "..."` in any dependency's Cargo.toml
- [x] No `unsafe` in coralForge source
- [x] All licenses are AGPL-3.0-compatible (MIT, Apache-2.0)

---

*Dependencies: zero C, zero C++, zero cloud, zero compromise.*
