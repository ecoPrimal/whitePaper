# Convergence Tiering — DAG Collapse, Dedup, and Multi-Resolution Spines

**Status**: Concept → pattern (discovered during westGate NVMe drain analysis)
**Wave**: 157a | **Date**: Aug 8, 2026
**From**: westGate data team + overwatch
**Audience**: primalSpring, nestGate, rhizoCrypt, loamSpine teams

---

## The Observation

westGate's NVMe warm tier filled to 88% with CAS objects that already existed
on cold ZFS. nestGate's `content.put` writes to warm, but there is no drain
or eviction mechanism. The initial instinct was to build a separate tiering
subsystem — an rsync-based drain script, a cron job, an operational layer
outside the provenance chain.

The insight: **tiering IS provenance**. The same primitives that track "what
data exists and where it came from" can track "where data lives and when it
moved." DAG collapse, deduplication, and tier management are all the same
convergence operation at different scales.

---

## The Unification

### Three operations that are structurally identical

| Operation | Input | Convergence | Output |
|-----------|-------|-------------|--------|
| **Braiding** | Many files across chunks | BLAKE3 → CAS → DAG → Merkle | Spine entry: "these files are provenanced" |
| **Dedup** | Object hash vs. existing store | content.exists across tiers | Boolean: "already have it" |
| **Tier drain** | Warm objects vs. cold existence | Verify warm ⊆ cold, evict warm | Spine entry: "these objects are archived" |

All three follow the same pattern:
1. **Enumerate** a set of items (files, objects, tier contents)
2. **Check convergence** (hash match, existence, tier presence)
3. **Collapse** the enumeration into a single proof (Merkle root)
4. **Commit** the proof linearly (spine entry)

The primals already do steps 1-4 for braiding. Tiering is the same steps
applied to a different domain.

---

## The Architecture

### rhizoCrypt as convergence engine

rhizoCrypt's DAG is not "a data structure for provenance events." It's a
**convergence engine** — it tracks any set of parallel operations and collapses
them into a verifiable state. The operations it tracks today:

- File → BLAKE3 hash → CAS put → DAG event (braiding)

The operations it should also track:

- CAS object on warm → verified on cold → evicted from warm (tier transition)
- Object hash checked across N tiers → existence bitmap → DAG event (cross-tier dedup)
- Batch of transitions → Merkle root → spine commit (drain proof)

The DAG event schema extends naturally:

```
Braiding event:
  { type: "cas.put", hash: "abc...", source: "/data/alphafold/v1/file.tar" }

Tier transition event:
  { type: "tier.drain", hash: "abc...", from: "warm", to: "cold", verified: true }

Tier verification event:
  { type: "tier.verify", prefix: "a3", count: 28542, merkle: "def..." }
```

Same DAG. Same dedup. Same collapse. Different event types.

### loamSpine as multi-resolution commitment

Today, loamSpine has one spine per dataset — a linear sequence of commits, each
containing a Merkle root over a batch of DAG events. This is the **long spine**:
complete, cryptographically exhaustive, expensive to traverse.

The pattern extends to **multiple spine resolutions**:

#### Long spine (full history)
```
Entry 0: "alphafold v1 braided, 20 files, merkle=550b..."
Entry 1: "alphafold v2 braided, 49 files, merkle=6517..."
Entry 2: "alphafold v3 braided, 51 files, merkle=1743..."
  ...
Entry N: "warm batch 7 drained to cold, 28K objects, merkle=9a1f..."
```

Every event, every transition, complete chain of custody. This is the audit
trail. It answers: "prove that object X was braided at time T and moved to
cold at time T+1."

#### Short spine (tier index)
```
Entry 00: merkle_root over all objects with prefix 00 → tier=cold, verified
Entry 01: merkle_root over all objects with prefix 01 → tier=cold, verified
  ...
Entry ff: merkle_root over all objects with prefix ff → tier=cold, verified
```

256 entries. One per CAS prefix bucket. Each entry is a Merkle root over
every object in that bucket, plus a tier assertion. This is the **operational
index** — it answers: "is prefix bucket `a3` fully drained?" in O(1).

#### The hash collision insight

The short spine doesn't avoid hash collisions — it **uses them as the
sharding mechanism**. When you truncate a BLAKE3 hash to its first byte
(the CAS prefix directory), all objects sharing that prefix "collide" into
the same bucket. This is exactly what a hash table does:

```
Short spine key: first byte of BLAKE3 (00-ff)
  → 256 buckets
  → Each bucket: Merkle root over all objects in that prefix
  → Hash "collision" = objects share a prefix = same bucket

Secondary hash table: the actual CAS prefix directory
  00/0000030b5f... → { tier: cold, size: 4096, verified: 2026-08-08 }
  00/0001a7e2c4... → { tier: warm, pending_drain: true }
  00/0003fb19d8... → { tier: cold, size: 8192, verified: 2026-08-08 }
```

The short spine is a **Merkle-committed hash table** where:
- Level 0: 256 buckets (1-byte prefix)
- Level 1: 65,536 buckets (2-byte prefix) — if you need finer resolution
- Level N: the full BLAKE3 hash — equivalent to the long spine

Each level is a valid spine on its own. Shorter = faster lookup, less
precision. Longer = slower lookup, full auditability. The levels nest:
the Level 0 Merkle root for bucket `a3` covers everything that Level 1
entries `a300` through `a3ff` cover, which covers everything that the
full hashes starting with `a3` cover.

This is a **Merkle trie** where the spine levels correspond to hash
prefix lengths.

---

## How Drain Works in This Architecture

### Without this pattern (operational script)

```
for each object on warm:
    if exists on cold:
        rm from warm
    else:
        cp warm → cold
        rm from warm
```

No proof it happened correctly. No audit trail. No crash recovery. No way
to verify after the fact that every object was accounted for.

### With this pattern (rhizoCrypt-backed drain)

```
1. Enumerate warm prefix bucket (e.g., 00/)
   → 28,542 objects

2. For each object: content.exists on cold tier
   → DAG event: { type: "tier.verify", hash, cold_exists: true/false }
   → Batch: dag.event.append_batch (200 events/RPC)

3. For missing objects: content.put to cold
   → DAG event: { type: "tier.replicate", hash, from: warm, to: cold }

4. Collapse bucket to Merkle root
   → dag.dehydration.trigger for bucket 00/
   → Merkle root covers all 28,542 verify + replicate events

5. Commit to short spine
   → session.commit: { prefix: "00", merkle: "...", objects: 28542, all_cold: true }

6. Evict from warm
   → rm warm/00/* (safe: spine proves cold has everything)
   → DAG event: { type: "tier.evict", prefix: "00", count: 28542 }

7. Commit eviction to long spine
   → Full audit trail: "bucket 00 drained, all objects verified, eviction proven"
```

**Crash recovery**: If the process dies at step 3, the short spine doesn't
have the commit for bucket `00/`, so the next run re-enumerates and
re-verifies. The DAG events from the partial run are already recorded —
the next run deduplicates against them.

**Verification**: After drain, anyone can check:
- Short spine says bucket `00/` merkle = X
- Recompute Merkle over cold/00/ objects → should match X
- If match: drain was correct. If not: data integrity issue.

---

## Implications

### 1. nestGate doesn't need tier.drain

The drain is not a nestGate feature — it's a **composition** of existing
primal capabilities:
- `content.exists` (nestGate) — tier check
- `dag.event.append_batch` (rhizoCrypt) — transition log
- `dag.dehydration.trigger` (rhizoCrypt) — Merkle collapse
- `session.commit` (loamSpine) — spine entry
- `braid.create` (sweetGrass) — provenance seal

This is a biomeOS graph, not a single-primal method.

### 2. Dedup is free

Cross-tier dedup falls out of the architecture. If `content.exists` returns
true on cold, you don't replicate — you just record the verification event
and evict from warm. The DAG tracks the proof, not the data movement.

### 3. Multiple short spines for different purposes

The multi-resolution spine pattern isn't limited to tiering:
- **Tier spine** (256 entries): which objects are on which tier
- **Dataset spine** (per-dataset): provenance for a specific dataset
- **Convergence spine** (per-gate): has this gate's data converged with mesh?
- **Attribution spine** (per-DID): what has this identity produced?

Each is a different "view" over the same underlying DAG events, committed
at a different hash resolution or filtering criterion.

### 4. ZFS ARC becomes the read cache, not the tier cache

Once warm CAS drains to cold, reads go through ZFS. ZFS ARC (RAM) and
L2ARC (SSD) automatically cache hot reads. The NVMe warm tier returns to
its intended role: **ephemeral workspace for active braiding**, not
permanent storage. The 4-tier hierarchy reasserts:

```
T0: RAM (ZFS ARC)    — automatic, 32 GB, read cache
T1: NVMe             — ephemeral, braiding workspace, drains after commit
T2: SSD (L2ARC)      — automatic, warm read cache
T3: HDD (ZFS raidz1) — durable archive, canonical cold tier
```

NVMe is the **active braiding surface**. Data arrives, gets hashed, gets
CAS-put, gets DAG-tracked, gets spine-committed, gets braid-sealed. Then
it drains to cold. The NVMe is never more than one active braiding session
worth of data.

### 5. The short spine IS the CAS index

Today, finding "what objects exist in the CAS" requires walking the prefix
directories on disk. The short spine replaces this with a Merkle-committed
index that can be queried without touching the filesystem:

```
"How many objects in prefix a3?"
  → Short spine entry a3: count=28,542, merkle=def..., tier=cold

"Is object a3f7e2... in the CAS?"
  → Short spine says a3 bucket exists with merkle def...
  → Verify object hash is in the Merkle tree (log N proof)
  → No disk read needed for existence check
```

This is the bridge between "provenance tracking" and "content-addressed
storage" — the spine IS the index, not a parallel bookkeeping system.

---

## Pattern Evolution Path

### Phase 1: Operational drain (now)
Script-level drain: enumerate warm, check cold, rsync missing, rm warm.
Record the drain as a long spine entry. No short spine yet.

### Phase 2: rhizoCrypt-backed drain
Replace script with DAG-tracked drain. Each tier transition is a DAG event.
Batch collapse to Merkle roots. Long spine commits.

### Phase 3: Short spine
Introduce 256-entry short spine for tier index. Merkle root per prefix
bucket. O(1) "is this bucket drained?" check.

### Phase 4: Multi-resolution
Generalize to N-level hash trie. Short spine at 1-byte, 2-byte, or
arbitrary prefix lengths. Different spines for different query patterns
(tier, dataset, attribution, convergence).

### Phase 5: Self-draining
biomeOS graph that runs automatically: when warm tier exceeds threshold,
trigger rhizoCrypt-backed drain, commit to short spine, evict. The
"backpressure" system becomes a spine-committed drain cycle, not a
write-rejection threshold.

---

## For primalSpring

This pattern requires no new primals. It requires:

1. **rhizoCrypt**: Accept tier transition event types in the DAG schema
   (or treat them as generic events — the DAG doesn't need to know what
   the events mean, just that they form a tree)

2. **loamSpine**: Support multiple named spines per dataset (long spine
   for audit, short spine for index). May already be possible if spine
   creation is parameterized.

3. **nestGate**: Expose `content.exists` with explicit tier targeting
   (check cold only, check warm only). Currently checks all tiers.

4. **biomeOS**: Graph executor wires the drain as a composition:
   enumerate → verify → replicate → collapse → commit → evict.
   This is the "complex dispatching and graphs" the blurb calls for.

5. **sweetGrass**: Braid the drain itself — the tier transition gets the
   same provenance seal as the data ingress. Full chain of custody from
   "data arrived" through "data archived."

---

*The deepest architectural insight from westGate data operations: DAG
collapse, content dedup, and tier management are the same convergence
operation at different scales. rhizoCrypt is a convergence engine, not
just a provenance tracker. loamSpine commits at multiple hash resolutions,
not just linear history. The short spine — a Merkle-committed hash table
where collisions are the sharding mechanism — unifies the CAS index with
the provenance chain. Tiering becomes provenance. The warm tier becomes
truly ephemeral. And the architecture already has every primitive needed —
the composition just hasn't been wired yet.*
