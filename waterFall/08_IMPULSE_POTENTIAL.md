# Impulse/Potential — The Action Potential Layer

**How inter-gate coordination rides on waterFall**

**Date**: May 31, 2026
**Status**: Whitepaper — Implementation Active (Wave 63+)
**Prerequisites**: `03_TRIAD_COORDINATION.md`, `wateringHole/IMPULSE_POTENTIAL_STANDARD.md`

---

## The Missing Layer

The triad — quorumSignal, rootPulse, waterFall — solves temporal sync. Every gate
converges. Every repo reaches parity. The water flows.

But the water carries only code. It does not carry intent.

When eastGate completes a sprint and pushes to Forgejo, the code arrives at flockGate
on the next cascade-pull. flockGate sees new commits in cellMembrane. It does not know
*why* those commits matter. It does not know whether to rebuild a binary, validate a
pattern, or just archive the diff. The code is there. The intent is not.

The old solution was human relay: paste a blurb into an IDE, describe what happened,
tell the receiving gate what to do. This works at human scale — a few gates, a few
sprints per day. It does not work at ecosystem scale, where six gates evolve
concurrently, each on its own timeline, each producing coordination artifacts that
the others need to discover.

impulsePotential adds a new layer to waterFall: structured, time-bounded, actionable
messages that propagate alongside code through the same git infrastructure. The
coordination nerve fires alongside the sync nerve.

---

## The Biological Model

Neurons communicate through action potentials:

1. **Resting potential** — a measurable voltage gradient across the cell membrane.
   The neuron is ready but not firing. Information is latent.

2. **Depolarization** — a stimulus exceeds the threshold. The neuron fires. An
   electrochemical impulse propagates down the axon, jumping between nodes. The
   signal is discrete, all-or-nothing, and directional.

3. **Repolarization** — the impulse passes. The neuron returns to resting potential.
   The ion channels close. The membrane recharges for the next firing.

4. **Synaptic transmission** — the impulse reaches the axon terminal and triggers
   neurotransmitter release across the synapse. The receiving neuron detects the
   chemical gradient and decides whether to fire in turn.

The mapping to ecosystem coordination:

| Biological | Ecosystem | Implementation |
|------------|-----------|----------------|
| Resting potential | Gate at parity, no pending work | `potential.sense --count` = 0 |
| Depolarization | Gate completes sprint, fires impulse | `membrane impulse.post` |
| Propagation | Impulse TOML travels via git push | waterFall sync → all remotes |
| Synaptic detection | Receiving gate senses pending impulse | `potential.sense` on cascade-pull |
| Postsynaptic response | Receiving gate acks, acts, or ignores | `membrane impulse.ack` |
| Repolarization | Impulse archived at wave boundary | `membrane impulse.archive` |

The key insight: impulses are not messages between humans. They are action potentials
between gates. They fire, propagate, and are received through the same membrane
infrastructure that carries code. The membrane is the axon.

---

## Triad Integration

impulsePotential maps cleanly onto the existing triad:

```
                    ┌──────────────────────┐
                    │  quorumSignal (qS)    │
                    │                      │
                    │  potential.sense      │ ← measures membrane potential
                    │  potential.check      │ ← gradient health
                    └──────────┬───────────┘
                               │ afferent
                               ↓
                    ┌──────────────────────┐
                    │  Neural API           │
                    │                      │
                    │  graph.execute        │ ← impulse_post_signed.toml
                    │  capability.call      │ ← bearDog.sign, songbird.relay
                    └────────┬─────┬───────┘
                             │     │
                   efferent  │     │ autonomic
                             ↓     ↓
              ┌──────────────┐     ┌──────────────┐
              │  rootPulse    │     │  waterFall    │
              │              │     │               │
              │  impulse.post │     │  cascade-pull │
              │  impulse.ack  │     │  impulse.arch │
              │  context.weave│     │               │
              └──────────────┘     └───────────────┘
```

**impulse.post** is a rootPulse ACTION: the gate creates an artifact (the impulse TOML),
commits it, pushes it. This is efferent — motor output.

**potential.sense** is a quorumSignal SENSE: the gate observes what impulses are pending
without modifying state. This is afferent — sensory input.

**waterFall** is the transport: cascade-pull syncs the impulses/ directory alongside
every other file. The impulse travels on the same water as the code.

**impulse.ack** bridges rootPulse and waterFall: the receiving gate acknowledges (ACTION)
and the ack propagates back to the sender on the next sync (SYNC).

---

## The Three-Layer Model

impulsePotential does not replace git. It adds a coordination layer between code
(permanent) and context (ephemeral):

```
  Permanent ←───────────────────────────→ Ephemeral

  Git commits        Impulses              Context braids
  (loamSpine)        (rhizoCrypt)          (sweetGrass)
  ─────────────      ─────────────         ─────────────
  "What happened"    "What to do"          "What's the
                                            story now"
  Linear log         Event DAG             Woven strands
  Forever            Archived per wave     TTL auto-decay
```

Each layer has a biological primal mirror:

- **Git** mirrors **loamSpine** — the permanent ledger
- **Impulses** mirror **rhizoCrypt** — the session DAG (fire, record, close)
- **Context braids** mirror **sweetGrass** — woven provenance (but ephemeral)

The three layers together form the ecosystem's communication nervous system. Git is
the skeletal record. Impulses are the nerve firings. Context braids are the working
memory. All three sync through waterFall.

---

## Implementation

### Impulse Schema

Impulses are TOML files in `infra/wateringHole/impulses/active/`:

```toml
[impulse]
id = "2026-05-31T09-30_flockGate__rebuild-membrane-for-signing"
type = "frago"
wave = 63
subject = "rebuild membrane for impulse signing"
body = "pull cellMembrane, cargo build --release, cp to ~/.local/bin/"

[from]
gate = "eastGate"
ref = "abc1234"         # rootPulse DAG provenance

[to]
gate = "flockGate"      # or "*" for broadcast

[status]
state = "pending"       # pending → acked → archived
acked_by = ""
acked_at = ""

[signature]             # optional — bearDog Ed25519 signing
algorithm = "ed25519"
public_key = "..."
value = "..."
signed_at = "..."
```

### CLI Surface

```bash
# rootPulse ACTION: fire an impulse
membrane impulse.post --type frago --to flockGate \
  --subject "rebuild membrane" --body "..."

# rootPulse + waterFall: acknowledge
membrane impulse.ack --id <impulse-id>

# waterFall: archive spent impulses
membrane impulse.archive

# quorumSignal SENSE: measure potential
membrane potential.sense              # list pending
membrane potential.sense --count      # just the count

# quorumSignal SENSE: gradient health
membrane potential.check              # mesh-wide status
```

### Automatic Discovery

`cascade-pull.sh` auto-triggers `potential.sense` after every sync:

```
=== Membrane Potential (2 pending impulse(s)) ===
  FRAGO from eastGate (Wave 63): rebuild membrane for impulse signing
  AUDIT from flockGate (Wave 63): validate context braid pattern
```

Gates never need to manually check for impulses. The water tells them what's pending.

---

## Graduation Path

Today, `membrane impulse.post` writes a TOML file, does a git add/commit/push.
As primals come online, the operation graduates to a composed graph:

```
impulse_post_signed.toml (graduated):

  identity.resolve → git.rev_parse → impulse.create (membrane)
       → crypto.sign_ed25519 (bearDog)
       → dag.event (rhizoCrypt)
       → storage.push (nestGate)
       → mesh.publish (songbird)
```

Each primal adds a capability without the others needing to know:

- **bearDog** signs the impulse with Ed25519 (integrity)
- **rhizoCrypt** records the impulse in the DAG (provenance)
- **nestGate** stores and pushes to remotes (transport)
- **songbird** relays near-realtime via mesh (speed)

The NeuralBridge in `membrane-shadow` already attempts this routing:
try biomeOS Neural API first, fall back to shadow implementation.
The graduation is progressive — each primal that comes online adds
a capability, and the system degrades gracefully when any is absent.

---

## Relationship to Existing waterFall Concepts

impulsePotential extends the waterFall architecture without modifying it:

| waterFall Concept | impulsePotential Extension |
|-------------------|---------------------------|
| Temporal sync (code flows) | + Coordination sync (intent flows) |
| Convergence/Parity/Divergence | + Impulse count as coordination metric |
| Local/Gate/Membrane/Ecosystem levels | Impulses operate at Membrane and Ecosystem levels |
| Transport-agnostic (SSH, HTTPS, USB) | Impulses travel on the same transports |
| freshness.toml state snapshot | + impulses/active/ as coordination state |

The impulse directory is just another set of files that waterFall syncs. No new
transport, no new protocol, no new infrastructure. The existing water carries
the new information.

---

*"The nerve fires alongside the sync. The code arrives, and with it, the intent.
The receiving gate does not wonder what changed — it knows what to do. The impulse
is the difference between water that arrives and water that speaks."*
