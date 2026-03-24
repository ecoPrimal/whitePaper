# Loam Certificates Live

**Certificates as Compositions: Game Keys, Collectibles, Credentials, and Chain-of-Custody**

**Date**: March 24, 2026
**Status**: Bridge ready in esotericWebb V4, primal infrastructure mature
**Lineage**: wateringHole/LOAMSPINE_LEVERAGE_GUIDE → gen3/baseCamp/20-22 → gen4

---

## What a Loam Certificate Is

A Loam Certificate is a hash-chained immutable record minted by
loamSpine. It certifies something: ownership, identity, transformation,
completion, derivation. It is the atomic unit of permanent provenance
in the ecoPrimals ecosystem.

In gen3, certificates were infrastructure — the mechanism by which
primals tracked their own evolution. In gen4, certificates become
**products** — things that end users hold, inspect, trade, and value.

---

## Certificate Types in gen4

### Game Keys

A game key is a Loam Certificate that grants access to a sporeGarden
product:

```
Certificate: Game Key
  ├── holder: player_identity (BearDog-verified)
  ├── product: "Thornwood Tales v1.2"
  ├── granted_by: creator_identity
  ├── capabilities: [play, mod, lend]
  ├── restrictions: [no_resale_first_30_days]
  ├── provenance: minted 2026-03-24, chain hash: abc123...
  └── lending_record: []
```

The key is verifiable (Merkle proof against loamSpine root), lendable
(the holder can grant temporary access without transferring ownership),
and sovereign (no platform can revoke it — the certificate is local
to the holder).

This solves the digital ownership problem that Valve/Steam created:
you don't "buy" a game on Steam — you buy a license that Valve can
revoke. A Loam Certificate is actual ownership.

### Collectibles (Fermented Objects)

A collectible is a Novel Ferment Transcript (see
NOVEL_FERMENT_TRANSCRIPTS.md) minted as a Loam Certificate:

```
Certificate: Fermented Object
  ├── object: "Thornrender" (sword)
  ├── created: session_id_abc, room 3
  ├── fermentation_summary:
  │   ├── sessions_carried: 14
  │   ├── notable_events: ["defeated The Warden", "enchanted frostbite"]
  │   ├── players_held: [player_a, player_b]
  │   └── total_fermentation_time: 42.3 hours
  ├── full_dag_hash: rhizocrypt_merkle_root_xyz
  ├── attribution_braid: sweetgrass_braid_id_456
  └── current_holder: player_b
```

The collectible is the certificate. The certificate is the history.
The history is the value.

### Creator Credentials

A creator credential certifies that someone authored content for the
ecosystem:

```
Certificate: Creator Credential
  ├── creator: solo_creator_handle
  ├── created_works:
  │   ├── "Thornwood Tales" (world, 2026-03-15)
  │   ├── "Thornwood System" (ruleset, 2026-03-10)
  │   └── "Miravel" (NPC personality, 2026-03-12)
  ├── attribution_summary:
  │   ├── total_playthroughs: 847
  │   ├── derived_works: 12
  │   └── community_rating: 4.7/5
  └── provenance: loamSpine chain, verifiable
```

The credential is a living document — it accumulates as the creator
produces more work and more players experience it. It is a professional
portfolio backed by provenance.

### RulesetCerts

A RulesetCert (see RPGPT_ENGINE.md) is a Loam Certificate that encodes
a complete RPG ruleset. It certifies the rules, their authorship, their
version chain, and their derivation from earlier rulesets.

### NPC Personality Certs

An NPC personality cert is a Loam Certificate that encodes an NPC's
knowledge, trust gates, lie tables, arc phases, and voice personality.
It is the "soul" of the NPC — the constraints within which AI narration
operates.

### Chain-of-Custody Certificates

For non-game domains (field genomics, medical records), Loam
Certificates provide chain-of-custody tracking:

```
Certificate: Sample Chain-of-Custody
  ├── sample_id: field_sample_2026_0324_001
  ├── collected_by: researcher_a
  ├── collection_site: GPS coordinates (encrypted)
  ├── custody_chain:
  │   ├── step 1: field → transport (researcher_a, 2026-03-24 09:00)
  │   ├── step 2: transport → lab (courier_b, 2026-03-24 14:00)
  │   └── step 3: lab → sequencer (technician_c, 2026-03-24 16:00)
  ├── processing_record: rhizoCrypt DAG (full pipeline)
  └── integrity: BearDog signature (unbroken chain)
```

This is baseCamp paper 21 (Sovereign Sample Provenance) activated as
a gen4 product.

---

## The Certificate Lifecycle

```
Create (author mints)
    │
    ├── Certify (loamSpine hashes, BearDog signs)
    │
    ├── Use (holder exercises capabilities)
    │   ├── Each use is a rhizoCrypt event
    │   └── Accumulated use = fermentation
    │
    ├── Lend (holder grants temporary access)
    │   └── Lending record appended to cert
    │
    ├── Derive (someone creates a new work based on this)
    │   ├── sweetGrass records derivation
    │   └── New cert created with derivation_from link
    │
    ├── Transfer (holder transfers ownership)
    │   └── Transfer record appended to cert
    │
    └── Archive (cert enters permanent storage)
        └── Full provenance chain preserved
```

Every lifecycle event is a vertex in the cert's rhizoCrypt DAG. The
cert remembers everything. The cert IS its history.

---

## Verification Model

Anyone can verify a Loam Certificate:

1. **Content hash**: Recompute the hash from the cert data. Does it
   match the declared hash?
2. **Chain integrity**: Walk the hash chain backward. Is every link
   valid?
3. **Merkle proof**: Request a proof from loamSpine. Does the cert
   exist in the global spine?
4. **BearDog signature**: Verify the cryptographic signature. Is it
   valid for the declared signer?
5. **Attribution braid**: Query sweetGrass. Is the attribution chain
   consistent with the cert's claimed authorship?

All five checks can be performed locally. No server, no platform, no
third party. The cert is self-verifying given the primal infrastructure.

---

## Lending Protocol

Lending is a first-class operation on Loam Certificates. The holder
grants temporary access without transferring ownership:

### Lending Rules

- **Duration**: Set by the lender (1 session, 1 week, indefinite)
- **Capabilities**: Lender can restrict capabilities (play but not mod,
  view but not copy)
- **Recall**: Lender can recall at any time (the cert returns)
- **Sublending**: Configurable (allow or disallow the borrower from
  lending further)

### Why Lending Matters

Digital goods have historically been non-lendable. You can't lend a
Steam game to a friend the way you lend a physical book. This is an
artificial restriction imposed by platforms.

Loam Certificates restore lending because the certificate is sovereign
— the holder controls it, not a platform. The lending record becomes
part of the cert's provenance. The cert remembers being lent. The
lending is a fermentation event.

---

## AR and Physical-Digital Bridge

baseCamp paper 19 (Games@Home) describes physical-digital bridge via
NFC/QR:

- A physical card (MTG, sports, custom) has an NFC chip or QR code
- The chip/code links to a Loam Certificate
- The certificate tracks every tournament, every trade, every game
- The physical card and the digital cert are bound — the card is the
  cert's physical embodiment

This means:
- Tournament results are provenance-tracked
- Card condition (physical) and history (digital) are both recorded
- Trading includes provenance (you know the card's full history)
- Forgery is detectable (the cert's hash chain doesn't match a fake)

---

## Implementation Status

| Feature | Status | Where |
|---------|--------|-------|
| `certificate.mint` bridge method | Bridge ready | esotericWebb V4 |
| NPC personality certs | Spec complete | CONTENT_AUTHORING_SPEC.md |
| RulesetCerts | Spec complete | RPGPT_ENGINE.md |
| Game key certs | Designed | This document |
| Lending protocol | Designed | This document |
| Chain-of-custody | Designed | baseCamp/21 |
| AR bridge | Conceptual | baseCamp/19 |

---

*Ownership is a certificate. History is a certificate. Identity is a
certificate. The certificate is the thing. The thing is its history.*
