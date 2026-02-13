# Mise en Place - Control Experiment Setup

**Status**: Active preparation  
**Purpose**: Set up the Python scientific computing stack to reproduce Murillo Group work as our control experiment. BarraCUDA evolves in parallel on ToadStool's timeline.  
**Last Updated**: February 7, 2026

**Implementation**: `ecoPrimals/hotSpring/` - the working project directory with conda environments, clone scripts, benchmark protocols, and all control experiment work.

---

## Overview

Mise en place: everything in its place before cooking begins. This document is the reference guide. The working code lives in `hotSpring/`.

- **`hotSpring/scripts/setup-envs.sh`** - Creates all three conda environments
- **`hotSpring/scripts/clone-repos.sh`** - Clones all Murillo Group repos
- **`hotSpring/envs/`** - Conda YAML specs (sarkas, surrogate, ttm)
- **`hotSpring/control/`** - Control experiment work (sarkas, surrogate, ttm)
- **`hotSpring/benchmarks/`** - Cross-gate benchmark results and protocol
- **`hotSpring/data/`** - Reference data (Dense Plasma Properties DB, Zenodo downloads)

Phase B (BarraCUDA re-execution) evolves in ToadStool independently. See `BARRACUDA_SCIENTIFIC_COMPUTE_GAPS.md` for the gap analysis that informs ToadStool's roadmap.

**What can happen now** (no NUCLEUS needed):
- Clone repos, download data, install Sarkas, run tutorials on a single gate
- Read papers, review code, understand the computational pipelines

**What waits for NUCLEUS**:
- Cross-gate benchmarks, Westgate cold storage, biomeOS coordination, 10G data transfer

---

## 1. Sarkas - Molecular Dynamics (Control)

### Get the Code

```bash
# On any gate (start with Eastgate for dev, Strandgate for production)
mkdir -p ~/research/murillo-group
cd ~/research/murillo-group
git clone https://github.com/murillo-group/sarkas.git
git clone https://github.com/MurilloGroupMSU/Dense-Plasma-Properties-Database.git
git clone https://github.com/MurilloGroupMSU/Two-Temperature-Model.git
```

| Repository | Size | Contents |
|-----------|------|----------|
| sarkas | ~small | Pure Python MD code, docs, examples |
| Dense-Plasma-Properties-Database | <1GB | Reference data (VACF, g(r), EOS, ionization) in 14+ subdirectories |
| Two-Temperature-Model | ~small | Python ODE solver, Jupyter notebooks, reference papers |

### Install Sarkas

Sarkas provides a conda environment file. Use it.

```bash
# Option A: Use their env file directly
cd ~/research/murillo-group/sarkas
conda env create -f sarkas_env.yaml
conda activate sarkas

# Option B: Manual (if env file has issues with newer Python)
conda create --name sarkas python=3.9 pip
conda activate sarkas
conda install -c conda-forge numpy scipy pandas numba>=0.50 pyfftw=0.12.0 pytables pyyaml tqdm matplotlib seaborn jupyter jupyterlab
pip install sarkas fmm3dpy
```

### System Dependencies

These need to be installed at the OS level before the Python packages work:

| Package | What | Install (Ubuntu/Debian) | Install (Fedora/RHEL) |
|---------|------|------------------------|----------------------|
| **FFTW3** | Fast Fourier transforms (C library) | `sudo apt install libfftw3-dev` | `sudo dnf install fftw-devel` |
| **FMM3D** | Fast Multipole Method (Fortran) | Build from source or `pip install fmm3dpy` | Same |
| **gcc/gfortran** | Needed to compile FMM3D | `sudo apt install build-essential gfortran` | `sudo dnf install gcc gcc-gfortran` |

**Known issue**: pyfftw 0.12.0 is pinned specifically. Newer versions have a runtime error with nthreads. Stick to 0.12.0.

### Validate Installation

```bash
conda activate sarkas
python -c "import sarkas; print(sarkas.__version__)"
python -c "import pyfftw; print('pyfftw OK')"
python -c "import numba; print(f'Numba {numba.__version__}, threads: {numba.config.NUMBA_NUM_THREADS}')"
```

### Run Quickstart

Sarkas docs include a [Quickstart notebook](https://murillo-group.github.io/sarkas/documentation/Tutorial_NB/Quickstart.html). Run it first.

```bash
cd ~/research/murillo-group/sarkas
jupyter lab
# Open and run the quickstart notebook
# Compare output to expected results in the docs
```

Then run the full [Tutorial](https://murillo-group.github.io/sarkas/documentation/tutorial.html) which covers:
- Setting up YAML input files for simulations
- Yukawa (screened Coulomb) potentials
- Pre-processing, simulation, post-processing workflow
- Analysis: VACF, g(r), structure factors

### Validate Against Reference Data

After Sarkas runs, compare results to the Dense Plasma Properties Database:

```bash
cd ~/research/murillo-group/Dense-Plasma-Properties-Database
jupyter lab
# Open Main.ipynb - this is the database browser
# Compare Sarkas output to database reference values for:
#   - Yukawa VACF
#   - Yukawa g(r)
#   - Yukawa dynamic structure factors
```

**This is the critical control step**: our hardware produces the same physics as published results.

### Profile Sarkas

Before benchmarking across gates, understand where time goes:

```python
# In a Jupyter notebook or script
import cProfile
import sarkas
# Run a small simulation with profiling
# Identify: force calc vs FFT vs neighbor list vs integration vs I/O
```

Key questions:
- What percentage of wall time is force calculation?
- What percentage is FFT (PPPM long-range)?
- How does Numba JIT affect first-run vs subsequent runs?
- What is memory usage vs particle count?

### Hardware Benchmark Plan

Run the **same simulation** on each gate. Control for everything except hardware.

| Gate | CPU | Cores | RAM | Key Variable |
|------|-----|-------|-----|-------------|
| **Strandgate** | Dual EPYC 7452 | 64 | 256GB ECC | Core count, ECC |
| **Northgate** | i9-14900K | 24 (8P+16E) | 192GB | Single-thread speed, hybrid cores |
| **Southgate** | 5800X3D | 8 | 64GB | 3D V-Cache (96MB L3) |
| **Eastgate** | (dev/test) | - | - | Initial validation |

**Benchmark protocol**:
1. Same YAML input file
2. Same particle count (start small: 1K, then 10K, then 100K)
3. Same number of timesteps
4. Record: wall time, time per step, peak memory, Numba thread count
5. Run 3x each, report median

---

## 2. Surrogate Learning - Nature MI 2024 (Control)

### Get the Data and Code

| Resource | URL | Action |
|----------|-----|--------|
| **Paper** | [doi.org/10.1038/s42256-024-00839-1](https://doi.org/10.1038/s42256-024-00839-1) | Read thoroughly |
| **Datasets** | [Zenodo: 10.5281/zenodo.10908462](https://doi.org/10.5281/zenodo.10908462) | Download now |
| **Code** | [Code Ocean: 10.24433/CO.1152070.v1](https://doi.org/10.24433/CO.1152070.v1) | Download capsule |

```bash
# Download Zenodo datasets (can do now, no NUCLEUS needed)
mkdir -p ~/research/murillo-group/surrogate-learning
cd ~/research/murillo-group/surrogate-learning

# Go to Zenodo page, download all files
# wget or browser download from https://zenodo.org/records/10908462

# Download Code Ocean capsule
# Code Ocean provides a "Download" option for the compute capsule
# Extract and review the environment/dependencies
```

### Install Environment

```bash
conda create --name surrogate python=3.10 pip
conda activate surrogate
pip install mystic numpy scipy matplotlib

# Check Code Ocean capsule for additional deps
# Likely: scikit-learn, PyTorch or TensorFlow
# Install whatever the capsule requires
```

### Reproduction Steps

1. **Read the paper** - understand optimizer-driven sampling vs traditional sampling
2. **Review Code Ocean capsule** - understand the code structure, inputs, outputs
3. **Run on benchmark functions first** (Rastrigin, Rosenbrock, Easom) - these are fast and validate the method works
4. **Run on nuclear EOS models** - this is the headline result
5. **Record**: training time, surrogate accuracy, number of simulation evaluations needed

### Hardware Assignment (Control)

For the control experiment, run on whatever GPU PyTorch/TensorFlow detects. The point is reproducing the results, not benchmarking hardware yet.

| Gate | GPU | Role |
|------|-----|------|
| **Northgate** | RTX 5090 | Primary (best GPU for training) |
| **Strandgate** | RTX 3090 | Comparison if desired |

---

## 3. Two-Temperature Model (Control)

### Get the Code

```bash
cd ~/research/murillo-group
git clone https://github.com/MurilloGroupMSU/Two-Temperature-Model.git
```

### Structure

```
Two-Temperature-Model/
├── core/
│   ├── physics.py      # Fermi Energy, model parameters (class-based)
│   ├── constants.py    # SI numerical constants
│   └── TTM.py          # ODE solver + experiment classes
├── data/               # Experimental/simulation reference data
├── jupyter/            # Notebooks (primary interface)
├── PDF_papers/         # Reference papers
├── Presentations/      # Slides
├── notes/              # Working notes
└── media/              # Figures
```

### Install and Run

```bash
conda create --name ttm python=3.10 pip
conda activate ttm
pip install numpy scipy matplotlib jupyter

# Check core/ imports for any additional deps
cd ~/research/murillo-group/Two-Temperature-Model
jupyter lab
# Open notebooks in jupyter/ directory
```

The TTM is pure Python (NumPy/SciPy ODE solver). No special hardware needed. Runs on any gate.

---

## 4. Additional Murillo Group Repos (Review Only)

Clone for reference. Don't set up environments yet.

```bash
cd ~/research/murillo-group
# These are older/niche - review first, install if relevant
# git clone https://github.com/MurilloGroupMSU/BIM_HNC.git              # Fortran, 2016
# git clone https://github.com/MurilloGroupMSU/Thomas-Fermi-Multispecies-Ionization.git  # Jupyter, 2018
# git clone https://github.com/MurilloGroupMSU/Teaching_Content.git     # Nov 2024 - may have CMSE 890 examples
```

The Teaching_Content repo (updated November 2024) may contain examples from Applied Machine Learning (CMSE 890) - the course where the neuromorphic conversation happened. Worth reviewing.

---

## 5. ToadStool Benchmark Data (Internal - In Progress)

ToadStool is actively running benchmarks. Data will populate as it's generated.

| Workload | Hardware | Status |
|----------|----------|--------|
| NPU inference (k-mer, intent, MNIST) | Akida (3x: Strandgate 2x, Eastgate 1x) | Running |
| GPU tensor ops | NVIDIA (RTX 3090, 4070, 5090) + AMD (RX 6950 XT) | Running |
| FHE operations | All GPUs | Running |
| Cross-substrate comparison | Same workload, all substrates | In progress |

Data format: CSV/JSON per workload per substrate. Storage plan:

```
/data/benchmarks/toadstool/
├── npu/
├── gpu/{nvidia-rtx5090,nvidia-rtx3090,nvidia-rtx4070,amd-rx6950xt}/
├── cpu/{epyc-7452,i9-14900k,5800x3d}/
├── fhe/
└── cross-substrate/
```

---

## 6. Storage Architecture

### Now (Pre-NUCLEUS)

Each gate stores data locally in `~/research/murillo-group/`. This is fine for single-gate development and validation.

### Later (Post-NUCLEUS)

Westgate becomes the cold data hub via Nest Atomic:

```
Westgate (76TB ZFS)
├── /data/research/murillo-group/
│   ├── Dense-Plasma-Properties-Database/   (~<1GB)
│   ├── sarkas-simulations/                 (~TBD)
│   ├── surrogate-learning/                 (~TBD, Zenodo data)
│   └── Two-Temperature-Model/              (~small)
├── /data/benchmarks/toadstool/             (~growing)
└── /data/models/trained-surrogates/        (~TBD)
```

Access pattern: Westgate stores → compute gates pull via NestGate → 10G backbone moves the data → results flow back to Westgate.

---

## 7. Python Environment Summary

Three conda environments, isolated to avoid dependency conflicts:

| Environment | Python | Key Packages | Purpose |
|------------|--------|-------------|---------|
| `sarkas` | 3.9 | numpy, numba>=0.50, pyfftw=0.12.0, scipy, pandas, pytables, sarkas, fmm3dpy | Molecular dynamics |
| `surrogate` | 3.10 | numpy, scipy, mystic, PyTorch/TF (from Code Ocean capsule), scikit-learn | Surrogate learning |
| `ttm` | 3.10 | numpy, scipy, matplotlib, jupyter | Two-Temperature Model |

System-level: FFTW3 dev libraries, gfortran (for FMM3D compilation).

---

## 8. Action Checklist

### Done

- [x] Identify all Murillo Group repositories and open-source resources
- [x] Locate Sarkas installation instructions and full dependency chain
- [x] Locate surrogate learning paper data (Zenodo) and code (Code Ocean)
- [x] Document Dense Plasma Properties Database structure (14+ subdirectories)
- [x] Document Two-Temperature Model structure and code layout
- [x] Plan storage architecture (local now, Westgate later)
- [x] Plan hardware assignment for cross-gate benchmarks
- [x] Document all Python environment requirements
- [x] Map BarraCUDA capabilities to scientific computing needs (see `BARRACUDA_SCIENTIFIC_COMPUTE_GAPS.md`)
- [x] Identify gaps for Phase B (FFT, complex arithmetic, PBC, force kernels, Bessel functions)

### Do Now (Any Gate, No NUCLEUS)

- [ ] Install FFTW3 system libraries on Strandgate
- [ ] Install FFTW3 system libraries on Northgate and Southgate
- [ ] Create `sarkas` conda environment on Strandgate
- [ ] Install Sarkas and validate import
- [ ] Clone all three primary repos to `~/research/murillo-group/`
- [ ] Run Sarkas quickstart notebook
- [ ] Run Sarkas full tutorial (Yukawa simulation)
- [ ] Compare Sarkas output to Dense Plasma Properties Database reference data
- [ ] Download Zenodo surrogate learning datasets
- [ ] Download Code Ocean surrogate learning capsule
- [ ] Review Code Ocean capsule structure and dependencies
- [ ] Create `surrogate` conda environment
- [ ] Read Nature Machine Intelligence paper in full
- [ ] Create `ttm` conda environment
- [ ] Run TTM Jupyter notebooks
- [ ] Review Teaching_Content repo for CMSE 890 materials
- [ ] Profile Sarkas: where does compute time go?

### Do After NUCLEUS Stabilizes (Cross-Gate Benchmarks)

- [ ] Install Sarkas on Northgate and Southgate (identical environments)
- [ ] Cable 10G backbone
- [ ] Deploy Nest Atomic on Westgate
- [ ] Move all repos and data to Westgate cold storage
- [ ] Run Sarkas benchmark protocol: same sim, 3 gates, 3 particle counts, 3 runs each
- [ ] Run surrogate learning reproduction on Northgate GPU
- [ ] Run TTM parameter sweeps on Strandgate
- [ ] Acquire ABM code from Murillo Group (collaboration dependent)

### Phase B (BarraCUDA - Evolves on ToadStool's Timeline)

BarraCUDA evolves in ToadStool independently. The Phase A control results tell us exactly what to target. See:
- `BARRACUDA_SCIENTIFIC_COMPUTE_GAPS.md` - what new shaders to evolve
- `MURILLO_REPRODUCTION_PLAN.md` - kernel-to-shader mapping for each study

---

**The control experiment comes first. Get Sarkas running, get correct physics, get profiling data. That data drives everything - it tells us where BarraCUDA needs to evolve and what performance target to beat.**
