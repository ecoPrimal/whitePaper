# Impulse/Potential Coordination — Triad Integration

**Gen5 Foundation** (evolved from gen4 FRAGO patterns → Wave 66 SYNC impulses + divergence policy)
**See also**: `FUNCTIONAL_PATTERN_CONVERGENCE.md` — canonical triad/trio vocabulary

---

## Evolution from Gen4

Gen4 introduced FRAGO (Fragmentary Order) as an ad-hoc coordination
mechanism — handoff blurbs pasted between gates. Gen5 graduates this to
a formal Neural API triad integration:

| Gen4 | Gen5 |
|------|------|
| FRAGO handoff blurbs | `impulse.post` — structured, git-mediated impulses |
| Manual status checks | `potential.sense` — automated membrane gradient sensing |
| Copy-paste coordination | Context braids — ephemeral state weaving across mesh |
| Legacy signal shim (removed Wave 66) | Impulse/Potential modules with provenance trio |

---

## The Coordination Triad

Three primals form a closed coordination loop (see `FUNCTIONAL_PATTERN_CONVERGENCE.md`
for the canonical definition):

```
quorumSignal (SENSE)          rootPulse (ACTION)          waterFall (SYNC)
─────────────────────         ─────────────────           ────────────────
potential.sense               impulse.post                temporal.cascade
potential.check               impulse.ack                 temporal.sync
                              impulse.archive             temporal.check
```

### quorumSignal — Sense
Measures the state of the membrane. "What's happening across the mesh?"
- `potential.sense` reads pending impulses, mesh state, context braids
- `potential.check` validates gradient health across all reachable gates
- Pure observation — no side effects

### rootPulse — Action
Fires discrete impulses that propagate through the membrane:
- `impulse.post` creates a time-bounded, typed impulse (FRAGO, STATUS, AAR, RELEASE, SYNC)
- `impulse.ack` acknowledges receipt and optionally responds
- `impulse.archive` discharges spent impulses
- Directional, carries payload, auto-links to git commits

### waterFall — Sync
Keeps the distributed workspace converged:
- `temporal.cascade` syncs all repos from manifest profiles
- `temporal.sync` handles individual repo sync
- `temporal.check` reports parity without modifying state

---

## Context Braids — The Provenance Trio External Analog

Three layers of coordination, each with a different lifetime:

| Layer | Internal Analog | External Pattern | Lifetime |
|-------|-----------------|------------------|----------|
| **Git** | loamSpine ledger | Commits, permanent record | Forever |
| **Impulses** | rhizoCrypt DAG sessions | Event-driven directives | Time-bounded |
| **Context** | sweetGrass braids | Ephemeral developer state | Auto-decay |

### Provenance Trio Integration

The three provenance primals (loamSpine, rhizoCrypt, sweetGrass) each
have an external coordination analog:

```
Internal (primal data)              External (gate coordination)
─────────────────────               ─────────────────────────────
loamSpine ledger                ←→  Git commits (permanent history)
  → anchoring, DID resolution       → waterFall sync, temporal position
  → immutable, append-only           → immutable, append-only

rhizoCrypt DAG sessions         ←→  Impulses (fire, propagate, ack)
  → content-addressable, DAG         → git-mediated, typed, directional
  → session-scoped, purgeable         → time-bounded, archivable

sweetGrass braids               ←→  Context braids (weave, sense, clear)
  → W3C PROV-O, signed               → TOML, superseding, ephemeral
  → artifact provenance               → developer state provenance
```

---

## Impulse Lifecycle

```
Gate A                      Forgejo (periplasm)              Gate B
──────                      ────────────────────             ──────
impulse.post ──push────────▶ impulses/active/   ◀──pull──── cascade-pull
  │                                                           │
  │ commits to impulses/       (rides waterFall)       potential.sense
  │ auto-links rootPulse ref                                  │
  │                                                    reads pending
  ▼                                                           ▼
FRAGO|STATUS|AAR|RELEASE                               impulse.ack
  in TOML format                                         │
                                                         ▼
                                                  archive when spent
```

### Impulse Types

| Type | Purpose | Urgency | Triad Owner |
|------|---------|---------|-------------|
| `frago` | Amend existing directive | High — action required | rP ACTION |
| `status` | Report gate state | Medium — informational | rP ACTION |
| `aar` | After-action review | Low — retrospective | rP ACTION |
| `release` | Announce deployment | Medium — awareness | rP ACTION |
| `sync` | Divergence detected — resolution needed | High — automated or agentic | wF SYNC → rP ACTION |

### SYNC Impulses (Wave 66+)

SYNC impulses are fired automatically by `temporal.cascade` when divergence is
detected and `diverge_impulse = true` in the ecosystem manifest. They differ
from other impulse types in three ways:

1. **Machine-generated**: fired by `membrane temporal.cascade`, not by a human
2. **Payload-rich**: carry structured divergence context (repo, remotes, HEADs,
   divergence type, suggested action)
3. **Policy-governed**: the receiving gate's response depends on the repo's
   `divergence_policy` in `ecosystem_manifest.toml`

#### SYNC Impulse Payload

```toml
[impulse.payload]
repo = "primals/bearDog"
diverge_type = "fork"           # fork | drift | conflict
remote_a = "origin"
remote_b = "forgejo"
head_a = "a58a676c"
head_b = "b3c4d5e6"
common_ancestor = "9f8e7d6c"
suggested_action = "merge-ff"   # merge-ff | merge-rebase | flag | escalate
```

#### Divergence Policy Engine

Each repo in the ecosystem manifest declares a `divergence_policy` that governs
automated resolution behavior. The policy is a graduated scale from passive
observation to full agentic resolution:

| Policy | Behavior | Automation Level |
|--------|----------|-----------------|
| `flag` (default) | Report divergence, take no action | Human reviews |
| `merge-ff` | Fast-forward if one side is a strict ancestor | Safe automation |
| `merge-rebase` | Rebase on leader, fall back to flag on conflict | Moderate automation |
| `impulse-only` | Fire SYNC impulse, do not attempt resolution | Coordination only |
| `agentic` | Full resolution via `sync_resolve.toml` composition graph with provenance recording | Future: squirrel-assisted |

Policies are declared per-repo in the manifest:

```toml
[repos.plasmidBin]
divergence_policy = "merge-ff"

[repos.sporePrint]
divergence_policy = "impulse-only"
```

The policy engine runs inside `temporal.cascade` (membrane-shadow `temporal.rs`).
When a divergence is detected and the policy permits automated resolution, the
engine attempts resolution and records the outcome. When the policy is `agentic`,
the engine delegates to the `sync_resolve.toml` composition graph, which records
the pre-state in rhizoCrypt, performs the merge, certifies the result in loamSpine,
and attributes the resolution in sweetGrass.

---

## Wave 66 Implementation State

| Component | Module | Status |
|-----------|--------|--------|
| Impulse engine (FRAGO/STATUS/AAR/RELEASE/SYNC) | `membrane-shadow/src/impulse.rs` | Operational — SYNC type added Wave 66 |
| SYNC impulse posting (`post_sync_diverge`) | `membrane-shadow/src/impulse.rs` | Operational — auto-fires on divergence |
| Divergence policy engine | `membrane-shadow/src/temporal.rs` | Operational — flag/merge-ff/merge-rebase/impulse-only |
| Context braids | `membrane-shadow/src/context.rs` | Operational |
| Temporal cascade + policy dispatch | `membrane-shadow/src/temporal.rs` | Operational — manifest-driven policy |
| Remote exclusion (`exclude_remotes`) | `membrane-shadow/src/temporal.rs` | Operational — per-repo in manifest |
| Manifest agentic sync fields | `membrane-shadow/src/manifest.rs` | Operational — `divergence_policy`, `exclude_remotes`, `diverge_impulse` |
| Git operations | `membrane-shadow/src/git_ops.rs` | Shared infra |
| CLI parsing | `membrane-shadow/src/cli.rs` | Shared infra |
| Command dispatch | `membrane-shadow/src/dispatch.rs` | Router |

---

## Key Files

| File | Purpose |
|------|---------|
| `wateringHole/IMPULSE_POTENTIAL_STANDARD.md` | Canonical standard (includes SYNC impulse type) |
| `wateringHole/CONTEXT_BRAID_STANDARD.md` | Context braid spec |
| `wateringHole/WATERFALL_PATTERN.md` | Sync architecture |
| `wateringHole/ecosystem_manifest.toml` | Manifest — `divergence_policy`, `exclude_remotes`, `diverge_impulse` |
| `primalSpring/config/capability_registry.toml` | Impulse/potential/temporal methods + composition tiers |
| `primalSpring/graphs/signals/sync_diverge.toml` | qS composition graph — divergence detection + SYNC impulse |
| `primalSpring/graphs/signals/sync_resolve.toml` | wF + rP composition graph — resolution with provenance trio |
| `primalSpring/graphs/signals/sync_resolve_crossgate.toml` | Cross-gate resolution with federation |
| `cellMembrane/crates/membrane-shadow/src/impulse.rs` | Rust implementation (including `post_sync_diverge`) |
| `cellMembrane/crates/membrane-shadow/src/temporal.rs` | Cascade engine with policy dispatch |
| `cellMembrane/crates/membrane-shadow/src/context.rs` | Context braids |

---

## Related Documents

| Document | Relationship |
|----------|-------------|
| `FUNCTIONAL_PATTERN_CONVERGENCE.md` | Canonical triad/trio vocabulary and composition model |
| `waterFall/09_AGENTIC_SYNC.md` | Full agentic sync paper |
| `waterFall/08_IMPULSE_POTENTIAL.md` | impulsePotential as waterFall extension |
| `primalSpring/specs/WATERFALL_TEMPORAL_SYNC.md` | Technical specification for temporal sync |
