# Faculty → Spring Profiles

**Status**: Working draft  
**Purpose**: Map known faculty to ecoPrimals springs, identify candidate papers for reproduction  
**Last Updated**: February 12, 2026

---

## How This Document Works

Each professor is profiled with:
1. **Connection** — how we know them and what spring(s) their work maps to
2. **Key Papers** — candidate publications for Phase A reproduction in the springs
3. **BarraCUDA Relevance** — which GPU primitives their work exercises
4. **Status** — what has already been reproduced vs. what is candidate work

---

## hotSpring — Computational Plasma Physics

### Michael Murillo
**Associate Professor, CMSE, MSU**  
https://engineering.msu.edu/faculty/michael-murillo  
**Connection**: MSDS professor (master's program)

**Spring Status**: 195/195 Phase A checks PASS, Phase C GPU MD validated (9/9 Yukawa)

**Reproduced Papers**:
| Paper | Status | Checks |
|-------|--------|--------|
| Silvestri, Diaw, Murillo (2024) "Surrogate learning" — Nature Machine Intelligence | Reproduced | hotSpring Phase A |
| Sarkas MD — Yukawa OCP | Reproduced + GPU | Phase A + Phase C |
| Two-Temperature Model (TTM) | Reproduced | Phase A |

**Candidate Papers for Future Reproduction**:
- Stanton & Murillo (2016) "Ionic transport in high-energy-density matter" — J. Phys. A
- Murillo & Weisheit (1998) "Dense plasmas, screened interactions, and atomic ionization" — Physics Reports
- Diaw & Murillo (2023) "Generalized Hydrodynamics Model for Strongly Coupled Plasmas"

**BarraCUDA primitives exercised**: GEMM, particle integration (Velocity Verlet), pair forces (Yukawa), MLP surrogate, RBF interpolation

---

## airSpring — Evapotranspiration & Precision Irrigation

### Younsuk Dong
**Assistant Professor, Biosystems & Agricultural Engineering, MSU**  
https://www.egr.msu.edu/bae/water/irrigation/  
**Connection**: New lab job (2026)

**Spring Status**: 142/142 Phase A checks PASS, 918 station-days real data pipeline

**Reproduced Papers**:
| Paper | Status | Checks |
|-------|--------|--------|
| Dong (2020) sensor validation | Reproduced | airSpring Phase A |
| Dong (2024) soil calibration | Reproduced | airSpring Phase A |
| FAO-56 Penman-Monteith reference ET₀ | Reproduced | airSpring Phase A |

**Candidate Papers for Future Reproduction**:
- Dong et al. — IoT soil moisture sensor network calibration (fieldwork data)
- Allen et al. (1998) FAO-56 — extended crop coefficient studies
- Regional ET₀ model comparisons across Michigan microclimates

**BarraCUDA primitives exercised**: MLP surrogate (FAO-56 approximation), time-series LSTM (weather forecasting), data pipeline batch processing

---

## wetSpring — Microbial Ecology, Phage Biology, Environmental Chemistry

### Jesse Cahill
**Senior MTS, Sandia National Laboratories (Bioscience)**  
**Connection**: Time at Sandia

**Spring Area**: Track 1 — Life Science (algae ponds, phage biocontrol)

**Candidate Papers for Reproduction**:
- Cahill et al. — Phage-mediated biocontrol in algal raceway ponds
- Phage lifecycle dynamics and predator-prey oscillations in bioreactor systems
- Algal pond crash forensics — temporal metagenomics

**BarraCUDA relevance**: Time-series anomaly detection (pond crash prediction), population dynamics ODE solvers

---

### Chuck Smallwood
**Principal MTS, Sandia National Laboratories (Bioscience)**  
**Connection**: Time at Sandia

**Spring Area**: Track 1 — Life Science (metagenomics, microbial community monitoring)

**Candidate Papers for Reproduction**:
- Smallwood et al. — Raceway pond metagenomic surveillance pipelines
- Microbial community stability metrics under perturbation

**BarraCUDA relevance**: Sequence alignment (GEMM-heavy), dimensionality reduction, diversity index computation

---

### A. Daniel Jones
**Professor, Biochemistry & Molecular Biology / Chemistry, MSU**  
https://www.canr.msu.edu/news/center-for-pfas-research-faculty-spotlight-a-daniel-jones  
**Connection**: PFAS job

**Spring Area**: Track 2 — PFAS / blueFish

**Candidate Papers for Reproduction**:
- Jones et al. — PFAS mass spectrometry detection pipelines
- High-resolution mass spec peak identification and quantification
- Environmental PFAS fate-and-transport modeling

**BarraCUDA relevance**: Signal processing (FFT, peak detection), spectral analysis shaders, anomaly detection in analytical chemistry data

---

### Christopher Waters
**Professor, Microbiology, Genetics & Immunology, MSU**  
https://directory.natsci.msu.edu/directory/Profiles/Person/101708  
https://mgi.natsci.msu.edu/labs/waters-lab/  
watersc3@msu.edu  
**Connection**: Undergraduate professor

**Spring Area**: wetSpring Track 1 — Microbial signaling, biofilm dynamics, quorum sensing

**Key Research Themes**:
1. **c-di-GMP signaling** — second messenger controlling biofilm ↔ motility switch in V. cholerae
2. **Quorum sensing** — density-dependent gene regulation via autoinducers
3. **Integration of signaling pathways** — c-di-GMP + quorum sensing convergence
4. **Phage defense** — deoxycytidine deaminase protection (Nature Microbiology 2022)
5. **Cancer immunotherapy** — cyclic di-nucleotides as immune adjuvants

**Candidate Papers for Reproduction**:

| Paper | Domain | Spring Relevance |
|-------|--------|-----------------|
| Waters et al. (2008) "Quorum Sensing Controls Biofilm Formation in V. cholerae Through Modulation of Cyclic Di-GMP." J Bacteriology | Signaling dynamics | wetSpring: ODE models of c-di-GMP concentration ↔ biofilm phenotype. Population-level signaling = quorum noise problem |
| Massie et al. (2012) "Quantification of High Specificity Cyclic di-GMP Signaling." PNAS | Signal specificity | groundSpring: How do cells resolve signal from noise when 60+ enzymes control a single diffusible molecule? |
| Hsueh, Severin et al. (2022) "A Broadly Conserved Deoxycytidine Deaminase Protects Bacteria from Phage Infection." Nature Microbiology | Phage defense | wetSpring: Phage-bacteria arms race dynamics. Evolutionary game theory models |
| Bruger & Waters (2018) "Maximizing Growth Yield and Dispersal via QS Promotes Cooperation in Vibrio Bacteria." AEM | Cooperation evolution | neuralSpring: Game-theoretic optimization, evolutionary strategy landscapes |
| Fernandez et al. (2020) "V. cholerae adapts to sessile and motile lifestyles by c-di-GMP regulation of cell shape." PNAS | Morphological adaptation | groundSpring: Phenotypic switching as bistable dynamical system. Bifurcation analysis |
| Mhatre et al. (2020) "One gene, multiple ecological strategies: a biofilm regulator is a capacitor for sustainable diversity." PNAS | Ecological diversity | neuralSpring: Constrained evolution — single regulatory node enabling phenotypic diversity |
| Waters (2021) "Au naturale: use of biologically derived cyclic di-nucleotides for cancer immunotherapy." Open Biol | Applied immunology | wetSpring: Bridge from fundamental microbiology to therapeutic applications |
| Srivastava et al. (2011) "Integration of Cyclic di-GMP and Quorum Sensing in the Control of vpsT and aphA." J Bacteriology | Pathway integration | neuralSpring: Multi-input regulatory network = attention mechanism analog |

**BarraCUDA relevance**: ODE/PDE solvers (reaction-diffusion for signaling), stochastic simulation (Gillespie algorithm for quorum sensing), bifurcation analysis, graph computation (regulatory networks → neuralAPI pathway graphs)

---

## Master's Program Professors — Computational Methods

### Emily Dolson
**Assistant Professor, Computer Science & Engineering, MSU**  
https://engineering.msu.edu/directory/faculty/dolsonem  
dolsonem@msu.edu  
**Connection**: Master's program professor  
**Core faculty**: Ecology, Evolution, and Behavior program

**Key Research Themes**:
1. **Controlling evolutionary trajectories** — counterdiabatic driving applied to evolution
2. **Open-ended evolution** — measuring when systems produce genuine novelty
3. **Eco-evolutionary dynamics** — ecology and evolution as coupled processes
4. **Mathematical oncology** — evolutionary dynamics of cancer

**Candidate Papers for Reproduction**:

| Paper | Domain | Spring Relevance |
|-------|--------|-----------------|
| Iram, Dolson et al. (2020) "Controlling the speed and trajectory of evolution with counterdiabatic driving." Nature Physics | Evolutionary control theory | neuralSpring: Constrained evolution formalized — directly validates gen3/CONSTRAINED_EVOLUTION_FORMAL.md thesis. Can we reproduce the counterdiabatic protocol computationally? |
| Dolson & Vostinar et al. (2019) "The MODES Toolbox: Measurements of Open-Ended Dynamics in Evolving Systems." Artificial Life | Evolutionary metrics | neuralSpring: Metrics for measuring whether BarraCUDA's constrained evolution produces open-ended innovation |
| Dolson & Ofria (2018) "Ecological Theory Provides Insights about Evolutionary Computation." GECCO | Theory bridge | neuralSpring: Ecological dynamics in evolutionary algorithms — maps to primal competition/cooperation in biomeOS |
| Dolson et al. (2023) "The ecology-evolution continuum and the origin of life." J R Soc Interface | Origins of life | wetSpring + groundSpring: Emergence of organization from chemical noise |
| Dolson et al. (2022) "Artificial selection methods from evolutionary computing show promise for directed evolution of microbes." eLife | Directed evolution | wetSpring: Computational → wet lab bridge. Directed evolution of microbial communities |
| Foreback, Bohm, Dolson (2025) "Leveraging Heterogeneous Controller Representations for Evolutionary Swarm Robotics." IEEE | Swarm intelligence | neuralSpring: Heterogeneous representations ↔ primal diversity. Different primals as different controller architectures |

**BarraCUDA relevance**: Fitness landscape evaluation (GEMM), population simulation (parallel agents), evolutionary optimization (genetic algorithm shaders), diversity metrics computation

**Critical connection to gen3/**: Dolson's work on counterdiabatic driving of evolution is the closest published analog to the constrained evolution methodology described in `CONSTRAINED_EVOLUTION_FORMAL.md`. Reproducing Iram et al. (2020) would provide external validation of the theoretical framework.

---

### Kevin Liu
**Associate Professor, CMSE, MSU**  
https://engineering.msu.edu/directory/faculty/kjl  
kjl@msu.edu  
**Connection**: Master's program professor  
**Faculty in**: Genetics & Genome Sciences, Ecology, Evolution & Behavior

**Key Research Themes**:
1. **Phylogenetic inference at scale** — SATé/SATé-II for massive tree estimation
2. **Introgression detection** — PhyloNet-HMM for gene flow across species
3. **Comparative genomics** — detecting adaptive introgression in eukaryotes
4. **Resampling methods** — bootstrap and RAWR for phylogenetic confidence

**Candidate Papers for Reproduction**:

| Paper | Domain | Spring Relevance |
|-------|--------|-----------------|
| Liu et al. (2009) "Rapid and accurate large-scale coestimation of sequence alignments and phylogenetic trees." Science | Phylogenetics | neuralSpring: Divide-and-conquer + iterative refinement = surrogate + optimization loop. SATé's co-estimation mirrors biomeOS pathway iteration |
| Liu et al. (2014) "An HMM-based Comparative Genomic Framework for Detecting Introgression in Eukaryotes." PLoS Comp Bio | HMM inference | neuralSpring: PhyloNet-HMM is a Hidden Markov Model — validates LSTM/sequence model primitives. State-space models on genomic data |
| Liu et al. (2015) "Interspecific Introgressive Origin of Genomic Diversity in the House Mouse." PNAS | Adaptive introgression | wetSpring + neuralSpring: Gene flow detection = transfer learning analog. Introgression = knowledge transfer between species |
| Wang et al. (2021) "Build a better bootstrap and the RAWR shall beat a random path to your door." Bioinformatics (ISMB) | Statistical resampling | groundSpring: Bootstrap/resampling methods for confidence estimation on noisy phylogenetic data |
| Alamin & Liu (2024) "Phylogenetic Placement of Aligned Genomes and Metagenomes with Non-tree-like Evolutionary Histories." IEEE/ACM TCBB | Metagenomics | wetSpring: Metagenomic placement = classifying environmental samples. Directly applicable to pond/soil microbiome analysis |
| Zheng et al. (2023) "The Impact of Species Tree Estimation Error on Cophylogenetic Reconstruction." BCB (top 10%) | Cophylogenetics | wetSpring: Host-microbe coevolution — fungal endosymbiont studies with Bonito lab |

**BarraCUDA relevance**: Sequence alignment (GEMM-heavy Smith-Waterman), HMM forward/backward/Viterbi (matrix operations), phylogenetic likelihood computation (parallel tree evaluation), bootstrap resampling (embarrassingly parallel)

**Working manuscripts to watch**:
- "A phylogenomic study of adaptive co-evolution between early diverging fungi and obligate bacterial endosymbionts" — direct wetSpring relevance
- "Scalable statistical inference of species phylogenies from large-scale resequenced genomic datasets" — HPC/GPU candidate

---

### Alexei Bazavov
**Associate Professor, CMSE & Physics & Astronomy, MSU**  
https://directory.natsci.msu.edu/directory/Profiles/Person/101033  
bazavov@msu.edu  
**Connection**: Master's program professor  
**Affiliations**: CERN Theory Division, Fermilab Lattice, HPQCD, MILC Collaborations

**Key Research Themes**:
1. **Lattice QCD** — ab initio computation of strong force properties
2. **Hadronic vacuum polarization** — precision calculation for muon g-2
3. **Inverse problems** — spectral reconstruction from lattice data
4. **Parallel algorithms** — molecular dynamics on lattice gauge configurations

**Candidate Papers for Reproduction**:

| Paper | Domain | Spring Relevance |
|-------|--------|-----------------|
| Bazavov [HotQCD] (2014) "The QCD equation of state." Nuclear Physics A | Equation of state | hotSpring: Lattice QCD EOS ↔ Sarkas plasma EOS. Both compute thermodynamic properties of strongly coupled systems via particle methods |
| Bazavov et al. (2025) "Hadronic vacuum polarization for the muon g-2: Complete short and intermediate windows." Phys Rev D | Precision physics | groundSpring: Subpercent precision from noisy lattice data. Statistical analysis, jackknife/bootstrap error estimation |
| Bazavov et al. (2016) "Polyakov loop in 2+1 flavor QCD from low to high temperatures." Phys Rev D | Phase transitions | hotSpring: Deconfinement transition in QCD ↔ phase transitions in dense plasmas |
| Bazavov et al. (2016) "Curvature of the freeze-out line in heavy ion collisions." Phys Rev D | Heavy ion physics | groundSpring: Inverse problem — inferring freeze-out conditions from experimental observables |
| Bazavov et al. (2015) "Gauge-invariant implementation of the Abelian Higgs model on optical lattices." Phys Rev D | Quantum simulation | neuralSpring: Mapping quantum field theories onto computational lattices — analog computing concepts |
| (2025) Spectral reconstruction inverse problem in lattice QCD (arXiv 2501.12259) | Inverse problems | groundSpring: Spectral reconstruction = signal recovery from incomplete/noisy data. Direct connection to seismic inversion and sensor noise decomposition |

**BarraCUDA relevance**: Lattice gauge theory requires: GEMM (link multiplication), FFT (momentum-space operations), parallel molecular dynamics (HMC algorithm), reduction operations (gauge averaging), stochastic estimators. Massive GPU workload — ideal BarraCUDA target.

**Critical connection to hotSpring**: Bazavov's lattice QCD and Murillo's plasma physics are both studying strongly coupled many-body systems. The computational methods overlap significantly — both use molecular dynamics, both need equation of state calculations, both deal with long-range correlations. A shared BarraCUDA kernel library could serve both.

---

### Ilya Kachkovskiy
**Assistant Professor, Department of Mathematics, MSU**  
https://users.math.msu.edu/users/ikachkov/  
ikachkov@msu.edu  
**Connection**: Sold the NucBox M6 on Facebook Marketplace; brief GPU conversation  
**Previously at**: Institute for Advanced Study, UC Irvine  
**NSF funded**: DMS-1758326 "Spectral theory of periodic and quasiperiodic quantum systems"

**Key Research Themes**:
1. **Anderson localization** — how disorder causes quantum waves to localize (absence of transport in disordered media)
2. **Spectral theory of quasiperiodic operators** — eigenvalue structure of systems that are "almost periodic" (structured noise)
3. **Transport in quantum spin systems** — energy/information propagation through spin chains
4. **Almost commuting operators** — approximate symmetries in quantum systems (C*-algebra framework)

**Candidate Papers for Reproduction**:

| Paper | Domain | Spring Relevance |
|-------|--------|-----------------|
| Bourgain & Kachkovskiy (2018) "Anderson localization for two interacting quasiperiodic particles." GAFA | Localization theory | groundSpring: Anderson localization = signal trapped by noise. Two-particle case adds interaction — directly models how coupled noisy sensors affect each other |
| Jitomirskaya & Kachkovskiy (2018) "All couplings localization for quasiperiodic operators with Lipschitz monotone potentials." JEMS | Quasiperiodic systems | groundSpring + hotSpring: Quasiperiodic = structured noise with incommensurate frequencies. Maps to sensor drift, seasonal + sub-seasonal climate patterns, lattice vibrations |
| Filonov & Kachkovskiy (2018) "On the structure of band edges of 2d periodic elliptic operators." Acta Math | Band structure | hotSpring: Band edges determine electronic/phononic transport properties. Same eigenvalue mathematics as Bazavov's spectral reconstruction |
| Kachkovskiy (2016) "On transport properties of isotropic quasiperiodic XY spin chains." CMP | Quantum transport | hotSpring: Spin chain transport ↔ Murillo's plasma energy transport. Both ask: how does energy propagate through a coupled many-body system? |
| Kachkovskiy & Safarov (2016) "Distance to normal elements in C*-algebras of real rank zero." JAMS | Operator theory | neuralSpring: Approximate commutativity = approximate symmetry. Relevant to understanding when neural network layers approximately commute (skip connections, residual nets) |

**BarraCUDA relevance**: Eigenvalue solvers (iterative diagonalization, Lanczos), matrix exponentiation (time evolution of quantum systems), sparse matrix-vector products (Hamiltonian action on wavefunctions), FFT (momentum-space transformations). The spectral methods require f64 precision — same requirement as hotSpring's plasma MD and Bazavov's lattice QCD.

**Why this matters**: Kachkovskiy provides the *mathematical* layer that sits between Murillo's physics (transport in classical plasmas) and Bazavov's physics (transport in quantum field theories). His spectral theory is the eigenvalue mathematics both of them use but neither of them proves. Anderson localization — the core of his research — is the rigorous mathematical framework for "when does signal propagate vs. when does noise trap it?" That's groundSpring's central question stated in the language of quantum mechanics.

**Co-author network**: Jean Bourgain (Fields Medalist, IAS — deceased 2018), Svetlana Jitomirskaya (UCI, Dannie Heineman Prize), Nikolay Filonov (Steklov Institute), Yuri Safarov (King's College London). This is a tier-1 mathematics pedigree.

---

## Cross-Spring Faculty Connections

```
                    hotSpring (Murillo, Bazavov, Kachkovskiy)
                    ┌──────────────────────────┐
                    │ Strongly coupled           │
                    │ many-body systems          │
                    │ MD, EOS, spectral theory   │
                    │ GPU compute                │
                    └──────┬─────────────────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
   groundSpring            │         neuralSpring
   (Bazavov inverse,       │    (Dolson evolution,
    Kachkovskiy localize)  │     Liu HMM/phylo,
   ┌──────────────┐        │     Bazavov parallel,
   │ Inverse probs│        │     Kachkovskiy spectral)
   │ Noise/signal │        │    ┌──────────────┐
   │ Anderson loc │        │    │ ML primitives │
   │ Spectral recon│       │    │ Evolutionary  │
   └──────┬───────┘        │    │ optimization  │
          │                │    └──────┬───────┘
          │                │           │
          └────────┬───────┘───────────┘
                   │
            wetSpring (Cahill, Smallwood, Jones, Waters, Liu)
            ┌──────────────────────────┐
            │ Microbial ecology         │
            │ Metagenomics              │
            │ Quorum sensing/signaling  │
            │ PFAS detection            │
            │ Phage dynamics            │
            └──────────────────────────┘
```

## Priority Reproduction Candidates (Next Phase)

Ranked by: (1) direct spring relevance, (2) reproducibility, (3) BarraCUDA kernel coverage

### Tier 1 — High priority, clear reproduction path
1. **Iram, Dolson et al. (2020)** — Nature Physics — Counterdiabatic evolution control → validates constrained evolution thesis
2. **Waters et al. (2008)** — J Bacteriology — c-di-GMP/QS biofilm model → ODE system, fully specified
3. **Liu et al. (2014)** — PLoS Comp Bio — PhyloNet-HMM introgression → HMM implementation validates sequence model primitives
4. **Bazavov [HotQCD] (2014)** — Nuclear Physics A — QCD EOS → extends hotSpring beyond plasma

### Tier 2 — Strong candidates, may need data access
5. **Dolson et al. (2019)** — MODES Toolbox — Open-ended evolution metrics → apply to BarraCUDA's own evolution
6. **Massie et al. (2012)** — PNAS — c-di-GMP signaling specificity → quantitative signaling model
7. **Liu et al. (2009)** — Science — SATé phylogenetic estimation → large-scale divide-and-conquer benchmark
8. **Hsueh et al. (2022)** — Nature Microbiology — Phage defense deaminase → evolutionary arms race dynamics

### Tier 2.5 — Mathematical foundations, strengthens multiple springs
9. **Bourgain & Kachkovskiy (2018)** — GAFA — Anderson localization for interacting particles → groundSpring noise/signal theory, computational eigenvalue methods for BarraCUDA
10. **Kachkovskiy (2016)** — CMP — Quasiperiodic spin chain transport → hotSpring plasma transport bridge, validates Lanczos/spectral BarraCUDA primitives

### Tier 3 — Longer horizon, connect to broader themes
11. **Bazavov et al. (2025)** — Phys Rev D — Muon g-2 HVP → precision lattice computation
12. **Fernandez et al. (2020)** — PNAS — Cell shape regulation → bistable dynamical systems
13. **Dolson (2023)** — J R Soc Interface — Ecology-evolution continuum → origin-of-life context
14. **Liu working manuscript** — Fungi-bacteria coevolution → cophylogenetic methods for wetSpring
15. **Filonov & Kachkovskiy (2018)** — Acta Math — 2D band edge structure → electronic/phononic transport, deep eigenvalue mathematics
