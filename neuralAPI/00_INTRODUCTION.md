# Introduction to Neural API Architecture

**What is Neural API and why does it matter?**

**Date**: January 4, 2026 (revised May 14, 2026 — Phase 32 atomic model)
**Status**: Whitepaper - Conceptual Design + Implementation Underway

---

## 🎯 The Vision

**Neural API** is an architectural pattern for adaptive, learning-based orchestration in biomeOS. Instead of static workflows that execute the same way every time, Neural API enables systems that **learn from usage**, **discover patterns**, and **evolve coordination strategies over time**.

---

## 🌊 The Problem

### **Traditional Orchestration (Static)**

```
Day 1:    Request → Route → Execute → Response
Day 100:  Request → Route → Execute → Response  (same)
Day 1000: Request → Route → Execute → Response  (still same)
```

**Characteristics:**
- ❌ Fixed pathways
- ❌ Manual optimization
- ❌ No adaptation
- ❌ Linear complexity growth

**Examples:**
- Kubernetes: You define pods, they deploy the same way
- Docker Compose: You define services, they start the same way
- Systemd: You define units, they run the same way

**Problems:**
1. **Scalability**: As you add more services, complexity explodes (N² connections)
2. **Optimization**: Performance improvements require manual rewriting
3. **Adaptation**: Changing conditions require manual reconfiguration
4. **Discovery**: New patterns must be manually identified

---

## 🧠 The Solution

### **Neural API Orchestration (Adaptive)**

```
Day 1:    Request → Execute → Learn
Day 100:  Request → Optimized Execute → Learn More
Day 1000: Request → Self-Optimized → Discover New Patterns
                    ↑                    ↓
                    └────────────────────┘
```

**Characteristics:**
- ✅ Adaptive pathways
- ✅ Automatic optimization
- ✅ Learns from usage
- ✅ Emergent intelligence

**Result**: System gets better over time, automatically!

---

## 🏗️ The Three-Layer Architecture

### **Layer 1: Primals (Capabilities)**

```
┌───────────────────────────────────────────────────────────┐
│              Primals — 13 Autonomous Capabilities          │
│                                                           │
│  Tower:     BearDog    Songbird   skunkBat                │
│  Compute:   ToadStool  barraCuda  coralReef               │
│  Storage:   NestGate   rhizoCrypt LoamSpine  SweetGrass   │
│  Meta:      biomeOS    Squirrel   petalTongue             │
│                                                           │
│  • 427 registered capability methods                      │
│  • 13/13 BTSP AEAD authenticated                          │
│  • All at zero debt (Waves 1-14 complete)                 │
│  • Dark Forest Glacial Gate compliant                     │
│  • Report usage metrics ← learning signal                 │
└───────────────────────────────────────────────────────────┘
```

**Primals:**
- Do ONE thing well (single responsibility)
- Know only themselves (self-knowledge only)
- Report metrics to biomeOS (optional, for learning)
- Compose into atomic tiers: Tower (3), Node (6), Nest (7), NUCLEUS (10+3 meta)

**Atomic tiers (Phase 32):**
- **Tower** (bearDog + songbird + skunkBat): Trust boundary — crypto + discovery + defense
- **Node** (Tower + compute trio): Compute substrate — dispatch + execute + compile
- **Nest** (Tower + provenance trio + nestGate): Storage + provenance
- **NUCLEUS** (Node + Nest): Full atom — 10 unique primals + 3 meta-tier

---

### **Layer 2: biomeOS (Orchestration Engine)**

```
┌──────────────────────────────────────────────┐
│     biomeOS - Adaptive Orchestration Engine  │
│                                              │
│  Capability Registry  •  Graph Executor      │
│  Health Monitor       •  Pathway Learner     │
│  Dependency Resolver  •  Optimizer           │
│                                              │
│  • Coordinates primals                       │
│  • Executes workflows as graphs              │
│  • Learns usage patterns ← NEW!              │
│  • Optimizes over time ← NEW!                │
└──────────────────────────────────────────────┘
```

**biomeOS:**
- Manages primal lifecycle (spawn, monitor, restart)
- Resolves dependencies (who provides what?)
- **Executes primal graphs** (not just linear workflows)
- **Learns from execution** (tracks metrics, discovers patterns)
- **Optimizes pathways** (automatic performance improvements)

---

### **Layer 3: Niche APIs (High-Level Abstractions)**

```
┌──────────────────────────────────────────────┐
│      Niche APIs - Domain-Specific Patterns   │
│                                              │
│  RootPulse    Hive      Reef     CustomNiche│
│  (version     (CI/CD)   (deploy) (user)     │
│   control)                                   │
│                                              │
│  • Complex multi-primal workflows            │
│  • Domain-specific orchestration             │
│  • High-level user APIs                      │
│  • Learn and adapt ← NEW!                    │
└──────────────────────────────────────────────┘
```

**Niche APIs:**
- Provide high-level abstractions (e.g., "commit", "push", "deploy")
- Coordinate multiple primals (complex workflows)
- Learn from user behavior (adapt APIs over time)
- Abstract away complexity (users don't see primals)

**Example: RootPulse (Version Control)**
```rust
// User calls high-level API
rootpulse.commit("Feature complete").await?;

// Behind the scenes: Nest atomic signal decomposes into 6 primal calls:
// BearDog.sign → NestGate.store → rhizoCrypt.dehydrate →
// LoamSpine.commit → SweetGrass.braid → skunkBat.audit
// biomeOS learns: "sweetGrass and NestGate can parallelize"
// Next time: Optimized graph (30% faster)
```

---

## 🔄 Bidirectional Learning

### **The Key Innovation: Information flows BOTH ways**

```
┌─────────────────────────────────────────────┐
│  Layer 3: Niche APIs                        │
│  "I need to commit changes"                 │
└───────────────────┬─────────────────────────┘
                    ↓ Forward (Execution)
┌───────────────────┴─────────────────────────┐
│  Layer 2: biomeOS                           │
│  "Execute graph: NestGate → BearDog → ..."  │
└───────────────────┬─────────────────────────┘
                    ↓ Forward (Activation)
┌───────────────────┴─────────────────────────┐
│  Layer 1: Primals                           │
│  "Executing... Done. Metrics: 5ms, OK"      │
└───────────────────┬─────────────────────────┘
                    ↑ Backward (Feedback)
┌───────────────────┴─────────────────────────┐
│  Layer 2: biomeOS                           │
│  "Learned: 5ms latency, 100% success"       │
│  "Opportunity: NestGate + SweetGrass can    │
│   run in parallel (no dependency)"          │
└───────────────────┬─────────────────────────┘
                    ↑ Backward (Learning)
┌───────────────────┴─────────────────────────┐
│  Layer 3: Niche APIs                        │
│  "Next execution will be 30% faster!"       │
└─────────────────────────────────────────────┘
```

**Forward Pass:**
- User calls niche API
- biomeOS executes primal graph
- Primals do their work

**Backward Pass:**
- Primals report metrics
- biomeOS learns patterns
- Niche APIs adapt

**Result:** System improves over time, automatically!

---

## 🎯 Core Concepts

### **1. Graph Execution**

Instead of executing primals one-by-one, biomeOS executes **graphs** of primals:

```rust
// OLD: Linear execution
nestgate.store().await?;
beardog.sign().await?;
sweetgrass.attribute().await?;
loamspine.append().await?;

// NEW: Graph execution
let commit_graph = PrimalGraph {
    nodes: vec![nestgate, beardog, sweetgrass, loamspine],
    edges: vec![
        nestgate → beardog,
        beardog → sweetgrass,
        sweetgrass → loamspine
    ],
    pattern: Sequential,
};

biome.execute_graph(commit_graph).await?;
```

**Benefits:**
- Explicit dependencies (clear data flow)
- Optimizable (can detect parallelization opportunities)
- Reusable (same graph for multiple operations)

---

### **2. Pathway Learning**

biomeOS tracks **how primals are used together**:

```rust
// After 1000 executions of commit_graph:
let stats = biome.learner.get_stats("commit_graph").await?;

println!("Co-occurrence:");
println!("  nestgate + beardog: 1000 times");
println!("  beardog + sweetgrass: 1000 times");
println!("  sweetgrass + loamspine: 1000 times");

println!("Average latency:");
println!("  nestgate: 2ms");
println!("  beardog: 3ms");
println!("  sweetgrass: 10ms");  // Bottleneck!
println!("  loamspine: 30ms");   // Biggest bottleneck!

println!("Opportunities:");
println!("  • nestgate and sweetgrass can run in parallel");
println!("  • beardog can be pre-warmed (high usage)");
println!("  • loamspine could benefit from batching");
```

**biomeOS learns this automatically, just by observing!**

---

### **3. Automatic Optimization**

Based on learned patterns, biomeOS **suggests optimizations**:

```rust
// Original graph (sequential)
nestgate → beardog → sweetgrass → loamspine

// Optimized graph (parallel where possible)
nestgate ──┐
           ├──> beardog ──> loamspine
sweetgrass─┘

// Speedup: 30% (empirically measured!)
```

**User experience:**
```bash
$ rootpulse commit "Feature complete"
✓ Committed in 50ms

💡 Optimization available:
   NestGate and SweetGrass can run in parallel
   Expected speedup: 30%
   Apply? [Y/n] y

✓ Optimization applied!

$ rootpulse commit "Another commit"
✓ Committed in 35ms  ← Faster!
```

**System gets better over time, without manual tuning!**

---

### **4. Emergent Intelligence**

After thousands of executions, biomeOS can **discover new patterns**:

```rust
// Examples of emergent discoveries:
// - "When committing >100 files, batch in groups of 10"
// - "When network latency >50ms, pre-fetch from loamspine"
// - "When beardog is busy, queue requests (don't block)"
// - "Users who commit often also push often (pre-warm songbird)"

// biomeOS discovers these WITHOUT being told!
```

**Result**: Patterns humans didn't think of, automatically discovered!

---

## 🌟 Real-World Example: RootPulse

### **Traditional Git (Static)**

```bash
$ git add file.txt          # Always same speed
$ git commit -m "msg"       # Always same speed
$ git push                  # Always same speed
```

**After 1000 commits**: Still the same speed!

---

### **RootPulse with Neural API (Adaptive)**

```bash
# Day 1: First commit
$ rootpulse commit "Initial"
✓ Committed in 50ms

# Day 30: After 100 commits, biomeOS learned patterns
$ rootpulse commit "Feature"
✓ Committed in 35ms  (30% faster, optimized graph!)

# Day 90: After 1000 commits, biomeOS discovered patterns
$ rootpulse commit "Refactor"
✓ Committed in 25ms  (50% faster, prewarmed primals!)

# Day 180: System continues to evolve
$ rootpulse commit "Polish"
✓ Committed in 20ms  (60% faster, batch operations!)
```

**After 1000 commits**: 3x faster, automatically!

---

## 💡 Key Benefits

### **For Users**
- 🚀 **Performance improves over time** - No manual tuning needed
- 🎯 **Simpler APIs** - High-level abstractions hide complexity
- 🔄 **Adapts to your workflow** - System learns how you work

### **For Developers**
- 🧩 **Composable** - Build complex workflows from graphs
- 📊 **Observable** - Full visibility into what's learned
- 🎨 **Flexible** - Support any coordination pattern

### **For the Ecosystem**
- 🌱 **Emergent** - New patterns discovered automatically
- 🔗 **Federated** - Learning can be shared across towers
- ♾️ **Scalable** - Complexity managed through abstraction

---

## 🔬 Why This Works

### **Nature Already Does This!**

**Biological Neural Networks:**
- Neurons fire, patterns emerge
- Repeated patterns strengthen (learning)
- New patterns discovered (creativity)

**Economic Systems:**
- Individuals trade, markets emerge
- Supply/demand signals optimize (price discovery)
- New trade routes discovered (innovation)

**Ecological Systems:**
- Species interact, ecosystems emerge
- Resource flows optimize (co-evolution)
- New symbioses discovered (mutualism)

**Neural API mimics nature:** Simple components + coordination + learning = emergent intelligence!

---

## May 2026 Addendum: Composition Collapse

The original vision described learning and optimization as the primary
goals. Two additional goals have emerged from ecosystem evolution:

### Goal: Atomic Signal Collapse

The 427-method surface across 13 primals produces a combinatorial
explosion for springs. Atomic signals (see `02_ARCHITECTURE.md`)
collapse this into ~20 tier-level operations. A spring calls
`signal("nest", "store", payload)` instead of 6 individual primal
calls. biomeOS decomposes the signal into the correct graph.

### Goal: Barrick Lab Pipeline Convergence

lithoSpore now has access to the full Barrick Lab software stack
(breseq, pLannotate, OSTIR, EFM Calculator, CryptKeeper). Each tool
has Python/R pipelines that produce known-correct output. The Neural
API provides the graph execution layer for Rust reproductions: fetch
data → compute → store with provenance → visualize via petalTongue.
This is a `nest.store` + `node.compute` signal composition.

---

## What's Next?

### **Read the Series:**
1. **[01_PHILOSOPHY.md](./01_PHILOSOPHY.md)** — Why this approach?
2. **[02_ARCHITECTURE.md](./02_ARCHITECTURE.md)** — Atomic decomposition layer (Tower/Node/Nest/NUCLEUS)
3. **[03_GRAPH_EXECUTION.md](./03_GRAPH_EXECUTION.md)** — How graphs work
4. **[04_BIDIRECTIONAL_LEARNING.md](./04_BIDIRECTIONAL_LEARNING.md)** — Learning mechanism
5. **[05_PATHWAY_OPTIMIZATION.md](./05_PATHWAY_OPTIMIZATION.md)** — Pattern discovery and signal collapse metrics

### **Implementation Guides:**
6. **[06_BIOMEOS_IMPLEMENTATION.md](./06_BIOMEOS_IMPLEMENTATION.md)** — What biomeOS needs
7. **[07_PRIMAL_REQUIREMENTS.md](./07_PRIMAL_REQUIREMENTS.md)** — 13/13 primals: Dark Forest compliant
8. **[10_ROADMAP.md](./10_ROADMAP.md)** — Atomic signal activation path

---

*"The best systems are not designed — they emerge from the right kind of simplicity, repeated and refined."*

