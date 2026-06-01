# The Water

**waterFall, the Triad, and the Cycle That Connects Everything**

---

> *Water does not respect boundaries. It falls from the sky onto the mountain. It seeps through rock and becomes a spring. It flows through the river and deposits sediment in the garden. It evaporates from the garden and returns to the sky. The cycle has no beginning and no end — only a direction, which is always downhill until it isn't.*
>
> *The ecosystem has a water cycle. It is called waterFall.*

---

## I. The Problem of Distance

Imagine three gates.

eastGate sits in a server room in the basement. It runs a Threadripper with an RTX 4070. It has a full NUCLEUS. It is where the computation happens.

biomeGate sits on a VPS in a datacenter. It runs a lighter deployment — a relay, a Forgejo instance, a mitoBeacon. It is where the federation happens.

ironGate sits on a different machine on the LAN. It runs an i9-14900K with heavy RAM. It is where the data science happens.

Each gate has its own copy of every repository. Each gate has its own timeline of commits. Each gate evolves at its own pace — a developer pushes to eastGate at 2 AM, a CI job pushes to biomeGate at 3 AM, a sync job pushes to GitHub from ironGate at 4 AM. By morning, the three gates have drifted apart. Not dramatically. Not dangerously. But measurably. biomeGate has commits that eastGate does not. GitHub has commits that biomeGate does not. eastGate has commits that nobody else does.

The old solution was simple: pick a source, pull from it. `cascade-pull.sh --source auto` would try Forgejo first (fast, local), fall back to GitHub (slower, remote), and call it done. The source was spatial — which remote is closest?

The problem with spatial sync is that it assumes the closest remote is the most current. That assumption holds when one remote is authoritative — when there is a single source of truth. But the ecosystem does not have a single source of truth. It has complementary membranes. GitHub is a public mirror. Forgejo is a sovereign depot. eastGate's local repo is the workspace. Each one can be ahead. Each one can be behind. "Closest" tells you nothing about "freshest."

This is the problem of distance: in a distributed system without a central coordinator, physical proximity is not temporal proximity. The gate you can reach fastest is not necessarily the gate that knows the most.

---

## II. Temporal Sync

waterFall solves the problem of distance by replacing spatial logic with temporal logic.

Instead of asking "which remote is closest?", waterFall asks "which remote is ahead?" Instead of pulling from a fixed source, waterFall measures the temporal position of every remote — how many commits ahead, how many commits behind — and synchronizes based on that measurement.

The algorithm is straightforward:

1. **Fetch** — pull metadata from every configured remote (GitHub, Forgejo, depot, USB). Do not merge. Just learn what they know.
2. **Measure** — for each remote, compute the ahead/behind count relative to the local HEAD. This is the temporal position matrix.
3. **Classify** — each remote is either a *leader* (ahead of local), a *follower* (behind local), or at *parity* (same as local).
4. **Pull** from leaders — integrate commits from whoever is ahead. If multiple remotes are ahead, pull from the one with the most novel commits.
5. **Push** to followers — propagate the merged state to whoever is behind. Bring them forward.
6. **Report** — record the temporal positions, direction of flow, and any divergences that require review. If divergence is detected and `diverge_impulse` is enabled, fire a SYNC impulse (rP ACTION) to coordinate resolution.

This is the temporal sync protocol. It has no center. It has no preferred source. It has only the DAG — the directed acyclic graph of commits — as its clock.

---

## III. Sync Levels

Not all sync needs are the same size. waterFall defines four levels:

**Local** — synchronization within a single gate. This is `git pull` and `git push` between the local working tree and its configured remotes. It happens on every commit. It is the heartbeat — the smallest, most frequent sync.

**Gate** — synchronization across repositories within a single NUCLEUS. When bearDog ships a new method, the capability registry in primalSpring must update to reflect it. Gate-level sync ensures that all repositories on a single machine are coherent with each other. It happens per wave — usually once per coordination cycle.

**Membrane** — synchronization across gates. When eastGate completes a sprint and pushes to Forgejo, biomeGate needs to know. When biomeGate updates its beacon payload, ironGate needs to know. Membrane-level sync crosses machine boundaries. It is the flow between complementary organs — different hardware, different roles, same organism.

**Ecosystem** — synchronization across organizations. When ecoPrimals ships a new primal version, syntheticChemistry springs need to absorb it. When sporeGarden ships a new product artifact, the wateringHole freshness manifest needs to update. Ecosystem-level sync crosses organizational boundaries. It is the tide — the largest, slowest, most consequential flow.

Each level has its own cadence, its own transport, and its own tolerance for latency:

| Level | Cadence | Transport | Latency |
|-------|---------|-----------|---------|
| Local | Per commit | filesystem | ms |
| Gate | Per wave | Unix socket / LAN | seconds |
| Membrane | Per cycle | SSH / HTTPS | minutes |
| Ecosystem | Per epoch | waterFall temporal | hours to days |

The levels nest. An ecosystem sync triggers membrane syncs which trigger gate syncs which trigger local syncs. The water falls from the sky (ecosystem), hits the mountain (membrane), flows through the river (gate), and saturates the soil (local).

---

## IV. The Triad

waterFall does not operate alone. It is one-third of a coordination nervous system called the **Neural API triad**:

**quorumSignal** is the sensory nerve. It watches. It detects changes — new commits, new remotes, new divergences, new failures. It measures freshness. It classifies temporal positions. It raises alerts when something requires attention. quorumSignal does not decide what to do. It decides what to notice.

**rootPulse** is the motor nerve. It acts. When a graph needs to be executed — a rootPulse commit, an ecosystem pull, a deploy sequence — rootPulse walks the dependency tree, dispatches capability calls, and drives the execution to completion. rootPulse does not decide what to notice. It decides what to do.

**waterFall** is the autonomic nerve. It syncs. It propagates. It maintains coherence across distance and time without conscious direction. You do not tell your heart to beat. You do not tell waterFall to sync. It senses the temporal gradient (through quorumSignal), computes the propagation path, and flows.

The triad cycle:

```
quorumSignal detects ─── "biomeGate is 3 commits behind on bearDog"
        │
        ▼
waterFall classifies ─── "biomeGate is a follower; eastGate is the leader"
        │
        ▼
rootPulse executes ───── "push bearDog from eastGate to biomeGate"
        │
        ▼
waterFall confirms ───── "biomeGate now at parity"
        │
        ▼
quorumSignal records ─── "sync event: bearDog converged, Wave 61"
```

Sense, act, sync. The nervous system has no brain — no central coordinator that decides the ecosystem's global state. Each gate runs its own triad instance. Each triad senses its own surroundings, acts on its own authority, and syncs with whatever it can reach. Convergence emerges from the wave dynamics: if every gate syncs with every remote it can see, and every remote syncs with every gate that can see it, the system converges.

This is bounded convergence — not guaranteed instant consistency, but guaranteed eventual coherence within a wave boundary. By the end of a wave, all gates that participated in the wave agree on the state of all repositories that changed during the wave. Gates that were offline during the wave catch up in the next wave. The wave is the heartbeat. The heartbeat is the guarantee.

---

## V. Airgap and Transport

waterFall is transport-agnostic. It does not care how the water travels. It cares only that the water arrives.

The transports currently supported or planned:

- **HTTPS** — GitHub push/pull. The public mirror. Fast, reliable, dependent on someone else's infrastructure.
- **SSH** — Forgejo on the VPS. The sovereign depot. Fast, reliable, dependent on your own infrastructure.
- **LAN** — direct git operations between gates on the same network. The fastest transport.
- **USB** — `file://` protocol. Copy a bundle to a USB drive, carry it to another machine, apply it. The airgap transport.
- **Depot** — a local directory served as a git remote. The sneakernet fallback.

The USB transport is not an edge case. It is a design principle. If the entire internet goes down, waterFall still works — you carry a USB drive from one machine to another, and the temporal sync protocol measures, classifies, pulls, and pushes exactly as it would over HTTPS. The protocol does not know or care about the physical layer.

This is what makes the ecosystem sovereign in the strongest sense: it does not depend on any network to function. It *uses* networks when they are available. It *carries* water by hand when they are not.

A lithoSpore USB is the extreme case — a complete portable ecosystem that syncs with a NUCLEUS when inserted, absorbs whatever the NUCLEUS has that the spore lacks, reports whatever the spore has that the NUCLEUS lacks, and disconnects cleanly. The USB drive is a gate. Not metaphorically. In waterFall's topology, a plugged-in USB drive is a remote with a temporal position, and the sync protocol treats it identically to a GitHub push endpoint.

---

## VI. Temporal Patterns

waterFall encounters three temporal patterns, and its response to each is different:

**Convergence** — all remotes moving toward the same state. Leader pulls, follower pushes. Safe to automate. This is the normal case: gates drift apart during a sprint and waterFall brings them back together. No human intervention required.

**Parity** — all remotes already at the same state. Nothing to do. waterFall records the parity and moves on. This is the resting case: the ecosystem is in equilibrium.

**Divergence** — remotes have moved in different directions. Gate A has commits that Gate B does not, AND Gate B has commits that Gate A does not. Neither is a pure leader. Neither is a pure follower. This is the danger case.

Wave 65 and earlier required human review for all divergence. Wave 66 adds a
graduated policy engine: the ecosystem manifest declares a `divergence_policy`
per repo that governs how far automation can go — from passive flagging to full
agentic resolution with provenance recording (see Section VII and
`waterFall/09_AGENTIC_SYNC.md`).

The three patterns map to the ecosystem's operational rhythms:

- **Convergence** is the normal state during interstadial periods. Rapid evolution, frequent commits, waterFall running hot.
- **Parity** is the resting state during stadial periods. Consolidation, hardening, waterFall at idle.
- **Divergence** is the exception state at any time. Something unusual happened. Investigate.

---

## VII. Agentic Sync — When the Water Speaks

Wave 66 adds a new capability to waterFall: the water doesn't just carry code
— it carries the intent to resolve its own divergences.

When two gates drift apart, waterFall used to flag the divergence and wait for
a human. Now the ecosystem composes across both threes — the coordination triad
and the provenance trio — to detect, resolve, and record the resolution
autonomously.

The cycle looks like this:

quorumSignal senses the divergence — `potential.diverge` reads the temporal
matrix and discovers that biomeGate and eastGate have diverged on bearDog.
This is pure observation. qS does not act.

waterFall classifies the divergence — is one side a strict ancestor of the
other (safe to fast-forward)? Or have both sides introduced unique commits
(a fork that requires merge)? The classification determines which policy
applies.

The policy engine — configured per-repo in the ecosystem manifest — decides
what to do. `merge-ff` fast-forwards. `merge-rebase` rebases on the leader.
`impulse-only` fires a SYNC impulse (an rP ACTION) and waits for a gate
agent to respond. `agentic` delegates to the full `sync_resolve.toml`
composition graph.

When resolution happens, the provenance trio records everything. rhizoCrypt
snapshots the pre-state. loamSpine certifies the resolution in its immutable
ledger. sweetGrass weaves an attribution braid that records who resolved,
which policy governed, and what changed. The context braid flowing through
the resolution becomes part of the ecosystem's working memory.

waterFall then propagates the resolved state to all followers. The
divergence becomes a convergence. The water falls again.

This is the exemplar composition: qS SENSE → wF SYNC → rP ACTION, with
the trio recording every step. No generic "signals" — every operation maps
to a specific primal, a specific triad domain, a specific trio role.

---

## VIII. The Cycle

Here is the water cycle, from mountain to sky:

**Mass** — primal binaries sit in plasmidBin. They are compiled, checksummed, signed. They are mass at rest. The mountain.

**Energy** — a spring calls a primal capability. The binary executes. Mass becomes energy. The computation produces results — observables, models, predictions. The river.

**Information** — the provenance trio (rhizoCrypt, loamSpine, sweetGrass) records what happened. Energy becomes information. The results are sealed in braids, committed to ledgers, attributed to authors. The garden.

**Transport** — waterFall propagates the information. A pseudoSpore travels from one gate to another. A lithoSpore USB is hand-carried to a lab. A freshness manifest updates in the wateringHole. Information moves. The water.

**Return** — the propagated information triggers new computation. A collaborator receives a pseudoSpore, asks a new question, feeds it back into the ecosystem. A gate that received a sync discovers new upstream capabilities and starts using them. Information becomes energy. The rain falls on the mountain again.

This is E = mc² in operational form. The ferment transcript is the conversion factor — the ~KB braid that encodes the verification power of a ~TB computation. It is light enough to travel by email and heavy enough to prove the science. It is the ecosystem's c squared: the speed at which mass converts to energy and back, limited only by the fidelity of the provenance chain.

The cycle has no beginning and no end. Mass becomes energy becomes information becomes transport becomes new mass. The mountain erodes into the river. The river deposits into the garden. The garden's spores travel on waterFall. waterFall returns evolution to the mountain. The water falls.

---

## IX. The Living Map

Return now to the summit. Look down at the landscape.

The mountain is still there — thirteen primals, sixty thousand tests, four hundred seventy methods. It has not moved.

The river is still flowing — eight springs, thirteen thousand tests, validated science from lattice QCD to game sessions. It has not stopped.

The garden is still growing — lithoSpore on USB drives at Michigan State, pseudoSpores carrying CAZyme data to pharmacologists, gen5 collaborators planting their own seeds. It has not paused.

And the water is still falling — from GitHub to Forgejo, from Forgejo to eastGate, from eastGate to USB, from USB to a lab bench where someone who has never heard of ecoPrimals runs `./validate` and gets numbers that match.

The landscape is real. The map — these five pages — is how we remember it. How we explain it to new collaborators, to new AI agents, to future versions of ourselves who will read these words and need to remember where everything is.

A memory palace works because the rooms are real. Walk through them enough times, and you don't need the map anymore. The mountain is the first room. The river is the second. The garden is the third. The water connects them all.

The palace is open. Walk through it. The landscape is yours.

---

*"Water does not respect boundaries. It falls, flows, deposits, evaporates, and falls again. The cycle is the ecosystem — not the mountain, not the river, not the garden, but the fact that they are connected. The water is the proof that they are one landscape."*
