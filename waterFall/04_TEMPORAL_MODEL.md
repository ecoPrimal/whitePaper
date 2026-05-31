# The Temporal Model

**Waves, DAG clocks, and convergence dynamics**

**Date**: May 29, 2026
**Status**: Whitepaper — Formal Model

---

## The DAG as Clock

Git's directed acyclic graph encodes a partial order over all events.
This partial order is sufficient for all sync decisions:

```
A partial order ≤ on commits satisfies:

  Reflexive:     c ≤ c
  Antisymmetric: if c₁ ≤ c₂ and c₂ ≤ c₁, then c₁ = c₂
  Transitive:    if c₁ ≤ c₂ and c₂ ≤ c₃, then c₁ ≤ c₃

  c₁ ≤ c₂ iff c₁ is an ancestor of c₂ in the DAG
  c₁ ∥ c₂ (concurrent) iff neither c₁ ≤ c₂ nor c₂ ≤ c₁
```

This partial order maps directly to temporal patterns:

| DAG relationship | Temporal pattern | Sync action |
|-----------------|-----------------|-------------|
| `local ≤ remote` | BEHIND — remote leads | Pull (fast-forward) |
| `remote ≤ local` | AHEAD — local leads | Push |
| `local = remote` | PARITY | No-op |
| `local ∥ remote` | DIVERGED — concurrent | Flag for review |

No wall-clock time needed. No NTP. No vector clocks. The DAG carries
all temporal information in its structure.

---

## Wave Dynamics

### Single Gate Wave

A wave is a single sync cycle on one gate. It has three phases:

```
Wave W on gate G at time T:

  Phase 1 (qS):  ∀ repo ∈ profile(G):
                    ∀ remote ∈ remotes(repo):
                      fetch(remote)
                      measure(ahead, behind)
                    classify(converge | diverge | parity)

  Phase 2 (wF):  ∀ repo where classify = converge:
                    pull(leader_remote)
                    ∀ remote where behind(remote) > 0:
                      push(remote)

  Phase 3:        publish(freshness)
```

Complexity: O(R × M) where R = repos, M = remotes per repo.
For eastGate: O(38 × 2) = 76 fetch + measure operations.

### Multi-Gate Convergence

Given N gates with wave period P, the convergence time for a single
push event is bounded:

```
T_convergence ≤ (D + 1) × P

where:
  D = diameter of the remote topology graph
  P = wave period

For the current topology:
  D = 2 (gate → GitHub ← VPS → other gate)
  P = 15 min
  T_convergence ≤ 45 min worst case
```

In practice, convergence is faster because:
- The VPS Forgejo is a central hub (D = 1 for most paths)
- Gates can sync on-demand (P → 0 for manual triggers)
- Mesh-published freshness lets gates skip unnecessary fetches

### Convergence Guarantee

**Claim**: If no new commits are pushed, all gates converge within
`(D + 1) × P` time, assuming all gates are online and all remotes
are reachable.

**Proof sketch**: After one wave, the gate that pushed the commit
has propagated it to all its reachable remotes. After a second wave,
any gate that shares a remote with the first gate has received the
commit and propagated it to its remotes. After D + 1 waves, every
gate reachable through the remote topology has the commit.

**Divergence**: If two gates push different commits to different
remotes between waves, the system detects DIVERGE and flags it.
Convergence requires human resolution of the divergence, after which
the next wave completes convergence.

---

## Freshness Semantics

### Point-in-Time Freshness

Freshness is a snapshot of the temporal position matrix at the time
of measurement. It answers: "As of time T, what did gate G see?"

```toml
[wave]
id = 61
gate = "eastGate"
measured = "2026-05-29T16:04:00Z"

[repos."primals/songBird"]
local = "a58a676c"
origin = "a58a676c"
forgejo = "a58a676c"
pattern = "parity"
```

Freshness is NOT a guarantee of current state — it's a snapshot that
becomes stale as new commits are pushed. The staleness bound is the
wave period.

### Mesh-Published Freshness

When gate G publishes freshness to the songbird mesh, other gates can
use it as a hint:

```
Gate A publishes: "primals/songBird is at a58a676c on forgejo"
Gate B reads hint: "forgejo probably has a58a676c — skip fetch if
                    my local HEAD matches"
```

This is an optimization. Gate B can always fall back to fetching.
The hint saves one fetch round-trip per repo that's already current.

### Freshness Decay

A freshness snapshot decays over time. The decay rate depends on
the repo's activity:

| Activity level | Repos | Decay rate |
|---------------|-------|-----------|
| Hot (daily pushes) | primals/*, springs/* | High — stale within hours |
| Warm (weekly pushes) | gardens/*, infra/* | Medium — stale within days |
| Cold (monthly pushes) | gen1/, gen2/ | Low — stale within weeks |

waterFall could use activity history to set per-repo sync priority,
checking hot repos more frequently than cold ones. This is an adaptive
optimization for Phase 3.

---

## Divergence Resolution

When temporal measurement detects DIVERGE, waterFall does NOT
auto-resolve. The resolution model:

### Detect

```
primals/rhizoCrypt:
  origin:  a1b2c3 (has commits X, Y unique to origin)
  forgejo: d4e5f6 (has commits P, Q unique to forgejo)
  local:   g7h8i9 (behind both)

  Pattern: DIVERGE
```

### Report

waterFall produces a human-readable divergence report:

```
DIVERGE primals/rhizoCrypt
  origin  has 2 commits not on forgejo: X ("dag.branch impl"), Y ("tests")
  forgejo has 2 commits not on origin:  P ("config fix"), Q ("docs update")
  Resolution options:
    1. Merge origin into forgejo (preserves both histories)
    2. Merge forgejo into origin (preserves both histories)
    3. Rebase one onto the other (rewrites one history)
    4. Manual review: git log --oneline --graph origin/main forgejo/main
```

### Resolve (Human or quorumSignal)

Today: the operator picks a resolution strategy.

Future: quorumSignal could assess whether the divergence is safe to
auto-merge (no conflicting file changes) or requires human review
(same files modified differently).

### Re-converge

After resolution, the next waterFall wave sees the repo back in
CONVERGE or PARITY state and propagates the merged result to all
remotes.

---

## Formal Properties

### Safety

waterFall never creates commits. It only moves branch pointers forward
(fast-forward) or reports that it cannot. This means:

- **No data loss**: existing commits are never removed
- **No silent merge**: divergence is always reported
- **No force push**: branch protection is respected
- **History preservation**: the DAG only grows, never shrinks

### Liveness

Assuming eventually-reachable remotes and finite wave periods:

- **Eventually consistent**: all gates converge to the same HEAD
  for each repo, given no new divergence
- **Bounded delay**: convergence time ≤ (D + 1) × P
- **Progress**: each wave reduces total drift (sum of behind counts)
  by at least the minimum drift of any convergeable repo

### Partition Tolerance

During network partitions:

- Gates continue to sync with reachable remotes
- Unreachable remotes are skipped, not failed
- When partition heals, next wave discovers and reconciles drift
- If both sides evolved independently → DIVERGE is detected

This gives waterFall the same CAP characteristics as git itself:
AP (available + partition-tolerant), eventually consistent.

---

## Next Reading

- **[05_IMPLEMENTATION.md](./05_IMPLEMENTATION.md)** — Concrete implementation path
- **[06_AIRGAP_FEDERATION.md](./06_AIRGAP_FEDERATION.md)** — How this works without network
- **[03_TRIAD_COORDINATION.md](./03_TRIAD_COORDINATION.md)** — Triad cycle in practice

---

*"The DAG is the clock. Waves are the heartbeat. Convergence is
the emergent property of independent temporal awareness."*
