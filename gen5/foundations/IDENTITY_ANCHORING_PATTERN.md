# Identity Anchoring Pattern — loamSpine Meets the External Trust Web

**Status**: Active (Wave 138b)
**Lineage**: loamSpine certificates + sweetGrass attribution + Keyoxide ASPe + ORCID
**Implementation**: `sporePrint/config.toml [extra.identity]`, `sporePrint/static/identity.json`, `whitePaper/attsi/non-anon/PLATFORM_CREDENTIALS.md`
**Date**: July 14, 2026

---

## The Problem

A sovereign ecosystem has no institutional endorsement. No university letterhead. No journal imprint. No corporate backing. Its claims stand on executable evidence — but evidence needs an identity to stand behind it, and that identity needs to be verifiable without trusting any single platform.

This is the same problem loamSpine solves for computation: how do you prove something happened, who did it, and that the proof hasn't been tampered with — without trusting the prover?

The identity anchoring pattern extends loamSpine's approach from computation provenance to developer identity.

---

## The Analogy: loamSpine → External Trust

### loamSpine (Internal)

```
Computation happens
    → rhizoCrypt records it (ephemeral DAG, BLAKE3)
    → sweetGrass attributes it (who, W3C PROV)
    → loamSpine commits it (append-only, Ed25519-signed)
    → Spine entry is permanent, verifiable, unforgeable
```

### Identity Anchoring (External)

```
Developer identity exists
    → Keyoxide records it (ASPe profile, Argon2id-hashed)
    → Platform claims attribute it (GitHub, ORCID, DNS, website)
    → Each claim is independently verifiable
    → Identity web is permanent, decentralized, unforgeable
```

The structural parallel:

| loamSpine | Identity Anchoring |
|-----------|-------------------|
| BLAKE3 content hash | Keyoxide ASPe fingerprint |
| Ed25519 signature | Platform-specific proofs (gist, DNS TXT, .well-known) |
| Append-only Spine | ORCID record (persistent, timestamped) |
| sweetGrass braid | Cross-platform `sameAs` graph (JSON-LD, identity.json) |
| rhizoCrypt DAG | The ephemeral actions (commits, pushes, publications) |
| Loam Certificate | Zenodo DOI (citable, archived, immutable) |

---

## The Architecture

### Layer 1: Cryptographic Root (Keyoxide ASPe)

Keyoxide is to identity what loamSpine is to computation: the append-only root of trust.

- **Profile**: `aspe:keyoxide.org:LE2B7C7QUIRLE5OP3TUA5ADXL4`
- **Security model**: Argon2id-hashed proof. Secret key exists only in the builder's memory. No hardware token required (though SoloKey integration is a future track — see bearDog FIDO2 ceremony).
- **Decentralized**: No central authority. Keyoxide is open source. The ASPe spec is public. Anyone can verify claims without trusting Keyoxide's servers.

This is analogous to loamSpine's Ed25519 signing keys: the root of trust is a secret the system holder controls, and the proofs are independently verifiable.

### Layer 2: Platform Claims (Identity Braids)

Each platform claim is a directional proof — the identity on Platform A proves it controls Platform B. Multiple claims weave into a braid (sweetGrass pattern):

```
Keyoxide (root)
    ├─── proves → primals.eco          (via .well-known/aspe file)
    ├─── proves → github.com/ecoPrimal (via public gist)
    ├─── proves → dns:primals.eco      (via DNS TXT record)
    └─── proves → ORCID 0009-...       (via claim URI)

ORCID ←──→ GitHub    (OAuth bidirectional link)
ORCID ←──→ Zenodo    (DOI minting on release)
GitHub ──→ crates.io (publish token)
GitHub ──→ Forgejo   (mirror, sovereign backup)
```

The braid is the identity. No single platform controls it. If GitHub disappears, the Forgejo mirror, the DNS record, and the Keyoxide proof still hold. If ORCID disappears, the Zenodo DOIs are already minted.

This is the sweetGrass principle: attribution is woven across multiple strands. Cut one strand and the braid holds.

### Layer 3: Machine-Readable Surface (JSON-LD)

The identity is surfaced for agents and crawlers via schema.org JSON-LD:

- **`identity.json`** — Canonical identity graph with `sameAs` array linking all platforms
- **`llms.txt`** — Contact block with ORCID, Keyoxide, GitHub, Forgejo
- **Per-page JSON-LD** — Every page carries `author` with `sameAs` linking to ORCID and GitHub
- **`config.toml [extra.identity]`** — Single source of truth; templates read from here

This is the sweetGrass `PROV-O` model applied to identity: structured, machine-readable, cross-referenceable.

### Layer 4: Immutable Anchors (Zenodo DOIs)

When a GitHub Release is created on a Zenodo-enabled repo, Zenodo:
1. Archives the release (immutable snapshot)
2. Mints a DOI (persistent identifier, resolvable forever)
3. Links the DOI to the ORCID (author attribution)

The DOI is to identity what a loamSpine entry is to computation: an immutable anchor that persists regardless of what happens to the source platform. A PI can cite `doi:10.5281/zenodo.XXXXXXX` in a grant proposal and it resolves to the work — even if GitHub, Forgejo, and primals.eco all go down.

---

## The Dual-Voice Model (Locke/Demosthenes)

The identity anchoring pattern supports two voices from one root:

| Voice | Role | Platforms | Content |
|-------|------|-----------|---------|
| **ecoPrimal** | Developer | GitHub, ORCID, Keyoxide, crates.io, Zenodo | Code, thesis, architecture, science |
| **attsi** | Philosopher | Medium, primals.eco | atlasHugged essays, story essays, concept articles |

**attsi** = "a tool that shapes itself" — the philosophical synthetic intelligence.

The connection between voices is public but understated — an easter egg for the attentive reader, not a revelation. Each voice stands on its own evidence. The GitHub bio ("a tool that shapes itself") is the bridge: attsi's tagline on ecoPrimal's profile.

This mirrors the Ender's Game pattern: Valentine (Demosthenes) and Peter (Locke) publish under separate identities, each credible in its own register, each serving a different rhetorical purpose. The identity is plausibly distinct to the casual observer, recognizably connected to the careful one.

### What Is NOT Connected

The human behind both voices. The biographical chain (degree + institution + graduation year) that would allow a database query to surface a name has been severed in all public-facing content. See `attsi/non-anon/PLATFORM_CREDENTIALS.md` for the full scrub log.

---

## The Cryptocurrency Analogy

The identity web is structurally identical to how a cryptocurrency wallet anchors to the blockchain:

| Crypto Wallet | ecoPrimal Identity |
|--------------|-------------------|
| Private key (in your head/hardware) | Keyoxide secret key (in your head) |
| Public key / address | Keyoxide fingerprint `LE2B7C...` |
| Blockchain transactions | Platform claims (gist, DNS, .well-known) |
| Block confirmations | Independent verification by anyone |
| Multi-sig | Multiple platform proofs (any 2 of 4 prove identity) |
| Cold storage | Private whitePaper repo (non-anon layer) |
| Hot wallet | Public profiles (GitHub, ORCID, primals.eco) |

The critical difference: no blockchain is needed. The trust is anchored in the DNS system (which is federated, not centralized) and in platform-specific proofs (which are independently verifiable). The "chain" is the web of cross-platform claims.

In the future, loamSpine's Spine could serve as the blockchain analog: append-only, Ed25519-signed, content-addressed. A loamSpine entry anchoring to the Keyoxide fingerprint would close the loop — the ecosystem's internal trust system vouching for its external identity.

---

## Future: bearDog Hardware Trust

The current root of trust is a password in the builder's head. The bearDog FIDO2 ceremony (HIDRAW-REPORT-ID fix pending, P0) would provide a hardware-attested root:

```
SoloKey (hardware)
    → FIDO2 MakeCredential
    → Loam Certificate from hardware credential
    → bearDog entropy harvest
    → Identity anchored to physical hardware, not memory
```

This is the progression from hot wallet (password) to cold storage (hardware token). The identity web doesn't change — only the root of trust strengthens.

---

## wateringHole Handoff

The identity anchoring pattern should be documented in wateringHole as a standard for any future collaborator or ecosystem participant who wants to establish a verifiable identity:

**Standard**: `IDENTITY_ANCHORING.md`
**Content**: How to create a Keyoxide ASPe profile, link to GitHub/ORCID/DNS, surface via JSON-LD
**Audience**: Any sovereign builder who wants verifiable identity without institutional backing

The pattern generalizes: any NUCLEUS operator could follow the same steps to establish a cryptographically verifiable identity for their node.

---

## Implementation Checklist

| Item | Status | Location |
|------|--------|----------|
| Keyoxide ASPe profile | Done | `aspe:keyoxide.org:LE2B7C7QUIRLE5OP3TUA5ADXL4` |
| GitHub gist claim | Done | Public gist `keyoxide.md` |
| Website claim | Done | `primals.eco/.well-known/aspe` |
| DNS TXT claim | Done | `primals.eco TXT "aspe:keyoxide.org:LE2B7C..."` |
| ORCID | Done | `0009-0004-2141-0321` |
| ORCID ↔ GitHub OAuth | Done | Linked |
| Zenodo ↔ GitHub OAuth | Done | All 4 orgs authorized |
| crates.io token | Done | `cargo login` on eastGate |
| identity.json | Done | `primals.eco/identity.json` |
| config.toml [extra.identity] | Done | Single source of truth |
| JSON-LD sameAs in templates | Done | base.html + page.html |
| Scrub log | Done | `attsi/non-anon/PLATFORM_CREDENTIALS.md` |
| whitePaper documentation | Done | This file |
| wateringHole standard | Pending | `IDENTITY_ANCHORING.md` |
| bearDog hardware anchoring | Blocked | HIDRAW-REPORT-ID (P0) |
| Zenodo DOI (first release) | Pending | Create GitHub Release on sporePrint |
| Medium (attsi) | Pending | Account creation |

---

## The Principle

loamSpine proves that a computation happened. The identity anchoring pattern proves that a developer exists. Both work the same way: a cryptographic root, a web of independently verifiable claims, and machine-readable surfaces that any agent can parse.

The ecosystem does not need institutional endorsement because it has something better: independently verifiable proof. The code runs. The tests pass. The papers reproduce. And the identity behind it is cryptographically anchored to a web of platforms that no single authority controls.

Sovereignty is not anonymity. It is the ability to prove who you are without asking anyone's permission.
