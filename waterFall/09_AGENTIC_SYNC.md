# Agentic Sync — Provenance-Aware Divergence Resolution

**When the ecosystem resolves its own conflicts**

**Date**: June 1, 2026
**Status**: Whitepaper — Wave 66 implementation
**Prerequisites**: `03_TRIAD_COORDINATION.md`, `05_IMPLEMENTATION.md`, `08_IMPULSE_POTENTIAL.md`
**Vocabulary**: `gen5/foundations/FUNCTIONAL_PATTERN_CONVERGENCE.md`

---

## The Problem That Agentic Sync Solves

waterFall's temporal sync protocol handles three patterns: convergence (safe to
automate), parity (nothing to do), and divergence (danger). Through Wave 65,
divergence was a wall — waterFall flagged it and stopped. Resolution required a
human to inspect both sides, decide which commits to keep, merge or rebase, push
the result, and hope the provenance chain wasn't broken.

This approach has three flaws:

1. **Lossy**: ad-hoc `git push --force` or manual rebase discards history. The
   fact that a divergence occurred — and how it was resolved — is not recorded
   anywhere in the ecosystem's provenance chain.

2. **Non-agentic**: a human relay step in the middle of an otherwise autonomous
   sync pipeline. Every divergence breaks the waterFall heartbeat until someone
   manually intervenes.

3. **Ungraded**: every divergence is treated identically. A trivial
   fast-forward-able drift (one side has extra commits, the other has none)
   receives the same treatment as a genuine fork (both sides introduced unique
   commits that conflict).

Agentic sync addresses all three.

---

## The Five Phases

### Phase 1: Structural Fixes

Before the policy engine could work, the ecosystem needed structural repairs:

- **plasmidBin CI**: the `auto-harvest.yml` GitHub Action pushed to origin
  but not to Forgejo, creating systematic divergence on every harvest cycle.
  Fixed: harvest now pushes to both remotes.
- **sporePrint CI**: same pattern — `auto-refresh.yml` pushed to origin only.
  Fixed: conditional push to Forgejo sovereign primary.
- **rustChip upstream noise**: the `upstream` remote pointed to an unrelated
  Rust toolchain repository, polluting temporal checks. Fixed: remote removed,
  `exclude_remotes = ["upstream"]` added to manifest.

These are not agentic sync features. They are prerequisites — divergence
caused by structural CI gaps, not by concurrent development.

### Phase 2: SYNC Impulses

When `temporal.cascade` detects divergence and `diverge_impulse = true` in the
manifest `[sync]` section, the cascade engine fires a SYNC impulse.

A SYNC impulse is an rP ACTION — it creates a structured TOML artifact that
propagates through waterFall alongside code:

```toml
[impulse]
id = "2026-06-01T08-30_eastGate__sync-diverge-bearDog"
type = "sync"
wave = 66
subject = "divergence detected: primals/bearDog"

[impulse.payload]
repo = "primals/bearDog"
diverge_type = "fork"
remote_a = "origin"
remote_b = "forgejo"
head_a = "a58a676c"
head_b = "b3c4d5e6"
common_ancestor = "9f8e7d6c"
suggested_action = "merge-ff"

[from]
gate = "eastGate"

[to]
gate = "*"

[status]
state = "pending"
```

The impulse carries enough context for the receiving gate (or agent) to
understand the divergence without re-running temporal checks. The
`suggested_action` is a hint from the detecting gate's policy classification,
not a command.

### Phase 3: Graduated Divergence Policy

The policy engine in `temporal.rs` applies per-repo policies from the
ecosystem manifest:

| Policy | When to Use | What Happens |
|--------|-------------|-------------|
| `flag` | Default — unknown or sensitive repos | Report divergence, no action. Human reviews. |
| `merge-ff` | Binary artifacts, CI-managed repos | If one side is a strict ancestor of the other, fast-forward. Otherwise fall through to flag. |
| `merge-rebase` | Active development repos | Rebase local on the leader remote. On conflict, fall through to flag. |
| `impulse-only` | Content repos, external collaboration | Fire SYNC impulse. Do not attempt merge. Coordination only. |
| `agentic` | Future — squirrel-assisted repos | Delegate to `sync_resolve.toml` composition graph with full provenance recording. |

The policy is a graduated scale. Repos start at `flag` (safest) and graduate
to higher automation levels as confidence grows. The manifest is the single
source of truth for which repos trust which level of automation.

### Phase 4: Provenance-Recorded Resolution

When the policy permits resolution (merge-ff, merge-rebase, or agentic), the
resolution is recorded using the provenance trio:

```
Step              Trio Member      What It Records
────              ───────────      ───────────────
Pre-state         rhizoCrypt       Snapshot both HEADs before resolution
Resolution        —                The merge/rebase itself (git operation)
Certification     loamSpine        Immutable record: "divergence resolved, here's the proof"
Signing           bearDog          Ed25519 signature on the resolution certificate
Attribution       sweetGrass       PROV-O braid: who resolved, which policy, what changed
```

This means the ecosystem can answer questions that ad-hoc force-push cannot:

- "When did bearDog diverge between origin and forgejo?"
- "Which policy governed the resolution?"
- "Who (or what agent) performed the merge?"
- "What was the state before resolution?"
- "Is the resolution cryptographically signed?"

### Phase 5: Cross-Gate Resolution

When divergence spans multiple gates — eastGate is ahead of forgejo, but
biomeGate is ahead of eastGate on a different repo — resolution requires
federation:

```
sync_resolve_crossgate.toml composition graph:

  load_context_braid (sweetGrass)
      → "what is each gate working on?"
  discover_peer (songbird)
      → "which gates have relevant state?"
  diff_remote_state (rhizoCrypt)
      → "what does each gate know that others don't?"
  sync_resolve (the base resolution graph)
      → standard resolve with provenance recording
  federate_resolution (songbird)
      → push resolved state across the mesh
```

Cross-gate resolution uses sweetGrass context braids to understand *why*
each gate diverged — not just the commit difference, but the developer
intent behind the commits. This is the difference between merging code and
merging work.

---

## Composition Graph Detail

Three biomeOS composition graphs implement agentic sync. All are defined in
`primalSpring/graphs/signals/` and validated by the `s_atomic_signals` scenario.

### sync_diverge.toml — qS SENSE

Detects divergence and fires SYNC impulses.

| Node | Primal | Capability | Triad |
|------|--------|-----------|-------|
| resolve_profile | biomeOS | manifest.gate_profile | — |
| fetch_heads | membrane | temporal.check | qS |
| classify_divergence | membrane | temporal.classify | qS |
| fire_sync_impulse | membrane | impulse.post | rP |
| publish_drift | songbird | mesh.publish | — |

Coordination: ecosystem tier, waterFall domain.

### sync_resolve.toml — wF SYNC + rP ACTION

Resolves divergence with full provenance recording.

| Node | Primal | Capability | Trio |
|------|--------|-----------|------|
| load_sync_impulse | membrane | impulse.read | — |
| record_pre_state | rhizoCrypt | dag.snapshot | Working DAG |
| execute_merge | membrane | temporal.sync | — |
| certify_resolution | loamSpine | spine.commit | Immutable ledger |
| sign_certificate | bearDog | crypto.sign | — |
| attribute_resolution | sweetGrass | braid.create | Attribution |
| acknowledge_impulse | membrane | impulse.ack | — |
| cascade_push | membrane | temporal.cascade | — |

Coordination: ecosystem tier, waterFall domain. Integrates the `provenance_trio`
fragment — the trio's recording steps are not optional when resolution is
agentic.

### sync_resolve_crossgate.toml — Cross-gate federation

Extends sync_resolve with peer discovery and context braids.

| Node | Primal | Capability | What It Adds |
|------|--------|-----------|-------------|
| load_context_braid | sweetGrass | context.sense | Gate working state |
| discover_peer | songbird | mesh.discover | Peer gate enumeration |
| diff_remote_state | rhizoCrypt | dag.diff | Cross-gate DAG comparison |
| *(all sync_resolve nodes)* | | | Base resolution |
| federate_resolution | songbird | mesh.federate | Push across mesh |

Coordination: ecosystem tier, waterFall domain with songbird mesh transport.

---

## Triad + Trio Composition Map

Every step in agentic sync maps to a specific owner. No generic "signals":

```
                    TRIAD                           TRIO
                    ─────                           ────
Detect     ──►  qS (potential.diverge)
Classify   ──►  qS (temporal.classify)
Fire       ──►  rP (impulse.post SYNC)
                                            Record pre ──► rhizoCrypt (dag.snapshot)
Resolve    ──►  wF (temporal.sync)
                                            Certify    ──► loamSpine (spine.commit)
Sign       ──►  rP (crypto.sign)
                                            Attribute  ──► sweetGrass (braid.create)
Propagate  ──►  wF (temporal.cascade)
Sense      ──►  qS (potential.sense)        ... cycle continues
```

---

## Manifest Fields Reference

All agentic sync configuration lives in the ecosystem manifest:

```toml
[sync]
diverge_impulse = true              # global: fire SYNC impulses on divergence

[repos.example]
divergence_policy = "merge-ff"      # per-repo: flag | merge-ff | merge-rebase | impulse-only | agentic
exclude_remotes = ["upstream"]      # per-repo: remotes to ignore in temporal checks
```

---

## What This Enables

1. **Provenance-complete history**: every divergence and resolution is recorded
   in the trio — rhizoCrypt snapshots, loamSpine certifications, sweetGrass
   attributions
2. **Graduated trust**: repos start at `flag`, graduate to `merge-ff`, then
   `agentic` as confidence grows
3. **Structural divergence elimination**: CI workflows now push to both remotes,
   preventing the class of divergence that plasmidBin and sporePrint exhibited
4. **Agent-ready coordination**: SYNC impulses carry structured payloads that
   squirrel (or any agent) can consume via `potential.sense` and resolve via
   `sync_resolve.toml`
5. **Cross-gate awareness**: context braids flowing through resolution give
   agents visibility into developer intent, not just commit diffs

---

## Next Reading

- **[05_IMPLEMENTATION.md](./05_IMPLEMENTATION.md)** — The cascade engine internals
- **[08_IMPULSE_POTENTIAL.md](./08_IMPULSE_POTENTIAL.md)** — impulsePotential layer
- **[03_TRIAD_COORDINATION.md](./03_TRIAD_COORDINATION.md)** — Triad mechanics
- **[gen5/foundations/FUNCTIONAL_PATTERN_CONVERGENCE.md](../gen5/foundations/FUNCTIONAL_PATTERN_CONVERGENCE.md)** — The Two Threes

---

*"Divergence is not failure — it is the ecosystem discovering that two gates
evolved independently. The question is not whether divergence happens, but
whether the ecosystem remembers how it was resolved. Ad-hoc force-push
forgets. Agentic sync remembers — in rhizoCrypt, in loamSpine, in sweetGrass.
The provenance chain is unbroken."*
