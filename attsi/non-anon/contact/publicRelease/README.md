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
| `CAPABILITY_PARITY_BRIEF.md` | Technical evaluators, grant reviewers | Honest parity assessment across 8 domains: what we match, exceed, and lack vs proprietary tools. Rebuild instructions. |
| `FOR_FACULTY_AND_PIS.md` | Principal investigators, lab managers | What ecoPrimals actually replaces in a lab. Costs, speed benchmarks, gap analysis, infrastructure integration paths (Genomics Core, HTS, ICER, clinical trials). Faculty evaluation network. |
| `FOR_STUDENTS_AND_CORE_FACILITIES.md` | Graduate students, lab techs, core facility staff | 5-minute setup guide. Full 16S pipeline walkthrough. Common lab data formats. Student project ideas (real science). Troubleshooting. Hardware requirements. |
| `FOR_HARDWARE_BUILDERS_AND_HOBBYISTS.md` | Gamers, hardware hobbyists, r/homelab, distributed compute enthusiasts | The f64 Vulkan discovery. What your GPU actually does. Build topology (solo → household → mesh). Hardware acquisition strategy. NPU edge computing. Games@Home distributed compute. Comparison to mining/BOINC. |
| `FOR_COMPLIANCE_AND_INSTITUTIONAL_REVIEW.md` | Legal counsel, IRB, QA auditors, grant compliance, regulatory bodies | FDA 21 CFR Part 11 mapping. ISO 17025/15189 clause-by-clause. HIPAA Privacy/Security Rule alignment. GDPR data subject rights. IRB readiness. Licensing (AGPL-3.0). Dependency audit. Validation evidence summary. |

## Planned

| Document | Audience | Content |
|----------|----------|---------|
| `MSU_ASSET_ACCELERATION.md` | MSU faculty, ICER, Genomics Core | How MSU infrastructure plugs into validated pipelines |
| `GRANT_TECHNICAL_APPENDIX.md` | Grant reviewers (NIH, NSF, USDA, DOE) | Validation evidence organized by agency program |
| `KNOME_TEACHING_BRIEF.md` | Curriculum committees, MSDS faculty | K-Nome as pedagogy for real science pipelines |
| `DRUG_DISCOVERY_PIPELINE.md` | Gonzales lab, ADDRC, Drug Discovery Program | End-to-end iPSC → HTS → MATRIX → Anderson → validation |

## Guidelines

- **Sendable without context**: each document should be self-contained
- **Honest gaps**: always state what proprietary tools still do better
- **Verifiable claims**: every capability claim references a specific binary (`cargo run --bin validate_*`)
- **No internal strategy**: interview notes, email drafts, and contact logs stay in their respective directories
- **License**: documents here are CC-BY-SA-4.0; code references point to AGPL-3.0 repos
