# Property Profile — John Bean Building

**Date**: Jul 20, 2026
**Status**: Updated with Martin Commercial offering memorandum (2025)
**Wave**: 150

---

## Identity

| Field | Value |
|-------|-------|
| **Address** | 1305 S Cedar St, Lansing, MI 48910 |
| **Common name** | John Bean Building |
| **Municipality** | City of Lansing |
| **Zoning** | IND-1 (Industrial) |
| **Primary parcel** | 33-01-01-21-426-005 |
| **Listing broker** | Martin Commercial Properties, 1111 Michigan Ave., Ste 300, East Lansing, MI 48823 |
| **Contacts** | Christopher Miller, SIOR, SVP — (517) 242-7561 / christopher.miller@martincommercial.com |
| | Van W. Martin, CCIM, SIOR, CRE, President — 517.319.9245 / van.martin@martincommercial.com |
| **Listing** | [Martin Commercial](https://martincommercial.com) / [CPIX](https://cpix.resimplifi.com/listings/0b1ab1f0-464000-sf-redevelopment-opp-iconic-john-bean-building) |

---

## Physical Facts

| Attribute | Value | Source |
|-----------|-------|--------|
| **Total area** | 464,281 SF | Offering memorandum |
| **Combined parcels** | 12.10 acres (5 parcels) | Offering memorandum |
| **Year built** | 1941 | Offering memorandum |
| **Sale price** | $4,250,000 ($9.15/SF) | Offering memorandum |
| **Terms** | Cash / Conventional | Offering memorandum |
| **Current status** | **VACANT** | Offering memorandum |
| **Previous use** | Commercial cannabis grow operation | Offering memorandum |
| **Sprinklered** | Combination wet/dry system | Offering memorandum |
| **Signage** | Billboard & building signage | Offering memorandum |
| **Parking** | On-site | Offering memorandum |
| **Freight elevator** | 30,000 lb capacity (all 3 floors) | Offering memorandum |

---

## Building Structure

The building has two distinct structural sections:

### Three-Floor Section (South Side)

| Attribute | Value |
|-----------|-------|
| Floors | 3 |
| Area per floor | 116,000 SF |
| **Total** | **348,000 SF** |
| Bay size | 18' x 20' |
| Clear height | 10'10" / 13.5' to deck |

### Single-Floor Section (North Side)

| Attribute | Value |
|-----------|-------|
| Floors | 1 |
| **Total** | **102,795 SF** |
| Bay size | 55' x 18' |
| Clear height | **14'7"** |
| Mezzanine | 250' x 33' (~8,250 SF) |

**Implications for zone assignment:**
- The **north section** (single floor, 14'7" clear, 55' bays) is ideal for
  compute (tall ceilings for hot/cold aisle) and sand thermal storage
  (warehouse-scale volume). The 55' bay width accommodates large
  installations.
- The **south section** (3 floors, 116K SF each) is ideal for science,
  community, and office use. The freight elevator (30,000 lbs) enables
  moving heavy equipment between floors.
- The **3rd floor** already has per-room electrical buildout from the
  cannabis grow operation — directly reusable for GPU compute.

---

## Electrical System (Game-Changing)

The building has **data-center-grade power** — already installed.

### Primary Power

| Attribute | Value |
|-----------|-------|
| **Total transformer capacity** | **8 Megawatts** |
| Primary circuit | 600 AMP @ 13,200V (dedicated from BWL) |
| Switchgear | VFI (Vacuum Fault Interrupter) + visible disconnect |
| Construction cost (BWL) | ~$330,000 (paid by BWL — new poles, underground conduit, vault, primary feeder cable) |

### 3rd Floor Electrical Room

| Equipment | Specification |
|-----------|--------------|
| 3x 3,000 KVA transformers | 480/277V and 208/120V |
| 3x 500 KVA transformers | 480/277V and 208/120V |
| Switchboards | 4,000 AMP and 1,600 AMP |
| Potential lighting load | 2.3 million watts |
| Potential A/C load | 3 million watts |

### Per-Room Power (3rd Floor, 9 Rooms)

| Attribute | Value |
|-----------|-------|
| **480/277V service** | **400 amps per room** |
| **208/120V service** | **225 amps per room** |
| Light capacity per room | 100,000 watts (standard) / 130,000 watts (large) |
| A/C capacity per room | 70 tons (standard) / 100 tons (large) |

**What this means for compute:**

400 amps at 480V per room = ~192 kW per room. A single room can power:
- ~640 RTX 3090s (at 300W each), or
- ~426 RTX 5090s (at 450W each), or
- More realistically, 20-40 high-density GPU servers

Nine rooms on the 3rd floor = **~1.7 MW of per-room compute power**
already wired and ready. The cannabis grow operation built exactly the
electrical infrastructure that GPU compute needs: high-amperage
per-room circuits, dedicated cooling per room, and centralized
switchgear.

The building does not need electrical upgrades for Phase 1-3 of the
campus plan. The power is already there.

---

## HVAC System (Already Installed)

18 large-scale rooftop units, 30-50 tons each:

| Space | Equipment |
|-------|-----------|
| Room 301 | (3) 20 Ton Lennox Split Systems |
| Room 302 | (3) 20 Ton Lennox Split Systems |
| Room 303 | (2) 35 Ton Daikin RTUs |
| Room 304 | (2) 50 Ton Daikin RTUs |
| Room 305 | (2) 35 Ton Daikin RTUs |
| Room 306 | (2) 35 Ton Daikin RTUs |
| Room 307 | (2) 35 Ton Daikin RTUs |
| Room 308 | (2) 35 Ton Daikin RTUs |
| Room 309 | (2) 35 Ton Daikin RTUs |
| Hallway East | (1) 35 Ton Daikin RTU |
| Hallway West | (1) 35 Ton Daikin RTU |
| Electrical Room | (1) 15 Ton Daikin RTU |
| Harvest Room | (1) 15 Ton Daikin RTU |

Total cooling capacity: ~600+ tons. For reference, 1 ton of cooling
handles ~3.5 kW of heat. 600 tons = **~2.1 MW of cooling capacity**.

For the thermal sovereignty model: these existing HVAC units represent
infrastructure that can be phased out as the heat-capture system comes
online. In Year 1, use the existing cooling. In Year 2-3, redirect
heat to sand storage instead of venting it.

---

## 3rd Floor Room Layout

From the offering memorandum (cannabis grow buildout):

| Room | Dimensions | Notes |
|------|-----------|-------|
| 301 | 53'-7" x 59' (~3,162 SF) | Standard room |
| 302 | 53'-7" x 59' (~3,162 SF) | Standard room |
| 303 | 53'-7" x 59' (~3,162 SF) | Standard room |
| 304 | 71'-7" x 59' (~4,224 SF) | **Large room** |
| 305 | 53'-7" x 59' (~3,162 SF) | Standard room |
| 306 | 71'-7" x 49'-2" (~3,520 SF) | Large room (wider hallway side) |
| 307 | 53'-7" x 59' (~3,162 SF) | Standard room |
| 308 | 53'-7" x 59' (~3,162 SF) | Standard room |
| 309 | 53'-7" x 59' (~3,162 SF) | Standard room |

Plus: Hallway East, Hallway West, Electrical Room, Harvest Room, Kitchen

**Total 3rd floor room area**: ~29,878 SF in 9 rooms, plus corridors
and utility spaces.

**Zone mapping for compute:**
Each 3,162 SF room with 400A/480V is a self-contained compute cell:
- Its own power circuit
- Its own HVAC (35-70 tons)
- Its own overhead doors
- Separated from adjacent rooms

This is better than purpose-built data center pods. The cannabis
industry solved the power-density and per-room-cooling problem for us.

---

## Parcels

| # | Address | Acreage | SEV (2025) | Taxable (2025) | Taxes (2024) | Parcel ID |
|---|---------|---------|-----------|---------------|-------------|-----------|
| 1 | 1305 Cedar St | 10.06 | $2,697,900 | $1,871,474 | $151,166 | 33-01-01-21-426-005 |
| 2 | Linval St | 1.75 | $55,100 | $45,979 | $3,715 | 33-01-01-21-428-082 |
| 3 | 518 Christiancy St | 0.15 | $4,400 | $3,864 | $312 | 33-01-01-21-427-147 |
| 4 | 535 Christiancy St | 0.07 | $3,100 | $2,728 | $349 | 33-01-01-21-426-006 |
| 5 | 537 Christiancy St | 0.07 | $3,100 | $2,581 | $337 | 33-01-01-21-426-009 |
| | **Total** | **12.10** | **$2,763,600** | **$1,926,626** | **$155,879** | |

Annual property taxes: ~$155,879. This is a significant carrying cost
and a strong argument for OPRA (12-year tax freeze on improvements).

---

## Site Plan

From the offering memorandum site plan:

```
                        CHRISTIANCY STREET
                    ┌────────────────────────┐
                    │                        │
          LINVAL   │    JOHN BEAN BUILDING   │   CEDAR
          STREET   │                        │   STREET
                    │  ┌──── 3-FLOOR ────┐  │
                    │  │  (South Side)   │  │
                    │  │  116K SF/floor  │  │
                    │  │  348K SF total  │  │
                    │  └─────────────────┘  │
                    │  ┌── SINGLE FLOOR ──┐ │
                    │  │  (North Side)    │ │
                    │  │  102,795 SF      │ │
                    │  │  14'7" clear     │ │
                    │  └─────────────────┘  │
                    │                        │
                    │  RAMP  DOCK  OVERHANG  │
                    │                        │
                    │  R.R. SPUR             │
                    │  ═══════════════════   │
                    │  JACKSON & LANSING RR  │
                    │  CANADIAN NATIONAL RR  │
                    └────────────────────────┘
                        LYONS AVENUE
```

### Surrounding Context

| Direction | Feature |
|-----------|---------|
| West | Cedar Street frontage |
| North/NE | Christiancy Street |
| East | Linval Street, Linval St parcel (1.75 acres) |
| South | Lyons Avenue, residential properties |
| SE | Railroad spur, Jackson & Lansing RR, Canadian National RR |
| Adjacent | O'Leary Paint Co. (415 Baker St), City of Lansing Fleet Services (530 E. South St.) |

### Building Dimensions (from site plan callouts)

Dimension callouts from the site plan: 127', 150', 165', 110', 69',
369', 147', 170', 434', 749', 543'. These describe the building
perimeter and setbacks. The longest dimension (749') suggests the
building runs approximately 750 feet along its longest axis.

---

## History

| Period | Use |
|--------|-----|
| 1941 | Constructed (wartime manufacturing) |
| 1941-~1974 | John Bean Mfg. / FMC Corp. — fire trucks, military vehicles |
| 1974-~2020 | Multi-tenant: artists, small businesses, storage |
| ~2020-~2024 | Commercial cannabis grow operation (3rd floor buildout) |
| 2024-present | **Vacant** |

The cannabis operation's legacy is the electrical infrastructure:
8 MW transformers, per-room 400A circuits, per-room HVAC, and the
3rd floor room buildout. This infrastructure cost hundreds of
thousands of dollars to install and is directly reusable for
GPU compute.

---

## Loading and Access

| Feature | Specification |
|---------|--------------|
| Loading docks | 5 |
| Grade-level doors | 4 |
| Door 1 | 11' x 14' |
| Door 2 | 14' x 12' |
| Door 3 | 10' x 14' |
| Door 4 | 10' x 9' |
| Freight elevator | 30,000 lb capacity (all 3 floors) |
| Vehicle ramps | Each floor serviced by vehicle ramps |
| R.R. spur | Direct rail spur access |

The freight elevator and vehicle ramps mean heavy equipment (GPU
servers, sand storage containers, lab instruments) can reach any
floor without crane operations.

---

## Floor Plans

The offering memorandum includes floor plans for all three floors
plus a site plan:

| Page | Content |
|------|---------|
| p.10 | First floor plan (north section + south section ground level) |
| p.11 | Second floor plan (south section only — shows single-floor north section ceiling) |
| p.12 | Third floor plan (south section only — shows 9 rooms, hallways, electrical room, kitchen) |
| p.13 | Site plan (full parcel, surrounding streets, rail, dimensions) |

**Source file**: `1305-s-cedar-st-lansing-property-brochure.pdf`
(Martin Commercial Properties, 2025 offering memorandum)

These floor plans should be digitized into footPrint as the
building-level geometry layer. The 3rd floor room layout is the most
detailed and directly maps to the K-Derm zone model.

### Floor Plan Refinement Path

1. **Done**: Extracted text/dimensions from PDF brochure
2. **Next**: Trace floor plan images into GeoJSON polygons for footPrint
3. **Year 1**: Physical walkthrough with laser measurements to verify
4. **Ongoing**: Refine as suites are leased and inspected

---

## Environmental Considerations

| Factor | Assessment |
|--------|-----------|
| **Age** | 1941 — pre-EPA (1970), pre-Clean Air/Water Acts |
| **Original use** | Heavy manufacturing (fire trucks, military vehicles) |
| **Recent use** | Cannabis grow (chemicals, fertilizers) |
| **Likely contaminants** | Petroleum products, solvents, heavy metals, PCBs (transformers), asbestos (insulation, floor tiles), cannabis grow chemicals |
| **Phase I ESA** | Required before occupancy |
| **Phase II ESA** | Required if Phase I identifies recognized environmental conditions |
| **Remediation** | Brownfield TIF can fund remediation through tax increment financing |
| **Lead/asbestos** | Common in 1941 construction — survey required before renovation |

---

## Opportunity Zone and Incentive Status

| Program | Status |
|---------|--------|
| **Federal Opportunity Zone** | South Cedar Corridor — confirmed |
| **OPRA** (Obsolete Property Rehabilitation Act) | Strong candidate — vacant 1941 industrial, IND-1 zoning |
| **Brownfield TIF** | Strong candidate — historical industrial contamination likely |
| **Industrial Property Tax Abatement** (PA 198) | Eligible — IND-1 zoning, high-tech reuse |
| **Historic Tax Credit** | Possible — 1941 wartime construction, requires NPS evaluation |

At $155,879/year in current property taxes, OPRA's 12-year tax freeze
on improvements is extremely valuable for any rehabilitation project.

---

## What This Changes About the Plan

The brochure data significantly improves the campus plan:

| Previous Assumption | Actual (from brochure) | Impact |
|--------------------|----------------------|--------|
| Multi-tenant, suites available | **VACANT** — entire building available | No tenant coordination needed. Full building available for phased occupation. |
| 10.1 acres | **12.10 acres** (5 parcels) | More land for solar, gardens, parking, community space |
| Year built 1936 | **Year built 1941** | Wartime construction (stronger), but slightly less historic-credit potential |
| "Heavy power" (vague) | **8 MW transformers, per-room 400A/480V** | Data-center-grade power. No electrical upgrades needed for Phase 1-3. |
| Standard HVAC | **18 units, 30-50 tons each, ~600 tons total** | Cooling infrastructure exists. Phase into heat-capture over time. |
| Unknown floor layout | **3-floor south (116K/floor) + 1-floor north (103K) + mezzanine** | Clear zone assignment: north=compute/sand, south floors=science/community |
| Suite-by-suite lease at $0.08-0.20/sqft | **Vacant building, $4.25M sale, lease rates may differ** | Lease negotiation starts from vacancy — potentially better terms |
| Unknown room layout | **9 rooms on 3rd floor, each ~3,100 SF with dedicated power+HVAC** | Pre-built compute cells. Each room is a self-contained GPU pod. |

---

## References

| Source | Description |
|--------|-------------|
| Martin Commercial offering memorandum (2025) | Primary source — 17-page brochure with floor plans, electrical, parcel data |
| [CPIX listing](https://cpix.resimplifi.com/listings/0b1ab1f0-464000-sf-redevelopment-opp-iconic-john-bean-building) | Online listing |
| [Rofo listing](https://m.rofo.com/building/MI/Lansing/1305-S-Cedar-St-178692.html) | Suite availability (may be outdated — building is now vacant) |
| [Ingham County FetchGIS](https://ingham-equalization.rsgis.msu.edu/) | Parcel boundary, GIS data |
| [Lansing EDC Incentives](https://lansingedc.com/resources/developer/tax-incentives) | OPRA, Brownfield TIF, PA 198 |
