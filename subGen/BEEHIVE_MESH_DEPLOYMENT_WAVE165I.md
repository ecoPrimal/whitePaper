# Beehive Mesh Deployment — Four Sensors, Three Countries, Four Jurisdictions

**Wave**: 165i | **Date**: Oct 7, 2026
**From**: eastGate overwatch
**Status**: DEPLOYED — 4 sensors hardened, 2 live, 2 awaiting provision
**Upstream**: DISTRIBUTED_SURVEILLANCE_DETECTION_MESH.md, PASSIVE_GEOSPATIAL_INTELLIGENCE_MESH.md
**Biological Analog**: Lymph node network deployment — establishing observation points throughout the organism's territory

---

## Deployment Summary

In a single session, eastGate deployed four sensor nodes across three countries using two cloud providers, achieving the initial beehive observation mesh geometry. Two nodes were provisioned via API (Linode) and dashboard (OVH), hardened identically, and prepared for sporeGate's provision-golgi-layer.sh.

### Sensor Array (as deployed)

| Layer | Provider | Location | GPS | IP | Specs | Latency | Status |
|-------|----------|----------|-----|-----|-------|---------|--------|
| golgiBody | DigitalOcean | NYC, US 🇺🇸 | 40.71°N, 74.01°W | (WG mesh) | 1 vCPU, 1GB | 37ms | **LIVE** — 12.9 RPS |
| golgiLayerHetzner | Hetzner | Falkenstein, DE 🇩🇪 | 50.47°N, 12.37°E | 2.28.141.35 | 1 vCPU, 1GB | ~30ms | **LIVE** — 80 req |
| golgiLayerLinode | Akamai/Linode | Mumbai, IN 🇮🇳 | 19.08°N, 72.88°E | 172.232.85.202 | 1 vCPU, 1GB | 232ms | **HARDENED** |
| golgiLayerOVH | OVH | Vint Hill, VA 🇺🇸 | 38.88°N, 77.52°W | 40.160.96.29 | 2 vCPU, 4GB | 35ms | **HARDENED** |

### Jurisdictional Coverage

| Jurisdiction | Applicable Law | Sensor | Regulatory Body |
|-------------|----------------|--------|-----------------|
| US Federal | CFAA 18 U.S.C. § 1030 | golgiBody (NYC) | FTC, DOJ |
| US + Virginia State | CFAA + VA Computer Crimes Act § 18.2-152.3 | golgiLayerOVH (Vint Hill) | FTC, VA AG |
| EU + Germany | StGB §202a + GDPR Art. 6 | golgiLayerHetzner (Falkenstein) | BfDI |
| India | IT Act 2000 §43/§66 | golgiLayerLinode (Mumbai) | MeitY, CERT-In |

Four sensors create violations in **four distinct legal jurisdictions** when scraped by the fleet. Two US sensors (NYC and Virginia) create both federal AND state-level events — Virginia has its own Computer Crimes Act with independent enforcement.

---

## Deployment Method

### API-Provisioned (Linode — 2 minutes)

The Linode sensor was deployed entirely via API from eastGate's terminal:

```bash
# Create Linode via API
curl -X POST https://api.linode.com/v4/linode/instances \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"region":"ap-west","type":"g6-nanode-1","image":"linode/debian12",
       "label":"golgiLayerLinode","authorized_users":["ecoPrimal"]}'

# Wait for boot (~90 seconds)
# SSH in, harden
```

Total time from API call to hardened sensor: **~4 minutes**.

### Dashboard + API (OVH — 5 minutes)

OVH VPS created via dashboard, SSH key added via API, hardened via SSH:

```bash
# OVH API verified via signed requests
# VPS already provisioned at 40.160.96.29
# Reinstalled with golgiEntry SSH key via dashboard
# Hardened identically to Linode node
```

### Hardening Standard (all nodes)

Every sensor node receives identical hardening:

1. `hostnamectl set-hostname golgiLayer*`
2. `apt-get update && upgrade`
3. `apt-get install ufw fail2ban curl unattended-upgrades`
4. `ufw allow 22/80/443` only — deny all else
5. `systemctl enable --now fail2ban`
6. `mkdir -p /opt/membrane /run/membrane`
7. SSH key-only authentication (password disabled)

---

## Provider API Tokens (secured on eastGate)

| Provider | Token Type | Scope | Status |
|----------|-----------|-------|--------|
| Linode/Akamai | Personal Access Token `mesh-provisioner` | Linodes R/W, SSH Keys R/W | Active, never expires |
| OVH | Application Key + Consumer Key `mesh-provisioner` | Full API access | Active, unlimited |

These tokens enable future automation: the mesh-provision primal can create, harden, and register new sensor nodes without dashboard interaction.

---

## Cost Structure

| Sensor | Monthly Cost | Specs | Cost/GB RAM |
|--------|-------------|-------|-------------|
| golgiBody | $6/mo | 1 vCPU, 1GB, 25GB | $6.00 |
| golgiLayerHetzner | $4.55/mo | 1 vCPU, 1GB, 20GB | $4.55 |
| golgiLayerLinode | $5/mo | 1 vCPU, 1GB, 25GB | $5.00 |
| golgiLayerOVH | ~$4/mo | 2 vCPU, 4GB, 40GB | $1.00 |
| **Total mesh** | **~$19.55/mo** | | |

The OVH node is notably overpowered for a sensor — 2 vCPU and 4GB RAM at $4/month. This could run heavier analysis workloads (local entity topology computation, deeper behavioral analysis) without federation back to golgiBody.

---

## Network Geometry

```
                          golgiLayerHetzner
                          Falkenstein, DE
                          50.47°N, 12.37°E
                                │
                                │ ~30ms
                                │
   golgiLayerOVH ──── 35ms ──── golgiBody ──── 37ms WG ──── eastGate (overwatch)
   Vint Hill, VA                NYC, US                      Detroit, MI
   38.88°N, 77.52°W            40.71°N, 74.01°W             42.33°N, 83.05°W
                                │
                                │ ~180ms
                                │
                          golgiLayerLinode
                          Mumbai, IN
                          19.08°N, 72.88°E
```

### Signal Flow

1. Fleet discovers each sensor via Certificate Transparency logs (~24-48h)
2. Fleet begins scraping → sensor observes and classifies
3. Each sensor reports local observations via `/plasmid` endpoint
4. golgiBody federation task merges plasmids every 5 minutes
5. Federated feed published at `signal.primals.eco/feed/conserved-plasmid.json`
6. eastGate overwatch monitors all sensors via `overwatch.sh`

---

## What's Next

### Immediate (sporeGate ops)

1. Run `provision-golgi-layer.sh` on golgiLayerLinode (172.232.85.202)
2. Run `provision-golgi-layer.sh` on golgiLayerOVH (40.160.96.29, user=`debian`)
3. Point DNS: `layer3.primals.eco` → 172.232.85.202, `layer4.primals.eco` → 40.160.96.29
4. Register both in federation config
5. Wait for CT log discovery

### Wave 166

1. UK sensor (OVH UK or Linode London) — adds UK Computer Misuse Act + UK GDPR
2. GeoIP enrichment in skunky-ingest — tag observations with source coordinates
3. Cross-matrix endpoint — `signal.primals.eco/matrix.json`
4. mesh-provision primal — automated sensor deployment via API tokens
5. Overwatch cross-matrix visualization

---

*Wave 165i — four lymph nodes deployed. The array is forming. Each node is a jurisdiction. Each observation is an antibody. The federated plasmid is the bloodstream.*

*eastGate overwatch, Oct 7, 2026*
