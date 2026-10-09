# Nested Relay Privacy — Three-Tier Selective Permeability

**Wave 171 — October 9, 2026**
**Classification**: subGen architecture — relay privacy, Anderson transport, membrane biology
**Status**: ACTIVE — Tier 1 deployed (keyless beacon), Tier 2 verified (MitoBeacon infrastructure), Tier 3 operational (WireGuard + genetic lock)

---

## Abstract

The relay at `beacon.primals.eco` is not one membrane — it is three nested membranes. Each tier maps 1:1 to an existing riboCipher transport signal, an Anderson disorder regime, and a cryptographic identity layer from the primals stack. Entities evolve between tiers as their imaginary dimension equilibrates (Paper 46). This document describes the operational state, the mathematical mapping, and the future wiring.

**Companion documents:**
- **Paper 47** (`47_nested_relay_privacy.md`) — the formal science paper
- **Paper 46** (`46_inverse_anderson.md`) — inverse Anderson mapping (imaginary dimension)
- **Paper 43** (`43_selective_permeability_anderson.md`) — orthogonal Anderson / permeability tensor
- **COMMENSAL_RELAY_BEACON_WAVE167** — prior commensal architecture (now Tier 1)

---

## The Three Tiers

### Tier 1 — Beacon / Commensal

| Property | Value |
|----------|-------|
| **Name** | Beacon |
| **riboCipher** | `0xEC` (clear) |
| **Entry** | Keyless — `custom-rendezvous-server = 'beacon.primals.eco'` |
| **Service** | RustDesk relay (hbbs + hbbr on golgiBody) |
| **Anderson W** | 12–15 (high disorder) |
| **d_eff** | 1.0 (single vantage) |
| **Imaginary** | Large negative (active defense) |
| **Protection** | RUSTDESK_MEMBRANE chain, Schwann cell isolation, E2E encryption |

**Wave 171 changes:**
- Removed basicauth from beacon page Caddyfile (page now returns HTTP 200 without credentials)
- Server key moved from "required" to "optional hardening"
- Default client config is keyless (2 steps: server address + permanent password)
- Beacon page redesigned with tier badges: green (Tier 1), blue (Tier 2), red (Tier 3)
- sporeGate RustDesk config migrated from raw IP `157.230.3.183` to `beacon.primals.eco`

**Beacon page URL:** `https://beacon.primals.eco` — fully public, no authentication.

### Tier 2 — MitoBeacon / Family

| Property | Value |
|----------|-------|
| **Name** | MitoBeacon |
| **riboCipher** | `0xED` (mito-obfuscated) |
| **Entry** | `.beacon.seed` via USB bootstrap |
| **Service** | songBird relay (federation port 7700, drawbridge 7780) |
| **Anderson W** | 3–8 (moderate disorder) |
| **d_eff** | 2–3 (multiple family vantage points) |
| **Imaginary** | Small (less active defense needed) |
| **Key derivation** | bearDog HKDF-SHA256(lineage_seed, "birdsong_beacon_v1") → 32 bytes |

**Infrastructure verified (Wave 171):**
- `.beacon.seed` (32 bytes) present on sporeGate and golgiBody at `/etc/membrane/family/`
- `family.key` (64 bytes) present on both nodes
- `FAMILY_SEED` env var configured in songBird and bearDog service files
- songBird running on sporeGate: `membrane-songbird.service` (ports 7700, 8091) + `songbird-gateway.service` (ports 7701, 7780)
- riboCipher Tier 2 HMAC (`mito_tag()`, `mito_signal()`) implemented in bearDog
- Dark-forest mode active on songBird (unadvertised services)

**Not yet wired:**
- `relay.authorize` — explicit MitoBeacon verification before gossip relay forwarding
- songBird on golgiBody is inactive (relay-side MitoBeacon not gating yet)

### Tier 3 — Genetic Lock / Sovereign

| Property | Value |
|----------|-------|
| **Name** | Genetic Lock |
| **riboCipher** | `0xEE` (nuclear-sealed) |
| **Entry** | bearDog lineage token (`bd1-*`) + WireGuard peer |
| **Service** | Full inner membrane: Forgejo, nucleus, all primals services |
| **Anderson W** | 0.5–2 (minimal disorder) |
| **d_eff** | 4+ (entire mesh observation) |
| **Imaginary** | Near zero (equilibrium) |
| **Authentication** | Argon2id key ceremony → BLAKE3 bearer token → Caddy passthrough |

**Operational (no changes needed):**
- WireGuard mesh active: sporeGate (10.13.37.2) ↔ golgiBody (10.13.37.1)
- bearDog genetic lock: `membrane-passthrough-v1` (Gen 0)
- Caddy passthrough validates `Authorization: Bearer bd1-*`

---

## Nesting Invariant

An entity at Tier N cannot observe that Tier N+1 exists.

- **Tier 1 → Tier 2:** RustDesk relay IDs are unrelated to songBird federation. Commensals see a relay, not a mesh.
- **Tier 2 → Tier 3:** MitoBeacon family members see songBird services, not WireGuard endpoints or genetic lock tokens.

This is structural, not policy:
1. riboCipher transport signals are cryptographically distinct (`0xEC` ≠ `0xED` ≠ `0xEE`)
2. Schwann cell isolation prevents relay ID → operator ID mapping
3. MitoBeacon HMAC cannot be forged without the family seed
4. bearDog lineage tokens require hardware-backed entropy provenance

---

## Tier Evolution — Anderson Equilibration

Entities evolve between tiers based on behavioral observation, not bureaucratic process. The Anderson imaginary dimension (Paper 46) is the instrument reading:

| Transition | Signal | Mechanism | Human role |
|------------|--------|-----------|------------|
| Tier 1 → 2 | Imaginary → 0 over multiple windows | Behavior matches prediction. Active defense compiles into passive structure. | Evaluate observation data, grant `.beacon.seed` |
| Tier 2 → 3 | Sustained equilibrium | Family member demonstrates sovereign trust | bearDog lineage ceremony, WireGuard peer enrollment |

**Key principle:** The imaginary dimension is an instrument reading, not a trigger. A human evaluates the reading and makes the decision. Anderson provides the evidence; the human provides the judgment.

---

## Anderson Mapping

| Tier | W range | d_eff | Regime | Physical analogy |
|------|---------|-------|--------|-----------------|
| 1 (Beacon) | 12–15 | 1.0 | Localized (1D) | Signal in a wire — easy to block |
| 2 (Family) | 3–8 | 2–3 | Weak localization (2D–3D) | Signal in a film — harder to block |
| 3 (Sovereign) | 0.5–2 | 4+ | Extended (3D+) | Signal in bulk — propagates freely |

Selectivity S between tiers measures membrane quality:
- S = 0: rock or breach — cannot distinguish tiers
- S > 0.5: healthy — clear separation
- S → 1: perfect — Tier 3 propagates freely, Tier 1 rate-limited to commensal levels

---

## Implementation Inventory

### Deployed artifacts (Wave 171)

| Artifact | Location | Change |
|----------|----------|--------|
| Beacon page | golgiBody `/opt/membrane/beacon-page/index.html` | Rewritten — public, keyless, tier badges |
| Caddyfile | golgiBody `/etc/membrane/Caddyfile` | basicauth removed from beacon section |
| sporeGate RustDesk config | `/home/sporegate/.config/rustdesk/RustDesk2.toml` | IP → DNS, key removed |
| Cursor rule | `.cursor/rules/outer-membrane-rustdesk.mdc` | Tier table, keyless default, public beacon |
| Paper 47 | `sporePrint/content/science/47_nested_relay_privacy.md` | NEW — 236 lines |

### Existing infrastructure (verified operational)

| Component | Location | Tier |
|-----------|----------|------|
| hbbs + hbbr | golgiBody `/opt/membrane/` | 1 |
| RUSTDESK_MEMBRANE chain | golgiBody nftables | 1 |
| `.beacon.seed` + `family.key` | sporeGate + golgiBody `/etc/membrane/family/` | 2 |
| songBird relay | sporeGate `membrane-songbird.service` | 2 |
| riboCipher constants | `beardog-types/src/constants/domains/network/ribocipher.rs` | 1–3 |
| WireGuard mesh | sporeGate ↔ golgiBody (10.13.37.x) | 3 |
| bearDog genetic lock | Caddy passthrough + `bd1-*` tokens | 3 |

### Future wiring

| Task | Tier | Priority |
|------|------|----------|
| Wire `relay.authorize` with MitoBeacon verification | 2 | Medium |
| Activate songBird on golgiBody | 2 | Medium |
| Per-entity imaginary dimension time series | 1→2 | Low |
| Automated tier-2 suggestion (imaginary convergence alert) | 1→2 | Low |
| northGate RustDesk config update (keyless) | 1 | High — client-side |

---

## Origin

The northGate key mismatch incident (Wave 170) revealed that server key authentication created friction incompatible with the commensal principle. When sporeGate rebooted and northGate couldn't reconnect via RustDesk, the human had to plug in peripherals — the membrane had become temporarily impermeable to its own operator.

Resolution: make the outermost tier frictionless (keyless), nest higher tiers inside. The existing genetics model (riboCipher, MitoBeacon, bearDog lineage) already provides the nested authentication — it just hadn't been mapped to the relay.

The three-tier model emerged from the human's directive: "all of the above... we have nested privacy so at least 3... and then let them evolve from there." Three tiers, three riboCipher bytes, three Anderson regimes. The biological parallel (gut epithelium → mucosal immune → bloodstream) confirmed the architecture was convergent.

---

*subGen — Operational architecture document. What has been built, proven, deployed.*
*ecoPrimal · Wave 171 · October 9, 2026*
