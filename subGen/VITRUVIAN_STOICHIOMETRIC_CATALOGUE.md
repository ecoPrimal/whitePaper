# Vitruvian Stoichiometric Catalogue

**Wave**: 178 | **Date**: October 21, 2026
**Method**: Full census → Shannon width → body-region mapping

---

## 1. Language Census (the Layers)

| Language | Files | Lines | Role in Organism | Vitruvian Layer |
|----------|------:|------:|-----------------|----------------|
| **Rust** (.rs) | 20,075 | 5,372,244 | Bones — type system, compiled, the skeleton | Musculoskeletal |
| **Markdown** (.md) | 17,014 | 4,428,877 | Knowledge — papers, docs, memory | Brain/Mind |
| **HTML** (.html) | 4,496 | 623,417 | Skin — the visible surface | Integumentary |
| **Python** (.py) | 904 | 212,871 | Nerves — scripting, glue, signal processing | Nervous |
| **TOML** (.toml) | 1,901 | 171,017 | DNA — configuration, manifest, genotype | Genetic |
| **Shell** (.sh) | 856 | 155,180 | Breath — cron jobs, automation, the breathing | Respiratory |
| **JavaScript** (.js) | 230 | 81,997 | Senses — vision, sound, touch (the HUD) | Sensory |
| **TOTAL** | **45,476** | **11,045,603** | | |

### Width (Type Vocabulary — Rust only)

| Type | Count | Density |
|------|------:|---------|
| `pub enum` | 5,386 | 1 per 997 lines — enum every ~1K lines |
| `pub struct` | 18,308 | 1 per 293 lines — struct every ~300 lines |
| `impl` blocks | 17,111 | 1 per 314 lines |
| `pub trait` | 813 | 1 per 6,608 lines — traits are rare (irreducible) |

**Width score**: 41,618 type definitions across 5.37M lines = 1 type per 129 lines.
This is DENSE. For comparison, typical Rust codebases average 1 type per 200-400 lines.
The ecosystem has high type diversity — many small, specific types rather than few large ones.

---

## 2. Vitruvian Man — Body Regions by Organism

```
                    ┌─────────────────────┐
                    │       HEAD          │
                    │  bingoCube    10,509 │
                    │  cellMembrane 79,270 │
                    │            = 89,779  │
                    └────────┬────────────┘
                             │
                    ┌────────┴────────────┐
                    │       EYES          │
                    │  squirrel   191,198  │
                    │  songBird   477,292  │
                    │            = 668,490 │
                    └────────┬────────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                  │
  ┌────────┴──────┐ ┌───────┴────────┐ ┌───────┴──────┐
  │    HANDS      │ │     SPINE      │ │     SKIN     │
  │ bearDog 540,950│ │ biomeOS 311,743│ │ skunkBat  73,033│
  │ nestGate414,728│ │ petalT  232,031│ │ rhizoC    62,573│
  │        =955,678│ │ sourD    24,444│ │ sweetG    66,150│
  └───────────────┘ │        =568,218│ │ loamS     69,710│
                    └────────────────┘ │         =271,466│
                             │         └────────────────┘
                    ┌────────┴────────────┐
                    │       HEART         │
                    │  swarmVine    7,965  │
                    │  benchScale   ~8,000 │
                    │            = ~15,965 │
                    └────────┬────────────┘
                             │
                    ┌────────┴────────────┐
                    │       FEET          │
                    │  toadStool  718,846  │
                    │  coralReef  158,410  │
                    │  barracuda        0  │
                    │            = 877,256 │
                    └─────────────────────┘
```

### Body Region Summary (Rust lines only)

| Region | Organisms | Rust Lines | % Total | Mass | Stability |
|--------|-----------|----------:|--------:|-----:|-----------|
| Feet (grounding) | toadStool, coralReef | 877,256 | 25.3% | 175+ | HEAVY — neuromorphic substrate |
| Hands (motor) | bearDog, nestGate | 955,678 | 27.6% | 200+135 | HEAVY — identity + storage |
| Eyes (sensory) | squirrel, songBird | 668,490 | 19.3% | 155+160 | MEDIUM — observation + network |
| Spine (autonomic) | biomeOS, petalTongue, sourDough | 568,218 | 16.4% | 150+120+145 | MEDIUM — routing + display + tooling |
| Skin (immune) | skunkBat, rhizoCrypt, sweetGrass, loamSpine | 271,466 | 7.8% | 165+170+185+190 | THIN — defense perimeter (correct!) |
| Head (executive) | bingoCube, cellMembrane | 89,779 | 2.6% | 100+N/A | TINY — synthesis is compression |
| Heart (vital) | swarmVine, benchScale | ~15,965 | 0.5% | 110 | TINY — the heart is small |
| **barracuda** | (empty primal) | 0 | 0% | 140 | **NULL BODY** — compute lives in springs |

### The Ratios

- **Hands + Feet** (motor + grounding) = 52.9% — more than half the code moves things or stabilizes
- **Skin** = 7.8% — the membrane IS the thinnest surface (correct per Klein bottle)
- **Head** = 2.6% — the brain is tiny compared to the body (biologically correct — synthesis IS compression)
- **Heart** = 0.5% — the heart doesn't need to be big, just reliable

---

## 3. The Fat (Over-Stable, Gunk, Duplicates)

### Over-Fat Files (candidates for grinding)

| File | Lines | Issue |
|------|------:|-------|
| `chipmunk-commands.js` | 4,116 | Fattest JS — likely accumulated commands, needs splitting |
| `wordlist.rs` | 2,059 | Static word list — data, not logic |
| `opsonize-rs/main.rs` | 1,847 | Everything in one file — needs splitting into modules |
| `stone_book.rs` | 1,846 | The stoneBook counter — fat but functional |
| `scan_sweep_sort.py` | 2,764 | Core pipeline — fat because it's the SPINE of Python |
| `dialogue-weave.py` | 2,000 | Mesh dialogue — large but may be irreducible |
| `_CONSOLIDATED_GUIDANCE.md` | 23,563 | Bloated export — fossil (stale) |

### Stale/Duplicate (food for sourdough)

| What | Size | Status |
|------|------|--------|
| `phase1/` | 549,697 lines | Superseded by current primals — FOSSIL |
| `fossilRecord/*.py` | 78 files | Deprecated scripts — FOSSIL |
| `network-graph.js` | 3 copies | detroit + publicRecord static + public — DUPLICATE |
| `network-data.js` | 2 copies | publicRecord static + public — DUPLICATE |
| `brainchip_devhub/*.ipynb` | 16,331 lines | Notebooks — reference, not active |
| `braid_pentest.py` | 2 copies × 1,336 | fossilRecord + wateringHole — DUPLICATE |
| `barracuda/` primal | 0 lines | **NULL BODY** — compute lives in springs/hotSpring/barracuda |
| `protists/footPrint/coverage/` | 30 HTML files | Generated coverage — STALE |

### Stale Lines Total: ~600,000+ lines

That's ~5.4% of the codebase that is fossil/duplicate/stale. Sourdough food.

---

## 4. The Irreducible (What Cannot Be Ground Further)

### Rust Bones

| Irreducible | What | Why it can't shrink |
|------------|------|-------------------|
| 813 pub traits | The immune receptors — each defines a capability boundary | Traits ARE the membrane's selectivity |
| 5,386 pub enums | The epitope vocabulary — each names a state | Enums ARE the sort keys |
| Type density 1:129 | One type per 129 lines | This IS the information density |

### JavaScript Senses (HUD)

| Irreducible | What | Why |
|------------|------|-----|
| 106 HUD modules | Each is a unique sensory surface | Each module IS a nerve ending |
| 54,796 lines | The sensory cortex | Vision, sound, touch, smell (third-eye) |
| 4 primitives | Point · Balance = Wedge ∧ Arc ⌒ | Paper 88 — the irreducible toolkit |

### Python Nerves

| Irreducible | What | Why |
|------------|------|-----|
| scan_sweep_sort.py | The core pipeline (2,764 lines) | This IS the nervous system's main trunk |
| membrane-lens.py | The observation relay (715 lines) | The lens between AI and membrane |
| serve-local.py | The HUD server (1,614 lines) | The local nerve bundle |

### Shell Breath

| Irreducible | What | Why |
|------------|------|-----|
| klein-io.sh | The fold (every 2min) | The inhale |
| klein-vent.sh | The gas vent (every 5min) | The exhale |
| sourdough-cache.sh | Succession (every 5min) | The fermentation |
| membrane-pulse.sh | Vitals (every 5min) | The heartbeat |

---

## 5. Jellystein Has Bones Underneath

coGen 5 (EVOLUTION_CHAIN): "jellystein has usefulness" — the 4-stage evolution chain.

| Stage | Language | Lines | What it IS |
|-------|----------|------:|-----------|
| Jellyfish | JavaScript | 81,997 | Soft body, no skeleton, all nerve. The 106 HUD modules. |
| Bones underneath | Rust (cellmembrane-types) | 79,270 | The type system that JS reads via JSON feeds |
| Exoskeleton | TOML | 171,017 | Configuration = the shell that holds shape |
| Endoskeleton | Rust (primals) | 5,372,244 | The internal skeleton — compiled, typed, tested |

JS has no types. But JS reads JSON. JSON is typed by the Rust structs that produced it. The jellyfish (HUD) floats on top of bones (cellmembrane-types) that it never sees. The klein-io.js reads state.json, which was written by klein-io.sh, which reads from Rust services, which are typed by pub structs. The bones are underneath.

---

## 6. Over-Stable vs Prime (π-Stability Applied to Code)

| Metric | Value | Divisors | Stability |
|--------|------:|---------|-----------|
| Rust files | 20,075 | many | Over-stable |
| JS modules (HUD) | 106 | 2 (2×53) | 53 is PRIME — good! |
| Python files | 904 | many | Over-stable |
| Pub traits | 813 | 3 (3×271) | 271 is PRIME — the trait count wobbles |
| Pub enums | 5,386 | many | Over-stable — the vocabulary is settled |
| Body regions | 7 | 1,7 | PRIME — the anatomy is irreducible |
| Total files | 45,476 | many | Over-stable — time to grind |

---

---

## 7. The Senses (Papers 90-93)

### Touch (Paper 91: Homunculus)

| Sense | Metric | Score |
|-------|--------|-------|
| CNS (central) | 20,347 files (44.7%) | Sensitivity: 0.3227 |
| PNS (peripheral) | 25,127 files (55.3%) | Sensitivity: 0.2237 |
| **CNS/PNS ratio** | **1.4422** | **≈ 1/ln(2) = 1.4427 (0.035% off)** |

The spine converts nats to bits at the Shannon constant. The fingertips (most sensitive): `scan_sweep_sort.py` (0.602), `opsonize-rs/main.rs` (0.601). The dead tissue (numbest): `docs-fossil-feb-2026` (0.106, 418 days old).

### Sight (Paper 92b: Trig-View)

| Angle | Files | % | Character |
|-------|------:|---:|-----------|
| 0° | 1,411 | 3.1% | Pure core — the skeleton |
| 45° (π/4) | 3,119 | 6.9% | THE BALANCE (tan=1) |
| 90° (π/2) | 29,749 | 65.4% | THE WALL (tan=∞) |
| >90° | 0 | 0% | THE FOLD (empty — hasn't manifested in code yet) |

65.4% at 90°. 0% past 90°. The Klein fold hasn't reached into source structure yet.

### Taste (Paper 93: Flavor)

| Flavor | Receptor | What it detects | Vitruvian location |
|--------|----------|----------------|-------------------|
| **Sweet** | T1R2/T1R3 | Nourishment — production > consumption | Mouth (head) |
| **Sour** | PKD2L1 | Extraction — consumption > production | Mouth (head) |
| **Spicy** | TRPV1 | Provocation — falsifiable, burns, not toxic | Mouth (head) |
| **Bitter** | T2R (25 types) | Toxin — broken, dead, fossil | Mouth (head) |
| **Umami** | T1R1/T1R3 | Complexity — deep, layered, takes time | Mouth (head) |

Codebase flavor profile:
- **Sweet**: type definition modules, anti-secret feeds (production > consumption)
- **Sour**: 0 parasitic sinks (all 30 sinks are correct test/deploy tissue)
- **Spicy**: Paper 92 (the extraction hypothesis), the Jester's Conjecture
- **Bitter**: 600K fossil lines (5.4%), 5 DOWN services
- **Umami**: 473 vertebrate files (deep structure, 10+ types each)

### Evolution (Paper 90: Evolutionary Sort)

| Stage | Files | % Lines | Note |
|-------|------:|--------:|------|
| Banana | 2,157 | 0.2% | Config stubs |
| Flatworm | 10,661 | 10.0% | Bilateral, has a head |
| **Jellyfish** | **21,220** | **58.6%** | **DOMINANT — nerve net, no skeleton** |
| Centipede | 2,113 | 6.3% | PRIME count (2,113) |
| Millipede | 8,846 | 23.0% | Many paired segments |
| **Spider** | **0** | **0%** | **THE GAP — missing body plan** |
| Vertebrate | 473 | 2.0% | Internal skeleton — Rust-only |

98% invertebrate. Split ratio: 43:1 (prime). The spider niche is the wedge.

---

*The Vitruvian man stands in the circle (the geodesic) and the square (the grid).*
*The hands reach the circumference (π). The feet touch the ground (integer).*
*The head is tiny and compresses. The feet are massive and stabilize.*
*The skin is thin — the thinnest surface between inside and outside.*
*The heart is small — it just needs to beat.*
*The tongue tastes five flavors. The eyes see angles. The fingers feel sensitivity.*
*The body sorted itself into evolutionary stages. 58.6% jellyfish. 2% vertebrate. 0% spider.*
*5.4% of the body is fossil. Sourdough food.*
*The rest is alive. 11 million lines. One organism. Five senses.*

*— Wave 178 · Stoichiometric Catalogue v2*
