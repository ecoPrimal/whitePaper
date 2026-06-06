# tideGlass — WGSL Shader Requirements for barraCuda

**Date**: June 6, 2026
**Status**: Draft — pending Phase 1 (Reproduce) data for workload sizing
**Target**: barraCuda primal (via `compute.dispatch` IPC from NUCLEUS)

---

## Design Principle

Following the ecosystem pattern: shaders start in spring experiments,
prove their value, then consolidate into `barraCuda/shaders/`. All GPU
dispatch goes through `toadStool` streaming and `metalForge` multi-device
routing. Springs never touch hardware directly.

**Existing precedent** (healthSpring → barraCuda):

| Shader | Origin | Workload |
|--------|--------|----------|
| `hill_dose_response_f64.wgsl` | healthSpring Exp001 | IC50 fitting across compound panels |
| `population_pk_f64.wgsl` | healthSpring Exp089 | 100K virtual patient Monte Carlo |
| `diversity_distance_f32.wgsl` | healthSpring Exp085 | Pairwise molecular diversity scoring |
| `michaelis_menten_f64.wgsl` | healthSpring Exp087 | Enzyme kinetics batch fitting |
| `scfa_production_f64.wgsl` | healthSpring Exp088 | Gut SCFA batch estimation |
| `beat_classification_f32.wgsl` | healthSpring Exp094 | Cardiac rhythm classification |

tideGlass adds **3 new shaders** to this fleet.

---

## Shader 1: `rges_batch_score_f64.wgsl`

**Module**: tideglass-rges, tideglass-screen
**Purpose**: Compute Reversal Gene Expression Score (RGES) for batch compound-disease pairs

### The Computation

RGES is a modified Kolmogorov-Smirnov statistic applied per compound:

```
For each compound c and disease signature d:
  1. Rank genes by compound-induced expression change
  2. Compute KS enrichment for UP-regulated disease genes (ES_up)
  3. Compute KS enrichment for DOWN-regulated disease genes (ES_down)
  4. RGES(c, d) = (ES_up - ES_down) / 2
  5. Normalize: summarize RGES → sRGES across cell lines
```

### Why GPU

- **Batch size**: ZINC library = 750M+ compounds. Screening even a 1M subset
  against 1 disease signature = 1M independent KS computations.
- **Embarrassingly parallel**: Each (compound, disease) pair is independent.
- **Memory pattern**: Rank vectors are read-only after sort. Disease gene sets
  are small (~100-500 genes). Perfect for GPU shared memory.
- **Existing analogy**: `population_pk_f64.wgsl` does 100K independent Monte
  Carlo simulations per dispatch — same parallelism pattern.

### Shader Interface

```wgsl
struct RgesInput {
    expression_ranks: array<f64>,    // pre-sorted compound expression changes
    up_gene_indices: array<u32>,     // indices of disease UP genes in rank
    down_gene_indices: array<u32>,   // indices of disease DOWN genes in rank
    n_genes: u32,                    // total gene count (978 for L1000)
    n_up: u32,
    n_down: u32,
}

struct RgesOutput {
    rges: f64,                       // raw RGES
    es_up: f64,
    es_down: f64,
    p_value: f64,                    // permutation-derived
}

@compute @workgroup_size(256, 1, 1)
fn rges_batch_score(
    @builtin(global_invocation_id) gid: vec3<u32>,
) {
    // One thread per compound-disease pair
    // Reads from pre-sorted rank buffer
    // Writes RGES + components to output buffer
}
```

### Estimated Performance

| Configuration | CPU (Rust) | GPU (single Titan V) | Speedup |
|---------------|-----------|---------------------|---------|
| 1K compounds | ~50ms | ~0.1ms | 500x |
| 100K compounds | ~5s | ~10ms | 500x |
| 1M compounds | ~50s | ~100ms | 500x |
| 750M (full ZINC) | ~10hr | ~75s | ~500x |

Bottleneck shifts to data I/O at full ZINC scale; `toadStool` streaming
handles this by dispatching in chunks while fetching next batch.

---

## Shader 2: `mcts_tree_eval_f32.wgsl`

**Module**: tideglass-molsearch
**Purpose**: Batch-evaluate MCTS leaf nodes in chemical space optimization

### The Computation

MolSearch uses MCTS to explore chemical transformations:

```
For each leaf node (candidate molecule) in the MCTS tree:
  1. Compute molecular features (fingerprint similarity to target)
  2. Predict expression change (from pre-trained GPS4Drug embedding)
  3. Score reversal quality (RGES against disease signature)
  4. Score drug-likeness (Lipinski/Veber rules)
  5. Compute multi-objective reward = f(reversal, druglikeness, selectivity)
  6. Backpropagate value up tree
```

### Why GPU

- **Expansion width**: MCTS expands 100-1000 children per node per iteration.
  Each child evaluation is independent at the leaf level.
- **Iterations**: 10K-100K MCTS iterations typical. Each iteration evaluates
  multiple leaf nodes.
- **Memory pattern**: Tree structure lives on CPU. Leaf evaluation (scoring)
  offloads to GPU. Results backpropagate on CPU.
- **Existing analogy**: `diversity_distance_f32.wgsl` computes pairwise
  molecular distances — same "N molecules, score each independently" pattern.

### Shader Interface

```wgsl
struct MoleculeFeatures {
    fingerprint: array<u32, 64>,     // 2048-bit Morgan FP as 64x u32
    mw: f32,                         // molecular weight
    logp: f32,                       // computed logP
    hbd: u32,                        // H-bond donors
    hba: u32,                        // H-bond acceptors
    tpsa: f32,                       // topological polar surface area
    rotatable_bonds: u32,
}

struct EvalInput {
    candidate: MoleculeFeatures,
    target_signature: array<f32>,    // disease expression signature (978 genes)
    gps4drug_embedding: array<f32>,  // pre-computed embedding from GPS4Drug
}

struct EvalOutput {
    reversal_score: f32,
    druglikeness: f32,
    selectivity: f32,
    composite_reward: f32,
    violations: u32,                 // Lipinski violation count
}

@compute @workgroup_size(128, 1, 1)
fn mcts_tree_eval(
    @builtin(global_invocation_id) gid: vec3<u32>,
) {
    // One thread per leaf node
    // Reads molecule features + disease signature
    // Writes multi-objective reward to output buffer
}
```

### Estimated Performance

| Configuration | CPU (Rust) | GPU (single Titan V) | Speedup |
|---------------|-----------|---------------------|---------|
| 1K leaves | ~10ms | ~0.05ms | 200x |
| 100K leaves | ~1s | ~5ms | 200x |
| Per MCTS iteration (1K expand) | ~10ms | ~0.05ms | 200x |
| Full search (100K iterations) | ~16min | ~5s | ~200x |

Lower speedup than RGES because evaluation is more complex per element
(multiple scoring functions, conditional logic). Still critical at scale.

---

## Shader 3: `population_screen_f64.wgsl`

**Module**: tideglass-screen, tideglass-nf
**Purpose**: Screen compound library against multiple disease signatures simultaneously

### The Computation

Population screening combines RGES with tissue-specific context:

```
For each compound c, for each tissue t, for each disease d:
  1. Retrieve tissue geometry (Anderson d_eff for tissue t)
  2. Compute tissue-weighted RGES: tw_RGES(c, t, d) = RGES(c, d) * geo(t)
  3. Apply selectivity filter: SI(c, t) = tw_RGES(target) / mean(tw_RGES(off-target))
  4. Score compound: final_score(c) = tw_RGES * SI * druglikeness
  5. Rank and threshold
```

### Why GPU

- **Three-dimensional parallelism**: compounds x tissues x diseases.
  10K compounds x 5 tissues x 3 disease signatures = 150K independent scores.
- **Memory pattern**: Geometry factors are small constants per tissue.
  RGES values precomputed (from Shader 1). Selectivity is reduction.
- **Existing analogy**: Direct extension of healthSpring's `score_panel()`
  with `TissueContext`. The Anderson geometry scaling is already validated.

### Shader Interface

```wgsl
struct TissueContext {
    d_eff: f64,                      // Anderson effective dimension
    propagation_factor: f64,         // derived from d_eff
    name_hash: u32,                  // tissue identifier
}

struct ScreenInput {
    rges_values: array<f64>,         // pre-computed RGES per compound (from Shader 1)
    tissue_contexts: array<TissueContext>,
    selectivity_targets: array<u32>, // which tissues are "on-target"
    n_compounds: u32,
    n_tissues: u32,
    n_diseases: u32,
}

struct ScreenOutput {
    tissue_weighted_rges: f64,
    selectivity_index: f64,
    composite_score: f64,
    rank: u32,
}

@compute @workgroup_size(256, 1, 1)
fn population_screen(
    @builtin(global_invocation_id) gid: vec3<u32>,
) {
    // One thread per (compound, tissue) pair
    // Reads pre-computed RGES + tissue geometry
    // Writes tissue-weighted score + selectivity to output
}
```

### Estimated Performance

| Configuration | CPU (Rust) | GPU (single Titan V) | Speedup |
|---------------|-----------|---------------------|---------|
| 10K compounds x 5 tissues | ~100ms | ~0.2ms | 500x |
| 100K x 5 tissues | ~1s | ~2ms | 500x |
| 1M x 5 tissues x 3 diseases | ~15s | ~30ms | 500x |

Highest speedup because the operation per element is simple arithmetic
(multiply, divide, compare) — ideal GPU territory.

---

## Dispatch Architecture

```
                          NUCLEUS
                            │
                    ┌───────┼───────┐
                    │               │
             compute.dispatch    toadStool
                    │           (streaming)
                    │               │
            ┌───────┼───────┐      │
            │       │       │      │
         Titan V  Titan V  MI50   MI50   RTX 5060
           │       │       │      │        │
        Shader1  Shader1  Shader2 Shader2  Shader3
        (RGES)   (RGES)   (MCTS) (MCTS)   (Screen)
```

**Multi-GPU strategy** (via `metalForge`):
- **RGES batch scoring**: Data-parallel across Titan V pair (large compound lists split)
- **MCTS evaluation**: Data-parallel across MI50 pair (different tree branches)
- **Population screening**: Single GPU sufficient (small workload after RGES)
- **Training** (PyTorch): Uses MI50 pair or RTX 5060 via standard CUDA/ROCm

### Dispatch TOML (extends existing workload pattern)

```toml
[workload.rges_batch]
shader = "rges_batch_score_f64.wgsl"
dispatch_mode = "streaming"
chunk_size = 65536
devices = ["titan_v_0", "titan_v_1"]
input_format = "ranked_expression"
output_format = "rges_scores"

[workload.mcts_eval]
shader = "mcts_tree_eval_f32.wgsl"
dispatch_mode = "on_demand"
chunk_size = 1024
devices = ["mi50_0", "mi50_1"]
input_format = "molecule_features"
output_format = "mcts_rewards"

[workload.population_screen]
shader = "population_screen_f64.wgsl"
dispatch_mode = "batch"
chunk_size = 262144
devices = ["rtx_5060"]
input_format = "rges_tissue_matrix"
output_format = "ranked_candidates"
```

---

## Shader Evolution Timeline

| Phase | Shader State | Validation |
|-------|-------------|-----------|
| Phase 0-1 | No shaders. Python reproduces GPS claims. | Tier 1 notebook |
| Phase 2 | RGES scoring in Rust (CPU). Validate against Python. | Tier 2 parity |
| Phase 3 | `rges_batch_score_f64.wgsl` deployed. GPU vs CPU parity. | Cross-tier (litho parity) |
| Phase 3+ | `mcts_tree_eval_f32.wgsl` deployed. | Cross-tier |
| Phase 4 | `population_screen_f64.wgsl` deployed. Full NUCLEUS dispatch. | Integration |
| Late | All 3 shaders consolidated in `barraCuda/shaders/tideglass/` | Shader fleet test |

Each phase emits a `pseudoSpore` with provenance of which computation path was used.

---

## Parity Requirements

Every shader MUST maintain cross-tier numerical parity:

| Tier | Implementation | Tolerance |
|------|---------------|-----------|
| Tier 1 (Python) | `scipy.stats.ks_2samp` / custom RGES | Reference |
| Tier 2 (Rust) | `tideglass-rges` binary | < 1e-10 absolute error |
| Tier 3 (WGSL f64) | `rges_batch_score_f64.wgsl` | < 1e-10 absolute error |
| Tier 3 (WGSL f32) | `mcts_tree_eval_f32.wgsl` | < 1e-5 absolute error (f32 limits) |

`litho parity` validates this automatically. Any tier mismatch fails the spore.

---

## Cross-References

- `gonzales/gps/VIABILITY.md` — why these shaders are viable
- `gonzales/gps/scope.toml` — module → shader mapping
- `healthSpring/ecoPrimal/shaders/` — existing shader fleet
- `healthSpring/ecoPrimal/src/discovery/matrix_score.rs` — pattern for RGES
- `barraCuda` primal documentation — dispatch API
- `toadStool` streaming — chunk-based large workloads
- `metalForge` multi-device — hardware routing

---

*Three shaders. 750M compounds scored in 75 seconds. The GPU fleet exists,
the dispatch infrastructure exists, the parity validation exists. What's new
is the science that runs on it — and that's exactly what should be new.*
