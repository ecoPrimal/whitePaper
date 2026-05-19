# NUCLEUS Sovereignty Architecture — From Calibration to Sovereign Primals

**Date**: May 19, 2026 (updated from May 15 baseline)
**Status**: Active evolution — shadow parity operational
**Lineage**: gen3 cell membrane (May 10) → gen4 sovereignty architecture (May 15) → shadow runs (May 19)

---

## The Arc

NUCLEUS began as a local deployment tool — a way to stand up 13 primals
on gate hardware and run science workloads. That was Phase 1: covalent
bonding, full trust, one machine.

Phase 2 opened the cell to external traffic: ABG collaborators accessing
JupyterHub through Cloudflare Tunnel, authenticated by PAM, gated by
Cloudflare Access. This worked. But every request passed through
Cloudflare's edge servers — they saw all the TLS handshakes, all the DNS
queries, all the HTTP traffic. The cell had a membrane, but the membrane
was rented.

The sovereignty evolution is the systematic replacement of rented
membrane with owned membrane. Not by ripping things out, but by growing
primal capabilities alongside the externals and proving they work better.

---

## What Has Evolved

### Layer 1: External Security (Horizon 1) — COMPLETE

Every gap discovered during the Phase 2 pen tests has been resolved:

| Category | Gaps Resolved | Method |
|----------|---------------|--------|
| RPC authentication | JH-0 through JH-5 | MethodGate enforced (13/13 primals) |
| Network binding | DF-1 (5 primals on 0.0.0.0) | Phase 60 PG-55 default 127.0.0.1 |
| Process isolation | hidepid=2 | fstab mount option |
| DNS exfiltration | JH-8 | iptables restrict to local resolver |
| Supply chain | JH-9 | Root-owned conda envs (755) |
| Session management | JH-4, H1-06 | BearDog `auth.issue_session`, cookie rotation |
| ABG tier enforcement | H1-04, H1-05 | setfacl on systemctl, python3 |

**Validation**: darkforest v0.2.1 — 267 PASS, 0 FAIL, 1 WARN, 11 INFO.
5-layer `security_validation.sh`. Dark Forest Glacial Gate PASS (33/33 checks).
Membrane audit (VPS): 17 PASS, 0 FAIL, 1 SKIP.

This layer is the **foundation**. Everything above it assumes Horizon 1
is complete. No sovereignty replacement begins until the local security
posture is validated.

### Layer 2: Sovereignty Parallels (Horizon 2) — IN PROGRESS

Four sovereign systems running in parallel with their external
counterparts:

#### S1: BearDog TLS Shadow (H2-12) — LIVE on ironGate + VPS
- BearDog v0.9.0 on :8443 alongside Cloudflare :443
- **6-12ms RPC latency** (ironGate loopback) vs 163ms Cloudflare TTFB p95 (13-27× faster)
- **10-14ms RPC** on VPS loopback, **71ms** from ironGate → VPS over network
- rustls X.509 termination, per-IP sliding-window rate limiter
- `beardog-acme` crate shipped (Wave 106): HTTP-01, cert storage, hot-reload
- `btsp_tls_parity.sh` measuring JSON-RPC round-trip via `nc -q 0`
- Deployed on VPS as `beardog-tls-shadow.service` (systemd, PrivateTmp, 64MB cap)
- **What it proves**: Sovereign TLS massively outperforms rented TLS; VPS deployment works

#### Channel 3 TLS Surface — LIVE (membrane.primals.eco)
- DNS-only A record → 157.230.3.183 (grey-cloud, not proxied)
- ACME cert auto-obtained (Let's Encrypt E8, valid to Aug 13 2026)
- Caddy serves sporePrint content (19MB synced from gate) + health/status endpoints
- **Content parity PASS**: VPS 67ms TTFB vs GitHub Pages 111ms (40% faster, May 19)
- **What it proves**: VPS can serve content faster than commercial CDN

#### S2: Songbird NAT Relay (H2-14) — LIVE on VPS
- cellMembrane fieldMouse on 157.230.3.183 (DigitalOcean nyc1)
- Songbird TURN relay v0.2.1 on UDP :3478, **100% reachable** (15/15 probes over 3 days)
- `songbird-relay.service` active since May 16 (3+ days continuous)
- 5-tier ConnectionFallbackChain shipped (direct → STUN → lineage → TURN → emergency)
- **What it proves**: NAT traversal works on owned infrastructure, relay is stable

#### S3: Content Hosting — LIVE on VPS
- petalTongue web mode on :8080, deployed as `petaltongue-web.service`
- NestGate 8 `content.*` methods on 4 transports (Session 60)
- **TTFB parity**: 0.4ms local / 67ms VPS vs 111ms GitHub Pages — PASS
- **Content hash parity**: pending (sporePrint not mirrored via `content.put` yet)
- **What it proves**: Sovereign content delivery is faster; mirror is the remaining step

#### S4: BTSP Dual-Auth (H2-01) — READY
- Ed25519 ionic tokens with TTL/expiry (Wave 102)
- BTSP Phase 3 AEAD (ChaCha20-Poly1305) on all 13 primals
- FIDO2/CTAP2 IPC surface for hardware attestation (Wave 103)
- JupyterHub dual-auth spec shipped (`JUPYTERHUB_DUAL_AUTH_INTEGRATION.md`, Wave 106)
- **What remains**: Implement dual-auth middleware, session mapping, <50ms p95 target

#### DNS-over-TLS (Step 4) — INTERMEDIATE
- Gate resolves via DoT to Cloudflare (1.0.0.1) with Quad9 fallback
- ISP resolver bypassed — no DNS metadata leak to AT&T
- DoT baseline captured: 3-8ms latency, 10/10 success, all 6 domains
- Sovereign resolver (knot-dns) pending (H2-17→20)
- **What it proves**: DNS encryption works; sovereignty needs own resolver

### Layer 3: Content Pipeline (H2-05/06) — READY

NestGate Session 60 shipped `content.*` transport parity — 8 methods on
4 transports. The full pipeline for sovereign content serving is
unblocked:

```
Content creation (gate)
  → NestGate content.put (content-addressed, BLAKE3)
  → publish_sporeprint.sh (push to VPS cache)
  → VPS serves static from /var/cache/membrane/nestgate/
  → petalTongue renders dynamic content (backend=nestgate)
```

This replaces GitHub Pages (extracellular CDN) with sovereign content
delivery through the membrane. The CDN remains as fallback.

### Layer 4: Forgejo Primary (H3-04) — ACTIVE

GitHub is no longer the source of truth. Forgejo hosts all 32 repositories
across 3 organizations. The workflow is:

```
Developer → git push forgejo (primary)
         → git push origin (mirror to GitHub, outer membrane)
```

32 repos mirrored. Dual-push configured. `.netrc` credential caching.
SSH server enabled on :2222. GitHub becomes the outer membrane — visible,
public, but not authoritative.

**Remaining**: Forgejo Actions (74 workflow files to port from GitHub
Actions) and GitHub-to-read-only mirror (Forgejo webhook push).

---

## What Has Been Validated as Secure

### Gate (Intracellular) — Dark Forest PASS

| Validation | Result | Tool |
|------------|--------|------|
| 5-layer security | 267+ PASS, 0 FAIL | `security_validation.sh` |
| Dark Forest gate | 33/33 PASS, 5 pillars | `dark_forest_gate_local.sh` |
| MethodGate enforcement | 13/13 confirmed | TCP probe |
| Primal binding | 14 ports on 127.0.0.1 | UFW + iptables |
| ABG tier isolation | 62 assertions, 0 FAIL | `tier_enforcement_test.sh` |
| Provenance pipeline | 6/12 workloads through trio | `provenance_pipeline.sh` |
| Observer surface | 86 PASS, 0 FAIL | `darkforest --suite observer` |

### VPS (Inner Membrane) — 17 PASS

| Validation | Result | Tool |
|------------|--------|------|
| Membrane audit | 17 PASS, 0 FAIL, 1 SKIP | `darkforest_membrane.sh` |
| SSH hardening | Key-only, fail2ban active | MEM-02, MEM-03 |
| Firewall posture | deny-default, targeted allows | MEM-04 |
| TURN auth rejection | 0 bytes to unauthenticated | MEM-05 |
| Credential encryption | DO token AES-256-GCM | MEM-15 |
| Service inventory | No unnecessary services | MEM-06 |

### Baselines Captured

| External | Duration | Key Metrics |
|----------|----------|-------------|
| Cloudflare TLS | 9 days, 950 samples | p50=73ms, p95=101ms |
| Cloudflare TTFB | 9 days, 950 samples | p50=119ms, p95=190ms |
| DNS-over-TLS | 10 probes | 3-8ms, 100% success |
| Songbird TURN | 10 probes | 100% reachable |

---

## What Remains

### Horizon 2 — Active Work

| System | External | Primal Replacement | Status | Blocks |
|--------|----------|-------------------|--------|--------|
| TLS termination | Cloudflare TLS | BearDog → Songbird (via Caddy transitional) | Shadow LIVE, needs formal 7-day | DNS grey-cloud |
| NAT traversal | cloudflared | Songbird TURN | LIVE, needs HTTP parity test | Integration testing |
| Auth | PAM passwords | BTSP ionic tokens | Dual-auth active | 7-day shadow clean |
| DNS authority | Cloudflare NS | knot-dns on VPS | DoT intermediate | VPS has headroom |
| DNS recursion | Cloudflare DoT | unbound local | Baseline captured | Low effort |
| Content serving | GitHub Pages | NestGate + petalTongue | Pipeline ready | Wire and test |

### Horizon 3 — Future

| System | External | Primal Replacement | Status |
|--------|----------|-------------------|--------|
| CI/CD | GitHub Actions | Forgejo Actions | 74 workflows to port |
| Source hosting | GitHub repos | Forgejo primary | **ACTIVE** (32 repos) |
| Package registry | crates.io / PyPI | NestGate + private registry | Low priority |
| AI inference | Anthropic / OpenAI | Ollama + barraCuda WGSL | Partial |
| Container registry | Docker Hub / ghcr.io | NestGate OCI store | Unblocked |
| Cross-primal auth | Manual token distribution | biomeOS CompositionContext | Unblocked |
| Audit forwarding | Local ring buffer | skunkBat → rhizoCrypt DAG | Unblocked |

### Irreducible Externals (never sovereign)
- Domain registrar (primals.eco)
- Linux kernel / systemd
- NVIDIA GPU drivers
- Let's Encrypt / ACME (browser trust chain)
- VPS commodity substrate (~$12/mo DigitalOcean)

---

## The Evolution Pattern

The pattern is glacial. Each capability builds on the previous:

```
Phase 1 (Covalent)     → 13 primals on one gate, provenance pipeline
Phase 2 (Ionic)        → ABG access, tunnel, multi-gate, membrane
Phase 3 (Self-Hosted)  → BTSP replaces TLS, Songbird replaces tunnel
Phase 4 (Full NUCLEUS) → biomeOS as OS, zero external dependencies
```

Nothing is removed until it is replaced. Nothing is replaced until the
replacement proves parity. The external services are calibration
instruments — they tell us what "good enough" looks like, and the
primals must exceed that bar.

The current moment: we are in the **interstadial-to-stadial transition**.
The interstadial pre-wired all sovereignty capabilities. The stadial
will drive cutover through external validation — Cloudflare baselines,
upstream peers, Barrick Lab, community frameworks.

The glacial metaphor is precise: the ice sheet advances when external
pressure (baselines, peers, real users) forces the system to evolve.
The warm period (interstadial) wires the plumbing. The cold period
(stadial) tests it under load.

---

## Relationship to Other Architecture Documents

| Document | What It Covers |
|----------|---------------|
| `MEMBRANE_CHANNEL_ARCHITECTURE.md` | The three channels (Signal/Relay/Surface) |
| `CELLMEMBRANE_FIELDMOUSE_ARCHITECTURE.md` | VPS deployment model and evolution |
| `TUNNEL_EVOLUTION.md` | Step-by-step external replacement roadmap |
| `SOVEREIGNTY_VALIDATION_PROTOCOL.md` | Calibrate → shadow → cutover methodology |
| `COMPLETE_DEPENDENCY_INVENTORY.md` | Full 40+ dependency map |
| `EVOLUTION_GAPS.md` | Living gap tracker across 3 horizons |
| `SOVEREIGNTY_STANDARDS.md` (wateringHole) | Ecosystem-wide standards and behaviors |
