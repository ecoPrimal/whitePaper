# guideStone–LTEE: Deployable Validation Artifact for Barrick Lab

**Class**: guideStone (verification artifact)
**Springs**: wetSpring + neuralSpring
**Target**: LTEE / Barrick Lab / second interview USB
**Date**: May 11, 2026
**Status**: Concept — handoff to spring teams

---

## Purpose

A USB-deployable artifact that demonstrates computational parity with
institutional tools on Barrick Lab's own science. Plug it into any
Linux machine in Barrick's lab, run `./ltee validate`, and it reproduces
key LTEE results from public data — no internet, no install, no dependencies.

Three tiers prove the stack at every level:

```
Tier 1 — Python    Familiar. Jupyter notebooks. "I can read this."
Tier 2 — Rust      Fast. Validated binaries. "This is 100× faster."
Tier 3 — Primal    Composed. NUCLEUS dispatch. "This is the infrastructure."
```

The artifact IS the interview. Not slides. Not a talk. A USB drive that
runs their science on their hardware and produces their numbers.

---

## What It Proves to Barrick

1. **I can reproduce your published results computationally** — not a claim, a demonstration
2. **The pipelines are validated against your data** — same inputs, same outputs, named tolerances
3. **The infrastructure scales from USB to cluster** — same binaries, same math, different hardware
4. **I understand the LTEE deeply enough to build tools for it** — not just read the papers, but encode the science
5. **BioBricks are a natural extension** — standardized parts registry → computational target

---

## Science Payload

### Module 1: LTEE Fitness Dynamics (Wiser et al. 2013)

**Data source**: Dryad — `doi:10.5061/dryad.0hc2m` (public, no restrictions)

| Analysis | Python Tier | Rust Tier | What It Shows |
|----------|-------------|-----------|---------------|
| Power-law fit: W(t) = (1 + αt)^β | scipy.optimize least-squares | groundSpring jackknife + AIC/BIC model comparison | Our fit matches their published parameters |
| Asymptotic model comparison | matplotlib figure reproducing Fig. 1 | Bayesian model selection (power-law vs hyperbolic vs asymptotic) | Power law wins — we reproduce the finding |
| Cross-replicate prediction | Train on 6 populations, predict other 6 | neuralSpring LSTM + transfer learning | ML predicts fitness trajectories across replicates |
| Error quantification | Bootstrap CI on parameters | groundSpring Exp 019 jackknife (subpercent) | Tighter error bars than published |

**Key output**: JSON with measured parameters, published parameters, tolerance, and PASS/FAIL.

---

### Module 2: Mutation Accumulation (Barrick 2009 + Tenaillon 2016)

**Data source**: NCBI BioProject (264 genomes from Tenaillon 2016) — pre-downloaded into artifact

| Analysis | Python Tier | Rust Tier | What It Shows |
|----------|-------------|-----------|---------------|
| Mutation count per population over time | pandas + matplotlib | wetSpring sovereign pipeline | Clock-like accumulation reproduced |
| Synonymous vs nonsynonymous ratio | BioPython | wetSpring HMM annotation | Selection signature confirmed |
| Mutation rate shift detection | changepoint (ruptures) | neuralSpring ESN regime classifier | Automatic detection of hypermutator transition |
| Parallel evolution scoring | manual gene-by-gene | neuralSpring ML parallel evolution detector | Same genes hit independently across populations |

**Key output**: Per-population mutation trajectories with regime annotations.

---

### Module 3: Allele Frequency Trajectories (Good et al. 2017)

**Data source**: NCBI BioProject PRJNA380528 (metagenomic time series) — subset pre-downloaded

| Analysis | Python Tier | Rust Tier | What It Shows |
|----------|-------------|-----------|---------------|
| Allele frequency tracking | pandas time-series | neuralSpring LSTM prediction | Trajectory prediction across 500-gen intervals |
| Clade detection | manual threshold | neuralSpring HMM hidden-state inference | Competing clades identified automatically |
| Regime classification | visual | neuralSpring ESN (sweep vs interference vs coexistence) | Evolutionary regime labeled per time window |
| Clonal interference quantification | — | groundSpring rare biosphere + quasispecies threshold | When does interference dominate sweeps? |

**Key output**: Interactive allele trajectory plots with ML-annotated regimes.

---

### Module 4: Citrate Innovation (Blount 2008, 2012)

| Analysis | Python Tier | Rust Tier | What It Shows |
|----------|-------------|-----------|---------------|
| Potentiating mutation cascade | timeline figure | groundSpring rare event statistics (Poisson process) | Probability quantification of the innovation |
| CitT structural analysis | PyMOL visualization | coralForge: ancestral vs mutant CitT structure prediction | Structural consequence of tandem duplication |
| Early warning detection | — | neuralSpring ESN on pre-citrate allele trajectories | Can we detect potentiation before innovation? |

**Key output**: Structural comparison figure + probability analysis.

---

### Module 5: BioBrick Burden (Barrick et al. 2024)

**Data source**: Supplementary data from *Nature Communications* paper (public)

| Analysis | Python Tier | Rust Tier | What It Shows |
|----------|-------------|-----------|---------------|
| Burden distribution across 301 plasmids | seaborn violin plot | wetSpring diversity metrics on burden values | 19.6% burdensome reproduced |
| ML burden prediction from sequence features | scikit-learn (GC%, codon usage, promoter) | neuralSpring transfer learning (sequence → burden) | Predict burden before building the construct |
| Constructability limit | histogram + 45% threshold | groundSpring Anderson W_c analogy | Physical theory for why there's a limit |
| Part compatibility matrix | — | wetSpring + visualization | Which parts compose safely? |

**Key output**: Burden prediction model + interactive part explorer.

---

### Module 6: breseq Parity

| Analysis | Python Tier | Rust Tier | What It Shows |
|----------|-------------|-----------|---------------|
| Mutation calling on reference dataset | breseq (installed separately, comparison baseline) | wetSpring Rust pipeline on same reads | Same mutations found, Rust is faster |
| SNP/indel concordance | diff | wetSpring concordance report with tolerances | Quantified agreement |
| Runtime comparison | time breseq | time wetspring-mutcall | Wall-clock speedup |

**Key output**: Concordance table + speedup metrics.

---

### Module 7: Anderson-QS Predictions for LTEE (Novel — baseCamp Paper 02)

This is the unique contribution. Not reproducing their work — extending it.

| Analysis | Python Tier | Rust Tier | What It Shows |
|----------|-------------|-----------|---------------|
| sdiA expression prediction (biofilm vs planktonic) | Conceptual diagram | wetSpring Anderson model: W_eff = W_base / occupancy | Specific, falsifiable prediction for their strains |
| Disorder parameter mapping across 12 populations | matplotlib | wetSpring Exp140-142 framework | Each LTEE population has a predicted Anderson regime |
| QS eavesdropper enrichment | — | wetSpring NCBI sovereign pipeline (Exp142 result) | sdiA-only organisms enriched in 3D environments |

**Key output**: Predictions document + visualization of expected results.

---

## Media Format — Lesson from First Deploy (May 18, 2026)

The first lithoSpore USB was GPT/ext4. Plugged into a Windows machine:
partition type "Unknown," no drive letter assigned, no access. The
cross-compiled binaries inside were unreachable.

**Rule**: The USB filesystem must be **exFAT**.

| Format | Windows | macOS | Linux | Max File | Permissions | Verdict |
|--------|---------|-------|-------|----------|-------------|---------|
| FAT32 | Yes | Yes | Yes | 4 GB | None | Too small for OCI images |
| ext4 | No | No | Yes | 16 TB | Full Unix | Invisible to Windows/macOS |
| NTFS | Yes | Read-only | Read-only | 16 TB | Windows ACL | Write problems on Unix |
| **exFAT** | **Yes** | **Yes** | **Yes (≥5.4)** | **128 PB** | **None** | **Universal** |

exFAT has no Unix permission bits. Binaries can't be executed directly
from the mount. The entry point script must:
1. Copy binaries to a tmpdir (`/tmp/ltee-guidestone/`)
2. `chmod +x` the copies
3. Execute from tmpdir
4. On Windows: use `ltee.bat` → WSL2 or Docker fallback

The output tier (pre-rendered HTML notebooks, JSON results, docs) is
always readable — no execution needed to browse the artifact contents.
This means even on a system that can't run the binaries, the science
is still visible.

**Layer model**:
```
Layer 0 — Media:     exFAT (every OS can mount)
Layer 1 — Browse:    README, HTML notebooks, docs (every OS can read)
Layer 2 — Launch:    Platform-specific entry point (ltee.sh / ltee.bat)
Layer 3 — Execute:   tmpdir + chmod (Linux/macOS) or container (Windows)
Layer 4 — Validate:  Rust binaries produce JSON + figures
```

---

## Artifact Structure

```
ltee-guidestone-v1.0/
├── README                          # Plain text, no dependencies to read
├── CHECKSUMS                       # SHA-256 of every file
├── liveSpore.json                  # Tracks every machine this USB visits
├── ltee                            # Unified entry point (shell script)
│
├── bin/
│   ├── x86_64/
│   │   ├── static/                 # musl static binaries (CPU-only, any Linux)
│   │   │   ├── ltee-fitness        # Module 1: power-law fitness
│   │   │   ├── ltee-mutations      # Module 2: mutation accumulation
│   │   │   ├── ltee-alleles        # Module 3: allele trajectories
│   │   │   ├── ltee-citrate        # Module 4: citrate structural
│   │   │   ├── ltee-biobricks      # Module 5: BioBrick burden
│   │   │   ├── ltee-breseq-parity  # Module 6: breseq comparison
│   │   │   └── ltee-anderson       # Module 7: Anderson-QS predictions
│   │   └── gpu/                    # glibc dynamic binaries (GPU via Vulkan)
│   │       └── (same binaries, GPU-accelerated)
│   └── aarch64/
│       └── static/                 # ARM builds (Apple Silicon via container)
│
├── python/
│   ├── requirements.txt            # Pinned deps for reproducibility
│   ├── notebooks/
│   │   ├── 01_fitness_dynamics.ipynb
│   │   ├── 02_mutation_accumulation.ipynb
│   │   ├── 03_allele_trajectories.ipynb
│   │   ├── 04_citrate_innovation.ipynb
│   │   ├── 05_biobrick_burden.ipynb
│   │   ├── 06_breseq_parity.ipynb
│   │   └── 07_anderson_predictions.ipynb
│   └── rendered/                   # Pre-rendered HTML (no Python needed to view)
│       └── (same notebooks as .html)
│
├── data/
│   ├── wiser_2013/                 # Dryad fitness data
│   ├── tenaillon_2016/             # Subset of 264 genomes (variant calls, not raw reads)
│   ├── good_2017/                  # Allele frequency time series (processed)
│   ├── biobrick_burden/            # 301 plasmid burden measurements
│   ├── ltee_reference/             # Ancestral REL606 genome + annotations
│   └── ncbi_qs/                    # Pre-downloaded QS gene data (Exp142)
│
├── expected/
│   ├── wiser_parameters.json       # Published power-law parameters (α, β)
│   ├── tenaillon_mutation_counts.json
│   ├── good_allele_summary.json
│   ├── biobrick_burden_summary.json
│   └── anderson_predictions.json   # Our predictions (falsifiable)
│
├── results/                        # Written at runtime
│   └── (per-module JSON output + figures)
│
├── container/
│   └── ltee-guidestone.tar         # OCI image for non-Linux or restricted systems
│
└── docs/
    ├── GUIDESTONE.md               # What this artifact is and why
    ├── LTEE_SCIENCE.md             # The science behind each module
    ├── TOLERANCES.md               # Every named tolerance with derivation
    └── FOR_BARRICK.md              # "Why this matters for your lab"
```

---

## Entry Points

### Linux / macOS
```bash
# The shell launcher handles tmpdir copy + chmod automatically
bash ltee.sh validate          # Full validation — all 7 modules, ~10 min
bash ltee.sh validate --module fitness
bash ltee.sh notebooks         # Opens pre-rendered HTML in browser
bash ltee.sh benchmark         # Characterize this machine
bash ltee.sh python            # Requires Python 3.10+
```

### Windows
```cmd
REM Batch launcher — tries WSL2 first, falls back to Docker
ltee.bat validate
ltee.bat notebooks             REM Opens HTML directly (no WSL needed)
```

### Direct (if mounted with exec permissions, e.g. ext4 on Linux)
```bash
./ltee validate
```

### Browse only (no execution, any OS)
Open `python/rendered/` in a browser — pre-rendered HTML notebooks
with all figures and results. Open `docs/FOR_BARRICK.md` in any text
editor. The science is accessible even if execution isn't possible.

---

## The Three-Tier Demonstration

### Tier 1: Python — "I can read this"

Jupyter notebooks that a biologist can open, read, and understand.
Familiar libraries (pandas, scipy, matplotlib, seaborn). Each notebook
reproduces one module's analysis in ~50 lines of Python. The point is
not performance — it's legibility. Barrick or any lab member can open
a notebook and see exactly what the analysis does.

Pre-rendered HTML versions are included so notebooks can be viewed
without Python installed. `./ltee notebooks` opens them in a browser.

### Tier 2: Rust — "This is 100× faster"

The same analyses, implemented in validated Rust binaries from wetSpring
and neuralSpring. Static musl binaries — no install, no dependencies,
any Linux. GPU-accelerated versions for machines with NVIDIA/AMD cards.

Each binary produces structured JSON output with:
- Measured values
- Published reference values
- Named tolerances with mathematical derivations
- PASS/FAIL verdict
- Runtime in milliseconds

The Rust tier proves: the same science, dramatically faster, with
formal validation that Python notebooks cannot provide.

### Tier 3: Primal — "This is the infrastructure"

The primal tier shows what happens when the Rust binaries compose into
a coordinated system. toadStool dispatches workloads. NestGate manages
the LTEE data. The provenance trio tracks every computation.

This tier requires NUCLEUS primals running (not USB-portable in the same
way), but the artifact includes deploy graphs that show how the Rust
binaries compose into a multi-primal pipeline:

```
NestGate (LTEE data)
    → toadStool (dispatch to GPU/CPU)
        → wetSpring binaries (diversity, mutation analysis)
        → neuralSpring binaries (ML prediction, regime detection)
    → rhizoCrypt (DAG of every analysis step)
    → petalTongue (live dashboard)
```

If they want to see Tier 3 live, that's `lab.primals.eco` — or we
set up a NUCLEUS on their hardware.

---

## Data Licensing and Ethics

All data in this artifact is from **public sources**:

| Dataset | Source | License |
|---------|--------|---------|
| Wiser 2013 fitness | Dryad doi:10.5061/dryad.0hc2m | CC0 |
| Tenaillon 2016 genomes | NCBI BioProject | Public domain |
| Good 2017 alleles | NCBI BioProject PRJNA380528 | Public domain |
| BioBrick burden | Nature Communications supplementary | CC-BY 4.0 |
| REL606 reference | NCBI GenBank U00096 | Public domain |
| QS gene data | NCBI Protein/Nucleotide | Public domain |

No proprietary data. No restricted access. No institutional dependencies.
The artifact carries everything it needs.

---

## Size Budget

Target: fits on a 32 GB USB drive with room to spare.

| Component | Estimated Size |
|-----------|---------------|
| Rust binaries (dual arch, static + GPU) | ~200 MB |
| Python notebooks + rendered HTML | ~50 MB |
| Pre-processed LTEE data (variant calls, not raw reads) | ~2 GB |
| BioBrick burden data | ~10 MB |
| Reference genomes + annotations | ~50 MB |
| OCI container image | ~500 MB |
| Expected results + docs | ~5 MB |
| **Total** | **~3 GB** |

Raw sequencing reads would be 100+ GB. We include processed variant calls
and allele frequencies — enough to reproduce the analyses, small enough
for USB. The Python notebooks show how to fetch raw data from NCBI if
someone wants to re-process from scratch.

---

## What Makes This Different from a Poster or a Talk

| Traditional Interview | guideStone Interview |
|----------------------|---------------------|
| "I've read your papers" | "I've reproduced your results" |
| "I can learn breseq" | "Here's a concordance table vs our pipeline" |
| "I'm interested in LTEE" | "Here are falsifiable predictions for your strains" |
| "I know Python and R" | "Here's the same analysis in Python, Rust, and a composed system" |
| "I can handle data" | "Here's your published data, pre-processed, with provenance" |
| Slides on a laptop | USB drive they keep |

The USB stays with them. After the interview, anyone in the lab can
plug it in and run `./ltee validate`. The artifact continues to make
the case after you leave the room.

---

## Build Dependencies (for spring teams)

### wetSpring team
- [ ] `ltee-fitness` binary: power-law fitting with jackknife CI
- [ ] `ltee-mutations` binary: mutation accumulation from variant call files
- [ ] `ltee-biobricks` binary: burden analysis + part compatibility
- [ ] `ltee-breseq-parity` binary: mutation calling on reference reads
- [ ] `ltee-anderson` binary: Anderson-QS model applied to LTEE parameters
- [ ] Pre-processed LTEE data in `data/` (variant calls, allele frequencies)
- [ ] Expected results in `expected/` with published reference values

### neuralSpring team
- [ ] `ltee-alleles` binary: LSTM trajectory prediction + HMM clade detection + ESN regime classification
- [ ] `ltee-citrate` binary: early warning ESN + structural comparison
- [ ] ML models pre-trained on LTEE data (serialized, no training at runtime)
- [ ] Transfer learning weights for cross-replicate prediction

### groundSpring team
- [ ] Jackknife module linked into `ltee-fitness`
- [ ] Rare event statistics linked into `ltee-citrate`
- [ ] Quasispecies threshold linked into `ltee-alleles`
- [ ] Anderson W_c analogy linked into `ltee-biobricks`

### coralForge team
- [ ] CitT ancestral vs mutant structure predictions (pre-computed, included as PDB files)
- [ ] Structure comparison visualization

### Infrastructure
- [ ] `ltee` shell wrapper (follows hotSpring guideStone `_lib.sh` pattern)
- [ ] CHECKSUMS generation
- [ ] liveSpore.json tracking
- [ ] OCI container build
- [ ] Cross-arch compilation (x86_64 + aarch64)
- [ ] Pre-rendered notebook HTML generation

---

## Timeline Target

**Second interview**: date TBD (after initial Zoom May 11).
Likely 1-3 weeks out. The artifact needs to be USB-ready before that date.

### Phase 1 (Days 1-3): Data + Python notebooks
- Download and pre-process all public LTEE datasets
- Write 7 Python notebooks reproducing each module
- Render to HTML
- Validate against published figures/numbers

### Phase 2 (Days 4-7): Rust binaries
- Build each `ltee-*` binary from existing spring primitives
- Cross-compile static musl + GPU variants
- Generate expected results JSON with tolerances
- CHECKSUMS + liveSpore.json

### Phase 3 (Days 8-10): Integration + Polish
- Unified `./ltee` entry point
- OCI container
- `FOR_BARRICK.md` — the "why this matters" doc
- Full validation on 3+ substrates
- Copy to USB, test cold boot on unfamiliar machine

---

## The Pitch in One Sentence

*"I brought a USB drive. It reproduces five of your lab's key papers,
predicts BioBrick burden from sequence features, and makes a falsifiable
prediction about sdiA expression in your LTEE strains. It runs on any
Linux machine in your lab, no install required."*
