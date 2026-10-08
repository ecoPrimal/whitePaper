# biomeOS HUD — petalTongue Goes Live

**Wave 167 — October 8, 2026**
**Classification**: subGen architecture — shared observation surface + meta-tier primal deployment
**Status**: ACTIVE — petalTongue v1.7.0 serving hud.primals.eco on golgiBody

---

## Abstract

The ecoPrimal mesh now has a shared observation surface at `hud.primals.eco` (aliases: `biomeos.primals.eco`, `os.primals.eco`). This is the first live deployment of petalTongue — the Universal User Interface primal — in web mode on golgiBody. The HUD renders real-time fleet telemetry (epitope organisms, geographic subdivision, entity topology) and exposes petalTongue's API/SSE/WebSocket infrastructure for future primal wiring.

The HUD is Phase 1 of evolving from static JS dashboards toward full Rust primal UI. petalTongue's motor system (SAME DAVE efferent) and WASM rendering pipeline are now deployed and waiting for signals.

---

## Architecture

### Topology

```
              ┌─────────────────────────────────────────────┐
              │  Caddy TLS (golgiBody :443)                 │
              │                                             │
              │  hud / biomeos / os .primals.eco            │
              │    ├── /api/* /health /ws /viz → :8092      │
              │    ├── /ops/* → basicauth + file_server     │
              │    └── /* → static Zola HUD site            │
              │                                             │
              │  petaltongue-hud.service (:8092)            │
              │    └── petaltongue web --docroot HUD        │
              │                                             │
              │  membrane-petaltongue.service (:8090)       │
              │    └── petaltongue web --docroot sporePrint  │
              └─────────────────────────────────────────────┘
                         ▲                    ▲
                         │                    │
              signal.primals.eco       skunky-ingest
              (scatter endpoints)      (dashboard culture)
```

### Multi-Domain Aliasing (Scatter Intelligence)

Three domains point to the same service. Humans see the same HUD. Fleet sees different Host headers — each alias is a free behavioral fingerprint:

| Domain | Purpose |
|--------|---------|
| `hud.primals.eco` | Primary — operational name |
| `biomeos.primals.eco` | biomeOS branding — OS identity |
| `os.primals.eco` | Short alias — minimalist |

If a crawler hits `biomeos.primals.eco`, the Host header reveals which domain list the crawler is working from. This is the same technique as the 12 honeycomb scatter domains, extended to the observation layer. Free intelligence, zero cost.

### Layered Access

| Layer | Path | Auth | Content |
|-------|------|------|---------|
| Public | `/*` | None | Live dashboard — epitopes, geo, fleet, topology, billboard |
| API | `/api/*` | None | petalTongue JSON API — primals, ecosystem, status, SSE events |
| WebSocket | `/ws` | None | JSON-RPC bridge (future: motor commands from browser) |
| Operator | `/ops/*` | basicauth | Gate status, service health, WireGuard mesh, deploy state |

---

## What Was Built

### Phase 1: Static HUD (Zola + JS)

| Component | Size | Role |
|-----------|------|------|
| `hud-core.js` | 19KB | Standalone dashboard — polls signal.primals.eco for `dashboard.json` (8s) + `topology.json` (30s). Renders billboard, summary strip, epitope organisms, geo subdivision, offenders, subnets, targets, timing, entity topology, comparative fingerprints. |
| `hud-widget.js` | 9KB | Embeddable bottom bar for any primals.eco site. Self-contained (all styles inline). Shows RPS, fleet %, machine confidence, billboard, organisms, geo. Expands on click. |
| `hud.css` | 5.5KB | Dark theme consistent with signal/detroit/sporePrint. Information-dense dashboard layout. |

### Phase 2: petalTongue Deployment

| Item | Details |
|------|---------|
| Binary | `petaltongue` v1.7.0, 8.4MB, x86_64-unknown-linux-musl, static-pie linked |
| Features | `--no-default-features` (no egui, no TUI, no X11/Wayland — pure web server) |
| Service | `petaltongue-hud.service` — `petaltongue web --bind 127.0.0.1:8092 --docroot /opt/ecoPrimals/hud/site/public --spa --allowed-origins "*" --cache-ttl 30` |
| API endpoints | `/health`, `/api/status`, `/api/primals`, `/api/ecosystem`, `/api/events` (SSE), `/ws` (WebSocket JSON-RPC), `/viz/*` |
| DataService | Tutorial mode (biomeOS Neural API not running on golgiBody — expected) |

### Cross-Site Widget Wiring

The `hud-widget.js` script tag was added to `base.html` of every primals.eco Zola site:

- signal.primals.eco
- detroit.primals.eco
- thesis.primals.eco
- tuebor.primals.eco
- sporeprint.primals.eco

Each site now loads the HUD bottom bar from `hud.primals.eco/js/hud-widget.js`. The widget auto-disables on the HUD site itself (no double-mount).

### Operator Layer

A cron script (`/opt/membrane/ops-status.sh`) runs every minute on golgiBody and writes `/opt/ecoPrimals/hud/site/public/ops/ops-status.json`:

```json
{
  "services": [caddy-tls, skunky-ingest, hbbs-membrane, hbbr-membrane, forgejo],
  "wireguard": [5 WireGuard peers with endpoint, handshake age],
  "deploys": {sporePrint, detroit, signal, thesis, tuebor, hud — last deploy timestamps},
  "system": {load, memory, disk, uptime}
}
```

Protected by basicauth at `/ops/`.

---

## Biological Model

### petalTongue as Sensory Cortex

petalTongue implements the **SAME DAVE** model (Sensory Afferent / Motor Efferent). In biological terms:

| Biological | petalTongue |
|-----------|-------------|
| **Visual cortex** | Grammar-of-graphics scene compiler — translates data into visual representations |
| **Sensory afferent** | `visualization.render.*` IPC — receives data from other primals |
| **Motor efferent** | `motor.*` commands — pushes panel content, notifications, navigation |
| **Multi-modal processing** | Same data → egui desktop, ratatui TUI, axum web, headless SVG, WASM browser |
| **Cortical map** | Panel system — each domain (epitopes, geo, topology) maps to a panel region |

The HUD is the **external receptor surface** — the first point where the mesh's internal sensory processing becomes visible to human observers. Previously, this receptor was hand-wired JS polling JSON files. Now petalTongue itself is the receptor.

### Meta-Tier Atomic Model

petalTongue sits in the Meta tier alongside biomeOS and Squirrel:

```
Foundation Tier:  BearDog + Songbird + swarmVine (trust + network + gossip)
Compute Tier:     ToadStool (compute substrate)
Storage Tier:     NestGate + CoralReef (CAS + reef)
Meta Tier:        biomeOS + Squirrel + petalTongue (orchestration + AI + UI)
```

The Meta tier is the nervous system. biomeOS is the autonomic nervous system (orchestration), Squirrel is the cognitive cortex (AI/inference), petalTongue is the sensory-motor cortex (perception/action). The HUD deployment means the sensory-motor cortex now has an external surface.

---

## Evolution Path

### Unlocked by This Deployment

| Capability | Status | Next step |
|-----------|--------|-----------|
| **SSE push** | `/api/events` live, no events yet | Wire skunky-ingest → petalTongue motor → SSE |
| **WebSocket bridge** | `/ws` active | Browser → petalTongue JSON-RPC commands |
| **WASM rendering** | `petal-tongue-wasm` crate exists (593KB) | Replace `hud-core.js` with Rust-compiled rendering |
| **Motor IPC** | `motor.panel.update` handler exists | Push live epitope/geo/entity data as panel updates |
| **Composition mounts** | `PETALTONGUE_COMPOSITIONS` env var | Mount sub-apps at `/app/{name}/` |
| **Scene streaming** | `/ws/scene` for WebGL | Push grammar-compiled scenes to browser |

### Phase 3: Motor Wiring (Next)

```
skunky-ingest (Caddy log tail)
  → dashboard_writer.rs (dashboard.json)
    → motor IPC (petaltongue socket)
      → SSE push (/api/events)
        → browser real-time update (no polling)
```

This eliminates the 8-second polling interval. Data flows from Caddy access log → skunky-ingest → petalTongue → browser in real time.

### Phase 4: WASM Rendering

Replace `hud-core.js` (19KB hand-written JS) with `petal-tongue-wasm` (593KB Rust-compiled). The WASM module uses petalTongue's grammar-of-graphics engine — same rendering code that powers the desktop GUI, compiled to WebAssembly. This means:

- Epitope organism cards rendered by the scene compiler
- Geographic bars computed with proper visualization math
- Entity topology as a force-directed graph (egui_plot algebra, compiled to WebGL)
- All rendering code shared between desktop, TUI, and browser

### Phase 5: UI Atomic Composition

Deploy the full UI Atomic composition from `biomeOS/graphs/ui_atomic.toml`:

```
Tower Atomic (BearDog + Songbird) → UI Atomic (Squirrel + petalTongue)
```

Squirrel provides AI coordination (signal planning, inference routing). petalTongue renders. biomeOS orchestrates. The HUD becomes a live window into the mesh's cognitive state.

---

## Commits & Artifacts

### Files Created

| Path | Purpose |
|------|---------|
| `infra/hud/site/config.toml` | Zola site config |
| `infra/hud/site/content/_index.md` | Dashboard layout with widget mounting points |
| `infra/hud/site/templates/base.html` | Dark theme, no tracking |
| `infra/hud/site/templates/index.html` | Extends base |
| `infra/hud/site/static/css/hud.css` | Dashboard CSS |
| `infra/hud/site/static/js/hud-core.js` | Standalone dashboard rendering |
| `infra/hud/site/static/js/hud-widget.js` | Cross-site embeddable widget |
| `infra/hud/site/static/ops/index.html` | Operator dashboard |
| `infra/hud/site/templates/shortcodes/hud.html` | Shortcode for Zola sites |
| `infra/hud/site/templates/shortcodes/artisan_footer.html` | Artisan footer (copied from signal) |

### Files Modified

| Path | Change |
|------|--------|
| `infra/signal/site/templates/base.html` | Added `hud-widget.js` script tag |
| `infra/detroit/site/templates/base.html` | Added `hud-widget.js` script tag |
| `infra/thesis/site/templates/base.html` | Added `hud-widget.js` script tag |
| `infra/tuebor/site/templates/base.html` | Added `hud-widget.js` script tag |
| `infra/sporePrint/templates/base.html` | Added `hud-widget.js` script tag |
| `gardens/cellMembrane/crates/membrane-shadow/src/seo/mod.rs` | Added HUD to PUBLISH_SITES |

### golgiBody Artifacts

| Path | Purpose |
|------|---------|
| `/opt/membrane/petaltongue` | v1.7.0 binary (8.4MB musl) |
| `/opt/membrane/ops-status.sh` | Operator status JSON generator (cron) |
| `/etc/systemd/system/petaltongue-hud.service` | HUD service unit |
| `/opt/ecoPrimals/hud/site/public/` | Deployed HUD static site |
| `/etc/membrane/Caddyfile` | Updated: HUD vhost with split routing |

---

## Privacy Invariant

Unchanged across all surfaces:
- No cookies, no tracking pixels, no JS analytics
- No IP addresses stored or logged in receptor/signal systems
- No PII on any public surface
- Log-based analysis only, IPs stripped before dashboard aggregation
- petalTongue web mode: CORS enabled, no auth cookies, no session state

---

## Technical Notes

### Port Allocation (golgiBody)

| Port | Service | Purpose |
|------|---------|---------|
| 8090 | membrane-petaltongue | sporePrint web serving |
| 8091 | songBird | Discovery/mesh (already occupied) |
| 8092 | petaltongue-hud | HUD observation surface |

### Build Configuration

petalTongue headless web build: `cargo build --release --no-default-features --target x86_64-unknown-linux-musl`

- No egui/eframe (no X11/Wayland/OpenGL deps)
- No ratatui/crossterm (no terminal deps)
- axum web server always included (not feature-gated)
- 8.4MB static binary vs 19MB with full UI features

### DataService Fallback

petalTongue starts in "tutorial mode" when biomeOS Neural API is not available. The `/api/primals` and `/api/ecosystem` endpoints return empty data. This is correct for golgiBody where biomeOS is not deployed. The live data (epitopes, geo, fleet) flows through the static JS layer polling signal.primals.eco scatter endpoints.

As the NUCLEUS composition evolves, these endpoints will be populated by the Neural API mesh.

---

## Anderson Rendering Chain — Agent × petalTongue × BarraCuda

### The Loop

The agent (Cursor/Claude) connected to petalTongue's live WebSocket JSON-RPC bridge at `wss://hud.primals.eco/ws` and closed the full thesis-to-rendering pipeline:

```
Paper 43 (theory)          "Selective Permeability: The Orthogonal Anderson Dimension"
    ↓
BarraCuda (computation)    localization_length(), dimensional_localization_length(),
                           membrane_permeability(), membrane_profile()
    ↓
Agent (Python port)        Faithful port of BarraCuda's Rust formulas
    ↓
petalTongue (rendering)    DataBinding → GrammarCompiler → SvgCompiler / WebGlCompiler
    ↓
golgiBody (live)           wss://hud.primals.eco/ws → SVG + WebGL output
```

### WebSocket JSON-RPC Capabilities

8 methods exposed through the embedded platform runtime:

| Method | Response |
|--------|----------|
| `health.check` | `{"status":"ok","state":"Running"}` |
| `capabilities.list` | Lists all available methods |
| `pt.state` | Runtime state |
| `pt.metrics` | Real-time CPU, memory, core count from golgiBody |
| `pt.scenarios` | 8 built-in visualization scenarios (agriculture + measurement) |
| `pt.render_svg` | Scenario → SVG (scene compiler) |
| `pt.render_binding` | Custom DataBinding → SVG (grammar-of-graphics) |
| `pt.render_webgl` | Custom DataBinding → GPU draw calls (WebGL) |

### DataBinding Channel Types (verified live)

| Channel | Fields | SVG Output |
|---------|--------|------------|
| `timeseries` | x_values, y_values, x_label, y_label, unit | Line plot |
| `bar` | categories, values, unit | Bar chart |
| `gauge` | value, min, max, normal_range, warning_range, unit | Gauge meter |
| `heatmap` | x_labels, y_labels, values (row-major), unit | 2D matrix |
| `scatter` | x, y, unit | Scatter plot |

### Anderson Permeability — Computed and Rendered

Six biological systems from Paper 43, computed through BarraCuda's exact formulas, rendered through petalTongue's scene compiler:

| System | Modes | S (selectivity) | Meaning |
|--------|-------|-----------------|---------|
| Commensal Relay | 5 | **1.000** | Maximally selective — commensals pass, scanners blocked, nervous system impermeable |
| Gut Epithelium | 4 | **1.000** | Glucose passes, pathogens blocked |
| Healthy Skin (d=2) | 4 | **1.000** | Water vapor passes, cytokines contained, allergens blocked |
| AD Skin (d→3) | 4 | **0.000** | Barrier breach — everything passes, selectivity destroyed |
| Fleet (S=0) | 4 | **0.000** | Stomachs with no eyes — real code and scatter consumed identically |
| No-Till Soil | 4 | **0.743** | Selectively permeable — different QS autoinducers see different pore networks |

### Visualizations Generated

| Visualization | Type | Bytes | Physics |
|---|---|---|---|
| Permeability Tensor | Heatmap | 22,270 | 6 systems × 20 modes — which signals pass which membranes |
| Selectivity Comparison | Bar chart | 5,778 | S for each system |
| 6 Selectivity Gauges | Gauges | ~29,000 | One per system, normal/warning thresholds |
| AD Dimensional Promotion | TimeSeries | 5,680 | S(d_eff) from d=2→3 — the disease curve |
| Disorder Sweeps (d=1,2,3) | 3× TimeSeries | ~19,000 | P(W) — the metal-insulator transition |
| Anderson Localization | Heatmap | 14,052 | Built-in groundspring scenario |
| Phase Space Scatter | Scatter + WebGL | 7,322 + 52 draw calls | All modes in (W, P) space |

Total: 15 SVGs + 1 WebGL scene, ~103KB of visualization data, rendered in 1.1 seconds through the live WebSocket bridge.

### What This Proves

1. **petalTongue's scene compiler works headless** — no GPU, no display, pure SVG/WebGL compilation on a $6 VPS
2. **The agent can drive petalTongue** — WebSocket JSON-RPC is a universal control surface for any computational actor
3. **BarraCuda → petalTongue is a viable pipeline** — computation crate feeds rendering crate, both from the same ecosystem
4. **The thesis renders itself** — Paper 43's selective permeability theory, computed through the ecosystem's own physics engine, visualized through its own rendering engine, served from its own infrastructure

---

## Cross-Site Wiring — petalTongue Across the Ecosystem

### The Pattern

Following the Anderson rendering chain proof, petalTongue's server-side rendering was wired into **4 independent sites** (5 including sporePrint's existing WASM path). Each site has its own bridge JS following the same architecture:

```
[site]-pt.js (browser)
  ├── fetch() ──→ data source (local JSON or cross-origin signal)
  ├── transform() ──→ DataBinding (channel-typed)
  └── rpc('pt.render_binding') ──→ wss://hud.primals.eco/ws
                                     ↓
                                  petalTongue v1.7.0 GrammarCompiler → SvgCompiler
                                     ↓
                                  SVG → DOM injection
```

### Sites Wired

| Site | Bridge | Panels | Data | WS |
|------|--------|--------|------|-----|
| signal.primals.eco | `signal-pt.js` (15.2KB) | 10 | Local dashboard.json + topology.json | Cross-origin WSS |
| hud.primals.eco | `hud-pt.js` (10.8KB) | 10 | Cross-origin signal data | Same-origin WSS |
| detroit.primals.eco | `detroit-pt.js` (12.1KB) | 12 | `window.DETROIT_NETWORK` (91 nodes, 140 edges) | Cross-origin WSS |
| thesis.primals.eco | `thesis-pt.js` (8.1KB) | 8 | Cross-origin signal data | Cross-origin WSS |
| sporeprint.primals.eco | `viz-hydrate.js` (294 LOC) | WASM scenes | Scene JSON via `data-viz-src` | Client-side (no WS) |

**Total: 40 server-side panels + sporePrint WASM scenes, all rendered by the same Rust engine.**

### Detroit Panels (12)

Detroit's `DETROIT_NETWORK` global (1,167 LOC, generated from TOML registries) provides the richest graph data in the ecosystem. 12 petalTongue panels on the `/network/` page:

- **Structural**: Node types, flow types, communities, nexus coverage, tier structure, dynasties
- **Relational**: Degree distribution (scatter), geographic × flow type (heatmap)
- **Anderson**: Bench capture gauge (Anderson disorder — captured judges ÷ total)
- **Financial**: Ownership groups, money trail ($documented flows), oversight cycles

### Thesis Panels (8)

The live research paper ("Stomachs With No Eyes") had zero visualization until this wiring. Now 8 panels render fleet behavioral data live from signal.primals.eco:

- **Core findings**: Fleet vs human gauge, machine confidence (CV), honest vs deceptive bar
- **Fleet anatomy**: Entity volume, ASN infrastructure, epitope organisms, epitope feature matrix
- **Anderson**: Membrane selectivity gauge (S = 1.0)

### CSP Resolution

Thesis used `csp_static` (`connect-src 'self'` only) which blocked both cross-origin fetch to signal and WSS to hud. Updated golgiBody Caddyfile to allow `https://signal.primals.eco` + `wss://hud.primals.eco`.

### Not Wired (and Why)

| Site | Reason |
|------|--------|
| clutch.primals.eco | Repo is remote only (GitHub `amicusContra/clutch`), not cloned locally |
| barry/tuebor | No JSON data endpoints, pure static text — nothing to render |

### Incremental Path Forward

The bridge pattern is proven and scales. Next work is **per-section / per-type drilling**:

| Target | Panels to add |
|--------|---------------|
| Detroit → Anderson lattice page | Per-court capture gauges, localization length chart |
| Detroit → Timeline page | Timeline API → timeseries rendering |
| Detroit → Funding flow page | Money trail → Sankey-style bar progression |
| Signal → Per-epitope drilldown | One panel per organism — conserved feature comparison |
| Thesis → SSE live update | Replace 30s polling with SSE push from petalTongue |
| Clutch → Clone + wire | Investigation graph stats through petalTongue |
| sporePrint → Server-side option | Add WS CSP for server-side rendering alongside WASM |

### Deployment Handoff: `AAR_PETALTONGUE_CROSS_SITE_WIRING_WAVE167.md`

Full operational details, CSP map, file inventory, verification results, and lessons learned in the companion wateringHole AAR.

---

## Subsystem Wiring — Unlocking What Already Exists (Wave 167, Session 2)

### The Gap

`runtime.rs` line 182 called `self.compiler.compile()` instead of `self.compiler.compile_faceted()`. The faceting system — `compile_faceted()` in `facets.rs` — was fully implemented and tested (4 tests, handles `Wrap` and `Grid` layouts, partitions data by field) but the WS JSON-RPC binding path that all JS bridges use skipped it entirely. One-line fix, zero regression.

### New DataBinding Channel Types

| Channel Type | Geometry | Coordinate | Faceting | Use Case |
|---|---|---|---|---|
| `faceted_bar` | Bar | Cartesian | `FacetLayout::Wrap` | Per-organism epitope profiles, per-entity behavioral breakdowns |
| `faceted_gauge` | Arc | Cartesian | `FacetLayout::Wrap` | Per-entity timing CV gauges, per-court capture ratios |
| `donut` | Arc | **Polar** | None | Traffic composition, actor type distribution, community sizes |

Supporting structs: `FacetGroup` (key + categories + values) and `FacetGaugeEntry` (key + value + min/max + normal/warning ranges).

### Normalization Layer

Mixed-metric panels (IPs=199, UA Pool=12, Blame%=45 in one faceted bar) produced crushed visualizations. Added `Normalization` enum as a first-class compile-time transform:

```
Normalization::None        → raw values (default, backward compatible)
Normalization::MinMax      → [0, 1] per-column across groups
Normalization::Symmetric   → [-1, 1] centered
Normalization::ZScore      → (x - μ) / σ
Normalization::Log1p       → ln(1 + |x|) · sign(x)
Normalization::Rank        → ordinal percentile [0, 1]
Normalization::LeakyRelu   → max(α·x, x) for mixed-sign data
```

**Per-column independence**: Each category column (IPs, UA Pool, Blame%) is normalized independently across all groups. This preserves "Meta has more IPs than Anthropic" while making IPs and UA Pool visually comparable.

**Original value preservation**: Every data row carries `original_value` alongside the normalized rendering value. Labels display real numbers; geometry renders at normalized scale.

### Panel Consolidation

| Before | After | Effect |
|--------|-------|--------|
| 4 organism bars (IPs, UA, blame, lang) | 1 `faceted_bar` + 1 `donut` | Small multiples: each organism gets its own panel with all metrics |
| 4 entity bars (CV, chrome, blame, RPS) | 1 `faceted_gauge` + 1 `faceted_bar` | Each entity gets a timing gauge + behavioral bar group |
| 3 detroit bars (nodes, flows, communities) | 3 `donut` charts | Proportional distribution → polar arc segments |
| 1 detroit bar (per-court capture) | 1 `faceted_gauge` | Each court gets its own capture ratio gauge |

**Total**: 87 panels → 77 panels. Fewer panels carry more information per panel through faceting.

### Architecture After Wiring

```
JS Bridge (browser)
  ├── fetch data (local JSON or cross-origin)
  ├── classify organisms/entities
  ├── build DataBinding JSON with normalization field
  └── rpc('pt.render_binding', {binding, domain})
        ↓
petalTongue runtime (golgiBody)
  ├── deserialize DataBinding
  ├── DataBindingCompiler::compile()
  │     ├── per-column normalization (if Normalization ≠ None)
  │     ├── GrammarExpr with facet/polar/scale
  │     └── data rows with original_value
  ├── GrammarCompiler::compile_faceted()  ← THE FIX
  │     ├── partition data by facet variable
  │     ├── compile each group as sub-scene
  │     └── offset primitives per layout
  └── SvgCompiler → SVG string → WS response
```

### Known Debt (Post-Wiring, Pre-Reorganization)

| Item | Severity | Path Forward |
|------|----------|--------------|
| `normalization` field missing in UI/headless/graph test constructors | HIGH | ✅ Fixed in debt sweep |
| No SVG baseline tests for FacetedBar/FacetedGauge/Donut | HIGH | ✅ 4 tests added |
| ~80% JS duplication between signal-pt.js and hud-pt.js | MEDIUM | ✅ Extracted pt-bridge-core.js |
| Organism classification heuristic in 5+ JS files | MEDIUM | ✅ Centralized to classifyOrganism() |
| Thesis not yet migrated to faceted panels | MEDIUM | ✅ Migrated via shared build*() helpers |

---

## Bridge Re-ORGAN-ization

**Session**: October 8, 2026 (same day, second session)
**Goal**: Eliminate JS duplication, centralize organism heuristic, unify DOM IDs, migrate thesis to faceted panels

### The Extraction: pt-bridge-core.js

Created `infra/shared/js/pt-bridge-core.js` (251 lines) — single source of truth for all cross-site bridge infrastructure:

```
pt-bridge-core.js
  ├── PetalBridge(config)       — WS connect, JSON-RPC 2.0, status, SVG inject
  ├── classifyOrganism(cluster) — unified heuristic: Meta/Anthropic/Self/Unknown
  ├── buildOrganismProfile()    — faceted_bar: per-organism IPs, UA pool, blame%
  ├── buildEntityGauges()       — faceted_gauge: per-entity timing CV
  ├── buildEntityDetail()       — faceted_bar: per-entity chrome lag, blame%, RPS
  ├── buildEntityMatrix()       — heatmap: entities × 5 behavioral features
  └── buildAcceptLanguageDonut()— donut: human vs machine Accept-Language
```

Config is parameterized for per-site overrides:

| Config Key | signal | hud | detroit | thesis |
|-----------|--------|-----|---------|--------|
| `wsUrl` | cross-origin hud | same-origin | cross-origin hud | cross-origin hud |
| `domain` | `'signal'` | `'hud'` | `'detroit'` | `'thesis'` |
| `maxHeight` | 300px | 280px | 260px | 260px |
| `reconnectMs` | 5000 | 5000 | 8000 | 8000 |
| `metricsEl` | `'pt-metrics'` | `'pt-metrics'` | null | null |

### Line Count Before/After

| File | Before | After | Change |
|------|--------|-------|--------|
| signal-pt.js | 562 | 335 | −40% |
| hud-pt.js | 445 | 309 | −31% |
| detroit-pt.js | 422 | 376 | −11% |
| thesis-pt.js | 250 | 237 | +faceted |
| **pt-bridge-core.js** | — | **251** | new |
| **Total** | **1,679** | **1,508** | −10% total, **−100% duplication** |

### Organism Classification — Unified

The organism classification heuristic was duplicated in 5 files with 3 behavioral variants:
- Dashboard cards: strict isSelf (br,zstd check), labels "Meta (FB-BLOCK)"
- PT bridges: relaxed isSelf (has_lang + ips=1), labels "Meta"
- HUD widget: relaxed, compact labels

Unified to single `classifyOrganism()` in pt-bridge-core.js with the relaxed rule. All bridges use it via the shared `build*()` helpers.

### DOM ID Unification

All 4 bridges now use standardized short `pt-*` IDs. Signal and hud have **identical** ID sets. Thesis retains paper-specific panels (pt-fleet-ratio, pt-machine-conf). Detroit retains graph-specific panels (pt-node-types, pt-flow-types, etc.).

### Thesis Migration to Faceted Panels

thesis-pt.js gained 5 new panels via shared builders:
- Organism Profile (faceted_bar, min_max normalization)
- Entity Timing Gauges (faceted_gauge)
- Entity Behavioral Profile (faceted_bar)
- Entity Behavioral Matrix (heatmap, min_max)
- Accept-Language Donut

### Build + Deploy

All 4 sites rebuilt with Zola (zero errors), deployed via rsync to golgiBody. `pt-bridge-core.js` verified present in all 4 site's `public/js/` directories.

### Remaining Debt (Post-Reorganization)

| Item | Severity | Notes |
|------|----------|-------|
| Canonical shared/js/ vs per-site copies | MEDIUM | Manual copy; could use symlinks |
| CSS class naming differs per site | LOW | Intentional (different stylesheets) |
| hud-core.js (19KB) still hand-wired | LOW | Future: WASM replaces JS dashboard |
| signal-dashboard.js (19KB) still hand-wired | LOW | Gradually replaced by PT panels |

### Deployment Handoffs

- `AAR_PETALTONGUE_SUBSYSTEM_WIRING_NORMALIZATION_WAVE167.md` — subsystem wiring + normalization details
- `AAR_PETALTONGUE_REORGANIZATION_WAVE167.md` — bridge extraction + cleanup details
