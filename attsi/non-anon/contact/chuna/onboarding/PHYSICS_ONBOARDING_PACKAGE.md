# Physics Onboarding Package — TC Chuna / Murillo Group

**Author**: Kevin Mok
**Date**: April 2026
**Recipient**: Thomas (TC) Chuna, PhD candidate, Murillo Group / LANL
**Purpose**: Bridge Chuna's Python/MILC workflow into the hotSpring
Collaborator Engine, enabling him to prototype lattice QCD experiments
on consumer hardware without waiting for HPC SSH.

---

## 1. For TC — What's Built from Your Papers

Three of your published papers are reproduced and validated in pure Rust.
The code derives integrator coefficients independently, validates against
your published results, and runs on any machine with `cargo`.

| Paper | Citation | What We Reproduced | Checks |
|-------|----------|-------------------|:------:|
| 43 | Bazavov & Chuna, arXiv:2101.05320 | Gradient flow: 5 integrators (Euler, RK2, W6, W7, CK4), t0/w0 scale, convergence | 14/14 |
| 44 | Chuna & Murillo, PRE 111, 035206 | Standard + completed Mermin, f-sum, DSF, conductivity | 25/25 |
| 45 | Haack et al., JCP (2024) | BGK relaxation, Sod shock, coupled kinetic-fluid | 20/20 |

**Total: 59 checks pass. Three independent implementations: Python, Rust CPU, Rust GPU.**

### What the Engine Does for Your Workflow

The Chuna Engine is not a paper demo. It is a production tool for your
actual research — generating thermalized gauge configurations, measuring
observables with full provenance, and exporting in formats your existing
tools already consume.

| Binary | What It Does | Your Use Case |
|--------|-------------|---------------|
| `chuna_generate` | ILDG gauge config generation (CPU or GPU HMC) | Generate ensembles at any beta/L/Nf without MILC |
| `chuna_flow` | Gradient flow on any ILDG config | Test new integrators, compare W7 efficiency |
| `chuna_measure` | Observable suite with provenance JSON | Measure plaquette, Polyakov, Wilson loops, HVP, flow, condensate |
| `chuna_analyze` | Jackknife + autocorrelation + susceptibilities | Ensemble-level statistics, TSV export for papers |
| `chuna_convert` | ILDG/LIME/QCDml conversion | Load MILC configs, export for collaborators |
| `chuna_benchmark_flow` | Integrator efficiency workbench | Your core expertise: compare integrator families |

### Python Bridge

Your GitHub repos (DynamicResponseModels, InverseProblemSolvers) are
Python/NumPy. The `hotspring_reader` utility loads all Engine output
into NumPy arrays with zero setup:

```python
import hotspring_reader as hs

meas = hs.load_measurements("data/b6.0_L8/measurements/")
print(meas["plaquette"])     # float64 array
hs.to_tsv(ana, "table.tsv")  # paper-ready table
```

CG solver convergence history (via `--cg-history`) exports as TSV that
you can compare directly against your InverseProblemSolvers.

---

## 2. For Bazavov / Murillo — Downstream Data

### For Bazavov

Every measurement carries `ImplementationInfo` provenance (code name,
version, machine, institution). Output is ILDG-compliant with QCDml 2.0
metadata. Bazavov can load hotSpring configs directly in his analysis
pipeline without conversion.

**What we'd need from Bazavov**: MILC reference configurations at
matched parameters (beta, L, Nf) for cross-validation. Any format
(MILC binary, ILDG/LIME) works — `chuna_convert` handles translation.

### For Murillo

Papers 44-45 (dielectric + kinetic-fluid) reproduce Murillo group
results. The hotSpring Python controls (`bgk_dielectric_control.py`,
`kinetic_fluid_control.py`) produce JSON validated against the
Rust implementation.

**Sensitivity note**: No proprietary data is used. All inputs are
published parameters from the papers. Reference MD data from the
Murillo Group plasma DB is already public.

---

## 3. Compute — ICER vs Lab vs Laptop

The same code runs everywhere. The difference is speed and scale.

| Platform | Hardware | Time for 59 checks | What it proves |
|----------|----------|:-------------------:|---------------|
| TC's laptop | Any x86_64 CPU | ~5 hours | All physics is correct |
| ICER A100 | A100 80GB | ~20 min (estimated) | GPU scales correctly |
| biomeGate | TR 3970X + RTX 3090 | ~3 hours | Cross-vendor GPU parity |
| LANL HPC | Future target | TBD | Production-scale ensembles |

**CPU-only path**: All validation passes without a GPU. Set
`HOTSPRING_NO_GPU=1` to skip GPU discovery entirely. This is the path
TC uses on an HPC login node — the math validates on CPU, the GPU
just makes it fast.

**LANL transition**: When TC moves to LANL, the same `cargo build`
produces binaries for any Vulkan-capable HPC node. No CUDA dependency,
no MILC compilation, no vendor SDK. If the node has an f64 GPU,
hotSpring uses it automatically.

---

## 4. Open Data and References

| Source | What | How Used |
|--------|------|----------|
| arXiv:2101.05320 (Bazavov & Chuna) | LSCFRK integrator coefficients, convergence data | Reproduced; coefficients derived independently |
| PRE 111, 035206 (Chuna & Murillo) | Standard/completed Mermin, plasma parameters | Reproduced; 25 checks |
| JCP (2024) (Haack et al.) | BGK relaxation, Sod shock tube parameters | Reproduced; 20 checks |
| Murillo Group plasma DB | DSF reference data (OCP, Yukawa) | Public; validated in `validate_dsf_vs_md` |
| MILC public configs | Quenched SU(3) at standard betas | Future: cross-validation with MILC |
| PDG (Particle Data Group) | Physical constants | Embedded in code via CODATA |

**Public-first principle**: All current validation uses published data.
MILC comparison data from Bazavov/ICER would be the first "partner"
data requiring coordination.

---

## 5. Pilot Experiments

### Week 1: Validation and Familiarization

- **Day 1**: `git clone` + `cargo test` on TC's laptop or ICER login node
- **Day 2**: Run `validation/run` (59 checks, CPU-only, ~5 hours)
- **Day 3**: Load results with `hotspring_reader.py`, inspect JSON output
- **Day 4**: Run `chuna_generate --beta=6.0 --dims=8,8,8,8 --n-configs=10`
- **Day 5**: Measure with `chuna_measure`, analyze with `chuna_analyze --format=tsv`
- **Outcome**: TC has validated that our code reproduces his numbers
- **Grant seed**: "Independent Rust implementation validates published LSCFRK results"

### Weeks 2-4: Cross-Validation with MILC

- Generate matched-parameter ensembles (same beta, L, Nf as MILC runs)
- Run gradient flow on both hotSpring and MILC configs
- Compare t0/w0 scale setting between implementations
- Use CG convergence history (`--cg-history`) to compare solver behavior
- **Outcome**: Quantified agreement between two independent codebases
- **Grant seed**: "Cross-codebase validation reduces systematic uncertainty"

### Month 2-3: Custom Integrator Prototyping

- TC designs new LSCFRK schemes (his core expertise)
- Implement in `chuna_benchmark_flow` or as a new flow integrator
- Validate on generated ensembles across multiple betas and volumes
- Compare efficiency curves: new integrator vs W7 vs CK4
- **Outcome**: New integrator validated on consumer hardware, ready for production
- **Grant seed**: "Novel integrator developed and validated in portable open-source framework"

---

## 6. Document Index

| Document | Audience | Purpose |
|----------|----------|---------|
| `CHUNA_REVIEW.md` (repo root) | TC, Bazavov | External-facing data sheet with numbers |
| `validation/GUIDESTONE.md` | TC, reviewers | Certification checklist (5 properties + NUCLEUS) |
| `validation/README` | TC | Quick-start guide for running validation |
| `specs/COLLABORATOR_ENGINE_ARCHITECTURE.md` | Internal | Three-phase pattern, engine anatomy |
| `specs/PAPER_REVIEW_QUEUE.md` | Internal | Full 25-paper pipeline status |
| `control/hotspring_reader/README.md` | TC | Python reader usage examples |
| `whitePaper/baseCamp/chuna_*.md` | TC, Bazavov | Per-paper detailed artifacts |

---

## 7. Asks

| Need | From Whom | Timeline |
|------|-----------|----------|
| Validation feedback on Papers 43-45 | TC | Week 1 pilot |
| MILC reference configs at matched parameters | Bazavov (via TC) | Weeks 2-4 |
| LSCFRK coefficient review (our independent derivation) | TC | Week 1 |
| LANL compute access for production-scale testing | TC (post-move) | Month 3+ |
| Feedback on Python reader usability | TC | Week 1-2 |
| Convergence history comparison (CG vs MILC CG) | TC | Week 2 |

---

## Bottom Line

TC gets a workbench that runs his physics at home. No HPC queue, no
vendor SDK, no MILC compilation. The same binary runs on his laptop
(CPU), his office GPU (if any), ICER (A100), and eventually LANL.
Python bridge means his existing analysis workflow works unchanged.

The onboarding is: **validate our numbers against yours (Week 1),
cross-check with MILC (Weeks 2-4), then prototype new integrators
(Month 2+)**. Each phase produces grant-ready results.
