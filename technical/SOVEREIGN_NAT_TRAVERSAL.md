# Sovereign NAT Traversal - Peer-to-Peer Connectivity Without Dependence

**Category**: Network Architecture  
**Status**: Production (Tiers 1-3), Evolving (Tier 4+)  
**Last Updated**: February 6, 2026

---

## Abstract

Sovereign NAT traversal is the ecoPrimals strategy for achieving peer-to-peer connectivity between primals across network address translation boundaries - without dependence on corporate infrastructure. The approach is sovereignty-first: prefer family-owned STUN servers, family-operated relays, and self-hosted onion services before falling back to public infrastructure. The system handles every NAT type including symmetric NAT, the hardest to traverse, through a multi-tier architecture built entirely on Tower Atomic (BearDog + Songbird).

---

## The Problem

Network Address Translation (NAT) is the primary barrier to peer-to-peer communication. Most devices on the internet sit behind NAT - their real address is hidden behind a router that rewrites packet headers. Two devices behind NAT cannot directly connect to each other because neither knows the other's actual address, and neither router knows to forward incoming packets.

Traditional solutions depend on corporate infrastructure: Google's STUN servers for address discovery, Twilio's TURN servers for relay, centralized signaling servers for coordination. This creates the exact dependency that sovereign computing is designed to eliminate.

The additional complication is NAT type diversity:

| NAT Type | Hole Punch Success | Challenge |
|----------|-------------------|-----------|
| Full Cone | ~95% | Minimal - any external host can reach mapped port |
| Restricted Cone | ~90% | Must send to specific IP first |
| Port Restricted Cone | ~80% | Must send to specific IP:port first |
| **Symmetric** | **~30%** | **Each destination gets a different mapped port - prediction required** |

Symmetric NAT, common on mobile networks and enterprise firewalls, requires relay infrastructure because hole punching is unreliable when the NAT assigns a different external port for every destination.

---

## The Multi-Tier Architecture

### Tier 1: Direct UDP Hole Punch

**Strategy**: Use STUN to discover public address, exchange address information via BirdSong beacons, perform simultaneous UDP open.

**How it works**:
1. Both peers query a STUN server to learn their public IP:port mapping
2. Both peers exchange their public addresses via BirdSong encrypted discovery
3. Both peers simultaneously send UDP packets to each other's public address
4. NAT routers see outgoing packets and create mappings for incoming responses
5. Packets cross, and the connection is established

**Success rate**: ~80-95% for non-symmetric NAT. ~30% for symmetric NAT.

**Dependencies**: STUN address discovery (can use family or public servers), BirdSong for address exchange.

### Tier 2: Family STUN Server

**Strategy**: Run Songbird as a STUN server within the family infrastructure. Zero external dependency for address discovery.

**How it works**:
Songbird implements RFC 5389 STUN in Pure Rust. Any Tower Atomic deployment can serve as a STUN server on ports 13478 and 23478. Family members query their own infrastructure for NAT address discovery instead of Google or Cloudflare.

**Advantage**: Complete sovereignty over address discovery. No metadata leakage to external STUN providers. STUN queries reveal your public IP to the server - with family STUN, that information stays within the family.

**Requirement**: At least one family member must have a publicly reachable address (server, VPS, or a device on a non-restrictive NAT).

### Tier 3: Family Relay (Lineage-Gated)

**Strategy**: When hole punching fails (symmetric NAT, double NAT), relay traffic through a family member that has connectivity. Access is gated by BearDog genetic lineage - only family members can use the relay.

**How it works**:
1. A family member with public connectivity runs Songbird as a relay server (port 3479)
2. Peers that cannot hole-punch connect to the relay via standard TCP or UDP
3. BearDog verifies genetic lineage before relay access is granted
4. Traffic is encrypted end-to-end with keys derived through BearDog (the relay sees only ciphertext)
5. The relay forwards packets between the two peers

**Relay Protocol Messages**:
- `Allocate` - Request a relay allocation (authenticated via lineage)
- `DataPacket` - Forward encrypted data through the relay
- `Refresh` - Keep allocation alive
- `Deallocate` - Release relay resources
- `Response` - Relay status and allocation confirmation

**Privacy**: The relay cannot read traffic content. End-to-end encryption means the relay sees encrypted blobs only. Even a compromised relay reveals nothing about the communication.

**Symmetric NAT solution**: This tier is specifically designed for symmetric NAT. When both peers have symmetric NAT, direct hole punching has only ~30% success. Family relay provides 100% connectivity at the cost of relay hop latency.

**Status**: Production ready (February 5, 2026). UDP forwarding implemented and validated.

### Tier 4: Public STUN Fallback

**Strategy**: Fall back to public STUN servers (Google, Cloudflare, Nextcloud) for address discovery only when no family STUN is available.

**What is exposed**: Only your public IP address (which the STUN provider necessarily sees). No beacon content, no family information, no communication payload.

**Mitigation**: Server rotation for privacy (don't use the same STUN server repeatedly). Address discovery only (never relay through public infrastructure).

**Servers**: `stun.l.google.com:19302`, `stun.cloudflare.com:3478`, `stun.nextcloud.com:3478` with rotation.

---

## Sovereign Beacon Mesh

Beyond the four tiers, the ecosystem is evolving toward a fully sovereign beacon mesh for discovery and connectivity without any port forwarding.

### Onion Service Bootstrap

Tor hidden services via Arti (Pure Rust Tor client) provide a discovery bootstrap that requires no port forwarding and no public IP address. Any device, regardless of NAT type, can create a `.onion` address and be reachable.

**Implementation**: BearDog provides the cryptographic primitives (SHA3-256 for `.onion` address generation, Ed25519 for identity keys, X25519 for session keys). Songbird provides the Tor circuit management and traffic routing. The composition follows the same Tower Atomic pattern used for HTTPS.

### Organic Mesh Growth

Every family connection becomes a potential relay. When device A connects to device B (via any tier), that connection can serve as a relay path for device C. The mesh grows organically as more family members come online.

### Layered Encryption

The beacon mesh uses three encryption layers:
1. **Family layer**: Encrypted with family broadcast key (all family members can decrypt)
2. **Lineage layer**: Encrypted with lineage-specific key (only members of specific lineage)
3. **Device layer**: Encrypted with device-specific key (only the target device)

This enables broadcast discovery (family layer), group communication (lineage layer), and private messaging (device layer) within the same mesh protocol.

### Gossip Protocol

Beacons propagate via store-and-forward gossip. When a family member receives a beacon, it stores it and forwards it to other known family members. This handles intermittent connectivity - a device that was offline will receive beacons that were broadcast while it was unavailable.

---

## NAT Type Detection and Strategy Selection

Songbird detects NAT type via STUN and selects the optimal connection strategy:

| Peer A NAT | Peer B NAT | Strategy |
|-----------|-----------|----------|
| Full Cone | Any | Direct hole punch (Tier 1) |
| Restricted | Restricted | Direct hole punch (Tier 1) |
| Port Restricted | Port Restricted | Direct hole punch with timing (Tier 1) |
| Symmetric | Full/Restricted Cone | Direct hole punch, 50-70% success (Tier 1) |
| **Symmetric** | **Symmetric** | **Family relay (Tier 3)** |
| Any | Any (Tier 1 failed) | Family relay (Tier 3) |
| Any | Any (no family infra) | Public STUN + relay planning |

The strategy is selected automatically at connection time. Peers exchange NAT type information via BirdSong and agree on the optimal approach.

---

## Integration with Tower Atomic

Sovereign NAT traversal is built entirely on the Tower Atomic composition:

**BearDog provides**:
- Genetic lineage verification (relay access control)
- Beacon encryption/decryption (BirdSong payloads)
- End-to-end key derivation (relay traffic encryption)
- Identity keys (Ed25519 for STUN binding, onion addresses)
- Session keys (X25519 for peer communication)

**Songbird provides**:
- STUN server and client (RFC 5389, Pure Rust)
- UDP hole punching (simultaneous open)
- Relay server (lineage-gated UDP forwarding)
- BirdSong encrypted discovery (address exchange)
- NAT type detection and strategy selection
- Onion circuit management (via Arti)

**Neural API routes**:
- `stun.discover` → Songbird (get public address)
- `stun.detect_nat_type` → Songbird (classify NAT behavior)
- `punch.request` → Songbird (initiate hole punch)
- `relay.serve` → Songbird (start relay service)
- `relay.allocate` → Songbird (request relay allocation)
- `mesh.announce` → Songbird (join beacon mesh)
- `mesh.find_path` → Songbird (find route to peer)

---

## Security Properties

**Relay privacy**: End-to-end encryption ensures relays see only ciphertext. A compromised relay reveals nothing about communication content, and BearDog lineage verification prevents unauthorized relay use.

**STUN privacy**: Family STUN servers keep address discovery within the family. Public STUN fallback exposes only public IP (which is already visible to the public internet), with server rotation to prevent tracking.

**Beacon privacy**: BirdSong beacons are encrypted with family broadcast keys. Outsiders see encrypted noise. The beacon mesh reveals nothing about family structure, membership, or communication patterns.

**Lineage gating**: All relay access requires BearDog genetic lineage verification. Non-family members cannot use family infrastructure. This is cryptographic enforcement, not policy - without the correct lineage seed, relay allocation requests are mathematically impossible to forge.

---

## Current Status and Evolution

| Component | Status | Notes |
|-----------|--------|-------|
| STUN Server | Production | Pure Rust RFC 5389, ports 13478/23478 |
| STUN Client | Production | NAT type detection, address discovery |
| UDP Hole Punch | Production | Simultaneous open, timing coordination |
| Family Relay | Production | Lineage-gated UDP forwarding, 5 message types |
| Privacy Masking | Production | 4 levels implemented |
| BirdSong Integration | Production | Address exchange via encrypted beacons |
| Onion Bootstrap | Architecture | BearDog SHA3-256 ready, Arti integration planned |
| Organic Mesh | Architecture | Gossip protocol specified, implementation planned |
| Symmetric NAT | Production | Handled via Tier 3 relay |

The immediate priority is validating cross-NAT connectivity between real devices: a Linux workstation, a Pixel 8a on mobile data (likely symmetric NAT), and a Raspberry Pi behind consumer NAT. This will exercise all tiers and prove the sovereignty-first strategy in practice.

---

## Rationale

The conventional approach to NAT traversal is to pay a cloud provider for TURN relay infrastructure. This creates a permanent dependency: your peer-to-peer network is only as reliable as your cloud subscription, and the relay provider can see connection metadata (who is talking to whom, when, how much data).

Sovereign NAT traversal eliminates this dependency. The family's own infrastructure provides STUN and relay services. The family's own cryptographic lineage gates access. The family's own encryption protects traffic. The only external dependency is the internet itself - and even that is mitigated by local network discovery via BirdSong multicast.

This is not about avoiding all external infrastructure. Tier 4 exists as a fallback. It is about ensuring that the default path - the path that works when everything is healthy - depends on nothing outside the family.
