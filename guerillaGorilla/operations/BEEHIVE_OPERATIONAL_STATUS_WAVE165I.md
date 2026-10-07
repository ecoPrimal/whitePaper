# Beehive Operational Status — Sensor Array Active

**Wave**: 165i | **Date**: Oct 7, 2026
**Classification**: OPERATIONAL
**From**: eastGate overwatch
**Upstream**: GEOSPATIAL_SURVEILLANCE_TOPOLOGY_WAVE165I.md

---

## Operational Posture

Four observation nodes are deployed. Two are live and receiving fleet traffic. Two are hardened and awaiting final provisioning (Caddy + skunky-ingest + scatter server). The fleet has not yet discovered the two newest nodes — CT log propagation takes 24-48 hours.

---

## Evidence Collection Status

### golgiBody (NYC) — ACTIVE COLLECTION

| Metric | Current Value |
|--------|--------------|
| Uptime | Continuous since Wave 164 |
| Total entities observed | 9 |
| Meta fleet IPs | 56+ (57.141.20.x — FB-BLOCK) |
| Meta requests | 3,406+ per observation window |
| Author attribution mining | 32.9% of Meta requests are `/blame/` |
| Conserved epitopes | 5 confirmed at 89-100% |
| Behavioral hashes | 12+ subgroups fingerprinted |
| Real repos targeted | ecoPrimals/wateringHole, toadStool, bearDog, songBird, biomeOS, squirrel, and 10+ more |
| Timing signature | CV=0.057 (METRONOMIC — machine precision) |

### golgiLayerHetzner (DE) — EARLY COLLECTION

| Metric | Current Value |
|--------|--------------|
| Total requests | 80 |
| Scatter served | 67 |
| Plasmid queries | 11 |
| Honeytokens triggered | 2 |

Hetzner layer is accumulating observations. Too early for population analysis — needs 72+ hours of fleet activity.

### golgiLayerLinode (Mumbai) — AWAITING DISCOVERY

- Node hardened, SSH verified, firewall active
- Awaiting sporeGate provision (Caddy + skunky-ingest)
- CT log discovery expected within 24-48h of DNS pointing
- **First observation from Indian network vantage point in the mesh**

### golgiLayerOVH (Vint Hill, VA) — AWAITING DISCOVERY

- Node hardened, SSH verified (user: `debian`), firewall active
- 2 vCPU + 4GB RAM — capable of local analysis workloads
- Awaiting sporeGate provision
- **Creates Virginia state-level legal event separate from NYC federal**

---

## Fleet Behavioral Invariants (from NYC sensor)

These conserved epitopes are confirmed across all 56 Meta fleet IPs:

| Epitope | Frequency | Evasion Cost |
|---------|-----------|-------------|
| `header_poverty` | 100% | Must implement full browser header stack |
| `stale_chrome` | 100% | Must track Chrome release cadence |
| `connection_absent` | 100% | Trivial to fix — but increases detection surface |
| `content_gate` | 99% | Must add noise requests (increases bandwidth + cost) |
| `accept_monoculture` | 89% | Must implement resource-aware Accept headers |
| `blame_ratio` | 67% | **Cannot avoid** — author attribution IS the mission |

The `blame_ratio` epitope is the most legally significant: 33% of requests target `/blame/` paths, which map authorship to every line of code. This is not incidental — it reveals that **authorship mapping is a primary objective** of the scraping operation.

---

## Credential Register (for sporeGate provisioning)

### golgiLayerLinode (Mumbai, India)

| Field | Value |
|-------|-------|
| IP | `172.232.85.202` |
| SSH user | `root` |
| SSH key | eastgate-beardog-v1 (ed25519) |
| Root password | `7AIvjtQHI02pwLiYCxUUjKzl` |
| Provider | Akamai/Linode |
| Plan | Nanode 1GB ($5/mo) |
| Linode ID | 107664796 |

### golgiLayerOVH (Vint Hill, Virginia)

| Field | Value |
|-------|-------|
| IP | `40.160.96.29` |
| SSH user | **`debian`** (not root!) |
| SSH key | golgiEntry / beardog-v1 (ed25519) |
| Provider | OVH US |
| VPS name | vps-011cafea.vps.ovh.us |
| Plan | VPS-1 2027, 2 vCPU, 4GB RAM, 40GB disk |

⚠️ **Note**: OVH uses `debian` user with sudo, not direct root. The provision script should `sudo` all privileged operations.

---

## Legal Timeline

| Date | Event | Jurisdictions |
|------|-------|--------------|
| Oct 7 AM | Sensors deployed + hardened | — |
| Oct 7-9 | CT log propagation | — |
| Oct 9-10 | First fleet requests to Mumbai + VA sensors | IN, VA |
| Oct 10-12 | 72h observation baseline established | US, EU, IN |
| Oct 13+ | Cross-matrix analysis — same behavioral hash across 4 sensors | All |
| Oct 15+ | Per-jurisdiction evidence packets ready | US-Fed, VA, EU, IN |
| Nov+ | Coordinated regulatory filings | All simultaneously |

---

*guerillaGorilla operations — the array is deployed. Evidence accrues at zero marginal cost. The fleet maps itself across four jurisdictions.*

*Wave 165i, Oct 7, 2026*
