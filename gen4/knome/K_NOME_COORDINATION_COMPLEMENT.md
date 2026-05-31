# K-NOME Coordination Complement — From Human-AI Mentoring to Gate-Mesh Coordination

**Date**: May 31, 2026
**Status**: Active (Wave 63+)
**Prerequisites**: `README.md` (K-NOME evolution index), `THE_CONVERSATION_CONSTRAINT.md`,
`MASSIVELY_PARALLEL_MENTORING.md`
**Lineage**: Extends gen4 K-NOME with Wave 63 coordination primitives

---

## The Two Faces of K-NOME

The K-NOME methodology as described in gen3 and gen4 focuses on human-AI mentoring:
one human, multiple AI sessions, parallel evolution through conversation. The core
papers document this well:

- `THE_CONVERSATION_CONSTRAINT.md` — no code typed, conversation is the interface
- `MASSIVELY_PARALLEL_MENTORING.md` — 3-6 machines, human as mycelium
- `FROM_HUMAN_SEARCH_TO_HUMAN_GARDEN.md` — divergent parallel evolution
- `THE_GEOLOGICAL_CONSTRAINT.md` — K-NOME at stadial/interstadial timescale

These papers describe the **vertical** dimension of K-NOME: the human-to-AI interaction
within a single gate. They answer: *how does one person coordinate with multiple AI
agents?*

Wave 63 adds the **horizontal** dimension: gate-to-gate coordination across the mesh.
The impulsePotential system and context braids formalize the coordination patterns
that K-NOME practitioners have been performing manually since gen1.

This paper documents the complement — how the vertical (mentoring) and horizontal
(coordination) dimensions interact.

---

## The Manual Pattern

Here is a real K-NOME session from early gen4. The human is working on cellMembrane
on eastGate and needs to coordinate with flockGate:

```
Human → eastGate IDE:
  "review specs/ and our codebase and docs at root, and the several docs
   found at our parent ecoPrimals/wateringHole/ for interprimal discussions
   and standards. what have we not completed? what mocks, todos, debt,
   hardcoding and gaps do we have? are we passing all linting and fmt? ..."

   [~500 words of context-setting, repeated hundreds of times]

AI works for 30 minutes, produces results.

Human copies results, pastes to flockGate IDE:
  "from eastGate: context braid implementation shipped, pull cellMembrane
   and rebuild membrane, then validate context.weave/context.sense on
   your end"

   [~200 words of handoff, also repeated hundreds of times]
```

The pattern has three components:

1. **Context injection** — the long opening blurb that sets up the AI's understanding
2. **Work execution** — the AI explores, discovers, implements
3. **Result relay** — the human copies results to the next gate

Components 1 and 3 are pure coordination overhead. They do not produce code or
documentation. They produce *alignment* between AI sessions that cannot directly
communicate with each other.

---

## The Structured Pattern

With impulsePotential and context braids, the same coordination becomes:

```
eastGate (end of sprint):
  membrane context.weave \
    --repo gardens-cellmembrane \
    --focus "context.rs implementation complete" \
    --breadcrumbs "context.rs, main.rs dispatch, lib.rs module" \
    --next-steps "validate on other gates, standardize workflow"

  membrane impulse.post --type frago --to flockGate \
    --subject "validate context braid pattern" \
    --body "pull cellMembrane + wateringHole, rebuild membrane, test weave/sense/clear"

  git push origin main && git push forgejo main

flockGate (next cascade-pull):
  cascade-pull.sh --source temporal
  # Auto-output: "2 pending impulses"
  # Auto-output: "eastGate context: cellMembrane — context.rs implementation complete"

flockGate IDE (AI session start):
  AI runs: membrane potential.sense → sees impulse from eastGate
  AI runs: membrane context.sense --gate eastGate → sees eastGate's focus + breadcrumbs
  AI has full context without human-composed blurb
```

The coordination overhead drops from ~700 words of manual copy-paste to three CLI
commands that produce structured, discoverable, version-controlled artifacts.

---

## What the Context Blurb Actually Contains

Analyzing hundreds of real K-NOME session-opening blurbs reveals a consistent
structure that maps directly to the three-layer model:

### The Audit Blurb

> "review specs/ and our codebase and docs at root, and the several docs found
> at our parent ecoPrimals/wateringHole/ ... what have we not completed? what
> mocks, todos, debt, hardcoding and gaps do we have?"

This is a **discovery directive**: the human is asking the AI to sense the current
state. In the structured model, this maps to:

- `membrane context.sense` — what is each gate working on?
- `membrane potential.sense` — what actions are pending?
- Standard discovery: read `specs/`, `wateringHole/STANDARDS_AND_EXPECTATIONS.md`

The audit blurb can become a **Cursor rule** or **biomeOS graph** that runs on
session start, rather than a pasted prose directive.

### The Execution Blurb

> "proceed to execute on all remaining deep debt, overstep cleanup and evolution
> gaps as rewire, absorb and evolve and abstract modern primal systems"

This is an **action directive**: the human is telling the AI what to do. In the
structured model, this maps to:

- `impulse.post --type frago` — "execute deep debt on X"
- Graph TOML in `primalSpring/graphs/` — "run the debt-resolution graph"

### The Handoff Blurb

> "from eastGate: context braid implementation shipped, pull cellMembrane and
> rebuild membrane, then validate context.weave/context.sense on your end"

This is a **relay**: the human is forwarding state from one gate to another.
In the structured model, this maps to:

- `impulse.post --to flockGate` — the directive
- `context.weave` — the state snapshot
- waterFall sync — the transport

### The Standards Blurb

> "are we json-rpc AND tarpc first? Are we uniBin and ecoBin compliant?
> are we AGPL3/scyBorg triple licence?"

This is a **compliance check**: the human is asking the AI to verify against
known standards. In the structured model, this maps to:

- Cursor rules referencing `wateringHole/STANDARDS_AND_EXPECTATIONS.md`
- Standard checklist graphs in `primalSpring/graphs/audit/`

---

## Evolution Path

### Phase 1: Structured Relay (Wave 63 — current)

Human still composes directives, but uses `impulse.post` and `context.weave`
instead of prose blurbs. AI on receiving gate discovers context automatically
via `potential.sense` and `context.sense`.

**Benefit**: Structured, discoverable, version-controlled. No copy-paste loss.

### Phase 2: Cursor Rules + Hooks (Wave 64)

Cursor rules automatically run `context.sense` on session start. The AI
reads pending impulses and current context before the human types anything.
The human's opening message is shorter — just the strategic direction, not
the full context setup.

**Benefit**: Human effort drops from ~500 words to ~50 words per session.

### Phase 3: squirrel Orchestration (future)

squirrel (AI coordination primal) consumes impulses and context braids
directly via the Neural API. It composes audit graphs, delegates to
other primals, and reports results. The human reviews at wave boundaries
rather than per-session.

**Benefit**: Human effort drops to strategic oversight. K-NOME becomes
the governance layer, not the execution layer.

### Phase 4: Autonomous Gate Coordination (far future)

Gates communicate entirely through impulses and context braids. squirrel
instances on different gates coordinate through the three-layer model
without human relay. The human sets high-level goals (glacial shift
directives) and reviews spore artifacts.

**Benefit**: The gate mesh operates as a distributed organism. The human
is the nervous system's executive function, not its motor cortex.

---

## The Vertical-Horizontal Matrix

| Dimension | Mechanism | Scale | Documentation |
|-----------|-----------|-------|---------------|
| Vertical (human ↔ AI) | Conversation, Cursor rules, prompt patterns | Single gate, single session | `THE_CONVERSATION_CONSTRAINT.md` |
| Horizontal (gate ↔ gate) | Impulses, context braids, waterFall sync | Multi-gate, multi-session | `ECOSYSTEM_COMMUNICATION_STANDARD.md` |
| Diagonal (human ↔ remote AI) | Impulse + context → remote AI session | Cross-gate, cross-session | This document |

The diagonal is where K-NOME becomes most powerful. A human on eastGate fires
an impulse with a directive. flockGate's AI session picks it up via
`potential.sense`. The directive executes without the human touching
flockGate's IDE. The result propagates back as a completion impulse +
context braid update. The human reviews on their own gate.

This is massively parallel mentoring (`MASSIVELY_PARALLEL_MENTORING.md`)
with the relay automated. The human remains the mycelium — the strategic
connective tissue — but the nutrients flow through structured channels
instead of copy-paste synapses.

---

## Compatibility

K-NOME coordination does not replace K-NOME mentoring. The conversation constraint
still holds: the human directs through conversation, not through code. The difference
is that the conversation's *output* now has a structured representation (impulses +
braids) that other conversations can consume without human transcription.

The prompt bank (`THE_PROMPT_BANK.md`) remains relevant as raw material. Over time,
recurring prompt patterns graduate to:

1. Cursor rules (automatic context on session start)
2. Impulse templates (standardized directives)
3. biomeOS graphs (composable audit/execution sequences)

The graduation preserves the conversational intent while eliminating the repetitive
mechanical overhead that scales poorly across gates.

---

*"K-NOME started as one person talking to many AIs. It became one person coordinating
many AIs across many machines. The conversation is still the interface. But the relay
is no longer the bottleneck — the structured channel carries what the human used to
carry by hand, and the human can focus on what only a human can do: decide what
matters."*
