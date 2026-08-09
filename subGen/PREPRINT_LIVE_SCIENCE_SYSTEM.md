# Preprint Live Science System — arXiv Snapshot + ecoPrimals Live Data

**Status**: Architecture defined, components identified, wiring in progress
**Date**: Aug 9, 2026 | **Wave**: 157a
**Principle**: The arXiv is a snapshot. ecoPrimals deals in live real science.

---

## Core Architecture

The reviewer (Murillo, Bazavov, Chuna) receives a preprint that points to a
**fully inspectable live system**. Not a PDF with dead links — a system where
every claim can be independently verified by pulling data, running code, and
checking provenance.

```
┌─────────────────────────────────────────────────────────────────────┐
│                          REVIEWER EXPERIENCE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. Read preprint (arXiv PDF / sporePrint web page)                 │
│  2. Visit sporeprint.primals.eco/hotspring-qcd-sun/                 │
│  3. Pull pseudoSpore: curl ... | tar xz                            │
│  4. Run validate.sh → BLAKE3 integrity + Ed25519 signature          │
│  5. Inspect configs (ILDG export → MILC toolchain)                  │
│  6. Re-run measurement: cargo run --bin arxiv_measure_battery        │
│  7. Compare: their numbers = our numbers = paper numbers             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Data Topology — Where Things Live

### westGate (CAS — Content-Addressed Storage)

The raw scientific data. 2.5 TB ZFS pool, sweetGrass braided, BLAKE3 addressed.

| Content | Size | Format | Access |
|---------|------|--------|--------|
| SU(N) thermalized configs | ~50 GB | `.lat` (internal) + `.milc` (ILDG) | `content.locate` via songBird |
| Observable measurements | ~2 GB | JSON + binary | CAS hash lookup |
| Benchmark results | ~500 MB | JSON timeseries | CAS hash lookup |
| Source snapshots | ~200 MB | Git archives | BLAKE3 tagged |

### ironGate (NFT — Results/Artifacts)

The signed, frozen, publishable artifacts. Ed25519 signed by bearDog.

| Artifact | Contents | Hash | Signature |
|----------|----------|------|-----------|
| `hotspring-qcd-sun-v1.0.0-rung1.pseudospore` | Configs + code + provenance | BLAKE3 DAG root | Ed25519 (bearDog) |
| `hotspring-qcd-sun-v2.0.0-rung2.pseudospore` | + GPU parity + silicon offloading | BLAKE3 DAG root | Ed25519 |
| `hotspring-qcd-sun-v3.0.0-rung3.pseudospore` | + dynamical fermions + MILC | BLAKE3 DAG root | Ed25519 |

### sporePrint (Public Face)

The web-viewable presentation at `sporeprint.primals.eco`:

| Page | Content | Status |
|------|---------|--------|
| `/hotspring-qcd-sun/` | Landing page: abstract, results summary, download links | Live (needs relabel) |
| `/hotspring-qcd-sun/rung1/` | Pure gauge: plaquettes, cross-GPU, precision | To build |
| `/hotspring-qcd-sun/rung2/` | GPU parity + silicon offloading + capacity | To build |
| `/hotspring-qcd-sun/rung3/` | Dynamical fermions + MILC comparison | Future |
| `/hotspring-qcd-sun/data/` | Interactive observable browser | Future |
| `/pseudospore/hotspring-qcd-sun/` | Download: .tar.gz + validate.sh + signature | Wired (needs content) |

### nestgate.io (Trust Dashboard)

The mesh-visible provenance view:

| Section | Shows | Status |
|---------|-------|--------|
| Data Braids | westGate CAS entries for QCD configs | Wired (NG-05 closed) |
| Pseudospores | ironGate NFT artifacts (signed bundles) | UI exists, content pending |
| Mesh Peers | Which gates hold which data | Live (11 peers) |

---

## The Braid Chain — Full Validation Path

```
Thermalize (strandGate GPU)
    ↓ content-addressed .lat file
    ↓ BLAKE3 hash = config identity
Store on westGate CAS (sweetGrass braid)
    ↓ braid.head announces to songBird mesh
    ↓ any gate can content.locate → pull
Measure (strandGate GPU or any gate)
    ↓ observable JSON with config hash ref
    ↓ provenance: which binary, which seed, which hardware
Package (lithoSpore → ironGate)
    ↓ pseudoSpore bundle: configs + observables + code + DAG
    ↓ Ed25519 signed by bearDog
    ↓ BLAKE3 root = bundle identity
Serve (sporePrint + petalTongue)
    ↓ /pseudospore/hotspring-qcd-sun/ → .tar.gz download
    ↓ validate.sh: check BLAKE3 integrity + Ed25519 signature
    ↓ cargo run: reproduce any measurement from source
```

A reviewer can:
1. Download the pseudoSpore (a .tar.gz from the website)
2. Run `validate.sh` — checks every file's BLAKE3, verifies the DAG, checks Ed25519
3. Load any config into their own MILC toolchain (ILDG format included)
4. Re-run our measurements with our code (Rust + cargo, no CUDA required)
5. Compare their independent calculation to our published values

**This is what "live science" means**: not just a PDF, but an inspectable, reproducible, verifiable system.

---

## Rung Write-up Status

### Rung 1 — SU(N) Pure Gauge (PAPER COMPLETE, 41/42)

| Component | Status | Location |
|-----------|--------|----------|
| Paper source | DONE | `subGen/LATTICE_QCD_CONSUMER_GPU_ARXIV.md` |
| LaTeX | DONE | `subGen/lattice_qcd_consumer_gpu.tex` |
| Data (105 configs) | DONE | `~/.local/share/hotspring/configs/` |
| Cross-GPU parity | DONE | `bench_silicon_crosspath_qcd` binary |
| MILC round-trip | DONE | `ildg_roundtrip_b11` binary |
| Figures (4 PDF) | DONE | `subGen/generate_figures.py` |
| pseudoSpore bundle | **PENDING** | lithoSpore packaging |
| validate.sh | **PENDING** | Write BLAKE3 + Ed25519 verification |
| sporePrint page | **PARTIAL** | Needs SU(N) relabel + download links |

**Remaining for reviewer send**: validate.sh + pseudoSpore package + sporePrint page update.

### Rung 2 — GPU Parity + Silicon Offloading + Capacity (DATA COMPLETE)

| Component | Status | Location |
|-----------|--------|----------|
| GPU/CPU thermalization parity | DONE | `validate_gpu_cpu_therm_parity` |
| GPU-to-GPU PCIe streaming | DONE | `bench_gpu_pcie_stream` |
| Cross-silicon profiling (AMD 19x) | DONE | `bench_silicon_volume_scaling` |
| Silicon offloading (ROP/TMU/subgroup) | DONE | `profile_lattice_capacity` |
| 32⁴ GPU thermalization | DONE | `test_32_4_gpu_therm` (validated today) |
| Capacity analysis (22⁴ → 73⁴) | DONE | Profiled, documented |
| NPU phase classification | DONE | `sun_npu_metalforge` |
| Write-up | **PARTIAL** | Scattered across profiling docs |

**Remaining**: Consolidate into paper §3.5 (silicon offloading) + §4.9 (capacity). Write Rung 2 section.

### Rung 3 — Dynamical Fermions / RHMC (CODE COMPLETE, DATA PENDING)

| Component | Status | Location |
|-----------|--------|----------|
| Staggered Dirac operator | Implemented | `lattice/dirac.rs` + WGSL |
| Multi-shift CG (8 poles) | Implemented | `rhmc/multishift_cg.rs` + GPU |
| Pseudofermion action + force | Implemented | `pseudofermion/` |
| Hasenbusch preconditioning | Implemented | `pseudofermion/hasenbusch.rs` |
| RHMC rational approximation | Implemented | `rhmc/mod.rs` |
| GPU RHMC trajectory | Implemented | `gpu_hmc/gpu_rhmc.rs` |
| Nf=2 production data | **PENDING** | Need: plaquette vs β with fermions |
| MILC comparison (dynamical) | **PENDING** | Need: Chuna's MILC configs |
| Write-up | **SCAFFOLD** | See below |

### Rung 4 — Nf=2+1 / Physical Point (CODE COMPLETE, DATA PENDING)

| Component | Status | Location |
|-----------|--------|----------|
| Nf=2+1 configuration | Implemented | `rhmc/mod.rs` (`nf2p1()`) |
| Light + strange sector | Implemented | Two independent RHMC sectors |
| Scale setting (w₀) | **PENDING** | Need gradient flow measurement |
| Hadron spectrum | **PENDING** | Need correlator analysis |
| Write-up | **SCAFFOLD** | See below |

### Rung 5 — Finite-Temperature (CODE READY, DATA PENDING)

| Component | Status | Location |
|-----------|--------|----------|
| Asymmetric lattices (Ns³×Nt) | Ready | `wilson.rs` (arbitrary dims) |
| Polyakov loop | Implemented | `wilson.rs` + GPU |
| Temperature scan | **PENDING** | Need: β-scan on 32³×{6,8,10,12} |
| Continuum extrapolation | **PENDING** | Need: multiple Nt at same T |
| EOS (p, s, ε) | **PENDING** | Need: trace anomaly method |
| Write-up | **SCAFFOLD** | See below |

---

## What the PIs Get — The Inspectable System

When you send to Murillo, Bazavov, and Chuna, they don't get a PDF. They get:

1. **The PDF** (arXiv snapshot) — traditional paper with all claims
2. **The URL** (`sporeprint.primals.eco/hotspring-qcd-sun/`) — live rendered version
3. **The pseudoSpore** (downloadable .tar.gz) — all data + code + provenance
4. **The validation** (`validate.sh`) — cryptographic verification they run locally
5. **The mesh** (nestgate.io) — live dashboard showing data braids + trust surfaces

The scyBorg coverage (ORCID + CC-BY-SA) means:
- They can cite, extend, and build on the data
- The provenance chain proves authorship independent of any journal
- The AGPL code means any modifications they make are also open

---

## Implementation Priority

| Task | Effort | Blocks |
|------|--------|--------|
| `validate.sh` (BLAKE3 + Ed25519 script) | 2-3 hr | Reviewer send |
| lithoSpore package (configs → .tar.gz) | 2-3 hr | Reviewer send |
| sporePrint page update (SU(N) relabel + links) | 1-2 hr | Reviewer send |
| Paper §3.5 silicon offloading | 2-3 hr writing | Paper completeness |
| Consolidate Rung 2 data into paper sections | 3-4 hr writing | Paper completeness |
| Rung 3 scaffold (section headers + data plan) | 1 hr | Roadmap clarity |
| Rung 4-5 scaffold (section headers + data plan) | 1 hr | Roadmap clarity |

---

*strandGate — Wave 157a — Aug 9, 2026. The arXiv is a snapshot; ecoPrimals
is live science. Reviewers get a fully inspectable system: PDF + URL + pseudoSpore
+ validate.sh + mesh dashboard. westGate CAS + ironGate NFT + sporePrint web =
complete trust surface for independent verification and replication.*
