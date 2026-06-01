# Implementation — membrane temporal.cascade

**From bash to Rust to agentic composition**

**Date**: June 1, 2026
**Status**: Whitepaper — Wave 66 production reality
**See also**: `FUNCTIONAL_PATTERN_CONVERGENCE.md` — canonical triad/trio vocabulary

---

## Current State: Rust Production (Wave 66)

The waterFall implementation has evolved from `cascade-pull.sh` (bash, spatial)
to `membrane temporal.cascade` (Rust, temporal, policy-driven). The Rust
implementation in `cellMembrane/crates/membrane-shadow/src/temporal.rs` is the
production engine.

| Feature | Status |
|---------|--------|
| Manifest-driven repo list | Production |
| Gate profiles (`--gate eastGate`) | Production |
| `.gate` identity file | Production |
| Temporal sync (fetch all, measure, pull leader, push followers) | **Production** |
| `--publish-freshness` | **Production** — writes `freshness.toml` |
| Remote exclusion (`exclude_remotes` per repo) | **Production** — manifest-driven |
| Divergence policy engine (flag/merge-ff/merge-rebase/impulse-only) | **Production** |
| SYNC impulse posting on divergence | **Production** — `post_sync_diverge` |
| `--parallel N` (concurrent repos) | Production |
| `--clone-missing` | Production |
| `--dry-run` | Production |
| impulsePotential auto-trigger (`potential.sense` after sync) | Production |
| NeuralBridge try-primal-first routing | Implemented (feature-gated) |
| bearDog impulse signing | Implemented (optional Ed25519 via UDS) |
| songbird impulse relay | Implemented (optional mesh.publish via UDS) |
| Composition graph dispatch via biomeOS | Defined — `sync_diverge.toml`, `sync_resolve.toml` |

---

## The `membrane temporal` Command Surface

### temporal.cascade — Full ecosystem sync

```bash
membrane temporal.cascade --gate eastGate --publish-freshness
```

The cascade engine:

1. Loads the ecosystem manifest and resolves the gate profile (which repos
   this gate manages)
2. For each repo, reads `divergence_policy` and `exclude_remotes` from
   the manifest
3. Fetches all remotes (excluding those in `exclude_remotes`)
4. Builds the temporal position matrix (ahead/behind per remote)
5. Classifies: converge (one leader), diverge (multiple leaders), parity
6. Applies the repo's `divergence_policy`:
   - `flag`: report divergence, take no action
   - `merge-ff`: fast-forward if one side is a strict ancestor
   - `merge-rebase`: rebase on leader, fall back to flag on conflict
   - `impulse-only`: fire SYNC impulse via `post_sync_diverge`, no merge
   - `agentic`: future — delegate to `sync_resolve.toml` composition graph
7. Pushes to followers (any remote behind local HEAD after resolution)
8. If `diverge_impulse = true` in `[sync]` and divergence was detected,
   fires a SYNC impulse to `infra/wateringHole/impulses/active/`
9. Writes `freshness.toml` if `--publish-freshness` is set
10. Auto-triggers `potential.sense` to show pending impulses

### temporal.sync — Single repo sync

```bash
membrane temporal.sync primals/bearDog
```

Same temporal logic as cascade, applied to a single repository.

### temporal.check — Read-only parity check

```bash
membrane temporal.check
```

Fetches all remotes, measures temporal positions, reports without modifying
state. Pure qS SENSE — no side effects.

---

## Manifest Configuration

The ecosystem manifest (`wateringHole/ecosystem_manifest.toml`) drives the
cascade engine. Wave 66 added three agentic sync fields:

### Sync-level configuration

```toml
[sync]
diverge_impulse = true     # fire SYNC impulses on detected divergence
```

### Per-repo configuration

```toml
[repos.plasmidBin]
divergence_policy = "merge-ff"    # safe fast-forward for binary artifacts

[repos.sporePrint]
divergence_policy = "impulse-only"  # content repo — human/agent reviews

[repos.rustChip]
exclude_remotes = ["upstream"]      # ignore unrelated upstream history
```

---

## Evolution from Bash

The implementation evolved through three phases:

### Phase 1: cascade-pull.sh (Wave 58–62)

Bash script with `--source auto` (spatial — forgejo-first, origin-fallback).
Reliable but temporally naive: pulled from the closest reachable remote
regardless of which remote was actually ahead.

**The May 29 incident**: 8 upstream primals shipped evolution to GitHub.
`--source auto` pulled zero changes because Forgejo was reachable but stale.
This proved that spatial sync was structurally unsound.

### Phase 2: cascade-pull.sh --source temporal (Wave 62–64)

Bash script extended with `--source temporal`: fetch all remotes, measure
ahead/behind, pull from leader, push to followers. Solved the spatial
problem. Still bash — no manifest-driven policy, no impulse integration.

### Phase 3: membrane temporal.cascade (Wave 64–66)

Full Rust implementation in `membrane-shadow`. The cascade engine:

- Reads the ecosystem manifest for gate profiles, repo lists, policies
- Implements the temporal position matrix in Rust
- Adds `divergence_policy` per repo (flag/merge-ff/merge-rebase/impulse-only)
- Adds `exclude_remotes` per repo (filter out noise remotes)
- Fires SYNC impulses via `post_sync_diverge` on divergence detection
- Integrates with NeuralBridge for primal-assisted operations
- Auto-triggers `potential.sense` post-sync

### Phase 4: biomeOS composition dispatch (future)

The end state: `cascade-pull.sh` is replaced entirely by biomeOS
composition dispatch:

```
biomeOS composition dispatch: ecosystem.pull
  → manifest.gate_profile (biomeOS)
  → mesh.discover_remotes (songbird)
  → content.sync with temporal policy (nestGate/membrane)
  → mesh.publish freshness (songbird)
```

The `sync_diverge.toml` and `sync_resolve.toml` composition graphs in
`primalSpring/graphs/signals/` define the biomeOS-native equivalents.
Phase A (graph definition in primalSpring) is complete. Phase B (biomeOS
dispatch) awaits upstream NeuralRouter evolution.

---

## SYNC Impulse Flow

When `temporal.cascade` detects divergence on a repo with
`diverge_impulse = true`:

```
membrane temporal.cascade
    │
    │ fetches all remotes, builds temporal matrix
    │ detects: forgejo +2, origin +3, local at common ancestor
    │
    ├─ policy = "merge-ff"?
    │   └── attempts fast-forward → succeeds or falls through to flag
    │
    ├─ policy = "impulse-only" or resolution failed?
    │   └── post_sync_diverge:
    │       ├── classifies diverge type (fork/drift/conflict)
    │       ├── creates SyncImpulseFile (TOML) with payload
    │       ├── git add + commit to wateringHole/impulses/active/
    │       └── git push (rides waterFall to all gates)
    │
    └─ other gates on next cascade-pull:
        ├── waterFall syncs impulses/active/ directory
        └── potential.sense detects pending SYNC impulse
            └── human or agent reviews and resolves
```

---

## Architecture

```
membrane CLI (main.rs)
    └── dispatch.rs → temporal domain
        └── temporal.rs
            ├── cascade()       — full ecosystem sync with policy engine
            ├── sync()          — single repo sync
            ├── check()         — read-only parity check
            ├── check_with_excludes() — filters exclude_remotes
            ├── sync_with_policy()    — applies divergence_policy
            └── try_policy_resolve()  — merge-ff / merge-rebase logic
                    │
                    └── impulse.rs::post_sync_diverge()
                        ├── classify_diverge_type()
                        ├── suggest_action()
                        └── SyncImpulseFile creation + git push
```

### Key modules

| Module | Responsibility |
|--------|---------------|
| `temporal.rs` | Cascade engine, temporal matrix, policy dispatch |
| `impulse.rs` | Impulse lifecycle + SYNC impulse posting |
| `manifest.rs` | Manifest reader — `divergence_policy`, `exclude_remotes`, `diverge_impulse` |
| `git_ops.rs` | Shared git add/commit/push operations |
| `bridge.rs` | NeuralBridge — try-primal-first routing to biomeOS |
| `config.rs` | `membrane.toml` + environment configuration |

---

## Testing Strategy

### Validation via primalSpring

- `s_atomic_signals` — validates all 32 composition graphs structurally
  (including `sync_diverge`, `sync_resolve`, `sync_resolve_crossgate`)
- `s_meta_tier_signals` — validates tool schemas and composition tier coverage
- `s_routing_consistency` — validates `temporal` domain routes to `membrane` primal

### Integration tests (cellMembrane)

- `membrane temporal.check` against live multi-remote repos
- `membrane temporal.cascade --gate eastGate` on production ecosystem
- SYNC impulse round-trip: fire on eastGate, sense on flockGate

### Ecosystem validation

- 39 repos across 7 gate profiles managed by `temporal.cascade`
- Daily cascade runs on eastGate with `--publish-freshness`
- SYNC impulses observed flowing through wateringHole

---

## Next Reading

- **[09_AGENTIC_SYNC.md](./09_AGENTIC_SYNC.md)** — Full agentic sync paper
- **[06_AIRGAP_FEDERATION.md](./06_AIRGAP_FEDERATION.md)** — Depot and USB patterns
- **[07_ROADMAP.md](./07_ROADMAP.md)** — Glacial gate path
- **[03_TRIAD_COORDINATION.md](./03_TRIAD_COORDINATION.md)** — Triad mechanics

---

*"The best implementation is the one that makes the common case trivial
and the uncommon case visible. Convergence is trivial — it happens on every
cascade. Divergence is visible — it fires an impulse and records its own
provenance."*
