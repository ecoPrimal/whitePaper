# Outreach Status — Active Contact Tracks

**Status**: Living document — updated on contact events
**Wave**: 155i | **Date**: Jul 29, 2026

---

## Active Tracks

### 1. Valve / Inkfish — Gabe Newell

| Field | Value |
|-------|-------|
| **Status** | **EMAIL SENT** |
| **Date sent** | Jul 29, 2026 |
| **Recipient** | gaben@valvesoftware.com |
| **Version** | v3 (scientist-first, no ask, identity reveal) |
| **Pitch** | Microbiologist who brings his own compute. Parallel sovereignty thesis. 19-year Steam member. |
| **Science** | Marine microbiome, eDNA, coral holobionts — "I see the organisms inside the organisms your team collects" |
| **Products offered** | barraCuda (Vulkan field genomics), nestGate (BLAKE3 provenance), songBird (ship-to-shore mesh) |
| **Infrastructure parallel** | Own vessels/own gates, Vulkan/Vulkan, open data/AGPL, fleet/mesh |

**What's stronger now than when v3 was drafted:**

- barraCuda validated on real silicon: RTX 3090 FP64 ~104 TFLOPS, FHE bit-perfect, 4,957/4,957 tests
- 9-gate mesh (was ~4–5), composition broker LIVE (704 capabilities)
- Node Atomic validated: 746 pipelines/sec, sub-ms GPU dispatch
- Nest Atomic on Windows (blueGate 10/10) — proves cross-platform deployment
- ~63K+ tests across primals (was ~105K across ecosystem)

**Response protocol:**

| Scenario | Timeline | Action |
|----------|----------|--------|
| Gabe responds | Within days–weeks | Engage directly. Offer demo dataset. Be the scientist, not the vendor. |
| Gabe forwards to Pim | Within weeks | Follow Pim's lead. Prepare coral holobiont data demo. |
| Silence at 2 weeks | Aug 12, 2026 | LinkedIn warm engagement with Pim Bongaerts. Publish Inkfish-relevant demo dataset. |
| Silence at 4 weeks | Aug 26, 2026 | Direct email to Pim (scientist-to-scientist). Reference Gabe email if appropriate. |
| Silence at 8 weeks | Sep 23, 2026 | Evaluate RV6000 timeline (Q2 2028). Consider Ocean Census / Cal Academy paths. |

**Pre-send checklist status:**

- [x] Email draft v3 reviewed
- [x] Steam ID verified (76561198002558137)
- [ ] LinkedIn profile populated (secondary — not blocking)
- [ ] Inkfish demo dataset published (secondary — follow-up material)
- [ ] PADI certification current (verify for expedition readiness)

**Supporting docs:** `attsi/non-anon/contact/valve_inkfish/`

---

### 2. Andrea Gonzales — NF Drug Discovery / tideGlass

| Field | Value |
|-------|-------|
| **Status** | **PRODUCING** (relationship active, code not started) |
| **First contact** | RA III at MSU |
| **Assignment date** | Jun 5, 2026 (GPS rebuild assigned) |
| **Relationship** | Domain expert collaborator. PI on CTF NDU ($125K). |
| **Science** | NF1 RAS/MAPK, JAK/STAT bridge, GPS Cell 2026 (Bin Chen Lab) |
| **Product** | tideGlass — first protoKarya lens. 7-module GPS rebuild → lithoSpore USB. |
| **Infrastructure** | Forces: SMILES encoding, GCTx streaming, MCTS, statistical tolerances |
| **Grant** | CTF NDU: $50K Y1 bioinformatics + $75K Y2 wet lab. Andrea PI, Kevin compute. |

**Critical path:**

```
bearDog crypto.sign_ed25519 (P1)
    → Provenance Trio 7/7
        → tideGlass Phase 0 (GPS archaeology)
            → NF Data Portal ingestion
                → One NF pseudoSpore
                    → JOSS draft / CTF NDU prelim data
```

**Phase status:**

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Archaeology — Zenodo, deps, data trace | NOT STARTED |
| 1 | Reproduce — RCL, GPS4Drug, figures | BLOCKED on Phase 0 |
| 2 | Validate — cross-validate vs LINCS/ChEMBL | BLOCKED on Phase 1 |
| 3 | Rebuild sovereign — Rust/Python modern | BLOCKED on Phase 2 |
| 4 | Package — pseudoSpore, lithoSpore USB | BLOCKED on Phase 3 |

**Data readiness:** T1 ~35 GB (reproduction), T2 ~49 GB (validation), T3 ~317 GB (archaeology). Not yet downloaded.

**Bin Chen intro:** Offered by Andrea, pending. USB lithoSpore is the handoff artifact.

**Supporting docs:** `attsi/non-anon/contact/gonzales/gps/`

---

### 3. Jeff Jones — PFAS / blueFish

| Field | Value |
|-------|-------|
| **Status** | **EMERITUS CONSULTING** |
| **Science** | EPA 1633A PFAS LC-MS/MS QC. Chromeleon replacement. |
| **Product** | blueFish — open PFAS QC tool |
| **Data** | Two May 2026 data dumps received |
| **Spring** | wetSpring Track 2 (40/40 checks) |
| **Next** | Jones retired. On-campus successors: Ilango, Murphy, Kumar. |
| **Supporting docs** | `gen5/collaborators/JONES_BLUEFISH.md` |

---

### 4. Jeff Barrick — LTEE / lithoSpore

| Field | Value |
|-------|-------|
| **Status** | **USB DELIVERED** |
| **Science** | Lenski LTEE frozen stocks, microbial evolution |
| **Product** | lithoSpore v0.1.0 — 4 USBs delivered May 18, 2026 |
| **Artifact** | 7 modules, 75 checks, ~200 MB, exFAT |
| **Next** | Awaiting Barrick lab response. lithoSpore chassis validates gen4 guideStone. |

---

### 5. ABG (Anderson Biology Group)

| Field | Value |
|-------|-------|
| **Status** | **PRODUCING** |
| **Science** | Whole-cell expression (Karr 2012 → Thornburg 2026) |
| **Product** | initioChem pseudoSpore |
| **Infrastructure** | JupyterHub LIVE at `lab.primals.eco` |
| **Next** | First foundation thread. initioChem → guideStone → pseudoSpore. |

---

### 6. MSU Faculty Network

| Field | Value |
|-------|-------|
| **Status** | **CONTACTED / MAPPED** |
| **Contacts** | Murillo (neuromorphic), Kachkovskiy (math/spectral), Eaves (anthro), Chuna (physics/LANL) |
| **Spring links** | neuralSpring, hotSpring, healthSpring |
| **Next** | Faculty profiles in gen3 `FACULTY_SPRING_PROFILES`. No active deliverables pending. |

---

## Outreach Pipeline — Temporal View

```
        CONTACTED       ENGAGED        PRODUCING      PUBLISHED
            │               │               │              │
 Murillo ───┤               │               │              │
 Kachkovskiy┤               │               │              │
 Eaves ─────┤               │               │              │
 Chuna ─────┤               │               │              │
            │               │               │              │
 Barrick ───┼───────────────┤  USB delivered │              │
            │               │               │              │
 Jones ─────┼───────────────┤  data received │              │
            │               │               │              │
 Gonzales ──┼───────────────┼───────────────┤  GPS assigned │
            │               │               │              │
 ABG ───────┼───────────────┼───────────────┤  JupyterHub   │
            │               │               │              │
 Gabe ──────┼── EMAIL SENT  │               │              │
            │  Jul 29       │               │              │
```

**gen5 success metric**: At least one track reaches PUBLISHED — collaborator-owned science exits the ecosystem.

**Closest to PUBLISHED**: Gonzales/NF (if tideGlass Phase 0 starts) or ABG (if initioChem pseudoSpore ships).

---

*subGen Wave 155i — Outreach master tracker. Inkfish email SENT. Gonzales producing.
Six active tracks across marine biology, drug discovery, PFAS, microbial evolution,
whole-cell biology, and faculty network.*
