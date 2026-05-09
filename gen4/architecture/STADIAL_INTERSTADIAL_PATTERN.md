# The Stadial/Interstadial Pattern

**A constraint-driven optimization framework for evolving distributed systems**

**Date**: May 9, 2026
**Lineage**: gen3/CONSTRAINED_EVOLUTION_FORMAL → gen3/ECOSYSTEM_ARCHITECTURE → gen4
**Status**: Working paper — observed and formalized from the ecoPrimals ecosystem

---

## The Pattern Named

Distributed systems evolve. Not metaphorically — they undergo
selection, specialization, extinction, and adaptation under
constraint. The stadial/interstadial pattern is a framework for
reasoning about this evolution at ecosystem scale, drawn from
glacial geology and grounded in the constrained evolution thesis
formalized in gen3.

The pattern is a cycle with four phases:

```
  ┌──────────────┐
  │   STADIAL     │  Hard convergence.
  │ (ice age)     │  All components forced to a common
  │               │  fitness threshold. Those that do
  │               │  not satisfy the invariants are
  │               │  selected against.
  └──────┬───────┘
         │ gate clears
         ▼
  ┌──────────────┐
  │ INTERSTADIAL  │  Diversification under constraint.
  │ (warming)     │  New patterns emerge. Components
  │               │  specialize into niches. The exemplar
  │               │  forms and propagates.
  └──────┬───────┘
         │ extinction wave
         ▼
  ┌──────────────┐
  │  EXTINCTION   │  Old patterns culled. Fossil record
  │ (selection)   │  preserved. The ecosystem simplifies
  │               │  to the patterns that survived.
  └──────┬───────┘
         │ next constraint visible
         ▼
  ┌──────────────┐
  │ NEXT STADIAL  │  New hard convergence. The cycle
  │ (next ice age)│  repeats at a higher level of
  │               │  organization.
  └──────────────┘
```

Each phase serves a different function in the optimization
process. None is optional. A system that never undergoes stadial
convergence accumulates drift. A system that never enters
interstadial diversification never innovates. A system that
never experiences extinction carries dead weight. A system that
cannot anticipate the next stadial is perpetually surprised.

---

## The Stadial Gate as Ecosystem-Level Type System

gen3 established that Rust's type system functions as an
environmental constraint: it eliminates unsound solutions at
compile time, reshaping the fitness landscape so that surviving
code is specialized for correctness. The constraint does not
prescribe solutions. It defines what "fit" means.

The stadial gate extends this principle to architecture. A
stadial gate is a set of invariants that every component in a
distributed system must satisfy simultaneously. Like a type
system, the gate is:

- **Universal**: it applies to every component, not selectively.
- **Binary**: each invariant is either satisfied or not.
- **Non-prescriptive**: the gate defines what properties are
  required, not how to achieve them.
- **Mechanically verifiable**: satisfaction can be checked
  without human judgment.

The ecoPrimals stadial gate (April 2026) required:

- async-trait eliminated (native async in traits)
- Enum dispatch for finite implementors
- cargo deny check bans passes (ring, openssl, aws-lc-sys)
- Edition 2024
- JH-0 MethodGate pre-dispatch authorization
- BTSP Phase 3 AEAD encryption
- Capability Wire Standard L2+
- localhost-default binding
- plasmidBin musl-static ecoBin deployment
- forbid(unsafe_code) or justified opt-out

Each invariant is independently verifiable. Each can be satisfied
by different implementations. The gate does not care how a
component eliminates async-trait — it cares that async-trait is
absent. This is the key property: like a type system, the gate
constrains the solution space without prescribing the solution.

The gate clears at a specific moment. Before the gate, the
ecosystem is heterogeneous — some components satisfy the
invariants, some do not. After the gate, the ecosystem is
homogeneous at the invariant level — every component satisfies
every requirement — while remaining heterogeneous at the
implementation level.

This is the distinction between convergent and identical. All
components converge on the same fitness properties. None produce
identical implementations. This is gen3's convergent evolution
(section 4.3) — cephalization, eyes, and wings evolving
independently in different lineages — applied to architecture.

---

## The Interstadial as Creative Period

The stadial enforces convergence. The interstadial enables
divergence. Both are necessary.

Once the gate clears, the constraint environment changes. The
survival threshold is met. The ecosystem enters a warming period
where selective pressure shifts from "satisfy the invariants" to
"specialize for your niche." Components that were spending all
their evolutionary budget on stadial compliance are now free to
invest in domain-specific adaptation.

The interstadial is where new architectural patterns emerge. Not
because anyone designed them, but because the stadial gate cleared
the debris that was blocking them. When every component encrypts
every channel (BTSP Phase 3), authenticated composition becomes
possible. When every component deploys as a static binary
(plasmidBin), binary-only IPC becomes feasible. When every
component implements pre-dispatch authorization (MethodGate),
token federation becomes the next meaningful goal.

This is gen3's "constraint specificity creates solution
specificity" (section 4.1) operating at ecosystem timescale. The
stadial constraint (encrypt everything) created a specific fitness
landscape (authenticated channels) that the interstadial explores
(token federation, audit log forwarding, cross-atomic auth).

The interstadial is the creative period, but it is not
unconstrained. The stadial invariants still hold. The ice has
receded, but the physics of the environment remain. New patterns
emerge within the invariant envelope, not outside it.

---

## The Exemplar Pattern

A recurring structure in constraint-driven optimization: one
component completes evolution first and becomes the reference
implementation that other components are selected against.

The exemplar is not a specification document. It is a running,
tested, proven implementation that demonstrates what the target
state looks like in practice. The difference matters: a
specification describes what should be true. An exemplar proves
what can be true.

The exemplar operates as a seed crystal in the ecosystem. A
supersaturated solution remains liquid until a seed crystal is
introduced; then the entire solution crystallizes around the
seed's lattice structure. In a distributed system, the exemplar
provides the lattice: here is the directory layout, here is the
CLI surface, here is the module decomposition, here is the
migration table, here is what the test output looks like.

Components that absorb the exemplar do not clone it. They adapt
it to their own niche. The exemplar's directory structure becomes
a template. Its CLI surface becomes a convention. Its migration
table becomes a checklist. Each adaptation is different — shaped
by the component's domain, constraints, and history — but all
share the seed crystal's structural properties.

The exemplar pattern is an optimization technique: rather than
specifying the target state in documentation and hoping every
component interprets the specification correctly, produce a single
working instance and let other components crystallize around it.
The working instance eliminates ambiguity by being concrete.

---

## The Fossil Record as Provenance

Extinction events in distributed systems carry an information
loss risk: if old patterns are simply deleted, the evolutionary
trajectory of the system becomes unreconstructable. Future
developers cannot understand why the current architecture exists
because they cannot see what it replaced.

The fossil record pattern addresses this: before culling old
patterns, snapshot them with provenance. Date them. Explain what
they were, why they existed, and what supersedes them. Preserve
the relationship between the old pattern and its successor.

The fossil record is the changelog elevated to geological
status. A changelog records what changed. A fossil record records
what was, why it died, and what it became. The changelog is a
list. The fossil record is a narrative.

Properties of a well-formed fossil record entry:

- **Dated**: the snapshot is timestamped to a specific point in
  geologic time (the stadial/interstadial boundary).
- **Provenance-tagged**: the entry explains what external
  conditions (stadial gate, interstadial pressure, exemplar
  pattern) drove the extinction.
- **Relationship-documented**: the entry explicitly maps old
  patterns to their successors.
- **Immutable**: once deposited, the fossil is not modified.
  Later understanding is added as new entries, not as edits to
  old ones.

The fossil record serves two audiences: the current team (who
need to understand why deprecated patterns exist and what
replaces them) and the future team (who need to reconstruct the
evolutionary trajectory of the system from its geological
layers).

---

## The Wave Model for Ecosystem-Scale Migration

Large-scale architectural migrations in distributed systems fail
when they attempt to move every component simultaneously. The
wave model phases the migration through three stages:

**Phase 1: Absorption.** Study the exemplar. Pull the reference
implementation. Read the architecture document. Run the new
binary. Understand what the target state looks like before
attempting to reach it. This phase is observational — no code
changes, only learning.

**Phase 2: Extinction.** Apply the evolutionary pressure.
Migrate APIs. Absorb experiment binaries into the unified
binary. Deprecate old patterns with explicit notes. Snapshot
pre-extinction code to the fossil record. This is the phase
where the code changes.

**Phase 3: Validation.** Prove fitness. Build, lint, test — zero
warnings, zero failures. Run the new binary's validation suite.
Confirm that the component satisfies the same invariants the
exemplar satisfies. This is the selection event: either the
component is fit for the post-interstadial environment, or it
is not.

The wave model is ordered but not simultaneous. Components enter
Phase 2 when they have completed Phase 1. Components enter Phase
3 when they have completed Phase 2. Different components may be
in different phases at the same time. The ecosystem migrates as
a wave, not as a synchronized jump.

The handoff document is the inheritance mechanism. It carries the
acquired characteristics from the exemplar to each component:
here is what changed, here is the API migration table, here is
the timeline, here is your component-specific guidance. The
handoff is Lamarckian inheritance — acquired characteristics
transmitted directly between lineages — operating through a
document rather than through a genome.

---

## The Two-Tier Gate

gen3 established that Rust's compiler catches unsound code before
it reaches the binary (compile-time selection), and the test
suite catches incorrect behavior after the binary runs (runtime
selection). Two tiers of selection, each catching a different
class of defect.

The stadial/interstadial pattern introduces a two-tier gate at
ecosystem scale:

**Tier 1 (Structural)**: Can the component satisfy the
invariants in isolation? Does the code compile, pass linting,
pass formatting, pass unit tests? This tier requires no external
dependencies. It is the compile-time check of the ecosystem — it
catches what is structurally unsound without exercising behavior.

**Tier 2 (Behavioral)**: Can the component participate in live
compositions? Does it discover deployed primals? Does it route
capability calls through IPC? Does it handle authenticated
tokens? This tier requires a running ecosystem. It is the
runtime check of the ecosystem — it catches what compiles but
does not compose.

The two-tier gate maps directly to gen3's compiler-vs-runtime
selection:

| Gen3 Level | Ecosystem Level | What It Catches |
|------------|-----------------|-----------------|
| Compiler | Tier 1 (Structural) | Does not build, lint, or pass isolated tests |
| Runtime | Tier 2 (Behavioral) | Builds but does not compose with live primals |

A component that passes Tier 1 but fails Tier 2 is like code
that compiles but produces wrong answers at runtime. It is
structurally valid but behaviorally incorrect. Both tiers must
pass for the component to be considered fit.

The two-tier gate is useful because Tier 1 is cheap and fast
(CI-safe, no external dependencies) while Tier 2 is expensive
and slow (requires deployed infrastructure). Running Tier 1
first eliminates structurally unfit components before investing
in behavioral testing. This is the same optimization principle
as compile-time rejection: catch the cheap failures early.

---

## The Next Stadial as Architectural Pressure

The stadial/interstadial cycle is not a single event. It repeats.
The next stadial is always visible from the current interstadial
— not in detail, but in outline. The patterns that are deferred
or marked "future" during the interstadial are the invariants
that the next stadial will enforce.

Recognizing the next stadial during the current interstadial is
a strategic advantage. It allows the ecosystem to pre-adapt —
to invest interstadial creative energy in patterns that will
become requirements when the next ice age arrives.

This is the gardener's foresight, described in
gen4/knome/THE_GEOLOGICAL_CONSTRAINT: the ability to read the
ecosystem's trajectory and mentor the current generation toward
fitness for a constraint that does not yet exist but is coming.
Natural selection lacks this foresight. Directed evolution —
K-NOME's Lamarckian layer — provides it.

The interstadial work is not arbitrary innovation. It is
preparation. The patterns that emerge during the interstadial are
the patterns that will be tested by the next stadial. The
ecosystem that anticipates the gate is pre-adapted. The ecosystem
that does not is surprised.

---

## Connection to gen3

The stadial/interstadial pattern extends three gen3 concepts
from organism to ecosystem:

**Constraint Specificity Creates Solution Specificity (4.1)**:
The stadial gate creates a specific post-stadial fitness
landscape. The interstadial diversification explores that
landscape. Different components find different niches within the
landscape defined by the gate's invariants.

**Fitness Without Innovation (4.2)**: Not every component
produces architectural innovation during the interstadial. Some
simply become more fit for the constrained environment — cleaner
APIs, tighter module boundaries, fewer warnings, better
documentation. The stadial/interstadial pattern values this
incremental fitness equally with headline innovation.

**The Fastidious Genome (4.5)**: Components that pass through a
stadial/interstadial cycle become more specialized for their
ecosystem and less portable to other ecosystems. This is a
trade-off, not a defect. The specialization is the fitness.
The portability loss is the cost. The fossil record preserves
the pre-specialized state for reference.

---

## The Pattern as Optimization Framework

The stadial/interstadial pattern is not specific to ecoPrimals.
It is a general framework for evolving distributed systems under
constraint:

1. **Define invariants** that every component must satisfy. Make
   them universal, binary, non-prescriptive, and mechanically
   verifiable.

2. **Enforce the gate** across the entire ecosystem
   simultaneously. This is the stadial. Components that do not
   satisfy the invariants are selected against.

3. **Release creative pressure** once the gate clears. Allow
   components to diversify into domain-specific niches. This is
   the interstadial. Mentor specialization, not convergence.

4. **Produce an exemplar** — a single component that completes
   the interstadial evolution first and becomes the reference
   implementation for the rest.

5. **Propagate through waves** — absorption, extinction,
   validation — using handoff documents as the inheritance
   mechanism.

6. **Preserve the fossil record** — snapshot pre-extinction
   patterns with dated provenance before culling.

7. **Anticipate the next gate** — identify deferred invariants
   and pre-adapt the ecosystem during the current interstadial.

The framework is fractal. It can operate at the function level
(compile cycles), the component level (release cycles), and the
ecosystem level (stadial cycles). The principles are identical
at every scale. The timescale changes. The constraint changes.
The optimization dynamic does not.

---

*The stadial is the compiler for the ecosystem. The interstadial
is the solution space. The extinction is the selection event. The
fossil record is the provenance. The next stadial is the
anticipated constraint. The cycle repeats — each time at a higher
level of organization, each time producing a more specialized,
more fit, more composed system.*
