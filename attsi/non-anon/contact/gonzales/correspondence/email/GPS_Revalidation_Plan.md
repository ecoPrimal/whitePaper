# GPS Platform — Revalidation Plan

**Prepared by**: Kevin Mok
**Date**: June 8, 2026
**For**: Andrea Gonzales / Bin Chen introduction
**Infrastructure**: [primals.eco](https://primals.eco) | [lab.primals.eco](https://lab.primals.eco)

---

## Who We Are

### The Short Version

A sovereign computational science ecosystem — hardware, software, and validated pipelines — built over two years on personal hardware, open source, and AI-accelerated development. No cloud dependency, no institutional overhead, no gatekeepers. Everything published, everything AGPL-3.0, everything running.

### The Generational Arc

This project has been evolving through distinct generations, each answering a harder question than the last:

| Gen | Question | Answer | Scale |
|-----|----------|--------|-------|
| **gen1** (2024) | Can we build sovereign HPC? | Yes — $15K sovereign mesh, fault-tolerant, AI-assisted development | 11 gates, first primals |
| **gen2** (2025) | What should the architecture be? | A composable protocol — 8 primals, sovereignty as operating principle | biomeOS, BYOAI, Philosophy of Forgetting |
| **gen3** (early 2026) | Does the science actually work? | Yes — 12,510+ automated checks, 70+ published papers reproduced, 7 scientific domains, 14 composable primals | PhD thesis, Anderson framework, 7 springs |
| **gen4** (spring 2026) | Who uses it? | Game designers, computational chemists, analytical chemists, microbiologists, genomicists — via 5 shipped products | esotericWebb, lithoSpore, initioChem, blueFish, helixVision |
| **gen5** (now) | Does someone else's science come out the other end? | In progress — GPS rebuild is the first test | Andrea's NF + GPS = first external science production |

**gen4 and gen5 are where we are now.** The ecosystem proved it can validate published science (gen3) and ships early products (gen4). The question gen5 answers is whether this infrastructure can support an external domain expert's real biological question — and produce science they own. The GPS revalidation, connected through Andrea Gonzales's consultation on AI/data science approaches to drug discovery, is the first instance of that pattern.

### What Already Exists

The ecosystem isn't a plan — it's running code with validated results:

| Domain | Spring | Validated Work | Checks |
|--------|--------|---------------|--------|
| Drug discovery / PK/PD | healthSpring | Hill dose-response, MATRIX repurposing, Anderson tissue geometry, ChEMBL bioactivity, HTS pipelines, 6 barraCuda GPU shaders | 1,021 tests, 95 experiments |
| Genomics / data fetch | wetSpring | ChEMBL/PubChem/GEO fetch via NestGate with provenance trio tracking, expression analysis | 6,656+ checks |
| Molecular dynamics | hotSpring | GROMACS/PLUMED parity, conformational landscapes, QCD, plasma physics | 190+ checks |
| Machine learning | neuralSpring | Echo state networks, Akida neuromorphic, regime classification | 154+ checks |
| Microbial evolution | groundSpring | LTEE mutation/fitness trajectories, drift/selection statistics | Validated |
| Environmental chemistry | airSpring | FAO-56 evapotranspiration, soil physics, water balance | Validated |
| Game design | ludoSpring | Sovereign RPG engine, Overwatch coordination patterns | 791 tests |

**Total**: 12,510+ automated science checks across 70+ reproduced papers, all Rust, all GPU-enabled, all provenance-tracked.

### Active Collaborators

| Collaborator | Domain | Status | Deliverable |
|-------------|--------|--------|-------------|
| **Gonzales** (MSU Pharmacology) | NF data mining, GPS connection | **Engaged** — GPS consultation, Bin Chen intro offered | pseudoSpore, CTF NDU prelim data |
| **ABG** (citizen science) | CAZyme conformational dynamics | **Producing** — pseudoSpore v1.7.0 delivered | Self-verifying artifact shipped |
| **Jones** (emeritus, analytical chem) | PFAS quantification | **Active** — consulting, product spec | blueFish pipeline |
| **Barrick** (MSU, LTEE) | Microbial evolution | **Contacted** — 4 USB drives delivered | lithoSpore (73 science checks) |

---

## The 20-Year Lineage

The GPS platform sits at the end of a 20-year intellectual chain. Each step built on the last — and each step is a validation target.

| Year | Paper | Scale | What It Did |
|------|-------|-------|-------------|
| 2006 | Lamb — Connectivity Map | 164 compounds, 3 cell lines | Proved reversal hypothesis: drug-induced expression opposite to disease = therapeutic candidate |
| 2010-2020 | NIH LINCS Program | $150M, 3,000,000+ profiles | 1000x scale-up of CMap. L1000 assay: 978 landmark genes, $2/sample |
| 2016 | Duan — L1000CDS2 | 22,000+ signatures | Search engine for perturbation signatures. Cosine similarity, <4 sec per query |
| 2017 | Chen — RGES | 66,000 compound profiles, 12M activity measurements | Proved reversal score correlates with IC50 (r=0.52). 4 HCC compounds validated in vivo |
| 2017 | Subramanian — L1000 Platform | 1,319,138 profiles, 42,080 perturbagens, 77 cell lines | THE training data. All public. All fetchable |
| 2021 | Zeng — OCTAD | 19,127 patient samples, 50+ cancer types, 12,442 compounds | Drug repurposing platform. GPS predecessor — same lab, same philosophy |
| 2026 | Xing — GPS (Cell) | RCL + GPS4Drug + MolSearch | Predicts expression from structure. Screens 750M+ compounds. Designs novel therapeutics |

164 compounds in 2006. 750 million in 2026. The data exists. The question is what we do with it.

---

## The Data Landscape

### Tier 1: Required for Reproduction (~35 GB)

| Source | Dataset | Size | What GPS Uses It For |
|--------|---------|------|---------------------|
| Broad/LINCS | L1000 Level 5 Phase 1 ([GSE92742](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742)) | 23 GB | 473,647 drug perturbation signatures (training data) |
| Broad/LINCS | L1000 Level 5 Phase 2 ([GSE70138](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE70138)) | 5 GB | 118,050 additional signatures |
| Zenodo | GPS artifact v6 ([record 17956238](https://zenodo.org/records/17956238)) | 840 MB | Code, model weights, figure data |
| Figshare | ChEMBL transformation rules | 1.5 GB | MolSearch reaction templates (SQLite) |
| ZINC | Screened subset ([zinc.docking.org](https://zinc.docking.org)) | ~5 GB | 750M+ purchasable compounds for virtual screening |

### Tier 2: Full Validation (+14 GB)

| Source | Dataset | Size | Purpose |
|--------|---------|------|---------|
| Bioconductor | OCTAD database | ~6 GB | 19,127 patient samples for cross-validation |
| EBI | ChEMBL activity database ([chembl](https://www.ebi.ac.uk/chembl/)) | ~3 GB | Compound activity validation |
| NCI GDC | TCGA HCC + IPF expression | ~2 GB | Disease signature validation |
| DepMap | CCLE cancer cell line profiles | ~1 GB | Cell line mapping |
| Enamine | HTS compound library | ~2 GB | Extended screening |

### Tier 3: Full Archaeology (+268 GB)

| Source | Dataset | Size | Purpose |
|--------|---------|------|---------|
| Broad/LINCS | L1000 Level 1 (raw fluorescence) | 223 GB | Ground truth — proves Level 5 is correct |
| Broad/LINCS | L1000 Level 2 (expression) | ~15 GB | Pre-normalization |
| Broad/LINCS | L1000 Level 3 (inferred) | ~30 GB | Full 12,328 gene inference |

**Total storage budget**: 35 GB (reproduction) → 49 GB (full validation) → 317 GB (archaeology)

---

## Hardware

I own every watt and every piece of silicon. No queue times, no shared anything, no cloud dependency. ~$15K total investment, assembled from consumer and secondary market hardware over two years. The mesh is coordinated by biomeOS — our orchestration substrate — with workloads dispatched via toadStool (hardware routing) and math executed via barraCuda (WGSL GPU shaders). Data is content-addressed and provenance-tracked through the nestGate primal.

### The Mesh — 11 Sovereign Gates

| Gate | CPU | RAM | GPUs | Role |
|------|-----|-----|------|------|
| **biomeGate** | Threadripper 3970X (32c/64t) | 256 GB DDR4 | RTX 5060 + Titan V + Tesla K80 (+ float pool) | **GPS primary** — HBM2 test bench, heavy compute |
| **strandGate** | Dual EPYC 7452 (64c/128t) | 256 GB ECC DDR4 | RTX 3090 + RX 6950 XT + Akida NPU | Bioinformatics, dual-vendor GPU validation |
| **northGate** | Ryzen 9 9950X3D | 96 GB DDR5 | RTX 5090 (32 GB) | Flagship single-GPU (Blackwell SM120) |
| **ironGate** | i9-14900K | 96 GB DDR5 | RTX 5070 | Agentic development, composition validation |
| **southGate** | Ryzen 5800X3D | 128 GB DDR4 | RTX 4060 + PCIe slots for work cards | Heavy compute, work cards slot in |
| **eastGate** | i9-12900 | 32 GB DDR5 | RTX 4070 + Akida NPU | Utility, neuromorphic workloads |
| **swiftGate** | Ryzen 5800X | 64 GB DDR4 | RTX 3070 FE | Mobile/compact compute |
| **flockGate** | i9-13900K | 64 GB DDR5 | RTX 3070 Ti | Remote covalent gate |
| **kinGate** | i7-6700K | 32 GB DDR4 | RTX 3070 | Staging / utility |
| **westGate** | i7-4771 | 32 GB DDR3 | RTX 2070 Super | Cold storage archive (76 TB ZFS) |
| **blueGate** | TBD | 128 GB DDR4 | — | Expansion gate |

### Floating Work Card Pool

Large GPUs move between gates based on workload — any gate with PCIe slots can host them.

| Card | Qty | Memory | Type | GPS Role |
|------|-----|--------|------|----------|
| Titan V | 2 | 12 GB HBM2 each | Volta SM70 | Batch compound screening |
| MI50 | 2 | 16 GB HBM2 each | Vega 20 GCN 5.0 | GPS4Drug training, MCTS |
| RTX 3090 | 2 | 24 GB GDDR6X each | Ampere GA102 | Large-model inference |
| Tesla K80 | 1 | 24 GB GDDR5 (2x12) | Kepler GK210 | Kepler architecture coverage |

### Aggregate

| Resource | Total |
|----------|-------|
| **Gates** | 11 |
| **CPU cores** | 154+ |
| **System RAM** | ~1.0 TB |
| **GPU VRAM (all cards)** | ~248 GB |
| **HBM2 VRAM** | 56 GB (2x Titan V + 2x MI50) |
| **Storage** | ~122 TB (46 TB NVMe + 76 TB HDD ZFS) |
| **GPU vendors** | NVIDIA + AMD (universal compute validated on both) |
| **GPU architectures** | Kepler → Volta → Ampere → Ada → Blackwell (NVIDIA) + Vega 20 + RDNA 2 (AMD) |
| **NPUs** | 3x BrainChip Akida AKD1000 |
| **HSMs** | 4x SoloKey FIDO2 |
| **Network** | 10G backbone (4 primary gates) + 1G mesh (remaining) |
| **VPS outer membrane** | DigitalOcean nyc1 ($12/mo), `membrane.primals.eco` TLS surface |

### GPS Rebuild Fit

The GPS rebuild is trivial to this infrastructure:

| GPS Requirement | What Handles It |
|----------------|-----------------|
| L1000 training data (23 GB) | biomeGate 256 GB RAM — fits entirely in memory |
| GPS4Drug model training | Titan V pair or MI50 pair — 96 GB GPU VRAM distributes across fleet |
| MCTS tree search (MolSearch) | MI50 pair — 32 GB HBM2 for tree expansion |
| ZINC batch screening (750M compounds) | Titan V pair — streaming dispatch via toadStool |
| Full archaeology dataset (317 GB) | biomeGate NVMe array (5 TB available) |
| Cold storage / archival | westGate 76 TB ZFS |
| 10G data movement | Backbone live — 4 primary gates interconnected |

**What this means for Bin Chen**: Once I revalidate the platform, his group gains access to dedicated compute for running further experiments while the preprint matures — new disease signatures, larger screening libraries, parameter sweeps that would sit in a university queue for days. The mesh is here and it's mine to point at whatever the science needs.

### Infrastructure Links

- [primals.eco](https://primals.eco) — project overview, published papers, validated pipeline
- [lab.primals.eco](https://lab.primals.eco) — live computational environment (browsable, no login required), nascent, but intended for full compute visibility
- [github.com/sporeGarden/projectNUCLEUS](https://github.com/sporeGarden/projectNUCLEUS) — NUCLEUS composition layer (gate germination, 13/13 primals)
- [github.com/ecoPrimals/barraCuda](https://github.com/ecoPrimals/barraCuda) — GPU math primal (712+ WGSL f64 shaders, multi-device dispatch)
- [github.com/ecoPrimals/toadStool](https://github.com/ecoPrimals/toadStool) — hardware primal (gate discovery, GPU/NPU dispatch, 20,843 tests)
- [github.com/syntheticChemistry/healthSpring](https://github.com/syntheticChemistry/healthSpring) — drug discovery spring (1,021 tests, 6 barraCuda shaders)
- [github.com/syntheticChemistry/wetSpring](https://github.com/syntheticChemistry/wetSpring) — genomics spring (provenance-tracked data fetch, 6,656+ checks)

---

## Observations from the Preprint

### The Compression Problem

The paper calls the system "GPS" and talks about building an "Atlas" of metabolic signatures. These are good metaphors but they undersell the problem.

An atlas loses enormous amounts of data — it's a static projection of something dynamic. At each stage of the lineage, the field compressed:

| Stage | What Was Compressed | What Was Lost |
|-------|-------------------|---------------|
| CMap (2006) | 164 compound profiles → similarity scores | Per-gene resolution |
| LINCS (2017) | 12,328 genes → 978 landmarks | 92% of transcriptome (inferred back, but still) |
| OCTAD (2021) | 19,127 patient transcriptomes → summary signatures | Patient-level variation |
| GPS (2026) | 473,647 profiles → learned embedding space | Explicit mechanistic relationships |

Each step is useful. Each step also throws away information the biology actually carries. And GPS is a route finder between known points — it predicts expression along paths the training data defines, but doesn't map the terrain between those paths.

### Topographic Maps of a Dark System

What the biological reality demands is full topographic maps of metabolic and transcriptomic landscapes we can't directly observe — with a pathfinder that uses GPS-like feedback to explore and update as it learns.

I spent years in the Army building terrain models from topographic maps — translating contour lines and elevation data into three-dimensional pictures of ground you couldn't see yet, so that when you got there, you already understood the landscape. The problem here is the same problem at a different scale. The expression data is the contour lines. The diseases are the terrain. The compounds are the routes. And the current platform gives you route suggestions without building the full terrain model first.

The question is how far we can push it toward mapping the actual terrain rather than finding routes through a simplified version of it.

### Why Revalidation Reveals This

By rebuilding from the methods rather than just running their code, I can see where the compression happens — where the pipeline flattens information that the biology needs. That's where the evolution starts. That's what makes this more than a reproduction exercise.

---

## The Plan

### Phase 0: Archaeology (Week 1-2)
- Inventory all files, dependencies, environments from Zenodo artifact
- Map Python 2 vs Python 3 boundaries
- Trace every data dependency to its primary source
- Document the full 20-year paper chain as validation targets

### Phase 1: Reproduce — Paper Parity (Week 2-4)
- Stand up RCL on VCAP_t1 (their example case)
- Reproduce GPS4Drug inference on held-out test data
- Reproduce MolSearch HCC lead optimization (IC50 4 uM → 0.5 uM claim)
- Reproduce all figures from `data_for_GPS_figures.zip`
- Document every reproduction failure and workaround
- Each reproduced module emits a pseudoSpore milestone

### Phase 2: Validate — guideStone Grade (Week 4-6)
- Cross-validate RCL output against raw LINCS data
- Validate GPS4Drug predictions against ChEMBL experimental data
- Quantify: how much of the claimed performance is real vs pipeline artifact?
- Write validation report (guideStone format: check count, pass/fail, evidence, named tolerances)

### Phase 3: Rebuild Sovereign (Week 6-12)
- Clean inference pipeline, remove dead code, modern Python
- Scoring math in Rust via barraCuda primitives (RGES, reversal, MCTS — extends existing validated shaders)
- All data fetch through NestGate provenance-tracked pipelines
- Provenance trio (rhizoCrypt DAG + loamSpine ledger + sweetGrass braid) on every computation
- Automated test suite for every reproduction target

### Phase 4: Package + Extend — lithoSpore (Week 12+)
- pseudoSpore: self-verifying artifact with all modules, data, validation, one command to check
- lithoSpore: USB-deployable guideStone — portable, runs offline, self-proving
- Extend to NF: screen against NF Data Portal transcriptomic signatures
- Cross-species: Anderson tissue geometry modulates reversal predictions per tissue type

---

## NF Extension (Parallel Work)

While correspondence with Bin Chen develops, I'll apply the GPS reversal screening to NF:

1. Fetch NF disease signatures from [NF Data Portal](https://nf.synapse.org) via NestGate (content-addressed, provenance-tracked)
2. Compute RGES for all LINCS-profiled compounds against NF signatures (barraCuda WGSL shaders for batch scoring)
3. Screen ZINC with GPS4Drug for novel NF reversal candidates
4. Cross-reference with existing healthSpring scoring (MATRIX, selectivity index, Anderson geometry for nerve sheath tissue)
5. Validate against known NF therapeutics (MEK inhibitors — selumetinib, trametinib)
6. Package results as a pseudoSpore — self-verifying computational preliminary data for CTF NDU

This produces computational preliminary data for the CTF NDU application. Same methods as the Cell paper, applied to a disease Andrea's group is already working on.

---

## Questions for Bin Chen

1. Which GPS results does he trust most? Which modules has he seen break?
2. What validation data would convince him the rebuild is correct?
3. License discrepancy: Apache 2.0 on GitHub vs GPL-3.0 on Zenodo — which is authoritative?
4. Are there unpublished preprocessing steps or model weights not in the public artifact?
5. What disease signatures would he most want to see GPS extended to next?

---

## Links

### GPS Platform
- [GPS Paper (Cell 2026)](https://www.cell.com/cell/fulltext/S0092-8674(26)00223-0)
- [GPS Zenodo v6](https://zenodo.org/records/17956238)
- [GPS GitHub](https://github.com/Bin-Chen-Lab/GPS)
- [OCTAD GitHub](https://github.com/Bin-Chen-Lab/octad)
- [RGES GitHub](https://github.com/Bin-Chen-Lab/RGES)
- [GPS Web Portal](http://apps.octad.org/GPS/)

### Data Sources
- [LINCS L1000 Phase 1 (GSE92742)](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742)
- [LINCS L1000 Phase 2 (GSE70138)](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE70138)
- [CLUE Portal](https://clue.io)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)
- [ZINC](https://zinc.docking.org)
- [NF Data Portal](https://nf.synapse.org)
- [OCTAD](http://octad.org)

### Ecosystem
- [primals.eco](https://primals.eco) — project overview, published papers, validated pipelines
- [lab.primals.eco](https://lab.primals.eco) — live computational environment (browsable, no login)
- [github.com/sporeGarden/projectNUCLEUS](https://github.com/sporeGarden/projectNUCLEUS) — NUCLEUS composition layer (gate germination, primal coordination)
- [github.com/ecoPrimals/barraCuda](https://github.com/ecoPrimals/barraCuda) — GPU math primal (712+ WGSL shaders)
- [github.com/ecoPrimals/toadStool](https://github.com/ecoPrimals/toadStool) — hardware primal (gate discovery, dispatch)
- [github.com/ecoPrimals/coralReef](https://github.com/ecoPrimals/coralReef) — sovereign shader compiler (WGSL → native GPU binary)
- [github.com/syntheticChemistry/healthSpring](https://github.com/syntheticChemistry/healthSpring) — drug discovery spring (1,021 tests)
- [github.com/syntheticChemistry/wetSpring](https://github.com/syntheticChemistry/wetSpring) — genomics spring (provenance-tracked fetch, 6,656+ checks)
