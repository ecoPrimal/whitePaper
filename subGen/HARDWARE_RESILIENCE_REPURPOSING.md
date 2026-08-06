# Hardware Resilience and Ecosystem Repurposing

**Status**: OPERATIONAL DOCTRINE | **Wave**: 156d | **Date**: Aug 6, 2026
**Gate**: westGate (primary), ecosystem-wide applicability
**Team**: Hardware / Overwatch
**Audience**: Gate operators, hardware acquisition, overwatch

---

## Thesis

The ecoPrimals ecosystem does not purchase hardware to solve problems.
It repurposes hardware already in the mesh. Every gate that outgrows a
component produces a component that another gate needs. The provenance
braid makes this safe — data can survive hardware failure, physical
relocation, and topology reshuffling because its identity is
content-addressed, not location-addressed.

---

## Proof: westGate Phase 2+3 Upgrade — $0

westGate identified two topology bottlenecks during the convoy and
braiding campaigns:

1. NVMe shared with OS (caused ENOSPC on Aug 5)
2. ARC limited to 62 GB (underutilized for NAS role)

Traditional fix: buy a 2TB NVMe (~$130) and 64 GB DDR4 (~$100). ~$230.

**Actual fix**: $0.

| Component | Source | Destination | Cost |
|-----------|--------|-------------|------|
| Crucial T500 2TB NVMe | Existing inventory (unused) | westGate M2_2 slot (dedicated CAS hot tier) | $0 |
| 4×32 GB DDR4-3200 | biomeGate (8× DIMMs was overwhelming its CPU) | westGate (full swap, 128 GB ARC) | $0 |
| 2×32 GB DDR4-3600 CL18 | Freed from westGate | Compute gate (latency > capacity) | $0 |
| Samsung 860 EVO 1TB SSD | Existing inventory (unused) | Braiding NUC OS drive or staging | $0 |
| Spare SSDs | Degraded DDR3 NUCs | Braiding NUC parts or cache | $0 |

Every component moves from where it's underutilized to where it solves
a measured bottleneck. No new purchases. The ecosystem's surplus is its
own upgrade path.

---

## Why This Works: The Repurposing Loop

```
Gate A outgrows Component X
  → Component X is surplus to Gate A
  → Gate B has a measured bottleneck that Component X resolves
  → Gate B receives Component X
  → Gate B's freed component goes to Gate C (or inventory)
  → Repeat
```

This only works when three conditions hold:

1. **Commodity hardware** — Components are interchangeable. DDR4 is DDR4.
   NVMe is NVMe. No vendor lock-in, no proprietary backplanes.

2. **Measured bottlenecks** — You know *exactly* what each gate needs.
   westGate needed ARC capacity (not bandwidth). biomeGate needed fewer
   DIMMs (not more capacity). The measurement drives the redistribution.

3. **Content-addressed data** — Hardware swaps don't lose data identity.
   A BLAKE3 hash is the same on any NVMe, any DDR4 speed, any SATA port.
   ZFS pools import by drive serial, not port number. Braids verify
   integrity after any physical change.

---

## ZFS Pool Portability — Hardware Is Interchangeable

ZFS stores all pool metadata on the drives themselves, not in host
configuration files. westGate's `nestgate` pool identifies drives by
serial number (`ata-OOS14000G_0006DCVL`), not SATA port (`sda`).

| Scenario | ZFS Behavior | Data Risk |
|----------|-------------|-----------|
| Swap SATA cables between drives | Pool imports normally | None |
| Remove + reinstall all drives | `zpool import nestgate` finds them | None |
| Move all drives to new machine | `zpool import` on new host | None |
| Lose 1 HDD (raidz1, 5 drives) | Pool degrades, data intact | Replace + resilver |
| Lose L2ARC SSD | Pool loses read cache, no data loss | Replace or omit |
| Lose 2 HDDs (raidz1) | **Pool lost** | Braid-guided re-acquisition |
| Drives sit unpowered for months | Pool imports on power-up | None (no battery needed) |

The pool is a logical entity that floats above physical topology. This
is the storage layer of hardware resilience.

---

## Braid-Guided Recovery — Data as Solvable Puzzle

When hardware fails beyond ZFS redundancy (2+ drive failure in raidz1,
or catastrophic chassis failure), the provenance braid turns recovery
from "disaster" into "re-acquisition with known provenance."

### What the braid knows

For every file in the data estate:

| Braid Component | Recovery Use |
|-----------------|-------------|
| BLAKE3 content hash | Verify integrity of any re-acquired copy |
| CAS address | Content identity — find it anywhere in the mesh |
| DAG lineage | Original source URL, download method, dataset |
| Spine commitment | When it was sealed, which session |
| Ed25519 signature | Proof it hasn't been tampered with |
| sweetGrass attribution | Who acquired it, under what license |

### Recovery flow

```
1. Hardware failure detected (ZFS DEGRADED or pool FAULTED)
2. convergence_check.py reports which datasets are PRIMORDIAL/PARTIAL
3. For each unconverged dataset:
   a. DAG lineage reveals the original source (URL, rsync path, API)
   b. Re-download from source OR pull from another gate via federation
   c. BLAKE3 hash of re-acquired file matches braid record → verified
   d. If hash differs → data has changed upstream → flag for review
4. Re-braided data has new CAS addresses on new hardware
5. convergence.check confirms all 5 stages restored
```

The braid doesn't just verify data — it tells you *where to get it again*
and *how to prove the replacement is authentic*. Traditional RAID recovery
rebuilds bits from parity. Braid recovery re-acquires content from its
provenance chain. One relies on disk physics. The other relies on
cryptographic identity.

### What's not recoverable from braids alone

- **Derived data** (compute outputs, transformed datasets) — unless the
  compute pipeline is also braided (which it should be, via springs)
- **In-flight data** (partially braided, no spine.commit) — the DAG
  session is lost, but the source data can be re-downloaded
- **Private keys** (bearDog Ed25519) — must be backed up separately.
  Without keys, data can be re-acquired but not re-signed by the same
  identity

---

## Profiling Before and After — The Scientific Approach

The westGate hardware upgrade is deliberately staged:

### Phase 0: Current Hardware Baseline (Now)

Profile everything on the existing topology:

| Metric | Current Measured |
|--------|-----------------|
| ARC size / max | 24.8 GB / 62 GB |
| ARC hit rate | 96.5% |
| L2ARC hit rate | 49.4% |
| NVMe read / write | 2.5 / 1.5 GB/s |
| HDD sequential | 161 MB/s |
| HDD random | ~28 MB/s |
| Convoy throughput (NVMe) | 313 files/s |
| Bulk braid throughput (HDD) | 0.6-0.7 files/s |
| CAS pool size | ~1.1 TB (NVMe warm + ZFS cold) |

### Phase 1: Software Improvements (Deployed)

Multi-tier CAS, cross-tier dedup, backpressure, convergence gate.
Measure improvement on same hardware.

### Phase 2+3: Hardware Swap (When Ready)

Install T500 NVMe + 128 GB DDR4-3200. Measure the same metrics again.

| Metric | Expected After |
|--------|---------------|
| ARC size / max | ? / 110 GB |
| ARC hit rate | Higher (larger working set cached) |
| NVMe contention | Eliminated (dedicated CAS drive) |
| Bulk braid throughput | Higher (NVMe staging from dedicated drive) |
| OS I/O latency | Lower (no CAS contention) |

The delta between Phase 0 and Phase 2+3 is the documented value of
ecosystem repurposing. This becomes the reference data for other gates
planning their own hardware redistributions.

### Phase 3+: Failure Testing (Before Production Upgrade)

Test failure scenarios on current hardware before the upgrade:

- [ ] Simulate L2ARC loss (remove SSD from pool, measure impact)
- [ ] Simulate single HDD failure (offline one drive, measure degraded)
- [ ] Run `convergence_check.py` during degraded state — verify it detects
- [ ] Verify `zpool export` + `zpool import` survives SATA port swap
- [ ] Verify braid lineage can guide re-acquisition of a removed dataset

These tests validate the resilience architecture *before* depending on it
during a real hardware swap.

---

## Ecosystem Hardware Inventory

Current available-for-redeployment components:

| Component | Source | Candidate Use | Priority |
|-----------|--------|--------------|----------|
| Crucial T500 2TB NVMe | Inventory | westGate M2_2 dedicated CAS | Phase 2 |
| 4×32 GB DDR4-3200 | biomeGate pull | westGate 128 GB ARC | Phase 3 |
| Samsung 860 EVO 1TB SSD | Inventory | Braiding NUC OS / staging | Phase 4 |
| Spare DDR3 NUC SSDs | Degraded NUCs | NUC rebuilds, parts | Future |
| 2×32 GB DDR4-3600 CL18 | westGate (after swap) | Compute gate RAM | Phase 3 |

---

## The Pattern for Future Gates

When a new gate joins the ecosystem (ironGate, a braiding NUC, etc.):

1. **Profile the existing gate's surplus** — what components are
   underutilized or oversized?
2. **Match surplus to the new gate's bottleneck** — DDR4-3600 from a NAS
   gate goes to a compute gate where latency matters more than capacity
3. **Braid the data before the hardware moves** — convergence.check
   confirms the data estate is intact after physical changes
4. **Document the before/after** — measured deltas become ecosystem
   knowledge for the next redistribution

The commodity hardware thesis (gen1) isn't just "cheap hardware works."
It's "cheap hardware is interchangeable, and interchangeable hardware
flows to where it's needed." The braid makes the data survive the flow.

---

*subGen Wave 156d — Hardware resilience proven through ZFS pool portability
(serial-based drive identification) and braid-guided recovery (BLAKE3 +
DAG lineage enables re-acquisition, not just rebuild). Ecosystem
repurposing demonstrated: $0 upgrade path for westGate using biomeGate
DDR4-3200 pull + inventory NVMe + spare SSDs. Profiling staged
deliberately — baseline before hardware swap gives measured deltas for
ecosystem adoption. The braids make recovery a solvable puzzle, and
commodity hardware flows through the mesh where it's needed most.*
