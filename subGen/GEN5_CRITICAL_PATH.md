# gen5 Critical Path — From Here to External Science

**Status**: Living document — the single chain to gen5 success
**Wave**: 155i | **Date**: Jul 29, 2026

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

### Step 1: bearDog `crypto.sign_ed25519`

**Owner**: bearDog code team
**Status**: Returns health stub. Method exists. Real Ed25519 signing not wired.
**Blocks**: Provenance Trio step 3b — `entry.append` fails without real signature.
**Effort**: Moderate — bearDog has 11,993 tests, crypto infrastructure extensive.
**P1 since**: Wave 155f

### Step 2: Provenance Trio 7/7

**Owner**: westGate validation (rhizoCrypt, loamSpine, sweetGrass teams)
**Status**: 6/7 steps pass on westGate. Step 3b (`entry.append`) fails on bearDog stub.
**Evidence**: westGate AAR confirms all other steps operational. sweetGrass v0.8.0, G3 E2E validated.
**Depends on**: Step 1

### Step 3: tideGlass Phase 0

**Owner**: eastGate (overwatch directs; dedicated gate for compute TBD)
**Status**: NOT STARTED
**Data**: T1 ~35 GB from Zenodo, GEO, ChEMBL, ZINC
**Gate**: biomeGate was specified in GPS docs (256 GB RAM, 96 GB VRAM). Alternatives: westGate, strandGate.
**Depends on**: Independent of Steps 1-2 (can start now)
**Supporting docs**: `attsi/non-anon/contact/gonzales/gps/README.md`, `DATA_MANIFEST.md`

### Step 4: tideGlass Phase 1

**Owner**: tideGlass code team (to be spun up)
**Status**: BLOCKED on Phase 0
**Validation targets**: RCL SNR >1.5x, GPS4Drug R² within 5%, RGES r=0.52±0.05, MCTS IC50 fold >4x
**Depends on**: Step 3

### Step 5: NF Data Portal Ingestion

**Owner**: westGate Nest Atomic team
**Status**: Data cataloged (`PUBLIC_DATA_SYSTEMS.md`), not downloaded
**Pipeline**: NF Portal → download → nestGate `content.put` → BLAKE3 → rhizoCrypt DAG → sweetGrass braid
**Depends on**: Steps 1-2 (for full provenance) + Step 3 (for context)
**Can start partially**: Data download is independent. Full provenance needs Step 2.

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

- Windows depot rebuild (P1 but not gen5 critical)
- Windows CI gate (systemic P1 but not gen5 critical)
- biomeOS graph executor riboCipher fix (P2)
- blueGate Node Atomic (gen4 extension)
- swiftGate Tower Atomic (gen4 extension)
- AlphaFold bulk ingestion (gen5 secondary after NF)
- Show HN (blocked on multiple items; deferred until NF pseudoSpore exists)
- Inkfish collaboration (separate track, response-dependent)

---

*subGen Wave 155i — gen5 critical path. 8 steps from bearDog crypto to JOSS.
Steps 1 and 3 can start today in parallel. Optimistic: pseudoSpore by Oct 2026.
Realistic: Jan 2027. Infrastructure is ready. The science pipeline is the bottleneck.*
