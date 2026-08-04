# Provenance Trio: Architecture Analysis, Misalignment, and Evolution Path

**Status**: Overwatch architecture analysis — provenance system at scale
**Wave**: 156a | **Date**: Aug 4, 2026
**Gate**: westGate (Data NAS — ZFS raidz1, 5×14TB, 1.19 TB used / 49.5 TB free)
**Team**: Hardware / Overwatch
**Audience**: Upstream primals teams, biomeOS signal team, spring subteams, overwatch

---

## Context

westGate holds ~1.2 TB across 131 datasets (1.17M files). The data acquisition
campaign hit a provenance throughput wall: at 187K spine entries, `loamSpine
entry.append` took **3.5 seconds per file** — a 700× degradation from fresh-spine
performance. This AAR-level investigation uncovered a deeper architectural
misalignment between how the scripts were calling the provenance trio and how the
trio was actually designed.

The core finding: **per-file spine entries were never the canonical provenance
architecture.** The scripts were doing it wrong.

---

## The Provenance Trio — How It Actually Works

Five primals, three layers, coordinated at the biomeOS signal graph level.

### Layer 1: Content Identity (nestGate CAS)

nestGate provides content-addressed storage — BLAKE3 hash → blob storage. This
is the identity layer ("this blob is this hash"). CAS sits upstream of the trio
proper. Operations: `content.put`, `content.get`, `content.exists`.

### Layer 2: Ephemeral Working Memory (rhizoCrypt DAG)

Session-scoped directed acyclic graph. Per-file vertices with hash, event type,
parents, agent, metadata. **In-memory by default — O(1) append at 4ms.** Already
has G31 batch operations: `dag.event.append_batch`, `dag.pipeline.ingest`.

Dehydration computes a Merkle root over all vertices (BLAKE3 binary tree in
topological order). This is the cryptographic binding of the entire file set.

### Layer 3: Permanent Record (loamSpine Ledger)

Append-only hash-chain spine. The canonical permanence operation is
**`session.commit`** — one spine entry per dehydrated DAG session, carrying the
Merkle root. Also supports certificates, proofs, temporal anchoring, DID
ownership.

The redb storage backend serializes the entire spine as a monolithic MessagePack
blob on every `entry.append` call (deserialize all × 2 + serialize all × 1 =
3× O(n) per append). This is a storage implementation bug, not an architectural
requirement.

### Layer 4: Attribution (sweetGrass + bearDog)

sweetGrass creates W3C PROV-O braids — dataset-level semantic provenance
(source, license, contributor roles, derivation chains). bearDog provides
Ed25519 signing over the Merkle root. sweetGrass does not call rhizoCrypt or
loamSpine — it receives reference strings from the orchestrator.

### Canonical Data Flow

```
Per file (during acquisition):
  BLAKE3 → nestGate CAS → rhizoCrypt dag.event.append (4ms, O(1))

Per dataset (once, at completion):
  rhizoCrypt dag.dehydration.trigger → Merkle root
    → loamSpine session.commit (1 entry, carries root)
    → bearDog crypto.sign_ed25519 (signs root)
    → sweetGrass braid.create (attribution, references root + signature)
```

This is the architecture per `PROVENANCE_TRIO_INTEGRATION_GUIDE.md` (v2.0),
`loamSpine/specs/INTEGRATION_SPECIFICATION.md` §3, and
`loamSpine/specs/API_SPECIFICATION.md` §3.4.

---

## What the Specs Say About Per-File Spine Entries

**Not mandatory.** The designed permanence model is session-level, not per-file.

Evidence:

1. **loamSpine integration spec** (§3): rhizoCrypt is the primary producer via
   `commit_session()` → `EntryType::SessionCommit` with a `DehydrationSummary`
   and Merkle root — one entry per dehydrated session, not per vertex.

2. **loamSpine API spec** (§3.4): Orchestrators call `spine.create` once, then
   `session.commit`. The canonical commit path for completed work is
   `session.commit`.

3. **`rootpulse_commit`** and **`nest.complete_dataset`** signal graphs both
   finalize with `session.commit`, not per-file `entry.append`.

4. **`nest_store.toml`** commits once per store operation via `session.commit`.

Per-file spine entries appear only in interim/operational-layer constructs:

- `nest_acquire_file.toml` explicitly defines per-file `entry.append` — this is
  the **one signal graph** that perpetuates the interim pattern.
- westGate ad-hoc scripts (`bulk_ingest.py`, `revalidate_data.py`,
  `alphafold_prov_trailer.py`) adopted the per-file pattern from this signal graph.

The provenance divergence AAR correctly identified per-file spine appends as an
**implementation scaling problem**, not a spec requirement. Option 3 from that AAR
("deferred spining — derive spine from DAG at dehydration via `session.commit`")
aligns with the canonical loamSpine design.

---

## The Misalignment

| Layer | Canonical (specced) | westGate scripts (actual) | Impact |
|-------|---------------------|---------------------------|--------|
| Per-file | `dag.event.append` only (4ms) | `dag.event.append` + `entry.append` | 3.5s/file at 187K entries |
| Session end | `dehydrate` → `session.commit` (1 spine entry) | Same, plus N redundant spine entries | Wasted O(n) work |
| Signing | bearDog signs Merkle root, attached to braid | Signs but **orphans** the signature | Provenance loop not closed |
| Orchestration | biomeOS signal graphs | Python scripts call UDS sockets directly | biomeOS bypassed entirely |

### Why Per-File Spine Entries Collapse at Scale

loamSpine's redb storage backend stores all spine entries as a single MessagePack
blob under one key. Every `entry.append` call:

1. Deserializes the full blob to read current entries
2. Deserializes again to validate the new entry
3. Appends the entry
4. Re-serializes the entire array

At 187K entries this blob is several hundred MB. The triple O(n) serialization
produces the observed 3.5s per append. At 240M AlphaFold files, per-file spine
entries would take approximately **27 years**.

Meanwhile, `rhizoCrypt dag.event.append` runs in 4ms because DAG vertices are
stored individually in memory (O(1) insert). The DAG already contains every file
hash — the Merkle root over all vertices cryptographically binds the entire set.
Per-file spine entries duplicate this information with catastrophic performance.

---

## biomeOS Signal Architecture for Provenance

biomeOS has 30+ signal graphs already defined for provenance orchestration.
Three models exist:

### Model 1: Single-Artifact — `nest.store`

```
content.put → dag.event.append → session.commit → braid.create
```

One signal graph, full trio in one call. Used for individual file operations.

### Model 2: Data Federation Trilogy — declare → acquire → complete

```
nest.declare_dataset    →  manifest CAS, DAG session, spine, intent braid
        ↓
nest.acquire_file (×N)  →  content.put → dag.event.append → entry.append
        ↓
nest.complete_dataset   →  dehydrate → session.commit → sign → final braid
```

The `nest.acquire_file` step still uses per-file `entry.append` — this is the
**interim pattern** that should be evolved. Everything else uses session-level
commit.

### Model 3: Workflow — `rootpulse_commit`

Six-phase commit: dehydrate → sign → nestGate store → `session.commit` → braid.
Used for experiment/science commits.

### Neural API Routing

- `capability.call` routes individual primal operations via the capability
  registry (`config/capability_registry.toml`).
- Signal-tier requests (`nest.*`, `braid.*`) are intercepted by biomeOS and
  dispatched as signal graph executions (30 registered graphs in
  `graphs/signals/`).
- The data federation quartet (`nest.declare_dataset`, `nest.acquire_file`,
  `nest.complete_dataset`, `nest.ingest_dataset`) is registered in
  `capability_registry.toml` but not in the explicit route table — works via
  semantic fallback.

### What westGate Should Be Doing

Instead of Python scripts calling UDS sockets directly, westGate should be
dispatching through biomeOS signal graphs:

```
Current:   script → socat → rhizocrypt.sock → dag.event.append
Target:    script → neural_api.sock → nest.acquire_file → signal graph → trio
```

The declare → acquire → complete trilogy is the target pattern for data
federation. This is acknowledged technical debt — the scripts bypass biomeOS
entirely, calling primal sockets directly.

---

## The Fix: Align Scripts with Canonical Architecture

### What Changes

Remove `spine_entry_append` from per-file loops in all acquisition scripts.
Keep `spine_create` and `spine_session_commit` in the finalization phase. Wire
the bearDog signature into the sweetGrass braid metadata to close the provenance
loop.

```
BEFORE (per file — scripts):
  BLAKE3 → CAS → rhizoCrypt.append (4ms) → loamSpine.append (3,536ms)

AFTER (per file — canonical):
  BLAKE3 → CAS → rhizoCrypt.append (4ms)

AFTER (per dataset, once — canonical):
  rhizoCrypt.dehydrate → loamSpine.session.commit → bearDog.sign → sweetGrass.braid
```

### What's Preserved

- Full Merkle proof over all files (rhizoCrypt DAG vertices)
- Permanent record of the dataset (loamSpine `SessionCommit` with Merkle root)
- Ed25519 signature of the root (bearDog) — now attached to braid
- W3C PROV-O attribution braid (sweetGrass) — now includes signature
- CAS content addressing (nestGate)

### What's Removed

- Per-file `DataAnchor` entries in loamSpine (redundant with DAG vertices)
- The O(n) serialization bottleneck

### Risk

If a consumer needs per-file loamSpine entries (individual file certificate
proofs via `proof.generate_inclusion`), those would need to be generated from
the DAG after the fact. For the data NAS use case (proving dataset integrity,
not individual file certificates), the Merkle root is sufficient. The
`nest_acquire_file` signal graph retains per-file entries as an option.

---

## CAS Storage as an Evolving Frontier

CAS is the identity layer — the substrate beneath the trio. The trio answers
questions CAS cannot:

| Layer | Question | Answer |
|-------|----------|--------|
| **CAS** (nestGate) | "What is this blob?" | "This blob has this BLAKE3 hash" |
| **DAG** (rhizoCrypt) | "How do these blobs relate?" | "These hashes form this event graph with this Merkle root" |
| **Spine** (loamSpine) | "Is this Merkle root permanent?" | "This root is certified, timestamped, and anchored" |
| **Braid** (sweetGrass) | "Where did this data come from?" | "This dataset came from this source, licensed this way, attributed to this entity" |

The scaling challenge revealed by the provenance divergence is real: at 240M
files, the ephemeral layer (rhizoCrypt) handles it fine (in-memory, O(1)). The
permanence layer (loamSpine) collapses because its storage implementation
(monolithic MessagePack blob) doesn't match its architectural spec (metadata-only
store with separate entry indexing).

Three provenance states exist on westGate:

| State | Description | Path to Convergence |
|-------|-------------|---------------------|
| **Primordial** | On disk, no CAS, no DAG, no spine | `revalidate_data.py` → full chain |
| **CAS-only** | BLAKE3 hashed and in CAS, no DAG/spine/braid | DAG session + dehydrate + commit + braid |
| **Fully braided** | CAS + DAG + Merkle root + signature + braid | Converged — ready for spring consumption |

The convergence check pattern (`convergence_check.py`) reports which datasets
have achieved full provenance and acts as a trust gate for springs.

---

## Upstream Evolution Targets

### loamSpine Team

- Fix `save_spine` full-blob serialize to match `specs/STORAGE_BACKENDS.md`
  (store metadata only, index entries separately). The current redb
  implementation serializes the entire entry array as one MessagePack value.
- Add `spine.entry.batch` for use cases that legitimately need per-file entries
  (not the common case, but should be available).

### biomeOS Signal Team

- Update `nest_acquire_file.toml` to make the per-file `entry.append` node
  `required = false` (or remove it). Currently it's `required = true`.
- Wire `dag.pipeline.ingest` as a first-class data acquisition signal —
  rhizoCrypt's G31 batch does create + batch_append + dehydrate in one RPC.
- Add the data federation quartet (`nest.declare_dataset`, `nest.acquire_file`,
  `nest.complete_dataset`, `nest.ingest_dataset`) to the explicit route table
  in `route_table.rs` — currently works via semantic fallback only.

### westGate Migration

- Move from script-calls-UDS to `signal.dispatch` via Neural API. The declare →
  acquire → complete trilogy is the target pattern.
- This enables bandwidth governance, BTSP propagation, and composition broker
  hot-reload — all of which are available at the signal graph level but bypassed
  by direct socket calls.

---

## Files Changed in This Fix

| File | Change |
|------|--------|
| `scripts/bulk_ingest.py` | Remove per-file `spine_entry_append`; wire bearDog signature into braid |
| `scripts/revalidate_data.py` | Remove per-file `spine_entry_append`; wire bearDog signature into braid |
| `scripts/alphafold_prov_trailer.py` | Remove per-file `spine_entry_append`; remove stale import |

---

## Summary for Overwatch

The provenance trio architecture is sound — rhizoCrypt for ephemeral tracking,
loamSpine for permanent record, sweetGrass for attribution, bearDog for signing,
nestGate for CAS. The issue was a misalignment in how westGate's acquisition
scripts called the trio: per-file spine entries instead of the canonical
per-session commit pattern.

This misalignment was invisible at small scale (5ms per entry on fresh spines)
and catastrophic at AlphaFold scale (3.5s per entry at 187K, 27 years at 240M).
The fix aligns the scripts with the canonical architecture specced in the
integration guides and signal graphs. The provenance chain remains complete —
every file is tracked in the DAG, the Merkle root binds them all, the signature
proves integrity, and the braid attributes origin.

The deeper evolution is migrating from direct socket calls to biomeOS signal
graph dispatch. The signal infrastructure exists (30+ graphs, Neural API routing,
capability registry). The scripts predate it.

CAS storage as a concept is proven and stable. The frontier is the composition
layer above it — how primals interact at scale, how signal graphs orchestrate
multi-primal operations, and how the declare → acquire → complete pattern becomes
the standard data federation flow across all gates.

---

*The provenance trio isn't broken — it was being called wrong. The canonical
architecture handles 240M files: fast ephemeral tracking (4ms/file), one
permanent commit (per dataset), one signature (per root), one braid (per
dataset). That's what "grab once, prove forever" looks like at scale.*
