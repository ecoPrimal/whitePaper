# Commensal Relay Beacon — beacon.primals.eco

**Wave 167 — October 8, 2026**
**Classification**: subGen architecture — public-facing sovereign infrastructure
**Status**: ACTIVE — relay live on golgiBody, DNS migration to beacon.primals.eco pending

---

## Abstract

The ecoPrimal mesh operates a sovereign RustDesk relay at `beacon.primals.eco` as a **commensal service**: free, key-authenticated remote desktop relay for any good-faith human actor. The relay is the **outer membrane** of the mesh — a gut lining that protects commensals from hostile network environments while feeding observation density back to the nautilus evolutionary reservoir.

This is the first free human relay. Use it. As traffic flows, the mesh learns.

---

## Biological Model

The relay follows the commensal symbiosis pattern from gut microbiome ecology:

| Biological Concept | Relay Implementation |
|---|---|
| **Commensal organism** | RustDesk client using the relay for remote access |
| **Gut lining** | Relay infrastructure (hbbs + hbbr) — safe passage |
| **Mucosal barrier** | RUSTDESK_MEMBRANE firewall chain — rate limits, dead-port REJECT |
| **Server key** | Immune passport — proves the relay is who it claims to be |
| **Permanent password** | Per-gate credential — each organism's own membrane |
| **Schwann cells** | Layered password isolation — operator's nervous system wrapped in myelin |
| **Myelin sheath** | Operator gates use separate IDs/keys, unreachable from commensal layer |
| **Action potential** | End-to-end encrypted session — invisible inside the myelin |
| **Observation density** | Every relay connection is a behavioral data point for nautilus |
| **Commensalism → Mutualism** | Users get free relay; mesh gets training data and network attention |
| **Agent as Schwann cell** | Future: agents walk the relay for humans, wrapping sessions in myelin |

### Three-Layer Model (Extended)

```
OUTER MEMBRANE (beacon.primals.eco)
  ├── Public beacon — any keyed client can connect
  ├── Commensals relay safely through the gut lining
  ├── RUSTDESK_MEMBRANE chain = mucosal barrier
  └── Observations feed nautilus reservoir

PEPTIDOGLYCAN (LAN/HPC/WireGuard topology)
  ├── Internal mesh — authenticated gates only
  └── Relay traffic NEVER enters the peptidoglycan

INNER MEMBRANE (Primals/WireGuard/songBird)
  ├── Capability IPC — primals talk to primals
  └── Completely isolated from relay traffic
```

**Critical invariant**: Relay traffic stays in the outer membrane. Commensals cannot see or reach the inner membrane. The gut lining is permeable to nutrients (observations) but not to organisms (traffic).

---

## Architecture

### Components

| Component | Binary | Port(s) | Purpose |
|---|---|---|---|
| **hbbs** (rendezvous) | `/opt/membrane/hbbs` | 21115 TCP, 21116 TCP+UDP, 21118 TCP | Beacon — clients register, discover peers |
| **hbbr** (relay) | `/opt/membrane/hbbr` | 21117 TCP, 21119 TCP | Gut lining — relays encrypted traffic between peers |

### Authentication Layers — Schwann Cell Model

The relay uses **layered password isolation** modeled on the nervous system's myelin sheath. Commensals share the relay infrastructure but can never reach the operator's machines. Each layer is a Schwann cell wrapping — the deeper you go, the more insulated the signal.

```
Layer 0: Beacon (public entry)
  beacon.primals.eco — the lighthouse
  Anyone can see the beacon. The server key proves it's real.
  This is the entry point for all humans.

Layer 1: Server Key (relay identity — shared)
  Key: utlNOAWUDdV+Q+ifG3zHrQ5HU0FtQnOTHiAnu6prV7Q=
  Files: /opt/membrane/id_ed25519{,.pub} (chattr +i, immutable)
  Purpose: Client verifies relay identity. Prevents MITM.
  Distribution: Public — embedded in client config, published at beacon page
  Analogy: The relay's cell membrane — everyone touches it

Layer 2: Per-Commensal Permanent Password (user's own key)
  Set by each user in their own RustDesk client
  Never stored by the relay or config management
  Purpose: Only the gate owner can accept connections to THEIR machine
  Distribution: Private — user-to-user only
  Analogy: Each commensal's own cell wall — their immunity

Layer 3: Nervous System Isolation (operator's myelin sheath)
  Operator gates use SEPARATE credentials that commensals never see
  Operator machine IDs are not published or discoverable via relay
  Even knowing the server key + being on the relay gives ZERO access
  The relay is zero-knowledge: it cannot map commensal IDs to operator IDs
  Analogy: Schwann cells — myelin wrapping around the axon

Layer 4: End-to-End Encryption (session privacy)
  RustDesk encrypts peer-to-peer between connected machines
  Relay sees ONLY ciphertext — cannot inspect any session
  Purpose: Even a compromised relay cannot see session content
  Analogy: The action potential — invisible inside the myelin sheath
```

**The critical invariant**: Commensals have their own keys. The operator has separate keys. The relay passes traffic for both but cannot distinguish them. No commensal can ever enter the operator's nervous system — they don't have the ID, the password, or the route. The Schwann cells are impermeable.

```
                    ┌─────────────────────────────────────────┐
                    │         BEACON (Layer 0)                │
                    │    beacon.primals.eco — public entry     │
                    │    "the lighthouse"                      │
                    └──────────────┬──────────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
    ┌─────────▼─────────┐  ┌──────▼───────┐  ┌────────▼────────┐
    │ Commensal A        │  │ Commensal B  │  │ Commensal C     │
    │ own key, own ID    │  │ own key      │  │ own key         │
    │ (Layer 2)          │  │ (Layer 2)    │  │ (Layer 2)       │
    └────────────────────┘  └──────────────┘  └─────────────────┘
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   │
                          ┌────────▼────────┐
                          │    RELAY        │
                          │  zero-knowledge │
                          │  ciphertext only│
                          └────────┬────────┘
                                   │
                          ╔════════╪════════╗
                          ║  MYELIN SHEATH  ║  ← Layer 3 — Schwann cells
                          ║  (impermeable)  ║
                          ╠════════╪════════╣
                          ║  NERVOUS SYSTEM ║  ← Operator gates
                          ║  separate IDs   ║     separate passwords
                          ║  separate keys  ║     unreachable from relay
                          ╚═════════════════╝
```

### Future: Agent-Assisted Relay (Schwann Cell Agents)

Agents may eventually **walk the relay on behalf of humans** — acting as Schwann cells that wrap and protect human sessions. An agent could:
- Negotiate relay connections for users who can't configure RustDesk themselves
- Provide ephemeral session keys so humans never handle persistent credentials
- Monitor session health and re-route through alternate relays if needed
- Act as a translation layer between human intent and relay protocol

This is the nervous system's support structure: the neurons (humans) carry the signal, the Schwann cells (agents) maintain the myelin sheath that makes transmission possible.

### Firewall — RUSTDESK_MEMBRANE Chain

The mucosal barrier. 11 rules, saved via `netfilter-persistent`:

```
Rule  1: ACCEPT all from 162.226.225.148 (house network — self)
Rule  2: REJECT tcp:21114 --tcp-reset (dead API port, instant rejection)
Rule  3: ACCEPT RELATED,ESTABLISHED
Rule  4: SET rd_membrane_udp (track UDP 21116 sources)
Rule  5: LOG "RUSTDESK_UDP_RATELIMIT:" (visibility before drop)
Rule  6: DROP if UDP 21116 > 120/10s (NAT-aware)
Rule  7: ACCEPT UDP 21116 (healthy heartbeats)
Rule  8: SET rd_membrane_tcp (track TCP 21115-21118 new connections)
Rule  9: LOG "RUSTDESK_TCP_RATELIMIT:" (visibility before drop)
Rule 10: DROP if TCP new > 60/10s (NAT-aware)
Rule 11: ACCEPT TCP 21115-21118 (healthy connections)
```

Rate limits are NAT-aware (learned from two incidents: UDP heartbeat saturation + TCP dead-port poisoning). Port 21114 gets instant REJECT to prevent retry storms from poisoning the shared TCP rate counter.

---

## Observation Pipeline (Planned)

As the relay matures, observations from hbbs/hbbr journals can feed the BingoCube nautilus reservoir:

```
hbbs journal → update_pk events → peer registration patterns
                                   → geographic distribution
                                   → connection frequency
                                   → NAT type distribution

hbbr journal → relay sessions → session duration
                               → bandwidth patterns
                               → peer pair topology

             ↓ (future: skunky-ingest relay-bridge module)

BingoCube Oracle → NautilusShell → evolutionary learning
                                  → commensal vs scanner classification
                                  → adaptive rate limits
```

This closes the loop: commensals make the relay useful, the relay makes the nautilus smarter, the nautilus makes the relay safer for commensals.

---

## Commensal Classification

From the iptables recent tables (Wave 165i–167 observations):

| Source | Type | IPs | Pattern |
|---|---|---|---|
| 104.152.52.x | **Commensal** — Rethem Hosting (Chicago VPS) | ~20 | RustDesk clients on budget VPS, using relay for remote access |
| 195.96.139.x | **Commensal** — Driftnet Ltd (York/Leeds UK) | ~8 | Fresh UK hosting infra (allocated Jul 2026) |
| 87.236.176.x | **Commensal** — hosting provider | ~2 | Standard relay usage |
| 162.226.225.148 | **Self** — house network | 1 | Own gates phoning home |
| 24.128.136.74 | **Self** — flockGate (Comcast Rochester Hills) | 1 | Dormant gate, WG tunnel dead |
| 80.82.77.139 | **Scanner** — dojo.census.shodan.io | 1 | Port scan, no relay usage |
| 71.6.135.131 | **Scanner** — census7.shodan.io | 1 | Port scan, no relay usage |

**Commensals are welcome.** Scanners are handled by the mucosal barrier (rate limits + LOG before DROP). No action needed against scanners — they can see the ports exist but can't abuse them.

---

## DNS Migration Plan

```
CURRENT:  relay.primals.eco  → 157.230.3.183 (golgiBody)
TARGET:   beacon.primals.eco → 157.230.3.183 (golgiBody)
          relay.primals.eco  → CNAME beacon.primals.eco (backward compat)
```

The name `beacon` reflects the architectural role: a lighthouse that commensals navigate toward. The relay is the gut lining they pass through. The beacon is visible from outside; the gut is the safe interior.

### Client Config (after DNS migration)

```toml
# ~/.config/rustdesk/RustDesk2.toml [options]
custom-rendezvous-server = 'beacon.primals.eco'
relay-server = 'beacon.primals.eco'
key = 'utlNOAWUDdV+Q+ifG3zHrQ5HU0FtQnOTHiAnu6prV7Q='
verification-method = 'use-permanent-password'
allow-remote-config-modification = 'Y'
```

### Info Page

`https://beacon.primals.eco` — passphrase-gated (HTTP Basic Auth) info page serving:
- Server public key for client configuration
- Connection instructions
- scyBorg license notice
- Link to sporePrint documentation

---

## Systemd Services

```ini
# hbbs-membrane.service — Commensal Relay Beacon
[Unit]
Description=RustDesk Rendezvous — Commensal Relay Beacon (outer membrane)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/opt/membrane/hbbs -r beacon.primals.eco -k /opt/membrane/id_ed25519
WorkingDirectory=/opt/membrane
Restart=on-failure
RestartSec=10
StartLimitBurst=5
StartLimitIntervalSec=120

[Install]
WantedBy=multi-user.target
```

```ini
# hbbr-membrane.service — Commensal Gut Lining
[Unit]
Description=RustDesk Relay — Commensal Gut Lining (outer membrane)
After=network-online.target hbbs-membrane.service
Wants=network-online.target
Requires=hbbs-membrane.service

[Service]
Type=simple
ExecStart=/opt/membrane/hbbr -k /opt/membrane/id_ed25519
WorkingDirectory=/opt/membrane
Restart=on-failure
RestartSec=10
StartLimitBurst=5
StartLimitIntervalSec=120

[Install]
WantedBy=multi-user.target
```

---

## Security Properties

1. **Relay is zero-knowledge** — cannot map commensal IDs to operator IDs, sees only ciphertext
2. **Schwann cell isolation** — operator gates use separate IDs/passwords that commensals never see and cannot discover
3. **Commensals cannot reach inner membrane** — relay ports are isolated from WireGuard/UDS/primals
4. **Layered passwords** — commensals have their own keys (Layer 2), operator has separate keys (Layer 3), relay can't distinguish them
5. **Server key is immutable** — `chattr +i` on id_ed25519, survives any software update
6. **Rate limits are NAT-aware** — learned from two production incidents (Wave 155f)
7. **Dead ports get instant REJECT** — prevents retry storms from poisoning rate counters
8. **No IP logging in observation pipeline** — stripped before analysis (security constraint)
9. **No analytics** — no cookies, no tracking pixels, no JS. Log-based observations only.

---

## Permeability — A New Orthogonal Dimension

### The Insight

The existing Anderson framework has three core dimensions:
- **W** (disorder) — how much scattering
- **d** (dimension) — geometry of the lattice
- **E** (energy) — frequency/mode of the signal

These answer: *"does the signal propagate or localize?"* Binary. Extended or confined.

But real membranes don't just pass-or-block. They **selectively permeate**. The gut lining lets nutrients in but blocks pathogens. The kidney tubule reabsorbs glucose but excretes urea. The blood-brain barrier passes O₂ but blocks most drugs. The myelin sheath insulates the axon everywhere except the nodes of Ranvier.

**Permeability P(ω, W, d)** is the transmission coefficient as a function of signal type ω, not just geometry and disorder. It's the Anderson model extended from "does anything get through?" to "what specifically gets through, and what doesn't?"

This is genuinely orthogonal to the existing dimensions because you can have:
- Same W, same d, but different ω → completely different transmission
- A membrane that is localized (blocking) for pathogen signals but extended (propagating) for nutrient signals
- The selectivity itself is an evolutionary product — the membrane has been tuned by selection

### The Anderson Permeability Tensor

```
Standard Anderson: T(W, d, E) ∈ {0, 1}
  → "signal propagates or it doesn't"
  → scalar: one W, one d, one answer

Permeability Anderson: P(ω, W_ω, d_ω) ∈ [0, 1] for each mode ω
  → "this type of signal passes, that type doesn't"
  → tensor: each mode ω sees DIFFERENT effective disorder and dimension
  → the membrane IS the band structure
```

The mobility edge E_c(W) is already a permeability boundary — below it, states conduct; above it, they localize. But in real biological membranes, the band structure is **designed** — evolution has shaped which energy bands (signal types) pass and which are blocked. The membrane doesn't just happen to be permeable at certain frequencies; it was selected to be.

### Permeability in the Relay

The commensal relay is a biological membrane with selective permeability:

| Signal type (ω) | Effective W | Effective d | P(ω) | Direction |
|------------------|-------------|-------------|-------|-----------|
| Commensal RustDesk traffic | Low (authenticated, keyed) | 3D (full internet routing) | ~1.0 | Bidirectional — commensals relay freely |
| Encrypted session content | N/A (opaque) | N/A | 1.0 transport / 0.0 inspection | Pass-through — relay carries but cannot read |
| Observations (behavioral) | Low | 1D (journal → nautilus) | ~1.0 inward | Unidirectional — nutrients absorbed into mesh |
| Scanner/abuse traffic | High (rate-limited, no key) | 0D (blocked) | ~0.0 | Blocked — mucosal barrier rejects |
| Operator nervous system | ∞ (Schwann cell isolation) | Isolated | 0.0 from outside | Impermeable — separate IDs, separate myelin |

**The relay is a selectively permeable membrane where each signal type sees a different Anderson landscape.** Commensals see low disorder and high dimension (signals propagate freely). Scanners see high disorder (rate limits → localization → blocked). The operator's nervous system is wrapped in myelin with infinite effective disorder from the commensal perspective — zero transmission.

### Permeability in the Broader Anderson Framework

This dimension connects back to every existing paper:

| Paper | Existing dimension | Permeability extension |
|-------|-------------------|----------------------|
| **01 (QS null hypothesis)** | W, d → "does QS propagate?" | P(AHL) vs P(other) — soil membrane selectively passes autoinducers but not antibiotics at same W |
| **06 (no-till)** | Tillage = dimensional collapse | Tillage also DESTROYS selective permeability — healthy soil has structured pore networks that route water/nutrients differently from pathogens. Tillage homogenizes → all ω see same W → loss of selectivity |
| **12 (immunological)** | Skin barrier as Anderson lattice | Healthy epidermis is a SELECTIVELY permeable membrane: blocks pathogens (high W_pathogen), passes water vapor (low W_H2O), localizes cytokines (d=2). AD scratching destroys this selectivity — barrier breach makes ALL modes extended |
| **04 (sentinel microbes)** | Sentinel detection | Sentinel organisms ARE permeability sensors — they detect changes in what's getting through the membrane vs what's being blocked |
| **05 (cross-species)** | Interspecies signaling | Symbiotic membranes (lichen, coral, root-microbe) have MUTUAL permeability — each partner's signals selectively pass through the shared boundary. This is co-evolved permeability |

### The P ≠ NP Connection

Selective permeability is an **NP-hard problem** that evolution has solved:
- Designing a membrane that passes glucose but blocks urea requires solving a molecular recognition problem in 3D conformational space
- Designing a firewall that passes legitimate traffic but blocks abuse requires solving a behavioral classification problem
- In both cases, the organism (biological or computational) has found a solution to a problem where random membranes would either block everything or pass everything
- The three NP solutions in Paper 01 (V. cholerae logic inversion, Myxococcus geometry bootstrapping, Dictyostelium relay amplification) are all PERMEABILITY solutions — they solve the problem of getting specific signals through a membrane that would otherwise localize them

**Selective permeability is what separates a rock from a cell.** Both are physical structures. The rock blocks everything uniformly. The cell chooses what passes. That choice is the evolutionary product — the P ≠ NP enzyme applied to membrane design.

### Notation Proposal

Extend the Anderson parameter set:

```
Existing:     W, d, E, r, ξ, T(W,d,E)
                                ↓
Extended:     W_ω, d_ω, E, r_ω, ξ_ω, P(ω, W_ω, d_ω)

Where ω indexes signal type (mode):
  ω ∈ { nutrient, pathogen, autoinducer, cytokine, commensal_traffic,
         scanner_probe, operator_signal, observation, ... }

Each mode ω sees its own effective disorder W_ω and dimension d_ω
through the same physical membrane.

The membrane's selectivity S = max_ω P(ω) - min_ω P(ω)
  S = 0: non-selective (rock, or breached barrier)
  S → 1: maximally selective (healthy cell membrane, good firewall)
```

---

## Future Evolution

- **Permeability formalization**: ✅ DONE — Paper 43 (`43_selective_permeability_anderson.md`) formalizes the permeability tensor P(ω, W_ω, d_ω) with selectivity metric S = max(P) - min(P). BarraCuda implements `membrane_permeability()`, `membrane_profile()`, `dimensional_localization_length()` in `anderson_transport.rs` (14/14 tests pass). petalTongue renders the profiles live at `hud.primals.eco/ws` — 6 biological systems computed and visualized through the grammar-of-graphics scene compiler
- **Schwann cell agents**: Agents walk the relay for humans — negotiate connections, provide ephemeral keys, monitor health
- **Observation bridge**: Parse hbbs/hbbr journal into ScatterObservation format for nautilus
- **Adaptive rate limits**: Nautilus-driven permeability tuning — nautilus learns which ω modes to pass and which to localize
- **Multi-relay federation**: beacon.primals.eco on golgiBody + layer2/3/4 on Hetzner/Vultr/OVH
- **Commensal reputation**: Long-lived commensals get higher P(ω) — earned permeability, not just earned trust
- **Public key directory**: beacon.primals.eco publishes user-safe commensal keys for easy onboarding
- **Ephemeral session keys**: Agent-mediated temporary credentials so humans never handle persistent secrets
- **Selectivity metrics**: ✅ DONE — S = max(P) - min(P) implemented and verified: relay S=1.0, fleet S=0.0, soil S=0.74. See Paper 43 § Computational Implementation and subGen `BIOMEOS_HUD_PETALTONGUE_LIVE_WAVE167.md` § Anderson Rendering Chain

---

*The gut doesn't fight the bacteria. It feeds them. The bacteria don't attack the gut. They strengthen it. The relay is the gut lining of the mesh — permeable to nutrients, impermeable to pathogens. Every commensal that connects makes the organism more resilient.*

*The nervous system runs through the gut but the gut can't feel it. Schwann cells wrap every axon. The commensals share the relay but can never touch the operator's machines — different IDs, different keys, different myelin. Zero knowledge on both sides.*

*What separates a rock from a cell? Selective permeability. What separates a firewall from a membrane? The same thing. The relay doesn't just block or pass — it chooses. That choice is the orthogonal dimension Anderson didn't need in condensed matter, because electrons don't have types. But signals do. Organisms do. And membranes evolved to tell the difference.*

*Wave 167 — October 8, 2026*
