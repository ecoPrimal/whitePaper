# Codebase Audit — 1000-Line Cap Enforcement

**Wave**: 167 (continued)
**Date**: 2026-10-08 00:50 UTC
**Classification**: Architecture — File Size Governance

---

## Findings

**52 actionable files** exceed 1000 lines (fossils and changelogs excluded).
Total: ~75,000 lines across these files.

### By Category

| Category | Files | Total Lines | Action |
|----------|-------|-------------|--------|
| Rust code | 11 | ~17,500 | Split into modules |
| Spec docs | 21 | ~25,000 | Consolidate, wire to code |
| Config/manifest | 9 | ~16,200 | Dedup, auto-generate |
| Site code (JS/HTML) | 3 | ~3,500 | Extract inline, modularize |
| Research/whitepaper | 9 | ~12,000 | Archive — no action |
| Scripts | 2 | ~2,700 | Extract shared library |

### Critical (over 2000 lines, active code)

1. **scatter_server.rs** — 5051 lines. The big one. Already planned:
   split into scatter_compliance, scatter_content, scatter_http,
   scatter_honeycomb, keeping core routing at ~1000.

2. **experiment_dispatch.rs** — 2176 lines. cellMembrane shadow dispatch.
   Extract types, result handlers, test scaffolding.

### High Priority (1000-1500 lines, active code)

3. alphafold_dispatch.rs (1403), receptor.rs (1315), fleet.rs (1151),
   caddy_bridge.rs (1149), network_data.rs (1126), dispatch/tests.rs (1064),
   threats_tests.rs (1003)

4. network-graph.js (1226), network-data.js (1166) — detroit JS
5. petalTongue/web/index.html (1097) — same inline pattern as signal

### Medium: Spec Consolidation Needed

- loamSpine has 3 overlapping specs (DATA_MODEL + CERTIFICATE_LAYER +
  LOAMSPINE_SPECIFICATION = 3658 lines). Consolidate.
- rhizoCrypt has 3 overlapping specs (SPECIFICATION + DATA_MODEL +
  SLICE_SEMANTICS = 3427 lines). Consolidate.
- biomeOS + primalSpring share identical capability_registry.toml
  (2796 lines combined). One source of truth.
- sporePrint content-manifest.toml exists twice (5937 lines). Auto-generate.

## Refactor Priority Queue

1. scatter_server.rs (critical, 5051) → 5 modules
2. experiment_dispatch.rs (critical, 2176) → 3 modules
3. caddy_bridge.rs (high, 1149) → 3 modules
4. detroit JS (high, 2392) → modularize + auto-generate data
5. petalTongue index.html (high, 1097) → extract inline
6. receptor.rs + fleet.rs (high, 2466) → sub-modules
7. Spec consolidation (medium, ~7000 across overlapping specs)
8. Config dedup (medium, ~8700 across duplicated configs)
9. sporePrint auto-gen (medium, 5937 duplicate manifest)

## Already Completed This Wave

- signal/_index.md: 1253 → 986 lines (shortcodes, external JS)
- scatter_server.rs: UTF-8 panic fix (but file still 5051 lines)

## Canvas

Interactive audit catalog generated at:
`canvases/codebase-audit-1000.canvas.tsx`
