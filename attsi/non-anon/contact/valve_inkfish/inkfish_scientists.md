# Inkfish Scientists — Profiles for Outreach

These are the scientists most likely to understand what ecoPrimals offers
and evaluate whether it fits their data pipeline. The goal is not to
cold-email all of them — it's to CC Dr. Bongaerts on the letter to Gabe,
and to be ready if Gabe forwards internally.

---

## Dr. Pim Bongaerts — Lead Scientist, Inkfish Expeditions

**Title**: McCosker Chair of Aquatic Biology, Curator of Invertebrate Zoology
**Institution**: California Academy of Sciences (San Francisco)
**Also**: Associate Professor, San Francisco State University; Associate Scientist, CARMABI Research Institute
**Lab**: Reefscape Genomics Lab (reefscapegenomics.com)
**LinkedIn**: linkedin.com/in/bongaerts
**ORCID**: Check Google Scholar profile
**Location**: Warkworth, Auckland, New Zealand
**Education**: PhD Biology (U. Queensland, 2011), MSc Limnology & Oceanography (U. Amsterdam, 2006), BSc Biology (Utrecht, 2004)
**Publications**: 100-150 scholarly works

### Research Focus
- Mesophotic coral ecosystems (30-150m depth) — the "twilight zone" of reefs
- Molecular ecology: genomics + field ecology to understand coral diversification
- "Deep reef refugia" hypothesis — can deep reefs replenish shallow reefs?
- Genetic patterns "across the reef slope" (over depth)
- Cross-species comparisons between shallow and mesophotic environments

### Inkfish Involvement
- **Lead scientist** on multiple Inkfish expeditions:
  - Solomon Islands Leg 3 (2025) — mesophotic coral around Rennell Island
  - Samoa Expedition Leg 2 (2025) — mesophotic reefs around Savai'i
  - Curaçao Expedition (2023) — coastal seas program
- Methods: closed-circuit rebreather diving + AUV surveys → 3D photogrammetric models
- Data: >1,200 coral tissue samples geo-referenced within 3D models for genome sequencing
- Submersible dives to 300m to investigate lower depth limits of photosynthetic corals

### Why He Matters for ecoPrimals
- **Generates massive genomic datasets** from expeditions — exactly what barraCuda/wetSpring processes
- **Field biologist who understands compute constraints** — processing data on vessels with limited connectivity
- **Open science**: all Inkfish data goes to open repositories
- **Molecular ecologist**: overlaps with Kevin's microbiology background (microbial communities in coral holobionts)
- **Dutch-Australian-NZ**: international, collaborative, accessible on LinkedIn

### Compute Relevance
His lab sequences >1,200 coral genomes per expedition. Current pipeline likely:
- Sample collection → preservation → shore-side DNA extraction → sequencing facility
- Data return → HPC cluster for alignment, assembly, phylogenetics
- Photogrammetry: AUV imagery → 3D reconstruction (GPU-intensive)

ecoPrimals could offer:
- On-vessel preliminary analysis via barraCuda (any Vulkan GPU)
- Content-addressed storage for provenance chains (sample → sequence → analysis)
- Mesh networking for ship-to-shore data sync (songBird)

---

## Stu Buckle — New Builds & Special Projects, Inkfish

**Role**: Oversees RV6000 and RV11000 vessel design and construction
**Quote**: "This next-generation vessel builds on earlier designs to deliver
significantly greater capability, flexibility, and reach to enable science."

### Why He Matters
- Decision-maker for onboard technology infrastructure
- Bridges science requirements with engineering implementation
- If Inkfish were to evaluate onboard compute solutions, Stu would be involved
- The RV11000 spec includes "dedicated working spaces, laboratories, and workshops"
  plus IACS cybersecurity certification — sovereign compute aligns with this

---

## Edd Stockdale — Advanced Diving Research & Technology, Inkfish

**Role**: Dive operations management, safety, logistics for remote expeditions
**Expertise**: Technical diving (advanced to occupational scientific levels),
integration of underwater data-gathering technologies
**Previously**: Marine field station work in Indonesia (2011+), Ocean Census dive contractor

### Why He Matters
- Technology integration specialist for remote operations
- Understands the constraints of fieldwork: connectivity, power, durability
- Could evaluate songBird mesh for dive team coordination

---

## Supporting Scientists (Expedition Team)

| Person | Role | Expedition |
|--------|------|-----------|
| **Norbert Englebert** | Senior Technician, Dive Safety Officer (Reefscape Genomics) | Solomon Islands Leg 3 |
| **Dr. Ale Hernandez** | Marine scientist, rebreather diver | Solomon Islands |
| **Jenn Thomson** | Expedition logistics, scientific diving, web design | Solomon Islands Leg 4, multiple |
| **Zuzu Askin** | NatGeo explorer, OWUSS Rolex Scholar, Inkfish contractor | Trans-Pacific Transit |
| **Francesca "Franny" Krysiak** | Expedition diver, photographer | Solomon Islands Leg 3 |

---

## Adjacent Organizations

| Organization | Connection | Key Person |
|-------------|-----------|-----------|
| **Ocean Census** | Nippon Foundation + Nekton, 1,500+ scientists | Dr. Alex Rogers (Science Director, Oxford), Michelle Taylor (Head of Science) |
| **California Academy of Sciences** | Bongaerts' home institution | — |
| **British Geological Survey** | Collaborated with Inkfish on RV Dagon Trans-Pacific | — |
| **CSIRO** | Coral Sea Marine Park expedition partner | — |
| **Schmidt Ocean Institute** | Ocean Census expedition partner, species discovery workshops | — |

---

## Data Pipeline Analysis (Speculative)

Based on published expedition reports, Inkfish's science data pipeline likely:

```
Field collection (rebreathers, submersibles, AUVs, ROVs)
  → Tissue samples preserved in ethanol/RNAlater
  → AUV imagery (terabytes per dive day)
  → CTD casts, water samples, sediment cores
  → Onboard: preliminary sorting, cataloging, photography
  → Shore transfer: physical samples → sequencing facility
  → Data transfer: imagery → cloud or institutional HPC
  → Analysis: alignment, assembly, phylogenetics, 3D reconstruction
  → Publication: open-source repositories + papers
```

**Compute bottlenecks**:
1. AUV photogrammetry (3D reconstruction) — GPU-intensive, currently shore-side
2. Genomic analysis — typically requires HPC, delays results by weeks/months
3. Data integrity — how to maintain provenance across ship/shore/lab boundaries
4. Connectivity — multi-month expeditions with limited bandwidth

**ecoPrimals solution fit**:
1. barraCuda: GPU-accelerated analysis on vessel hardware (any Vulkan GPU)
2. nestGate: content-addressed storage with deduplication (6 PDBs in CAS proven)
3. sweetGrass: cryptographic provenance (sample → sequence → analysis chain)
4. songBird: mesh networking for disconnected operation and sync-on-reconnect
5. cellMembrane: deployment automation for non-technical vessel crew

---

*Profiles compiled July 29, 2026. Sources: LinkedIn, California Academy of Sciences,
VARD press releases, expedition blog posts, Reefscape Genomics Lab website.*
