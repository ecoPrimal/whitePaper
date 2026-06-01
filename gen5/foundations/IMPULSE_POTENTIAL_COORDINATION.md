# Impulse/Potential Coordination — Neural API Triad Integration

**Gen5 Foundation** (evolved from gen4 signal/FRAGO patterns)

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
| Signal module (deprecated) | Impulse/Potential modules with provenance trio |

---

## The Neural API Triad

Three coordination patterns map to three primal capabilities:

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
Fires discrete events that propagate through the membrane:
- `impulse.post` creates a time-bounded, typed impulse (FRAGO, STATUS, AAR, RELEASE)
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

| Type | Purpose | Urgency |
|------|---------|---------|
| `frago` | Amend existing directive | High — action required |
| `status` | Report gate state | Medium — informational |
| `aar` | After-action review | Low — retrospective |
| `release` | Announce deployment | Medium — awareness |

---

## Wave 65 Implementation State

| Component | Module | Lines | Status |
|-----------|--------|-------|--------|
| Impulse engine | `membrane-shadow/src/impulse.rs` | 712 | Operational |
| Context braids | `membrane-shadow/src/context.rs` | 464 | Operational |
| Temporal cascade | `membrane-shadow/src/temporal.rs` | 638 | Operational |
| Git operations | `membrane-shadow/src/git_ops.rs` | 94 | Shared infra |
| CLI parsing | `membrane-shadow/src/cli.rs` | 176 | Shared infra |
| Command dispatch | `membrane-shadow/src/dispatch.rs` | 709 | Router |
| Signal (deprecated) | `membrane-shadow/src/signal.rs` | 20 | Shim → remove Wave 66 |

---

## Key Files

| File | Purpose |
|------|---------|
| `wateringHole/IMPULSE_POTENTIAL_STANDARD.md` | Canonical standard |
| `wateringHole/CONTEXT_BRAID_STANDARD.md` | Context braid spec |
| `wateringHole/WATERFALL_PATTERN.md` | Sync architecture |
| `primalSpring/config/capability_registry.toml` | Impulse/potential methods |
| `cellMembrane/crates/membrane-shadow/src/impulse.rs` | Rust implementation |
| `cellMembrane/crates/membrane-shadow/src/context.rs` | Context braids |
