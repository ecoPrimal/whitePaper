# Sovereign Transaction Membrane — How the Organism Transacts with the World

**Date**: May 15, 2026
**Status**: Architecture — composing existing infrastructure into transaction flows
**Lineage**: `SOVEREIGN_HPC_EVOLUTION.md` (compute) → this document (transactions)
**Relates to**: `economics/NOVEL_FERMENT_TRANSCRIPTS.md`, `economics/LOAM_CERTIFICATES_LIVE.md`,
`economics/SUNCLOUD_ACTIVATION.md`, `NUCLEUS_TWO_TIER_CRYPTO_MODEL.md`,
`ENTROPY_HIERARCHY_PRINCIPLE.md`, `STEAM_DATA_SERVICE_SPEC.md`, `BONDING_MODELS.md`

---

## The Question This Document Answers

`SOVEREIGN_HPC_EVOLUTION.md` answers: "How does the organism **compute**?"

This document answers: **"How does the organism transact with the world —
value in, value out, trust at each boundary?"**

The organism computes intracellularly. But computation without transaction
is a brain in a jar. The membrane exists so the organism can exchange
value with its environment while maintaining sovereignty over its
intracellular state.

---

## The Transaction Membrane Model

Every transaction — a cert minted, a save synced, a workload paid for,
an entropy ceremony conducted, a ferment token matured — crosses membrane
boundaries. The gram-negative model determines **what** crosses **where**
and **how trust is established** at each boundary.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    EXTRACELLULAR (The World)                          │
│                                                                       │
│  End users · Artists · ABG collaborators · Steam ecosystem            │
│  Valve (federation) · Audiences (ceremony) · Public (sporePrint)     │
└────────────────────────────────┬────────────────────────────────────┘
                                 │ ionic tokens, TLS certs, federation sync
┌────────────────────────────────▼────────────────────────────────────┐
│              OUTER MEMBRANE (VPS — Transaction Surface)               │
│                                                                       │
│  Caddy TLS :443 ─── sporePrint content, cert verification API        │
│  BearDog :9100 ──── ionic token validation, BTSP handshake           │
│  NestGate :9500 ─── federation sync endpoint, off-site backup        │
│  SkunkBat :9140 ─── audit trail for all transactions                 │
│  Songbird :3478 ─── relay for NAT-traversal (federation, P2P)        │
└────────────────────────────────┬────────────────────────────────────┘
                                 │ routing decisions, attribution, metabolic splits
┌────────────────────────────────▼────────────────────────────────────┐
│               PERIPLASM (Transaction Routing + Economics)             │
│                                                                       │
│  sweetGrass ──── attribution braids (who contributed what)            │
│  sunCloud ────── metabolic mandate (value routing along braids)       │
│  bonding ─────── trust classification (covalent/ionic/ceremony)       │
│  routing ─────── content-aware: static→cache, auth→gate, cert→spine  │
│  entropy ─────── hierarchy validation (human vs machine vs HSM)       │
└────────────────────────────────┬────────────────────────────────────┘
                                 │ full trust (family seed, 10G, all primals)
┌────────────────────────────────▼────────────────────────────────────┐
│            INTRACELLULAR (Where Transactions Originate)               │
│                                                                       │
│  rhizoCrypt ──── working DAG (active fermentation vessel)             │
│  loamSpine ───── permanent certs (minting, ownership, history)        │
│  toadStool ───── compute dispatch (science workloads)                 │
│  coralReef ───── shader compilation (barraCuda math)                  │
│  NestGate ────── blob storage (save files, FASTQs, content)           │
│  BearDog ─────── genetic authority (keys, seeds, entropy, auth)       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 1. The Fermentation-to-Certificate Pipeline

### How a Novel Ferment Transcript is Born

A Novel Ferment Transcript (NFT) is not minted — it is **fermented**.
The process is irreversible, time-bound, and memory-accumulating:

```
Phase 1: FERMENTATION (intracellular — rhizoCrypt)
┌─────────────────────────────────────────────────────────────┐
│  User interacts with object (plays game, runs experiment)    │
│  Every action → vertex in rhizoCrypt DAG                     │
│  DAG grows: 40 hours play, 12 boss fights, 3 trades         │
│  Working memory: lock-free concurrent append                 │
│  Merkle root updates: any vertex provable against root       │
└──────────────────────────────┬──────────────────────────────┘
                               │ session ends / object traded / experiment complete
Phase 2: BOTTLING (intracellular → periplasm)
┌──────────────────────────────▼──────────────────────────────┐
│  rhizoCrypt DAG dehydrates to loamSpine                      │
│  Loam Certificate minted: hash-chained, tamper-evident       │
│  sweetGrass braid captures all contributors                  │
│  sunCloud metabolic split computed (3-7% infrastructure)     │
└──────────────────────────────┬──────────────────────────────┘
                               │ cert ready for delivery
Phase 3: DELIVERY (periplasm → outer membrane → extracellular)
┌──────────────────────────────▼──────────────────────────────┐
│  Certificate verifiable via outer membrane TLS surface        │
│  Holder access via ionic token (BearDog BTSP scoped)         │
│  Public summary on sporePrint (attribution, not content)      │
│  Lending/transfer via loamSpine API through bonding logic     │
└─────────────────────────────────────────────────────────────┘
```

### What Makes This Not a Blockchain NFT

| Property | Blockchain NFT | Novel Ferment Transcript |
|----------|---------------|-------------------------|
| Value source | Artificial scarcity (supply cap) | Accumulated history (memory-bound) |
| Storage | On-chain hash, off-chain JPEG | Full DAG in content-addressed storage |
| Verification | Consensus of anonymous miners | Merkle proof against sovereign spine |
| Ownership | Wallet address (key = identity) | BearDog-verified DID + loamSpine cert |
| Transfer | Gas fee + network confirmation | loamSpine `certificate.transfer` (zero cost) |
| Lending | Not supported (DeFi wrapping needed) | Native: `certificate.loan` with expiry + return |
| Attribution | Creator address only | Full sweetGrass braid (every contributor) |
| Revocation | Immutable (even if stolen) | Owner can revoke loan, report theft |
| Platform dependency | Ethereum, Solana, etc. | Sovereign (runs on your hardware) |

---

## 2. Tier 2: The Human Entropy Ceremony

### What Tier 2 Solves

The current two-tier crypto model provides:
- **Tier 0**: Public DNA — plaintext-free by default (translation, not secrecy)
- **Tier 1**: Family key — deployment isolation (nuclear envelope)

Both tiers are **deterministic given their inputs**. Anyone with the published
fingerprints derives the same Tier 0. Anyone with the family seed derives
the same Tier 1. This is correct for infrastructure but insufficient for
**personal sovereignty**.

**Tier 2** adds: `family_key + human entropy → sovereign key`

The human entropy "clips the connection" — the sovereign key inherits the
genetic lineage (it can prove membership in the family) but cannot be
derived by the family alone. The individual owns something the collective
cannot reproduce.

### The Entropy Mixing Protocol

```
┌─────────────────────────────────────────────────────────────┐
│  INPUT SOURCES (must satisfy entropy hierarchy)              │
│                                                              │
│  ┌───────────┐  ┌───────────────┐  ┌──────────────────┐    │
│  │ HSM Witness│  │ Human Behavior│  │ Environmental    │    │
│  │ (SoloKey)  │  │ (typing, move)│  │ (ambient noise)  │    │
│  │ Tier 1     │  │ Tier 3        │  │ Tier 3           │    │
│  └─────┬─────┘  └──────┬────────┘  └────────┬─────────┘    │
│        │                │                     │              │
│        ▼                ▼                     ▼              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  BearDog genetic.mix_entropy                         │    │
│  │  - Validates source classification                    │    │
│  │  - Enforces: ≥1 HumanLivedExperience source          │    │
│  │  - Mixing: HKDF-SHA256(hsm || human || env)          │    │
│  │  - Output: EntropySeed with provenance metadata       │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│                         ▼                                    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Sovereign Key Derivation                            │    │
│  │  sovereign_key = HMAC-SHA256(                        │    │
│  │      key = family_key + entropy_seed,                │    │
│  │      msg = "sovereign-v1:" + human_id + timestamp    │    │
│  │  )                                                   │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│                         ▼                                    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Sovereignty Proof                                   │    │
│  │  - Can prove family membership (lineage derivable)   │    │
│  │  - Cannot be reproduced by family (entropy unique)   │    │
│  │  - Provenance: timestamp + source classification     │    │
│  │  - Revocable by owner only (not family, not platform)│    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### The Ceremony Model (Architecture Pattern)

A **ceremony** is a generalized event where N participants contribute entropy
to produce cryptographic material. The ceremony pattern applies to multiple
use cases:

| Ceremony Type | Participants | Output | Trust Lifetime |
|--------------|-------------|--------|----------------|
| **Family seed creation** | Family members + HSMs | Family root key | Permanent (until rotation) |
| **Personal sovereignty** | Individual + HSM | Tier 2 sovereign key | Permanent (owned by individual) |
| **Key rotation** | Current holder + HSM | New key (old revoked) | Permanent (replaces prior) |
| **Event ceremony** | Artist + N attendees | Event key + per-attendee derivations | Time-bound (attenuates) |
| **Collaborative creation** | N creators | Shared creation key | Project lifetime |

All ceremonies share the same protocol core:
1. **Gather**: participants connect (physically or via Songbird relay)
2. **Contribute**: each participant provides entropy (BearDog validates class)
3. **Mix**: BearDog `genetic.mix_entropy` combines all sources
4. **Derive**: output key material produced from mixed entropy
5. **Distribute**: per-participant keys derived from ceremony output
6. **Record**: ceremony event recorded in loamSpine (provenance)

### The Stadium Example (Event Ceremony)

An artist at a live show wants to create content that is provably tied to
"you were there." The ceremony:

```
SETUP (artist, before show):
  Artist's HSM (SoloKey) → artist_entropy
  Artist's BearDog → ceremony_config (max_attendees, content_scope, expiry)
  VPS outer membrane → ceremony_endpoint (Songbird relay for NAT traversal)

GATHERING (during show):
  Attendee phones connect via Songbird relay → BearDog validates presence
  Each phone contributes device entropy → BearDog classifies as StoreBoughtMachine
  Artist contributes HumanLivedExperience (performance timing, HSM witness)
  
MIXING (end of show / designated moment):
  BearDog genetic.mix_entropy:
    sources = [artist_hsm, artist_human, attendee_1_device, ..., attendee_N_device]
    validation: at least 1 HumanLivedExperience (artist) required
    output: event_entropy_seed

DERIVATION:
  event_key = HMAC-SHA256(artist_family_key + event_entropy_seed, "event-v1:" + event_id)
  For each attendee i:
    attendee_key_i = HMAC-SHA256(event_key, "attendee-v1:" + attendee_i_device_hash)

MINTING:
  Content created during ceremony window → rhizoCrypt DAG
  DAG dehydrates → loamSpine certificate (event cert)
  Each attendee gets: loamSpine cert derived from event_key
    - Proves: "this content was created during event X"
    - Proves: "attendee device was present at mixing time"
    - Capabilities: play, share, but NOT transfer (memory-bound to presence)

ATTENUATION (over time):
  Day 0: attendees have covalent-like access (ceremony bond, full content)
  Day 30: bond attenuates to ionic (scoped access, no new derivations)
  Day 365: content becomes publicly viewable (attribution preserved)
  Forever: attendee cert proves "I was there" (non-transferable)
```

### Relationship to Bonding Models

The ceremony introduces a new bonding dynamic:

| Bond Type | Genetics | Permeability | Duration |
|-----------|----------|-------------|----------|
| **Covalent** | Shared family seed | Full | Permanent |
| **Ionic** | BTSP scoped token | Selective | Session/expiry |
| **Ceremony** | Shared entropy event | Full initially → attenuates to ionic | Time-bound decay |
| **Metallic** | Institutional agreement | Uniform/delocalized | Contract term |
| **Weak** | Public/pre-auth | Observe only | Ephemeral |

The ceremony bond is biologically analogous to **temporary cell fusion**
(as in myoblasts forming muscle fibers) — cells briefly share cytoplasm,
then re-establish individual membranes while retaining shared proteins.
Ceremony participants briefly share entropy, then re-establish individual
keys while retaining ceremony-derived certs.

---

## 3. Steam Data Federation via Membrane

### The Problem Steam Solves (Poorly)

Steam Cloud syncs save files across devices via Valve's servers. This means:
- Valve can lose your saves (has happened)
- Saves are inaccessible during Steam outages
- Valve sees your play data (privacy)
- Cross-platform sync is inconsistent
- No local backup strategy beyond manual copy

### The Sovereign Federation Alternative

NestGate already has the `STEAM_DATA_SERVICE_SPEC.md` — save federation,
library caching, workshop items, achievement data. What the membrane
infrastructure adds is the **operational surface**:

```
┌──────────────────────────────────────────────────────────────────┐
│  SAVE FEDERATION: Cross-Gate (10G Backbone)                       │
│                                                                    │
│  northGate (gaming) ──10G──→ westGate (76 TB ZFS)                │
│  southGate (gaming) ──10G──→ westGate (76 TB ZFS)                │
│                                                                    │
│  Strategy: OnGameExit sync (NestGate federation protocol)          │
│  Bandwidth: 10G means multi-GB saves complete in <1s              │
│  Storage: ZFS snapshots = instant versioning (100 in 0.17s)        │
│  Encryption: BearDog family key at rest (Tier 1)                   │
│  Provenance: sweetGrass braid per save event (who, when, what)     │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  SAVE FEDERATION: Cross-Membrane (Off-Site Backup)                │
│                                                                    │
│  westGate ──SSH──→ VPS outer membrane (NestGate sync endpoint)    │
│                                                                    │
│  Strategy: Periodic (daily) encrypted delta sync                   │
│  Encryption: BearDog family key (VPS cannot read saves)            │
│  Storage: Content-addressed blobs (deduplicated)                   │
│  Recovery: VPS holds encrypted saves; gate holds key               │
│  Sovereignty: VPS operator sees noise, not save data               │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  SAVE FEDERATION: Multi-Household (flockGate pattern)             │
│                                                                    │
│  flockGate (remote) ──WAN──→ westGate (via Songbird relay)       │
│                                                                    │
│  Strategy: OnGameExit sync (latency-tolerant, encrypted)           │
│  Transport: Songbird TCP fallback (BirdSong over WAN)              │
│  Bandwidth: Residential upload (~10 Mbps) limits large saves       │
│  Priority: Small saves (<100 MB) sync immediately; large queued    │
│  Benefit: remote family member's saves backed up to family ZFS     │
└──────────────────────────────────────────────────────────────────┘
```

### What This Demonstrates for Valve

The architecture that Valve would need for sovereign Steam Deck / multi-device
sync without depending on their own cloud:

| Feature | Steam Cloud | Sovereign NestGate Federation |
|---------|-------------|------------------------------|
| Multi-device sync | Valve servers | 10G backbone + Songbird |
| Off-site backup | Valve servers | VPS outer membrane (encrypted) |
| Conflict resolution | Valve's timestamp-based | NestGate content-addressed + DAG |
| Privacy | Valve reads saves | Family key encryption (Tier 1) |
| Availability | Depends on Steam being up | Local-first, always available |
| Bandwidth | Internet upload to Valve | 10G local (1.2 GB/s), WAN for off-site |
| Versioning | Last-write-wins | ZFS snapshots (full history) |
| Cost | Included in Steam (your data = their product) | $0 (own hardware) + $12/mo VPS |

The Valve pitch: "This federation protocol could run on every Steam Deck,
syncing saves peer-to-peer without touching Valve servers. Songbird handles
NAT traversal. BearDog handles family sharing permissions. NestGate handles
content-addressed deduplication. Your infrastructure cost drops; user
sovereignty increases; saves never lost."

---

## 4. Economics Through the Membrane

### Where Each Economic Function Lives

| Function | Membrane Layer | Primal | Operation |
|----------|---------------|--------|-----------|
| **Fermentation** (value creation) | Intracellular | rhizoCrypt | DAG append (user actions accumulate) |
| **Bottling** (value capture) | Intracellular | loamSpine | Certificate mint (DAG → permanent cert) |
| **Attribution** (value mapping) | Periplasm | sweetGrass | Braid computation (who contributed what %) |
| **Metabolic split** (value routing) | Periplasm | sunCloud | Route % to infrastructure/science/product |
| **Access grant** (value exchange) | Outer membrane | BearDog | Ionic token (scoped capability for cert) |
| **Verification** (value proof) | Outer membrane | Caddy + loamSpine | Merkle proof via TLS API |
| **Public display** (value signal) | Outer membrane | sporePrint | Attribution summary (not content) |

### The Metabolic Mandate in Membrane Terms

The metabolic mandate (3-7% infrastructure, 2-5% science, 0% product) maps
directly to membrane biology:

- **Infrastructure tax** = membrane maintenance (lipid turnover, porin repair).
  Without it, the membrane degrades and the cell dies.
- **Science tax** = ribosome investment (protein synthesis for growth).
  Without it, the cell cannot adapt to environmental change.
- **Zero product tax** = the cell's export products (enzymes, signals) are
  free to reach their targets without being intercepted by the membrane.

In operational terms:
```
Value flow: User pays for game key ($20)
  ├── $20.00 → Product layer (esotericWebb game)     [100% of product share]
  │    └── sweetGrass braid splits among creators proportionally
  ├── $0.60-$1.40 → Infrastructure (primals hosting)  [3-7% metabolic]
  │    └── Feeds gate compute costs, VPS, bandwidth
  └── $0.40-$1.00 → Science (spring reproduction)     [2-5% metabolic]
       └── Funds spring maintenance, data hosting, reproduction runs

Compare: Steam takes 30% ($6). Apple takes 30% ($6).
         sunCloud takes 5-12% ($1-2.40). The creator keeps $17.60-$19.
```

### Ferment Token Value Accumulation

The Novel Ferment Transcript model means value is not static. A freshly
minted game key has base value. A game key that has been:
- Played for 200 hours (fermentation time)
- Used to defeat every boss (notable events)
- Lent to 3 friends (social history)
- Associated with speedrun records (performance history)

...has accumulated **memory-bound value** beyond its purchase price. The
history IS the value. The Loam Certificate IS the history. The sweetGrass
braid IS the attribution. The sunCloud split IS the economics.

This is **value creation through use**, not value creation through
artificial scarcity. The more the object is used, the more valuable it
becomes — the opposite of crypto-NFTs where value derives from NOT using
(holding, speculating, flipping).

---

## 5. BearDog Genetics as Membrane Permeability

### The Entropy Hierarchy Controls Trust Ceiling

The entropy hierarchy (from `ENTROPY_HIERARCHY_PRINCIPLE.md`) directly
determines what level of trust a transaction can achieve:

| Entropy Class | Trust Ceiling | Cert Type | Bond Capability |
|--------------|---------------|-----------|-----------------|
| **HumanLivedExperience** | Maximum | Sovereign key, ceremony event key | Can create covalent bonds |
| **HumanSupervisedMachine** | High | Family operations, key rotation | Can derive ionic tokens |
| **StoreBoughtMachine** | Operational | Session keys, device entropy | Can participate in ceremonies |
| **SimulatedHuman** | REJECTED | None | Trust violation — rejected by BearDog |

This means:
- **Tier 2 sovereign keys** REQUIRE HumanLivedExperience entropy (cannot be
  automated, cannot be simulated, cannot be delegated)
- **Ceremony event keys** REQUIRE at least one HumanLivedExperience source
  (the artist's HSM + behavior — attendee devices are StoreBoughtMachine
  but the artist's contribution elevates the ceremony)
- **Operational keys** (Tier 0, Tier 1) can be StoreBoughtMachine (/dev/urandom)
  because they serve infrastructure, not personal sovereignty

### Genetics as Membrane Permeability Control

The genetic model (family seed → lineage → purpose keys) maps to membrane
channel proteins:

```
COVALENT (full permeability — aquaporin, always open):
  ┌─────────────────────────────────────────────────────────────┐
  │  Shared family seed → identical HKDF derivation on both sides│
  │  All RPC methods available                                    │
  │  All data types cross freely                                  │
  │  Example: ironGate ↔ northGate (same family seed)            │
  └─────────────────────────────────────────────────────────────┘

IONIC (selective permeability — gated ion channel):
  ┌─────────────────────────────────────────────────────────────┐
  │  BTSP token: Ed25519-signed, scope claim, expiry, JTI        │
  │  Only methods matching scope claim are permitted              │
  │  BearDog validates token without revealing family seed        │
  │  Example: ABG user → ironGate (scoped notebook access)       │
  └─────────────────────────────────────────────────────────────┘

CEREMONY (time-bound permeability — voltage-gated channel):
  ┌─────────────────────────────────────────────────────────────┐
  │  Shared entropy event → temporary full access                 │
  │  Attenuates over time: covalent → ionic → weak               │
  │  Event key derivable by all ceremony participants             │
  │  Content minted during ceremony window = "you were there"     │
  │  Example: concert attendees → artist's content (30-day full) │
  └─────────────────────────────────────────────────────────────┘

WEAK (minimal permeability — passive diffusion):
  ┌─────────────────────────────────────────────────────────────┐
  │  No genetic material shared                                   │
  │  Public content only (sporePrint, health endpoints)           │
  │  No authentication required                                   │
  │  Example: anonymous browser → primals.eco (read-only)         │
  └─────────────────────────────────────────────────────────────┘
```

### The Genetic Trust Chain for Transactions

Every transaction in the system can be traced back to its genetic authority:

```
Transaction: "Mint a Loam Certificate for game key"
  ├── WHO: Creator identity (BearDog-verified DID)
  │    └── Proven via: lineage seed → family membership → known creator
  ├── WHAT: Certificate content (game, version, capabilities)
  │    └── Signed via: purpose_key("ledger") derived from family_key
  ├── WHERE: loamSpine spine on ironGate
  │    └── Authorized via: gate bonding = "covalent" (family seed present)
  ├── WHEN: Timestamp + entry hash chain
  │    └── Witnessed via: BearDog crypto.sign (Ed25519, family-derived)
  └── TO WHOM: Recipient DID (buyer/recipient)
       └── Verified via: ionic token scope check (if external)
                     or: covalent trust (if family member)
```

---

## 6. What This Enables Today (Gate Demonstrations)

With the infrastructure we have operational (May 15, 2026):

| Demonstration | Gate(s) | Prerequisites | Status |
|--------------|---------|---------------|--------|
| Ferment token mint (esotericWebb playthrough) | ironGate | rhizoCrypt + loamSpine + sweetGrass running | Ready (primals deployed) |
| Loam Certificate game key (sovereign ownership) | ironGate | loamSpine `certificate.mint` API | Ready |
| Save federation (NestGate cross-gate sync) | westGate + northGate | 10G cables + NestGate federation protocol | Blocked: 10G cables |
| Save federation (single-gate demo) | ironGate | NestGate + NUC M6 covalent pair | Ready (USB-C P2P) |
| Tier 2 ceremony (family key rotation) | ironGate + SoloKey | BearDog `genetic.mix_entropy` + HSM | Ready (hardware present) |
| Stadium ceremony (multi-device) | ironGate + phones via Songbird | Songbird relay + BearDog ceremony mode | Needs: ceremony protocol |
| sunCloud attribution split | ironGate | sweetGrass braid + sunCloud router | Needs: sunCloud activation |
| Membrane cert verification (ionic) | VPS outer membrane | BearDog ionic validation + Caddy endpoint | Ready (TLS surface live) |
| Off-site save backup (encrypted) | ironGate → VPS | NestGate + BearDog Tier 1 encryption | Ready (SSH + crypto) |

### Priority Sequence for Demonstrations

1. **Now**: Ferment token mint on ironGate (all primals present)
2. **Now**: Loam Certificate game key (loamSpine API ready)
3. **Now**: Single-gate save federation (NUC M6 ↔ ironGate)
4. **Now**: Tier 2 family key rotation (SoloKey + BearDog on ironGate)
5. **After cables**: Cross-gate save federation (westGate + northGate)
6. **Needs protocol**: Stadium ceremony (Songbird + multi-device BearDog)
7. **Needs activation**: sunCloud value routing (sweetGrass braid → split)

---

## 7. Cross-References

| Document | What It Covers | How This Doc Uses It |
|----------|---------------|---------------------|
| `economics/NOVEL_FERMENT_TRANSCRIPTS.md` | NFT definition | Section 1: fermentation pipeline |
| `economics/LOAM_CERTIFICATES_LIVE.md` | Cert products | Section 1: certificate types |
| `economics/SUNCLOUD_ACTIVATION.md` | Metabolic mandate | Section 4: economics through membrane |
| `economics/THE_FLYWHEEL.md` | Seed-stage sustainability | Context: pre-revenue operations |
| `NUCLEUS_TWO_TIER_CRYPTO_MODEL.md` | Tier 0/1 key hierarchy | Section 2: Tier 2 extends this |
| `ENTROPY_HIERARCHY_PRINCIPLE.md` | Entropy classification | Section 5: trust ceiling |
| `STEAM_DATA_SERVICE_SPEC.md` | Save federation spec | Section 3: operational surface |
| `BONDING_MODELS.md` | Trust classification | Section 5: permeability model |
| `SOVEREIGN_HPC_EVOLUTION.md` | Compute membrane | Companion: how organism computes |
| `GPU_HEAT_RECOVERY_OPERATIONS.md` | Thermal economics | Complements: physical metabolism |
| `projectNUCLEUS/specs/TIER2_CEREMONY_DESIGN.md` | Ceremony protocol (operational) | Implementation of Section 2 |

---

*The organism computes intracellularly. It transacts through its membrane.
The membrane determines what crosses, at what trust level, with what
economics. Sovereignty is maintained not by isolation but by selective
permeability — the organism chooses what enters, what leaves, and what
the exchange costs.*
