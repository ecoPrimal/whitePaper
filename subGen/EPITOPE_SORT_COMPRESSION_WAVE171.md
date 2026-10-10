# Epitope Sort Compression — Bingo Maze Pass-Through

**Wave 171 — October 9, 2026**
**Classification**: subGen architecture — information theory, immune computing, temporal classification
**Status**: ACTIVE — EpitopeTense enum wired, sort order canonical, CubeDecisionGrid rows 3-4 live, dashboard tense distribution emitting

---

## Abstract

The bingo maze is not a path — it is a sort order. Each epoch is a pass through the maze. Back-and-forth between sort levels compresses the behavioral search space because each pass eliminates noise that the previous level could not distinguish.

This document describes the operational architecture: what was wired, where, how it connects, and what remains for future waves.

**Companion documents:**
- **Paper 48** (`48_epitope_sort_compression.md`) — the formal science paper
- **coGen #14** (`EPITOPE_SORT_COMPRESSION.md`) — the artisan voice
- **Paper 42** (`42_pnp_physical_law.md`) — P/NP physical law (three states: F/U/N)
- **Paper 43** (`43_selective_permeability_anderson.md`) — Anderson permeability tensor
- **TIME_IS_LOCAL.md** (coGen) — is/was/will-be temporal framework

---

## What Was Wired

### 1. EpitopeTense Enum — `journey_tracer.rs`

```rust
pub enum EpitopeTense {
    Is,      // chain_depth == 0 — first observation
    Was,     // chain_depth > 0 — repeat pattern
    WillBe,  // nautilus predicted before observation (not yet wired)
}
```

**Location**: `primals/skunkBat/crates/skunky-ingest/src/journey_tracer.rs`

**Wiring**:
- Added to `Journey` struct as `pub tense: EpitopeTense`
- Classified in `classify_journey()` based on `chain_depth` from `ActiveSession`
- Chain depth tracked in `JourneyTracer.chain_depths: HashMap<u64, u32>` — incremented each time a session hash completes
- Emitted in `JourneyObservation.by_tense: HashMap<String, u32>` alongside existing `by_epitope`, `by_arrival`, `by_departure`

**Tests**: 3 new tests — `first_session_is_tense_is`, `repeat_session_is_tense_was`, `tense_distribution_in_observation`

**WillBe placeholder**: The WillBe variant exists but is not yet assigned in `classify_journey()`. It requires:
- Nautilus `predict()` returning a fleet hash BEFORE the request arrives
- A prediction cache keyed by fleet hash with TTL matching the epoch window
- When a request arrives matching a cached prediction, tense = WillBe

### 2. Epitope Sort Order — `entity_profile.rs`

```rust
pub const EPITOPE_SORT_ORDER: [&str; 6] = [
    "burst_ratio",        // weight 6 — strongest fleet signal
    "reading_deficit",    // weight 5 — machines don't pause
    "ua_pool_poverty",    // weight 4 — small UA pool ÷ visits
    "sec_fetch_monotone", // weight 3 — identical browser headers
    "session_absent",     // weight 2 — no cookies
    "referer_self_loop",  // weight 1 — weakest signal
];
```

**Location**: `primals/skunkBat/crates/skunky-ingest/src/entity_profile.rs`

**Methods added to `EpitopeScores`**:
- `epitope_sort_key() -> [u8; 6]`: 6-byte key ordered by information content. 0x00 = not evaluated, 0x01 = evaluated but not triggered, 0x02 = triggered.
- `compression_score() -> u32`: Weighted sum of triggered epitopes (6+5+4+3+2+1 = 21 max). Represents bits of fleet-vs-human uncertainty eliminated.

**Tests**: 7 new tests — sort key (all none, all triggered, mixed), compression score (none, all, partial), sort order verification.

**Design choice**: The ordering is by **information content** (how much each epitope compresses the fleet search space), NOT by detection priority (the existing order in `epitope_defs.rs`). `burst_ratio` is first because CV < 0.15 is definitive and cannot be cheaply evaded. `referer_self_loop` is last because privacy tools legitimately strip referrers.

### 3. CubeDecisionGrid Rows 3-4 — `cube_oracle.rs`

**Location**: `primals/skunkBat/crates/skunky-ingest/src/cube_oracle.rs`

**Row 3 — Tense dimension**:

| Cell | Name | Range | Function |
|------|------|-------|----------|
| (3,0) | tense_gate | Is (50%) / Was (37.5%) / WillBe (12.5%) | Which temporal frame the response inhabits |
| (3,1) | tense_depth | 0-15 | How far into history (Was) or prediction horizon (WillBe) |
| (3,2) | tense_confidence | 0-15 | How certain the tense classification is (< 4 → fall back to Is) |
| (3,3) | tense_decay | 0-15 | How quickly temporal context expires across epochs |
| (3,4) | tense_invert | bool (12.5%) | Whether to present the opposite tense (disorienting) |

**Row 4 — Sort dimension**:

| Cell | Name | Range | Function |
|------|------|-------|----------|
| (4,0) | sort_level | Alphabetic (50%) / Epitope (31.25%) / Tense (18.75%) | Which sort dimension dominates this epoch |
| (4,1) | sort_grain | 0-15 | Granularity within the sort level |
| (4,2) | sort_compress | 0-15 | Entropy reduction from last pass (feedback signal) |
| (4,3) | sort_epoch | 0-15 | How often the sort level rotates |
| (4,4) | sort_feedback | 0-15 | How strongly compression result feeds back to nautilus |

**Enums added**:
- `TenseGate { Is, Was, WillBe }` — temporal frame for the scatter response
- `SortLevel { Alphabetic, Epitope, Tense }` — which sort dimension the maze applies

**Tests**: 6 new tests — tense gate reachability + distribution, sort level reachability + distribution, tense invert rarity, depth/grain range coverage.

**Integration point**: The scatter server path (`scatter_server.rs`) does not yet read rows 3-4. When it does, the pattern is:

```rust
let grid = oracle.decide(fleet_hash, path, epoch);
let tense = grid.tense_gate();
let sort = grid.sort_level();
// Use tense + sort to modulate response content
```

### 4. Dashboard Tense Distribution — `dashboard_writer.rs`

**Location**: `primals/skunkBat/crates/skunky-ingest/src/dashboard_writer.rs`

**New JSON fields in `dashboard.json`**:

```json
{
  "tense_distribution": { "is": 42, "was": 156, "will_be": 0 },
  "sort_compression": { "alpha": 7.3, "epitope": 3.8, "tense": 6.5 }
}
```

**Classification logic**:
- Is: `profile.requests == 1` (first-time IP)
- Was: `profile.requests > 1` (repeat visitor)
- WillBe: 0 (nautilus integration point)

**Sort compression calculation**:
- `alpha`: `log₂(total_ips)` — baseline positional entropy
- `epitope`: `alpha - log₂(unique_epitope_clusters)` — reduction from epitope grouping
- `tense`: `alpha - H(tense_distribution)` — reduction from is/was partition

**Tests**: 1 new test — `tense_distribution_in_dashboard` verifies Is/Was counts and sort_compression presence.

### 5. PetalTongue Panels — `detroit-pt.js`

**Location**: `infra/detroit/site/static/js/detroit-pt.js`

**Panels added**:
- **Panel 22**: Tense Distribution donut — Is (green) / Was (orange) / Will Be (purple). Currently derived from network graph tier structure (Tier 1-2 → Is, Tier 3-4 → Was, Tier 5 → WillBe). When the live dashboard.json endpoint is wired, it will read `tense_distribution` directly.
- **Panel 23**: Sort Compression bar chart — bits of compression at Alphabetic / Epitope / Tense levels. Computed from graph stats.

---

## What Remains

### Nautilus → WillBe (Wave 172+)

The `WillBe` tense variant is defined but never assigned. Wiring it requires:

1. **Prediction cache**: `HashMap<String, (EpitopeTense, f64)>` keyed by fleet hash, with TTL matching the epoch window (180s default). When `predict()` returns a hash before the request arrives, cache it as WillBe.

2. **Scatter serve integration**: `scatter_server.rs` reads `grid.tense_gate()` and `grid.sort_level()` to modulate response content. If `tense_gate() == WillBe && tense_confidence() >= 4`, the response includes information that implies the system predicted the fleet's arrival.

3. **Dashboard live update**: `dashboard_writer.flush()` counts WillBe from prediction cache hits, not from request counts.

### Sort Feedback Loop (Wave 172+)

The `sort_compress` and `sort_feedback` cells in row 4 are populated by the BingoCube hash but not yet read by any consumer. When wired:

```rust
// After serving a response at sort_level X:
let compression = h_pre_sort - h_post_sort;
oracle.observe(ScatterObservation {
    // ... existing fields ...
    response_type: match grid.sort_level() {
        SortLevel::Alphabetic => ResponseType::Normal,
        SortLevel::Epitope => ResponseType::CrossType,
        SortLevel::Tense => ResponseType::TemporalPhaseout,
    },
});
```

This creates the adaptive compression schedule: nautilus learns which sort dimensions are most informative per fleet and increases their frequency.

### EpitopeScores in Entity Profiles

The `epitope_sort_key()` and `compression_score()` methods are implemented but not yet emitted in the dashboard JSON. Adding them:

```rust
// In dashboard_writer.rs flush():
"epitope_sort_key": format!("{:?}", p.epitopes.epitope_sort_key()),
"compression_score": p.epitopes.compression_score(),
```

### Detroit Signal Page Live Tense Donut

The signal page at `detroit.primals.eco/signal/` has petalTongue panels (Wave 171b) but does not yet include the tense donut. When the WebSocket bridge carries `tense_distribution` from dashboard.json, add a panel:

```javascript
pt.renderBinding({
    channel_type: 'donut', id: 'live-tense',
    label: 'Live Tense Distribution',
    slices: [
        { label: 'Is', value: data.tense_distribution.is },
        { label: 'Was', value: data.tense_distribution.was },
        { label: 'Will Be', value: data.tense_distribution.will_be }
    ]
}, 'pt-live-tense');
```

---

## File Inventory

| File | Change | Tests |
|------|--------|-------|
| `skunky-ingest/src/journey_tracer.rs` | +EpitopeTense enum, +tense field on Journey, +chain_depths tracking, +by_tense in JourneyObservation | 14 total (3 new) |
| `skunky-ingest/src/entity_profile.rs` | +EPITOPE_SORT_ORDER const, +epitope_sort_key(), +compression_score() | 7 new |
| `skunky-ingest/src/cube_oracle.rs` | +TenseGate enum, +SortLevel enum, +row 3 accessors (5), +row 4 accessors (5) | 16 total (6 new) |
| `skunky-ingest/src/dashboard_writer.rs` | +tense_distribution JSON, +sort_compression JSON | 8 total (1 new) |
| `detroit/site/static/js/detroit-pt.js` | +panel 22 (tense donut), +panel 23 (sort compression bar) | — |
| `sporePrint/content/science/48_epitope_sort_compression.md` | New paper | — |
| `whitePaper/coGen/EPITOPE_SORT_COMPRESSION.md` | New coGen entry #14 | — |

**Test totals**: 309 tests pass across skunky-ingest (17 new tests added). 0 failures.

---

## Corollary: Numeric Base Is an Epitope Set (Wave 171, 9:30 PM)

Added to Paper 48 §6 and coGen #14 (amended).

### The Insight

A numeric base is a choice of epitope set. `palette_size = 16` means the BingoCube sorts every scalar into one of 16 groups. That modular reduction (`scalar % 16`) IS the epitope sort. The choice of 16 (hex) is not arbitrary — hex is the base whose epitope set makes byte boundaries visible, and BLAKE3 hashes are byte-oriented.

### Where It Was Wired

| File | Change |
|------|--------|
| `bingoCube/crates/core/src/lib.rs` | `palette_size` doc comment: "the numeric base of the epitope sort" |
| `skunky-ingest/src/cube_oracle.rs` | `palette_size: 16` comment: "Base-16: the epitope set for behavioral clustering" |
| `skunky-ingest/src/ribocipher_const.rs` | `CLEAR_JSONRPC` doc: hex makes protocol taxonomy visible (upper nybble = genus, lower = species) |
| `skunky-ingest/src/epitope_defs.rs` | `EPITOPE_NAMES` doc: detection priority ≠ information content, cross-ref to `EPITOPE_SORT_ORDER` |
| `sporePrint/content/science/48_epitope_sort_compression.md` | §6 — full corollary with compression inequality, BingoCube palette analysis, riboCipher alignment, generalization table |
| `whitePaper/coGen/EPITOPE_SORT_COMPRESSION.md` | Addendum — 9:30 PM section |

### The Three BingoCube Bases

| Config | palette_size | Base | Epitope granularity | Forgery resistance |
|--------|-------------|------|--------------------|--------------------|
| Standard | 16 | Base-16 (hex) | 16 groups, coarse | ~2^-50 |
| Extended | 64 | Base-64 | 64 groups, medium | ~2^-192 |
| Full | 256 | Base-256 (byte) | 256 groups, fine | ~2^-576 |

The maze is not just a sort order. It is a sort order at a chosen base.

---

*ecoPrimal · subGen · Wave 171 · October 9, 2026*
