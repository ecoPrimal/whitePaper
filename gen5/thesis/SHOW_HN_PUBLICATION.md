# Show HN as Sovereign Publication — The Peer Review Event

**Date**: July 7, 2026
**Status**: Active — rubric established, pre-flight criteria defined
**License**: scyBorg triple — AGPL-3.0-or-later (code), ORC (system mechanics), CC-BY-SA 4.0 (this document)
**Lineage**: gen3/baseCamp (paper reproduction) → gen4/products (validated tools) → gen5 (external science) → **gen5/dissemination (this)**

---

## The Thesis

Traditional academic publication is gated: peer review by 2-3 anonymous reviewers, 6-18 month cycle, journal paywalls, citation politics. The ecosystem's methodology (constrained evolution, K-NOME, sovereign publication) already rejects those gates at the code level. The dissemination layer should reject them too.

Hacker News is peer review without the gate:
- **Open submission** — no institutional affiliation required
- **Real-time cross-examination** — domain experts in the thread within minutes
- **Public record** — the thread is permanent, searchable, citeable
- **Evidence-first** — working code > credentials; `cargo test` > impact factor
- **Falsifiable** — critics can clone the repo and disprove claims on the spot

The "paper" is primals.eco. The "defense" is the HN thread. The "citation" is an inbound email from someone who ran the tests themselves.

---

## Generational Context

| Gen | Publication Model | Audience | Artifact |
|-----|-------------------|----------|----------|
| gen3 | Reproduce papers → validate internally | Self, thesis committee | 12,510+ checks, catalogs |
| gen4 | Sovereign publication → guideStone, loamSpine, lithoSpore | Users, collaborators | Provenance-anchored artifacts |
| gen5 | **Peer review event → HN** | Engineers, domain scientists, the public | Thread + primals.eco + inbound |

gen3 proved internal validity. gen4 proved delivery. gen5 proves the work **survives public cross-examination by people with no reason to be kind**.

---

## Three-Channel Architecture

The HN post does not stand alone. It is one channel in a three-part dissemination model:

```
Channel         Voice       Purpose                         Format
-------         -----       -------                         ------
HN              ecoPrimal   Technical peer review event     Title + link + thread defense
Blog (TBD)      attsi       Philosophy, methodology, ethos  Long-form editorial series
primals.eco     neutral     Permanent evidence record       Static site (the "paper")
```

**Sequencing**: primals.eco must be complete FIRST (it is the link target). HN happens SECOND (the cross-examination). Blog happens THIRD (philosophical context, after technical credibility is established — "ecoPrimal has the receipts" is a link, not a claim).

**Cross-reference model**: HN links to primals.eco/lab/. Blog says "see the evidence at primals.eco." primals.eco links to neither — it IS the evidence, standalone, self-proving.

---

## The Rosalind Anti-Pattern

[Rosalind](https://news.ycombinator.com/item?id=48222600) — a Rust genomics toolkit posted to HN in 2026. Received attention, then was systematically dismantled:

| Criticism | Root Cause | ecoPrimals Counter |
|-----------|-----------|-------------------|
| "Tests don't check correctness, just no errors" | Shallow test suite | 14,314+ checks validated against published science at machine-epsilon |
| "70 single-author preprints = AI psychosis" | No external validation | Papers reproduced, not preprinted — matched against 70+ peer-reviewed results |
| "All code in one commit" | Dump, not development | 18 months commit history across 39 repos |
| "Useless toolkit-in-my-language repo" | No users, no composition | Live mesh, working JupyterHub, real collaborators producing science |
| "Vibe coding" | No methodology | K-NOME: human domain constraint + AI implementation + compiler verification + test validation |

The thread reveals HN's implicit rubric:
1. **Evidence of correctness** — validated against ground truth, not just "compiles"
2. **Sustained development** — commit history showing evolution, not a weekend project
3. **Honest limitations** — acknowledged gaps signal engineering maturity
4. **Specificity** — comparison to existing tools, not vague "better" claims
5. **Methodology** — "how did you know it's right?" must have a clear answer

---

## Rubric — Scored Pre-Flight Checklist

Each item is binary (PASS/FAIL). All must PASS before submission.

### Category 1: Evidence Integrity (the "paper")

| ID | Criterion | Measured By | Team |
|----|-----------|-------------|------|
| E-1 | primals.eco Lab section renders correctly and all links resolve | Manual site crawl + `zola check` | sporePrint |
| E-2 | At least one spring passes `cargo test` cold on a clean machine | Fresh VM or container `cargo test` from git clone | spring teams |
| E-3 | "Reproduce It Yourself" guide works end-to-end on stated prerequisites | Manual walkthrough on fresh system | primalSpring |
| E-4 | Test count claims match actual (`cargo test` output line counts) | Automated count vs. stated number | primalSpring |
| E-5 | Paper reproduction claims are individually verifiable (test name → paper citation) | Test naming convention audit | spring teams |
| E-6 | No broken CI badges on public repos | GitHub Actions status check | all teams |
| E-7 | Contact page live with ecoPrimal@pm.me | HTTP check | sporePrint |

### Category 2: Narrative Readiness (the "defense")

| ID | Criterion | Measured By | Team |
|----|-----------|-------------|------|
| N-1 | Title draft finalized (under 80 chars, passes HN title rules) | Manual review | overwatch |
| N-2 | First comment draft reviewed and timed (readable in <90 seconds) | Timed reading | overwatch |
| N-3 | "Is this AI slop?" response prepared (K-NOME framing) | Draft in this document | overwatch |
| N-4 | Comparison table drafted (vs. QIIME2, Nextflow, Snakemake) | Document exists in this file | overwatch |
| N-5 | Limitation statement is specific and honest (not false modesty) | Review by collaborator if possible | overwatch |
| N-6 | Response templates for top 5 predicted criticisms exist | Drafted in this document | overwatch |

### Category 3: Ecosystem Standards (internal readiness — the system must BE what we claim)

These are the ecosystem's own stadial/glacial criteria. We cannot claim "self-healing mesh" if the mesh isn't meshed. We cannot claim "14K checks" if tests fail. The system must be in the state we describe.

| ID | Criterion | Current State | Required for Submission |
|----|-----------|---------------|------------------------|
| S-1 | All 7 stadial criteria CLEAR | **CLEAR** (Wave 111 assessment) | Remain CLEAR |
| S-2 | LAN mesh operational (3+ gates) | **4-gate collective LIVE** (eastGate↔golgi↔ironGate+southGate) | Maintain 3+ |
| S-3 | WAN mesh operational (1+ remote gate) | **flockGate peered** via golgi relay | Maintain reachable |
| S-4 | Sovereignty S1-S4 graduated (inner membrane) | **ALL GRADUATED** (Jun 9) | No regression |
| S-5 | primalSpring 0 test failures | **1097 tests, 0 fail** (Wave 133c) | Maintain 0 fail |
| S-6 | pepti depot current (all ecobins match HEAD) | 30/30 present, **4 stale** (need rebuild) | All match HEAD |
| S-7 | External collaborator engaged (gen5 proof) | **Gonzales NF engaged** (producing) | At least 1 active |
| S-8 | `capability.call` works cross-gate | **Code READY**, deployment pending (WAN-DISPATCH-01) | Live demonstration |
| S-9 | Zero P1 blockers in GLACIAL_SHIFT_READINESS | **ZERO P1** (since Wave 145) | Maintain zero |
| S-10 | sporePrint (primals.eco) sovereign on inner membrane | **Pending** — still GitHub Pages (outer membrane) | Inner membrane LIVE |

**Philosophy**: We submit when the system IS what the post claims. Not aspirationally, not "almost" — the tests pass, the mesh meshes, the sovereignty is sovereign. A stranger who reads the HN post and clones the repo should find exactly what was described. Anything less is the Rosalind anti-pattern.

**Current gaps to close before submission**:
- S-6: Pepti rebuild for 4 changed primals (songBird, skunkBat, nestGate, coralReef, sweetGrass)
- S-8: WAN-DISPATCH-01 needs live validation after sporeGate redeploy
- S-10: sporePrint NUCLEUS deploy on golgi (handoff filed, not yet cut over)

### Category 4: Operational Readiness (the "logistics")

| ID | Criterion | Measured By | Team |
|----|-----------|-------------|------|
| O-1 | HN account exists with >100 karma (3+ months commenting history) | Account age + karma check | human |
| O-2 | 2-hour availability block confirmed for post-submission engagement | Calendar block | human |
| O-3 | Posting time selected (Sunday 7pm ET or Tuesday 7-10am ET) | Decision recorded | overwatch |
| O-4 | primals.eco can handle traffic spike (static site, CDN or no concern) | Architecture check (Zola = static, fine) | sporePrint |
| O-5 | GitHub repos can handle star influx (no private dependencies blocking clone) | Test clone from public URL | all teams |

---

## Title Candidates

Constraints: HN titles must be under 80 characters. No hype adjectives. No exclamation marks. Factual, specific, one differentiator.

| # | Title | Angle | Length |
|---|-------|-------|--------|
| 1 | Show HN: ecoPrimals – 14K checks in pure Rust, built by a microbiologist who can't read it | K-NOME surprise | 89 (OVER — trim) |
| 1a | Show HN: ecoPrimals – 14K science checks in Rust, by a microbiologist who can't read it | K-NOME surprise (trimmed) | 84 (trim more) |
| 1b | Show HN: 14K science checks in pure Rust, built by someone who can't read Rust | K-NOME (no brand) | 76 ✓ |
| 2 | Show HN: 70 papers reproduced in pure Rust on commodity hardware | Evidence | 58 ✓ |
| 2a | Show HN: 70 papers reproduced in Rust, zero C deps, runs on a basement i9 | Evidence + constraint | 73 ✓ |
| 3 | Show HN: ecoPrimals – sovereign bioinformatics, 13 services, 14K validated checks | Architecture | 76 ✓ |
| 4 | Show HN: I reproduced 70 papers in Rust without knowing Rust | Personal narrative | 60 ✓ |

**Recommended**: Title 4 — shortest, most personal, embeds the surprise, invites "how?" clicks. The brand name (ecoPrimals) appears in the link URL and first comment, not the title.

**Backup**: Title 2a — leads with evidence quantity if the personal angle feels risky.

---

## First Comment Draft

Post within 60 seconds of submission. Must be readable in under 90 seconds.

---

I'm a bench microbiologist (BSL2, fermentation, 16S pipelines) who got laid off and needed to keep doing science on hardware I own. Institutional HPC was priced out. Python pipelines were slow and black-box. I wanted sequencing workflows that run offline on a basement i9.

So I built 13 Rust services that compose into a self-healing scientific compute mesh. 14,314 validated checks across 8 domains. 70+ peer-reviewed papers reproduced at machine-epsilon precision (Python→Rust parity). Zero C dependencies. Zero unsafe blocks. Runs on commodity hardware.

The constraint: I don't know Rust. Every line was produced through AI conversation (K-NOME methodology) where I provide domain expertise and selective pressure, the AI handles implementation, and the compiler + test suite catch everything mechanical. The unfamiliarity is load-bearing — it forces every assertion through the test, because I can't eyeball correctness in the source.

Evidence: https://primals.eco/lab/ — live validation results with provenance chains. Each test maps to a specific published paper.

Honest limitation: the ecosystem is hardened for MY science (microbial ecology, LC-MS, drug repurposing, soil physics). External adoption means someone runs `cargo test` on a spring and decides if the reproducibility pattern fits their domain. I don't know if it generalizes until someone else tries.

Ask: bioinformaticians who want to validate that this transfers to their pipelines — what breaks? What's missing?

---

## Predicted Criticisms and Response Templates

### C-1: "This is AI slop / vibe coding"

> Not vibe coding — structured K-NOME methodology. I provide domain constraint (which published result to reproduce). The AI proposes implementation. The test suite validates against the published ground truth. If the test fails, the implementation is wrong regardless of how it reads. I don't need to read Rust — I need to define what "correct" means scientifically and verify the output matches.
>
> The distinction from vibe coding: vibe coding has no ground truth. This has 14,314 ground truths — each one a published scientific result that either matches or doesn't.

### C-2: "Another bioinformatics-toolkit-in-my-language"

> Not a toolkit — a composition mesh. 13 services that discover each other, negotiate capabilities, route computation, and produce provenance-chained results. The test counts aren't unit tests on a library — they're end-to-end validations: "does the pipeline reproduce what {paper} found, on real data?"
>
> The JupyterHub at lab.primals.eco runs real workloads on real NCBI data through the composition. It's not a library — it's deployed infrastructure.

### C-3: "How do you know the AI didn't introduce subtle errors?"

> Every check has a ground truth: a published result, a known constant, or a validated Python/R baseline. The workflow is: Python implementation → validated against paper → Rust implementation → validated against Python output at machine-epsilon. If the outputs diverge, the gap flows upstream.
>
> The test suite isn't "does it compile" — it's "does this DADA2 output match QIIME2's output on the same input data to 14 decimal places?"

### C-4: "Can I actually use this?"

> Yes. All springs are public, AGPL-3.0. `git clone https://github.com/syntheticChemistry/groundSpring && cargo test` works cold. The "Reproduce It Yourself" page on primals.eco has the walkthrough for the full composition.
>
> Honest caveat: the dependency graph across all 13 primals is complex. Individual springs (groundSpring, wetSpring) are the easiest entry point.

### C-5: "What's different from Nextflow/Snakemake/QIIME2?"

> [Link to comparison table — see next section]
>
> Short version: those are workflow managers (DAG execution on top of existing tools). ecoPrimals replaces the tools themselves — the algorithms are reimplemented in Rust and validated against the originals. The mesh handles discovery, routing, and provenance natively. No Python runtime, no conda environments, no Docker required.

---

## Comparison Table (for use in thread)

| | ecoPrimals | QIIME2 | Nextflow | Snakemake | Rosalind |
|---|---|---|---|---|---|
| **Language** | Pure Rust (zero C deps) | Python + plugins | Groovy/Java orchestrator | Python orchestrator | Rust (LLM-generated) |
| **What it IS** | 13-service compute mesh | Microbiome analysis framework | Workflow engine | Workflow engine | Genomics toolkit |
| **Algorithms** | Reimplemented + validated | Wraps existing tools (VSEARCH, MAFFT, etc.) | Wraps existing tools | Wraps existing tools | Reimplemented (unvalidated) |
| **Validation** | 14,314 checks vs. published papers | Plugin tests (variable quality) | Pipeline tests | Pipeline tests | ~20 tests (no correctness checks) |
| **Ground truth** | Python→Rust parity at machine-epsilon | Reference databases | Depends on wrapped tools | Depends on wrapped tools | None documented |
| **Dependencies** | 0 C, 0 unsafe, 0 conda | conda, ~200 Python packages | Java, Docker recommended | conda, Python | Minimal (but unproven) |
| **GPU** | Native WGSL (vendor-agnostic) | Via plugins (rare) | Via containers | Via wrappers | None |
| **Provenance** | BLAKE3 → DAG → ledger → ed25519 braid | QIIME2 provenance (metadata) | Tower/reports | Logging | None |
| **Hardware** | Runs on i9 basement node, no cloud | Cloud or local, conda required | Cloud-native (AWS Batch etc.) | Local or cluster | Local |
| **External adoption** | In progress (gen5 — first collaborator) | Thousands of labs worldwide | Thousands of pipelines | Thousands of pipelines | 0 known users |
| **Maturity** | 18 months, 39 repos, 13 services | 10+ years, massive community | 10+ years, Seqera-backed | 10+ years, academic standard | 6 months, abandoned |

**Positioning statement** (for thread use): "QIIME2 and Nextflow are battle-tested. I'm not claiming ecoPrimals replaces them today. The claim is: the science comes out the same (validated), with fewer dependencies, on hardware you own, with cryptographic provenance. If you trust QIIME2's output, you can verify ecoPrimals produces the same output — that's what the 14K checks do."

---

## Post-Mortem Template

Fill in after submission:

```
Date submitted:
Time (UTC):
Title used:
Link submitted:

--- 2-hour window ---
Peak position:
Final points (24h):
Comment count:
Stars gained (Day 1):
Stars gained (Day 7):

--- Inbound ---
Emails received (7d):
Quality emails (decision makers, researchers):
Collaboration offers:
Criticism themes:

--- Lessons ---
What worked:
What didn't:
Unexpected reactions:
What to change if re-posting:
Thread link:
```

---

## Actionable Evolution Targets (for all teams)

These are the concrete deliverables each team needs to produce. Organized by rubric category.

### sporePrint team (E-1, E-7, S-10)
- [ ] All Lab page internal links resolve (no 404s)
- [ ] Fix 5 stale `spring-catalog-status-science-and-evolution` URLs
- [ ] Fix 6 GitHub URLs pointing to wrong org (`ecoPrimals` → `syntheticChemistry`)
- [ ] `zola check` passes with 0 content errors (DOI timeouts acceptable)
- [ ] Contact page live and tested
- [ ] "Reproduce It Yourself" page reviewed for current Wave accuracy
- [ ] sporePrint NUCLEUS deployed on golgi inner membrane (S-10)

### Spring teams (E-2, E-5, E-6)
- [ ] `cargo test` passes from cold clone on fresh machine (no local-only dependencies)
- [ ] wetSpring: `nautilus` feature default OFF (or dep resolved to published crate)
- [ ] README includes: test count, paper count, how to run
- [ ] Test names follow pattern: `test_{paper_author}_{year}_{method}` (traceable to citation)
- [ ] CI badge green on GitHub (or badge removed if CI not configured)
- [ ] No path dependencies on private repos in published Cargo.toml

### primalSpring team (E-4, S-5)
- [ ] `registry_all_rust_tier_pass` green
- [ ] Scenario count matches claimed number
- [ ] `PRIMAL_GAPS.md` reflects current state (no stale entries)
- [ ] Test count in sporePrint matches actual `cargo test` output

### Gate teams (S-2, S-3, S-6, S-8)
- [ ] Pepti depot current — rebuild songBird, skunkBat, nestGate, coralReef, sweetGrass (S-6)
- [ ] sporeGate: redeploy songBird with drawbridge auto-advertisement
- [ ] flockGate: validate `capability.call("jupyter")` over WAN (S-8)
- [ ] Maintain 3+ LAN gates meshed (S-2)
- [ ] strandGate: SSH enrollment when physically accessible
- [ ] grapheneGate: redeploy 13/13 from fresh pepti

### Collaborator surface (S-7, gen5 proof)
- [ ] Gonzales NF: at least one delivered pseudoSpore or preliminary data artifact
- [ ] ABG: JupyterHub accessible and pipeline work demonstrable
- [ ] At minimum, one "producing" or "published" collaborator per gen5/collaborators/README.md

### overwatch (N-1 through N-6, O-1 through O-3)
- [ ] Title finalized
- [ ] First comment timed and revised
- [ ] Response templates reviewed
- [ ] Comparison table fact-checked against latest tool versions
- [ ] Posting date selected and calendar-blocked
- [ ] HN account karma buildup begun (authentic participation)

---

## Karma Buildup Protocol

HN penalizes new accounts and rewards established participants. The posting account needs:

- **Minimum**: 100 karma, 3+ months age
- **Recommended**: 500+ karma, 6+ months, visible comment history in Rust/bioinformatics threads
- **Method**: Authentic participation — comment on Rust posts, bioinformatics discussions, scientific computing threads. Not gaming; contributing. The comment history itself becomes evidence of domain expertise if anyone checks.
- **Threads to participate in**: Rosalind-style posts (engage with criticism constructively), Rust crate announcements, scientific computing discussions, AI-assisted development debates

---

## Timeline Model

```
NOW (Wave 133c)
  │
  ├── Create HN account (if not existing) ─────────────────┐
  │                                                          │ 3-6 months
  ├── Spring teams address E-2, E-5, E-6 gaps               │ karma buildup
  │                                                          │
  ├── sporePrint E-1, E-3, E-7 verification                 │
  │                                                          │
  ├── Comparison table fact-checked (N-4)                    │
  │                                                          │
  ├── First comment refined through read-aloud (N-2)        │
  │                                                          │
  └── SUBMISSION ───────────────────────────────────────────┘
       │
       ├── 2-hour active defense window
       │
       ├── Day 1: monitor stars, respond to stragglers
       │
       ├── Day 7: post-mortem, measure inbound
       │
       └── Blog (attsi) publishes with "receipts" link ──→ ongoing
```

The submission date is NOT fixed. It happens when ALL rubric items PASS. This prevents premature exposure. The karma buildup period (~3-6 months) provides natural pacing for the spring teams to reach full readiness.

---

## Readiness Audit — Current State (Wave 133c, Jul 7 2026)

### E-2: Cold `cargo test` from clone

| Spring | Public Repo | Cold Compile | Cold Test | Path Deps to Private | Verdict |
|--------|-------------|:------------:|:---------:|:--------------------:|---------|
| groundSpring | syntheticChemistry/groundSpring | PASS (16s) | PASS (189s total) | None | **READY** |
| wetSpring | syntheticChemistry/wetSpring | FAIL | — | `bingoCube/nautilus` (optional) | BLOCKED |
| hotSpring | syntheticChemistry/hotSpring | N/A (no root Cargo.toml) | — | Rust in `barracuda/` subdir | NOT STANDALONE |
| airSpring | syntheticChemistry/airSpring | N/A (no root Cargo.toml) | — | Rust in subdir | NOT STANDALONE |
| healthSpring | — | Not tested | — | — | UNKNOWN |
| primalSpring | ecoPrimals/primalSpring (private?) | PASS locally | PASS (1097 tests) | Many cross-deps | NOT PUBLIC STANDALONE |

**Recommendation**: Lead with groundSpring as the "try it yourself" spring. It compiles cold from a public clone, all tests pass, README is compelling, CI badge present. wetSpring is the flagship science but is blocked by an optional dep on a private primal.

**Action for spring teams**: wetSpring needs `nautilus` feature-gated behind a cargo feature flag that defaults to OFF for public consumption, or the dep path resolved to a published crate.

### E-1: sporePrint site health

- `zola build`: PASS (builds in 1.9s)
- `zola check`: Running (checks external links — may timeout on network)
- Contact page: LIVE at /contact/
- Lab section: 15+ notebook pages, reproduce guide, provenance docs
- Known gap: "Reproduce It Yourself" references `plasmidBin` (public) and `projectNUCLEUS/deploy/deploy.sh` — verify these repos are cloneable without auth

### E-6: CI badges

| Repo | Badge in README | Badge Status |
|------|:---------------:|:------------:|
| groundSpring | Yes (CI + Coverage + License + Rust + ecoBin) | Needs live verification |
| wetSpring | Likely yes (well-maintained README) | Needs live verification |

### O-5: Public clone test

- groundSpring: `git clone https://github.com/syntheticChemistry/groundSpring.git && cd groundSpring && cargo test` — **expected to work** (verified locally, no private deps)
- wetSpring: Will fail if `nautilus` feature is enabled by default
- plasmidBin: Public repo — binaries present but may be outdated post-pepti-first cleanup

---

## Cross-References

- `gen5/thesis/SCIENTIFIC_CHALLENGES.md` — gen5 credibility engine (challenges + HN are parallel surfaces)
- `gen4/thesis/THE_SOVEREIGN_PUBLICATION.md` — sovereign publication as conceptual ancestor
- `outreach/medium/split/README.md` — superseded two-voice Medium plan (ecoPrimal voice → HN)
- `outreach/medium/split/ecoPrimal/01_I_DONT_KNOW_RUST.md` — source material for first comment
- `outreach/medium/split/ecoPrimal/03_70_PAPERS_ONE_STACK.md` — source material for title/evidence framing
- `gen5/collaborators/README.md` — the "real users" evidence (counters "no adoption" criticism)
- `sporePrint/content/contact.md` — the inbound surface (success metric endpoint)
