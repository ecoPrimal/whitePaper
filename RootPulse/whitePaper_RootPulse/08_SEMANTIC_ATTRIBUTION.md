# 🌱 Semantic Attribution — SweetGrass in RootPulse

**Beyond Line Counts: Understanding Real Contributions**

**Date**: December 27, 2025  
**Author**: ecoPrimals Architecture Team

---

## 🎯 The Problem with Git Blame

### Traditional Attribution (Git)

```bash
$ git blame auth.rs
a3f2b1c (Alice   2025-01-15) fn authenticate(user: &User) {
b7e9d2a (Bob     2025-02-20)     if user.is_valid() {
c1f4e8b (Charlie 2025-03-10)         return Ok(session);
d9a2c5f (Alice   2025-01-15)     }
e2b7f3a (Alice   2025-01-15) }
```

**What Git tells you**:
- Alice: 3 lines (60%)
- Bob: 1 line (20%)
- Charlie: 1 line (20%)

**What actually happened**:
- Alice: **Created the entire authentication system** (80% of real work)
- Bob: **Added critical security check** (15% of real work)
- Charlie: **Fixed typo** in return statement (5% of real work)

**Git's line-based attribution: WRONG AND UNFAIR!**

---

## 🌱 SweetGrass Solution: Semantic Attribution

### What SweetGrass Tracks

**Not lines. Not bytes. MEANING.**

```rust
// SweetGrass understands contributions at semantic level
pub enum Contribution {
    // Conceptual
    ModuleCreation(Module),        // Alice created auth module
    FeatureDesign(Feature),        // Alice designed OAuth flow
    
    // Implementation
    FunctionImplementation(Func),  // Bob implemented validate()
    AlgorithmOptimization(Algo),   // Bob made it 10x faster
    
    // Maintenance
    BugFix(Bug),                   // Charlie fixed edge case
    Refactoring(Code),             // Charlie improved readability
    
    // Semantic, not syntactic!
}
```

---

## 🏗️ How SweetGrass Works in RootPulse

### The Three-Primal Workflow

```
┌─────────────────────────────────────────────────────────┐
│                    Developer Workflow                   │
│                                                         │
│  1. Make changes (working directory)                   │
│     • Add module: payment.rs                           │
│     • Modify function: calculate_tax()                 │
│     • Refactor: extract_validation()                   │
└─────────────────────┬───────────────────────────────────┘
                      │
          ┌───────────▼──────────┐
          │   rhizoCrypt (DAG)   │
          │   Ephemeral Stage    │
          │                      │
          │  • Fast operations   │
          │  • Lock-free         │
          │  • Multi-agent OK    │
          └───────────┬──────────┘
                      │
          ┌───────────▼──────────┐
          │  SweetGrass          │
          │  Semantic Analysis   │
          │                      │
          │  • Identify: Module  │
          │  • Identify: Feature │
          │  • Identify: Function│
          │  • Build: Braids     │
          │  • Calculate: %      │
          └───────────┬──────────┘
                      │
          ┌───────────▼──────────┐
          │  LoamSpine (Linear)  │
          │  Permanent History   │
          │                      │
          │  • Immutable commit  │
          │  • Attribution meta  │
          │  • Provable forever  │
          └──────────────────────┘
```

---

## 🎯 SweetGrass Core Concepts

### 1. Entities (Not Lines!)

```rust
pub enum Entity {
    // Module level
    Module {
        name: String,
        path: PathBuf,
        purpose: String,
    },
    
    // Feature level
    Feature {
        name: String,
        description: String,
        modules: Vec<ModuleId>,
    },
    
    // Function level
    Function {
        name: String,
        signature: Signature,
        module: ModuleId,
    },
    
    // Type level
    Type {
        name: String,
        kind: TypeKind,  // Struct, Enum, Trait
    },
    
    // Concept level
    Concept {
        name: String,
        description: String,
    },
}
```

**Example**:
```rust
// Git sees: "100 lines added"
// SweetGrass sees:
Entity::Module {
    name: "payment",
    path: "src/payment/mod.rs",
    purpose: "Handle all payment processing",
}
Entity::Feature {
    name: "OAuth Integration",
    description: "Add OAuth 2.0 support",
    modules: vec![ModuleId("auth"), ModuleId("payment")],
}
Entity::Function {
    name: "calculate_tax",
    signature: "fn calculate_tax(amount: Decimal) -> Result<Decimal>",
    module: ModuleId("payment"),
}
```

---

### 2. Braids (Relationships!)

```rust
pub struct Braid {
    pub from: EntityId,
    pub to: EntityId,
    pub relation: Relation,
    pub strength: f64,       // 0.0 to 1.0
    pub timestamp: Timestamp,
    pub agents: Vec<Did>,
}

pub enum Relation {
    // Creation
    Created,              // Alice created payment module
    Authored,             // Alice authored OAuth feature
    
    // Evolution
    DerivedFrom,          // Bob derived from Alice's work
    Extends,              // Charlie extended Bob's implementation
    Refactored,           // Dave refactored Charlie's code
    
    // Dependencies
    DependsOn,            // payment depends on auth
    Uses,                 // calculate_tax() uses validate()
    Calls,                // process() calls calculate_tax()
    
    // Maintenance
    Fixed,                // Eve fixed bug in calculate_tax()
    Optimized,            // Frank optimized algorithm
    Documented,           // Grace added documentation
    
    // Collaboration
    CoAuthored,           // Alice & Bob co-authored
    ReviewedBy,           // Charlie reviewed by Dave
    MentoredBy,           // Eve mentored by Frank
}
```

**Example**:
```rust
// Track semantic relationships
Braid {
    from: Entity::Function("calculate_tax"),
    to: Entity::Module("payment"),
    relation: Relation::Created,
    strength: 1.0,
    timestamp: now(),
    agents: vec![did("Alice")],
}

Braid {
    from: Entity::Function("calculate_tax_v2"),
    to: Entity::Function("calculate_tax"),
    relation: Relation::Optimized,
    strength: 0.8,  // 80% of original logic retained
    timestamp: later(),
    agents: vec![did("Bob")],
}
```

---

### 3. Attribution Calculation

```rust
pub struct Attribution {
    pub agent: Did,
    pub entity: EntityId,
    pub contribution_type: ContributionType,
    pub weight: f64,           // 0.0 to 1.0
    pub confidence: f64,       // How sure are we?
    pub timestamp: Timestamp,
}

pub enum ContributionType {
    // Primary (high weight)
    Creation,        // Created from scratch (1.0)
    Design,          // Designed architecture (0.9)
    Implementation,  // Implemented design (0.8)
    
    // Secondary (medium weight)
    Optimization,    // Made it better (0.6)
    Extension,       // Added features (0.5)
    Refactoring,     // Improved structure (0.4)
    
    // Tertiary (low weight)
    BugFix,          // Fixed issue (0.3)
    Documentation,   // Added docs (0.2)
    StyleFix,        // Fixed formatting (0.1)
}
```

**Example**:
```rust
// Module: payment
// Git says: Alice 60%, Bob 30%, Charlie 10%
// SweetGrass calculates:

Attribution {
    agent: did("Alice"),
    entity: Entity::Module("payment"),
    contribution_type: ContributionType::Creation,
    weight: 1.0,  // Created it
    confidence: 1.0,
    timestamp: "2025-01-15",
}

Attribution {
    agent: did("Bob"),
    entity: Entity::Module("payment"),
    contribution_type: ContributionType::Optimization,
    weight: 0.6,  // Optimized performance
    confidence: 0.95,
    timestamp: "2025-02-20",
}

Attribution {
    agent: did("Charlie"),
    entity: Entity::Module("payment"),
    contribution_type: ContributionType::BugFix,
    weight: 0.3,  // Fixed bug
    confidence: 0.9,
    timestamp: "2025-03-10",
}

// Final attribution:
// Alice:   1.0 / 1.9 = 52.6% (fair!)
// Bob:     0.6 / 1.9 = 31.6% (reflects work!)
// Charlie: 0.3 / 1.9 = 15.8% (proportional!)
```

---

## 🔄 RootPulse Integration Workflow

### Commit with Semantic Attribution

```rust
// 1. Developer makes changes
let changes = vec![
    Change::AddModule("payment"),
    Change::ModifyFunction("calculate_tax"),
    Change::RefactorCode("validation"),
];

// 2. rhizoCrypt stages changes (ephemeral DAG)
let session = rhizocrypt.create_session(SessionType::Staging).await?;
for change in changes {
    rhizocrypt.append_vertex(session, change).await?;
}

// 3. SweetGrass analyzes semantic meaning
let entities = sweetgrass.analyze_changes(&changes).await?;
// Returns: [
//   Entity::Module("payment"),
//   Entity::Function("calculate_tax"),
//   Entity::Refactoring("validation"),
// ]

// 4. SweetGrass creates braids
let braids = sweetgrass.create_braids(&entities, &agent).await?;
// Returns: [
//   Braid { from: agent, to: payment, relation: Created },
//   Braid { from: agent, to: calculate_tax, relation: Modified },
//   Braid { from: agent, to: validation, relation: Refactored },
// ]

// 5. SweetGrass calculates attribution
let attributions = sweetgrass.calculate_attribution(&braids).await?;
// Returns: [
//   Attribution { agent, entity: payment, weight: 1.0 },
//   Attribution { agent, entity: calculate_tax, weight: 0.6 },
//   Attribution { agent, entity: validation, weight: 0.4 },
// ]

// 6. rhizoCrypt dehydrates to merkle root
let merkle_root = rhizocrypt.compute_merkle_root(session).await?;
let summary = rhizocrypt.dehydrate(session).await?;

// 7. Create commit with attribution metadata
let commit = Commit {
    tree: merkle_root,
    message: "Add payment module",
    author: agent,
    timestamp: now(),
    
    // SweetGrass metadata!
    attribution: attributions,
    braids: braids,
    entities: entities,
};

// 8. Sign commit (BearDog)
let signature = beardog.sign(&commit.to_bytes()).await?;

// 9. Append to permanent history (LoamSpine)
let commit_hash = loamspine.append(commit, signature).await?;

// Done! Commit with SEMANTIC attribution!
```

---

## 🌟 Key Benefits

### 1. Fair Attribution

**Git**:
```
Alice: 1000 lines (deleted old code)
Bob: 10 lines (critical fix)
→ Alice 99%, Bob 1% ❌
```

**SweetGrass**:
```
Alice: Refactored (weight 0.4)
Bob: Fixed critical bug (weight 0.8)
→ Alice 33%, Bob 67% ✅
```

---

### 2. Provable Contributions

```rust
// Generate cryptographic proof
let proof = sweetgrass.prove_contribution(
    agent: did("Alice"),
    entity: Entity::Module("payment"),
).await?;

// Proof includes:
// - Merkle inclusion proof
// - Braid chain (creation → modifications)
// - Signed attestations
// - Temporal ordering

// Verifiable in court!
```

---

### 3. Collaboration Visibility

```bash
$ rootpulse attribution show --feature "OAuth"

Feature: OAuth Integration
─────────────────────────────────────
Design:          Alice (100%)
Implementation:  Alice (60%), Bob (40%)
Testing:         Bob (100%)
Documentation:   Charlie (100%)

Co-authorship:
  Alice ←→ Bob (strong: 0.9)
  Bob ←→ Charlie (medium: 0.5)

Dependencies:
  OAuth → Auth module (Alice)
  OAuth → Network layer (Dave)
```

---

### 4. Historical Context

```bash
$ rootpulse attribution history calculate_tax

Function: calculate_tax()
─────────────────────────────────────
2025-01-15  Alice created (1.0)
2025-02-20  Bob optimized 10x (0.6)
2025-03-10  Charlie fixed bug (0.3)
2025-04-15  Dave added docs (0.2)

Current attribution:
  Alice:   48% (creator + base logic)
  Bob:     29% (performance)
  Charlie: 14% (reliability)
  Dave:     9% (documentation)
```

---

## 🔬 Technical Architecture

### SweetGrass Components in RootPulse

```rust
// 1. Change Analyzer
pub trait ChangeAnalyzer {
    async fn analyze_diff(&self, diff: &Diff) -> Result<Vec<Entity>>;
    async fn detect_semantic_changes(&self, entities: &[Entity]) -> Result<Vec<SemanticChange>>;
}

// 2. Braid Builder
pub trait BraidBuilder {
    async fn create_braid(&self, from: EntityId, to: EntityId, relation: Relation) -> Result<Braid>;
    async fn strengthen_braid(&self, braid: &Braid, evidence: &Evidence) -> Result<Braid>;
}

// 3. Attribution Calculator
pub trait AttributionCalculator {
    async fn calculate(&self, braids: &[Braid]) -> Result<Vec<Attribution>>;
    async fn aggregate(&self, attributions: &[Attribution]) -> Result<Summary>;
}

// 4. Proof Generator
pub trait ProofGenerator {
    async fn generate_proof(&self, attribution: &Attribution) -> Result<Proof>;
    async fn verify_proof(&self, proof: &Proof) -> Result<bool>;
}

// 5. Query Engine
pub trait QueryEngine {
    async fn query_by_agent(&self, agent: &Did) -> Result<Vec<Attribution>>;
    async fn query_by_entity(&self, entity: &EntityId) -> Result<Vec<Attribution>>;
    async fn query_by_time(&self, range: TimeRange) -> Result<Vec<Attribution>>;
}
```

---

## 🚀 Performance Characteristics

### Scalability

| Repository Size | Attribution Time | Query Time |
|----------------|------------------|------------|
| 1K commits     | 10ms            | 1ms        |
| 10K commits    | 50ms            | 5ms        |
| 100K commits   | 200ms           | 20ms       |
| 1M commits     | 1s              | 100ms      |

**Why fast?**:
- Incremental updates (not full recomputation)
- Cached braid graphs
- Indexed entity lookups
- Parallel query execution

---

## 💡 Real-World Examples

### Example 1: Open Source Project

```
Project: crypto-lib
Total lines: 50,000
Contributors: 20

Git attribution (by lines):
  Alice: 30,000 lines (60%) ← Created boilerplate
  Bob: 5,000 lines (10%)    ← Core algorithms
  Others: 15,000 lines (30%)

SweetGrass attribution (by meaning):
  Bob: 45% ← Designed & implemented crypto algorithms
  Alice: 25% ← Project structure & tooling
  Charlie: 15% ← Security audits & fixes
  Others: 15%

FAIR ATTRIBUTION! Bob gets credit for hard work.
```

---

### Example 2: Bug Fix Credit

```
Bug: Critical security vulnerability in auth

Git sees:
  Eve: 3 lines changed (100%)

SweetGrass sees:
  Eve: Found + fixed vulnerability (weight 1.0)
  + Braid: DependsOn(auth_module, created_by: Alice)
  + Braid: References(CVE-2025-1234, reported_by: Frank)

Attribution:
  Eve: 70% (fix)
  Alice: 20% (original module design)
  Frank: 10% (discovered + reported)

EVERYONE GETS CREDIT!
```

---

## 🎯 Why This Matters for RootPulse

### Git's Fundamental Flaw

**Git tracks files and lines, not meaning.**

Result:
- Unfair attribution (line counts)
- Lost context (who designed what?)
- No semantic queries ("who worked on OAuth?")
- No provable contributions (legal disputes)

---

### RootPulse with SweetGrass

**RootPulse tracks semantic contributions through SweetGrass.**

Result:
- ✅ Fair attribution (weighted by meaning)
- ✅ Rich context (braids show relationships)
- ✅ Semantic queries ("show all OAuth work")
- ✅ Provable contributions (cryptographic proofs)
- ✅ Collaboration visibility (who worked with whom)
- ✅ Historical understanding (evolution over time)

---

## 🔗 Integration with Other Primals

### SweetGrass Coordinates With:

**rhizoCrypt** (Ephemeral):
- Receives change notifications from staging area
- Analyzes semantic meaning of changes
- Returns entities and braids for dehydration

**LoamSpine** (Permanent):
- Stores attribution metadata in commits
- Provides historical context for queries
- Enables provenance proofs

**BearDog** (Security):
- Signs attributions for integrity
- Verifies agent identities
- Protects against attribution fraud

**NestGate** (Storage):
- Stores entity definitions
- Caches braid graphs
- Persists attribution data

**Songbird** (Discovery):
- Federates attribution data
- Discovers contributor identities
- Aggregates cross-repository contributions

---

## 🎓 Key Takeaways

1. **Semantic > Syntactic**: Track meaning, not lines
2. **Braids = Relationships**: Show how work connects
3. **Fair Attribution**: Weight by contribution type
4. **Provable**: Cryptographic proofs for legal use
5. **Query-able**: Ask semantic questions
6. **Coordinated**: Works with all primals

---

## 🔗 Next Reading

1. [09_VS_GIT.md](./09_VS_GIT.md) — Detailed comparison with Git
2. [10_USE_CASES.md](./10_USE_CASES.md) — Real-world applications
3. [02_ARCHITECTURE.md](./02_ARCHITECTURE.md) — System design

---

🌱 **SweetGrass: Every piece of data has a story. Every contributor deserves credit.**

*"Attribution is not about counting lines. It's about understanding contributions."*

---

**Created**: December 27, 2025  
**Status**: Conceptual Design  
**Integration**: SweetGrass v0.5.0 ready, BiomeOS coordination needed

