# Dark Forest Protocol - Zero Metadata Leakage Security

**Category**: Security Architecture  
**Status**: Production (A++ LEGENDARY)  
**Last Updated**: February 6, 2026

---

## Abstract

The Dark Forest Protocol is the ecoPrimals security model for peer discovery and federation. Named after the Dark Forest theory from Liu Cixin's fiction - where civilizations survive by remaining invisible - the protocol enables primals to discover family members while revealing nothing to outsiders. Not even the fact that discovery is occurring is visible. Attackers cannot identify family members, cannot understand traffic, cannot inject into the network, and a compromised relay sees only encrypted noise.

The protocol is built on a two-seed genetic model and implemented entirely through the Tower Atomic composition (BearDog + Songbird).

---

## The Problem

Conventional service discovery reveals metadata. mDNS broadcasts service names in plaintext. DNS queries expose what you're looking for. Even encrypted protocols like TLS leak the Server Name Indication (SNI) in plaintext during the handshake. Metadata - who is talking to whom, when, how often, how much data - is often more valuable to an adversary than content.

For a sovereign computing ecosystem, metadata leakage is unacceptable. If an adversary can observe that two devices are communicating, they can infer relationships, behavior patterns, and intentions without ever reading a single byte of content.

---

## The Two-Seed Genetic Model

The foundation of Dark Forest security is a two-seed cryptographic identity model, inspired by biological genetics:

### Beacon Seed (Mitochondrial DNA)

The beacon seed controls discovery visibility. It is used to derive the family broadcast encryption key. Beacons encrypted with this key are discoverable by anyone who holds the same beacon seed.

Biological analogy: mitochondrial DNA is inherited maternally and shared across a lineage. It identifies family membership.

**Derived from**: Family seed → HKDF-SHA256 → beacon broadcast key  
**Used for**: BirdSong beacon encryption/decryption  
**Shared with**: All family members (they need it to see beacons)  
**Protects**: Discovery - outsiders cannot decrypt beacons

### Lineage Seed (Nuclear DNA)

The lineage seed controls permissions and identity verification. It is used for challenge-response authentication after discovery. Knowing someone is family (via beacon seed) is not enough to interact - you must prove lineage (via lineage seed).

Biological analogy: nuclear DNA provides specific identity within a family. Two siblings share mitochondrial DNA (same mother) but have different nuclear DNA (different combinations from parents).

**Derived from**: Family seed → HKDF-SHA256 → lineage verification key  
**Used for**: Challenge-response verification, session key derivation  
**Shared with**: Specific lineage members (more restrictive than beacon seed)  
**Protects**: Authorization - family discovery doesn't grant automatic access

### Why Two Seeds

A single seed for both discovery and authorization creates a vulnerability: anyone who can see beacons can also authenticate. By separating the concerns, the protocol enables scenarios like:

- Public family beacons (discoverable) with restricted lineage access (authorized)
- Multiple lineages within a single family (different access levels)
- Beacon rotation without disrupting existing authenticated sessions
- Lineage revocation without affecting other family members' discovery

---

## Protocol Layers

### Layer 1: Encrypted Beacons

All BirdSong beacons are encrypted with ChaCha20-Poly1305 using a key derived from the beacon seed. An outsider observing the network sees:

- UDP packets on a multicast address (239.255.0.1:4200)
- Random-looking encrypted payloads
- No identifiable headers, service names, or metadata
- Packets are indistinguishable from random noise

A family member with the beacon seed can decrypt and sees:
- Primal capabilities being advertised
- Socket hints for connection
- Family identifier
- Timestamp and freshness information

**Security property**: An adversary cannot determine whether encrypted UDP traffic is BirdSong beacons or random noise. The encryption is IND-CPA secure - ciphertext reveals nothing about plaintext.

### Layer 2: Challenge-Before-Reveal

Even after decrypting a beacon (proving family membership), the discovering primal does not automatically gain access. A challenge-response protocol follows:

1. Discoverer sends a challenge (encrypted with beacon seed - non-family can't even understand the challenge)
2. Respondent proves lineage by deriving a response from the lineage seed
3. BearDog independently verifies the lineage derivation (HKDF-SHA256)
4. Only after successful verification does communication begin

**Security property**: A device that somehow obtains the beacon seed (seeing family beacons) but lacks the lineage seed cannot authenticate. Discovery and authorization are cryptographically separated.

### Layer 3: Lineage Relay (Grandma's Phonebook)

When two family members cannot directly connect (different networks, NAT barriers), an ancestor with connectivity can relay introductions:

1. Ancestor receives connection request from descendant A
2. Ancestor verifies A's lineage via BearDog
3. Ancestor introduces A to descendant B (encrypted introduction)
4. B independently verifies A's lineage (does not simply trust the ancestor's word)
5. A and B establish direct encrypted communication

**Security property**: The ancestor (relay) cannot forge introductions. Both parties independently verify lineage. Even if the ancestor is compromised, the verification step prevents unauthorized connections.

### Layer 4: Physical Anchor Entry

The highest-security entry point uses hardware anchoring:

- SoloKey hardware token provides the cryptographic root of trust
- LiveSpore USB contains the family seed and biomeOS bootstrap
- Hardware authentication + family seed = entry point to the network
- Physical presence required for initial network entry

**Security property**: Network entry requires physical possession of hardware. Remote compromise of a single device does not grant access to new devices.

### Layer 5: Every Server is a Relay

In the Dark Forest model, there is no dedicated relay infrastructure that can be targeted. Every family member can route traffic for other family members. The family network IS the relay network.

- No single point of failure (family mesh is the relay mesh)
- No payment required (family helps family)
- No corporate infrastructure dependency
- Relay capabilities are advertised via BirdSong (themselves encrypted)

**Security property**: An adversary cannot identify relay nodes because all family members are potential relays. There is no central relay to target or subvert.

---

## Security Properties Summary

| Property | Guarantee |
|----------|-----------|
| **Beacon confidentiality** | Outsiders see encrypted noise, not beacons |
| **Metadata privacy** | Observers cannot determine if communication is occurring |
| **Family isolation** | Non-family cannot discover family members |
| **Lineage separation** | Beacon discovery does not grant authorization |
| **Relay blindness** | Relays see encrypted blobs, not content |
| **Introduction integrity** | Relay introductions are independently verified |
| **Forward secrecy** | Per-session ephemeral keys, derived via X25519 |
| **Post-compromise recovery** | Beacon seed rotation invalidates compromised seeds |

---

## Comparison to Existing Systems

| Feature | Signal | Tor | Dark Forest |
|---------|--------|-----|-------------|
| Content encryption | Yes | Yes | Yes |
| Metadata protection | Partial (sees who messages whom) | Yes (onion routing) | Yes (encrypted beacons) |
| Discovery privacy | No (phone number required) | Yes (hidden services) | Yes (encrypted BirdSong) |
| Server dependency | Yes (Signal servers) | Yes (Tor relays) | No (family mesh) |
| Self-hosted | No | Possible but complex | Yes (default) |
| Hardware anchoring | No | No | Yes (SoloKey/LiveSpore) |
| Family/trust model | None (individual keys) | None (anonymous) | Genetic lineage |

The Dark Forest protocol combines metadata protection (like Tor) with trust relationships (unlike Tor's anonymity model) and self-hosted infrastructure (unlike Signal's centralized servers). The trade-off is that the protocol requires a family structure - it is not designed for anonymous communication with strangers, but for sovereign communication within trusted groups.

---

## Implementation

The Dark Forest protocol is implemented entirely through the Tower Atomic composition:

**BearDog provides**:
- Beacon seed derivation (HKDF-SHA256 from family seed)
- Lineage seed derivation (HKDF-SHA256 from family seed)
- Beacon encryption/decryption (ChaCha20-Poly1305)
- Challenge-response generation and verification
- Ephemeral key generation (X25519 for session keys)
- Certificate generation (X.509 for long-lived identity)

**Songbird provides**:
- BirdSong UDP multicast broadcasting
- Beacon packet construction and parsing
- Discovery coordination (address exchange)
- Relay traffic forwarding
- STUN for NAT address discovery
- Onion routing (planned, via Arti)

**biomeOS provides**:
- NUCLEUS 5-layer discovery protocol (physical → identity → capability → trust → registration)
- Orchestration of the challenge-response flow
- Primal lifecycle management (registration/deregistration on trust changes)

---

## Threat Model

**Passive network observer**: Sees encrypted UDP packets. Cannot distinguish BirdSong from random noise. Cannot identify family members or infer network structure.

**Active network attacker**: Can inject packets but cannot forge valid encrypted beacons (requires beacon seed). Can replay packets but freshness checking prevents replay attacks. Cannot disrupt established sessions (session keys are per-connection).

**Compromised family member**: Can see decrypted beacons for their family. Cannot impersonate a different lineage (lineage verification is per-member). If detected, their lineage seed can be rotated without affecting other members.

**Compromised relay**: Sees encrypted blobs transiting through it. Cannot read, modify, or selectively drop traffic without detection (integrity checks). Cannot forge introductions (independent verification).

**State-level adversary**: Can observe all network traffic globally. Cannot decrypt beacons without the beacon seed. Cannot break ChaCha20-Poly1305 or X25519. The best attack is traffic analysis (timing, volume), mitigated by the gossip protocol's store-and-forward pattern.

---

## Rationale

The Dark Forest model reflects a specific worldview: that the default state of a network should be invisible, and visibility should be a deliberate, authenticated act. This is the opposite of conventional networking, where services advertise themselves openly and security is added as a layer on top.

In the ecoPrimals ecosystem, security is not a layer. It is the substrate. Primals do not start by being visible and then add encryption. They start invisible and selectively reveal themselves to verified family members.

The biological metaphor is apt: organisms in nature do not broadcast their location to predators. They communicate with family through chemical signals (pheromones) that are specific to their species. An outsider cannot interpret the signal. The Dark Forest protocol is the digital equivalent - cryptographic pheromones that only family members can perceive.
