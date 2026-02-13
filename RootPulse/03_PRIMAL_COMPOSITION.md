# 🔗 Primal Composition — How Primals Work Together

**The Dance of Coordination**

**Date**: December 27, 2025

---

## 🎯 Core Concept

> **"Primals don't know about RootPulse. They don't need to. BiomeOS coordinates them, and version control emerges."**

This is the essence of primal composition.

---

## 🎭 The Actors

### Meet the Primals

Think of them as musicians in an orchestra. Each plays their instrument. None knows the full symphony. Yet together, they create music.

```
🔐 rhizoCrypt = Piano      (ephemeral melody / working memory)
🦴 LoamSpine  = Drums      (keeps the beat / permanent history)
🏰 NestGate   = Bass       (provides foundation / storage)
🐻 BearDog    = Lead       (takes center / security)
🌱 SweetGrass = Strings    (adds richness / attribution)
🎵 Songbird   = Conductor  (coordinates / discovery)
```

**BiomeOS** is the composer — it wrote the symphony (coordination pattern).

---

## 🔄 Composition Principles

### 1. **Interface Segregation**

Each primal exposes **narrow, focused interfaces**:

```rust
// LoamSpine doesn't know about:
// - What you're storing (could be commits, transactions, events)
// - Who signed it (just verifies signature exists)
// - Where it goes (just appends)

pub trait AppendOnly {
    async fn append(&self, entry: Entry, proof: Signature) -> Result<Hash>;
    async fn get(&self, hash: Hash) -> Result<Entry>;
    async fn prove(&self, hash: Hash) -> Result<InclusionProof>;
}

// That's it. Simple. Focused.
```

**Benefit**: LoamSpine can be used for:
- Version control (RootPulse)
- Audit logs
- Blockchain
- Event sourcing
- Anything requiring immutable history!

---

### 2. **Dependency Inversion**

Primals don't depend on each other. They depend on **abstract capabilities**:

```rust
// ❌ Wrong: Direct dependency
impl LoamSpine {
    fn new(storage: NestGate) -> Self {
        // Tightly coupled to NestGate!
    }
}

// ✅ Right: Abstract dependency
impl LoamSpine {
    fn new(storage: impl BlobStorage) -> Self {
        // Works with ANY storage implementation!
    }
}

// Could be:
// - NestGate
// - S3
// - Local filesystem
// - In-memory (for tests)
```

**Benefit**: Swap implementations without changing primals.

---

### 3. **Message Passing, Not Shared State**

Primals communicate via **messages**, not shared memory:

```rust
// ❌ Wrong: Shared state
static COMMITS: Mutex<Vec<Commit>> = Mutex::new(Vec::new());

// ✅ Right: Message passing
async fn commit(biome: &BiomeOS, commit: Commit) {
    // Send message to LoamSpine
    biome.loamspine().send(Message::Append(commit)).await?;
    
    // Send message to SweetGrass
    biome.sweetgrass().send(Message::RecordAttribution(commit)).await?;
}
```

**Benefit**: No locks, no race conditions, inherently concurrent.

---

### 4. **Single Responsibility**

Each primal does **ONE thing**:

```rust
// LoamSpine: Immutable history
// - Doesn't store blobs (that's NestGate)
// - Doesn't sign (that's BearDog)
// - Doesn't discover (that's Songbird)
// ONLY: Append-only history with proofs

// NestGate: Content storage
// - Doesn't track history (that's LoamSpine)
// - Doesn't sign (that's BearDog)
// ONLY: Store and retrieve content-addressed objects

// BearDog: Security
// - Doesn't store (that's NestGate)
// - Doesn't track history (that's LoamSpine)
// ONLY: Sign, verify, encrypt, secure transport
```

**Benefit**: Easy to understand, test, and maintain.

---

## 🎼 Composition in Action

### Example: The `commit` Operation

Let's watch primals compose to create a commit:

```rust
async fn commit(message: String) -> Result<CommitHash> {
    // ┌─────────────────────────────────────────┐
    // │  Step 1: Hash working directory         │
    // │  (Local operation, no primals)          │
    // └─────────────────────────────────────────┘
    let tree = hash_directory(".")?;
    
    // ┌─────────────────────────────────────────┐
    // │  Step 2: Store tree in NestGate         │
    // │  🏰 NestGate active                     │
    // └─────────────────────────────────────────┘
    let tree_hash = nestgate.store_tree(tree).await?;
    //   │
    //   │  NestGate: "I stored it at hash abc123"
    //   │  NestGate: "I don't know what this is for"
    //   │  NestGate: "Could be git, could be anything"
    //   └──> tree_hash = abc123
    
    // ┌─────────────────────────────────────────┐
    // │  Step 3: Create commit object           │
    // │  (Local operation, no primals)          │
    // └─────────────────────────────────────────┘
    let commit = Commit {
        tree: tree_hash,
        message,
        author: get_author(),
        timestamp: now(),
        ...
    };
    
    // ┌─────────────────────────────────────────┐
    // │  Step 4: Sign commit with BearDog      │
    // │  🐻 BearDog active                      │
    // └─────────────────────────────────────────┘
    let signature = beardog.sign(&commit.to_bytes()).await?;
    //   │
    //   │  BearDog: "I signed these bytes"
    //   │  BearDog: "I don't know it's a commit"
    //   │  BearDog: "Could be git, email, anything"
    //   └──> signature = sig_xyz
    
    // ┌─────────────────────────────────────────┐
    // │  Step 5: Record in SweetGrass           │
    // │  🌱 SweetGrass active                   │
    // └─────────────────────────────────────────┘
    let contributions = analyze_changes(&commit);
    sweetgrass.record_contributions(contributions).await?;
    //   │
    //   │  SweetGrass: "I recorded semantic changes"
    //   │  SweetGrass: "I created attribution braids"
    //   │  SweetGrass: "But I don't own the history"
    //   └──> (attribution stored)
    
    // ┌─────────────────────────────────────────┐
    // │  Step 6: Append to LoamSpine            │
    // │  🦴 LoamSpine active                    │
    // └─────────────────────────────────────────┘
    let commit_hash = loamspine.append(commit, signature).await?;
    //   │
    //   │  LoamSpine: "I appended entry #12,543"
    //   │  LoamSpine: "I verified signature exists"
    //   │  LoamSpine: "But I don't know what it means"
    //   └──> commit_hash = hash_456
    
    // ┌─────────────────────────────────────────┐
    // │  Result: Commit complete!               │
    // │  🎉 Version control emerged!            │
    // └─────────────────────────────────────────┘
    Ok(commit_hash)
}
```

**Key Observations**:
1. No primal knows about "version control"
2. Each primal does its job
3. BiomeOS orchestrates the sequence
4. Version control behavior **emerges**

---

## 🔄 Composition Patterns

### Pattern 1: Sequential Composition

**One primal after another**:

```rust
// Commit workflow
async fn commit_sequential() {
    let a = primal_a.step_1().await?;  // NestGate stores
    let b = primal_b.step_2(a).await?; // BearDog signs
    let c = primal_c.step_3(b).await?; // LoamSpine appends
}
```

**Use when**: Steps depend on previous results.

---

### Pattern 2: Parallel Composition

**Multiple primals simultaneously**:

```rust
// Discover multiple remotes
async fn discover_parallel() {
    let (local, dns, dht) = tokio::join!(
        primal_a.discover_local().await,   // Songbird mDNS
        primal_a.discover_dns().await,     // Songbird DNS-SRV
        primal_a.discover_dht().await,     // Songbird DHT
    );
    
    // Merge results
    combine(local, dns, dht)
}
```

**Use when**: Steps are independent.

---

### Pattern 3: Conditional Composition

**Different primals based on state**:

```rust
// Push with optional CI/CD
async fn push_conditional(run_ci: bool) {
    // Always do these
    let commits = loamspine.get_new_commits().await?;
    beardog.establish_channel(remote).await?;
    
    // Optionally run CI
    if run_ci {
        toadstool.run_tests(commits).await?;  // Only if enabled
    }
    
    // Complete push
    nestgate.transfer_objects(commits).await?;
}
```

**Use when**: Optional features.

---

### Pattern 4: Feedback Composition

**Primals inform each other via coordinator**:

```rust
// Pull with merge detection
async fn pull_with_merge() {
    let remote_commits = fetch_commits().await?;
    let local_commits = loamspine.get_head().await?;
    
    // Check for conflicts (local decision)
    if has_conflicts(&remote_commits, &local_commits) {
        // Ask Squirrel for help
        let resolution = squirrel.suggest_merge(
            &remote_commits,
            &local_commits
        ).await?;
        
        apply_merge(resolution).await?;
    }
    
    // Append merged result
    loamspine.append(merged_commit).await?;
}
```

**Use when**: Decisions need context from multiple primals.

---

## 🎨 Composition Benefits

### Benefit 1: Reusability

**Same primals, different applications**:

```rust
// RootPulse (version control)
LoamSpine + NestGate + BearDog + SweetGrass + Songbird

// Audit log system
LoamSpine + BearDog

// Distributed database
NestGate + LoamSpine + BearDog

// Social network
SweetGrass + NestGate + BearDog + Songbird

// AI platform
Squirrel + ToadStool + NestGate + LoamSpine
```

**Each primal used in multiple contexts!**

---

### Benefit 2: Testability

**Test primals independently**:

```rust
#[cfg(test)]
mod tests {
    // Test LoamSpine alone
    #[tokio::test]
    async fn test_loamspine_append() {
        let spine = LoamSpine::new(mock_storage());
        let result = spine.append(test_entry()).await;
        assert!(result.is_ok());
    }
    
    // Test NestGate alone
    #[tokio::test]
    async fn test_nestgate_store() {
        let storage = NestGate::new(test_config());
        let result = storage.store_blob(test_data()).await;
        assert!(result.is_ok());
    }
    
    // Test composition
    #[tokio::test]
    async fn test_commit_workflow() {
        let biome = BiomeOS::new_test();
        let result = commit(&biome, "test").await;
        assert!(result.is_ok());
        
        // Verify each primal was called correctly
        assert_eq!(biome.nestgate_call_count(), 1);
        assert_eq!(biome.beardog_call_count(), 1);
        assert_eq!(biome.loamspine_call_count(), 1);
    }
}
```

**Test units and composition separately!**

---

### Benefit 3: Evolvability

**Improve primals independently**:

```
Week 1: Improve LoamSpine performance (10x faster)
        → RootPulse gets faster automatically!
        
Week 2: Add quantum-resistant crypto to BearDog
        → RootPulse becomes quantum-resistant!
        
Week 3: Add semantic search to SweetGrass
        → RootPulse gains semantic search!
```

**No RootPulse code changes needed!**

---

### Benefit 4: Substitutability

**Swap implementations**:

```rust
// Production: Use real primals
let biome = BiomeOS::new()
    .with_loamspine(LoamSpine::production())
    .with_nestgate(NestGate::production())
    .with_beardog(BearDog::production());

// Testing: Use mocks
let biome = BiomeOS::new()
    .with_loamspine(MockLoamSpine::new())
    .with_nestgate(MockNestGate::new())
    .with_beardog(MockBearDog::new());

// Edge deployment: Use lightweight versions
let biome = BiomeOS::new()
    .with_loamspine(LoamSpine::embedded())
    .with_nestgate(NestGate::sqlite())  // Instead of ZFS
    .with_beardog(BearDog::software());  // Instead of HSM
```

**Same coordination, different implementations!**

---

## 🎭 Anti-Patterns (What NOT to Do)

### Anti-Pattern 1: Primal-to-Primal Coupling

```rust
// ❌ WRONG: LoamSpine directly calls NestGate
impl LoamSpine {
    async fn append(&self, entry: Entry) -> Result<Hash> {
        // DON'T DO THIS!
        self.nestgate.store(entry.clone()).await?;
        // ...
    }
}
```

**Why bad**: Creates tight coupling. Can't swap implementations.

**Fix**: BiomeOS coordinates, primals don't call each other.

---

### Anti-Pattern 2: Primals Knowing Application Logic

```rust
// ❌ WRONG: LoamSpine knows about "commits"
impl LoamSpine {
    async fn append_commit(&self, commit: Commit) -> Result<Hash> {
        // DON'T DO THIS!
        // LoamSpine shouldn't know about commits
    }
}
```

**Why bad**: Reduces reusability. LoamSpine is now git-specific.

**Fix**: LoamSpine stores generic entries. Application defines meaning.

---

### Anti-Pattern 3: Shared Mutable State

```rust
// ❌ WRONG: Primals share state
static GLOBAL_STATE: Mutex<State> = Mutex::new(State::new());

impl LoamSpine {
    async fn append(&self) {
        let mut state = GLOBAL_STATE.lock().unwrap();
        // Shared state! Race conditions! Deadlocks!
    }
}
```

**Why bad**: Concurrency issues. Hard to reason about.

**Fix**: Message passing. Each primal owns its state.

---

## 🚀 Advanced Composition

### Recursive Composition

**Primals themselves are compositions**:

```rust
// LoamSpine is built from:
LoamSpine = MerkleTree + BlobStorage + SignatureVerification

// Which are built from:
MerkleTree = Hash + BinaryTree
BlobStorage = FileSystem + ContentAddressing
SignatureVerification = PublicKey + CryptoAlgorithm

// Turtles all the way down!
```

**Composition at every level!**

---

### Dynamic Composition

**Determine primals at runtime**:

```rust
async fn commit_dynamic(config: Config) {
    let biome = BiomeOS::builder()
        .with_loamspine(LoamSpine::new())
        .with_nestgate(NestGate::new());
    
    // Add optional primals based on config
    if config.attribution_enabled {
        biome = biome.with_sweetgrass(SweetGrass::new());
    }
    
    if config.ai_enabled {
        biome = biome.with_squirrel(Squirrel::new());
    }
    
    // Coordinate whatever primals we have
    biome.commit(message).await?;
}
```

**Customize composition per deployment!**

---

## 💡 Key Takeaways

1. **Primals are dumb, coordination is smart**
   - Primals: "I append entries"
   - BiomeOS: "Let's make version control!"

2. **Interface segregation enables reuse**
   - Narrow interfaces = broad applicability

3. **Message passing prevents coupling**
   - No shared state = no shared problems

4. **Single responsibility ensures clarity**
   - Do ONE thing well = infinite combinations

5. **Composition scales infinitely**
   - 7 primals = 100+ applications

---

## 🔗 Next Reading

1. [04_BIOME_DEPLOYMENT.md](./04_BIOME_DEPLOYMENT.md) — How BiomeOS coordinates
2. [05_COORDINATION_PATTERNS.md](./05_COORDINATION_PATTERNS.md) — Pattern definitions
3. [11_API_REFERENCE.md](./11_API_REFERENCE.md) — Technical API details

---

🌳 **RootPulse: Harmony through composition**

*"The sum is greater than the parts — when the parts play in harmony."*

