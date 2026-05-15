# baseCamp: Independent Explorations Alongside the Constrained Evolution Thesis

**Date:** May 2026 — **Phase 60+ / post-interstadial** — Cell membrane architecture + deep debt evolution sweep complete. **13/13 NUCLEUS primals** deployed, all BTSP Phase 3 AEAD. **MethodGate enforced**: **13/13** primals (toadStool + squirrel resolved May 11). **darkforest v0.2.1**: pure Rust security validator. **Cell membrane**: primals.eco on CDN (extracellular), lab/git.primals.eco via tunnel replicas (membrane), sovereign compute inside. **pappusCast**: modular 7-module daemon (Python→Rust→Primal path). **8/8 springs** Tier 4 IPC-first, 13,100+ tests. **Deep debt swept**: zero hardcoded paths, gate-agnostic systemd, spec reconciliation, upstream handbacks. **Next priority**: NestGate content pipeline for full data/compute chains. Current: wetSpring V163 (1,613 tests), neuralSpring S201b (1,453 tests), groundSpring V135 (1,125 tests, LTEE B2+B1 DONE), healthSpring V63 (999 tests), airSpring v0.10.0 (1,389 tests), ludoSpring V63 (854 tests), hotSpring v0.6.32 (1,025 tests, LTEE B2 + 3-GPU sovereign)
**Author:** Kevin Mok (BS Microbiology, MSU 2018; MS Data Science, MSU 2025)

**wetSpring V137:** Full provenance + tolerance centralization + IPC modularization — `//! Provenance:` headers on all 355 validation/benchmark binaries (first spring with 100% binary provenance), 8 new named tolerance constants (242 total, zero inline literals), `ipc/connection.rs` extraction (protocol pipeline separated from server lifecycle), GPU buffer renames. 1,902 tests, 355 binaries, 242 named tolerances, 91.20% coverage. V136: thiserror, named casts (~60), upstream contract pinning, determinism tests, CI pin, hardcoding audit, CONTRIBUTING + SECURITY. V135: doc reconciliation. V134: drug NMF delegation, validation harness refactored, primal discovery extended.

**Provenance Pipeline Elevation (May 2026):** The provenance trio is now **operationally validated** end-to-end. projectNUCLEUS deployed full NUCLEUS (13 primals) on ironGate and ran the full ABG pipeline (235+ checks, 10 workloads, real NCBI data from PRJNA488170) with every artifact content-addressed via BLAKE3, tracked in rhizoCrypt DAG sessions (26 events), committed to loamSpine permanent ledger (SessionCommit with Merkle root), and witnessed via sweetGrass ed25519 attribution braid. This is the first live validation of the python → rust → primal composition → provenance chain described in Papers 20-22 and 26.

**RootPulse Commit Workflow (May 7, 2026):** The `rootpulse_commit.toml` graph was ported to projectNUCLEUS and tested phase-by-phase against live primals. Results: health checks PASS (rhizoCrypt + LoamSpine), DAG dehydration PASS (merkle root returned), BearDog Ed25519 signing PASS, NestGate KV storage PASS, sweetGrass braid creation PASS (W3C PROV witness). LoamSpine commit (Phase 5) FAIL — method name and parameter structure mismatch between graph spec and primal API. The workflow is **80% executable today**. 5 upstream gaps documented in `projectNUCLEUS/validation/ROOTPULSE_GAPS_HANDBACK.md`. This is the first attempt to run the RootPulse distributed VCS workflow against real infrastructure.

**Sovereignty Evolution (May 7–15, 2026):** 40+ dependencies mapped across 7 clusters. Forgejo v15.0.0 installed → now **PRIMARY git host** (32 repos, 3 orgs, GitHub is push mirror). VPS Tower composition LIVE (2GB, BearDog + SkunkBat + Songbird + RustDesk + Caddy). Channel 3 TLS shadow active. Content-aware routing prototype deployed. petalTongue + NestGate gaps ALL SHIPPED upstream (PT-1→PT-5, NG-1→NG-4). See `projectNUCLEUS/specs/EVOLUTION_GAPS.md`.

**Multi-User Security Hardening (May 7, 2026):** Live pentest from compute-tier user (tamison) via `nucleus-security-validation.ipynb`. Critical finding: `NUCLEUS_READONLY=1` env var was convention with zero enforcement — reviewer-tier users could execute arbitrary code (JH-0). Fixed with 4 hardening layers: (1) `hidepid=2` on /proc hides primal PIDs from ABG users, (2) iptables/ip6tables owner match blocks all outbound internet for ABG UIDs (localhost + LAN preserved), (3) reviewer/observer tiers: no kernels, no terminals, filesystem read-only (root-owned chmod 550), (4) shared notebooks immutable (chmod 444, compute users run but can't save back). 5 new upstream gaps documented in `projectNUCLEUS/validation/JUPYTERHUB_PATTERNS_HANDBACK.md` (JH-0 through JH-5). Key pattern: convention flags are not security — every capability restriction must be enforced at the gate.

**Phase 60 Absorption + MethodGate Enforced (May 8, 2026):** Pulled primalSpring v0.9.25, all 15 primals at HEAD, plasmidBin v2026.05.08. JH-0 through JH-5 all resolved upstream. MethodGate enforced on 10/13 primals via TCP `auth.mode`. Ionic token flow validated end-to-end: `identity.create` → `auth.issue_session` → `_bearer_token` → MethodGate accepts. Scope rejection confirmed. Cross-primal federation deferred (JH-11). Full validation: 265 PASS, 0 FAIL, 0 KNOWN_GAP, 5 DARK_FOREST. DNS exfil closed (JH-8), supply chain locked (JH-9).

**darkforest v0.2.0 — Pure Rust Security Validator (May 8, 2026):** Modular auditable security framework in `projectNUCLEUS/validation/darkforest/` — 939KB binary, zero runtime deps. 7 source modules: `check.rs` (structured types, OCSF-inspired), `net.rs` (TCP/HTTP helpers), `pentest.rs` (3 threat actors), `fuzz.rs` (13 primals + JupyterHub), `crypto.rs` (13 crypto strength checks: CRY-01→CRY-13), `report.rs` (pipe + JSON output), `main.rs` (CLI + runner). Supersedes legacy bash/python pen test tools. **175 PASS, 0 FAIL, 6 DARK_FOREST**. `--output <path>` for auditable structured JSON reports with per-check severity, category, evidence, remediation, and timestamps. Demonstrates python → Rust → primal validation of peer-reviewed science security posture.

**ABG Workspace Scaffolding (May 8, 2026):** Workspace lifecycle: scratch → commons → pilot → projects → showcase → public. Pilot lifecycle with `abg_accounts.sh create-pilot` subcommand (hypothesis, decision criteria, timeline). Per-user private `scratch/` (chmod 700). Reviewer showcase-only visibility via symlink-level isolation (reviewers see `~/notebooks/showcase/` instead of full `~/notebooks/shared/`). Tier-appropriate `Welcome.ipynb` symlinked at login for all 4 tiers (admin, compute, reviewer, observer). Validation dashboard (`showcase/validation-dashboard.ipynb`) surfaces darkforest JSON via Voila. READMEs in all shared directories. Work lifecycle mirrors scientific method: explore, structure, formalize, publish, share.

**ABG Compute Usability (May 8, 2026):** Per-user Python venvs (`~/.venv/bioinfo/`, `--system-site-packages` on shared bioinfo env). Local wheelhouse (`/home/irongate/shared/abg/wheelhouse/`) for offline `%pip install` — admin provisions packages, users install freely without internet. `pre_spawn_hook` PATH priority for user venv binaries. `Getting-Started.ipynb` onboarding notebook in commons. `deploy/wheelhouse_sync.sh` admin utility for wheelhouse management. Key pattern: user-facing simplicity (just `%pip install`) backed by mechanism-level enforcement (no-index, find-links, venv isolation).

**Open Observer + pappusCast (May 9, 2026):** The observer surface is now open — no credentials, no login. `lab.primals.eco` is the default landing page, rendering the entire project as read-only notebooks via Voila. This is the Python→Rust→Primal validation of peer-reviewed science made tangible: the science is the public artifact, the compute is the gated workspace, and the propagation between them is automated and validated.

**pappusCast daemon** (named for the dandelion pappus — the parachute that carries seeds to new ground) auto-propagates validated content from the compute workspace to the observer surface. Three-tier validation: Light (on-change: structural), Medium (periodic: execution), Heavy (~6h: regression + changelog). Adaptive rate limiting scales publish interval with active JupyterHub users. Snapshot architecture replaces live symlinks with managed copies — the observer surface is stable, validated, and decoupled from active editing. Evolution path: Python (now) → Rust binary → pappusCast primal. This directly demonstrates Paper 26's thesis (primal composition as scientific methodology) — the validation pipeline itself evolves through the ecosystem's own patterns.

**Multi-Tier Test Suite (May 9, 2026):** `tier_test_observer.py`, `tier_test_reviewer.py`, `tier_test_compute.py`, and `tier_test_all.sh` exercise each access level end-to-end. The test suite surfaced and fixed: kernel mismatches on 8 notebooks, missing metadata titles, relative path errors after snapshot conversion, dashboard KeyError on status normalization, package import issues. Pattern: tier-specific testing is the traveling salesman problem of shared systems — each access level must be independently validated because their constraints compose non-linearly.

**tunnelKeeper Rust Crate (May 9, 2026):** `validation/tunnelKeeper/` — programmatic Cloudflare tunnel health checks, DNS resolution fallback chain (`getent` → `host` → `dig`), config file parsing. Integrated into darkforest pen test as A6 (tunnel health). First step toward Rust-native Cloudflare interaction — the Python→Rust evolution applied to infrastructure management. tunnelKeeper may absorb into songBird when Songbird replaces cloudflared.

**Cell Membrane Architecture (May 10, 2026):** Architectural inversion — `primals.eco` permanently on GitHub Pages CDN (extracellular), `lab/git.primals.eco` via Cloudflare tunnel replicas (membrane), sovereign compute inside (intracellular). `gate_provision.sh` provisions remote hosts as membrane replicas with sub-second failover. Key insight: accept that the extracellular world is uncontrolled; inside the membrane, total sovereign control. The boundary is a clean delineation for skunkBat audit data and future ionic/weak bonding as gated channels.

**Deep Debt Evolution Sweep (May 11, 2026):** The final structural cleanup of projectNUCLEUS before full data/compute chain work. `pappusCast.py` (953 lines — the only >800L file) smart-refactored into 7 modules (`pappuscast/{config,state,tiers,publisher,export,daemon}.py` + thin CLI). All hardcoded `/home/irongate` paths eliminated from Rust (`pentest.rs`, `crypto.rs`) via `gate_home()` env-var pattern. Four systemd units parameterized via `EnvironmentFile=/etc/projectnucleus/gate.env`. Superseded Python tier test archived. Exception blocks narrowed. Three spec docs reconciled against current state. MethodGate claim corrected to 11/13 → subsequently resolved to **13/13** (toadStool + squirrel shipped May 11). barraCuda crypto delegation target documented. This demonstrates the Python→Rust→Primal evolution applied to the validation infrastructure itself — pappusCast moves from monolith to modular Python, tier tests migrate from Python to Rust (darkforest), and deploy scripts evolve toward `composition.deploy(graph)`.

**NestGate Priority (May 11, 2026):** NestGate is the critical upstream dependency for next-round evolution. NestGate runs in the composition (port 9500, alive) but lacks the content pipeline (`content.put`, collections, manifests) needed for: (1) sovereign `primals.eco` serving via petalTongue, (2) plasmidBin binary hosting (replacing GitHub Releases), (3) OCI blob storage (replacing Docker Hub/ghcr.io). Full data/compute chains require NestGate storage → rhizoCrypt provenance → sweetGrass attestation → loamSpine ledger as a complete path. H2-05 through H2-08 in EVOLUTION_GAPS.md track this.

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
| 07 | Sovereign Warm Dense Matter Simulation on Consumer GPU | Plasma Physics × Distributed Computing | hotSpring Tier 4 + neuralSpring surrogates + groundSpring uncertainty | WDM transport on $600 GPU; deconfinement at β_c=5.69 on $1,500 GPU; **11-head NPU GPU conductor** (Exp 023); coralReef sovereign compile **46/46** shaders (Iter 33); 12/12 NVVM bypass; FMA lowering (`FmaPolicy::Separate`); precision brain self-routing (12 domains); **Exp 053: live Kokkos parity** — 9/9 cases, 12.4× gap (DF64 transcendental poisoning fix); **Exp 058: VFIO PBDMA context load** — 3 Volta register discoveries (preempt 0x2638, ACK 0x2A00, SIGNATURE), PBDMA2 loads RAMFC zero-error, USERD DMA read remaining. coralReef P10 Iter 44+. Dual Titan V planned. **guideStone v0.7.0: universal deployment artifact — 5 substrates, cross-arch, OCI container.** | **Validated** — hotSpring v0.6.31. **guideStone-certified** — artifact deployable on any OS/arch. |
| 08 | Neuromorphic Edge Intelligence for Sovereign Agricultural IoT | Agricultural IoT × Neuromorphic Computing | airSpring Exp 028-029 (88 checks) + wetSpring NPU driver | NPU inference at 0.0009% of active cycle energy; 10.7× more efficient than cloud; 1-min cadence unlocked; multi-crop hot-swap | **Validated on Live Hardware** — AKD1000, streaming + evolution + power budget. airSpring v0.10.0 (March 24, 2026): 986 lib + 316 integration + 62 forge = 1,364 Rust tests; barraCuda 0.3.7 (wgpu 28), `default-features = false` (gpu + domain-pde only); fused Welford + Pearson wired, 14.3× CPU speedup (24/24 parity), 90.56% line coverage, cargo-deny 0.19 clean, zero `#[allow()]`, CONTRIBUTING/SECURITY, upstream contract pinning, deploy graph metadata |
| 09 | Sovereign Field Genomics — Nanopore + NPU | Environmental Genomics × Edge Inference | wetSpring Exp193-195 (NPU) + Exp184-185 (16S) + planned Exp196-202 | MinION sequencing + AKD1000 classification + BarraCuda 16S pipeline = autonomous field sentinel. NPU-driven adaptive sampling (37x read-rate headroom). No cloud, no Python. | **Architecture defined** — all compute components validated, awaiting sequencer hardware |
| 10 | First Dynamical QCD Production on Consumer GPU | Lattice QCD × Neuromorphic Computing | hotSpring Exp 024 (8⁴ dynamical, 1,031+ traj, 17 β points), Exp 028-031, **Exp 099-103** | First NPU-steered dynamical fermion QCD scan. Smooth crossover confirmed. β_c ~ 5.5. NPU expanded 4-seed scan to 17 points. CG–disorder correlation validates Anderson proxy. **Exp 031: NPU controls dt/n_md with mid-beta adaptation, targeting 70% acceptance.** **Exp 099-103: GPU RHMC (Nf=2, 2+1), gradient flow at volume, self-tuning calibrator — zero hand-tuned magic numbers.** **guideStone v0.7.0: 59/59 checks × 5 substrates, cross-arch (x86_64 + aarch64 bit-identical), OCI container, universal deployment.** | **Complete + Evolving** — 17 β points, Nf=2+1 RHMC, self-tuning calibrator (Exp 103). **guideStone-certified**, benchScale 5-substrate validated (40/40 cross-substrate parity). |
| 11 | The Nautilus Shell — Evolutionary Reservoir Computing from Bingo Boards | Reservoir Computing × Neuromorphic × Evolutionary Algorithms | primalTools/bingoCube/nautilus/ (31 tests, 5 examples); **ToadStool S80**: barracuda::nautilus (7 files, 22 tests, 8 JSON-RPC methods) | Bingo boards as structured random projections; evolutionary generations replace temporal recurrence for feed-forward hardware; nautilus shell = layered evolutionary history, portable between instances. Column-range-preserving crossover maps natively to AKD1000 int4. Self-regulating drift monitor + edge seeding. AKD1000 int4 weight export. Quenched→dynamical transfer: 540× cost reduction. | **Validated** — 5.3% LOO CG error, 2.6% blind prediction on Exp 029, 31 tests. **S80**: Standalone absorption into ToadStool/BarraCuda (7 files, 22 tests, 8 ai.nautilus.* JSON-RPC methods). |
| 12 | Anderson Localization in Immunological Signaling — Cytokine Propagation, Drug Geometry, and the Fajgenbaum Repurposing Bridge | Immunology × Condensed Matter Physics × Pharmacology × Drug Repurposing | wetSpring Exp273-286 (359/359), neuralSpring nS-601–605 (329/329), airSpring Exp066-069 (94/94), groundSpring Exp008/012/015/018 | Cytokine (IL-31/IL-4/IL-13) propagation through inflamed skin tissue follows Anderson localization; AD barrier disruption = dimensional promotion (inverse of Paper 06 tillage collapse); Fajgenbaum MATRIX drug-disease scoring gains geometry dimension via Anderson transport; **groundSpring** provides 2D/3D spectral validation (Exp 008), cytokine transport modeling (Exp 012), uncertainty bridge (Exp 015), band edge for epidermal periodicity (Exp 018), ConceptEdge for AD flare detection, DriftAction for treatment steering. **MSU Drug Discovery pipeline**: Anderson-augmented MATRIX scores (nS-605) → ADDRC HTS (8,000+ compounds, Lisabeth) → Gonzales iPSC validation → Ellsworth medicinal chemistry. Neubig Rho/MRTF/SRF skin fibrosis → cross-talk with JAK/STAT open question | **Validated** (Gonzales G1-G6 + Fajgenbaum MATRIX complete); **Evolving** (ADDRC pipeline, Rho cross-talk, skin-layer lattice). Source: Dr. Andrea J. Gonzales (MSU Pharmacology & Toxicology), Erika Lisabeth (ADDRC Director), Richard Neubig (Drug Discovery Director) |
| 13 | Sovereign Human Health Computing — Per-Person Translation of PK/PD, Microbiome, Biosignal, Endocrine, NLME, Comparative Medicine, Drug Discovery, Toxicology, Simulation | Human Health × Pharmacology × Microbiome × Biosignal × Endocrinology × NLME × Comparative Medicine × Drug Discovery × Toxicology × Simulation | healthSpring Exp001-111 (83 experiments). 928 tests, 113/113 cross-validation checks (all 9 tracks). barraCuda v0.3.7 (6 GPU ops). | **9-track human health spring + per-person translation**: PK/PD (Hill, PBPK, population PK, Michaelis-Menten, NLME FOCE+SAEM, NCA), Microbiome (Anderson gut, FMT, antibiotics, SCFA, serotonin), Biosignal (Pan-Tompkins, HRV, SpO2, EDA, arrhythmia, WFDB), Endocrinology (testosterone PK, TRT, gut axis), Comparative Medicine (canine AD, feline hyperthyroid, cross-species PK), Drug Discovery (MATRIX, ADDRC HTS, compound library, fibrosis), Toxicology (Anderson delocalization, hormesis, mithridatism), Simulation (multi-scale causal chain). 6 WGSL shaders (absorbed by barraCuda), 59 JSON-RPC capabilities (46 science + 13 infra), 54 Python baselines. **V44: Deep debt + modern idiomatic Rust** — `primal_names` module (zero hardcoded primal strings), `gpu/mod.rs` smart-refactored (696→413 LOC), provenance registry accessors, toadStool 51 tests, WFDB 11 annotation tests, tolerance migration (8 experiments), TensorSession evaluated, FFT absorption documented. **V40: Cross-ecosystem absorption** — 39 new tests, 17 magic numbers extracted, provenance smart-refactored. **V39: Toxicology/Simulation** — 3 new domains, cross-spring hormesis. **V38: Deep debt** — all experiments ValidationHarness. Zero clippy (pedantic+nursery), zero unsafe, zero `#[allow]`. | **Validated** — V44, Tier 0+1+2+3 complete, 9 tracks. Source: Gonzales (PK/PD + Drug Discovery), Mok (clinical TRT), Beal & Sheiner (FOCE), Kuhn & Lavielle (SAEM) |
| 15 | Self-Routing Precision Brain for Heterogeneous GPU Compute | GPU Computing × Precision Engineering × Hardware Discovery | hotSpring Exp 049-051 (precision eval + coralReef sovereign validation + Iter 30 FMA/hardware data) | Data-driven self-routing brain discovers hardware, routes physics to optimal precision tier per-domain (12 domains), survives NVIDIA NVVM device poisoning. coralReef sovereign bypass integrated: 46/46 compile, 12/12 NVVM bypass patterns, FMA lowering (`FmaPolicy::Separate`) unlocks F64Precise via sovereign path. Portable across springs. toadStool S146 absorbed PrecisionBrain with `PrecisionHint` routing + `NvkZeroGuard`. | **Validated** — hotSpring v0.6.29 |
| 16 | Anaerobic-Aerobic QS Phase Transition — Microbial Signaling Across Oxygen Regimes | Microbial Ecology × Environmental Engineering × Anderson Localization | Planned — bridges wetSpring (QS), healthSpring (gut), airSpring (soil O₂), ADREC digesters. **neuralSpring benchmark: Paper 027 (Wang/Liao 2020 digester prediction) COMPLETE** — ESN methane yield predictor, 36/36 CPU + 23/23 bC/gT PASS. **wetSpring Exp356 (V110): O₂-modulated Anderson W model validated (H3, r=0.851)** | Oxygen triggers global transcription reprogramming (FNR/ArcAB/Rex) that modulates QS gene expression → Anderson disorder parameter W undergoes phase transition at oxygen boundary. **V110 Exp356 confirms:** W = 3.5·H' + 8·O₂ outperforms single-variable W (r=0.851 vs -0.575) across 10 environments. Diversity IS disorder (signal dilution), oxygen adds second dimension. Anaerobic communities show lower effective W, explaining higher QS prevalence in gut, digesters, biofilm. Testable with paired 16S/metatranscriptome data. | **Computationally validated** — Exp356 (18/18 PASS). H3 O₂-modulated model proven. Concept→lab path defined (reporter strain assays). **neuralSpring digester ML benchmark validated (S142: Paper 027)**. Faculty anchor: Wei Liao (ADREC, MSU BAE). Source: MSUBI bioreactor experience (5 years) |
| 17 | Game Design as Rigorous Science — Validated HCI Models for Interactive Systems | Game Science × HCI × Procedural Generation × GPU Compute × Cross-Spring × Provenance × Lysogeny × Economics × Niche Deployment | ludoSpring **V18: 77 experiments** (66 science + 11 composition), 222 workspace tests, 1439 checks, 9 deploy graphs, 9 proto sketches for esotericWebb. **V15-V18 composition arc**: typed deploy graph parsing, topological wave ordering, session lifecycle IPC, composition recipe pattern, 5 novel multi-primal leverage compositions (sovereign save, session-as-primal, attributed narration, live science viz, hardware dispatch). Ecosystem evolution map with per-layer gap analysis. BYOB deploy graph schema standardized. | 13 foundational HCI models validated. Game genres = interaction architectures. **Key finding: Flow state discriminates quality**. External controls prove metrics content-agnostic. **Lysogeny catalog**: 6 proprietary mechanics. **Cross-spring provenance**: same fraud detectors across gaming/science/medical (>80% similarity). **RPGPT Dialogue Plane**: NPC personality certs, internal voices, trust dynamics, plane transitions. **V37.1 live**: barraCuda tensor/stats/noise/activation all correct via UDS IPC. BearDog crypto + NestGate storage validated. 60Hz loop at 0.18ms/tick. rhizoCrypt (no UDS), loamSpine (startup panic), barraCuda (Fitts/Hick formulas) are the evolution targets. | **Validated + Primal Composition** — V18: 77 experiments, 1439 checks, 222 tests, 9 deploy graphs, 9 proto sketches. Ecosystem evolution map. Faculty anchors: Csikszentmihalyi (Flow), Fitts, Yannakakis & Togelius, Lazzaro, Hunicke, Merkle, Diffie & Hellman |
| 18 | RPGPT — Sovereign RPG Engine with Ingestible Rulesets | Game Science × Provenance × AI × Open RPG Systems | ludoSpring (13 HCI models) + rhizoCrypt (session DAG) + sweetGrass (creative attribution) + loamSpine (ruleset/character/world certs) + Squirrel (AI narration) + BearDog (anti-cheat signing). Ingestible open rulesets: Pathfinder 2e (ORC), FATE Core (CC-BY), PbtA, Cypher. | **Anti-cheat = chain-of-custody isomorphism**: same DAG operation for item lineage (extraction shooters), sample lineage (field genomics), loot lineage (tabletop RPG). Rulesets as loamSpine certificates constrain AI — no hallucination past anchored rules. Player-as-DM: sweetGrass Creation → Implementation → Extension attribution. Any world + any open ruleset = playable RPG. Provenance trio evolution goals scaffold cross-domain capability (turn-based sessions, condition decay, branch diff/merge). | **Architecture defined** — structural sketch validated, provenance trio evolution goals documented. Faculty anchors: Gygax & Arneson (1974), Cook (PF2e), Csikszentmihalyi (Flow) |
| 19 | Games@Home — Distributed Human Computation via Interactive Systems | Game Science × Combinatorics × Distributed Computing × Provenance × Cross-Domain Transfer | ludoSpring (exp048-051: stack folding, novel data combinatorics, game tree design metric, Games@Home model) + rhizoCrypt (trajectory DAG) + sweetGrass (creative attribution) + loamSpine (deck/ruleset certs). MTG Turing completeness (Churchill et al. 2019). | **Human gameplay as compute engine**: Stack resolution = protein folding (same cards, different order → different outcomes). MTG game tree is 2^ℵ₀ (uncountably infinite, proven Turing complete). Every game produces novel data (birthday bound ~10^179 vs ~10^10.5 games ever played). Game tree complexity is a design metric — Commander format rules ×216 expansion, designed-for-commander cards ×0.036 contraction. Enzymatic shortcut model: cards that "solve" parts of the space narrow exploration. Folding@Home isomorphism across 12 concepts. 7 cross-domain transfer paths (avg 76% structural similarity). AR card gaming concept for physical-anchored digital enhancement. | **Validated** — 4 experiments, 127/127 checks. Faculty anchors: Churchill, Biderman & Herrick (2019), Shannon (1950), Pande (F@H), von Ahn (2006) |
| 20 | Novel Ferment Transcript Economics — Radiating Attribution Through Provenance | Economics × Provenance × Cryptography × Cross-Domain Transfer | ludoSpring exp061_fermenting (89 checks) + rhizoCrypt (DAG history) + loamSpine (certificate lifecycle, trading protocol) + sweetGrass (object memory, PROV-O attribution) + BearDog (Ed25519 signing) + biomeOS (provenance_node_atomic deployment). sunCloud economic model. scyBorg licensing (AGPL-3.0 + ORC + CC-BY-SA 4.0). | **Memory-bound digital objects whose value derives from accumulated history, not artificial scarcity.** Novel Ferment Transcript (NFT) = loamSpine cert + rhizoCrypt DAG + sweetGrass braids + BearDog signatures + optional public chain anchor. Same architecture serves gaming (tournament sword), collectibles (trading card), science (sample chain-of-custody), and sensitive data (medical records). Public anchor activates radiating attribution: value flows backward through sweetGrass chain to every contributor. Functionally NOT a currency — no exchange rate, no gas, no mining. Trading protocol with atomic swap. Object memory with PROV-O timeline export. Composable IPC protocol for live trio deployment. Evolves sunCloud (2025) + LATENT_VALUE_ECONOMY into working code. | **Validated** — 89/89 checks (exp061). Trio modifications shipped (loamSpine trading protocol, sweetGrass object memory). Faculty anchors: Merkle (1987), Diffie & Hellman (1976), Moreau & Missier (W3C PROV-O, 2013) |
| 21 | Sovereign Sample Provenance — Field-to-Publication Chain-of-Custody | Field Genomics × Provenance × Fraud Detection × Cross-Spring | ludoSpring exp062 (39/39), exp064 (39/39), exp065 (74/74), exp066 (41/41). Provenance trio (rhizoCrypt + loamSpine + sweetGrass) + BearDog signing. ISO 17025/15189 mapping. | **Same provenance architecture that tracks game items tracks biological samples.** 6 fraud types (PhantomSample, DuplicateAccession, BrokenColdChain, UnauthorizedAccess, MislabeledSpecimen, ContaminationGap) reduce to graph analysis. DAG isomorphism with extraction shooter (exp053). Cross-domain fraud unification proves same code path detects fraud in gaming and science (>80% structural similarity). Radiating attribution gives field collectors permanent credit. Every sample is a Novel Ferment Transcript. | **Validated** — 193 checks across 4 experiments. Faculty anchors: ISO 17025 (2017), Kahn (1962), Moreau & Missier (W3C PROV-O, 2013) |
| 22 | Zero-Knowledge Medical Provenance — Patient-Owned Records with Consent Certificates | Medical Data × Provenance × Zero-Knowledge × Cross-Spring | ludoSpring exp063 (35/35), exp064 (39/39), exp065 (74/74), exp066 (41/41). Consent as loamSpine lending. BearDog zero-knowledge access proofs. HIPAA alignment. | **Patient-owned medical records via DID-based loamSpine certificates.** Consent certificates as scoped loans (record types + expiry + revocation). Every access is a DAG vertex. 5 fraud types (UnauthorizedAccess, ExpiredConsent, ScopeViolation, PhantomAccess, ConsentForgery). BearDog selective disclosure proofs. Same fraud detectors catch item duplication in games and unauthorized medical record access. Patient as Creator in radiating attribution. | **Validated** — 189 checks across 4 experiments. Faculty anchors: HIPAA Privacy Rule §164.524, HIPAA Security Rule §164.312, Diffie & Hellman (1976) |
| 25 | Self-Tuning Simulation — Physics-Validated Parameter Discovery for Lattice QCD | Lattice QCD × Adaptive Algorithms × Neuromorphic Computing × Reproducible Science | hotSpring Exp 099-103 (GPU RHMC, gradient flow, self-tuning calibrator). `rhmc_calibrator.rs`, `spectral_probe.rs`, 12 tolerance constants. | **Zero hand-tuned magic numbers in RHMC.** GPU spectral probe (power iteration λ_max, analytical m² λ_min), acceptance-driven step adaptation, consistency-monitored pole count, force/Metropolis CG tolerance split. Five parameter categories: mathematical, discovered, adapted, validated, learned (NPU pending). Constrained evolution applied to algorithm design — physics constraints as fitness landscape. Cross-spring pattern: any simulation with tunable parameters can adopt the classify→discover→adapt→validate loop. | **Phases 1-4 Complete** — spectral discovery, step adaptation, approx quality, solver calibration. NPU bridge (Phase 5) pending. Faculty anchors: Golub & Van Loan (power iteration), Kalkreuter (LQCD eigenvalues), Clark & Kennedy (RHMC) |
| 26 | Primal Composition as Scientific Methodology — From Validated Science to Sovereign Deployment | Composition Methodology × Deploy Graphs × IPC × Ecosystem Evolution | ludoSpring V15-V18 (11 experiments: exp067-077), primalSpring (NUCLEUS model, 89 deploy graphs), esotericWebb (9 proto sketch absorptions). BYOB deploy graph schema. Ecosystem evolution map. | **Springs compose FROM primals independently — no shared crates, only shared TOML schemas and patterns in wateringHole.** Typed deploy graph parsing (DeployGraph, GraphNode, topological_waves) without importing primalSpring. Composition recipe pattern: parse → validate → waves → discover → health → science → report. Session lifecycle IPC (begin/complete/state/tick_health). Session-as-primal via sourDough (ephemeral biomeOS citizens). Proto sketch taxonomy for garden absorption. Gap discovery methodology produces per-layer evolution tasks. BYOB schema as RFC (wateringHole standard, not shared crate). | **Validated** — 11 experiments (90 checks), 9 deploy graphs, 9 proto sketches, ecosystem evolution map. ludoSpring V18. Faculty anchors: primalSpring NUCLEUS model, biomeOS Neural API |

## Reading Order

**For a microbiologist**: 01 (Anderson-QS, the headline result) → 05 (cross-species) → 03 (bioag) → 06 (no-till)

**For an immunologist or pharmacologist**: 12 (immunological Anderson — cytokine propagation, Fajgenbaum bridge) → 01 (Anderson-QS foundation) → 05 (cross-species signaling) → 04 (sentinels — ESN regime classification)

**For an ecologist**: 05 (symbiotic signaling) → 02 (LTEE extensions) → 04 (sentinels) → 06 (no-till)

**For a soil scientist or agronomist**: 06 (no-till Anderson mechanism) → 03 (tree crop inoculants) → 01 (underlying physics)

**For a physicist**: 01 (Anderson applied to biology) → 06 (dynamic Anderson with time series) → the wetSpring experiment docs (Exp107-143)

**For a plasma physicist**: 07 (sovereign WDM on consumer GPU) → 10 (dynamical QCD production) → 25 (self-tuning RHMC — physics-validated parameter discovery) → 15 (precision brain, heterogeneous GPU) → 01 (Anderson framework) → the hotSpring paper queue (Tier 0–4)

**For a GPU systems researcher**: 15 (precision brain, NVVM poisoning) → 14 (`14_sovereign_compute_hardware.md` — **Apr 2, 2026:** ACR HS auth root cause (VBIOS DEVINIT), dual GPU sovereign boot, uncrashable safety arch, DMA path fully fixed; hotSpring Exp 132–141; `hotSpring/specs/SOVEREIGN_VALIDATION_MATRIX.md`) → 24 (all-silicon science) → 07 (sovereign WDM) → 10 (dynamical QCD) → 25 (self-tuning — adaptive algorithms on GPU) → 11 (nautilus shell, evolutionary reservoir)

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

**For a reservoir computing researcher**: 11 (nautilus shell — evolutionary reservoir from bingo boards) → 10 (ESN-steered dynamical QCD) → 25 (self-tuning — NPU predictions for parameter discovery) → 07 (NPU brain architecture) → 04 (sentinels, NPU edge deployment)

**For a lattice QCD practitioner**: 25 (self-tuning RHMC — eliminate hand-tuned magic numbers) → 10 (dynamical QCD production on consumer GPU) → 24 (all-silicon science — every hardware unit contributes) → 15 (precision brain — self-routing hardware discovery) → 07 (sovereign WDM — consumer GPU validation)

**For an immunologist or veterinary pharmacologist**: 12 (Anderson in immunological signaling) → 01 (underlying Anderson-QS physics) → 06 (dimensional collapse/promotion duality) → 05 (cross-species signaling)

**For a drug repurposing researcher**: 12 §3 (Fajgenbaum bridge — geometry-aware scoring) → 12 §2 (Anderson mapping) → 01 (framework) → 04 (sentinels as diagnostic analog)

**For an ecosystem architect or DevOps researcher**: 26 (primal composition methodology — deploy graphs, BYOB schema, gap discovery) → 23 (primal coordination — NUCLEUS atomics, biomeOS substrate) → 17 (game design as science — the domain that drove composition) → 18-22 (cross-domain provenance proving the composition pattern is universal)

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

- **wetSpring**: Anderson QS, 16S pipeline, DADA2, taxonomy, NPU live, field genomics architecture, bio brain (5,707+ checks, 379 experiments, **1,891** tests, **355** binaries (333 barracuda + 22 forge), 49 CPU + 44 GPU bio modules, **V136**, standalone `barraCuda` **v0.3.7** (wgpu 28, Fp64Strategy), 150+ primitives consumed, 234 named tolerances, zero local WGSL, zero TODO/FIXME/HACK, `forbid(unsafe_code)` at workspace level + per-crate, clippy pedantic+nursery ZERO WARNINGS, **zero `#[allow()]` in entire codebase** — all `#[expect(reason)]` with self-documenting justifications. **91.20%** line coverage (gated at 90%). **V136:** deep debt resolution — thiserror (6 types), named cast helpers, upstream contract pinning, bitwise determinism tests, CI pin, provenance headers (5 validators), hardcoding audit, ipc/server.rs refactored, CONTRIBUTING + SECURITY. **V135:** doc reconciliation, canonical metrics, V135 handoff. **V134:** deep audit — drug NMF delegation, validation harness refactored, primal discovery extended (7 primals), SPDX, CI feature-matrix. **V133:** `validate_all`, `GpuContext`/`TensorSession`, `performance_surface`, zero-copy I/O, IPC modules. **V132:** workspace `lints.workspace`, `DeviceCapabilities`, `ValidationSink`, `PROVENANCE_REGISTRY`. 64 papers reproduced.)
- **neuralSpring**: ML primitives (LSTM, HMM, transfer learning, spectral analysis,
  ESN reservoir computing), **27 papers** (full queue complete) + 5 WDM surrogates +
  5 novel compositions + 4 GPU experiments + playGround (Squirrel MCP + HuggingFace
  Model Lab + compute triangle + typed BiomeOsClient), validated at 4,500+ checks,
  ~1,385 tests, 267 binaries. 92% line coverage. 225 named tolerances. 25 absorbed
  workloads, 1 local remaining. 0 clippy (pedantic+nursery, all-features), 0 doc
  warnings, 0 unsafe (forbid on all crate roots). barraCuda v0.3.7, toadStool S146+,
  coralReef Phase 10. **S173**: `thiserror` typed errors, module decompositions (nucleus_pipeline, glucose_prediction, immunological_anderson), cargo-deny CI, IPC smoke test, barraCuda explicit features, coral forge shader absorption plan.
  **S163**: Edition 2024, health probes (health.liveness/health.readiness), ipc_resilience (RetryPolicy + CircuitBreaker), 6 proptest invariants, deny.toml hardened, V114 handoff.
  **S162**: Cross-ecosystem absorption — 4-format parse_capabilities, discover_primal, DispatchOutcome, resilient_call circuit breaker, safe_cast module, zero eprintln workspace-wide.
  **S161**: Doc cleanup + logging — zero eprintln in playGround, zero hardcoded paths, doc consolidation + V112 handoff.
  **S160**: Structured `IpcError`, `call_typed()`, typed `compute.dispatch` protocol.
  **S157–S159**: OrExit<T>, deny.toml, structured logging, zero C deps, `#[expect(reason)]`.
  Cross-spring provenance mapped: hotSpring precision → wetSpring bio → neuralSpring
  domain → barraCuda fused ops → all Springs
- **hotSpring**: MD simulation, nuclear EOS, lattice QCD, transport, 4-layer brain architecture, **self-routing precision brain** (848 tests, 115 binaries, 85 WGSL shaders, 0 clippy warnings, 0 files >1000 lines). **25 papers** (Papers 43-45: Chuna gradient flow integrators, conservative dielectric functions, kinetic-fluid coupling — **44/44 overnight checks pass**). coralReef sovereign pipeline: **46/46** standalone shaders compile to native SM70/SM86 SASS. Full `GpuBackend` impl. **Exp 049**: Precision brain + NVVM device poisoning discovery. Dual-GPU cooperative patterns (Split BCS 2.2×, PCIe 1.2 GB/s). Kokkos parity: 12.4× gap persists — primary blocker is NVVM-safe DF64 exp. **Exp 074**: Ember hardened — VRAM write-readback canary, BDF allowlist, pre-flight device checks, display GPU safety guard. 86 ember + 178 glowplug tests. Both Titans warm-swapped, HBM2 alive. v0.6.32, barraCuda v0.3.7, toadStool S158, coralReef ce66de4.
- **airSpring**: FAO-56 ET₀ (8 methods), Priestley-Taylor, Thornthwaite, GDD, Saxton-Rawls
  pedotransfer, water balance, Richards PDE, isotherms, yield response, scheduling, lysimeter,
  sensitivity, SCS-CN runoff, Green-Ampt infiltration, Anderson coupling, diversity indices,
  100-station Michigan Crop Water Atlas, NUCLEUS primal (41 capabilities), metalForge dispatch,
  AirSpringBrain (Nautilus evolutionary reservoir: ET₀/soil/crop heads), MonitoredAtlasStream
  (DriftMonitor regime change detection), Paper 12 immunological Anderson (tissue diversity +
  CytokineBrain + barrier state + cross-species), 6 local WGSL compute shaders
  (`local_elementwise_f64.wgsl`: SCS-CN, Stewart yield, Makkink, Turc, Hamon, Blaney-Criddle)
  via `gpu::local_dispatch::LocalElementwise` (f64 canonical, compile_shader_universal).
  **v0.10.0 (March 24, 2026)**: Standalone barraCuda **0.3.7** (wgpu 28); **`default-features = false`** (gpu + domain-pde only). **1,237** Python checks **;** **943** lib + **316** integration/doc + **62** forge = **1,321** Rust tests (**1,259** barracuda crate). **91** binaries, **87** experiments, **58** named tolerances, **45** capabilities.
  25 Tier A + 6 GPU-local (3/6 absorbed upstream: Makkink, Turc, Hamon),
  fused Welford mean-variance + fused Pearson correlation wired from upstream,
  DF64 precision tier documented, Fp64Strategy::Concurrent for cross-validation.
  20.6× CPU speedup (24/24 parity). 146/146 cross-spring evolution, 34 ShaderProvenance entries.
  27 GPU tests fail upstream (wgpu 28 + NVK/Titan V), CPU fallback in SeasonalReducer.
  Zero clippy pedantic+nursery warnings, cargo-deny clean.
- **groundSpring**: Uncertainty quantification, noise labels, spectral theory (Anderson, Almost-Mathieu, band edge), transport, quasispecies, rare biosphere, jackknife, freeze-out, spectral recon, WDM precision/convergence/vendor-parity, NPU Anderson regime classification, mixed-hardware pipeline dispatch (`PCIe` topology, NUCLEUS atomics, fallback chains) (34 experiments, 395/395 Rust checks + 187 metalForge checks, 10 domains, 876+ workspace tests; live hardware: RTX 4070, Titan V, AKD1000 NPU; 2.2× GPU speedup). V107: 39 modules, 906 tests, AGPL-3.0-only, enriched `niche.rs` (`OperationDeps` + `CostEstimate` const fns for biomeOS scheduling), tolerance provenance citations (13 `tol::` constants with mathematical derivation + source citations + validation binary refs), typed `BiomeOsError` enum (7 variants), `primal_names.rs` centralized constants, release profile (`lto + codegen-units=1 + strip`), zero bare numeric literals in production (~15 named constants extracted), typed tarpc IPC client, panic-free production, 14 proptest, 102 delegations (61 CPU + 41 GPU). barraCuda v0.3.5, zero hardcoded primal strings, 13-tier named tolerance architecture, biomeOS Neural API + NestGate data pipelines (NCBI, NOAA, IRIS). All files < 1000 lines, zero unsafe, zero production mocks, zero `unwrap()` in production, zero TODO/FIXME in Rust source

Every experiment can be reproduced with the corresponding Spring's binaries:

```bash
# wetSpring experiments (Anderson QS, 16S, metagenomics)
cd wetSpring/barracuda && cargo run --release --features gpu --bin <binary_name>

# neuralSpring experiments (ML, spectral, surrogates)
cd neuralSpring && cargo run --release --bin neuralspring

# hotSpring experiments (MD, nuclear EOS, lattice QCD)
cd hotSpring && cargo run --release --features gpu --bin <binary_name>
```

No proprietary data. No restricted access. No institutional dependencies.

## Cross-Spring Provenance (standalone barraCuda v0.3.7 at `03986ce`)

**Validated March 11, 2026** — all springs rewired to standalone `barraCuda`:

```
┌─ hotSpring v0.6.32 ─ spectral (Anderson, Lanczos, level statistics), 4-layer brain, precision brain, coralReef sovereign compile 46/46, Kokkos parity (12.4× gap, DF64 exp blocker), **Ember hardened** (Exp 074: VRAM write-readback, BDF allowlist, preflight checks, display GPU guard, 264 coral tests, coralReef ce66de4)
├─ neuralSpring S173 ─ 27/27 papers + 5 compositions + playGround (Squirrel MCP, Model Lab, compute triangle). Edition 2024, health probes, ipc_resilience, typed errors + cargo-deny + IPC smoke test, ~1,385 total tests, 67 modules, 225 named tolerances, zero eprintln workspace-wide, zero hardcoded paths, V117 handoff
├─ wetSpring V137 ──── 379 experiments, 5,707+ checks, **1,902** tests, **355** binaries (all with `//! Provenance:` headers), standalone barraCuda **v0.3.7**, 91.20% coverage (gated at 90%), `forbid(unsafe_code)` workspace-level, **242** named tolerances (zero inline literals), `ipc/connection.rs` extraction, thiserror (6 types), named cast helpers, bitwise determinism, upstream contract pinning, 7-primal discovery, all `#[expect(reason)]`, CONTRIBUTING + SECURITY
├─ groundSpring V123 ── 41 modules, 1020+ tests, ≥92% library coverage, cross-ecosystem absorption + provenance (SECURITY.md, rustfmt.toml, 6 upstream contract tolerance pins, provenance_registry.rs, CastOverflowError, 5 bitwise determinism tests), V122: cast evolution + module extraction, V121: deep debt, 110 delegations (67 CPU + 43 GPU), barraCuda v0.3.7, zero clippy (pedantic+nursery), zero unsafe, zero TODO/FIXME, zero unwrap/expect in production
├─ airSpring v0.10.0 ── 87 experiments (1,284 Python ; 986 lib + 316 integration + 62 forge = 1,364 Rust tests, 1,302 barracuda crate), 91 validation binaries, 58 named tolerances, 45 capabilities, 4 deploy graphs (with [graph.metadata]), barraCuda 0.3.7 (wgpu 28, default-features=false gpu+domain-pde), 25 Tier A GPU modules (20 ops upstream), platform-agnostic IPC (Transport: Unix + TCP), provenance trio fully migrated, CONTRIBUTING/SECURITY (neuralSpring S174 pattern), upstream contract pinning (5 tolerance invariant tests), GPU test resilience (test_pool delegation), zero `#[allow()]`, zero unsafe, zero C deps, zero hardcoded primals, 14.3× CPU speedup, 21/21 CPU-GPU parity, `#![forbid(unsafe_code)]`, `#![deny(cast_*)]`, clippy pedantic+nursery zero warnings, 90.56% llvm-cov (fail-under-lines 90), cargo-deny 0.19 clean (ecoBin enforcement, barracuda + forge), CI symlink path deps, MSRV 1.92 documented
├─ healthSpring V44 ── 928 tests, 83 experiments, 54 Python baselines, barraCuda v0.3.7 (6 GPU ops). 9 tracks complete: PK/PD (Hill, PBPK, population PK, MM, NLME FOCE+SAEM, NCA), Microbiome (Anderson gut, FMT, SCFA, serotonin), Biosignal (Pan-Tompkins, HRV, EDA, arrhythmia, SpO2, WFDB), Endocrine (TRT, testosterone-gut axis), Comparative Medicine (canine AD, feline hyperthyroid, cross-species PK), Drug Discovery (MATRIX, ADDRC HTS, compound library, fibrosis), Toxicology (Anderson delocalization, hormesis, mithridatism), Simulation (multi-scale causal chain). 6 WGSL shaders (absorbed), 59 JSON-RPC (46 science + 13 infra), `primal_names` module, `gpu/mod.rs` smart-refactored (696→413), toadStool 51 tests, WFDB 11 annotation tests, tolerance migration (8 experiments). Zero clippy (pedantic+nursery), zero unsafe, zero `#[allow]`
├─ ludoSpring V30 ──── 13 HCI models (Fitts, Hick, Steering, GOMS, Flow, DDA, Four Keys, Engagement, Perlin, WFC, L-systems, BSP, Tufte), 75 experiments, 1692 checks, 394+12+6 tests, ≥90% coverage, 0 clippy warnings (pedantic+nursery), 0 `#[allow()]`, 0 magic numbers, 0 production panics, `#![forbid(unsafe_code)]`, 24 IPC capabilities, toadStool direct dispatch (`compute.dispatch.*`), dual-format discovery, Python tolerance mirror (46 constants), Write→Absorb→Lean documented, session decomposition, typed `TransitionIssue` enum, pluggable `ValidationSink`, NeuralBridge typed IPC, RPGPT dialogue plane (9 experiments), ecosystem absorption V22
├─ wateringHole V69 ── Boltzmann sampling (Metropolis-Hastings MCMC)
├─ primalSpring v0.9.4 ─ 72 experiments, 15 tracks, 404 tests, **BTSP + INFERENCE + PROTO-NUCLEATE (87/87 gates)** — Tower 41/41 + Nest 8/8 + Node 5/5 + NUCLEUS 4/4 + Graph Overlays 14/14 + Squirrel Discovery 5/5 + Graph Execution 6/6 + Provenance Readiness 4/4. **Phase 28**: BTSP Phase 2 cascade (11/13 primals), inference wire standard (`inference.complete`/`embed`/`models`), WGSL shader composition model (same barraCuda shaders compose into ML/QCD/biology — Paper 23 mass-energy-information equivalence realized), 5 proto-nucleate graphs (neuralSpring ML, hotSpring QCD, healthSpring enclave), 3 pipeline graphs, 107 deploy graphs with `secure_by_default` metadata, zero clippy, zero unsafe, zero C deps
├─ bingoCube/nautilus ─ NautilusBrain → BioNautilusBrain (concept edge, drift)
└─ multi-spring ────── special functions, bootstrap, correlation
```

All 826+ `barraCuda` WGSL shaders are f64-canonical with f16/f32/f64/Df64
precision dispatch per hardware. `barraCuda` is the standalone math primal
(WHAT to compute); `toadStool` handles hardware dispatch (WHERE and HOW);
`coralReef` compiles WGSL programs into domain-specific compositions.
Springs depend on `barraCuda` directly for math. Cross-spring evolution is
bidirectional: each spring's innovations flow through `barraCuda` and benefit
all springs.

**WGSL Shader Composition (April 10, 2026)**: Paper 23's mass-energy-information
equivalence is now realized in code: the same barraCuda WGSL shaders compose
into ML inference (neuralSpring: matmul + attention + FFT), QCD physics
(hotSpring: df64 Wilson-Dirac + plaquette), and biology (wetSpring: diversity +
Anderson spectral). Springs are application layers composing barraCuda/coralReef/
toadStool — not standalone compute engines. Proto-nucleate graphs in
`primalSpring/graphs/downstream/` define these target compositions.

### Cross-spring evolution status

**wetSpring V137** is the current ecosystem anchor for barraCuda **v0.3.7** migration, **`DeviceCapabilities`**-aligned device discovery, pluggable **`ValidationSink`**, **`PROVENANCE_REGISTRY`**, workspace-level **`forbid(unsafe_code)`**, validation harness decomposition (6 domain submodules), 7-primal runtime discovery, and IPC **normalization** against standalone barraCuda method naming. **V137** completes provenance discipline: `//! Provenance:` headers on all 355 binaries (first spring at 100%), 8 new tolerance constants (242 total, zero inline literals), and `ipc/connection.rs` extraction (protocol pipeline separated from server lifecycle). The **8-axis audit methodology** (completion, quality, fidelity, dependency health, GPU readiness, coverage, ecosystem standards, primal coordination) is reusable across springs.

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
 ludoSpring V30 (13 HCI models,
   75 experiments, 1692 checks,
   4 cross-spring: NCBI, NUCLEUS,
   Anderson QS explorer,
   toadStool direct dispatch,
   dual-format discovery,
   Python tolerance mirror)
 barraCuda (sigmoid, dot,
   lcg_step primitives)
 toadStool (GPU dispatch +
   compute.dispatch.* direct)
 metalForge (cross-substrate)
 petalTongue (live dashboards)
 wetSpring (Anderson W model,
   QS propagation, disorder,
   Python tolerance pattern)
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

Paper 23 (Primal Coordination)
  primalSpring v0.9.3 (72 experiments,
   15 tracks. Phase 26: MIXED COMPOSITION +
   LIVE VALIDATION MATRIX — 87/87 gates,
   404 tests, 99 deploy graphs. Particle model
   (Tower=electron, Node=proton, Nest=neutron,
   NUCLEUS=atom, Paper 23 grounded). Layered
   validation L0-L3. 17 sketch graphs, exp091-093.
   Live Tower Atomic probes on Eastgate (BearDog
   crypto + Songbird HTTPS LIVE PASS). 6 GAP-MATRIX
   items (Critical: Neural API capability registration).
   100% provenance, zero unsafe, zero C deps)
 biomeOS (primary test subject:
   all 5 coordination patterns)
 All NUCLEUS primals (deploy +
   health + capability discovery)
 nestgate (storage store/retrieve,
   model cache, filesystem fallback)
 toadstool (compute health, caps,
   4 workload types, 24 CPU cores)
 Provenance Trio (RootPulse
   end-to-end validation)
 coralForge (neural object
   Pipeline graph validation)
```

**What each spring contributes:**

| Spring | Contributes To | Key Primitives |
|--------|---------------|----------------|
| wetSpring | 01, 03, 04, 05, 06 | Anderson QS, diversity, Bray-Curtis, FASTA, NCBI, NPU int8 |
| hotSpring | 01, 07 | Spectral theory (Lanczos, Anderson 3D), GPU MD, lattice QCD |
| airSpring | 03, 06, **08**, **12**, **16** | FAO-56 ET₀, soil moisture, Richards PDE, **NPU int8 eco classifiers, IoT sensor pipeline**, GpuDiversity (tissue W), CytokineBrain (AD flare prediction), barrier state (VG analogue), cross-species Anderson, **MC ET₀ uncertainty, Bootstrap/Jackknife CI, SPI drought index**, **soil O₂ zonation (aerobic/anaerobic QS boundary)** |
| neuralSpring | 01, 02, 04, 05, 06, 07, **13**, **16** | ESN/LSTM anomaly detection, WDM surrogates, HMM, transfer learning, **digester ML prediction (Paper 027: ESN methane yield, bC/gT validated)** |
| groundSpring | **01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13** | Spectral theory validation (Anderson, Almost-Mathieu, band edge, transport), uncertainty budgets, sensor noise calibration, rare biosphere, jackknife error bars, freeze-out inverse, spectral recon, drift vs selection, quasispecies threshold, WDM precision/convergence/vendor-parity, **NPU Anderson regime classification (AKD1000)**, metalForge cross-substrate validation, **immunological Anderson mapping (Exp 008/012/015/018 → cytokine propagation)** |
| **healthSpring** | **13**, **16** | **Hill, PBPK 5-tissue, population PK Monte Carlo, Michaelis-Menten nonlinear PK, Anderson gut lattice, FMT engraftment, antibiotic perturbation, SCFA production, gut-brain serotonin, Pan-Tompkins QRS, HRV/PPG SpO2/EDA stress/arrhythmia classification, WFDB, testosterone PK, TRT outcomes, testosterone-gut axis, NLME (FOCE+SAEM — sovereign NONMEM/Monolix), NCA (sovereign WinNonlin), 6 WGSL compute shaders, GPU dispatch + metalForge routing + toadStool streaming (51 tests), petalTongue pipeline (28 nodes, 121 channels, 14 scenarios), gut as anaerobic QS system. V44: `primal_names` centralized, `gpu/mod.rs` smart-refactored (696→413), provenance registry accessors, tolerance migration (8 experiments), 928 tests** |
| **ludoSpring** | **17, 18, 19, 20, 21, 22** | **Fitts's law, Hick's law, Steering law, GOMS, Flow theory, DDA, Four Keys to Fun, Engagement metrics, Perlin noise, WFC, L-systems, BSP trees, Tufte data-ink. 75 experiments, 1692 checks, 394+12+6 tests, ≥90% coverage. Playable prototypes (Doom terminal, roguelike), game telemetry protocol (NDJSON), 3 external game adapters (Veloren, Fish Folk, A/B Street), external control groups. GPU dispatch (Tier A WGSL) + metalForge capability routing + NUCLEUS atomics + petalTongue live dashboards. Lysogeny catalog (6 proprietary mechanics). Cross-spring provenance (>80% similarity). RPGPT + 9 dialogue plane experiments, Games@Home, Novel Ferment Transcript. V22 ecosystem absorption: toadStool direct dispatch, dual-format discovery, Python tolerance mirror, Write→Absorb→Lean documented, session decomposition, typed transition verification, pluggable validation, `#![forbid(unsafe_code)]`** |

| **primalSpring** | **23** | **Coordination and composition validation: 53 experiments, 10 tracks (Atomic Composition, Graph Execution, Emergent Systems, Bonding & Plasmodium, coralForge Redefinition, Cross-Spring Coordination, Showcase-Mined Patterns, Live Composition, Multi-Node Bonding, Cross-Gate Deployment). biomeOS is primary test subject. 364 tests. Phase 16: DEEP DEBT AUDIT + CENTRALIZED TOLERANCES (87/87 gates: Tower 41/41 + Nest 8/8 + Node 5/5 + NUCLEUS 4/4 + Graph Overlays 14/14 + Squirrel Discovery 5/5 + Graph Execution 6/6 + Provenance Readiness 4/4). Centralized tolerances (trio resilience + remote TCP ports), deduplicated capability parsing (4-format), hardcoding→capability-based evolution in experiments and tests. Builder `.run()` on all 53 experiments, 100% provenance, zero `.unwrap()`/`#[allow()]`. 22 deploy graphs (18 single-node + 4 multi-node), all nodes `by_capability`. 17 RPC endpoints, 37 capabilities. 22 proptest fuzz tests total. MCP tools (8 typed for Squirrel AI), 5-tier discovery + Neural API, deny.toml hardened, zero clippy warnings (all-targets), zero unsafe (workspace forbid), zero C deps, zero missing docs. v0.7.0 Phase 16.** |

groundSpring V123 now contributes to ALL 10 active baseCamp papers (01-09, 12) —
reflecting the expansion from 5 experiments (sensor noise only) to 35 experiments
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
| 13 | NLME GPU shaders (FOCE per-subject gradient, VPC Monte Carlo). NLME at scale (10K+ subjects). Multi-drug NLME for combination therapy. Population PK on GPU (100K patients). coralReef f64 lowering to replace f32 workarounds. QS gene profiling → effective disorder parameter. Real 16S data via NestGate. biomeOS NUCLEUS local integration. EDA SIMD optimization (numpy C convolution currently faster). TensorSession integration when dependent multi-op chains needed. | **healthSpring** (83 experiments, V44, 928 tests, 6 WGSL shaders, `primal_names` centralized, `gpu/mod.rs` smart-refactored, 51 toadStool tests, full-stack portability) × **barraCuda** (canonical ops — Hill, PopPK, diversity, MM batch, SCFA batch, beat classify) × **toadStool** (pipeline dispatch, streaming StageOp, V16 dispatch validated) × **metalForge** (cross-system routing, 9 Workload variants, NUCLEUS dispatch with P2P bypass) × **coralReef** (f64 transcendental lowering) × **petalTongue** (28-node pipeline, 121 channels) × **wetSpring** (diversity → gut health, QS genes) × **groundSpring** (uncertainty budgets) × **biomeOS** (NUCLEUS local, NestGate data) |
| 16 | ~~Reproduce Wang 2020 ML digester prediction~~ **(DONE — Paper 027, S142)**. Apply 16S pipeline to public anaerobic digester datasets (NCBI BioProjects: ADREC, municipal WWTPs). Map FNR/ArcAB/Rex-regulated QS genes via NCBI Protein. Model oxygen-dependent Anderson W. Test gut mucosal O₂ gradient → spatial W prediction. Extend ESN digester model to real operational data. | **wetSpring** (Anderson-QS, 16S, diversity) × **healthSpring** (Anderson gut lattice, anaerobic gut) × **airSpring** (soil O₂ zonation, Paper 06) × **neuralSpring** (ESN/LSTM time series, **Paper 027 digester benchmark COMPLETE**) × **groundSpring** (spectral W modeling, uncertainty) |
| 17 | ~~Anderson QS interactive explorer~~ **(DONE)**. ~~NCBI QS gene data~~ **(DONE)**. ~~Tower Atomic boot~~ **(DONE)**. ~~Deep audit~~ **(DONE — V14, V17 deep evolution)**. ~~GPU dispatch buildout~~ **(DONE — V15)**. ~~Niche deployment~~ **(DONE — V16)**. ~~Code quality evolution~~ **(DONE — V17)**. ~~Niche self-knowledge~~ **(DONE — V18)**. ~~RPGPT dialogue plane~~ **(DONE — V18-V19: 9 experiments, 321 checks)**. ~~Deep primal integration~~ **(DONE — V20: 24 IPC capabilities, typed provenance)**. ~~Deep debt evolution~~ **(DONE — V21: session decomposition, typed transitions, pluggable validation)**. ~~Ecosystem absorption~~ **(DONE — V22: toadStool dispatch, dual-format discovery, Python tolerances)**. Live biomeOS Continuous mode for 60 Hz game engine. Engagement metrics for patient compliance (healthSpring). Fitts/Hick for medical UI evaluation. Real game telemetry from Veloren/Fish Folk sessions. Perlin 3D/fBm 3D absorption into barraCuda core (2D absorbed, 3D pending). | **ludoSpring** (75 experiments, 1692 checks, 394+12+6 tests, V22 ecosystem absorption) × **barraCuda** (sigmoid, dot, lcg_step consumed; Perlin 2D absorbed, 3D pending; 12 proptest invariants ready for upstream) × **toadStool** (11 WGSL shaders + `compute.dispatch.*` direct dispatch wired) × **metalForge** (capability routing validated) × **petalTongue** (live dashboards + gaming niche graph, VisualizationPushClient capability discovery) × **biomeOS** (deploy graphs + niche YAML ready) × **healthSpring** (Fitts/Hick for medical UI) × **wetSpring** (Anderson QS, diversity dominates O₂, Python tolerance pattern) × **nestgate** (NCBI E-utilities) |
| 18 | Ruleset-as-certificate format (PF2e, FATE, Cypher → loamSpine certs). Turn-based session DAG (rhizoCrypt action economy, condition decay, phase transitions). AI narration loop (Squirrel constrained by ruleset cert + ludoSpring quality metrics). Multi-agent creative attribution (sweetGrass player/AI/NPC derivation chains). NPC personality certs with knowledge bounds. World lore certs with canonicity levels. Branch diff/merge for "what if?" exploration. | **ludoSpring** (13 HCI models, Flow/DDA/engagement for session quality) × **rhizoCrypt** (session DAG, turn-based mode, condition tracking) × **loamSpine** (ruleset certs, character sheet certs, NPC templates, world lore) × **sweetGrass** (creative attribution, FATE Aspects as semantic entities) × **Squirrel** (AI narration constrained by anchored rules) × **BearDog** (anti-cheat action signing) × **biomeOS** (orchestration) |
| 19 | Open data source integration for visualization (Scryfall CC0 card data, EDHREC synergy rates, tournament meta snapshots). AR hardware prototype (glasses/projection for counter/token/stack management). Trajectory aggregation pipeline (session DAGs → strategic landscape models). Cross-domain transfer validation (game patterns applied to protein folding / drug discovery / materials science). Commander enzymatic card audit (measure branching effect of real card sets). | **ludoSpring** (exp048-051 validated, 127/127 checks) × **rhizoCrypt** (trajectory DAG capture at decision-point granularity) × **sweetGrass** (per-decision attribution, cross-domain transfer records) × **loamSpine** (deck-as-certificate, physical card provenance) × **barracuda** (combinatoric analysis, validation math) × **biomeOS** (AR device orchestration, remote pod play) |
| 20 | BearDog signing integration (every operation: vertex, cert, braid). Public chain anchor entry type in loamSpine. Owner inventory query (`list_by_owner`). Cross-session derivation links in rhizoCrypt. License-aware attribution notices (scyBorg). Radiating attribution calculator (sunCloud Phase 4). Physical-digital bridge (NFC/QR → certificate). Marketplace protocol as biomeOS graph. | **ludoSpring** (exp061 validated, 89/89 checks) × **loamSpine** (trading protocol DONE, anchor entry type needed) × **rhizoCrypt** (DAG history DONE, cross-session links needed) × **sweetGrass** (object memory DONE, license-aware notices needed) × **BearDog** (signing RPC needed) × **biomeOS** (provenance_node_atomic DONE, marketplace graph needed) × **sunCloud** (radiating attribution calculator — long-term) |
| 21 | wetSpring adoption (adapt SampleType/ProcessingStep to field genomics pipeline). Real BearDog signing (replace model signatures with live IPC). Public chain anchor for regulatory proof. Cross-institution provenance (songbird discovery for multi-lab chains). ISO 17025 compliance matrix (formal requirement → trio operation mapping). | **ludoSpring** (exp062/064/065/066 validated, 193 checks) × **wetSpring** (field genomics pipeline: sub_thesis_06) × **BearDog** (live Ed25519 signing RPC) × **biomeOS** (multi-lab deployment graph) × **songbird** (cross-institution discovery) |
| 22 | healthSpring adoption (adapt RecordType to clinical tracks). Full ZK proofs (BearDog ZK circuit for true zero-knowledge verification). FHIR/HL7 interop (loamSpine certificates → FHIR resources). Cross-institution consent (songbird for multi-provider chains). Patient portal (petalTongue consent visualization). Clinical trial consent certificates. | **ludoSpring** (exp063/064/065/066 validated, 189 checks) × **healthSpring** (clinical tracks: PK/PD, microbiome, biosignal, TRT) × **BearDog** (ZK circuit for access proofs) × **petalTongue** (patient consent portal) × **songbird** (cross-provider discovery) |

| 23 | ~~Crate rename~~ **(DONE)**. ~~IPC module~~ **(DONE)**. ~~Real discover_primal()~~ **(DONE)**. ~~CheckOutcome + check_skip~~ **(DONE)**. ~~Tolerance provenance~~ **(DONE)**. ~~Zero clippy warnings~~ **(DONE)**. ~~genomeBin pinned~~ **(DONE)**. ~~IPC resilience stack~~ **(DONE v0.2.0)**. ~~4-format capability parsing~~ **(DONE v0.2.0)**. ~~health.liveness/readiness~~ **(DONE v0.2.0)**. ~~proptest IPC fuzzing~~ **(DONE v0.2.0, expanded v0.3.0 — 15)**. ~~Graph format unified~~ **(DONE v0.9.2)**. ~~Capability names canonical~~ **(DONE v0.9.2)**. ~~http_health_probe deprecated~~ **(DONE v0.9.2)**. ~~Tower Atomic HTTPS validated~~ **(DONE v0.9.2)**. ~~Covalent bonding modernized~~ **(DONE v0.9.2)**. ~~NA-009/NA-016 resolved~~ **(DONE v0.9.2)**. ~~Particle model adopted~~ **(DONE v0.9.3)**. ~~Layered validation L0-L3~~ **(DONE v0.9.3)**. ~~Live Tower Atomic probes~~ **(DONE v0.9.3)**. ~~6 GAP-MATRIX items documented~~ **(DONE v0.9.3)**. ~~BTSP Phase 2 cascade~~ **(DONE v0.9.4 — 11/13 primals, all 107 graphs secure_by_default)**. ~~Inference wire standard~~ **(DONE v0.9.4 — inference.complete/embed/models, Squirrel bridge)**. ~~WGSL shader composition model~~ **(DONE v0.9.4 — same barraCuda shaders compose into ML/QCD/biology)**. ~~Proto-nucleate graphs~~ **(DONE v0.9.4 — neuralSpring ML, hotSpring QCD, healthSpring enclave)**. RootPulse end-to-end (awaiting live trio). coralForge Pipeline graph. Live multi-node validation. Bonding live coordination. Anchoring + Economics (BTC/ETH attestation). BYOB primal DAG execution. GAP-MATRIX-01 resolution (biomeOS team). | **primalSpring** (72 experiments, 15 tracks, v0.9.4 Phase 28 BTSP + INFERENCE + NUCLEATION 87/87, 404 tests, 107 graphs) x **biomeOS** (primary test subject, GAP-MATRIX-01 owner) x **all NUCLEUS primals** x **nestgate** (storage + federation) x **toadstool** (compute + idle) x **Squirrel** (cross-primal AI + inference bridge) x **Provenance Trio** (Neural API wired) x **Songbird** (mesh + STUN + TLS 1.3) x **BearDog** (lineage trust, LIVE PASS, BTSP authority) x **6 science springs** (nucleated deploy + proto-nucleate graphs) |
| 26 | ~~Typed deploy graph parsing~~ **(DONE V15)**. ~~Topological wave ordering~~ **(DONE V15)**. ~~Session lifecycle IPC~~ **(DONE V15)**. ~~Composition recipe pattern~~ **(DONE V16)**. ~~Primal leverage map~~ **(DONE V17)**. ~~Proto sketch taxonomy~~ **(DONE V18)**. ~~BYOB deploy graph schema~~ **(DONE V18)**. ~~Ecosystem evolution map~~ **(DONE V18)**. Other springs adopt composition methodology. biomeOS absorbs BYOB `[[graph.node]]` ingestion. Gardens validate proto sketch absorption. Cross-spring gap discovery replication. | **ludoSpring** (V15-V18: 11 composition experiments, 9 deploy graphs, 9 proto sketches) x **primalSpring** (NUCLEUS model, 89 deploy graphs, proto sketch source) x **esotericWebb** (garden absorption target) x **biomeOS** (BYOB ingestion evolution) x **all sibling springs** (composition methodology adoption) |

## gen4 Cross-Pollination: Esoteric Webb

**esotericWebb V4** (March 24, 2026) is the first gen4 consumer — a CRPG
substrate that composes deployed primals into a playable game system. It
directly exercises the infrastructure that baseCamp papers 17–22 describe:

- **Paper 17 (Game Science)**: ludoSpring's 13 HCI models are wired live
  into Webb's `GameSession::act()`. Flow evaluation, engagement, and DDA
  run per-action when the game science primal is connected.
- **Paper 18 (RPGPT)**: Webb's `GameDirector` + `NarrativeGraph` + provenance
  trio implement the RPGPT engine architecture. NPC personality certs,
  AI-constrained narration (Squirrel), DAG-traced sessions (rhizoCrypt).
- **Paper 19 (Games@Home)**: Webb's bounded-space-infinite-exploration thesis
  validates that game tree complexity is a design metric — authored topology
  × combinatorial state space.
- **Paper 20 (Novel Ferment Transcripts)**: Webb's provenance lifecycle
  (`dag.session.create` → `dag.event.append` → `dag.session.complete`) is
  exactly the NFT lifecycle: every playthrough is a Novel Ferment Transcript.
- **Paper 21 (Sample Provenance)**: Same `PrimalBridge` → rhizoCrypt DAG
  operations that track game actions can track biological sample custody.
  Cross-domain fraud unification proven at >80% structural similarity.
- **Paper 22 (Medical Provenance)**: Consent-as-certificate pattern maps
  to Webb's NPC personality certs (scoped knowledge, trust gates, lies).

Webb's architecture: 166 tests, 32 Rust files (~8.5k LOC), 23 bridge methods
across 8 primal domains, all with graceful degradation. Zero unsafe, zero C
deps, zero spring imports. JSON-RPC IPC over TCP/UDS. Deploy graphs for
primal spawning (topological wave ordering). sporeGarden org on GitHub.

This is the gen3→gen4 boundary: the primals disappear into the product.

### helixVision (planned — sporeGarden)

The second gen4 product pattern: **helixVision** composes wetSpring genomics
(16S pipeline, microbiome analytics, PFAS screening) and neuralSpring/coralForge
(AlphaFold structure prediction) into a sovereign genomics discovery platform.
Same PrimalBridge, same deploy graphs, different domain. coralForge becomes
helixVision's structure prediction module; the gen3 science doesn't rename.

### primalSpring gen4 Bridge (Phase 17)

primalSpring Phase 17 wires the gen3→gen4 bridge. esotericWebb deploy graphs
declare `primalspring_primal` as a post-deploy validator with 6
`composition.webb_*_health` capabilities. The `GEN4_COMPOSITION_AUDIT.md`
identifies 7 shortcomings between what primalSpring validates (gen3) and what
gen4 products need. Key: composition health namespace mismatch, transport
priority inversion (UDS-first vs TCP-first), capability string drift across
4 surfaces, session pipeline ordering, resilience semantics.

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
  AKD1000 + BarraCuda for autonomous environmental sentinels. Experiments
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
  signal to classified community state: MinION → BarraCuda 16S → AKD1000
  NPU classification → adaptive sampling feedback. Target deployments:
  Great Lakes HAB monitoring (Saginaw Bay / Lake Erie), soil health
  sentinel for no-till monitoring, AMR wastewater surveillance, PFAS
  dual-mode detection. NPU-driven adaptive sampling provides 37x headroom
  over MinION read generation. New BarraCuda modules: `io::nanopore`
  (FAST5/POD5 reader), `bio::basecall` (signal → base). All downstream
  math operational (4,748+ checks). Experiments 196-202 planned.
