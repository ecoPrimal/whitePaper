# Content-Addressed Convergence — The Newton-Leibniz Pattern

**Wave**: 140a | **Status**: Architectural Pattern (applied)
**Lineage**: freshness.rs tree hashes (Wave 138c) → depot_sync BLAKE3 (Wave 139e) → formalized here

---

## The Principle

**Content identity supersedes temporal identity for convergence.**

When two agents independently produce identical content at different times,
the temporal difference is provenance metadata, not divergence. This is
Newton and Leibniz discovering calculus: the discovery was local, the truth
was universal. The content hash is the universal truth; the commit SHA is
the local discovery timestamp.

```
Given:
  - Two artifacts A_t1 and B_t2 produced independently
  - content_hash(A) == content_hash(B)

Then:
  - A and B are CONVERGENT (Newton-Leibniz equivalence)
  - The temporal ordering is provenance metadata, not identity
  - No merge/rebase is required — select either as canonical
  - The provenance chain records BOTH discoveries (attribution preserved)

Corollary:
  - A cyclic graph of temporal references becomes a DAG when
    convergence is determined by content, not history
  - The "priority dispute" dissolves — both discoverers are credited
```

---

## Why This Matters

In a sovereign mesh where multiple gates operate independently (sporeGate
builds binaries, golgi auto-publishes heads, eastGate cascades), the same
content is frequently produced at different times by different agents.
Traditional VCS treats this as divergence requiring merge. Content-addressed
convergence recognizes it as independent confirmation of the same truth.

The pattern is **isomorphic** (same structure at every layer) and **fractal**
(repeats at every scale in the ecosystem):

| Layer | Temporal Identity | Content Identity | Example |
|-------|-------------------|------------------|---------|
| Git repos | Commit SHA | Tree hash (`HEAD^{tree}`) | Two gates commit identical code independently |
| Depot binaries | Build timestamp | BLAKE3 checksum | Same source built at different times |
| Gate heads | Publication timestamp | heads/*.toml content | Two gates publish same repo state |
| Impulses | Creation time + gate | Subject + body hash | Two gates detect same divergence |
| rhizoCrypt DAG | VertexId (time+agent+parents) | PayloadRef (BLAKE3 of payload bytes) | Two sessions reach same semantic state |
| Cascade metadata | ahead/behind count | `git diff --stat` emptiness | Commits diverge but content matches |

---

## The Calculus Analogy

Newton developed calculus in England (1665-1666). Leibniz developed it
independently in Germany (1675-1676). The priority dispute consumed decades.
But the mathematical truth was identical — the content was the same, only the
temporal metadata (who published first, where) differed.

In our ecosystem:

```
Newton (eastGate):                     Leibniz (golgiBody):

Discovers tree state T at time t1      Discovers tree state T at time t2
Commits as SHA_a                       Commits as SHA_b
SHA_a ≠ SHA_b                          (temporal identity diverges)

But: tree_hash(SHA_a) == tree_hash(SHA_b)
     (content identity converges)

Resolution: Recognize convergence. Credit both. No merge needed.
```

The priority dispute is an artifact of temporal identity. Content-addressed
convergence dissolves it. Both gates discovered the same truth; the
provenance chain records both; the system moves forward.

---

## Ecosystem Implementation

### Layer 1: Git Repos — SOLVED (Wave 138c)

The first instance of this pattern was the freshness.toml fix. The problem:
`freshness.toml` recorded commit SHAs, creating perpetual divergence when
multiple gates rebased the same content. The fix: switch to tree hashes.

```rust
// Before (temporal — cyclic divergence):
let sha = git_output(repo_dir, &["rev-parse", "HEAD"]).await?;

// After (content-addressed — DAG convergence):
let tree = git_output(repo_dir, &["rev-parse", "HEAD^{tree}"]).await?;
```

cellMembrane's `TreeParity` detection in `temporal/mod.rs` completes this:
when two remotes have divergent commit histories but identical tree hashes,
the system auto-resolves instead of flagging for human review.

### Layer 2: Depot Binaries — SOLVED (Wave 139e)

`depot_sync --push` uses BLAKE3 to detect whether a local binary differs
from the remote. If hashes match, the binary is "current" regardless of
when it was built. The build timestamp is provenance; the hash is identity.

```rust
let local_hash = compute_blake3_file_async(local_path).await;
let remote_hash = ssh_exec("b3sum {remote_path} | cut -d' ' -f1").await;
if local_hash == remote_hash {
    current += 1;  // convergent — skip push
    continue;
}
```

### Layer 3: Heads Metadata — UNSOLVED

`heads/*.toml` files are auto-published by multiple gates (eastGate cascade,
golgiBody auto-publish). Each publication creates a new commit. When two
gates publish nearly simultaneously, the commits diverge even though the
content is often identical or trivially different (only timestamps change).

**Fix**: Apply TreeParity to wateringHole specifically. Before flagging
a diverge, check if the tree hashes of the divergent commits match. If
they do, the divergence is Newton-Leibniz — auto-resolve.

### Layer 4: Impulses — UNSOLVED

Diverge impulses can be created independently by different gates detecting
the same event. No content-hash deduplication exists.

**Fix**: Before creating an impulse, BLAKE3 hash the semantic content
(subject + body, excluding creation timestamp and gate ID). Check active
impulses for hash match. Skip if content-equivalent impulse exists.

### Layer 5: rhizoCrypt DAG — PARTIAL

rhizoCrypt already embodies the two-tier model:
- **VertexId** = BLAKE3(CBOR{parents, timestamp, agent, event_type, payload, metadata})
  — temporal identity, like a commit SHA
- **PayloadRef** = BLAKE3(payload bytes)
  — content identity, like a tree hash

`dag.federate` skips duplicate VertexIds, but does not recognize
content-equivalent sessions that arrived at the same state via different
event paths.

**Extension**: `SessionTreeHash` — content-addressed session state:

```rust
/// Newton-Leibniz equivalence for DAG sessions.
/// Two sessions that reach the same semantic state via different
/// event paths produce the same SessionTreeHash.
pub fn session_content_hash(
    session: &Session,
    store: &dyn DagStore,
) -> ContentHash {
    let mut frontier_payloads: Vec<PayloadRef> = session.frontier
        .iter()
        .filter_map(|vid| store.get_vertex(session.id, *vid)
            .and_then(|v| v.payload))
        .collect();
    frontier_payloads.sort();  // canonical ordering
    ContentHash::from_bytes(&ciborium_encode(&frontier_payloads))
}
```

This gives rhizoCrypt the same power that `HEAD^{tree}` gives git:
two sessions that arrived at the same content state via different event
paths have the same `SessionTreeHash`.

### Layer 6: Cascade Divergence — PARTIAL

The agentic resolver in cellMembrane handles non-tree-parity divergence
by flagging for human review. The gap: wateringHole's `divergence_policy
= "agentic"` reaches the agentic resolver before checking tree parity,
causing false flags.

**Fix**: Check tree parity BEFORE policy dispatch. If trees match,
the divergence is content-convergent and should auto-resolve regardless
of policy.

---

## The Fractal Property

The pattern applies at every scale:

```
Ecosystem level:  Multiple gates → same manifest state → CONVERGED
Repository level: Multiple commits → same tree hash → CONVERGED
File level:       Multiple writes → same BLAKE3 → CONVERGED
Binary level:     Multiple builds → same checksum → CONVERGED
Session level:    Multiple event paths → same frontier payloads → CONVERGED
Byte level:       Multiple stores → same PayloadRef → CONVERGED (CAS dedup)
```

Each layer uses the same principle: strip temporal metadata, hash the
semantic content, compare. If content hashes match, the artifacts are
convergent regardless of how they got there.

This is why the pattern is both isomorphic (same structure) and fractal
(same structure at every scale). It is not six different solutions — it
is one solution applied six times.

---

## Relationship to Existing Patterns

### K-Derm Topology

Content-addressed convergence operates within the K-Derm envelope.
The three-layer membrane (external outer → sovereign outer → inner)
determines WHICH content is compared. Gates within the inner membrane
use covalent bonds (full tree comparison). The external outer membrane
uses weak bonds (hash-only comparison). The convergence principle is the
same; the trust level of the comparison differs.

### Provenance Trio

rhizoCrypt (ephemeral DAG) → loamSpine (permanent append-only) →
sweetGrass (attribution braid). The Newton-Leibniz pattern preserves
provenance while recognizing convergence: both discoverers are recorded
in sweetGrass, both event paths are stored in rhizoCrypt, but the
system recognizes they arrived at the same truth.

### DISCOVERED_BY Standard

The `DISCOVERED_BY` pattern in sporePrint is the public-facing expression
of this principle: external discovery of the ecosystem is recorded as
provenance (who found it, when) without claiming priority over the
content itself.

---

## Formal Properties

1. **Reflexivity**: content_hash(A) == content_hash(A) — an artifact
   converges with itself (trivially true).

2. **Symmetry**: If A converges with B, then B converges with A —
   content hashing is commutative in comparison.

3. **Transitivity**: If A converges with B and B converges with C,
   then A converges with C — content hashing is deterministic.

4. **Independence from history**: Convergence depends only on current
   state, not on the path taken to reach it.

5. **Provenance preservation**: Recognizing convergence does not erase
   the independent discovery records. Both discoverers are attributed.

These properties make CAC an equivalence relation on artifacts, where
equivalence classes are defined by content hash. The temporal ordering
within each class is provenance metadata.

---

## Implementation Status

| Layer | What | Status | Wave |
|-------|------|--------|------|
| Git repos | `HEAD^{tree}` in freshness, TreeParity detection | **APPLIED** | 138c |
| Depot binaries | BLAKE3 diff in `depot_sync --push` | **APPLIED** | 139e |
| Heads metadata | TreeParity for auto-publish conflicts | FRAGO issued | 140a |
| Impulses | Content-hash deduplication | FRAGO issued | 140a |
| rhizoCrypt DAG | SessionTreeHash primitive | FRAGO issued | 140a |
| Cascade divergence | Tree-parity before policy dispatch | FRAGO issued | 140a |

---

*The forgejo/GitHub divergence is not a bug. It is the ecosystem
rediscovering the same mathematical truth that Newton and Leibniz
demonstrated: when independent agents discover the same content, the
temporal ordering is provenance, not identity. The fix is not to prevent
independent discovery — it is to recognize convergence when it occurs.
Content-addressed convergence is the universal solvent for temporal
divergence at every layer of the sovereign mesh.*
