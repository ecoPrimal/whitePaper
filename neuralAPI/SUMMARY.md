# 🧠 Neural API - Quick Reference

**For people who want the TL;DR**

**Date**: January 4, 2026

---

## 🎯 What Is It?

**Neural API** makes biomeOS learn and adapt over time. Instead of executing the same workflows forever, it discovers patterns, suggests optimizations, and gets better automatically.

---

## 🌟 Key Ideas

### **1. Graph Execution**
Execute **graphs** of primals (not just one-at-a-time):

```rust
let graph = PrimalGraph {
    nodes: vec![nestgate, beardog, loamspine],
    pattern: Sequential, // or Parallel, DAG, Pipeline
};

biome.execute_graph(graph).await?;
```

### **2. Automatic Learning**
biomeOS tracks how primals are used and learns patterns:

```rust
// After 1000 executions:
- nestgate and sweetgrass have no dependencies
- They can run in parallel!
- Expected speedup: 30%
```

### **3. Bidirectional Feedback**
Information flows both ways:

```
User → biomeOS → Primals (execution)
User ← biomeOS ← Primals (learning)
```

---

## 📊 Three Layers

```
Layer 3: Niche APIs (RootPulse, Hive, Reef)
         ↕ (learning)
Layer 2: biomeOS (orchestration + learning)
         ↕ (metrics)
Layer 1: Primals (capabilities)
```

---

## 🚀 Timeline

- **Phase 1** (Weeks 1-3): Graph execution
- **Phase 2** (Weeks 3-5): Metrics collection
- **Phase 3** (Weeks 5-9): Learning & optimization
- **Phase 4** (Weeks 9-15): Bidirectional feedback
- **Phase 5** (Week 15+): Self-evolution (research)

**Total**: 10-16 weeks to production-ready

---

## 💡 For Each Role

### **biomeOS Developers**
- Build graph executor
- Build metrics collector  
- Build pathway learner
- **Effort**: 10-16 weeks

### **Primal Developers**
- Add structured logging (5 min)
- Declare dependencies (30 min, optional)
- **Effort**: 5 min - 2 hours per primal

### **Niche API Developers**
- Use graph execution API
- Trust system to optimize
- **Effort**: Use existing APIs

---

## 📖 Read More

- **[README.md](./README.md)** - Full index
- **[00_INTRODUCTION.md](./00_INTRODUCTION.md)** - Conceptual overview
- **[01_PHILOSOPHY.md](./01_PHILOSOPHY.md)** - Why this approach?
- **[06_BIOMEOS_IMPLEMENTATION.md](./06_BIOMEOS_IMPLEMENTATION.md)** - What biomeOS needs
- **[07_PRIMAL_REQUIREMENTS.md](./07_PRIMAL_REQUIREMENTS.md)** - What primals need
- **[10_ROADMAP.md](./10_ROADMAP.md)** - Implementation timeline

---

🧠 **Neural API: Orchestration that learns!**
