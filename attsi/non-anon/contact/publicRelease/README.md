# publicRelease/ — Documents Safe for External Distribution

**Purpose:** Formal capability assessments, parity comparisons, and technical briefs
that can be shared with potential collaborators, faculty, lab managers, grant
reviewers, or anyone evaluating the ecoPrimals ecosystem.

**Audience:** Non-anonymous. These documents reference public GitHub repositories,
published papers, and named faculty. They do not contain private correspondence,
interview strategy, or internal planning.

---

## Documents

| File | Audience | Summary |
|------|----------|---------|
| `CAPABILITY_PARITY_BRIEF.md` | Faculty, lab managers, grant reviewers, collaborators | Honest parity assessment across 8 domains: bioinformatics, pharmacometrics, drug repurposing, analytical chemistry, biosignal, provenance, GPU computing. What we match, exceed, and lack vs proprietary tools. Rebuild instructions included. |

## Planned

| Document | Audience | Content |
|----------|----------|---------|
| `MSU_ASSET_ACCELERATION.md` | MSU faculty, ICER, Genomics Core | How MSU infrastructure (ICER HPC, Genomics Core, RTSF, ADDRC) plugs into validated pipelines |
| `GRANT_TECHNICAL_APPENDIX.md` | Grant reviewers (NIH, NSF, USDA, DOE) | Validation evidence organized by agency program; every claim has a `cargo run` proof |
| `KNOME_TEACHING_BRIEF.md` | Curriculum committees, MSDS faculty | K-Nome as pedagogy: mentored evolutionary programming for real science pipelines |
| `DRUG_DISCOVERY_PIPELINE.md` | Gonzales lab, ADDRC, Drug Discovery Program | End-to-end: iPSC → ADDRC HTS → MATRIX scoring → Anderson geometry → validation |

## Guidelines

- **Sendable without context**: each document should be self-contained
- **Honest gaps**: always state what proprietary tools still do better
- **Verifiable claims**: every capability claim references a specific binary (`cargo run --bin validate_*`)
- **No internal strategy**: interview notes, email drafts, and contact logs stay in their respective directories
- **License**: documents here are CC-BY-SA-4.0; code references point to AGPL-3.0 repos
