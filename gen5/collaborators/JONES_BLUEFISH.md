# Dan Jones — PFAS Consulting & blueFish Product Specification

**Status**: Active — emeritus consulting confirmed, two technical data dumps received
**Collaborator**: A. Daniel Jones, PhD, Professor Emeritus, Biochemistry & Molecular Biology, MSU
**Product**: blueFish (sovereign PFAS analytical chemistry ETL)
**Springs Fed**: wetSpring Track 2
**Date**: May 28, 2026

---

## The Relationship

Kevin worked as Research Specialist in the associated Murphy Lab (Oct 2024 - Oct 2025). Jones was the remote PI for PFAS analytical chemistry work. Kevin was laid off when PFAS funding ended. Jones retired May 2026, now Professor Emeritus in Rancho Cordova, CA.

Kevin reached back in May 2026 with the pseudoSpore artifact and the blueFish pitch. Jones replied same day — twice within 24 hours — with technical resources and confirmed willingness to consult informally.

This is not a typical gen5 collaboration (PI + grant). It is an emeritus domain expert providing the product specification and validation rubric for blueFish through accumulated institutional knowledge.

---

## What Jones Gave Us

### Data Dump 1 — May 27, 2026

Three technical resources with domain insight:

**1. NIST Reference Data for Untargeted PFAS**
- URL: https://www.nist.gov/programs-projects/and-polyfluoroalkyl-substances-pfas/research/reference-data-and-tools/
- Purpose: Validation baseline for untargeted PFAS analysis
- blueFish action: Ingest NIST reference spectra, build untargeted validation suite

**2. EPA Method 1633A (Targeted Analysis of 40 PFAS)**
- URL: https://www.epa.gov/system/files/documents/2024-12/method-1633a-december-5-2024-508-compliant.pdf
- Jones's key insight: Most labs (including commercial) don't actually perform all QC checks — particularly **ion abundance ratios**. No published data exists to evaluate QC compliance beyond single-letter qualifiers in lab reports.
- LOQ reporting: State labs report measurements below LOQ as equal to LOQ (not "< LOQ") because they can't verify lower values. Jones personally corrected Grayling MI water reports.
- blueFish action: Implement full 1633A QC checks including ion abundance ratios. This is the gap commercial labs aren't filling.

**3. LC/MS File Conversion**
- Chromeleon Console exports to .mzML or .CDF
- Standard converter: Proteowizard msConvert (https://proteowizard.sourceforge.io/)
- blueFish action: Sovereign mzML/CDF ingestion pipeline

**Open-Source Tool Assessment:**

| Tool | Jones Assessment |
|------|-----------------|
| MZmine | "Failure rates I have found unacceptable" |
| MS-DIAL | Same |
| XCMS | Same |
| Progenesis QI | Good graphical evaluation, **now obsolete** |

The gap: No open-source tool gives acceptable failure rates AND graphical evaluation of feature detection / measurement quality. This is blueFish's target.

### Data Dump 2 — May 28, 2026

Additional technical detail and a new data source:

**1. MANA SODA Group (Metabolomics Cross-Validation)**
- URL: https://sites.google.com/metabolomicsna.org/soda/home
- Provides common datasets + multiple processing software for comparison
- Purpose: Data quality review via cross-tool comparison
- Jones: "most people don't want to go to that much effort"
- blueFish action: Use MANA SODA datasets as benchmark validation suite. This is the scientific challenge equivalent for analytical chemistry.

**2. MRM Architecture (how PFAS samples actually work)**
- Most PFAS analyses are targeted **MRM (Multiple Reaction Monitoring)**
- Single sample → **~100 chromatograms** (2 per analyte + internal standards)
- Each chromatogram: 1+ peaks integrated and reported
- Current lab workflow: Ehab exports into a "grand consolidated spreadsheet"
- Setup: "quite tedious compared to untargeted analyses"
- blueFish action: Template-driven MRM batch processing, automated peak integration across 100 chromatograms/sample

**3. Consulting Confirmed**
- Jones: "I would be glad to review"
- Caveat: "limited access to data sets and proprietary software these days"
- Best use: Architecture review, QC compliance validation, domain sanity checks
- Not a data source (retired, no lab access) — an expertise source

---

## blueFish Product Specification (from Jones data)

Jones didn't just give resources. He gave the product specification through accumulated domain knowledge:

| blueFish Feature | Source | Jones Evidence |
|-----------------|--------|----------------|
| Full EPA 1633A QC (including ion abundance ratios) | Data dump 1 | "Most labs don't actually perform all QC checks" |
| LOQ boundary handling | Data dump 1 | State labs report below-LOQ as equal to LOQ |
| Visual QC for feature detection | Data dump 1 | Progenesis QI was good at this but is now dead |
| Low failure rate peak detection | Data dump 1 | MZmine, MS-DIAL, XCMS all have "unacceptable failure rates" |
| Sovereign mzML ingestion | Data dump 1 | Chromeleon → msConvert → mzML is the standard path |
| NIST reference validation | Data dump 1 | Untargeted PFAS reference spectra as validation baseline |
| MANA SODA benchmarking | Data dump 2 | Cross-validation consortium datasets for quality review |
| Template-driven MRM batch processing | Data dump 2 | ~100 chromatograms/sample, tedious manual setup |
| Grand consolidated spreadsheet compatibility | Data dump 2 | Current output format (Ehab's workflow) |

### The Critical Path (from Jones domain expertise)

1. **EPA 1633A**: Parse for exact ion abundance ratio tolerances → implement as automated checks
2. **NIST reference data**: Ingest as validation baseline for untargeted analysis
3. **MANA SODA**: Acquire benchmark datasets → run through blueFish → compare against published tool results
4. **MRM batch architecture**: Template-driven, 100 chromatograms/sample, automated peak integration
5. **Visual QC**: petalTongue integration for peak evaluation — fill the Progenesis QI gap

---

## What Jones's Science Creates for the Ecosystem

### New Spring Validation Targets

Jones's data dumps don't just specify blueFish — they create new wetSpring Track 2 validation targets:

| Target | Source | Spring Check |
|--------|--------|-------------|
| EPA 1633A ion abundance ratio QC | Data dump 1 | Full method compliance checks |
| LOQ boundary validation | Data dump 1 | Below-LOQ detection and reporting accuracy |
| NIST reference spectra matching | Data dump 1 | Untargeted PFAS validation suite |
| MANA SODA cross-validation parity | Data dump 2 | Multi-tool benchmark comparison |
| MRM peak integration accuracy | Data dump 2 | 100-chromatogram batch processing |

These are validation targets the ecosystem could never have generated internally — they come from 30+ years of analytical chemistry domain expertise.

### New Public Data Systems

| System | Origin | Ingestion Status |
|--------|--------|-----------------|
| NIST PFAS Reference Data | Jones data dump 1 | Planned |
| EPA Method 1633A | Jones data dump 1 | Planned |
| MANA SODA Benchmark Datasets | Jones data dump 2 | Planned |

All three are cataloged in `gen5/foundations/PUBLIC_DATA_SYSTEMS.md`.

---

## The gen5 Pattern

Jones is a different kind of gen5 collaborator — not a PI with a grant, but an emeritus expert whose institutional knowledge becomes the product specification. The gen5 feedback loop still works:

```
Jones domain expertise (30+ years analytical chemistry)
    → Technical data dumps (NIST, EPA 1633A, MANA SODA, MRM architecture)
    → blueFish product specification
    → wetSpring Track 2 new validation targets
    → blueFish implementation (sovereign PFAS ETL)
    → Jones reviews architecture and QC compliance
    → blueFish available to any PFAS lab (AGPL-3.0)
    → Jones's domain knowledge becomes embodied in open tooling
```

The science Jones produced over decades feeds forward through blueFish. His retirement doesn't end the impact — it transforms it from institutional to sovereign.

---

## On-Campus Contacts

Jones is retired and remote (California). The lab continues:

| Contact | Role | Potential |
|---------|------|-----------|
| **Dr. Aswin Kumar Ilango** | New lab manager (replacing Jones as on-site lead) | Data source contact, MRM workflow details |
| **Cheryl Murphy** | Professor / PI, Fisheries & Wildlife | Lab supervisor, institutional connection |
| **Sima Kumar** | Research Assistant III, Murphy Lab | Peer contact, lab workflow insight |

---

## Cross-References

- `attsi/non-anon/contact/pfas/README.md` — full contact profile and intel log
- `attsi/non-anon/contact/pfas/email_spore_may2026.md` — initial outreach email
- `attsi/non-anon/contact/pfas/email_jones_reply_may2026.md` — first reply
- `attsi/non-anon/contact/pfas/email_jones_reply2_may2026.md` — second reply (MANA SODA, MRM)
- `gen4/products/BLUEFISH.md` — gen4 product document
- `gen5/foundations/PUBLIC_DATA_SYSTEMS.md` — data systems catalog
- `gen5/thesis/SCIENTIFIC_CHALLENGES.md` — MANA SODA as analytical chemistry benchmark

---

*Jones retired from the university. He didn't retire from the science. His 30 years of analytical chemistry expertise — what tools fail, what QC labs skip, where the data quality gaps are — is now the specification for an open tool that outlives any single institution. That's the gen5 pattern: domain knowledge becomes sovereign infrastructure.*
