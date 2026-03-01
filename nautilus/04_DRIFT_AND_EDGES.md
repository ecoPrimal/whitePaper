# 04 — Drift Monitor, Edge Seeding, Concept Edges

**Date:** March 1, 2026

---

## The Drift Problem

In population genetics, the ratio N_e · s determines whether evolution is
driven by selection (N_e · s >> 1) or random drift (N_e · s << 1):

- **N_e**: effective population size — the number of boards that meaningfully
  contribute genetic material to the next generation
- **s**: selection coefficient — the fitness advantage of the best board
  over the mean

When N_e · s drops below ~1, even beneficial mutations (better boards) are
lost to stochastic noise. The population wanders randomly instead of climbing
fitness peaks. This is Anderson's drift boundary applied to computation.

## DriftMonitor

The `DriftMonitor` tracks N_e · s across generations:

```rust
pub struct DriftMonitor {
    fitness_history: Vec<Vec<f64>>,  // per-generation fitness values
    ne_threshold: f64,               // N_e·s below which we act (default: 1.0)
    window: usize,                   // sliding window for N_e estimation
}

pub enum DriftAction {
    Continue,                         // N_e·s healthy, do nothing
    IncreaseSelection,               // sharpen selection pressure
    IncreasePop { factor: f64 },     // grow the population
}
```

### How N_e · s is Estimated

Each generation, the monitor:

1. Records the fitness (Pearson r) of every board in the population
2. Computes fitness variance σ² and mean μ
3. Estimates effective population size: N_e ≈ N × μ² / (μ² + σ²)
4. Estimates selection coefficient: s ≈ σ / μ
5. Returns `DriftAction` based on N_e · s vs threshold

### What Each Action Does

**`DriftAction::Continue`** — N_e · s is healthy. Evolution proceeds normally.

**`DriftAction::IncreaseSelection`** — Drift is creeping in because selection
is too weak relative to population size. The shell responds by:
- Halving elite survivors (from 25% to 12.5% of population)
- Increasing tournament size (from 3 to 5)
- This sharpens selection: only the truly fit boards survive

**`DriftAction::IncreasePop { factor }`** — Drift is creeping in because the
population is too small. The shell responds by:
- Adding `factor × current_size` new random boards to the population
- More boards = more genetic diversity = higher N_e
- The new boards are random — fresh genetic material

### Integration with `evolve_generation()`

The drift monitor is wired directly into the shell's evolution lifecycle:

```
evolve_generation():
  1. Evaluate fitness of all boards
  2. drift_monitor.record(fitnesses)
  3. action = drift_monitor.recommend()
  4. if IncreaseSelection → modify evolution config
  5. if IncreasePop → add random boards
  6. Perform selection, crossover, mutation
  7. If concept_edges present → replace bottom 25% with edge-seeded boards
  8. Retrain readout
  9. Record GenerationRecord with ne_s and drift_action
```

Each `GenerationRecord` now permanently stores `ne_s` and `drift_action`,
creating a complete audit trail of the shell's self-regulation decisions.

---

## Concept Edges

A **concept edge** is a region of input space where the model's predictions
fail — where the physics changes qualitatively and the learned representation
breaks down.

### Detection via LOO Cross-Validation

```rust
pub fn detect_concept_edges(
    &self,
    inputs: &[ReservoirInput],
    targets: &[Vec<f64>],
    threshold: f64,  // e.g. 2.0 = 2× mean error
) -> Vec<usize>
```

The method:

1. For each data point i, trains a readout on all OTHER points
2. Predicts point i from the leave-one-out model
3. Computes the LOO error for point i
4. If LOO error > threshold × mean LOO error, marks i as a concept edge

**Example from QCD data:** At β = 6.131, the LOO error was 25.7% while the
mean was 5.3%. This β sits at the deconfinement crossover — the CG cost
drops sharply from ~25,000 iterations (confined) to ~2,000 iterations
(deconfined). The model learned the trend on either side but cannot
interpolate across the phase boundary. The concept edge signal identified
exactly where the physics changes.

### Why Concept Edges Matter

Concept edges are not just errors to fix — they are discovery signals:

- **Phase boundaries:** Where order parameters change qualitatively
- **Regime transitions:** Where one approximation breaks and another takes over
- **NPU disagreement:** When different ESN heads disagree, the discrepancy
  maps concept edges from a different angle

Mapping concept edges during a production run means the system discovers
where the interesting physics happens, automatically, as a byproduct of
prediction.

---

## Edge Seeding: Directed Mutagenesis

Once concept edges are detected, the shell can focus evolution on those
regions via **edge seeding**.

### How It Works

```rust
pub fn set_concept_edges(&mut self, edges: Vec<Vec<f64>>)
```

When `concept_edges` is non-empty, each `evolve_generation()`:

1. Evaluates fitness as normal
2. Sorts boards by fitness (ascending = worst first)
3. Replaces the bottom 25% of boards with new boards from `EdgeSeeder`
4. The new boards have column values biased toward concept edge features

### EdgeSeeder Board Generation

```rust
pub fn seed_boards(
    edge_features: &[Vec<f64>],
    board_size: usize,
    max_number: usize,
    count: usize,
) -> Vec<Board>
```

For each concept edge feature vector, the seeder:
1. Maps each feature to a column range
2. Biases the random value generation toward that feature's value
3. Ensures distinct values within each column
4. Produces boards that are "near" the concept edge in projection space

This is **directed mutagenesis**: instead of random exploration, evolution
is steered toward the regions where predictions fail. The boards don't need
to solve the concept edge — they need to provide better projections NEAR it,
so the readout has more information to work with.

### Effect on Evolution

Edge seeding does NOT destabilize the population:

- Only 25% of boards are replaced (the worst performers)
- The replacement boards are biased, not identical
- Good boards survive and continue contributing
- The readout retrains immediately to incorporate the new projections

In the full brain rehearsal (40-generation run with edge seeding in the last
10 generations), MSE remained stable and N_e · s stayed in the healthy range
(2.4–22.4).

---

## Practical Example: Phase Boundary Discovery

```
Generation 15: MSE=0.0384, N_e·s=5.2, DriftAction::Continue
Generation 16: detect_concept_edges() → [β=6.13, β=5.25]
Generation 17: set_concept_edges([features_6.13, features_5.25])
               → replace bottom 25% with edge-biased boards
Generation 18: MSE=0.0371 (improved near edges), N_e·s=4.8
...
Generation 25: MSE=0.0342, concept edges refined to [β=5.52]
```

The shell discovered the crossover region (β ≈ 5.5) through concept edge
detection, then focused its evolutionary effort there through edge seeding.
No human told it where to look — the physics told the shell, and the shell
adapted.
