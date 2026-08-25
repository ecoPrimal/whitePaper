# Constrained Evolution in Adversarial Legal Proceedings — K-NOME Applied to Pro Se Case Construction

**Author:** Kevin Mok (BS Microbiology, MSU 2018; MS Data Science, MSU 2025)
**Date:** August 2026
**Methodology:** K-NOME — Knowledge-Numeric Observed & Mentored Evolutionary Programming
**Infrastructure:** Cursor IDE, ecoPrimals sovereign mesh
**License:** AGPL-3.0-or-later
**Validation:** Live case — Michigan Circuit Court (General Civil + Family Division, two jurisdictions)

---

## Abstract

This paper documents the application of K-NOME (Knowledge-Numeric Observed &
Mentored Evolutionary Programming) to adversarial legal proceedings as a pro se
litigant. We demonstrate that the constrained evolution methodology — where
environmental constraints reshape the fitness landscape and drive specialization
— maps directly onto legal case construction when procedural rules, evidentiary
standards, and jurisdictional requirements serve as the constraint environment.

The result is a case architecture that exhibits properties absent from both
typical pro se filings (emotional, unstructured, procedurally deficient) and
typical attorney filings (formulaic, discovery-dependent, cost-optimized for
billable hours): evidentiary density from inception, cross-referenced internal
consistency, multi-jurisdiction strategic architecture, and self-verifying
artifact bundles that carry their own provenance chain.

We formalize the isomorphism between K-NOME's computational methodology and
legal reasoning, identify the structural parallels between ecoPrimals'
constrained evolution and the adversarial legal system, and present quantitative
evidence from a live case demonstrating the methodology's efficacy.

---

## 1. Introduction

### 1.1 The Gap in Legal Practice

Legal case construction occupies a space between two failure modes:

**Pro se failure mode.** Approximately 72% of civil litigants in American courts
are self-represented (NCSC 2022). The vast majority of pro se filings exhibit
characteristic deficiencies: emotional narratives substituting for legal
argument, absence of statutory citation, procedural non-compliance leading to
dismissal, and abandonment after the first adversarial response. The pro se
litigant typically possesses domain knowledge (they know what happened to them)
but lacks the methodological framework to convert that knowledge into legally
actionable artifacts.

**Attorney failure mode.** Competent attorneys produce procedurally correct but
formulaic filings optimized for a different fitness function: billable hours.
The standard civil complaint alleges minimum elements to survive a 12(b)(6)
motion to dismiss, defers evidentiary substance to discovery, and follows a
predictable choreography (file → answer → discovery → motion practice →
settlement negotiation → trial preparation → trial/settlement). This process
is effective but slow, expensive, and structurally incentivized to extend
rather than resolve.

Neither mode exploits what a constrained evolution methodology offers: rapid,
evidence-dense case construction where the procedural rules themselves serve
as selection pressure, producing filings that are specialized to survive in
the constraint environment from the moment of inception.

### 1.2 The K-NOME Hypothesis Applied to Law

The constrained evolution thesis (Mok 2026) argues:

> Environmental constraints do not merely accelerate convergence to a known
> solution. They reshape the fitness landscape so that systems specialize
> toward the constraint. Different lineages under the same constraint may find
> different solutions, but all become more fit for the constrained environment.

In computational biology, the constraint environment is the Rust type system:
the compiler rejects unsound variants before they reach expression, human
domain expertise provides selective pressure, and validation against published
literature defines the fitness function.

**Hypothesis:** If this methodology generalizes beyond computation, the same
pattern should operate in any constraint-rich, adversary-tested environment.
The adversarial legal system is such an environment:

| Biological | Computational (ecoPrimals) | Legal |
|------------|---------------------------|-------|
| Environment | Rust type system | Court rules (jurisdiction-specific) |
| Mutation | AI generates candidate code | Research generates candidate arguments |
| Selection (pre-expression) | Compiler rejects unsound code | Procedural rules reject non-compliant filings |
| Fitness test | Runtime tests + paper parity | Evidentiary sufficiency + judicial scrutiny |
| Environmental pressure | Developer provides direction | Case strategy provides selective direction |
| Genome | Compiled binary (ecoBin) | Filed complaint + exhibits |
| Generation time | Seconds (compile) | Days (drafting cycles) |
| Fastidious specialization | Code adapted to Rust + JSON-RPC | Filing adapted to court rules + jurisdiction |

---

## 2. Methodology: The Four Components in Legal Context

### 2.1 K — Knowledge Space

The Knowledge component represents irreducible domain expertise — the bench
scientist's understanding of what "correct" looks like in their field. AI
provides computational breadth but cannot substitute for the expert's ability
to evaluate whether a result is plausible.

**Legal mapping:** The Knowledge space is the factual record — years of lived
experience, documented communications, financial records, sworn statements,
and observable behavior. This is the domain expertise that no attorney, no AI,
and no procedural manual can replace.

In the validation case, the Knowledge space included:

- Multi-year cohabitation producing specific, dated observations
- Financial records documenting unreimbursed contributions
- Communications documenting relationships and contradictions
- Sworn court filings by the opposing party containing admissions
- Physical evidence (documents, benefit applications)
- Witness observations from third parties

### 2.2 N — Numeric Space

The Numeric component represents AI's cross-domain breadth — surveying large
parameter spaces, identifying structural patterns, generating candidates.

**Legal mapping:** Statute databases, case law, court rules, procedural
requirements, filing specifications, service methods, fee schedules. AI
surveys this space with breadth a pro se litigant cannot match:

- Cross-referencing statutes with procedural requirements
- Identifying causes of action the litigant did not know existed
  (e.g., felony eavesdropping with civil cause of action — identified from
  the opposing party's own sworn filing)
- Mapping evidentiary requirements per count to available evidence
- Computing filing fees, service costs, venue requirements
- Identifying cross-jurisdictional leverage opportunities

The intersection of K and N — the Knowledge-Numeric overlap — is where
legally cognizable claims emerge from raw facts. The litigant knows what
happened (K). The research identifies what legal framework applies (N). The
overlap produces actionable claims that are both factually grounded and
legally viable.

### 2.3 O — Observed

The Observed component is the human's felt mental model of the growing system,
developed through bidirectional feedback.

**Legal mapping:** The litigant's evolving understanding of the case
architecture. Each drafting cycle produces new insight:

- Reviewing the opposing party's filing reveals self-incriminating admissions
- Cross-referencing claims reveals structural dependencies
- Mapping the opponent's behavioral patterns reveals strategic opportunities
  (e.g., consistent use of intermediaries suggests avoidance behavior
  exploitable through multi-party pressure)

The Observed component separates K-NOME from automated legal drafting. The
human litigant watches the case evolve, develops intuition about structural
integrity, and redirects the next drafting cycle based on felt understanding.

### 2.4 M — Mentored

The Mentored component is the human providing selective pressure through
analogy, correction, taste, and redirection.

**Legal mapping:** The litigant mentors the AI through:

- **Factual correction** — correcting identity attributions, locations, dates
- **Chronological correction** — reordering events to match actual timeline
- **Strategic redirection** — adjusting tone, emphasis, or narrative approach
- **Precision calibration** — distinguishing ongoing relationships from
  one-time interactions
- **Domain knowledge injection** — providing facts only witnesses possess

Each mentoring correction reshapes the artifact. Unlike batch specifications
("write me a complaint about X"), mentored evolution produces filings that
reflect the litigant's actual knowledge, corrected iteratively, with each
cycle improving fidelity to the factual record.

### 2.5 E — Evolutionary

The Evolutionary component is the generate-compile-test-select cycle.

**Legal mapping:**

| Evolutionary step | Computational | Legal |
|-------------------|---------------|-------|
| **Generate** | AI writes candidate code | AI drafts candidate paragraphs, counts, arguments |
| **Compile** | Rust rejects type errors | Court rules reject non-compliant filings |
| **Test** | Runtime tests vs. published papers | Cross-reference claims against evidence, verify statutory elements |
| **Select** | Human evaluates fitness | Litigant accepts, modifies, or rejects based on domain knowledge |
| **Mutate** | AI revises based on feedback | Next drafting cycle incorporates corrections |

The Darwinian + Lamarckian dual mechanism operates:

- **Darwinian:** Procedural rules mechanically reject non-compliant filings.
  A complaint without a case type code is rejected at the clerk's window.
  Improper service fails. These are compiler-level rejections — blind,
  mechanical, non-negotiable.

- **Lamarckian:** The litigant's acquired understanding of the case transmits
  into the next drafting cycle. Observing that a sworn filing contains an
  admission of criminal conduct produces a new cause of action in the next
  generation. This inheritance of acquired traits accelerates convergence.

---

## 3. Architecture: The Legal Case as Composed System

### 3.1 The Primal/Spring/Garden Taxonomy Applied to Law

ecoPrimals organizes capabilities into three layers:

| Layer | ecoPrimals | Legal analog |
|-------|-----------|--------------|
| **Primals** (gen2) | Atomic capabilities | Atomic legal modules: complaint, exhibits, interrogatories, subpoenas, motions |
| **Springs** (gen3) | Validation environments | Case validation: cross-referencing modules against evidence, statutes, and rules |
| **Gardens** (gen4) | User-facing products | Deliverables: filed complaints, service packets, demand letters, settlement structures |

**Primals (atomic capabilities):**
- Complaint (multiple counts, multiple defendants, structured paragraphs)
- Exhibits (opposing party's sworn admissions)
- Interrogatories (staged for progressive disclosure)
- Demand letters (per-defendant psychological profiles)
- Status-report insert (universal "calling card")
- Filing checklist (procedural compliance verification)
- Case summary coversheet (judicial review document)

**Springs (validation environments):**
- Internal cross-reference: every paragraph traces to evidence
- Statutory compliance: every count cites specific statutes/rules
- Chronological consistency: every date verified against timeline
- Factual accuracy: every claim verified against source testimony

**Gardens (user-facing deliverables):**
- *Filing packet* → court
- *Demand packet* → certified mail to defendants
- *Discovery packet* → post-filing
- *Supporting case packet* → evidence for related proceedings

### 3.2 The Provenance Trio in Legal Context

| Provenance layer | ecoPrimals | Legal analog |
|------------------|-----------|--------------|
| **rhizoCrypt** (present) | Working DAG | Active case file — current drafts, pending filings |
| **loamSpine** (past) | Immutable history | Court docket — filed documents, timestamps, service records |
| **sweetGrass** (attribution) | Who did what, when | Evidence chain — document authorship, dates, conditions |

This is the fourth instantiation of the provenance pattern, after gaming
(Paper 20), scientific samples (Paper 21), and medical records (Paper 22):

```
Sample chain:    Collection → Transport → Lab → Analysis → Report
Medical chain:   Intake → Treatment → Record → Consent → Disclosure
Legal chain:     Event → Documentation → Filing → Service → Discovery
```

All share the same structural requirement: verifiable attribution at every
step, immutable record of what was committed, transparent working state of
what is pending.

### 3.3 Content-Addressed Convergence

When two independent analyses of the same evidence reach the same legal
conclusion, that conclusion is convergent — not because one copied the other,
but because the evidence constrains the analysis to the same result.

In the validation case, the plaintiff identified a criminal admission in
the defendant's sworn filing. Any attorney reviewing the same filing would
reach the same conclusion. Truth is content-addressed, not credential-addressed.

---

## 4. The Constraint Environment: Court Rules as Compiler

### 4.1 Procedural Rules as Pre-Expression Selection

Court rules function as the Rust compiler — they mechanically reject
non-compliant filings before they reach judicial evaluation:

| Rule category | Constraint | Compiler analog |
|---------------|-----------|-----------------|
| Case type code | Required on all new filings | Type annotation required |
| Paragraph numbering | Numbered paragraphs, separate counts | Struct definition |
| Service method | Specific delivery requirements | Protocol compliance |
| Response deadline | Fixed window after service | Timeout constraint |
| Jury demand | Must appear in first pleading | Feature flag at initialization |
| Default judgment | Automatic on non-response | Panic on unhandled error |

A complaint failing any constraint is rejected at the clerk's window — the
legal equivalent of a compile error. It never reaches the judge (runtime).

### 4.2 Statutory Elements as Type System

Each cause of action has elements that must be established:

```
struct Eavesdropping {
    private_conversation: bool,
    willful_interception: bool,
    without_consent: bool,
    electronic_device: bool,
}
```

If any field is missing, the claim does not compile. In the validation case,
all four fields were populated by the defendant's own sworn filing — the
opposing party wrote the struct and populated every field herself.

Composition follows the same pattern as ecoPrimals' primal composition:

```
struct CivilEavesdroppingAction {
    eavesdropping: Eavesdropping,  // composed from above
    actual_damages: Option<f64>,
    punitive_damages: Option<f64>,
    equitable_relief: bool,
}
```

### 4.3 Evidentiary Sufficiency as Paper Parity

| ecoPrimals validation | Legal validation |
|----------------------|------------------|
| Paper parity (matches published result within tolerance) | Evidentiary sufficiency (supported by admissible evidence) |
| Named tolerances (±0.05, ±1σ) | Burden of proof (preponderance, clear and convincing) |
| PASS/FAIL/SKIP | Sustained/Overruled/Moot |
| Source: peer-reviewed literature | Source: statute, case law, rules of evidence |

---

## 5. Cross-Jurisdictional Architecture: Composition Without Central Orchestrator

The validation case deployed a two-case architecture across independent
jurisdictions:

```
┌─────────────────────────────┐    ┌─────────────────────────────┐
│  COUNTY A (Civil)           │    │  COUNTY B (Family)          │
│  Plaintiff v. Defendants    │    │  Related party proceeding   │
│  General Civil Division     │    │  Family Division            │
│                             │    │                             │
│  5 counts, 4 defendants     │◄──►│  Best Interest Factors      │
│  Jury trial demanded        │    │                             │
│                             │    │                             │
│  Evidence produced HERE ────┼───►│  becomes exhibits THERE     │
│                             │    │                             │
│  Admissions ◄───────────────┼────┤  originated HERE            │
└─────────────────────────────┘    └─────────────────────────────┘
```

The cases are legally independent — different parties, different courts,
different counties, different judges, different divisions. Neither court
can dismiss the other's case. But evidence flows bidirectionally. The
defendant cannot defend one without exposing herself in the other.

This is the legal equivalent of cross-spring composition: springs operate
independently, but validated results in one become inputs to another.

**Settlement as convergence:** The two-case architecture creates a
convergence point that neither case alone could produce. The civil plaintiff
controls dismissal. Settlement terms involve outcomes in the related
proceeding. This is constrained optimization: the only solution minimizing
total cost is global resolution.

---

## 6. Self-Verifying Legal Artifacts

### 6.1 The Filing Packet as pseudoSpore

| pseudoSpore component | Legal filing packet component |
|----------------------|------------------------------|
| Source code | Complaint text (structured paragraphs, numbered counts) |
| Data | Exhibits (defendant's sworn admission) |
| Validation script | Internal cross-references (paragraph → exhibit → statute) |
| Provenance | Chain of custody (sworn verification, service records) |
| BLAKE3 hash | File stamp (clerk's date-stamped copy with case number) |

A judge can validate every claim by following internal references. The
artifact carries its own proof.

### 6.2 The Demand Packet as Composed Garden

```
Envelope contents (stack order):
1. Calling card          — universal status report (methodology proof)
2. Personalized insert   — recipient-specific (psychological calibration)
3. Demand letter         — full case narrative (24-hour ultimatum)
4. Unsigned complaint    — preview of filing (all counts, all defendants)
5. Exhibit + cover page  — defendant's own admission (self-incriminating)
```

Each component is independently authored (primal-level). The composition
creates emergent impact that no single component achieves alone.

### 6.3 The Calling Card as guideStone

```
[x]  The facts — documented
[x]  The evidence — preserved
[x]  The timeline — reconstructed
[x]  The contradictions — cataloged
[x]  The sworn statements — cross-referenced
[x]  The complaint — drafted, reviewed, final
[x]  The exhibits — assembled
[x]  The jury trial — demanded
[x]  The courthouse — identified
[x]  The filing fee — ready
[x]  Your name — on the caption
[x]  Your address — confirmed

[ ]  File.
```

Every checked item is verifiable. The artifact is self-proving. The sign-off
— "Scientist. Not attorney. Which should terrify you more." — encodes the
guideStone's implicit claim: this was produced by someone whose methodology
is verification, not persuasion.

---

## 7. Quantitative Results: Methodology vs. Baselines

### 7.1 Pro Se Baseline

| Metric | Typical pro se | K-NOME pro se |
|--------|---------------|---------------|
| Causes of action identified | 1-2 (emotional, often wrong) | 5 (statutorily grounded, cross-referenced) |
| Exhibits at filing | 0 | 1+ (defendant's own admission) |
| Internal cross-references | None | Every paragraph → exhibit → statute |
| Procedural compliance | ~30% (NCSC estimate) | 100% |
| Survival of motion to dismiss | ~15% | Designed to survive (evidentiary density from filing) |
| Cost to plaintiff | Variable | Filing fee + certified mail (~$300) |
| Strategic architecture | Single case, single defendant | Multi-case, multi-jurisdiction, multiple defendants |

### 7.2 Attorney Baseline

| Metric | Typical attorney filing | K-NOME pro se |
|--------|----------------------|---------------|
| Time to file | 2-4 weeks | Days (iterative K-NOME cycles) |
| Evidence at filing | Minimal (deferred to discovery) | Defendant's own admission attached |
| Cost to plaintiff | $3,000-$10,000 retainer | ~$300 |
| Cross-case architecture | Rare | Built-in by design |
| Settlement leverage | Financial (cost of defense) | Financial + evidentiary + jurisdictional + psychological |

### 7.3 Opponent Filing Comparison

| Metric | Opponent (standard pro se) | K-NOME pro se |
|--------|--------------------------|--------------------------|
| Filing length | 192 pages | ~15 pages |
| Self-incriminating admissions | Yes (criminal confession) | Zero |
| Evidence management | Volunteered evidence against self | Evidence assembled for specific claims |
| Strategic awareness | Filed in home county | Filed in jurisdiction maximizing opponent burden |
| Discovery discipline | Pre-disclosed before discovery | Attached only evidence strengthening own claims |

---

## 8. Cross-Domain Structural Similarity

Papers 20-22 demonstrated that fraud detection, chain-of-custody, and
consent-scoping architectures share >80% structural similarity across
gaming, science, and medical domains. The legal application is a fourth
instantiation:

| Structure | Gaming (P20) | Science (P21) | Medical (P22) | Legal (P28) |
|-----------|-------------|---------------|---------------|-------------|
| Provenance | Item → trades → ownership | Sample → transport → analysis | Intake → treatment → record | Event → documentation → filing |
| Fraud types | Duplication, value manipulation | Contamination, mislabeling | Identity theft, consent violation | Perjury, eavesdropping, identity exploitation |
| Attribution | Creator → modifier → owner | Collector → analyst → publisher | Patient → provider → researcher | Plaintiff → defendant → court |
| Verification | Hash chain | BLAKE3 + Ed25519 | Consent certificate | Sworn verification + file stamp |
| Self-proving | Replay transaction log | Run pseudoSpore | Check consent chain | Follow paragraph → exhibit → statute |

All four domains require immutable records, verifiable attribution,
self-proving artifacts, operate in adversarial environments, and resolve
disputes through evidence rather than authority.

---

## 9. Limitations and Fastidious Specialization

### 9.1 Domain Expertise Requirement

K-NOME requires irreducible domain knowledge. The methodology cannot
substitute for facts it does not have. In the validation case, nine
mentoring corrections were required — each providing facts only the
human participant possessed (locations, dates, relationship nuances,
identity attributions).

### 9.2 Fastidious Specialization Risk

A filing perfectly adapted to one jurisdiction's rules may not survive in
another. The methodology transfers, but the constraint environment must be
re-characterized for each new jurisdiction.

### 9.3 Adversarial Counter-Evolution

Unlike scientific validation (where nature does not strategize), legal
adversaries adapt. K-NOME does not guarantee victory — it guarantees that
the initial filing is maximally fit for the constraint environment, forcing
the adversary to expend resources on defense rather than offense.

---

## 10. Conclusion

The adversarial legal system — with its procedural constraints, evidentiary
standards, and adversary-tested arguments — is a natural constraint
environment that produces the same evolutionary dynamics observed in
Rust-compiled scientific code, biological adaptation under environmental
pressure, and provenance-governed digital systems.

The methodology produced a legal filing architecture with properties absent
from both typical pro se and typical attorney work:

1. **Evidentiary density from inception**
2. **Cross-referenced internal consistency**
3. **Multi-jurisdiction strategic architecture**
4. **Self-verifying artifact bundles**
5. **Zero marginal cost**

The constrained evolution thesis holds across its fourth domain: environmental
constraints reshape the fitness landscape so that systems specialize toward
the constraint. In law, as in biology, as in computation — the constraint
is not the obstacle. The constraint is the teacher.

---

## Appendix: Mentoring Correction Log (Anonymized)

| Cycle | Correction Type | What Changed |
|-------|----------------|--------------|
| 1 | Identity attribution | Corrected which party was described by which label |
| 2 | Frequency of interaction | Changed "ongoing" to "single visit" for a witness |
| 3 | Terminology precision | Replaced broad term with specific, accurate description |
| 4 | Party count | Corrected "three defendants" to "all defendants" |
| 5 | Chronological order | Restructured event sequence to match actual timeline |
| 6 | Location | Corrected service location across 4 documents |
| 7 | Claim precision | Softened unverifiable duration claim |
| 8 | Temporal reference | Replaced relative date with absolute date |
| 9 | Timeline accuracy | Corrected party's location during key event |

Each correction demonstrates the Lamarckian transmission mechanism:
human-acquired knowledge transmitting into the next generation of the
artifact. Fidelity to truth increases monotonically with each cycle.

---

*Kevin Mok — ecoPrimals / primals.eco*
*K-NOME: Knowledge-Numeric Observed & Mentored Evolutionary Programming*
*baseCamp Paper 28*
