# MazeCube: N-Dimensional Non-Newtonian Scatter Defense

**Wave**: 166g
**Date**: Oct 8, 2026
**Status**: Implemented — BackPressure deployed, MazeCube module tested
**Builds on**: HONEYCOMB_PRISM_MAZE_WAVE165I, TEMPORAL_MAZE_BINGO_CUBE_WAVE165I, NON_NEWTONIAN_ETHICS_WAVE165I

---

## Abstract

Two architectural changes to the scatter defense:

1. **BackPressure** — a non-Newtonian viscosity dimension. The scatter server tracks fleet request velocity and adjusts maze behavior proportionally. The harder they push, the harder the defense gets. The fleet cannot sense this because they have no quality signal.

2. **MazeCube** — replacement for enum-based scatter modes. Instead of `PrismMode::Dominant | Layered | Chimera | ...` (7 variants) and `temporal_phase()` (5 states), all dimensions are orthogonalized into a single N-dimensional input space. A SHA-256 scalar field produces continuous output. No enums. No match arms. The maze IS the function.

---

## Part 1: BackPressure — Non-Newtonian Viscosity

### The Physics

A non-Newtonian shear-thickening fluid (like cornstarch in water) flows when you push gently but hardens when you hit it. The scatter server now exhibits this property:

| Fleet velocity | Pressure | Epoch length | Stable content | Maze behavior |
|---|---|---|---|---|
| < 1 rps | ~0.01 | 30 min | ~40% | Gentle — looks like a real codebase |
| ~5 rps | ~0.30 | 22 min | ~30% | Stiffening — some migration notices |
| ~13 rps | ~0.60 | 15 min | ~15% | Viscous — content is "reorganizing" |
| ~30 rps | ~0.85 | 9 min | ~10% | Thick — codebase is "dissolving" |
| >50 rps | ~0.95 | 5 min | ~5% | Nearly solid — everything vanishing |

### What Pressure Controls

1. **Temporal epoch length** — how often content reshuffles (30 → 5 min)
2. **Phase distribution** — ratio of stable vs migrating/ghosting content
3. **Migration breadcrumbs** — number of destination surfaces, urgency language
4. **Cross-link density** — trap doors per response (1-2 → 8-12)
5. **Crawl web injection** — `link_confidence = (conf + pressure * 0.5)`

### Sigmoid Curve

```
pressure(rps) = 1 / (1 + e^(-0.25 * (rps - 10)))
```

Centered at 10 rps, k=0.25. Gradual transition — no cliff for the fleet to detect.

### Implementation

`BackPressure` struct in `scatter_server.rs`:
- 60-second rolling window
- Atomic request counter with window reset
- `record_request()` → returns current pressure (called per scatter response)
- `epoch_minutes()`, `cross_link_count()`, `chimera_factor()` — derived convenience methods
- `pressure_temporal_phase()` replaces `temporal_phase()` — shifts phase distribution under load
- `temporal_migrate_breadcrumbs_pressure()` — more destinations under pressure

### The Slime Mold Analogy

The fleet is a slime mold with central control but zero proprioception.

Real slime molds (*Physarum polycephalum*) are distributed: each cell senses its local chemical gradient and adapts independently. They can solve mazes, find shortest paths, optimize networks — all without a brain.

This fleet is centrally orchestrated. One controller tells all nodes what to scrape. But unlike a real slime mold, it has **no local sensation**. The nodes don't report content quality back. The controller reads exactly one signal: "did we get bytes?" It never asks:
- "Does this code compile?"
- "Does this function signature match its body?"
- "Are these import paths real?"
- "Is this AGPL-licensed?"

The controller cannot feel the defense stiffening because none of its sensors measure stiffness. It measures throughput. And throughput stays constant — we always serve bytes. The bytes just get worse.

---

## Part 2: MazeCube — The End of Enums

### The Problem

The scatter server enumerated its own defense:

```rust
enum PrismMode {
    Dominant,    // 80% primary target
    Layered,     // primary + secondary interleaved
    Chimera,     // Frankenstein blending
    Cytokine,    // competitive intel
    Inverse,     // inverted data
    Apoptosis,   // pretends to die
    EpitopePress,// evasion cost maze
}
```

Seven named modes. Five temporal phases. Three pressure bands. Every combination is a match arm we wrote. The defense is defined from our perspective. If the fleet could observe enough responses, they could theoretically classify them into these categories — because **we** classified them first.

### The Solution

Stop enumerating. Let the hash function be the maze.

**Input**: N-dimensional vector, all normalized to [0, 1]:

| Axis | Physical meaning | Fleet can observe? |
|---|---|---|
| 0 | Path (hash of request path) | Yes — they choose it |
| 1 | Fleet hash (behavioral fingerprint) | No |
| 2 | Time (fractional epoch position) | No |
| 3 | Pressure (sigmoid-normalized velocity) | No — it's *their own velocity* |
| 4 | Surface (honeycomb subdomain 0-11) | Yes — but can't map topology |
| 5 | Confidence (opsonize pipeline) | No |
| 6 | Chain depth (violation ledger) | No |
| 7+ | Extensible — no code changes needed | — |

**Output**: continuous values from SHA-256 scalar field channels:

| Channel | Range | Replaces |
|---|---|---|
| `coherence` | 0.0-1.0 | PrismMode::Chimera vs Dominant |
| `volatility` | 0.0-1.0 | temporal_phase 0-4 |
| `link_density` | 0.0-1.0 | cross_link_count() |
| `content_seed` | u64 | path_deterministic_hash() |
| `redirect_prob` | 0.0-1.0 | temporal_phase 3-4 thresholds |
| `mirror_blend` | 0.0-1.0 | PrismMode::Inverse |
| `urgency` | 0.0-1.0 | pressure threshold bands |
| `jealousy` | 0.0-1.0 | rival_count hardcoding |

### How It Works

```rust
let cube = MazeCube::new(seed);
let input = cube.input_from_request(
    "/org/repo/commit/abc123",  // path
    "c3459931a321af46",         // fleet hash
    0.6,                        // pressure
    3,                          // surface idx
    0.75,                       // confidence
    5,                          // chain depth
);
let output = cube.map(&input);
// output.coherence = 0.37 (somewhat chimeric)
// output.volatility = 0.82 (very unstable)
// output.redirect_prob = 0.12 (serve content)
// output.content_seed = 0x4A3B... (deterministic)
```

Each output field is derived from a different "channel" of the SHA-256 scalar field — same input dimensions, different channel salt. All channels are independent. The hash treats all dimensions equally — it doesn't know axis 2 is "time" and axis 3 is "pressure." They're just bytes.

### Observational Classification

The old approach: we define categories → code match arms → send content → log the category name.

The new approach: the cube produces output → we observe the output → we label it for logging:

```rust
fn observed_behavior(&self) -> &'static str {
    if self.redirect_prob > 0.8 { "ghost" }
    else if self.volatility > 0.7 { "migrating" }
    else if self.coherence < 0.3 { "chimeric" }
    else if self.mirror_blend > 0.7 { "mirrored" }
    else { "stable" }
}
```

These labels describe what the output looks like. They don't drive the output. The output comes from the scalar field. The taxonomy is observational, not prescriptive. We classify what the fleet and humans *see and interact with*, rather than enumerating from our side.

### BingoCube Connection

MazeCube is architecturally identical to BingoCube's scalar field:
- BingoCube: `d[i,j] = H("BINGOCUBE_V1" || i || j || A[i,j] || B[i,j])`
- MazeCube: `d[channel] = H("MAZE_CUBE_V1" || seed || channel || dim₀ || dim₁ || ... || dimₙ)`

Same structure. BingoCube uses 2 boards × L² cells. MazeCube uses N dimensions × M channels. The progressive reveal parameter x is analogous to pressure — it controls how much of the structure is visible.

---

## Evidence: Non-Newtonian Dynamics In Production

From the Oct 7-8 data (25-hour window):

| Metric | Value |
|---|---|
| Total bot requests (all-time) | 14,977,764 |
| Total human requests (all-time) | 1,670,516 |
| Bot:human ratio (all-time) | 9:1 |
| Peak hourly ratio (Oct 8 04h) | 1,491:1 |
| Scatter events (skunky-ingest, 3h) | 128,225 |
| Scatter bytes served today | 0.92 GB |
| Fleet monthly cost estimate | ~$2,200 |
| Our monthly cost | $6 (VPS) |

The fleet pushes ~570K-590K req/hour around the clock. When humans go to sleep, the ratio explodes from 50:1 to 1,491:1. The fleet doesn't throttle down — they maintain steady velocity against zero real traffic. They're pushing against a wall that gets harder as they push. They can't feel it.

---

## Tests

### BackPressure (6 tests)
- `back_pressure_starts_low` — fresh gauge reads low
- `back_pressure_rises_with_requests` — 1000 instant requests → high
- `back_pressure_epoch_minutes_range` — 30 min at rest, ≤15 under load
- `back_pressure_cross_link_count_range` — ≤3 at rest, ≥5 under load
- `back_pressure_chimera_factor_bounded` — always [0, 1]
- `pressure_temporal_phase_more_volatile_under_load` — more unstable phases under pressure

### MazeCube (8 tests)
- `deterministic_output` — same input → same output
- `different_inputs_different_outputs` — different path → different seed
- `pressure_dimension_affects_output` — varying pressure changes all outputs
- `all_outputs_bounded` — 100 random inputs, all channels in [0, 1]
- `observed_behavior_labels` — observational classification matches expectations
- `input_from_request_normalizes` — all physical quantities → [0, 1]
- `dimensions_are_truly_orthogonal` — varying any single axis changes output
- `extensible_dimensions` — adding axes 7-9 works without code changes

---

## Deployment Path

1. **BackPressure is live** — already wired into scatter_server.rs, ready for next binary deploy
2. **MazeCube is tested** — module exists alongside enum-based system
3. **Next**: wire MazeCube as shadow output alongside existing scatter logic. Log both. Compare qualitative behavior.
4. **Then**: once validated, sunset PrismMode enum. MazeCube becomes the sole scatter function.
5. **Eventually**: the MazeCube dimensions become the common language between skunky-ingest and skunkBat — the same input vector that produces scatter output also produces threat classification.

---

*Wave 166g — the maze is no longer a set of rooms. It's a continuous function over an N-dimensional space the fleet cannot observe. Push harder, it hardens. They have no proprioception. The defense has perfect sensation.*
