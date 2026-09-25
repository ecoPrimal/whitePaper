# concrete/ — Kevin Mok's Physical Reality

**Status**: Active working directory
**Date**: Aug 16, 2026
**Agent**: northGate (external surface team)

---

## What This Is

The ecoPrimals agents handle code, experiments, and inner membrane infrastructure.
This directory handles the meat-space reality that makes it all possible:

- Physical infrastructure (solar, thermal, power, garage conversion)
- Money and legal (self-employment, grants as applicant, income bridge)
- Hardware logistics (moving towers, rack layout, cabling, cooling)
- Time and energy (prioritization, scheduling, what to do this week)
- Long-term vision logistics (wet lab camper, expedition readiness)
- External positioning (resume, LinkedIn, professional communications)

---

## Current State (Aug 2026)

| Reality | Value |
|---------|-------|
| Location | Lansing, MI |
| Housing | House (owned? rented? — confirm) |
| Income | 401k distributions (no earned income) |
| Hardware | ~$15K in HPC equipment, 10+ towers, basement deployment |
| Power cost | ~$485/month metabolic (electricity + ISP + VPS) |
| Networking | 10G backbone installed (switch + 4 NICs) |
| Vehicle | (Kevin's personal — confirm status) |
| Legal entity | None filed yet for ecoPrimals income |
| Health insurance | (confirm status) |

---

## Immediate Goals (Aug-Sep 2026)

1. **Self-employment filing** — Schedule C at minimum. Establishes earned income for:
   - Receiving grant sub-awards (CTF NDU compute role)
   - Accepting challenge prize money
   - Writing off hardware, power, and home office
   - Building Social Security quarters (401k doesn't count)

2. **Thermal sovereignty plan** — Towers generate heat.
   - Summer: heat must exit (garage cooling strategy)
   - Winter: heat recovery into living space
   - Transition: moving from basement to garage
   - Goal: compute waste heat replaces furnace load

3. **Solar research** — Michigan net metering, roof assessment, compute load calc.
   - The $485/month is the target to offset
   - Grid-tie with battery backup for UPS
   - ITC (30% federal tax credit) applies to self-employed

4. **Income bridge** — How long does 401k last at current burn?
   - Monthly expenses (power, mortgage/rent, food, DaSean support)
   - When does first grant money realistically arrive?
   - What fills the gap?

---

## Long-Term Vision

A wet lab camper with sovereign compute, exploring unique biomes.
Field genomics (eDNA, 16S, nanopore sequencing) from ecosystems no one else visits.
The Inkfish email wasn't just outreach — it's what Kevin actually wants to do.

This is concrete. It requires:
- Vehicle (camper/van conversion or trailer)
- Nanopore sequencer (MinION, ~$1K)
- Field compute (swiftGate or equivalent, battery-powered)
- PADI certification (for marine work)
- Target biomes identified
- Partnership or solo expedition structure

---

## Upstream Interface

What we need from ecoPrimals agents (and vice versa):
- Signal when Phase 0 validation completes (triggers Gonzales email)
- Data on actual power consumption per gate (for solar sizing)
- Thermal output measurements (for heat recovery design)
- Gate uptime requirements (for UPS/battery sizing)

What they need from us:
- Physical hardware moves executed
- Power circuits installed
- Solar panels on roof
- Garage insulated and conditioned
- Legal entity formed (for crates.io, ORCID, grant banking)

---

## Directory Plan

```
concrete/
├── README.md                    ← You are here
├── SELF_EMPLOYMENT.md           ← Filing options, timeline, tax implications
├── THERMAL_PLAN.md              ← Heat budget, garage conversion, seasonal strategy
├── SOLAR_RESEARCH.md            ← Michigan specifics, load calc, incentives
├── INCOME_BRIDGE.md             ← 401k runway, expenses, when income arrives
├── POWER_BUDGET.md              ← Per-gate wattage, 10G switch, total draw
├── CAMPER_VISION.md             ← Long-term mobile lab specs
└── UPSTREAM_INTERFACE.md        ← What we trade with eco agents
```

---

*The code doesn't run without electricity. The grants don't arrive without a legal entity.
The science doesn't happen in unique biomes without a vehicle that gets there.
This is the foundation under the foundation.*
