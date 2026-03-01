# 06 — Validation: Tests, Predictions, State Persistence

**Date:** March 1, 2026

---

## Unit Tests (31 passing)

### Core Functionality (20 original)

| Test | What it validates |
|------|-------------------|
| `test_shell_creation` | NautilusShell initializes with correct dimensions |
| `test_board_response` | Boards produce deterministic response vectors |
| `test_population_fitness` | Pearson correlation fitness is computed correctly |
| `test_evolution_one_gen` | One generation of evolution preserves population size |
| `test_readout_training` | Ridge regression readout trains and predicts |
| `test_shell_history` | History grows with each generation |
| `test_save_restore` | JSON serialization round-trips perfectly |
| `test_instance_transfer` | `continue_from` inherits population and history |
| `test_shell_merge` | `merge_shell` combines two shells correctly |
| `test_crossover` | Column-swap crossover preserves column-range constraints |
| `test_mutation` | Mutation stays within column ranges |
| `test_selection_elitism` | Elitism keeps top k boards |
| `test_selection_tournament` | Tournament selection with configurable size |
| `test_ridge_regression` | Cholesky solver matches expected output |
| `test_response_dimensions` | Response vector has correct shape |
| `test_multi_target` | Multiple target outputs train and predict |
| `test_large_population` | 64-board populations work correctly |
| `test_instance_id` | UUID generation and lineage tracking |
| `test_empty_evolve` | Edge case: evolving with no training data |
| `test_config_validation` | Invalid configs rejected cleanly |

### New Tests (11 added)

| Test | What it validates |
|------|-------------------|
| `test_drift_monitor_wired_into_evolution` | `evolve_generation()` records ne_s and drift_action |
| `test_edge_seeding_integration` | `set_concept_edges` + evolution performs edge seeding |
| `test_akd1000_export` | Int4 quantization in [-8,7], correct dimensions, low MSE |
| `test_concept_edge_detection` | LOO CV identifies high-error samples as concept edges |
| `test_drift_action_serialization` | DriftAction round-trips through serde |
| `test_drift_monitor_increase_selection` | Monitor recommends IncreaseSelection when N_e·s low |
| `test_drift_monitor_increase_pop` | Monitor recommends IncreasePop when population small |
| `test_edge_seeder_boards` | EdgeSeeder produces valid boards biased toward features |
| `test_concept_edges_with_discontinuity` | Synthetic step function → edges detected at step |
| `test_akd1000_predict_dequantized` | Quantized prediction matches full precision within tolerance |
| `test_akd1000_serialization` | Akd1000Export round-trips through JSON |

## Examples (5)

### 1. `shell_lifecycle` — Basic demonstration

Creates a shell, generates synthetic data, trains, evolves 20 generations,
saves/restores state, transfers to a second instance, merges.

### 2. `qcd_quenched_transfer` — 540× cost reduction

Trains on quenched QCD features (cheap to generate: ~2s/config), then
predicts dynamical CG cost (expensive: ~1,080s/config) without ever seeing
dynamical data. LOO error: 4.4%. Cost reduction: 540×.

### 3. `predict_live_exp029` — Blind prediction on live data

Loads Exp 029 production data that the shell has never seen. Predicts CG cost
and plaquette for each beta point. Blind CG error: 2.6%.

### 4. `full_brain_rehearsal` — End-to-end pipeline validation

8 phases validating the complete pipeline:

| Phase | Duration | What |
|-------|----------|------|
| Bootstrap | ~5 ms | Generate synthetic QCD phase transition data |
| Drift evolution | ~15 ms | 15 generations, N_e·s stable 2.4–22.4 |
| Concept edges | ~3 ms | LOO CV identifies 4 edges at phase boundary |
| Edge-seeded evolution | ~10 ms | 10 more generations with directed mutagenesis |
| AKD1000 export | ~1 ms | Int4 quantization, MSE=0.004, spot checks |
| Save/restore | ~2 ms | Bit-perfect prediction match (delta < 10⁻¹⁶) |
| Transfer/merge | ~5 ms | 2 instances, 30 combined history entries |
| Production reset | ~1 ms | Clear edges, save production-ready state |

### 5. `multi_stream_prediction` — Multiple data streams

Demonstrates the shell handling multiple simultaneous data streams (simulating
multi-beta-point production) with independent readouts.

## Live Experiment Results

### Exp 024+028: Training Data

| Source | Beta Points | Trajectories | Features |
|--------|-------------|--------------|----------|
| Exp 024 | 17 | 1,071 | Plaquette, Polyakov, CG iters |
| Exp 028 | 8 | 760 | Same + brain weights |
| Combined | 21 unique β | 1,831 | Aggregated per β |

### LOO Cross-Validation Results

| Beta | Plaquette Error | CG Error | Notes |
|------|-----------------|----------|-------|
| 4.5 | 0.8% | 1.2% | Deep confined |
| 5.0 | 1.1% | 3.4% | Approaching transition |
| 5.25 | 2.3% | 4.7% | Transition region |
| 5.5 | 3.1% | 6.8% | Near crossover |
| 5.69 | 1.9% | 3.2% | At β_c (quenched) |
| 6.0 | 0.7% | 2.1% | Deconfined |
| 6.131 | 8.2% | 25.7% | **Concept edge** — phase boundary |
| Mean | 2.1% | 5.3% | |

The outlier at β=6.131 is a genuine concept edge where CG cost drops
sharply from ~25,000 to ~2,000 iterations.

### Exp 029: Blind Prediction

Shell trained on Exp 024+028 data, then predicts Exp 029 data it has never
seen:

| Beta | Predicted CG | Actual CG | Error |
|------|-------------|-----------|-------|
| 4.5 | 24,800 | 25,100 | 1.2% |
| 5.25 | 22,300 | 23,100 | 3.5% |
| 5.69 | 18,900 | 18,400 | 2.7% |
| 6.5 | 1,800 | 1,750 | 2.9% |
| Mean | | | **2.6%** |

The shell has never seen dynamical fermion data from Exp 029. It was trained
only on Exp 024 (parameter sweep) and Exp 028 (brain pipeline) data. The
2.6% blind error validates that the evolutionary reservoir generalizes
across runs.

## State Persistence

### Save/Restore Fidelity

After serializing the full shell to JSON and restoring:

```
prediction_before = shell.predict(test_input)
json = serde_json::to_string(&shell)?;
shell_restored = serde_json::from_str(&json)?;
prediction_after = shell_restored.predict(test_input)

assert!(|prediction_before - prediction_after| < 1e-16)
```

**Bit-perfect** — f64 values survive JSON round-trip within floating-point
representation limits. The shell's entire state (population, readout weights,
history, drift monitor, concept edges) is preserved.

### What is Serialized

| Component | Size | Notes |
|-----------|------|-------|
| Population (16 boards × 25 values) | ~3 KB | Board definitions |
| Readout weights (400 × 2) | ~6 KB | Ridge regression coefficients |
| History (20 generations) | ~8 KB | GenerationRecords with ne_s, drift_action |
| Drift monitor state | ~2 KB | Fitness history window |
| Concept edges | ~1 KB | Feature vectors (if any) |
| Metadata | ~1 KB | Instance ID, parent, config |
| **Total** | **~23 KB** | Entire shell in a single JSON file |

23 KB for a complete trained predictor with full evolutionary history. This
fits in a single UDP packet. It fits in the AKD1000's SRAM 40 times over.
