# waterFall Architecture

**Sync levels, temporal patterns, and remote topology**

**Date**: May 29, 2026
**Status**: Whitepaper — Technical Design

---

## Sync Level Architecture

waterFall operates across four nested sync levels. Each level composes
the level below it.

```
┌─────────────────────────────────────────────────────────────┐
│  ECOSYSTEM                                                  │
│  All gates × all remotes × all transports                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  MEMBRANE                                           │    │
│  │  Gate ↔ VPS depot (Forgejo SSH)                     │    │
│  │                                                     │    │
│  │  ┌─────────────────────────────────────────────┐    │    │
│  │  │  GATE                                       │    │    │
│  │  │  All repos on one workstation               │    │    │
│  │  │                                             │    │    │
│  │  │  ┌─────────────────────────────────────┐    │    │    │
│  │  │  │  LOCAL                               │    │    │    │
│  │  │  │  Working tree ↔ HEAD (single repo)   │    │    │    │
│  │  │  └─────────────────────────────────────┘    │    │    │
│  │  │                                             │    │    │
│  │  └─────────────────────────────────────────────┘    │    │
│  │                                                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Level 0: Local

Boundary: single git repository, working tree to HEAD.

| Check | Command | Outcome |
|-------|---------|---------|
| Dirty check | `git status --porcelain` | Uncommitted changes? |
| Stash check | `git stash list` | Stashed work? |
| Ahead/behind | `git rev-list --count HEAD..@{u}` | Unpushed commits? |

A local-level sync ensures the working tree is clean before attempting
remote operations. waterFall's cascade-pull does a dirty check per repo
and can stash-and-pull or skip-and-report.

### Level 1: Gate

Boundary: filesystem — all repos under `$ECOPRIMALS_ROOT/`.

Gate-level sync iterates all repos matching the gate profile (from
`ecosystem_manifest.toml`) and performs local-level checks on each.
The gate profile determines which repos exist on this gate:

```toml
[gates.eastGate]
repos = ["primals/*", "springs/*", "gardens/*", "infra/*"]

[gates.ironGate]
repos = ["primals/*", "gardens/projectNUCLEUS", "gardens/cellMembrane"]
```

Gate-level output: N repos checked, M pulled, K failed, J skipped.

### Level 2: Membrane

Boundary: network — gate to depot (VPS Forgejo, GitHub, LAN NAS).

Membrane-level sync extends gate-level by adding push-to-depot after
pull. This ensures the depot membrane reflects the gate's state:

```
Gate                    Membrane (Forgejo)
 │                           │
 │  1. pull from leader      │
 │←──────────────────────────│
 │                           │
 │  2. push to followers     │
 │──────────────────────────→│
 │                           │
```

### Level 3: Ecosystem

Boundary: all reachable remotes across all transports.

Ecosystem-level sync operates across all membranes simultaneously.
It's the full temporal reconciliation:

1. Fetch ALL remotes for ALL repos
2. Build temporal position matrix
3. For each repo: classify pattern (converge/diverge/parity)
4. Pull from leaders, push to followers
5. Report divergences
6. Publish freshness to mesh

---

## Temporal Position Matrix

The core data structure of waterFall. For each repo, it maps every
known remote to its temporal position relative to local HEAD.

```
primals/songBird:
  Remote      HEAD      Ahead  Behind  Pattern
  ──────      ────      ─────  ──────  ───────
  origin      a58a676c  4      0       LEADER
  forgejo     a6ef1ec8  0      0       PARITY (with local)
  usb         d4e5f6a7  0      2       FOLLOWER

  Classification: CONVERGE (origin leads)
  Action: pull origin → push forgejo, push usb
```

The matrix is computed by:

```bash
git fetch --all --quiet
for remote in $(git remote); do
  ahead=$(git rev-list --count ${remote}/main..HEAD)
  behind=$(git rev-list --count HEAD..${remote}/main)
done
```

Classification rules:

```
if all_behind == 0 and all_ahead == 0:
    PARITY

elif exactly_one_remote_ahead and no_divergence:
    CONVERGE (that remote is leader)

elif multiple_remotes_ahead and their_commits_are_shared:
    CONVERGE (furthest-ahead remote is leader)

elif multiple_remotes_have_unique_commits:
    DIVERGE
```

Divergence detection: if remote A has commits not in remote B, AND
remote B has commits not in remote A, then the repo has diverged.

---

## Remote Topology

### Static Remotes (manifest-declared)

Every repo in the ecosystem has at most two canonical remotes
declared in `ecosystem_manifest.toml`:

```toml
[[repos]]
name = "primals/songBird"
github_repo = "ecoPrimals/songBird"
forgejo_repo = "ecoPrimals/songBird"
```

These map to:
- `origin` → `https://github.com/ecoPrimals/songBird.git`
- `forgejo` → `ssh://git.primals.eco:2222/ecoPrimals/songBird.git`

### Dynamic Remotes (gate-local)

Gates can add local remotes not in the manifest:

```bash
git remote add usb file:///media/usb/songBird.git
git remote add lan-depot git://192.168.1.50/songBird.git
git remote add project-vps ssh://helix-vps.example.com/songBird.git
```

waterFall's temporal measurement includes ALL configured remotes,
whether manifest-declared or gate-local. This means a USB drive
plugged into one gate automatically participates in sync.

### Depot Patterns

| Depot type | Transport | Reachability | Use case |
|-----------|-----------|-------------|----------|
| VPS Forgejo | SSH | Global (port 2222) | Primary inner membrane |
| GitHub | HTTPS | Global (cloud) | Outer membrane, open-source |
| LAN NAS | Git protocol / SSH | LAN only | High-bandwidth local sync |
| USB bare repo | file:// | Physical | Airgap, cold storage |
| Project VPS | SSH | Global | Subproject isolation |

A subproject like helixVision could have its own VPS depot. waterFall
treats it like any other remote — fetch, measure, converge.

---

## Manifest Sync Configuration

### Current (`ecosystem_manifest.toml`)

```toml
[sync]
forgejo_ssh = "ssh://git.primals.eco:2222"
default_source = "github"
```

### Proposed Extension

```toml
[sync]
default_source = "temporal"
freshness_cadence = "15min"
divergence_policy = "flag"

[sync.remotes.forgejo]
url_template = "ssh://git.primals.eco:2222/ecoPrimals/{repo}.git"
role = "membrane"

[sync.remotes.origin]
url_template = "https://github.com/ecoPrimals/{repo}.git"
role = "ecosystem"

[sync.remotes.helixvision-depot]
url_template = "ssh://helix-vps.example.com:2222/repos/{repo}.git"
role = "depot"
repos = ["gardens/helixVision"]
```

The `role` field is informational — it tells the freshness dashboard
what kind of membrane this remote represents. It does not affect
temporal measurement.

---

## Freshness State

### Current: `freshness.toml`

A wave snapshot — one HEAD per repo at publish time:

```toml
[wave]
id = 60
date = "2026-05-29"

[heads]
"primals/songBird" = "a58a676ca6ef1ec8..."
```

### Proposed: Temporal Freshness

Per-repo, per-remote HEAD snapshots with measurement timestamp:

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

[repos."primals/rhizoCrypt"]
local = "69c461d0"
origin = "69c461d0"
forgejo = "06b6dd6c"
pattern = "converge"
action = "pushed forgejo"
```

This richer freshness state enables:
- Mesh-published drift reports (songbird broadcasts to other gates)
- Historical sync tracking (which repos sync frequently, which lag)
- Divergence timeline (when did the fork happen)

---

## Security Model

waterFall inherits the ecosystem's security layers:

| Layer | Mechanism | waterFall role |
|-------|-----------|---------------|
| Transport | SSH keys (Forgejo), HTTPS (GitHub) | Authentication per remote |
| Content | bearDog `crypto.verify_ed25519` | Verify signed commits on push |
| Identity | `.gate` file + MitoBeacon | Gate identity for profile resolution |
| Authorization | Forgejo repo permissions | Write access per repo per key |

The `ecosystem.push` signal graph includes bearDog signature
verification before pushing to Forgejo. This ensures only
cryptographically signed commits propagate through the inner membrane.

---

## Next Reading

- **[03_TRIAD_COORDINATION.md](./03_TRIAD_COORDINATION.md)** — How sync levels interact with the triad
- **[04_TEMPORAL_MODEL.md](./04_TEMPORAL_MODEL.md)** — The wave model in detail
- **[05_IMPLEMENTATION.md](./05_IMPLEMENTATION.md)** — Concrete implementation path

---

*"Every remote is a temporal witness. waterFall's job is to call all
witnesses and let the evidence decide."*
