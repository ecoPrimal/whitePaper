# westGate Science Landscape — Data Estate, Use Cases, and Spring Guidance

**Status**: Living document — science capabilities enabled by colocated sovereign data
**Wave**: 155v/156d | **Date**: Aug 4, 2026 PM
**Gate**: westGate (Data NAS — ZFS raidz1, 5×14TB, 3.65 TB allocated / 60 TB free)
**Hardware**: AMD Ryzen 7 5700X (8C/16T), 64 GB DDR4, RTX 3070 (8 GB), Pop!_OS 22.04
**Audience**: Spring subteams, overwatch, gate operators spinning up parallel IDEs

---

## Why This Document

westGate holds **3.65 TB across 154 datasets spanning 17+ domains**, with the
provenance pipeline running at **43 files/s sustained** through the canonical
chain (BLAKE3 → CAS → batch DAG event → session-level Merkle commit → bearDog
Ed25519 → sweetGrass braid). 25 primal sockets live in membrane. Full NUCLEUS
tower operational. This document maps that data estate to the science it enables.

The principle: **grab once at 1 Gbps (internet), serve forever at 10 Gbps (LAN),
zero egress cost.** Every dataset downloaded once becomes a permanent sovereign
asset reusable by any gate, any spring, any experiment — with cryptographic
provenance proving where it came from and that it hasn't been modified.

**Provenance pipeline**: Canonical architecture — per-file CAS + batch DAG
events only (no per-file spine entries). Session-level spine commit at
dehydration. bearDog signature wired into sweetGrass braid. 122x throughput
improvement over the initial per-file spine pattern (0.3/s → 43/s).
See `PROVENANCE_TRIO_ARCHITECTURE.md` for the full analysis.

---

## I. Local Use Cases — westGate Standalone (No Mesh Required)

These run entirely on westGate with data already on ZFS. No inter-gate
connectivity needed. Phase 4 workloads per the 155p/156a blurb.

### 1. GPS Drug Repurposing Pipeline (tideGlass)

**The single most compelling local use case.**

tideGlass rebuilds the Bin Chen Lab GPS platform (Cell 2026) from scratch —
sovereign drug repurposing. The pipeline:

```
Disease signature → LINCS reversal screen → ChEMBL bioactivity validation
    → PDB structural docking → molecular tree search optimization
```

All 7 guideStone modules are **data-unblocked** on westGate:

| Module | Claim Validated | Key Datasets on ZFS |
|--------|-----------------|---------------------|
| tideglass-rges | RGES correlates with IC50 (r=0.52) | lincs_l1000 (20 GB), gps_platform (1.5 GB) |
| tideglass-rcl | RCL improves VCAP_t1 signal-to-noise | lincs_l1000, archs4 (40 GB) |
| tideglass-gps4drug | Structure → expression prediction | pdb_mmcif (88 GB), chembl37 (15 GB) |
| tideglass-screen | ZINC reversal screening recovers HCC actives | zinc20_smiles, lincs_l1000 |
| tideglass-molsearch | MCTS optimizes HCC lead (4→0.5 µM IC50) | chembl37, bindingdb (580 MB) |
| tideglass-octad | GPS exceeds OCTAD for HCC | tcga_gdc (15 GB), gtex_v8 (2.4 GB) |
| tideglass-nf | Novel NF1 tumor reversal scoring | nf_data_portal (246 MB), cosmic (5.2 GB) |

**Why it matters**: Cross-referencing LINCS L1000 Level 5 (1.3M drug perturbation
profiles) against TCGA + COSMIC + ChEMBL at scale is impractical via APIs — rate
limits, incomplete joins, missing bulk data. With everything colocated, the full
screen-to-lead pipeline runs without a single external API call.

**For the tideGlass subteam**: Your data is at `/mnt/nestgate/cold/zfs/data/`.
Key paths: `lincs_l1000/`, `chembl37/`, `gps_platform/`, `tcga_gdc/`, `cosmic/`,
`nf_data_portal/`, `pdb_mmcif/`. All BLAKE3-hashed and CAS-indexed. Start with
Module 1 (RGES) — it's the validation anchor for the entire GPS rebuild.

Additional expression data: `archs4/` (40 GB — human + mouse bulk RNA-seq
compendium in HDF5) and `gtex_v8/` (2.4 GB tissue baseline). These aren't in
the original GPS paper but enable training RCL/GPS4Drug with orders of magnitude
more conditions than LINCS alone.

---

### 2. Sovereign Metagenomics Pipeline (wetSpring)

**The hardest-to-replace asset on ZFS.**

267 GB of raw paired-end FASTQ from 5 BioProjects — downloaded once from ENA,
never re-downloadable at this scale via any API:

| BioProject | Environment | Size | Samples |
|------------|-------------|------|---------|
| PRJNA234377 | Mid-Cayman Rise hydrothermal vents | ~150 GB | 12 metagenomes |
| PRJNA362212 | Guaymas Basin sediments | ~113 GB | 4 metagenomes |
| PRJNA1224988 | Cyanobacterial bloom | — | community samples |
| PRJNA552483 | Florida red tide | — | harmful algal bloom |
| PRJNA524461 | Baltic Sea bloom | — | eutrophication |

wetSpring has **386 indexed experiments** and a full sovereign pipeline in pure
Rust: FASTQ → DADA2 → chimera detection → taxonomy → UniFrac → diversity →
pangenomics → Anderson spectral analysis. 625× Smith-Waterman speedup over
Python. Zero QIIME2, zero Galaxy dependency.

**For the wetSpring subteam**: Raw reads at `sra_fastq/`. Supporting databases:
`uniprot/` (844 MB), `pfam/` (23 GB), `interpro/` (13 GB), `ncbi_gene/` (9.6 GB),
`silva_138/` (implicit in ncbi_16s), `ensembl/` (72 MB). The barracuda workspace
has streaming I/O for FASTQ and mzML already wired.

---

### 3. Precision Agriculture (airSpring)

**The most "ready to boot" spring on westGate.**

90 experiments, 1,446 Rust tests, all data local. Eight ET₀ methods validated
against 15,300 real NOAA station-days (R²=0.97). The Michigan Crop Water Atlas:
100 stations × 80 years × 10 crops computed on consumer hardware.

| Dataset | Size | What It Enables |
|---------|------|-----------------|
| noaa_ghcnd | 3.5 GB | 120+ years global historical weather |
| noaa_global_temp | 98 KB | Global temperature anomaly series |
| noaa_co2 | small | Mauna Loa CO₂ reference |
| usda_nass | 132 MB | Crop yield statistics |
| epa_ucmr5 | 26 MB | Contaminant monitoring (PFAS context) |
| usgs_3dep | 20 KB | Elevation data |
| iris_earthquake | 2.4 MB | Seismic station metadata |
| iris_fdsn | 28 files | Seismic waveform data |

Vision: **sovereign irrigation scheduling on consumer hardware** — weather
station to field recommendation without cloud dependency. The FAO-56 dual Kc +
Richards equation + water balance pipeline runs entirely local.

**For the airSpring subteam**: Deploy graph `airspring_deploy` v2.0.0 is
registered in biomeOS with `assigned_gate = "westGate"`. Weather data at
`noaa_ghcnd/`, agriculture at `usda_nass/`. Shared datasets with groundSpring.

---

### 4. Measurement Science (groundSpring)

**The reality layer — quantifies the gap between models and noise.**

39 experiments, 461 validation checks. Five pillars: signal vs noise, inverse
problems, sensing systems, temporal dynamics, spatial propagation.

Uses NOAA weather, NCBI 16S metagenomes, and IRIS seismic data for real-world
validation — all on ZFS. The core thesis: other springs compute clean models,
groundSpring measures how far reality deviates and why.

**For the groundSpring subteam**: Deploy graph `groundspring_deploy` v2.0.0 is
ready. Shares NOAA and IRIS data with airSpring. The Cargo workspace has 2
crates + metalForge + 3 experiments. The measurement uncertainty bridge connects
to Anderson localization (hotSpring) and soil moisture (airSpring).

---

## II. Cross-Domain Threads — What Colocation Uniquely Enables

These analyses are impractical when data lives on different servers behind
different APIs. Having it all on one ZFS pool with 10 Gbps LAN access makes
them routine.

### The Anderson Disorder Thread

The most scientifically interesting pattern in the ecosystem. The same spectral
mathematics maps across four completely different physical domains:

| Domain | Spring | Datasets on ZFS | Phenomenon |
|--------|--------|-----------------|------------|
| Condensed matter | hotSpring | sarkas, murillo_plasma/surrogate | Electron localization in disordered metals |
| Deep-sea ecology | wetSpring | sra_fastq (267 GB), emp, silva | QS gene network disorder in vent communities |
| Pharmacology | healthSpring | chembl37, open_targets, intact | Drug binding landscapes, tissue penetration |
| Agriculture | airSpring | noaa_ghcnd, usda_nass | Soil moisture Anderson coupling |

The claim: **Anderson eigenvalue statistics predict both electron transport in
disordered lattices AND bacterial quorum sensing in hydrothermal vent biofilms.**
All the data to test this sits on one machine. The `anderson_spectral` module
is shared across springs.

### Expression + Structure + Variant Triangulation

Local COSMIC + ClinVar + gnomAD + TCGA + GTEx + ARCHS4 + LINCS + PDB + AlphaFold:

```
Somatic mutation (COSMIC) → Tissue expression context (GTEx/TCGA)
    → Drug perturbation reversal (LINCS) → Structure validation (PDB/AlphaFold)
```

This join across 9 databases at scale requires ~500 GB of colocated data.
Via APIs, the cross-referencing would take weeks and hit rate limits on every
source. Locally, it's a single pipeline.

### PFAS Environmental Chemistry Stack

Jones PFAS + EPA UCMR5 + Michigan EGLE (when unblocked) + MassBank + wetSpring
LC-MS pipeline → blueFish product:

```
Environmental sample → LC-MS/MS feature extraction → PFAS screening (KMD)
    → EPA 1633A QC validation → provenance-sealed report
```

blueFish is early (seed CLI) but the wetSpring science backing it has **40/40
validated checks** (FindPFAS, EPA PFAS ML, MassBank matching).

---

## III. Mesh Use Cases — What Lights Up With Inter-Gate Connectivity

These require songBird mesh validation (Phase 5) but represent the ecosystem's
full potential.

### Sovereign Structure Prediction (neuralSpring × strandGate)

westGate holds the data (335 GB AlphaFold + 88 GB PDB + 23 GB Pfam + 68 GB
UniRef90). strandGate has compute (dual EPYC + RTX 3090 + RX 6950 XT).
neuralSpring's coralForge path reproduces AlphaFold2/3 Evoformer.

The mesh enables: **stream 293 GB structural biology data from westGate →
run structure prediction on strandGate GPU → results back with full provenance
chain.** This is the single largest inter-gate data flow.

### Live Cell Composition (esotericWebb on ironGate)

The first-ever live cell composition boot in the ecosystem. esotericWebb
(CRPG, 453 tests, 9 primals) on ironGate proves the biomeOS deploy executor
chain. Once proven, every garden gets the same pattern — including the 4
westGate springs.

### Compute Dispatch (wetSpring → strandGate)

wetSpring science runs on westGate (data local), but GPU-heavy computations
(Smith-Waterman alignment at scale, structure prediction, Anderson spectral
on large matrices) dispatch to strandGate's RTX 3090 via toadStool. The mesh
enables data-local science with remote compute — no data movement, just
computation dispatch.

---

## IV. Spring-to-Data Matrix

Quick reference for which datasets serve which springs. Bold = primary consumer.

| Dataset | Size | tideGlass | wetSpring | airSpring | groundSpring | healthSpring | hotSpring | neuralSpring |
|---------|------|-----------|-----------|-----------|--------------|--------------|-----------|--------------|
| lincs_l1000 | 20 GB | **primary** | | | | | | |
| archs4 | 40 GB | **primary** | | | | | | |
| chembl37 | 15 GB | **primary** | | | | secondary | | |
| gps_platform | 1.5 GB | **primary** | | | | | | |
| pdb_mmcif | 88 GB | secondary | | | | | **primary** | secondary |
| alphafold* | 335 GB | secondary | | | | | | **primary** |
| tcga_gdc | 15 GB | **primary** | | | | secondary | | |
| cosmic | 5.2 GB | **primary** | | | | secondary | | |
| nf_data_portal | 246 MB | **primary** | | | | | | |
| sra_fastq | 267 GB | | **primary** | | | | | |
| uniprot* | 111 GB | | **primary** | | | secondary | | |
| pfam | 23 GB | | **primary** | | | | | secondary |
| interpro | 13 GB | | **primary** | | | | | |
| ncbi_gene | 9.6 GB | | **primary** | | | secondary | | |
| noaa_ghcnd | 3.5 GB | | | **primary** | **primary** | | | |
| noaa_global_temp | 98 KB | | | **primary** | secondary | | | |
| usda_nass | 132 MB | | | **primary** | secondary | | | |
| iris_earthquake | 2.4 MB | | | | **primary** | | | |
| iris_fdsn | 28 files | | | | **primary** | | | |
| epa_ucmr5 | 26 MB | | | **primary** | | | | |
| sarkas | 200 KB | | | | | | **primary** | |
| murillo_* | 329 MB | | | | | | **primary** | |
| gtex_v8 | 2.4 GB | secondary | | | | **primary** | | |
| open_targets | 1.2 GB | secondary | | | | **primary** | | |
| bindingdb | 580 MB | **primary** | | | | secondary | | |
| string_full | 23 GB | secondary | | | | secondary | | **primary** |
| ncbi_nr | 49 GB | | secondary | | | | | **primary** |
| pubchem_bioassay | 11 GB | secondary | | | | | | |

---

## V. Data Blockers — What's Still Missing

### Needs User Action (browser/registration)

| Dataset | Blocker | Priority | Spring Impact |
|---------|---------|----------|---------------|
| DepMap/CCLE | Cloudflare bot protection | P1 | healthSpring, tideGlass |
| EPA CompTox PFAS | Browser-only download | P1 | blueFish, wetSpring |
| Copernicus ERA5 | Licence acceptance needed | P2 | airSpring, groundSpring |
| DrugBank | Academic registration | P2 | tideGlass |
| OMIM genemap2 | API key pending (JHU) | P2 | healthSpring |
| HMDB metabolites | Cloudflare bot protection | P2 | wetSpring, blueFish |
| DisGeNET | API serves React SPA | P2 | healthSpring |
| PharmGKB | Terms acceptance | P2 | healthSpring |
| AmeriFlux | Registration required | P2 | airSpring |
| EcoCyc | Browser auth for flat files | P3 | wetSpring |
| Bgee expression | Cloudflare bot protection | P3 | healthSpring |

### Open Download Failures (need API research)

| Dataset | Issue | Spring Impact |
|---------|-------|---------------|
| Dryad LTEE fitness | 401/403 on download | wetSpring, lithoSpore |
| CORUM complexes | Site returns 0 bytes | healthSpring |
| dbNSFP | S3 bucket removed | healthSpring |
| MalariaGEN Pf6 | Site redesigned | healthSpring |
| HMP gene catalog | HMPDACC FTP non-functional | wetSpring |

Full details in `infra/wateringHole/scripts/data_blockers.md`.

---

## VI. Spring Bootup Readiness Summary

| Spring | Cargo Workspace | Deploy Graph | Data on ZFS | biomeOS Registered | Boot Status |
|--------|----------------|-------------|-------------|-------------------|-------------|
| **groundSpring** | 2 crates + 3 experiments (1,166 tests) | v2.0.0 | 3.6 GB | YES | **READY** |
| **airSpring** | per-experiment + metalForge (1,240 tests) | v2.0.0 | 3.6 GB (shared) | YES | **READY** |
| **wetSpring** | barracuda + experiments (2,210 tests) | v2.0.0 | 481 GB | YES | **READY** |
| **tideGlass** | 9-crate workspace (176 tests) | Cell graph v2.0.0 | 123 GB | Cell graph | **CODE + DATA READY** |

**biomeOS cell attach**: `biomeos nucleus attach` SHIPPED upstream (v4.57). westGate
currently running v4.56 — depot update needed. ironGate proves the chain first
(Phase 1: esotericWebb cell boot UNBLOCKED), then westGate springs follow (Phase 4).
Cell TOMLs exist for all 4 springs — see `westgate.toml` `[science.cell_graphs]`.

**tideGlass**: Full Rust rebuild complete — 9 crates (`tideglass-core`, `-rges`,
`-rcl`, `-gps4drug`, `-screen`, `-molsearch`, `-octad`, `-nf`, `-bin`), 176
tests, G56 Neural API routing, CAS wiring with graceful degradation, convergence
gate. Cell deploy graph at `gardens/tideGlass/graphs/cells/tideglass_cell.toml`.
**Data gap**: GPS platform data still NumPy/pickle format in CAS — needs JSON
conversion for Rust consumption.

**westGate data team provides**: ZFS storage, CAS indexing, provenance braiding,
convergence checks, data format readiness. Spring teams own their code.

---

## VII. Background Jobs

| Job | Status | Rate | Notes |
|-----|--------|------|-------|
| alphafold-bulk.service | Running | 56/s | 190K/246M done. Systemd, restart-safe. |
| alphafold-prov.service | **Running** | **43/s** | Provenance trailer — 81K braided, 0 errors. Canonical pipeline (CAS + batch DAG). |
| alphafold-sync.timer | Daily 03:00 | rsync | Proteome sync + sequences |

The provenance trailer runs the canonical pipeline: BLAKE3 → CAS → batch DAG
append (200 events/RPC) with periodic partial dehydration. No per-file spine
entries. The trailer catches up during download pauses. At 43/s, the 6.1M
queued files will be braided in ~40 hours.

These complete independently and don't block spring bootup.

---

## VIII. For Overwatch — Strategic View

### What We Can Do That Others Can't

1. **Cross-domain Anderson analysis** — same math tested against quantum physics,
   deep-sea metagenomics, pharmacology, and agriculture data, all on one machine,
   all provenance-tracked. No university HPC or cloud provider has this colocation.

2. **GPS drug repurposing without API dependency** — the full LINCS → ChEMBL →
   TCGA → PDB → AlphaFold pipeline runs locally. Cloud egress for this volume
   would cost thousands per run.

3. **Sovereign metagenomics** — 267 GB of irreplaceable deep-sea sequencing data
   with a 625× faster-than-Python analysis pipeline.

4. **Reproducible science on a USB stick** — lithoSpore guideStones are
   self-verifying scientific artifacts. Four USB drives already at MSU.

### What's Next

- **biomeOS depot update**: Update from v4.56 to v4.57 for `nucleus attach`
  (westGate ops — enables cell boot locally)
- **GPS data format**: Convert NumPy/pickle → JSON for tideGlass Rust consumption
  (westGate data team — unblocks tideGlass science)
- **Convergence sweep**: Run `convergence_check.py` across all 154 datasets,
  publish results for spring teams (westGate data team)
- **Phase 4 spring boot**: Cell TOMLs exist for all 4 springs. biomeOS cell
  attach is shipped upstream. westGate boots after ironGate Phase 1 proves chain.
  `biomeos nucleus attach --cell tideglass_cell.toml` once v4.57 deployed.
- **Phase 5 mesh**: songBird content.get dispatch validated upstream (22 bonds).
  westGate songBird healthy on UDS but discovery/federation degraded (no WG).
  Need WG activation or Tower Atomic LAN direct for inter-gate content.get.
- **Tower Atomic LAN**: westGate at 192.168.4.149/22, WireGuard not active.
  All Tower Atomic components shipped (bearDog BTSP, riboCipher, songBird TCP).
  353× faster than WG on LAN. Transition: dnsmasq resolves primal.eco to LAN IPs.
- **Data estate growth**: 60 TB available. Current 3.65 TB is 5.7% utilized.
  AlphaFold full 246M structures will add ~15 TB over time.
- **Neural API migration**: Spring consumers should route CAS through
  `neural-api-westgate-tower-155f.sock` for capability-based discovery,
  not direct `nestgate-westgate-tower-155f.sock` calls

---

*westGate is a sovereign scientific data root. Every byte is hashed, tracked, and
signed. The provenance pipeline runs at 43 files/s through the canonical
architecture — per-file CAS + batch DAG, session-level spine commit, bearDog
signature in the sweetGrass braid. The springs don't query external APIs — they
query local CAS with cryptographic proof of origin. This is what "grab once,
prove forever" looks like in practice.*
