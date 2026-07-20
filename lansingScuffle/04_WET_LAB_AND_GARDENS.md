# Wet Lab and Gardens — Science Meets Agriculture

**Date**: Jul 20, 2026
**Status**: Concept — lab design projected from spring science needs
**Lineage**: gen5/thesis/ → springs/ → gen5/products/SOVEREIGN_PALLET → 00_THE_SCUFFLE
**Wave**: 150

---

## Thesis

The ecoPrimals spring ecosystem produces computational biology that
currently lives entirely in silico: metagenomics pipelines (wetSpring),
soil sensor networks (airSpring), protein folding (hotSpring), health
informatics (healthSpring). Each spring generates hypotheses that
demand bench validation. A wet lab converts computational predictions
into physical confirmation — and the data flows back into the springs
as new validation targets.

The rooftop provides a second validation surface: food production
in GPU-warmed greenhouses, with airSpring sensor networks monitoring
soil chemistry, moisture, temperature, and microbial communities in
real time. The gardens are not decoration. They are instrumented
science experiments that also produce food.

---

## BSL-1 Wet Lab — The Primary Science Space

### Design Requirements

Biosafety Level 1: agents not known to consistently cause disease in
healthy adults. Standard microbiological practices. No special
containment beyond good lab practice.

| Requirement | Specification |
|-------------|--------------|
| Floor | Sealed epoxy or vinyl — easy decontamination |
| Bench surfaces | Chemical-resistant laminate or stainless steel |
| Sink | Hands-free operation, positioned near exit |
| Eyewash / shower | Required within 10 seconds of travel |
| Ventilation | General room ventilation, no special containment |
| Waste | Autoclave access for biohazard waste |
| Storage | Flammable cabinet, chemical storage, -80°C freezer |
| Power | Dedicated circuits for instruments (sequencer, centrifuge, PCR) |
| Data | Ethernet drop to cytoplasm network (nestGate CAS endpoint) |

### Spring Science at the Bench

| Spring | Bench Work | Pipeline |
|--------|-----------|----------|
| **wetSpring** | 16S/ITS amplicon sequencing, environmental DNA extraction | Sample → extraction → PCR → sequencer → FASTQ → nestGate CAS → wetSpring pipeline → loamSpine provenance |
| **airSpring** | Soil sample processing, calibration of sensor arrays | Field sample → BSL-1 bench → analytical chemistry → airSpring model refinement |
| **healthSpring** | Clinical sample processing (BSL-2 if needed) | De-identified samples → extraction → analysis → healthSpring pipeline |
| **hotSpring** | Validation of lattice QCD predictions against physical measurements | Computational prediction → bench experiment → comparison → hotSpring paper |
| **groundSpring** | Geochemical sample analysis, mineral characterization | Core samples → XRF/XRD → mineral ID → groundSpring geological model |

### The Data Pipeline

```
Bench Work (physical)
    │
    ▼
Sample Preparation (extraction, amplification, sequencing)
    │
    ▼
Raw Data (FASTQ, CSV, images)
    │
    ▼
nestGate CAS (content-addressed ingest, BLAKE3 hash)
    │
    ▼
Spring Validation Pipeline (wetSpring, airSpring, etc.)
    │
    ▼
loamSpine Provenance (append-only ledger, Merkle proofs)
    │
    ▼
rhizoCrypt Signatures (cryptographic attestation)
    │
    ▼
Publication / sweetGrass Attribution
```

Every sample that touches the bench enters the provenance chain.
The physical lab and the computational pipeline share the same
identity system. A soil sample collected at the building's rail-side
corridor carries the same BLAKE3 hash and loamSpine chain as the
airSpring analysis that processed it.

---

## BSL-2 Expansion (Future)

BSL-2 adds containment for agents associated with human disease
where exposure routes are known. Requires:

- Biological safety cabinet (BSC Class II)
- Restricted access during work
- Decontamination procedures for all waste
- Personnel vaccination where appropriate

Trigger: when healthSpring clinical collaborations require processing
of human-derived samples. Not needed for Year 1-2.

---

## Rooftop Gardens — Instrumented Agriculture

### GPU-Warmed Growing

Michigan is USDA zone 5b/6a. Growing season: roughly May-October.
GPU waste heat extends the season:

| Growing Mode | Season | Heat Source |
|-------------|--------|------------|
| Open raised beds | May-Oct | Sun only |
| Cold frames (passive) | Mar-Nov | Sun + thermal mass |
| GPU-warmed cold frames | Feb-Dec | Sun + glycol loop from cytoplasm |
| GPU-warmed greenhouse | Year-round | Heated underfloor from sand storage |

A glycol loop carrying GPU waste heat to underfloor heating in a
rooftop greenhouse maintains growing temperatures even in Michigan
winters. The sand thermal storage acts as a buffer — charging from
GPU heat during the day, discharging to the greenhouse at night.

### What Grows

| Category | Crops | Notes |
|----------|-------|-------|
| Leafy greens | Lettuce, spinach, kale, arugula | Year-round in heated greenhouse |
| Herbs | Basil, cilantro, parsley, dill | High-value, quick turnaround |
| Root vegetables | Carrots, beets, radishes | Raised beds, 3-season |
| Legumes | Beans, peas | Nitrogen-fixing, soil building |
| Nightshades | Tomatoes, peppers | Greenhouse-only in winter |
| Pollinator plants | Wildflowers, native Michigan species | Rail-side corridor |

### airSpring Sensor Networks

Every growing zone is an airSpring deployment:

| Sensor | Measurement | Platform |
|--------|------------|----------|
| Soil moisture | Volumetric water content | ESP32 + capacitive probe |
| Soil temperature | Root zone thermal profile | ESP32 + DS18B20 |
| Air temperature / humidity | Microclimate in greenhouse | ESP32 + BME280 |
| Light intensity | PAR (photosynthetically active radiation) | ESP32 + TSL2591 |
| Soil pH | Acidity of growing medium | Periodic manual + analytical |
| CO2 | Greenhouse atmosphere | ESP32 + SCD40 |

Data flows: sensor → ESP32 → LAN → nestGate CAS → airSpring pipeline.
The rooftop garden is simultaneously a food production system and a
distributed sensor experiment.

---

## Rail-Side Pollinator Corridor

The building's railroad adjacency provides a strip of land along the
tracks suitable for a pollinator corridor:

- **Wildflower strips** with native Michigan species
- **USDA habitat restoration** potential funding
- **airSpring monitoring**: soil, microclimate, pollinator activity
- **Community engagement**: volunteer planting days, citizen science
- **Aesthetic**: solarpunk visible from Cedar St and the rail corridor

The corridor is both ecological restoration and public-facing
demonstration of the campus ethos.

---

## Faculty Collaboration

From the `attsi/` directory and gen5 collaborator network:

| Faculty | Domain | Lab Connection |
|---------|--------|---------------|
| Barrick (MSU) | Experimental evolution (LTEE) | wetSpring bench validation |
| Murillo (MSU) | Microbiology, antimicrobial resistance | healthSpring clinical pipeline |
| Gonzales (MSU) | Neurofibromatosis data mining | helixVision + tideGlass composition |

The wet lab provides a physical collaboration point — faculty visit,
bring samples, use instruments, and the computational results flow
through the ecosystem's provenance chain. The lab is not competing
with university facilities. It is supplementing them with sovereign
compute and cryptographic provenance.

---

## Space Requirements

| Space | Size | Phase |
|-------|------|-------|
| BSL-1 wet lab | 800-1,500 SF | Year 2 |
| Dry lab / analysis room | 400-800 SF | Year 1 (can share beachhead) |
| -80°C freezer room | 100-200 SF | Year 2 |
| Instrument room (sequencer, PCR, centrifuge) | 200-400 SF | Year 2 |
| Rooftop greenhouse (pilot) | 2,000-5,000 SF | Year 2 |
| Rooftop greenhouse (expanded) | 10,000-20,000 SF | Year 3-4 |
| Rail-side pollinator corridor | Linear strip, ~100 ft wide | Year 2 |

---

## References

| Document | Contribution |
|----------|-------------|
| `gen5/thesis/SCIENTIFIC_CHALLENGES.md` | External science production demands |
| `springs/wetSpring/whitePaper/` | Metagenomics pipeline, bench validation needs |
| `springs/airSpring/whitePaper/` | Sensor networks, soil science, environmental monitoring |
| `gen5/products/SOVEREIGN_PALLET.md` | Community kitchen fed by rooftop gardens |
| `gen5/collaborators/` | Faculty engagement pipeline |
| `attsi/` | Faculty outreach contacts |
