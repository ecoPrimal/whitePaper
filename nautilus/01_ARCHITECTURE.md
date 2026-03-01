# 01 — Nautilus Shell Architecture

**Date:** March 1, 2026

---

## Core Concept: Boards as Reservoirs

A BingoCube board is a structured random projection matrix. For an L×L board:

- Column k draws values from [k·R, (k+1)·R) where R = ⌈N/L⌉
- All values within a column are distinct
- The combinatorial space is vast: ~10³¹ (L=5), ~10⁸⁴ (L=8), ~10¹⁹⁰ (L=12)

When a data stream flows through the boards (replacing the bingo caller),
each board produces a **response vector** — a deterministic nonlinear
projection of the input into a high-dimensional space. A population of P
boards produces a P × L² dimensional representation.

The readout is a simple linear regression (ridge / Cholesky) from this
high-dimensional space to the target observable. The boards are the reservoir;
the readout is the decoder.

## Evolution as Time

Traditional ESNs use temporal recurrence for memory:

```
state(t) = f(W_in · input(t) + W · state(t-1))
```

The Nautilus Shell replaces temporal recurrence with evolutionary generations:

```
population(g) = evolve(select(population(g-1), fitness(g-1)))
```

What recurrence encodes in hidden state, evolution encodes in population
structure. The key insight: for feed-forward hardware (AKD1000), this is not
a limitation — it is the only viable path. The constraint (no recurrence)
forced the architecture (evolution as time).

### What Evolution Preserves

Each generation preserves:

- **Column values** that correlate with good predictions (via crossover)
- **Structural motifs** that produce useful projections (via selection)
- **Population diversity** to avoid premature convergence (via mutation)

### What Evolution Discards

- Boards with poor fitness (high prediction error)
- Structural patterns that don't generalize across inputs
- Redundant representations (boards that duplicate another's projection)

## The Shell: Layered Evolutionary History

```
Shell = [Generation 0, Generation 1, ..., Generation G]
```

Each `GenerationRecord` contains:

| Field | Type | Purpose |
|-------|------|---------|
| `generation` | usize | Generation number |
| `best_fitness` | f64 | Best Pearson r in this generation |
| `mean_fitness` | f64 | Population average |
| `population_size` | usize | How many boards competed |
| `board_checksums` | Vec<u64> | Fingerprints of surviving boards |
| `mse` | f64 | Mean squared error of readout |
| `ne_s` | f64 | Effective population × selection coefficient |
| `drift_action` | DriftAction | What the drift monitor recommended |

The shell is:

- **Serializable**: full state to JSON (~23 KB for 16 boards, 20 gens)
- **Transferable**: `shell_a.continue_from(shell_b)` inherits population + history
- **Mergeable**: `shell_a.merge_shell(shell_b)` combines two shells, taking
  the fitter population and concatenating histories

### Within an Instance

A single Nautilus Shell instance evolves through generations, building up its
shell layer by layer. Each generation wraps the previous — you can read the
full history by unwinding the layers. The shell records not just what survived,
but why (fitness, drift state, population size).

### Between Instances

Two shells can interact:

- **Transfer**: Shell B starts where Shell A left off. B inherits A's
  population and evolutionary state, then continues evolving in a new
  environment. Like a culture transferred to a new medium.

- **Merge**: Two shells that evolved independently combine their knowledge.
  The fitter population is kept; both histories are preserved. Like
  horizontal gene transfer — external genetic material enters the population.

## Key Types

```rust
pub struct NautilusShell {
    config: ShellConfig,           // Board dimensions, population, targets
    current_population: Population, // The living boards
    readout: LinearReadout,         // Ridge regression decoder
    history: Vec<GenerationRecord>, // The shell — full evolutionary record
    instance_id: InstanceId,        // Unique identity (UUID + creation time)
    parent_id: Option<InstanceId>,  // Lineage tracking
    drift_monitor: DriftMonitor,    // N_e · s tracker
    concept_edges: Vec<Vec<f64>>,   // Detected prediction failure regions
}

pub struct ShellConfig {
    pub board_size: usize,          // L (typically 5)
    pub max_number: usize,          // N (typically 75)
    pub population_size: usize,     // P (typically 16-32)
    pub n_targets: usize,           // Output dimensions (e.g. 2: plaquette + CG)
}
```

## Lifecycle

```
1. new(config)           → empty shell, random population
2. train(inputs, targets) → fit readout via ridge regression
3. evolve_generation()   → one generation of selection + crossover + mutation
4. predict(input)        → readout from current population's response
5. save_state() / restore_state() → full serialization
6. continue_from(other)  → inherit another shell's learned state
7. merge_shell(other)    → combine two shells
```

Steps 2-3 repeat for as many generations as needed. The shell grows with
each `evolve_generation()` call. The readout is retrained after each
evolution step to reflect the new population.

## Computational Cost

| Operation | Cost | Notes |
|-----------|------|-------|
| Board response (P=16, L=5) | ~800 column lookups | O(P × L²) |
| Readout train (ridge) | ~0.1 ms | Cholesky on 400×400 |
| Evolution (1 generation) | ~0.5 ms | Selection + crossover + mutation |
| Full 40-generation run | ~25 ms | Includes readout retraining |
| Serialization | ~1 ms | JSON, ~23 KB |

The entire Nautilus Shell lifecycle — from random boards to trained predictor —
runs in tens of milliseconds on CPU. This is not a training bottleneck. The
bottleneck is generating the physics data to train on.
