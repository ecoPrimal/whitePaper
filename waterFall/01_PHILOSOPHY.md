# Philosophy of waterFall

**Temporal sovereignty through async reconciliation**

**Date**: May 29, 2026
**Status**: Whitepaper — Conceptual Foundation

---

## Sovereignty Requires Temporal Independence

A sovereign ecosystem cannot depend on a single point of truth for its
temporal state. If GitHub is the only source, then Microsoft owns your
timeline. If a self-hosted Forgejo is the only source, then the VPS
provider owns your timeline. If your LAN is the only network, then
your ISP owns your timeline.

True sovereignty means every gate holds a complete temporal record and
can independently determine what happened, when, and where. The DAG
— git's directed acyclic graph — already provides this. waterFall
makes it operational across gates.

---

## Principle 1: Temporal Awareness Over Spatial Preference

Traditional sync asks: "Which remote should I pull from?"
This is a spatial question — it selects a location.

Temporal sync asks: "Which remote is furthest ahead?"
This is a temporal question — it selects the most evolved state.

The distinction matters because spatial preference (always use Forgejo,
fall back to GitHub) conflates reachability with currency. A remote
can be reachable and stale. A remote can be unreachable and hold the
latest truth.

waterFall separates the questions:
1. Which remotes are reachable? (connectivity — transport layer)
2. Of those, which has the most recent state? (temporality — DAG layer)
3. After pulling the leader, which remotes are behind? (propagation)

---

## Principle 2: The DAG Is the Only Clock

waterFall never needs wall-clock time, logical clocks, Lamport timestamps,
or vector clocks. Git's DAG already encodes a partial order over all events:

- Commit A is before commit B if A is an ancestor of B
- Commit A and commit B are concurrent if neither is an ancestor of the other
- A fast-forward means the leader's history is a strict superset of the follower's

This partial order is sufficient for sync decisions:
- **converge**: leader's DAG is a superset → fast-forward
- **diverge**: neither is a superset → concurrent histories → merge required
- **parity**: identical DAGs → nothing to do

No external time source. No NTP dependency. No clock skew issues. The
DAG is the clock, and it's embedded in every git repository.

---

## Principle 3: Async Over Coordinated

Synchronous coordination requires all participants to be available at
the same time. This fails for:
- Gates on different continents (WAN latency)
- Gates behind NAT/firewalls (limited reachability)
- Gates that are offline (mobile, airgapped)
- Gates that are asleep (power management)

waterFall is fully asynchronous. Each gate:
1. Wakes up on its own schedule (timer, manual, on-connect)
2. Fetches all reachable remotes
3. Measures temporal position independently
4. Acts on what it found (pull leader, push followers)
5. Goes back to sleep

No gate needs to coordinate with another gate. No gate needs to be
online when another gate syncs. The VPS depot is a convenience (always
reachable, fast), not a requirement (any remote works).

---

## Principle 4: Complementary Membranes

The ecosystem has multiple membranes (GitHub, Forgejo, LAN depot, USB).
These are not competing sources — they are complementary:

```
                    ┌──────────────────────┐
                    │   Ecosystem State    │
                    │   (union of all      │
                    │    remote DAGs)      │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
        ┌─────┴─────┐   ┌─────┴─────┐   ┌─────┴─────┐
        │  GitHub   │   │  Forgejo  │   │ USB depot │
        │  (outer)  │   │  (inner)  │   │ (airgap)  │
        └───────────┘   └───────────┘   └───────────┘
```

Each membrane serves a purpose:
- **GitHub** — global reachability, external collaboration, open-source
- **Forgejo** — sovereign inner membrane, LAN-fast, SSH auth
- **USB depot** — airgap support, cold storage, offline transfer
- **LAN depot** — high-bandwidth local sync, NAS integration

A team pushes to whichever membrane is nearest. waterFall ensures the
truth propagates to all others. The membrane that happens to be ahead
leads; the rest follow. Complementary, not competitive.

---

## Principle 5: Gravity, Not Pumping

Water falls downhill. It doesn't need a pump for the common case. The
energy comes from the difference in height — in our case, the difference
in commit count between leader and follower.

```
Leader (origin +4)        Follower (forgejo +0)
     ┌────┐                    ┌────┐
     │    │                    │    │
     │ H₁ │ ────────────────→  │ H₁ │
     │ H₂ │   4 commits flow   │ H₂ │
     │ H₃ │   downhill via     │ H₃ │
     │ H₄ │   fast-forward     │ H₄ │
     └────┘                    └────┘
```

The common case — one remote ahead, the rest behind — resolves by
gravity. No merge, no rebase, no conflict. Just fast-forward.

The uncommon case — divergence — is like a dam. Water can't flow in
two directions at once. Someone needs to decide which channel to take.
waterFall reports the dam; humans (or future quorumSignal consensus)
break it.

---

## Principle 6: Waves Over Events

Traditional sync is event-driven: "A push happened, trigger a sync."
This requires webhooks, notification services, and always-on listeners.

waterFall is wave-driven: "Every N minutes, check what changed." This
is simpler, more resilient, and works offline:

| Model | Requires | Failure mode | Latency |
|-------|----------|-------------|---------|
| Event-driven | Webhooks, listeners | Silent miss if listener down | ~0 (instant) |
| Wave-driven | Timer (systemd/cron) | Bounded delay (wave period) | ≤ wave period |

The tradeoff is latency: waves have a bounded delay equal to the wave
period. For a 15-minute wave, the worst case is 15 minutes stale. For
most development workflows, this is acceptable. For time-critical
operations, the wave period can be reduced or a manual wave triggered.

The advantage is simplicity: no webhook infrastructure, no notification
bus, no always-on listeners. A gate just wakes up, checks, and acts.

---

## Biological Precedent

### Quorum Sensing in Bacteria

Bacteria don't have a coordinator. Each cell produces and senses
signaling molecules (autoinducers). When enough cells are present,
the concentration crosses a threshold and triggers a collective
response. No leader election. No coordinator. Just temporal
accumulation reaching a quorum.

waterFall's temporal measurement works similarly: each gate
independently measures the state of all remotes. When enough
gates have converged (the concentration of up-to-date gates
crosses a threshold), the ecosystem is coherent. No coordinator
needed.

### Circadian Rhythms

Circadian rhythms are not synchronized by a master clock. Each
cell has its own oscillator. The suprachiasmatic nucleus (SCN)
provides a weak coupling signal (like the VPS depot providing a
convenient sync point), but individual cells maintain their own
rhythms and can free-run without the SCN.

waterFall gates are like cells with their own oscillators. The VPS
provides a convenient common reference, but each gate can free-run
(sync to GitHub, to USB, to LAN depot) without the VPS.

### Tidal Patterns

Tides are driven by gravity, not by a controller. The moon pulls,
water responds. waterFall's "gravity" is the commit-count differential.
Changes flow from where they were created to where they're needed,
driven by the temporal gradient — no controller required.

---

## Anti-Patterns

| Anti-Pattern | Problem | waterFall Alternative |
|-------------|---------|----------------------|
| Single source of truth | SPOF, sovereignty loss | Complementary membranes, temporal leader |
| Always-pull-from-X | Ignores temporality | Measure all, pull leader |
| Manual sync | Doesn't scale to 38 repos × 6 gates | Automated waves |
| Webhook-driven sync | Fragile, requires infrastructure | Timer-driven waves |
| Force push to resolve conflicts | Destroys history | Flag divergence, human resolution |
| Lock-and-update | Blocks concurrent work | Async waves, no locks |

---

## Next Reading

- **[02_ARCHITECTURE.md](./02_ARCHITECTURE.md)** — Sync levels and patterns
- **[04_TEMPORAL_MODEL.md](./04_TEMPORAL_MODEL.md)** — The wave model in detail
- **[06_AIRGAP_FEDERATION.md](./06_AIRGAP_FEDERATION.md)** — Sovereignty under connectivity constraints

---

*"Sovereignty is not about owning one truth. It's about holding all
truths and letting the most evolved state lead."*
