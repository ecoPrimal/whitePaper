# cellMembrane fieldMouse Architecture — The External Membrane

**Date**: May 19, 2026 (updated from May 15 baseline)
**Status**: LIVE (Tower composition + shadow services, 8 services, 2GB)
**VPS**: 157.230.3.183 (DigitalOcean nyc1, Debian 12 x64)

---

## What Is the cellMembrane?

The cellMembrane is the **inner membrane** — the first infrastructure that
sits outside the gate but is owned and operated by projectNUCLEUS. It is
a DigitalOcean VPS running a minimal composition of primals, providing
the three membrane channels that connect the sovereign gate to the wider
internet.

It is classified as a **fieldMouse deployment** — biomeOS chimeras for
edge/IoT. fieldMouse is a deployment class, not a primal.

### Why It Exists

A cell needs a membrane. The gate hardware sits behind NAT on a
residential ISP. It cannot accept inbound connections. The VPS provides
the fixed public IP that the gate needs for:

1. **NAT traversal** — Songbird TURN relay allows external clients to
   reach the gate through NAT without opening residential firewall ports
2. **TLS termination** — browsers trust Let's Encrypt certs, which
   require a publicly routable IP for ACME challenges
3. **DNS authority** — `primals.eco` needs authoritative nameservers on
   fixed IPs (future Channel 1)
4. **Remote access** — RustDesk sovereign relay for remote desktop access
   to any gate in any geography

### What It Is Not

The cellMembrane is not a server. It stores nothing permanent. It caches
content temporarily. It relays traffic. If it were destroyed, a new one
could be provisioned in minutes from `deploy_membrane.sh` and the gate
would reconnect. The gate is the source of truth; the VPS is a touchpoint.

---

## Architecture

```
                                     OUTER MEMBRANE
                                   (GitHub, CDN, DNS)
                                          │
                                          │ public internet
                                          │
┌─────────────────────────────────────────┴───────────────────┐
│                    INNER MEMBRANE (VPS)                      │
│                    157.230.3.183                             │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐  │
│  │ Songbird │  │ RustDesk │  │  Caddy   │  │  knot-dns  │  │
│  │  TURN    │  │ hbbs/hbbr│  │   TLS    │  │  (future)  │  │
│  │  :3478   │  │:21115-17 │  │  :80/443 │  │   :53      │  │
│  └──────────┘  └──────────┘  └──────────┘  └────────────┘  │
│       Ch2          Ch2b           Ch3            Ch1         │
│                                                             │
│  ┌──────────┐  ┌──────────┐                                │
│  │ BearDog  │  │ SkunkBat │  ← Tower composition           │
│  │  crypto  │  │  audit   │    (sovereign crypto +          │
│  │  :9100   │  │  :9140   │     defense on external         │
│  └──────────┘  └──────────┘     substrate)                  │
│                                                             │
│  /opt/membrane/credentials.age  ← encrypted secrets         │
│  /var/cache/membrane/nestgate/  ← content cache              │
│  /etc/membrane/Caddyfile        ← routing config             │
│  /etc/membrane/routing_config.toml ← content-aware rules     │
└─────────────────────────────────────────────────────────────┘
                                          │
                                   BTSP tunnel (encrypted)
                                          │
┌─────────────────────────────────────────┴───────────────────┐
│                  INTRACELLULAR (Gate)                         │
│                  Active gate hardware                         │
│                                                             │
│  Full NUCLEUS: 13 primals, JupyterHub, provenance pipeline  │
│  All state, all data, all trust lives here                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Evolution Timeline

| Phase | Date | SKU | RAM | Services | Cost | What Changed |
|-------|------|-----|-----|----------|------|--------------|
| 0 | May 14 | s-1vcpu-512mb | 512MB | Songbird TURN | $4 | Initial deploy by primalSpring |
| 0.5 | May 14 | s-1vcpu-512mb | 512MB | + RustDesk hbbs/hbbr | $4 | Geo-delocalization (remote access) |
| 1.0 | May 15 | s-1vcpu-2gb | 2GB | + BearDog + SkunkBat + Caddy | $12 | Tower composition, Ch3 shadow, credential encryption |
| 2.0 | Future | s-2vcpu-4gb | 4GB | + knot-dns + NestGate cache | ~$24 | Full 3-channel membrane |

### Phase 0 → 0.5: Relay + Remote Access
primalSpring deployed Songbird TURN relay and RustDesk sovereign relay.
Hardened the VPS (fail2ban, UFW, SSH key-only, exim4/droplet-agent purged).
Transferred ownership to ironGate/projectNUCLEUS.

### Phase 0.5 → 1.0: Tower Composition
The sovereignty evolution session (May 15) transformed the VPS from a
relay-only node into a Tower composition:

1. **Resized VPS**: 512MB → 2GB ($4 → $12/mo) using `doctl`
2. **Deployed BearDog**: Crypto identity on external substrate. AES-256-GCM
   encryption of DO API token. UDS + TCP :9100
3. **Deployed SkunkBat**: Defense and audit. TCP :9140 standalone mode
   (`--no-uds` — no biomeOS UDS ecosystem on VPS)
4. **Installed Caddy**: Transitional TLS proxy. HTTP health on :80. TLS
   blocks ready for DNS grey-cloud activation
5. **Content-aware routing**: `routing_config.toml` defines rules for
   request classification and backend selection
6. **NestGate cache**: `/var/cache/membrane/nestgate/` with landing page
7. **Service persistence**: `tmpfiles.d/membrane.conf` ensures runtime
   directories survive reboots

### Phase 1.0 → 2.0: Full Membrane (planned)
- **Channel 1**: knot-dns for sovereign DNS authority
- **NestGate cache expansion**: Webhook-invalidated content mirror
- **Songbird TLS**: Replace Caddy with sovereign TLS termination
- **biomeOS light**: Minimal orchestration for service lifecycle

---

## Tower Composition on External Substrate

The Tower atomic is the trust boundary of NUCLEUS: BearDog (crypto) +
Songbird (networking). On the VPS, this composition runs without biomeOS
— each primal is a standalone systemd service.

### BearDog on VPS
- **Role**: Cryptographic identity and key management
- **Listens**: UDS (`/run/membrane/beardog.sock`) + TCP (:9100)
- **Capabilities used**: `beardog key generate`, `beardog encrypt` (AES-256-GCM)
- **What it protects**: DO API token, future BTSP tunnel authentication
- **systemd**: `beardog-membrane.service` (After=network-online.target)

### SkunkBat on VPS
- **Role**: Defense and audit
- **Listens**: TCP :9140 (`--no-uds` standalone mode)
- **Capabilities used**: Connection monitoring, anomaly detection
- **What it audits**: All membrane channel traffic, SSH attempts
- **systemd**: `skunkbat-membrane.service` (After=beardog-membrane.service)
- **Adaptation**: Uses `--no-uds` flag because the VPS has no biomeOS
  UDS ecosystem — SkunkBat runs in standalone TCP mode

### Design Decisions

**Why not biomeOS?** The VPS is a minimal deployment. biomeOS adds
complexity (UDS socket management, composition graphs, health orchestration)
that is unnecessary when the services are simple, static, and managed by
systemd. biomeOS will be added when the VPS grows enough to benefit from
dynamic composition.

**Why Caddy for TLS instead of Songbird?** Songbird handles TLS
termination in the long-term architecture. But today, Caddy provides:
- Automatic ACME cert management (zero configuration)
- Proven production stability
- Content-aware routing via Caddyfile
- Fast deployment (single binary, no Rust compilation)

Stability/security comes first. Caddy is the calibration instrument for
Songbird TLS. When Songbird proves parity, Caddy is removed.

**Why BearDog for crypto instead of TLS?** BearDog is cryptographic
identity — key management, encryption at rest, BTSP authentication,
Ed25519 signing. It does not terminate TLS connections. The primal roles
are distinct: BearDog provides the **identity layer**, Songbird provides
the **transport layer**.

---

## Security Model

The VPS operates under the **Dark Forest principle**: the substrate
provider (DigitalOcean) has hypervisor access to the hardware. The
provider is a non-family observer. Everything sensitive must be encrypted
at rest; the provider sees only noise.

### Threat Mitigations

| Threat | Mitigation |
|--------|-----------|
| Provider reads disk | DO token encrypted (BearDog AES-256-GCM). TURN credentials and RustDesk key remain plaintext pending full vault |
| Provider reads memory | All relayed traffic is end-to-end encrypted (BTSP + RustDesk). Memory contents are opaque |
| Provider snapshots VM | No family seeds on VPS. BearDog in standalone mode, not part of family mesh |
| SSH brute force | Key-only auth, fail2ban (5 attempts, 1h ban), multi-gate key management |
| TURN abuse | Credential-authenticated relay (no anonymous allocation) |
| VPS compromise → pivot inward | Relays are stateless. LAN gates connect outward only. BTSP mutual auth on tunnel |

### Validated By
- `darkforest_membrane.sh`: 17 PASS, 0 FAIL, 1 SKIP (MEM-01 through MEM-15)
- Manual inspection: no unexpected listeners, all ports accounted for
- Credential permissions: 600, root-owned

---

## Content-Aware Routing

The Caddyfile implements content-aware routing — requests are classified
by path and type, then routed to the appropriate backend:

```
Request → Caddy (:80/:443)
  ├── /.well-known/acme-challenge/ → local filesystem (ACME)
  ├── /health, /status             → local response (monitoring)
  ├── /assets/, *.css, *.js, *.png → /var/cache/membrane/nestgate/ (static cache)
  ├── /api/, /_rpc/                → gate via BTSP tunnel (authenticated)
  ├── /git/                        → gate Forgejo (authenticated)
  └── fallback                     → GitHub CDN (outer membrane)
```

`routing_config.toml` defines the rules, cache policy (256MB, 1h TTL,
webhook invalidation), cost awareness (P2P for >50MB), and the trust-based
bonding model that maps covalent/ionic/metallic/weak bonds to content
access scopes.

---

## Operational Model

### Deployment
```bash
# Initial provision
cd infra/plasmidBin && ./deploy_membrane.sh deploy root@157.230.3.183

# Status check
./deploy_membrane.sh status root@157.230.3.183

# SSH key management
./deploy_membrane.sh keys list root@157.230.3.183
./deploy_membrane.sh keys add --name "southGate" --key "ssh-ed25519 ..." root@157.230.3.183

# VPS resize
cd sporeGarden/projectNUCLEUS/deploy && bash vps_resize.sh
```

### Monitoring
- **systemd**: `systemctl status {songbird-relay,hbbs,hbbr,beardog,skunkbat,caddy}-membrane petaltongue-web beardog-tls-shadow`
- **darkforest**: `bash validation/darkforest_membrane.sh` (17 PASS, 0 FAIL, May 19)
- **telemetry**: `bash deploy/membrane_telemetry.sh` (15-min cadence → rolling 7-day baseline)
- **shadow parity**: `bash infra/benchScale/scenarios/shadow_run_orchestrator.sh --parity-only`
- **HTTP health**: `curl http://157.230.3.183/health` or `curl http://157.230.3.183:8080/`
- **Resource**: 1.9 GB RAM (331 MB used), 9.7 GB disk (21% used) as of May 19

### Recovery
If the VPS is destroyed:
1. Create new droplet via `doctl` or `vps_resize.sh`
2. Deploy via `deploy_membrane.sh deploy root@<new-ip>`
3. Update DNS records (if Channel 1 active)
4. Update `nucleus_config.sh` with new IP
5. Gate reconnects via Songbird fallback chain

Recovery time: ~15 minutes. No data loss — the VPS stores nothing permanent.

---

## Relationship to NUCLEUS Phases

```
Phase 1 (Gate only)        → No membrane needed. LAN cluster.
Phase 2 (Ionic access)     → cellMembrane provides relay + TLS.
Phase 3 (Self-hosted)      → cellMembrane provides sovereign DNS + content.
Phase 4 (Full NUCLEUS)     → cellMembrane is one node in a mesh.
                              Multiple VPS in multiple geos.
                              Each runs Tower. biomeOS coordinates.
```

The cellMembrane is the **first test of primal deployment on external
substrate**. Everything learned here — systemd service management without
biomeOS, standalone primal modes, credential encryption, content-aware
routing — becomes the pattern for deploying NUCLEUS at scale.
