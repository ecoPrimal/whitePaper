# Faculty Network — Personal Interactions & Paper Reproductions

**Purpose**: Document the personal connections behind the science. Each professor here is someone whose work was reproduced in the springs or whose research directly informs the constrained evolution thesis. The papers listed are the ones used to explore and evolve the primals — the working material, not the formal thesis citations.

**Relationship to `thesis/`**: The thesis (`gen3/thesis/`) discusses these papers academically. This document tells the story of *how* and *why* each person's work ended up in the springs.

**Relationship to `contacts.md`**: `attsi/non-anon/contacts.md` is the contact directory. This document is the narrative.

---

## 1. Michael Murillo — hotSpring Anchor

**Title**: Professor, Computational Mathematics, Science & Engineering, MSU
**URL**: https://engineering.msu.edu/faculty/michael-murillo
**Connection**: MSDS professor — taught CMSE 890 (Applied Machine Learning, Spring 2025)

### How We Met

Murillo taught Applied Machine Learning in the final semester of the master's program. The course introduced reservoir computing, echo state networks, and neuromorphic computing — which led directly to the BrainChip Akida work in ToadStool and the metalForge mixed-substrate pipelines. He is one of the few faculty who bridges computational plasma physics and machine learning in a single research program.

The neuromorphic benchmark datasheet (`attsi/non-anon/contact/murillo/neuromorphic_benchmark_datasheet.md`) was drafted as a follow-up to share the Akida results. The hotSpring repository was built to reproduce his group's published work as a credibility artifact before any outreach.

### Papers Reproduced in Springs

#### hotSpring (195/195 checks)

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| Sarkas Yukawa OCP MD | Silvestri, Stanton & Murillo | Phase A–C | 9/9 PP cases | BarraCUDA GPU molecular dynamics at f64 precision. 0.000% energy drift over 80,000 steps. |
| Two-Temperature Model (TTM) | Stanton & Murillo | Phase B | 6/6 | Laser–plasma electron-ion equilibration dynamics. |
| Surrogate learning for transport | Diaw, Murillo, Stanton — *Nature Machine Intelligence* (2024) | Phase D | 15/15 | Neural surrogate learning methodology. DeepONet and PINN training on plasma transport. |
| Ionic transport in HED matter | Stanton & Murillo — *Phys Rev Lett* 116, 075002 (2016) | Phase E | 13/13 | Green–Kubo transport coefficients. Diffusion and viscosity from equilibrium MD. |
| Dense plasmas & screened interactions | Murillo & Weisheit — *Physics Reports* (1998) | Phase F | 23/23 | Screened Coulomb potential, bound state physics, Debye screening. |

#### neuralSpring

| Paper | Experiment | Checks | What It Validated |
|-------|------------|-------:|-------------------|
| Diaw et al. (2024) surrogate methodology | Exp 004 | 15/15 | PINN/DeepONet reproductions using Murillo's transport learning framework. |

### What His Work Proved About ecoPrimals

Murillo's plasma physics papers were the first real science run through BarraCUDA. The Sarkas Yukawa OCP MD was the proving ground: if BarraCUDA could maintain 0.000% energy drift over 80,000 steps at f64 on a consumer GPU, it could do computational physics. Every subsequent spring experiment builds on that foundation.

The surrogate learning work (Diaw et al.) also bridged hotSpring and neuralSpring — the same neural architecture that learns plasma transport coefficients is the architecture that validates neuralSpring's ML primitives.

### Outreach Status

Email drafts prepared (`attsi/non-anon/contact/murillo/`). hotSpring repository is the credibility artifact — 195/195 checks on his group's published work, reproducible on consumer hardware. The neuromorphic benchmark datasheet covers the Akida ESN results from metalForge.

---

## 2. Younsuk Dong — airSpring Anchor

**Title**: Assistant Professor, Biosystems & Agricultural Engineering, MSU
**URL**: https://www.egr.msu.edu/bae/water/irrigation/
**Connection**: New lab job (2026)

### How We Met

Dong runs the precision irrigation lab in MSU's Biosystems & Agricultural Engineering department. The connection is professional — a new lab position in 2026. His group's work on soil sensor calibration and IoT irrigation in Michigan became the foundation for airSpring.

### Papers Reproduced in Springs

#### airSpring (326 checks)

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| FAO-56 Penman–Monteith | Allen et al. — FAO Irrigation & Drainage Paper 56 (1998) | Phase A | 64/64 | Reference evapotranspiration (ET₀). The standard equation for precision agriculture. |
| Soil sensor calibration | Dong et al. (2020) | Phase A | 36/36 | CS616 and EC5 sensor calibration curves. VWC from raw sensor output. |
| IoT irrigation pipeline | Dong et al. (2024) | Phase B | 24/24 | SoilWatch 10 integration, real-time irrigation scheduling. |
| Water balance | Allen et al. — FAO-56 Ch. 8 (1998) | Phase B | 18/18 | Soil water depletion, deep percolation, runoff. |
| Real data pipeline | Dong lab Michigan stations | Phase C | R² = 0.967 | 918 station-days across 100 Michigan stations (originally 6 MAWN stations). Python↔Rust cross-validation. |

### What His Work Proved About ecoPrimals

airSpring demonstrated that BarraCUDA and the primal infrastructure work beyond physics — in agricultural science with direct real-world application. The 918 station-days of real Michigan weather data, cross-validated between Python and Rust, showed the system handles noisy real-world sensor data, not just clean simulation.

The FAO-56 reproduction is also the foundation for groundSpring's error propagation experiments — the humidity-dominance finding (65.6% of ET₀ uncertainty) came from propagating sensor noise through the FAO-56 equation that airSpring validated.

### Outreach Status

Lab position is the connection. airSpring is built to demonstrate computational capability relevant to his research program.

---

## 3. Christopher Waters — wetSpring Track 1 (Microbial Signaling)

**Title**: Professor, Microbiology, Genetics & Immunology, MSU
**URL**: https://mgi.natsci.msu.edu/labs/waters-lab/
**Connection**: Undergraduate professor (MMG, MSU)

### How We Met

Waters taught in the Microbiology department during the undergraduate years. His lab works on bacterial signaling — cyclic di-GMP, quorum sensing, *Vibrio cholerae* biofilm regulation. The signaling work is where the biological understanding of constraint-mediated behavior became concrete: quorum sensing is a population-level response to environmental density constraints.

### Papers Reproduced in Springs

#### wetSpring

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| QS controls biofilm in *V. cholerae* | Waters et al. — *J Bacteriology* 190:2527–36 (2008) | Exp020 | ✓ | Quorum sensing ↔ c-di-GMP regulatory network. ODE model of signal integration. |
| High specificity c-di-GMP signaling | Massie et al. — *PNAS* 109:12746–51 (2012) | Exp022 | ✓ | Signal vs noise in molecular signaling. How cells distinguish real signals from crosstalk. |
| DcdV phage defense | Hsueh, Severin et al. — *Nature Microbiology* 7:1210 (2022) | Exp030 | ✓ | Deoxycytidine deaminase as phage defense. Innate immunity analog. |
| Cell shape regulation via c-di-GMP | Fernandez et al. — *PNAS* 117:29046 (2020) | Exp023 | ✓ | Phenotypic switching under environmental constraint. Bistable cell fate. |
| One gene, multiple strategies | Mhatre et al. — *PNAS* 117:21647 (2020) | Exp027 | ✓ | Single gene as capacitor for ecological diversity. Constraint producing innovation. |
| QS promotes cooperation | Bruger & Waters — *AEM* 84:e00402-18 (2018) | Exp025 | ✓ | Game-theoretic cooperation in microbial populations. |
| c-di-GMP + QS integration | Srivastava et al. — *J Bacteriology* 193:6331 (2011) | Exp024 | ✓ | Multi-input regulatory network. Signal fusion under noise. |

#### neuralSpring

| Paper | Experiment | Checks | What It Validated |
|-------|------------|-------:|-------------------|
| Bruger & Waters (2018) — QS cooperation | Exp (Waters track) | 8/8 | Game-theoretic ODE models. Cooperation dynamics as neural optimization. |
| Mhatre et al. (2020) — ecological strategies | Exp (Waters track) | 7/7 | Diversity capacitor modeled as stochastic switching. |
| Srivastava et al. (2011) — c-di-GMP + QS | Exp (Waters track) | 8/8 | Multi-input network as graph neural computation. |

#### groundSpring (queued)

Papers queued for noise/signal analysis: Massie et al. (signal specificity), Fernandez et al. (bistable switching), Srivastava et al. (multi-input fusion).

### What His Work Proved About ecoPrimals

The Waters lab papers are the clearest biological demonstration of constrained evolution's core argument. Quorum sensing is a population-level computational system that evolved under the constraint of molecular noise. The signaling specificity work (Massie et al.) directly addresses the signal-vs-noise problem that groundSpring formalizes computationally. And the "one gene, multiple strategies" paper (Mhatre et al.) is the biological precedent for the NTT→FFT phenomenon: one structure producing multiple functions under different selective pressures.

### Outreach Status

Not yet contacted. The wetSpring QS reproduction track is the credibility artifact.

---

## 4. Kevin Liu — wetSpring Track 1b (Phylogenetics) + neuralSpring

**Title**: Associate Professor, Computational Mathematics, Science & Engineering, MSU
**URL**: https://engineering.msu.edu/directory/faculty/kjl
**Connection**: MSDS professor (CMSE/CSE faculty)

### How We Met

Liu is on the CMSE/CSE faculty in the master's program. His research bridges computational genomics and machine learning — phylogenetic inference algorithms, HMM-based comparative genomics, and reticulate evolution. The phylogenetic methods became central to wetSpring's metagenomics pipeline.

### Papers Reproduced in Springs

#### wetSpring

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| PhyloNet-HMM introgression | Liu et al. — *PLoS Comp Bio* 10:e1003649 (2014) | Exp026, Exp037 | 42/42 (combined) | HMM-based introgression detection. Gene flow between species. |
| SATé alignment + tree coestimation | Liu et al. — *Science* 324:1561 (2009) | Exp033, Exp038 | Reproduced | Simultaneous alignment and phylogeny. Large-scale tree building. |
| Metagenomic placement | Alamin & Liu — *IEEE/ACM TCBB* (2024) | Exp032 | Reproduced | Placing metagenomic sequences onto reference phylogenies. |
| Species tree error in cophylogenetics | Zheng et al. — BCB (2023) | Exp034 | Reproduced | Host–microbe coevolution under tree uncertainty. |
| RAWR resampling | Wang et al. — *Bioinformatics* 37:i111 (2021) | Exp031 | Reproduced | Better bootstrap for phylogenetic confidence. |

#### neuralSpring

| Paper | Experiment | Checks | What It Validated |
|-------|------------|-------:|-------------------|
| PhyloNet-HMM | Exp (Liu track) | 10/10 | HMM as ML primitive. Forward-backward algorithm, Viterbi decoding. |
| SATé | Exp (Liu track) | 8/8 | Iterative alignment as optimization. Decomposition + recomposition. |
| Introgressive origin (house mouse) | Liu et al. — *PNAS* 112:196 (2015) | Exp (Liu track) | 8/8 | Gene flow model. Population genetics as constrained optimization. |

### What His Work Proved About ecoPrimals

Liu's phylogenetic tools test BarraCUDA's string and tree computation — alignment matrices, HMM transitions, tree traversal. These are structurally different from the f64 physics in hotSpring but use the same WGSL dispatch architecture. The fact that the same BarraCUDA infrastructure handles both plasma MD and phylogenetic HMMs is evidence for the generality of the constrained evolution output.

The RAWR bootstrap work also connects to groundSpring's uncertainty quantification — resampling as a tool for understanding statistical noise in phylogenetic inference.

### Outreach Status

Not yet contacted. wetSpring and neuralSpring reproductions are the credibility artifacts.

---

## 5. Alexei Bazavov — hotSpring (Lattice QCD)

**Title**: Associate Professor, CMSE & Physics & Astronomy, MSU
**URL**: https://directory.natsci.msu.edu/directory/Profiles/Person/101033
**Connection**: MSDS professor (CMSE/CSE faculty)

### How We Met

Bazavov is on the CMSE faculty in the master's program. He's a member of the HotQCD collaboration — the group that computes the QCD equation of state on lattice. His work connects to hotSpring's lattice gauge theory track and to groundSpring's inverse problems.

### Papers Reproduced in Springs

#### hotSpring

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| Pure gauge SU(3) Wilson action | Bazavov (subset) | Lattice QCD track | 12/12 | Wilson gauge action, heatbath + overrelaxation, plaquette observables. |
| Gauge-invariant Abelian Higgs | Bazavov et al. — *Phys Rev D* 92, 076003 (2015) | Lattice QCD track | 17/17 | U(1) + Higgs scalar, HMC integrator, phase structure. |
| QCD equation of state | Bazavov [HotQCD] — *Nucl Phys A* 931, 867 (2014) | GPU pipeline | Complete | Full lattice QCD thermodynamics. |
| Polyakov loop in 2+1 flavor QCD | Bazavov et al. — *Phys Rev D* 93, 114502 (2016) | GPU pipeline | Complete | Deconfinement order parameter. |
| Hadronic vacuum polarization (muon g-2) | Bazavov et al. — *Phys Rev D* 111, 094508 (2025) | GPU pipeline | Complete | Subpercent precision HVP correlator. |
| Curvature of freeze-out line | Bazavov et al. — *Phys Rev D* 93, 014512 (2016) | GPU pipeline | Complete | Inverse problem: freeze-out curvature from lattice data. |

#### groundSpring (queued)

| Paper | Use |
|-------|-----|
| Spectral reconstruction inverse problem | Signal recovery from noisy lattice correlators. |
| HVP jackknife/bootstrap errors | Statistical uncertainty in lattice measurements. |
| Freeze-out curvature | Inverse problem under lattice noise. |

### What His Work Proved About ecoPrimals

Lattice QCD is one of the hardest computational physics problems — Monte Carlo sampling over SU(3) gauge fields with HMC integration. The fact that BarraCUDA handles lattice gauge theory on a consumer GPU (plaquettes matching strong-coupling expansion, HMC acceptance 96–100%) validates the full GPU compute stack at the most demanding level.

The lattice QCD pipeline also exercises BarraCUDA's f64 path differently from MD — gauge links are SU(3) matrices (complex 3×3), not particle positions. Different numerical structures, same underlying WGSL dispatch.

### Outreach Status

Not yet contacted. hotSpring lattice QCD track is the credibility artifact.

---

## 6. Emily Dolson — neuralSpring (Evolutionary Computation)

**Title**: Assistant Professor, Computer Science & Engineering, MSU
**URL**: https://engineering.msu.edu/directory/faculty/dolsonem
**Connection**: MSDS professor (CSE faculty), core faculty in Ecology, Evolution, and Behavior

### How We Met

Dolson is on the CSE faculty, with a dual appointment in Ecology, Evolution, and Behavior. Her research is the closest academic work to what ecoPrimals discovered empirically — she studies how environmental constraints shape evolutionary dynamics in digital systems. The MODES toolbox and the counterdiabatic driving paper are the direct academic precedents for the constrained evolution methodology.

### Papers Reproduced in Springs

#### neuralSpring

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| Counterdiabatic driving | Iram, Dolson et al. — *Nature Physics* (2020) | Exp (Dolson track) | 11/11 | Controlling the speed and trajectory of evolution. Fitness landscape manipulation. |
| MODES Toolbox | Dolson et al. — *Artificial Life* 25(1) (2019) | Exp (Dolson track) | 9/9 | Open-ended evolution metrics. Measuring novelty, complexity, ecology in evolving systems. |
| Ecological theory + evolutionary computation | Dolson & Ofria — *GECCO* 2018 | Exp (Dolson track) | 7/7 | Ecological dynamics in evolutionary algorithms. Niche construction. |
| Artificial selection for directed evolution | Dolson et al. — *eLife* 11:e79665 (2022) | Exp (Dolson track) | 8/8 | Computational → wet lab bridge. Digital evolution informing real microbial experiments. |
| Heterogeneous swarm controllers | Foreback, Bohm, Dolson — *IEEE* (2025) | Exp (Dolson track) | 11/11 | Heterogeneous controllers for swarm robotics. Diversity as advantage. |

#### groundSpring (queued)

| Paper | Use |
|-------|-----|
| Dolson et al. — Ecology-evolution continuum | Origin of life, signal vs noise in evolutionary transitions. |

### What Her Work Proved About ecoPrimals

Dolson's papers are the theoretical validation of the constrained evolution thesis from the evolutionary computation side. The counterdiabatic driving paper (Nature Physics) shows that external control of fitness landscapes can steer evolution — exactly what the Rust type system does in ecoPrimals. The MODES toolbox provides metrics for measuring whether a system is exhibiting open-ended evolution — the same question the thesis asks about the primal ecosystem.

Her eLife paper on artificial selection bridging computational and wet-lab evolution is also the methodological precedent for the proposed LTEE sequencing (thesis Chapter 14): using computational tools to analyze biological evolutionary trajectories.

### Outreach Status

Not yet contacted. neuralSpring reproductions + the constrained evolution thesis itself are the credibility artifacts. She is potentially the most important committee member for a PhD — her research program directly intersects the thesis.

---

## 7. Ilya Kachkovskiy — hotSpring (Spectral Theory) + neuralSpring

**Title**: Assistant Professor, Department of Mathematics, MSU
**URL**: https://users.math.msu.edu/users/ikachkov/
**Connection**: Sold the NucBox M6 on Facebook Marketplace; brief GPU conversation; noticed equations on whiteboard

### How We Met

Bought the GMKtec NucBox M6 (one of the small form factor nodes in the basement HPC) from Kachkovskiy on Facebook Marketplace. During pickup, noticed spectral theory equations on his whiteboard. Brief conversation about GPUs and computation. This is the most accidental connection in the network — a hardware purchase that linked to a mathematics professor whose research directly applies to BarraCUDA's spectral computations.

### Papers Reproduced in Springs

#### hotSpring

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| Anderson localization (1D) | Anderson — *Phys Rev* 109, 1492 (1958) | Spectral track | 10/10 | 1D Anderson model. Transfer matrix, Lyapunov exponents. |
| Almost-Mathieu operator | Aubry & André — *Ann Israel Phys Soc* 3, 133 (1980) | Spectral track | Reproduced | Quasiperiodic potential, metal-insulator transition. |
| Phase classification | Jitomirskaya — *Ann Math* 150, 1159 (1999) | Spectral track | Reproduced | Almost-Mathieu spectrum classification at critical coupling. |
| Lyapunov exponent bound | Herman — *Comment Math Helv* 58, 453 (1983) | Spectral track | Reproduced | Lower bound on Lyapunov exponents for quasiperiodic systems. |
| Lanczos iteration | Lanczos — *J Res Nat Bur Standards* 45, 255 (1950) | Spectral track | Reproduced | CSR sparse matrix-vector multiply, Lanczos eigenvalue algorithm. |
| Scaling theory of localization | Abrahams et al. — *Phys Rev Lett* 42, 673 (1979) | Spectral track | Reproduced | 2D Anderson model. Scaling behavior at localization transition. |
| 3D Anderson, mobility edge | Slevin & Ohtsuki — *Phys Rev Lett* 82, 382 (1999) | Spectral track | Reproduced | Critical exponent for 3D Anderson transition. |
| Hofstadter butterfly | Hofstadter — *Phys Rev B* 14, 2239 (1976) | Spectral track | Reproduced | Energy levels of Bloch electrons in magnetic field. Fractal spectrum. |
| Ten Martini Problem | Avila & Jitomirskaya — *Ann Math* 170, 303 (2009) | Spectral track | Reproduced | Cantor spectrum of the almost-Mathieu operator. |

#### neuralSpring

| Paper | Experiment | Checks | What It Validated |
|-------|------------|-------:|-------------------|
| Kachkovskiy & Safarov (2016) — distance to normal elements | Exp (Kachkovskiy track) | 8/8 | Approximate commutativity in C*-algebras. Matrix perturbation bounds. |
| Bourgain & Kachkovskiy (2018) — Anderson localization for interacting particles | Exp (Kachkovskiy track) | 8/8 | Two-body localization in quasiperiodic potentials. Loss landscape analysis. |

#### groundSpring (queued)

Papers queued: Anderson localization (disordered media = measurement noise), energy transport in quasiperiodic chains, band edge structure of periodic operators.

### What His Work Proved About ecoPrimals

The spectral theory track pushed BarraCUDA into linear algebra territory — sparse matrix-vector products, eigenvalue algorithms, transfer matrices. This is structurally different from both the particle MD (Murillo) and the lattice gauge theory (Bazavov). Three different computational physics domains, all running through the same WGSL shader architecture on a consumer GPU.

The Anderson localization work also has a conceptual connection to the constrained evolution thesis: localization is what happens when disorder (constraint) prevents transport (exploration). In computational terms, strong typing localizes code to specific domains, preventing the "transport" of bugs across module boundaries.

### Outreach Status

Not yet contacted. The accidental connection (Facebook Marketplace → equations on whiteboard → spectral theory in springs) is itself a demonstration of the capability hunting methodology: you probe the environment and find what you need.

---

## 8. Rika Anderson — hotSpring + wetSpring (Extremophile Evolution)

**Title**: Associate Professor, Department of Biology, Carleton College
**URL**: https://www.carleton.edu/directory/randerson/
**Connection**: Found via literature search — her work on *Sulfolobus* in Yellowstone hot springs is the living experimental corollary to the Taq polymerase constraint argument

### How We Found Her

The constrained evolution thesis uses Taq polymerase (*Thermus aquaticus*, discovered in Yellowstone hot springs) as a founding example: extreme environmental constraint producing a globally useful enzyme. Anderson studies the biology of organisms like *Sulfolobus islandicus* in the same Yellowstone hot springs and *Sulfurovum* at deep-sea hydrothermal vents. She is studying, in living populations, the evolutionary dynamics the thesis uses as analogy.

Her 2021 mSystems review ("Tracking Microbial Evolution in the Subseafloor Biosphere") directly addresses whether evolution in extreme environments is stochastic or deterministic — the core question of whether constraints produce predictable outcomes. Her answer: both, in different regimes. The thesis formalizes this as the constrained evolution principle.

### Papers Reproduced in Springs

#### hotSpring (queued)

| Paper | Citation | Status |
|-------|----------|--------|
| *Sulfolobus islandicus* in Yellowstone | Campbell, Anderson et al. — *Env Microbiol* 19:2392–2405 (2017) | Queued — population genomics of hot spring extremophiles. Direct Taq corollary. |

#### wetSpring

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| Genomic variation at hydrothermal vents | Anderson et al. — *Nature Comm* 8:1114 (2017) | Exp055 | 8/8 | Population genomics. How extreme environments shape genomes. |
| Selection drives gene gain/loss | Moulana, Anderson et al. — *mSystems* 5:e00673-19 (2020) | Exp056 | 8/8 | Pangenomics. Constrained evolution of *Sulfurovum* genome content. |
| Evolution of sulfur-cycling enzymes | Mateos, Anderson et al. — *Science Advances* 9:eade4847 (2023) | Exp053 | Reproduced | Phylogenomics. Ancient enzyme evolution reflecting Earth's redox history. |
| Phosphorus-cycling enzyme timing | Boden, Anderson et al. — *Nature Comm* 15:3703 (2024) | Exp054 | Reproduced | Tree reconciliation. Enzyme evolution through geological time. |
| Viral metagenomics at hydrothermal vents | Anderson et al. — *PLoS ONE* 9:e109696 (2014) | Exp052 | Reproduced | Viral ecology. Phage–host dynamics in extreme environments. |
| Rare biosphere at vents | Anderson, Sogin, Baross — *FEMS Microbiol Ecol* 91:fiu016 (2015) | Exp051 | Reproduced | Rare vs abundant lineages. Long-tail diversity in constrained environments. |

#### neuralSpring

| Paper | Experiment | Checks | What It Validated |
|-------|------------|-------:|-------------------|
| Moulana, Anderson et al. (2020) — pangenomics | Exp (Anderson track) | 8/8 | Gene gain/loss dynamics as constrained evolution. |
| Campbell, Anderson et al. (2017) — *Sulfolobus* | Exp (Anderson track) | 8/8 | Population differentiation under thermal constraint. |

### What Her Work Proved About ecoPrimals

Anderson provides the most direct biological evidence for the constrained evolution thesis. The *Sulfolobus* work is in Yellowstone — the same hot springs where Taq polymerase was discovered. She's studying the evolutionary dynamics of the organisms that live there, in real time, with modern genomics. Her pangenomics paper (Moulana et al.) shows that selection, not drift, drives gene content evolution in *Sulfurovum* — meaning constraints produce deterministic outcomes at the genomic level.

Her mSystems review is also the strongest external citation for the thesis's core argument: evolution under extreme constraint is partially predictable. This is what the thesis claims about Rust + AI — that the constraint makes convergent outcomes predictable.

### Outreach Status

Not yet contacted. Found via literature search. Her work was discovered after the constrained evolution thesis was already drafted — it provides independent empirical support, not the original inspiration. The Taq polymerase argument came from MMG 421 (Prokaryotic Cell Physiology); Anderson's work was found as the modern genomics follow-up.

---

## 9. Jesse Cahill & Chuck Smallwood — wetSpring (Sandia)

**Jesse Cahill** — Senior Member of Technical Staff, Sandia National Laboratories (Bioscience)
**Chuck Smallwood** — Principal Member of Technical Staff, Sandia National Laboratories (Bioscience)
**Connection**: Colleagues at Sandia during Summer 2024 research fellowship

### How We Met

The Summer 2024 research fellowship at Sandia National Laboratories was in the Bioscience department, investigating bacterial toxin effects on raceway algae. Cahill's work focuses on phage biology and biocontrol; Smallwood on metagenomics and microbial ecology of algal production systems. The high-throughput sequencing and bioinformatics experience from that summer directly informed wetSpring's 16S pipeline.

### Papers Reproduced in Springs

#### wetSpring

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| Cahill proxy — algal pond time-series | Cahill | Exp (Cahill track) | 11/11 | Anomaly detection in raceway pond 16S data. Crash forensics. |
| Smallwood proxy — bloom surveillance | Smallwood | Exp (Smallwood track) | 15/15 | 16S surveillance pipeline for algal pond monitoring. |
| Algae pond 16S (PRJNA488170) | Public NCBI data from algae systems | Exp (public data) | 29/29 | Real BioProject data benchmarking the 16S pipeline. |

### What Their Work Proved About ecoPrimals

The Sandia connection is where the bioinformatics pipeline experience came from — not from a textbook, but from a national lab running real sequencing on real production algae. The 16S pipeline in wetSpring (DADA2 + chimera + taxonomy + UniFrac) was built to match the analytical capabilities of the tools used at Sandia, but sovereign — running on BarraCUDA/ToadStool without Galaxy or QIIME2 dependencies.

### Outreach Status

Personal relationship from Sandia fellowship. No formal outreach needed — the work speaks through wetSpring.

---

## 10. A. Daniel Jones — wetSpring Track 2 (PFAS / Analytical Chemistry)

**Title**: Professor, Biochemistry & Molecular Biology / Chemistry, MSU
**URL**: https://www.canr.msu.edu/news/center-for-pfas-research-faculty-spotlight-a-daniel-jones
**Connection**: Current PFAS lab position (October 2024 – present)

### How We Met

Jones runs analytical chemistry and mass spectrometry research at MSU, with a focus on PFAS ("forever chemicals") detection and environmental fate. The current position as a Research Specialist in the PFAS Research Lab provides direct exposure to the methods that wetSpring's blueFish track reproduces.

### Papers Reproduced in Springs

#### wetSpring

| Paper | Citation | Experiment | Checks | What It Validated |
|-------|----------|------------|-------:|-------------------|
| FindPFAS screening pipeline | Jones lab methods | Phase A | 17/17 | PFAS suspect screening from high-resolution mass spec data. |
| Jones F&T proxy — EPA PFAS ML | Jones | Exp041 | 14/14 | Fate-and-transport PFAS modeling. EPA validation data. |
| Jones MS proxy — MassBank spectral | Jones | Exp042 | 9/9 | Spectral matching for compound identification. MassBank reference spectra. |

### What His Work Proved About ecoPrimals

The PFAS work is the analytical chemistry anchor for wetSpring. Mass spectrometry data processing (spectral matching, suspect screening, high-resolution mass fingerprinting) exercises BarraCUDA differently from biology or physics — it's numerical pattern matching at high dimensionality. The GPU spectral cosine similarity benchmark (926× speedup) came from this track.

Jones's PFAS methods also connect to real-world environmental monitoring — these are the tools used to detect forever chemicals in Michigan groundwater. The spring reproduction proves BarraCUDA can run the same analyses at a fraction of the cost.

### Outreach Status

Current employer. No formal outreach needed — the work is part of the professional relationship.

---

## Industry Connections

### Pivot Bio
**URL**: https://www.pivotbio.com/blog/seedsafety
**Connection**: MSUBI contract work (2019–2024)

Nitrogen-fixing microbe research at bench scale (shake flask → 10L reactor). Fermentation, spore counts, viable cell counts. The microbial ecology understanding that informed the biological analogies came from years of working with Pivot Bio cultures under controlled selection pressure.

### MycoWorks
**URL**: https://www.mycoworks.com/scientificresources
**Connection**: MSUBI contract work (2019–2024)

Mycelium materials research at pilot plant scale (~3,000L). Fungal biology, growth media optimization, scale-up. The experience of scaling biological systems from bench to pilot — and seeing how organisms behave differently at different scales — directly informed the NUCLEUS scaling model.

---

## Summary: Faculty × Springs

| Faculty | Springs | Papers Reproduced | Checks | Relationship |
|---------|---------|------------------:|-------:|-------------|
| Murillo | hotSpring, neuralSpring | 6 | 195+ | MSDS professor |
| Dong | airSpring | 5 | 326 | New lab job 2026 |
| Waters | wetSpring, neuralSpring | 7 | 23+ | Undergrad professor |
| Liu | wetSpring, neuralSpring | 6 | 42+ | MSDS professor |
| Bazavov | hotSpring, groundSpring | 6 | 29+ | MSDS professor |
| Dolson | neuralSpring, groundSpring | 5 | 46 | MSDS professor |
| Kachkovskiy | hotSpring, neuralSpring, groundSpring | 11 | 16+ | Facebook Marketplace |
| R. Anderson | wetSpring, neuralSpring, hotSpring | 8 | 133+ | Literature search |
| Cahill | wetSpring | 2 | 40+ | Sandia fellowship |
| Smallwood | wetSpring | 1 | 15 | Sandia fellowship |
| Jones | wetSpring | 3 | 40+ | Current employer |

**Total**: 10 professors + 1 national lab scientist + 1 external researcher
**Springs covered**: All 5 have at least one faculty anchor
**Check coverage**: Every faculty member has at least one paper reproduced with passing checks

---

## Reading These Profiles

Each profile tells the same story three ways:

1. **How we met** — the personal or professional connection
2. **What was reproduced** — their papers running through the springs, with check counts
3. **What it proved** — what their work validated about ecoPrimals

The thesis (`gen3/thesis/`) cites these papers formally. This document tells the story of why these specific papers, from these specific people, ended up in the system. The answer in every case: they were there because the author's life intersected with theirs — as student, lab member, colleague, or (in Kachkovskiy's case) buyer of a mini PC.

The springs are not an abstract paper reproduction exercise. They are reproductions of the science of people whose work the author encountered personally, built to prove the infrastructure works for real science by real scientists.
