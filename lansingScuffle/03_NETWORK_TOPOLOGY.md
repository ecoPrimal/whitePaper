# Network Topology — Building Network and Neighborhood Mesh Supernode

**Date**: Jul 20, 2026
**Status**: Concept — building network projected from house topology
**Lineage**: wateringHole/TOPOLOGY_MAP.toml → COMMUNITY_MESH_PROFILE → INFRA_LAYERS.toml → 00_THE_SCUFFLE
**Wave**: 150

---

## Thesis

The current ecoPrimals network is a two-house star topology with a 10G
AOC trunk between adjacent lots in Old Everett, Lansing. The building
at 1305 S Cedar scales this pattern: same K-Derm membrane model, same
WireGuard overlay, same songBird federation — but with commercial fiber,
10G+ internal backbone, and a rooftop position that turns the building
into the neighborhood mesh supernode described in COMMUNITY_MESH_PROFILE.

---

## Current Topology (House Scale)

From TOPOLOGY_MAP.toml (Wave 133):

```
House 1 (4422 Southgate)        House 2 (641 Samantha)
ATT Fiber → BGW320              ┌─────────────────────┐
    │                           │ Omada SX3008F (10G) │
    ▼                           │   ├── ironGate       │
  sporeGate (NAT/FW/DNS)       │   ├── southGate      │
    │                           │   ├── strandGate     │
    ▼                           │   └── fieldGate      │
  CRS310 (10G backbone)        └──────────┬──────────┘
    ├── eastGate (10G)                    │
    ├── northGate (2.5G)          80m AOC (10G SFP+)
    ├── biomeGate                  ~20m physical
    └────────────────────────────────────┘
```

- **Topology**: Single-exit star (all traffic → sporeGate → ATT fiber)
- **Backbone**: 10G SFP+ (CRS310 ↔ Omada via 80m AOC)
- **Subnet**: Flat 192.168.4.0/22 spanning both houses
- **Overlay**: WireGuard 10.13.37.0/24 (golgiBody hub, 5 peers)
- **Federation**: songBird TCP :7700 (eastGate, golgi, ironGate, southGate, grapheneGate)

---

## Building Network (scuffleGate Topology)

### Phase 1 — Beachhead (1-2K SF, Year 1)

```
Internet ──→ Commercial Fiber (dedicated drop)
                │
                ▼
         scuffleGate (site router)
         NucBox or tower, runs:
           - nftables / NAT / DHCP
           - WireGuard (10.13.37.10)
           - songBird node
           - NUCLEUS (13 primals)
                │
         ┌──────┼──────┐
         │      │      │
     compute  intake  mesh AP
     rack     NUC     (community WiFi)
```

Minimal. One router, one rack, one AP. Joins the existing WireGuard
mesh as `scuffleGate` (10.13.37.10). songBird federation links it to
golgiBody and the house gates.

### Phase 2 — Expansion (12-30K SF, Year 2-3)

```
Internet ──→ Commercial Fiber (1 Gbps+ symmetric)
                │
                ▼
         marshGate (building site router, evolved from INFRA_LAYERS)
         ├── WAN: fiber uplink
         ├── LAN: 10G trunk to zone switches
         ├── WireGuard: 10.13.37.0/24 (mesh hub)
         └── songBird: federation hub for building gates
                │
     ┌──────────┼──────────────────┐
     │          │                  │
  Zone A     Zone B             Zone C
  (compute)  (lab/community)    (humanitarian)
     │          │                  │
  10G switch  1G switch         mesh APs
  GPU racks   workstations      hotspot, WiFi
  NUCs        lab instruments   charging
```

marshGate is the building's sovereignty boundary — the same role sporeGate
plays at house1. Internal backbone is 10G between zones, mirroring the
CRS310↔Omada pattern at larger scale.

### Phase 3 — Full Campus (50K+ SF, Year 4-5)

```
                         ┌── Fiber Drop 1 (primary, 1-10 Gbps)
Internet ──→ marshGate ──┤
                         └── Fiber Drop 2 (redundant, different provider)
                │
         ┌──────┼──────────────────────────┐
         │      │         │                │
      10G     10G       10G             Mesh
      Core    Science   Community       Supernode
         │      │         │                │
    ┌────┼────┐ │    ┌────┼────┐     ┌────┼────┐
    │racks   │ │    │maker  │ │     │sector W│
    │sand    │ │    │cowork │ │     │sector S│
    │storage │ │    │events │ │     │sector E│
    └────────┘ │    └───────┘ │     └────────┘
          ┌────┘             │
       wetLab           humanitarian
       dryLab           (open WiFi,
       coldStore         no credentials)
```

Multiple fiber drops (different providers) for WAN redundancy.
The building's roof becomes the mesh supernode.

---

## Mesh Supernode — Neighborhood Coverage

From COMMUNITY_MESH_PROFILE (Wave 115):

The Old Everett rectangle (Cavanaugh → Jolly, Cedar → Pennsylvania) is
~1.76 km², ~800-1200 households. The original mesh plan placed the
supernode at 4422 Southgate. The John Bean Building is a better position:

| Factor | 4422 Southgate | John Bean Building |
|--------|---------------|-------------------|
| Elevation | Single-story residential | 3-story industrial |
| Roof area | ~1,200 SF residential | ~464,000 SF industrial |
| Antenna mounting | Residential chimney/pole | Industrial roof, any position |
| Power for radios | Residential 200A shared | Heavy power, dedicated circuits |
| Line of sight | Tree canopy obstruction | Above most canopy from 3 stories |
| Coverage radius | ~300-500m usable | ~1-2 km with sector antennas |
| Location | Center of rectangle | Western edge (Cedar St) |

The building's Cedar St position means sector antennas cover:
- **East**: Full Old Everett rectangle to Pennsylvania Ave (~1.1 km)
- **North**: Toward Cavanaugh Rd and I-496 interchange
- **South**: Toward Jolly Rd and South Lansing

From NEIGHBORHOOD_MESH_HARDWARE: any radio in the Ubiquiti/MikroTik
class has perfect signal at Old Everett distances (~300m max). From a
3-story industrial roof, the range extends to 1+ km — covering the
entire target rectangle from a single site.

### Mesh Layer Architecture

```
Layer 1: Backbone
    marshGate ↔ commercial fiber ↔ internet
    Building internal 10G

Layer 2: Distribution
    Sector antennas on roof → neighborhood relay nodes
    Point-to-point links to house1/house2 (backup path)

Layer 3: Access
    Per-household CPE (customer premises equipment)
    Indoor mesh APs in community spaces
    Open WiFi in humanitarian zone (no auth)
```

### Per-Household Economics

From COMMUNITY_MESH_PROFILE:

| Cost Element | Per Household |
|-------------|---------------|
| CPE device (MikroTik SXTsq or similar) | ~$60-80 one-time |
| Monthly shared bandwidth | ~$10-20/month |
| Installation (volunteer labor) | ~$0 (community install days) |

At $15/month average and 100 subscribers:
**$1,500/month mesh revenue** — covering a significant portion of building
lease + fiber costs.

---

## WireGuard Mesh Integration

The building joins the existing WireGuard overlay:

| Gate | WG IP | Role |
|------|-------|------|
| golgiBody (VPS) | 10.13.37.0 | Hub, relay |
| sporeGate (house1) | 10.13.37.1 | House router |
| flockGate (remote) | 10.13.37.2 | Remote compute |
| eastGate | 10.13.37.3 | House1 compute |
| ironGate | 10.13.37.4 | House2 compute |
| southGate | 10.13.37.9 | House2 compute |
| **scuffleGate** | **10.13.37.10** | **Building site router** |
| **marshGate** | **10.13.37.11** | **Building backbone (Phase 2)** |

scuffleGate is the building's first mesh presence (Year 1 beachhead).
marshGate assumes the site router role when the building scales (Year 2+).

---

## songBird Federation

songBird TCP :7700 federation extends to the building:

```
golgiBody (VPS relay)
    ├── eastGate (house1, 10G)
    ├── ironGate (house2, 10G)
    ├── southGate (house2, 10G)
    ├── grapheneGate (portable)
    └── scuffleGate (building, fiber)
            └── marshGate (building backbone, Phase 2)
```

capability.call routing treats the building as another segment.
Affinity scores from TOPOLOGY_MAP:

| Path | Affinity |
|------|----------|
| Within building (same switch) | 0.9 |
| Building ↔ houses (WireGuard + fiber) | 0.7 |
| Building ↔ VPS (direct fiber) | 0.85 |
| Building ↔ portable (TURN) | 0.3 |

The building's commercial fiber connection to golgiBody will have lower
latency than the current residential ATT path — potentially 15-20ms
vs 30ms, improving cross-site capability routing.

---

## Rail-Side Fiber Opportunity

The building's rail adjacency presents a potential fiber conduit
opportunity. Railroad rights-of-way often carry fiber trunk lines.
If the NS South Yard corridor has dark fiber, the building could
potentially obtain a direct fiber connection at competitive rates —
bypassing residential ISPs entirely.

This is speculative and requires investigation during Year 1
(broker contact, utility survey).

---

## References

| Document | Contribution |
|----------|-------------|
| `wateringHole/TOPOLOGY_MAP.toml` | Current physical topology, segments, affinity scores |
| `COMMUNITY_MESH_PROFILE.md` | Old Everett rectangle dimensions, mesh architecture, per-household economics |
| `INFRA_LAYERS.toml` | Device inventory, subnet carving, marshGate future role |
| `NEIGHBORHOOD_MESH_HARDWARE.md` | Radio options, range calculations, site profile |
| `SOVEREIGN_COMPUTE_SHARING.md` | NUC intake pattern, security evolution phases |
