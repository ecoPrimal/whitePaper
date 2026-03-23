# BearDog — Cryptographic Service Provider

## Identity

| Field | Value |
|-------|-------|
| Phase | 1 (Foundation) |
| Domain | Cryptography, identity, trust |
| Rust lines | 600,000+ |
| Tests | 14,201 (0 failures, fully concurrent) |
| Coverage | 87.0%+ line (llvm-cov) |
| Crates | 30 (`crates/*`) |
| JSON-RPC methods | 91+ |
| Edition | 2024 (MSRV 1.93.0) |
| AGPL-3.0 | Yes (100% SPDX headers) |
| Clippy | 0 warnings (pedantic + nursery + cast + unwrap/expect warn) |
| Unsafe | `forbid(unsafe_code)` workspace-wide |
| C deps | Zero (100% Pure Rust, ecoBin compliant) |

## What It Is

BearDog is the cryptographic spine of ecoPrimals. Every operation that requires signing, encrypting, hashing, key derivation, or identity verification is delegated to BearDog via JSON-RPC. No other primal implements its own crypto. This is the **Tower Atomic pattern**: a single, auditable cryptographic surface for the entire ecosystem.

Pure Rust. RustCrypto libraries. Zero C dependencies. Zero OpenSSL. `forbid(unsafe_code)` workspace-wide. Edition 2024, MSRV 1.93.0. `unwrap_used`/`expect_used` warn at workspace level — justified invariants use `#[expect(reason)]`.

## Why It Exists

In the gen1 AI Swarm, NestGate and Squirrel each embedded their own crypto logic. When Songbird was added for networking, it needed TLS — which meant a third crypto implementation. The duplication was unsustainable: three codebases to audit, three trust surfaces, three places for key management bugs.

BearDog consolidated all crypto into one primal. The others delegate to it. The result: every primal gets crypto from the same source, the same key store, the same audit trail.

## Key Capabilities

### Namespaces (JSON-RPC)

| Namespace | Operations | Purpose |
|-----------|-----------|---------|
| `crypto.*` | Ed25519, X25519, AES-256-GCM, ChaCha20-Poly1305, BLAKE3, Argon2 | Core cryptographic primitives |
| `secrets.*` | Store, retrieve, rotate, destroy | Encrypted secret management |
| `genetic.*` | Create lineage, verify, attest, relay | Family identity and trust lineage |
| `tor.*` | Create circuit, stream, resolve | Pure Rust Tor v3 (3,345 lines) |
| `beacon.*` | Create, detect, challenge | Dark Forest encrypted discovery |
| `relay.*` | Family relay, blind relay | Lineage-based message routing |
| `quantum.*` | Key encapsulation (ML-KEM) | Post-quantum readiness |

### The Entropy Hierarchy

BearDog enforces a strict entropy hierarchy: hardware RNG (SoloKey FIDO2) → OS entropy (`/dev/urandom`) → CSPRNG (ChaCha20). No operation uses a weaker source when a stronger one is available. This is not configurable — it's structural.

### Multi-Family Support

BearDog supports multiple independent key stores via `--family-id`. Each family gets its own Unix socket, its own key material, its own trust chain. A single machine can host BearDog instances for multiple families without key leakage between them.

## How It Connects

```
Every primal ──JSON-RPC──▶ BearDog
                              │
                              ▼
              crypto.sign, crypto.encrypt,
              genetic.verify, secrets.get,
              tor.create_circuit, beacon.create
```

BearDog is a **server** to every other primal. It does not initiate connections; it responds to requests. The socket lives at `$XDG_RUNTIME_DIR/biomeos/beardog.sock` (or `beardog-{family_id}.sock` for multi-family).

### Key Relationships

- **Songbird** depends on BearDog for TLS key material and Ed25519 signing → together they form **Tower Atomic** (Pure Rust HTTPS)
- **biomeOS** uses BearDog for NUCLEUS bootstrap identity verification
- **LoamSpine** uses BearDog for ledger entry signing
- **sweetGrass** uses BearDog for provenance attestation
- **skunkBat** uses BearDog for lineage verification in threat assessment

## Internal Architecture

30 crates organized as a Cargo workspace:

- `beardog-core` — Key types, crypto trait definitions
- `beardog-auth` — Authentication, JWT, session management
- `beardog-genetics` — Family lineage, trust chains, attestation
- `beardog-ipc` — JSON-RPC server, Unix socket transport
- `beardog-adapters` — Hardware HSM integration (SoloKey, Pixel 8a)
- `beardog-production` — Deployment, configuration, health checks
- `beardog-tor` — Pure Rust Tor v3 implementation

## Discovery

4-tier socket discovery: environment variable → XDG runtime → home directory → system default. Every primal that needs BearDog tries these paths in order. No hardcoded addresses.

## What Makes It Interesting

BearDog's 91 JSON-RPC methods are the largest API surface of any primal. The Dark Forest beacon protocol (ChaCha20-Poly1305 encrypted discovery, challenge-before-reveal) is novel — beacons are indistinguishable from random noise to anyone without the family key.

The Pure Rust Tor implementation (3,345 lines) is not a wrapper around the C Tor daemon. It implements the Tor v3 protocol directly in Rust. This was forced by the Pure Rust constraint — no C dependencies allowed.
