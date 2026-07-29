# Valve / Inkfish — Outreach Strategy

**Type**: Cold-warm hybrid — no personal connection, but deep alignment
**Organization**: Inkfish (marine research, est. 2021) + Valve Corporation (gaming)
**Owner**: Gabe Newell (co-founder of Valve, owner of Oceanco since Aug 2025)
**HQ**: Inkfish: Seattle, WA | 74 employees across 15 countries (+60% YoY)
**Domain**: Deep-sea exploration, mesophotic coral genomics, seafloor mapping, submersible ops

---

## Why This Contact

Gabe Newell is not "a billionaire with a yacht." He built a 74-person
philanthropic research organization that sends marine biologists on
multi-month expeditions with closed-circuit rebreathers, submersibles,
and AUVs — and contributes all data to open-source repositories.

The overlap with ecoPrimals is structural, not aspirational:

| Dimension | Inkfish/Valve | ecoPrimals |
|-----------|-------------|------------|
| Open data | All expedition data → open repositories | AGPL-3.0 + CC-BY-SA, open repos |
| GPU compute | Coral genome sequencing (>1,200 per expedition) | barraCuda/wetSpring: GPU-accelerated genomics |
| Infrastructure sovereignty | Building own vessels ($1B+ fleet) instead of chartering | Building own compute instead of renting cloud |
| Linux/Vulkan | Valve funded DXVK, VKD3D, NVK, Proton, SteamOS | ecoPrimals proved Vulkan works for science-grade GPU |
| Mesh networking | Ship-to-shore, vessel-to-vessel coordination | songBird sovereign mesh, Tower Atomic |
| Content-addressed storage | Petabytes of SONAR, spectral, genomic data | nestGate CAS, Nest Atomic LIVE |

The key angle: **a microbiologist who built sovereign genomics infrastructure
reaching out to marine biologists who generate genomic data on floating
research campuses**. This is a science conversation, not a tech pitch.

---

## Inkfish Fleet

| Vessel | Length | Status | Capacity |
|--------|--------|--------|----------|
| **RV Hydra** | — | Active | Currently in Solomon Islands (2025) |
| **RV Dagon** | — | Active | Trans-Pacific transit expeditions |
| **RV6000** | 100m | Under construction (VARD, delivery Q2 2028) | 70 crew+scientists |
| **RV11000** | 162m | Contracted May 2026 (€700M, delivery Q1 2030) | 130 crew+scientists |

RV11000 features: dual submersibles, ROV hangar (11,000m depth), 40m corer,
largest battery installation ever fitted on a ship (12hr silent sub ops),
IACS cybersecurity certified, laboratories and data-processing facilities.

---

## Key People

See individual profiles in this directory for detailed research backgrounds.

| Person | Role | Why Contact | Priority |
|--------|------|-------------|----------|
| **Gabe Newell** | Owner, Inkfish/Valve | Decision-maker. Shares infrastructure sovereignty thesis. | Primary |
| **Dr. Pim Bongaerts** | Lead Scientist, Inkfish expeditions | Mesophotic coral genomics — direct barraCuda/wetSpring user | Primary (CC) |
| **Stu Buckle** | New Builds & Special Projects | Ship design, science program direction | Secondary |
| **Edd Stockdale** | Advanced Diving Research & Technology | Technology integration, remote expedition logistics | Tertiary |

---

## The Pitch (Core Message)

**From**: eco Primal (eco.primal@pm.me → eco.primal@primal.eco when live)
**To**: Gabe Newell (gaben@valvesoftware.com or Inkfish contact)
**CC**: Dr. Pim Bongaerts (California Academy of Sciences)
**Subject**: Sovereign GPU genomics for Inkfish expeditions — from a microbiologist

Three concrete offers:

1. **GPU-accelerated coral genomics on expedition hardware**: barraCuda runs
   DADA2/16S/metagenomic pipelines on any Vulkan GPU. No CUDA, no cloud.
   Process >1,200 coral genome samples on a laptop-class GPU aboard RV Hydra
   instead of waiting for shore-side HPC time.

2. **Sovereign data pipeline for open-source contributions**: nestGate
   content-addressed storage with cryptographic provenance (sweetGrass/loamSpine).
   Every sample, every sequence, every measurement gets a BLAKE3 hash and
   attribution chain. Inkfish's open-data commitment gets cryptographic teeth.

3. **Mesh networking for vessel operations**: songBird sovereign mesh for
   ship-to-shore data sync, vessel-to-vessel coordination, and disconnected
   operation. Tower Atomic runs on everything from RTX 5090 to 30MB RSS
   edge devices — including the kind of embedded hardware on research vessels.

---

## What Kevin Brings (as a Microbiologist)

- BS Microbiology, MS Data Science
- Built the DADA2 GPU pipeline that reproduces published 16S results
- Reproduced 63 papers computationally (wetSpring validation)
- Understanding of microbial community dynamics applicable to:
  - Marine microbiome (coral holobiont, deep-sea chemosynthetic communities)
  - Environmental DNA (eDNA) from water column sampling
  - Metagenomics from sediment cores
- Can speak to the biology AND the infrastructure — rare combination

---

## Approach

1. **Research phase** (NOW): Profile Inkfish scientists, understand their
   data pipelines, identify specific computational pain points
2. **Draft phase**: Write a letter that leads with microbiology, not
   infrastructure. The letter should read like "I'm a microbiologist who
   built compute tools that could help your marine genomics program"
3. **Validation prerequisite**: wetSpring JOSS submission or barraCuda
   crates.io release adds credibility
4. **Send**: Email to gaben with Pim Bongaerts in CC. Short, concrete,
   with links to reproducible evidence. Human response guaranteed.

---

## Timing

Medium priority. Send after:
- [ ] barraCuda or wetSpring has a published release (crates.io, JOSS, or Zenodo)
- [ ] ecoPrimal LinkedIn profile is established
- [ ] The Inkfish Samoa expedition data is published (validates their pipeline)
- [ ] Draft letter is reviewed by attsi for tone

The approach is strongest when it includes:
- "I reproduced 63 published 16S papers on consumer GPUs"
- "The pipeline runs without CUDA — any Vulkan GPU, including mobile"
- "All code is AGPL-3.0, all data is CC-BY-SA — same open commitment as Inkfish"

---

## Personal Connection

Kevin is a Steam user since the Orange Box (2007) — Steam ID
76561198002558137. ~19 years on the platform. This is not a cold
contact from someone who Googled Valve. This is a community member
who grew up on Steam, became a microbiologist, built sovereign
compute in Rust on the same Vulkan substrate Valve championed,
and realized the person funding the science he wants to do is the
same person who built the platform he's been gaming on since he
was a teenager.

The connection between Valve and ecoPrimals isn't manufactured.
Kevin chose Vulkan for GPU compute because it was the only
vendor-neutral substrate. Valve funded Vulkan's ecosystem for
the same reason. The convergence is independent.

## Risk

Low-medium. Gabe Newell is known for responding to thoughtful emails
(his gaben@valvesoftware.com is famously accessible). Pim Bongaerts is
active on LinkedIn and appears approachable about research collaborations.

Worst case: no response.
Best case: Inkfish tests barraCuda/wetSpring pipeline on expedition data,
publishes results, provides independent validation. Potential compute
partnership for RV6000/RV11000 onboard labs.

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — strategy and contact map |
| `inkfish_scientists.md` | Detailed profiles of key Inkfish scientists |
| `email_draft_gaben.md` | Draft outreach letter |
| `EXPEDITION_DATA_ANALYSIS.md` | Analysis of Inkfish data pipeline and compute needs |

---

*Contact directory created July 29, 2026. Outreach pending published release + letter draft.*
