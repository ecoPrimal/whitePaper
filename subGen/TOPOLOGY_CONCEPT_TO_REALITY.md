# Topology: From Concept to Primals to Reality

**Status**: OPERATIONAL PROOF | **Wave**: 156d | **Date**: Aug 6, 2026
**Gate**: westGate (Data NAS — 62 GB DDR4, 2TB NVMe, 2TB SSD, 5×14TB raidz1)
**Team**: Hardware / Overwatch
**Audience**: Ecosystem architects, whitePaper contributors, future gate builders

---

## The Question This Document Answers

The ecoPrimals whitePaper describes a system of Rust primals — nestGate,
rhizoCrypt, loamSpine, sweetGrass, bearDog — that provide content-addressed
storage, DAG-based provenance, cryptographic spine commitments, attribution
braids, and Ed25519 signatures. These primals are fast: 16,352 RPCs/s over
native sockets, sub-millisecond BLAKE3 hashing, 4ms DAG appends.

The whitePaper also describes hardware: commodity NAS builds, raidz1 pools,
10G backbones, multi-tier storage.

**What the whitePaper couldn't describe until now** is what happens when
these two topologies — the primal interaction topology and the hardware
storage topology — meet under production load. This document records what
we learned when concept became reality at the scale of 11 million files,
1.3 terabytes, and 153 scientific datasets.

---

## Three Topologies

The word "topology" appears throughout ecoPrimals documentation, but it
describes three distinct things that interact in non-obvious ways.

### 1. Primal Topology: The Interaction Graph

The provenance trio defines a directed acyclic interaction:

```
data  →  BLAKE3  →  nestGate (CAS put)
                        ↓
                    rhizoCrypt (DAG event)
                        ↓
                    loamSpine (spine commit)
                        ↓
                    bearDog (sign)
                        ↓
                    sweetGrass (braid)
```

This is a pipeline. Each primal depends on the output of the previous one.
The ordering is not arbitrary — you cannot create a DAG event without the
CAS hash, you cannot commit to the spine without the Merkle root, you
cannot sign without the spine tip.

**What gen1–gen3 assumed**: This pipeline would be the performance constraint.
Design focused on making each primal fast: native sockets instead of HTTP,
batch RPCs, in-memory DAGs, zero-copy I/O.

**What production proved**: The primals are so fast that the pipeline completes
in ~5 ms per file. The bottleneck is not the primal topology. The bottleneck
is what happens at each node in the graph — specifically, the disk I/O that
nestGate's `content.put` triggers.

### 2. Hardware Topology: The Storage Tier Graph

```
RAM (ARC 18-31 GB)  ←─ reads ─→  NVMe (2TB)  ←─ reads/writes ─→  SSD (L2ARC)
                                      ↑↓ writes
                                  HDD raidz1 (70TB raw, 50TB usable)
```

Each tier has different latency characteristics:

| Tier | Read Latency | Write Latency | Bandwidth |
|------|-------------|---------------|-----------|
| ARC (RAM) | ~100 ns | — | 5.9 GB/s |
| NVMe | ~100 μs | ~100 μs | 2.5 / 1.5 GB/s R/W |
| SSD (L2ARC) | ~1 ms | — | ~500 MB/s |
| HDD raidz1 | ~10 ms (seq) / ~36 ms (rand) | ~36 ms | 161 / 28 MB/s seq/rand |

**What gen1 assumed**: ZFS on spinners would be adequate for CAS.

**What production proved**: ZFS copy-on-write on raidz1 converts every CAS
write into a random write. BLAKE3 hashing reads files sequentially, but
CAS stores them by content address — the physical location on disk bears
no relation to the logical order of ingest. A spinner-backed CAS pool
serves random I/O at 28 MB/s. The primals' 5 ms pipeline sits idle for
36 ms while the disk completes each write.

### 3. Interaction Topology: The Ordering of Operations

This is the topology that only becomes visible under production load. It
is not the primal pipeline (which is fixed) or the hardware tiers (which
are physical). It is the ordering of operations across both.

**Example 1: Staging order matters.**

Reading files from HDD and hashing them in-place: 0.1 files/s.
Copying files HDD→NVMe (sequential) then hashing from NVMe: 81–1500 files/s.

The primal operations are identical. The hardware is identical. The only
difference is the order: stage first, then braid. This converts random HDD
reads into sequential HDD reads (fast) followed by random NVMe reads (fast).

**Example 2: Dedup check order matters.**

First braid of nf_data_portal: 81 files/s (CAS writes to disk).
Second braid of nf_data_portal: 1481 files/s (CAS dedup returns immediately).

The primal operations and hardware are identical. The difference is that
`content.put` checks existence before writing. On the second pass, every
file is already CAS'd, so the disk write is eliminated entirely.

**Example 3: Chunk commit order matters.**

`InlineBraid`: one session for the whole dataset. Crash at 80% = 100% re-work.
`ChunkedBraid`: one session per chunk. Crash at 80% = 20% re-work.

The provenance chain is identical. The hardware is identical. The difference
is where the spine commits are placed — after each chunk vs. after the
entire dataset.

---

## How Concepts Became Primals

### Content-Addressed Storage (gen1 concept → nestGate primal)

**Concept** (gen1): Store data by its hash. Dedup is free. Verification is
constant-time.

**Primal** (nestGate): BLAKE3 hash → two-level directory tree
(`ab/cdef.../`) on the configured storage backend. `content.put` accepts
base64-encoded data over UDS, returns the hash. `content.get` retrieves by
hash. Cross-tier dedup checks warm and cold tiers before writing.

**Reality** (Wave 156a): The concept works. 866 GB CAS pool on ZFS + 303 GB
on NVMe. But the concept didn't anticipate that the storage backend's
topology would dominate performance. nestGate's `content.put` is 0.5 ms.
The ZFS COW write underneath it is 36 ms. The concept assumed the primal
was the bottleneck — it's the storage topology underneath.

### Provenance DAG (gen2 concept → rhizoCrypt primal)

**Concept** (gen2): Every data transformation is a vertex in a directed
acyclic graph. The graph is dehydratable — compress it to a Merkle root
for compact verification.

**Primal** (rhizoCrypt): `dag.session.create` opens a session.
`dag.event.append_batch` adds vertices with metadata.
`dag.dehydration.trigger` produces the Merkle root.
`dag.partial_dehydrate` checkpoints without closing.

**Reality** (Wave 156d): The DAG is fast (4 ms append, in-memory). But the
session model assumed one session per dataset. For a 1.3 TB dataset with
6 version directories, a single session meant no crash resume. The concept
needed evolution: multiple sessions on the same spine, each independently
dehydratable. rhizoCrypt already supported this — the `dag.session.create`
API creates independent sessions. The concept was always there; the
interaction topology (when to create sessions, when to commit) was wrong.

### Spine Commitments (gen3 concept → loamSpine primal)

**Concept** (gen3): A total-ordered chain of Merkle commitments. Each entry
proves that a session's data existed at a specific point in time.

**Primal** (loamSpine): `spine.create` with a name and owner.
`session.commit` appends a commitment with the session's Merkle root.
Multiple commits on the same spine are append-only — no contention.

**Reality** (Wave 156d): The spine is the enabler for chunked braiding.
Each `session.commit` is a bead on the strand. The `ChunkedBraid` pattern
commits after each chunk — if the process crashes, the committed chunks
are permanent on the spine. The spine is what makes crash resume possible
without re-hashing or re-DAGging committed data.

What we discovered: `spine.create` requires an `owner` field that the
original `InlineBraid` never passed. The spine was silently failing and
returning `"pending"`. Every spine created before Aug 6 was a no-op. The
primal was correct; the caller was wrong. The error was visible in the RPC
response — `"missing field 'owner'"` — but `_rpc_result` swallowed it.

### Attribution Braids (gen3 concept → sweetGrass primal)

**Concept** (gen3): A braid ties together CAS, DAG, spine, and signature
into a single verifiable attribution record.

**Primal** (sweetGrass): `braid.create` with the content hash, dataset,
license, committer, Merkle root, and signature.

**Reality**: The braid is the capstone. It only fires once per dataset
(or per chunked dataset finalization). Its topology position — last in the
pipeline — means it's never the bottleneck. But its existence is what
makes the entire chain verifiable by a third party.

### Convergence Backpressure (Wave 156d concept → sweetGrass + nestGate)

**Concept**: Don't download faster than you can braid. Don't braid faster
than you can drain to cold storage.

**Implementation**: `convergence_gate()` checks warm tier free space and
sweetGrass convergence lag. Returns GO/WAIT/STOP. Download scripts and
braiders call this in their main loops.

**Reality**: This pattern emerged from the ENOSPC event. The concept
didn't exist in gen1–gen4. It was born from operational pressure — the
system teaching us what it needed.

---

## Topology Impacts: What Ordering Taught Us

### The Jelly String Pattern

A "jelly string" is a configuration glue point where the wrong ordering
or the wrong binding causes silent degradation. Every jelly string we
found was a topology error — not a primal error or a hardware error, but
a mismatch in how they were connected.

| Jelly String | Topology Error |
|-------------|----------------|
| `NESTGATE_STORAGE_PATH` env var | Primal ignored it; XDG symlink was the real control surface |
| XDG symlink → NVMe | Hardware topology error: shared OS drive as CAS tier |
| Single-tier dedup check | Interaction error: `exists()` only checked active tier |
| No `owner` on `spine.create` | Interaction error: caller didn't match primal's API |
| `read_bytes()` for large files | Interaction error: Python memory model vs file size |
| Single session per dataset | Interaction error: no recovery point in the pipeline |

Every one of these was fixable without changing the primals' core logic.
The Rust binaries performed exactly as designed. The errors were in the
topology — how the primals were called, in what order, with what parameters,
over what storage.

### The Latency Revelation

gen1 expected the primals to be the bottleneck. They're not. The measured
primal pipeline is ~5 ms per file. The measured disk write on spinners is
36 ms. The ratio is 7:1 — the primals spend 7× more time waiting for
the disk than doing their own work.

This is actually good news. It means the primals scale with hardware.
Drop in an NVMe (write latency ~100 μs), and the 36 ms disappears. The
5 ms primal pipeline becomes the constraint, and suddenly you need parallel
workers to saturate the storage. On westGate, moving CAS writes to NVMe
gave an immediate 2.4× throughput increase (131→313 files/s).

### The Staging Insight

The most impactful topology discovery was staging. It's not a primal
feature or a hardware feature — it's an interaction ordering feature.

Without staging: the braider issues random reads to spinning disks. Each
read seeks to a different physical location. Throughput: ~0.1 files/s.

With staging: `rsync` copies data sequentially from HDD to NVMe. Then the
braider issues random reads to NVMe (where random = sequential in latency
terms). The total time is longer (you add the copy step), but the braiding
phase is ~1000× faster, and the copy phase runs at the HDD's best mode
(sequential reads, 161-254 MB/s).

This is latency folding applied to the interaction topology, not just the
hardware. The staging step folds the random-read latency class out of the
braiding step.

### The Chunked Spine Insight

`InlineBraid` was designed as a concept: one session, one spine, one
dataset. It works for small datasets processed inline during download.

`ChunkedBraid` was designed from operational pressure: AlphaFold has 6
version directories totaling 1.3 TB. `alphafold_structures` has 228
prefix directories with 5.4 million files. A single session for either
of these is fragile — any crash means starting over.

The chunked pattern uses primal capabilities that already existed:
- `dag.session.create` creates independent sessions (always could)
- `session.commit` appends to a spine (always could)
- `dag.partial_dehydrate` checkpoints without closing (always could)

The primals didn't need to change. The interaction topology changed —
where we place session boundaries, when we commit to the spine, what
we persist to disk between chunks.

---

## From Concept to Reality: The Timeline

| Phase | What Existed | What Was Missing |
|-------|-------------|-----------------|
| **gen1** (concept) | CAS thesis, commodity hardware thesis | I/O topology, tier awareness |
| **gen2** (protocol) | 16K RPCs/s, UDS sockets, BTSP | How protocol speed exposes hardware limits |
| **gen3** (primals) | nestGate, rhizoCrypt, loamSpine, sweetGrass, bearDog | Multi-tier CAS, chunked sessions, backpressure |
| **gen4** (silicon deism) | ISA independence, 10G backbone | How backbone interacts with local tiers |
| **Wave 156a** (convoy) | 4-worker parallel provenance | Discovery: primals fast, spinners slow |
| **Wave 156b** (ENOSPC) | NVMe hot tier activated | Discovery: hot tier is ephemeral, not permanent |
| **Wave 156c** (multi-tier) | Cross-tier dedup, backpressure | Wired SubstrateTiers into content.put |
| **Wave 156d** (chunked) | ChunkedBraid, staging, streaming hash | Crash resume, per-chunk spine commits |

Each wave didn't invent new primals. It discovered which existing primal
capabilities were unwired, which interaction orderings were wrong, and
which hardware topology assumptions were invalid.

**The primals were always fast enough. The topology was always the variable.**

---

## What This Means for the Ecosystem

### For Gate Builders

The primals are ready. If you build a gate and the provenance pipeline is
slow, the problem is your storage topology, not the primals. Profile your
tiers. Stage to the fastest one. Use `ChunkedBraid` for large datasets.
Configure `NESTGATE_WARM_PATHS`/`NESTGATE_COLD_PATHS`. The primals will
saturate whatever you put underneath them.

### For the WhitePaper

gen1–gen4 were correct in their theses. Commodity hardware works. Sovereign
cost works. The protocol layer works. ISA independence works. What the
whitePaper can now add is the operational proof: the primals' speed is
validated, the hardware topology is understood, and the interaction
ordering patterns are documented and deployable.

### For Future Generations

The pattern that emerged — concept → primal → operational pressure → topology
discovery → interaction evolution — is the development model. Don't try to
design the perfect interaction topology in advance. Build fast primals with
clean APIs, deploy them against real data, and let the operational pressure
reveal the topology errors. Every jelly string is a topology lesson. Every
ENOSPC is a design pattern waiting to be born.

The primals didn't evolve during this wave. The topology did. And that's
the point: the primals are the constants, the topology is the variable,
and the ecosystem's job is to find the topology that lets the constants
perform.
