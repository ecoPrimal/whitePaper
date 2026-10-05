# Individualized Legal Kinetics — Monte Carlo Case Simulation and the Per-Person Translation of Law

**Working title.** Inception tagline: *"The statute is the engine. The life is the data. The motion is the simulation result."*

**Parent framework:** K-NOME (constrained optimization methodology)
**Bridges:** healthSpring Paper 13 (NLME / per-person PK/PD) → guerillaGorilla (legal primal) → amicusContra (outward function)
**Scientific foundation:** Population PK/PD (NONMEM/Monolix equivalent), Monte Carlo patient simulation (healthSpring Exp001-087), Anderson-augmented MATRIX (Gonzales iPSC pipeline), NLME per-subject gradient computation
**Domain application:** Legal case construction as per-person pharmacokinetic modeling — identical mathematical framework, different substrate
**Live validation:** DaSean Mitchell — 26-108221-DC (Wayne County), F.A.M.E. motion filed Oct 5, 2026
**Wave:** 1 legal-primal → subGen generalization | **Date:** Oct 5, 2026

---

## THE BRIDGE

This is the third subGen concept to emerge from the legal primal, and
the most structurally revealing.

Institutional Localization (Paper 28 backward-flow) showed that the
physics of signal propagation through disordered media maps isomorphically
to oversight failure in captured institutions.

Information Refraction (PRISM) showed that signal routing in adversarial
communications follows the same optics as wavelength splitting.

Individualized Legal Kinetics shows that **per-person case construction
follows the same mathematics as per-person pharmacokinetic modeling.**
The bridge is not metaphor. It is structural isomorphism. The optimization
problems are identical. The constraint environment is identical. The
failure mode of population-level treatment is identical.

---

## THE PROBLEM — POPULATION-LEVEL LEGAL PRACTICE

### How Legal Aid Works (Population PK)

Traditional legal assistance treats every client as a member of a
population class:

```
Client presents with "custody dispute"
    → Retrieve template: "Custody Response Template"
    → Fill in blanks: names, dates, case number
    → Output: Generic motion that could be anyone's case
```

This is **population-level pharmacokinetics.** The drug (the statute)
is administered at a standard dose (the template) to every patient
(every client) in the population class (custody defendants). The dose
does not vary by patient weight, metabolism, comorbidities, or drug
interactions. It is the mean treatment for the mean patient.

Population PK works for the average patient. It fails the individual.

| Population PK failure | Legal template failure |
|---|---|
| Patient metabolizes faster than average → underdosed | Client's facts are stronger than the template captures → underargued |
| Patient has drug interaction → adverse event | Client's case intersects with parallel proceedings → procedural conflict |
| Patient has comorbidity → wrong drug entirely | Client's situation requires a different legal theory than the template assumes |
| Patient doesn't understand dosing instructions → noncompliance | Client doesn't understand the filing → can't testify to its contents |

The legal aid clinic gives DaSean a template motion. DaSean reads it. It
says "custody" and "best interest" and "Father requests." It could be
anyone's motion. DaSean cannot testify to its contents because it does
not contain HIS life. The words are legal. The person is absent.

### How healthSpring Paper 13 Solved This (Per-Person PK)

healthSpring's Monte Carlo patient simulator does not administer a
population-level dose. It models the INDIVIDUAL:

```
Patient substrate: {weight, age, genotype, metabolism, comorbidities,
                    concurrent medications, organ function, history}

Pharmacokinetic model: {absorption, distribution, metabolism, excretion}

Monte Carlo simulation: N=10,000 virtual patients with THIS patient's
                        parameters ± uncertainty

Output: Personalized dosing regimen optimized for THIS patient
```

The statute (drug) is the same. The procedure (route of administration)
is the same. The **individualization is in the content layer** — the
patient's specific substrate determines the output.

395 tests. 194 Python cross-validation checks. 6 WGSL compute shaders.
61 experiments. FOCE per-subject gradients. Population PK on GPU for
100K+ virtual patients. The math is validated.

---

## THE ISOMORPHISM — LEGAL KINETICS

### Three-Layer Architecture

What Kevin built for DaSean is the legal instantiation of the per-person
pharmacokinetic model:

```
PHARMACOKINETICS                    LEGAL KINETICS

Drug reference material             Education layer
(mechanism, interactions,           (ECE walkthrough — what the
 pharmacology, warnings)             law means in YOUR life)
         ↓                                    ↓
Patient-specific simulation         Instrument layer
(Monte Carlo with THIS              (FAME motion — YOUR facts
 patient's parameters)               mapped to the statutes)
         ↓                                    ↓
Dosing output                       Skeleton layer
(personalized prescription          (Proof of service, exhibit
 the patient can follow)             list, filing procedure)
```

| PK/PD Component | Legal Kinetics Component | DaSean Instantiation |
|---|---|---|
| **Drug** (the therapeutic agent) | **Statute** (the legal authority) | MCL 722.27(1)(c), MCR 3.210(C)(1), MCL 722.1003/1004 |
| **Patient substrate** (individual biology) | **Case substrate** (individual facts) | 9 years primary caretaker, AOP signed at hospital, ECE in both homes, Shayla's unilateral disruption |
| **Pharmacokinetic model** (ADME) | **Legal procedure** (filing, service, hearing, order) | E-file 3rdcc.org, serve email + mail, Referee Biggar hearing Oct 8, 56-day clock |
| **Monte Carlo simulation** (10K virtual patients with this patient's parameters) | **Case-specific analysis** (the motion built from this client's facts, tested against the statute) | "For nine years I was the stay-at-home father..." mapped to each MCL 722.23 factor |
| **Dosing output** (what the patient actually takes) | **Filing output** (what the client actually signs and submits) | FAME motion + Proof of Service + exhibit set |
| **Patient education** (why this drug, at this dose, for this condition) | **Client education** (why this statute, in this motion, for this hearing) | ECE walkthrough: "You signed a paper because you're the dad. Here's what the law calls that." |
| **Compliance** (patient understands and follows the regimen) | **Testimony** (client understands and can speak to the filing) | DaSean reads the walkthrough, reads the motion, recognizes his own life, signs it, can testify to every fact because they ARE his facts |

### The Compliance Insight

In PK/PD, the most common failure mode is **non-compliance** — the patient
doesn't take the medication correctly because they don't understand it.
The drug works. The patient fails. The system blames the patient.

In law, the equivalent failure mode is **the client who cannot testify to
their own filing.** The motion was correct. The law was right. But the
client didn't understand what they signed, couldn't explain it to the
referee, and the case collapsed — not because the law failed, but because
the translation was absent.

Population PK solves this by adding a patient education layer. Per-person
PK solves it by making the education SPECIFIC: "You are taking this dose
because YOUR weight and YOUR metabolism mean that the standard dose would
be [too much / too little]."

Legal kinetics solves it the same way. The ECE walkthrough doesn't teach
DaSean "custody law." It teaches DaSean: "This thing you already do —
feeding them breakfast, putting them to bed, being the one who was HOME —
the law has a name for that. The name is Established Custodial Environment.
You didn't learn it. You lived it. Now you know the word."

DaSean's compliance is perfect because the education is individualized.
He's not memorizing legal terms. He's recognizing his own life in a
new vocabulary. The simulation matches the patient. The dosing is correct.

---

## THE GENERALIZATION — amicusContra as Per-Person Legal PK Engine

### What amicusContra Builds For Each Case

amicusContra is not a legal aid clinic. It does not administer population-
level templates. It is the outward function of guerillaGorilla — and
guerillaGorilla was built on per-person kinetics from day one.

For each case amicusContra touches, the three-layer architecture produces:

**Layer 1 — Education (the drug reference for this patient)**
A document written FOR this person, in their language, explaining what the
law says about THEIR specific situation. Not a pamphlet. Not a FAQ. A
narrative that maps their life onto the statutory framework, so they
can SEE themselves in the law.

**Layer 2 — Instrument (the personalized dosing regimen)**
A motion, complaint, or filing built FROM this person's facts, citing
the specific statutes that apply to their specific situation, with
exhibits drawn from their specific evidence. The skeleton (formatting,
procedure, service requirements) is reusable. The content is unique
to the patient.

**Layer 3 — Skeleton (the route of administration)**
Filing procedures, proof of service templates, exhibit lists, hearing
preparation guides. These are reusable across cases because they are
procedural, not substantive. The skeleton is the syringe. The content
is the drug. The patient is the one who needs it.

### The Reusable Skeleton vs. the Unique Content

This is the key architectural insight that maps perfectly from PK/PD:

```
REUSABLE (the math)                   UNIQUE (the patient)
├── Statutes                          ├── The person's story
├── Case law                          ├── Their specific facts
├── Procedural rules                  ├── Their specific evidence
├── Filing formats                    ├── Their specific statutes that apply
├── Service requirements              ├── Their specific hearing dates
├── Exhibit formatting                ├── Their specific exhibits
└── Proof of service template         └── Their specific proof
```

A legal aid clinic gives everyone the left column. It works for the
average case. It fails the individual.

amicusContra gives the right column — individualized to the substrate —
while the left column runs in the background. The client never interacts
with the abstract law. They interact with their own story, told back to
them in legal language. The math is invisible. The person is visible.

**This is boutique representation at zero marginal cost.** The three-layer
architecture produces what APPEARS to be one-on-one legal counsel — because
the education is personalized, the motion is built from their facts, and
the client can testify to every word. But the COST is near-zero because:

1. The operator is pro se (no billing)
2. AI augmentation handles statute recall, drafting, cross-referencing
3. The skeleton is reusable
4. The evidence comes from public records (free)
5. The individualization — the expensive part, the part that makes it
   boutique — is a **translation operation**, not a research operation

The drug already exists (the statute). The patient already has the
condition (the legal problem). The PK model already works (the procedural
framework). The ONLY work is translating the patient's individual
substrate into the model's input parameters and generating the
personalized output.

That translation — from DaSean's nine years of fatherhood into
MCL 722.27(1)(c) — is what the Monte Carlo simulator does. It is
not law practice. It is **simulation of the individual case through
a validated legal-kinetic model.** The output is a filing. The
filing is signed by the person whose life it describes. The person
can testify to every word because every word IS their life.

---

## THE MATHEMATICS — FORMAL CORRESPONDENCE

### NLME and the Legal Individual

In Non-Linear Mixed Effects modeling (NLME — healthSpring's sovereign
NONMEM/Monolix equivalent):

```
y_ij = f(θ_i, x_ij) + ε_ij

where:
  y_ij  = observed outcome for individual i at time j
  θ_i   = individual parameters (θ_i = θ_pop + η_i)
  θ_pop = population-level parameters (the statute)
  η_i   = individual random effect (the person's specific deviation)
  x_ij  = covariates (the person's facts at time j)
  ε_ij  = residual error (uncertainty in evidence)
```

In legal kinetics:

```
y_ij = f(θ_i, x_ij) + ε_ij

where:
  y_ij  = legal outcome for case i at proceeding j
  θ_i   = case-specific legal parameters (θ_pop + η_i)
  θ_pop = statutory framework (MCL 722.27, MCR 3.210, etc.)
  η_i   = case-specific deviation (DaSean's facts differ from average)
  x_ij  = case covariates at proceeding j (evidence available, witnesses,
           prior rulings, referee assignment)
  ε_ij  = residual uncertainty (how the referee interprets the facts)
```

The FOCE (First-Order Conditional Estimation) algorithm in healthSpring
computes per-subject gradients — the derivative of the outcome with
respect to each individual's parameters. This is precisely what the
ECE walkthrough does: it computes the gradient of the legal outcome
with respect to DaSean's specific facts.

"If you can show 9 years of daily caretaking, the ECE factor shifts
this much in your favor." That is a per-subject gradient. It is
computed for DaSean, not for the average custody defendant. It is
the legal equivalent of: "Given your weight and metabolism, this
dose will produce this blood concentration at this time."

---

## CONNECTION TO THE GONZALES PIPELINE

The Gonzales iPSC validation pipeline (healthSpring Paper 12/13) is
the closest computational analog:

```
Anderson-augmented MATRIX score     →    Institutional Localization score
(drug-disease geometric match)           (oversight-capture network match)
         ↓                                          ↓
Gonzales iPSC validation            →    Live case validation
(bench confirmation of prediction)       (DaSean's hearing confirms the model)
         ↓                                          ↓
Per-patient PK/PD simulation        →    Per-case legal kinetics
(personalized dosing)                    (personalized motion)
         ↓                                          ↓
Clinical outcome                    →    Court outcome
```

The drug matrix scored drug-disease pairs using geometric distance in
Anderson transport space. The legal matrix scores statute-case pairs
using the same structural correspondence: which statutes have the
highest "affinity" for this case's specific substrate?

For DaSean: MCL 722.27(1)(c) (ECE) has the highest affinity because his
substrate — 9 years primary caretaker, AOP signed, both homes — is
the highest-concentration match for the ECE statutory model. The
"dose" (motion citing ECE) is optimized for his "pharmacokinetics"
(case-specific facts).

The iPSC validation step — where the computational prediction is
confirmed at the bench — is the hearing. The referee reads the motion.
DaSean testifies to the facts. The simulation matches the patient.
The drug works because the dosing was personalized.

---

## WHAT THIS MEANS FOR amicusContra

amicusContra is not a legal practice. It is a **per-person legal
pharmacokinetic engine.** The three-layer architecture (education +
instrument + skeleton) is the clinical delivery system. The
individualization is the simulation. The public record is the
drug library. The operator is the pharmacist — not the one who
invented the drug, but the one who translates the population-level
medicine into the per-patient dose.

And like the Monte Carlo patient simulator: the engine runs at
machine speed. 10,000 virtual patients in healthSpring. One real
patient — DaSean — reading a motion that describes his life in
legal language and recognizing every word.

The math ran in the background. The person sees only the output.
The output is their own story, told back to them, in the language
the court speaks. They sign it because it's true. They testify to
it because they lived it. The simulation matched the patient.

**This is what K-NOME means.** The constrained optimization methodology
does not belong to any domain. It bridges them. The same math that
models drug absorption in a specific patient models statute
application in a specific case. The optimization structure transfers.
The substrate changes. The architecture is domain-independent.

healthSpring was 395 tests. DaSean's motion is one filing.
The math is the same.

---

*subGen concept document. Wave 1.*
*Bridges to: healthSpring Paper 13, Gonzales iPSC pipeline, amicusContra,
guerillaGorilla three-layer case architecture*
*Part of the K-NOME / ecoPrimals / guerillaGorilla architecture.*
*Kevin Mok / ecoPrimal · attsi*
*October 5, 2026*
