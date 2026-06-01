# waterFall — Temporal Ecosystem Sync

**Asynchronous multi-membrane reconciliation through temporal awareness**

**Updated**: June 1, 2026
**Wave**: 66+
**Vocabulary**: `gen5/foundations/FUNCTIONAL_PATTERN_CONVERGENCE.md`

---

## White Paper Series

waterFall is not a primal. It is a coordination pattern — a set of TOML
composition graphs that biomeOS dispatches over existing primals. Multi-repo
alignment, freshness tracking, divergence resolution, and cross-gate
federation all use the same temporal primitives: fetch, measure, converge,
propagate.

waterFall completes the Neural API coordination triad:

| Domain | Role | Metaphor | What it does |
|--------|------|----------|-------------|
| **quorumSignal** | SENSE | Quorum sensing | Observes, discovers, classifies |
| **rootPulse** | ACTION | Emergent VCS | Creates, mutates, proves |
| **waterFall** | SYNC | Autonomic heartbeat | Reconciles, propagates, maintains coherence |

### Documents

**Core Concepts**

1. **[00_INTRODUCTION.md](./00_INTRODUCTION.md)** — What is waterFall?
2. **[01_PHILOSOPHY.md](./01_PHILOSOPHY.md)** — Temporal sovereignty
3. **[02_ARCHITECTURE.md](./02_ARCHITECTURE.md)** — Sync levels, patterns, remote topology

**Coordination**

4. **[03_TRIAD_COORDINATION.md](./03_TRIAD_COORDINATION.md)** — How qS / rP / wF work together
5. **[04_TEMPORAL_MODEL.md](./04_TEMPORAL_MODEL.md)** — Wave model and the DAG as clock

**Implementation**

6. **[05_IMPLEMENTATION.md](./05_IMPLEMENTATION.md)** — membrane temporal.cascade (Rust production)
7. **[06_AIRGAP_FEDERATION.md](./06_AIRGAP_FEDERATION.md)** — Sneakernet, depot, USB patterns
8. **[07_ROADMAP.md](./07_ROADMAP.md)** — Glacial gate path

**Extensions (Wave 63+)**

9. **[08_IMPULSE_POTENTIAL.md](./08_IMPULSE_POTENTIAL.md)** — The action potential layer: inter-gate coordination riding on waterFall
10. **[09_AGENTIC_SYNC.md](./09_AGENTIC_SYNC.md)** — Provenance-aware divergence resolution (triad + trio composition)

---

## waterFall is NOT a Primal

Fall is what primals DO together across time and space, not what they ARE.

Five existing primals compose the sync stack:

| Primal | Role in waterFall | Current |
|--------|-------------------|---------|
| **biomeOS** | Gate profile resolution, graph execution | `manifest.gate_profile` shipped |
| **nestGate** | Content sync, push, fetch heads | `content.sync` registered, upstream pending |
| **songbird** | Remote discovery, mesh freshness | `mesh.publish` registered, upstream pending |
| **bearDog** | Signature verification on push | `crypto.verify_ed25519` — production |
| **squirrel** | Manifest parsing, gate identity | `ecosystem_manifest.toml` — production |

biomeOS executes graphs over these primals. The graphs define sync
patterns. No new primal needed.

---

## Three Temporal Patterns

For any repo, the relationship between local HEAD and remote HEADs
determines the pattern:

| Pattern | Condition | Action | Automation |
|---------|-----------|--------|------------|
| **converge** | One remote ahead, others behind | Pull leader → push followers | Safe to automate |
| **diverge** | Multiple remotes have unique commits | Flag for human/quorumSignal review | Not automatable |
| **parity** | All remotes at same HEAD | No-op, update freshness | Trivially safe |

The converge pattern is the common case. Teams push to their nearest
membrane (GitHub, Forgejo, LAN depot). waterFall discovers who's ahead
and propagates forward.

---

## Four Sync Levels

| Level | Scope | Boundary |
|-------|-------|----------|
| **local** | Working tree ↔ HEAD | Single repo |
| **gate** | All repos on one workstation | Filesystem |
| **membrane** | Gate ↔ VPS depot | SSH/HTTPS |
| **ecosystem** | All membranes ↔ all remotes | Network + DAG + sneakernet |

See [02_ARCHITECTURE.md](./02_ARCHITECTURE.md) for the full decomposition.

---

## The Wave Model

There is no single sync moment. Waves pass through the ecosystem:

```
Wave N    ironGate rP: team pushes evolution to GitHub
Wave N+1  eastGate qS: fetch all → origin +4, forgejo stale
Wave N+2  eastGate wF: pull origin → push forgejo (converge)
Wave N+3  southGate qS: forgejo now current (parity)
Wave N+4  southGate wF: no-op, freshness confirmed
```

Each gate runs its own waves independently. Fully async. Fully
concurrent. Works across LAN, WAN, airgap. A gate offline for a week
comes back, runs one wave, and converges with everything that happened.

See [04_TEMPORAL_MODEL.md](./04_TEMPORAL_MODEL.md) for the deep dive.

---

## Why waterFall Matters

### The Problem We Hit (May 29, 2026)

8 upstream primals shipped major evolution to GitHub. Our `--source auto`
(Forgejo-first) pulled zero new changes because Forgejo was reachable
but stale. We were spatially correct (Forgejo was up) but temporally
wrong (GitHub had the truth).

The fix: pull from GitHub, push to Forgejo, verify parity. But this
required manual intervention — exactly what autonomic sync should prevent.

### The Solution

`--source temporal` replaces `--source auto`:

1. Fetch ALL remotes (not just the preferred one)
2. Measure temporal position per remote (ahead/behind counts)
3. Pull from the leader (whichever remote is furthest ahead)
4. Push to followers (any remote behind local HEAD after pull)
5. Report divergences that need human attention

The ecosystem doesn't need a coordinator. It needs temporal awareness.

---

## gen4 Context — waterFall as Infrastructure Evolution

waterFall is the infrastructure equivalent of what RootPulse does for
version control and what the Neural API does for primal orchestration.
All three are coordination patterns — not primals, not code — that emerge
from graph execution over existing capabilities.

| Pattern | Domain | Emerges from |
|---------|--------|-------------|
| **RootPulse** | Version control | rhizoCrypt + loamSpine + sweetGrass + bearDog |
| **Neural API** | Primal orchestration | biomeOS capability routing + graph execution |
| **waterFall** | Ecosystem sync | nestGate + songbird + biomeOS + manifest |

Together, these three patterns make the ecosystem self-maintaining:
rootPulse creates versioned artifacts, waterFall propagates them across
gates, and the Neural API orchestrates the primals that do the work.

---

## Implementation Status (June 1, 2026)

| Component | Status |
|-----------|--------|
| `membrane temporal.cascade` | **Production** — Rust engine, manifest-driven, policy dispatch |
| Temporal sync (fetch all, measure, pull leader, push followers) | **Production** |
| Divergence policy engine (flag/merge-ff/merge-rebase/impulse-only) | **Production** — per-repo in manifest |
| SYNC impulse posting (`post_sync_diverge`) | **Production** — auto-fires on divergence |
| Remote exclusion (`exclude_remotes`) | **Production** — per-repo in manifest |
| `ecosystem_manifest.toml` gate profiles | Production — 39 repos, 7 gate profiles |
| `.gate` identity file | Production — replaces hostname heuristic |
| impulsePotential (FRAGO/STATUS/AAR/RELEASE/SYNC) | **Production** — `impulse.post/ack/archive`, `potential.sense/check` |
| Context braids | **Production** — `context.weave/sense/clear` |
| `cascade-pull.sh` → `potential.sense` | **Production** — auto-triggers after sync |
| NeuralBridge (membrane-shadow) | **Implemented** — feature-gated try-primal-first routing |
| bearDog impulse signing | **Implemented** — optional Ed25519 via UDS |
| songbird impulse relay | **Implemented** — optional mesh.publish via UDS |
| Composition graphs (32 defined) | **Defined** — including `sync_diverge`, `sync_resolve`, `sync_resolve_crossgate` |
| Freshness mesh (songbird) | Not started |
| Cross-gate temporal coordination | Spec + composition graphs defined |
| Airgap/USB remote support | Conceptual — protocol-agnostic by design |

---

## Related Work

- **[Spore-waterFall Mass-Energy Duality](../gen4/architecture/SPORE_WATERFALL_MASS_ENERGY.md)** — Paper 23 realized: spores as mass, waterFall as energy, braids as information
- **[RootPulse](../RootPulse/)** — Emergent VCS (ACTION domain of the triad)
- **[Neural API](../neuralAPI/)** — Orchestration layer (executes waterFall graphs)
- **[WATERFALL_TEMPORAL_SYNC.md](../../springs/primalSpring/specs/WATERFALL_TEMPORAL_SYNC.md)** — Technical specification
- **[NEURAL_API_EVOLUTION.md](../../springs/primalSpring/specs/NEURAL_API_EVOLUTION.md)** — Triad coordination spec
- **[CROSS_GATE_GRAPH_EXECUTOR.md](../../springs/primalSpring/specs/CROSS_GATE_GRAPH_EXECUTOR.md)** — Cross-gate execution design

### Primal Repositories
- **biomeOS** — Graph executor, manifest resolution
- **nestGate** — Content sync, push, fetch heads
- **songbird** — Remote discovery, mesh freshness
- **bearDog** — Signature verification
- **squirrel** — Manifest parsing

---

## License

Part of the ecoPrimals ecosystem. AGPL-3.0-or-later.
See individual primal licenses for details.
