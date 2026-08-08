# Data Staging I/O Patterns: When Hardware Topology Meets Data Shape

**Status**: EXPERIMENTAL PROOF | **Wave**: 156d | **Date**: Aug 7, 2026
**Gate**: westGate (Data NAS — 62 GB DDR4, 2TB NVMe, 2TB SSD L2ARC, 5×14TB raidz1)
**Team**: Hardware / Overwatch
**Audience**: Ecosystem architects, gate operators, whitePaper contributors
**Prereqs**: TOPOLOGY_CONCEPT_TO_REALITY.md, CHUNKED_SPINE_BRAIDING_PATTERNS_AAR

---

## The Problem

The TOPOLOGY_CONCEPT_TO_REALITY piece established that the bottleneck in
provenance braiding is never the primal pipeline (~5 ms/file) — it is always
data movement between storage tiers. The question left open was: **does it
matter *how* we move data between tiers, and does the answer depend on the
shape of the data?**

The intuitive assumption was "no" — a file copy is a file copy. The
experimental evidence says otherwise, and the implications reach beyond
braiding into every data pipeline the ecosystem will ever run.

---

## The Experiment

### Hardware Under Test

| Tier | Medium | Capacity | Sequential BW | Random IOPS |
|------|--------|----------|---------------|-------------|
| T0 (ARC) | DDR4 RAM | 25.6 GB active | >10 GB/s | N/A |
| T1 (Hot) | NVMe Samsung 990 Pro | 1.8 TB | 3+ GB/s | ~1M |
| T2 (Warm) | SSD L2ARC | 2 TB (5.1 TB indexed) | ~500 MB/s | ~50K |
| T3 (Cold) | 5× Seagate 14TB raidz1 | 63.7 TB | ~600 MB/s | ~500 |

Cache effectiveness at time of test: ARC 96.2% hit rate, L2ARC 5.1 TB
indexed. Only 1.8% of reads reach spinning rust under normal workload.

### Data Taxonomy

Scientific datasets are not uniform. They fall into distinct I/O profiles
that interact with the storage hierarchy in fundamentally different ways:

| Type | Profile | Example | File Count | Avg Size | I/O Character |
|------|---------|---------|-----------|----------|---------------|
| A | Many small files | AlphaFold CIF structures | 5,000–7,000 per chunk | 100–300 KB | Metadata-heavy: readdir + stat dominate |
| B | Few large files | RNAcentral (.gz) | 1–5 | 1–10 GB | Bandwidth-bound: sequential read |
| C | Medium archives | SRA FASTQ (.fastq.gz) | 50–500 | 5–50 MB | Balanced: some metadata, mostly sequential |
| D | Moderate structured | Open Targets (.parquet) | 10–50 | 30–100 MB | Low metadata, sequential dominant |

This taxonomy is not arbitrary — it maps directly to the physics of spinning
disks vs. flash storage. The distinction that matters is **IOPS-bound vs.
bandwidth-bound**, and the dividing line is the ratio of `stat()` system calls
to actual data bytes read.

### Methods Tested

Three staging strategies for moving data from cold HDD to hot NVMe before
provenance braiding:

1. **rsync** (`rsync -a src/ dst/`): Per-file `stat()` + `readdir()` + copy.
   The traditional approach. Creates one seek per file for metadata resolution.

2. **tar-pipe** (`tar cf - -C src . | tar xf - -C dst/`): Sequential directory
   traversal. tar reads the directory in inode order, streams bytes linearly.
   One seek per directory, not per file.

3. **direct-ingest** (`content.ingest(cold_path)`): No staging — point the
   Rust CAS directly at cold storage and let it read from spinners.

### Controls

Each test used a cold (uncached) chunk. ARC/L2ARC state was recorded before
and after via `/proc/spl/kstat/zfs/arcstats`. `zpool iostat 2` sampled
throughout. Concurrent braiding workers were active on other chunks, creating
a realistic shared-I/O environment.

---

## Results

### Type A: Many Small Files — The Decisive Case

| Method | Wall Clock | Staging | Ingest | Effective MB/s |
|--------|-----------|---------|--------|----------------|
| **tar-pipe** | **192s** | 187s | 4.5s | 7.8 |
| rsync | 314s | 301s | 12.9s | 4.9 |
| direct | 754s | — | 754s | 2.7 |

**tar-pipe wins by 1.6× over rsync and 3.9× over direct.**

This is the result that matters. AlphaFold structures — the largest single
dataset in the federation (989,423 files, ~1.5 TB) — is Type A. The dataset
that took the most wall-clock time is the one most sensitive to staging method.

*Why*: A directory with 6,000 files requires 6,000 `stat()` calls under rsync.
On spinning disks behind raidz1, each `stat()` requires a seek (~8ms average
for 7200 RPM). 6,000 × 8ms = 48 seconds of pure seek time per directory, before
a single data byte is read. tar avoids this by reading the directory in a single
sequential pass and streaming file data in inode order.

### Type B: Few Large Files — Method Doesn't Matter

| Method | Wall Clock | Notes |
|--------|-----------|-------|
| rsync | 89s | 102 MB/s sequential |
| tar | 117s | 78 MB/s (pipe framing overhead) |
| direct | 0s | `content.ingest` skips files >256 MB |

Both methods saturate available sequential bandwidth. The bottleneck is pure
data transfer, not metadata. rsync is marginally faster (no tar framing).

**Discovery**: `content.ingest` has an `INLINE_MAX_FILE_SIZE` limit of 256 MB.
Files larger than this are silently skipped. This is an open architectural item —
large-file CAS ingestion needs a streaming RPC or chunked upload path.

### Type C/D: Moderate Files — Equivalent

| Type | rsync | tar | Δ |
|------|-------|-----|---|
| C (351 files, 8 MB avg) | 35s | 37s | ~1:1 |
| D (18 files, 50 MB avg) | 22s | 16s | ~1:1 |

Below ~200 files, metadata overhead is negligible. Choose either method based
on convenience.

---

## The 15 MB/s Floor

Every method showed ~15.4 MB/s aggregate read from the ZFS pool. This was
initially alarming — a 5-drive raidz1 should deliver 300–600 MB/s sequential.

The explanation: the test ran alongside 2 active braiding workers processing
other chunks. The pool's ~500 random IOPS budget was shared across all
consumers. The 15 MB/s floor represents the achievable throughput in a
**contested I/O environment**, which is the realistic operating condition.

The relative speedups (tar 1.6× vs rsync) remain valid because both methods
competed for the same shared budget. In isolation, the gap would widen further:

| Method | Projected Isolated Throughput (Type A) |
|--------|---------------------------------------|
| tar | 200–400 MB/s (sequential, full stripe utilization) |
| rsync | 30–50 MB/s (stat-bound, seeks per file) |
| direct | 15–30 MB/s (Rust readdir + stat, cold reads) |

---

## The Decision Matrix

This matrix is now **implemented in `native_braid.py`** as `choose_staging_method()`:

| Data Profile | File Count | Avg Size | Optimal | Rationale |
|-------------|-----------|----------|---------|-----------|
| Many small | >200 | <1 MB | **tar-pipe** | Sequential readdir avoids seek storms |
| Few large | <50 | >100 MB | **rsync** | Sequential I/O, simpler error handling |
| Oversized dirs | >100K | <1 MB | **find+tar batched** | Prefix-filtered tar in NVMe-sized batches |
| Moderate | 50–200 | Any | **either** | No meaningful performance difference |

---

## Implications for the Ecosystem

### 1. Data Shape Is an Architectural Primitive

The Type A/B distinction is not specific to braiding. Any pipeline that
reads scientific data from cold storage will encounter the same I/O patterns.
Genomic variant files (VCF), protein structure collections (CIF/PDB),
metagenomic reads (FASTQ) — each has a characteristic I/O shape that
determines how it should move through the storage hierarchy.

**Recommendation**: Every dataset in the federation should carry a `data_type`
annotation (A/B/C/D) in its provenance metadata. Downstream pipelines — spring
compute jobs, tideGlass queries, neuralSpring training runs — can use this
annotation to choose optimal staging without re-discovering it experimentally.

### 2. The Ephemeral Hot Tier Is the Correct Architecture

direct-ingest (reading from cold) was 3.9× slower than staging to NVMe first.
This validates the ephemeral hot tier pattern from TOPOLOGY_CONCEPT_TO_REALITY:
**cold storage is for durability, not for work.** Data should always be warmed
to the fastest available tier before processing, then evicted when done.

The cost of the staging copy (187s for tar) is amortized across every file
in the chunk (~6K files). The per-file processing benefit on NVMe (sub-ms
random reads vs. 8ms seeks) compounds across the entire pipeline.

### 3. ZFS raidz1 IOPS Budget Must Be Managed

500 random IOPS across 5 drives is a hard ceiling. In a contested environment,
every unnecessary `stat()` call steals IOPS from productive data reads.
This directly connects to the scrolling lag observed during overnight downloads:
rsync to cold storage generates metadata I/O that competes with ARC cache fills.

**Mitigation strategies**:
- Backpressure-gated downloads: pause cold writes when warm-tier free space
  is low or when interactive I/O latency exceeds threshold
- Night-window scheduling: shift bulk downloads to low-interaction windows
  with explicit IOPS budgeting
- L2ARC pre-warming: before interactive sessions, `zfs send | zfs receive`
  hot datasets to ensure they're in L2ARC

### 4. The Batch Staging Pattern for Oversized Chunks

AlphaFold's A0 subdirectory (~400K files) exceeds NVMe capacity. The solution
is batch staging: `find` with filename prefix filters pipes into tar, creating
NVMe-sized batches (500 GB each). Each batch is staged, braided, and evicted
before the next arrives. This pattern generalizes to any dataset larger than
the hot tier.

```
find $COLD/A0/ -maxdepth 1 -name "AF-A0A*" -print0 | \
  tar --null -T - -cf - | \
  tar -xf - -C $NVME_STAGING/
# → braid batch on NVMe → evict → next prefix batch
```

The key insight is that **the prefix filter preserves sequential access** —
`find` walks the directory once, the tar pipe streams the filtered results
linearly. No random seeks for the excluded files.

### 5. content.ingest 256 MB Ceiling

nestGate's `content.ingest` silently skips files larger than 256 MB. This
means Type B datasets (large genomic files, compressed databases, raw
sequencing runs) cannot be ingested through the standard bulk path. They
require either:
- A streaming CAS ingest RPC (file → chunked → hash-per-chunk → reassemble)
- Pre-splitting large files into <256 MB chunks before ingest
- A dedicated large-file handler in the braiding pipeline

This is tracked as an open primal enhancement.

---

## Experimental Infrastructure

`staging_experiment.py` provides a repeatable benchmark framework:

- Accepts `--test N --method rsync|tar|direct` for targeted runs
- Instruments `zpool iostat` sampling (2s interval) throughout each run
- Records ARC/L2ARC hit deltas via `/proc/spl/kstat/zfs/arcstats`
- Measures peak RSS, wall clock, and effective MB/s
- Persists all results to `staging_experiment_results.json` for cross-run
  comparison

### Planned Follow-Up Experiments

1. **Idle-window Type A**: Re-run tar vs. rsync with no competing workers
   to measure true isolated throughput gap (projected 4–8× based on IOPS model)

2. **L2ARC warming experiment**: Stage a Type A chunk, evict from ARC, then
   re-read. Measure L2ARC hit rate improvement and its effect on subsequent
   braiding passes

3. **Batch size optimization**: For oversized chunks, vary the NVMe batch
   size (100 GB, 250 GB, 500 GB) and measure amortized staging overhead
   vs. per-batch startup cost

4. **content.ingest streaming**: When the large-file CAS path is implemented,
   benchmark direct cold-to-CAS for Type B to see if staging is still
   beneficial for sequential large files

5. **Cross-gate staging**: When songBird federation is live, measure the
   cost of staging from a remote gate's cold tier over 10 GbE LAN vs.
   local cold tier. If LAN NVMe-to-NVMe transfer exceeds local HDD-to-NVMe,
   remote-first may be optimal for certain workloads.

---

## Connection to Broader Architecture

This work connects three threads in the whitePaper:

- **TOPOLOGY_CONCEPT_TO_REALITY**: Established that hardware topology
  dominates primal topology. This document quantifies *how much* it
  dominates and shows that data shape is the missing variable.

- **PROVENANCE_TRIO_ARCHITECTURE**: The provenance pipeline assumes data
  is "available." This work defines what "available" means operationally:
  data must be on the correct tier before the pipeline can achieve its
  theoretical throughput.

- **SILICON_DEISM_HARDWARE_GUIDE**: The hardware guide specifies *what* to
  buy. This document specifies *how to use it* — the operational patterns
  that extract maximum throughput from commodity hardware.

The unifying principle: **topology is not just what you have, it's how data
flows through what you have.** The primal topology is fixed by design. The
hardware topology is fixed by budget. The data flow topology — staging
method, batch size, tier selection — is the degree of freedom that
determines actual performance. This is where operational learning happens.
