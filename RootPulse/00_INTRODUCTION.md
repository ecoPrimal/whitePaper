# 🌳 RootPulse — Introduction

**Distributed Version Control Through Primal Emergence**

**Version**: 1.0.0-concept  
**Date**: December 27, 2025  
**Status**: Conceptual Design

---

## 🎯 What is RootPulse?

**RootPulse** is a distributed version control system that **emerges from the coordination of ecoPrimals** rather than being built as a monolithic service.

### The One-Sentence Summary
> **"RootPulse is Git reimagined as a coordination pattern between sovereign, composable primitives rather than a monolithic tool."**

---

## 🌟 Key Insight

### Traditional Approach (Git)
```
┌─────────────────────────────────────┐
│         Monolithic Git              │
│  ┌──────────────────────────────┐  │
│  │ Storage + Crypto + Network   │  │
│  │ + Attribution + Everything   │  │
│  └──────────────────────────────┘  │
└─────────────────────────────────────┘
```
**Everything in one tool. Tightly coupled. Hard to evolve.**

### RootPulse Approach (Emergence)
```
┌──────────┐  ┌──────────┐  ┌──────────┐
│LoamSpine │  │ NestGate │  │ BearDog  │
│(History) │  │(Storage) │  │(Security)│
└────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │
     └─────────┬───┴─────────────┘
               │
         ┌─────▼──────┐
         │  BiomeOS   │  ← Coordinates
         │(Conductor) │
         └────────────┘
               ▲
           RootPulse emerges here!
```
**Each primal does ONE thing. Coordination creates version control.**

---

## 🎭 What RootPulse IS

### A Coordination Pattern
RootPulse is a **recipe** for how primals work together:
- Not a new service to run
- Not a monolithic application
- Not another primal to build

It's a **pattern definition** that BiomeOS executes.

### An Emergent Capability
When you coordinate:
- 🔐 **rhizoCrypt** (ephemeral workspace — fast operations)
- 🦴 **LoamSpine** (immutable history)
- 🏰 **NestGate** (content storage)
- 🐻 **BearDog** (cryptography)
- 🌱 **SweetGrass** (attribution)
- 🎵 **Songbird** (discovery)

**Version control emerges!**

No new code needed. Just coordination.

---

## 🎯 Core Operations

### Commit Example
```bash
# User types:
rootpulse commit -m "Fix bug"

# BiomeOS coordinates:
1. NestGate stores file tree
2. BearDog signs commit
3. SweetGrass records attribution
4. LoamSpine appends to history

# Result: Cryptographically verified commit
```

**No "RootPulse service" running. Just primals doing their jobs.**

### Push Example
```bash
# User types:
rootpulse push origin main

# BiomeOS coordinates:
1. Songbird discovers remote
2. BearDog establishes secure channel
3. NestGate transfers objects
4. LoamSpine transfers commits

# Result: Federated, secure push
```

**Distributed by nature. Secure by design.**

---

## 🌍 Why This Matters

### For Users
- ✅ **Sovereign** — You own your infrastructure
- ✅ **Private** — No GitHub surveillance
- ✅ **Fast** — Pure Rust, zero-copy optimized
- ✅ **Secure** — Substrate cryptography (HSM support)
- ✅ **Verifiable** — Cryptographic proofs for everything

### For Developers
- ✅ **Simple** — Each primal is straightforward
- ✅ **Composable** — Same primals, different patterns
- ✅ **Maintainable** — Primals evolve independently
- ✅ **Testable** — Test coordination, not reimplementation
- ✅ **Extensible** — Add features via new patterns

### For the Ecosystem
- ✅ **Validates primals** — Proves composition works
- ✅ **Shows maturity** — Real-world capability
- ✅ **Demonstrates value** — Tangible, useful output
- ✅ **Attracts users** — Familiar use case (version control)
- ✅ **Enables more** — Same pattern for databases, social, etc.

---

## 🔑 Key Differences from Git

| Aspect | Git | RootPulse |
|--------|-----|-----------|
| **Architecture** | Monolithic | Emergent composition |
| **Security** | GPG (optional, separate) | BearDog (unified, built-in) |
| **Transport** | SSH (separate config) | BearDog (same keys) |
| **Storage** | Local .git/ | Sovereign (NestGate + ZFS) |
| **Attribution** | Line-based blame | Semantic braids |
| **Provenance** | Trust-based | Cryptographic proofs |
| **Federation** | Manual remotes | Auto-discovery |
| **Asset Types** | Code (+ git-lfs hack) | Code, art, data, models |
| **Ownership** | You own repo | You own infrastructure |

---

## 🎨 What You Can Version Control

### Beyond Code
RootPulse handles **any content type**:

```rust
pub enum AssetType {
    // Traditional
    Code(Language),
    
    // Creative
    Art(ArtType),              // Images, 3D models
    Music(AudioFormat),
    Video(VideoFormat),
    
    // Data Science
    Dataset(DataFormat),
    MLModel(ModelType),
    Notebook(NotebookType),
    
    // Documentation
    Docs(DocFormat),
    Whitepaper(PaperFormat),
    
    // Anything else
    Binary(MimeType),
}
```

**One version control system for everything.**

---

## 🚀 Quick Examples

### Initialize Repository
```bash
rootpulse init my-project
# BiomeOS: Creates LoamSpine, configures NestGate, registers with Songbird
```

### Make Commit
```bash
rootpulse add .
rootpulse commit -m "Initial commit"
# BiomeOS: NestGate stores → BearDog signs → SweetGrass attributes → LoamSpine records
```

### Push to Remote
```bash
rootpulse push origin main
# BiomeOS: Songbird discovers → BearDog secures → NestGate + LoamSpine transfer
```

### Semantic Attribution
```bash
rootpulse attribution show
# SweetGrass: Shows WHO contributed WHAT at semantic level
# Not just line counts — actual features/modules
```

### Cryptographic Proof
```bash
rootpulse prove --commit abc123
# LoamSpine: Generates inclusion + provenance proof
# Mathematically verifiable, legally admissible
```

### AI Code Review
```bash
rootpulse review --ai
# Squirrel: Analyzes changes, finds issues, suggests improvements
```

---

## 🏗️ Implementation Status

### Primals (Phase 1 & 2)
✅ **rhizoCrypt** — v0.13.0-dev, production ready (862 tests, 87.78% coverage)  
✅ **LoamSpine** — v0.8.0, production ready (700 tests, 90.6% coverage)  
✅ **NestGate** — production ready (A++ TOP 1%)  
✅ **BearDog** — v0.15.0, production ready (A+ LEGENDARY)  
✅ **SweetGrass** — v0.7.3, production ready (746 tests, 94% coverage)  
✅ **Songbird** — v3.6, production ready (S+)  
✅ **Squirrel** — production ready (A++)  
✅ **ToadStool** — S153, production ready (A++ GOLD, 20,015+ tests)

### BiomeOS Integration
✅ **Coordination patterns** — `rootpulse_commit.toml` (6-phase), `provenance_pipeline.toml`  
✅ **Workflow engine** — Graph executor + ContinuousExecutor validated  
✅ **Provenance trio** — End-to-end validated (March 13, 2026)  
⏳ **CLI frontend** — Needs development

### Timeline
- **Concept**: ✅ Complete (this document)
- **Design**: ✅ Complete (white papers)
- **Ephemeral Workspace**: ✅ **Complete (rhizoCrypt v0.13.0)** 🎯
- **Prototyping**: ⏳ 1-2 months (accelerated with rhizoCrypt)
- **MVP**: ⏳ 3-5 months (accelerated)
- **Production**: ⏳ **6-9 months** (accelerated from 12-15 months)

---

## 🎓 Reading Path

### For Newcomers
1. Read this document (you're here!)
2. [01_PHILOSOPHY.md](./01_PHILOSOPHY.md) — Understand emergence
3. [08_VS_GIT.md](./08_VS_GIT.md) — See the differences
4. [09_USE_CASES.md](./09_USE_CASES.md) — Real-world applications

### For Technical Readers
1. [02_ARCHITECTURE.md](./02_ARCHITECTURE.md) — System design
2. [03_PRIMAL_COMPOSITION.md](./03_PRIMAL_COMPOSITION.md) — How primals coordinate
3. [06_SUBSTRATE_CRYPTOGRAPHY.md](./06_SUBSTRATE_CRYPTOGRAPHY.md) — BearDog security
4. [11_API_REFERENCE.md](./11_API_REFERENCE.md) — Technical details

### For Implementers
1. [04_BIOME_DEPLOYMENT.md](./04_BIOME_DEPLOYMENT.md) — BiomeOS integration
2. [05_COORDINATION_PATTERNS.md](./05_COORDINATION_PATTERNS.md) — Pattern definitions
3. [10_ROADMAP.md](./10_ROADMAP.md) — Implementation plan

---

## 💡 The Big Picture

### The Problem
Git is great, but:
- Monolithic (hard to evolve)
- Centralized in practice (GitHub monopoly)
- Limited security (GPG/SSH separate, optional)
- Poor attribution (line counts, not semantics)
- Code-only (git-lfs is a hack)

### The Solution
RootPulse:
- **Emergent** (composition of primitives)
- **Federated** (Songbird discovery)
- **Secure** (BearDog substrate crypto)
- **Attributed** (SweetGrass semantics)
- **Universal** (NestGate stores anything)
- **Sovereign** (you own it all)

### The Proof
**This validates the entire ecoPrimals vision!**

If primals can coordinate to create version control, they can create:
- Databases
- Social networks
- AI platforms
- Anything!

**RootPulse proves emergence works.**

---

## 🌟 Tagline

> **"Version control that grows with you — rooted in sovereignty, pulsing with life."**

---

## 🔗 Next Steps

1. Read [01_PHILOSOPHY.md](./01_PHILOSOPHY.md) — Understand why emergence matters
2. Explore [02_ARCHITECTURE.md](./02_ARCHITECTURE.md) — See how it's built
3. Review [10_ROADMAP.md](./10_ROADMAP.md) — Learn the implementation plan

---

**Welcome to RootPulse!** 🌳🚀

*Where code becomes permanent through primal harmony.*

