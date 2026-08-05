# Latency Folding — Hardware Topology for Data CAS Systems

**Status**: PROVEN | **Wave**: 156a latency-folded | **Date**: Aug 5, 2026 PM
**Gate**: westGate (Data NAS — 62 GB DDR4, 2TB NVMe, 2TB SSD, 5×14TB raidz1)
**Team**: Hardware / Overwatch
**Audience**: Gate builders, infra teams, future hardware acquisition

---

## Context

Early generational documents theorized concepts that are now proven under
production load. gen1 (`SOVEREIGN_HPC_EVOLUTION.md`) projected the hardware
thesis — commodity hardware at sovereign cost. gen2 (`INTERSYSTEM_TRUST.md`)
defined the protocol layer. gen4 (`SILICON_DEISM_HARDWARE_GUIDE.md`) mapped
the ISA and OS coverage matrix.

What none of those documents addressed was the **I/O topology inside a single
gate**: how storage tiers interact under mixed workloads, where the bottlenecks
emerge, and how the Rust primals' speed exposes (rather than causes) hardware
contention.

Wave 156a proved this through operational pressure — a 4-worker convoy braiding
11M+ files through the provenance trio on westGate's ZFS pool. The primals were
never the bottleneck. The bottleneck was always the storage topology underneath
them. This document records what we learned and what it means for future builds.

---

## Latency Folding — The Principle

Latency folding is a design pattern: each layer in the system folds away a
class of latency so the layers above it never experience it.

| Layer | Folds Away | Latency Class | Example |
|-------|-----------|---------------|---------|
| **L1 cache** | Register spills | ~1 ns | CPU internal — not managed |
| **RAM (ZFS ARC)** | Disk seeks | ~100 ns | Hot CAS objects served from memory |
| **NVMe** | Spinner random I/O | ~100 μs | CAS writes land on flash |
| **SSD (L2ARC)** | Cold HDD reads | ~1 ms | Warm read cache for repeated access |
| **HDD raidz1** | Re-download | ~10 ms seek | Archive — data lives here permanently |
| **10G LAN** | WAN latency | ~50 μs | Inter-gate data at near-memory speed |
| **1G WAN / fiber** | No access | ~20 ms RTT | Initial download — happens once |

The same principle operates at every scale:

- **Within a gate**: RAM folds NVMe latency; NVMe folds spinner latency;
  SSD caches fold cold-read latency.
- **Across the LAN**: 10G backbone folds WAN latency. A gate pulls data
  from westGate at 10 Gbps instead of re-downloading at 1 Gbps.
- **Across WAN**: golgiBody's VPS depot folds public internet for gates
  without LAN access (blueGate pulling binaries).

This is not new computer science. What's new is applying it systematically
to a content-addressed storage system with cryptographic provenance — where
every tier must preserve the BLAKE3 → CAS → DAG → Merkle → signature → braid
chain regardless of which hardware serves the object.

---

## What gen1–gen4 Theorized

### gen1: Commodity Hardware Thesis

gen1 (`SOVEREIGN_HPC_EVOLUTION.md`) proved that ~$11K of commodity hardware
could match cloud HPC. The thesis was validated: 9-gate mesh, 104 TFLOPS FP64,
~$485/mo metabolic cost.

**What gen1 didn't address**: I/O topology within a gate. gen1 assumed storage
was "ZFS on spinners" and moved on. The implicit assumption was that disk I/O
would not be the bottleneck for provenance operations.

### gen2: Protocol Layer

gen2 (`INTERSYSTEM_TRUST.md`, `BTSP`) defined how primals communicate —
JSON-RPC 2.0 over UDS, BTSP handshakes, capability routing. The protocol
layer is fast (16,352 RPCs/s over native sockets, 353× LAN improvement over
WAN).

**What gen2 proved without intending to**: The protocol layer is so fast that
the bottleneck shifts entirely to the storage layer beneath it. A primal
responding in 4ms per RPC call is idle 99% of the time if the disk underneath
it takes 36ms to complete a write.

### gen4: Silicon Deism

gen4 (`SILICON_DEISM.md`, `SILICON_DEISM_HARDWARE_GUIDE.md`) proved ISA
independence (x86_64 + Windows, ARM planned) and projected the 10G backbone.

**What gen4 didn't address**: How the 10G backbone interacts with local
storage tiers. A 10G pipe to westGate is useless if westGate's spinners
can only serve at 100 MB/s random. The backbone folds WAN latency, but the
local storage tier determines serving throughput.

### gen4: 10G Backbone (Proven)

The CRS310↔Omada 10G AOC trunk is operational. This is the inter-gate latency
folding layer. What the convoy exploration revealed is that **the 10G pipe
needs an NVMe or SSD hot tier behind it** to serve data at speeds that
justify the backbone investment. Spinners behind 10G is a mismatch.

---

## What Wave 156a Proved

### The Rust Primals Are Not the Bottleneck

This was the single most important finding of the convoy exploration.

| Operation | Latency | Where It Happens |
|-----------|---------|-----------------|
| BLAKE3 hash (in-process Python) | 0.3 ms/MB | CPU + RAM |
| nestGate `content.put` (UDS) | 0.5 ms | Primal → storage backend |
| rhizoCrypt `dag.event.append` | 4 ms | In-memory DAG |
| loamSpine `session.commit` | 10 ms (once) | One spine entry per dataset |
| bearDog `crypto.sign_ed25519` | 0.1 ms | Pure CPU |
| sweetGrass `braid.create` | 2 ms | Metadata only |
| **Total primal time per file** | **~5 ms** | — |
| **Disk write (spinner, random)** | **36 ms** | ZFS COW on raidz1 |
| **Disk read (spinner, cold)** | **15-30 ms** | Seek + rotational |

The primals complete their work in ~5ms. The disk takes 36ms to write a single
CAS object. The primals are **7× faster than the storage they sit on.** This
ratio inverts on NVMe (0.02ms write latency), which is why moving CAS writes
to NVMe immediately boosted convoy throughput by 2.7×.

### socat Was an Artificial Bottleneck

Before the convoy optimization, every RPC call spawned a `socat` subprocess
(~10ms overhead per call). With 4 RPC calls per file (hash, CAS put, DAG
append, spine commit), that was 40ms of subprocess overhead alone — more
than the actual primal work. Eliminating socat and using native Python
`socket.AF_UNIX` connections removed this entirely.

**Pattern**: Subprocess IPC is always wrong for hot-path operations. Native
sockets should be the default for any orchestration code talking to primals.

### ZFS COW Write Amplification Is Real

ZFS copy-on-write turns every 4KB random write into a full transaction:
allocate block → write data → update metadata → update uberblock. On raidz1
with 5 spinners, each logical write produces ~3× physical writes (data +
parity + metadata). The convoy's 80 logical CAS writes/s became 247 disk
IOPS, consuming the spinners' entire write bandwidth.

**Pattern**: Never do random writes on spinning raidz. Sequential writes
(rsync, `zfs send`) are 5-10× more efficient. The braiding tier should
always be flash-backed.

### NVMe Partitioning Works

westGate's 2TB NVMe is the OS drive. Only 177 GB is used for the OS (11%).
We pointed CAS writes at a directory on the same NVMe by repointing the XDG
symlink (`~/.local/share/nestgate/storage` → `/mnt/cas-hot`). Convoy
throughput jumped to **313/s instantaneous** (2.4× over spinner baseline).
Note: the `NESTGATE_STORAGE_PATH` env var is a dead letter — nestGate
resolves storage through `data_dir.join("storage")` using XDG paths. The
symlink is the actual tier control surface. The OS workload (light systemd,
primals, journal) does not contend with CAS writes because the access
patterns are orthogonal (sequential OS reads vs random CAS writes, both fast
on flash). After 1 hour the hot tier held 303 GB, absorbing at ~107 MB/s.

For future builds: dedicated NVMe per role is cleaner, but sharing works
fine when one role is light (OS) and the other is heavy (CAS). The 1.6 TB
of free NVMe on westGate was sitting idle — a latent capability.

### L2ARC Is Read-Only and That's Correct

The Crucial BX500 2TB as ZFS L2ARC provides a 65.9% hit rate on reads —
every second read is served from SSD instead of spinners. This is the correct
use of SSD in a read-heavy serving topology. Using the SSD for writes would
sacrifice the read cache. The NVMe should handle writes; the SSD should
handle read caching.

**Pattern**: Dedicate SSD to reads (L2ARC), NVMe to writes (hot ingest).
Don't mix roles on the same device.

---

## The 4-Tier Architecture

This generalizes from westGate's specific hardware into a pattern for any
data CAS gate:

```
T0: RAM (ARC)     — ~100 GB/s — Hottest reads, auto-managed by ZFS
T1: NVMe (hot)    — ~1.7 GB/s — Active braiding, CAS writes land here
T2: SSD (warm)    — ~500 MB/s — Read cache (L2ARC), federation pre-warm
T3: HDD (cold)    — ~28 MB/s  — Bulk archive, sequential access only
```

### Data Flow

```
1. DOWNLOAD  →  Internet at 1 Gbps
2. BRAID     →  NVMe: BLAKE3 + CAS put + DAG append (T1, random writes OK)
3. ARCHIVE   →  HDD: sequential rsync from NVMe to raidz (T3, off-peak)
4. SERVE     →  Auto-tiered: ARC → L2ARC → NVMe → HDD (fastest available)
```

Steps 2 and 3 are decoupled — braiding happens at NVMe speed, archival
happens later at sequential speed. This eliminates the contention that
collapsed convoy throughput when both happened on spinners simultaneously.

---

## The Braiding NUC Pattern

The cleanest architectural separation is a dedicated braiding appliance:

| Component | Braiding NUC | Data NAS (westGate) |
|-----------|-------------|-------------------|
| **Role** | Download + braid | Archive + serve |
| **NVMe** | 1× 2TB (all CAS) | Shared with OS or dedicated |
| **SSD** | None needed | L2ARC read cache |
| **HDD** | None | raidz1/raidz2 cold archive |
| **RAM** | 32 GB | 64-128 GB (ARC) |
| **Network** | 2.5G or 10G | 10G |
| **I/O pattern** | 100% random writes | 100% sequential writes + random reads |

The NUC downloads data, braids it on NVMe (hash, CAS, DAG, Merkle, sign,
braid), then pushes the fully-braided CAS objects to the NAS via songBird
federation. The NAS receives sequential writes of already-braided data —
spinners are happy, no contention, no COW amplification from random writes.

This is the inter-gate version of latency folding: the NUC folds the
braiding latency so the NAS never sees random writes. The 10G backbone
between them ensures the push is fast.

The NUC can also serve as a **pre-warming tier** for other gates: when
ironGate comes online and needs AlphaFold data, the NUC can serve it from
NVMe at 3.5 GB/s read speed while the NAS serves archival queries from
spinners. Hot and cold serving paths separated across hardware.

This pattern also generalizes to **enmeshing**: a new gate joins the network
and immediately starts receiving braided data from the nearest NUC or NAS.
No re-download, no re-braiding. The mesh delivers already-proven data.

---

## Lessons for Future Hardware Builds

### Proven Principles

1. **Separate read and write I/O paths.** Never braid on spinners. Never
   serve exclusively from NVMe (it fills up). Each tier does one thing well.

2. **NVMe is cheap insurance.** A $150 NVMe eliminates the spinner bottleneck
   entirely. westGate's 2TB NVMe was always there, underutilized.

3. **ZFS ARC is the best free cache.** At 98% hit rate, ARC eliminates most
   disk reads. More RAM = more ARC = fewer SSD/HDD reads. 128 GB RAM in
   future builds is the single highest-ROI upgrade.

4. **L2ARC is the second-best cache.** At 65.9% hit rate on reads that miss
   ARC, the SSD prevents most cold spinner reads. Dedicated SSD for L2ARC
   is worth it on any NAS gate.

5. **10G backbone needs fast local storage.** A 10G pipe is wasted if the
   serving tier can only push 100 MB/s. NVMe or SSD behind the 10G port
   ensures the backbone is utilized.

6. **Spinners are for cold bulk.** Sequential reads/writes only. raidz2
   at scale (8+ disks) for safety. Never random writes.

7. **The primals are fast.** The Rust primal stack processes a file in ~5ms.
   If throughput is low, the bottleneck is underneath the primals, not in them.

### Recommended Configurations

#### Data NAS (westGate-next)

| Component | Spec | Why |
|-----------|------|-----|
| CPU | Ryzen 7/9 or EPYC (16+ cores) | ARC management, primal threads |
| RAM | **128 GB ECC** | ARC cache — doubles current 62 GB |
| NVMe #1 | 1 TB (OS + system) | Dedicated OS drive |
| NVMe #2 | 2-4 TB (hot CAS) | Dedicated braiding tier |
| SSD | 2-4 TB (L2ARC) | Dedicated read cache |
| HDD | 8× 20TB raidz2 (320 TB raw) | Cold archive, sequential only |
| Network | 10G SFP+ | Federation backbone |

#### Braiding NUC

| Component | Spec | Why |
|-----------|------|-----|
| CPU | i7/i9 NUC or Ryzen mini (8+ cores) | BLAKE3 hashing, primal RPCs |
| RAM | 32 GB | Convoy workers, primal memory |
| NVMe | 1× 2TB (OS + hot CAS) | Only storage needed |
| SSD/HDD | None | No archival — pushes to NAS |
| Network | 2.5G or 10G | Federation push to NAS |

#### Compute Gate (strandGate-next)

| Component | Spec | Why |
|-----------|------|-----|
| CPU | EPYC / Threadripper (32+ cores) | Science compute |
| RAM | 128 GB ECC | GPU staging, ARC for pulled data |
| GPU | RTX 4090 or equivalent | Lattice QCD, ML inference |
| NVMe | 1× 1-2 TB (OS + scratch) | Local working set |
| SSD/HDD | None | Pulls braided data from NAS |
| Network | 10G SFP+ | Data pull from NAS |

---

## Hardware Topology Issues Encountered

| Issue | Impact | Resolution | Future Fix |
|-------|--------|------------|------------|
| NVMe shared with OS | Works but unclean | Directory on OS partition | Dedicated NVMe for CAS |
| SSD locked to L2ARC | No write tier available | Used NVMe for writes | 2 SSDs or NVMe+SSD split |
| Single raidz1 pool | Reads and writes share spinners | NVMe hot tier eliminated write contention | Separate pools or dedicated NVMe |
| 62 GB RAM (low for NAS) | ARC limited to ~40 GB | Works but leaves performance on table | 128 GB in next build |
| ZFS COW random write amplification | 80 IOPS → 247 IOPS on spinners | Sequential migration after braiding | Flash-backed braiding tier standard |
| No 10G on NUC tier | Can't do braiding NUC yet | Direct braiding on NAS for now | 10G NUC or 2.5G NUC |

---

## Relationship to Prior subGen Documents

| Document | What It Covers | What This Adds |
|----------|---------------|----------------|
| `SILICON_DEISM_HARDWARE_GUIDE` | ISA/OS coverage matrix | Storage tier topology within a gate |
| `PROVENANCE_TRIO_ARCHITECTURE` | DAG/spine/braid flow | Where each trio operation hits storage |
| `DATA_FEDERATION_STATUS` | What data exists | How data moves through tiers during ingest |
| `PIPELINE_PROOF` | Cross-gate deployment | Same latency folding at deployment level |
| `GPU_SCALING_HYPOTHESIS` | VRAM scaling per rung | Compute-tier storage needs (scratch NVMe) |

---

## The Evolutionary Arc

gen1 asked: "Can commodity hardware do sovereign HPC?"
gen2 asked: "What protocol binds them?"
gen4 asked: "Does it work on any hardware?"

This document answers: **"What hardware topology makes a CAS system fast?"**

The answer is latency folding — the same principle that makes the 10G LAN
backbone work (fold WAN latency), that makes BTSP 353× faster on LAN than
WAN (fold handshake RTT), and that makes ARC effective at 98% hit rate
(fold disk latency into RAM).

The primals were always fast. The protocol was always efficient. The storage
topology was the unstated assumption, and the convoy proved that when you get
it right (separate read/write tiers, flash-backed braiding, spinners for cold
bulk), the system's design thesis holds at scale.

The braiding NUC pattern extends this to the inter-gate level: fold braiding
latency into a dedicated appliance so the NAS never sees random writes. The
mesh delivers already-proven data. Every gate in the ecosystem benefits from
the topology of every other gate.

---

*subGen Wave 156a — Latency folding proven on westGate hardware. Convoy at
313/s instantaneous on NVMe hot tier (2.4× over spinner baseline). Rust
primals at ~5ms/file — every issue was topology, latency, or jelly strings,
never the binaries. 4-tier architecture (RAM/NVMe/SSD/HDD) documented.
`NESTGATE_STORAGE_PATH` env var is dead letter; XDG symlink is the actual
tier control surface. Braiding NUC pattern defined. Future builds: dedicated NVMe per
role, 128 GB RAM, 10G backbone, separate read/write paths. The hardware
thesis holds — it just needed the right topology.*
