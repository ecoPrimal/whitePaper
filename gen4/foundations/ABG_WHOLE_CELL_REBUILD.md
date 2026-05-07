# ABG Whole-Cell Rebuild: A gen4 Foundation Expression

**Thread 1 of the Unified Lineage — Reproducing and Validating the Complete Whole-Cell Computational Modeling Lineage (2012–2026) Through NUCLEUS Composition**

**Date**: May 6, 2026
**Author**: Kevin Mok (BS Microbiology, MSU 2018; MS Data Science, MSU 2025)
**Status**: Active — analysis and composition mapping
**License**: scyBorg triple — AGPL-3.0-or-later (code), ORC (system mechanics), CC-BY-SA 4.0 (this document)
**Lineage**: gen3/thesis (constrained evolution) → gen3/baseCamp (science explorations) → gen4/foundations (unified lineage) → this expression (Thread 1)
**Context**: This is one expression of the unified foundation described in `THE_UNIFIED_LINEAGE.md`. It zooms into Thread 1 (Whole-Cell Modeling) with detailed paper-by-paper analysis, NUCLEUS composition blueprints, and petalTongue visualization maps. Cross-thread connections to Anderson mathematics (Thread 7), immunology (Thread 3), and environmental genomics (Thread 4) are noted throughout.

---

## 1. Framing: The Continued Outcome

### Why This Exists

gen3 proved that sovereign Rust+GPU infrastructure computes correct science
by reproducing 70+ published papers across 8 domains (12,510+ checks in
~69 days). The constrained evolution thesis — that environmental constraints
reshape fitness landscapes and drive specialization — was validated by the
evidence those springs produced.

But the constraints did not stop evolving. Eight springs absorbed new science.
The library-to-binary rewiring matured through four tiers. The provenance trio
(rhizoCrypt, loamSpine, sweetGrass) became operationally validated end-to-end.
External contact — the ABG (Accelerated Bioinformatics Group) community, the
whole-cell modeling literature, new spring domains — exposed systems the
ecosystem had not yet expressed.

This document is the continued outcome. The constraints grew. Now the question
is not "can we reproduce a paper?" but "can we reproduce an **entire field**
and fill the provenance gaps that the original authors could not?"

### The Validation Target

Seven publications spanning 2012–2026 document the complete history of
whole-cell computational modeling — from the first *Mycoplasma genitalium*
model (Karr et al., Cell, 2012) through the first 4D (space + time) cell
cycle simulation of JCVI-syn3A (Thornburg et al., Cell, 2026). These papers
are published in top-tier journals (Cell, PNAS, Cell Systems), cited thousands
of times, and represent the accumulated effort of five research groups across
14 years.

They also represent exactly the kind of science that NUCLEUS is designed to
replace: parameters borrowed across organisms with citation-only provenance,
MATLAB/Python/C++ simulations with no reproducibility chain, hand-reconciled
data between scales, and post-hoc figure generation disconnected from the
computation that produced them.

Rebuilding this lineage through NUCLEUS creates irrefutable proof that
ecoPrimals can handle the highest-impact computational biology — and that
the provenance gaps in the original work can be structurally filled.

### The scyBorg Anchor

This document, the code that implements the rebuild, and the resulting
publications are released under the scyBorg triple license:

- **AGPL-3.0-or-later**: All code (NUCLEUS compositions, deploy graphs,
  spring experiments). Anyone who builds on it shares modifications back.
- **ORC (Open RPG Creative)**: System mechanics and composition patterns.
  Irrevocable open license administered by Paizo.
- **CC-BY-SA 4.0**: This document and all generated papers. Share-alike
  ensures the knowledge stays open.

The rebuild itself becomes a sovereign publication: DAG-recorded,
BLAKE3-hashed, ed25519-witnessed, loamSpine-committed. Every parameter,
every computation step, every intermediate result is content-addressed
and permanently attributed. The publication pipeline described in
`gen4/thesis/THE_SOVEREIGN_PUBLICATION.md` is instantiated here for the
first time against external science.

### Connection to the Generational Arc

| Gen | Question | This Foundation's Answer |
|-----|----------|------------------------|
| gen1 | Can we build it? | The hardware exists (ironGate cluster: 154 cores, 1 TB RAM, 248 GB VRAM) |
| gen2 | What should we build? | A system that can express any computational science with structural provenance |
| gen3 | Does it work? | Yes — 12,510+ checks across 70+ papers prove the infrastructure computes correctly |
| gen4 | Who uses it? | Anyone who needs to reproduce, validate, or extend whole-cell computational modeling |
| **gen4/foundations** | **Can it replay the classics?** | **This document answers that question** |

---

## 2. The Paper Lineage

Seven papers, three organisms, four research groups, fourteen years. Each
paper built on the last — inheriting parameters, extending methods, and
accumulating provenance debt.

### Paper A — Whole-Cell Computational Model Predicts Phenotype from Genotype

- **Citation**: Karr JR et al. (2012) Cell 150(2):389–401
- **Organism**: *Mycoplasma genitalium* (525 genes, smallest free-living cell)
- **Contribution**: First comprehensive whole-cell model — 28 coupled submodels covering metabolism, transcription, translation, DNA replication, cytokinesis, and more
- **Toolchain**: MATLAB (>28 submodel classes), custom ODE solvers, Gillespie stochastic simulation
- **Data sources**: ~1,900 experimentally observed parameters from >900 publications. BRENDA enzyme kinetics, EcoCyc, KEGG, UniProt
- **Key results**: Predicts cell cycle duration (~9 hours), growth rate, macromolecular composition. Phenotype predictions for 79% of gene disruptions match experimental data.
- **Published code**: WholeCell GitHub repository (MATLAB)
- **Figures**: 7 main figures — growth curves, cell cycle timing, single-cell variability, gene essentiality predictions, metabolite concentrations

### Paper B — Whole-Cell Models and Simulations in Molecular Detail

- **Citation**: Feig M, Sugita Y (2019) Annu Rev Cell Dev Biol 35:191–211
- **Organism**: Review (covers *M. genitalium*, *E. coli*, *M. pneumoniae*)
- **Contribution**: Review paper surveying physical/atomistic approaches to whole-cell modeling. Identifies the gap between kinetic models (Paper A) and all-atom structural models. Discusses integration challenges.
- **Toolchain**: N/A (review)
- **Key arguments**: Need for multi-scale integration (kinetic + spatial + structural). Challenges: system size (billions of atoms), timescale gaps (ns to hours), force field accuracy for crowded environments.
- **NUCLEUS relevance**: Frames the exact multi-scale composition problem that Papers E–G attempt and NUCLEUS formalizes

### Paper C — Designing Minimal Genomes Using Whole-Cell Models

- **Citation**: Rees-Garbutt J et al. (2020) Nat Commun 11:836
- **Organism**: *Mycoplasma genitalium* (using Paper A model)
- **Contribution**: Algorithmic genome minimization — two algorithms (Minesweeper greedy and GAMA genetic algorithm) that systematically remove genes while maintaining viability in-silico
- **Toolchain**: MATLAB (Paper A model as substrate), custom Minesweeper/GAMA implementations
- **Data sources**: Paper A model + gene essentiality data
- **Key results**: GAMA explored 53,451 genomes, found designs with up to 237 genes removed (45% of genome). Minesweeper produced smaller reductions faster but less optimal.
- **Parameter inheritance**: Directly inherits Paper A's 1,900+ parameters and 28 submodels. No independent parameter validation.
- **Figures**: 6 main figures — algorithm schematics, genome reduction trajectories, viability landscapes, comparison of Minesweeper vs GAMA

### Paper D — The E. coli Whole-Cell Modeling Project

- **Citation**: Sun G et al. (2020) Synth Biol (Oxf) 5(1):ysaa020
- **Organism**: *Escherichia coli* K-12 MG1655 (4,623 genes)
- **Contribution**: Multi-generation *E. coli* whole-cell model built through "deep curation" — systematic assembly of gene-by-gene kinetic parameters. First model to simulate cell lineages (mother → daughter cells).
- **Toolchain**: Python (Vivarium framework), multi-process architecture
- **Data sources**: EcoCyc, BRENDA, literature curation. ~2,000 gene products characterized.
- **Key results**: Reproduces growth, division, and multi-generation lineage behavior. Demonstrates deep curation methodology.
- **Architectural insight**: Python multi-process design parallels NUCLEUS composition — each submodel is an independent process communicating via message passing
- **Figures**: Multi-generation growth, composition dynamics, gene expression distributions

### Paper E — Fundamental Behaviors Emerge from Simulations of a Living Minimal Cell

- **Citation**: Thornburg ZR et al. (2022) Cell 185(2):345–360
- **Organism**: JCVI-syn3A (493 genes, synthetic minimal cell derived from *M. mycoides*)
- **Contribution**: First fully dynamical kinetic model of a minimal cell — hybrid stochastic-deterministic simulation with 3D spatial resolution. Couples genetic information processing (stochastic, Lattice Microbes) with metabolism (deterministic, ODE) in a realistic 3D cell geometry.
- **Toolchain**: Lattice Microbes (C++/CUDA, Luthey-Schulten group), custom ODE solver for metabolism, Python glue code
- **Data sources**: Proteomics, lipidomics, metabolomics from JCVI-syn3A. RNA-seq expression data. BRENDA enzyme kinetics. CG-MD membrane structures from a precursor to Paper F.
- **Key results**: Emergent ribosome biogenesis (20-minute doubling), spatial organization of ribosomes and mRNA, metabolite concentration dynamics matching experimental measurements
- **Parameter inheritance**: Draws kinetic parameters from BRENDA/TECRdb with literature-based estimation where data is missing. Cross-references proteomics for initial conditions.
- **Figures**: 7 main figures — 3D cell visualization, metabolite time courses, ribosome dynamics, mRNA spatial distributions, growth rate emergence
- **Compute**: GPU-accelerated (CUDA) for Lattice Microbes spatial stochastic simulation

### Paper F — Molecular Dynamics Simulation of an Entire Cell

- **Citation**: Stevens JA et al. (2023) Front Chem 11:1106495
- **Organism**: JCVI-syn3A
- **Contribution**: First coarse-grained molecular dynamics simulation of an entire cell — 561 million CG beads representing the complete proteome, genome, membrane, and metabolites of JCVI-syn3A
- **Toolchain**: GROMACS (MD engine), Martini 3 coarse-grained force field, OpenMM for validation, custom builder scripts (Python)
- **Data sources**: JCVI-syn3A proteomics for copy numbers, AlphaFold2 structure predictions for all proteins, Martini 3 parameters, experimental membrane composition
- **Key results**: Stable 200 ns simulation. Protein diffusion coefficients consistent with experimental measurements. Membrane organization and protein crowding match cryo-EM observations.
- **Parameter inheritance**: Protein structures from AlphaFold2 (no experimental structures for most syn3A proteins). Martini 3 CG parameters from the Marrink group. Copy numbers from Breuer et al. proteomics.
- **Figures**: 8 main figures — cell rendering, protein distribution, membrane cross-section, diffusion analysis, ribosome crowding, chromosome organization
- **Compute**: Massive GPU requirement — ~6 billion atom-equivalents in CG representation. GROMACS on HPC GPU clusters.

### Paper G — Bringing the Genetically Minimal Cell to Life

- **Citation**: Thornburg ZR et al. (2026) Cell (in press)
- **Organism**: JCVI-syn3A
- **Contribution**: Full 4D (space + time) cell cycle simulation — integrates kinetic model (Paper E), structural model (Paper F), chromosome dynamics, membrane morphology, and cell division. First simulation to capture an entire cell cycle from birth through division with spatial, temporal, and molecular resolution.
- **Toolchain**: Lattice Microbes (C++/CUDA) + custom ODE metabolism + CG-MD structural components + chromosome dynamics module + morphological transformation engine
- **Data sources**: All of Papers E and F, plus new experimental data on chromosome segregation and membrane remodeling during division
- **Key results**: Complete cell cycle timing (~2 hours), chromosome segregation dynamics, membrane constriction and scission, daughter cell asymmetry
- **Parameter inheritance**: Full inheritance from Papers E and F. New parameters for division machinery from literature and estimation.
- **Figures**: Cell cycle visualization, chromosome dynamics, morphological time series, metabolic oscillations, division checkpoint analysis
- **Compute**: Multi-GPU, multi-scale — Lattice Microbes (CUDA) for spatial stochastic, ODE for metabolism, specialized kernels for chromosome and membrane dynamics

### The Lineage Map

```
Paper A (2012)
  M. genitalium WCM — 28 MATLAB submodels, 1,900 parameters
  │
  ├── Paper C (2020)
  │     Genome minimization ON Paper A model
  │     53,451 genomes explored, same parameters inherited
  │
  └── Conceptual bridge → different organism, similar approach
        │
Paper D (2020)
  E. coli WCM — Python multi-process, "deep curation"
  Independent parameter set, parallel methodology
        │
Paper B (2019, review)
  Identifies the kinetic↔structural gap
  Frames the multi-scale challenge
        │
        ├── Paper E (2022)
        │     JCVI-syn3A kinetic model
        │     Lattice Microbes + ODE, hybrid stochastic-deterministic
        │     Draws from BRENDA/TECRdb, proteomics, lipidomics
        │     │
        │     └── Paper G (2026)
        │           Full 4D cell cycle
        │           Integrates E + F + chromosome + morphology
        │
        └── Paper F (2023)
              JCVI-syn3A MD — 561M CG beads
              GROMACS/Martini 3, AlphaFold2 structures
              │
              └── Paper G (2026) ← merges E and F lineages
```

---

## 3. The Jelly Strings Inventory

Every point where trust is social rather than structural — where the
lineage holds together because someone said "trust me" rather than
because the system enforces integrity.

### Cross-Paper Parameter Inheritance

| From | To | What Transfers | Provenance |
|------|----|---------------|-----------|
| ~900 publications | Paper A | 1,900 experimental parameters | Citation-only. No content hashing. No version tracking. |
| Paper A (all params) | Paper C | Full 28-submodel parameter set | "We used the published model." No parameter diff. No verification the same version was used. |
| BRENDA/TECRdb | Paper E | Enzyme kinetics for 493 genes | Database query with no snapshot. BRENDA updates continuously. Which version? |
| Experimental proteomics | Paper E | Initial protein copy numbers | Supplementary table. No machine-readable link to raw mass spec data. |
| AlphaFold2 predictions | Paper F | 3D structures for all syn3A proteins | AF2 model versions not pinned. Predictions evolve with model updates. Which weights? |
| Martini 3 force field | Paper F | CG parameters for all molecules | Martini version specified but parameter files not content-addressed. |
| Papers E + F (all) | Paper G | Complete kinetic + structural models | "We integrated the models from [refs]." No structural mechanism to verify parameter consistency between the two inherited codebases. |

### Software Version Ambiguity

| Paper | Tool | Version Concern |
|-------|------|----------------|
| A | MATLAB | Version unspecified. MATLAB numeric behavior varies between releases. |
| C | MATLAB (Paper A code) | Same MATLAB version? Same codebase commit? "We used the published model" — which commit? |
| D | Python (Vivarium) | Python version, numpy version, scipy version — floating-point behavior depends on all three |
| E | Lattice Microbes (C++/CUDA) | CUDA version, GPU architecture, compiler flags all affect stochastic simulation trajectories |
| F | GROMACS | GROMACS 2021.x vs 2022.x have known numerical differences. Which patch level? |
| F | OpenMM | Validation engine version vs production engine version |
| G | All of the above | Multi-tool integration — which versions of each were used together? |

### Manual Data Reconciliation

| Papers | Reconciliation Point | Method |
|--------|---------------------|--------|
| A ↔ experimental | Growth rate, cell cycle timing | Manual comparison to published experimental values |
| E ↔ proteomics | Protein concentrations | Manual mapping from mass spec to model species |
| E ↔ lipidomics | Membrane composition | Manual lipid species mapping between experimental and model nomenclature |
| F ↔ cryo-EM | Protein distribution | Visual comparison of simulation snapshots to electron microscopy images |
| E + F → G | Model integration | Manual alignment of kinetic state variables to structural coordinates — the most complex reconciliation in the lineage |

### Post-Hoc Figure Generation

Every paper generates figures as a separate step after simulation. The
figure code is not the simulation code. The figures show processed,
aggregated, and styled data — not the raw computation output. There is
no mechanism to verify that the figure accurately represents the
simulation state it claims to show.

NUCLEUS/petalTongue eliminates this gap: the computation IS the
visualization. Figures are screenshots of live computation surfaces.

### Citation-Only Provenance for Critical Constants

| Constant | Paper | Source | Structural Provenance |
|----------|-------|--------|--------------------|
| Ribosome elongation rate | E | Literature estimate | None — "approximately 12 aa/s based on [refs]" |
| Membrane lipid ratios | E, F | Experimental lipidomics | Supplementary table, not content-addressed |
| Gene essentiality calls | A, C | Experimental knockouts | Literature compilation, no machine-readable source |
| Diffusion coefficients | F | Experimental FRAP measurements | Reference to published values, no raw data link |
| Division machinery parameters | G | "Estimated from literature" | No specific source for several key parameters |

---

## 4. Data Targets

What the rebuild must reproduce — specific numerical and qualitative
outcomes that serve as validation checkpoints.

### Paper A Targets

| Target | Expected Value | Source |
|--------|---------------|--------|
| Cell cycle duration | ~9 hours (wild-type *M. genitalium*) | Karr et al. Table S4 |
| Growth rate | ~0.077 h⁻¹ | Karr et al. Fig 2 |
| Gene essentiality predictions | Match experimental for 79% of single-gene disruptions | Karr et al. Fig 5 |
| 28 submodel steady states | Metabolite concentrations within published ranges | Karr et al. Supplementary |
| Single-cell variability | Stochastic variation in division timing | Karr et al. Fig 3 |

### Paper C Targets

| Target | Expected Value | Source |
|--------|---------------|--------|
| Minesweeper minimum genome | ~310 genes remaining (215 removed) | Rees-Garbutt et al. Fig 2 |
| GAMA best design | ~288 genes remaining (237 removed) | Rees-Garbutt et al. Fig 3 |
| Total genomes evaluated by GAMA | 53,451 | Rees-Garbutt et al. Results |
| Viability landscape topology | Consistent with published fitness landscape | Rees-Garbutt et al. Fig 4 |

### Paper E Targets

| Target | Expected Value | Source |
|--------|---------------|--------|
| Doubling time | ~110 minutes (JCVI-syn3A) | Thornburg et al. 2022 Fig 1 |
| Ribosome count dynamics | ~500 → ~1000 over cell cycle | Thornburg et al. 2022 Fig 3 |
| ATP concentration | Steady-state within experimental range | Thornburg et al. 2022 Fig 2 |
| mRNA spatial distribution | Non-uniform, consistent with gene position | Thornburg et al. 2022 Fig 4 |
| Metabolite concentration trajectories | 7 key metabolites matching experimental time courses | Thornburg et al. 2022 Fig 2 |

### Paper F Targets

| Target | Expected Value | Source |
|--------|---------------|--------|
| Simulation stability | Stable over 200 ns trajectory | Stevens et al. 2023 Fig S2 |
| Protein diffusion coefficients | Within 2× of experimental FRAP values | Stevens et al. 2023 Fig 4 |
| Membrane thickness | ~4 nm (consistent with CG Martini membrane) | Stevens et al. 2023 Fig 3 |
| Ribosome spatial density | Consistent with cryo-ET tomograms | Stevens et al. 2023 Fig 5 |
| Total CG beads | ~561 million | Stevens et al. 2023 Methods |

### Paper G Targets

| Target | Expected Value | Source |
|--------|---------------|--------|
| Full cell cycle time | ~120 minutes | Thornburg et al. 2026 Fig 1 |
| Chromosome segregation timing | Consistent with experimental observations | Thornburg et al. 2026 Fig 3 |
| Division constriction dynamics | Membrane constriction rate matching FtsZ kinetics | Thornburg et al. 2026 Fig 4 |
| Daughter cell asymmetry | Mass ratio and content distribution | Thornburg et al. 2026 Fig 5 |
| Metabolic oscillations | Cell-cycle-coupled metabolite fluctuations | Thornburg et al. 2026 Fig 2 |

---

## 5. NUCLEUS Composition Blueprints

How each paper's workflow maps to NUCLEUS atomics. Each blueprint defines
the deploy graph shape — what toadStool dispatches, what NestGate stores,
what the provenance trio tracks, and what petalTongue renders.

### Paper A → NUCLEUS: The 28-Submodel Composition

```
Tower (BearDog + Songbird)
  ├── toadStool dispatch
  │     ├── Workload: metabolism_fba (flux balance, ODE)
  │     ├── Workload: transcription_stochastic (Gillespie)
  │     ├── Workload: translation_stochastic (Gillespie)
  │     ├── Workload: dna_replication (state machine)
  │     ├── Workload: protein_folding (kinetic)
  │     ├── Workload: rna_processing (kinetic)
  │     ├── ... (28 submodels total)
  │     └── Workload: cell_cycle_coordinator (master clock)
  │
  ├── barraCuda compute
  │     ├── ODE solver (metabolism — stiff system)
  │     ├── Gillespie SSA (transcription, translation)
  │     └── Matrix operations (FBA linear programming)
  │
  ├── NestGate storage
  │     ├── Parameter store: 1,900 experimental parameters (BLAKE3)
  │     ├── State snapshots: per-timestep cell state
  │     └── Results: growth curves, division events
  │
  └── Provenance trio
        ├── rhizoCrypt: simulation session DAG
        │     └── event per submodel timestep + coupling event
        ├── loamSpine: parameter certificates
        │     └── each of 1,900 parameters traced to publication
        └── sweetGrass: attribution braid
              └── Karr et al. + 900 source publications
```

**toadStool workload types needed**: ODE solver, Gillespie SSA, state
machine (DNA replication), FBA linear programming. All expressible as
existing or near-term toadStool workload types.

**barraCuda kernels needed**: Stiff ODE integrator (BDF/LSODA equivalent),
sparse matrix solver for FBA, random number generation for Gillespie.
hotSpring's existing ODE infrastructure covers the core; FBA requires
a new LP solver kernel.

### Paper C → NUCLEUS: The Genome Search

```
Tower
  ├── toadStool dispatch
  │     ├── Workload: minesweeper_search (greedy, sequential)
  │     ├── Workload: gama_evolution (genetic algorithm, parallelizable)
  │     └── Workload: viability_test (Paper A model evaluation per genome)
  │
  ├── barraCuda compute
  │     └── Paper A model evaluation (reused from Paper A blueprint)
  │
  ├── NestGate storage
  │     ├── Genome library: 53,451 genome designs (content-addressed)
  │     ├── Viability results: per-genome simulation outcomes
  │     └── Fitness landscape: topology of viable ↔ inviable boundary
  │
  └── Provenance trio
        ├── rhizoCrypt: search DAG (each genome evaluation is a node)
        ├── loamSpine: genome certificates (each design with its fitness)
        └── sweetGrass: Rees-Garbutt et al. + Paper A attribution
```

**Key composition pattern**: Paper C composes Paper A as a subroutine.
The Paper A NUCLEUS composition becomes a callable workload within
Paper C's search. This is NUCLEUS composition of compositions —
deploy graphs consuming deploy graphs.

### Paper E → NUCLEUS: The Hybrid Kinetic Model

```
Tower
  ├── toadStool dispatch
  │     ├── Workload: lattice_microbes (spatial stochastic, CUDA)
  │     ├── Workload: ode_metabolism (deterministic, coupled)
  │     ├── Workload: genetic_info_processing (stochastic)
  │     └── Workload: coupling_coordinator (exchanges state every dt)
  │
  ├── barraCuda compute
  │     ├── Lattice Microbes GPU kernels (reaction-diffusion on 3D grid)
  │     ├── ODE solver (metabolism)
  │     └── State exchange (spatial → bulk coupling)
  │
  ├── NestGate storage
  │     ├── 3D grid states: particle positions per timestep
  │     ├── Metabolite trajectories: concentration time series
  │     ├── Proteomics reference: experimental copy numbers (BLAKE3)
  │     └── Parameter store: BRENDA/TECRdb kinetic constants (BLAKE3)
  │
  └── Provenance trio
        ├── rhizoCrypt: simulation DAG
        │     ├── stochastic branch (Lattice Microbes events)
        │     └── deterministic branch (ODE steps)
        ├── loamSpine: parameter provenance
        │     ├── each BRENDA constant → database version + query
        │     └── each proteomics value → raw mass spec link
        └── sweetGrass: Thornburg et al. 2022 + Luthey-Schulten group
```

**New toadStool workload type needed**: Lattice Microbes (C++/CUDA spatial
stochastic simulator). This is the most significant new workload — a
compiled C++/CUDA binary dispatched as a toadStool job. The pattern
already exists (toadStool dispatches external binaries via IPC), but
Lattice Microbes requires GPU allocation and spatial grid management.

**New barraCuda kernels needed**: 3D reaction-diffusion on cubic lattice
(RDME solver). This is adjacent to hotSpring's existing PIC particle
kernels but operates on a fixed grid rather than particles.

### Paper F → NUCLEUS: The MD Simulation

```
Tower
  ├── toadStool dispatch
  │     ├── Workload: gromacs_md (CG-MD, GPU-accelerated)
  │     ├── Workload: structure_builder (cell assembly from components)
  │     ├── Workload: analysis_pipeline (diffusion, density, RDF)
  │     └── Workload: trajectory_processing (frame extraction, filtering)
  │
  ├── barraCuda compute
  │     ├── CG force field evaluation (Martini 3 nonbonded + bonded)
  │     ├── PME electrostatics (GPU FFT)
  │     └── Trajectory analysis kernels (diffusion, spatial correlation)
  │
  ├── NestGate storage
  │     ├── Trajectory frames: XTC/TRR format, content-addressed per frame
  │     ├── Structure files: PDB/GRO with BLAKE3 hashes
  │     ├── Force field parameters: Martini 3 ITP files (BLAKE3)
  │     ├── AlphaFold2 structures: per-protein predictions (BLAKE3, AF2 version pinned)
  │     └── Experimental reference: cryo-EM tomograms, FRAP data
  │
  └── Provenance trio
        ├── rhizoCrypt: MD session DAG
        │     ├── build phase (structure assembly events)
        │     ├── equilibration phase
        │     └── production phase (per-frame events)
        ├── loamSpine: structure certificates
        │     ├── each protein → AlphaFold2 prediction (model version + confidence)
        │     ├── each CG parameter → Martini 3 version
        │     └── each copy number → proteomics experiment
        └── sweetGrass: Stevens et al. 2023 + Marrink group (Martini) +
              DeepMind (AlphaFold2) + Breuer et al. (proteomics)
```

**New toadStool workload type needed**: GROMACS as an external binary
workload. GROMACS is the standard MD engine — toadStool dispatches it
as a managed process with GPU allocation, monitors progress via log
parsing, and captures trajectory output into NestGate.

**New NestGate patterns needed**: MD trajectory storage. XTC and TRR
formats are binary, large (GB to TB), and frame-sequential. NestGate
needs frame-level content addressing — each trajectory frame gets its
own BLAKE3 hash, enabling frame-level provenance and random access.

### Paper G → NUCLEUS: The Full 4D Composition

Paper G is the capstone — it integrates all preceding work into a single
multi-scale simulation. Its NUCLEUS blueprint is the most complex
composition in this foundation.

```
Tower
  ├── toadStool dispatch
  │     ├── Workload: lattice_microbes (from Paper E)
  │     ├── Workload: ode_metabolism (from Paper E)
  │     ├── Workload: chromosome_dynamics (new — polymer + motor model)
  │     ├── Workload: membrane_morphology (new — shape transformations)
  │     ├── Workload: division_machinery (new — FtsZ ring + constriction)
  │     ├── Workload: md_structural (from Paper F, optional refinement)
  │     └── Workload: integration_coordinator (couples all scales)
  │
  ├── barraCuda compute
  │     ├── All Paper E kernels (reaction-diffusion, ODE)
  │     ├── All Paper F kernels (CG force field, PME)
  │     ├── Chromosome polymer dynamics (bead-spring + motor forces)
  │     ├── Membrane shape solver (Helfrich energy + constriction)
  │     └── Multi-scale coupling (spatial interpolation between grids)
  │
  ├── NestGate storage
  │     ├── All Paper E + F storage patterns
  │     ├── Chromosome trajectories: polymer configurations over time
  │     ├── Morphology snapshots: cell shape at each timestep
  │     ├── Division events: constriction metrics, scission timing
  │     └── Full cell state checkpoints: complete serialized state
  │
  └── Provenance trio
        ├── rhizoCrypt: cell cycle DAG
        │     ├── birth event → growth phase → DNA replication →
        │     │   chromosome segregation → constriction → scission →
        │     │   daughter cells
        │     └── every coupling exchange between scales is a DAG event
        ├── loamSpine: complete parameter lineage
        │     └── merges Paper E + F certificates with new division params
        └── sweetGrass: full attribution braid
              └── Thornburg et al. 2026 + all upstream attributions
              (Karr, Rees-Garbutt, Sun, Thornburg 2022, Stevens,
               Luthey-Schulten group, Marrink group, JCVI)
```

**This is the ultimate NUCLEUS composition test**: five independent
compute workloads, three storage patterns, multi-scale coupling across
four spatial/temporal regimes, provenance DAGs spanning the full cell
cycle, and attribution braids reaching back 14 years to Paper A's 900
source publications.

---

## 6. Spring Alignment

Which existing springs already validate subsets of these workflows, and
where each paper's compute patterns have been proven.

### hotSpring → Papers E, F, G

| hotSpring Capability | Paper Alignment |
|---------------------|----------------|
| GPU-accelerated particle dynamics | Paper F: CG-MD is particle dynamics with Martini potentials |
| ODE solvers (Runge-Kutta, adaptive) | Paper E: metabolism ODE integration |
| Monte Carlo sampling | Paper A: stochastic submodels |
| metalForge hardware abstraction | All papers: same code on GPU/CPU/NPU |
| Yukawa/OCP potentials | Paper F: CG nonbonded potentials are structurally similar |
| Phase-space analysis | Paper F: diffusion and spatial correlation analysis |

hotSpring's RTX 5060 sovereign dispatch and metalForge multi-backend
pattern directly apply to Papers E–G. The GPU kernels for particle
dynamics in hotSpring are the closest existing infrastructure to the
CG-MD kernels Paper F needs.

### wetSpring → Papers A, C, D

| wetSpring Capability | Paper Alignment |
|---------------------|----------------|
| Genomics pipelines (16S, WGS) | Paper C: genome library management, gene annotation |
| DADA2 chimera detection | Paper D: quality control for gene curation data |
| Sequence analysis and taxonomy | Papers A, D: gene function classification |
| Provenance pipeline (BLAKE3 on all outputs) | All papers: parameter file integrity |
| Sovereign 16S (no QIIME2/Python) | Model for replacing MATLAB/Python dependencies |

wetSpring's 6,656+ checks and 100% binary provenance demonstrate the
pattern these papers need: every output content-addressed, every
computation step traceable.

### healthSpring → Paper E

| healthSpring Capability | Paper Alignment |
|------------------------|----------------|
| PK/PD kinetic modeling (Hill equation, NLME) | Paper E: enzyme kinetics (Michaelis-Menten, allosteric) |
| Biomarker progression modeling | Paper E: metabolite concentration dynamics |
| Stiff ODE integration | Paper E: metabolism has stiff coupling between fast/slow reactions |
| `primal-proof` IPC pattern | Model for all papers: library → binary rewiring |

healthSpring pioneered the `primal-proof` Cargo feature for conditionally
compiling library vs. IPC compute paths — exactly the pattern needed for
running these simulations through toadStool dispatch.

### neuralSpring → Papers D, E, G

| neuralSpring Capability | Paper Alignment |
|------------------------|----------------|
| Neural network inference | Paper D: ML-assisted parameter estimation |
| ESN reservoir computing | Papers E, G: time-series analysis of simulation output |
| Batched eigensolve | Paper F: normal mode analysis of protein dynamics |

### ludoSpring → All Papers (Composition Patterns)

| ludoSpring Capability | Paper Alignment |
|----------------------|----------------|
| Deploy graph validation (9 graphs, 90 checks) | Blueprint validation for all paper compositions |
| BYOB schema compliance | Deploy graph structure for each paper |
| Session-as-primal pattern | Each simulation run as an ephemeral primal |
| Proto sketch generation | Paper blueprints become proto sketches for springs |
| Composition-of-compositions | Paper C composing Paper A as a subroutine |

### Alignment Matrix

| Paper | hotSpring | wetSpring | healthSpring | neuralSpring | ludoSpring |
|-------|-----------|-----------|-------------|-------------|-----------|
| A | Monte Carlo | Gene annotation | Kinetics | — | Composition |
| B | (review) | (review) | (review) | (review) | (review) |
| C | — | Genome library | — | — | Composition-of-compositions |
| D | — | Gene curation | — | ML params | Composition |
| E | ODE, particles | — | Kinetics, stiff ODE | Time series | Composition |
| F | CG-MD, GPU | — | — | Eigensolve | Composition |
| G | All of E+F | — | Stiff ODE | Time series | Full NUCLEUS composition |

---

## 7. petalTongue: The Computation IS the Presentation

Every figure in every paper becomes a live computation surface. No
post-hoc figure generation. No matplotlib after the fact. The
simulation renders as it runs.

### Paper A → Live Submodel Dashboard

**Static figures**: Growth curves, metabolite concentrations, gene
essentiality heatmaps, cell cycle phase diagrams — all generated
after simulation.

**petalTongue transformation**:
- **28-panel live dashboard**: Each submodel renders its output as it
  computes. Metabolism flux balance updates in real time. Transcription
  events appear as gene expression pulses. Translation counts increment.
  DNA replication progress bar fills.
- **DataBinding channels**: `TimeSeries` for metabolite concentrations,
  `Categorical` for gene essentiality calls, `Scalar` for growth rate,
  `Event` for cell cycle phase transitions
- **Interaction**: Click any gene → see its expression, translation,
  and essentiality status across all submodels simultaneously

### Paper C → Genome Exploration Surface

**Static figures**: Algorithm schematics, genome reduction trajectories,
viability landscapes.

**petalTongue transformation**:
- **Fitness landscape explorer**: 3D surface where each point is a genome
  design. Color = viability score. Navigate through the 53,451 genomes
  GAMA explored. Watch the genetic algorithm population evolve in real time.
- **DataBinding channels**: `Grid2D` for fitness landscape, `Trajectory`
  for algorithm path through genome space, `Categorical` for gene
  essentiality per design
- **Interaction**: Click any genome design → see which genes are removed,
  viability score, and which submodels fail

### Paper E → 3D Living Cell

**Static figures**: 3D cell snapshots, metabolite time courses, ribosome
distribution heatmaps, mRNA spatial plots.

**petalTongue transformation**:
- **Live 3D cell**: Particles move and react in real time inside a 3D
  cell geometry. Ribosomes translate, mRNA diffuses, metabolites
  concentrate. The 3D view IS the simulation.
- **DataBinding channels**: `Spatial3D` for particle positions,
  `TimeSeries` for metabolite concentrations, `Histogram` for molecular
  distributions, `Event` for stochastic reaction events
- **Interaction**: Pause/rewind. Select a molecular species → highlight
  all instances. Select a region → see local concentrations. Toggle
  between scales (molecular, cellular, population).

### Paper F → Molecular Cinema

**Static figures**: Cell rendering, protein distribution maps, membrane
cross-sections, diffusion analysis plots, ribosome crowding images.

**petalTongue transformation**:
- **Live trajectory viewer**: 561 million CG beads rendered in real time
  (LOD rendering for performance). Membrane undulates. Proteins diffuse.
  Ribosomes cluster near mRNA.
- **DataBinding channels**: `Spatial3D` for bead positions (LOD-streamed),
  `TimeSeries` for diffusion coefficients, `Density` for spatial
  concentration fields, `Surface` for membrane shape
- **Interaction**: Slice the cell at any plane. Zoom from whole-cell to
  single-protein. Color by species, by mobility, by interaction partner.
  Time slider across the 200 ns trajectory.

### Paper G → The Cell Cycle Film

**Static figures**: Cell cycle timeline, chromosome dynamics snapshots,
division sequence images, metabolic oscillation plots.

**petalTongue transformation**:
- **4D cell cycle visualization**: Birth → growth → DNA replication →
  chromosome segregation → constriction → division → two daughters.
  The entire cell cycle as a continuous, interactive 4D rendering.
- **DataBinding channels**: All channels from Papers E and F, plus
  `Morphology` for cell shape evolution, `Polymer` for chromosome
  configuration, `Timeline` for cell cycle phase progression
- **Interaction**: Scrub through the cell cycle. Compare mother and
  daughter cells. Overlay metabolic state on morphological state. Watch
  the FtsZ ring form and constrict in 3D.

### The Presentational Argument

The paper lineage progresses from text + static plots (Paper A, 2012)
toward increasingly visual representations (Paper G, 2026). But even
Paper G generates figures post-hoc. petalTongue completes the trajectory:
the visualization is not documentation of the computation — it is the
computation itself, rendered live, interactive, and reproducible.

A researcher viewing the Paper G rebuild in petalTongue sees the cell
cycle unfold in 4D. They can pause at chromosome segregation, inspect
the forces on the FtsZ ring, check the metabolite concentrations at that
exact moment, trace the provenance of every parameter to its source
publication, and verify the BLAKE3 hash of the simulation state. Then
they can resume, and the cell divides.

The figure in the resulting publication is a screenshot of that moment.
The reproduction artifact is the deploy graph TOML. Anyone with a
NUCLEUS re-runs it on their own hardware and sees the same cell divide.

---

## 8. Evolution Targets Exposed

What NUCLEUS needs to evolve to fully express these workflows. Each
gap is a concrete evolution target — not a blocker, but a task that
the rebuild itself drives.

### New toadStool Workload Types

| Workload | Paper | Description | Priority |
|----------|-------|-------------|----------|
| `lattice_microbes` | E, G | C++/CUDA spatial stochastic simulator. External binary dispatch with GPU allocation. | High — core of Papers E and G |
| `gromacs_md` | F, G | GROMACS molecular dynamics. External binary with trajectory capture into NestGate. | High — core of Paper F |
| `matlab_interop` | A, C | MATLAB runtime dispatch for legacy model execution (bridge to Rust reimplementation). | Medium — enables immediate Paper A rebuild before Rust port |
| `genetic_algorithm` | C | Parallelizable genome search. May be expressible as existing barraCuda parallel map. | Medium |
| `openMM` | F | Alternative MD engine for validation. Same dispatch pattern as GROMACS. | Low — validation-only |

### New NestGate Storage Patterns

| Pattern | Paper | Description |
|---------|-------|-------------|
| MD trajectory frames | F, G | Per-frame content addressing for XTC/TRR binary trajectories. Frame-level random access. |
| Large simulation state | E, G | Serialized 3D grid states (GB-scale per snapshot). Chunked, content-addressed. |
| Genome library | C | 53,451 genome designs, each content-addressed with viability metadata. |
| Parameter snapshot | All | Database-version-pinned parameter sets (BRENDA v2024.1, not just "BRENDA"). |

### New petalTongue Channels

| Channel | Paper | Description |
|---------|-------|-------------|
| `Spatial3D` | E, F, G | 3D molecular/particle visualization with LOD streaming |
| `Morphology` | G | Cell shape evolution over time (deformable mesh) |
| `Polymer` | G | Chromosome bead-spring configuration rendering |
| `FitnessLandscape` | C | 2D/3D fitness landscape navigation with population trajectory |
| `MolecularStructure` | F | Protein/membrane CG structure rendering |

### New barraCuda Kernels

| Kernel | Paper | Description |
|--------|-------|-------------|
| CG force field evaluation | F, G | Martini 3 nonbonded + bonded potentials on GPU (WGSL) |
| Reaction-diffusion (RDME) | E, G | Spatial stochastic simulation on cubic lattice |
| FBA linear programming | A | Flux balance analysis LP solver |
| Stochastic simulation (Gillespie) | A, E | Exact and tau-leaping SSA on GPU |
| Chromosome polymer dynamics | G | Bead-spring with motor protein forces |
| Membrane shape solver | G | Helfrich energy minimization for deformable mesh |

### Parameter Provenance Patterns

| Pattern | Description |
|---------|-------------|
| Database snapshot pinning | BRENDA/TECRdb/UniProt queries recorded with database version, query timestamp, and result BLAKE3 hash |
| Literature parameter certificates | Each parameter from a publication gets a loamSpine certificate: source DOI, table/figure reference, extraction method, BLAKE3 of extracted value |
| Cross-paper parameter diff | When Paper C inherits Paper A's parameters, the diff is structural: loamSpine certificate chain from A to C with any modifications tracked |
| AlphaFold version pinning | AF2/AF3 predictions pinned to model weights version + confidence scores, not just "AlphaFold predicted" |

---

## 9. The Publication Argument

### What Gets Published

The rebuild produces multiple publishable artifacts, each anchored via
the sovereign publication pipeline:

1. **This document** (CC-BY-SA 4.0) — The analysis, composition blueprints,
   and provenance audit. A methods paper describing how NUCLEUS expresses
   the whole-cell modeling lineage.

2. **The rebuild itself** (AGPL-3.0-or-later) — Deploy graph TOML files,
   spring experiments validating each paper's composition, and the
   provenance DAGs recording every computation step.

3. **Provenance-complete reproductions** — For each paper (A, C, E, F, G),
   a reproduction with every parameter content-addressed, every computation
   step DAG-recorded, and every intermediate result stored in NestGate.
   These are the originals, rebuilt with the sheet music finally written down.

4. **Live computation surfaces** — petalTongue renderings of every paper's
   key figures as interactive, reproducible visualizations. Screenshots
   become paper figures. Deploy graphs become reproduction artifacts.

5. **The provenance audit** — A machine-readable inventory of every jelly
   string in the original lineage, with the structural solution applied.
   This is independently valuable: other groups can use the audit to
   assess provenance debt in their own whole-cell models.

### The Sovereign Publication Pipeline

Each artifact follows the pipeline from
`gen4/thesis/THE_SOVEREIGN_PUBLICATION.md`:

```
Computation (NUCLEUS deploy graph)
  → DAG recording (rhizoCrypt: every step content-addressed)
  → Signing (BearDog ed25519: scientist identity)
  → Dehydration (loamSpine: permanent ledger with Merkle root)
  → Attribution (sweetGrass: braid spanning all contributors)
  → Anchoring (BTC/ETH: cryptographic timestamp)
  → Publication (NestGate: content-addressed, globally retrievable)
```

The result is not a PDF that says "we did X and got Y." It is a
cryptographic proof that X was done, Y was obtained, using parameters
P₁...Pₙ each traced to their source, on hardware H at time T, by
contributors C₁...Cₘ each with ed25519 attestation.

### Why This Lineage

The whole-cell modeling lineage is the ideal first foundation because:

1. **High impact**: Cell (2012, 2022, 2026), Nature Communications,
   PNAS. Thousands of citations. The scientific community knows this work.

2. **Maximum provenance debt**: 14 years of parameter inheritance across
   organisms and toolchains. The jelly strings are thick and numerous.

3. **Multi-scale composition**: Kinetic + spatial + structural + genomic.
   Tests every NUCLEUS layer.

4. **Existing spring overlap**: hotSpring (MD/GPU), wetSpring (genomics),
   healthSpring (kinetics) already validate subsets. The composition is
   the new challenge.

5. **Community connection**: ABG members (Dennis, Mark) are actively
   interested in whole-cell modeling and MD simulation. The rebuild
   creates tangible value for the community Tamison is joining.

6. **Extensibility**: Once rebuilt, the lineage becomes a platform.
   New hypotheses can be tested by modifying the deploy graph — change
   a parameter, re-run, and the provenance chain captures the delta.
   Hand the NUCLEUS composition to another researcher, and they can
   explore, extend, and generate novel hypotheses with full structural
   support.

### The Handoff Vision

When complete, this foundation enables:

- A researcher downloads the deploy graph TOML
- They run it on their own NUCLEUS (sovereign hardware)
- The entire whole-cell modeling lineage rebuilds on their machine
- Every parameter is traceable to its source
- Every computation is reproducible
- Every figure is a live, interactive view they can explore
- They modify a parameter (new kinetic constant, new protein structure)
- The provenance chain captures the modification with attribution
- They publish the extension as a new sweetGrass braid
- The original authors receive attribution credit automatically

This is what "review, explore, extend, and generate new novel hypotheses
when we hand it to others" looks like in practice. The data has integrity.
The provenance is structural. The science travels.

---

## Appendix: Relationship to Existing ABG Work

This foundation connects to the ABG engagement documented in:

- `attsi/non-anon/contact/ABG/ABG_ANALYSIS.md` — Community analysis
  identifying overlap between ABG proposals and ecoPrimals capabilities
- `attsi/non-anon/contact/ABG/ABG_OUTREACH_STRATEGY.md` — Phased
  human-first outreach plan (Tamison as microbiologist peer)
- `attsi/non-anon/contact/ABG/SPOREPRINT_TRACTABILITY_AUDIT.md` —
  Documentation clarity assessment

The rebuild serves the outreach strategy without being an outreach
document. When ABG members encounter whole-cell modeling challenges,
the structural solutions exist — proven, provenance-complete, and
running on sovereign hardware. The foundation is the evidence that
backs the conversation.

---

*The original authors built the whole-cell model on jelly strings and
trust-me data because those were the only tools available. The strings
held — the science is real, the papers are cited, the field advanced.
This foundation does not replace their work. It rebuilds it with the
structural provenance they deserved from the start, and creates a
platform where the next 14 years of whole-cell modeling can stand on
verified ground.*
