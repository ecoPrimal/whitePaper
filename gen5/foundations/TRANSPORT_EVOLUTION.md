# Transport Evolution — Nanowire to Quorum Sensing

**Gen5 Foundation** (new concept, no gen4 precedent)

---

## Transport Metaphors

The ecosystem's inter-node communication follows a biological evolution
from direct physical connections to diffusion-based autonomous sensing:

| Phase | Metaphor | Implementation | Status |
|-------|----------|----------------|--------|
| **Nanowire** | Direct physical bacterial pili | SSH-triggered relay, manual coordination | **CURRENT** |
| **Quorum Phase 1** | Autoinducer concentration sensing | Timer-based `potential.sense` on VPS nodes | **NEXT** |
| **Quorum Phase 2** | Multi-species quorum (AI-2) | Songbird `mesh.publish` carries impulses | **FUTURE** |
| **Quorum Phase 3** | Capability-routed quorum | Topology-discoverable coordination | **FUTURE** |

---

## Nanowire (Current)

Nanowire transport models bacterial nanowires — direct physical
connections between cells for electron transfer. In the ecosystem:

- Gates connect to Forgejo via SSH (port 2222)
- `pepti-sync-relay.sh` uses SSH to chain relay
- `ext-github-push.sh` uses SSH to push extracellularly
- `cascade-pull.sh` executes SSH-based git operations

**Characteristics**: Point-to-point, synchronous, requires direct
connectivity, manually triggered.

**Appropriate for**: Covalent bonds (LAN gates), metallic bonds
(inner→peptidoglycan), and early-stage ionic bonds.

---

## Quorum Phase 1 — Timer-Based Sensing

Replace SSH-triggered relay with autonomous sensing loops:

```
┌─────────────────┐       ┌─────────────────┐
│  peptidoglycan  │       │  golgiBody-ext   │
│                 │       │                  │
│  every 60s:     │       │  every 60s:      │
│  potential.sense│──────▶│  potential.sense  │
│  → pull forgejo │       │  → pull pepti    │
│  → relay if new │       │  → push github   │
└─────────────────┘       └─────────────────┘
```

Nodes run `potential.sense` on timers (systemd timers or cron).
Each node independently checks its upstream for changes and
acts without being told. The "relay" becomes emergent from
independent sensing rather than orchestrated from a trigger.

**Key shift**: From "fire and wait" to "sense and respond."

---

## Quorum Phase 2 — Songbird Mesh Relay

Songbird's existing TCP federation carries impulse notifications:

- Gates publish impulses via `mesh.publish` (multicast)
- VPS nodes subscribe to K-Derm-relevant channels
- Relay becomes multicast event-driven, not point-to-point SSH
- Impulse propagation time drops from ~3s to sub-second

---

## Quorum Phase 3 — Capability-Routed Quorum

Full topology-discoverable coordination:

- Nodes register K-Derm layer roles via Songbird capabilities
- Coordination routing discovered at runtime, not hardcoded
- New VPS nodes self-integrate by announcing their layer role
- Multi-vendor peptidoglycan nodes form quorum for relay consensus

---

## Nanowire Retained Uses

Even at quorum maturity, nanowire SSH remains for:

- Initial gate bootstrap (clone from Forgejo)
- Metallic-bond operations (direct VPS management via `membrane` CLI)
- Emergency manual sync (bypass quorum for incident response)
- Air-gapped gate reconnection (biomeGate pattern)

The evolution adds capability, it doesn't replace all direct connections.

---

## Key Files

| File | Purpose |
|------|---------|
| `wateringHole/WATERFALL_PATTERN.md` | WaterFall sync architecture |
| `wateringHole/GATE_SETUP_STANDARD.md` | Gate bootstrap procedures |
| `wateringHole/hooks/forgejo/` | Current nanowire relay chain |
| `cellMembrane/crates/membrane-shadow/src/temporal.rs` | Rust temporal cascade |
