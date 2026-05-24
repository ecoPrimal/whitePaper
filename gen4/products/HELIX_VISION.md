# helixVision

**Sovereign Genomics Discovery: From Sample to Understanding on Your Hardware**

**Date**: March 24, 2026
**Status**: Conceptual — science validated in gen3, gen4 product layer planned
**Organization**: sporeGarden (planned)
**Lineage**: gen3/baseCamp/09 (Field Genomics) + gen3/baseCamp/10 (coralForge) + gen3/baseCamp/04 (Sentinels) + gen3/baseCamp/21 (Sample Provenance) → gen4

---

## What It Is

helixVision is a sovereign genomics discovery platform that composes
ecoPrimals infrastructure into a deployable pipeline from biological
sample to scientific understanding. It is not a spring — it does not
reproduce published science. It is a **product** — something a field
biologist, wastewater engineer, or environmental scientist uses to
analyze what's in a sample without cloud dependency.

Where esotericWebb proved the gen4 pattern for **creative** domains
(game engines), helixVision proves it for **science** domains. Same
primals, same PrimalBridge pattern, same graceful degradation — but
the user sees a genomics pipeline instead of a game loop.

**coralForge** (structure prediction) is not deprecated — it becomes
helixVision's structure prediction module. The gen3 science stays in
neuralSpring. helixVision is the gen4 product layer that composes it
with wetSpring genomics and other primals into something deployable.

---

## The Pipeline

```
Sample (soil, water, air, tissue)
  → Sequencing (MinION Mk1D, Illumina, or existing FASTQ)
  → helixVision pipeline:
      ├── wetSpring 16S/WGS (DADA2, chimera, taxonomy, diversity)
      ├── Community profiling (Shannon, Simpson, Anderson QS framework)
      ├── Anomaly detection (ESN classifiers on AKD1000 NPU)
      ├── coralForge structure prediction (AlphaFold on proteins of interest)
      ├── hotSpring MD validation (bonded FF + metadynamics → conformational trust)
      └── Provenance (trio: sample → analysis → results → publication)
  → Visualization (petalTongue: community profiles, 3D structures, FEL surfaces)
  → All on sovereign hardware, no cloud, no vendor lock-in
```

---

## Springs Consumed (gen3 Science)

helixVision composes validated science from three springs:

### wetSpring — Genomics and Environmental Monitoring

| Capability | baseCamp Paper | What It Provides |
|-----------|---------------|-----------------|
| 16S pipeline (DADA2) | 09 (Field Genomics) | Sovereign basecalling, chimera detection, taxonomy |
| Microbiome analytics | 03 (BioAg Microbiome) | Diversity indices, Anderson QS framework |
| Sentinel detection | 04 (Microbial Sentinels) | Community shift as biosensor for contamination |
| PFAS screening | 04 | Contaminant detection in water/soil |
| Wastewater surveillance | 04 | AMR gene monitoring, pathogen emergence |
| Genomic Vault | 09 | Consent-gated encrypted storage for MinION data |
| ESN classifiers | 04 | Real-time anomaly detection (AKD1000 NPU validated) |

wetSpring has 6,656+ checks across 260 experiments. The 16S pipeline
is sovereign — no QIIME2, no EPI2ME, no Python runtime.

### neuralSpring/coralForge — Structure Prediction

| Capability | baseCamp Paper | What It Provides |
|-----------|---------------|-----------------|
| AlphaFold2 primitives | 10 (coralForge) | Evoformer, IPA, triangle ops, embeddings |
| AlphaFold3 diffusion | 10 | DDPM/DDIM forward/reverse, pairformer, confidence |
| GPU acceleration | 10 | BarraCuda WGSL shaders, consumer GPU ($600 RTX 4070) |
| LTEE structural analysis | 02 (LTEE Extensions) | Protein fold evolution across 75,000 generations |

coralForge has 154 checks (62 Python + 55 Rust + 37 GPU) across
the full structure prediction stack. All quality gates green.

### hotSpring — Biomolecular MD Validation

| Capability | Experiment | What It Provides |
|-----------|------------|-----------------|
| Nonbonded MD engine | Exp 001–219 | LJ, Coulomb, PPPM, thermostats, cell/Verlet lists — 500+ checks |
| Bonded force fields | Exp 220 (Phase 1) | Harmonic bond/angle, dihedral torsion, improper — carbohydrate ring FF |
| Topology reader | Exp 220 (Phase 2) | GROMOS 45a4 / GLYCAM06 parameter parsing |
| Metadynamics bias | Exp 220 (Phase 3) | Cremer-Pople CVs, Gaussian hill deposition for conformational FEL |
| GROMACS parity | Exp 220 (Phase 4) | Industry control validation — proves MD correctness before trust |

hotSpring's MD engine validates that coralForge's predicted structures sit at
conformational energy minima — structure prediction is necessary but not
sufficient; MD validation proves the predicted geometry is physically stable.
GROMACS 2026.0 (CUDA, PLUMED, Colvars) is the industry control/parity anchor.

**The predict→validate→confirm→visualize loop:**
```
coralForge predicts structure (AlphaFold2/3)
  → hotSpring validates via MD (bonded FF + metadynamics on sovereign GPU)
  → GROMACS confirms hotSpring MD is correct (industry parity)
  → petalTongue renders FEL + 3D structure
```

---

## Primals Consumed via IPC

helixVision follows the PrimalBridge pattern established by
esotericWebb — JSON-RPC 2.0 over TCP, zero primal crate imports,
graceful degradation when primals are absent.

| Primal | Domain | Role in helixVision |
|--------|--------|-------------------|
| toadStool | compute | GPU dispatch for structure prediction, diversity analysis |
| coralReef | shaders | WGSL shader compilation (sovereign GPU stack) |
| barraCuda | math | f64 math primitives, WGSL shaders |
| NestGate | storage | FASTA/FASTQ storage, Genomic Vault |
| rhizoCrypt | dag | Analysis session DAG (sample → processing → results) |
| loamSpine | lineage | Sample certificates, chain-of-custody |
| sweetGrass | provenance | Attribution (collector, analyst, publisher) |
| BearDog | crypto | Sample signing, Genomic Vault encryption |
| Songbird | discovery | Federation between field station and lab |
| Squirrel | ai | AI-assisted interpretation of community profiles |
| petalTongue | visualization | Community profiles, 3D structures, dashboards |

---

## Applications

### Field Genomics

A field biologist carries a MinION sequencer and a laptop. helixVision
runs the full pipeline on-site: sequence → classify → visualize →
provenance. No network required. No cloud upload. The scientist owns
every bit from collection to publication.

**Validated by**: wetSpring Paper 09 (sovereign 16S pipeline), hotSpring
metalForge (AKD1000 NPU edge classification at 18.8K Hz, coin-cell
battery life).

### Wastewater Monitoring

A wastewater engineer runs continuous surveillance for PFAS markers,
antimicrobial resistance genes, and pathogen emergence. helixVision's
ESN classifiers detect community shifts that signal contamination
before chemical sensors can. The Anderson QS framework quantifies
whether the microbial community can coordinate a response.

**Validated by**: wetSpring Paper 04 (Sentinels — PFAS screening,
bloom detection, AMR surveillance), hotSpring (AKD1000 streaming
inference at 2.8us/step).

### Harmful Algal Bloom Detection

Lake monitoring stations detect *Microcystis* and other HAB-forming
organisms via eDNA. The sentinel framework treats community diversity
shifts as early warnings — detecting bloom conditions hours to days
before visible signs.

**Validated by**: wetSpring Exp118, Exp123 (bloom sentinel on real
AKD1000 hardware, 20 checks).

### LTEE Structural Analysis

The Lenski Long-Term Evolution Experiment maintains 75,000+ generations
of *E. coli* in frozen fossil records. helixVision can predict the 3D
structure of every protein at every generation, revealing which structural
folds are conserved, whether convergent structural solutions appear across
12 replicate populations, and whether the Ara-3 citrate innovation has a
detectable structural precursor.

**Validated by**: coralForge AlphaFold2/3 primitives (154 checks),
wetSpring 16S pipeline.

### Soil Microbiome

Orchard managers assess soil health, inoculant effectiveness, and
contamination via community profiling. The Anderson localization model
predicts whether inoculant strategies will succeed based on soil
geometry — 3D biofilm formation on root surfaces sustains QS while
dilute broadcast application fails.

**Validated by**: wetSpring Paper 03 (BioAg Microbiome — pistachio/almond,
Anderson QS predictions), Paper 06 (no-till Anderson).

### Environmental DNA

Airborne and waterborne eDNA sampling to assess whole biomes without
physical collection. Shotgun sequencing of environmental DNA through
the sovereign pipeline. Every sample is a Novel Ferment Transcript
with full chain-of-custody.

**Validated by**: wetSpring Paper 09, Paper 21 (Sovereign Sample
Provenance — field-to-publication chain-of-custody).

---

## Degradation Tiers

The esotericWebb pattern applies: no primal is required, every primal
is beneficial.

| Tier | Available | Capability |
|------|-----------|-----------|
| Full | All primals + GPU | Structure prediction, community profiling, provenance, visualization, AI interpretation, federation |
| Compute | No GPU | Community profiling + provenance + visualization (structure prediction skipped) |
| Minimal | Core only | 16S pipeline + local diversity metrics (text output, local provenance log) |
| Standalone | No primals | FASTQ → taxonomy assignment using local databases, CSV output |

The standalone tier means a researcher can process sequences on an
air-gapped laptop in a BSL-3/4 lab. Primals enrich the pipeline;
they don't gatekeep it.

---

## Deploy Graph Tiers

Following the atomic tier pattern from esotericWebb:

| Tier | Primals | Use Case |
|------|---------|----------|
| Sequence | toadStool + coralReef + barraCuda | GPU-accelerated analysis (structure prediction, large-scale diversity) |
| Provenance | Sequence + rhizoCrypt + loamSpine + sweetGrass | Full chain-of-custody from sample to publication |
| Field | Provenance + BearDog + Songbird | Field deployment with crypto signing and local mesh federation |
| Full | Field + NestGate + Squirrel + petalTongue | Complete pipeline with storage, AI interpretation, and visualization |

Each tier has a TOML deploy graph. The PrimalLauncher reads the graph,
topologically sorts, spawns from plasmidBin, and injects into the
PrimalBridge — same pattern as esotericWebb.

---

## Relationship to coralForge

coralForge is gen3 science. helixVision is gen4 product.

| | coralForge | helixVision |
|---|-----------|-------------|
| **Gen** | gen3 | gen4 |
| **Org** | syntheticChemistry (neuralSpring) | sporeGarden |
| **Scope** | AlphaFold2/3 structure prediction primitives | Full sample → understanding pipeline |
| **Coupling** | Source-level (Rust crate in neuralSpring) | Binary-only (IPC via PrimalBridge) |
| **Audience** | Computational biologists, thesis committee | Field biologists, wastewater engineers, lab scientists |
| **Output** | Validated numerical checks | Actionable analysis results |

coralForge does not rename. The baseCamp papers continue to reference
coralForge as the structure prediction validation. helixVision is the
product that makes coralForge's science accessible to people who don't
know what an evoformer is.

---

## The Name

**Helix**: The DNA double helix — the structure at the center of
everything helixVision analyzes. From soil bacteria to wastewater
pathogens to LTEE *E. coli*, the helix is the common thread.

**Vision**: Applied discovery. Not just seeing what's there, but
understanding what it means. The vision goes from raw sequence to
community profile to protein structure to publication — each step
making the invisible visible.

Together: an instrument for seeing through the lens of genomic data.

---

## What helixVision Will Prove

When implemented, helixVision will demonstrate:

1. **The sporeGarden pattern works for science** — same PrimalBridge,
   deploy graphs, and degradation as esotericWebb, but for genomics
2. **Spring science becomes deployable** — wetSpring + coralForge
   gen3 validation crosses to gen4 product without reimplementation
3. **Sovereign field science is viable** — MinION + laptop + primals
   = complete pipeline from collection to publication
4. **Provenance as infrastructure works for science** — sample
   chain-of-custody uses the same trio that tracks game sessions
5. **Edge compute is production-ready** — AKD1000 NPU at 18.8K Hz
   provides real-time classification in the field

---

*helixVision is not the microscope. It is what the scientist sees
through the microscope — community profiles from wastewater, protein
folds from frozen fossils, contamination warnings from sentinel
microbes — all traced from sample to publication, all on hardware
they own.*
