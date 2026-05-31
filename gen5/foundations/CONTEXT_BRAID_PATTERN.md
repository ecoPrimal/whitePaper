# Context Braids — Developer State as Woven Provenance

**Status**: Active (Wave 63+)
**Lineage**: External analog of sweetGrass braids
**Implementation**: `wateringHole/CONTEXT_BRAID_STANDARD.md`, `membrane context.*`
**Date**: May 31, 2026

---

## From Data Provenance to Developer Provenance

gen3 proved that data provenance works: rhizoCrypt records what happened, sweetGrass
weaves why it matters, loamSpine anchors the proof. A pseudoSpore carries the full
provenance chain — any recipient can verify every computation, every input, every
attribution, back to the original data.

gen5 asks whether the same provenance architecture works for developer coordination.
Not the provenance of data — the provenance of intent.

When six gates evolve concurrently, each running its own Cursor IDE instance, each
pushing to different remotes on different schedules, the coordination problem is not
"where is the code?" (waterFall solves that) or "what should I do next?" (impulses
solve that). The coordination problem is: **"what is the story of this gate right now?"**

Context braids answer this question.

---

## The Braid Metaphor

sweetGrass braids weave three strands into a single record:

1. **What** (the data) — hashes, sizes, formats
2. **How** (the computation) — methods, parameters, reproducibility proofs
3. **Who** (the attribution) — authors, organizations, timestamps

Context braids weave three analogous strands into developer state:

1. **Focus** (the what) — which repos, which files, which capabilities
2. **Breadcrumbs** (the how) — the trail of decisions that led here
3. **Next steps** (the who-cares) — what matters next, for whom

The parallel is structural, not metaphorical. sweetGrass braids produce W3C PROV-O
records that machine-readable tools can verify. Context braids produce TOML records
that machine-readable tools (membrane CLI, Cursor hooks, AI agents) can consume.

The difference is lifetime. sweetGrass braids are permanent — they anchor to loamSpine
and become part of the scientific record. Context braids are ephemeral — they auto-decay
when superseded, cleared when the sprint ends, archived only if they describe
completed milestones worth remembering.

---

## Architecture

### Storage

Context braids live in `infra/wateringHole/context/{gate}/`:

```
context/
├── eastGate/
│   └── gardens-cellmembrane.toml     # eastGate's current work on cellMembrane
├── flockGate/
│   └── infra-wateringhole.toml       # flockGate's current work on wateringHole
├── ironGate/                          # (empty — ironGate hasn't woven yet)
└── southGate/                         # (empty — southGate hasn't woven yet)
```

Each gate owns its own directory. Gates never modify another gate's context.
waterFall syncs the entire `context/` tree, so every gate can read every other
gate's current state.

### Schema

```toml
[context]
gate = "eastGate"
repo = "gardens-cellmembrane"
woven_at = "2026-05-31T10:15:00-04:00"
wave = 63
ttl_hours = 48

[focus]
summary = "impulse.rs bearDog signing integration"
files = ["src/impulse.rs", "src/bridge.rs", "src/main.rs"]
capabilities = ["impulse.post", "crypto.sign_ed25519"]

[breadcrumbs]
trail = [
  "bridge.rs: NeuralBridge discover() + capability_call()",
  "impulse.rs: try_sign_impulse() calls bearDog via UDS",
  "main.rs: dispatch routes impulse.* and potential.* commands",
]

[next_steps]
items = [
  "test signing with live bearDog UDS socket",
  "validate ImpulseSignature appears in TOML output",
  "push to both remotes, fire impulse to flockGate",
]
priority = "high"
```

### Lifecycle

```
weave → sense → supersede → clear/decay
  │                  │
  │                  └── new weave on same repo replaces old
  │
  └── other gates read via context.sense on cascade-pull
```

Context braids are **superseding**: weaving a new braid for the same `(gate, repo)`
pair replaces the previous one. There is no history — only the current state. This
is intentional. Developer working context should reflect what's true *now*, not what
was true yesterday.

---

## The Three-Layer Model in gen5

gen5 external collaboration needs all three layers:

| Layer | Internal gate use | External collaborator use |
|-------|-------------------|--------------------------|
| Git | Code + docs | Forked repos, pseudoSpore inputs |
| Impulses | "Rebuild membrane" directives | "New data available" notifications |
| Context braids | Developer sprint state | Collaborator focus and priorities |

When Gonzales (NF collaborator) begins working with the ecosystem, her gate would
weave context braids describing her current focus (CAZyme family 47 analysis,
helixVision composition), and the internal gates would see her state alongside
everyone else's. The gate mesh becomes transparent — every participant's working
state is discoverable without human relay.

This requires the `EXTERNAL_SOVEREIGNTY_PATTERN.md` gate routing: external
collaborators get scoped gate profiles with appropriate visibility into the
context tree. Their braids are visible. Internal braids that reference
sensitive work can use capability-scoped filtering (future evolution).

---

## Relationship to K-NOME

The K-NOME programming system's core pattern is:

1. Human provides context (the "blurb")
2. AI explores, discovers, acts
3. Results flow back to human

Context braids formalize step 1. Instead of composing a long prose blurb and
pasting it into an IDE, the human (or the previous AI session) weaves a
structured context braid that the next session can consume automatically.

The evolution path:

```
Manual K-NOME (gen3-4):
  Human pastes blurb → AI reads, works → Human pastes result to next gate

Structured K-NOME (gen5):
  membrane context.weave → waterFall sync → context.sense on session start
  membrane impulse.post  → waterFall sync → potential.sense auto-trigger
  AI reads braids + impulses → works → weaves new braids + fires completion impulse

Autonomous K-NOME (future):
  squirrel reads context.sense on startup
  biomeOS composes graph from impulse directives
  primals execute, weave braids, fire impulses
  Human reviews at wave boundary
```

Each step reduces human relay work while preserving human oversight at the
strategic level.

---

## Design Decisions

**Why TOML, not JSON?**
TOML is human-readable without tooling. A developer who opens `context/eastGate/`
in a file browser can read the braids directly. JSON requires parsing to be
comfortable. Since context braids bridge human and machine coordination, human
readability is non-negotiable.

**Why TTL-based decay, not explicit deletion?**
Developer context goes stale naturally. A sprint focus from 48 hours ago is
likely irrelevant. TTL-based decay ensures that stale context doesn't accumulate
and mislead future sessions. If the context is still relevant, the developer
(or AI) weaves a fresh braid — the act of re-weaving is itself a signal that
the focus persists.

**Why per-gate directories, not a flat namespace?**
Isolation. Gates own their context. No gate modifies another's braids. This
mirrors the primal self-knowledge principle: each gate knows itself, discovers
others through observation, never through mutation.

**Why superseding (not appending)?**
Context is state, not history. Git provides the history. Impulses provide the
events. Context braids provide the *current* answer to "what's happening?"
Appending would create a log, and the ecosystem already has a log (git).

---

*"sweetGrass weaves the story of data — where it came from, who touched it, why it
matters. Context braids weave the story of developers — what they're building, where
they've been, where they're going. Both are woven. Both are provenance. One is
permanent. The other is fog that burns off when the sun rises on a new sprint."*
