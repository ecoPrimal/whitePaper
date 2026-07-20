# The Lansing Scuffle

**A Solarpunk Sovereign Campus in a 1941 Factory**

**Date**: Jul 20, 2026
**Status**: Vision — Year 0 (document, model, prove at house scale)
**Lineage**: gen5/foundations/THERMAL_SOVEREIGNTY → gen3/atlasHugged/09_THE_MANY_ROOMS → gen4/economics/THE_FLYWHEEL → gen5/products/SOVEREIGN_PALLET
**Wave**: 150

---

## Why "Scuffle"

A scuffle is a small, scrappy fight. Not a war — a tangle. The kind of
thing that happens when you refuse to walk past the person lying in the
road. The Samaritan scuffled. He stopped, bandaged, paid the innkeeper,
and moved on. He didn't build an institution. He prepared a room.

This project is a scuffle: a scrappy, phased, flywheel-funded effort to
transform a 1941 industrial building into a solarpunk sovereign campus
that grows food on its roof, heats water with its GPUs, runs science in
its warehouse bays, and prepares rooms for people who need them.

It is not a data center project. It is not a community center project.
It is not a wet lab project. It is what happens when THERMAL_SOVEREIGNTY
meets THE_MANY_ROOMS meets SOVEREIGN_PALLET at industrial scale.

---

## The Shuffle and the Scuffle

The name is not accidental. Lansing already has a
[Shuffle](https://www.lansingshuffle.com/).

The **Lansing Shuffle** took a desirable riverfront location — the
former Lansing City Market at 325 Riverfront Dr, a community anchor
with farmers market vendors, small businesses, and public gathering
space — and replaced it with an entertainment venue. Shuffleboard
courts, restaurants, bars. The community's criticism was specific:
we lost the farmers market. We lost the public commons. The Shuffle
monetizes the location's desirability — foot traffic, riverfront,
downtown adjacency.

The **Lansing Scuffle** inverts every element. It takes an undesirable
industrial location — a vacant factory next to train tracks on south
Cedar — and builds community resources where none existed. There is
no displacement. The building is empty. There is no location premium.
There are train tracks and an asphalt lot. The value comes from latent
infrastructure that the market overlooks: 8 MW of transformer capacity,
14'7" ceilings, a rail spur, 12 acres, and 464K SF of space priced at
$9.15/sqft because nobody wants a factory.

The Shuffle monetizes desirability. The Scuffle creates value from
what others overlook. The cross-traffic is not the point. The silicon,
the science, the community service — that is the point.

See `06_ECONOMICS.md` for the full economic analysis of this inversion.

---

## The Building

**John Bean Building** — 1305 S Cedar St, Lansing, MI 48910

| Attribute | Value |
|-----------|-------|
| **Total area** | 464,281 SF | 
| **Lot** | 12.10 acres (5 parcels) |
| **Structure** | 3-floor south section (116K SF/floor) + 1-floor north section (102,795 SF) + mezzanine |
| **Year built** | 1941 (wartime construction) |
| **Original use** | John Bean Mfg. Co. (fire trucks) → FMC Corp. (military vehicles) |
| **Recent use** | Commercial cannabis grow (3rd floor electrical buildout) |
| **Current status** | **VACANT** |
| **Ceiling heights** | 10'10"/13.5' (south) / **14'7"** (north) |
| **Power** | **8 Megawatt transformers** — 400A/480V per room on 3rd floor |
| **HVAC** | 18 units, 30-50 tons each (~600 tons / ~2.1 MW cooling capacity) |
| **Freight elevator** | 30,000 lb capacity (all 3 floors) |
| **Loading** | 5 loading docks, 4 grade-level doors, vehicle ramps |
| **Sale price** | $4,250,000 ($9.15/SF) |
| **Zoning** | IND-1 (Industrial) |
| **Broker** | Martin Commercial Properties (Christopher Miller, Van Martin) |

### History

The John Bean Building was constructed in 1941 — wartime manufacturing.
Fire trucks and military vehicles for the war effort. The company
became part of Food Machinery Corporation (FMC). The plant closed
around 1974.

After FMC: multi-tenant industrial — artists, small businesses, storage.
Most recently: a commercial cannabis grow operation that built out the
3rd floor with 8 MW of transformer capacity, per-room 400A/480V
circuits, and 18 HVAC units totaling ~600 tons of cooling. The cannabis
operation solved the power-density problem for us. The building now
stands **vacant**.

The building has survived 85 years because it was built for war
production — heavy steel, heavy concrete, heavy power. The same
constraints that made it a factory make it a sovereign campus. And the
cannabis industry's electrical buildout makes it compute-ready on
day one.

### Location

- Just south of the **I-496 / Cedar St interchange** — direct highway access
- On **Cedar St** — the western boundary of the Old Everett rectangle
  (from COMMUNITY_MESH_PROFILE)
- **Adjacent to railroad tracks** — NS South Yard nearby, Cavanaugh Rd
  rail corridor runs along the building's east/south edge
- **~1.5 miles** from the current ecoPrimals cluster
  (4422 Southgate / 641 Samantha)
- **Federal Opportunity Zone** — South Cedar Corridor

---

## The Constrained Evolution Thesis

The ecosystem has been growing silicon in constrained environments since
gen1. The basement HPC cluster at 641 Samantha was the first: eleven
machines, Cat6e ethernet, 10G backbone switch, an AMD 9950X3D running
lattice QCD next to a Titan V running WDM transport simulations. The
constraints — residential power, residential cooling, residential
zoning — were the selective pressure that shaped sovereign compute.

The Rust type system is a constraint. The no-unsafe policy is a
constraint. musl-static compilation is a constraint. AGPL-3.0 is a
constraint. Every constraint that survived became load-bearing
architecture.

The John Bean Building is the next constraint set:

| Constraint | Selective Pressure |
|------------|-------------------|
| 1941 construction | Must work with existing structure, not against it |
| 8 MW power (cannabis buildout) | Data-center-grade electrical already installed — no upgrades needed |
| Warehouse ceilings (14'7" north) | Proper hot/cold aisle, sand battery bays, vertical gardens |
| Industrial zoning | No residential noise complaints. Run GPUs 24/7 |
| Rail adjacency | Bulk hardware logistics. Metaphor: raw materials → finished science |
| 10.1 acres | Room to grow outward (solar, gardens, parking, community) |
| Multi-tenant structure | Incremental lease — don't buy the building, lease one suite |

These are not problems. They are the evolutionary pressure that shapes
the next generation of sovereign infrastructure.

---

## Solarpunk, Not Cyberpunk

The aesthetic matters. This is not a server farm with a community room
bolted on. This is a living building:

- **Gardens on the roof**, not just antennas
- **Food alongside fiber**
- **Warmth alongside compute**
- **Science alongside service**

Growing forward from what exists. A 1941 factory that built fire trucks
becoming a campus that builds sovereign science and serves its
community. The steel beams that held tank turrets hold solar panels.
The warehouse bays that stored munitions store sand batteries. The
loading docks that shipped military vehicles receive donated hardware.

The solarpunk vision is not retrofuturism. It is not "wouldn't it be
nice if." It is the logical consequence of THERMAL_SOVEREIGNTY applied
to an industrial building: every joule used twice, every room prepared
for someone who needs it, every computation attributed and provenance-
chained, every contribution compounding through the geological record.

---

## The 3-5 Year Temporal Arc

This is a pre-pop document. We do not lease a suite tomorrow. We prepare.

The gen1 basement cluster took 18 months to prove — from first hardware
purchase to 12,510 passing checks and 70+ validated papers. The building
takes 3-5 years of pre-pop:

| Phase | Timeline | Focus |
|-------|----------|-------|
| **Year 0** (2026) | Now | Document the vision. Model in footPrint. Prove thermal sovereignty at house scale. Build flywheel momentum. |
| **Year 1** (2027) | Contact | Tour the building. Contact broker. Lease the beachhead suite (~1-2K SF, $216-432/month). Deploy scuffleGate. |
| **Year 2** (2028) | Expand | Second suite (12-30K SF). First wet lab bench. Rooftop solar pilot. Community WiFi. OPRA application. |
| **Year 3** (2029) | Operate | GPU heat capture loop. Sand storage. Hot water to community station. 30-50K SF. K-NOME active. |
| **Year 4-5** (2030-31) | Control | Building-wide lease or acquisition. Full campus. Neighborhood mesh hub. 501(c)(3) or cooperative. |

The key insight: **the entry point is not $4.3M.** The building is
leaseable by the suite. The smallest listed suite (H17-1, 1,080 SF) is
$216/month. That is the activation energy — not a million-dollar
acquisition.

See `06_ECONOMICS.md` for the full lease math and flywheel analysis.
See `07_PREPOP_TIMELINE.md` for the detailed phase breakdown.

---

## Phase 0 Is Always Residential

house1 (4422 Southgate) + house2 (641 Samantha) remain the fallback and
the proving ground. The building is additive, never replacement.

If the building lease falls through, the ecosystem continues from the
houses. If the building succeeds, the houses become residential nodes in
a campus-scale mesh. The architecture is the same at both scales —
K-Derm membrane model, primal composition, sweetGrass attribution,
loamSpine provenance. The building is just a larger cell.

---

## Document Index

| Document | Scope |
|----------|-------|
| **00_THE_SCUFFLE.md** | This document — vision, history, thesis |
| **01_ZONING_AND_ZONES.md** | K-Derm zone mapping for 464K SF |
| **02_THERMAL_SOVEREIGNTY.md** | Full energy loop at building scale |
| **03_NETWORK_TOPOLOGY.md** | Building network + mesh supernode |
| **04_WET_LAB_AND_GARDENS.md** | BSL-1/2 + rooftop agriculture |
| **05_COMMUNITY_AND_HUMANITARIAN.md** | Rooms for people who need them |
| **06_ECONOMICS.md** | Lease → ownership economics, financing, subtenant model, Shuffle inversion |
| **07_PREPOP_TIMELINE.md** | 3-5 year preparation phases |
| **PROPERTY_PROFILE.md** | Physical facts and floor plan sourcing |
| **EXISTING_MODEL.md** | House topology → building topology |

---

## Cross-References

| Document | Relevance |
|----------|-----------|
| `gen5/foundations/THERMAL_SOVEREIGNTY.md` | Core energy model — electricity as fuel, heat as medium |
| `gen5/products/SOVEREIGN_PALLET.md` | Humanitarian services model — biometric identity, hot water |
| `gen3/atlasHugged/09_THE_MANY_ROOMS.md` | Community space philosophy — preparing rooms |
| `gen3/atlasHugged/03_THE_NEW_CITY.md` | Architecture as ethics — no basement |
| `gen4/economics/THE_FLYWHEEL.md` | Seed-stage economics — metabolic cost, Loam Certificates |
| `gen4/architecture/GPU_HEAT_RECOVERY_OPERATIONS.md` | GPU waste heat as space heating |
| `gen4/architecture/SOVEREIGN_HPC_EVOLUTION.md` | Basement cluster → gram-negative organism |
| `gen4/knome/` | K-NOME mentoring methodology |
| `wateringHole/TOPOLOGY_MAP.toml` | Current physical topology |
| `technical/HARDWARE_INVENTORY.md` | Current hardware SSoT |
