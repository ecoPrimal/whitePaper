# 🚀 Neural API Implementation Roadmap

**Timeline and milestones for adaptive orchestration**

**Date**: January 4, 2026  
**Status**: Implementation Plan

---

## 🎯 Overview

This roadmap outlines the path from **static orchestration** (biomeOS v0.x) to **adaptive orchestration** (Neural API v1.0).

**Total Estimated Time**: 10-16 weeks  
**Approach**: Incremental, each phase builds on the previous  
**Risk**: Low (builds on existing foundation)

---

## 📊 Phases

```
Phase 1: Graph Execution        (Weeks 1-3)   ■■■□□□□□□□
Phase 2: Metrics Collection     (Weeks 3-5)   □□■■□□□□□□
Phase 3: Pathway Learning       (Weeks 5-9)   □□□■■■■□□□
Phase 4: Bidirectional Feedback (Weeks 9-15)  □□□□□□■■■■■■
Phase 5: Self-Evolution         (Weeks 15+)   □□□□□□□□□■■ (Research)
```

---

## 🏗️ Phase 1: Graph Execution

**Duration**: 2-3 weeks  
**Goal**: Execute primal graphs (not just linear workflows)  
**Status**: 🟡 Ready to start

### **Deliverables**

1. **Data Structures** (`biomeos-core/src/graph_executor.rs`)
   - `PrimalGraph` - Represents a coordination pattern
   - `PrimalNode` - Individual primal in the graph
   - `PrimalEdge` - Dependencies between primals
   - `CoordinationPattern` - Sequential, Parallel, DAG, Pipeline

2. **Graph Executor**
   - Execute sequential graphs
   - Execute parallel graphs
   - Execute DAG graphs (wave-based)
   - Execute pipeline graphs (streaming)

3. **Integration**
   - Integrate with existing `CapabilityRegistry`
   - Add `execute_graph()` to `BiomeOS` API
   - Update `tower` CLI to support graphs

### **Success Criteria**

- ✅ Can execute a 2-node sequential graph (A → B)
- ✅ Can execute a 2-node parallel graph (A, B)
- ✅ Can execute a 4-node DAG graph (RootPulse commit)
- ✅ All nodes execute successfully
- ✅ Results returned correctly

### **Testing**

```rust
#[tokio::test]
async fn test_rootpulse_commit_graph() {
    let graph = PrimalGraph {
        nodes: vec![
            nestgate_store_node,
            beardog_sign_node,
            sweetgrass_attribute_node,
            loamspine_append_node,
        ],
        edges: vec![
            nestgate → beardog,
            beardog → sweetgrass,
            sweetgrass → loamspine,
        ],
        pattern: Sequential,
    };
    
    let result = biome.execute_graph(graph).await.unwrap();
    assert_eq!(result.results.len(), 4);
    assert!(result.success);
}
```

### **Risks & Mitigation**

| Risk | Mitigation |
|------|------------|
| Graph cycles (A → B → A) | Validate DAG before execution |
| Node failures | Rollback strategy, partial results |
| Performance overhead | Benchmark vs. direct calls |

### **Week-by-Week Plan**

**Week 1:**
- [ ] Design data structures
- [ ] Implement `PrimalGraph`, `PrimalNode`, `PrimalEdge`
- [ ] Basic sequential executor

**Week 2:**
- [ ] Parallel executor
- [ ] DAG executor (wave-based)
- [ ] Integration with capability registry

**Week 3:**
- [ ] Testing & debugging
- [ ] Documentation
- [ ] Example: RootPulse commit graph

---

## 📊 Phase 2: Metrics Collection

**Duration**: 1-2 weeks  
**Goal**: Collect usage metrics from graph executions  
**Status**: 🟡 Depends on Phase 1

### **Deliverables**

1. **Metrics Collector** (`biomeos-core/src/metrics_collector.rs`)
   - Track primal usage counts
   - Track co-occurrence (which primals used together)
   - Track latency per primal
   - Track success/failure rates

2. **Storage**
   - In-memory stats (for current session)
   - Optional persistence (for long-term learning)

3. **API**
   - `get_metrics()` - Query current stats
   - `export_metrics()` - Export for analysis

### **Success Criteria**

- ✅ Metrics collected for all graph executions
- ✅ Co-occurrence tracked correctly
- ✅ Latency measurements accurate
- ✅ API returns correct statistics

### **Testing**

```rust
#[tokio::test]
async fn test_metrics_collection() {
    // Execute graph 10 times
    for _ in 0..10 {
        biome.execute_graph(commit_graph.clone()).await.unwrap();
    }
    
    let stats = biome.get_metrics().await;
    assert_eq!(stats.primal_usage["nestgate"], 10);
    assert_eq!(stats.primal_usage["beardog"], 10);
    assert_eq!(stats.co_occurrence[("nestgate", "beardog")], 10);
}
```

### **Week-by-Week Plan**

**Week 1:**
- [ ] Implement `MetricsCollector`
- [ ] Hook into `GraphExecutor`
- [ ] Test with simple graphs

**Week 2:**
- [ ] Add query API
- [ ] Add export functionality
- [ ] Documentation

---

## 🧠 Phase 3: Pathway Learning

**Duration**: 3-4 weeks  
**Goal**: Analyze metrics and suggest optimizations  
**Status**: 🟡 Depends on Phase 2

### **Deliverables**

1. **Pathway Learner** (`biomeos-core/src/pathway_learner.rs`)
   - Detect parallelization opportunities
   - Detect prewarming opportunities
   - Detect batching opportunities
   - Suggest optimizations

2. **Optimization Engine**
   - Apply parallelization
   - Apply prewarming
   - Apply batching
   - Track optimization effectiveness

3. **API**
   - `suggest_optimizations()` - Get suggestions
   - `apply_optimization()` - Apply an optimization
   - `get_optimization()` - Retrieve cached optimization

### **Success Criteria**

- ✅ Can detect when 2 nodes can run in parallel
- ✅ Can suggest parallelization with expected speedup
- ✅ Can apply optimization to graph
- ✅ Optimized graph executes correctly
- ✅ Speedup prediction accurate (±20%)

### **Testing**

```rust
#[tokio::test]
async fn test_parallelization_detection() {
    // Execute sequential graph 100 times
    for _ in 0..100 {
        biome.execute_graph(sequential_graph.clone()).await.unwrap();
    }
    
    // Check for optimization suggestions
    let opts = biome.suggest_optimizations(&sequential_graph.id).await.unwrap();
    
    assert!(!opts.is_empty());
    assert_eq!(opts[0].optimization_type, OptimizationType::Parallelization);
    assert!(opts[0].expected_speedup > 1.0);
}
```

### **Algorithms**

#### **Parallelization Detection**

```rust
// Pseudocode:
for each pair of consecutive nodes (A, B) in sequential graph:
    if no edge A → B:  // No data dependency
        if avg_latency(A) > threshold && avg_latency(B) > threshold:
            // Both are slow enough to benefit from parallelization
            suggest: run A and B in parallel
            expected_speedup = (latency_A + latency_B) / max(latency_A, latency_B)
```

#### **Prewarming Detection**

```rust
// Pseudocode:
for each primal P:
    if usage_frequency(P) > threshold:
        if startup_latency(P) > threshold:
            suggest: prewarm P (keep it running)
            expected_speedup = startup_latency(P) / usage_frequency(P)
```

#### **Batching Detection**

```rust
// Pseudocode:
for each primal P:
    if execution_count_per_minute(P) > threshold:
        if P supports batching:
            suggest: batch multiple requests to P
            expected_speedup = overhead_per_request * batch_size
```

### **Week-by-Week Plan**

**Week 1:**
- [ ] Implement parallelization detection
- [ ] Test on simple cases

**Week 2:**
- [ ] Implement prewarming detection
- [ ] Implement batching detection
- [ ] Test on RootPulse workload

**Week 3:**
- [ ] Optimization application logic
- [ ] Track optimization effectiveness
- [ ] Refine algorithms based on results

**Week 4:**
- [ ] Documentation
- [ ] Performance benchmarks
- [ ] Example: RootPulse optimizations

---

## 🔄 Phase 4: Bidirectional Feedback

**Duration**: 4-6 weeks  
**Goal**: Enable learning from niche APIs to primals  
**Status**: 🟡 Depends on Phase 3

### **Deliverables**

1. **Primal Metrics API**
   - Define standard metrics format
   - Implement Unix socket metrics collector
   - Document for primal teams

2. **Niche API Framework**
   - `NicheAPI` trait
   - Learning integration
   - Example: `RootPulseAPI`

3. **Primal Enhancements** (work with primal teams)
   - Add structured logging (all primals, 5 min each)
   - Add dependency hints (key primals, 30 min each)
   - Add cost estimates (critical primals, 1 hour each)

4. **Feedback Loop**
   - Primals report metrics
   - biomeOS aggregates and learns
   - Niche APIs adapt based on learning
   - Users see improvements

### **Success Criteria**

- ✅ Primals can report metrics to biomeOS
- ✅ biomeOS aggregates primal metrics
- ✅ Niche APIs use learned patterns
- ✅ User-visible performance improvements
- ✅ At least 3 primals enhanced (BearDog, Songbird, LoamSpine)

### **Primal Enhancement Schedule**

**Week 1-2: Foundational Primals**
- [ ] BearDog: Structured logging, dependency hints
- [ ] Songbird: Structured logging, peer statistics
- [ ] LoamSpine: Structured logging, batching hints

**Week 3-4: Supporting Primals**
- [ ] NestGate: Structured logging, caching hints
- [ ] ToadStool: Workflow dependencies
- [ ] SweetGrass: Dependency hints

**Week 5-6: Niche API Development**
- [ ] Implement `RootPulseAPI`
- [ ] Integrate with biomeOS learning
- [ ] Test end-to-end improvements
- [ ] Documentation & examples

### **Week-by-Week Plan**

**Week 1:**
- [ ] Define metrics API
- [ ] Implement metrics collector
- [ ] Document for primal teams

**Weeks 2-4:**
- [ ] Work with each primal team
- [ ] Implement enhancements
- [ ] Test metrics collection

**Weeks 5-6:**
- [ ] Build example niche API (RootPulse)
- [ ] End-to-end testing
- [ ] Performance validation

---

## 🌱 Phase 5: Self-Evolution (Research)

**Duration**: 6-8 weeks (ongoing research)  
**Goal**: Discover new coordination patterns automatically  
**Status**: 🔵 Research phase

### **Research Questions**

1. **Pattern Discovery**
   - Can biomeOS discover novel coordination patterns?
   - What algorithms work best? (clustering, ML, genetic algorithms?)
   - How to validate discovered patterns?

2. **Distributed Learning**
   - Can learning be shared across towers?
   - How to aggregate patterns from multiple towers?
   - Privacy considerations?

3. **Adaptive Strategies**
   - Can biomeOS adapt to changing conditions? (network, load, failures)
   - How to balance exploration vs. exploitation?
   - When to discard old patterns?

### **Experimental Features**

1. **Pattern Clustering**
   - Group similar graph executions
   - Identify common sub-patterns
   - Abstract into reusable templates

2. **Genetic Algorithm Optimization**
   - Generate variant graphs
   - Test performance
   - Evolve towards optimal

3. **Multi-Tower Learning**
   - Share learned patterns via Songbird
   - Aggregate statistics
   - Federated learning approach

### **Success Criteria**

- ⏳ System discovers at least 1 novel pattern
- ⏳ Novel pattern provides measurable benefit (>10% speedup)
- ⏳ Learning can be shared across 2+ towers
- ⏳ Adaptive strategies respond to changing conditions

### **Timeline**

**Months 1-2:** Research & prototyping  
**Months 3-4:** Implementation & testing  
**Months 5-6:** Validation & refinement  
**Ongoing:** Continuous improvement

---

## 📅 Overall Timeline

### **Q1 2026 (Weeks 1-12)**

**January (Weeks 1-4):**
- [ ] Phase 1: Graph Execution (Weeks 1-3)
- [ ] Phase 2: Metrics Collection (Weeks 3-5)

**February (Weeks 5-8):**
- [ ] Phase 2 complete (Week 5)
- [ ] Phase 3: Pathway Learning (Weeks 5-9)

**March (Weeks 9-12):**
- [ ] Phase 3 complete (Week 9)
- [ ] Phase 4: Bidirectional Feedback (Weeks 9-15)

### **Q2 2026 (Weeks 13-24)**

**April (Weeks 13-16):**
- [ ] Phase 4 complete (Week 15)
- [ ] Production testing with RootPulse
- [ ] Phase 5: Research begins (Week 15+)

**May-June (Weeks 17-24):**
- [ ] Phase 5: Self-Evolution research
- [ ] Expand to other niche APIs (Hive, Reef)
- [ ] Multi-tower federation testing

---

## 🎯 Milestones

### **Milestone 1: Graph Execution (Week 3)**
- ✅ Can execute primal graphs
- ✅ Basic RootPulse commit works via graph
- **Demo**: Show sequential vs. parallel execution

### **Milestone 2: Learning (Week 9)**
- ✅ Metrics collected and analyzed
- ✅ Optimizations suggested automatically
- **Demo**: Show 30% speedup from parallelization

### **Milestone 3: Production Ready (Week 15)**
- ✅ Primals enhanced with metrics
- ✅ RootPulse uses Neural API
- ✅ User-visible improvements
- **Demo**: RootPulse 2x faster than Day 1

### **Milestone 4: Ecosystem (Week 24)**
- ✅ Multiple niche APIs (RootPulse, Hive, Reef)
- ✅ Multi-tower learning
- ✅ Self-evolution research complete
- **Demo**: System discovers novel optimizations

---

## 🧪 Validation Strategy

### **Performance Benchmarks**

```bash
# Baseline (biomeOS v0.x, no Neural API)
$ rootpulse commit "Test" --iterations 1000
Average: 50ms per commit

# After Phase 3 (with optimizations)
$ rootpulse commit "Test" --iterations 1000
Average: 35ms per commit  (30% faster! ✅)

# After Phase 4 (with primal enhancements)
$ rootpulse commit "Test" --iterations 1000
Average: 25ms per commit  (50% faster! ✅)
```

### **Learning Validation**

```bash
# Show learned patterns
$ tower graph analyze rootpulse:commit
Pattern: commit
Executions: 1000
Optimizations discovered:
  ✓ Parallelization: nestgate + sweetgrass (30% speedup)
  ✓ Prewarming: beardog (5% speedup)
  ✓ Batching: loamspine (15% speedup)
Total improvement: 50%
```

---

## 📊 Resource Requirements

### **Team**

- **1 biomeOS Developer**: Graph execution, metrics, learning
- **Primal Teams**: 1 hour each for enhancements
- **Niche API Developer**: RootPulse integration

### **Infrastructure**

- **Development Environment**: Standard (no special requirements)
- **Testing**: 2 USB towers for multi-tower federation
- **Benchmarking**: Long-running test suite (1000+ iterations)

### **Dependencies**

- Existing biomeOS v0.x (capability registry, orchestrator)
- Primal teams available for enhancements (Phase 4)
- RootPulse as example niche API

---

## 🚀 Next Steps

### **Immediate (This Week)**

1. [ ] Review whitepaper series with all teams
2. [ ] Get approval to proceed
3. [ ] Set up tracking (GitHub issues, project board)

### **Week 1**

1. [ ] Begin Phase 1 implementation
2. [ ] Design data structures
3. [ ] Implement basic sequential executor

### **Week 2**

1. [ ] Parallel and DAG executors
2. [ ] Integration with capability registry
3. [ ] Initial testing

### **Week 3**

1. [ ] Complete Phase 1
2. [ ] Begin Phase 2 (metrics)
3. [ ] Demo Milestone 1

---

## 📈 Success Metrics

### **Technical Metrics**

- [ ] Graph execution latency < 5% overhead
- [ ] Optimization suggestions accurate (±20%)
- [ ] Performance improvements measured (>30% speedup)
- [ ] System learns from 100+ executions

### **Adoption Metrics**

- [ ] RootPulse migrated to Neural API
- [ ] 3+ primal teams enhanced for learning
- [ ] 1+ other niche API built on Neural API
- [ ] Multi-tower federation tested

### **Ecosystem Impact**

- [ ] Whitepaper published and shared
- [ ] Pattern templates available for reuse
- [ ] Learning can be shared across towers
- [ ] Community contributions (new niche APIs)

---

🚀 **Neural API: From vision to reality in 12-24 weeks!**

*"The journey of a thousand miles begins with a single step."*  
**— Our step: Phase 1, Week 1, Day 1**

