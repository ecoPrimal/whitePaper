# sporePrint — Live Science as Public Surface

**Status**: Living document — shapes the public web presence
**Wave**: 155m | **Date**: Jul 30, 2026

---

## The Thesis

sporePrint is not a marketing site. It's a **presentation of subGen to the world** —
the project's operational truth, rendered as verifiable evidence. The site should
show live science running on sovereign infrastructure, and then offer a pseudoSpore
of it: clone it, run it, verify it, grow from it.

The current site (Wave ~150) presents ecoPrimals as a scientific computing platform.
The Wave 155m reality is much stronger: 3 NUCLEUS gates, Provenance 7/7 validated,
Sovereign CI live, cross-platform proven. The site needs to reflect achieved reality,
not promised architecture.

---

## Design Principle: Science First, Then Infrastructure

The visitor flow should be:

```
1. See live science (hotSpring QCD, footPrint GIS, wetSpring genomics)
2. Notice it's running on commodity hardware (no cloud, no CUDA)
3. Grab a pseudoSpore of it (clone, validate, grow)
4. Discover the infrastructure underneath (primals, provenance, mesh)
```

NOT:

```
1. See infrastructure architecture
2. Trust that science runs on it
3. Maybe find evidence somewhere
```

---

## Live Science Surfaces — What We Can Show

### hotSpring → petalTongue: Lattice QCD Visualization

Dynamic WebGL visualization of lattice gauge theory running on consumer GPUs.
Not a static image — the simulation is live, petalTongue renders it in real-time,
the physics is happening in the background via toadStool GPU dispatch.

**What it proves**: Real physics, real GPU, real-time, no CUDA, on your browser.

### footPrint: Live GIS Data Acquisition

Geographic data system running at `primals.eco/footprint/`. Shows real locations,
real sensor data, real acquisition challenges. The visitor sees science problems
(data gaps, calibration issues) being solved by location — not abstract demos.

**What it proves**: The mesh handles real-world data at geographic scale.

### esotericWebb: Graphics Engine Challenge

The game engine / creative surface that pushes petalTongue's WebGL pipeline.
Scene binding, real-time composition of visual elements. This challenges the
rendering infrastructure and proves it handles creative workloads too.

**What it proves**: The same GPU infrastructure that does QCD also does real-time graphics.

### wetSpring: Genomics Pipeline

GPU-accelerated 16S rRNA pipeline. Real NCBI data (11.9M paired-end reads).
Python → Rust parity at machine-epsilon precision. This is the flagship evidence.

**What it proves**: Production bioinformatics on commodity hardware, no cloud.

---

## The PseudoSpore Pattern on the Web

Every live science surface should offer a **pseudoSpore grab**:

```
┌─────────────────────────────────────────┐
│  You're watching: lattice QCD on GPU    │
│                                          │
│  [Grab PseudoSpore]                     │
│  → Downloads: data + code + provenance   │
│  → `./validate` proves it works          │
│  → You now own this science              │
└─────────────────────────────────────────┘
```

This is the gen5 thesis in action: someone else's science comes out the other end.
The website IS the demonstration of that thesis.

---

## Site Architecture — Inter/Intra Membrane

The site itself should reflect the K-Derm topology:

### Outer Membrane (public, no auth)
- `primals.eco` / `sporeprint.primals.eco` — evidence record, science showcase
- `footprint.primals.eco` — live GIS
- `live.primals.eco` — mesh topology visualization (esotericWebb)

### Periplasmic Space (reviewer access)
- `lab.primals.eco` — JupyterHub, notebooks, interactive compute
- Evidence pages with deeper provenance chains visible

### Inner Membrane (mesh-only, authenticated)
- Gate-to-gate IPC, Neural API, BTSP communications
- Not visible from outside — but the RESULTS are visible on outer membrane

The public surface shows what the inner membrane produces. The provenance chain
bridges them: "this result was computed on strandGate RTX 3090, signed by bearDog,
committed to loamSpine, attributed via sweetGrass — here's the braid ID."

---

## Updates Needed (from 155m audit)

### Headlines to Add
- "3 NUCLEUS gates live. Provenance 7/7 validated. 3 operating systems."
- "Push-to-deploy: Sovereign CI builds, signs, and publishes — zero cloud."
- "34 genomeBins across 5 targets. BLAKE3 verified. One depot."

### Content Fixes
- Replace `coralForge` with `helixVision` in comparison table
- Update hardware: multi-gate (EPYC + Ryzen + RTX 3090 + RTX 4070)
- Add "Living Deployment" section showing actual running NUCLEUS
- Add Provenance Trio as headline feature (not just pipeline diagram)

### New Pages Needed
- **Living Systems (refresh)** — 3 NUCLEUS gates, Sovereign CI, depot status
- **Provenance Trio** — dedicated page explaining 7-step chain with evidence
- **Cross-Platform** — "Same binary. Same provenance. Linux, Windows, Android."
- **PseudoSpore** — what it is, how to grab one, how to validate it

### sporePrint Impulses (blog posts)
1. "Achieving NUCLEUS" — first lifecycle-managed deployment from depot
2. "Provenance 7/7" — the full signed chain on live hardware
3. "Sovereign CI" — push-to-deploy without cloud
4. "Cross-Platform Proof" — same provenance chain on Linux and Windows
5. "The $485/month Mesh" — what 10+ gates cost to run

---

## Supporting Teams

| Team | Role | Gate |
|------|------|------|
| **sporePrint** | Site design, Zola templates, content pages, SEO | golgiBody |
| **projectFOUNDATION** | Knowledge layer, thread lineage, structured evidence | TBD |
| **projectNUCLEUS** | Full NUCLEUS product packaging, pseudoSpore delivery | TBD |
| **petalTongue** | WebGL/WASM rendering for live science visualizations | westGate |
| **esotericWebb** | Graphics engine, scene composition, creative surface | flockGate |
| **footPrint** | GIS data acquisition, location-based science | flockGate |

---

## Sequencing

```
Phase 1 (now):    Update site content to Wave 155m reality (text changes)
Phase 2 (next):   Live science surfaces (hotSpring QCD viz, footPrint, wetSpring)
Phase 3 (gen5):   PseudoSpore grab pattern (NF as first downloadable artifact)
Phase 4 (mature): projectFOUNDATION feeds site automatically from provenance
```

Phase 1 is a sporePrint team handoff. Phases 2-4 require cross-team coordination
and live data flowing through the Nest Atomic pipeline.

---

*subGen Wave 155m — sporePrint is subGen presented to the world. Live science first,
pseudoSpore grab second, infrastructure discovery third. The site needs to reflect
achieved reality (NUCLEUS, Provenance 7/7, Sovereign CI, cross-platform). Supporting
teams: sporePrint (design), projectFOUNDATION (knowledge), projectNUCLEUS (packaging),
petalTongue (rendering), esotericWebb (graphics), footPrint (GIS).*
