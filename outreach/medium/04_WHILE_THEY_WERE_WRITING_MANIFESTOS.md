# While They Were Writing Manifestos

*A structural comparison between a 320-page thesis on civilization and a working system in a basement*

**By**: attsi | ecoPrimal
**Status**: Draft — evolving document
**Published**: [pending]

---

In April 2026, Palantir Technologies — a $70 billion defense contractor whose
primary products are surveillance platforms for military and intelligence
agencies — published a 22-point summary of a book called *The Technological
Republic: Hard Power, Soft Belief, and the Future of the West.*

It declares that Silicon Valley has a "moral debt" to the nation. That
technology must serve "national purpose." That hard power "will be built on
software." That "national service should be a universal duty." That pluralism
has become "hollow." That the restraints placed on Germany and Japan after
the deadliest war in human history "must be undone."

The document was called a manifesto. Critics called it techno-fascist. Both
descriptions miss the more interesting observation, which is structural:

A company that sells targeting software to militaries published a philosophy
of civilization. During the same period, a bench scientist in a basement was
building one.

This is not a rebuttal. Rebuttals dignify the thing they respond to. This is
a juxtaposition. Two approaches to the same question — "what should
technology be for?" — running in parallel, producing different artifacts.

---

## While they were writing about moral debt

We deployed a JupyterHub where graduate students and independent researchers
run provenance-backed science for free.

The system has four access tiers, modeled on scientific peer review rather
than military clearance. The compute tier gives researchers full kernel
access, GPU dispatch, and a private workspace. The reviewer tier gives
dashboard access with no code execution — read the methods, interact with the
pipeline, evaluate the results. The observer tier shows attributed outputs
and provenance chains.

Every tier's restrictions are enforced by the operating system, not by
policy documents. Filesystem permissions. Kernel blocking. Network isolation.
Process hiding. If it matters, it is enforced by a mechanism, not by an
honor code.

The cost to users is zero. The cost to us is electricity.

The Technological Republic argues that Silicon Valley owes a debt. We think
the debt framing is structurally backwards. Debt implies obligation to
a creditor. The question is who the creditor is. If the creditor is the state
and the currency is weapons software, you get Palantir. If the creditor is
the commons and the currency is reproducible science, you get this.

---

## While they were arguing for AI weapons

We built AI-assisted development where the AI writes science tools, not
targeting systems.

The methodology is called K-NOME: the human provides direction, domain
knowledge, and quality judgment. The AI provides implementation. The compiler
provides environmental constraint. What emerges is shaped by all three — the
human cannot write the code, the AI cannot evaluate the science, the compiler
cannot be negotiated with. The conversation is the development environment.

This produced 14 composable services, 8 scientific validation frameworks,
27,000+ tests, and 70+ published papers reproduced from scratch. The AI
wrote every line. The human evaluated every result. The compiler rejected
everything that wasn't mechanically sound.

Palantir's thesis is that AI should serve "democratic power" and "strategic
deterrence." Their products help militaries identify targets. Our AI
identifies whether a lattice QCD computation reproduces a published result
within error bars. Both are "AI serving purpose." The purposes are not
equivalent.

---

## While they declared some cultures regressive

We built a system where a microbiologist, a physicist, a pharmacologist, and
a Discord bioinformatics community all contribute through the same attributed
pipeline.

The provenance system does not record nationality, institutional affiliation,
or cultural identity. It records: what data went in, what computation ran,
what result came out, who contributed, when it happened. The attribution is
cryptographic — Ed25519-signed, BLAKE3 content-addressed, DAG-tracked,
ledger-committed. It cannot be edited after the fact. It cannot be revoked.

If a researcher in Lagos reproduces a plasma physics result that was first
validated in a Michigan basement, the provenance chain records both
contributions with equal cryptographic weight. The attribution is structural.
It does not require a committee to adjudicate credit. The math handles it.

The Technological Republic speaks of "Western civilization" as the entity
that must be defended. Our system does not have a concept of civilization.
It has a concept of contribution. The two are not the same thing.

---

## While they called pluralism hollow

We built radiating attribution where every contribution compounds regardless
of who you are.

The attribution system (sweetGrass) uses a braid structure. When you
contribute — data, computation, review, a bug report, a reproduction of a
published result on different hardware — your contribution is woven into the
braid with cryptographic permanence. Every subsequent computation that
depends on your contribution carries your attribution forward. The braid
grows. The attribution radiates.

This is not a meritocracy in the libertarian sense — it does not claim that
outcomes reflect inherent worth. It is a provenance chain that records
what happened. If your contribution improved the system, that fact is
cryptographically permanent. If it didn't, that fact is equally permanent.
The system is agnostic about everything except verifiable history.

Pluralism is hollow when it is a declaration with no mechanism. "We value
diverse perspectives" is hollow when the attribution system gives credit to
the PI and erases the grad student, the technician, the collaborator who
provided the dataset, the reviewer who caught the error.

Pluralism backed by cryptographic attribution is not hollow. It is
structural. The braid does not forget.

---

## While they proposed reinstating the draft

We built volunteer infrastructure.

One person pays the electricity. Researchers contribute because the science
is interesting and the tools work. The attribution pipeline exists so that
when value eventually flows through the system, the people who built it and
used it receive credit proportional to their contribution — not proportional
to their proximity to power.

There is no coercion in this model. There is no debt. There is no
obligation framed as service. There is compute, offered freely, used
voluntarily, attributed permanently.

The Technological Republic frames national service as duty. Duty to whom is
the structural question they decline to answer precisely. Duty to "the
nation" is an abstraction that, in practice, means duty to the institutions
that define what the nation requires. When those institutions are defense
contractors, the duty is military. When those institutions are scientific
communities, the duty is discovery. The framing determines the outcome.

And then Detachment 201 happened. The Army directly commissioned the
Palantir CTO, the Meta CTO, and two OpenAI executives as Lieutenant
Colonels. No military background. Two-week training. No recusal from
billion-dollar DoD contracts. "National service should be a universal duty"
— unless you're wealthy enough to enter at field grade while the people who
actually served navigate the VA backlog. One of the people who built this
system actually served. Infantry. Went through the process. Managed real
cryptographic keys in a real communications platoon. He didn't get a
ceremony at Conmy Hall. He built a sovereign compute platform and gave it
away under AGPL.

---

## The scale inversion

Here is what is structurally interesting about this juxtaposition:

Palantir is a $70 billion company with thousands of engineers, government
contracts worth billions, institutional partnerships with defense and
intelligence agencies across the Western world, and the resources to publish
a 320-page book, commission a 22-point summary, and generate global media
coverage for their philosophy of civilization.

The system described in this article was built by one person, in
conversation with AI, on $15,000 of consumer hardware in a basement, over
two years, with zero funding, zero institutional backing, and zero media
coverage.

The manifesto is 320 pages of argument about what civilization requires.
The system is 14 services, 27,000 tests, 70 reproduced papers, and a
cryptographic provenance chain — running.

One of these is a document about what should be built. The other is a
thing that was built.

---

## What we were doing that week

The week Palantir's 22 points circulated, we were:

- Deploying workspace scaffolding for the external research group: shared
  data directories, pilot experiment lifecycle, reviewer-visible dashboards
- Running darkforest v2.0, our security validator: 175 PASS, 0 FAIL across
  pen tests, protocol fuzzing, and crypto audits
- Setting up per-user Python environments with offline package installation
  so researchers can work without internet access
- Documenting composition patterns for upstream teams to absorb

We were not writing about what technology should do. We were making
technology do it.

---

## A note on tone

This article is not angry at Alex Karp. Anger at individuals is the bread
thief problem — you point at one person and miss the structure that produces
them. There will always be another Karp, another manifesto, another
declaration from another well-funded entity about what civilization requires.

The disgust is architectural. It is directed at the structure that allows a
defense contractor to position itself as a philosopher of civilization — and
to be taken seriously — while the actual work of building sovereign,
attributed, reproducible scientific infrastructure happens in silence, in
basements, on consumer hardware, with no funding and no platform.

The manifesto is not dangerous because of its specific claims. It is
dangerous because of the structural assumption that undergirds all of them:
that civilization is a thing to be managed by the capable few, rather than a
thing that emerges from the attributed contributions of the many.

We built the attribution system. We built the provenance chain. We built
the compute platform. We built the security validator. We reproduced the
science. We served the researchers. We did it in the open, under AGPL,
with every line traceable.

The repos are public. The provenance is transparent. The attribution will
find you if you help.

---

## Links

- **Code**: github.com/ecoPrimals
- **Deployment**: github.com/sporeGarden/projectNUCLEUS
- **Live system**: lab.primals.eco
- **License**: AGPL-3.0-or-later (code), CC-BY-SA 4.0 (docs)
