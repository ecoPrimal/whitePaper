# publicRelease/ — Documents Safe for External Distribution

**Purpose:** Formal capability assessments, parity comparisons, and technical briefs
that can be shared with potential collaborators, faculty, lab managers, grant
reviewers, or anyone evaluating the ecoPrimals ecosystem.

**Audience:** Non-anonymous. These documents reference public GitHub repositories,
published papers, and named faculty. They do not contain private correspondence,
interview strategy, or internal planning.

**Last Updated:** March 19, 2026

---

## Current Documents

### Audience-Specific Briefs

| File | Audience | Summary |
|------|----------|---------|
| `CAPABILITY_PARITY_BRIEF.md` | Technical evaluators, grant reviewers | Honest parity assessment across 8 domains: what we match, exceed, and lack vs proprietary tools. Rebuild instructions. |
| `FOR_FACULTY_AND_PIS.md` | Principal investigators, lab managers | What ecoPrimals actually replaces in a lab. Costs, speed benchmarks, gap analysis, infrastructure integration paths. |
| `FOR_STUDENTS_AND_CORE_FACILITIES.md` | Graduate students, lab techs, core facility staff | 5-minute setup guide. Full 16S pipeline walkthrough. Common lab data formats. Student project ideas. |
| `FOR_HARDWARE_BUILDERS_AND_HOBBYISTS.md` | Gamers, hardware hobbyists, r/homelab, distributed compute | The f64 Vulkan discovery. What your GPU actually does. Build topology. Games@Home distributed compute. |
| `FOR_COMPLIANCE_AND_INSTITUTIONAL_REVIEW.md` | Legal counsel, IRB, QA auditors, grant compliance, regulatory | FDA 21 CFR Part 11, ISO 17025/15189, HIPAA, GDPR, IRB readiness, licensing. |
| `COLLABORATION_BRIEF.md` | Any MSU lab or PI | One-pager: free computation, what we analyze, what you get back, how to start. Designed for cold outreach to new collaborators. |

### Technical and Strategic Documents

| File | Audience | Summary |
|------|----------|---------|
| `DRUG_DISCOVERY_PIPELINE.md` | Gonzales lab, ADDRC, MSU Drug Discovery | End-to-end iPSC → HTS → MATRIX → Anderson → validation. Anderson-augmented MATRIX scoring (329/329 checks). Full pipeline architecture. |
| `MSU_ASSET_ACCELERATION.md` | MSU faculty, ICER, Genomics Core, ADDRC | How MSU infrastructure plugs into validated pipelines. Asset-by-asset mapping: Genomics Core, ICER HPC, ADDRC HTS, MSDS talent, lab compute mesh. |
| `GRANT_TECHNICAL_APPENDIX.md` | Grant reviewers — NIH, NSF, USDA, DOE, ARPA-H | Validation evidence organized by agency program. Every claim references a public binary that produces explicit PASS/FAIL output. |
| `KNOME_TEACHING_BRIEF.md` | Curriculum committees, MSDS faculty, DS/CS instructors | K-Nome as pedagogy for real science pipelines. What it is, what a course looks like, why it works. Evidence: 15,000+ checks, 10 months, one developer. |

---

## Guidelines

- **Sendable without context**: each document should be self-contained
- **Honest gaps**: always state what proprietary tools still do better
- **Verifiable claims**: every capability claim references a specific binary
  (`cargo run --bin validate_*` → exit 0 = pass)
- **No internal strategy**: interview notes, email drafts, and contact logs stay
  in their respective directories
- **License**: documents here are CC-BY-SA-4.0; code references point to AGPL-3.0 repos

---

## Toward a Standalone Published Whitepaper

This directory is the seed of a standalone published whitepaper repository.
The evolution path:

```
Phase 1 — NOW:
  publicRelease/ (this directory)
  ├── Audience-specific briefs (done)
  ├── Technical documents (done — 4 new docs this session)
  └── All content lives inside whitePaper (non-anonymous layer)

Phase 2 — NEXT:
  Bring baseCamp science papers into publicRelease/science/
  ├── Papers are the most public-safe content in gen3/
  ├── They reference only published science and public spring repos
  ├── Start with highest-impact: Paper 01 (Anderson QS), Paper 07 (WDM),
  │   Paper 12 (Immunological Anderson), Paper 17 (Game Science)
  └── Add methodology layer: constrained evolution formal paper

Phase 3 — RELEASE:
  publicRelease/ extracted to standalone repo
  ├── Own git history
  ├── Own LICENSE (CC-BY-SA-4.0)
  ├── Own README as published whitepaper index
  ├── GitHub Pages rendering (academic-style)
  └── DOI (Zenodo or equivalent) for citability
```

### What Goes In vs What Stays Private

| Content | Public (this dir) | Private (stays in whitePaper) |
|---------|:-----------------:|:-----------------------------:|
| baseCamp papers (22 science explorations) | ✓ (Phase 2) | |
| Constrained evolution methodology | ✓ (Phase 2) | |
| Ecosystem architecture | ✓ (Phase 2) | |
| Primal catalog | ✓ (Phase 2) | |
| Spring catalog | ✓ (Phase 2) | |
| Audience-specific briefs | ✓ (done) | |
| Grant/collab technical docs | ✓ (done) | |
| PhD thesis | | ✓ |
| atlasHugged essays | | ✓ (personal) |
| about/ (resume, transcript) | | ✓ (non-anon but personal) |
| data/ (faculty profiles, plans) | | ✓ (internal strategy) |
| Faculty outreach notes | | ✓ (private correspondence) |

### Science Papers to Import (Ordered by Priority)

**Round 1 — Foundation:**
1. `Paper 01` — Anderson Localization as QS Null Hypothesis (wetSpring, 3,100+ checks)
2. `CONSTRAINED_EVOLUTION_FORMAL.md` — The methodology paper
3. `ECOSYSTEM_ARCHITECTURE.md` — What the methodology produced
4. `Paper 07` — Sovereign WDM Simulation on Consumer GPU

**Round 2 — Breadth:**
5. `Paper 06` — Anderson as the Mechanism Behind No-Till Soil Health
6. `Paper 12` — Anderson in Immunological Signaling (DRUG_DISCOVERY_PIPELINE links here)
7. `Paper 17` — Game Design as Rigorous Science
8. `PRIMAL_CATALOG.md` + `SPRING_CATALOG.md`

**Round 3 — Full baseCamp:**
9. Papers 02–05, 08–11, 13–16, 18–22 (all 22 baseCamp papers)

---

## Quick Reference — All Spring Repositories

| Spring | Domain | Repository | Checks |
|--------|--------|-----------|:------:|
| wetSpring | Life science, microbiome, QS, field genomics | [syntheticChemistry/wetSpring](https://github.com/syntheticChemistry/wetSpring) | 5,707+ |
| airSpring | Precision agriculture, ET₀, soil, phenology | [syntheticChemistry/airSpring](https://github.com/syntheticChemistry/airSpring) | 3,123+ |
| neuralSpring | ML primitives, reservoir, spectral, surrogates | [syntheticChemistry/neuralSpring](https://github.com/syntheticChemistry/neuralSpring) | 4,500+ |
| hotSpring | Plasma physics, lattice QCD, GPU compute | [syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring) | 664+ |
| groundSpring | Uncertainty, noise, spectral theory | [syntheticChemistry/groundSpring](https://github.com/syntheticChemistry/groundSpring) | 535+ |
| healthSpring | Human health, PK/PD, microbiome, biosignal | [syntheticChemistry/healthSpring](https://github.com/syntheticChemistry/healthSpring) | 474+ |
| ludoSpring | Game science, HCI, provenance, distributed compute | [syntheticChemistry/ludoSpring](https://github.com/syntheticChemistry/ludoSpring) | 1,692+ |
| **Total** | | | **16,695+** |

Infrastructure (public):
- [ecoPrimals/toadStool](https://github.com/ecoPrimals/toadStool) — Compute orchestration
- [ecoPrimals/barraCuda](https://github.com/ecoPrimals/barraCuda) — WGSL math, 806 shaders
- [ecoPrimals/coralReef](https://github.com/ecoPrimals/coralReef) — Sovereign GPU compiler
