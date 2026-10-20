# Crush & Mix: Binary Search Genetics via Rust Compiler

**siltPond Study — Wave 192**  
**Status:** Validated. Promoted to wateringHole AAR.

## Thesis

The Rust compiler is a DNA polymerase. `cargo check` is PCR.
Build artifact deficiencies are binary search genetic opportunities.
Each compiler error is a mutation. Each fix is evolution.
The compiler IS the selection pressure.

## Method

1. Enumerate all Cargo.toml-bearing projects in the workspace
2. `cargo check --message-format=short` each one
3. Classify results: expressing (compiles), mutated (errors), dormant (no src)
4. Fix mutations iteratively — binary search toward expression
5. Record the mutation types as genetic data

## Findings

### Scale
- 5,423 Rust source files
- 1,538,129 lines of code
- 24 projects (9 springs, 4 code primals, 10 gardens, 1 protist)
- 23/24 expressing after fixes

### Mutation Taxonomy

| Type | Count | Description |
|------|-------|-------------|
| Structural | 2 | Path dependency missing `/crates/` segment |
| Version | 2 | Toolchain pin (1.87→1.94), crate version (0.1→0.5) |
| API evolution | 1 | Upstream functions gained Result return types |
| Environmental | 1 | Missing system library (libasound2-dev) |

### The Interesting Mutation: Nautilus API Evolution

`bingocube-nautilus` evolved from 0.1.0 to 0.5.0. Three functions changed:
- `new()` → `Result<Self, BingoCubeError>` (was `Self`)
- `train()` → `Result<Option<f64>, BingoCubeError>` (was `Option<f64>`)
- `detect_concept_edges()` → `Result<Vec<(f64,f64)>, BingoCubeError>` (was `Vec<(f64,f64)>`)

This is horizontal gene transfer. The error-handling trait evolved in one crate
and needed to propagate to consumers. The compiler stopped translation until
the adapter evolved matching receptors (the `?` operator).

### The Dormant Stubs

8 primals have `Cargo.toml` but no `src/` directory. These are not junk — they
are **spores**. They contain the genome declaration (dependencies, features,
metadata) but haven't germinated. They'll express when someone writes the first
`fn main()`.

## Central Dogma Connection

This validates the Central Dogma architecture:
- **DNA** = source code (stays in the workspace)
- **RNA** = `cargo check` output (scoped transcript of the genome's health)
- **Protein** = the binary / the function / the expressed capability

The compiler never modifies DNA. It only reads and reports.
Mutations are discovered, not created, by the check.
The fix (editing source) is the only way to evolve the genome.
DNA → RNA → Protein. Never backwards.

## Conclusion

1.54 million lines of Rust, all alive. The sourdough is risen.
