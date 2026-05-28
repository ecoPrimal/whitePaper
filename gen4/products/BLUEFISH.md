# blueFish

**Sovereign Analytical Chemistry: PFAS Detection Without Vendor Lock-in**

**Date**: May 28, 2026
**Status**: Seeded (gardens/blueFish) — science validated in wetSpring Track 2
**Organization**: [sporeGarden](https://github.com/sporeGarden) (planned)
**Lineage**: wetSpring Track 2 (Jones Lab PFAS work, 40/40 checks) → gen4
**Faculty Contact**: A. Daniel Jones, PhD (MSU Biochemistry)

---

## What It Is

blueFish is a sovereign analytical chemistry data pipeline that replaces
vendor-locked chromatography software (Chromeleon, MassHunter, Xcalibur) with
an open, reproducible, provenance-tracked processing system for PFAS
(per- and polyfluoroalkyl substances) and broader mass spectrometry data.

Where esotericWebb proved the gen4 pattern for **creative** domains, and
helixVision proves it for **genomics**, blueFish proves it for **analytical
chemistry ETL**. Same primals, same PrimalBridge, same graceful degradation —
but the user sees chromatograms, mass spectra, and PFAS detection reports
instead of game worlds or genomics pipelines.

**blueFish is the data plumbing** — it ingests raw instrument data (mzML,
RAW, CDF), processes it through validated detection algorithms, and produces
provenance-sealed analytical results. It is to analytical chemistry what
helixVision's 16S pipeline is to genomics.

---

## The Pipeline

```
Instrument data (LC-MS/MS, GC-MS)
  → blueFish pipeline:
      ├── Format conversion (RAW → mzML via msconvert or sovereign parser)
      ├── Peak detection (FindPFAS algorithm, 17/17 checks)
      ├── Spectral matching (MassBank reference library, 9/9 checks)
      ├── EPA PFAS ML classification (14/14 checks)
      ├── Quantification (calibration curves, QC standards)
      ├── QA/QC (blanks, duplicates, spike recovery)
      └── Provenance (trio: sample → analysis → results → report)
  → Reporting (EPA SOPs, regulatory format compliance)
  → All on sovereign hardware, no Chromeleon, no vendor license
```

---

## Science Source: wetSpring Track 2

blueFish composes validated science from wetSpring:

| Capability | Checks | What It Provides |
|-----------|--------|-----------------|
| FindPFAS detection | 17/17 PASS | PFAS identification from LC-MS/MS spectra |
| EPA PFAS ML | 14/14 PASS | Machine learning classification of PFAS compounds |
| MassBank spectral | 9/9 PASS | Reference spectral library matching |
| **Total** | **40/40 PASS** | Complete PFAS detection + classification + identification |

wetSpring Track 2 was built in direct collaboration with the Jones Lab
at MSU, reproducing their published PFAS detection methods in sovereign
Rust implementations.

---

## Faculty Connection

### A. Daniel Jones, PhD

Professor of Biochemistry & Molecular Biology / Chemistry at MSU.
Center for PFAS Research faculty. Domain: analytical chemistry, mass
spectrometry, PFAS detection.

Kevin worked as Research Specialist in the associated Murphy Lab
(Oct 2024–Oct 2025). The wetSpring Track 2 validation reproduces methods
from this lab. blueFish is the product that makes this validated science
deployable for any lab running PFAS analysis.

### Confirmed Expert Assessment (Jones, May 2026)

Jones reviewed the open-source landscape and confirmed the gap:

| Open-Source Tool | Jones Assessment |
|-----------------|-----------------|
| MZmine | "Failure rates I have found unacceptable" |
| MS-DIAL | Same |
| XCMS | Same |
| Progenesis QI | Good graphical eval, **now obsolete** |

Key insight: "Most of the open source tools don't give you information
that allows for data quality review." The proprietary tool that did
(Progenesis QI) is now dead. **The gap is wide open.**

### The Value Proposition

Labs currently pay for Chromeleon (Thermo Fisher) or MassHunter (Agilent)
to process mass spec data. These tools are:
- Vendor-locked (only work with that vendor's instruments)
- Opaque (proprietary peak detection algorithms)
- Non-reproducible (results vary with software version)
- Expensive (annual licenses, per-seat pricing)

blueFish provides:
- Vendor-agnostic (any mzML/CDF input)
- Transparent (open algorithms, Derivation Anchoring)
- Reproducible (pseudoSpore packaging, BLAKE3 integrity)
- Sovereign (runs on lab hardware, no cloud, no license)
- **Visual QC** (the Progenesis QI feature that died — via petalTongue)
- **Low failure rate** (the MZmine/MS-DIAL/XCMS weakness — Rust precision)

---

## Primals Consumed via IPC

| Primal | Domain | Role in blueFish |
|--------|--------|-----------------|
| toadStool | compute | GPU-accelerated spectral processing (large datasets) |
| barraCuda | math | Statistical computations, calibration curve fitting |
| NestGate | storage | Raw data archive, processed results persistence |
| rhizoCrypt | dag | Analysis session DAG (sample → processing → results) |
| loamSpine | lineage | Chain-of-custody certificates |
| sweetGrass | provenance | Analyst attribution, lab provenance |
| BearDog | crypto | Result signing, data integrity |
| Songbird | discovery | Federation between instruments and processing nodes |
| petalTongue | visualization | Chromatograms, mass spectra, QC dashboards |
| Squirrel | ai | Compound identification assistance, anomaly detection |

---

## Degradation Tiers

| Tier | Available | Capability |
|------|-----------|-----------|
| Standalone | No primals | Process mzML → PFAS report (local, text output) |
| Compute | + toadStool | GPU-accelerated batch processing of large datasets |
| Storage | + NestGate | Persistent archive, cross-session querying |
| Provenance | + trio | Full chain-of-custody from sample to report |
| Full | All | Interactive dashboards, AI identification, federation |

---

## Relationship to helixVision

Both are science ETL products. They complement:

| | helixVision | blueFish |
|---|------------|----------|
| **Input** | FASTQ (sequences) | mzML (spectra) |
| **Domain** | Genomics | Analytical chemistry |
| **Detection** | Taxonomy assignment | Compound identification |
| **Output** | Community profiles | PFAS detection reports |
| **Overlap** | PFAS gene detection (AMR) | PFAS compound detection (MS) |

The PFAS problem bridges both: helixVision detects PFAS-degrading organisms
in environmental samples, while blueFish detects the PFAS compounds
themselves in water/soil. Together they answer "what PFAS is here?" (blueFish)
and "can anything break it down?" (helixVision).

---

## The Name

**blue**: Water — PFAS contamination is primarily a water quality problem.
Also: blueprint, as in the validated plan for sovereign analytical chemistry.

**Fish**: The Murphy Lab (Fisheries and Wildlife) where the PFAS detection
methods were developed. Also: fishing for compounds in complex spectra.

Together: finding contamination in water, using sovereign tools.

---

## What blueFish Will Prove

When implemented, blueFish will demonstrate:

1. **Vendor-locked analytical software is replaceable** — open algorithms
   match proprietary tools for PFAS detection
2. **The sporeGarden pattern works for ETL** — data processing pipelines
   compose primals just like game engines and genomics pipelines
3. **Provenance matters for regulatory chemistry** — EPA SOPs require
   documented chain-of-custody; the trio provides this cryptographically
4. **Lab instruments can be sovereign** — data flows from instrument to
   report without touching vendor cloud services

---

## References

- Garden seed: `gardens/blueFish/`
- wetSpring Track 2: 40/40 PFAS detection checks
- PFAS contact: `whitePaper/attsi/non-anon/contact/pfas/`
- Jones Lab: MSU Center for PFAS Research
- EPA PFAS methods: EPA 533, EPA 537.1, EPA 1633
- Foundation thread: Thread 4 (Environmental Genomics — PFAS detection)

---

*blueFish is not the instrument. It is what the scientist sees from the
instrument — chromatographic peaks that confirm PFAS presence, spectral
matches that identify compounds, detection limits that satisfy EPA
requirements — all traced from sample to report, all on hardware they own.*
