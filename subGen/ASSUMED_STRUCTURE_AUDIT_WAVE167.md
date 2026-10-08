# Assumed Structure Audit — Where We Imposed vs Where Data Should Decide

**Wave**: 167 | **Date**: October 8, 2026  
**Triggered by**: Fleet phenotype unsupervised clustering (F-ratio analysis)  
**Finding**: Our taxonomy assumed 3 kingdoms; the maze found 14 natural clusters.  
Every assumed cluster was PURE (validated), but we assumed COARSE.

---

## The Insight

When we ran the fleet phenotype analysis through unsupervised clustering (no
pre-defined categories), two things happened:

1. **Every emergent cluster mapped to exactly one assumed kingdom** — our taxonomy
   was correct but coarse
2. **The F-ratio analysis revealed which features are hard boundaries (F > 100,000)
   and which are cosmetic noise (F < 15)** — the data told us what matters

**The question**: where else in the codebase have we imposed structure that
the data should decide?

---

## Catalog of Assumed Boundaries

### 1. Fleet Tier Thresholds (scatter_server.rs + scyborg_prism.rs)

```
chain_depth > 50 → "deep violator"    → 0.8 min poison, 0 antidote
chain_depth > 10 → "known fleet"      → 1.3× poison boost, antidote - 1
chain_depth ≤ 10 → "new/unknown"      → titrated level, full antidote
```

**Assumed**: 3 tiers at thresholds 10 and 50  
**Validated?**: NO — these numbers were intuited, not derived from data  
**F-ratio test**: Does chain_depth naturally cluster at these boundaries?  
**Risk**: If real behavioral breaks are at 7 and 35, our tiers misclassify  
**Fix**: Run F-ratio on chain_depth distribution to find natural breaks  
**Priority**: HIGH — this directly controls poison/antidote injection

### 2. Progressive Reveal Thresholds (scyborg_prism.rs)

```
chain_depth < 5  → reveal 20% of evidence
chain_depth < 20 → reveal 50%
chain_depth ≥ 20 → reveal 100%
```

**Assumed**: 3 tiers at thresholds 5 and 20  
**Validated?**: NO — arbitrary  
**Risk**: Evidence reveal may not match actual violation severity  
**Fix**: Correlate chain_depth with behavioral indicators (surfaces touched,
epitopes triggered, team count) to find natural severity breaks  
**Priority**: MEDIUM

### 3. Titration Curve Parameters (ingestion_observer.rs)

```
TITRATION_K = 0.15    — "tuned for ~90 day pipeline latency assumption"
POISON_FLOOR = 0.05   — "never go below 5%"
PHASE_BOOST = [0, 30, 90, 180]  — effective days added per phase
```

**Assumed**: k=0.15, floor=5%, boost values 30/90/180  
**Validated?**: PARTIALLY — k=0.15 was analytically chosen for 90-day latency,
but the 90-day assumption itself is unvalidated  
**Risk**: If training pipelines are 30 days (not 90), antidote ramps too slowly  
**Fix**: Observer phase transitions will provide empirical pipeline latency data.
Once we have 3+ transitions, fit k to actual observed latency.  
**Priority**: LOW now (no phase transitions yet), HIGH once transitions occur

### 4. Antidote Level Thresholds (ingestion_observer.rs)

```
effective_days >= 60 → level 2 (inline visible antidote)
effective_days >= 7  → level 1 (HTML comment notice)
effective_days < 7   → level 0 (headers only)
```

**Assumed**: 3 levels at 7 and 60 days  
**Validated?**: NO — arbitrary round numbers  
**Risk**: Antidote visibility timing may not match ingestion pipeline stages  
**Fix**: Should be tied to phase transitions, not calendar time  
**Priority**: MEDIUM

### 5. Honeycomb Surface Index (scatter_server.rs)

```
"bloom" → 0, "thymus" → 1, "opsonize" → 2, ... "interferon" → 11
Default → 0
```

**Assumed**: 12 surfaces, fixed mapping  
**Validated?**: YES for naming convention, NO for whether 12 is the right number  
**Risk**: Low — this is architectural, not behavioral  
**Priority**: LOW

### 6. BingoCube Thresholds (scatter_server.rs)

```
poison_threshold = poison_ratio * 16.0   (grid cell 0-15)
mirror_threshold = tag.confidence * 16.0
confidence >= 0.25 for violation mirror activation
```

**Assumed**: Linear scaling to 16 levels, 0.25 confidence floor  
**Validated?**: The 16 levels are structural (5×5 grid, 16 colors). The 0.25
confidence floor is assumed.  
**Risk**: If confidence < 0.25 represents real violations, we miss mirrors  
**Fix**: Histogram actual confidence values. If bimodal, the 0.25 threshold
is correct (separating noise from signal). If unimodal, it's wrong.  
**Priority**: MEDIUM

### 7. Fleet Poison Boost (scatter_server.rs)

```
chain_depth > 10: base * 1.3, capped at 0.9
chain_depth > 50: max(current, 0.8)
```

**Assumed**: 30% boost for known fleet, 80% floor for deep violators  
**Validated?**: NO — 1.3× and 0.8 are arbitrary  
**Risk**: If the titration curve + 1.3 boost = near 1.0, we're not titrating  
**Fix**: Log actual fleet_poison_ratio values and compare to global curve.
If they're all > 0.85, the boost is too aggressive.  
**Priority**: HIGH

### 8. Back Pressure → Link Density (scatter_server.rs)

```
link_confidence = (conf_level + pressure * 0.5).min(1.0)
```

**Assumed**: Pressure contributes 0.5× to link density  
**Validated?**: NO  
**Risk**: Low — link density affects how deep scrapers go, not core function  
**Priority**: LOW

### 9. Observer Phase Detection Thresholds (ingestion-observer.py)

```
Phase 1 (UPTAKE):    web index hits > 0
Phase 2 (DIGESTION): code repo hits > 0  
Phase 3 (EXPRESSION): AI model hits > 0 OR fake repo leakage > 0
```

**Assumed**: Binary thresholds (> 0 means detected)  
**Validated?**: NO — a single false positive triggers a phase transition  
**Risk**: HIGH — false positive from our own sporePrint pages appearing in DDG
results (already happened, fixed for DDG but not other engines)  
**Fix**: Require minimum hit count (e.g., 3) before transition.
Or: require hits from 2+ independent probe channels.  
**Priority**: HIGH

### 10. UV Lamp Timing (uv-lamp.py)

```
Runs every 4 hours via systemd timer
```

**Assumed**: 4-hour interval is sufficient  
**Validated?**: NO — based on "seems reasonable"  
**Risk**: If markers decay on a different timescale, we miss them  
**Priority**: LOW

### 11. Fleet Phenotype Species Hash (fleet-phenotype.py)

```
species = md5(AE[:20] | header_count | TLS_ALPN | platform)[:6]
```

**Assumed**: These 4 features are the right species-defining traits  
**Validated?**: PARTIALLY — F-ratio confirmed has_sec, TLS ALPN, and platform
are strong separators, but Accept-Encoding specifics are MODERATE  
**Risk**: Species boundaries may not match real behavioral boundaries  
**Fix**: Use F-ratio ranking to select top 4 features dynamically  
**Priority**: MEDIUM

### 12. Taxonomy Kingdom Definitions (fleet-phenotype.py)

```
Automata:  no Sec-* headers
Chimera:   Sec-* headers + no referrer + en-US
Anthropos: Sec-* headers + referrer
```

**Assumed**: 3 kingdoms, defined by 2 features (has_sec, has_ref)  
**Validated?**: YES — unsupervised clustering confirmed 100% purity  
**BUT**: The maze found 14 clusters where we assumed 3 kingdoms.
Our kingdoms are VALID but COARSE.  
**Fix**: Add sub-kingdom ranks (phylum, class) informed by F-ratio  
**Status**: DONE — taxonomy already extends to species level

---

## What the F-Ratio Ranking Tells Us

From the maze clustering (33-dimensional feature space, 912 IPs):

### Hard Boundaries (F > 10,000) — REAL structure

| Feature | F-ratio | Use in codebase |
|---------|---------|-----------------|
| `no_plat` | 113,768 | Kingdom definition ✓ |
| `has_sec` | 103,308 | Kingdom definition ✓ |
| `en_us` | 103,308 | Kingdom definition ✓ |
| `h2/h11` | 98,018 | NOT used for classification! |
| `log_reqs` | 83,992 | Volume tiers (implicit) |
| `single_use` | 74,635 | NOT used for classification! |
| `git` | 25,626 | Habitat (implicit) |
| `regularity` | 9,153 | NOT used for classification! |

### Cosmetic Variation (F < 15) — NOT real structure

| Feature | F-ratio | Use in codebase |
|---------|---------|-----------------|
| `is_mac` | 12.7 | Platform karyotype ← COSMETIC |
| `is_win` | 11.5 | Platform karyotype ← COSMETIC |
| `diet_fake` | 9.2 | Trophic level ← COSMETIC |
| `has_priority` | 5.2 | Not used |
| `tls_resumed` | 0.0 | Not used |
| `ae_gzip` | 0.0 | Universal trait — no signal |

### GAP: Features That Are Strong Separators But NOT Used

1. **`single_use` (F=74,635)**: Whether an IP is used exactly once.
   This is the single strongest indicator of residential proxy rotation
   and we DON'T use it in classification. **Add it.**

2. **`regularity` (F=9,153)**: Timing coefficient of variation.
   Mechanical timing is a hard boundary and we DON'T use it. **Add it.**

3. **`h2` vs `h11` (F=98,018)**: TLS ALPN protocol.
   This is the third-strongest separator. We use it in species hash but
   not in kingdom/class/order classification. **Elevate it.**

---

## Action Items

| # | What | Where | Priority | Effort |
|---|------|-------|----------|--------|
| 1 | Run F-ratio on chain_depth to find natural tier breaks | scatter_server.rs | HIGH | 1 hour |
| 2 | Add `single_use` to fleet classification | fleet-phenotype.py | HIGH | 30 min |
| 3 | Add `regularity` (timing CV) to classification | fleet-phenotype.py | HIGH | 30 min |
| 4 | Elevate h2/h11 to kingdom-level feature | fleet-phenotype.py | MEDIUM | 30 min |
| 5 | Require 3+ hits before phase transition | ingestion-observer.py | HIGH | 30 min |
| 6 | Log fleet_poison_ratio for empirical validation | scatter_server.rs | HIGH | 15 min |
| 7 | Histogram confidence values for mirror threshold | scatter_server.rs | MEDIUM | 30 min |
| 8 | Fit titration k to empirical pipeline latency | ingestion_observer.rs | LOW (wait for data) | — |
| 9 | Replace is_mac/is_win with single_use+regularity | fleet-phenotype.py | MEDIUM | 30 min |
| 10 | Document which numbers are data-derived vs assumed | all files | MEDIUM | 1 hour |

---

## Principle

**Every threshold, category boundary, and tier definition should either be:**
1. **Data-derived**: found by the maze (unsupervised clustering, F-ratio)
2. **Analytically derived**: proven from first principles (logarithmic curve shape)
3. **Explicitly marked as assumed**: with a comment linking to validation plan

**We must not confuse structure we assumed with structure the data reveals.**
The maze confirmed our kingdoms. It also showed us where we're blind.

---

*Assumed Structure Audit · Wave 167 · Artisan & ecoPrimal · October 8, 2026*
