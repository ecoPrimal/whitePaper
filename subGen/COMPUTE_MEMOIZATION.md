# Compute Memoization — Never Do Work Twice

**Status**: Implemented | **Wave**: 156e | **Date**: Aug 5, 2026
**Gate**: strandGate | **Principle**: Doing work twice is burning energy and time we can never recover.

---

## Thesis

Every computation that produces a deterministic result should be stored as a
content-addressed artifact. The BLAKE3 hash of the inputs determines the hash of
the output. If the artifact exists, skip the computation. If it doesn't, compute
it once, store it, and never compute it again.

This is the compute side of the provenance trio. westGate handles data acquisition
and provenance (what was measured). strandGate handles compute memoization and
provenance (how it was computed). They are complementary and abstract of each
other — the same BLAKE3 content-addressing, the same CAS storage pattern, the
same braid structure.

---

## The NFT Production Pattern

Every cached configuration is a **Novel Fermentation Transcript** — an auditable,
replicable artifact:

```
Input parameters (deterministic):
  gauge_group = "su3"
  dims        = [32, 32, 32, 32]
  beta        = 6.0
  seed        = 42
  n_therm     = 300
  integrator  = "omelyan"
  dt          = 0.005
  n_md_steps  = 60
         │
         ▼
  BLAKE3(input_string) → cache_key → filename
         │
         ▼
  If exists: SKIP (zero compute cost)
  If not:    Thermalize → Save → BLAKE3(content) → verify
```

The braid is the data. The ferment transcript is the results. The hash is the
identity. Anyone, anywhere, with the same code and parameters, produces the
same hash. No trust required.

---

## Dynamic Programming: Tiling Smaller Configs into Larger Volumes

### The Insight

A thermalized 16⁴ lattice at β=6.0 contains local physics that is identical to
the local physics of a 32⁴ lattice at β=6.0. The correlation length ξ at typical
β values is 3-8 lattice spacings — well within 16. This means the 16⁴ config
already contains statistically independent regions.

We can **tile** the 16⁴ config into a 32⁴ volume by periodic replication:
each site (x,y,z,t) in the 32⁴ lattice copies its link from
(x mod 16, y mod 16, z mod 16, t mod 16) in the 16⁴ config.

This preserves gauge invariance exactly — every plaquette in the tiled lattice
is identical to a plaquette in the source. The starting action density is
physically correct. A short HMC burn-in (75 trajectories instead of 300+) breaks
the artificial periodicity across tile boundaries.

### The Dependency Graph

```
 8⁴ (seconds)
  │
  ▼
16⁴ (minutes) ──── memoized, BLAKE3-addressed
  │
  ├──tile──▶ 32⁴ (hours, not days) ─── 75 traj burn-in
  │
  └──tile──▶ 24⁴ stays full (not 2× multiple of 16)
              24³×Nt (finite-T, not tileable from symmetric)
```

Each rung of the volume ladder can seed the next. The 16⁴ cache (built in
minutes) pays for itself by cutting 32⁴ wall time from ~6 days to ~1-2 days
per config.

### What's Not Decomposable

You cannot partition a 32⁴ into 16 independent 16⁴ blocks, thermalize them
independently, and stitch them back. The gauge force at the seams depends on
staples that reach across block boundaries. Independent thermalization produces
discontinuities in the action density at every seam.

Tiling UP works (small → large). Partitioning DOWN doesn't (large → many small → large).

### Speedup Table

| Config | Cold Start | Tiled from 16⁴ | Speedup |
|--------|-----------|----------------|---------|
| SU(2) 32⁴ (400 traj) | ~30 hours | ~5.6 hours (75 traj) | **5.3×** |
| SU(3) 32⁴ (300 traj) | ~6 days | ~1.5 days (75 traj) | **4×** |
| SU(4) 24⁴ (300 traj) | ~4 days | not tileable (24 ≠ 2×16) | 1× |

The savings compound: every SU(N) group at 32⁴ benefits from its own 16⁴ cache.

---

## Compute CAS and Data CAS — Dual Storage

The ecosystem has two complementary CAS stores:

| | westGate (Data CAS) | ironGate/strandGate (Compute CAS) |
|---|---|---|
| **What** | Raw science data (GPS, AlphaFold, NOAA, USGS) | Computed artifacts (thermalized configs, measurements) |
| **Size** | 3.21 TB / 153 datasets (growing: 20 TB AlphaFold incoming) | ~30 GB projected (87 configs + measurements) |
| **Addressing** | BLAKE3 content hash | BLAKE3 content hash (identical scheme) |
| **Provenance** | sweetGrass braid + bearDog signature | sweetGrass braid + bearDog signature |
| **Pipeline** | Ingest → CAS → DAG → Spine → Braid | Compute → Cache → Verify → Braid |
| **Bottleneck** | Disk I/O (spinning raidz1, 15.4% iowait) | CPU (EPYC threads, pure arithmetic) |
| **Throughput** | 145/s (convoy, 460× improvement) | 1 config / minutes-to-hours (HMC cost) |

These are complementary:
- They don't compete for the same bottleneck (I/O vs CPU)
- They use the same addressing and provenance scheme
- They federate naturally via the same songBird mesh
- A braid from westGate (data lineage) can reference a braid from strandGate
  (compute lineage) — full provenance chain from raw data through computation
  to published result

### Storage Topology Target

As the mesh evolves, the natural placement:

```
westGate (Data CAS)           ←── raw science data, 50.7 TB ZFS
    │
    ├── mesh (songBird) ──▶ strandGate (Compute)
    │                           │
    │                           └── produces configs + measurements
    │
    └── mesh (songBird) ──▶ ironGate (Product CAS)
                                │
                                └── 12.7 TB CAS, downstream consumers
                                    stores compute braids alongside data braids
                                    serves results to petalTongue for visualization
```

westGate stores what was measured. strandGate computes. ironGate serves the
products — both data and compute artifacts — to consumers. The compute braids
on ironGate complement westGate's data braids: together they form the complete
provenance chain from raw observation to published figure.

---

## Memoization Beyond Lattice QCD

The pattern is not specific to lattice gauge theory. Any deterministic computation
with expensive runtime and content-addressable inputs benefits:

- **AlphaFold structure predictions**: Input sequence + model version → structure.
  BLAKE3(sequence + model) = cache key. 20 TB of predictions, never recompute.
- **RGES drug screens (tideGlass)**: Input gene expression + drug library →
  enrichment scores. Cache the result per (expression_profile, drug_set) pair.
- **GIS raster processing (footPrint)**: Input tiles + processing pipeline →
  output layers. Cache per (tile_hash, pipeline_version).
- **Neural network inference (neuralSpring)**: Input data + model weights →
  predictions. Cache per (data_hash, model_hash).

In each case: compute once, store the BLAKE3-addressed result, never compute again.
The cache is the memo table. The braid is the provenance. The hash is the proof
that the result matches the inputs.

Doing work twice is burning energy and time we can never recover.

---

*subGen Wave 156e — Compute Memoization. tile_from() implements dynamic programming
for lattice thermalization: 16⁴ → 32⁴ at 4-5× speedup. Compute CAS complements
data CAS — same BLAKE3 addressing, same braid structure, different bottleneck.
ironGate serves the products. The pattern generalizes beyond QCD to any
deterministic computation with expensive runtime.*
