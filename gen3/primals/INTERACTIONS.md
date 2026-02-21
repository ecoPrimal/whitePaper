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
   ToadStool (GPU dispatch via BarraCUDA)
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
- Run computations (ToadStool/BarraCUDA)
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
