# 07 — Roadmap: Evolution Plans & LTEE Library Vision

**Date:** March 1, 2026

---

## Current State

The Nautilus system is validated at the component level:

| Component | Status |
|-----------|--------|
| Nautilus Shell (reservoir + evolution) | Validated — 31 tests, 5 examples |
| Drift monitor (self-regulation) | Wired into evolve_generation() |
| Edge seeding (directed mutagenesis) | Integrated, validated in brain rehearsal |
| AKD1000 int4 export | Validated — MSE=0.004 |
| State persistence (save/restore) | Bit-perfect |
| Instance transfer/merge | Validated |
| ESN (11 production heads) | Active in Exp 029, 030 |
| Brain architecture (4-layer) | Exp 028 validated basic pipeline |
| Adaptive steering | Fixed in Exp 030, running |

## Near-Term Evolution (Exp 031+)

### Phase 1: Full Brain Pipeline (Next Run)

Wire all four layers of the brain architecture into a single production run:

1. **Async CG on 3090** — switch from `gpu_cg_solve_resident` to
   `gpu_cg_solve_resident_async`. Stream residuals to NPU at batch boundaries.
2. **Titan V pre-motor** — spawn pre-thermalization thread for next beta.
   Use existing multi-GPU infrastructure from `bench_multi_gpu.rs`.
3. **CPU cortex** — spawn Anderson 4D proxy thread. Feed proxy features to
   NPU Heads 12-14.
4. **NPU interrupt** — implement GREEN/YELLOW/RED attention state machine.
   NPU watches passively, interrupts only on anomaly.

**Expected outcome:** All four substrates active simultaneously. 3090 never
waits for pre-thermalization. NPU has physics-informed predictions before
each trajectory.

### Phase 2: Larger Lattices (16⁴ → 32⁴)

Move from 8⁴ to 16⁴ to saturate the 3090:

| Metric | 8⁴ | 16⁴ | 32⁴ |
|--------|-----|------|------|
| VRAM | 14 MB | 219 MB | 3.5 GB |
| SM utilization | 20% | 100% | 100% |
| CG per trajectory | ~0.5s | ~15s | ~480s |
| Physics volume | Toy | Publication | Production |

At 16⁴, the full brain architecture becomes critical — the CG solve takes
15 seconds, giving the Titan V and CPU cortex meaningful time to work in
parallel.

### Phase 3: Independent Dual-GPU Chains

Run two independent dynamical HMC chains simultaneously:

- **3090**: 16⁴ at beta points A
- **Titan V**: 8⁴ (or 12⁴) at beta points B
- **NPU**: steering both chains, cross-comparing predictions

2× beta-point throughput. The NPU can detect when one chain discovers a
feature the other should investigate, dynamically coordinating the scan.

### Phase 4: Quenched→Dynamical Cost Reduction in Production

Use the 540× cost reduction in production:

1. Titan V runs cheap quenched scans at candidate beta points
2. Nautilus Shell predicts dynamical CG cost from quenched features
3. NPU selects the most scientifically valuable beta points
4. 3090 runs expensive dynamical HMC only at selected points

This turns the Titan V into a "scout" — cheap reconnaissance before
committing the expensive 3090 to a full dynamical run.

## Multi-Spring Deployment

### wetSpring: Anderson Localization for QS Prediction

The Nautilus Shell can be trained on wetSpring's 3D Anderson localization
data. The same evolutionary reservoir that predicts CG cost can predict
quorum sensing activation levels. The drift monitor maps directly to
microbial population dynamics (N_e · s is literally the population genetics
quantity).

**Transfer path:** Shell trained on hotSpring QCD → transfer to wetSpring
Anderson 3D → evolve for QS prediction. The quenched→dynamical transfer
pattern (540× cost reduction) may apply to single-species → community
transfer.

### airSpring: Agricultural NPU Models

The AKD1000 int4 export pipeline is ready for airSpring deployment. A
Nautilus Shell trained on soil sensor data can be quantized and deployed to
the same NPU that handles QCD predictions. Different heads, same hardware.

### neuralSpring: Evolutionary Surrogates

coralForge structure prediction could use the Nautilus Shell as a surrogate
model — predict protein folding metrics from sequence features using evolved
boards instead of neural network surrogates.

### groundSpring: Uncertainty Quantification

Concept edge detection (LOO CV) provides uncertainty quantification for free.
The regions where the shell disagrees with itself are the regions where the
model is least certain. groundSpring can use this as an uncertainty signal
without running separate UQ models.

## LTEE Library Vision

The Long-Term Evolution Experiment (LTEE) is the definitive study of
evolution under constraint — 12 populations of E. coli evolving in glucose
minimal medium for 80,000+ generations. The Nautilus Shell is the
computational analog:

| LTEE | Nautilus Shell |
|------|---------------|
| 12 populations | Multiple shell instances |
| Glucose minimal medium | Column-range constraint + data stream |
| Generations | Evolution steps |
| Fitness (growth rate) | Pearson correlation with target |
| Frozen fossil record | Shell history (GenerationRecords) |
| Cit+ mutation | Concept edge discovery |
| N_e · s drift | DriftMonitor tracking |

### What the Library Provides

The LTEE library vision uses the Nautilus Shell to run digital evolution
experiments:

1. **Populations under constraint:** Define the constraint (column ranges,
   data stream, selection method) and evolve.
2. **Drift monitoring:** Track when drift dominates selection, exactly as
   population geneticists track in natural populations.
3. **Fitness tracking:** Generation-by-generation fitness curves, directly
   comparable to LTEE fitness trajectories.
4. **Concept edge detection:** Discover regime boundaries — the computational
   analog of the Cit+ mutation (a qualitative change enabled by accumulated
   mutations).
5. **Frozen fossil record:** Serialized shell history can be "thawed" and
   re-analyzed, exactly as LTEE frozen cultures can be revived.
6. **Transfer and merge:** Simulate horizontal gene transfer, migration,
   and population mixing.

### Testing Constrained Evolution Predictions

The thesis (Chapter 14) makes specific predictions about constrained
evolution. The Nautilus Shell can test them computationally:

- **Prediction 1:** Constraint narrows the solution space, concentrating
  fitness peaks → Test: compare convergence rates with/without column-range
  constraints. Already confirmed: constrained boards outperform random.

- **Prediction 2:** Environmental change (new data stream) causes fitness
  landscape reshaping → Test: transfer a shell trained on quenched data to
  dynamical data. Already confirmed: 540× cost reduction, 4.4% LOO.

- **Prediction 3:** Small populations under constraint degrade via drift →
  Test: run evolution with varying population sizes, monitor N_e · s. Already
  confirmed: DriftMonitor detects and corrects.

- **Prediction 4:** Concept edges mark regime boundaries → Test: detect
  concept edges, verify they correspond to known phase transitions. Already
  confirmed: β=6.131 concept edge at deconfinement.

## Open Questions

1. **Multi-flavor evolution:** Can boards be structured with multiple
   constraint types simultaneously (e.g., column ranges + row sums + diagonal
   properties)? This would model multi-flavor QCD where different fermion
   species impose different constraints.

2. **Hierarchical shells:** Can a shell of shells — where each "board" is
   itself an evolved shell — capture multi-scale physics? Anderson on Anderson:
   a matrix of matrices.

3. **Competitive evolution:** Can two populations evolve adversarially, where
   one tries to predict the other's behavior? This would model predator-prey
   dynamics and could improve robustness.

4. **Living data streams:** Can the Nautilus Shell learn from real-time sensor
   data (soil moisture, microbial fluorescence, nanopore reads) with the same
   efficiency it learns from physics simulations?

5. **Cross-chip transfer:** Validated for AKD1000. Can the same shell deploy
   to FPGA, TPU, or future neuromorphic chips with minimal adaptation?

---

## Timeline

| When | What |
|------|------|
| **Now** | Exp 030 running (adaptive steering fix) |
| **Next run** | Full 4-layer brain, 16⁴ lattice validation |
| **Run after** | Independent dual-GPU chains, Titan V scouting |
| **Q2 2026** | Multi-spring deployment (wetSpring Anderson) |
| **Q3 2026** | LTEE library v1: populations under constraint with drift monitoring |
| **Q4 2026** | Hierarchical shells, competitive evolution experiments |
