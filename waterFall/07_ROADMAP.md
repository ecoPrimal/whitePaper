# waterFall Roadmap

**From bash to sovereign sync**

**Date**: May 29, 2026
**Status**: Whitepaper — Implementation Roadmap

---

## Current State (Wave 60)

waterFall exists as a manifest-driven bash script with spatial source
selection. The Neural API triad is formalized. Signal graphs are
specified but structural-only. Upstream primals are implementing the
methods that waterFall's graphs will call.

| Component | State |
|-----------|-------|
| `cascade-pull.sh` | Production (spatial `--source auto`) |
| `ecosystem_manifest.toml` | Production (38 repos, 6 gate profiles) |
| `.gate` identity | Production |
| `ecosystem.pull/push/check` signal graphs | Specified, structural validation |
| `WATERFALL_TEMPORAL_SYNC.md` spec | Written (Wave 60) |
| whitePaper/waterFall/ series | Written (Wave 60) |
| Upstream primal methods | 1/14 shipped (`manifest.gate_profile`) |

---

## Phase 1: Temporal cascade-pull (Wave 61)

**Goal**: Replace `--source auto` (spatial) with `--source temporal`.

| Task | Owner | Effort |
|------|-------|--------|
| Implement `temporal_pull_one_repo()` in bash | primalSpring / infra | Small |
| Temporal position matrix output in `--check` | primalSpring / infra | Small |
| Push-to-followers after pull | primalSpring / infra | Small |
| Divergence detection and report | primalSpring / infra | Small |
| benchScale test: 3-gate temporal sync | primalSpring / infra | Medium |

**Exit criteria**: `cascade-pull.sh --source temporal` on eastGate
correctly pulls from GitHub when it's ahead of Forgejo, pushes to
Forgejo, and reports parity on subsequent check.

---

## Phase 2: Freshness Protocol (Wave 62-63)

**Goal**: Extended `freshness.toml` with per-remote state, optional
mesh publishing.

| Task | Owner | Effort |
|------|-------|--------|
| Extended freshness.toml schema | primalSpring / infra | Small |
| `--publish-freshness` flag in cascade-pull | primalSpring / infra | Small |
| songbird `mesh.publish` implementation | songbird team | Medium |
| Freshness hint consumption in qS phase | primalSpring / infra | Medium |
| `s_waterfall_freshness_schema` scenario | primalSpring | Small |

**Depends on**: songbird `mesh.publish` upstream.

**Exit criteria**: After temporal sync, `freshness.toml` contains
per-repo per-remote HEAD snapshots. If songbird mesh is available,
freshness is published and other gates can read it.

---

## Phase 3: Neural API Ecosystem Signals (Wave 63-65)

**Goal**: Replace bash with `signal.dispatch("ecosystem.pull")`.

| Task | Owner | Effort |
|------|-------|--------|
| nestGate `content.sync` with temporal source | nestGate team | Large |
| nestGate `content.fetch_heads` | nestGate team | Medium |
| nestGate `content.push` | nestGate team | Medium |
| songbird `mesh.discover_remotes` | songbird team | Medium |
| biomeOS `signal.dispatch` for ecosystem tier | biomeOS team | Medium |
| Wire ecosystem.pull graph to live execution | biomeOS team | Medium |
| `s_waterfall_signal_dispatch` scenario | primalSpring | Medium |

**Depends on**: 5 upstream primal methods (nestGate ×3, songbird ×1,
biomeOS signal dispatch).

**Exit criteria**: `biomeos signal dispatch ecosystem.pull --gate eastGate`
produces the same result as `cascade-pull.sh --source temporal`.

---

## Phase 4: Cross-Gate Coordination (Wave 65+)

**Goal**: Fleet-wide temporal awareness, adaptive sync cadence.

| Task | Owner | Effort |
|------|-------|--------|
| biomeOS cross-gate `graph.execute` Phase B | biomeOS team | Large |
| `ecosystem.check` with `gate = "any"` fan-out | biomeOS team | Large |
| Fleet freshness dashboard | primalSpring / infra | Medium |
| Adaptive sync cadence (drift-based) | primalSpring / infra | Medium |
| `s_cross_gate_temporal` scenario | primalSpring | Medium |

**Depends on**: biomeOS cross-gate graph executor Phase B.

**Exit criteria**: eastGate can query freshness from southGate and
ironGate via cross-gate signal, producing a fleet-wide temporal view.

---

## Glacial Gate Requirements

waterFall contributes to the glacial gate through these checkpoints:

| Glacial Criterion | waterFall Contribution | Phase |
|-------------------|----------------------|-------|
| Sovereign inner membrane | Temporal sync keeps Forgejo current | 1 |
| Multi-gate mesh validated | Mesh-published freshness proves coherence | 2 |
| Cross-gate capability calls | Ecosystem signals execute across gates | 3-4 |
| Cloudflare removal | Forgejo-primary sync (inversion) | 2 |
| 3+ gates meshed | Fleet temporal coordination | 4 |

### Forgejo Inversion

The current `ecosystem_manifest.toml` has `default_source = "github"`.
Inversion to `default_source = "forgejo"` requires:

1. **Forgejo mirror of GitHub pushes** — ironGate's `forgejo_mirror.sh`
   or a Forgejo webhook that pulls GitHub on push
2. **7-day shadow period** — run temporal sync in shadow mode, comparing
   Forgejo freshness against GitHub freshness
3. **Parity confirmation** — zero divergence across all 38 repos for 7
   consecutive days
4. **Flip default** — change `default_source` to "forgejo" in manifest

With temporal sync, inversion is less critical — `--source temporal`
naturally prefers whoever is ahead. But formally declaring Forgejo as
default is a sovereignty milestone.

---

## Upstream Primal Evolution Required

waterFall's Neural API integration depends on these upstream methods:

| Primal | Method | Used by | Priority |
|--------|--------|---------|----------|
| **nestGate** | `content.sync` | ecosystem.pull | HIGH |
| **nestGate** | `content.fetch_heads` | ecosystem.check | HIGH |
| **nestGate** | `content.push` | ecosystem.push | HIGH |
| **songbird** | `mesh.discover_remotes` | ecosystem.pull | MEDIUM |
| **songbird** | `mesh.mirror` | ecosystem.push | MEDIUM |
| **songbird** | `mesh.publish` | all ecosystem signals | MEDIUM |
| **biomeOS** | `manifest.gate_profile` | all ecosystem signals | **SHIPPED** |
| **biomeOS** | cross-gate `graph.execute` | Phase 4 | Wave 65 |

The bash implementation (Phases 1-2) does NOT depend on upstream
primals. It's a parallel path that delivers value immediately while
primals evolve.

---

## Downstream Pattern Ingestion

Springs and gates that adopt waterFall patterns:

| Consumer | Pattern | Phase |
|----------|---------|-------|
| All gates | `cascade-pull.sh --source temporal` | 1 |
| VPS (cellMembrane) | `forgejo_mirror.sh` → temporal sync | 1-2 |
| ironGate (projectNUCLEUS) | Upstream method implementations | 3 |
| All springs | `biomeos signal dispatch ecosystem.pull` | 3 |
| Fleet management | Cross-gate freshness queries | 4 |
| Collaborators (gen5) | Project-specific depot sync | 2+ |

---

## Success Metrics

| Metric | Current | Phase 1 | Phase 3 | Phase 4 |
|--------|---------|---------|---------|---------|
| Sync correctness | Spatial only | Temporal | Neural API | Fleet-wide |
| Stale pulls | Common (May 29 incident) | Eliminated | Eliminated | Eliminated |
| Divergence detection | Manual | Automatic | Signal-based | Cross-gate |
| Follower propagation | Manual | Automatic | Neural API | Fleet mesh |
| Gate convergence time | Unbounded | ≤ 2P | ≤ P | ≤ P |
| Freshness visibility | None | `--check` | Mesh published | Fleet dashboard |

---

## Timeline Summary

```
Wave 60 (now)     Spec + whitePaper complete
                  │
Wave 61           Phase 1: --source temporal in bash
                  │
Wave 62-63        Phase 2: Freshness protocol + mesh publish
                  │         (parallel: upstream primals implementing methods)
                  │
Wave 63-65        Phase 3: Neural API signal integration
                  │
Wave 65+          Phase 4: Cross-gate temporal coordination
                  │
Glacial Gate      Sovereign inner membrane, 3+ gates meshed,
                  fleet-wide temporal coherence
```

---

*"Phase 1 is a bash script change. Phase 4 is an emergent nervous
system. The path between them is one upstream method at a time."*
