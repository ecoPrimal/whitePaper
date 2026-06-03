# Overwatch as Distributed Coordination — A Sovereign Pattern

**Gen5 Foundation** — how sovereign infrastructure enables a floating coordination
position that can operate from any gate, any session, any project.

**Date**: June 3, 2026  
**Wave**: 75  
**Status**: Active

---

## The Pattern

In distributed systems, coordination is the hard problem. Most solutions
centralize it: a project manager, a CI server, a Slack channel, a Jira board.
The coordinator becomes a single point of failure and a dependency on commercial
infrastructure.

The ecoPrimals ecosystem solves this differently. **Overwatch** is a coordination
*position* — not a service, not a server, not a person. It is a role that any
sufficiently-connected node can assume, enabled by sovereign infrastructure
that makes coordination state portable, verifiable, and universally accessible.

---

## Why This Is a Gen5 Problem

| Generation | Coordination Model | Limitation |
|------------|-------------------|------------|
| gen1 | Single machine, single operator | No distribution to coordinate |
| gen2 | Multiple primals, one gate | Local process coordination (UDS, socket) |
| gen3 | Multiple gates, bash scripts | SSH-based, fragile, operator-dependent |
| gen4 | waterFall cascade, Forgejo relay | Infrastructure exists but coordination is implicit |
| **gen5** | **Overwatch position, sovereign stack** | **Coordination is formalized, portable, trust-verified** |

Gen5 is where coordination scales beyond the operator's immediate attention.
Multiple gates run parallel evolution teams. The operator moves between
workstations. AI agents need context bootstrapping. The coordination system
must work regardless of which gate the operator is sitting at.

---

## The Sovereignty Dependency

Overwatch cannot float without sovereignty. Here's why:

### The Commercial Failure Mode

Imagine overwatch depends on GitHub Issues for tracking, Slack for blurbs,
and Cloudflare for relay. Now:

- GitHub has an outage → coordination state is unreachable
- Slack rate-limits → blurb delivery fails
- Cloudflare blocks a region → remote gate can't sync

The overwatch position is pinned to whichever machine still has access to
these services. It cannot float. It is caged.

### The Sovereign Solution

Every layer of the overwatch stack is sovereign:

```
┌────────────────────────────────────────────────────┐
│                  OVERWATCH STACK                    │
│                                                    │
│  ┌──────────────────────────────────────────────┐  │
│  │  Layer 5: Trust         bearDog BTSP         │  │
│  │  ── signed FRAGOs, verified cross-gate ───── │  │
│  ├──────────────────────────────────────────────┤  │
│  │  Layer 4: Discovery     Songbird mesh        │  │
│  │  ── who's online, what's healthy ─────────── │  │
│  ├──────────────────────────────────────────────┤  │
│  │  Layer 3: Relay         K-Derm diderm VPS    │  │
│  │  ── cross-network coordination relay ─────── │  │
│  ├──────────────────────────────────────────────┤  │
│  │  Layer 2: Sync          waterFall cascade    │  │
│  │  ── temporal propagation across all gates ── │  │
│  ├──────────────────────────────────────────────┤  │
│  │  Layer 1: State         wateringHole (git)   │  │
│  │  ── all coordination artifacts in git ────── │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  ANY gate with layers 1-2 can run overwatch.       │
│  Layers 3-5 extend reach (WAN, trust, discovery).  │
└────────────────────────────────────────────────────┘
```

The minimum viable overwatch needs only layers 1-2: git access to
wateringHole and the ability to run a cascade. This means a laptop on
WiFi, a Raspberry Pi on the LAN, or grapheneGate on cellular data can
all assume overwatch.

Layers 3-5 extend overwatch's reach. The K-Derm relay enables coordination
with WAN gates. Songbird mesh enables real-time topology awareness. bearDog
BTSP enables trust-verified coordination.

---

## The Biological Model

Overwatch maps to the **central nervous system** in the ecosystem's biological
metaphor, but with a critical difference: it is not centralized.

### Traditional CNS (Centralized)

```
Brain (single point) → spinal cord → peripheral nerves → organs
```

If the brain fails, the organism dies. If the spinal cord is severed,
organs below the cut are disconnected.

### Ecosystem CNS (Distributed)

```
Any gate + wateringHole access → cascade nerve → all gates
```

If eastGate goes offline, the user opens ironGate and assumes overwatch
there. The "brain" moved. The organism continues because:

1. All coordination state is in git (wateringHole), not in a single gate
2. The cascade nerve (waterFall) is peer-to-peer, not hub-and-spoke
3. Each gate has enough local autonomy to continue working without overwatch

This is closer to an **octopus nervous system** — each arm (gate) has
significant local processing, but one can take the lead when needed.

---

## The Three Artifacts as Coordination Primitives

Overwatch's output is entirely expressible as three artifact types
(see `ECOSYSTEM_COMMUNICATION_STANDARD.md`):

| Artifact | Coordination Function | Biological Analog |
|----------|----------------------|-------------------|
| **Handoffs** | Permanent memory — what happened and why | Long-term memory (hippocampus) |
| **FRAGOs** | Action directives — what to do next | Motor commands (efferent signals) |
| **Blurbs** | Context injection — who you are and what matters | Sensory priming (afferent context) |

All three are **git-native**. They live in wateringHole. They propagate
via cascade. They are readable by any gate. This is what makes overwatch
portable — its entire output is already in the shared state.

---

## The Floating Position in Practice

### Movement Triggers

The overwatch position moves when the user's coordination attention moves:

| Trigger | Before | After | Mechanism |
|---------|--------|-------|-----------|
| User opens new gate | eastGate overwatch | ironGate overwatch | User paste + "cascade and review" |
| Sprint focus shift | Strategic (all gates) | Tactical (one primal) | Overwatch narrows scope |
| Gate comes online | N gates | N+1 gates | westGate joins, needs onboarding |
| Gate goes offline | N gates | N-1 gates | biomeGate down, overwatch pauses its FRAGOs |
| User switches IDE | Desktop Cursor | Laptop Cursor | wateringHole state is the same |

### What Moves vs What Stays

| Moves with Overwatch | Stays in wateringHole |
|---------------------|----------------------|
| User's attention and judgment | Readiness docs, handoffs, FRAGOs |
| Chat context and history | Blurb templates (in archive) |
| Strategic priorities | Gate inventory, team assignments |
| Real-time decisions | Impulse history, wave archives |

The overwatch position is **stateless** in the sense that all persistent
state lives in wateringHole. A fresh chat on a fresh gate can become
overwatch by reading wateringHole — the documents *are* the continuity.

---

## Scaling Overwatch

### Today: Single Overwatch

One user, one overwatch chat, multiple evolution chats receiving blurbs.

```
User ──→ Overwatch (primalSpring/eastGate)
           ├── blurb → Songbird evolution (southGate)
           ├── blurb → biomeOS evolution (southGate)
           ├── blurb → bearDog evolution (southGate)
           ├── blurb → toadStool evolution (strandGate)
           ├── blurb → barraCuda evolution (strandGate)
           ├── blurb → coralReef evolution (strandGate)
           ├── blurb → cellMembrane evolution (ironGate)
           └── ...
```

### Tomorrow: Hierarchical Overwatch

Multiple users or AI agents, each with overwatch scope:

```
Strategic Overwatch (ecosystem-wide)
  ├── Gate Overwatch (ironGate) — cellMembrane + projectNUCLEUS
  ├── Gate Overwatch (southGate) — Songbird + biomeOS + bearDog
  ├── Gate Overwatch (strandGate) — compute trio + provenance trio
  └── Gate Overwatch (flockGate) — sporePrint + content pipeline
```

Each gate overwatch runs its own cascade-review-blurb cycle for its
domain. Strategic overwatch coordinates between gate overwatches.
FRAGOs flow bidirectionally. The hierarchy is not imposed — it emerges
from which gates have active coordination sessions.

### Horizon: Autonomous Overwatch

When `membrane context.weave` and `membrane potential.sense` are mature,
overwatch functions can be partially automated:

- Cascade → auto-sense → structured diff report
- Delivery detection → auto-archive completed handoffs
- Test regression → auto-fire FRAGO to responsible gate
- Readiness criteria met → auto-update readiness.md

The human retains strategic authority: which goals matter, what the
critical path is, when to cut over sovereignty shadows. The AI handles
the mechanical coordination. This is the endgame of the overwatch pattern.

---

## Connection to Other Gen5 Foundations

| Foundation | Connection to Overwatch |
|-----------|----------------------|
| `COVALENT_MESH_TRUST_VALIDATION.md` | Overwatch validates the mesh. The mesh enables overwatch to float. Circular dependency resolved by sovereignty. |
| `SOVEREIGNTY_SHADOW_EVOLUTION.md` | Each sovereignty shadow graduation reduces overwatch's dependency on commercial services. S1-S5 complete = fully sovereign overwatch. |
| `KDERM_DIDERM_ENVELOPE.md` | The VPS relay enables overwatch to reach WAN gates (flockGate) and external collaborators (gen5 thesis). |
| `TRANSPORT_EVOLUTION.md` | Nanowire → quorum sensing = overwatch's communication evolving from manual relay to autonomous sensing. |
| `FUNCTIONAL_PATTERN_CONVERGENCE.md` | The Two Threes (triad + trio) are overwatch's compositional vocabulary. Overwatch speaks in qS/wF/rP. |
| `CONTEXT_BRAID_PATTERN.md` | Context braids are the automated future of blurbs. When braids graduate, overwatch's blurb composition becomes machine-assisted. |

---

## The Gen5 Significance

Gen5 asks: "does someone else's science come out the other end?" For that to
work, coordination must scale beyond one person at one keyboard. External
collaborators (Gonzales NF, ABG, Jones) will interact with the ecosystem
through scoped gate profiles — essentially, they receive blurbs and produce
handoffs, mediated by waterFall.

Overwatch is the pattern that makes this possible. It is the coordination
layer that doesn't depend on the coordinator being in one place. The
sovereignty stack is what makes it real.

---

*"Overwatch is not a person, a gate, or a program. It is a position — a
point of view over the whole ecosystem. It floats because the ground
(wateringHole) is everywhere, and the sky (cascade) reaches everything.
Sovereignty is what makes the ground solid and the sky clear."*
