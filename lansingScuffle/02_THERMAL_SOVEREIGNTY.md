# Thermal Sovereignty at Building Scale

**Date**: Jul 20, 2026
**Status**: Concept — building-scale projection from house-scale model
**Lineage**: gen5/foundations/THERMAL_SOVEREIGNTY → gen4/architecture/GPU_HEAT_RECOVERY_OPERATIONS → 00_THE_SCUFFLE
**Wave**: 150

---

## Thesis

> There is no "waste heat." There is no "electricity" vs "heat" vs "compute."
> There is only energy in different forms, flowing through the system at
> different conversion efficiencies.
> — THERMAL_SOVEREIGNTY.md

The John Bean Building is the THERMAL_SOVEREIGNTY thesis realized at
industrial scale. The flat roof is the solar collector. The GPU racks
are the heat generators. The warehouse bays are the sand batteries.
The hot water station is the community sink. The rooftop gardens are
the food sink. Every joule used twice.

---

## The Unified Energy Loop

```
                    ┌──── SOLAR ARRAY (roof) ────┐
                    │    ~464K SF flat roof        │
                    │    Potential 1-2 MW array    │
                    │    ~15W/sqft usable          │
                    └──────────┬──────────────────┘
                               │ electricity
                    ┌──────────▼──────────────────┐
                    │    GPU COMPUTE (cytoplasm)   │
                    │    Science, AI, community    │
                    │    100% of electricity       │
                    │    becomes heat              │
                    └──────────┬──────────────────┘
                               │ heat (disordered energy)
                    ┌──────────▼──────────────────┐
                    │    HOT/COLD AISLE (capture)  │
                    │    Warehouse ceilings enable │
                    │    proper airflow management │
                    │    All heat captured, none   │
                    │    vented to atmosphere      │
                    └──────────┬──────────────────┘
                               │ hot air / glycol
              ┌────────────────┼────────────────┐
              │                │                │
    ┌─────────▼────┐  ┌───────▼──────┐  ┌──────▼───────┐
    │ SAND STORAGE │  │ HOT WATER    │  │ ROOFTOP      │
    │ (warehouse   │  │ (community   │  │ GARDENS      │
    │  bays)       │  │  station)    │  │ (cold frames,│
    │              │  │              │  │  greenhouses) │
    │ $10/kWh      │  │ Showers,     │  │              │
    │ thermal vs   │  │ kitchen,     │  │ GPU warmth   │
    │ $500/kWh     │  │ hygiene      │  │ extends      │
    │ electrical   │  │              │  │ Michigan     │
    │              │  │ 24/7, no     │  │ growing      │
    │ Store summer │  │ credentials  │  │ season       │
    │ heat for     │  │              │  │              │
    │ winter       │  │              │  │ Zone 5b/6a   │
    └──────┬───────┘  └──────────────┘  └──────────────┘
           │
    ┌──────▼───────┐
    │ WARMING      │
    │ CENTER       │
    │ Sand battery │
    │ discharges   │
    │ through      │
    │ winter       │
    │ nights       │
    └──────────────┘
```

---

## Energy Budget — Building Scale

### Solar Potential

| Parameter | Value |
|-----------|-------|
| Roof area | ~464,000 SF (total building footprint) |
| Usable roof (50% — HVAC, setbacks, walkways) | ~232,000 SF |
| Panel efficiency at 15W/sqft | ~3.5 MW nameplate |
| Michigan capacity factor (~15%) | ~525 kW average |
| Annual production estimate | ~4,600 MWh |

For comparison, the current ecoPrimals cluster draws ~2-3 kW average.
Even a small pilot section of roof (10,000 SF) would produce ~150 kW
nameplate / ~22 kW average — enough to run 50+ GPUs.

### GPU Heat Production

Scaling from GPU_HEAT_RECOVERY_OPERATIONS:

| Scale | GPUs | Avg TDP | Total Heat | Heating Equivalent |
|-------|------|---------|------------|-------------------|
| Current (house scale) | 5-7 | 300W | 1.5-2.1 kW | Small room heater |
| Beachhead (1-2K SF) | 8-12 | 300W | 2.4-3.6 kW | Suite heating |
| Mid-scale (12K SF) | 30-50 | 300W | 9-15 kW | Zone heating |
| Full scale (50K SF) | 100-200 | 300W | 30-60 kW | Building section heating |

At 100 GPUs: 30 kW continuous heat = ~102,000 BTU/hr. That is a
commercial HVAC system's worth of heat — for free, as a byproduct
of computation that produces science.

### Sand Thermal Storage

From THERMAL_SOVEREIGNTY: sand stores heat at $10/kWh thermal (vs
$500/kWh for lithium batteries). Warehouse bays are ideal:

| Parameter | Value |
|-----------|-------|
| Sand density | ~1,600 kg/m³ |
| Specific heat | ~0.84 kJ/(kg·°C) |
| Target ΔT | 50°C (ambient → 120°C) |
| Energy per m³ | ~67 MJ = ~18.6 kWh |
| Cost per kWh | ~$10 (sand + insulated container) |

A 10×10×3m warehouse bay filled with sand (~480 m³) stores:
- **~8,900 kWh thermal** — enough to heat 50K SF for several winter days
- Cost: ~$89,000 in sand + insulation + containment
- Comparison: equivalent lithium storage = $4.45 million

Sand does not degrade. Sand does not catch fire. Sand does not need
battery management systems. Sand is the medium.

### Hot Water Cascade

```
GPU heat (60-80°C exhaust)
    → Heat exchanger → glycol loop
    → Sand storage (buffer, 80-120°C)
    → Water-to-water heat exchanger
    → Domestic hot water (50-60°C)
    → Community station: showers, kitchen, hygiene
```

At 30 kW continuous GPU heat, the system can heat approximately
**1,500 liters/hour** from 10°C to 30°C — enough for a continuous
community hot water station serving dozens of people daily.

---

## Seasonal Strategy

Michigan climate (zone 5b/6a) creates a seasonal rhythm:

| Season | GPU Heat Utility | Sand Role | Rooftop Gardens |
|--------|-----------------|-----------|-----------------|
| **Winter** (Nov-Mar) | 100% useful — offsets HVAC | Discharging stored summer heat | Dormant (unless GPU-warmed greenhouse) |
| **Shoulder** (Apr, Oct) | 50% useful | Buffer — absorbing/releasing | Planting / harvest |
| **Summer** (May-Sep) | Excess heat → sand storage | Absorbing summer GPU heat | Peak growing season |

The seasonal loop completes itself: summer GPU heat charges the sand
batteries, which discharge through winter to heat the building, grow
food in greenhouses, and provide hot water to the community station.

From GPU_HEAT_RECOVERY_OPERATIONS, the annual heating offset for 5 GPUs
at house scale is ~$500. At 100 GPUs in the building, that scales to
**~$10,000/year in heating displacement** — real money against the
building's operating costs.

---

## The Two Energies in the Building

From THERMAL_SOVEREIGNTY — the core distinction:

**Electricity (ordered energy, fuel):**
- Enters from grid or solar
- Does one job: run compute
- Travels on wires, point-to-point, fast, expensive
- The nervous system of the building

**Heat (disordered energy, medium):**
- Created by compute (100% conversion, irreversible)
- Fills volumes, moves through mass, slow, cheap
- Stored in sand ($10/kWh vs $500/kWh electrical)
- The circulatory system of the building

The building's thermal infrastructure is not a cooling system that
removes waste heat. It is a **distribution system** that routes heat
to where it has value. The GPU racks are not the building's problem —
they are its furnace.

---

## Existing Infrastructure (From Cannabis Grow Buildout)

The building already has data-center-grade power and cooling:

| System | Specification | Implication |
|--------|--------------|-------------|
| **Power** | 8 MW transformer capacity | No electrical upgrades needed for Phase 1-3 |
| **Per-room power** | 400A/480V + 225A/208V per room (9 rooms) | Each room is a self-contained compute cell |
| **HVAC** | 18 units, 30-50 tons each (~600 tons total, ~2.1 MW cooling) | Existing cooling handles full compute load |
| **Switchgear** | VFI + visible disconnect, dedicated 600A @ 13,200V from BWL | Utility-grade protection already in place |

The cannabis grow operation's electrical buildout cost hundreds of
thousands of dollars. For compute, this infrastructure is directly
reusable — the power density profile (high wattage per room, heavy
cooling, dedicated circuits) is identical.

## Implementation Phases

| Phase | Heat Infrastructure |
|-------|-------------------|
| **Year 1** (beachhead) | Use existing 35-ton HVAC per room. Document baseline energy. Portable heat capture pilot on one room's exhaust. |
| **Year 2** (expansion) | Ducted hot/cold aisle in north section (14'7" ceilings). Glycol loop from compute exhaust to hot water pre-heater. |
| **Year 3** (sand pilot) | First sand storage bay in north section (55' bays ideal). Hot water station operational. Begin phasing out roof HVAC units in favor of heat capture. |
| **Year 4** (full loop) | Solar pilot section. Sand storage scaled. Rooftop greenhouse with GPU-heated underfloor. |
| **Year 5** (sovereignty) | Full solar array. Building-wide heat distribution. Sand batteries for winter. Community hot water 24/7. Remaining HVAC units decommissioned or repurposed. |

---

## References

| Document | Contribution |
|----------|-------------|
| `gen5/foundations/THERMAL_SOVEREIGNTY.md` | Core energy model — unified accounting, two-energy thesis, sand storage economics |
| `gen4/architecture/GPU_HEAT_RECOVERY_OPERATIONS.md` | Per-GPU heat budget, seasonal dispatch, annual heating offset calculations |
| `gen3/baseCamp/14_sovereign_compute_hardware.md` | Three-tier precision model, fleet thermal profiles |
| `gen5/products/SOVEREIGN_PALLET.md` | Hot water as humanitarian service, sand battery discharge model |
