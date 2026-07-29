# JOSS Publication Strategy — Gonzales NF Pipeline as Live System

**Date**: July 26, 2026 (Wave 151c)
**Parallel to**: `SHOW_HN_PUBLICATION.md` (community dissemination)
**Target journal**: Journal of Open Source Software (JOSS)
**Candidate**: Gonzales NF drug discovery pipeline — live system over sovereign infrastructure

---

## Why JOSS

JOSS publishes peer-reviewed software papers. A JOSS paper:
- Provides a citable DOI for the software
- Requires functioning code, documentation, tests, and a real use case
- Is indexed in academic databases (Crossref, ADS, Scopus via DOAJ)
- Feeds directly into grant applications (CTF NDU, NIH R01/R21)
- Establishes credibility that crates.io alone cannot

JOSS is complementary to Show HN. HN proves the community cares; JOSS proves
the academy accepts it. Together they cover both audiences the ecosystem serves.

---

## The Paper: A Live System, Not a Library

### What We Are NOT Submitting

A standalone crate paper (barraCuda, wetSpring). While these are valid JOSS
candidates individually, they miss the gen5 thesis: does someone else's science
come out the other end?

### What We ARE Submitting

A live drug discovery pipeline for neurofibromatosis data mining, running on
sovereign infrastructure, producing real preliminary data for an external PI.

The paper documents the system: how tideGlass (GPS platform rebuild) composes
with helixVision (genomics), healthSpring (MATRIX drug repurposing), initioChem
(conformational dynamics), and coralForge (structure prediction) — all running
over Tower Atomic transport with bearDog per-object encryption and Nest Atomic
CAS storage.

The NF package for Gonzales is a live system publication. It can be submitted
for grants and pre-pipeline funding, and built into the Fajgenbaum MATRIX and
QS Anderson frameworks as live isolations.

---

## JOSS Requirements Mapped to Ecosystem

| JOSS Requirement | Ecosystem Asset | Gap |
|-----------------|-----------------|-----|
| **Summary** (250-1000 words) | NF_CASE_STUDY.md + GONZALES_NF.md | Need: paper.md format |
| **Statement of need** | Pre-grant pipeline concept — zero-cost drug discovery | Need: formal articulation |
| **State of the field** | GPS legacy (Python 2, Fortran, 713 MB) vs sovereign rebuild | Exists in gps/README.md |
| **Functionality** | tideGlass 7 modules + 4-product composition | Need: tideGlass Phase 0+ |
| **Tests** | 782/782 Gonzales checks, 197 primalSpring scenarios, 14K+ total | Exists |
| **Documentation** | primals.eco, sporeprint.primals.eco | Need: tideglass.primals.eco |
| **Example usage** | NF Data Portal ingestion → MATRIX scoring → pseudoSpore | Need: one working example |
| **Community guidelines** | CONTRIBUTING.md, AGPL-3.0, Forgejo issues | Exists |
| **References** | baseCamp Paper 12, Fajgenbaum, Chen Cell 2026, Gonzales G1-G6 | Exists in bib |
| **Authors** | Kevin Mok + Andrea Gonzales (co-author, domain PI) | Need: ORCID confirmation |

---

## The Scientific Argument

### Statement of Need (draft)

Academic drug discovery labs face a computation gap: the tools exist (transcriptomic
reversal screening, pathway scoring, structure prediction) but the infrastructure
to compose them is fragmented across Python 2 codebases, cloud dependencies, and
vendor lock-in. A PI starting an NF data mining project must either:

1. Use legacy platforms (GPS: Python 2, Fortran, pinned deps, dying web portal)
2. Build ad-hoc pipelines with no provenance or reproducibility
3. Pay for commercial cloud compute that universities cannot sustain

The ecoPrimals ecosystem provides a third path: sovereign, composable, validated
infrastructure that an external PI can point at their scientific question and
produce self-verifying preliminary data at zero cost to the university.

### The Live System

tideGlass rebuilds the GPS platform (Chen Lab, Cell 2026) as a sovereign
pseudoSpore with seven modules:

| Module | Function | Spring Consumed |
|--------|----------|----------------|
| tideglass-rges | Reverse Gene Expression Score (drug→expression) | wetSpring |
| tideglass-rcl | Robust Collaborative Learning (noise cleaning) | neuralSpring |
| tideglass-gps4drug | Structure→expression prediction + virtual screening | neuralSpring |
| tideglass-screen | ZINC compound reversal screening | wetSpring |
| tideglass-molsearch | MCTS multi-objective lead optimization | neuralSpring |
| tideglass-octad | OCTAD parity validation | wetSpring |
| tideglass-nf | NF1 reversal screening (Gonzales bridge) | healthSpring |

Module 7 (tideglass-nf) is the novel contribution: screening NF Data Portal
transcriptomic signatures against compound libraries using GPS reversal scoring
augmented by Anderson tissue geometry (d_eff = 2.4 for nerve sheath) and
Fajgenbaum MATRIX pathway scoring.

### Anderson + Fajgenbaum as Live Isolations

The JOSS paper demonstrates two theoretical frameworks as running code:

**Anderson localization** (Philip Anderson, 1958; baseCamp Paper 01/12):
- Signal propagation through disordered media → cytokine propagation through tissue
- d_eff determines whether drug signal reaches target (3D dermis vs 2D epidermis)
- NF nerve sheath geometry (d_eff = 2.4) predicts MEK inhibitor reachability
- Live isolation: `Score = pathway_match × tissue_geometry × disorder_factor`

**Fajgenbaum MATRIX** (ARPA-H $48.3M pathway repurposing):
- Pathway scoring augmented by tissue reachability (Anderson geometry)
- Cross-species: dog AD (Gonzales G1-G6) → human NF (same signaling, different geometry)
- Live isolation: nS-605 Anderson-augmented MATRIX extension

**QS (Quorum Sensing)** as the biological null hypothesis:
- Anderson W_c ≈ 16.26 determines QS signal viability
- 3D tissue = QS active = drug signal propagates
- Applied to NF tumor microenvironment cytokine signaling

These are not theoretical claims — they are running as validated spring checks
(782/782 on Gonzales data, 329/329 neuralSpring, 94/94 airSpring).

---

## Infrastructure Section

The paper includes a section on the sovereign infrastructure that makes the
pipeline possible:

### Tower Atomic (transport)
- bearDog (crypto) + songBird (routing) + skunkBat (defense)
- 353x LAN latency vs WireGuard (0.45ms vs 158ms)
- 1.7x WAN throughput vs WireGuard
- Genetic enrollment with trust tiers
- 197 stress/pen test scenarios, all PASS

### Nest Atomic (data, pending)
- nestGate CAS: content-addressed storage for all pipeline outputs
- Provenance Trio: rhizoCrypt (DAG), loamSpine (ledger), sweetGrass (attribution)
- Per-object encryption via bearDog
- Self-verifying pseudoSpore artifacts

### Node Atomic (coordination, future)
- biomeOS orchestration of multi-product composition
- rootPulse replacing waterFall cascade for sovereign VCS
- Neural API capability-routed graph execution

---

## Dependencies and Timeline

### What Must Be Built (ordered)

1. **nestGate BTSP ClientHello** — unblocks Nest Atomic Phase 0 (flockGate, P1)
2. **tideGlass Phase 0** — reproduce GPS figures, validate against Zenodo source
3. **NF Data Portal ingestion** — first external data through the pipeline
4. **tideglass-nf module** — novel NF reversal screening
5. **One NF pseudoSpore** — minimum viable deliverable for JOSS "usage" section
6. **crates.io releases** — versioned artifacts for DOI citation path
7. **paper.md + paper.bib** — JOSS submission format

### What Already Exists

- 782/782 validated checks on Gonzales published data
- 197 primalSpring scenarios (Tower Atomic complete)
- Tower Atomic transport: 353x LAN, 1.7x WAN (LIVE)
- Provenance trio membranes: LIVE on cellMembrane VPS
- primals.eco: LIVE (evidence pages)
- 43/43 repos converged
- GPS source: Zenodo (Cell 2026 paper, 713 MB)
- NF Data Portal: public access via Synapse

### Timeline Estimate

| Phase | Work | Timeline |
|-------|------|----------|
| Nest Atomic Phase 0 | nestGate BTSP + CAS integration | Wave 151-152 |
| tideGlass Phase 0 | GPS archaeology + reproduction | Wave 152-153 |
| NF Data Ingestion | Synapse → nestGate CAS | Wave 153 |
| tideglass-nf | Novel NF screening module | Wave 153-154 |
| First pseudoSpore | NF preliminary data package | Wave 154 |
| Paper draft | paper.md + paper.bib | Wave 154-155 |
| JOSS submission | Review + revision cycle | Wave 155+ |

The JOSS paper is the end-goal motivator. Each wave of Atomic development
brings a concrete piece closer to submission.

---

## Grant Integration

The JOSS paper feeds directly into grant applications:

| Grant | How JOSS Helps |
|-------|---------------|
| CTF NDU ($125K) | JOSS acceptance = peer-reviewed computational infrastructure |
| NIH R01/R21 | JOSS paper cited as "Computational Methods" section |
| ARPA-H | Fajgenbaum MATRIX extension documented in peer-reviewed venue |

The pre-grant pipeline concept (zero cost to university, computational
preliminary data before a dollar is spent) becomes citable via JOSS DOI.

### 8 Grant Hypotheses (from LAB_ONBOARDING_PACKAGE.md)

The Gonzales collaboration has identified $5.775M in addressable funding
across NCI, NIGMS, NIAMS, NIDDK, and NIAID mechanisms. The JOSS paper
provides the computational credibility for all 8 hypotheses.

---

## Parallel Channels

| Channel | Audience | Relationship to JOSS |
|---------|----------|---------------------|
| crates.io | Rust ecosystem | "Install and verify" path; versioned releases for JOSS DOI |
| Show HN | Tech community | Broader story; JOSS = academic credibility anchor |
| primals.eco | Everyone | Permanent evidence record linked from JOSS paper |
| CTF NDU | NF community | JOSS paper as computational methods citation |
| NIH R01/R21 | Funding agencies | JOSS DOI in grant bibliography |
| Scientific Computing in Rust | Niche Rust community | Domain-specific outreach |

---

## Pre-Flight Rubric

Adapted from SHOW_HN_PUBLICATION.md for JOSS-specific requirements:

### Category 1: Evidence Integrity
- [ ] tideGlass Phase 0 complete (GPS figures reproduced)
- [ ] tideglass-nf produces NF screening results
- [ ] At least one NF pseudoSpore delivered and self-verified
- [ ] 782/782 Gonzales checks still passing
- [ ] All spring tests pass on clean checkout

### Category 2: Software Quality
- [ ] crates.io releases for all component primals
- [ ] CITATION.cff with Andrea as co-author
- [ ] cargo test --workspace passes on fresh clone
- [ ] Documentation at primals.eco covers NF pipeline
- [ ] tideglass.primals.eco live

### Category 3: Scientific Validity
- [ ] Anderson geometry applied to NF tissue (d_eff = 2.4)
- [ ] Fajgenbaum MATRIX scores for NF drug candidates
- [ ] GPS reversal screening validated against known NF therapeutics (selumetinib)
- [ ] Cross-species comparison: dog AD → human NF
- [ ] Andrea Gonzales confirms domain accuracy

### Category 4: Operational Readiness
- [ ] Tower Atomic transport operational (LIVE)
- [ ] Nest Atomic CAS storing pipeline outputs
- [ ] Provenance trio recording analysis lineage
- [ ] Pipeline reproducible on any enrolled gate

---

## Cross-References

- `gen5/thesis/SHOW_HN_PUBLICATION.md` — parallel community dissemination strategy
- `gen5/products/NF_CASE_STUDY.md` — product composition for NF
- `gen5/collaborators/GONZALES_NF.md` — collaboration status
- `attsi/non-anon/contact/gonzales/gps/` — GPS/tideGlass rebuild specs (7 files)
- `attsi/non-anon/contact/gonzales/onboarding/PRE_GRANT_PIPELINE.md` — zero-cost model
- `attsi/non-anon/contact/gonzales/onboarding/LAB_ONBOARDING_PACKAGE.md` — 8 grant hypotheses
- `gen3/baseCamp/12_immunological_anderson.md` — Fajgenbaum bridge paper
- `GEN_REVIEW_151c.md` — generational review that motivated this document

---

*JOSS is not the goal. The goal is Andrea's science shipping through sovereign
infrastructure. JOSS is the mechanism that makes that science citable, grantable,
and credible to the academy. The NF pipeline is a live system — the paper documents
a running thing, not a proposed thing.*
