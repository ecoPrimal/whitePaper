# NUCLEUS Architecture - Atomic Composition of Primals

**Category**: System Architecture  
**Status**: Production  
**Last Updated**: February 6, 2026

---

## Abstract

NUCLEUS is the deployment architecture of the ecoPrimals ecosystem. It defines how primals - autonomous, self-contained services - compose into larger functional units called atomics. Each atomic is a validated composition of primals that provides a specific capability layer. The three atomics (Tower, Node, Nest) build upon each other, and their full union forms a complete NUCLEUS capable of secure computation, storage, networking, and AI coordination.

The central insight is that no atomic is a monolith. Each is a runtime composition - primals discover each other by capability, coordinate via JSON-RPC over local IPC, and are orchestrated by biomeOS through graph-based deployment. Primals within an atomic do not know they are part of one.

---

## The Three Atomics

### Tower Atomic - Communication Foundation

**Components**: BearDog (cryptography) + Songbird (networking)

Tower Atomic is the foundation of every deployment. It provides the secure communication layer that all other primals depend on. BearDog handles all cryptographic operations - signing, encryption, key exchange, hashing, certificate generation. Songbird handles all network operations - TLS 1.3, service discovery, NAT traversal, federation.

Together they form the Tower Atomic pattern: Songbird implements the TLS 1.3 protocol state machine in Pure Rust, delegating all cryptographic operations to BearDog via JSON-RPC over a local Unix socket. Neither primal embeds the other's code. The result is a fully Pure Rust HTTPS stack with zero C dependencies.

**Capabilities provided**:
- `crypto.*` - All cryptographic operations (signing, encryption, hashing, KDF)
- `tls.*` - TLS 1.3 handshake and session management
- `http.*` - HTTPS request/response handling
- `discovery.*` - BirdSong encrypted multicast, mDNS, capability-based discovery
- `security.*` - Genetic lineage, Dark Forest federation, challenge-response
- `routing.*` - Network routing, NAT traversal, relay coordination

**Deployment sequence**: BearDog starts first (security must exist before anything communicates), then Songbird starts and discovers BearDog by capability. Songbird connects to BearDog's socket and begins advertising discovery capabilities.

**Status**: Production ready. 93% TLS 1.3 validation (81/87 test sites). Pure Rust HTTPS with 366ms latency.

### Node Atomic - Compute Layer

**Components**: Tower Atomic + ToadStool (compute)

Node Atomic extends Tower with compute capabilities. ToadStool provides universal compute orchestration - the ability to run workloads on CPU, GPU, neuromorphic hardware, WebAssembly, or containers. Its BarraCUDA library provides 124 tensor operations with WGSL shaders that run identically on any hardware.

With Tower providing secure communication and ToadStool providing compute, Node Atomic is what you deploy when you need to process data securely. AI inference, scientific computation, image processing, training runs - these all happen within a Node Atomic.

**Capabilities provided**:
- All Tower capabilities (crypto, TLS, HTTP, discovery, security)
- `compute.*` - Workload execution, GPU detection, CPU fallback
- `ai.local_inference` - Local AI model execution
- `workload.*` - Workload scheduling and orchestration

**Deployment sequence**: Tower deploys first (BearDog then Songbird), then ToadStool starts, discovers Tower capabilities, and begins advertising compute. GPU initialization may take up to 45 seconds as hardware is detected and validated.

**Status**: Production ready. GPU detection working. 56ms health check latency.

### Nest Atomic - Storage Layer

**Components**: Tower Atomic + NestGate (data storage)

Nest Atomic extends Tower with persistent storage. NestGate provides content-addressed storage where data is identified by its BLAKE3 hash. It handles blob storage, tree structures, metadata, and quota management. Storage is encrypted at rest via BearDog (AES-256-GCM) and all transport is encrypted via Songbird (BTSP over local IPC).

With Tower providing security and NestGate providing persistence, Nest Atomic is the composition for storing and retrieving data within the ecosystem. Content-addressed storage means the same data always produces the same hash, enabling deduplication, integrity verification, and efficient caching.

**Capabilities provided**:
- All Tower capabilities (crypto, TLS, HTTP, discovery, security)
- `storage.*` - Put, get, delete, list, copy, move, quota
- `persistence.*` - Long-term data management
- `provenance.*` - Storage-level provenance tracking

**Deployment sequence**: Tower deploys first, then NestGate starts, discovers Tower capabilities, and begins advertising storage. NestGate coordinates with BearDog for encryption of data at rest.

**Status**: Store and list operations working. Retrieve persistence under development.

---

## Full NUCLEUS

**Components**: Tower Atomic + Node Atomic + Nest Atomic + Squirrel (AI)

A full NUCLEUS is the complete ecosystem - all primals coordinated by biomeOS. It can secure communications, discover peers, traverse NATs, run compute workloads, store data, and coordinate AI models. Squirrel adds the AI coordination layer, enabling intelligent routing, merge resolution, and multi-model orchestration.

The NUCLEUS is not a monolith. It is a runtime composition of autonomous primals that happen to be running together. Remove ToadStool and you lose compute but everything else keeps working. Remove NestGate and you lose storage but crypto and networking continue. The system degrades gracefully because nothing is tightly coupled.

```
NUCLEUS Complete
  |
  +-- Tower Atomic (always present)
  |     +-- BearDog (cryptography)
  |     +-- Songbird (networking)
  |
  +-- Node Atomic (compute)
  |     +-- ToadStool (CPU/GPU/NPU/WASM)
  |
  +-- Nest Atomic (storage)
  |     +-- NestGate (content-addressed)
  |
  +-- AI Layer (optional)
        +-- Squirrel (model coordination)
```

---

## Composition Mechanics

### Graph-Based Deployment

Atomics are defined as TOML deployment graphs. Each graph specifies which primals to start, in what order, with what capabilities, and what health checks to perform.

```toml
[graph]
id = "tower_atomic_bootstrap"
coordination = "Sequential"

[[nodes]]
id = "germinate_beardog"
primal = { by_capability = "security" }
operation = { name = "start" }
depends_on = []

[[nodes]]
id = "germinate_songbird"
primal = { by_capability = "discovery" }
depends_on = ["germinate_beardog"]
```

Primals are referenced by **capability**, not by name. The graph says "start a primal that provides security" - not "start BearDog." This means the graph works even if the security primal is replaced in the future.

### Capability Discovery at Composition Time

When biomeOS deploys an atomic, it uses NUCLEUS secure discovery to find primals:

1. **Physical Discovery** (Layer 1): Songbird broadcasts encrypted BirdSong beacons. Primals on the network that share the same family seed can decrypt and discover each other.

2. **Identity Verification** (Layer 2): BearDog verifies Ed25519 signatures. Is this primal who it claims to be?

3. **Capability Verification** (Layer 3): biomeOS queries the primal's socket directly. Does it actually provide the capabilities it advertises?

4. **Trust Evaluation** (Layer 4): BearDog performs genetic lineage verification using HKDF-SHA256. Is this primal part of our family?

5. **Registration** (Layer 5): Neural API registers the verified primal in its capability registry. Future requests can be routed to it.

### Capability Translation

The Neural API translates semantic capability names to primal-specific method names:

| Semantic Request | Translated To | Routed To |
|-----------------|---------------|-----------|
| `crypto.generate_keypair` | `x25519_generate_ephemeral` | BearDog |
| `crypto.sign` | `ed25519_sign` | BearDog |
| `http.request` | `secure_http_request` | Songbird (via Tower Atomic) |
| `storage.put` | `storage.put` | NestGate |
| `compute.execute` | `workload.submit` | ToadStool |

A calling primal requests `capability.call("crypto.sign", ...)` and the Neural API discovers which primal provides that capability, translates the method name, routes the request, and returns the result. The caller never needs to know about BearDog.

---

## Bonding Model

The bonding model describes how NUCLEUS deployments interact with **each other** - across physical machines, networks, and trust boundaries. Each physical computer (called a "gate") runs its own NUCLEUS. The bonding type determines how two NUCLEUS instances relate: how much trust they share, how freely they distribute work, and what verification is required at the boundary.

This is a chemistry metaphor applied to distributed systems. Just as molecular bonding determines how atoms share electrons and form structures, NUCLEUS bonding determines how gates share capabilities and form compute meshes.

### Covalent Bonding - Shared Electrons, Family Trust

Covalent bonding describes NUCLEUS instances that share genetic trust and distribute workloads freely across their boundary. The gates in a basement HPC are the primary example.

**Physical context**: A mesh of physical computers - Northgate (i9-14900K, RTX 5090, 192GB), Southgate (5800X3D, RTX 3090, 128GB), Strandgate (Dual EPYC 7452, RTX 3090 + RX 6950 XT + 2x Akida NPU, 256GB ECC), Westgate (76TB ZFS cold storage), and others - each running their own NUCLEUS. They share a common family seed. BearDog on each gate verifies genetic lineage of every other gate. Songbird on each gate discovers the others via BirdSong encrypted multicast on the local network.

**Behavior**: When a workload arrives at Northgate that exceeds its capacity, biomeOS can distribute it to Southgate or Strandgate without contract negotiation. The trust is genetic - these gates share a family seed, so capability sharing is automatic. A compute job submitted to the mesh can be split across GPUs on three different gates as naturally as threads are split across cores on one machine.

**Electron sharing analogy**: In covalent bonding, atoms share electron pairs. In covalent NUCLEUS bonding, gates share capabilities. Northgate's RTX 5090 is available to Strandgate's bioinformatics pipeline. Westgate's 76TB ZFS pool is available to Northgate's AI training run. The capabilities are shared, not rented.

**Access level**: Full genetic trust. Any workload permission granted by the family seed holder propagates to all covalently bonded gates. If someone is given workload permission, the covalent mesh can distribute that work across any gate in the mesh without further authorization.

### Ionic Bonding - Contract-Based, Metered

Ionic bonding describes NUCLEUS instances that interact via explicit contracts with metered access and limited trust. This is the relationship between the HPC mesh and external services - cloud deployments, rented compute, or someone renting compute on the HPC.

**Physical context**: The basement HPC mesh (covalent internally) connects to a cloud VM running a NUCLEUS for burst compute. Or an external researcher rents GPU time on Northgate. Or Squirrel routes a task to a cloud-hosted large model. The internal covalent mesh remains tightly bonded, but the external interaction is ionic - contract-based, metered, with restricted access.

**Behavior**: An ionic bond treats interaction as a trade. The cloud VM gets access to specific capabilities (e.g., `compute.execute` on designated workloads) but not to the family's genetic lineage, storage, or discovery infrastructure. Usage is metered. Access is scoped to the contract. The underlying covalent nature of the HPC mesh remains invisible to the ionic partner - from the cloud VM's perspective, it is talking to a single NUCLEUS, not a distributed mesh of gates.

**Electron transfer analogy**: In ionic bonding, an electron is transferred (not shared). One atom gains, one loses. In ionic NUCLEUS bonding, capability access is transferred under contract. The HPC provides compute; the cloud provides burst capacity. Neither has full access to the other's internal structure.

**Access level**: Contract-scoped. Metered. Auditable. Each interaction is verified. The ionic partner maintains its own Tower (its own BearDog + Songbird) and communication crosses the trust boundary via explicit API contracts, not genetic lineage.

### Metallic Bonding - Electron Sea, Sub-Specialization

Metallic bonding describes NUCLEUS instances in more homogeneous, data-center-style deployments where individual gates sub-specialize rather than running identical full NUCLEUS stacks.

**Physical context**: A rack of similar machines in a facility, or a fleet of cloud VMs. Rather than each gate running a complete NUCLEUS with all atomics, gates specialize: some run only Node Atomics (pure compute), some run only Nest Atomics (pure storage), some run Tower Atomics as dedicated relay/discovery nodes. The capabilities are delocalized - any compute request can land on any compute-specialized gate.

**Behavior**: The delocalized capability pool enables specialization without fragility. If three gates specialize in GPU compute and one goes down, the remaining two absorb the load because the compute capability was never localized to a single gate. This is how large-scale deployments achieve both efficiency and resilience.

**Electron sea analogy**: In metallic bonding, valence electrons are delocalized across the metal lattice - they belong to no single atom. In metallic NUCLEUS bonding, capabilities are delocalized across the deployment. Compute belongs to the mesh, not to any specific gate.

**Access level**: High internal trust (similar to covalent within the deployment), but the structure is optimized for throughput and specialization rather than for the diverse, heterogeneous hardware profile of a covalent family mesh.

### Weak Forces - Minimal Interaction, Pre-Trust

Weak forces describe NUCLEUS interactions at the lowest trust level: external API access with no shared infrastructure, no genetic lineage, and no persistent relationship. This is also the **default starting state** for all interactions before trust is established.

**Physical context**: Squirrel calling the OpenAI API for a large language model inference. A primal querying a public REST endpoint. A Dark Forest beacon arriving from an unknown source. The Pixel 8a appearing on the network for the first time after being offline - before its lineage has been re-verified.

**Behavior**: Weak force interactions are read-only, stateless, and assume nothing about the other party. Squirrel sends a prompt to an API and receives a response. The API has no access to the ecosystem - it doesn't know about BearDog, Songbird, or the family seed. There is no bidirectional trust, no capability sharing, no workload distribution.

**Crucially, Dark Forest beacons begin as weak forces.** When a BirdSong beacon arrives, the receiving NUCLEUS does not know if it is from family or an attacker. The beacon is fully encrypted precisely because weak interaction is assumed. Only after the beacon is decrypted (proving shared beacon seed), the challenge-response succeeds (proving lineage), and identity is verified (proving specific membership) does the interaction escalate to a stronger bonding type.

**Van der Waals analogy**: In chemistry, weak forces (van der Waals, London dispersion) are temporary, distance-dependent, and involve no electron sharing. In NUCLEUS, weak forces are temporary, require no trust, and involve no capability sharing.

**Access level**: None. The external party has no access to the ecosystem. The ecosystem has no trust in the external party. If trust is established through verification, the interaction can escalate to ionic (contract) or covalent (family).

### Mixed Bonding - The Real System

In practice, a running ecoPrimals deployment exhibits multiple bonding types simultaneously, just as real materials exhibit mixed bonding character.

**Organo-metallo-salt interactions**: The basement HPC mesh is covalent (family trust between gates). When Squirrel on Northgate calls a cloud LLM API, that specific interaction is weak forces, even though Northgate is covalently bonded to the mesh. When an external researcher rents compute, the mesh presents an ionic interface while maintaining covalent bonding internally. If a subset of gates is deployed in a rack for a specific workload, those gates may adopt metallic bonding for that workload while remaining covalently bonded to the family mesh.

**The Pixel 8a pattern**: The Pixel enters the network as a mobile device carrying new data and the hardware seed (SoloKey authentication). When it appears, it begins at weak forces - just another device on the network. BirdSong discovery detects it. Dark Forest verification escalates through beacon decryption, lineage challenge, and identity confirmation. Once verified, it transitions to covalent bonding with the mesh. The data it carries is incorporated after trust clears. When the Pixel leaves the network, the bond is suspended (not broken) - the genetic trust remains, but the interaction ceases until the device returns and re-verifies.

This dynamic bonding - where interactions move between weak, ionic, covalent, and metallic depending on context and trust state - is what makes the system adaptive. A single NUCLEUS can simultaneously maintain covalent bonds with its HPC siblings, ionic bonds with cloud services, weak force interactions with external APIs, and handle a mobile device transitioning from weak to covalent as trust is established.

```
Basement HPC Mesh (Covalent)
  |
  +-- Northgate ←→ Southgate ←→ Strandgate ←→ Westgate ←→ ...
  |   (genetic trust, free workload distribution)
  |
  +--[ionic]-- Cloud VM (contract-based compute burst)
  |
  +--[ionic]-- External researcher (rented GPU time)
  |
  +--[weak]--- OpenAI API (Squirrel, no trust, no access)
  |
  +--[weak→covalent]-- Pixel 8a (enters weak, escalates to covalent after verification)
```

---

## Encryption Architecture

Within a NUCLEUS, all communication is encrypted at multiple layers:

- **Data at rest**: NestGate stores encrypted blobs using BearDog AES-256-GCM
- **Transport**: All IPC uses BTSP (BearDog Secure Tunnel Protocol) over local sockets
- **Discovery**: BirdSong beacons are encrypted with family broadcast key (ChaCha20-Poly1305)
- **Ephemeral**: Per-task genetics are derived and destroyed after use
- **Traceability**: Only hashes are logged, never plaintext

---

## Deployment Patterns

### Layered Composition (Standard)

Deploy Tower first, then add capabilities:

```
Tower → Tower + ToadStool → Tower + ToadStool + NestGate → Full NUCLEUS
```

Each layer is validated before the next is added. If compute fails, storage still works on top of Tower.

### Parallel Composition

When Tower is stable, deploy Node and Nest atomics simultaneously:

```
Tower (stable)
  ├── ToadStool (parallel)
  └── NestGate (parallel)
```

Reduces deployment time when the foundation is already running.

### HSM-Anchored Composition

Use a mobile device as the cryptographic root of trust and a data courier:

```
Pixel 8a (BearDog + SoloKey + family seed)
  └── Enters network → weak forces
        └── BirdSong discovery → beacon decryption
              └── Dark Forest verification → lineage confirmed
                    └── Covalent bond established
                          └── Data incorporated after trust clears
                                └── Device leaves → bond suspended
```

The Pixel 8a carries the hardware seed (SoloKey FIDO2 authentication) and runs BearDog for cryptographic operations. When it enters the HPC network, it begins at weak forces - the mesh does not immediately trust it. Dark Forest verification escalates trust through beacon decryption, lineage challenge, and identity confirmation. Once verified, it bonds covalently with the mesh, and any new data it carries (field measurements, external results, new models) is incorporated into the mesh's storage and compute pipeline.

When the Pixel leaves the network, the bond is suspended. It may collect new data while disconnected. When it returns, verification repeats before incorporation. This enter-verify-incorporate-depart cycle is how mobile devices participate in a sovereign mesh without compromising the trust model.

---

## Lifecycle Management

biomeOS manages the lifecycle of every primal in a NUCLEUS:

**Incubation**: Primal starts, health checks pass, capabilities registered  
**Active**: Normal operation, periodic health monitoring  
**Degraded**: Health checks failing, automatic recovery attempts  
**Apoptosis**: Graceful shutdown, resources cleaned, deregistered from capability registry

Resurrection is automatic - if a primal enters degraded state, biomeOS attempts to restart it. If the primal cannot recover, its capabilities are deregistered and dependent atomics are notified.

---

## Why Atomics, Not Monoliths

The atomic composition model exists because the alternative - monolithic services that internalize all capabilities - creates systems that are impossible to evolve, debug, or deploy incrementally.

With atomics:
- You deploy only what you need (Tower alone for a relay node, full NUCLEUS for a development workstation)
- Each primal evolves independently (BearDog can upgrade its cipher suites without touching Songbird)
- Failures are isolated (NestGate crash doesn't take down networking)
- New capabilities are added without modifying existing primals (add a new primal, advertise capabilities, biomeOS discovers it)

The physical reality makes this concrete. Westgate (i7-4771, 76TB ZFS) is optimized for cold storage - it runs a heavy Nest Atomic but a lightweight Node Atomic. Northgate (i9-14900K, RTX 5090, 192GB) is optimized for AI compute - it runs a heavy Node Atomic. Strandgate (Dual EPYC 7452, RTX 3090 + RX 6950 XT + 2x Akida NPU, 256GB ECC) is optimized for parallel bioinformatics and multi-substrate compute - its Node Atomic spans CPU, NVIDIA GPU, AMD GPU, and neuromorphic hardware simultaneously. Each gate runs the atomics that match its hardware, and biomeOS coordinates the mesh so that workloads land on the right gate.

The bonding model then describes how these differently-configured NUCLEUS instances interact. The heterogeneous hardware (DDR3 to DDR5, RTX 2070 to RTX 5090, Intel to AMD to BrainChip, 32GB to 256GB) is a strength, not a problem - each gate specializes in what its hardware does best, and the covalent mesh distributes work accordingly.

The atomic model is how biological organisms work. Cells don't contain copies of every other cell. They contain their own capabilities and coordinate through chemical signaling. A liver cell and a neuron share DNA but express different genes. Northgate and Westgate share a family seed but express different atomics. NUCLEUS applies the same principle to distributed systems.
