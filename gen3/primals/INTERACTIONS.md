# Primal Interactions

## How Primals Coordinate

### The Rule

No primal imports another primal's code. No compile-time coupling. All coordination happens at runtime through JSON-RPC 2.0 over Unix sockets, discovered via capability-based routing.

This is deliberate: each primal is an independent evolutionary lineage. If BearDog's internal architecture changes, Songbird doesn't notice — the JSON-RPC interface is the contract. This mirrors biological species interacting through chemical signals, not shared DNA.

---

## The IPC Stack

### Transport

| Layer | Technology | Used By |
|-------|-----------|---------|
| Primary | Unix domain sockets | All primals (local) |
| Secondary | Abstract sockets | Android deployments |
| Fallback | TCP | Cross-machine communication |
| HTTP bridge | Axum/hyper | Songbird AI Bridge, petalTongue web |

Socket paths follow `$XDG_RUNTIME_DIR/biomeos/{primal}.sock`, with multi-family variants at `{primal}-{family_id}.sock`.

### Protocol

JSON-RPC 2.0, standard format:

```json
{
  "jsonrpc": "2.0",
  "method": "crypto.sign",
  "params": { "message": "...", "key_id": "..." },
  "id": 1
}
```

Performance-critical paths use tarpc (Rust-specific async RPC) alongside JSON-RPC for external callers.

### Discovery

4-tier discovery for every primal:
1. Environment variable (`BEARDOG_SOCKET`, etc.)
2. XDG runtime directory scan
3. Home directory fallback
4. System default

biomeOS's Neural API adds a semantic layer: `capability.call("crypto.sign", ...)` resolves to BearDog without the caller knowing.

---

## Dependency Graph

### Startup Order

```
1. BearDog     (crypto — everything needs this)
2. Songbird    (networking — registration depends on this)
3. ToadStool   (compute — GPU discovery is hardware-dependent)
4. NestGate    (storage — data layer)
5. Squirrel    (AI — needs all of the above)
6. biomeOS     (orchestrator — needs all foundation primals)
7+ Post-NUCLEUS primals (any order, registered with biomeOS)
```

### Who Calls Whom

```
                          biomeOS
                       (orchestrator)
                    ┌───────┼───────┐
                    │       │       │
                    ▼       ▼       ▼
              ┌──────────────────────────┐
              │    Neural API routes     │
              │    capability.call()     │
              └──────────┬───────────────┘
         ┌───────────────┼───────────────────┐
         │               │                   │
    ┌────▼────┐    ┌────▼─────┐       ┌────▼─────┐
    │ BearDog │    │ Songbird │       │ToadStool │
    │ (crypto)│    │(network) │       │(compute) │
    └────▲────┘    └────▲─────┘       └────▲─────┘
         │              │                   │
    ┌────┴────┐    ┌────┴─────┐       ┌────┴─────┐
    │All other│    │LoamSpine │       │ Squirrel │
    │ primals │    │(federate)│       │ (AI)     │
    └─────────┘    └──────────┘       └──────────┘
```

### Interaction Matrix

| Caller → Provider | BearDog | Songbird | ToadStool | NestGate | Squirrel | biomeOS |
|-------------------|:-------:|:--------:|:---------:|:--------:|:--------:|:-------:|
| **BearDog** | — | | | | | |
| **Songbird** | crypto | — | | | | |
| **ToadStool** | auth | register | — | models | | |
| **NestGate** | | discover | | — | | |
| **Squirrel** | secrets | HTTP bridge | GPU inference | model cache | — | |
| **biomeOS** | identity | routing | health | health | AI | — |
| **petalTongue** | | register | | | | capabilities |
| **sweetGrass** | signing | discover | | storage | | |
| **LoamSpine** | signing | federate | | | | |
| **rhizoCrypt** | signing | | | blob store | | |
| **skunkBat** | lineage | metadata | resource | usage | | alerts |

**Note on skunkBat**: The row above shows what skunkBat *consumes* from other primals. skunkBat also *provides* anomaly monitoring back: `baseline.observe`/`baseline.anomaly` can profile telemetry from any primal (compilation times from coralReef, dispatch rates from ToadStool, commit rates from LoamSpine, inference volumes from Squirrel, DAG vertex rates from rhizoCrypt, storage access patterns from NestGate). It provides anomaly assessments to sweetGrass as braid metadata and to petalTongue as dashboard data.
| **sourDough** | identity | discover | | | | |

---

## Key Compositions

### Tower Atomic (BearDog + Songbird)

The headline composition. Pure Rust HTTPS with zero C dependencies.

```
External HTTPS request
        │
        ▼
   Songbird (TLS 1.3 state machine)
        │
        │ JSON-RPC over Unix socket
        │
        ▼
   BearDog (crypto operations)
        │
        ▼
   Response encrypted, signed, sent
```

Songbird handles the protocol; BearDog handles the math. Neither has the complete capability alone. The composition emerged from the Pure Rust constraint — OpenSSL was impossible, so IPC-based crypto delegation was the only path.

### Node Atomic (Tower + ToadStool)

Tower provides secure networking; ToadStool adds compute.

```
External compute request
        │
        ▼
   Tower (HTTPS in, authenticated)
        │
        ▼
   ToadStool (GPU dispatch via BarraCuda)
        │
        ▼
   Result returned through Tower
```

### Nest Atomic (Tower + NestGate)

Tower provides secure networking; NestGate adds storage.

```
External storage request
        │
        ▼
   Tower (HTTPS in, authenticated)
        │
        ▼
   NestGate (content-addressed storage)
        │
        ▼
   Data stored/retrieved through Tower
```

### Full NUCLEUS (Tower + Node + Nest + Squirrel)

All capabilities available. A single machine running full NUCLEUS can:
- Store data (NestGate)
- Run computations (ToadStool/BarraCuda)
- Serve AI inference (Squirrel + ToadStool)
- Communicate securely (Songbird + BearDog)
- Coordinate (biomeOS)

---

## The Memory Model

### Ephemeral ↔ Permanent (rhizoCrypt ↔ LoamSpine)

```
Session starts
        │
        ▼
   rhizoCrypt (ephemeral DAG)
        │
   Working memory: drafts, intermediates,
   conversation context, exploration state
        │
        ▼ (dehydrate when permanence needed)
        │
   LoamSpine (permanent spine)
        │
   Permanent record: identity, ownership,
   scientific provenance, license attestation
```

### Attribution Layer (sweetGrass)

sweetGrass wraps both rhizoCrypt and LoamSpine with provenance metadata:

```
   rhizoCrypt ←──provenance──→ sweetGrass ←──provenance──→ LoamSpine
   (ephemeral)                 (attribution)                 (permanent)
```

Every piece of data, ephemeral or permanent, has a provenance chain tracked by sweetGrass.

---

## Convergent Patterns

All 12 primals independently evolved these patterns:

| Pattern | Description | Primals |
|---------|-------------|---------|
| JSON-RPC 2.0 | Standard message format | 12/12 |
| Unix socket transport | `$XDG_RUNTIME_DIR/biomeos/` | 12/12 |
| Async Tokio runtime | Non-blocking I/O | 12/12 |
| 4-tier socket discovery | env → XDG → home → system | 12/12 |
| Capability advertisement | Register capabilities on connect | 11/12 |
| Structured error types | `enum Error` with Display | 12/12 |
| Zero unsafe (production) | Enforced by Rust, not by convention | 12/12 |

These patterns were not specified in a design document. They emerged independently because the constraint environment (Rust + JSON-RPC + Unix sockets + capability-based routing) rewarded them. This is convergent evolution — the computational analog of eyes evolving independently in multiple lineages because the physics of light rewards visual sensors.

---

## Deployment History — What's Running

### Phase 1: Distributed Workloads on LAN (~November 2025)

ToadStool and Songbird managed basic distributed workloads — LAN-based, plaintext. Compute dispatch across machines in the basement mesh, discovered via Songbird, executed via ToadStool. This was the first proof that primals could coordinate across machines. No encryption, no NAT traversal, no cross-network. Just LAN.

### The `ring` Discovery

The Rust crypto ecosystem depends heavily on the `ring` crate for TLS, key exchange, and hashing. `ring` wraps BoringSSL — a C library. This means any Rust project using `ring` has a C dependency, breaking the Pure Rust constraint.

This was an existential problem: if the networking stack needs TLS (it does), and TLS needs `ring` (it did), and `ring` needs C (it does), then the Pure Rust directive is dead.

**Tower Atomic was the solution.** Instead of embedding crypto in Songbird (which would require `ring`), crypto was delegated to BearDog via IPC. BearDog owns all cryptographic operations — TLS key exchange, certificate handling, symmetric encryption — using Pure Rust implementations (`RustCrypto` crates, no C). Songbird handles the TLS state machine and protocol logic, calling BearDog for every crypto operation over a Unix socket.

The result: **Pure Rust HTTPS with zero C dependencies.** Not a workaround — a composition pattern that emerged because the constraint eliminated the conventional approach.

This is why Tower Atomic is the headline composition. It wasn't designed as "let's split crypto from networking." It was discovered as the only way to have TLS without C. The constraint produced the architecture.

### Phase 2: Tower Atomic Deployed

Tower Atomic (BearDog + Songbird) provides:
- Pure Rust HTTPS (TLS 1.3, no OpenSSL, no BoringSSL, no `ring`)
- Onion routing (Pure Rust Tor)
- Dark Forest beacons (BirdSong, ChaCha20-Poly1305)
- NAT traversal (4-tier: LAN → direct punch → coordinated punch → relay)
- BearDog lineage verification for family-based trust

Tower runs on every gate in the basement. It's the foundation for everything else.

### Phase 3: USB-to-Pixel Handshake Across Separate Networks

**The achievement:** A USB LiveSpore (x86_64 binary on a flash drive, plugged into a desktop on LAN) and a Pixel 8a (aarch64 binary, running on its own mobile hotspot) completed a cryptographic handshake — while on completely separate networks.

**The path:**
```
USB (x86_64, LAN) ──[encrypted beacon]──> api.nestgate.io ──> Tower:3492
Pixel (aarch64, hotspot) ──[encrypted beacon]──> api.nestgate.io ──> Tower:3492
```

Both devices POST BirdSong beacons (ChaCha20-Poly1305 encrypted with the shared `.family.seed`) to the Tower's rendezvous endpoint via `api.nestgate.io` (Cloudflare tunnel). The Tower verifies lineage via BearDog, matches peers by lineage hash, and pairs them. The Tower never sees plaintext — it's a blind matchmaker. The 4-tier NAT traversal strategy then negotiates a direct connection.

**What this proved:**
- **Cross-architecture works.** x86_64 and aarch64 binaries, same protocol, same crypto handshake.
- **Cross-network works.** LAN and mobile hotspot — completely isolated IP spaces — found each other through the nestgate.io tunnel.
- **Dark Forest security works.** BirdSong beacons are encrypted; only devices with the same family seed can complete the handshake.
- **The Tower is sovereign infrastructure.** nestgate.io → Cloudflare tunnel → Tower:3492 in the basement. Not AWS. Not a third-party relay. Your domain, your machine.
- **NAT traversal works without institutional infrastructure.** No rented TURN servers. The 4-tier strategy is self-hosted.

The E2E test (`sovereign_mesh_e2e.rs`) covers the full Pixel-USB-Tower flow: beacon posting, lineage verification, peer matching, encrypted data transfer. All automated, all passing.

### Phase 4: Node + Nest Atomics (In Progress)

Node Atomic (Tower + ToadStool) and Nest Atomic (Tower + NestGate) will complete the capability set for the basement HPC. Once deployed:

- **Node** gates can accept authenticated compute requests over HTTPS and dispatch to BarraCuda
- **Nest** gates can accept authenticated storage requests and route to NestGate's content-addressed store
- The basement mesh becomes a **covalent NUCLEUS** — machines bonded by family seed (SoloKey FIDO2), each running the atomics that match their hardware profile

This is when the springs start running distributed: hotSpring's lattice QCD on Strandgate's dual EPYC + RTX 3090, while Eastgate's RTX 4070 handles the MD, coordinated by biomeOS's plasmodium across the mesh.

---

## The Bonding Model (Multi-Machine)

When multiple machines run NUCLEUS instances, biomeOS coordinates them through chemistry-inspired trust levels:

| Bond | Trust | Mechanism | Example |
|------|-------|-----------|---------|
| **Covalent** | Genetic (family seed) | BearDog lineage verification, SoloKey FIDO2 | Basement HPC mesh (Northgate, Southgate, Westgate) |
| **Ionic** | Contract-based, metered | API keys, rate limits, billing | Cloud burst compute |
| **Metallic** | Sub-specialization | Role-based (compute-only, storage-only) | GPU rack |
| **Weak** | Pre-trust, probing | Challenge-before-reveal | Unknown beacons |

Covalent bonds are the strongest: machines that share a family key (physical SoloKey FIDO2) trust each other completely. This is the basement HPC: Northgate, Southgate, Strandgate, Westgate — machines physically controlled by the same person.

Ionic bonds are contract-based: cloud instances that provide compute for a fee. Trust is metered and revocable.

Metallic bonds allow sub-specialization within a mesh: a rack of GPUs bonded as compute-only nodes, not running the full NUCLEUS stack.

Weak bonds are the default: unknown entities that must prove themselves before any trust is extended.
