# SwarmVine Ant Colony Pattern & NUCLEUS Atomic Composition

**Status**: Overwatch architecture analysis — gossip substrate evolution
**Wave**: 157k | **Date**: Aug 12, 2026
**Gate**: eastGate (overwatch)
**Team**: Hardware / Overwatch
**Audience**: All primal teams, biomeOS signal team, spring subteams, overwatch

---

## Context

Wave 157e deployed swarmVine on westGate as service 14/14 — the newest primal in the
ecosystem. During overwatch validation, we probed its capabilities, transport, and
interactions with skunkBat (vine-bat pre-accept loop). What emerged is a pattern
recognition: swarmVine is an **ant colony** — and the NUCLEUS atomic model maps
directly to how primals compose into the three atomic systems.

Wave 157k proved the model: graftGate achieved Full NUCLEUS via biomeOS Neural API
(`nucleus start --mode full`) — 21 ACTIVE domains, 1830 capabilities, <60s on a
platform biomeOS had never been tested against. The composition graph runtime is
validated. iosGate achieved first deploy (6th OS family).

This document captures:
1. The NUCLEUS atomic model (Tower / Node / Nest) and the bonding model
2. The bearDog genetics hierarchy (mito-beacon / nuclear / genetic child)
3. The ant colony pattern and gossip vector evolution
4. Interaction patterns between primals at full composition

---

## The NUCLEUS Atomic Model

NUCLEUS gates run three atomic systems — named by analogy to subatomic particles
not because they are small, but because they **compose into something larger**.

The key insight is the **bonding model**: Tower Atomic is the electron — shared
across all compositions like electrons in chemical bonds. Nest Atomic and Node
Atomic always include Tower. A gate running "just Nest" is really running
Tower + Nest primals. The Tower electron cloud provides encryption, routing,
defense, and gossip to every composition.

### Tower Atomic — The Electron (Security & Communication)

The electron mediates all electromagnetic interaction — all communication
between atoms. In chemistry, electrons are shared or transferred depending
on bond type (covalent, ionic, metallic). Tower Atomic works the same way:
it is the **shared communication and security substrate** present in every
composition.

| Primal | Role | Analogy |
|--------|------|---------|
| **bearDog** | Crypto, signing, key management, genetic engine, entropy hierarchy | The charge — the fundamental property that enables all secure interaction. Mito-beacon for family recognition, nuclear keys for gate identity, genetic children for interaction identity. |
| **songBird** | Capability discovery, mesh routing, peer registry, lineage transport | The orbital — defines reachability, shape of the communication shell. Carries bearDog lineage genetics across the mesh. |
| **skunkBat** | Metadata validation, pre-accept defense, gossip immunity | The spin — determines acceptance or rejection of incoming interactions |
| **swarmVine** | Epidemic gossip, cross-gate state propagation, enmeshment | The field — carries information between gates without direct coupling. The ant colony nervous system. |

bearDog and songBird were always core Tower primals. skunkBat and swarmVine
are formally Tower because they enable enmeshment and defense — which all
other atomics depend on. Every composition inherits Tower's security (bearDog),
routing (songBird), defense (skunkBat), and gossip (swarmVine).

### Node Atomic — The Proton (Tower + Compute & Silicon)

The proton is the massive, positively-charged particle. It defines the element's
identity — what the atom *is*. Node Atomic is the **compute substrate** — but it
always includes Tower, because compute without secure communication is inert.

**Node Atomic = Tower Atomic AND:**

| Primal | Role | Analogy |
|--------|------|---------|
| **toadStool** | Workload dispatch, resource management, sandbox | The strong force — binds compute resources, determines what can be done |
| **barraCuda** | GPU IPC, shader dispatch, silicon-aware routing | The mass — the raw computational capability, hardware-bound |
| **coralReef** | GEMM compilation, shader optimization | The binding energy — how efficiently compute resources combine |

A Node Atomic gate (strandGate, biomeGate) has bearDog crypto, songBird
mesh, skunkBat defense, swarmVine gossip — AND toadStool dispatch, barraCuda
GPU, coralReef shaders. The compute trio uses Tower's gossip to advertise
GPU availability and Tower's crypto to sign computational results.

### Nest Atomic — The Neutron (Tower + Data & Provenance)

The neutron is the neutral, stabilizing particle. Without neutrons, nuclei above
hydrogen are unstable — they fly apart. Nest Atomic is the **data substrate** that
holds everything together — but it always includes Tower, because data without
secure transport and identity is untrusted.

**Nest Atomic = Tower Atomic AND:**

| Primal | Role | Analogy |
|--------|------|---------|
| **nestGate** | Content-addressed storage, BLAKE3 identity | The neutral mass — stores without charge, gives weight and stability |
| **rhizoCrypt** | DAG sessions, Merkle trees, ephemeral working memory | The decay path — the neutron's internal structure, how data transforms |
| **loamSpine** | Certificates, spine commits, signed audit trail | The binding — what keeps the nucleus from flying apart, the audit chain |
| **sweetGrass** | Attribution, braids, convergence check | The stability — determines whether the isotope is stable or radioactive |

The provenance trio uses bearDog (from Tower) for Ed25519 signing at every
step of the chain: nestGate stores → rhizoCrypt builds DAGs → loamSpine signs
the audit trail → sweetGrass braids the attribution → bearDog signs. The
security comes from the Tower electron cloud, not from Nest itself.

### NUCLEUS — The Full Atom

NUCLEUS is not a flat list of primals — it is a **graph of composition sub-graphs**.
Tower + Nest + Node, plus the surfaces and orchestration that make it a live platform.

**NUCLEUS = Tower + Nest + Node + surfaces/interactions:**

| Primal | Role in NUCLEUS | Analogy |
|--------|----------------|---------|
| **biomeOS** | Neural API, capability dispatch, graph execution. Orchestrator AND force carrier between atomics. | The Hamiltonian — governs evolution, routing, and interaction between atomic forces |
| **petalTongue** | Visualization, WebGL scenes, data rendering | The photon — carries observable information to the viewer |
| **squirrel** | AI orchestration, agentic interaction (theoretically many instances on subtasks) | The observer — interacts with the system, collapses possibilities into actions |
| **cellMembrane** | Sovereignty boundary, transport, depot, riboCipher enforcement | The membrane — selectively permeable boundary that defines self vs non-self |

biomeOS is doing double duty: it's the Hamiltonian that starts and orders primals,
but it's also the **force carrier** between atomics via Neural API. When
`capability.call("content", "get", ...)` routes from a Node primal to a Nest
primal, that's biomeOS mediating the interaction between the proton and neutron.

```
┌─────────────────────────────────────────────────────────┐
│  NUCLEUS = graph(Tower, Nest, Node, surfaces)            │
│  biome.yaml = composition manifest (BYOB per gate)       │
│  biomeOS = Hamiltonian (orchestrator + force carrier)     │
├─────────────────────────────────────────────────────────┤
│  ┌─── Tower Atomic (the electron cloud) ──┐              │
│  │ bearDog → songBird → skunkBat → swarmVine│  shared    │
│  └────────────────────────────────────────┘  across all  │
│                                                          │
│  ┌─── Nest Atomic (Tower + data) ─────────┐              │
│  │ Tower + nestGate → rhizoCrypt →         │  CAS + DAG  │
│  │         loamSpine → sweetGrass          │  + braids   │
│  └────────────────────────────────────────┘              │
│                                                          │
│  ┌─── Node Atomic (Tower + compute) ──────┐              │
│  │ Tower + toadStool → barraCuda →         │  dispatch   │
│  │         coralReef                       │  + shaders  │
│  └────────────────────────────────────────┘              │
│                                                          │
│  ┌─── Surfaces / Interactions ────────────┐              │
│  │ biomeOS (Hamiltonian + force carrier)   │              │
│  │ petalTongue (photon — visualization)    │              │
│  │ squirrel (observer — AI agent)          │              │
│  │ cellMembrane (membrane — sovereignty)   │              │
│  └────────────────────────────────────────┘              │
├─────────────────────────────────────────────────────────┤
│  primalSpring = experimental ground for compositions     │
│  Prototypes biome.yaml, validates sub-graph lifecycle    │
└─────────────────────────────────────────────────────────┘
```

---

## bearDog Genetics & Entropy Hierarchy

bearDog is not just "crypto and signing" — it is the **genetic engine** that
manages the entire identity hierarchy from species to individual to interaction.

### Three Layers of Identity

| Layer | Question | Mechanism | Biological Analogy |
|-------|----------|-----------|-------------------|
| **Mito-Beacon** | "Are you family?" | Shared mitochondrial beacon seed — family secret | Mitochondrial DNA — inherited, identifies the species |
| **Nuclear** | "Which individual are you?" | Gate's own derivation chain from root — Ed25519 keypair | Nuclear DNA — unique to the individual |
| **Genetic Child** | "What did our interaction produce?" | Fresh key spawn when two systems meet — inherits from both parents | Sexual reproduction — child inherits from both parents |

The mito-beacon is the broadest identity: everyone in the ecosystem family has it.
riboCipher uses the mito-beacon signal (`0xED` prefix) to *hear* the birdSong/BTSP.
If you can decode it, you're family. Discovery never exposes authorization material.

The nuclear identity is per-gate. eastGate has its own keys, westGate has its own
keys. Gates closer to the root (shorter derivation chain) get higher trust tiers.

The genetic child is the generative principle: every meaningful point of contact
between two different systems produces a new identity that inherits behaviors from
both parents. The interaction isn't just authenticated — it's *reproductive*.

### Bond Escalation = K-Derm Crossing

The bond types from chemistry map to the trust escalation through the K-Derm layers:

```
Weak (extracellular)           → bearDog TLS termination      = stranger
  → Ionic (outer → periplasm)  → BTSP scoped token            = authenticated stranger
    → Metallic (peri → plasma) → Mito-Beacon membership proof  = family member
      → Covalent (plasma → cyto) → Nuclear session             = trusted individual
                                   (fresh genetic child spawn)
```

Each crossing is a K-Derm boundary. The reverse path (covalent → weak) is
**Ceremony** — controlled temporal decay. The outward path across VPS layers
is **bond degradation**.

**Endosymbiosis**: External systems progressively internalize — weak → ionic →
metallic → covalent over time, like the biological process where independent
organisms become organelles.

### Entropy Hierarchy Controls Trust Ceiling

bearDog enforces this structurally, not by configuration:

```
Hardware RNG (SoloKey FIDO2)  →  highest entropy, human-mixed
  → OS entropy (kernel CSPRNG) →  machine entropy
    → Software CSPRNG (ChaCha20) →  derived entropy
```

The entropy source determines the *ceiling* of trust a node can achieve. A human
node with FIDO2 hardware entropy has the highest trust ceiling. An automated node
with only software entropy has a lower ceiling. This is how the system distinguishes
human sovereignty from automated operation — embedded in the cryptographic structure.

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
| Scout exploration | Local primals calling `gossip.inject` after events | 9/16 PRIMALS LIVE |
| Riding on a bird | `TransportEndpoint::MeshRelay` via songBird | TYPE EXISTS, MeshRelay ENABLED on ironGate |
| Riding on a bear | bearDog-signed gossip entries for trust chains | NOT YET |
| Multi-surface crawling | UDS + TCP + QUIC + mDNS discovery | TCP for cross-gate, UDS for local |
| Persistent trails | Durable gossip state surviving restarts | NOT YET (in-memory only) |
| **Deployment pheromone** | `deploy.result` gossip for fleet convergence | SPEC'D (Phase 1 target) |

### Current Architecture (Wave 157k)

```
                   ┌─────────────────────────────────────┐
                   │        swarmVine (any NUCLEUS gate)   │
                   │        186 tests, 90.8% coverage      │
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
               ┌───────────────────┼───────────────────┐
               │                   │                   │
          TCP :7800           TCP :7800           TCP :7800
               │                   │                   │
          westGate            ironGate           southGate
        (1170 ingested)    (594 ingested)      (342 ingested)
                                              (bidirectional)
```

### Gossip Vector Evolution

**Phase 1 — Scout Injection (9/16 primals now LIVE)**

| Event | Injector | Topic | Key | Status |
|-------|----------|-------|-----|--------|
| Braid finalized | sweetGrass | Data | `braid.head:{dataset}` | NOT YET |
| CAS high-water | convergence drain | Data | `cas.pressure:{gate}` | NOT YET |
| Build complete | sporeGate harvest | Tower | `depot.build:{primal}` | NOT YET |
| GPU available | toadStool | Compute | `gpu.available:{gate}` | LIVE |
| Signing ceremony | bearDog | Tower | `key.rotated:{gate}` | NOT YET |
| Service health | any primal | Tower | `health:{gate}:{primal}` | LIVE (endpoint.alive) |
| **Deploy result** | biomeOS | Tower | `deploy.result:{gate}` | **SPEC'D** |
| Compute events | barraCuda | Compute | various | **22/22 LIVE** |
| CAS sites | nestGate | Data | various | 11 sites wired |
| Session lifecycle | esotericWebb | Tower | various | 2 events LIVE |
| All events | wetSpring | Data | various | 4/4 LIVE |

**Phase 2 — Multi-Surface Transport**

| Transport | Mechanism | Use Case | Status |
|-----------|-----------|----------|--------|
| **TCP** | Direct peer-to-peer, riboCipher prefix | LAN gossip between known gates | LIVE (7-gate mesh) |
| **songBird mesh relay** | `gossip.spread` piggybacked on `:7700` mesh | Cross-subnet, NAT traversal, rides the bird | MeshRelay ENABLED on ironGate |
| **mDNS/SSDP discovery** | Multicast for automatic peer detection | Zero-config LAN enrollment | NOT YET |
| **QUIC** | Multiplexed, encrypted, connection migration | Mobile gates, unreliable networks | NOT YET |
| **bearDog-signed entries** | Ed25519 signature on gossip payload | Trust chain for entries crossing trust boundaries | NOT YET |

**Phase 3 — Persistent Trails & Convergence**

| Feature | Mechanism | Benefit |
|---------|-----------|---------|
| **WAL-backed gossip** | Write-ahead log for gossip entries | Survive restarts, catch up with peers |
| **Convergent state** | CRDT-like merge for long-lived entries | Eventually-consistent topology view |
| **Trail strength metric** | Count of independent observations per key | Stronger trails = higher confidence |
| **Selective subscription** | `gossip.subscribe` with topic/key filters | Primals listen for what they care about |

---

## Tower Atomic Composition — How It Fully Evolves

Tower Atomic is the shared electron cloud. Every other composition inherits it.
When Tower reaches full composition, the four primals form a self-reinforcing loop:

### bearDog ↔ songBird (Genetics Travels the Mesh)

bearDog provides the identity — mito-beacon for family recognition, nuclear keys
for gate identity, genetic children for interaction identity. songBird carries
those lineage genetics across the mesh via routing and federation.

```
bearDog signs identity    →  songBird transports across mesh
songBird discovers peer   →  bearDog validates genetic lineage
meeting of two gates      →  genetic child spawned with inherited behaviors
```

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

### bearDog ↔ skunkBat (Genetics Inform Defense)

bearDog's genetic lineage information feeds skunkBat's trust decisions. A gossip
entry from a gate with shorter nuclear derivation distance (higher trust tier)
gets more lenient validation than one from a distant gate.

```
bearDog knows gate lineage  →  skunkBat weighs trust in validation
skunkBat detects anomaly    →  bearDog can revoke genetic trust
```

---

## Cross-Atomic Interactions (Mediated by biomeOS Neural API)

The cross-atomic interactions are mediated by biomeOS Neural API — `capability.call`
routes between primals in different atomics. biomeOS is the force carrier.

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

The provenance chain at every step uses bearDog (Tower) for signing. The
security of the data comes from the shared electron cloud.

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

Both Nest and Node have Tower — the electron cloud is shared. When data
crosses from Nest to Node, the bearDog genetics and songBird routing from
Tower make that crossing secure and traceable. The genetic child of the
Nest↔Node interaction inherits the provenance chain from Nest and the
compute attestation from Node.

---

## Jelly Strings → Primal Composition

The issues found during overwatch validation map to jelly strings that evolve
into proper primal composition:

| Jelly String | Current | Primal Composition Target |
|-------------|---------|---------------------------|
| Convergence drain path hardcoded in systemd | Python script in `deprecated/` | nestGate tier-aware ingest with rhizoCrypt convergence DAG |
| songBird registration via shell script | `songbird-register.sh` oneshot | Primals self-register via `primal.announce` on startup |
| swarmVine peers hardcoded in env var | `SWARMVINE_PEERS=sporeGate,ironGate` | Dynamic discovery via songBird `mesh.peers` + mDNS |
| No gossip injection from any primal | ~~Zero entries~~ **9/16 primals LIVE** | Primals inject after significant events (braid, build, GPU) |
| Cross-gate gossip unreachable | ~~TCP to fixed IPs~~ **7-gate mesh, MeshRelay ENABLED** | songBird mesh relay + automatic peer discovery |
| Braid orchestration in Python | `native_braid.py` (4/7 jelly strings remaining) | biomeOS graph executor with Tower Atomic routing |
| **No deployment feedback** | Human writes AARs | biomeOS `deploy.result` gossip (SPEC'D) |

---

## Execution Priority

### Immediate

1. **Depot rebuild** — 4 fixed primals (songBird, swarmVine, toadStool, biomeOS) not yet in depot. Rebuild from current HEADs.
2. **biomeOS deploy.result gossip** — Phase 1 of deployment signaling evolution. Emit structured gossip after `composition.orchestrate`.

### Near-term

3. **bearDog-signed gossip entries** — Ed25519 signatures on gossip payloads for cross-trust-boundary propagation. Genetic child of bearDog ↔ swarmVine interaction.
4. **songBird mesh relay for gossip** — implement `MeshRelay` transport variant so swarmVine can gossip through songBird's `:7700` mesh when direct TCP fails.
5. **Self-registration** — primals call `primal.announce` on startup instead of relying on `songbird-register.sh`.

### Glacial (full composition)

6. **Genetic children for cross-gate interactions** — every meaningful gate↔gate interaction spawns a session with inherited behaviors from both nuclear identities.
7. **CRDT convergent state** — long-lived entries that merge rather than expire.
8. **biomeOS graph executor** — replace Python braid orchestration with biomeOS-dispatched computation graphs using gossip as input.

---

*swarmVine is an ant. Small, quiet, rides on a bird or a bear, crawls in the soil,
talks to other ants. When it finds the resource — the connection, the data, the
capability — it leads in a line as ants do, laying a trail that strengthens with
each ant that follows. The colony has 9 scouts now. The trails are forming. The
deployment pheromone is spec'd. The genetics hierarchy gives every ant its identity
— mito-beacon for family, nuclear for self, genetic child for every interaction.
And biomeOS, the Hamiltonian, mediates the forces between the atomics through
Neural API — not just orchestrating the graph, but carrying the interactions
between protons, neutrons, and electrons.*

*Wave 157k — post-pandemic evolution. 7 NUCLEUS gates. The ant colony converges.*
