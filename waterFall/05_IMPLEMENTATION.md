# Implementation Path

**From bash to Neural API**

**Date**: May 29, 2026
**Status**: Whitepaper — Implementation Guide

---

## Current State: cascade-pull.sh

The current implementation is a bash script at
`infra/wateringHole/cascade-pull.sh`. It provides:

| Feature | Status |
|---------|--------|
| Manifest-driven repo list | Production |
| Gate profiles (`--gate eastGate`) | Production |
| `.gate` identity file | Production |
| `--source auto` (forgejo-first) | Production — **spatially aware, temporally naive** |
| `--source forgejo` / `--source origin` | Production |
| `--check` (parity check) | Production |
| `--parallel N` (concurrent pulls) | Production |
| `--clone-missing` | Production |
| `--dry-run` | Production |
| `--publish-freshness` | **Not implemented** |
| `--source temporal` | **Not implemented** |

### What `--source auto` Does Today

```bash
if git remote get-url forgejo >/dev/null 2>&1; then
    pull_source="forgejo"
else
    pull_source="origin"
fi
git pull "$pull_source" main --ff-only
```

This is spatial: "use forgejo if configured, else origin." It does NOT:
- Fetch all remotes to compare
- Measure which remote is ahead
- Push to followers after pulling

---

## Phase 1: `--source temporal` in cascade-pull.sh

**Effort**: Small — bash changes to existing script
**Wave target**: 61

### Algorithm

```bash
temporal_pull_one_repo() {
    local repo_path="$1"
    cd "$ECOPRIMALS_ROOT/$repo_path"

    # 1. Fetch all remotes
    git fetch --all --quiet

    # 2. Build temporal position matrix
    local leader=""
    local leader_behind=0
    local diverged=false

    for remote in $(git remote); do
        ref="${remote}/main"
        git rev-parse --verify "$ref" >/dev/null 2>&1 || continue

        ahead=$(git rev-list --count "${ref}..HEAD")
        behind=$(git rev-list --count "HEAD..${ref}")

        if [[ $behind -gt $leader_behind ]]; then
            leader="$remote"
            leader_behind=$behind
        fi

        if [[ $ahead -gt 0 && $behind -gt 0 ]]; then
            diverged=true
        fi
    done

    # 3. Classify and act
    if $diverged; then
        echo "DIVERGE $repo_path"
        return 1
    elif [[ -n "$leader" && $leader_behind -gt 0 ]]; then
        git pull "$leader" main --ff-only
        # Push to followers
        for remote in $(git remote); do
            [[ "$remote" == "$leader" ]] && continue
            behind=$(git rev-list --count "HEAD..${remote}/main" 2>/dev/null || echo 0)
            if [[ $behind -lt 0 ]] || ! git rev-list --count "${remote}/main..HEAD" >/dev/null 2>&1; then
                continue
            fi
            local remote_behind=$(git rev-list --count "${remote}/main..HEAD")
            if [[ $remote_behind -gt 0 ]]; then
                git push "$remote" main 2>/dev/null && echo "  pushed → $remote"
            fi
        done
    else
        echo "PARITY  $repo_path"
    fi
}
```

### Output Format

```
=== WaterFall Temporal Sync ===
Manifest: v2.0.0 wave 60 (38 repos)
Gate:    eastGate
Source:  temporal

  primals/songBird      CONVERGE origin→local→forgejo (+4)
  primals/toadStool      CONVERGE origin→local→forgejo (+3)
  primals/bearDog        PARITY
  primals/rhizoCrypt     CONVERGE origin→local→forgejo (+3)
  gardens/helixVision    DIVERGE (origin +2 / forgejo +1)
  ...

=== Summary ===
Parity:    30 / 38
Converged:  7 / 38
Diverged:   1 / 38
```

### New Flags

```
--source temporal     Fetch all, measure, pull leader, push followers
--publish-freshness   Write temporal freshness.toml after sync
--divergence-report   Produce detailed divergence report for flagged repos
```

---

## Phase 2: Freshness Mesh

**Effort**: Medium — songbird + `freshness.toml` evolution
**Wave target**: 62–63
**Depends on**: songbird `mesh.publish` upstream implementation

### Freshness Publishing

After a `--source temporal` sync, `cascade-pull.sh` writes an extended
`freshness.toml` and optionally publishes it to the songbird mesh:

```toml
[wave]
id = 61
gate = "eastGate"
measured = "2026-05-29T16:04:00Z"
source = "temporal"

[summary]
total = 38
parity = 30
converged = 7
diverged = 1

[repos."primals/songBird"]
local = "a58a676c"
origin = "a58a676c"
forgejo = "a58a676c"
pattern = "parity"

[repos."gardens/helixVision"]
local = "b3c4d5e6"
origin = "f7g8h9i0"
forgejo = "j1k2l3m4"
pattern = "diverge"
origin_unique = 2
forgejo_unique = 1
```

### Mesh Broadcast

songbird's `mesh.publish` broadcasts the freshness snapshot to all
connected gates. Receiving gates can use it as a hint to skip
unnecessary fetches.

---

## Phase 3: Neural API Signal Integration

**Effort**: Large — requires upstream primal methods
**Wave target**: 63–65
**Depends on**: nestGate `content.sync` with temporal source, songbird
`mesh.discover_remotes`, biomeOS cross-gate executor

### ecosystem.pull Graph Evolution

Current `ecosystem_pull.toml`:

```toml
[[nodes]]
primal = "biomeOS"
capability = "manifest.gate_profile"
input = { gate = "${GATE_NAME}" }

[[nodes]]
primal = "songbird"
capability = "mesh.discover_remotes"
input = { repos = "${gate_repos}" }

[[nodes]]
primal = "nestGate"
capability = "content.sync"
input = { repos = "${gate_repos}", source = "auto" }
coordination = "parallel"

[[nodes]]
primal = "songbird"
capability = "mesh.publish"
input = { type = "freshness", data = "${sync_result}" }
```

Temporal evolution:

```toml
[[nodes]]
primal = "nestGate"
capability = "content.sync"
input = {
    repos = "${gate_repos}",
    source = "temporal",            # NEW: temporal source selection
    push_followers = true,          # NEW: push to behind remotes
    divergence_policy = "flag"      # NEW: flag, don't merge
}
coordination = "parallel"
```

The `content.sync` method on nestGate would need to implement the
temporal position matrix internally, replacing the bash logic with
native Rust.

### signal.dispatch Replacement

The end state: `cascade-pull.sh` becomes a thin wrapper around:

```bash
biomeos signal dispatch ecosystem.pull \
    --gate "$GATE_NAME" \
    --source temporal
```

biomeOS executes the ecosystem.pull graph, which calls nestGate's
temporal sync, songbird's mesh publish, and reports results.

---

## Phase 4: Cross-Gate Temporal Coordination

**Effort**: Large — requires cross-gate graph executor Phase B+
**Wave target**: 65+
**Depends on**: biomeOS `graph.execute` with `gate` hints

### Fleet Freshness Dashboard

With cross-gate execution, a coordinator gate can query freshness
from all gates:

```toml
[[nodes]]
primal = "songbird"
capability = "mesh.discover_remotes"
gate = "any"
relay = "songbird_turn"

[[nodes]]
primal = "biomeOS"
capability = "ecosystem.check"
gate = "any"
fan_out = true
```

This produces a fleet-wide freshness view without requiring all gates
to independently publish.

### Adaptive Sync Cadence

Based on fleet freshness data, gates can adjust their wave period:

| Gate drift | Action |
|-----------|--------|
| 0 repos behind | Lengthen wave period (less work) |
| 1–5 repos behind | Normal wave period |
| 5+ repos behind | Shorten wave period (catch up faster) |
| Divergences detected | Alert + manual wave trigger |

---

## Migration Path

| Phase | Tool | Source | Gate awareness | Mesh |
|-------|------|--------|:-------------:|:----:|
| Current | `cascade-pull.sh` | `--source auto` (spatial) | `.gate` file | No |
| Phase 1 | `cascade-pull.sh` | `--source temporal` | `.gate` file | No |
| Phase 2 | `cascade-pull.sh` | temporal + freshness | `.gate` file | Publish only |
| Phase 3 | `signal.dispatch` | temporal via nestGate | biomeOS profile | Full mesh |
| Phase 4 | cross-gate graph | temporal + fleet-wide | cross-gate discovery | Fleet mesh |

Each phase is independently valuable. Phase 1 alone solves the
"stale Forgejo" problem we hit on May 29. Phases 2+ add progressive
intelligence.

---

## Testing Strategy

### Unit Tests (primalSpring)

- `s_waterfall_temporal_position` — validate temporal matrix computation
- `s_waterfall_pattern_classification` — converge/diverge/parity logic
- `s_waterfall_freshness_schema` — freshness.toml validation

### Integration Tests (benchScale)

- `test-waterfall-temporal.sh` — Docker lab with 3 gates, 2 remotes,
  push to one remote, verify temporal sync discovers and converges

### Ecosystem Tests (live)

- Run `--source temporal` on eastGate after known GitHub pushes
- Verify Forgejo receives propagation
- Run `--check` on southGate to confirm convergence

---

## Next Reading

- **[06_AIRGAP_FEDERATION.md](./06_AIRGAP_FEDERATION.md)** — Depot and USB patterns
- **[07_ROADMAP.md](./07_ROADMAP.md)** — Full glacial gate path
- **[02_ARCHITECTURE.md](./02_ARCHITECTURE.md)** — Sync levels and topology

---

*"The best implementation is the one that makes the common case trivial
and the uncommon case visible."*
