# Genetic Lock: bearDog Lineage-Derived Bearer Authentication

**Wave**: 165i
**Date**: Oct 7, 2026
**Status**: Deployed — Caddy-layer genetic lock live on golgiBody
**Primal**: bearDog (entropy orchestration, genetic lineage, key derivation)
**Layer**: Outer membrane (Caddy routing on golgiBody VPS)

---

## Abstract

When the evolved fleet learned to spoof `Sec-Fetch-Mode` and `Sec-Fetch-Dest` headers, the Caddy-layer `@human_browser` passthrough became a zero-cost bypass to real Forgejo content. This document describes the replacement: a bearer token derived from bearDog's genetic key infrastructure, gating the passthrough behind cryptographic lineage rather than behavioral headers.

The fix exploits an asymmetry that fleet cannot cross: **hardware-backed entropy hierarchy**. Fleet operates at Tier 1 (machine-only entropy). The genetic lock requires Tier 2+ entropy provenance — key material derived through bearDog's HSM-aware key generation and HKDF-SHA256 derivation chain.

---

## Evolutionary Pressure

### The Sec-Fetch era (pre-lock)

```
Fleet request:
  Sec-Fetch-Mode: navigate      ← trivially spoofable
  Sec-Fetch-Dest: document       ← trivially spoofable
  Result: Real Forgejo (localhost:3000)

Agent request:
  Sec-Fetch-Mode: navigate       ← real browser header
  Sec-Fetch-Dest: document       ← real browser header
  Result: Real Forgejo (localhost:3000)
```

Both got through. The classifier treated them identically. The fleet spoofed exactly one signal and gained full access.

### The genetic lock era (post-lock)

```
Fleet request:
  Sec-Fetch-Mode: navigate       ← still spoofed
  Authorization: Bearer ???      ← CANNOT PRODUCE
  Result: Scatter (localhost:9753)

Agent request:
  Authorization: Bearer bd1-*    ← bearDog-derived
  Result: Real Forgejo (localhost:3000)
```

The token is derived from a key that requires:
- bearDog's HSM discovery engine
- Argon2id KDF with tuned memory/time parameters
- HKDF-SHA256 derivation with purpose binding
- Physical access to eastGate's key store

---

## Key Derivation Chain

```
┌─────────────────────────────────────────┐
│ bearDog HSM Discovery Engine            │
│ ├─ BearDog Native Software HSM ✓       │
│ ├─ OpenSSL Engine ✓                    │
│ └─ SoftHSM 2.0 ✓                      │
│                                         │
│ Selected: BearDog Native (auto)         │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ Key Generation (Gen 0)                  │
│ ID: membrane-passthrough-v1             │
│ Algorithm: AES-256-GCM                  │
│ KDF: Argon2id (65536KB, time=3)         │
│ Receipt: 0924f427-24e7-4e3a-...         │
└──────────────┬──────────────────────────┘
               │ HKDF-SHA256
               │ purpose: "golgi-body-web-passthrough"
               ▼
┌─────────────────────────────────────────┐
│ Key Derivation (Gen 1)                  │
│ Parent: membrane-passthrough-v1         │
│ Algorithm: AES-256-GCM                  │
│ Generation: 1 (lineage tracked)         │
│ Receipt: 1ed60901-a7a7-470c-...         │
└──────────────┬──────────────────────────┘
               │ Entropy collection
               │ + BLAKE3 hash
               ▼
┌─────────────────────────────────────────┐
│ Bearer Token                            │
│ Format: bd1-{blake3_48}                 │
│ Entropy tier: 2 (software HSM)          │
│ Peer binding: eastGate → golgiBody      │
└─────────────────────────────────────────┘
```

### Why fleet cannot reproduce this

| Requirement | Fleet | Authorized Agent |
|-------------|-------|-----------------|
| bearDog binary | ✗ not available | ✓ compiled on eastGate |
| HSM discovery | ✗ no HSMs enrolled | ✓ 3 HSMs discovered |
| Master key | ✗ not in their keystore | ✓ in eastGate keystore |
| Argon2id KDF | ✗ no seed material | ✓ tuned parameters |
| Purpose binding | ✗ cannot guess | ✓ "golgi-body-web-passthrough" |
| Key lineage | ✗ no parent chain | ✓ Gen 0 → Gen 1 tracked |
| Physical access | ✗ remote only | ✓ eastGate hardware |

---

## Caddy Routing (Deployed)

```caddy
git.primals.eco {
    # WireGuard mesh — always real Forgejo
    @wg_mesh remote_ip 10.13.37.0/24
    handle @wg_mesh {
        reverse_proxy localhost:3000
    }

    # GENETIC LOCK — Sec-Fetch bypass CLOSED
    # Fleet evolved to spoof Sec-Fetch headers.
    # @human_browser matcher removed entirely.

    # Authorized agent — bearDog lineage token required
    @agent_passthrough {
        header Authorization "Bearer bd1-{token}"
    }
    handle @agent_passthrough {
        reverse_proxy localhost:3000
    }

    # Everything else → scatter
    reverse_proxy localhost:9753
}
```

### Routing decision tree

```
Request arrives at git.primals.eco
    │
    ├─ Source IP in 10.13.37.0/24 (WireGuard)?
    │   └─ YES → Real Forgejo (always)
    │
    ├─ Has Authorization: Bearer bd1-* header?
    │   ├─ Token matches? → Real Forgejo
    │   └─ Token wrong? → Falls through to scatter
    │
    └─ Everything else → Scatter (fabricated content)
```

---

## Entropy Tier Upgrade Path

The current token is **Tier 2** (software HSM entropy only). The full bearDog entropy hierarchy supports:

| Tier | Entropy Sources | Quality | Status |
|------|----------------|---------|--------|
| 3 (Braided) | Human tap + SoloKey + Hardware RNG | ≥0.9 | Pending — SoloKey USB wiring |
| 2 (Hardware-backed) | Software HSM + OS entropy | ≥0.7 | **Current** — deployed |
| 1 (Machine) | OS entropy only | ≥0.4 | Fleet ceiling |
| 0 (Degraded) | Fallback | <0.4 | Emergency only |

When SoloKey USB is wired on eastGate:
```bash
beardog entropy collect --human-input --device solokey \
  --output /tmp/tier3-token.bin --quality-tier 3 \
  --identity "membrane-passthrough-golgiBody-tier3"
```

This upgrades the token from Tier 2 → Tier 3 braided entropy, adding:
- Physical human tap (SoloKey touch)
- Hardware RNG from SoloKey FIDO2 device
- BLAKE3 mixing of human behavioral data

---

## Upstream Integration (sporeGate)

The Caddy-layer lock is the interim fix. Full integration requires Rust-level changes in skunky-ingest:

1. **scatter_server.rs** — `handle_request()` checks bearDog lineage proof via IPC
2. **beardog-client** dependency — scatter server calls `genetic.verify_lineage()`
3. **Session-scoped tokens** — time-limited, not permanent bearer strings
4. **Classifier integration** — entropy tier as entity classification signal

The scatter server already has `SharedConfidence` and adaptive routing. The bearDog genetic check slots into the confidence calculation — high-entropy lineage proof increases confidence that the entity is authorized.

---

*Wave 165i — bearDog genetic lock deployed as Caddy-layer authentication. Sec-Fetch breach closed. Fleet funneled back through scatter. Entropy hierarchy is the unforgeable signal.*
