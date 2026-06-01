# Triad Coordination

**How quorumSignal, rootPulse, and waterFall work together**

**Date**: June 1, 2026 (updated Wave 66)
**Status**: Whitepaper — Coordination Design
**Vocabulary**: `gen5/foundations/FUNCTIONAL_PATTERN_CONVERGENCE.md`

---

## The Nervous System Analogy

The coordination triad maps to the biological nervous system:

```
                    ┌──────────────────────┐
                    │    Sensory Input      │
                    │   (quorumSignal)      │
                    │                      │
                    │  "origin is +4"      │
                    │  "forgejo is stale"  │
                    │  "rhizoCrypt has     │
                    │   dag.branch now"    │
                    └──────────┬───────────┘
                               │ afferent
                               ↓
                    ┌──────────────────────┐
                    │    Integration        │
                    │    (Neural API)       │
                    │                      │
                    │  graph.execute()      │
                    │  capability.call()    │
                    │  routing weights      │
                    └────────┬─────┬───────┘
                             │     │
                   efferent  │     │ autonomic
                             ↓     ↓
              ┌──────────────┐     ┌──────────────┐
              │  Motor Output│     │  Homeostasis  │
              │  (rootPulse) │     │  (waterFall)  │
              │              │     │               │
              │  commit      │     │  converge     │
              │  branch      │     │  propagate    │
              │  merge       │     │  cohere       │
              │  federate    │     │               │
              └──────────────┘     └───────────────┘
```

- **quorumSignal** (afferent): senses the state of all remotes, discovers
  capabilities, classifies drift
- **rootPulse** (efferent): creates versioned artifacts, pushes to nearest
  membrane
- **waterFall** (autonomic): maintains coherence without conscious
  intervention, propagates changes across membranes

The Neural API is the integration layer — it doesn't belong to any
domain but serves all three.

---

## The Triad Cycle

A complete ecosystem evolution cycle passes through all three domains:

### Phase 1: rP (action) — Teams Create

```
ironGate                          GitHub
   │                                │
   │  rhizoCrypt team implements    │
   │  dag.branch, commits, pushes   │
   │──────────────────────────────→│
   │                                │
   │  rootPulse graph:              │
   │  dehydrate → sign → store →   │
   │  commit → attribute            │
   │                                │
```

The team pushes to their nearest membrane (GitHub). They don't think
about other gates. They don't think about Forgejo. They just create.

### Phase 2: qS (sense) — Gates Observe

```
eastGate
   │
   │  fetch all remotes
   │  ├── origin:  a58a676c (+4)
   │  ├── forgejo: a6ef1ec8 (+0)
   │  └── local:   a6ef1ec8
   │
   │  Classification:
   │  ├── songBird:   CONVERGE (origin leads)
   │  ├── rhizoCrypt: CONVERGE (origin leads)
   │  ├── toadStool:  CONVERGE (origin leads)
   │  ├── bearDog:    PARITY
   │  └── coralReef:  PARITY
   │
   │  Drift report: 8 repos behind origin
   │
```

Each gate runs quorumSignal independently. No coordination with other
gates. The sense phase only reads — it never modifies state.

### Phase 3: wF (sync) — Ecosystem Converges

```
eastGate                 GitHub              Forgejo
   │                       │                    │
   │  pull 8 from origin   │                    │
   │←──────────────────────│                    │
   │                       │                    │
   │  push 8 to forgejo    │                    │
   │───────────────────────│───────────────────→│
   │                       │                    │
   │  freshness.toml updated                    │
   │  mesh.publish via songbird                 │
   │                       │                    │

southGate (next wave)    GitHub              Forgejo
   │                       │                    │
   │  fetch all remotes    │                    │
   │  ├── origin:  a58a676c│                    │
   │  ├── forgejo: a58a676c│ (now synced!)      │
   │  └── PARITY           │                    │
   │                       │                    │
   │  No action needed     │                    │
   │                       │                    │
```

eastGate's waterFall pulled from origin (leader) and pushed to forgejo
(follower). When southGate wakes up for its next wave, it sees parity
everywhere — the ecosystem has converged.

---

## Temporal Decoupling

The triad domains are temporally decoupled. They never wait for each other:

| Domain | Frequency | Trigger | Duration |
|--------|-----------|---------|----------|
| rP | Continuous | Developer action | Seconds (per commit) |
| qS | Periodic | Timer (15 min) or manual | Seconds (fetch + classify) |
| wF | Periodic | After qS completes | Minutes (38 repos × pull/push) |

A team can rP (push commits) at any time without triggering wF on
other gates. qS runs on its own schedule and discovers what rP did.
wF runs after qS and acts on what qS found.

This temporal decoupling is what enables:
- **Concurrent development**: teams on different gates push simultaneously
- **Async sync**: gates sync on their own schedule
- **Airgap support**: a disconnected gate catches up when reconnected
- **Fault tolerance**: one gate failing doesn't block others

---

## Composition Graphs per Domain

Each triad domain has biomeOS composition graphs (see
`FUNCTIONAL_PATTERN_CONVERGENCE.md` for the canonical vocabulary — these are
composition graphs dispatched by biomeOS, not generic "signals"):

### quorumSignal Compositions (SENSE)

```
ecosystem.check
├── biomeOS:   manifest.gate_profile (resolve repo list)
├── nestGate:  content.fetch_heads (fetch without pull)
└── songbird:  mesh.publish (drift report)
```

### rootPulse Compositions (ACTION)

```
rootpulse.commit
├── rhizoCrypt: dag.dehydrate (collapse DAG to commit)
├── bearDog:    crypto.sign (sign commit)
├── nestGate:   content.put (store content)
├── loamSpine:  spine.commit (append to ledger)
└── sweetGrass: braid.create (attribution)
```

### waterFall Compositions (SYNC)

```
ecosystem.pull
├── biomeOS:   manifest.gate_profile (resolve gate repo list)
├── songbird:  mesh.discover_remotes (enumerate remotes per repo)
├── nestGate:  content.sync (temporal pull from leader)
└── songbird:  mesh.publish (freshness update)

ecosystem.push
├── bearDog:   crypto.verify_ed25519 (verify signatures)
├── nestGate:  content.push (push to forgejo)
├── songbird:  mesh.mirror (GitHub trailing mirror)
└── songbird:  mesh.publish (freshness update)
```

### Agentic Sync Compositions (wF + rP + trio) — Wave 66+

Agentic sync is the fullest triad composition — it uses all three triad
domains and all three provenance trio members in a single operation:

```
sync_diverge (qS SENSE)
├── biomeOS:   manifest.gate_profile
├── membrane:  temporal.check (fetch + classify)
├── membrane:  impulse.post SYNC (fire if diverged)
└── songbird:  mesh.publish (drift + impulse)

sync_resolve (wF SYNC + rP ACTION + provenance trio)
├── membrane:   impulse.read (load SYNC impulse)
├── rhizoCrypt: dag.snapshot (pre-state)
├── membrane:   temporal.sync (merge per policy)
├── loamSpine:  spine.commit (certify resolution)
├── bearDog:    crypto.sign (sign certificate)
├── sweetGrass: braid.create (attribute resolution)
├── membrane:   impulse.ack (close SYNC impulse)
└── membrane:   temporal.cascade (propagate)

sync_resolve_crossgate (extends sync_resolve)
├── sweetGrass: context.sense (gate working state)
├── songbird:   mesh.discover (peer enumeration)
├── rhizoCrypt: dag.diff (cross-gate comparison)
├── *(sync_resolve nodes)*
└── songbird:   mesh.federate (push across mesh)
```

See `09_AGENTIC_SYNC.md` for the full paper on agentic sync design.

All graphs use capability-based routing. No primal names in the graphs.
biomeOS resolves capabilities to primals at runtime.

---

## Cross-Gate Coordination

### Today: Independent Waves

Each gate runs qS + wF independently. Coordination happens through
shared remotes (Forgejo, GitHub). No direct gate-to-gate communication
needed for sync.

### Future: Mesh-Assisted Coordination (Wave 65+)

With cross-gate graph execution, gates can assist each other:

```
eastGate                          southGate
   │                                  │
   │  mesh.publish(freshness)         │
   │─────────────────────────────────→│
   │                                  │
   │  southGate sees drift report     │
   │  from eastGate — knows which     │
   │  repos are fresh without fetch   │
   │                                  │
   │                  qS: check only  │
   │                  repos not in    │
   │                  eastGate's      │
   │                  freshness       │
   │                                  │
```

Mesh-published freshness lets gates skip fetch for repos that another
gate recently confirmed as current. This is an optimization, not a
requirement — gates can always fall back to fetching everything.

---

## Error Handling

| Failure | Triad domain | Response |
|---------|:------------:|----------|
| Remote unreachable | qS | Skip remote, measure remaining |
| Dirty working tree | wF | Stash or skip repo, report |
| Merge conflict | wF | Flag as DIVERGE, report |
| Push rejected | wF | Report, do not force-push |
| All remotes stale | qS | Report PARITY (may be true) |
| SSH key rejected | wF | Report auth failure, skip remote |

waterFall never force-pushes. waterFall never auto-merges diverged
histories. waterFall never modifies the working tree (except
fast-forward pulls). Destructive operations require human decision.

---

## Next Reading

- **[04_TEMPORAL_MODEL.md](./04_TEMPORAL_MODEL.md)** — The wave model in mathematical detail
- **[05_IMPLEMENTATION.md](./05_IMPLEMENTATION.md)** — How to build this
- **[00_INTRODUCTION.md](./00_INTRODUCTION.md)** — Start here if you haven't read the series

---

*"The three domains share one language: git refs. quorumSignal reads
them, rootPulse writes them, waterFall propagates them. The DAG is
the only coordination substrate they need."*
