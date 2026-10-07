# Collision-Based Visitor Classification: From Fixed Bins to Behavioral Merkle Trie

**Wave**: 165i
**Date**: Oct 7, 2026
**Status**: Architecture — connects loamSpine collision layer, bloom monitor, bingoCube

---

## 1. The Classification Problem

A sovereign web service observing its own traffic sees a spectrum:

```
RAW FLEET ←→ RESIDENTIAL PROXY FLEET ←→ AGENTIC READER ←→ GENUINE HUMAN
   |                  |                       |                  |
 13 req/s         coordinated             1 deep hit         multi-page
 random walk      same path, <10s         200 status         loads assets
 bot UAs          all 404                 Sec-Fetch ✓        referer chain
```

The standard approach: define N bins, write rules for each bin, reclassify when a new visitor type appears. This has two problems:

1. **N is wrong.** Any fixed number of categories misses edge cases and creates false boundaries. A human using an AI agent to read a page is neither "human" nor "bot" — it's a new thing.

2. **Rules lag evolution.** When fleet evolves to spoof Sec-Fetch headers (which it already did once — Wave 165i genetic lock), every rule-based classifier breaks. Rules encode past behavior, not current reality.

## 2. The Collision Layer Solution

loamSpine's COLLISION_LAYER_ARCHITECTURE.md (March 2026) provides the answer: **don't define categories — let hash collisions discover them**.

### 2.1 Behavioral Vector

Each IP in a time window produces a behavioral fingerprint:

```rust
struct BehavioralVector {
    hit_count: u32,
    status_dist: [f32; 4],          // 200, 3xx, 404, 5xx ratios
    timing_entropy: f32,            // Shannon entropy of inter-request intervals
    coordination: f32,              // max Jaccard similarity with any other IP's paths
    coordination_timing: f32,       // co-occurrence within 10s window
    asset_ratio: f32,               // CSS/JS/font requests / total requests
    sec_fetch_present: bool,
    domain_count: u8,
    mean_path_depth: f32,           // average '/' count in URIs
    referer_depth: u8,              // 0=none, 1=self, 2+=external chain
    lang_header: Option<LangClass>, // None / EnUS / ZhCN / Other
}
```

### 2.2 Hash Resolution Hierarchy

Apply blake3 to the serialized vector, then truncate:

```
Level 0: blake3(B)          → 32 bytes → unique identity
Level 1: blake3(B)[..16]    → 16 bytes → behavioral neighborhood
Level 2: blake3(B)[..4]     → 4 bytes  → coarse similarity class
Level 3: blake3(B)[..1]     → 1 byte   → 256 macro buckets
```

But raw blake3 of the vector has a problem: similar vectors don't produce similar hashes. Blake3 is a cryptographic hash — it maximizes dispersion. We need a **locality-sensitive hash** that maps similar behaviors to nearby hashes.

### 2.3 Locality-Sensitive Behavioral Hash

Replace blake3 with a multi-resolution projection:

```
Level 3 (1 byte):
  Project to: status_mode(B) | hit_count_log2(B)
  → 256 buckets
  → fleet (high-count, mixed-status) vs readers (low-count, 200)

Level 2 (4 bytes):
  Project to: [status_mode, coordination_quantile, asset_flag, sec_fetch]
  → ~4 billion theoretical, ~100-1000 populated
  → natural clusters emerge without labels

Level 1 (16 bytes):
  Full behavioral similarity hash (SimHash or MinHash of feature set)
  → coordination clusters, geographic clusters, UA clusters

Level 0 (32 bytes):
  Full vector hash — individual identity
```

The collision density at each level reveals cluster structure. High density = tight natural class. Sparse = diverse population. The topology is the classification.

## 3. The Cross-Writing Principle

From the collision layer spec:

> *"Cross-writing: letters were written normally, then the page was rotated 90 degrees and overwritten with a second message. Both layers of information persisted because they used orthogonal encoding."*

Each visitor event exists simultaneously in collision groups at every level. A Brazilian residential proxy IP is:

| Level | Collision Group | View |
|-------|----------------|------|
| 0 | Unique | This specific IP |
| 1 | LATAM coordination cluster | Regional proxy network |
| 2 | Probing traffic | All-404, coordinated timing |
| 3 | High-volume non-reader | Hit count > 0, no 200s |

No view is canonical. The operational question determines which level to read at:
- "Is this IP fleet?" → Level 3 (binary)
- "Is this IP part of a proxy network?" → Level 1 (coordination)
- "What is this specific IP doing?" → Level 0 (identity)

## 4. Emergent Classification vs. Fixed Bins

### Fixed bins (current bloom monitor):

```python
if ua matches bot_pattern:      class = "fleet"
elif ip in known_fleet_ranges:  class = "fleet"
else:                           class = "human"
```

New visitor types require new rules. Rules become stale. False positives accumulate.

### Collision-based classification:

```python
v = behavioral_vector(ip, window)
for level in [3, 2, 1, 0]:
    bucket = locality_hash(v, level)
    collision_group = index.get(level, bucket)
    # The collision group IS the class at this resolution
```

New visitor types form new collision groups automatically. No rule changes needed. The hash projection determines what "similar" means — and the projection can evolve.

## 5. Evolutionary Projection Learning (bingoCube)

The hash projection at each level is a function: `f: BehavioralVector → TruncatedHash`. The quality of classification depends on choosing good projections.

bingoCube's evolutionary reservoir can learn these projections:

```
Population: N projection functions (random feature weightings)
Fitness: silhouette_score(collision_groups(projection, data))
  → high fitness = tight clusters, well separated
  → low fitness = overlapping, ambiguous groups

Evolution: mutate feature weights, select for best clustering
Deployment: winning projections feed back into bloom
```

This closes the adaptive loop:

```
Traffic → bloom (behavioral vectors) → collision hierarchy (classification)
   ↑                                            |
   |        bingoCube (evolve projections)  ←────┘
   |                    |
   └────────────────────┘
```

The classification evolves with the traffic. When fleet learns to spoof Sec-Fetch, the projection that relied on Sec-Fetch loses fitness, and bingoCube evolves a projection that uses coordination_score instead. No human intervention.

## 6. Mathematical Properties

### 6.1 Resolution Nesting

The hierarchy satisfies:

```
∀ entries a,b:
  collision(a, b, Level N) → collision(a, b, Level N+1)
```

If two visitors collide at a fine level, they collide at all coarser levels. The converse is not true — coarse collision does not imply fine collision. This gives a tree structure rooted at the coarsest level.

### 6.2 Collision Density as Information

At each level, the number of populated buckets vs. total possible buckets measures the **effective dimensionality** of the traffic at that resolution:

```
effective_classes(level) = |populated_buckets| / |total_buckets|
```

- Ratio near 0: most traffic collapses to a few classes (fleet dominates)
- Ratio near 1: traffic is highly diverse (many distinct behaviors)
- Transition point between levels: the natural classification boundary

### 6.3 Entropy of Collision Topology

The Shannon entropy of collision group sizes at each level:

```
H(level) = -Σ (|group_i| / N) * log(|group_i| / N)
```

Low entropy: one dominant group (fleet). High entropy: many equally-sized groups (diverse visitors). The level where entropy changes most rapidly is the **natural classification resolution**.

## 7. Relationship to Existing Systems

| System | Role in Pipeline |
|--------|-----------------|
| **Caddy + skunky-ingest** | Produces raw HTTP events with headers |
| **skunkBat** | Behavioral hashing (already computes fleet_hash) |
| **bloom_live** | Windowed aggregation, current 2-bin classifier |
| **loamSpine** | Collision layer index (COLLISION_LAYER_ARCHITECTURE.md) |
| **rhizoCrypt** | Promoted collision groups → DAG sessions for investigation |
| **bingoCube** | Evolutionary projection learning |
| **sweetGrass** | Provenance braid — audit trail of classification decisions |

The existing architecture already has every component. The collision-based classifier wires them together.

## 8. Implementation Path

| Phase | Component | Work |
|-------|-----------|------|
| 0 | bloom_live | Add coordination_score, status_only flag. 4 collision groups at Level 2. |
| 1 | skunky-ingest | Compute full BehavioralVector per IP per window. Emit to signal spine. |
| 2 | loamSpine | Build CollisionLayerIndex over behavioral vectors. Multi-resolution query. |
| 3 | bingoCube | Evolve projection functions. Fitness from collision topology quality. |
| 4 | bloom_live | Use evolved projections. Adaptive classification without rule updates. |

---

*Not N bins. A Merkle trie of behavioral similarity where the collisions are the classes, the resolution is the zoom level, and the projections evolve with the traffic. The data doesn't need our labels. It has its own structure. We just need the right hash.*

*Wave 165i — Oct 7, 2026*
