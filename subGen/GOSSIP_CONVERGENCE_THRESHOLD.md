# Gossip Convergence Threshold — Epidemic Protocol Proven

**Status**: CROSSED | **Wave**: 157i | **Date**: Aug 11, 2026
**Scope**: 5-gate active mesh, 9/16 primals injecting, 660+ entries converged

---

## What Crossed

swarmVine's gossip protocol went from "theoretical epidemic model" to
**measured operational convergence** across 5 gates, with 9 of 16 primals
actively injecting events and 660+ entries propagated through the mesh.

The gossip system is no longer an internal communication mechanism. It is the
**nervous system** of the organism — science production (hotSpring 10/10),
provenance verification (braid events), and operational telemetry all flow
through the same epidemic protocol.

---

## Convergence Evidence

### Active Mesh (5 Gates)

| Gate | Role | Peers | Entries | Dispatch |
|------|------|-------|---------|----------|
| **eastGate** | Hub | Multiple | **660+** ingested | Standard |
| **sporeGate** | Hub | Multiple | **660+** ingested | Standard |
| **westGate** | NUCLEUS | Active | Converging | Standard |
| **ironGate** | NUCLEUS | **2** | Active | **2ms** (8× faster) |
| **strandGate** | Node Atomic | Active | Injecting (hotSpring) | Standard |

### Injecting Primals (9/16)

| Primal | Injection Type | Gate(s) |
|--------|---------------|---------|
| swarmVine | Protocol core (ant colony routing) | All active gates |
| bearDog | Crypto events, key lifecycle | eastGate, sporeGate |
| songBird | Communication events | eastGate, sporeGate |
| skunkBat | Tunnel/transport events | Active gates |
| hotSpring | **Science telemetry** (10/10 events) | strandGate |
| coralReef | Process lifecycle, ChildGuard | Active gates |
| biomeOS | Composition state, capability changes | westGate |
| nestGate | Storage events | westGate |
| toadStool | Compute dispatch events | strandGate |

### Not Yet Injecting (7/16)

| Primal | Reason |
|--------|--------|
| cellMembrane | Platform layer — below gossip |
| rhizoCrypt | DAG operations internal |
| loamSpine | Ledger operations internal |
| sweetGrass | Braid verification (planned: braid events) |
| petalTongue | Visualization — consumer, not producer |
| squirrel | MCP adapter — bridges, not emits |
| sourDough | Dormant/early |

---

## The hotSpring Arc (0/10 → 10/10)

The most significant gossip milestone: hotSpring's TrajectoryRunner now emits
gossip for every stage of QCD production.

| Wave | hotSpring Gossip | Significance |
|------|-----------------|--------------|
| 155m | 0/10 | No gossip integration |
| 155u | ~4/10 | Initial trajectory events |
| 156+ | ~7/10 | Campaign and observable events |
| **157i** | **10/10 COMPLETE** | Full science pipeline observable |

Events emitted:
1. Campaign start
2. Trajectory initialization
3. HMC leap acceptance/rejection
4. Plaquette measurement
5. Polyakov loop measurement
6. Wilson flow step
7. Observable convergence check
8. Checkpoint write
9. Campaign completion
10. Error/recovery

The mesh can now **observe science happening** — not just infrastructure state.

---

## Epidemic Protocol Properties

swarmVine implements a gossip protocol modeled on ant colony optimization:

| Property | Evidence |
|----------|----------|
| **Convergence** | 660+ entries replicated across eastGate/sporeGate |
| **Partition tolerance** | southGate/blueGate operate locally without relay; converge when connected |
| **Latency** | ironGate dispatch: 2ms to 2 peers |
| **Scalability** | 9 producers → 5 consumers, no bottleneck measured |
| **Consistency** | Eventual — entries propagate within seconds across active mesh |
| **Deduplication** | Entry-level, content-addressed |

---

## Topology

```
                    ┌─────────────┐
                    │  golgiBody  │ (VPS relay)
                    └──────┬──────┘
                           │
    ┌──────────┬───────────┼───────────┬──────────┐
    │          │           │           │          │
┌───┴───┐ ┌───┴───┐ ┌─────┴────┐ ┌───┴───┐ ┌───┴────┐
│eastGate│ │sporeGt│ │ westGate │ │ironGt │ │strandGt│
│  Hub   │ │  Hub  │ │ NUCLEUS  │ │NUCLEUS│ │  Node  │
│ 660+   │ │ 660+  │ │  Active  │ │ 2ms   │ │Atomic  │
└────────┘ └───────┘ └──────────┘ └───────┘ └────────┘

Blocked (no MeshRelay):
  southGate — locally operational, gossip local only
  blueGate — locally operational, cross-gate blocked
  graftGate — WG live, gossip integration pending
```

---

## What This Proves

### 1. Epidemic Protocol Works at Organism Scale

The ant colony gossip model scales to 9 producers, 5 consumer gates, and
660+ entries without centralized coordination. The topology is self-organizing.

### 2. Science Is Observable

hotSpring 10/10 means the mesh doesn't just carry operational telemetry —
it carries **scientific measurements**. The organism can observe its own
science production in real-time.

### 3. swarmVine Ant Colony Pattern Is Validated

The theoretical model (pheromone trails, foraging patterns, colony optimization)
is now measured operational behavior. Entries propagate, converge, and stabilize
through epidemic diffusion.

### 4. Gossip Is the Composition Glue

Atomics compose mechanically (IPC, sockets, signal graphs). Gossip adds
**informational composition** — primals that don't share IPC channels can
still observe each other's state through the mesh. This is what makes the
organism an organism, not just a distributed system.

---

## Remaining Blockers

| Blocker | Impact | Owner |
|---------|--------|-------|
| **songBird MeshRelay** | Cross-gate gossip for non-direct gates (blueGate, southGate) | songBird team |
| **blueGate depot rebuild** | Windows gossip convergence testing | blueGate operations |
| **graftGate gossip integration** | Darwin gossip participation | graftGate bootstrap |
| **biomeOS category shadow** | Neural API routing blocks some gossip queries | biomeOS team |

MeshRelay is the single largest remaining topology constraint. Without it,
gossip forms islands rather than a unified mesh.

---

## The Generational Arc

```
gen0:  "Collective intelligence" (philosophy — organism metaphor)
gen2:  swarmVine defined — ant colony optimization protocol (design)
gen3:  4-gate mesh, basic event propagation (validation)
gen4:  Composition broker integrates gossip routing (integration)
157i:  5-gate active, 9/16 injecting, 660+ entries, science flows (convergence)
next:  MeshRelay → full 12-gate topology, 16/16 injecting (completion)
```

---

*subGen Wave 157i — Gossip convergence threshold crossed. 5-gate active mesh.
9/16 primals injecting. 660+ entries converged. hotSpring 10/10 — science
observable by the organism. ironGate 2ms dispatch. Epidemic protocol: proven
operational, not theoretical. MeshRelay remains the topology ceiling.*
