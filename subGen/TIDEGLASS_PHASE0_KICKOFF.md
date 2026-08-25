# tideGlass Phase 0 — Kickoff Document

**Status:** Infrastructure COMPLETE. Phase 0 archaeology NOT STARTED.
**Priority:** HIGH — sole gen5 science bottleneck
**Blocker chain:** Phase 0 → Phase 1 → NF pseudoSpore → JOSS → CTF NDU $125K
**Date:** August 25, 2026

---

## What's Already Done (Don't Repeat This Work)

| Step | Status | Evidence |
|------|--------|---------|
| bearDog `crypto.sign_ed25519` | COMPLETE | Wave 155j (Jul 29), commit `3739e7078` |
| Provenance Trio 7/7 | COMPLETE | Wave 155k (Jul 30), DID `did:key:z6Mkryaa7n6hfpSbGaZwbqPMD6MzXukgdQK3XRKzwFSgce8o` |
| NF Data Portal ingestion | COMPLETE | 658 files (666 MB) on westGate ZFS |
| Data federation | COMPLETE | 482 GB across 7 modules on ZFS, 100% provenance |
| tideGlass Rust crates | EXIST | 9-crate workspace, 176 tests |
| GPS Platform data | ON ZFS | 11 JSON outputs (103.4 MB) CAS-ingested |

**Phase 0 is fully unblocked. It just hasn't started.**

---

## Phase 0: Archaeology (What You're Doing)

The goal is to understand the original GPS pipeline well enough to validate
tideGlass against it. This is documentation, not coding.

### Step 1: Inventory Zenodo Artifacts (~2 hours)

GPS source materials:
- Zenodo v5 (713 MB) / v6 (840 MB) — GPS Platform archive
- GitHub: gps4drugs/ repository
- Cell 2026 publication: GPS figure data (`data_for_GPS_figures.zip`)

Action:
- [ ] Download/inventory Zenodo artifacts to `gonzales/gps/phase0/zenodo_inventory.md`
- [ ] Map every file to its role in the pipeline
- [ ] Note Python version requirements (Python 2 vs 3 boundaries)

### Step 2: Map Dependency Graph (~2 hours)

The GPS pipeline has mixed dependencies:
- Python (multiple versions)
- Fortran components (compute chain)
- LINCS L1000 data joins
- GEO expression data
- ChEMBL joins
- Model weights

Action:
- [ ] Read `gps_env.yml` and trace every dependency
- [ ] Identify Fortran components in compute chain
- [ ] Document full dependency graph in `phase0/dependency_graph.md`
- [ ] Note license issues (Apache 2.0 vs GPL-3.0 discrepancy)

### Step 3: Trace Data Lineage (~3 hours)

The GPS pipeline consumes:
- LINCS L1000 (gene expression signatures)
- GEO (Gene Expression Omnibus datasets)
- ChEMBL 37 (compound bioactivity)
- NF Data Portal (disease-specific data)

Action:
- [ ] Trace each data source to its tideGlass ZFS location
- [ ] Map data flow: raw → processed → model input → output
- [ ] Document in `phase0/data_lineage.md`
- [ ] Verify ZFS data matches expected inputs

### Step 4: Read Paper Lineage (~2 hours)

Understand what GPS is built on:
- OCTAD (Open Cancer TherApeutic Discovery)
- L1000CDS2 (L1000 Characteristic Direction Signature search)
- Connectivity Map
- GPS Cell 2026 publication

Action:
- [ ] Read GPS Cell 2026 paper
- [ ] Read OCTAD paper (predecessor)
- [ ] Document evolution: OCTAD → L1000CDS2 → CMap → GPS
- [ ] Write `phase0/paper_lineage.md`

### Step 5: Write Phase 0 Summary (~1 hour)

Combine all archaeology into a single summary:
- [ ] `gonzales/gps/phase0/README.md` — what GPS is, how it works, what we need to reproduce
- [ ] Identify the minimum validation target for Phase 1

---

## Phase 1: Reproduce (After Phase 0)

| Module | Validation target | Data |
|--------|-------------------|------|
| RGES | r=0.52±0.05 vs IC50 | L1000 + ChEMBL |
| RCL | SNR improvement >1.5× on VCAP_t1 | L1000 |
| GPS4Drug | R² within 5% of held-out test | GPS model weights |
| MolSearch | IC50 4µM → 0.5µM (fold >4×) | ChEMBL |
| OCTAD parity | GPS exceeds OCTAD for HCC | GPS figures |
| NF extension | MEK inhibitors (selumetinib) in top-100 | NF Data Portal |

### Phase 1 Actions:
- [ ] Stand up legacy Docker reference from Zenodo/GitHub
- [ ] Run `cargo build --release` in tideGlass repo
- [ ] Boot tideGlass cell: `biomeos nucleus attach --cell tideglass_cell.toml`
- [ ] Run Tier 1 module 1 (RGES) as validation anchor
- [ ] Compare Rust output vs legacy Python output
- [ ] Document results in `phase1/` per module

---

## Phase 2-6 (After Phase 1)

```
Phase 2: Rust parity confirmed
Phase 3: Sovereign rebuild (SMILES encoding, GCTx streaming, MCTS chemistry)
Phase 4: NF reversal screen (selumetinib in top-100)
Phase 5: Package NF pseudoSpore
Phase 6: Deliver to Gonzales → Bin Chen intro → JOSS → CTF NDU
```

---

## Timeline

| Phase | Optimistic | Realistic |
|-------|-----------|-----------|
| Phase 0 (archaeology) | 2 days | 1 week |
| Phase 1 (reproduce) | 1 week | 2 weeks |
| Phase 2-4 (rebuild + NF screen) | 2 weeks | 4 weeks |
| Phase 5-6 (package + deliver) | 1 week | 2 weeks |
| **Total to NF pseudoSpore** | **4 weeks** | **9 weeks** |
| JOSS paper.md draft | +1 week | +2 weeks |

**Optimistic NF pseudoSpore:** Late September 2026
**Realistic NF pseudoSpore:** November 2026

---

## Checklist

- [ ] Phase 0 directory created: `gonzales/gps/phase0/`
- [ ] Zenodo artifacts inventoried
- [ ] Dependency graph mapped
- [ ] Data lineage traced
- [ ] Paper lineage documented
- [ ] Phase 0 README written
- [ ] Phase 1 validation targets confirmed
- [ ] Legacy Docker reference running
- [ ] tideGlass cell booted on westGate
- [ ] RGES module validated (first Tier 1 result)
