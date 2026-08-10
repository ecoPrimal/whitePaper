# SwarmVine Ant Colony Pattern & NUCLEUS Atomic Composition

**Status**: Overwatch architecture analysis — gossip substrate evolution
**Wave**: 157e | **Date**: Aug 10, 2026
**Gate**: westGate (overwatch)
**Team**: Hardware / Overwatch
**Audience**: All primal teams, biomeOS signal team, spring subteams, overwatch

---

## Context

Wave 157e deployed swarmVine on westGate as service 14/14 — the newest primal in the
ecosystem. During overwatch validation, we probed its capabilities, transport, and
interactions with skunkBat (vine-bat pre-accept loop). What emerged is a pattern
recognition: swarmVine is an **ant colony** — and the NUCLEUS atomic model maps
directly to how primals compose into the three atomic systems.

This document captures:
1. The ant colony pattern and its gossip vector evolution
2. How swarmVine fits into the Tower Atomic composition
3. The NUCLEUS atomic model (Tower / Node / Nest)
4. Interaction patterns between primals at full composition

---

## The NUCLEUS Atomic Model

NUCLEUS gates run three atomic systems — named by analogy to subatomic particles
not because they are small, but because they compose into something larger.

### Tower Atomic — The Electron (Communication & Topology)

The electron orbits the nucleus. It mediates all electromagnetic interaction — all
communication between atoms. Tower Atomic is the **communication substrate**:

| Primal | Role | Analogy |
|--------|------|---------|
| **songBird** | Capability discovery, mesh routing, peer registry | The orbital — defines reachability, shape of the communication shell |
| **swarmVine** | Epidemic gossip, cross-gate state propagation | The field — carries information between gates without direct coupling |
| **skunkBat** | Metadata validation, pre-accept defense | The spin — determines acceptance or rejection of incoming interactions |
| **cellMembrane** | Transport layer, riboCipher enforcement | The charge — the fundamental property that enables all interaction |

**Current state** (Wave 157e): songBird alive with 11 registrations and 1 mesh peer.
swarmVine alive with tarpc transport, TCP 7800 listening, vine-bat loop active.
cellMembrane deployed, riboCipher enforced. skunkBat alive, responding to
`metadata.analyze`.

### Node Atomic — The Proton (Compute & Silicon)

The proton is the massive, positively-charged particle. It defines the element's
identity — what the atom *is*. Node Atomic is the **compute substrate**:

| Primal | Role | Analogy |
|--------|------|---------|
| **toadStool** | Workload dispatch, resource management, sandbox | The strong force — binds compute resources, determines what can be done |
| **barraCuda** | GPU IPC, shader dispatch, silicon-aware routing | The mass — the raw computational capability, hardware-bound |
| **coralReef** | GEMM compilation, shader optimization | The binding energy — how efficiently compute resources combine |

**Current state**: toadStool dispatching workloads (v0.2.0, 16 cores, 63 GB).
barraCuda alive with NVIDIA 0x2484 detected. coralReef GEMM Phase 2 validated
on strandGate.

### Nest Atomic — The Neutron (Data & Provenance)

The neutron is the neutral, stabilizing particle. Without neutrons, nuclei above
hydrogen are unstable — they fly apart. Nest Atomic is the **data substrate** that
holds everything together:

| Primal | Role | Analogy |
|--------|------|---------|
| **nestGate** | Content-addressed storage, BLAKE3 identity | The neutral mass — stores without charge, gives weight and stability |
| **rhizoCrypt** | DAG sessions, Merkle trees, ephemeral working memory | The decay path — the neutron's internal structure, how data transforms |
| **loamSpine** | Certificates, spine commits, signed audit trail | The binding — what keeps the nucleus from flying apart, the audit chain |
| **sweetGrass** | Attribution, braids, convergence check | The stability — determines whether the isotope is stable or radioactive |
| **bearDog** | Ed25519 signing, key management, encryption | The weak force — rare but decisive interactions that change state |

**Current state**: Full provenance chain operational. 100 braids, 3 datasets
finalized. Ed25519 signing live (first signed commits in ecosystem history).
Pen test 86/87 PASS.

### The Electron Cloud — Visualization & Interaction Layer

Above the three atomics sits the interaction layer — how humans and systems
observe and interact with the atom:

| Primal | Role | Analogy |
|--------|------|---------|
| **petalTongue** | Visualization, WebGL scenes, data rendering | The photon — carries the observable information to the viewer |
| **squirrel** | AI orchestration, agentic interaction | The observer — interacts with the system, collapses possibilities into actions |
| **biomeOS** | Neural API, capability dispatch, graph execution | The Hamiltonian — the operator that governs evolution and routing |

---

## SwarmVine: The Ant Colony Pattern

### Why Ant Colony

An ant colony is a superorganism. No single ant has the full picture, but the
colony exhibits collective intelligence through simple rules:

1. **Pheromone trails** — ants lay chemical signals that evaporate over time
2. **Trail reinforcement** — active paths get stronger, abandoned paths fade
3. **Scouts** — individual ants explore, report back via trail
4. **Colony immune system** — guards at the nest entrance validate returning ants
5. **Multi-trail** — different pheromones for food, danger, nest location
6. **Riding** — ants ride on other organisms (birds, mammals) for long-distance transport

SwarmVine maps directly:

| Ant Behavior | SwarmVine Implementation | Status |
|-------------|--------------------------|--------|
| Pheromone trail | `GossipEntry` with TTL (default 8 hops) and expiry (10 min) | LIVE |
| Trail evaporation | TTL decrement on forwarding, epoch-based expiry | LIVE |
| Trail reinforcement | Monotonic `version` field — higher wins on conflict | LIVE |
| Three pheromone types | `GossipTopic::Tower`, `Data`, `Compute` | LIVE |
| Colony immune system | Vine-bat pre-accept via skunkBat `metadata.analyze` | LIVE |
| Nonce deduplication | 4096-entry nonce history prevents amplification | LIVE |
| Scout exploration | Local primals calling `gossip.inject` after events | NOT YET |
| Riding on a bird | `TransportEndpoint::MeshRelay` via songBird | TYPE EXISTS, NOT IMPLEMENTED |
| Riding on a bear | bearDog-signed gossip entries for trust chains | NOT YET |
| Multi-surface crawling | UDS + TCP + QUIC + mDNS discovery | TCP ONLY for cross-gate |
| Persistent trails | Durable gossip state surviving restarts | NOT YET (in-memory only) |

### Current Architecture (Wave 157e)

```
                   ┌─────────────────────────────────────┐
                   │          swarmVine (westGate)         │
                   │                                      │
                   │  ┌─────────┐  ┌────────┐  ┌───────┐ │
                   │  │  Tower  │  │  Data  │  │Compute│ │
                   │  │ gossip  │  │ gossip │  │gossip │ │
                   │  └─────────┘  └────────┘  └───────┘ │
                   │         │          │          │      │
                   │         └─────┬────┘──────────┘      │
                   │               │                      │
                   │    ┌──────────▼──────────┐           │
                   │    │   forward_queue     │           │
                   │    │  (drain → spread)   │           │
                   │    └──────────┬──────────┘           │
                   │               │                      │
                   │    ┌──────────▼──────────┐           │
                   │    │   vine-bat loop     │           │
                   │    │  skunkBat validate  │           │
                   │    └──────────┬──────────┘           │
                   └───────────────┼──────────────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
               TCP :7800     TCP :7800      TCP :7800
               (UNREACHABLE) (UNREACHABLE)
                    │              │              │
              sporeGate       ironGate        (future)
```

### Gossip Vector Evolution

The current swarmVine has one gossip vector: TCP peer-to-peer with hardcoded
addresses. The ant colony pattern implies many more:

**Phase 1 — Scout Injection (no new code in swarmVine)**

Local primals inject gossip entries after significant events. This requires no
swarmVine code changes — only callers using the existing `gossip.inject` RPC:

| Event | Injector | Topic | Key | Payload |
|-------|----------|-------|-----|---------|
| Braid finalized | `native_braid.py` or sweetGrass | Data | `braid.head:{dataset}` | `{braid_id, files, bytes, spine_id}` |
| CAS high-water | convergence drain | Data | `cas.pressure:{gate}` | `{usage_pct, tier, action}` |
| Build complete | sporeGate harvest | Tower | `depot.build:{primal}` | `{blake3, arch, version}` |
| GPU available | toadStool | Compute | `gpu.available:{gate}` | `{device, vram, personality}` |
| Signing ceremony | bearDog | Tower | `key.rotated:{gate}` | `{public_key, algorithm}` |
| Service health change | any primal | Tower | `health:{gate}:{primal}` | `{status, version}` |

**Phase 2 — Multi-Surface Transport**

| Transport | Mechanism | Use Case |
|-----------|-----------|----------|
| **TCP** (current) | Direct peer-to-peer, riboCipher prefix | LAN gossip between known gates |
| **songBird mesh relay** | `gossip.spread` piggybacked on `:7700` mesh | Cross-subnet, NAT traversal, rides the bird |
| **mDNS/SSDP discovery** | Multicast for automatic peer detection | Zero-config LAN enrollment (southGate, darwinGate) |
| **QUIC** | Multiplexed, encrypted, connection migration | Mobile gates, unreliable networks |
| **bearDog-signed entries** | Ed25519 signature on gossip payload | Trust chain for entries crossing trust boundaries |

**Phase 3 — Persistent Trails & Convergence**

| Feature | Mechanism | Benefit |
|---------|-----------|---------|
| **WAL-backed gossip** | Write-ahead log for gossip entries | Survive restarts, catch up with peers |
| **Convergent state** | CRDT-like merge for long-lived entries | Eventually-consistent topology view |
| **Trail strength metric** | Count of independent observations per key | Stronger trails = higher confidence |
| **Selective subscription** | `gossip.subscribe` with topic/key filters | Primals listen for what they care about |

---

## Tower Atomic Composition — How It Fully Evolves

When Tower Atomic reaches full composition, swarmVine becomes the connective
tissue between all gates. The interaction patterns:

### songBird ↔ swarmVine (The Bird Carries the Ant)

songBird manages the mesh — peer discovery, capability resolution, transport
negotiation. swarmVine rides on songBird's mesh for cross-gate gossip when
direct TCP is unavailable.

```
songBird discovers peer  →  swarmVine learns new gossip target
swarmVine discovers data  →  songBird learns new capability source
```

**Interaction**: songBird provides `mesh.peers` to swarmVine's `discover_peers()`.
swarmVine injects `Tower` gossip that songBird can use for capability freshness.
The bird finds the tree; the ant colony maps every branch.

### skunkBat ↔ swarmVine (The Bat Guards the Colony)

Every inbound gossip entry passes through skunkBat `metadata.analyze` before
acceptance. This is the vine-bat pre-accept loop — already live.

```
remote entry arrives  →  swarmVine calls skunkBat metadata.analyze
                      →  skunkBat returns verdict: allow / deny / quarantine
                      →  swarmVine accepts or rejects
```

**Evolution**: skunkBat learns from rejected entries. Patterns of malformed gossip
from a specific origin gate trigger reputation scoring. The bat remembers which
ants brought poisoned food.

### cellMembrane ↔ swarmVine (The Charge Enables the Field)

cellMembrane provides riboCipher transport — the `[0xEC, 0x01]` prefix that
authenticates all cross-primal communication. swarmVine already uses riboCipher
for both TCP gossip and skunkBat queries.

**Evolution**: cellMembrane could provide per-gate encryption keys for gossip
payloads, enabling encrypted gossip channels between trusted gates without
requiring bearDog per-entry signatures.

---

## Cross-Atomic Interactions

### Tower ↔ Nest (Electron ↔ Neutron: How Communication Serves Data)

swarmVine `Data` gossip carries braid HEADs, CAS availability, and content
freshness across gates. This is how the Nest Atomic on westGate (data CAS)
advertises to ironGate (NFT CAS) what's available for federation.

```
westGate braids AlphaFold  →  swarmVine injects Data gossip
                           →  gossip spreads to ironGate's swarmVine
                           →  ironGate's nestGate knows what's available
                           →  content.replicate pulls on demand
```

### Tower ↔ Node (Electron ↔ Proton: How Communication Serves Compute)

swarmVine `Compute` gossip carries GPU availability, workload capacity, and
build queue state. This is how strandGate (with AMD+NVIDIA GPUs) can advertise
available compute to the mesh.

```
strandGate GPU becomes idle  →  toadStool injects Compute gossip
                             →  gossip spreads to westGate's swarmVine
                             →  westGate biomeOS routes GPU workload
                             →  cross-gate dispatch via toadStool
```

### Nest ↔ Node (Neutron ↔ Proton: Data Feeds Compute)

The provenance trio (Nest) generates data that compute (Node) consumes.
Spring workloads (hotSpring QCD, wetSpring NCBI, neuralSpring ML) read
CAS-braided data and produce computed results that get braided back.

```
wetSpring reads NCBI data from CAS  →  GPU processes diversity analysis
                                     →  results braided into CAS
                                     →  swarmVine gossips new braid HEAD
                                     →  ironGate can federate the result
```

---

## The Visualization & Interaction Layer

### petalTongue — The Photon

petalTongue renders the observable state. When swarmVine gossip carries
`Data` entries about braid HEADs, petalTongue can render a live topology
map showing which gates hold which data. When `Compute` gossip carries
GPU utilization, petalTongue renders the compute landscape.

**Evolution**: `gossip.subscribe` with a WebSocket bridge to petalTongue
gives live topology visualization — watching the ant trails form in real time.

### squirrel — The Observer

squirrel provides agentic interaction. An AI agent can query swarmVine
`gossip.query` to understand the current state of the mesh, then make
decisions about where to route work or which data to request.

**Evolution**: squirrel subscribes to gossip topics and triggers automated
responses — "when a new braid HEAD appears for dataset X on gate Y,
initiate replication to gate Z."

### biomeOS — The Hamiltonian

biomeOS Neural API is the operator that governs system evolution. It resolves
capabilities, dispatches RPCs, and will eventually execute computation graphs.
swarmVine feeds biomeOS with fresh topology information via gossip, and
biomeOS uses that to make better routing decisions.

**Evolution**: biomeOS graph executor uses swarmVine gossip as input to
capability resolution — "route this content.get to the gate with the freshest
CAS for this hash" based on `Data` gossip rather than static registration.

---

## Jelly Strings → Primal Composition

The issues found during overwatch validation map to jelly strings that evolve
into proper primal composition:

| Jelly String | Current | Primal Composition Target |
|-------------|---------|---------------------------|
| Convergence drain path hardcoded in systemd | Python script in `deprecated/` | nestGate tier-aware ingest with rhizoCrypt convergence DAG |
| songBird registration via shell script | `songbird-register.sh` oneshot | Primals self-register via `primal.announce` on startup |
| swarmVine peers hardcoded in env var | `SWARMVINE_PEERS=sporeGate,ironGate` | Dynamic discovery via songBird `mesh.peers` + mDNS |
| No gossip injection from any primal | Zero entries in gossip table | Primals inject after significant events (braid, build, GPU) |
| Cross-gate gossip unreachable | TCP to fixed IPs, both down | songBird mesh relay + automatic peer discovery |
| Braid orchestration in Python | `native_braid.py` (4/7 jelly strings remaining) | biomeOS graph executor with Tower Atomic routing |

---

## Findings from Overwatch Validation

### What Works

- **14/14 services alive** on westGate
- **Vine-bat pre-accept loop** operational (skunkBat validates gossip before acceptance)
- **Three gossip domains** (Tower, Data, Compute) properly typed and separated
- **TTL-based epidemic spread** with nonce deduplication
- **Transport abstraction** in type system (UDS, TCP, MeshRelay)
- **Ed25519 signing** live — foundation for signed gossip entries
- **biomeOS FD leak fixed** — stable at 17 FDs after 2h

### What Needs Evolution

- **swarmVine gossip peers unreachable** — sporeGate:7800 and ironGate:7800 both down. Need songBird mesh relay or LAN topology fix.
- **Zero gossip entries injected** — no primal currently uses `gossip.inject`. The colony has no scouts.
- **`MeshRelay` transport** is a type variant returning `Unsupported`. songBird relay needs implementation.
- **Gossip state is ephemeral** — 10-minute TTL, in-memory only. Restarts lose everything.
- **swarmVine uses tarpc on UDS** — JSON-RPC dispatch exists on the TCP gossip port but local IPC is tarpc-only, making it inaccessible to Python orchestration and biomeOS Neural API routing.

### What Surprised Us

- swarmVine's architecture is cleaner than expected for a v0.1.0 primal. The three-domain gossip model, vine-bat validation, and transport abstraction show forethought.
- The `GossipEntry.for_forwarding()` method (TTL decrement + clone) is the exact ant trail evaporation mechanism.
- skunkBat integration is graceful: if skunkBat is unreachable, default to allow. The colony works without guards; guards make it stronger.

---

## Execution Priority for Overwatch

### Immediate (can be done from overwatch)

1. **Inject gossip from `native_braid.py`** — after braid finalization, call `gossip.inject` with a `Data` topic entry for the new braid HEAD. Zero swarmVine code changes needed.
2. **Fix convergence drain systemd path** — ✅ DONE (pointed to `deprecated/` path).
3. **Verify songBird mesh includes swarmVine port** — ensure `mesh.peers` responses include swarmVine port (7800) so dynamic peer discovery works.

### Near-term (upstream primal evolution)

4. **songBird mesh relay for gossip** — implement `MeshRelay` transport variant so swarmVine can gossip through songBird's `:7700` mesh when direct TCP fails.
5. **Self-registration** — primals call `primal.announce` on startup instead of relying on `songbird-register.sh`.
6. **JSON-RPC adapter on swarmVine UDS** — so biomeOS Neural API can route to swarmVine for gossip queries.

### Glacial (full composition)

7. **bearDog-signed gossip entries** — Ed25519 signatures on gossip payloads for cross-trust-boundary propagation.
8. **CRDT convergent state** — long-lived entries that merge rather than expire.
9. **biomeOS graph executor** — replace Python braid orchestration with biomeOS-dispatched computation graphs using gossip as input.

---

*swarmVine is an ant. Small, quiet, rides on a bird or a bear, crawls in the soil,
talks to other ants. When it finds the resource — the connection, the data, the
capability — it leads in a line as ants do, laying a trail that strengthens with
each ant that follows. The colony is just beginning. The trails are just starting
to form. But the nervous system — three pheromone types, nonce dedup, TTL
evaporation, vine-bat immunity — is already in place. The scouts are what's missing.
Once the primals begin injecting gossip after their significant events, the ant
trails will start mapping the ecosystem. And then the colony finds its food.*

*Wave 157e — overwatch validation. 14/14 alive. The ant is awake.*
