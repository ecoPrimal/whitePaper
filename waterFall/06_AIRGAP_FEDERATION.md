# Airgap Federation

**Sneakernet, depot, and USB patterns**

**Date**: May 29, 2026
**Status**: Whitepaper — Conceptual Design

---

## Transport Agnosticism

waterFall's temporal model doesn't care how commits arrived at a
remote. A USB drive with a bare repo is indistinguishable from a
cloud git server — both have a HEAD, both participate in the temporal
position matrix, both can be leaders or followers.

```
Transport          URL scheme          Network required?
─────────          ──────────          ─────────────────
SSH (Forgejo)      ssh://              Yes (TCP)
HTTPS (GitHub)     https://            Yes (TCP)
Git protocol       git://              Yes (TCP)
Local filesystem   file://             No
NFS mount          file://             LAN only
USB drive          file:///media/usb/  Physical only
```

All six transports participate identically in temporal sync. The fetch,
measure, pull, push cycle works the same for all.

---

## The Sneakernet Pattern

When no network connects two gates, a USB drive or portable SSD acts
as a physical membrane:

```
Gate A (airgapped)        USB Drive         Gate B (connected)
   │                         │                    │
   │  1. git push usb        │                    │
   │────────────────────────→│                    │
   │                         │                    │
   │         (physical       │                    │
   │          transport)     │                    │
   │                         │                    │
   │                         │  2. git pull usb   │
   │                         │←───────────────────│
   │                         │                    │
   │                         │  3. git push       │
   │                         │    forgejo         │
   │                         │───────────────────→│
   │                         │                    │
```

Gate A pushes to USB. USB is physically carried to Gate B. Gate B
pulls from USB and pushes to Forgejo. Next time Gate A gets the USB
back, it pulls from USB (now containing Gate B's changes).

### USB Depot Setup

```bash
# On USB drive: create bare repos for each primal
for repo in primals/bearDog primals/songBird ...; do
    git init --bare "/media/usb/ecoPrimals/$repo.git"
done

# On gate: add USB remote
for repo in primals/bearDog primals/songBird ...; do
    cd "$ECOPRIMALS_ROOT/$repo"
    git remote add usb "file:///media/usb/ecoPrimals/$repo.git"
done

# Sync: same cascade-pull with temporal awareness
cascade-pull.sh --source temporal
# USB participates as any other remote
```

### USB in Temporal Position Matrix

```
primals/songBird:
  Remote      HEAD      Ahead  Behind  Pattern
  ──────      ────      ─────  ──────  ───────
  origin      a58a676c  4      0       LEADER
  forgejo     a6ef1ec8  0      0       PARITY
  usb         d4e5f6a7  0      2       FOLLOWER

  Action: pull origin → push forgejo, push usb
```

The USB remote is just another remote. waterFall pushes to it after
pulling from the leader. Next time it's carried to another gate, it
carries the latest state.

---

## Depot Patterns

A depot is a persistent sync point — a remote that multiple gates
push to and pull from. Different depot types serve different needs:

### VPS Depot (Forgejo)

The primary inner membrane. Always reachable over SSH. Serves all
gates that can reach the internet.

```
Strengths:           Weaknesses:
─ Global reach       ─ Requires internet
─ Fast (SSD)         ─ Single VPS (SPOF)
─ SSH authenticated  ─ Bandwidth-limited for large repos
─ 24/7 available     ─ Monthly cost
```

### LAN NAS Depot

A NAS (Network Attached Storage) on the local network. High bandwidth,
low latency, but only reachable on the LAN.

```
Strengths:           Weaknesses:
─ Very fast (LAN)    ─ LAN only
─ Large storage      ─ Requires NAS hardware
─ No internet needed ─ Power-dependent
─ No monthly cost    ─ No WAN access
```

Future: westGate concept — a dedicated cold storage gate acting as
a NAS depot for braids and large datasets.

### Project VPS Depot

A dedicated VPS for a subproject. Useful when a collaborator works
on a specific project and needs their own sync point.

```
[sync.remotes.helixvision-depot]
url_template = "ssh://helix-vps.example.com:2222/repos/{repo}.git"
role = "depot"
repos = ["gardens/helixVision"]
```

Only repos in the `repos` list sync to this depot. Other repos are
unaffected. The project VPS is an ecosystem remote like any other.

### USB Depot (Sneakernet)

The physical membrane. No network required. Useful for:
- Airgapped gates (security-critical systems)
- Remote field work (no internet)
- Initial gate setup (bootstrap from USB before network configured)
- Cold storage (archive snapshots to USB)

---

## Gate Classes and Sync Topology

Different gate types have different sync topologies:

### Tower Gate (LAN, always-on)

eastGate, ironGate, southGate — desktop workstations on the LAN.

```
Remotes: origin (GitHub), forgejo (VPS), lan-depot (NAS, future)
Cadence: 15 min (systemd timer)
Topology: hub-and-spoke via VPS
```

### Mobile Gate (roaming)

sporeGate, swiftGate — laptops that move between LAN and WAN.

```
Remotes: origin (GitHub), forgejo (VPS)
Cadence: on-connect (when joining a network)
Topology: star via whichever remote is reachable
```

When a mobile gate is on the LAN, it can reach both Forgejo (direct
SSH) and GitHub (via internet). When roaming, it may only reach
GitHub. waterFall handles both transparently — measure what's
reachable, pull the leader, push to followers.

### WAN Gate (remote)

flockGate, kinGate — towers at other locations.

```
Remotes: origin (GitHub), forgejo (VPS via internet)
Cadence: 15 min or on-demand
Topology: star via VPS (primary), GitHub (fallback)
```

WAN gates rely on the VPS as their primary membrane. If the VPS is
unreachable, they fall back to GitHub. Temporal sync handles both
cases without reconfiguration.

### Airgapped Gate (no network)

Future: security-critical or field deployments.

```
Remotes: usb (physical)
Cadence: on-insert (when USB is plugged in)
Topology: point-to-point via USB
```

Airgapped gates only sync via physical media. waterFall's temporal
model works identically — the USB remote participates in the temporal
position matrix.

---

## MitoBeacon Integration

In the airgap scenario, how does a gate verify that the USB contents
are legitimate? The MitoBeacon genetic security model provides:

1. **Beacon seed** — shared key material embedded in the gate's
   `.beacon.seed` file, established during gate provisioning
2. **Signed commits** — bearDog signs all commits; waterFall verifies
   signatures before accepting pulls
3. **Gate identity** — the `.gate` file identifies the gate; the
   beacon confirms it's a legitimate ecosystem member

```
USB arrives at gate:
  1. waterFall fetches from usb remote
  2. For each new commit: bearDog.crypto.verify_ed25519(commit)
  3. If all signatures valid: fast-forward
  4. If any invalid: REJECT, report tampered media
```

This makes sneakernet as secure as SSH — the trust is in the
cryptographic signatures, not the transport.

---

## Bootstrap from USB

A fresh gate can be bootstrapped entirely from USB:

```bash
# 1. Plug in USB with bare repos
# 2. Clone ecosystem from USB
for repo in $(ls /media/usb/ecoPrimals/); do
    git clone "file:///media/usb/ecoPrimals/$repo" \
        "$ECOPRIMALS_ROOT/${repo%.git}"
done

# 3. Add canonical remotes from manifest
cascade-pull.sh --setup-remotes

# 4. First temporal sync (when network available)
cascade-pull.sh --source temporal

# Gate is now part of the ecosystem
```

This is the "zero to NUCLEUS in 5 minutes" goal from the airSpring
AAR, extended to work without any network at all.

---

## Next Reading

- **[07_ROADMAP.md](./07_ROADMAP.md)** — Full implementation roadmap
- **[02_ARCHITECTURE.md](./02_ARCHITECTURE.md)** — Sync levels and remote topology
- **[04_TEMPORAL_MODEL.md](./04_TEMPORAL_MODEL.md)** — Convergence dynamics

---

*"A USB drive is just a very slow, very reliable network link.
waterFall doesn't care about speed. It cares about temporal position."*
