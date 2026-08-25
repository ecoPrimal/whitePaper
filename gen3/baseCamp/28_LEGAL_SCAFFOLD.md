# K-NOME Legal Scaffold — Reusable Template for Pro Se Case Construction

**Purpose:** Step-by-step framework for applying K-NOME methodology to any
new litigation. Fill in each section to produce a filing-ready case
architecture with the properties documented in Paper 28.

**Companion to:** `28_constrained_evolution_legal_case_construction.md`
**Template version:** 1.0 | August 2026

---

## Phase 0: Constraint Environment Identification

Before drafting anything, characterize the constraint environment. This is
the equivalent of identifying the Rust compiler version and target platform.

### 0.1 Jurisdiction

```
State:           _______________
Court:           _______________ Circuit / District / Municipal
Division:        _______________ (General Civil / Family / Small Claims / etc.)
Case type code:  _______________
Filing method:   [ ] E-file  [ ] In person only  [ ] Both
Filing fee:      $_______________
Payment methods: _______________
Hours:           _______________
```

### 0.2 Applicable Rules (the "compiler")

```
Court rules:     _______________ (e.g., MCR, FRCP, local rules)
Service rules:   _______________ (rule # for service method)
Response window: ___ days after service
Jury demand:     [ ] Must be in first pleading  [ ] Can be filed later
Default rules:   _______________ (rule # for default judgment)
```

### 0.3 Fee Structure

```
Filing fee:          $___
Jury demand fee:     $___
Service (per def):   $___
Total per defendant: $___
Total estimated:     $___
```

---

## Phase 1: Knowledge Space (K) — Domain Expertise Inventory

What do you know that no one else can tell the AI?

### 1.1 Factual Record

```
Duration of events:    _______________
Key dates:             _______________
                       _______________
                       _______________
Key locations:         _______________
                       _______________
Key people:            _______________
                       _______________
```

### 1.2 Evidence Inventory

| # | Evidence type | Description | Location | Admissibility notes |
|---|--------------|-------------|----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

### 1.3 Opposing Party's Self-Incriminating Statements

This is the highest-value evidence category. Anything the opponent has
already said — in court filings, texts, emails, social media, voicemail —
that admits or implies wrongdoing.

| # | Statement | Source | Date | What it admits |
|---|-----------|--------|------|---------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### 1.4 Witness Inventory

| # | Name | Relationship | What they observed | Willingness |
|---|------|-------------|-------------------|-------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## Phase 2: Numeric Space (N) — Legal Research Mapping

AI surveys the legal landscape. For each fact in the Knowledge space,
identify the legal framework that applies.

### 2.1 Cause of Action Identification

For each factual wrong, map to a specific statute or common law claim:

| # | Factual wrong | Statute / cause of action | Elements required | Evidence mapping |
|---|--------------|--------------------------|-------------------|-----------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

### 2.2 Element Type-Check

For each cause of action, verify all elements are satisfied (the "struct"):

```
Cause of Action #___: _______________
Statute: _______________

struct CauseOfAction {
    element_1: ___,  // evidence: _______________
    element_2: ___,  // evidence: _______________
    element_3: ___,  // evidence: _______________
    element_4: ___,  // evidence: _______________
}

All fields populated: [ ] YES  [ ] NO — missing: _______________
```

(Repeat for each count.)

### 2.3 Defendant Mapping

| # | Defendant | Causes of action | Specific exposure | Service address |
|---|-----------|-----------------|-------------------|----------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

### 2.4 Cross-Jurisdictional Opportunities

Can related proceedings in other courts create leverage?

```
Related case 1:  _______________
Court/Division:  _______________
How evidence flows:  Case A → Case B: _______________
                     Case B → Case A: _______________

Related case 2:  _______________
Court/Division:  _______________
How evidence flows:  _______________
```

---

## Phase 3: Drafting Cycles (O + M + E) — Evolutionary Construction

### 3.1 Generation 1: Initial Draft

AI generates candidate complaint based on Phase 1 (K) and Phase 2 (N).
Human reviews and begins mentoring cycle.

### 3.2 Mentoring Correction Log

Track every correction. This is the Lamarckian transmission record.

| Cycle | Human input | What changed | Files affected |
|-------|------------|-------------|---------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### 3.3 Validation Checks (Spring-Level)

Run after each drafting cycle:

- [ ] Every paragraph traces to specific evidence
- [ ] Every count cites specific statute with all elements met
- [ ] All dates verified against factual timeline
- [ ] All names, addresses, relationships verified against source
- [ ] No self-incriminating language in own filing
- [ ] Case type code present in caption
- [ ] Paragraph numbering sequential and consistent
- [ ] Internal cross-references (paragraph numbers) match
- [ ] Jury demand present (if desired)
- [ ] Service method compliant with applicable rules
- [ ] Prayer for relief matches counts (no orphaned requests)
- [ ] Verification/signature block correct

---

## Phase 4: Artifact Assembly (Garden-Level)

### 4.1 Filing Packet (→ Court)

```
[ ] Complaint (__ copies: 1 court + 1 per defendant + 1 self)
[ ] Exhibits (__ sets)
[ ] Summons forms (pre-filled, __ copies)
[ ] Filing fee ($____)
[ ] Case type code verified
```

### 4.2 Demand Packet (→ Defendants, pre-filing)

```
[ ] Calling card (00_CALLING_CARD.txt or custom)
[ ] Personalized insert (per-defendant)
[ ] Demand letter (per-defendant, 24hr ultimatum)
[ ] Unsigned complaint (preview)
[ ] Key exhibit (opponent's admission)
```

### 4.3 Service Packet (→ Defendants, post-filing)

```
[ ] File-stamped complaint with case number
[ ] File-stamped summons
[ ] All exhibits
[ ] Service method: _______________
[ ] Tracking numbers recorded
```

### 4.4 Discovery Packet (→ Post-answer)

```
[ ] Interrogatories (Set 1: __ questions)
[ ] Requests for production
[ ] Requests for admission
[ ] Subpoenas (if needed)
```

### 4.5 Supporting Case Packet (→ Related proceedings)

```
[ ] Evidence from Case A formatted for Case B
[ ] Cross-references to filings in both cases
[ ] Timeline document linking both proceedings
```

---

## Phase 5: Psychological Operations Layer

This layer operates between the mailbox and the courthouse. It is not a
legal filing — it is pressure applied through legally protected speech
(truth as absolute defense).

### 5.1 Calling Card

Universal insert. Same for every recipient. Establishes:
- Methodology (checklist of completed items)
- Credibility (precision, not emotion)
- Finality (one box unchecked: "File")

### 5.2 Personalized Inserts

Per-recipient. Hits the nerve specific to that person:
- For the enabler: "You were in the house"
- For the authority figure: "Where were you?"
- For the faith-based: Scripture quoted against their inaction
- For the professional: Career/pension exposure

### 5.3 Demand Letters

Per-defendant or per-family-member. Full narrative with:
- Complete cause of action summary
- Specific evidence cited
- 24-hour or 48-hour ultimatum
- Explicit next steps if ultimatum expires
- Tone: factual, relentless, not angry

### 5.4 Escalation Sequence

```
Step 1: Demand packet via certified mail (pre-filing)
Step 2: If no response → File complaint
Step 3: Service via certified mail, restricted delivery
Step 4: If no answer → Motion for default judgment
Step 5: If answer → Discovery (interrogatories, subpoenas)
Step 6: Cross-feed evidence to related proceedings
```

---

## Phase 6: Post-Filing Maintenance

### 6.1 Docket Monitoring

Track all filings, responses, and deadlines:

| Date | Event | Deadline | Status |
|------|-------|----------|--------|
| | Complaint filed | — | |
| | Service confirmed | +21 days for answer | |
| | Answer received / default | | |
| | Discovery served | | |
| | Discovery responses due | | |

### 6.2 Evidence Cross-Feed Log

Track evidence flowing between related cases:

| Source case | Document | Destination case | Filed as | Date |
|-----------|----------|-----------------|---------|------|
| | | | | |
| | | | | |

### 6.3 Correction Log (Ongoing)

Continue the mentoring correction log through the entire case lifecycle.

---

## Appendix: Constraint Environment Quick-Reference

### Michigan (MCR)

| Rule | Requirement |
|------|-------------|
| MCR 8.119(C) | Case type code on all new filings |
| MCR 2.111(B) | Numbered paragraphs, separate counts |
| MCR 2.105(A)(2) | Service: certified mail, restricted delivery |
| MCR 2.108(A) | 21-day response deadline |
| MCR 2.508 | Jury demand in first pleading |
| MCR 2.603 | Default judgment on non-response |
| MCR 2.302-2.313 | Discovery rules |
| MCR 2.116 | Summary disposition |

### Federal (FRCP) — placeholder

| Rule | Requirement |
|------|-------------|
| FRCP 8(a) | Short and plain statement |
| FRCP 4 | Service of process |
| FRCP 12(a) | 21-day response deadline |
| FRCP 38 | Jury demand within 14 days of last pleading |
| FRCP 55 | Default judgment |
| FRCP 26-37 | Discovery rules |

### Municipal / Code Enforcement — placeholder

| Rule | Requirement |
|------|-------------|
| Local ordinance # | _______________ |
| Appeal procedure | _______________ |
| Administrative hearing | _______________ |
| Judicial review | _______________ |
| Constitutional challenge | _______________ |

(Expand per jurisdiction as needed.)

---

## Appendix: Case Type Catalog (Michigan)

Common case type codes for new filings:

| Code | Type |
|------|------|
| CZ | General Civil |
| NO | Tort — Negligence, Other |
| PD | Personal Injury — Auto |
| CH | Equity — Injunction |
| AE | Administrative Appeal |
| DC | Domestic Relations — Custody |
| DM | Domestic Relations — Divorce |
| PP | Personal Protection Order |

---

*Template: K-NOME Legal Scaffold v1.0*
*baseCamp Paper 28 companion*
*Kevin Mok — ecoPrimals / primals.eco*
