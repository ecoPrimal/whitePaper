# Signal Braid — Immune Lineage via the Provenance Trio

**Wave**: 164d | **Date**: Oct 6, 2026
**Status**: ARCHITECTURE — design phase, informed by trio operational experience
**Domain**: Signal provenance, immune memory, log ingestion, resumable analysis
**Upstream**: PROVENANCE_TRIO_ARCHITECTURE.md, ADAPTIVE_IMMUNE_BLOOM_SENSOR.md,
SILT_POND_ACTIVE_INVESTIGATION.md, BRAID_VALIDATION_CHAIN.md
**Consumer**: skunky-ingest, bloom sensor, northgate investigation, siltPond

---

## The Problem

The organism's sensory data is ephemeral. Caddy access logs rotate by size
and disappear. Bloom observations write to `/run/membrane/bloom.signal` and
get overwritten every 30 seconds. The siltPond analysis reconstructs visitor
stories from raw logs, but the reconstruction can't be replayed, resumed,
or verified.

This means:
- **No immune memory** — the organism forgets what it saw yesterday
- **No resumability** — if skunky-ingest restarts, it starts fresh
- **No lineage** — we can't trace "this investigation conclusion was based
  on THIS data window with THESE classification rules"
- **No splitting** — we can't fork the analysis (e.g., "what if we used
  different classification thresholds?")
- **Unbounded growth** — logs accumulate forever with no compaction,
  summarization, or provenance-tracked archival

The provenance trio solves all five problems. It was designed for exactly
this pattern: ingest raw data → track lineage → commit to permanent record
→ sign → attribute. The science data pipeline on westGate already does this
for 519 GB across 130 datasets. The signal pipeline is the same architecture
applied to a different domain.

---

## The Biological Mapping

| Immune System | Provenance Trio | Signal Pipeline |
|---------------|----------------|-----------------|
| **Genetic code** (DNA) | Content-Addressed Storage (nestGate CAS) | Raw log data, BLAKE3-hashed, immutable |
| **Antigen presentation** (MHC) | DAG session (rhizoCrypt) | Classified observations: who visited, what type, what pattern |
| **B-cell memory** | Spine commit (loamSpine) | Permanent record of each observation window |
| **Antibody specificity** | Ed25519 signature (bearDog) | Cryptographic binding: this analysis used this data |
| **Immune lineage** | Attribution braid (sweetGrass) | Full provenance: data + classifier version + analyst + methodology |

The immune system doesn't store every pathogen it encounters — it stores
**memory cells** that encode the *pattern* of the encounter. When the same
pathogen returns, the memory cell activates faster than the first time.

The signal braid does the same thing: it doesn't store every HTTP request
forever. It stores **observation windows** — compressed, classified summaries
of what the bloom sensor saw — linked in a DAG that tracks lineage. When we
need to investigate a pattern that appeared last week, we can trace back
through the braid to the exact observation window, with the exact
classification rules, and the exact data that produced the conclusion.

---

## Architecture

### What Gets Braided

Not raw logs. Raw logs are too large, contain IPs (which we strip), and
have no analytical structure. What gets braided is the **observation** —
the bloom sensor's classified output after privacy filtering:

```
Observation Window (30 seconds):
  window_id:       BLAKE3(window_start || window_end || sensor_version)
  parent_id:       previous window's hash (chain)
  timestamp:       { start: 1791234567, end: 1791234597 } (UTC nanos)
  sensor_version:  "bloom-v1.0.0" (classification rules version)

  signal: {
    total_requests: 47,
    unique_ips:     23,       (count only, no IPs stored)
    domains: {
      detroit: { human: 12, ai_retrieval: 1, scanner: 0, ... },
      sporeprint: { human: 3, search_crawler: 8, ... },
      git: { other_bot: 23, ... },
    },
    cross_domain:   0,        (bridge count)
    languages:      ["en-US", "en-GB", "de"],
    divergences:    ["/keywords", "/key-analysis"],  (404s from human sessions)
    engagement: {
      attention:    ["/analysis/funding-flow/"],      (most-hit content pages)
      interest:     { deep_sessions: 2, avg_depth: 4.3 },
      divergence:   { human_404s: 2, naming_traps: 0 },
    }
  }

  immune: {
    fleet_ips:      1945,
    fleet_hashes:   ["49e77ea75aa7666e", "087ef04a48f7b1ca"],
    antibody_matches: 87,
    scatter_ratio:  0.42,
    opsonize_tags:  2,
  }
```

Each observation window is a node in the DAG. The parent hash chains them.
The content hash (BLAKE3 of the full observation) goes into CAS. The DAG
session accumulates windows. At session end (log rotation, midnight, or
restart), the session dehydrates to a Merkle root and commits to the spine.

### The Signal Spine

The spine is the permanent linear record — the immune memory:

```
Spine: "signal:golgiBody"

Entry 0: { merkle_root: abc123, windows: 2880, period: "2026-10-06", classifier: "v1.0.0" }
Entry 1: { merkle_root: def456, windows: 2880, period: "2026-10-07", classifier: "v1.0.0" }
Entry 2: { merkle_root: 789abc, windows: 2880, period: "2026-10-08", classifier: "v1.1.0" }
    ...                                                                  ↑ classifier updated
```

Each spine entry covers one day (2,880 windows at 30-second intervals).
The Merkle root cryptographically binds every observation window in that
day. The classifier version is recorded — so when we update classification
rules, we know exactly which spine entries used which rules.

### Resumability

If skunky-ingest restarts:
1. Read last spine entry → get the most recent Merkle root
2. Read the DAG session that produced it → get the last window_id
3. Resume from the next window after the last committed one
4. No data loss, no duplication, no ambiguity about "where were we?"

If we want to **reprocess** old data with new classification rules:
1. Fork the DAG at any spine entry
2. Re-ingest the raw log data (still in CAS) with the new classifier
3. The fork produces a new branch with different observation windows
4. Both branches exist in the DAG — we can compare results

### Splitting

The DAG naturally supports splitting. Two analysis paths from the same
data produce two branches:

```
                  [Oct 6, classifier v1.0.0]
                         |
              ┌──────────┴──────────┐
              │                     │
    [Oct 7, v1.0.0]      [Oct 7, v1.1.0 — refined]
              │                     │
    [Oct 8, v1.0.0]      [Oct 8, v1.1.0]
```

This is how the classification refinement we did today (6 → 9 categories)
would be tracked: the old 6-category branch and the new 9-category branch
are both in the DAG, rooted at the same raw data. The braid records which
branch produced which investigation conclusions in the siltPond.

---

## Data Flow — Canonical Path

*All times Eastern. Recorded in UTC.*

```
                           golgiBody (157.230.3.183)
                           ─────────────────────────
Caddy access log ──→ skunky-ingest ──→ bloom_sensor.ingest()
                           │
                    ┌──────┴──────┐
                    │             │
              IP stripped    Observation classified
                    │             │
                    ↓             ↓
              (discarded)   BloomObservation {
                              domains, readers, languages,
                              engagement topology,
                              immune status
                            }
                                │
                    ┌───────────┴───────────┐
                    │                       │
             BLAKE3 hash              Write to signal file
             (content identity)       (/run/membrane/bloom.signal)
                    │
                    ↓
             ┌── CAS (nestGate) ──┐
             │  Observation blob  │
             │  stored by hash    │
             └────────────────────┘
                    │
                    ↓
             ┌── DAG (rhizoCrypt) ──┐
             │  dag.event.append    │
             │  parent = prev hash  │
             │  4ms per window      │
             └──────────────────────┘
                    │
              (every 24h or on restart)
                    │
                    ↓
             ┌── Dehydrate ──────────┐
             │  Merkle root over     │
             │  all day's windows    │
             └───────────────────────┘
                    │
              ┌─────┴─────┐
              │           │
              ↓           ↓
       ┌── Spine ──┐  ┌── Sign ──┐
       │ session.   │  │ Ed25519  │
       │ commit     │  │ (root)   │
       └────────────┘  └──────────┘
              │           │
              └─────┬─────┘
                    ↓
             ┌── Braid (sweetGrass) ──┐
             │  Attribution:           │
             │  - sensor version       │
             │  - classifier rules     │
             │  - gate identity        │
             │  - observation period   │
             │  - spine entry ref      │
             └─────────────────────────┘
```

### At 4ms per DAG append (measured rhizoCrypt performance):

- 30-second windows → 2,880 windows/day → 11.5 seconds of DAG work/day
- Dehydration (Merkle root): one operation per day
- Spine commit: one entry per day (O(1), not O(n) — learned from westGate)
- Total overhead: negligible compared to the HTTP processing skunky-ingest
  already does

---

## Implementation Path

### Phase 1: Signal Spine Lite (skunky-ingest only, no trio deps)

Implement the essential pattern inside skunky-ingest without requiring the
full provenance trio to be running on golgiBody:

1. **Content hash each bloom observation** — BLAKE3 of the serialized
   BloomObservation struct. Already nearly free (bloom_sensor already
   produces the struct).
2. **Chain observations** — each window's hash includes the previous
   window's hash as a parent. This creates a verifiable chain without
   external dependencies.
3. **Write a daily spine file** — at midnight (or on restart), write a
   JSON file with the day's Merkle root (BLAKE3 over all window hashes
   in topological order):
   ```
   /run/membrane/signal-spine/2026-10-06.json
   {
     "date": "2026-10-06",
     "merkle_root": "abc123...",
     "window_count": 2880,
     "classifier_version": "bloom-v1.0.0",
     "parent_spine_entry": "2026-10-05.json:def456...",
     "summary": { ... aggregated day stats ... }
   }
   ```
4. **Resumability** — on startup, read the last spine file and the last
   window hash. Resume from there.

This gives us immune memory, resumability, and lineage tracking with zero
new dependencies. It's the DAG + spine pattern implemented in pure Rust
inside the existing binary.

### Phase 2: CAS Integration (nestGate on golgiBody)

When nestGate is deployed to golgiBody:
1. Store observation blobs in CAS by their BLAKE3 hash
2. The daily spine file references CAS addresses instead of ephemeral
   `/run/membrane/` paths
3. Old observation data is now permanent and content-addressable

### Phase 3: Full Trio Integration (biomeOS signal graph)

When the trio stack runs on golgiBody:
1. Replace the skunky-ingest internal chain with proper `dag.event.append`
   calls to rhizoCrypt (4ms per window, same as current)
2. Replace daily spine file with proper `session.commit` to loamSpine
3. Add `crypto.sign` via bearDog
4. Add `braid.create` via sweetGrass
5. Wire into biomeOS signal graph (new graph: `signal_braid_ingest.toml`)

### Phase 4: Cross-Gate Signal Gossip

When multiple gates have bloom sensors:
1. Each gate has its own signal spine
2. swarmVine gossips observation summaries between gates
3. The cross-gate DAG enables the cross-domain bridge detection we
   designed but haven't measured yet
4. The immune memory becomes mesh-wide — a fleet detected on one gate
   is remembered by all gates, with full provenance

---

## What This Enables for Investigation

### Traceable conclusions

Every statement in the siltPond can reference a specific spine entry:

> "The group cluster at 7:30 AM on Oct 6 was identified from observation
> windows `spine:golgiBody:2026-10-06:w1380..w1390` using classifier
> `bloom-v1.0.0`. The engagement topology (attention + interest + divergence)
> was computed from these 10 windows. The raw observations are in CAS at
> `blake3:abc123...`."

### Reproducible analysis

Anyone (including future-us) can:
1. Pull the spine entry
2. Pull the CAS blobs it references
3. Re-run the analysis with the same classifier version
4. Get the same results
5. Or re-run with a newer classifier and compare

### Permanent immune memory

The organism's memory of visitor patterns persists across restarts,
deployments, and hardware changes. The signal spine can be moved to a new
gate, forked for experimentation, or archived for long-term pattern analysis.

When the 6:01 AM → 7:30 AM hypothesis (AI retrieval → group cluster)
recurs next week, we can compare the two events with full provenance:
same classifier? Same observation window parameters? Same bloom sensor
version? The comparison is auditable because both events are in the spine.

### Investigation lineage

The siltPond's investigation threads trace back to signal data:

```
siltPond hypothesis → bloom observation windows → spine entry → CAS blobs
                        ↑                          ↑
                   classifier v1.0.0          Merkle root
                   (traceable)                (verifiable)
```

If the classification rules change (e.g., we discover a new spoofed
crawler pattern), we can re-analyze the historical observations with the
new rules and compare results. The old analysis and new analysis both
exist in the DAG — the fork documents the evolution.

---

## Connection to Upstream Architecture

The signal braid follows exactly the same pattern as the data braid
(`data_braid_ingress.toml`) and the depot lineage (`depot_lineage.toml`):

| Pattern | Data Braid (westGate) | Depot Lineage | Signal Braid |
|---------|----------------------|---------------|-------------|
| Content | Dataset files (BLAKE3) | Binary (BLAKE3) | Observation windows (BLAKE3) |
| DAG | Per-file events, batch | Single binary event | Per-window events, chained |
| Spine | 1 entry per dataset | 1 entry per binary build | 1 entry per day |
| Sign | Merkle root signed | Binary hash signed | Daily root signed |
| Braid | Dataset attribution | Build attribution | Observation attribution |

The POINTER_LAYER_ORTHOGONAL_REUSE.md pattern is visible again: the same
DAG/spine/braid architecture applied to a third orthogonal domain. Data
provenance, binary provenance, signal provenance — structurally isomorphic,
domain-independent.

---

## Privacy Constraint

The signal braid inherits the ecosystem's privacy guarantees:

- **No IPs enter the braid at any layer** — stripped before bloom
  sensor ingestion, never present in observations
- **Observation windows are population aggregates** — counts, not records
- **The DAG contains classified patterns, not raw requests**
- **CAS stores observation blobs, not log lines**
- **The braid's attribution records the analyst and methodology,
  not the visitors**

The spine enables immune memory without surveillance memory. The organism
remembers *what patterns it saw* without remembering *who generated them*.

---

*subGen Wave 164d — Signal braid architecture. The provenance trio
(sweetGrass/loamSpine/rhizoCrypt) maps to signal ingestion as immune
lineage: CAS for content identity, DAG for observation chains, spine for
permanent memory, braid for attribution. Phase 1 (spine lite in
skunky-ingest) requires zero new dependencies. The organism gets memory
that survives restarts, lineage that traces conclusions to data, and
branches that track classifier evolution. The same pointer-layer pattern
applied to data, binaries, and now signals — convergent architecture
across orthogonal domains.*
