# Thermal Sovereignty — Waste Heat as a Resource Stream

**Date**: Jun 27, 2026
**Status**: Concept — architectural vision, hardware planning stage
**Lineage**: gen4/economics/THE_FLYWHEEL §sunCloud → gen5/foundations/KDERM_DIDERM_ENVELOPE → topology/physical
**Wave**: 128

---

## Thesis

Every watt consumed by compute becomes heat. In a sovereign ecosystem, waste heat is not a problem to be cooled away — it is a resource stream to be captured, concentrated, and applied. The garage becomes a thermal plant: insulated for year-round compute, with heat pumps extracting energy from rack exhaust and delivering it where thermal energy has value.

The biological metaphor: mitochondria don't vent ATP synthesis waste heat into the void. The cell captures it as metabolic warmth, maintaining homeostasis. Our compute mesh should do the same.

---

## The Physics

### Compute Heat Output (Steady State)

| Source | TDP (W) | Annual kWh (24/7) | Annual BTU |
|--------|---------|--------------------|----|
| RTX 5070 (ironGate) | 250 | 2,190 | 7.47M |
| RTX 5090 (northGate) | 450 | 3,942 | 13.4M |
| sporeGate tower | 125 | 1,095 | 3.74M |
| eastGate tower | 200 | 1,752 | 5.98M |
| Additional towers (3-house mesh) | 200-600 | 1,752-5,256 | — |
| **Total (current 4-gate)** | **~1,025** | **~8,979** | **~30.6M** |

A typical home water heater uses ~4,500 kWh/year. A 4-gate garage rack generates **2× that** in waste heat alone. The question is not whether there's enough energy — it's whether we capture it efficiently.

### Heat Pump COP Advantage

Heat pumps move thermal energy at COP 3-5. Meaning: 1 kWh of electricity moves 3-5 kWh of heat energy from source to sink.

But we don't even need to *pump* against a gradient in the compute case — the exhaust air is already **hot** (40-60°C at the rack exhaust). This is a *source-side* advantage: the heat pump's source temperature is elevated, boosting COP significantly above ambient-source numbers.

```
Typical air-source COP (cold ambient → hot water): 2.5-3.5
Compute-exhaust-source COP (warm exhaust → hot water): 4.0-6.0+
```

---

## Architecture: The Thermal Cascade

```
┌──────────────────────────────────────────────────────────┐
│  GARAGE (insulated, year-round)                          │
│                                                          │
│  ┌─────────────────────┐                                 │
│  │  Compute Rack        │                                 │
│  │  (towers, GPUs)      │──── exhaust air (45-60°C) ────┐│
│  │  ~1-2 kW steady      │                               ││
│  └─────────────────────┘                               ││
│                                                         ▼│
│  ┌──────────────────────────────────────────────────────┐│
│  │  Heat Pump (air-to-water)                            ││
│  │  Source: rack exhaust duct                           ││
│  │  Sink: insulated water tank (60-80°C)               ││
│  │  COP: 4-6 (elevated source advantage)               ││
│  └────────────────────────┬─────────────────────────────┘│
│                           │                              │
└───────────────────────────┼──────────────────────────────┘
                            │
              ┌─────────────┼─────────────────┐
              ▼             ▼                  ▼
    ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐
    │ Domestic Hot  │ │ Sauna / Hot  │ │ Kiln / Furnace   │
    │ Water (DHW)   │ │ Tub          │ │ (arts + crafts)  │
    │ 50-60°C       │ │ 70-90°C      │ │ 200-1200°C       │
    │ replaces gas  │ │ wellness     │ │ (boosted by      │
    │ water heater  │ │ + social     │ │  resistance when │
    │               │ │              │ │  needed)          │
    └──────────────┘ └──────────────┘ └──────────────────┘
```

### Thermal Sinks (by temperature tier)

| Tier | Application | Temp Range | Feasibility from Compute Waste |
|------|-------------|-----------|-------------------------------|
| T1 | Space heating (garage) | 20-25°C | **Trivial** — rack exhaust alone |
| T2 | Domestic hot water | 50-60°C | **Direct** — heat pump from exhaust |
| T3 | Sauna | 70-90°C | **Heat pump + small boost** |
| T4 | Kiln/furnace preheat | 200-600°C | **Preheat only** — resistance tops off |
| T5 | High-temp kiln (ceramics) | 800-1200°C | Preheat saves 15-30% energy |

---

## Seasonal Dynamics

### Summer (Cooling Problem)

Traditional data centers fight heat in summer. Our advantage: the heat pump reverses. Compute exhaust feeds DHW year-round (you always need hot water). Excess goes to thermal mass (insulated tank, concrete slab).

If truly excessive: exhaust vents to exterior. The garage is open-air-able in summer.

### Winter (Heating Asset)

This is where the model shines. Compute heat:
1. Keeps the garage above freezing (free)
2. Feeds DHW (replacing gas/electric water heater)
3. Can supplement house heating via hydronic loop
4. Sauna runs "for free" on compute waste + small boost

**The more compute you run in winter, the less you spend on heating.** The economic incentive aligns: heavy workloads (training runs, rendering, science) are cheapest when heating value is highest.

---

## Economics

### Current Baseline (Typical US Household)

| Item | Annual Cost |
|------|------------|
| Water heating (gas) | $300-600 |
| Water heating (electric resistance) | $400-800 |
| Space heating contribution | $200-500 |
| Sauna (electric, 3x/week) | $400-600 |

### Post-Thermal-Sovereignty

| Item | Annual Cost | Notes |
|------|------------|-------|
| Water heating | $0-50 | Heat pump from compute exhaust |
| Garage space heating | $0 | Compute exhaust alone sufficient |
| Sauna | $50-100 | Small resistance boost only |
| Kiln preheat | Saves 20-30% per firing | Preheated intake air |

**Net: $800-1500/year in thermal value from compute waste that was previously vented.**

This is *in addition to* the compute value itself. The flywheel spins twice: once for compute output (science, products, sovereignty), once for thermal capture (DHW, wellness, craft).

---

## Hardware Path

### Phase 1 — Garage Insulation + Passive Capture

- Insulate garage walls + ceiling (R-19 walls, R-30 ceiling)
- Rack towers with directed exhaust (rear-exhaust orientation)
- Ducted exhaust to exterior damper (summer vent) / interior recirculation (winter heat)
- Temperature monitoring (metalForge probe integration)
- **Cost**: $500-1500 depending on insulation method
- **Thermal capture**: space heating only (T1), passive

### Phase 2 — Heat Pump + DHW

- Air-to-water heat pump (source: ducted rack exhaust)
- Insulated buffer tank (40-80 gallon, 60°C target)
- Plumbed to existing hot water system (preheat or replace)
- **Cost**: $2000-4000 (unit + plumbing + tank)
- **Thermal capture**: T1 + T2 (space + hot water)
- **Payback**: 3-5 years vs electric water heater

### Phase 3 — Wellness + Craft Integration

- Sauna (fed by buffer tank hydronic loop + small heater)
- Kiln exhaust preheat (ducted from rack exhaust through kiln intake)
- Concrete thermal mass in garage floor (passive storage)
- **Cost**: Variable (sauna $1500-5000, kiln $500-2000)
- **Thermal capture**: T1 + T2 + T3 + T4

---

## Integration with Ecosystem

### metalForge

Temperature probes throughout the thermal cascade: rack exhaust, heat pump inlet/outlet, buffer tank, ambient. metalForge `device_registry` tracks thermal nodes alongside network nodes.

### cellMembrane

Thermal state as a topology input. Compute scheduling could consider thermal value: "ironGate GPU training batch preferred in winter when thermal capture has highest value."

### sunCloud (Future)

If the flywheel scales to external compute (selling idle GPU time), thermal economics factor into pricing: winter compute is cheaper because heating value offsets electricity cost.

### The Three-House Mesh

Each house's garage becomes a thermal micro-plant:
- Hub 1: sporeGate + eastGate rack → DHW + sauna
- Hub 2: ironGate + future towers → kiln + craft studio
- Hub 3 (flockGate): minimal compute, but same pattern applies

---

## Biological Grounding

The cell doesn't vent metabolic heat — it uses it to maintain homeostasis, drive conformational changes, and power endothermic reactions. Similarly:

| Biology | Thermal Sovereignty |
|---------|-------------------|
| Mitochondrial waste heat → cell homeostasis | Compute waste heat → garage heating |
| Brown adipose tissue (thermogenesis) | Intentional heavy compute for heating |
| Metabolic rate scales with temperature demand | Workload scheduling scales with thermal value |
| Hibernation (reduce metabolic rate when warm) | Throttle compute when thermal sinks saturated |

---

## Open Questions

1. **Optimal heat pump sizing** — how many kW source capacity for a 1-2 kW steady compute load?
2. **Buffer tank sizing** — how much thermal mass to bridge overnight (compute off) to morning (hot water demand)?
3. **Code integration** — should `cellMembrane` expose thermal telemetry as a gate property?
4. **Zoning** — any permit requirements for hydronic systems or garage-to-house plumbing?
5. **Kiln feasibility** — is preheat from compute meaningful at pottery/glass temps, or only at low-fire?

---

*Heat is not waste. Heat is the other half of the flywheel. Every joule of compute produces two outputs: information and warmth. Capture both.*
