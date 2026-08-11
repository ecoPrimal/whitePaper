# gen5 Critical Path — From Here to External Science

**Status**: Living document — the single chain to gen5 success
**Wave**: 155f | **Date**: Aug 3, 2026

---

## The gen5 Question

> Does someone else's science come out the other end?

One chain answers this. Everything else is supporting work.

---

## The Chain

```
 ┌─────────────────────────────────────────────┐
 │  1. bearDog crypto.sign_ed25519             │ ← P1, blocks Provenance 7/7
 │     Real Ed25519 signing, not health stub   │
 └──────────────────┬──────────────────────────┘
                    │
 ┌──────────────────▼──────────────────────────┐
 │  2. Provenance Trio 7/7                     │ ← Currently 6/7
 │     loamSpine entry.append succeeds         │    Step 3b (bearDog sig) fails
 │     Full chain: nestGate → rhizoCrypt →     │
 │     loamSpine → sweetGrass                  │
 └──────────────────┬──────────────────────────┘
                    │
 ┌──────────────────▼──────────────────────────┐
 │  3. tideGlass Phase 0 — Archaeology         │ ← NOT STARTED
 │     Download Zenodo v5/v6 (~35 GB T1)       │    ~1-2 weeks
 │     Map GPS Python 2/3 dependencies         │
 │     Trace data lineage through LINCS/ChEMBL │
 │     Run original Docker as reference        │
 └──────────────────┬──────────────────────────┘
                    │
 ┌──────────────────▼──────────────────────────┐
 │  4. tideGlass Phase 1 — Reproduce           │ ← ~2-4 weeks
 │     RCL on VCAP_t1 (SNR improvement)        │
 │     GPS4Drug inference (expression pred)    │
 │     Figure data reproduction (HCC/IPF)      │
 │     MolSearch MCTS (IC50 4µM→0.5µM)        │
 └──────────────────┬──────────────────────────┘
                    │
 ┌──────────────────▼──────────────────────────┐
 │  5. NF Data Portal Ingestion                │ ← ~1-2 weeks
 │     Download NF disease signatures (~5 GB)  │
 │     Ingest through Nest Atomic pipeline     │
 │     Content-address in nestGate CAS         │
 │     Provenance Trio traces each object      │
 └──────────────────┬──────────────────────────┘
                    │
 ┌──────────────────▼──────────────────────────┐
 │  6. NF Reversal Screen                      │ ← ~2-4 weeks
 │     RGES scoring against LINCS              │
 │     ZINC compound screening                 │
 │     Anderson d_eff tissue geometry           │
 │     MEK inhibitors in top-100 (selumetinib) │
 └──────────────────┬──────────────────────────┘
                    │
 ┌──────────────────▼──────────────────────────┐
 │  7. One NF PseudoSpore                      │ ← THE gen5 ARTIFACT
 │     Self-verifying USB artifact             │
 │     Andrea Gonzales can run ./validate      │
 │     Bin Chen can review                     │
 │     Contains: data + code + provenance      │
 └──────────────────┬──────────────────────────┘
                    │
          ┌─────────┴─────────┐
          │                   │
 ┌────────▼────────┐ ┌───────▼────────┐
 │  8a. JOSS       │ │  8b. CTF NDU   │
 │  paper.md       │ │  Prelim data   │
 │  Live system    │ │  $125K grant   │
 │  usage section  │ │  Andrea PI     │
 │  ORCID/co-auth  │ │  Kevin compute │
 └─────────────────┘ └────────────────┘
```

---

## Step-by-Step Status

### Step 1: bearDog `crypto.sign_ed25519` — **COMPLETE**

**Owner**: bearDog code team
**Status**: ~~Returns health stub.~~ **SHIPPED** (`3739e7078`) — real Ed25519 signing live.
**Completed**: Wave 155j (Jul 29, 2026)

### Step 2: Provenance Trio 7/7 — **COMPLETE**

**Owner**: westGate + blueGate validation
**Status**: ~~6/7 steps pass.~~ **7/7 COMPLETE** — E2E validated on westGate (Linux/ZFS) + blueGate (Windows).
**Evidence**: Full signed provenance chain: CAS → DAG → Merkle → Spine → Ed25519 → Attribution braid.
**DID key**: `did:key:z6Mkryaa7n6hfpSbGaZwbqPMD6MzXukgdQK3XRKzwFSgce8o`
**Completed**: Wave 155k (Jul 30, 2026)

### Step 3: tideGlass Phase 0 — **NEXT**

**Owner**: eastGate (overwatch directs; dedicated gate for compute TBD)
**Status**: NOT STARTED — **FULLY UNBLOCKED** (Steps 1-2 complete, all 7 module datasets on ZFS)
**Data**: **482 GB across 7 modules on westGate ZFS with 100% provenance** — ChEMBL 37, PubChem, ZINC, BindingDB, GPS Platform v5+v6 (Zenodo), LINCS L1000, GTEx, GEO SOFT (15 series), PDB mmCIF, PDB70, AlphaFold v6 (42 proteomes), Pfam-A, InterPro, MONDO, Reactome, HPO, DO, KEGG, Open Targets, TCGA (full GDC + Xena), COSMIC v104, ClinVar, gnomAD, RefSeq, NCBI Gene (7 files), UniProt (SP+TrEMBL+isoforms), Ensembl, GENCODE, STRING, BioGRID, NF Data Portal (Synapse)
**Gate**: westGate (ZFS 50.7TB, Nest Atomic live, Provenance 7/7) or strandGate (RTX 3090, NUCLEUS)
**Depends on**: Independent — can start immediately
**Supporting docs**: `attsi/non-anon/contact/gonzales/gps/README.md`, `DATA_MANIFEST.md`, `subGen/DATA_FEDERATION_STATUS.md`
**Note**: This is now the **sole bottleneck** for gen5. Infrastructure AND data are complete. GPS Platform v5+v6 scoring artifacts from Gonzales/Chen Cell 2026 are on ZFS.

### Step 4: tideGlass Phase 1

**Owner**: tideGlass code team (to be spun up)
**Status**: BLOCKED on Phase 0
**Validation targets**: RCL SNR >1.5x, GPS4Drug R² within 5%, RGES r=0.52±0.05, MCTS IC50 fold >4x
**Depends on**: Step 3

### Step 5: NF Data Portal Ingestion — **COMPLETE**

**Owner**: westGate Nest Atomic team
**Status**: **DONE** — 658 files (666 MB) downloaded from Synapse, 100% provenance
**Data on ZFS**: NF1 HTS drug screening (8K compounds), 595 dose-response curves, NF2 Synodos kinomics (peptide/protein/differential), NF2 drug screen processed data
**Completed**: Wave 155f (Aug 2, 2026)

### Step 6: NF Reversal Screen

**Owner**: tideGlass code team + healthSpring
**Status**: BLOCKED on Steps 4-5
**Validation targets**: MEK inhibitors (selumetinib) in top-100 reversal compounds
**Anderson integration**: d_eff=2.4 nerve sheath geometry modulates RGES scoring
**Depends on**: Steps 4, 5

### Step 7: One NF PseudoSpore

**Owner**: lithoSpore + tideGlass
**Status**: BLOCKED on Step 6
**Format**: Self-verifying USB artifact. `./validate` runs all 7 modules.
**Recipient**: Andrea Gonzales → Bin Chen
**Depends on**: Step 6

### Steps 8a/8b: JOSS / CTF NDU

**Owner**: whitePaper / Gonzales
**Status**: Strategy defined. No draft. No submission.
**Depends on**: Step 7

---

## Parallelizable Work

Steps 1 and 3 are **independent**. Both can start immediately.

| Track | Steps | Can Start Now |
|-------|-------|---------------|
| **Provenance completion** | 1 → 2 | YES — bearDog team |
| **GPS archaeology** | 3 → 4 | YES — independent of provenance |
| **NF data download** | 5 (partial) | YES — download is independent |
| **Windows depot** | Parallel | YES — sporeGate/blueGate |
| **Windows CI** | Parallel | YES — eastGate |
| **Inkfish follow-up** | Parallel | WAITING — 2-week response window |

**The fastest path**: Start Steps 1 and 3 in parallel. Step 3 requires no
infrastructure work — it's downloading data and reading Python.

---

## Timeline (Optimistic / Realistic)

| Step | Optimistic | Realistic | Notes |
|------|-----------|-----------|-------|
| 1. bearDog crypto | 1 week | 2–3 weeks | Crypto infra exists, needs wiring |
| 2. Provenance 7/7 | +1 day | +1 week | Validation on westGate |
| 3. Phase 0 archaeology | 1–2 weeks | 2–3 weeks | Data download + dependency mapping |
| 4. Phase 1 reproduce | 2–4 weeks | 4–6 weeks | RCL + GPS4Drug + figures |
| 5. NF ingestion | 1–2 weeks | 2–3 weeks | Download + Nest Atomic pipeline |
| 6. NF screen | 2–4 weeks | 4–8 weeks | RGES + ZINC + Anderson |
| 7. PseudoSpore | 1 week | 2 weeks | Packaging + validation |
| 8. JOSS/CTF | 2–4 weeks | 4–8 weeks | Writing + co-author + submission |
| **Total** | **~10–14 weeks** | **~18–30 weeks** | From today to published |

**If Steps 1 and 3 start in parallel today**:
- Optimistic: NF pseudoSpore by mid-October 2026
- Realistic: NF pseudoSpore by January 2027
- JOSS submission: Q4 2026 (optimistic) or Q1 2027 (realistic)

---

## What This Does NOT Include

These are important but do not block the critical path:

- ~~Windows depot rebuild~~ — **DONE** (15/15, Sovereign CI live)
- ~~biomeOS graph executor riboCipher fix~~ — **DONE** (v4.50)
- ~~bearDog crypto.sign~~ — **DONE** (Step 1 complete)
- ~~Provenance 7/7~~ — **DONE** (Step 2 complete)
- steamGate (cross-platform expansion, gen4 extension)
- graftGate / iosGate (glacial, silicon deism)
- AlphaFold bulk ingestion (gen5 secondary — staged approach recommended, see `DATA_FEDERATION_STATUS.md`)
- Show HN (blocked until NF pseudoSpore exists)
- Inkfish collaboration (separate track, response-dependent)

---

## Revised Timeline (Wave 155m)

Steps 1 and 2 are **COMPLETE**. The remaining chain is Steps 3-8.

| Step | Optimistic | Realistic | Notes |
|------|-----------|-----------|-------|
| ~~1. bearDog crypto~~ | ~~1 week~~ | — | **DONE** (155j) |
| ~~2. Provenance 7/7~~ | ~~+1 day~~ | — | **DONE** (155k) |
| 3. Phase 0 archaeology | 1–2 weeks | 2–3 weeks | Data download + dependency mapping |
| 4. Phase 1 reproduce | 2–4 weeks | 4–6 weeks | RCL + GPS4Drug + figures |
| 5. NF ingestion | 1–2 weeks | 2–3 weeks | Download + Nest Atomic pipeline |
| 6. NF screen | 2–4 weeks | 4–8 weeks | RGES + ZINC + Anderson |
| 7. PseudoSpore | 1 week | 2 weeks | Packaging + validation |
| 8. JOSS/CTF | 2–4 weeks | 4–8 weeks | Writing + co-author + submission |
| **Total** | **~8–12 weeks** | **~16–28 weeks** | From today to published |

**If Step 3 starts today**:
- Optimistic: NF pseudoSpore by **late September 2026**
- Realistic: NF pseudoSpore by **December 2026**
- JOSS submission: Q4 2026 (optimistic) or Q1 2027 (realistic)

The critical path shortened by ~2-3 weeks vs 155i estimate because Steps 1-2 are done.

---

*subGen Wave 155f — gen5 critical path. Steps 1-2 COMPLETE (Provenance 7/7 live).
Step 5 COMPLETE (NF ingestion). 5 remaining steps from tideGlass Phase 0 to JOSS.
Step 3 can start immediately with 482 GB of tideGlass data including GPS Platform
scoring artifacts. 519 GB total sovereign data across 130 datasets. Infrastructure
is 100% ready. The science pipeline is the sole bottleneck.*
