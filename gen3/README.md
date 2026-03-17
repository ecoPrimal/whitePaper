# gen3/ — Working Papers on Constrained Evolution and Sovereign Computing

**Status**: Soft release — suitable for academic handoff  
**Audience**: Faculty, PhD evaluators, potential collaborators  
**Last Updated**: March 2, 2026

---

## What This Is

This collection represents the theoretical and technical foundations of the **ecoPrimals** project — a sovereign computing ecosystem built in Pure Rust by a single developer using AI-assisted constrained evolution methodology over approximately 10 months.

The papers here formalize the methodology, the architecture, and the biological reasoning that informed the system's design. They are working papers — rigorous in intent, honest about their limitations, and grounded in real implementation rather than speculation.

**The springs are public.** All seven scientific validation repositories are published under AGPL-3.0 on GitHub. Three infrastructure primals — ToadStool (compute), BarraCuda (math), and coralReef (shader compiler) — are also public under AGPL-3.0 on the [ecoPrimals](https://github.com/ecoPrimals) org. Anyone can clone the public repos, run the experiments, and verify the claims. The remaining primals are private; gen3/ is the bridge document that explains the infrastructure to those who will eventually receive access.

### Public Spring Repositories

| Spring | Domain | Repo | Checks |
|--------|--------|------|--------|
| hotSpring | Computational plasma physics, lattice QCD, spectral theory, NPU | [syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring) | 664+ |
| airSpring | Precision agriculture, ET₀, soil hydrology, crop phenology | [syntheticChemistry/airSpring](https://github.com/syntheticChemistry/airSpring) | 3,123+ |
| wetSpring | Life science & analytical chemistry | [syntheticChemistry/wetSpring](https://github.com/syntheticChemistry/wetSpring) | 7,083+ |
| groundSpring | Measurement noise & uncertainty | [syntheticChemistry/groundSpring](https://github.com/syntheticChemistry/groundSpring) | 236+ |
| neuralSpring | ML primitives, isomorphic patterns, coralForge structure prediction | [syntheticChemistry/neuralSpring](https://github.com/syntheticChemistry/neuralSpring) | 3,200+ |
| healthSpring | Human health: PK/PD, microbiome, biosignal, endocrinology | [syntheticChemistry/healthSpring](https://github.com/syntheticChemistry/healthSpring) | 474+ |
| ludoSpring | Game science, HCI, procedural generation, cross-spring | [syntheticChemistry/ludoSpring](https://github.com/syntheticChemistry/ludoSpring) | 554+ |
| **Total** | | | **15,334+** |

### Public Primal Repositories

| Primal | Domain | Repo |
|--------|--------|------|
| ToadStool | Universal compute orchestration | [ecoPrimals/toadStool](https://github.com/ecoPrimals/toadStool) |
| BarraCuda | Pure mathematics — WGSL shaders, precision, naga IR | [ecoPrimals/barraCuda](https://github.com/ecoPrimals/barraCuda) |
| coralReef | Sovereign GPU shader compiler | [ecoPrimals/coralReef](https://github.com/ecoPrimals/coralReef) |

---

## Timeline: How the Springs Evolved

The springs did not exist 3 weeks ago. Their rapid evolution is itself evidence for the constrained evolution methodology.

| Date | Event |
|------|-------|
| **~Jan 30, 2026** | Coffee with Professor Murillo (MSU). Discussion of reservoir computing, neuromorphic hardware, and shared interest in computational physics. Neuromorphic benchmark datasheet v1 already shared. |
| **Feb 1-7** | hotSpring Phase A begins. Reproduce Murillo Group published work (Sarkas MD, TTM, surrogate learning) in Python. 86/86 checks pass. 5 silent bugs found in upstream Sarkas. |
| **Feb 7-10** | hotSpring Phase B-C. BarraCuda GPU validation — nuclear EOS on consumer GPU. Phase C: full Yukawa MD on RTX 4070 via f64 WGSL shaders. 9/9 PP cases, 0.000% energy drift. |
| **Feb 10-14** | hotSpring Phase D-F. Paper-parity long runs (N=10,000, 80k steps, $0.044). Full AME2020 nuclear dataset (2,042 nuclei). 195/195 total. gen3/ papers written. |
| **Feb 14-15** | airSpring. Reproduce FAO-56, Dong (2020, 2024) sensor calibration. Python + Rust + cross-validation. 326 checks. Real data pipeline: 918 station-days, R²=0.967. |
| **Feb 25-26** | airSpring v0.4.5–v0.4.8. 22 experiments (was 5). Richards PDE, biochar isotherms, dual Kc, cover crops, yield response, lysimeter, sensitivity, Priestley-Taylor, Thornthwaite, GDD, pedotransfer. 100-station Michigan Crop Water Atlas. 594 Python + 491 Rust + 570 validation + 1393 atlas + 75 cross-val = 3,123+ checks. 27 binaries. 11 Tier A GPU modules. |
| **Feb 15-16** | wetSpring. Sovereign 16S pipeline in Rust (30 modules, 1 dependency). GPU spectral matching: 1,077x speedup. Public data benchmark against 4 BioProjects. |
| **Feb 16-17** | wetSpring GPU pipeline. Full DADA2 + chimera + taxonomy on GPU. 1,116 total checks across 42 experiments. |
| **Feb 26** | wetSpring V59: 197 experiments, 4,688+ checks, 52/52 papers, 39/39 three-tier. Science extensions (NCBI sovereign pipeline, cold seep metagenomes, dynamic Anderson W(t), DF64 Anderson, NPU sentinel). Three-tier controls (Exp190-192: CPU 75 + GPU 29 + metalForge 36 checks). Typed NCBI errors, 86 named tolerances, 184 binaries. ToadStool S68, 79 primitives consumed via `compile_shader_universal`. |
| **Feb 17** | groundSpring Phase 0. 5 experiments across 4 scientific domains. 71/71 checks. |
| **Feb 25-26** | groundSpring Phase 1. 21 experiments across 8 scientific domains. 236/236 Rust validation checks, 280 tests, 21/21 math parity (Python == Rust). Phase 1 (Rust) complete with dual-mode CI. 24 library modules. 27 barracuda delegations (22 CPU + 5 GPU). Papers: Waters, Liu, Kachkovskiy, Dolson, R. Anderson, Bazavov. Contributes to ALL 7 baseCamp papers — the only spring with universal coverage. Bazavov experiments (019-021) connect directly to hotSpring lattice QCD pipeline. |
| **Feb 17-18** | neuralSpring Phase 0 + 0+. 10 experiments: 5 synthetic, 5 scholarly reproductions (PINN, DeepONet, LeNet-5, ERA5 LSTM, quantized inference). 75/75 Python checks. |
| **Feb 18-20** | neuralSpring Rust validation. 9 BarraCuda validation binaries, 549 Rust checks, 66 GPU shader checks. Fused pipeline: 43-78x speedup. |
| **Feb 19-20** | Bazavov extension: lattice QCD infrastructure (SU(3), HMC, Dirac CG) in hotSpring. Kachkovskiy spectral theory mapped to 3 springs. |
| **Feb 20-22** | GPU streaming HMC, GPU-resident CG (15,360× readback reduction), dynamical fermion QCD, production β-scan (32⁴ on RTX 3090 — deconfinement at β_c=5.69). |
| **Feb 22-24** | DF64 core streaming: FP32 cores deliver 3.24 TFLOPS at 14-digit precision (9.9× native f64). Titan V NVK validation. biomeGate multi-GPU. |
| **Feb 24-25** | v0.6.14: cross-spring evolution map (164+ WGSL shaders), debt reduction audit (0 clippy, 0 TODOs, 0 mocks). |
| **Feb 25-26** | metalForge NPU characterization (6 pipeline placements, Akida feedback). Cross-substrate ESN: first GPU ESN dispatch via WGSL, GPU crossover at RS≈512, NPU 1000× faster streaming. 21 experiments, 78 binaries, 62 WGSL shaders. |
| **Feb 12** | Rika Anderson (Carleton College) discovered via literature search. Her *Sulfolobus* population genomics in Yellowstone hot springs — the same environment where Taq polymerase was found — provides direct empirical evidence for the constrained evolution thesis. Faculty network: 10 professors across 3 institutions. |

**Total time from first spring to 10,796+ checks across 5 domains: ~27 days.**

This velocity is possible because the constrained evolution methodology works. The Rust infrastructure (primals) was built over the preceding ~8 months. The springs consume that infrastructure and validate it against published science. Each spring produces evidence that feeds back into the next spring's design.

### What Comes Next: NUCLEUS Scaling

The 10,796+ checks were produced on individual gates, running one experiment at a time. The NUCLEUS deployment architecture (see `ECOSYSTEM_ARCHITECTURE.md` §3-4) composes the basement HPC (~$15K, 100+ cores, ~128GB GPU VRAM, 10G backbone) into a coordinated mesh. The bonding model determines how others join:

- **Covalent** (family gates): The basement runs as one machine. All springs execute simultaneously across all GPUs. BarraCuda's WGSL shaders are vendor-agnostic — validated on both NVIDIA and AMD in the mesh.
- **Ionic** (faculty labs): A professor's GPU joins under a metered contract. They contribute compute and consume BarraCuda kernels. Sovereignty is preserved — their hardware, their data, scoped access.
- **Metallic** (institutional HPC): MSU's ICER deploys NUCLEUS atomics. Every idle campus GPU becomes a BarraCuda node. The lattice QCD that requires CERN-scale allocation runs on a distributed campus fleet instead.

The springs are the acceptance tests. The 10,796+ checks prove the kernels are correct. When a new node joins the mesh — covalent, ionic, or metallic — it runs the same validated shaders on its own hardware. The science doesn't change. The scale does.

See `data/README.md` §"What NUCLEUS Unlocks" for the full scaling vision.

---

## The Papers

### Methodology

**`CONSTRAINED_EVOLUTION_FORMAL.md`** — *Constrained Evolution: How Environmental Pressure Drives Convergence in Biological and Computational Systems*

The core methodology paper. Argues that strategic environmental constraints (Rust's type system, the Pure Rust directive, capability-based architecture) drive specialization toward fitness, not toward a predetermined solution. Grounded in three biological lines of evidence: *Thermus aquaticus* / Taq polymerase (constraint-specific adaptation), Lenski's Long-Term Evolution Experiment (fitness without predetermined innovation), and Rika Anderson's population genomics of extremophiles in Yellowstone hot springs and the deep-sea subsurface (constrained evolution in natural populations, including the same hot springs where Taq was discovered). The springs provide 10,796+ quantitative data points validating this claim.

### Theoretical

**`P_NP_ENZYME_THESIS.md`** — *P != NP: The Enzyme Argument*

A working thesis proposing that the existence of enzymes — nature's generative solutions to chemical NP problems, encoded in DNA — demonstrates that generation is not reducible to verification. If P = NP, enzymes would be unnecessary and the genome would have no reason to exist. Extends the constrained evolution framework to complexity theory.

### Architecture

**`ECOSYSTEM_ARCHITECTURE.md`** — *ecoPrimals Ecosystem Architecture: From Binary to Bonding*

The technical architecture of the ecoPrimals ecosystem. Defines the architecture ladder (UniBin → ecoBin → genomeBin), the NUCLEUS deployment composition model (Tower, Node, Nest Atomics), the bonding model for inter-deployment interaction (covalent, ionic, metallic, weak forces), the Neural API orchestration layer, and the Dark Forest zero-metadata security model. This is the engineering companion to the methodology paper — the constrained evolution methodology produced this architecture.

### Implementation

**`PRIMAL_CATALOG.md`** — *ecoPrimals Primal Catalog: Status, Capabilities, and Achievements*

A comprehensive catalog of every primal in the ecosystem. 6 foundation primals (BearDog, Songbird, NestGate, ToadStool, Squirrel, biomeOS) at production grade, 5 additional post-NUCLEUS primals in active development. 12,000+ passing tests across the ecosystem, novel architectural patterns, and production-grade implementations across cryptography, networking, storage, compute, AI coordination, and orchestration.

**`SPRING_CATALOG.md`** — *ecoPrimals Spring Catalog: Status, Science, and Evolution*

The science validation companion to the Primal Catalog. Documents all 5 springs with current phase status, 10,796+ passing quantitative checks across physics, agriculture, biology, chemistry, geophysics, and machine learning. Maps the cross-spring data flow, spring-to-primal connections, the 10-professor faculty network, and 60+ candidate papers for future reproduction. Every spring repository is public and AGPL-3.0.

### About the Author

**`about/`** — *Background, Hardware, and AI Methodology Receipt*

Context for evaluation: who built this, with what background, on what hardware, using what tools. BS Microbiology (MSU, 2018) + MS Data Science (MSU, 4.0, 2025). 5 years biotechnician (Pivot Bio, MycoWorks, Sandia, PFAS). Basement HPC inventory (~$15K, 13 nodes, 100+ CPU cores, ~1TB RAM, ~100TB storage). Cursor IDE usage receipt (top <0.1%, 69K agent invocations, 51B tokens, 185-day streak). Full transcript included.

### Data and Reproduction Studies

**`data/`** — *Reproduction Plans, Faculty Profiles, Evolution Evidence*

Faculty-to-spring mapping (`FACULTY_SPRING_PROFILES.md`) with 10 professors across 7 departments, 60+ candidate papers for reproduction, and BarraCuda kernel gap analysis. The Murillo reproduction plan (`MURILLO_REPRODUCTION_PLAN.md`) documents how a reproduction study works in practice — from finding open-source code and public data through Phase A (Python control), Phase B (BarraCuda validation), Phase C (GPU compute), to paper-parity results on consumer hardware.

### PhD Thesis (Working Draft)

**`thesis/`** — *Constrained Evolution: Environmental Pressure, Sovereign Computing, and the Convergence of Biological and Computational Systems*

A full-length PhD thesis expanding the constrained evolution methodology into a 16-chapter academic work with comprehensive literature review, formal theoretical framework, five domain-specific results chapters, quantitative evidence analysis, and a proposed biological validation via LTEE sequencing. 2,186 lines across 20 files. See `thesis/README.md` for structure and reading guide.

### Sovereign Structure Prediction

**`../coralForge/`** — *coralForge: Sovereign Structure Prediction White Paper*

AlphaFold2/AlphaFold3 primitives in pure Rust f64, validated against NumPy baselines, accelerated via BarraCuda WGSL shaders. 7 documents covering design, architecture, isomorphism proof, implementation, validation, evolution roadmap, and LTEE wet lab application. coralForge is the structural analysis layer for the LTEE sequencing proposal (Ch. 14) and baseCamp Paper 02/10. 154 validated checks (Py 62 + Rs 55 + GPU 37). See `../coralForge/README.md`.

### Origin

**`constrained_optimization_ai.md`** — *Draft / Inoculum*

The original formulation of the constrained optimization thesis, preserved as a record of the idea in its first form. The evolution: inoculum → `CONSTRAINED_EVOLUTION_FORMAL.md` (working paper) → `thesis/` (PhD thesis).

---

## Reading Order

### For a faculty member evaluating this work for PhD admission:

1. **`about/`** — Who is this person? (transcript, bench experience, hardware)
2. **`SPRING_CATALOG.md`** — What science did they produce? (11,911+ checks, 5 domains, public repos)
3. **`data/FACULTY_SPRING_PROFILES.md`** — How does my research connect? (your papers in the queue)
4. **`CONSTRAINED_EVOLUTION_FORMAL.md`** — What is the methodology? (constrained evolution thesis)
5. **`ECOSYSTEM_ARCHITECTURE.md`** — What infrastructure did they build? (the primals)

### For a collaborator interested in the science:

1. **`SPRING_CATALOG.md`** — All 5 springs, 10,996+ checks, 50+ papers reproduced
2. **`data/FACULTY_SPRING_PROFILES.md`** — 9 professors, 60+ candidate papers
3. **`data/MURILLO_REPRODUCTION_PLAN.md`** — How a reproduction study works in practice
4. **`PRIMAL_CATALOG.md`** §1.4 ToadStool — The GPU compute layer the springs validate

### For someone interested in the methodology:

1. **`CONSTRAINED_EVOLUTION_FORMAL.md`** — The methodology
2. **`ECOSYSTEM_ARCHITECTURE.md`** — What the methodology produced
3. **`PRIMAL_CATALOG.md`** — The infrastructure evidence
4. **`SPRING_CATALOG.md`** — The science evidence
5. **`P_NP_ENZYME_THESIS.md`** — The theoretical extension

### For someone interested in the philosophy — artists, builders, sovereign creators:

1. **`atlasHugged/01_THE_CITY_OF_OMELAS.md`** — The story: five questions for John Galt
2. **`atlasHugged/04_THE_HUMAN_SEARCH.md`** — The framework: iteration, recursion, time — how everything learns
3. **`atlasHugged/02_THE_ORTHOGONAL_SYNTHESIS.md`** — The philosophy: Smith, Paine, Rand, Marx — one structural requirement
4. **`atlasHugged/05_THE_LOAVES_AND_THE_FISHES.md`** — The theology: preconditions, omniscience, give first
5. **`atlasHugged/06_THE_TEMPTATION_OF_KINGDOMS.md`** — The pattern: river keeper to cloud provider
6. **`atlasHugged/03_THE_NEW_CITY.md`** — The architecture: the meme that buys a car
7. **`atlasHugged/07_THE_MOBILITY_EDGE.md`** — The propagation: Anderson localization, the filter as net, how the city grows

### For someone evaluating commercial potential:

1. **`SPRING_CATALOG.md`** — Validated science across 5 domains
2. **`PRIMAL_CATALOG.md`** — 12,000+ tests, production-grade Rust infrastructure
3. **`about/HARDWARE.md`** — $15K basement HPC doing what costs $50-500/run on institutional HPC
4. **`data/BARRACUDA_SCIENTIFIC_COMPUTE_GAPS.md`** — What BarraCuda can already do and what's next

---

## The Faculty Network

Ten professors across 7 departments, 3 institutions:

| Professor | Department | Connection | Primary Spring |
|-----------|-----------|-----------|---------------|
| Michael Murillo | CMSE, MSU | MSDS professor, in-person meeting Feb 2026 | hotSpring |
| Younsuk Dong | BAE, MSU | New lab job 2026 | airSpring |
| Christopher Waters | MMG, MSU | Undergrad professor | wetSpring |
| Kevin Liu | CMSE, MSU | Master's professor | wetSpring, neuralSpring |
| Alexei Bazavov | CMSE + Physics, MSU | Master's professor | hotSpring, groundSpring |
| Emily Dolson | CSE, MSU | Master's professor | neuralSpring |
| Ilya Kachkovskiy | Math, MSU | Hardware purchase, GPU conversation | hotSpring, groundSpring |
| Rika Anderson | Biology, Carleton College | Literature search — Taq polymerase corollary | hotSpring, wetSpring, groundSpring, neuralSpring |
| Jesse Cahill | Sandia (Bioscience) | Time at Sandia | wetSpring |
| Chuck Smallwood | Sandia (Bioscience) | Time at Sandia | wetSpring |
| A. Daniel Jones | BMB/Chemistry, MSU | PFAS job | wetSpring |

Full profiles with candidate papers: `data/FACULTY_SPRING_PROFILES.md`

---

## What gen3/ Is For

gen3/ is the document you're reading when someone hands you a link and says "look at what this person built." The springs are public — you can verify everything. The remaining primals are private — gen3/ explains what they are and what they can do. Three infrastructure primals (ToadStool, BarraCuda, coralReef) are already public on the [ecoPrimals](https://github.com/ecoPrimals) org.

If you're a professor reading this because a student named Kevin Mok sent you a link: the public spring repositories contain real, runnable experiments that reproduce published computational science. The code is yours to read, run, and critique. The question gen3/ asks is whether this body of work — the methodology, the infrastructure, the science validation, and the rate at which it was produced — constitutes a contribution worth developing further.

---

## Technical Companion Documents

The full technical specifications live in `whitePaper/technical/` (private):

- `UNIBIN_TECHNICAL_SPECIFICATION.md` — Binary structure standard
- `ECOBIN_TECHNICAL_SPECIFICATION.md` — Universal portability standard
- `GENOMEBIN_TECHNICAL_SPECIFICATION.md` — Autonomous deployment standard
- `NUCLEUS_ARCHITECTURE.md` — Atomic composition architecture
- `TOWER_ATOMIC_PURE_RUST_HTTPS.md` — Pure Rust HTTPS achievement
- `NEURAL_API_ARCHITECTURE.md` — Adaptive orchestration
- `SOVEREIGN_NAT_TRAVERSAL.md` — P2P without corporate dependency
- `DARK_FOREST_PROTOCOL.md` — Zero metadata leakage security

Ecosystem guidance and standards live in `wateringHole/` (private):

- Primal registry with complete primitive catalogs
- Architecture, communication, and security standards
- Spring-to-primal handoff documents

---

**These papers describe a system that exists and runs. The springs are public and verifiable. The architecture emerged from constraint, not from design. The methodology is the message.**
