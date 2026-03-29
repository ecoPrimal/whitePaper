<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# Sub-Thesis 24: Esoteric Webb — Primal Composition as Creative Infrastructure

**Date:** March 25, 2026
**Status:** V5, 329 tests, 90.84% coverage, 35 Rust files (~12.5k LOC)
**Foundation:** ecoPrimals gen4 composition layer; primalSpring IPC patterns; wateringHole standards

## Abstract

We demonstrate that a complex creative product (a Disco Elysium-inspired CRPG
with DAG-traced narrative, deep NPCs, emergent ability interactions, and
meaningful bounded endings) can be built entirely from composed primal services
without importing any primal or spring Rust crate. All coordination occurs at
runtime via JSON-RPC IPC over TCP/UDS. This establishes the gen3→gen4
boundary: infrastructure becomes invisible inside a product someone actually
uses.

The key architectural contribution is a **6-phase graceful degradation
pipeline** where every player action flows through AI narration → NPC
dialogue → flow evaluation → scene push → provenance lifecycle, with each
phase degrading silently when its backing primal is unavailable. Gameplay is
never blocked by missing infrastructure.

## Relationship to the Constrained Evolution Thesis

The constrained evolution thesis (gen3) proved that science computes correctly
across 7 springs with 12k+ validation checks. Esoteric Webb asks the gen4
question: **can people who didn't build the primals compose them into tools
they care about?**

This mirrors biological evolution: once molecular machinery (primals) is
reliable, organisms (compositions) can use it without understanding its
internal mechanisms. The composition surface must be:

1. **Discovery-based** — primals found by capability, not hardcoded address
2. **Degradation-tolerant** — missing capabilities reduce fidelity but never
   break function
3. **Semantically classified** — errors carry operational meaning
   (retriable vs fatal) across IPC boundaries
4. **Zero coupling** — no shared Rust crates, no compile-time dependencies

## Key Findings

### 1. Semantic Error Classification Enables Resilient Composition

Flat error enums (`Io(String)`) lose operational meaning at IPC boundaries.
By classifying errors semantically (`ConnectionRefused`, `Timeout`,
`MethodNotFound`, `ApplicationError`), circuit breakers and retry policies
can make intelligent decisions without string parsing. This pattern emerged
independently in primalSpring and was absorbed by Webb, confirming it as an
ecosystem-wide need.

### 2. Single Source of Truth Eliminates Coordination Debt

Every system that maintains its own list of known primals accumulates
coordination debt as the ecosystem grows. A canonical names module reduces
the cost of adding new primals from "update N files" to "add one line."

### 3. Smart Refactoring Preserves Cohesion Under Size Constraints

When a module exceeds quality gates (1000 lines), naive splitting scatters
related logic. Identifying *semantic boundaries* (data types, pipeline logic,
core state management) produces modules that are independently comprehensible
while sharing state via `pub(crate)` visibility.

### 4. Coverage Gates Drive Targeted Testing

Setting `--fail-under-lines 90` as a CI gate forced identification of
untested *behavior paths* rather than inflating test counts with trivial
assertions. The most impactful coverage gains came from testing:
- Content validation edge cases (missing NPC, empty compound predicates)
- Topological sort edge cases (diamond dependencies, missing deps, cycles)
- Metadata ingestion edge cases (missing fields, bad TOML)
- Protocol handling (TCP listener parse errors, empty lines)

### 5. Edition 2024 Constraints Shape Design

Rust 2024's `unsafe` classification of `std::env::set_var()` means
env-var-dependent code paths cannot be directly unit-tested under
`#![forbid(unsafe_code)]`. This forces design toward pure-function
alternatives that accept configuration as parameters rather than reading
the environment directly.

## Architecture

```
Springs (science)  →  produce  →  primals (genomeBin/ecoBin)
                                         ↓
                                 plasmidBin/ (deployment surface)
                                         ↓
                    Webb discovers via 5-tier capability probe
                           (env vars → metadata → filesystem → Songbird)
                                         ↓
                    PrimalBridge composes 8 domains with 23 methods
                           (retry + circuit breaker per domain)
                                         ↓
                    6-phase enrichment per player action:
                      narrate → dialogue → flow → scene → DAG → close
                                         ↓
                    Each phase degrades silently → gameplay never blocked
```

## Metrics

| Metric | Value |
|--------|-------|
| Tests | 329 (316 unit + 12 E2E + 1 validation) |
| Coverage | 90.84% lines |
| Rust files | 35 |
| LOC | ~12,500 |
| Bridge methods | 23 (all domains, all degrading) |
| Primal domains | 8 (ai, game, viz, dag, lineage, compute, storage, provenance) |
| Unsafe code | `#![forbid(unsafe_code)]` |
| C dependencies | 0 |
| Quality gates | 6/6 (fmt, clippy, test, doc, deny, coverage) |

## Implications for Ecosystem Evolution

1. **Composition surfaces need semantic errors** — any primal producer should
   classify errors with `is_retriable()` / `is_recoverable()` methods.
2. **Discovery standards need enforcement** — capability-based discovery
   works at tiers 1-4 (filesystem) but tier-5 (Songbird) remains untested.
3. **plasmidBin needs CI** — the gap between "primals exist" and "primals
   are deployed" is the primary blocker for gen4 adoption.
4. **Creative surfaces validate infrastructure** — Webb found and logged 15+
   evolution gaps that fed back to 6 primal teams, proving that consumers
   are the best auditors of producer capabilities.
