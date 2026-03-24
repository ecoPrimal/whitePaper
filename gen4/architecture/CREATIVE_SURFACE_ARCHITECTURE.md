# Creative Surface Architecture

**The sporeGarden Organizational Model and How Products Relate to Infrastructure**

**Date**: March 24, 2026
**Lineage**: gen3/ECOSYSTEM_ARCHITECTURE → gen4/COMPOSITION_PATTERNS → sporeGarden

---

## Three Organizations, Three Functions

The ecoPrimals ecosystem is now three GitHub organizations:

```
ecoPrimals/              syntheticChemistry/        sporeGarden/
(infrastructure)         (science)                  (creative surface)
│                        │                          │
├── primals/             ├── hotSpring/             ├── esotericWebb/
│   ├── phase1/          ├── ludoSpring/            ├── [future products]
│   └── phase2/          ├── primalSpring/          └── ...
├── plasmidBin/          ├── neuralSpring/
├── wateringHole/        ├── groundSpring/
├── whitePaper/          ├── wetSpring/
└── ecoSprings/          ├── airSpring/
    └── esotericWebb/    └── healthSpring/
```

| Org | Question | Output | Audience |
|-----|----------|--------|----------|
| ecoPrimals | Does the infrastructure work? | Primals, standards, guidance | Developers, maintainers |
| syntheticChemistry | Does the science reproduce? | Springs, experiments, papers | Scientists, faculty |
| sporeGarden | Does someone use it? | Products, tools, creative systems | Creators, players, clinicians |

---

## The "Powered By" Model

A sporeGarden product is "powered by" ecoPrimals infrastructure. This
is not a marketing phrase; it is an architectural relationship:

### What "Powered By" Means

1. The product **consumes** primals via JSON-RPC TCP (zero imports)
2. The product **discovers** primals via Songbird capability broadcast
3. The product **degrades** gracefully when primals are absent
4. The product **attributes** via sweetGrass braids
5. The product **traces** via rhizoCrypt provenance DAGs
6. The product **owns** its creative content and license

### What "Powered By" Does Not Mean

1. The product is not an ecoPrimals project (different org, different license scope)
2. The product does not ship primal source code (binary composition only)
3. The product does not require all primals (graceful degradation)
4. The product does not pay ecoPrimals (sovereignty, not platform rent)

---

## The Spore Metaphor

The naming is biological and precise:

- **ecoPrimals** = the mycelium network (underground, invisible,
  everywhere, distributing nutrients)
- **syntheticChemistry / springs** = the fruiting conditions (specific
  environmental niches where mycelium produces spores — science domains)
- **sporeGarden** = the cultivation surface where spores land and grow
  into visible organisms (products people interact with)

A spore carries genetic information from the parent organism but grows
in its own soil, its own light, its own conditions. A sporeGarden
product carries primal capabilities but grows in its own creative
domain.

esotericWebb is a CRPG spore. A future health dashboard would be a
clinical spore. A field genomics kit would be a research spore. Same
mycelium, different gardens.

---

## Product Architecture Layers

Every sporeGarden product has four layers:

```
┌─────────────────────────────────────────────┐
│          Layer 4: Creative Content           │
│  YAML worlds, rulesets, NPCs, abilities     │
│  Authored by creators, validated by engine   │
├─────────────────────────────────────────────┤
│          Layer 3: Product Engine             │
│  GameSession, GameDirector, WorldState      │
│  The product's core logic                    │
├─────────────────────────────────────────────┤
│          Layer 2: PrimalBridge              │
│  JSON-RPC composition, degradation, cache   │
│  The invisible infrastructure interface      │
├─────────────────────────────────────────────┤
│          Layer 1: Primal Binaries           │
│  plasmidBin/ deployed via deploy graphs     │
│  The sovereign compute substrate             │
└─────────────────────────────────────────────┘
```

### Layer 1: Primal Binaries

Deployed from `plasmidBin/` or discovered via Songbird. The product
does not manage these — the deploy graph and PrimalLauncher handle
spawning, readiness checks, and lifecycle.

### Layer 2: PrimalBridge

The composition interface. All primal communication goes through the
bridge. The bridge handles connection pooling, retry logic, circuit
breaking, capability caching, and graceful degradation. This is the
only layer that knows primals exist.

### Layer 3: Product Engine

The product's core logic. For esotericWebb, this is `GameSession`,
`GameDirector`, `WorldState`, `NarrativeGraph`. This layer receives
`PrimalEnrichment` from the bridge and uses it to advance the product's
state. It does not know or care which primals contributed.

### Layer 4: Creative Content

The creator-facing surface. YAML files define worlds, rooms, NPCs,
abilities, rulesets, dialogue trees. The product engine validates and
consumes this content. The creator never interacts with layers 1–2.

---

## The Content Pipeline

Content flows from creator to player through the four layers:

```
Creator writes YAML
    │
    ├── validate (engine checks syntax, predicates, graph connectivity)
    ├── preview (text-mode playthrough, no primals needed)
    ├── graph (visualize narrative topology)
    │
    ├── [primals available?]
    │     ├── yes → full composition (AI narration, flow, provenance)
    │     └── no → standalone mode (templates, local state, text output)
    │
    └── Player experiences the world
          │
          └── NFT: the playthrough is a Novel Ferment Transcript
                  (provenance DAG → dehydrate → permanent record)
```

### Content Formats

| Format | Purpose | Spec |
|--------|---------|------|
| World YAML | Rooms, edges, predicates, metadata | CONTENT_AUTHORING_SPEC.md |
| NPC YAML | Personality, knowledge, trust, dialogue seeds | CONTENT_AUTHORING_SPEC.md |
| Ability YAML | Mechanics, stat effects, interaction rules | CONTENT_AUTHORING_SPEC.md |
| Ruleset TOML | Core rules, dice systems, stat definitions | RulesetCert (loamSpine) |
| Deploy graph TOML | Primal topology, ports, capabilities | COMPOSITION_PATTERNS.md |
| Niche TOML | Product metadata, version, capabilities | ecoBin standard |

---

## The Trust Model

### Creator → Product

The creator trusts the product engine to validate their content
correctly. The engine's validation is deterministic and inspectable
(transparent dice principle from Cliche Studio).

### Product → Primals

The product trusts primals because they are ecoBin-compliant: pure
Rust, zero unsafe, zero C deps, AGPL-licensed, capability-discoverable.
The bridge verifies capabilities via JSON-RPC handshake.

### Player → Product

The player trusts the product because:
- The provenance DAG (rhizoCrypt) records everything — the game cannot
  lie about what happened
- The ruleset is a loamSpine certificate — the rules are verifiable
- The attribution braids (sweetGrass) credit everyone — no silent
  extraction

### Creator → Player

sweetGrass braids connect creators to players. When a player experiences
authored content, the attribution records the relationship. When a
player's choices create emergent narrative, the player gets attribution
too. The Novel Ferment Transcript is the shared artifact.

---

## Lean Consumption vs. Hard Linking

Two models for how products relate to primals:

### Lean Consumption (recommended for gen4)

The product consumes primal capabilities via TCP. It does not know the
primal's implementation. It can swap primal versions without
recompilation. This is the model esotericWebb uses.

**Advantages**: Version independence, deployment flexibility, language
independence, clean license boundary.

**Tradeoff**: Network latency (mitigated by connection pooling and
local-machine TCP, which is microseconds).

### Hard Linking (gen3 model, for springs)

The spring imports primal crates directly. It compiles primal code into
its own binary. This is how springs work — they are validating the
primal code itself, so they need direct access.

**Advantages**: Zero network overhead, compile-time type checking,
direct access to internal APIs.

**Tradeoff**: Version coupling, recompilation on primal upgrade, license
contagion (AGPL applies to the linked binary).

gen4 products should use lean consumption. gen3 springs should use
hard linking. The distinction is architectural: products consume
capabilities, springs validate implementations.

---

## Federation and Multi-Node Products

TCP composition enables federation naturally. A gen4 product's primals
don't need to be on the same machine:

```
Machine A (creator's laptop)          Machine B (GPU server)
┌─────────────────────┐              ┌─────────────────────┐
│ esotericWebb        │    TCP       │ toadStool (GPU)     │
│ PrimalBridge ───────│──────────────│ Squirrel (AI model) │
│                     │              │ barraCuda (math)    │
│ rhizoCrypt (local)  │              └─────────────────────┘
│ loamSpine (local)   │
└─────────────────────┘
```

The deploy graph specifies remote endpoints. The PrimalBridge connects
to them. The product doesn't care whether a primal is local or remote —
the JSON-RPC interface is the same.

This is how a solo creator develops on a laptop (standalone mode with
local primals) and deploys to a server (full mode with GPU primals on
a separate machine). Same product, same content, different deployment
topology.

---

## The sporeGarden Product Catalog (Projected)

| Product | Domain | Status | Key primals |
|---------|--------|--------|-------------|
| esotericWebb | Interactive narrative / CRPG | V4 (active) | All 8 domains |
| RPGPT Engine | Ingestible rulesets / living game | Conceptual | ludoSpring, Squirrel, trio |
| Games@Home | Distributed human computation | Conceptual | toadStool, ludoSpring, BearDog |
| Field Genomics Kit | Sample provenance pipeline | Conceptual | trio, NestGate, BearDog |
| Patient Records | Zero-knowledge health dashboard | Conceptual | trio, BearDog, Squirrel |
| Creative Canvas | Visual art + attribution | Conceptual | petalTongue, sweetGrass, trio |

Each product follows the same four-layer architecture. Each consumes
primals via PrimalBridge. Each degrades gracefully. Each can be
developed standalone. The composition patterns are the same; the
creative domains are different.

---

*The mycelium doesn't care what grows in the garden. It just moves
nutrients. The garden doesn't care what's underground. It just grows.
That's the architecture.*
