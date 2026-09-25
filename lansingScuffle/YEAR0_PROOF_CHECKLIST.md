# Lansing Scuffle — Year 0 Proof Documentation

**Purpose:** Document house-scale proof of thermal sovereignty, compute
infrastructure, and community flywheel before Year 1 beachhead lease.
**Timeline:** Aug 2026 → Q1 2027
**Cost:** $0 incremental (proves with existing hardware)
**Date:** August 25, 2026

---

## Year 0 Exit Criteria

All items must be documented with evidence before approaching a Year 1 lease.

### Track A: Thermal Sovereignty Proof

| # | Deliverable | Status | Evidence needed |
|---|------------|--------|----------------|
| A1 | Garage electrical assessment | NOT STARTED | Panel capacity, circuit count, distance from main, permit path (Lansing Building Services) |
| A2 | Move strandGate to garage | NOT STARTED | Photo before/after; measure bedroom temp delta |
| A3 | Summer cooling strategy | NOT STARTED | Exhaust fans installed; interior temp log under GPU load |
| A4 | First thermal recovery cycle | NOT STARTED | GPU heat → measurable temperature increase in useful space (garage self-heating, hot water pre-heat, or duct recovery) |
| A5 | Baseline energy measurements | NOT STARTED | kWh/GPU-hour; BWL bills before/after garage migration |
| A6 | Seasonal heating offset documented | NOT STARTED | Winter data: GPU heat contribution to garage/house heating |

### Track B: Compute Infrastructure Proof

| # | Deliverable | Status | Evidence needed |
|---|------------|--------|----------------|
| B1 | southGate fully enrolled | IN PROGRESS | All gates on songBird mesh; 10G between properties |
| B2 | NUCLEUS operational on ≥3 gates | IN PROGRESS | biomeOS attesting; capability routing proven |
| B3 | Uptime log (30 consecutive days) | NOT STARTED | skunkBat metrics exported |
| B4 | Cross-gate computation demonstrated | IN PROGRESS | Job runs across southGate ↔ westGate ↔ blueGate |
| B5 | Power budget documented | PARTIAL | Total kW per gate; aggregate metabolic cost |

### Track C: Community Flywheel Proof

| # | Deliverable | Status | Evidence needed |
|---|------------|--------|----------------|
| C1 | ≥5 monthly supporters | NOT MET | GitHub Sponsors or Open Collective; documented recurring contributions |
| C2 | Old Everett Neighborhood Association contact | NOT STARTED | Attend meeting; introduce vision |
| C3 | Community WiFi pilot | NOT STARTED | One AP serving public space; no captive portal |
| C4 | Hardware donation received | UNKNOWN | At least one community-contributed gate or GPU |
| C5 | GitHub Sponsors / Open Collective | NOT STARTED | Page live with ecoPrimals branding |

### Track D: Scuffle Documentation

| # | Deliverable | Status | Evidence needed |
|---|------------|--------|----------------|
| D1 | lansingScuffle document set | COMPLETE | 10 docs in whitePaper/lansingScuffle/ |
| D2 | footPrint model with building | NOT STARTED | John Bean Building parcel loaded in footPrint GIS |
| D3 | Incentive research | COMPLETE | Opportunity Zone, OPRA, Brownfield TIF documented |
| D4 | Phase 0 residential fallback doc | NOT STARTED | All data replicated to house gates; building is additive, not required |

---

## Measurement Templates

### A5: Energy Baseline Log

| Date | Gate | GPU(s) | Hours | kWh (meter) | kWh/GPU-hr | Ambient temp | Interior temp |
|------|------|--------|-------|-------------|-----------|-------------|--------------|
| | | | | | | | |
| | | | | | | | |

### A4: Thermal Recovery Log

| Date | Heat source | Sink | Duration | Start temp | End temp | Delta | Method |
|------|------------|------|----------|-----------|---------|-------|--------|
| | strandGate (1kW) | Garage ambient | | | | | Exhaust duct |
| | | | | | | | |

### B5: Power Budget

| Gate | Location | GPU(s) | Idle (W) | Load (W) | Monthly kWh | Monthly cost |
|------|----------|--------|----------|----------|-------------|-------------|
| westGate | Samantha basement | | | | | |
| blueGate | Samantha | | | | | |
| strandGate | Southgate (→garage) | | | | | |
| southGate | | | | | | |
| **TOTAL** | | | | | | **$___/mo** |

---

## Year 1 Gate Criteria

Year 0 evidence feeds into Year 1 lease conversation:

| What Year 1 landlord/broker needs to see | Year 0 proof |
|------------------------------------------|-------------|
| "Can you actually run GPUs in a building?" | A2-A6: thermal logs, power budget |
| "Is your infrastructure real?" | B1-B5: uptime, cross-gate computation |
| "Do you have community support?" | C1-C5: supporters, neighborhood contact |
| "Is this a real plan?" | D1-D4: full document set + footPrint model |

---

## Phase 0 Residential Fallback

Critical documentation: even if the John Bean Building never materializes,
everything proven at house scale remains valuable:

- Thermal sovereignty reduces home energy costs
- Compute infrastructure serves collaborators regardless of location
- Community flywheel transfers to any physical location
- All data replicated across house gates — building is additive

Document this explicitly so the Scuffle vision doesn't become a
single point of failure.

---

*Year 0 costs $0. It proves the thesis at house scale with existing
hardware. Year 1 costs ~$778/mo for a single beachhead room. The
gap between them is documentation, not money.*
