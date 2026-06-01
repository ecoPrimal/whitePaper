# biomeOS Implementation Guide

**What biomeOS needs to implement for Neural API**

**Date**: January 4, 2026 (revised May 14, 2026 — v3.50+, Phase 1-2 COMPLETE)
**Status**: Implementation Specification — Phases 1-2 COMPLETE, Phase 3 PARTIAL

---

## 🎯 Overview

For Neural API to work, biomeOS needs to evolve from a **static orchestrator** to an **adaptive learning engine**. This document specifies exactly what needs to be built.

---

## 📊 Current State (biomeOS v0.x)

### **What We Have:**

```rust
// ✅ Capability Registry
pub struct CapabilityRegistry {
    primals: HashMap<PrimalId, PrimalInfo>,
    capabilities: HashMap<Capability, Vec<PrimalId>>,
}

// ✅ Primal Orchestrator
pub struct PrimalOrchestrator {
    primals: Vec<Arc<dyn ManagedPrimal>>,
    health_monitor: PrimalHealthMonitor,
}

// ✅ TOML Configuration
[primals.beardog]
binary = "./primals/beardog"
provides = ["Security", "Encryption"]
requires = ["Discovery"]
```

**Status**: Static orchestration works! Primals are spawned, monitored, and coordinated.

---

## 🚀 Required Additions

### **1. Graph Execution Engine**

#### **New Data Structures**

```rust
// FILE: biomeos-core/src/graph_executor.rs

/// A graph of primals with dependencies
#[derive(Debug, Clone)]
pub struct PrimalGraph {
    pub id: GraphId,
    pub name: String,
    pub nodes: Vec<PrimalNode>,
    pub edges: Vec<PrimalEdge>,
    pub coordination_pattern: CoordinationPattern,
}

/// A node in the primal graph
#[derive(Debug, Clone)]
pub struct PrimalNode {
    pub primal_id: PrimalId,
    pub capabilities: Vec<Capability>,
    pub action: PrimalAction,
    pub input: Option<Value>,
    pub output: Option<String>, // Variable name for output
}

/// An edge represents a dependency
#[derive(Debug, Clone)]
pub struct PrimalEdge {
    pub from: PrimalId,
    pub to: PrimalId,
    pub data_flow: Option<DataFlow>, // What data passes between them
}

/// How primals are coordinated
#[derive(Debug, Clone, PartialEq)]
pub enum CoordinationPattern {
    Sequential,      // One after another
    Parallel,        // All at once
    ConditionalDAG,  // Based on results
    Pipeline,        // Streaming data flow
}

/// What action to perform on a primal
#[derive(Debug, Clone)]
pub enum PrimalAction {
    Query { method: String, params: Value },
    Invoke { endpoint: String, body: Value },
    Stream { endpoint: String },
}
```

#### **Graph Executor**

```rust
/// Executes primal graphs
pub struct GraphExecutor {
    registry: Arc<CapabilityRegistry>,
    health_monitor: Arc<PrimalHealthMonitor>,
    metrics_collector: Arc<MetricsCollector>, // NEW!
}

impl GraphExecutor {
    /// Execute a primal graph
    pub async fn execute(&self, graph: PrimalGraph) -> Result<GraphResult, BiomeError> {
        let start = Instant::now();
        
        // Record execution start
        self.metrics_collector.record_graph_start(&graph).await;
        
        // Execute based on coordination pattern
        let result = match graph.coordination_pattern {
            CoordinationPattern::Sequential => self.execute_sequential(&graph).await?,
            CoordinationPattern::Parallel => self.execute_parallel(&graph).await?,
            CoordinationPattern::ConditionalDAG => self.execute_dag(&graph).await?,
            CoordinationPattern::Pipeline => self.execute_pipeline(&graph).await?,
        };
        
        let duration = start.elapsed();
        
        // Record execution complete
        self.metrics_collector.record_graph_complete(&graph, &result, duration).await;
        
        Ok(result)
    }
    
    async fn execute_sequential(&self, graph: &PrimalGraph) -> Result<GraphResult, BiomeError> {
        let mut context = ExecutionContext::new();
        let mut results = Vec::new();
        
        for node in &graph.nodes {
            // Resolve primal
            let primal_info = self.registry.get_primal(&node.primal_id).await?;
            
            // Execute action
            let result = self.execute_node(node, &primal_info, &context).await?;
            
            // Store result in context (for next node)
            if let Some(output_var) = &node.output {
                context.set(output_var, result.clone());
            }
            
            results.push(result);
        }
        
        Ok(GraphResult {
            graph_id: graph.id.clone(),
            success: true,
            results,
            duration: context.elapsed(),
        })
    }
    
    async fn execute_parallel(&self, graph: &PrimalGraph) -> Result<GraphResult, BiomeError> {
        let mut tasks = Vec::new();
        
        for node in &graph.nodes {
            let primal_info = self.registry.get_primal(&node.primal_id).await?;
            let node = node.clone();
            let executor = self.clone();
            
            tasks.push(tokio::spawn(async move {
                executor.execute_node(&node, &primal_info, &ExecutionContext::new()).await
            }));
        }
        
        let results = tokio::try_join_all(tasks).await?;
        
        Ok(GraphResult {
            graph_id: graph.id.clone(),
            success: true,
            results,
            duration: Duration::from_secs(0), // TODO: Track properly
        })
    }
    
    async fn execute_dag(&self, graph: &PrimalGraph) -> Result<GraphResult, BiomeError> {
        // Build dependency graph
        let dag = self.build_dag(graph)?;
        
        // Execute in waves (all nodes with satisfied dependencies)
        let mut context = ExecutionContext::new();
        let mut results = Vec::new();
        
        for wave in dag.waves() {
            let mut wave_tasks = Vec::new();
            
            for node in wave {
                let primal_info = self.registry.get_primal(&node.primal_id).await?;
                let node = node.clone();
                let context = context.clone();
                let executor = self.clone();
                
                wave_tasks.push(tokio::spawn(async move {
                    executor.execute_node(&node, &primal_info, &context).await
                }));
            }
            
            let wave_results = tokio::try_join_all(wave_tasks).await?;
            results.extend(wave_results);
        }
        
        Ok(GraphResult {
            graph_id: graph.id.clone(),
            success: true,
            results,
            duration: context.elapsed(),
        })
    }
    
    async fn execute_node(
        &self,
        node: &PrimalNode,
        primal_info: &PrimalInfo,
        context: &ExecutionContext,
    ) -> Result<Value, BiomeError> {
        let start = Instant::now();
        
        // Execute based on action type
        let result = match &node.action {
            PrimalAction::Query { method, params } => {
                self.query_primal(primal_info, method, params, context).await?
            }
            PrimalAction::Invoke { endpoint, body } => {
                self.invoke_primal(primal_info, endpoint, body, context).await?
            }
            PrimalAction::Stream { endpoint } => {
                self.stream_primal(primal_info, endpoint, context).await?
            }
        };
        
        let duration = start.elapsed();
        
        // Record node execution metrics
        self.metrics_collector.record_node_execution(
            &node.primal_id,
            duration,
            true,
        ).await;
        
        Ok(result)
    }
}
```

**Effort**: 2-3 weeks  
**Dependencies**: Existing capability registry  
**Testing**: Create test graphs, verify execution patterns

---

### **2. Metrics Collector**

#### **New Component**

```rust
// FILE: biomeos-core/src/metrics_collector.rs

/// Collects metrics from graph executions
pub struct MetricsCollector {
    usage_stats: Arc<RwLock<UsageStats>>,
}

/// Statistics about primal usage
#[derive(Debug, Default)]
pub struct UsageStats {
    /// How many times each primal was used
    pub primal_usage: HashMap<PrimalId, u64>,
    
    /// How many times two primals were used together
    pub co_occurrence: HashMap<(PrimalId, PrimalId), u64>,
    
    /// Latency measurements for each primal
    pub primal_latency: HashMap<PrimalId, Vec<Duration>>,
    
    /// Success/failure counts
    pub primal_success: HashMap<PrimalId, (u64, u64)>, // (success, total)
    
    /// Graph execution times
    pub graph_latency: HashMap<GraphId, Vec<Duration>>,
    
    /// Timestamp of first/last execution
    pub first_seen: HashMap<GraphId, Instant>,
    pub last_seen: HashMap<GraphId, Instant>,
}

impl MetricsCollector {
    pub async fn record_node_execution(
        &self,
        primal_id: &PrimalId,
        duration: Duration,
        success: bool,
    ) {
        let mut stats = self.usage_stats.write().await;
        
        // Update usage count
        *stats.primal_usage.entry(primal_id.clone()).or_insert(0) += 1;
        
        // Update latency
        stats.primal_latency
            .entry(primal_id.clone())
            .or_insert_with(Vec::new)
            .push(duration);
        
        // Update success rate
        let (successes, total) = stats.primal_success
            .entry(primal_id.clone())
            .or_insert((0, 0));
        *total += 1;
        if success {
            *successes += 1;
        }
    }
    
    pub async fn record_graph_complete(
        &self,
        graph: &PrimalGraph,
        result: &GraphResult,
        duration: Duration,
    ) {
        let mut stats = self.usage_stats.write().await;
        
        // Record co-occurrence (which primals used together)
        for edge in &graph.edges {
            *stats.co_occurrence
                .entry((edge.from.clone(), edge.to.clone()))
                .or_insert(0) += 1;
        }
        
        // Record graph latency
        stats.graph_latency
            .entry(graph.id.clone())
            .or_insert_with(Vec::new)
            .push(duration);
        
        // Update timestamps
        let now = Instant::now();
        stats.last_seen.insert(graph.id.clone(), now);
        stats.first_seen.entry(graph.id.clone()).or_insert(now);
    }
    
    /// Get statistics for analysis
    pub async fn get_stats(&self) -> UsageStats {
        self.usage_stats.read().await.clone()
    }
}
```

**Effort**: 1-2 weeks  
**Dependencies**: Graph executor  
**Testing**: Execute graphs, verify metrics collection

---

### **3. Pathway Learner**

#### **New Component**

```rust
// FILE: biomeos-core/src/pathway_learner.rs

/// Learns optimal coordination patterns from usage
pub struct PathwayLearner {
    metrics: Arc<MetricsCollector>,
    optimizations: Arc<RwLock<HashMap<GraphId, OptimizedGraph>>>,
}

/// An optimized version of a primal graph
#[derive(Debug, Clone)]
pub struct OptimizedGraph {
    pub original_graph: PrimalGraph,
    pub optimized_graph: PrimalGraph,
    pub optimization_type: OptimizationType,
    pub expected_speedup: f64,
    pub confidence: f64,
    pub reason: String,
}

#[derive(Debug, Clone)]
pub enum OptimizationType {
    Parallelization,    // Convert sequential to parallel
    Prewarming,         // Pre-warm frequently used primals
    Batching,           // Batch multiple operations
    Caching,            // Cache results
    Reordering,         // Reorder for better performance
}

impl PathwayLearner {
    /// Analyze usage and suggest optimizations
    pub async fn analyze(&self, graph_id: &GraphId) -> Result<Vec<OptimizedGraph>, BiomeError> {
        let stats = self.metrics.get_stats().await;
        let mut optimizations = Vec::new();
        
        // Check for parallelization opportunities
        if let Some(parallel_opt) = self.check_parallelization(graph_id, &stats).await? {
            optimizations.push(parallel_opt);
        }
        
        // Check for prewarming opportunities
        if let Some(prewarm_opt) = self.check_prewarming(graph_id, &stats).await? {
            optimizations.push(prewarm_opt);
        }
        
        // Check for batching opportunities
        if let Some(batch_opt) = self.check_batching(graph_id, &stats).await? {
            optimizations.push(batch_opt);
        }
        
        Ok(optimizations)
    }
    
    async fn check_parallelization(
        &self,
        graph_id: &GraphId,
        stats: &UsageStats,
    ) -> Result<Option<OptimizedGraph>, BiomeError> {
        // Logic:
        // 1. Find nodes in the graph that are sequential
        // 2. Check if they have data dependencies (edges between them)
        // 3. If no dependencies, they can run in parallel!
        // 4. Calculate expected speedup based on latency stats
        
        // Pseudocode:
        // if graph.pattern == Sequential {
        //     for each pair of consecutive nodes:
        //         if no edge between them:
        //             can_parallelize = true
        //             speedup = max(latency_a, latency_b) / (latency_a + latency_b)
        // }
        
        // TODO: Implement actual logic
        Ok(None)
    }
    
    /// Apply an optimization to a graph
    pub async fn apply_optimization(
        &self,
        graph: &PrimalGraph,
        optimization: &OptimizedGraph,
    ) -> Result<PrimalGraph, BiomeError> {
        // Store optimization for future use
        self.optimizations.write().await.insert(
            graph.id.clone(),
            optimization.clone(),
        );
        
        Ok(optimization.optimized_graph.clone())
    }
    
    /// Get cached optimization if available
    pub async fn get_optimization(&self, graph_id: &GraphId) -> Option<OptimizedGraph> {
        self.optimizations.read().await.get(graph_id).cloned()
    }
}
```

**Effort**: 3-4 weeks  
**Dependencies**: Metrics collector, graph executor  
**Testing**: Execute same graph 100+ times, verify optimizations suggested

---

## 🔗 API Surface

### **Public API for Niche Developers**

```rust
// FILE: biomeos-core/src/lib.rs

impl BiomeOS {
    /// Execute a primal graph (NEW!)
    pub async fn execute_graph(&self, graph: PrimalGraph) -> Result<GraphResult, BiomeError> {
        self.graph_executor.execute(graph).await
    }
    
    /// Get optimization suggestions (NEW!)
    pub async fn suggest_optimizations(
        &self,
        graph_id: &GraphId,
    ) -> Result<Vec<OptimizedGraph>, BiomeError> {
        self.pathway_learner.analyze(graph_id).await
    }
    
    /// Apply an optimization (NEW!)
    pub async fn apply_optimization(
        &self,
        graph: &PrimalGraph,
        optimization: &OptimizedGraph,
    ) -> Result<PrimalGraph, BiomeError> {
        self.pathway_learner.apply_optimization(graph, optimization).await
    }
    
    /// Get usage statistics (NEW!)
    pub async fn get_metrics(&self) -> UsageStats {
        self.metrics_collector.get_stats().await
    }
}
```

---

## 📁 File Structure

```
biomeos-core/src/
├── lib.rs                     (updated: export new modules)
├── graph_executor.rs          (NEW: execute primal graphs)
├── metrics_collector.rs       (NEW: collect usage metrics)
├── pathway_learner.rs         (NEW: learn & optimize)
│
├── capability_registry.rs     (EXISTING: primal discovery)
├── primal_orchestrator.rs     (EXISTING: primal lifecycle)
├── primal_health.rs           (EXISTING: health monitoring)
│
└── bin/
    └── tower.rs               (updated: expose graph execution)
```

---

## 🧪 Testing Strategy

### **Unit Tests**

```rust
#[cfg(test)]
mod tests {
    #[tokio::test]
    async fn test_sequential_graph() {
        let graph = PrimalGraph {
            nodes: vec![node_a, node_b, node_c],
            pattern: Sequential,
            ...
        };
        
        let result = executor.execute(graph).await.unwrap();
        assert_eq!(result.results.len(), 3);
    }
    
    #[tokio::test]
    async fn test_parallel_graph() {
        let graph = PrimalGraph {
            nodes: vec![node_a, node_b],
            pattern: Parallel,
            ...
        };
        
        let result = executor.execute(graph).await.unwrap();
        // Both should complete in ~max(latency_a, latency_b)
    }
    
    #[tokio::test]
    async fn test_metrics_collection() {
        executor.execute(graph).await.unwrap();
        
        let stats = metrics.get_stats().await;
        assert_eq!(stats.primal_usage["primal_a"], 1);
    }
}
```

### **Integration Tests**

```rust
#[tokio::test]
async fn test_pathway_learning() {
    let graph = create_test_graph();
    
    // Execute 100 times
    for _ in 0..100 {
        biome.execute_graph(graph.clone()).await.unwrap();
    }
    
    // Check if optimizations suggested
    let optimizations = biome.suggest_optimizations(&graph.id).await.unwrap();
    assert!(!optimizations.is_empty());
}
```

---

## 📊 Implementation Phases

### **Phase 1: Graph Execution** (2-3 weeks)
- [ ] Implement `PrimalGraph` data structures
- [ ] Implement `GraphExecutor` with Sequential, Parallel, DAG support
- [ ] Test with simple 2-3 node graphs
- [ ] Integrate with existing capability registry

### **Phase 2: Metrics Collection** (1-2 weeks)
- [ ] Implement `MetricsCollector`
- [ ] Collect primal usage, latency, success rate
- [ ] Add API to query metrics
- [ ] Test metrics accuracy

### **Phase 3: Pathway Learning** (3-4 weeks)
- [ ] Implement `PathwayLearner`
- [ ] Add parallelization detection
- [ ] Add prewarming detection
- [ ] Add optimization suggestion API
- [ ] Test on 100+ graph executions

### **Phase 4: Integration & Polish** (1-2 weeks)
- [ ] Integrate all components
- [ ] Add comprehensive tests
- [ ] Document all APIs
- [ ] Create example niche API (RootPulse)

---

## 🎯 Success Criteria

### **Phase 1: Graph Execution**
- ✅ Can execute sequential graphs
- ✅ Can execute parallel graphs
- ✅ Can execute DAG graphs
- ✅ All primals in graph are invoked correctly

### **Phase 2: Metrics Collection**
- ✅ Metrics are collected for all executions
- ✅ Co-occurrence tracked correctly
- ✅ Latency measurements accurate
- ✅ API returns correct statistics

### **Phase 3: Pathway Learning**
- ✅ Parallelization opportunities detected
- ✅ Prewarming suggestions generated
- ✅ Optimizations can be applied
- ✅ Speedup predictions reasonably accurate (±20%)

---

## 🚀 Next Steps

After biomeOS implements these components:
1. **Primal teams** can add metrics reporting (see `07_PRIMAL_REQUIREMENTS.md`)
2. **Niche API developers** can build high-level APIs (see `08_NICHE_API_PATTERNS.md`)
3. **RootPulse** can be migrated to use Neural API (see `09_ROOTPULSE_CASE_STUDY.md`)

---

---

## May 2026 Addendum: Current State (biomeOS v3.50)

Much of the Phase 1 and Phase 2 work described above is now **COMPLETE**.
The actual implementation differs from the January 2026 pseudocode in
important ways:

### What's implemented (v3.50)

- **7,924 tests** — comprehensive coverage
- **25 workspace crates** including `biomeos-graph`, `biomeos-atomic-deploy`,
  `neural-api-client`, `neural-api-client-sync`
- **320+ capability translations** across 27 domains
- **GraphExecutor** in `biomeos-atomic-deploy` — Sequential, Parallel,
  Continuous (ContinuousExecutor with TickClock, feedback edges, session lifecycle)
- **MetricsCollector** — redb-backed (persistent) + in-memory
- **NeuralRouter** — capability registry + tarpc escalation with JSON-RPC fallback
- **Token forwarding** — `_bearer_token` propagation through all capability paths (v3.50)
- **MethodGate** — JH-0/JH-2 resource envelope + `auth.check` compatibility
- **`composition.reload`** — hot reload aligned with primalSpring `CompositionContext::reload()`
- **55+ deploy/workflow graphs** in biomeOS `graphs/`

### primalSpring integration (NeuralBridge)

`ecoPrimal/src/ipc/neural_bridge.rs` provides the client bridge:

- `NeuralBridge::discover()` — tiered socket discovery (env → XDG → /tmp)
- `health_check()` — liveness probe with fallback chain
- `capability_call(capability, operation, args)` — semantic routing
- `graph_deploy(graph)` — execute a graph via the neural API
- `graph_status(id)`, `graph_rollback(id)` — lifecycle management
- `topology_rescan()` — force re-discovery of late-registering primals
- `discover_capability(cap)`, `discover_domain(domain)` — query routing

### What remains

- **PathwayLearner** — code exists but not wired into execution path
- **ConditionalDag** — parsed but executes as Sequential
- **Pipeline streaming** — parsed but executes as Sequential
- **Continuous via JSON-RPC** — only runs via `biomeos continuous` CLI
- **Unified graph schema** — `[[nodes]]` vs `[[graph.nodes]]` split
- **Signal dispatch** — NeuralRouter does not yet recognize atomic tier names
  (`tower`, `node`, `nest`, `nucleus`) as signal triggers

---

*"biomeOS: From orchestrator to adaptive learning engine — Phase 1-2 DONE, Phase 3 wiring next."*

