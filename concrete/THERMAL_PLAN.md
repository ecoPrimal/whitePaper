# Thermal Sovereignty Plan — Garage Compute Center

**Status**: Planning — physical work beginning
**Date**: Aug 16, 2026
**Priority**: HIGH — strandGate heat is immediate problem

---

## Physical Topology

```
┌─────────────────┐          ┌─────────────┐          ┌─────────────────┐
│  641 Samantha   │◄── 10G ──►│   GARAGE    │◄── 10G? ──►│ 4422 Southgate  │
│  Ave, Lansing   │  fiber    │ (Southgate) │           │  Ave, Lansing   │
│                 │           │             │           │                 │
│ Current compute │           │ FUTURE      │           │ Living / other  │
│ strandGate HERE │           │ COMPUTE     │           │ compute         │
│ (heat problem)  │           │ CENTER      │           │                 │
└─────────────────┘           └─────────────┘           └─────────────────┘
       ▲                            ▲
       │                            │
  Both properties OWNED        ~1970s garage
  by Kevin Mok                 Needs: power, insulation,
                               cooling, security
```

---

## Current Problem

strandGate (Dual EPYC 7452 64c + RTX 3090 + RX 6950 XT) in Samantha Ave house.
Under load:
- Dual EPYC 7452: ~225W TDP
- RTX 3090: 350W TDP
- RX 6950 XT: 335W TDP
- System overhead (RAM, fans, drives): ~100W
- **Total under full load: ~1,000W+ continuous**

That's a 1kW space heater running 24/7 in a bedroom/office. In Michigan summer
(80-90°F outside), this is brutal. AC fights the compute heat and loses.

The other gates add to this. If all 12 nodes are in one house, you're looking at
3-5 kW continuous waste heat. That's untenable indoors.

---

## The Solution: Garage as Thermal Sink

### Why the Garage Works

1. **Thermally isolated from living space** — heat doesn't warm your house in summer
2. **Between both properties** — 10G reach to either house
3. **Dedicated circuits possible** — rewire without affecting house electrical
4. **Ventilation is easy** — garage has (or can have) exhaust fans, louvers
5. **Winter heat recovery optional** — duct waste heat INTO house when wanted
6. **Physical security** — locked, not a bedroom

### What the Garage Needs

---

## Phase 1: Power (Must-Have Before Move)

### Electrical Requirements

| Gate | Estimated Max Draw | Circuit Needed |
|------|-------------------|----------------|
| strandGate (Dual EPYC + 3090 + 6950XT) | 1,000-1,200W | Dedicated 20A/120V or 240V |
| northGate (i9-14900K + RTX 5090) | 800-1,000W | Dedicated 20A/120V |
| biomeGate (TR 3970X + 2×Titan V + 2×MI50) | 1,200-1,500W | Dedicated 20A/240V |
| southGate (5800X3D + 4060) | 400-500W | Shared 20A |
| eastGate (i9-12900 + 4070) | 300-400W | Shared 20A |
| westGate (i7-4771 + 2070S + 76TB HDD) | 300-500W | Dedicated (drives) |
| Other gates (swift, kin, blue) | 200-400W each | Shared |
| 10G switch + networking | 50-100W | Shared |
| **TOTAL MAX** | **~5,000-6,000W** | |

**Electrical reality**: 5-6 kW continuous needs at minimum:
- A **60A sub-panel** fed from the house main (if it has capacity)
- OR a **separate meter** from Lansing BWL (more expensive but clean)
- 3-4 dedicated 20A circuits for the big gates
- 1-2 shared circuits for smaller gates + networking

### What to Assess

- [ ] What's the current garage electrical? (Single 15A circuit? 20A? Any 240V?)
- [ ] What's the main panel amperage at Southgate? (100A? 200A?)
- [ ] Is there spare capacity for a 60A sub-panel feed?
- [ ] Distance from main panel to garage (wire gauge needed)
- [ ] Does BWL allow a second meter on the same property? (for future solar)

### Cost Estimate (DIY vs Electrician)

| Item | DIY | Electrician |
|------|-----|-------------|
| 60A sub-panel + breakers | $200-400 | $800-1,500 |
| Wire run (house to garage, depends on distance) | $200-500 | Included above |
| 4× 20A circuits in garage | $100-200 | $400-800 |
| 240V outlet (for biomeGate or future) | $50-100 | $200-400 |
| Permit (Lansing requires for panel work) | $50-100 | Usually handled by electrician |
| **Total** | **$600-1,300** | **$1,500-3,000** |

**Note**: Panel work usually requires permit + inspection in Lansing. Check with
City of Lansing Building Services (517-483-4100). Some work (adding outlets to
existing circuits) doesn't require permit. Sub-panel installation does.

---

## Phase 2: Insulation (Before Winter)

A 1970s garage likely has:
- No wall insulation
- No ceiling insulation (or minimal)
- Single-pane windows (if any)
- Uninsulated garage door
- Concrete floor (cold sink in winter, thermal mass year-round)

### Minimum Viable Insulation (Compute-Ready)

You don't need the garage to be 72°F. Computers run fine between 50-85°F.
You need:
- Summer: Interior temp < 95°F (with 5kW heat load)
- Winter: Interior temp > 40°F (with 5kW heat load — this is nearly free)

| Improvement | Cost (DIY) | Impact |
|-------------|-----------|--------|
| Ceiling insulation (R-30 batts or blown-in) | $200-500 | Biggest single improvement |
| Garage door insulation kit | $50-100 | Reduces summer solar gain |
| Seal gaps/cracks (spray foam, weatherstrip) | $30-50 | Air infiltration control |
| Wall insulation (if accessible studs) | $300-600 | Good but not critical if heat load is internal |

### The Winter Win

**5 kW continuous = 17,000 BTU/hour.**

A typical space heater is 1,500W (5,100 BTU). You're running the equivalent of
3.3 space heaters 24/7. In a reasonably insulated garage, that ALONE keeps it
above freezing all winter. Michigan average winter temp is ~25°F.

With basic ceiling + door insulation, 5kW compute load probably maintains
50-60°F in the garage through winter WITHOUT any additional heating.

**The compute IS the furnace.** You just need insulation to keep the heat in.

---

## Phase 3: Summer Cooling

Summer is the real challenge. 5 kW inside + Michigan summer (80-90°F ambient) = 
too hot without active cooling.

### Options (cheapest to most expensive)

| Solution | Cost | Effect | Notes |
|----------|------|--------|-------|
| Exhaust fans (2× industrial) | $100-200 | Pull hot air out, fresh air in | Works to ~85°F ambient |
| Portable AC (2× 14,000 BTU) | $600-1,000 | Active cooling | Vented through wall/window |
| Mini-split (18,000-24,000 BTU) | $1,500-3,000 installed | Best solution long-term | Most efficient, quiet, permanent |
| Evaporative cooling | $200-400 | Works in dry conditions only | Michigan is humid — marginal |

**Recommended path**:
1. Start with exhaust fans (immediate, cheap, effective in spring/fall)
2. Add portable AC for first summer if needed
3. Install mini-split when solar offsets the power draw

### Rack Layout for Airflow

Wherever the towers go in the garage, plan for:
- Hot aisle / cold aisle concept (all exhausts face same direction → exhaust fan)
- Don't put towers against a wall with no airflow behind
- Elevated off concrete floor (reduces dust, uses convection)
- Consider a simple open rack ($100-200) to organize and improve airflow

---

## Phase 4: Winter Heat Recovery (Optional / Future)

The 5 kW you're dumping into the garage could heat your house.

| Method | Cost | Complexity | Notes |
|--------|------|-----------|-------|
| Insulated duct from garage to house | $100-300 | Low | Simple inline fan + insulated flex duct. Cold air return at floor. |
| Hot water loop (compute → radiator) | $500-1,000 | Medium | More efficient, no air mixing. Complex. |
| Just leave the garage warm | $0 | Zero | The garage stays 50-60°F. Use it as a warm workshop. |

**Practical approach**: In winter, the garage stays warm from compute heat alone.
If you want to actively heat the house from compute waste, run an insulated duct
with an inline fan + thermostat. When house temp drops below setpoint, fan runs
and pulls garage air into house. Simple. Reversible.

---

## Phase 5: Solar Integration (Future — After Garage is Stable)

Once the garage is the compute center:
- Total draw: ~5 kW continuous = ~3,600 kWh/month (high end)
- Realistic (not all gates loaded 24/7): ~2,000-2,500 kWh/month
- Current cost at ~$0.12/kWh (Lansing BWL): $240-300/month for compute alone

Solar sizing for this load is a separate doc (SOLAR_RESEARCH.md), but the key 
number: you'd need a **15-20 kW system** to fully offset, which is large but
doable across two roofs.

---

## Immediate Action (While Rewiring)

- [ ] Assess current garage electrical (amperage, circuits, panel)
- [ ] Measure distance from Southgate main panel to garage
- [ ] Check Southgate main panel capacity (total amps, spare breaker slots)
- [ ] Decide: sub-panel from house vs separate meter
- [ ] Get strandGate out of Samantha Ave (temporary: just move it, use existing outlet, limit load)
- [ ] Buy/install exhaust fans for summer heat management

---

## Migration Order (Suggested)

Don't move everything at once. Staged migration as circuits are added:

1. **First** (one 20A circuit): westGate (NAS, low power, benefits from isolation)
2. **Second** (one 20A circuit): strandGate (biggest heat problem, move it out of house)
3. **Third** (sub-panel installed): northGate + biomeGate (heavy compute)
4. **Fourth**: Remaining gates as space and circuits allow
5. **Keep in house**: 1-2 quiet gates for desk-side use (eastGate as daily driver?)

---

*The garage is the engine room. The houses are living space with 10G fiber docks.
Compute heat is either exhausted (summer) or recovered (winter). 
The thermal problem becomes a thermal asset.*
