# Songbird — Network Orchestration and Discovery

## Identity

| Field | Value |
|-------|-------|
| Phase | 1 (Foundation) |
| Domain | Networking, discovery, TLS, Tor, NAT traversal |
| Rust lines | 401,900 |
| Tests | 7,314 |
| Crates | 30+ |
| AGPL-3.0 | Yes |

## What It Is

Songbird is the network layer. TLS 1.3 (Pure Rust, no OpenSSL), discovery (BirdSong protocol), NAT traversal (4-tier), QUIC, relay server, and the networking half of Tower Atomic. If data needs to leave the machine, it goes through Songbird.

Songbird also serves as the **universal adapter** for discovery: instead of every primal discovering every other primal (O(n²) connections), each primal registers with Songbird (O(n) connections), and Songbird handles routing.

## Why It Exists

In gen1, NestGate had NFS/SMB networking and Squirrel had MCP networking — two ad-hoc networking stacks in two primals. When BearDog was split out for crypto, the question became: who does TLS? The answer was a dedicated networking primal.

Songbird was born from the realization that networking — TLS handshakes, NAT hole-punching, peer discovery, relay routing — is complex enough to warrant its own primal, and security-critical enough that it should be tightly integrated with BearDog's crypto.

## Key Capabilities

### Protocols

| Protocol | Implementation | Purpose |
|----------|---------------|---------|
| TLS 1.3 | Pure Rust (rustls) | Encrypted transport |
| Tor v3 | Coordinated with BearDog | Anonymous routing |
| QUIC | quinn | Low-latency UDP transport |
| STUN | Custom | NAT type detection |
| IGD | rupnp | Router port mapping |
| NFC Genesis | Custom | Physical-proximity bootstrap |

### Discovery

- **BirdSong protocol**: Encrypted service advertisement
- **Universal adapter**: O(n) discovery hub — primals register once, Songbird routes
- **Dark Forest discovery**: Coordinates with BearDog for zero-metadata beacons
- **DNS SRV + mDNS**: Standard service discovery for non-sovereign networks

### NAT Traversal (4-tier)

1. Direct connection (LAN / public IP)
2. IGD/UPnP port mapping
3. STUN hole-punching
4. Relay through Songbird relay server

## How It Connects

```
                    ┌─────────────┐
                    │  Songbird   │
                    │ (Discovery  │
                    │  + Network) │
                    └──────┬──────┘
              ┌────────────┼────────────┐
              │            │            │
         ┌────▼────┐  ┌───▼────┐  ┌───▼────┐
         │ BearDog │  │biomeOS │  │LoamSpine│
         │(crypto) │  │(routes)│  │(federate│
         └─────────┘  └────────┘  └─────────┘
              ▲
         Tower Atomic
         (BearDog crypto + Songbird TLS = Pure Rust HTTPS)
```

### Key Relationships

- **BearDog** provides all crypto to Songbird (Ed25519 signing, ChaCha20, X.509 certificates) → together they form **Tower Atomic**
- **biomeOS** routes AI requests through Songbird's HTTP bridge (Squirrel → Songbird → cloud AI)
- **LoamSpine** uses Songbird for federation (DNS SRV + mDNS discovery of remote Loam nodes)
- **Every primal** registers with Songbird via `ipc.register` for ecosystem-wide discovery

## Internal Architecture

30+ crates:

- `songbird-orchestrator` — Main binary and lifecycle
- `songbird-universal-ipc` — Transport abstraction (Unix, TCP, abstract sockets)
- `songbird-tor-protocol` — Tor circuit management (delegates crypto to BearDog)
- `songbird-tls` — TLS 1.3 state machine (rustls)
- `songbird-discovery` — BirdSong, STUN, IGD, mDNS
- `songbird-lineage-relay` — Family-aware message relay
- `songbird-ai-bridge` — HTTP proxy for Squirrel → cloud AI

## Tower Atomic — The Headline Composition

Tower Atomic is the most important composition in ecoPrimals: **Pure Rust HTTPS with zero C dependencies**.

BearDog provides the cryptographic operations (key generation, signing, certificate handling). Songbird provides the TLS 1.3 state machine and HTTP server. Neither can do HTTPS alone. Together, via JSON-RPC over Unix sockets, they produce HTTPS that:

- Has zero C dependencies (no OpenSSL, no BoringSSL)
- Has zero unsafe blocks in the production path
- Works on every platform Rust targets
- Achieves 93% validation across 87 production test sites
- Averages 366ms HTTPS latency

Tower Atomic was not designed. The Pure Rust constraint eliminated OpenSSL. The primal isolation constraint prevented Songbird from embedding BearDog's crypto. The only remaining option was composition via IPC — and it worked. This is the citrate metabolism of ecoPrimals: an innovation that emerged from constraint, not from intent.

## What Makes It Interesting

Songbird's Deep Debt rating is S+ — the highest tier. This means the networking layer has been through extensive refinement cycles, each one adding capability while maintaining the Pure Rust constraint.

The 4-tier NAT traversal means ecoPrimals can operate from a basement behind a consumer router (the actual deployment environment) without requiring port forwarding configuration. The system discovers its own network topology and adapts.
