# 🦴 Primal Requirements for Neural API

**What primals need to provide to enable adaptive orchestration**

**Date**: January 4, 2026  
**Status**: Implementation Specification

---

## 🎯 Overview

**Good news**: Primals don't need major changes! Neural API is designed to work with **minimal primal modifications**.

**Core principle**: Primals stay simple, biomeOS gets smart.

---

## ✅ What Primals Already Do (No Changes Needed!)

### **1. Capability Declaration**

Primals already declare what they provide:

```rust
// BearDog already does this:
pub fn capabilities() -> Vec<Capability> {
    vec![
        Capability::Security,
        Capability::Encryption,
        Capability::Trust,
    ]
}
```

**Status**: ✅ **Already works!** No changes needed.

---

### **2. Standard API**

Primals already expose APIs (HTTP, Unix socket, etc.):

```rust
// Songbird already does this:
// Unix socket at /tmp/songbird-{family}-{node}.sock
// JSON-RPC 2.0 API

{
  "jsonrpc": "2.0",
  "method": "discovery.register",
  "params": { ... },
  "id": 1
}
```

**Status**: ✅ **Already works!** No changes needed.

---

### **3. Health Checks**

Primals already support health checks:

```bash
# BearDog already supports:
$ curl http://localhost:9000/health
{"status": "healthy"}

# Songbird already supports:
$ echo '{"method":"health.check"}' | nc -U /tmp/songbird.sock
{"status": "ok"}
```

**Status**: ✅ **Already works!** No changes needed.

---

## 🆕 Optional Enhancements (For Better Learning)

Primals can **optionally** provide additional information to help biomeOS learn better. **These are all optional!**

---

### **Enhancement 1: Metrics Reporting**

#### **What It Is**

Primals can report execution metrics to biomeOS:

```rust
pub struct ExecutionMetrics {
    pub latency: Duration,
    pub cpu_usage: f64,      // 0.0-1.0
    pub memory_usage: u64,   // bytes
    pub success: bool,
}
```

#### **How to Implement**

**Option A: Passive (Recommended for most primals)**

Just log metrics in a structured format:

```rust
// Primal doesn't need to know about biomeOS
// Just log with structured fields
tracing::info!(
    primal_id = "beardog",
    operation = "sign",
    latency_ms = 3.5,
    success = true,
    "Operation complete"
);

// biomeOS can scrape logs for metrics!
```

**Effort**: 5 minutes (add structured logging fields)  
**Impact**: biomeOS can learn from logs

---

**Option B: Active (For primals that want direct integration)**

Report metrics via biomeOS API:

```rust
// Primal reports directly to biomeOS
impl BearDog {
    async fn sign(&self, data: &[u8]) -> Result<Signature> {
        let start = Instant::now();
        
        // Do the work
        let signature = self.do_sign(data)?;
        
        let duration = start.elapsed();
        
        // Report to biomeOS (optional!)
        if let Some(biome_socket) = env::var("BIOMEOS_METRICS_SOCKET").ok() {
            self.report_metrics(biome_socket, ExecutionMetrics {
                latency: duration,
                success: true,
                ...
            }).await.ok(); // Ignore errors (don't block on metrics)
        }
        
        Ok(signature)
    }
}
```

**Effort**: 1-2 hours (add metrics reporting)  
**Impact**: biomeOS gets real-time metrics

---

#### **When to Use Each**

| Approach | Best For | Effort | Accuracy |
|----------|----------|--------|----------|
| **Passive (logs)** | Most primals | 5 min | Good |
| **Active (direct)** | Critical primals | 1-2 hours | Excellent |

**Recommendation**: Start with **passive** (logs). Upgrade to **active** if you need real-time feedback.

---

### **Enhancement 2: Dependency Hints**

#### **What It Is**

Primals can declare **data dependencies** for operations:

```rust
// BearDog can declare: "To sign, I need data first"
pub struct OperationDependencies {
    pub operation: String,
    pub requires: Vec<String>, // What data/state needed
}

// Example:
beardog.dependencies() = {
    "sign": ["data"],
    "verify": ["data", "signature", "public_key"],
    "encrypt": ["data", "recipient_did"],
}
```

**Why?** biomeOS can use this to detect parallelization opportunities!

```rust
// biomeOS learns:
// - "sign" requires "data"
// - "attribute" requires "commit" (different data!)
// → They can run in parallel!
```

#### **How to Implement**

```rust
// Add to primal's capability declaration
impl BearDog {
    pub fn operation_dependencies() -> HashMap<String, Vec<String>> {
        hashmap! {
            "sign" => vec!["data"],
            "verify" => vec!["data", "signature", "public_key"],
            "encrypt" => vec!["data", "recipient_did"],
            "decrypt" => vec!["encrypted_data", "recipient_did"],
        }
    }
}
```

**Effort**: 30 minutes (document dependencies)  
**Impact**: biomeOS can auto-detect parallelization

---

### **Enhancement 3: Cost Estimates**

#### **What It Is**

Primals can provide **cost estimates** for operations:

```rust
pub struct OperationCost {
    pub operation: String,
    pub typical_latency: Duration,
    pub cpu_intensity: CostLevel,  // Low, Medium, High
    pub memory_usage: u64,
}

// Example:
beardog.cost_estimates() = {
    "sign": OperationCost {
        typical_latency: Duration::from_millis(3),
        cpu_intensity: CostLevel::Medium,
        memory_usage: 1024, // 1KB
    },
    "encrypt": OperationCost {
        typical_latency: Duration::from_millis(5),
        cpu_intensity: CostLevel::High,
        memory_usage: 4096, // 4KB
    },
}
```

**Why?** biomeOS can use this for scheduling and resource allocation!

```rust
// biomeOS learns:
// - "encrypt" is High CPU → schedule on less-loaded core
// - "sign" is fast → can batch multiple requests
```

#### **How to Implement**

```rust
impl BearDog {
    pub fn operation_costs() -> HashMap<String, OperationCost> {
        hashmap! {
            "sign" => OperationCost {
                typical_latency: Duration::from_millis(3),
                cpu_intensity: CostLevel::Medium,
                memory_usage: 1024,
            },
            // ... more operations
        }
    }
}
```

**Effort**: 1 hour (benchmark and document)  
**Impact**: biomeOS can optimize scheduling

---

## 📋 Implementation Checklist

### **Minimal (All Primals Should Do This)**

- [x] ✅ **Declare capabilities** (already done!)
- [x] ✅ **Expose standard API** (already done!)
- [x] ✅ **Support health checks** (already done!)

**Status**: **All primals are already compatible with Neural API!**

---

### **Recommended (For Better Learning)**

- [ ] 🟡 **Add structured logging** for metrics (5 minutes)
  - Add `latency_ms`, `success`, `operation` fields to logs
  - biomeOS can scrape for learning

**Status**: Quick win, high impact!

---

### **Advanced (For Optimal Performance)**

- [ ] 🔵 **Declare operation dependencies** (30 minutes)
  - Document what data each operation needs
  - Enables auto-parallelization

- [ ] 🔵 **Provide cost estimates** (1 hour)
  - Benchmark typical latencies
  - Document CPU/memory intensity
  - Enables optimal scheduling

- [ ] 🔵 **Direct metrics reporting** (1-2 hours)
  - Integrate with biomeOS metrics API
  - Real-time performance tracking

**Status**: Nice to have, not required!

---

## 🦴 Primal-Specific Recommendations

### **BearDog (Security Primal)**

**Current Status**: ✅ Already compatible!

**Recommended Enhancements**:
1. ✅ **Structured logging** (5 min)
   - Log `operation`, `latency_ms`, `key_type`
   - biomeOS can learn signing patterns

2. 🟡 **Operation dependencies** (30 min)
   - `sign`: requires `data`
   - `verify`: requires `data`, `signature`, `public_key`
   - `encrypt`: requires `data`, `recipient_did`

3. 🔵 **Cost estimates** (1 hour)
   - Benchmark Ed25519 signing (typically ~3ms)
   - Benchmark encryption (typically ~5ms)

**Impact**: biomeOS can batch signing requests, pre-warm for high-traffic periods

---

### **Songbird (Discovery Primal)**

**Current Status**: ✅ Already compatible!

**Recommended Enhancements**:
1. ✅ **Structured logging** (5 min)
   - Log `operation`, `peer_count`, `latency_ms`
   - biomeOS can learn discovery patterns

2. 🟡 **Operation dependencies** (30 min)
   - `discover`: no dependencies (can run anytime)
   - `register`: requires `primal_info`
   - `query`: requires `capability`

3. 🔵 **Peer statistics** (1 hour)
   - Report active peer count
   - Report discovery success rate
   - biomeOS can predict discovery latency

**Impact**: biomeOS can pre-warm discovery for high-peer-count scenarios

---

### **ToadStool (Compute Orchestrator)**

**Current Status**: ✅ Already compatible!

**Recommended Enhancements**:
1. ✅ **Structured logging** (5 min)
   - Log `workflow`, `duration_ms`, `resource_usage`
   - biomeOS can learn workflow patterns

2. 🟡 **Workflow dependencies** (30 min)
   - Document which workflows depend on which capabilities
   - `run_workflow`: requires `Security`, `Discovery`

3. 🔵 **Resource usage** (1 hour)
   - Report CPU/memory per workflow
   - biomeOS can optimize scheduling

**Impact**: biomeOS can schedule workflows on optimal towers

---

### **LoamSpine (History Primal)**

**Current Status**: ✅ Already compatible!

**Recommended Enhancements**:
1. ✅ **Structured logging** (5 min)
   - Log `operation`, `entry_count`, `latency_ms`
   - biomeOS can learn append patterns

2. 🟡 **Batching hints** (30 min)
   - `append`: can be batched (multiple entries at once)
   - `get`: can be cached (read-heavy)

3. 🔵 **Storage metrics** (1 hour)
   - Report entries per second
   - Report disk I/O patterns
   - biomeOS can optimize batching

**Impact**: biomeOS can batch multiple appends for 10x speedup

---

### **NestGate (Storage Primal)**

**Current Status**: ✅ Already compatible!

**Recommended Enhancements**:
1. ✅ **Structured logging** (5 min)
   - Log `operation`, `size_bytes`, `latency_ms`
   - biomeOS can learn storage patterns

2. 🟡 **Caching hints** (30 min)
   - `store`: write-once (no need to cache)
   - `get`: read-many (good candidate for caching)

3. 🔵 **Storage metrics** (1 hour)
   - Report cache hit rate
   - Report storage throughput
   - biomeOS can optimize caching

**Impact**: biomeOS can cache frequently-accessed blobs

---

### **SweetGrass (Attribution Primal)**

**Current Status**: ✅ Already compatible!

**Recommended Enhancements**:
1. ✅ **Structured logging** (5 min)
   - Log `operation`, `entity_type`, `latency_ms`
   - biomeOS can learn attribution patterns

2. 🟡 **Dependency hints** (30 min)
   - `record_contribution`: requires `commit` (not needed for signing)
   - Can run in parallel with signing!

**Impact**: biomeOS auto-parallelizes attribution with other operations (30% speedup)

---

## 🔌 Metrics API (For Active Reporting)

### **Standard Metrics Format**

```rust
// Primals can report metrics to biomeOS via Unix socket
// Socket path: env("BIOMEOS_METRICS_SOCKET")

#[derive(Serialize, Deserialize)]
pub struct PrimalMetrics {
    pub primal_id: String,
    pub operation: String,
    pub latency_ms: f64,
    pub cpu_usage: f64,        // 0.0-1.0
    pub memory_usage: u64,     // bytes
    pub success: bool,
    pub timestamp: u64,        // Unix timestamp
    pub extra: HashMap<String, Value>, // Custom fields
}

// Send via Unix socket (JSON)
let socket_path = env::var("BIOMEOS_METRICS_SOCKET")?;
let stream = UnixStream::connect(socket_path).await?;
serde_json::to_writer(&stream, &metrics)?;
```

### **Example: BearDog with Active Reporting**

```rust
impl BearDog {
    async fn sign(&self, data: &[u8]) -> Result<Signature> {
        let start = Instant::now();
        
        // Do the work
        let signature = self.do_sign(data)?;
        
        let latency = start.elapsed();
        
        // Report metrics (optional!)
        if let Ok(socket_path) = env::var("BIOMEOS_METRICS_SOCKET") {
            let metrics = PrimalMetrics {
                primal_id: "beardog".to_string(),
                operation: "sign".to_string(),
                latency_ms: latency.as_secs_f64() * 1000.0,
                cpu_usage: 0.15, // Example
                memory_usage: 1024,
                success: true,
                timestamp: now(),
                extra: hashmap! {
                    "key_type" => "Ed25519",
                    "data_size" => data.len(),
                },
            };
            
            // Send (fire-and-forget, don't block)
            tokio::spawn(async move {
                if let Ok(stream) = UnixStream::connect(socket_path).await {
                    serde_json::to_writer(&stream, &metrics).ok();
                }
            });
        }
        
        Ok(signature)
    }
}
```

---

## 🎯 Summary

### **What Primals MUST Do**
- ✅ **Nothing new!** Already compatible!

### **What Primals SHOULD Do (5 min)**
- 🟡 **Add structured logging** for key metrics
  - `operation`, `latency_ms`, `success`
  - biomeOS scrapes logs for learning

### **What Primals CAN Do (Optional)**
- 🔵 **Declare operation dependencies** (30 min)
- 🔵 **Provide cost estimates** (1 hour)
- 🔵 **Direct metrics reporting** (1-2 hours)

### **Impact Matrix**

| Enhancement | Effort | Impact | Priority |
|-------------|--------|--------|----------|
| **Structured logging** | 5 min | High | ⭐⭐⭐ Do now! |
| **Dependency hints** | 30 min | Medium | ⭐⭐ Recommended |
| **Cost estimates** | 1 hour | Medium | ⭐⭐ Recommended |
| **Direct reporting** | 1-2 hours | Low | ⭐ Nice to have |

---

## 🚀 Next Steps

1. **Review this document** with all primal teams
2. **Start with structured logging** (5 min per primal)
3. **Add dependency hints** for key operations (30 min per primal)
4. **Test with Neural API** once biomeOS implements graph execution

---

🦴 **Primals: Stay simple, enable intelligence!**

*"The best primals do one thing well and let biomeOS discover the rest."*

