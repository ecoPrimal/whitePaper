# initioChem

**Interactive Computational Chemistry: From Validated FEL to 3D Exploration on Your Hardware**

**Date**: May 28, 2026
**Status**: Seeded v0.1.0 — composition contract defined, seed binary compiles
**Organization**: [sporeGarden](https://github.com/sporeGarden/initioChem)
**Lineage**: hotSpring Exp 220 (CAZyme FEL) + pseudoSpore v1.7.0 + Paper 50 GPU shader → gen4
**ABG Link**: Project 3 (Alistaire) — conformational energy landscapes for CAZyme docking

---

## What It Is

initioChem is a sovereign interactive molecular research platform that composes
ecoPrimals infrastructure into a deployable tool for exploring conformational
free energy landscapes. It is not a spring — it does not reproduce published
science. It is a **product** — something a computational chemist uses to
visualize, compute, and share FEL results without cloud dependency.

Where esotericWebb proved the gen4 pattern for **creative** domains (game
engines), and helixVision proves it for **genomics**, initioChem proves it
for **computational chemistry**. Same primals, same PrimalBridge, same
graceful degradation — but the user sees 3D molecular surfaces and energy
landscapes instead of a game loop or a genomics pipeline.

---

## The Pipeline

```
Substrate structure (PDB/GRO)
  → initioChem pipeline:
      ├── hotSpring MD engine (GROMACS+PLUMED or sovereign GPU kernels)
      ├── FES reconstruction (GPU Gaussian summation, Paper 50 shader)
      ├── Cross-landscape comparison (free vs enzyme-bound)
      ├── Binding distance monitoring (substrate dissociation detection)
      ├── Kolmogorov-Smirnov validation (COLVAR distribution testing)
      └── Provenance (trio: experiment → analysis → results → pseudoSpore)
  → Visualization (petalTongue: 3D molecules, FEL surfaces, Cremer-Pople sphere)
  → All on sovereign hardware, no cloud, no vendor lock-in
```

---

## Science Source: hotSpring

initioChem composes validated science from hotSpring:

| Capability | Experiment | What It Provides |
|-----------|------------|-----------------|
| FES reconstruction | Exp 220 + Paper 50 | GPU-accelerated Gaussian summation (11-14×, RMSD 1e-14) |
| Cross-landscape analysis | cazyme-fel crate | Free vs enzyme-bound comparison, RMSD, difference maps |
| Artifact detection | nest-validate | Binding distance, KS test, substrate dissociation alerts |
| Derivation Anchoring | v1.7.0 standard | Zero magic numbers — 23 constants, 5-layer empirical chain |
| Metadynamics pipeline | GROMACS+PLUMED | Well-tempered metadynamics with Cremer-Pople CVs |
| pseudoSpore packaging | nest-validate deploy | GuideStone-grade reproducible artifacts (190/190 checks) |

hotSpring has 500+ quantitative checks across 229 experiments. The CompChem
FEL pipeline is the most recent: 190/190 PASS, Derivation Anchoring enforced.

---

## ABG Connection (Project 3: Alistaire)

initioChem is the product layer for ABG Project 3:

**Core Question**: Can AutoDock Vina molecular docking serve as a cheap
surrogate for full FEL calculations in predicting catalytically competent
sugar geometries inside CAZyme active sites?

**What exists**: pseudoSpore v1.7.0 with 16 FEL landscapes (free β-D-xylopyranose,
enzyme-bound GH10, 4 epimers, multi-subsite, GH11), delivered to Alistaire
May 2026. 190/190 automated validation checks.

**What initioChem adds**: Instead of shipping TOML files and static PNGs,
Alistaire (and future collaborators) can:
- Rotate the Cremer-Pople sphere in 3D and see energy basins
- Click a conformation and see the ring shape + energy
- Compare free vs enzyme-bound side-by-side with animated interpolation
- Launch new simulations from the GUI (new GH families, new substrates)
- Share results as provenance-sealed pseudoSpores

---

## Primals Consumed via IPC

| Primal | Domain | Role in initioChem |
|--------|--------|-------------------|
| toadStool | compute | GPU dispatch for FES reconstruction, parameter sweeps |
| coralReef | shaders | WGSL shader compilation (fes_gaussian_sum_f64.wgsl) |
| barraCuda | math | Isosurface tessellation, 3D projection, f64 primitives |
| petalTongue | visualization | 3D molecular rendering, FEL surfaces, orbit camera |
| NestGate | storage | PseudoSpore persistence, session state |
| rhizoCrypt | dag | Experiment session lineage (DAG per simulation run) |
| loamSpine | lineage | Permanent ledger of sealed experiments |
| sweetGrass | provenance | Collaborative attribution chains |
| BearDog | crypto | PseudoSpore signing, secure transport |
| Songbird | discovery | Primal mesh routing, capability discovery |
| Squirrel | ai | FEL feature summarization, simulation suggestions |

---

## Degradation Tiers

| Tier | Available | Capability |
|------|-----------|-----------|
| 1 (standalone) | No primals | Browse pseudoSpore, view pre-rendered figures, validate BLAKE3 integrity |
| 2 (GPU compute) | toadStool + barraCuda | Live FES reconstruction, parameter sweeps, cross-landscape comparison |
| 3 (interactive) | + petalTongue | 3D molecular visualization, Cremer-Pople sphere navigation |
| 4 (persistent) | + NestGate | Save/load sessions, share pseudoSpores |
| 5 (provenance) | + trio | Sealed experiments, cryptographic lineage per session |
| 6 (full) | + Squirrel | AI-assisted analysis, literature comparison |

---

## Deploy Graph Tiers

| Tier | Primals | Use Case |
|------|---------|----------|
| Tower | bearDog + songbird | Signed transport, pseudoSpore integrity |
| Node | Tower + toadStool + barraCuda + coralReef | GPU-accelerated FES computation |
| Viz | Node + petalTongue | Interactive 3D molecular visualization |
| Nest | Viz + NestGate | Persistent pseudoSpore archive |
| Provenance | Nest + rhizoCrypt + loamSpine + sweetGrass | Sealed experiment sessions |
| Full | Provenance + Squirrel | AI analysis + full composition |

Deploy: `biomeos deploy --graph graphs/initiochem_full.toml`

---

## Relationship to coralForge / helixVision

| | coralForge | helixVision | initioChem |
|---|-----------|-------------|-----------|
| **Gen** | gen3 | gen4 | gen4 |
| **Domain** | Structure prediction | Genomics pipeline | Conformational dynamics |
| **Source** | neuralSpring | wetSpring + neuralSpring | hotSpring |
| **Key method** | AlphaFold2/3 | 16S/WGS + structure | Metadynamics FEL |
| **Complementary** | Predicts static structure | Discovers what's there | Explores how it moves |

The three products form a complete molecular biology stack:
- **helixVision** sequences the genome and identifies proteins of interest
- **coralForge** (via helixVision) predicts the 3D structure
- **initioChem** explores the conformational energy landscape — how the
  structure moves, what conformations are accessible, how enzymes exploit
  ring distortion for catalysis

---

## The Name

**initio**: From *ab initio* — "from the beginning." Computational chemistry
that starts from first principles. Also: the initiation of a new product
category in the sporeGarden ecosystem.

**Chem**: Chemistry. The domain is specific — not all-purpose molecular
visualization, but computational chemistry research tools.

Together: first-principles chemistry, made interactive and sovereign.

---

## What initioChem Will Prove

When implemented, initioChem will demonstrate:

1. **The sporeGarden pattern works for computational chemistry** — same
   PrimalBridge, deploy graphs, and degradation as esotericWebb
2. **petalTongue Phase 4 drives real science** — first consumer of
   molecular visualization, proving it beyond game rendering
3. **Validated science becomes interactive** — pseudoSpore data can be
   explored, not just viewed
4. **Sovereign compute handles real MD** — GPU FES reconstruction at
   publication quality on consumer hardware
5. **The spore cycle completes** — product emits pseudoSpore → feeds back
   into spring validation → evolves primals → enriches the product

---

## References

- Product spec: `hotSpring/specs/COMPCHEM_SPOREGARDEN_PRODUCT.md`
- Garden seed: `gardens/initioChem/`
- Remote: `git@github.com:sporeGarden/initioChem.git`
- Upstream handoff: `infra/wateringHole/handoffs/HOTSPRING_COMPCHEM_PETALTONGUE_BARRACUDA_MAY28_2026.md`
- ABG Project 3: `whitePaper/attsi/non-anon/contact/ABG/projects/03_cazyme_landscapes/RESEARCH.md`
- pseudoSpore v1.7.0: `hotSpring/pseudoSpore_hotSpring-CompChem-GuideStone_v1.7.0/`
- Sovereign CompChem roadmap: `hotSpring/specs/SOVEREIGN_COMPCHEM_EVOLUTION.md`

---

*initioChem is not the simulation. It is what the chemist sees through the
simulation — energy basins on the Cremer-Pople sphere, ring distortion in
the enzyme active site, barrier heights that explain catalysis — all traced
from theory to computation to publication, all on hardware they own.*
