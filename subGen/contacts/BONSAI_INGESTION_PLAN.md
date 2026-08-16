# Bonsai-BT Ingestion Plan: Fork → Primal Subsystem

**Date**: Aug 16, 2026
**Source**: github.com/Sollimann/bonsai (MIT, v0.13.0)
**Target**: New ecoPrimals meta-primal — DECIDE layer
**Licensing**: AGPL3 + scyBorg triple license (discuss Cyborg with Solberg)

---

## Why This Project

Bonsai-bt is a one-human Rust project (Kristoffer Rakstad Solberg) with NASA
Lunabotics production use, zero runtime dependencies, zero unsafe, and 5,284
LOC of clean behavior-tree engine. ecoPrimals is a one-human Rust project.
Small projects recognizing and composing with each other IS the ecosystem thesis.

The project provides **deterministic orchestration over nondeterministic actions**
— the missing DECIDE layer between squirrel REASON and biomeOS ROUTE.

---

## Ingestion Pipeline

### Phase 0: Ingest + Code Review

1. Clone bonsai-bt into ecoPrimals org on Forgejo
2. Full code review against ecoPrimals standards:
   - scyBorg triple license conversion (AGPL3 fork, share-alike upstream)
   - `#[allow]` → `#[expect]` Rust 2024 idiom evolution
   - File size audit (800L max per file)
   - Zero `unsafe` (already clean)
   - Clippy pedantic + nursery (already `-D warnings`)
   - Documentation per wateringHole standards
3. Discuss with Solberg: Cyborg license, upstream collaboration, ecoPrimals intent
4. Initial Forgejo push with provenance trail (original MIT + fork license)

### Phase 1: sourDough Scaffold

Use sourDough (primal template) to bootstrap the workspace:

```
gardens/[name]/
├── Cargo.toml                    # workspace, ecoBin compliant
├── crates/
│   ├── [name]-core/              # behavior engine (bonsai fork, evolved)
│   │   ├── src/
│   │   │   ├── behavior.rs       # Behavior<A> (from bonsai)
│   │   │   ├── state.rs          # State<A> runtime cursor
│   │   │   ├── bt.rs             # BT<A, B> executor
│   │   │   ├── sequence.rs       # Sequence/Select + memoryless
│   │   │   ├── when_all.rs       # Parallel nodes
│   │   │   ├── eco_action.rs     # NEW: EcoAction enum (Neural API signals)
│   │   │   ├── eco_blackboard.rs # NEW: ecosystem-typed blackboard
│   │   │   └── provenance.rs     # NEW: per-tick sweetGrass witness
│   │   └── Cargo.toml
│   ├── [name]-rpc/               # JSON-RPC handlers + Neural API
│   │   ├── src/
│   │   │   ├── handler/
│   │   │   │   ├── behavior.rs   # behavior.* methods
│   │   │   │   ├── tree.rs       # tree.* methods
│   │   │   │   └── mod.rs        # dispatch registration
│   │   │   └── lib.rs
│   │   └── Cargo.toml
│   └── [name]-service/           # systemd/launchd service
│       ├── src/
│       │   ├── main.rs           # UDS socket, BTSP, primal.announce
│       │   └── shutdown.rs       # graceful shutdown
│       └── Cargo.toml
├── config/
│   ├── capability_registry.toml  # behavior.* + tree.* methods
│   └── ports.toml                # assigned port
├── graphs/
│   └── [name]_deploy.toml        # biomeOS deploy graph
├── CONTEXT.md
├── CONTRIBUTING.md
├── DEVELOPMENT.md
├── CHANGELOG.md
├── ROADMAP.md
└── whitePaper/
    └── subGen/
```

### Phase 2: ecoPrimals Evolution

**Ecosystem-specific types** (not in upstream bonsai):

```rust
/// Actions reference Neural API signals, never primal names
enum EcoAction {
    /// Call a Neural API capability: "compute.execute", "crypto.sign"
    Signal(String),
    /// Execute a named capability graph: "data_braid_ingress"
    Graph(String),
    /// Check a condition: "identity.authenticated?", "capacity.available?"
    Condition(String),
    /// Wait for async result by job ID
    Await(String),
    /// Emit gossip: "deploy.result", "behavior.decision"
    Gossip(String),
}

/// Blackboard = mesh state snapshot for this execution context
struct EcoBlackboard {
    gate_id: String,
    capabilities: HashMap<String, CapabilityStatus>,
    mesh_peers: Vec<PeerInfo>,
    pathway_hints: HashMap<String, f64>,  // PathwayLearner preferences
    witness_log: Vec<WitnessEntry>,       // sweetGrass provenance
}
```

**Provenance integration** — per-tick witnessing:

```rust
struct WitnessEntry {
    tree_hash: Blake3Hash,
    tree_version: String,
    tick: u64,
    node_path: Vec<usize>,
    action: EcoAction,
    result: Status,
    input_hash: Blake3Hash,
    result_hash: Blake3Hash,
    timestamp: u64,
    primal_identity: Did,
}
```

**Serializable trees as ecosystem artifacts:**

```rust
struct TreeArtifact {
    definition: Behavior<EcoAction>,
    hash: Blake3Hash,
    version: String,
    author: Did,
    required_signals: Vec<String>,
    constraints: Vec<Constraint>,
    provenance: Option<BraidRef>,  // sweetGrass attribution
}
```

### Phase 3: Neural API Capabilities

```toml
[behavior]
domain = "behavior"
provider = "[name]"
methods = [
    "behavior.load",
    "behavior.execute",
    "behavior.tick",
    "behavior.status",
    "behavior.pause",
    "behavior.resume",
    "behavior.cancel",
    "behavior.inspect",
    "behavior.replay",
    "behavior.validate",
    "behavior.export",
]

[tree]
domain = "tree"
provider = "[name]"
methods = [
    "tree.define",
    "tree.compose",
    "tree.hash",
    "tree.sign",
    "tree.braid",
]
```

### Phase 4: Protocol Compliance

- BTSP ClientHello (17th primal — or 18th if lithospore counts)
- G65 protocol negotiation
- G66 transport abstraction (TransportEndpoint/TransportStream)
- riboCipher framing on all IPC
- primal.announce with full capability registry
- gossip.inject for behavior decision events
- Deploy graphs for biomeOS germination

### Phase 5: Meta-Primal Integration

```
squirrel    → REASON  (what should we do?)
[name]      → DECIDE  (when/how/fallback — behavior tree execution)
biomeOS     → ROUTE   (which primal handles this capability?)
primals     → ACT     (execute the capability)
sweetGrass  → WITNESS (braid the execution trace)
PathwayLearner → ADAPT (learn from decision boundaries)
```

Like bingoCube (test/validation meta-primal), this doesn't do domain work —
it orchestrates HOW domain work gets done.

**Key integrations:**
- biomeOS: behavior trees as a new graph execution form alongside TOML graphs
- squirrel: transmits signed execution topologies instead of "do X" imperatives
- sweetGrass: braids per-tick execution records
- PathwayLearner: observes Select/Sequence decision boundaries for optimization
- petalTongue: renders tree visualizations (bonsai has graphviz + WebSocket inspector)
- footPrint: agent panel shows behavior tree state via conjugation layer

---

## Standards Checklist

| Standard | Status |
|----------|--------|
| scyBorg triple license | Phase 0 |
| Zero `unsafe` | Already clean |
| Clippy pedantic + nursery | Already `-D warnings` |
| Zero `#[allow]` in production | Phase 0 evolution |
| 800L max file size | Already compliant |
| Zero TODO/FIXME/HACK | Phase 0 audit |
| BTSP ClientHello | Phase 4 |
| G65 protocol negotiation | Phase 4 |
| G66 transport abstraction | Phase 4 |
| capability_registry.toml | Phase 3 |
| Deploy graph | Phase 3 |
| CONTEXT.md | Phase 1 |
| CONTRIBUTING.md | Phase 1 |
| DEVELOPMENT.md | Phase 1 |

---

## Naming (Working)

The ecoPrimals naming convention uses compound biological/natural words.
The name should evoke branching/decision/neural structure.

Working candidates:
- **brainTree** — direct, neural + tree
- **dendriTree** — dendrite (neural branches) + tree
- **nervVine** — nerve + vine (branching, echoes swarmVine)
- **bonsAI** — preserves provenance, AI pun
- **thornMap** — thorn (decision point) + map
- **rootMind** — root system + decision
- (Name will be chosen when it clicks)

---

## Upstream Relationship

- Fork is AGPL3 (ecoPrimals standard for internal primals)
- Share-alike: improvements to core BT semantics offered back to upstream MIT
- Discuss Cyborg license model with Solberg
- Ecosystem-specific types (EcoAction, EcoBlackboard, provenance) stay in fork
- Core algorithm improvements (new decorators, typed ports, perf) go upstream
- Credit and provenance: original MIT license preserved in fork, author credited

---

*Ingestion plan for new meta-primal. One-human project recognizing another.
Fork, evolve, abstract. The DECIDE layer the ecosystem needs.*
