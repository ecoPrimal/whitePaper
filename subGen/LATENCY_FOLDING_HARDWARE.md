# Latency Folding — Hardware Topology for Data CAS Systems

**Status**: PROVEN + PROFILED | **Wave**: 156d | **Date**: Aug 6, 2026
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

### Hot Tier Is Ephemeral Working Memory — Not Permanent Storage

The NVMe hot tier worked brilliantly for 5 hours (313/s), then filled the
1.8 TB OS drive to 100% and crashed the convoy. The failure mode revealed
the correct architectural pattern:

**The hot tier is rhizoCrypt's braiding workspace.** Data lands on NVMe
during active provenance sessions. Once `loamSpine spine.commit` seals
the session, the committed data is archival — it should drain to cold
(ZFS raidz1, optimized for sequential bulk writes). The hot tier should
never hold more than one session's worth of in-flight data.

```
nestGate content.put → NVMe warm tier (fast random write)
rhizoCrypt dag.event  → session accumulates on warm
loamSpine spine.commit → provenance sealed
    ↓ commit triggers drain
content.archive warm → cold (sequential rsync/zfs send)
    ↓ warm tier freed
NVMe ready for next session
```

This is analogous to ZFS's ZIL (intent log) at the application layer.
Writes land on fast storage, accumulate through a transaction (provenance
session), and flush to main pool on commit. The nest atomic should own
ALL its pools — warm and cold — and manage the transitions internally.

**What broke**: We repointed the XDG symlink from ZFS→NVMe with no drain
mechanism. CAS objects accumulated permanently on NVMe. Worse, the
single-path dedup check (`object_path.exists()`) only checked the NVMe
path, so ~600 GB of data already on ZFS was re-written to NVMe.

**What we deployed (Aug 6, 2026)**: Three changes to `nestgate-rpc`,
wiring `SubstrateTiers` into the `content.put` hot path:

| Function | What It Does |
|----------|-------------|
| `content_cas_write_path()` | Routes new CAS writes to first warm tier (`NESTGATE_WARM_PATHS`) |
| `content_cas_find_across_tiers()` | Dedup walks all warm + cold `SubstrateMount` paths before writing |
| `warm_tier_capacity()` | `statvfs` check rejects writes below `NESTGATE_WARM_MIN_FREE_BYTES` (10 GB) |

Env config: `NESTGATE_WARM_PATHS=/mnt/cas-hot`, `NESTGATE_COLD_PATHS=/mnt/nestgate/cold/zfs/cas`.
Verified live: warm writes ✓, same-tier dedup ✓, cross-tier dedup ✓.

**What remains unwired**:
- `nestgate-zfs/automation/tier_migration.rs`: `TierMigrationPlan` — drain
  hook on `spine.commit` (P1)
- `nestgate-cache/multi_tier.rs`: `MultiTierCache` promotion/demotion (future)

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

### Profiled Tier Speeds (Aug 6, 2026)

Benchmarked with `dd` on westGate production hardware under load (rsync
drain + bulk braider running simultaneously):

| Tier | Device | Read | Write | Measured |
|------|--------|------|-------|----------|
| T0 | RAM (ZFS ARC, 62 GB max) | **5.9 GB/s** | — | `dd` from cached ZFS file |
| T1 | NVMe (Samsung 970 EVO+ 2TB, PCIe 4.0 x4) | **2.5 GB/s** | **1.5 GB/s** | `dd` to `/mnt/cas-hot`, `oflag=direct` |
| T2 | SSD (Crucial BX500 2TB, SATA III, L2ARC) | **~500 MB/s** | — | SATA ceiling, dedicated read cache |
| T3 | HDD (5×14TB raidz1, SATA) | **161 MB/s** seq | **~28 MB/s** rand | `dd iflag=nocache` cold read |

Key ratios:
- ARC→NVMe: 2.4× (RAM is fastest, as expected)
- NVMe→HDD: **15.5× read**, **53× write** (this is why braiding on spinners was 0.1/s)
- SSD→HDD: 3.1× (L2ARC absorbs half of ARC misses at this ratio)
- NVMe write vs 10G NIC: 1.5 GB/s vs 1.25 GB/s — NVMe slightly exceeds backbone

ARC utilization: 8.7 GB active / 62 GB max. ZFS is conservative at 9% pool
fill. ARC hit rate: 96.5%. L2ARC hit rate: 48.6%. Combined cache hit rate
(ARC + L2ARC): ~98.1%.

These speeds informed the bulk braiding approach: stage datasets from HDD→NVMe
at 161 MB/s sequential, then braid from NVMe reads at 2.5 GB/s. The staging
rsync is the bottleneck (HDD-limited), but once staged, braiding runs at
NVMe speed — the same throughput profile as the convoy.

---

## westGate Upgrade Path (Same Chassis)

westGate runs on MSI B550 TOMAHAWK MAX WIFI (AM4, Ryzen 7 5700X). The board
has expansion capacity that can resolve every topology issue encountered:

### Current Expansion Inventory

| Slot | Current Occupant | Status |
|------|-----------------|--------|
| M2_1 (PCIe 4.0 x4, CPU) | Samsung 970 EVO+ 2TB (OS + CAS) | Occupied |
| M2_2 (PCIe 3.0 x4, chipset) | Empty | **AVAILABLE** |
| PCIe x16 (4.0, CPU) | RTX 3070 | Occupied |
| PCIe x16 (3.0 x4, chipset) | Empty | **AVAILABLE** (HBA card) |
| PCIe x1 (3.0, chipset) | Empty | **AVAILABLE** |
| SATA 1-6 | 5× HDD + 1× SSD | All occupied |
| RAM (4× DDR4 DIMM, 128 GB max) | 64 GB (configuration TBD) | Upgrade possible |
| NIC | 10 Gbps (enp4s0) | Active |

### Phase 1: No-Cost Fixes (Now — Done)

- Multi-tier CAS deployed (warm writes, cross-tier dedup, backpressure)
- High-water mark prevents ENOSPC on OS drive
- `NESTGATE_WARM_PATHS`/`NESTGATE_COLD_PATHS` replace symlink routing

### Phase 2: Dedicated CAS NVMe ($0 — Crucial T500 2TB on hand)

Add the Crucial T500 2TB (from existing inventory) in the empty M2_2 slot:

| What | Detail |
|------|--------|
| Slot | M2_2, PCIe 3.0 x4 (~3.5 GB/s ceiling) |
| Drive | Crucial T500 2TB (PCIe 4.0 x4, DRAM-cached, 1200 TBW) |
| Mount | `/mnt/cas-hot` (dedicated, not root partition) |
| Config | `NESTGATE_WARM_PATHS=/mnt/cas-hot` only |
| Impact | OS drive isolated. NVMe ENOSPC becomes impossible. |

The T500 is PCIe 4.0 but will run at PCIe 3.0 x4 speeds in M2_2 (~3.5 GB/s
read / ~3.0 GB/s write). Still 2× faster than the current 970 EVO+ measured
speeds. DRAM cache + high TBW endurance make it ideal for sustained CAS writes.

### Phase 3: RAM to 128 GB ($0 — biomeGate DDR4-3200 pull)

Full swap of current 2×32 GB DDR4-3600 with 4×32 GB DDR4-3200 from biomeGate:

| What | Detail |
|------|--------|
| Current | 2×32 GB DDR4-3600 CL18 (Corsair Vengeance) |
| Install | 4×32 GB DDR4-3200 (matched kit, biomeGate pull) |
| Freed | 2×32 GB DDR4-3600 → compute gate redeployment |
| ARC impact | ~110 GB available for ARC (up from ~62 GB max) |
| Trade-off | ~11% bandwidth reduction (3600→3200), 2× capacity gain |

For a NAS gate, doubling ARC capacity at slightly lower bandwidth is an
unambiguous win. ARC reads at DDR4-3200 (~5.2 GB/s) are still 4× NVMe
and 32× HDD random. The freed DDR4-3600 kit goes where latency matters
more than capacity.

### Phase 4: HDD Expansion (Future, Not Urgent)

Currently at 9% pool utilization (4.75 TB / 50.7 TB). Options:
- Replace 5×14 TB with 5×20 TB (same raidz1, 70 TB usable)
- Add HBA card (LSI 9207-8i) in PCIe x4 slot + 3-4 more HDDs → raidz2
- raidz2 preferred at 6+ disks for 2-disk redundancy

### Phase 2+3 Combined Cost: $0 (ecosystem repurposing)

Both upgrades use hardware already in the ecosystem inventory:
- Crucial T500 2TB NVMe — on hand, unused
- 4×32 GB DDR4-3200 — pulled from biomeGate (8× DIMMs was overwhelming its CPU)
- 2×32 GB DDR4-3600 — freed from westGate → redeployed to a compute gate

One maintenance window (~20 min), one power cycle, zero purchases. Resolves
all known topology jelly strings: dedicated NVMe for CAS, doubled RAM for
ARC. The ecosystem's surplus hardware is its own upgrade path.

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
| NVMe shared with OS | ENOSPC crashed convoy | Multi-tier CAS + backpressure deployed | Dedicated NVMe (M2_2 slot, ~$120) |
| SSD locked to L2ARC | No SSD write tier | NVMe handles writes; SSD correct as L2ARC | Keep SSD as L2ARC (proven pattern) |
| Single raidz1 pool | R/W contention on spinners | NVMe hot tier eliminated write contention | raidz2 at scale for redundancy |
| 62 GB RAM (low for NAS) | ARC at 8.7/62 GB active | Works at current scale | 128 GB DDR4 (~$120) |
| ZFS COW write amplification | 80 IOPS → 247 disk IOPS | Flash-backed braiding tier standard | Always braid on NVMe, never spinners |
| No braiding NUC yet | All I/O on NAS | Direct braiding on NAS for now | NUC when ironGate joins mesh |
| Cross-tier dedup missing | 600 GB re-written to NVMe | `resolve_cas_object` walks all tiers | Deployed ✓ |
| No backpressure | NVMe filled to 100% | `warm_tier_min_free` (10 GB floor) | sweetGrass convergence-aware flow |

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

## Ideal Dedicated CAS Gate — Bill of Materials

For a purpose-built CAS gate (westGate-next or a new gate):

| Component | Spec | Est. Cost | Rationale |
|-----------|------|-----------|-----------|
| CPU | AMD Ryzen 9 7950X (16C/32T) or EPYC 4244P (8C/16T ECC) | $400-800 | Primals are I/O bound; more cores = more convoy workers + ARC mgmt |
| RAM | 128 GB DDR5 (Ryzen) or DDR5 ECC (EPYC) | $300-500 | ~96 GB for ARC. Single highest-ROI spec for a CAS gate |
| NVMe #1 (OS) | 500 GB - 1 TB (any reliable) | $50-80 | System only. No CAS data. Eliminates ENOSPC class entirely |
| NVMe #2 (Hot CAS) | 2-4 TB high-endurance (Samsung 990 Pro, WD SN850X) | $150-300 | `NESTGATE_WARM_PATHS` exclusive. Write endurance > speed |
| SSD (L2ARC) | 2-4 TB SATA (Crucial MX500, Samsung 870 EVO) | $100-200 | Dedicated ZFS L2ARC. SATA is fine — L2ARC is sequential read |
| HDD | 8×20 TB raidz2 (~256 TB usable, 2-disk redundancy) | $2,000-3,000 | Cold archive. Sequential writes from NVMe drain. HBA card for SATA |
| Network | 10G SFP+ (or 2×10G bonded) | $30-100 | Federation backbone. NVMe or ARC behind it to avoid bottleneck |
| Board | AM5 (B650/X670) or EPYC SP5 | $200-500 | AM5: 3-4 M.2 slots. EPYC: 128 PCIe lanes, ECC |

**Total estimated**: ~$4,000-5,000 (Ryzen build), ~$6,000-8,000 (EPYC build).

**westGate minimal upgrade** (same chassis): Crucial T500 2TB (M2_2) + 4×32 GB DDR4-3200 (biomeGate pull) = **$0** (ecosystem repurposing).

---

*subGen Wave 156d — Latency folding proven and profiled on westGate hardware.
Tier speeds measured: ARC 5.9 GB/s, NVMe 2.5/1.5 GB/s R/W, SSD ~500 MB/s,
HDD 161 MB/s seq / 28 MB/s rand. Convoy at 313/s on NVMe (2.4× over spinner
baseline). Multi-tier CAS deployed with cross-tier dedup, warm routing, and
high-water mark backpressure. Upgrade path defined: Phase 2 (Crucial T500 2TB, on hand) + Phase 3
(4×32 GB DDR4-3200, biomeGate pull) = $0 to resolve all known jelly
strings. Ideal dedicated CAS gate spec'd at $4-8K. Braiding NUC pattern for
download/braid offload. The hardware thesis holds — commodity hardware at
sovereign cost, but only with the right storage topology.*
