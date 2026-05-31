# Introduction to waterFall

**What is waterFall and why does it matter?**

**Date**: May 29, 2026
**Status**: Whitepaper — Conceptual Design + Bash Implementation

---

## The Problem

An ecosystem with 13 primals, 8 springs, 38 repositories, and 6+ gates
has a synchronization problem. Teams push evolution from different
workstations to different remotes at different times. Without temporal
awareness, a gate pulling from a stale remote gets zero changes while
the truth sits on another remote 4 commits ahead.

### Traditional Git Sync (Spatial)

```
Day 1:    git pull origin main          → 3 new commits
Day 2:    git pull origin main          → 0 new commits (origin stale)
          git pull forgejo main         → 0 new commits (forgejo also stale)
          truth: a third remote has 4 commits nobody pulled
```

The problem: you pick ONE remote and hope it's current. If it's
reachable but stale, you get nothing. You don't even know you're
behind.

### waterFall Sync (Temporal)

```
Day 1:    fetch ALL remotes
          measure: origin +3, forgejo +0
          pull origin (leader)
          push forgejo (follower)
          → 3 new commits, all remotes converged

Day 2:    fetch ALL remotes
          measure: origin +0, forgejo +4 (someone pushed there)
          pull forgejo (now the leader)
          push origin (now the follower)
          → 4 new commits, all remotes converged
```

The solution: don't pick a remote. Measure all of them. Pull from
whoever is ahead. Push to whoever is behind.

---

## What waterFall Is

waterFall is a **temporal ecosystem sync pattern**. It is the third
domain of the Neural API coordination triad:

| Domain | Biology | Role |
|--------|---------|------|
| quorumSignal | Quorum sensing | SENSE — observe, discover, classify |
| rootPulse | Muscle contraction | ACTION — create, mutate, prove |
| **waterFall** | Autonomic heartbeat | **SYNC** — reconcile, propagate, cohere |

Like rootPulse, waterFall is not a primal. It is what primals do
together — a coordination pattern expressed as TOML graphs, executed
by biomeOS over existing capabilities.

Like the Neural API, waterFall is domain-agnostic. It doesn't care
whether the repos contain Rust code, TOML configs, scientific data,
or game assets. It only cares about temporal position: who's ahead,
who's behind, who's diverged.

---

## The Autonomic Metaphor

Your heartbeat doesn't wait for a coordinator. It doesn't check a
schedule. It maintains coherence continuously, without conscious
intervention. When you exercise (high activity), it speeds up. When
you sleep (low activity), it slows down. If it detects arrhythmia
(divergence), it flags it for attention.

waterFall aims for the same properties:

- **Automatic**: gates sync on a timer, not on manual command
- **Adaptive**: active gates sync more frequently than cold ones
- **Autonomous**: each gate syncs independently, no central coordinator
- **Alerting**: divergences are flagged, not silently merged

The "fall" in waterFall is gravity. Changes flow downhill — from where
they were created to where they're needed. No pumping required.

---

## Core Concepts

### Temporal Position

Every repo × remote pair has a temporal position: how many commits
ahead or behind the local HEAD. waterFall measures all positions
before acting.

```
repo: primals/songBird

  remote      ahead  behind  status
  ──────      ─────  ──────  ──────
  origin         4       0   LEADER
  forgejo        0       0   PARITY
  usb            0       2   FOLLOWER
```

### Three Patterns

The temporal position matrix classifies into exactly three patterns:

1. **converge** — one remote leads, others follow. Safe to automate.
2. **diverge** — multiple remotes have unique commits. Needs review.
3. **parity** — all remotes agree. Update freshness, move on.

### Four Sync Levels

1. **local** — working tree to HEAD (dirty check, stash)
2. **gate** — all repos on one workstation
3. **membrane** — gate to VPS depot
4. **ecosystem** — all membranes, all remotes, all transports

### Wave Model

Sync is not an event; it's a continuous wave. Each gate generates
waves independently. Waves propagate through membranes. Over time,
all gates converge — not because a coordinator tells them to, but
because the temporal model ensures the most recent state always wins.

---

## What waterFall Is NOT

waterFall is NOT:

- **A new version control system** — it uses git refs as-is
- **A centralized sync service** — each gate acts independently
- **A conflict resolution tool** — it detects conflicts, humans resolve them
- **A primal** — it's a coordination pattern over existing primals
- **A replacement for git push/pull** — it orchestrates git operations

waterFall is TO git sync what rootPulse is TO git commits: a
composition pattern that emerges from primal coordination, making
the ecosystem self-maintaining without any single component owning
the process.

---

## The Triad in Practice

A typical evolution cycle:

1. **rP**: ironGate's rhizoCrypt team implements `dag.branch`, pushes to GitHub
2. **qS**: eastGate runs quorumSignal — senses origin is +4, forgejo stale
3. **wF**: eastGate's waterFall pulls from origin (leader), pushes to forgejo (follower)
4. **qS**: southGate runs quorumSignal — sees forgejo is now current
5. **wF**: southGate's waterFall reports parity — no action needed

No subsystem called the others. They share one language: git refs.
qS reads them. rP writes them. wF propagates them.

---

## Reading Path

**For ecosystem operators**: Start with [02_ARCHITECTURE.md](./02_ARCHITECTURE.md) for sync levels and patterns

**For primal/spring teams**: Start with [03_TRIAD_COORDINATION.md](./03_TRIAD_COORDINATION.md) for how your pushes flow through the ecosystem

**For infrastructure**: Start with [05_IMPLEMENTATION.md](./05_IMPLEMENTATION.md) for the cascade-pull evolution path

**For airgap/WAN deployments**: Start with [06_AIRGAP_FEDERATION.md](./06_AIRGAP_FEDERATION.md) for depot and USB patterns

---

*"The ecosystem does not need a coordinator. It needs temporal awareness.
The DAG is the only clock that matters."*
