# Contributing to coralForge

coralForge lives inside `neuralSpring/src/coral_forge/` and follows the neuralSpring project conventions. This guide covers everything needed to add a primitive, evolve a shader, or extend the pipeline.

---

## Repository Layout

```
neuralSpring/
├── src/coral_forge/
│   ├── mod.rs              # Module root, re-exports public API
│   ├── activation.rs       # GELU, layer_norm, softmax
│   ├── attention.rs        # Scaled dot-product attention
│   ├── triangle.rs         # Triangle multiplication + attention
│   ├── msa.rs              # MSA row/column attention, OPM
│   ├── diffusion.rs        # Noise schedules, forward/reverse steps
│   ├── pairformer.rs       # Pairformer block + timestep conditioning
│   ├── confidence.rs       # pLDDT, PAE, pDE, ranking
│   └── structure/
│       ├── mod.rs           # Structure module root
│       ├── ipa.rs           # Invariant Point Attention
│       ├── backbone.rs      # Frame updates + torsion angles
│       └── frame.rs         # Quaternion/rotation/frame operations
├── control/coral_forge/     # Python baseline scripts
├── coral_forge/             # Specs, plans, requirements docs
├── metalForge/shaders/      # df64 WGSL shaders
└── src/bin/validate_*/      # Validation binaries
```

---

## Adding a New Primitive

### 1. Write the Python baseline first

```python
# control/coral_forge/my_new_primitive.py
import numpy as np
import json

np.random.seed(42)

def my_primitive(x, n, d):
    """Reference implementation using NumPy f64."""
    # ... algorithm from the paper ...
    return result

# Generate test cases
x = np.random.randn(8, 16).astype(np.float64)
result = my_primitive(x, 8, 16)

baselines = {
    "my_primitive_basic": {
        "input": x.flatten().tolist(),
        "n": 8, "d": 16,
        "expected": result.flatten().tolist()
    }
}

with open("control/coral_forge/my_primitive_baselines.json", "w") as f:
    json.dump(baselines, f, indent=2)
```

### 2. Implement in Rust

```rust
// src/coral_forge/my_primitive.rs

/// Brief description of what this does (cite the paper/algorithm number).
pub fn my_primitive(x: &[f64], n: usize, d: usize) -> Vec<f64> {
    assert_eq!(x.len(), n * d, "shape mismatch");
    // ... pure f64 implementation ...
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_my_primitive_basic() {
        // Small hand-verifiable case
        let x = vec![1.0, 2.0, 3.0, 4.0];
        let result = my_primitive(&x, 2, 2);
        assert!((result[0] - expected).abs() < 1e-12);
    }
}
```

### 3. Re-export from mod.rs

```rust
// src/coral_forge/mod.rs
mod my_primitive;
pub use my_primitive::my_primitive;
```

### 4. Add a validation binary

```rust
// src/bin/validate_coral_forge_my_primitive.rs
use neuralspring::coral_forge::my_primitive;
use neuralspring::validation::ValidationHarness;

fn main() {
    let h = ValidationHarness::new("coralForge my_primitive");
    let baselines: serde_json::Value = serde_json::from_str(
        include_str!("../../control/coral_forge/my_primitive_baselines.json")
    ).unwrap();

    let case = &baselines["my_primitive_basic"];
    let input: Vec<f64> = /* parse from baseline */;
    let expected: Vec<f64> = /* parse from baseline */;
    let result = my_primitive(&input, 8, 16);

    for (i, (&got, &exp)) in result.iter().zip(expected.iter()).enumerate() {
        require!(h, (got - exp).abs() < FOLDING_EPS,
            "my_primitive[{i}]: got {got}, expected {exp}");
    }

    h.finish();
}
```

### 5. Add provenance

```rust
// src/provenance.rs
pub const MY_PRIMITIVE_PROVENANCE: BaselineProvenance = BaselineProvenance {
    label: "coralForge my_primitive baselines",
    script: "control/coral_forge/my_new_primitive.py",
    commit: BASELINE_COMMIT,
    date: "2026-xx-xx",
    command: "python3 control/coral_forge/my_new_primitive.py",
    environment: "Python 3.10.12, NumPy 2.2.6, seed=42",
    value: 1.0,
    unit: "baselines generated",
};
```

### 6. Run quality gates

```bash
cargo fmt
cargo clippy --all-targets -- -D warnings -W clippy::pedantic
cargo test
cargo doc --no-deps 2>&1 | grep warning    # must be empty
bash control/validate_all.sh
```

All must pass before the primitive is considered complete.

---

## Design Rules

1. **Pure f64**: All arithmetic is `f64`. No `f32` at any point. This is the reference implementation.

2. **Flat arrays**: All tensors are `&[f64]` with explicit dimension parameters. No custom tensor types, no trait abstractions.

3. **No external ML frameworks**: No ndarray, no nalgebra, no tch-rs. Only `std` and the few pure-Rust crates in `Cargo.toml`.

4. **Cite the algorithm**: Every public function's doc comment cites the paper and algorithm number (e.g., "Algorithm 11, Jumper et al., 2021").

5. **Named tolerances**: Never write a bare `1e-10`. Use or create a named constant in `src/tolerances/mod.rs`. Name it for the domain: `FOLDING_EPS`, `DIFFUSION_NOISE_FLOOR`, etc.

6. **No `.expect()`**: Validation binaries use `require!(h, condition, message)` for graceful error recording instead of panicking.

7. **No `unsafe`**: Zero unsafe blocks in coralForge source.

8. **No mocks**: All tests use real computation, not mocked data paths.

---

## Evolving a df64 WGSL Shader

1. Start from the Rust f64 reference implementation
2. Translate to WGSL using the `df64` type (`vec2<f32>` representing high + low)
3. Verify max diff < 1e-6 against the Rust CPU output
4. Add to the GPU validation binary (`validate_coral_forge_gpu`)
5. Document the shader in `metalForge/shaders/` with a header comment

### df64 Conventions

```wgsl
// df64 = vec2<f32> where .x = high, .y = low
// Provides ~50 bits of mantissa precision on f32 cores

fn df64_add(a: vec2<f32>, b: vec2<f32>) -> vec2<f32> { ... }
fn df64_mul(a: vec2<f32>, b: vec2<f32>) -> vec2<f32> { ... }
fn df64_from_f32(x: f32) -> vec2<f32> { return vec2<f32>(x, 0.0); }
fn df64_to_f64(x: vec2<f32>) -> f32 { return x.x + x.y; }
```

---

## Commit Messages

Follow ecoPrimals convention:

```
neuralSpring S95: coralForge add [primitive] baseline + Rust + shader

- Python baseline: control/coral_forge/[primitive].py (N checks)
- Rust: src/coral_forge/[module].rs (M LOC)
- WGSL: metalForge/shaders/[primitive]_f64.wgsl
- Validation: validate_coral_forge_[stage] (P checks)
- Tolerance: [NEW_TOLERANCE_NAME] added to tolerances/mod.rs
```

---

## Pull Request Checklist

- [ ] Python baseline committed and drift-free
- [ ] Rust implementation with unit tests
- [ ] Validation binary using `require!` macro
- [ ] `BaselineProvenance` constant added
- [ ] Named tolerance for any new numerical threshold
- [ ] `cargo fmt` clean
- [ ] `cargo clippy --all-targets -- -D warnings -W clippy::pedantic` clean
- [ ] `cargo doc --no-deps` warning-free
- [ ] `cargo test` passes
- [ ] `validate_all.sh` passes (185/185+)
- [ ] No `unsafe`, no `.expect()` in validation, no inline magic numbers
- [ ] Updated `CHANGELOG.md` with session entry

---

*Contributing: correctness is not negotiable, clarity is not optional.*
