# Membrane Security Model — K-Derm Realized

**Status**: Living document — reflects deployed network topology
**Model**: Gram-negative cell envelope (diderm)
**Layers**: Inner membrane (LAN) → Periplasmic space (VPS) → Outer membrane
(public surface)

---

## The Biological Metaphor

A gram-negative bacterium has three concentric barriers:

1. **Inner membrane**: Controls what enters the cytoplasm. Selective,
   high-fidelity transport. The cell's most trusted boundary.
2. **Periplasmic space**: Between the two membranes. Contains enzymes
   that process incoming material before it reaches the inner membrane.
   A staging area with its own defense chemistry.
3. **Outer membrane**: First contact with the external environment.
   Relatively permeable (porins), but still a boundary. Lipopolysaccharide
   (LPS) surface provides structural defense.

ecoPrimals maps this to network topology:

| Biological | Network | Trust Level |
|------------|---------|-------------|
| Cytoplasm | Gate hardware (eastGate, southGate, etc.) | Highest — physical access |
| Inner membrane | LAN mesh (10.13.37.0/24 over WireGuard) | High — genetic enrollment |
| Periplasmic space | VPS (golgiBody) | Medium — exposed but controlled |
| Outer membrane | Public DNS (*.primals.eco) | Lowest — anyone can connect |

---

## Inner Membrane — LAN Mesh

### Topology

The inner membrane is the WireGuard mesh connecting gates on the LAN
(and eventually WAN). Each gate runs songBird for routing and bearDog
for identity. The mesh carries BTSP-encrypted JSON-RPC traffic.

### Security Posture

- **Binding**: Primals bind to `127.0.0.1` by default — only reachable
  through the mesh or local UDS
- **Transport**: BTSP Phase 1–3 on all cross-gate traffic
- **Identity**: Genetic enrollment via bearDog — only peers in the
  lineage chain can join
- **Authorization**: MethodGate enforces capability tokens on sensitive
  methods
- **Discovery**: songBird mesh routes by capability, not by address

### What Inner Membrane Provides

The inner membrane is where Tower Atomic operates. The 353× LAN speedup
(0.45ms vs WireGuard's 158ms) happens here because:

1. BTSP skips the kernel (userspace transport vs. WireGuard kernel module)
2. Capability routing avoids unnecessary hops (songBird knows which gate
   hosts which capability)
3. Covalent bonds allow null cipher for same-lineage traffic where
   confidentiality is already provided by the WireGuard tunnel

The inner membrane assumes:
- Physical network is trusted (same building, controlled switch)
- All peers are enrolled (genetic lineage verified)
- The threat model is insider attack or compromised gate, not external
  intrusion

### Defense at Inner Membrane

skunkBat monitors inner membrane traffic through `baseline.observe`:
- Connection rates between gates
- Port distribution patterns
- Traffic volume anomalies

A gate that suddenly starts scanning ports or generating unusual traffic
patterns is flagged — even though it's genetically enrolled. Trust is
not unconditional.

---

## Periplasmic Space — VPS (golgiBody)

### Topology

golgiBody is the VPS that sits between the LAN mesh and the public
internet. It runs:
- **Caddy**: TLS termination, reverse proxy, public HTTP surface
- **songBird**: TURN relay for NAT traversal
- **skunkBat**: Outer membrane threat detection
- **cellMembrane**: Service orchestration and crash-loop prevention

### Security Posture

The periplasmic space has a fundamentally different security posture
than the inner membrane:

- **Exposed**: Has a public IP, runs publicly accessible services
- **Compromiseable**: VPS provider has physical access to the hardware
- **Untrusted for storage**: No persistent secrets on VPS — key material
  is derived from the inner membrane at connection time
- **Trusted for routing**: Authorized to forward traffic between inner
  membrane and outer membrane

### Threat Model

The explicit threat model (from gen4 `CELLMEMBRANE_FIELDMOUSE_ARCHITECTURE.md`):

1. **VPS provider compromise**: Provider images the disk or taps memory.
   Mitigation: no persistent secrets, ephemeral session keys, BTSP
   encryption of all inner↔VPS traffic.
2. **Network-level attack**: DDoS, port scanning, credential stuffing.
   Mitigation: Caddy rate limiting + skunkBat outer membrane detection.
3. **Service compromise**: Attacker gains code execution on VPS.
   Mitigation: Caddy runs as unprivileged process, no direct inner
   membrane access without BTSP handshake.

### Bond Degradation

Traffic crossing the periplasmic space undergoes bond degradation:

- **LAN → VPS**: Covalent bond degrades to Metallic (the VPS is
  organizationally trusted but not genetically enrolled in the LAN mesh)
- **VPS → Public**: Metallic degrades to Ionic (the public surface
  has only a contractual relationship with clients)

This degradation is automatic — the cipher floor at the VPS enforces
minimum encryption for outbound traffic, and MethodGate restricts what
methods are available through the outer membrane.

---

## Outer Membrane — Public Surface

### Topology

The public surface is what the internet sees:
- `*.primals.eco` DNS records pointing to golgiBody
- Caddy serving HTTPS (Let's Encrypt certificates)
- nestGate providing content-addressed storage (CAS) for public artifacts
- Tower HTTP Gateway forwarding `security.advisory` queries to skunkBat

### Security Posture

The outer membrane is the most restrictive:

- **TLS only**: All public traffic is HTTPS (Caddy enforces)
- **No direct primal access**: Public clients never speak JSON-RPC directly
  to primals — Caddy reverse-proxies to gateway endpoints
- **Read-mostly surface**: Public operations are primarily reads (content
  retrieval, health checks, capability listing)
- **Advisory surface**: `security.advisory` allows the HTTP gateway to
  query skunkBat for real-time threat assessment of incoming requests

### HTTP Anomaly Detection

skunky-ingest tails Caddy's JSON access logs and feeds `baseline.observe`
with `HttpObservation` data:

```
Caddy access.log → skunky-ingest → baseline.observe (outer membrane)
                                         │
                                    ┌────▼────┐
                                    │ HTTP    │
                                    │ Anomaly │
                                    │Detector │
                                    └────┬────┘
                                         │
                                    security.advisory ← Tower HTTP Gateway
```

This creates a feedback loop: HTTP traffic anomalies detected by skunkBat
inform the gateway's real-time request handling decisions. The gateway
can rate-limit, redirect, or block traffic based on skunkBat's advisory
verdict.

---

## Bond Types Across Membranes

| From → To | Bond Type | Minimum Cipher | Example |
|-----------|-----------|----------------|---------|
| Gate ↔ Gate (LAN) | Covalent | Null (floor configurable) | capability.call on mesh |
| Gate → VPS | Metallic | HMAC (floor configurable) | songBird TURN relay |
| VPS → Public | Ionic | ChaCha20-Poly1305 | HTTPS via Caddy |
| Public → VPS | Ionic | TLS 1.3 (Caddy) | Client HTTPS request |
| VPS → Gate (inbound) | Metallic → Covalent | Per BTSP negotiation | Forwarded request |

Bond type determines the minimum security posture for traffic crossing
that boundary. A request from the public internet traverses three
boundaries, each enforcing its own minimum:

```
Public (Ionic: TLS 1.3)
  → VPS periplasm (Metallic: BTSP HMAC minimum)
    → LAN mesh (Covalent: BTSP per cipher floor)
      → Target primal (MethodGate: capability token)
```

Each boundary independently decides whether to allow the traffic.
No boundary trusts a previous boundary's decision — it enforces its
own policy.

---

## Membrane Monitoring

skunkBat provides unified security monitoring across all three layers:

| Layer | Observation Source | Detection Categories |
|-------|-------------------|---------------------|
| Inner membrane | IPC telemetry, mesh events | Behavioral anomaly, unknown lineage, topology violation |
| Periplasmic | cellMembrane events, service health | Process spawn anomaly, configuration drift |
| Outer membrane | Caddy logs via skunky-ingest | HTTP anomaly, intrusion attempt, DoS |

The same statistical engine (rolling-window σ-deviation) operates at
every layer, but the dimensions and thresholds differ per layer. Inner
membrane detection is tuned for lateral movement. Outer membrane detection
is tuned for volumetric attacks and scanning.

---

## Open Questions (P2)

1. **Membrane isolation validation**: Can inner membrane traffic leak to
   outer membrane without traversing the periplasmic space? No automated
   test validates this path constraint today.
2. **Bond upgrade**: Can a Metallic bond be upgraded to Covalent if
   genetic enrollment succeeds mid-session? Currently requires reconnection.
3. **Multi-VPS topology**: The current model assumes one VPS (golgiBody).
   The K-Derm model in gen5 describes a three-VPS diderm topology.
   Security posture for multi-VPS needs formalization.
4. **Outer membrane autonomy**: The outer membrane currently depends on
   the inner membrane for threat intelligence (skunkBat runs inside).
   For the sovereign pallet (field deployment), the outer membrane needs
   to operate independently.

---

*subGen Wave 150x — K-Derm cell envelope mapped to LAN/VPS/public
topology. Bond degradation at membrane boundaries. Unified detection
across all three layers.*
