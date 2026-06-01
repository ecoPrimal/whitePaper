# Functional Pattern Convergence — The Two Threes

**Gen5 Foundation** (convergence of gen4 triad + provenance trio into unified compositional vocabulary)

**Status**: Active (Wave 66+)
**Date**: June 1, 2026

---

## Why This Document Exists

Every coordination pattern in the ecosystem composes from six primals organized
into two groups of three. Gen4 discovered both groups independently — the triad
emerged from waterFall sync design, the trio emerged from RootPulse provenance
design. Gen5 recognizes that they are not two separate systems. They are two
aspects of a single compositional architecture: the triad coordinates, the trio
records, and biomeOS decomposes both into primal capability calls.

This document is the canonical reference. All other whitePaper documents that
discuss coordination, provenance, or composition point here.

---

## The Coordination Triad

Three primals form a closed coordination loop:

```
        quorumSignal (SENSE)
              │
              │  observes: potential.sense, potential.check
              │  discovers: mesh state, temporal positions, impulse gradients
              │
              ▼
        waterFall (SYNC)
              │
              │  propagates: temporal.cascade, temporal.sync, temporal.check
              │  reconciles: leader/follower classification, convergence, parity
              │
              ▼
        rootPulse (ACTION)
              │
              │  creates: impulse.post, impulse.ack, impulse.archive
              │  commits: rootpulse commit, branch, merge, federate
              │
              └──────────────────▶ quorumSignal (SENSE)
                                    ... the cycle repeats
```

Each member is a primal *and* a coordination domain:

| Member | Domain | Biological Analog | What It Does |
|--------|--------|-------------------|-------------|
| **quorumSignal** (qS) | SENSE | Afferent nerve (sensory) | Observes without modifying — membrane gradients, temporal positions, pending impulses |
| **waterFall** (wF) | SYNC | Autonomic nerve (homeostasis) | Reconciles distributed state — pull leaders, push followers, maintain coherence |
| **rootPulse** (rP) | ACTION | Efferent nerve (motor) | Creates versioned artifacts — fires impulses, commits provenance, federates state |

The cycle is closed: qS senses drift → wF propagates to restore coherence →
rP creates the artifact that makes coherence permanent → qS senses the new
state. No central coordinator. Each gate runs its own triad instance.

---

## The Provenance Trio

Three primals form a complete temporal recording substrate:

| Member | Temporal Role | What It Records |
|--------|---------------|----------------|
| **rhizoCrypt** | Present/future (working DAG) | Content-addressed sessions, branching exploration, purgeable when dehydrated |
| **loamSpine** | Past (immutable ledger) | Append-only linear history, cryptographic proofs, anchoring |
| **sweetGrass** | Attribution (woven braids) | W3C PROV-O provenance, semantic contributions, signed authorship |

Together they answer three questions about any artifact:

- **rhizoCrypt**: "What is being worked on right now?" (the ephemeral DAG)
- **loamSpine**: "What happened?" (the permanent record)
- **sweetGrass**: "Who did what, and why does it matter?" (the attribution chain)

The trio operates at a different level than the triad. The triad *coordinates*
across space (gates, membranes, remotes). The trio *records* across time
(sessions, commits, provenance chains). Both are composed from primals.
Neither is a primal itself.

---

## Composition: How the Two Threes Work Together

The triad and trio are not parallel systems — they compose. Every significant
ecosystem operation involves both.

### The Agentic Sync Exemplar

Agentic sync (Wave 66+) is the fullest composition of both groups. When gates
diverge, the ecosystem detects, resolves, and records the resolution using all
six primals:

```
Phase               Triad Member      Trio Member         Primal Calls
─────               ────────────      ───────────         ────────────
1. Detect           qS (SENSE)        —                   potential.diverge
   "biomeGate and eastGate have unique commits on bearDog"

2. Classify         qS (SENSE)        —                   temporal.check
   "fork divergence — neither is ancestor of the other"

3. Record pre-state —                 rhizoCrypt          dag.snapshot
   "capture both HEADs before resolution"

4. Resolve          wF (SYNC)         —                   temporal.sync (merge-ff or merge-rebase)
   "fast-forward biomeGate to eastGate's HEAD"

5. Certify          rP (ACTION)       loamSpine           spine.commit
   "append resolution record to immutable ledger"

6. Sign             rP (ACTION)       —                   crypto.sign (bearDog)
   "Ed25519 signature on resolution certificate"

7. Attribute        —                 sweetGrass          braid.create
   "weave resolution provenance — who resolved, why, what policy"

8. Propagate        wF (SYNC)         —                   temporal.cascade
   "push resolved state to all followers"
```

No step is generic. Every step maps to a specific primal, a specific triad
domain or trio role, and a specific capability call.

### Composition Graphs

biomeOS encodes these compositions as TOML graphs in `primalSpring/graphs/signals/`.
Three graphs implement agentic sync:

| Graph | Triad | Trio | What It Does |
|-------|-------|------|-------------|
| `sync_diverge.toml` | qS | — | Detects divergence, fires SYNC impulse |
| `sync_resolve.toml` | wF + rP | rhizoCrypt + loamSpine + sweetGrass | Resolves with full provenance recording |
| `sync_resolve_crossgate.toml` | wF + rP | + sweetGrass context braids | Cross-gate resolution with federation |

---

## biomeOS and the Neural API

biomeOS is not a member of either group. It is the **composition dispatch layer**
that decomposes high-level operations into sequences of primal capability calls.

```
Spring says:  ctx.signal("nest", "commit", payload)
biomeOS does: load nest_commit.toml
              → dag.dehydrate (rhizoCrypt)
              → crypto.sign (bearDog)
              → content.put (nestGate)
              → spine.commit (loamSpine)
              → braid.create (sweetGrass)
Spring gets:  single composed result
```

The `signal()` API — currently `ctx.signal("tier", "operation", payload)` — is
shorthand for "execute the biomeOS composition graph for this operation." The
method name in code is `signal.dispatch`, but the operation is composition
dispatch: biomeOS routes to primals, not to generic "signals."

### Composition Tiers

biomeOS organizes compositions into tiers that reflect the atomic model:

| Tier | Primals | Domain | Example Compositions |
|------|---------|--------|---------------------|
| **Tower** | bearDog + songbird + skunkBat | Trust boundary | `tower.publish`, `tower.authenticate` |
| **Node** | Tower + toadStool + barraCuda + coralReef | Compute substrate | `node.compute`, `node.validate` |
| **Nest** | Tower + nestGate + rhizoCrypt + loamSpine + sweetGrass | Storage + provenance | `nest.store`, `nest.commit` |
| **NUCLEUS** | Node + Nest (all 10 unique primals) | Full composition | `nucleus.deploy`, `nucleus.status` |
| **Meta** | biomeOS + squirrel + petalTongue | Orchestration/AI/UI | `meta.intent`, `meta.observe` |
| **Ecosystem** | wF compositions (triad + trio) | Cross-gate sync | `sync.diverge`, `sync.resolve` |

32 composition graphs are currently defined in `primalSpring/graphs/signals/`.

---

## Vocabulary

The ecosystem has its own names for its own things. Using generic CS terms
obscures which primal owns an operation, which triad domain coordinates it,
and which trio member records it.

### Canonical Vocabulary Table

| Generic (avoid in whitePaper) | Ecosystem term | Owner |
|-------------------------------|----------------|-------|
| "signal graph" | **composition graph** | biomeOS (dispatch layer) |
| "signal tier" | **composition tier** | biomeOS (Tower/Node/Nest/NUCLEUS/meta/ecosystem) |
| "fire a signal" | `impulse.post` (rP ACTION) or `potential.sense` (qS SENSE) | rootPulse or quorumSignal |
| "signal dispatch" | **biomeOS composition dispatch** | biomeOS Neural API |
| "sync signal" | **waterFall diverge/resolve graph** | wF + rP + trio |
| "auth system" | **bearDog crypto primitives** | bearDog (security domain) |
| "notification" | **impulse propagation** | rP → wF → qS cycle |
| "event bus" / "pub/sub" | **impulse/potential coordination** | impulsePotential (membrane-mediated) |
| "divergence detection" | `potential.diverge` | qS SENSE of the temporal matrix |
| "merge resolution" | **wF resolution with rP provenance recording** | waterFall + rootPulse + trio |
| "message passing" | **JSON-RPC capability calls** | primal-to-primal via UDS |

### When "Signal" Is Acceptable

Three uses of "signal" remain legitimate:

1. **Biological signaling** — gen3 science corpus (quorum sensing signal
   propagation, cytokine signaling, etc.). This is the source domain.
2. **K-Derm Signal channel** — the named outer-membrane communication
   channel in the K-Derm topology.
3. **`signal.dispatch()` API method** — the code-level method name in
   `CompositionContext`. In prose, clarify as "biomeOS composition
   dispatch" where the code name alone might confuse.

---

## Lineage

| Generation | Contribution |
|------------|-------------|
| **gen3** | Provenance trio primals implemented and validated (2,308+ tests) |
| **gen4** | Triad discovered through waterFall design; RootPulse proved trio composition; Neural API connected both |
| **gen5** | Convergence recognized — two threes as unified compositional vocabulary, agentic sync as exemplar |

### Related Documents

| Document | Relationship |
|----------|-------------|
| `waterFall/03_TRIAD_COORDINATION.md` | Triad mechanics in the sync domain |
| `waterFall/09_AGENTIC_SYNC.md` | Agentic sync — fullest composition of both groups |
| `RootPulse/03_PRIMAL_COMPOSITION.md` | Trio mechanics in the provenance domain |
| `neuralAPI/02_ARCHITECTURE.md` | biomeOS composition dispatch architecture |
| `gen5/foundations/IMPULSE_POTENTIAL_COORDINATION.md` | impulsePotential as triad coordination layer |
| `gen5/foundations/CONTEXT_BRAID_PATTERN.md` | sweetGrass external analog |
| `primalSpring/specs/WATERFALL_TEMPORAL_SYNC.md` | Technical specification for waterFall |

---

*"Six primals. Two groups of three. One coordinates across space, the other
records across time. Together they compose every operation the ecosystem
performs. The two threes are not architecture — they are the ecosystem's
grammar. Every sentence the system speaks uses these six words."*
