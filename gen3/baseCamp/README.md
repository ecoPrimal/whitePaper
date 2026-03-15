# baseCamp: Independent Explorations Alongside the Constrained Evolution Thesis

**Date:** March 15, 2026 (standalone barraCuda v0.3.5 at `03986ce`, airSpring v0.7.6 (deep debt: NautilusBrain, data Provider, tolerance provenance), wetSpring V115 (375 experiments, 5,707+ checks, **biomeOS niche** — deploy graph, 19 capabilities, provenance trio integration, cross-spring time series, Neural API workflow graphs. V115: deep audit — UniBin compliance, capability domains (4 domains), tolerance centralization, XDG path resolution, metalForge 90% coverage. V114: docs cleanup, niche setup guidance, BarraCUDA absorption handoff mapping 8 GPU primitives. V113: trio + capabilities + deploy graph. 1,662 tests, 354 binaries, zero clippy warnings pedantic+nursery), hotSpring v0.6.31 (**VFIO PBDMA context load achieved** — Exp 058, 3 Volta register discoveries, PBDMA2 loads RAMFC with zero errors), neuralSpring S147 (deep debt: zero inline magic numbers, zero duplicate math, 6 provenance records added, capability-based discovery, 1115 lib tests, 260 binaries, 0 clippy), groundSpring V101 (DRY evolution, capability-based primal discovery, ESNConfig upstream sync), healthSpring V20, toadStool S146 (`751b3849`), coralReef Phase 10 Iteration 44+ (Experiment Q: VramFullDispatch, PFIFO scheduler dispatches))
**Author:** Kevin Mok (BS Microbiology, MSU 2018; MS Data Science, MSU 2025)

---

## What This Is

These are independent scientific explorations that arose from applying the
ecoPrimals technology (barraCuda, toadStool, wetSpring, neuralSpring, hotSpring,
airSpring, groundSpring) to questions driven by curiosity and bench experience
rather than the specifics of the constrained evolution thesis. They are companion
papers, not thesis chapters.

Each document stands alone as a potential publication. Together they demonstrate
that the technology built for sovereign scientific computing produces real,
publishable science across multiple domains — from condensed matter physics
applied to microbiology, to agricultural biome engineering, to environmental
biosensing.

## How These Relate to the Main Thesis

The constrained evolution thesis (`thesis/03_theoretical_framework.md`) argues
that environmental constraints reshape fitness landscapes and drive
specialization. These baseCamp explorations are the scientific fruit of that
methodology: they were produced using the same constrained tools (Rust, GPU
via BarraCuda, validated against published papers) and they organically
connect back to constrained evolution where the biology demands it — but the
connection is never forced.

```
                    Main Thesis
            (Constrained Evolution)
                    │
        ┌───────────┼───────────┐
        │           │           │
     Theory      System    Validation
   (Chs 3-4)   (Chs 5-6)  (Chs 7-12)
                    │
            ────────┴────────
            │               │
      Spring Papers    baseCamp Papers
      (reproduce)      (explore)
```

Spring papers reproduce published work to validate the infrastructure.
baseCamp papers use that validated infrastructure to explore new science.

## The Papers

| # | Title | Domain | wetSpring Experiments | Key Finding | Status |
|---|-------|--------|---------------------|-------------|--------|
| 01 | Anderson Localization as QS Null Hypothesis | Physics × Microbiology | Exp107-156 (3,100+ checks), Exp170-182 (321 checks), **Exp356 (18 checks, V110)** | 3D geometry is necessary and sufficient for QS in diverse communities; 3 genuine NP solutions found; W_c = 16.26 ± 0.95 quantified. **V110: O₂-modulated W model (r=0.851) refines null hypothesis — disorder is two-dimensional (diversity + oxygen)** | **Validated** — 198 experiments, full three-tier + cross-environment |
| 02 | Extending the Frozen Fossil Record | Evolutionary Biology | Builds on Ch. 14 + Anderson anomaly catalog (Exp143) | Constrained evolution predictions for LTEE, permafrost, vent archives, agricultural time series | Proposal — predictions quantified |
| 03 | Precision Microbiome for Tree Crops | Agricultural Microbiology | Extension of Anderson model + Track 4 soil QS (Exp170-178) | Soil biome geometry guides inoculant design; rhizosphere W ≈ 6.7 (extended regime) | Proposal — Track 4 validates framework |
| 04 | Microbial Sentinels | Environmental Biosensing | Exp114-119, 123, 124, **193-195** (NPU), PFAS/algae | Community shifts as early-warning biosensors; **NPU validated on real AKD1000** (18.8K Hz, coin-cell 11 years, online evolution 136 gen/sec, PUF fingerprint) | **Validated on Live Hardware** — Pure Rust driver, Phase C sovereign |
| 05 | Cross-Species Signaling in Symbiotic Systems | Symbiotic Ecology | Exp142, 144-146 (cold seep + luxR phylogeny) | Mixed-species QS in lichen, rhizobia, coral; 299K QS genes across 170 metagenomes; eavesdropper enrichment confirmed | **Validated** — cold seep + phylogeny complete |
| 06 | Anderson Localization as the Mechanism Behind No-Till Soil Health | Soil Microbial Ecology × Physics | Track 4: Exp170-182 (321 checks), 9 papers, full three-tier | Tillage = dimensional collapse of QS-active 3D pore network; CPU + GPU + metalForge validated | **Validated** — Track 4 complete |
| 07 | Sovereign Warm Dense Matter Simulation on Consumer GPU | Plasma Physics × Distributed Computing | hotSpring Tier 4 + neuralSpring surrogates + groundSpring uncertainty | WDM transport on $600 GPU; deconfinement at β_c=5.69 on $1,500 GPU; **11-head NPU GPU conductor** (Exp 023); coralReef sovereign compile **46/46** shaders (Iter 33); 12/12 NVVM bypass; FMA lowering (`FmaPolicy::Separate`); precision brain self-routing (12 domains); **Exp 053: live Kokkos parity** — 9/9 cases, 12.4× gap (DF64 transcendental poisoning fix); **Exp 058: VFIO PBDMA context load** — 3 Volta register discoveries (preempt 0x2638, ACK 0x2A00, SIGNATURE), PBDMA2 loads RAMFC zero-error, USERD DMA read remaining. coralReef P10 Iter 44+. Dual Titan V planned. | **Validated** — hotSpring v0.6.31 |
| 08 | Neuromorphic Edge Intelligence for Sovereign Agricultural IoT | Agricultural IoT × Neuromorphic Computing | airSpring Exp 028-029 (88 checks) + wetSpring NPU driver | NPU inference at 0.0009% of active cycle energy; 10.7× more efficient than cloud; 1-min cadence unlocked; multi-crop hot-swap | **Validated on Live Hardware** — AKD1000, streaming + evolution + power budget. airSpring v0.7.0: 827 lib + 186 forge tests, barraCuda 0.3.3 (wgpu 28), fused Welford + Pearson wired, 20.6× CPU speedup (24/24 parity), 381/381 validation |
| 09 | Sovereign Field Genomics — Nanopore + NPU | Environmental Genomics × Edge Inference | wetSpring Exp193-195 (NPU) + Exp184-185 (16S) + planned Exp196-202 | MinION sequencing + AKD1000 classification + BarraCUDA 16S pipeline = autonomous field sentinel. NPU-driven adaptive sampling (37x read-rate headroom). No cloud, no Python. | **Architecture defined** — all compute components validated, awaiting sequencer hardware |
| 10 | First Dynamical QCD Production on Consumer GPU | Lattice QCD × Neuromorphic Computing | hotSpring Exp 024 (8⁴ dynamical, 1,031+ traj, 17 β points), Exp 028-031 | First NPU-steered dynamical fermion QCD scan. Smooth crossover confirmed. β_c ~ 5.5. NPU expanded 4-seed scan to 17 points. CG–disorder correlation validates Anderson proxy. **Exp 031: NPU controls dt/n_md with mid-beta adaptation, targeting 70% acceptance.** | **Complete + Evolving** — 17 β points, Exp 031 adds NPU parameter control. |
| 11 | The Nautilus Shell — Evolutionary Reservoir Computing from Bingo Boards | Reservoir Computing × Neuromorphic × Evolutionary Algorithms | primalTools/bingoCube/nautilus/ (31 tests, 5 examples); **ToadStool S80**: barracuda::nautilus (7 files, 22 tests, 8 JSON-RPC methods) | Bingo boards as structured random projections; evolutionary generations replace temporal recurrence for feed-forward hardware; nautilus shell = layered evolutionary history, portable between instances. Column-range-preserving crossover maps natively to AKD1000 int4. Self-regulating drift monitor + edge seeding. AKD1000 int4 weight export. Quenched→dynamical transfer: 540× cost reduction. | **Validated** — 5.3% LOO CG error, 2.6% blind prediction on Exp 029, 31 tests. **S80**: Standalone absorption into ToadStool/BarraCUDA (7 files, 22 tests, 8 ai.nautilus.* JSON-RPC methods). |
| 12 | Anderson Localization in Immunological Signaling — Cytokine Propagation, Drug Geometry, and the Fajgenbaum Repurposing Bridge | Immunology × Condensed Matter Physics × Pharmacology × Drug Repurposing | wetSpring Exp273-286 (359/359), neuralSpring nS-601–605 (329/329), airSpring Exp066-069 (94/94), groundSpring Exp008/012/015/018 | Cytokine (IL-31/IL-4/IL-13) propagation through inflamed skin tissue follows Anderson localization; AD barrier disruption = dimensional promotion (inverse of Paper 06 tillage collapse); Fajgenbaum MATRIX drug-disease scoring gains geometry dimension via Anderson transport; **groundSpring** provides 2D/3D spectral validation (Exp 008), cytokine transport modeling (Exp 012), uncertainty bridge (Exp 015), band edge for epidermal periodicity (Exp 018), ConceptEdge for AD flare detection, DriftAction for treatment steering. **MSU Drug Discovery pipeline**: Anderson-augmented MATRIX scores (nS-605) → ADDRC HTS (8,000+ compounds, Lisabeth) → Gonzales iPSC validation → Ellsworth medicinal chemistry. Neubig Rho/MRTF/SRF skin fibrosis → cross-talk with JAK/STAT open question | **Validated** (Gonzales G1-G6 + Fajgenbaum MATRIX complete); **Evolving** (ADDRC pipeline, Rho cross-talk, skin-layer lattice). Source: Dr. Andrea J. Gonzales (MSU Pharmacology & Toxicology), Erika Lisabeth (ADDRC Director), Richard Neubig (Drug Discovery Director) |
| 13 | Sovereign Human Health Computing — Per-Person Translation of PK/PD, Microbiome, Biosignal, Endocrine, and NLME Pipelines | Human Health × Pharmacology × Microbiome × Biosignal × Endocrinology × NLME × Clinical Translation | healthSpring Exp001-089 (61 experiments). 458 tests, 194 Python cross-validation checks. | **5-track human health spring + per-person translation**: PK/PD (Hill, PBPK 5-tissue, population Monte Carlo, Michaelis-Menten nonlinear PK), Microbiome (Anderson gut lattice, FMT engraftment, antibiotic perturbation, SCFA production, gut-brain serotonin), Biosignal (Pan-Tompkins, HRV, PPG SpO2, EDA stress, arrhythmia classification, WFDB), Endocrinology (testosterone PK, TRT outcomes, testosterone-gut axis), NLME (FOCE + SAEM — sovereign NONMEM/Monolix, NCA — sovereign WinNonlin). 6 WGSL compute shaders (Hill, PopPK, Diversity, MM batch, SCFA batch, Beat classify). **V21: Deep debt** — smart module refactors (nlme/, endocrine/, ipc_push/, clinical_nodes/), AGPL-3.0-only, named tolerances, provenance DOIs, XDG discovery, determinism tests. **V19: Full-stack portability** — GPU scaling (Exp085, 47/47), toadStool dispatch (Exp086, 24/24), mixed NUCLEUS with PCIe P2P bypass (Exp087, 35/35). **V18: Rust 84× faster** (Exp084). GPU dispatch + metalForge cross-system routing + toadStool streaming dispatch. Full petalTongue: 28 nodes, 121 channels, 14 scenarios. | **Validated** — V21, Tier 0+1+2+3 complete, deep debt resolved. Source: Gonzales (PK/PD), Mok (clinical TRT), Beal & Sheiner (FOCE), Kuhn & Lavielle (SAEM) |
| 15 | Self-Routing Precision Brain for Heterogeneous GPU Compute | GPU Computing × Precision Engineering × Hardware Discovery | hotSpring Exp 049-051 (precision eval + coralReef sovereign validation + Iter 30 FMA/hardware data) | Data-driven self-routing brain discovers hardware, routes physics to optimal precision tier per-domain (12 domains), survives NVIDIA NVVM device poisoning. coralReef sovereign bypass integrated: 46/46 compile, 12/12 NVVM bypass patterns, FMA lowering (`FmaPolicy::Separate`) unlocks F64Precise via sovereign path. Portable across springs. toadStool S146 absorbed PrecisionBrain with `PrecisionHint` routing + `NvkZeroGuard`. | **Validated** — hotSpring v0.6.29 |
| 16 | Anaerobic-Aerobic QS Phase Transition — Microbial Signaling Across Oxygen Regimes | Microbial Ecology × Environmental Engineering × Anderson Localization | Planned — bridges wetSpring (QS), healthSpring (gut), airSpring (soil O₂), ADREC digesters. **neuralSpring benchmark: Paper 027 (Wang/Liao 2020 digester prediction) COMPLETE** — ESN methane yield predictor, 36/36 CPU + 23/23 bC/gT PASS. **wetSpring Exp356 (V110): O₂-modulated Anderson W model validated (H3, r=0.851)** | Oxygen triggers global transcription reprogramming (FNR/ArcAB/Rex) that modulates QS gene expression → Anderson disorder parameter W undergoes phase transition at oxygen boundary. **V110 Exp356 confirms:** W = 3.5·H' + 8·O₂ outperforms single-variable W (r=0.851 vs -0.575) across 10 environments. Diversity IS disorder (signal dilution), oxygen adds second dimension. Anaerobic communities show lower effective W, explaining higher QS prevalence in gut, digesters, biofilm. Testable with paired 16S/metatranscriptome data. | **Computationally validated** — Exp356 (18/18 PASS). H3 O₂-modulated model proven. Concept→lab path defined (reporter strain assays). **neuralSpring digester ML benchmark validated (S142: Paper 027)**. Faculty anchor: Wei Liao (ADREC, MSU BAE). Source: MSUBI bioreactor experience (5 years) |
| 17 | Game Design as Rigorous Science — Validated HCI Models for Interactive Systems | Game Science × HCI × Procedural Generation × GPU Compute × Cross-Spring × Provenance × Lysogeny × Economics | ludoSpring V14: 66 experiments, 1349 checks, 22 tracks, 3 playable prototypes, 3 external control groups, 3 game adapters, 4 cross-spring experiments (NCBI, NUCLEUS, Anderson QS), 3 RPGPT, 4 Games@Home, 6 lysogeny, 1 fermenting, 5 cross-spring provenance. Python→Rust→GPU evolution pipeline. barraCuda v0.3.5 primitives consumed (sigmoid, dot, lcg_step). Provenance trio direct deps (rhizoCrypt, loamSpine, sweetGrass). Deep audit: LCG unified, 0 clippy warnings, 93.2% coverage. | 13 foundational HCI models validated (Fitts, Hick, Steering, GOMS, Flow, DDA, Four Keys, Engagement, Perlin, WFC, L-systems, BSP, Tufte). Game genres = interaction architectures. **Key finding: Flow state discriminates quality**. External controls prove metrics are content-agnostic. **Lysogeny catalog**: 6 proprietary mechanics recreated from open math. **Novel Ferment Transcript**: memory-bound digital objects with provenance trio. **Cross-spring provenance**: same fraud detectors work across gaming/science/medical (>80% similarity). **Radiating attribution**: sunCloud value distribution with decay. **V14 deep audit**: exp061 refactored (1227→102 lines), LCG aligned to barracuda::rng, 49 new tests, ValidationResult provenance tracking. | **Validated** — 66 experiments, 1349/1349 checks, 187 tests, 93.2% coverage. ludoSpring V14. Faculty anchors: Csikszentmihalyi (Flow), Fitts, Yannakakis & Togelius, Lazzaro, Hunicke, Merkle, Diffie & Hellman |
| 18 | RPGPT — Sovereign RPG Engine with Ingestible Rulesets | Game Science × Provenance × AI × Open RPG Systems | ludoSpring (13 HCI models) + rhizoCrypt (session DAG) + sweetGrass (creative attribution) + loamSpine (ruleset/character/world certs) + Squirrel (AI narration) + BearDog (anti-cheat signing). Ingestible open rulesets: Pathfinder 2e (ORC), FATE Core (CC-BY), PbtA, Cypher. | **Anti-cheat = chain-of-custody isomorphism**: same DAG operation for item lineage (extraction shooters), sample lineage (field genomics), loot lineage (tabletop RPG). Rulesets as loamSpine certificates constrain AI — no hallucination past anchored rules. Player-as-DM: sweetGrass Creation → Implementation → Extension attribution. Any world + any open ruleset = playable RPG. Provenance trio evolution goals scaffold cross-domain capability (turn-based sessions, condition decay, branch diff/merge). | **Architecture defined** — structural sketch validated, provenance trio evolution goals documented. Faculty anchors: Gygax & Arneson (1974), Cook (PF2e), Csikszentmihalyi (Flow) |
| 19 | Games@Home — Distributed Human Computation via Interactive Systems | Game Science × Combinatorics × Distributed Computing × Provenance × Cross-Domain Transfer | ludoSpring (exp048-051: stack folding, novel data combinatorics, game tree design metric, Games@Home model) + rhizoCrypt (trajectory DAG) + sweetGrass (creative attribution) + loamSpine (deck/ruleset certs). MTG Turing completeness (Churchill et al. 2019). | **Human gameplay as compute engine**: Stack resolution = protein folding (same cards, different order → different outcomes). MTG game tree is 2^ℵ₀ (uncountably infinite, proven Turing complete). Every game produces novel data (birthday bound ~10^179 vs ~10^10.5 games ever played). Game tree complexity is a design metric — Commander format rules ×216 expansion, designed-for-commander cards ×0.036 contraction. Enzymatic shortcut model: cards that "solve" parts of the space narrow exploration. Folding@Home isomorphism across 12 concepts. 7 cross-domain transfer paths (avg 76% structural similarity). AR card gaming concept for physical-anchored digital enhancement. | **Validated** — 4 experiments, 127/127 checks. Faculty anchors: Churchill, Biderman & Herrick (2019), Shannon (1950), Pande (F@H), von Ahn (2006) |
| 20 | Novel Ferment Transcript Economics — Radiating Attribution Through Provenance | Economics × Provenance × Cryptography × Cross-Domain Transfer | ludoSpring exp061_fermenting (89 checks) + rhizoCrypt (DAG history) + loamSpine (certificate lifecycle, trading protocol) + sweetGrass (object memory, PROV-O attribution) + BearDog (Ed25519 signing) + biomeOS (provenance_node_atomic deployment). sunCloud economic model. scyBorg licensing (AGPL-3.0 + ORC + CC-BY-SA 4.0). | **Memory-bound digital objects whose value derives from accumulated history, not artificial scarcity.** Novel Ferment Transcript (NFT) = loamSpine cert + rhizoCrypt DAG + sweetGrass braids + BearDog signatures + optional public chain anchor. Same architecture serves gaming (tournament sword), collectibles (trading card), science (sample chain-of-custody), and sensitive data (medical records). Public anchor activates radiating attribution: value flows backward through sweetGrass chain to every contributor. Functionally NOT a currency — no exchange rate, no gas, no mining. Trading protocol with atomic swap. Object memory with PROV-O timeline export. Composable IPC protocol for live trio deployment. Evolves sunCloud (2025) + LATENT_VALUE_ECONOMY into working code. | **Validated** — 89/89 checks (exp061). Trio modifications shipped (loamSpine trading protocol, sweetGrass object memory). Faculty anchors: Merkle (1987), Diffie & Hellman (1976), Moreau & Missier (W3C PROV-O, 2013) |
| 21 | Sovereign Sample Provenance — Field-to-Publication Chain-of-Custody | Field Genomics × Provenance × Fraud Detection × Cross-Spring | ludoSpring exp062 (39/39), exp064 (39/39), exp065 (74/74), exp066 (41/41). Provenance trio (rhizoCrypt + loamSpine + sweetGrass) + BearDog signing. ISO 17025/15189 mapping. | **Same provenance architecture that tracks game items tracks biological samples.** 6 fraud types (PhantomSample, DuplicateAccession, BrokenColdChain, UnauthorizedAccess, MislabeledSpecimen, ContaminationGap) reduce to graph analysis. DAG isomorphism with extraction shooter (exp053). Cross-domain fraud unification proves same code path detects fraud in gaming and science (>80% structural similarity). Radiating attribution gives field collectors permanent credit. Every sample is a Novel Ferment Transcript. | **Validated** — 193 checks across 4 experiments. Faculty anchors: ISO 17025 (2017), Kahn (1962), Moreau & Missier (W3C PROV-O, 2013) |
| 22 | Zero-Knowledge Medical Provenance — Patient-Owned Records with Consent Certificates | Medical Data × Provenance × Zero-Knowledge × Cross-Spring | ludoSpring exp063 (35/35), exp064 (39/39), exp065 (74/74), exp066 (41/41). Consent as loamSpine lending. BearDog zero-knowledge access proofs. HIPAA alignment. | **Patient-owned medical records via DID-based loamSpine certificates.** Consent certificates as scoped loans (record types + expiry + revocation). Every access is a DAG vertex. 5 fraud types (UnauthorizedAccess, ExpiredConsent, ScopeViolation, PhantomAccess, ConsentForgery). BearDog selective disclosure proofs. Same fraud detectors catch item duplication in games and unauthorized medical record access. Patient as Creator in radiating attribution. | **Validated** — 189 checks across 4 experiments. Faculty anchors: HIPAA Privacy Rule §164.524, HIPAA Security Rule §164.312, Diffie & Hellman (1976) |

## Reading Order

**For a microbiologist**: 01 (Anderson-QS, the headline result) → 05 (cross-species) → 03 (bioag) → 06 (no-till)

**For an immunologist or pharmacologist**: 12 (immunological Anderson — cytokine propagation, Fajgenbaum bridge) → 01 (Anderson-QS foundation) → 05 (cross-species signaling) → 04 (sentinels — ESN regime classification)

**For an ecologist**: 05 (symbiotic signaling) → 02 (LTEE extensions) → 04 (sentinels) → 06 (no-till)

**For a soil scientist or agronomist**: 06 (no-till Anderson mechanism) → 03 (tree crop inoculants) → 01 (underlying physics)

**For a physicist**: 01 (Anderson applied to biology) → 06 (dynamic Anderson with time series) → the wetSpring experiment docs (Exp107-143)

**For a plasma physicist**: 07 (sovereign WDM on consumer GPU) → 10 (dynamical QCD production) → 15 (precision brain, heterogeneous GPU) → 01 (Anderson framework) → the hotSpring paper queue (Tier 0–4)

**For a GPU systems researcher**: 15 (precision brain, NVVM poisoning) → 14 (sovereign compute hardware) → 07 (sovereign WDM) → 10 (dynamical QCD) → 11 (nautilus shell, evolutionary reservoir)

**For a PhD committee**: 01 (demonstrates novel contribution) → 06 (applied to 60-year dataset) → 07 (WDM + distributed compute) → 02 (connects to LTEE proposal) → 03-05 (breadth) → 08 (NPU edge deployment)

**For an agricultural engineer**: 08 (NPU edge IoT) → 09 (field genomics) → 06 (no-till physics) → 03 (bioag microbiome) → 04 (sentinel monitoring)

**For a field genomics researcher**: 09 (field genomics) → 04 (sentinel concept) → 01 (Anderson detection signal) → 08 (NPU agricultural IoT) → the wetSpring experiment docs (Exp193-195, planned Exp196-202)

**For a game designer or HCI researcher**: 17 (game design as rigorous science — 13 validated HCI models) → 01 (Anderson-QS — Perlin noise as disorder landscape) → 13 (sovereign health — Fitts/Hick for medical UI, engagement for patient compliance) → 12 (immuno-Anderson — DDA for treatment adaptation)

**For an environmental/bioprocess engineer**: 16 (anaerobic-aerobic QS phase transition) → 01 (Anderson-QS foundation) → 06 (no-till — soil O₂ zones) → 04 (sentinels — digester monitoring) → 03 (bioag microbiome) → 13 (gut = human anaerobic digester)

**For a game developer or systems designer**: 17 (game design as rigorous science — 13 HCI models) → 18 (RPGPT — sovereign RPG engine, ingestible rulesets, provenance-backed world state) → 19 (Games@Home — stack folding, novel data, game tree as design metric, distributed human computation, AR card gaming) → 01 (Anderson-QS — dungeon exploration = microbial exploration isomorphism) → 13 (sovereign health — patient engagement = player engagement)

**For a distributed computing researcher**: 19 (Games@Home — Folding@Home isomorphism, human creativity as compute) → 07 (sovereign WDM on consumer GPU) → 15 (precision brain) → 17 (game design as science — validated HCI metrics)

**For a digital economics or provenance researcher**: 20 (Novel Ferment Transcript — radiating attribution through provenance) → 19 (Games@Home — distributed human computation) → 18 (RPGPT — DAG isomorphism: game = science = sensitive data) → 17 (game design as science — foundational HCI models) → 01 (Anderson-QS — fermentation as biological analogy)

**For a collectibles, trading, or marketplace designer**: 20 (Novel Ferment Transcript — memory-bound objects, trading protocol) → 21 (sample provenance — cross-domain fraud unification) → 19 (Games@Home — physical card provenance, AR bridge) → 17 (game design as science — engagement vs flow) → 18 (RPGPT — chain-of-custody isomorphism)

**For a field genomics or lab science researcher**: 21 (Sovereign Sample Provenance — field-to-publication chain-of-custody, 6 fraud types) → 20 (NFT Economics — every sample is a Novel Ferment Transcript) → 09 (Field Genomics) → 04 (Sentinels) → 01 (Anderson-QS)

**For a clinical data or HIPAA compliance researcher**: 22 (Zero-Knowledge Medical Provenance — patient-owned records, consent certificates) → 13 (Sovereign Health — clinical tracks) → 20 (NFT Economics — radiating attribution) → 12 (Immuno-Anderson) → 21 (Sample Provenance — shared fraud infrastructure)

**For a reservoir computing researcher**: 11 (nautilus shell — evolutionary reservoir from bingo boards) → 10 (ESN-steered dynamical QCD) → 07 (NPU brain architecture) → 04 (sentinels, NPU edge deployment)

**For an immunologist or veterinary pharmacologist**: 12 (Anderson in immunological signaling) → 01 (underlying Anderson-QS physics) → 06 (dimensional collapse/promotion duality) → 05 (cross-species signaling)

**For a drug repurposing researcher**: 12 §3 (Fajgenbaum bridge — geometry-aware scoring) → 12 §2 (Anderson mapping) → 01 (framework) → 04 (sentinels as diagnostic analog)

## Connection to the Main Thesis

Paper 11 (Nautilus Shell) provides direct computational evidence for the
constrained evolution framework (thesis Ch. 3). The column-range constraint
on bingo boards reshapes the fitness landscape of the reservoir, producing
specialized boards that predict QCD observables at 5.3% LOO error —
structures that would not emerge from unconstrained neural architecture
search. The N_e·s drift monitor implements Anderson's drift boundary
(thesis §3.2.3) computationally, and edge seeding implements directed
mutagenesis where constraint identifies regions of qualitative physics
change. The Nautilus Shell is also the computational machinery needed for
the LTEE library vision (Paper 02): populations under constraint, with
drift monitoring, fitness tracking, and concept edge detection.

## Bench Experience Behind These Papers

These explorations draw directly on the author's lab experience:

- **Bioeconomy Institute (5 years)**: Fermentation, bioreactors, BSL2 work with
  fungi, mycobacteria, anaerobes, GMOs. Informed Sub-thesis 03 (bioag) and 05
  (mixed systems).
- **Pivot Bio project**: Soybean root isolate as N-fixation probiotic. Directly
  informed the rhizosphere QS predictions in Sub-thesis 01 and 03.
- **Sandia National Lab**: Bacterial toxins on raceway algae, high-throughput
  sequencing. Informed Sub-thesis 04 (sentinel microbes, algal bloom prediction).
- **PFAS Research Lab (MSU)**: Forever chemicals in environmental samples.
  Informed Sub-thesis 04 (contamination biosensing).
- **Microbial Ecology Lab (undergrad)**: Rumen bacteria isolation, RDP analysis.
  Informed the diversity-disorder mapping in Sub-thesis 01.

## Data and Reproducibility

Experimental data is generated by Spring binaries (public, AGPL-3.0).
NCBI queries use the Entrez E-utilities API (via NestGate `NCBILiveProvider`).
Springs contributing validated infrastructure:

- **wetSpring**: Anderson QS, 16S pipeline, DADA2, taxonomy, NPU live, field genomics architecture, bio brain (5,707+ checks, 372 experiments, 1,621 tests, 340 binaries, 47 CPU + 47 GPU bio modules, V112, standalone `barraCuda` v0.3.5 (wgpu 28, Fp64Strategy), 150+ primitives consumed, 180 named tolerances, zero local WGSL, zero TODO/FIXME/HACK, `#![forbid(unsafe_code)]` on all crate roots, clippy pedantic+nursery ZERO WARNINGS. V112: **streaming-only I/O** (deprecated buffering parsers removed), **capability-based runtime discovery** (zero hardcoded primal paths), zero clippy warnings. V111: deep debt resolution — build health, bingocube-nautilus, hot-path clone elimination. V110: petalTongue visualization pipeline (Exp353-355) + Anderson QS O₂-modulated model (Exp356, H3 r=0.851, 18/18). 63 papers reproduced.)
- **neuralSpring**: ML primitives (LSTM, HMM, transfer learning, spectral analysis,
  ESN reservoir computing), **27 papers** (full queue complete) + 5 WDM surrogates +
  5 novel compositions + 4 GPU experiments, validated at 4,500+ checks, 1115 lib tests,
  73 forge, 9 integration, 258 binaries. 92% line coverage. 80+ named tolerances.
  25 absorbed workloads, 1 local remaining. 0 clippy (pedantic+nursery, all-features),
  0 doc warnings. barraCuda v0.3.5 (`03986ce`), toadStool S146 (`751b3849`), coralReef
  Iter 33 (`b783217`, 46/46 sovereign compile). **S145**: GPU infra evolution sprint —
  5 workload rewires (chi², KL, HMM backward/Viterbi, pairwise L2), NUCLEUS GPU dispatch
  (eigensolve + attention_anderson via Dispatcher), 4 GPU experiments (Exp 103–106:
  eigensolve pipeline, batched spectral, sovereign compile on RTX 4070 Ada GSP,
  mixed-hardware composition). S143–144: 5 novel composition experiments (Exp 097–101),
  petalTongue composition visualization, NUCLEUS pipeline executor.
  Cross-spring provenance mapped: hotSpring precision → wetSpring bio → neuralSpring
  domain → barraCuda fused ops → consumed by all Springs
- **hotSpring**: MD simulation, nuclear EOS, lattice QCD, transport, 4-layer brain architecture, **self-routing precision brain** (848 tests, 115 binaries, 85 WGSL shaders, 0 clippy warnings, 0 files >1000 lines). **25 papers** (Papers 43-45: Chuna gradient flow integrators, conservative dielectric functions, kinetic-fluid coupling — **44/44 overnight checks pass**). coralReef sovereign pipeline: **46/46** standalone shaders compile to native SM70/SM86 SASS. Full `GpuBackend` impl. **Exp 049**: Precision brain + NVVM device poisoning discovery. Dual-GPU cooperative patterns (Split BCS 2.2×, PCIe 1.2 GB/s). Kokkos parity: 12.4× gap persists — primary blocker is NVVM-safe DF64 exp. **Exp 058**: VFIO PBDMA context load breakthrough — 3 Volta register discoveries, PBDMA2 loads RAMFC with zero errors, USERD DMA read remaining. v0.6.31, barraCuda v0.3.5, toadStool S146, coralReef P10 Iter 44+.
- **airSpring**: FAO-56 ET₀ (8 methods), Priestley-Taylor, Thornthwaite, GDD, Saxton-Rawls
  pedotransfer, water balance, Richards PDE, isotherms, yield response, scheduling, lysimeter,
  sensitivity, SCS-CN runoff, Green-Ampt infiltration, Anderson coupling, diversity indices,
  100-station Michigan Crop Water Atlas, NUCLEUS primal (30 capabilities), metalForge dispatch,
  AirSpringBrain (Nautilus evolutionary reservoir: ET₀/soil/crop heads), MonitoredAtlasStream
  (DriftMonitor regime change detection), Paper 12 immunological Anderson (tissue diversity +
  CytokineBrain + barrier state + cross-species), 6 local WGSL compute shaders
  (`local_elementwise_f64.wgsl`: SCS-CN, Stewart yield, Makkink, Turc, Hamon, Blaney-Criddle)
  via `gpu::local_dispatch::LocalElementwise` (f64 canonical, compile_shader_universal).
  **v0.7.0 (March 5, 2026)**: Rewired to standalone barraCuda 0.3.3 (wgpu 28). 1237 Python +
  827 lib + 186 forge tests + 86 binaries, 78 experiments. 381/381 validation checks.
  25 Tier A + 6 GPU-local (3/6 absorbed upstream: Makkink, Turc, Hamon),
  fused Welford mean-variance + fused Pearson correlation wired from upstream,
  DF64 precision tier documented, Fp64Strategy::Concurrent for cross-validation.
  20.6× CPU speedup (24/24 parity). 146/146 cross-spring evolution, 34 ShaderProvenance entries.
  27 GPU tests fail upstream (wgpu 28 + NVK/Titan V), CPU fallback in SeasonalReducer.
  Zero clippy pedantic+nursery warnings, cargo-deny clean.
- **groundSpring**: Uncertainty quantification, noise labels, spectral theory (Anderson, Almost-Mathieu, band edge), transport, quasispecies, rare biosphere, jackknife, freeze-out, spectral recon, WDM precision/convergence/vendor-parity, NPU Anderson regime classification, mixed-hardware pipeline dispatch (`PCIe` topology, NUCLEUS atomics, fallback chains) (34 experiments, 395/395 Rust checks + 187 metalForge checks, 10 domains, 807 workspace tests; live hardware: RTX 4070, Titan V, AKD1000 NPU; 2.2× GPU speedup). V79: Exp 035 Multi-Method ET₀ cross-validation (5 methods: PM, Hargreaves, Makkink, Turc, Hamon), seismic delegation strengthening. barraCuda v0.3.3, toadStool S94b fully synchronized, clippy pedantic CI, 13-tier named tolerance architecture (`tol::` module, `eps::` module), zero bare tolerance literals, full validation benchmark (34/34 binaries, −10% with barraCuda CPU delegation), cross-spring provenance documented. 97.25% library line coverage. 85 active delegations (51 CPU + 34 GPU). 29/29 mathematical parity. biomeOS Neural API + NestGate data pipelines (NCBI, NOAA, IRIS). All files < 1000 lines, zero unsafe, zero production mocks, zero `unwrap()` in production, zero TODO/FIXME in Rust source

Every experiment can be reproduced with the corresponding Spring's binaries:

```bash
# wetSpring experiments (Anderson QS, 16S, metagenomics)
cd wetSpring/barracuda && cargo run --release --features gpu --bin <binary_name>

# neuralSpring experiments (ML, spectral, surrogates)
cd neuralSpring && cargo run --release --bin <binary_name>

# hotSpring experiments (MD, nuclear EOS, lattice QCD)
cd hotSpring && cargo run --release --features gpu --bin <binary_name>
```

No proprietary data. No restricted access. No institutional dependencies.

## Cross-Spring Provenance (standalone barraCuda v0.3.5 at `03986ce`)

**Validated March 11, 2026** — all springs rewired to standalone `barraCuda`:

```
┌─ hotSpring v0.6.31 ─ spectral (Anderson, Lanczos, level statistics), 4-layer brain, precision brain, coralReef sovereign compile 46/46, Kokkos parity (12.4× gap, DF64 exp blocker), **VFIO PBDMA context load** (Exp 058, 3 Volta register discoveries, coralReef P10 Iter 44+)
├─ neuralSpring S145 ─ 27/27 papers + 5 compositions + 4 GPU experiments (Exp 103–106). 1115+73+9 tests, 258 binaries, 25 absorbed workloads, NUCLEUS GPU dispatch, sovereign compile on Ada GSP
├─ wetSpring V113 ──── 370 experiments, 9,886+ checks, paper extension roadmap (EMP 28K atlas, Liao real data, KBS LTER temporal, QS gene profiling, primal pipeline, LAN mesh plan)
├─ groundSpring V101 ── Kimura fixation, error threshold, jackknife, 13-tier tolerance, 102 delegations (61 CPU + 41 GPU), three-tier parity proven (29/29), DRY evolution, capability-based discovery
├─ airSpring v0.8.0 ── biomeOS composition: Provenance Trio integration (rhizoCrypt + loamSpine + sweetGrass via capability.call, graceful degradation), NestGateProvider three-tier routing, Cross-Spring Time Series v1, GPU compute provenance, 41 capabilities, 4 deploy graphs, 847 lib + 41 integration tests, 0 clippy warnings
├─ healthSpring V21 ── Hill, PBPK, population PK, Michaelis-Menten nonlinear PK, Anderson gut, antibiotic perturbation, SCFA, gut-brain serotonin, NLME (FOCE+SAEM), NCA, biosignal (Pan-Tompkins, HRV, EDA, arrhythmia), TRT, testosterone-gut axis, 6 WGSL shaders, metalForge routing, toadStool streaming, **Rust 84× faster** (Exp084), GPU scaling (Exp085), toadStool dispatch (Exp086), mixed NUCLEUS (Exp087), 61 experiments, 458 tests, deep debt (smart refactors, AGPL-3.0-only, named tolerances, provenance DOIs, determinism)
├─ ludoSpring V14 ──── 13 HCI models (Fitts, Hick, Steering, GOMS, Flow, DDA, Four Keys, Engagement, Perlin, WFC, L-systems, BSP, Tufte), 66 experiments, 1349 checks, 187 tests, 93.2% coverage, 0 clippy warnings (pedantic+nursery), barraCuda v0.3.5, deep audit complete (LCG unified, exp061 refactored, ValidationResult provenance, XDG capability discovery), 5 cross-spring provenance, 6 lysogeny, RPGPT + Games@Home
├─ wateringHole V69 ── Boltzmann sampling (Metropolis-Hastings MCMC)
├─ bingoCube/nautilus ─ NautilusBrain → BioNautilusBrain (concept edge, drift)
└─ multi-spring ────── special functions, bootstrap, correlation
```

All 767+ `barraCuda` WGSL shaders are f64-canonical with f16/f32/f64/Df64
precision dispatch per hardware. `barraCuda` is the standalone math primal
(WHAT to compute); `toadStool` handles hardware dispatch (WHERE and HOW).
Springs depend on `barraCuda` directly for math. Cross-spring evolution is
bidirectional: each spring's innovations flow through `barraCuda` and benefit
all springs.

## Cross-Spring Coordination

baseCamp papers are where springs meet. Each paper draws from multiple springs,
and future work on any spring is guided by what the baseCamp science needs.
This makes baseCamp the indirect coordination layer for the ecosystem.

```
                         baseCamp Papers
                              │
    ┌─────────────────────────┼─────────────────────────┐
    │                         │                         │
Paper 01 (Anderson QS)  Paper 06 (No-Till)         Paper 07 (WDM)
 wetSpring              wetSpring                   hotSpring
 hotSpring (spectral)   airSpring (ET₀)             neuralSpring (surrogates)
 groundSpring (spectral groundSpring (uncertainty   groundSpring (freeze-out
   theory validation)     bridge, rare biosphere)     inverse, spectral recon,
 neuralSpring (ESN)     neuralSpring (LSTM)           jackknife error bars)
    │                         │                         │
    │                         │                         │
Paper 04 (Sentinels)   Paper 03 (BioAg)           Paper 05 (Cross-Species)
 wetSpring (NPU)        wetSpring (Anderson)        wetSpring (metagenomes)
 neuralSpring (ESN)     airSpring (soil moisture)   neuralSpring (HMM)
 hotSpring (Akida)      groundSpring (sensor        groundSpring (transport,
 groundSpring (sensor     calibration, rare           band edge, quasispecies)
   noise, uncertainty)    biosphere, jackknife)
                              │
                        Paper 02 (LTEE)
                         wetSpring (16S)
                         neuralSpring (HMM, ESN)
                         groundSpring (drift vs
                           selection, quasispecies,
                           rare biosphere, jackknife)

Paper 08 (NPU Ag IoT)  Paper 09 (Field Genomics)
 airSpring (sensors)     wetSpring (16S, NPU, PFAS,
 wetSpring (NPU driver)    alignment, Anderson QS)
 neuralSpring (LSTM)     airSpring (soil sensors)
                         neuralSpring (ESN/LSTM)
                         groundSpring (rare biosphere,
                           uncertainty budgets)
                         hotSpring (akida-driver)

Paper 12 (Immuno-Anderson)
 wetSpring (Anderson spectral,
   cytokine lattice Exp270-274)
 neuralSpring (ESN regime,
   LSTM dose-response, IC50)
 groundSpring (transport,
   uncertainty bridge,
   spectral validation)

Paper 16 (Anaerobic-Aerobic QS)
 wetSpring (QS framework,
   16S pipeline, diversity)
 healthSpring (gut anaerobic)
 airSpring (soil O₂ zones)
 neuralSpring (ESN digester)
 groundSpring (spectral,
   uncertainty budgets)

Paper 17 (Game Design as Science)
 ludoSpring (13 HCI models,
   44 experiments, 410 checks,
   4 cross-spring: NCBI, NUCLEUS,
   Anderson QS explorer)
 barraCuda (sigmoid, dot,
   lcg_step primitives)
 toadStool (GPU dispatch)
 metalForge (cross-substrate)
 petalTongue (live dashboards)
 wetSpring (Anderson W model,
   QS propagation, disorder)
 nestgate (NCBI E-utilities,
   QS gene data)
 biomeOS (Tower Atomic:
   BearDog + Songbird)

Paper 18 (RPGPT — Sovereign RPG Engine)
 ludoSpring (Flow, DDA, engagement,
   session quality measurement)
 rhizoCrypt (session DAG, turn-based
   mode, condition tracking,
   branch diff/merge)
 loamSpine (ruleset certs, character
   sheets, NPC templates, world lore,
   item ownership)
 sweetGrass (creative attribution,
   player/AI/NPC derivation chains,
   FATE Aspects as semantic entities)
 Squirrel (AI narration constrained
   by loamSpine ruleset cert)
 BearDog (anti-cheat action signing =
   field genomics chain-of-custody)
 biomeOS (orchestration)

Paper 19 (Games@Home — Distributed Human Computation)
 ludoSpring (exp048-051: stack
   folding, novel data, design
   metric, Games@Home model,
   AR card gaming concept)
 rhizoCrypt (trajectory DAG —
   every decision point captured)
 sweetGrass (creative attribution —
   per-decision, cross-domain transfer)
 loamSpine (deck/ruleset certs,
   physical card provenance,
   model training data lineage)
 barracuda (validation math,
   combinatoric analysis)
 biomeOS (orchestration of
   AR devices, remote pod play)

Paper 20 (Novel Ferment Transcript Economics)
 ludoSpring (exp061: fermenting
   system, 89 checks, full lifecycle)
 rhizoCrypt (DAG history, session
   dehydration to loamSpine)
 loamSpine (certificate lifecycle,
   trading protocol: offer/accept/
   reject/cancel/atomic swap)
 sweetGrass (object memory API,
   PROV-O timeline export,
   radiating attribution chain)
 BearDog (Ed25519 signing for
   cryptographic binding)
 biomeOS (provenance_node_atomic
   deployment graph, Tower + Trio)
 sunCloud (radiating attribution
   activated by public chain anchor)

Paper 21 (Sovereign Sample Provenance)
 ludoSpring (exp062: field sample
   provenance, 39 checks + exp064:
   BearDog signing, 39 checks +
   exp065: cross-domain fraud, 74
   checks + exp066: radiating
   attribution, 41 checks)
 rhizoCrypt (sample lifecycle DAG)
 loamSpine (sample certificates,
   custody transfers)
 sweetGrass (collector/technician/
   analyst/PI attribution)
 BearDog (Ed25519 on every
   custody transfer)
 wetSpring (field genomics scaffold)

Paper 22 (Zero-Knowledge Medical Provenance)
 ludoSpring (exp063: consent-gated
   medical access, 35 checks +
   exp064/065/066 shared)
 rhizoCrypt (access event DAG)
 loamSpine (patient record certs,
   consent certs as scoped loans)
 sweetGrass (PROV-O audit trail,
   radiating attribution)
 BearDog (zero-knowledge access
   proofs, selective disclosure)
 healthSpring (clinical tracks
   scaffold: PK/PD, microbiome,
   biosignal, TRT)
```

**What each spring contributes:**

| Spring | Contributes To | Key Primitives |
|--------|---------------|----------------|
| wetSpring | 01, 03, 04, 05, 06 | Anderson QS, diversity, Bray-Curtis, FASTA, NCBI, NPU int8 |
| hotSpring | 01, 07 | Spectral theory (Lanczos, Anderson 3D), GPU MD, lattice QCD |
| airSpring | 03, 06, **08**, **12**, **16** | FAO-56 ET₀, soil moisture, Richards PDE, **NPU int8 eco classifiers, IoT sensor pipeline**, GpuDiversity (tissue W), CytokineBrain (AD flare prediction), barrier state (VG analogue), cross-species Anderson, **MC ET₀ uncertainty, Bootstrap/Jackknife CI, SPI drought index**, **soil O₂ zonation (aerobic/anaerobic QS boundary)** |
| neuralSpring | 01, 02, 04, 05, 06, 07, **13**, **16** | ESN/LSTM anomaly detection, WDM surrogates, HMM, transfer learning, **digester ML prediction (Paper 027: ESN methane yield, bC/gT validated)** |
| groundSpring | **01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13** | Spectral theory validation (Anderson, Almost-Mathieu, band edge, transport), uncertainty budgets, sensor noise calibration, rare biosphere, jackknife error bars, freeze-out inverse, spectral recon, drift vs selection, quasispecies threshold, WDM precision/convergence/vendor-parity, **NPU Anderson regime classification (AKD1000)**, metalForge cross-substrate validation, **immunological Anderson mapping (Exp 008/012/015/018 → cytokine propagation)** |
| **healthSpring** | **13**, **16** | **Hill, PBPK 5-tissue, population PK Monte Carlo, Michaelis-Menten nonlinear PK, Anderson gut lattice, FMT engraftment, antibiotic perturbation, SCFA production, gut-brain serotonin, Pan-Tompkins QRS, HRV/PPG SpO2/EDA stress/arrhythmia classification, WFDB, testosterone PK, TRT outcomes, testosterone-gut axis, NLME (FOCE+SAEM — sovereign NONMEM/Monolix), NCA (sovereign WinNonlin), 6 WGSL compute shaders, GPU dispatch + metalForge routing + toadStool streaming, petalTongue pipeline (28 nodes, 121 channels, 14 scenarios), gut as anaerobic QS system** |
| **ludoSpring** | **17, 18, 19, 20, 21, 22** | **Fitts's law, Hick's law, Steering law, GOMS, Flow theory, DDA, Four Keys to Fun, Engagement metrics, Perlin noise, WFC, L-systems, BSP trees, Tufte data-ink. 66 experiments, 1349 checks, 187 tests, 93.2% coverage. Playable prototypes (Doom terminal, roguelike), game telemetry protocol (NDJSON), 3 external game adapters (Veloren, Fish Folk, A/B Street), external control groups (bracket-pathfinding, noise-rs, fastnoise-lite). GPU dispatch + metalForge routing + NUCLEUS atomics + petalTongue live dashboards. Lysogeny catalog (6 proprietary mechanics from open math). Cross-spring provenance (fraud unification >80% similarity). RPGPT, Games@Home, Novel Ferment Transcript. Deep audit V14: 0 warnings, LCG unified, XDG capability discovery** |

groundSpring now contributes to ALL 10 active baseCamp papers (01-09, 12) —
reflecting the expansion from 5 experiments (sensor noise only) to 34 experiments
across 10 scientific domains including live NPU hardware. The spectral theory experiments (008, 009,
012, 018) validate the Anderson framework underlying papers 01, 05, and 06.
The Bazavov experiments (019-021) connect directly to paper 07's lattice QCD
science. The evolutionary biology experiments (014, 016, 017) serve papers 02
and 04. The WDM experiments (025-027) provide the uncertainty budget for paper
07's consumer GPU claims. Exp 028 (NPU Anderson classification on AKD1000)
directly validates the edge deployment architecture for papers 04, 08, and 09.
The metalForge cross-substrate validation (CPU + GPU + NPU parity on Anderson
localization) proves the mathematical portability that the entire baseCamp
program depends on.

**What each paper needs next (guides spring evolution):**

| Paper | Open Question | Springs Involved |
|-------|--------------|-----------------|
| 01 | DF64 Anderson at L=14-20 (large lattice, higher precision) | wetSpring × hotSpring × **groundSpring** (spectral validation at extended precision) |
| 02 | LTEE frozen fossil sequencing + sdiA expression | wetSpring × neuralSpring × **groundSpring** (drift vs selection quantification, jackknife error bars) |
| 03 | Pistachio/almond field inoculant trial design | wetSpring × airSpring × **groundSpring** (sensor calibration + rare biosphere monitoring of inoculant persistence) |
| 04 | Real-time HAB sentinel deployment (edge NPU) — **LIVE on AKD1000** | wetSpring × hotSpring (Akida) × **groundSpring** (uncertainty budget for detection threshold calibration, **NPU Anderson classification validated on live AKD1000 Exp 028**). V60: 3 ESN classifiers live, online evolution, PUF fingerprint, temporal streaming |
| 05 | Cross-kingdom metagenome 170-sample QS gene scan | wetSpring × neuralSpring × **groundSpring** (transport models for mycorrhizal relay) |
| 06 | Brandt farm real soil time series → r(t) prediction | wetSpring × airSpring × neuralSpring × **groundSpring** (uncertainty bridge: sensor → ξ → r) |
| 07/10 | WDM transport S(q,ω); **Dynamical QCD 32⁴ production** (Exp 024 8⁴ complete, Exp 025-027 scale-up); 4D Anderson + Wegner proxy pipeline | hotSpring × neuralSpring × **groundSpring** (spectral reconstruction + freeze-out + jackknife for lattice QCD observables; NPU GPU-conductor validation; Anderson CG proxy) |
| 08 | High-cadence NPU pipeline + field integration | airSpring (sensor + water balance) × wetSpring (NPU driver + ESN) × neuralSpring (LSTM time series) × **groundSpring** (NPU DMA validation, cross-substrate parity proof, uncertainty budget) |
| 09 | Nanopore + NPU field genomics end-to-end | wetSpring (16S + NPU + PFAS ML + alignment) × airSpring (soil sensors) × neuralSpring (ESN/LSTM) × **groundSpring** (rare biosphere + uncertainty + **metalForge cross-substrate dispatch validation**) |
| 11 | Live data stream prediction via Nautilus Shell | primalTools/bingoCube × hotSpring (trajectory data, NPU brain) × neuralSpring (ESN baseline comparison) × **groundSpring** (uncertainty budget for evolutionary vs recurrent reservoir) |
| 12 | Skin-layer Anderson lattice (2D epidermis + 3D dermis), barrier disruption dimensional promotion, ADDRC compound selection via Anderson-augmented MATRIX, Rho/MRTF/SRF cross-talk with JAK/STAT, Gonzales iPSC validation pipeline | wetSpring (Anderson spectral Exp270-286) × neuralSpring (nS-601–605: Hill, PK, IL-31, tissue, MATRIX) × **airSpring** (GpuDiversity, CytokineBrain, DriftMonitor, cross-species Exp066-069) × **groundSpring** (Exp 008/012/015/018 spectral + transport + uncertainty + band edge) |
| 13 | NLME GPU shaders (FOCE per-subject gradient, VPC Monte Carlo). NLME at scale (10K+ subjects). Multi-drug NLME for combination therapy. Population PK on GPU (100K patients). coralReef f64 lowering to replace f32 workarounds. QS gene profiling → effective disorder parameter. Real 16S data via NestGate. biomeOS NUCLEUS local integration. EDA SIMD optimization (numpy C convolution currently faster). | **healthSpring** (61 experiments, V20, 6 WGSL shaders, full-stack portability) × **barraCuda** (canonical ops — Hill, PopPK, diversity, MM batch, SCFA batch, beat classify) × **toadStool** (pipeline dispatch, streaming StageOp, V16 dispatch validated) × **metalForge** (cross-system routing, 9 Workload variants, NUCLEUS dispatch with P2P bypass) × **coralReef** (f64 transcendental lowering) × **petalTongue** (28-node pipeline, 121 channels) × **wetSpring** (diversity → gut health, QS genes) × **groundSpring** (uncertainty budgets) × **biomeOS** (NUCLEUS local, NestGate data) |
| 16 | ~~Reproduce Wang 2020 ML digester prediction~~ **(DONE — Paper 027, S142)**. Apply 16S pipeline to public anaerobic digester datasets (NCBI BioProjects: ADREC, municipal WWTPs). Map FNR/ArcAB/Rex-regulated QS genes via NCBI Protein. Model oxygen-dependent Anderson W. Test gut mucosal O₂ gradient → spatial W prediction. Extend ESN digester model to real operational data. | **wetSpring** (Anderson-QS, 16S, diversity) × **healthSpring** (Anderson gut lattice, anaerobic gut) × **airSpring** (soil O₂ zonation, Paper 06) × **neuralSpring** (ESN/LSTM time series, **Paper 027 digester benchmark COMPLETE**) × **groundSpring** (spectral W modeling, uncertainty) |
| 17 | ~~Anderson QS interactive explorer~~ **(DONE — exp044, 12/12)**. ~~NCBI QS gene data~~ **(DONE — exp041/043)**. ~~Tower Atomic boot~~ **(DONE — exp042, 10/10)**. ~~Deep audit~~ **(DONE — V14: 187 tests, 93.2% coverage, 0 warnings, LCG unified, exp061 refactored)**. GPU shader promotion (10 Tier A modules). Live biomeOS Continuous mode for 60 Hz. Engagement metrics for patient compliance (healthSpring). Fitts/Hick for medical UI evaluation. Real game telemetry from Veloren/Fish Folk sessions. Perlin noise absorption into barraCuda core (cross-spring critical). | **ludoSpring** (66 experiments, 1349 checks, V14) × **barraCuda** (sigmoid, dot, lcg_step consumed; Perlin absorption P0) × **toadStool** (GPU dispatch for 10 Tier A modules) × **metalForge** (cross-substrate routing) × **petalTongue** (live dashboards wired) × **biomeOS** (Tower Atomic validated — exp042) × **healthSpring** (Fitts/Hick for medical UI) × **wetSpring** (Anderson QS — exp044 validated W model, diversity dominates O₂) × **nestgate** (NCBI E-utilities — exp041/043, providers module needs wiring) |
| 18 | Ruleset-as-certificate format (PF2e, FATE, Cypher → loamSpine certs). Turn-based session DAG (rhizoCrypt action economy, condition decay, phase transitions). AI narration loop (Squirrel constrained by ruleset cert + ludoSpring quality metrics). Multi-agent creative attribution (sweetGrass player/AI/NPC derivation chains). NPC personality certs with knowledge bounds. World lore certs with canonicity levels. Branch diff/merge for "what if?" exploration. | **ludoSpring** (13 HCI models, Flow/DDA/engagement for session quality) × **rhizoCrypt** (session DAG, turn-based mode, condition tracking) × **loamSpine** (ruleset certs, character sheet certs, NPC templates, world lore) × **sweetGrass** (creative attribution, FATE Aspects as semantic entities) × **Squirrel** (AI narration constrained by anchored rules) × **BearDog** (anti-cheat action signing) × **biomeOS** (orchestration) |
| 19 | Open data source integration for visualization (Scryfall CC0 card data, EDHREC synergy rates, tournament meta snapshots). AR hardware prototype (glasses/projection for counter/token/stack management). Trajectory aggregation pipeline (session DAGs → strategic landscape models). Cross-domain transfer validation (game patterns applied to protein folding / drug discovery / materials science). Commander enzymatic card audit (measure branching effect of real card sets). | **ludoSpring** (exp048-051 validated, 127/127 checks) × **rhizoCrypt** (trajectory DAG capture at decision-point granularity) × **sweetGrass** (per-decision attribution, cross-domain transfer records) × **loamSpine** (deck-as-certificate, physical card provenance) × **barracuda** (combinatoric analysis, validation math) × **biomeOS** (AR device orchestration, remote pod play) |
| 20 | BearDog signing integration (every operation: vertex, cert, braid). Public chain anchor entry type in loamSpine. Owner inventory query (`list_by_owner`). Cross-session derivation links in rhizoCrypt. License-aware attribution notices (scyBorg). Radiating attribution calculator (sunCloud Phase 4). Physical-digital bridge (NFC/QR → certificate). Marketplace protocol as biomeOS graph. | **ludoSpring** (exp061 validated, 89/89 checks) × **loamSpine** (trading protocol DONE, anchor entry type needed) × **rhizoCrypt** (DAG history DONE, cross-session links needed) × **sweetGrass** (object memory DONE, license-aware notices needed) × **BearDog** (signing RPC needed) × **biomeOS** (provenance_node_atomic DONE, marketplace graph needed) × **sunCloud** (radiating attribution calculator — long-term) |
| 21 | wetSpring adoption (adapt SampleType/ProcessingStep to field genomics pipeline). Real BearDog signing (replace model signatures with live IPC). Public chain anchor for regulatory proof. Cross-institution provenance (songbird discovery for multi-lab chains). ISO 17025 compliance matrix (formal requirement → trio operation mapping). | **ludoSpring** (exp062/064/065/066 validated, 193 checks) × **wetSpring** (field genomics pipeline: sub_thesis_06) × **BearDog** (live Ed25519 signing RPC) × **biomeOS** (multi-lab deployment graph) × **songbird** (cross-institution discovery) |
| 22 | healthSpring adoption (adapt RecordType to clinical tracks). Full ZK proofs (BearDog ZK circuit for true zero-knowledge verification). FHIR/HL7 interop (loamSpine certificates → FHIR resources). Cross-institution consent (songbird for multi-provider chains). Patient portal (petalTongue consent visualization). Clinical trial consent certificates. | **ludoSpring** (exp063/064/065/066 validated, 189 checks) × **healthSpring** (clinical tracks: PK/PD, microbiome, biosignal, TRT) × **BearDog** (ZK circuit for access proofs) × **petalTongue** (patient consent portal) × **songbird** (cross-provider discovery) |

## Future Contributions

### Immediate (S80+)

- **Nautilus Absorption (DONE S80)**: `barracuda::nautilus` absorbed from
  bingoCube — 7 files, 22 tests, CPU-only. 8 `ai.nautilus.*` JSON-RPC
  methods in ToadStool daemon. Feature-gated `nautilus` in CLI.
- **BatchedEncoder (DONE S80)**: Fused multi-op GPU pipeline — single
  `queue.submit()` for MLP/Transformer forward passes.
- **Batch Nelder-Mead GPU (DONE S80)**: N parallel optimizations via
  batched simplex shaders. Available for isotherm fitting, multi-start
  optimization.
- **GpuDriverProfile Workarounds (DONE S80)**: Taylor-series sin/cos
  preamble for NVK driver. `asin`/`acos` protected.
- **ComputeDispatch at 95/250 (S80)**: 19 more ops migrated.

### Immediate (V63 — DONE)

- **Brain Architecture Integration (DONE V63)**: DriftAction, ConceptEdge,
  MultiHeadUncertainty from hotSpring/Nautilus. detect_concept_edges returns
  structured edges with drift action recommendations. seed_around_edges for
  focused phase boundary exploration.
- **NUCLEUS Capability Registration (DONE V63)**: 7 science.* capabilities
  registered/deregistered via biomeos::register_capabilities().
- **Hardcoded Primal Elimination (DONE V63)**: All primal names removed from
  routing and display labels. Capability-based discovery only.
- **Configurable Timeouts (DONE V63)**: biomeos connect/read timeouts via
  env vars.
- **Paper 12 Integration (DONE V63)**: Anderson immunological signaling
  mapped to groundSpring experiments 008/012/015/018.

### Previous Immediate (V61 — DONE)

- **Mixed-Hardware Pipeline Dispatch (DONE V61)**: groundSpring V61 adds `PCIe`
  topology modeling, multi-stage pipeline dispatch, NUCLEUS atomic types
  (Tower/Node/Nest/Full), and fallback chains. Infrastructure for NPU→GPU
  P2P bypass and mixed-substrate streaming. 42/42 validation checks, 120
  metalForge tests.
- **NPU Live (DONE)**: 3 ESN classifiers validated on real AKD1000 hardware
  (Exp193-195). Online evolution at 136 gen/sec, PUF fingerprinting (6.34 bits),
  12.9K Hz temporal streaming. Coin-cell viable (1.4 µJ/infer).
- **Field Genomics Architecture (DONE)**: Sub-thesis 06 defines MinION +
  AKD1000 + BarraCUDA for autonomous environmental sentinels. Experiments
  196-202 planned pending sequencer hardware.
- **Data Type Profiling (DONE)**: Comprehensive catalog of biological data
  types in `wetSpring/specs/DATA_TYPES.md` for NestGate evolution.
- **DF64 Anderson**: Extended precision (f64-pair) for large Anderson
  lattices (L=14-20). Phase 1 validated at f64 (Exp187); Phase 2 will
  use DF64 shaders from hotSpring.

### Immediate (V62 — DONE)

- **ToadStool S79 Catch-Up (DONE)**: Full rewire to `ToadStool` S79
  (`f97fc2ae`). Pollster dependency eliminated — all async bridging now
  uses `barracuda::device::test_pool::tokio_block_on`. GPU device
  initialization upgraded to `WgpuDevice::new_f64_capable()` with
  automatic fallback to `WgpuDevice::new()`. DF64 precision strategy
  wired end-to-end.
- **Shader Cleanup (DONE)**: 2 redundant local WGSL shaders
  (`mc_et0_propagate.wgsl`, `batched_multinomial.wgsl`) removed — both
  absorbed into ToadStool's f64-canonical bio shader library. Only 2
  unique Anderson Lyapunov shaders retained in metalForge.
- **Cross-Spring Shader Lineage (DONE)**: Full provenance documented in
  V62 handoff — tracing shader contributions across hotSpring (precision),
  wetSpring (bio), neuralSpring (domain), airSpring (hydrology), and
  groundSpring (spectral) through ToadStool's unified shader library.
- **License Harmonization (DONE)**: All `Cargo.toml` SPDX identifiers
  updated to `AGPL-3.0-only` for consistency with workspace root.
- **Validation (DONE)**: 710 workspace tests, 23/23 cross-spring
  benchmark, 39/39 GPU tier, 13/13 Titan V + RTX 4070 validation.
  Zero clippy warnings (pedantic + nursery), zero unsafe.

### Immediate (airSpring v0.6.1 — DONE)

- **ToadStool S79 Absorption (DONE)**: airSpring v0.6.1 absorbs ToadStool S79
  modernization — `libc`→`rustix`, `async-trait`→AFIT, universal f64 precision,
  `pollster`→`test_pool`. 7 new GPU orchestrators wired: `BatchedVanGenuchten`
  (ops 9-10: soil hydraulics θ(h)/K(h)), `BatchedThornthwaite` (op 11),
  `BatchedGdd` (op 12), `BatchedPedotransfer` (op 13), `GpuJackknife`,
  `GpuBootstrap`, `GpuDiversity` (Shannon/Simpson/Pielou). All with CPU
  fallbacks and unit tests. 25 Tier A GPU modules total (up from 15).
- **Cross-Spring Provenance Tracking (DONE)**: `ShaderProvenance` entries
  added for all new GPU modules — tracking origin across hotSpring (precision
  shaders), wetSpring (bio diversity), groundSpring (uncertainty stack),
  and airSpring (hydrology/ecology). `bench_cross_spring_evolution` binary
  extended with S79 ops 9-13 and GPU uncertainty benchmarks.
- **Validation (DONE)**: 737 lib tests, 94.15% llvm-cov coverage, zero
  clippy warnings (pedantic + nursery), `cargo doc` clean. Cross-spring
  evolution benchmark and GPU uncertainty stack fully exercised.
- **Directly enables**: Paper 06 (GPU van Genuchten for soil hydraulics at
  scale), Paper 03 (GPU pedotransfer for inoculant trial design), Paper 08
  (GPU uncertainty for NPU edge confidence intervals).

### Immediate (airSpring v0.6.4 — DONE)

- **GPU Multi-Field Pipeline (DONE)**: `SeasonalPipeline::run_multi_field()`
  dispatches Stage 3 (WB) to GPU per-day across M fields via `gpu_step()`.
  6.8M field-days/s at atlas scale (50 stations × 153 days). `MultiFieldResult`
  tracks GPU dispatch count for instrumentation.
- **CPU Parity Benchmark (DONE)**: 9 domains validated against Python, 34/34 PASS.
  13,000× Rust-vs-Python at atlas scale. Key throughputs: ET₀ 10M/s, Kc 1.9B/s,
  WB 162M days/s, seasonal pipeline 59K seasons/s.
- **Pure GPU End-to-End (DONE)**: All 4 stages on GPU (ET₀+Kc+WB+Yield), 46/46 PASS.
  19.7× GPU dispatch reduction for 20 fields. CPU↔GPU parity within 2mm seasonal.
- **metalForge 7-Stage Cross-System (DONE)**: Weather(CPU) → ET₀(GPU) → Kc(GPU) →
  WB(GPU) → Yield(GPU) → CropStress(NPU) → Validation(CPU). 66/66 PASS. GPU→NPU
  via PCIe P2P bypass. GPU stages 2-5 stay on device (zero CPU round-trips).
- **Validation (DONE)**: 815 lib tests (at v0.6.4), 82 binaries, 72 experiments,
  zero clippy pedantic warnings, all provenance documented.
- **Directly enables**: Paper 06 (atlas-scale multi-field GPU for no-till vs tilled
  comparison), Paper 08 (NPU edge with GPU-computed uncertainty intervals),
  Paper 12 (tissue diversity GPU + CytokineBrain streaming pipeline).

### Immediate (airSpring v0.6.6 — DONE)

- **Cross-Spring Rewire (DONE)**: `BrentGpu` wired into VG inverse (θ→h on GPU),
  `RichardsGpu` wired into Richards PDE (GPU Picard+CN+Thomas solver).
  68/68 cross-spring provenance validation — all 5 springs verified.
- **ToadStool S87 Sync (DONE)**: Absorbed `StatefulPipeline`, `BatchedStatefulF64`,
  `BrentGpu`, `RichardsGpu`, `BatchedNelderMeadGpu`, `nautilus`, `L-BFGS`,
  `anderson_4d`. Tier B→A promotions for water balance and isotherm.
- **Cross-Spring Evolution Benchmark (DONE)**: 138/138 PASS across S80-S87
  primitives. 68/68 rewire PASS across 5 springs.
- **Validation (DONE)**: 815 lib tests, 83 binaries, 73 experiments, zero clippy
  pedantic warnings, all provenance documented.
- **Directly enables**: Fused `SeasonalPipelineF64` adoption, batched multi-column
  Richards GPU, Green-Ampt/pedotransfer GPU shaders.

### Immediate (airSpring v0.6.8 — DONE)

- **Local GPU Compute Evolution (DONE)**: 6 element-wise ecological operations now
  run on GPU via `local_elementwise.wgsl` (f32 WGSL compute shader dispatched through
  wgpu directly). Operations: SCS-CN runoff (op=0), Stewart yield (op=1), Makkink ET₀
  (op=2), Turc ET₀ (op=3), Hamon PET (op=4), Blaney-Criddle (op=5).
- **`gpu::local_dispatch::LocalElementwise` (DONE)**: New wgpu dispatch engine —
  compiles shader, manages buffers, handles f64↔f32 conversion. Demonstrates the
  "write locally → absorb upstream → lean" cycle at the shader level.
- **metalForge Workload Expansion (DONE)**: 27 ecological workloads (21 existing +
  6 new with `ShaderOrigin::Local`). ToadStool absorption converts to `::Absorbed`.
- **NUCLEUS Mesh Routing (DONE)**: Exp 076 validates full NUCLEUS pipeline —
  capability-based dispatch, PCIe P2P bypass, Tower/Node/Nest atomics, multi-node
  cross-hop routing. 60/60 PASS.
- **ToadStool Absorption Handoff (DONE)**: V051 handoff documents proposed ops 14-19
  for `batched_elementwise_f64.wgsl`, precision characteristics, helper function
  mapping to existing df64 transcendentals. V053 consolidates absorption guide with
  cross-spring evolution intelligence, GPU driver insights, and performance data.
- **Exp 077 Cross-Spring Provenance (DONE)**: CPU↔GPU benchmark with 5-spring shader
  provenance tracking. Validates precision lineage (hotSpring→all), uncertainty stack,
  seasonal pipeline parity. 32/32 PASS.
- **Validation (DONE)**: 846 lib tests, 86 binaries, 77 experiments, zero clippy
  pedantic warnings. 146/146 cross-spring evolution benchmark + 32/32 provenance.
- **Directly enables**: ToadStool f64 absorption of 6 local ops (tightens tolerances
  by 6+ orders of magnitude), fused seasonal pipeline, full GPU-first workload chain.

### Immediate (airSpring v0.6.9 — DONE)

- **f64-Canonical Universal Precision (DONE)**: Evolved `local_elementwise.wgsl` (f32)
  to `local_elementwise_f64.wgsl` (f64 canonical) compiled via `compile_shader_universal()`.
  F64 native on pro GPUs (Titan V), F32 downcast on consumer GPUs (RTX 4070). "Math is
  universal, precision is silicon."
- **Deep Debt Audit (3 rounds — DONE)**: Provenance normalization (47 benchmark JSONs →
  `_provenance` key), `json_f64_required` structured failure (exit(1) not panic),
  `SubmitParams` refactor for wgpu dispatch, env-configurable RPC timeout
  (`BIOMEOS_RPC_TIMEOUT_SECS`), `bench_cpu_vs_python` multi-file refactor, BarraCuda
  `variance`/`std_dev` primitive wiring (zero local math duplication), streaming JSON I/O,
  all `#[allow]` annotations with reason strings.
- **Cross-Spring Evolution Benchmark (DONE)**: Exp 078 validates universal precision
  evolution across 6 f64-canonical ops, confirming `compile_shader_universal()` correctness.
- **Validation (DONE)**: 852 lib + 33 integration + 62 forge tests (947 total), 86 binaries,
  78 experiments, 95.66% line coverage, zero clippy pedantic+nursery warnings, zero unsafe,
  zero mocks in production. All provenance normalized with commit-level traceability.
- **Directly enables**: BarraCuda absorption of 6 f64-canonical local ops (ready for
  `batched_elementwise_f64` ops 14-19), cross-spring `compile_shader_universal()` pattern.

### Medium-term

- **`SeasonalPipelineF64` adoption**: Move from per-stage dispatch to fused upstream
  seasonal GPU pipeline (ET₀→Kc→WB→stress in one shader).
- **Batched Richards GPU**: M soil columns in one dispatch (amortize per-field overhead).
- **Green-Ampt + SCS-CN GPU**: Coupled runoff-infiltration on GPU for watershed-scale.
- **Pedotransfer GPU**: Saxton-Rawls θs/θr/Ks from texture (embarrassingly parallel).
- **Multi-GPU field parallelism**: Use upstream `multi_gpu` for horizontal scaling.
- **NCBI sovereign scaling**: Multi-BioProject sovereign pipeline
  via NestGate JSON-RPC, replacing all institutional API dependencies.
- **Cross-spring shared tolerances**: wetSpring's 86 named tolerance
  constants (with provenance) as a pattern for all springs.

### Long-term

- **metalForge cross-substrate**: GPU→NPU→CPU dispatch for heterogeneous
  workloads. NPU handles streaming sentinel inference while GPU handles
  batch Anderson spectral analysis.
- **LTEE validation**: Sequencing data from Lenski's frozen fossil record
  to test constrained evolution predictions (Paper 02).
- **Field deployment**: Sentinel microbe prototype using Akida NPU for
  real-time HAB prediction (Paper 04).
- **Field genomics (Paper 09)**: MinION nanopore sequencer as a new
  metalForge substrate class (SEQ). Sovereign Rust pipeline from raw
  signal to classified community state: MinION → BarraCUDA 16S → AKD1000
  NPU classification → adaptive sampling feedback. Target deployments:
  Great Lakes HAB monitoring (Saginaw Bay / Lake Erie), soil health
  sentinel for no-till monitoring, AMR wastewater surveillance, PFAS
  dual-mode detection. NPU-driven adaptive sampling provides 37x headroom
  over MinION read generation. New BarraCUDA modules: `io::nanopore`
  (FAST5/POD5 reader), `bio::basecall` (signal → base). All downstream
  math operational (4,748+ checks). Experiments 196-202 planned.
