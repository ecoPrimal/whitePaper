# Existing Model — House Topology Maps to Building Scale

**Date**: Jul 20, 2026
**Status**: Concept — scaling analysis from proven house infrastructure
**Lineage**: wateringHole/TOPOLOGY_MAP.toml → INFRA_LAYERS.toml → HARDWARE_INVENTORY.md → 00_THE_SCUFFLE
**Wave**: 150

---

## Thesis

The ecoPrimals ecosystem has been running at house scale since gen1.
Two adjacent houses in Old Everett, Lansing — connected by an 80m
10G active optical cable — form a sovereign compute mesh with
11+ machines, 10G backbone, WireGuard overlay, songBird federation,
and the full primal composition stack.

Everything built at the building scales from patterns already proven
at the houses. Nothing is invented from scratch. The building is the
same organism at a larger scale.

---

## The Mapping

### Network Topology

| House Scale | Building Scale | Scale Factor |
|-------------|---------------|-------------|
| sporeGate (NucBox M6, house1 router) | marshGate (building site router) | Same role, same software, better hardware |
| CRS310 (house1 10G backbone) | Building core switch (10G+) | Same architecture, more ports |
| Omada SX3008F (house2 distribution) | Zone switches (per-zone distribution) | Same pattern, per-zone instead of per-house |
| 80m AOC (10G SFP+ inter-house trunk) | Internal fiber (intra-building 10G trunk) | Shorter runs, same speed |
| ATT BGW320 (residential fiber) | Commercial fiber (dedicated drop) | Better SLA, symmetric speeds |
| TL-SG605S-M2 (2.5G expansion) | Zone access switches | Same role at zone level |

### From TOPOLOGY_MAP.toml

```
HOUSE TOPOLOGY                    BUILDING TOPOLOGY

House 1 backbone zone             Building compute zone
  CRS310 + sporeGate + east/north   Core switch + marshGate + GPU racks
  192.168.4.0/22                      192.168.8.0/22 (new subnet)

House 2 compute zone              Building expansion zones
  Omada + ironGate + southGate       Zone switches + zone gates
  10G trunk from backbone             10G trunk from core

Eero WiFi zone                    Community WiFi zone
  Bridge mode, ATT DHCP               Building backbone, mesh APs
  192.168.1.0/24 (legacy)             Dedicated VLAN

WireGuard overlay                 WireGuard overlay (extended)
  10.13.37.0/24                       + scuffleGate (.10), marshGate (.11)
  golgiBody hub                        Same hub, more peers

songBird federation               songBird federation (extended)
  5 peers (east, iron, south,         + building gates
   graphene, golgi)
```

### Compute Infrastructure

| House Scale | Building Scale | Scale Factor |
|-------------|---------------|-------------|
| **eastGate** (NUC, Akida NPU, 10G) | Building NUC intake (security perimeter) | Same NUC-as-intake pattern |
| **northGate** (9950X3D, RTX 5090) | Building flagship compute node | Same tower profile, dedicated circuit |
| **ironGate** (i9-14900K, RTX 5070) | Building mid-tier compute (multiple) | Scale horizontally |
| **southGate** (Xeon, 128GB ECC) | Building ECC compute / database node | Same role, more memory |
| **strandGate** (Dual EPYC, 256GB ECC) | Building HPC anchor node | Same profile, possibly more GPU |
| **biomeGate** (TR 3970X, HBM2) | Building specialized compute | Same exotic hardware pattern |
| **westGate** (76TB ZFS cold storage) | Building cold storage (ZFS, multiple vdevs) | Scale storage, same ZFS pattern |
| **fieldGate** (portable Raspberry Pi) | Building sensor nodes (ESP32, airSpring) | Scale from 1 to dozens |
| **grapheneGate** (Pixel 9 Pro) | Building mobile intake / portable trust anchor | Same ADB pattern |

### Thermal System

| House Scale | Building Scale | Scale Factor |
|-------------|---------------|-------------|
| GPU heat warms upper floors | GPU heat → sand storage → hot water + gardens + warming | Captured and distributed, not incidental |
| Winter dispatch to upper-floor gates | Year-round dispatch, thermal buffer in sand | Same seasonal logic, bigger battery |
| Basement = cool compute zone | Warehouse bay = sand battery + cool compute option | Same thermal zoning |
| $500/year heating offset (5 GPUs) | $10,000+/year heating displacement (100 GPUs) | ~20x linear scale |
| No hot water recovery | Full hot water cascade to community station | New capability at building scale |
| No food production from heat | Rooftop greenhouse with GPU-heated underfloor | New capability at building scale |

### Community/Network

| House Scale | Building Scale | Scale Factor |
|-------------|---------------|-------------|
| 4422 Southgate = planned mesh supernode | John Bean roof = actual mesh supernode | Better elevation, bigger roof, more antennas |
| Old Everett rectangle target | Same rectangle, better coverage from 3-story industrial | Same community, better physics |
| Residential roof = limited antenna space | Industrial roof = unlimited antenna mounting | Qualitative improvement |
| 1 Eero WiFi bridge (house2) | Mesh AP array (building-wide + humanitarian) | Scale from bridge to multi-AP |
| No public-facing services | Hot water, charging, WiFi, warming = humanitarian | New layer at building scale |
| K-NOME in bedrooms/offices | K-NOME in dedicated mentoring rooms | Same methodology, proper space |
| ABG on Discord | ABG in physical event space | Same science, physical collaboration |

### Science Pipeline

| House Scale | Building Scale | Scale Factor |
|-------------|---------------|-------------|
| In-silico only (all computational) | Computational + bench validation (wet lab) | New physical validation layer |
| No sample processing | BSL-1 wet lab: extraction, PCR, sequencing | Physical → digital pipeline |
| No instruments | Sequencer, centrifuge, -80°C freezer | Grant-funded instrumentation |
| airSpring = concept/prototype | airSpring deployed in rooftop gardens | Field deployment at scale |
| Faculty collaboration via Zoom/email | Faculty visiting the wet lab | Physical collaboration point |

---

## What's New at Building Scale

The building is not just "bigger house." It enables capabilities that
don't exist at residential scale:

| Capability | Why It Requires Building Scale |
|-----------|------------------------------|
| Sand thermal storage | Warehouse bay volume needed for meaningful thermal mass |
| Hot water community service | Industrial plumbing, commercial hot water heater, street-accessible location |
| BSL-1 wet lab | Requires sealed floor, proper ventilation, safety equipment, instrument space |
| Mesh supernode | Industrial roof height and area for sector antenna coverage |
| Public-facing humanitarian services | Zoning (industrial, not residential), ADA accessibility, commercial occupancy |
| 24/7 GPU compute | Industrial zoning = no residential noise/heat complaints, heavy power available |
| Rooftop greenhouse | Industrial roof load capacity, large contiguous area, plumbing access |
| Event space (50-100 people) | Occupancy permits, fire code, ADA, parking |

---

## What Stays the Same

| Pattern | House Scale | Building Scale |
|---------|-------------|---------------|
| K-Derm membrane model | Same zones, same permeability rules | Same zones, physically separated |
| WireGuard overlay | Same subnet, same hub | Extended with building gates |
| songBird federation | Same TCP :7700, same capability routing | More peers, same protocol |
| Primal composition | Same 13+ primals on every gate | Same stack, more gates |
| AGPL-3.0 + CC-BY-SA + ORC | Same triple copyleft | Same trust model |
| sweetGrass attribution | Same braids | More contributors, same chain |
| loamSpine provenance | Same append-only ledger | More sediment layers |
| Content-addressed storage | Same BLAKE3 + nestGate CAS | More data, same identity model |
| USB gate enrollment | Same gate-usb-bootstrap.sh | Same process for building gates |

The organism is the same. The habitat is larger.

---

## Lessons Learned at House Scale

| Lesson | Implication for Building |
|--------|------------------------|
| 80m AOC works flawlessly between buildings | Internal fiber runs in the building will be shorter and easier |
| sporeGate as single router works to ~15 gates | marshGate may need multiple route tables or VLANs above ~20 gates |
| Flat /22 subnet works but will need carving | Building zones should get their own /24 subnets from day 1 |
| Eero bridge mode solved double-NAT problem | WiFi at building scale should be bridged from the start |
| USB enrollment works for new gates | Same USB process for scuffleGate and all building gates |
| ATT fiber as single exit is a bottleneck | Building needs dual-fiber from different providers |
| Cellular failover works but is slow | Building should have fiber redundancy, not cellular |
| 10G backbone eliminates internal bottlenecks | Building backbone should be 10G minimum from day 1 |

---

## References

| Document | Contribution |
|----------|-------------|
| `wateringHole/TOPOLOGY_MAP.toml` | Current physical topology — all zones, segments, latency, affinity |
| `INFRA_LAYERS.toml` | Device inventory, subnet architecture, marshGate future role |
| `technical/HARDWARE_INVENTORY.md` | Gate hardware profiles, K-Derm layer mapping |
| `COMMUNITY_MESH_PROFILE.md` | Old Everett dimensions, mesh tier economics |
| `NEIGHBORHOOD_MESH_HARDWARE.md` | Radio options, range at neighborhood distances |
| `SOVEREIGN_COMPUTE_SHARING.md` | NUC intake pattern, security evolution, JupyterHub |
| `gen4/architecture/SOVEREIGN_HPC_EVOLUTION.md` | Gram-negative membrane model for infrastructure |
| `gen4/architecture/GPU_HEAT_RECOVERY_OPERATIONS.md` | Thermal zone dispatch, seasonal strategy |
