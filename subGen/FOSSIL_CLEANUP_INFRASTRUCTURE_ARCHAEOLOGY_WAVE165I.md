# Infrastructure Archaeology: Fossil Cleanup and Self-Diagnosis

**Wave**: 165i
**Date**: Oct 7, 2026
**Status**: Complete — golgiBody restored to healthy baseline

---

## Discovery

While investigating a load crisis on golgiBody (load average 32 on 1 vCPU), three distinct sources of infrastructure burden were discovered — none of which was fleet traffic.

### Source 1: Cascade Thundering Herd

sporeGate's `temporal.cascade` timer fires every 15 minutes, pushing to 15 repos simultaneously via Forgejo SSH. Each push spawns a `forgejo serv key-10` process. On a single-vCPU box, 15 concurrent git-receive operations cause IO contention:

```
15 processes × 3.2% CPU each = 48.5% total CPU
9 in Dl state (uninterruptible disk IO)
6 in Sl state (sleeping on dead pipes)
All running 10+ minutes with no network sockets
SSH connections closed but Forgejo workers orphaned
```

Each time the timer fired, 15 new stuck processes joined the existing stuck processes. Three rounds of killing were needed before the timer was disabled.

**Resolution**: `systemctl stop cascade-sense.timer && systemctl disable cascade-sense.timer`. All stuck servs killed. Load dropped 32 → 0.59.

### Source 2: Fossil Services (233 of 238 TCP connections)

```
Port 7700  songbird federation     160 conn (67.2%)  — 72 days old
Port 21119 hbbr RustDesk relay      67 conn (28.2%)  — 71 days old  
Port 8091  hbbs RustDesk signal      6 conn ( 2.5%)  — restarted today
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FOSSIL TOTAL                       233 conn (97.9%)
ACTIVE MISSION (Caddy + SSH)         5 conn ( 2.1%)
```

These services were deployed during the cellMembrane era (late July 2026) — before the scatter defense, genetic lock, honeycomb maze, or bloom monitor existed. They had been running continuously for 71-72 days:

- **songbird** (federation server + TURN relay): 160 persistent connections from the house network. The songbird federation was designed for inter-gate communication but these connections were maintenance noise — the house mesh holding channels open to a service that no current workflow uses.

- **hbbr/hbbs** (RustDesk relay + signaling): 67 external IPs routing remote desktop traffic through golgiBody as a free relay. These were strangers using our infrastructure as a transit node.

**Resolution**: All processes killed, systemd units disabled. Connection table collapsed from 238 → 7.

### Source 3: Stale WireGuard Peers

13 peers configured, only 5 with recent handshakes. The 8 stale peers included:

| Peer | IP | Staleness | Reason |
|------|-----|-----------|--------|
| flockGate | 10.13.37.6 | 70 days | Locked out during sovereign RustDesk migration |
| biomeGate | 10.13.37.3 | 54 days | Unknown |
| unknown-h1 | 10.13.37.7 | 52 days | Behind house NAT |
| unknown-h2 | 10.13.37.10 | 46 days | Behind house NAT |
| unknown-h3 | 10.13.37.12 | 52 days | Behind house NAT |
| graftGate | 10.13.37.13 | 52 days | Was USB tethering cellular |
| reserved-1 | 10.13.37.9 | Never | Provisioned, never used |
| reserved-2 | 10.13.37.11 | Never | Provisioned, never used |

flockGate is alive (ICMP responds from `24.128.136.74`, Comcast Rochester Hills MI) but behind NAT with no port forwards and WireGuard down. Requires physical visit to remesh.

**Resolution**: All 8 peers commented out in `wg0.conf` with `WALLED OFF Wave 165i` marker. WG reloaded via `wg syncconf`. Keepalive packets to dead peers stopped.

---

## Process Stratigraphy

The complete geological record of golgiBody's evolution, preserved in the process table:

```
Layer 0  May 15  145d  systemd              Genesis
Layer 1  May 31  129d  knotd                DNS sovereignty
Layer 2  Jun 17  112d  WireGuard            Mesh networking
Layer 3  Jul  8   91d  nestgate             Gateway establishment
Layer 4  Jul 11   88d  fail2ban             First immune layer
Layer 5  Jul 27   72d  beardog              Key management
Layer 5  Jul 27   72d  songbird ×2          Federation (FOSSIL — killed)
Layer 6  Jul 28   71d  hbbr                 RustDesk relay (FOSSIL — killed)
Layer 7  Jul 29   70d  step-ca              Internal PKI
Layer 7  Jul 29   70d  sshd                 Main SSH daemon
Layer 8  Aug  1   67d  dnsmasq              Mesh DNS resolver
Layer 9  Aug 10   58d  squirrel             Secret management
Layer 10 Aug 12   55d  petaltongue          Primal tool
Layer 11 Oct  6    1d  skunkbat             Behavioral hashing
Layer 12 Oct  7    0d  caddy                Web + scatter + honeycomb
Layer 12 Oct  7    0d  forgejo              Git hosting
Layer 12 Oct  7    0d  skunky-ingest        Fleet detection
Layer 12 Oct  7    0d  bloom_live           Monitoring
Layer 12 Oct  7    0d  swarmvine            Gossip protocol
Layer 12 Oct  7    0d  membrane webhook     CI listener
```

Each layer represents a response to a need that emerged from the previous layer. The fossils (Layers 5-6) predate the entire immune defense stack.

---

## The Fleet Proportion

After cleanup, the fleet's actual system footprint:

| Metric | Fleet | System Total | Fleet % |
|--------|-------|-------------|---------|
| TCP connections | 1 | 7 | 14% |
| CPU (Caddy + skunky + bloom) | 4.8% | ~8% | 60% of active |
| Requests (3.7h) | 162,845 | 162,845 | ~100% of HTTP |
| Load contribution | negligible | negligible | — |

The fleet dominates the **log stream** (100% of HTTP traffic) but is negligible on the **system**. The scatter defense is so efficient that handling 12 req/sec of hostile traffic costs less than the Forgejo web interface idling. The real infrastructure burden was us — our own cascade, our own fossils, our own ghost connections.

---

## Full Observation: Remaining Signals

### Active but needing attention:
1. **Caddy bridge error** (every 30s): skunky-ingest needs `~~FLEET_PRESSURE_START~~` / `~~FLEET_PRESSURE_END~~` markers in Caddyfile
2. **WordPress scanner** on nestgate.io: `185.104.44.182` probing `wp-json/gravitysmtp` — needs fail2ban rule
3. **New subdomain probe**: `ca.primals.eco` hit by `85.217.149.8`
4. **5 enabled-but-inactive services**: beardog-tls-shadow, biomeos-nucleus, membrane-socket-bridge, petaltongue-sporeprint, petaltongue-web

### Healthy and intentional:
- sporeGate SSH session tailing bloom feed (PID 2947383, 17:22 today)
- membrane webhook outbound to sporeGate CI (10.13.37.2:8190)
- refresh-signal-data.sh cron every 15 min (functional but could be optimized)

---

## Before & After

| Metric | Before | After |
|--------|--------|-------|
| Load average | 32.07 | ~2 (nominal) |
| TCP connections | 238 | 7 |
| Memory used | 856 MB | 656 MB |
| WG peers | 13 (8 dead) | 5 (all live) |
| Fossil processes | 4 | 0 |
| Stuck Forgejo servs | 15 (recurring) | 0 (timer disabled) |
| RustDesk relay users | 66 strangers | 0 |

---

*The organism diagnosed itself. The inflammation was self-inflicted — our cascade, our fossils, our ghost connections. The fleet was a rounding error. The stratigraphy is 145 days deep and every layer tells a story.*

*Wave 165i — Oct 7, 2026*
