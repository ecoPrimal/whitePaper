# Sovereignty Shadow Evolution — S1-S4 Track Status (Wave 65)

**Gen5 Foundation** (evolved from gen4 `SOVEREIGNTY_EVOLUTION_NARRATIVE.md`)

---

## The Shadow Protocol

Every sovereignty replacement follows Calibrate → Shadow → Cutover
(see `wateringHole/SOVEREIGNTY_STANDARDS.md`). No external dependency
is removed until the primal replacement proves parity under real load.

---

## S1 — TLS Termination

| Stage | Component | Status |
|-------|-----------|--------|
| External | Cloudflare | **INACTIVE** |
| Sovereign | Caddy + Let's Encrypt :443 | **7-DAY GATE RUNNING** |
| Probe | `s1-tls-gate-probe.sh` | q15min on VPS, logging to CSV |
| Metric | 80ms TTFB, 0 TLS failures | Target: p95 < 500ms |
| Gate completes | ~June 7, 2026 | |

**Gen4→Gen5 evolution**: Gen4 used BearDog's custom TLS on :8443 for
BTSP protocol auth. Gen5 separates concerns: Caddy handles standard
TLS termination for web traffic, BearDog retains :8443 for BTSP
dual-auth. Cloudflare was disabled once Caddy proved stable.

---

## S2 — NAT Relay

| Stage | Component | Status |
|-------|-----------|--------|
| External | cloudflared | **INACTIVE** |
| Sovereign | Songbird TURN :3478 | **LIVE** (100% 3+ days) |
| Gate | 7-day 100% reachable | **PASSED** |

**Fully sovereign**. Songbird's TURN relay handles all NAT traversal
for RustDesk and inter-gate connectivity. No external dependency.

---

## S3 — Content Serving

| Stage | Component | Status |
|-------|-----------|--------|
| External | GitHub Pages (111ms) | **ACTIVE** (trailing mirror) |
| Sovereign | NestGate + petalTongue (67ms TTFB) | **LIVE** |
| Static | sporePrint via Caddy on golgiBody-ext | **LIVE** (226 pages, 746ms build) |
| Gate | 7-day TTFB parity | **PASSED** |

**Sovereign parity achieved**. GitHub Pages retained as external
linear ledger (trailing mirror), not as primary content source.

---

## S4 — Auth

| Stage | Component | Status |
|-------|-----------|--------|
| External | OAuth2/PAM proxy | Available but not primary |
| Sovereign | BearDog BTSP dual-auth | **SHADOW LIVE on ironGate** |
| Gate | 7-day p95 < 50ms | **BLOCKED** on ironGate services restart |

**Remaining work**: ironGate needs SSH port open and NUCLEUS services
restarted for formal 7-day S4 validation. BearDog's auth infrastructure
is complete (14,940+ tests, zero debt, UDS-only by default).

---

## membrane-shadow Coverage (Wave 65)

The `membrane-shadow` Rust crate is the agentic control plane for
all sovereignty operations. Gen4 used bash scripts; Gen5 is fully Rust:

| Domain | Commands | Module | Status |
|--------|----------|--------|--------|
| Repo management | `repo.list`, `repo.create`, `repo.delete`, `repo.info` | `dispatch.rs` + `forgejo.rs` | Operational |
| Mirror management | `mirror.push-create`, `mirror.list`, `mirror.sync` | `dispatch.rs` + `forgejo.rs` | Operational |
| Token lifecycle | `auth.token.create`, `auth.token.revoke`, `auth.token.list` | `dispatch.rs` | Operational |
| Gate management | `gate.info`, `gate.pull`, `gate.check` | `gate.rs` | Operational |
| Service control | `gate.service.list`, `gate.service.start/stop/restart` | `dispatch.rs` | Operational |
| Temporal sync | `temporal.cascade`, `temporal.sync`, `temporal.check` | `temporal.rs` | Operational |
| Impulse coordination | `impulse.post`, `impulse.ack`, `impulse.fire`, `impulse.archive` | `impulse.rs` | Operational |
| Context braids | `context.weave`, `context.sense`, `context.clear` | `context.rs` | Operational |
| Potential sensing | `potential.sense`, `potential.check` | `impulse.rs` | Operational |
| Plasmid fetch | `plasmid.fetch`, `plasmid.list` | `plasmid.rs` | Operational |
| Manifest info | `manifest.info`, `manifest.gates` | `manifest.rs` | Operational |
| Identity resolution | `identity.resolve` | `identity.rs` | Operational |

### Architecture

```
membrane CLI (main.rs, 129 lines)
    ├── cli.rs (176L) — argument parsing helpers
    ├── dispatch.rs (709L) — command routing by domain prefix
    ├── temporal.rs (638L) — waterFall sync engine
    ├── impulse.rs (712L) — impulse/potential coordination
    ├── context.rs (464L) — context braid weaving
    ├── plasmid.rs (423L) — binary artifact fetching (was bash)
    ├── git_ops.rs (94L) — shared git add/commit/push
    ├── forgejo.rs — Forgejo API client
    ├── gate.rs — VPS gate operations
    ├── config.rs — membrane.toml + env config
    ├── manifest.rs — ecosystem_manifest.toml reader
    └── identity.rs — capability-based gate detection
```

---

## DNS Sovereignty

| Component | Status |
|-----------|--------|
| ns1.primals.eco (golgiBody) | **LIVE** — Knot DNS primary |
| ns2.primals.eco (golgiBody-ext) | **LIVE** — Knot DNS secondary, zone transfers confirmed |
| DNSSEC | **ACTIVE** |
| Registrar cutover | **PENDING** — glue records + DS record needed at registrar |

Once the registrar points to sovereign nameservers, Cloudflare is
fully removed from the DNS resolution path.

---

## Remaining Sovereignty Debt

| Item | Blocked By | Priority |
|------|-----------|----------|
| S4 formal 7-day gate | ironGate services restart | HIGH |
| DNS NS registrar cutover | Manual registrar action | HIGH |
| Forgejo Actions CI | Self-hosted runner SPOF resolution | MEDIUM |
| Caddy → BearDog ACME | Not started (Caddy is working) | LOW |
| BearDog Vault (encrypted creds at rest) | Phase 2 design | LOW |
| Multi-vendor peptidoglycan | Additional VPS provider account | FUTURE |

---

## Key Files

| File | Purpose |
|------|---------|
| `wateringHole/SOVEREIGNTY_STANDARDS.md` | Calibrate→Shadow→Cutover protocol |
| `wateringHole/GLACIAL_SHIFT_READINESS.md` | Readiness matrix with S1-S4 status |
| `wateringHole/scripts/s1-tls-gate-probe.sh` | S1 TLS probe script |
| `wateringHole/scripts/DNS_NS_CUTOVER_INSTRUCTIONS.md` | DNS registrar actions |
| `cellMembrane/crates/membrane-shadow/` | Rust control plane |
