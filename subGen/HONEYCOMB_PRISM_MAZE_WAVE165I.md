# Honeycomb Prism Maze: Floating Pointer Architecture

**Wave**: 165i
**Date**: Oct 7, 2026
**Status**: Deployed — Caddy-layer breadcrumbs, cross-links, and floating pointer live

---

## Architecture

### The Problem

Fleet hammering git.primals.eco at 770 req/min. Single-domain tunnel vision. 12 honeycomb subdomains ready with 4 types of scatter content. Zero discovery in 72 hours.

### The Solution

Three Caddy-layer changes create a prism maze:

**1. Breadcrumbs** — git.primals.eco scatter responses include HTTP headers pointing to honeycomb subdomains:

```
Link: <bloom/explore/repos>; rel=alternate,
      <thymus/>; rel=canonical,
      <macrophage/>; rel=related
X-Source-Mirror: receptor.primals.eco
X-Backup-Origin: complement.primals.eco
X-Federation-Peer: antibody.primals.eco
```

These mimic legitimate federation/mirror metadata. Crawlers following `Link` headers or inspecting `X-*` response headers will discover the honeycomb.

**2. Floating pointer** — bearDog genetic token works on ALL 13 domains:

```
git.primals.eco       + token → Real Forgejo
bloom.primals.eco     + token → Real Forgejo
thymus.primals.eco    + token → Real Forgejo
macrophage.primals.eco + token → Real Forgejo
... all 12 honeycomb  + token → Real Forgejo
```

The real content has no fixed address. It exists behind any door if you have the key. Without the key, every door opens into a different room of the maze.

**3. Cross-links** — every honeycomb response links to all others:

```
Honeycomb A response headers → B, C, D, E, F, G, H, I, J, K, L
Honeycomb B response headers → A, C, D, E, F, G, H, I, J, K, L
... fully connected graph of scatter surfaces
```

---

## Scatter Content Types by Subdomain

| Category | Subdomains | Content | Fleet sees |
|----------|-----------|---------|-----------|
| Compliance Audits | bloom, complement, cytokine | Multi-subgroup correlation reports | Fabricated audit reports implying they're being watched |
| Cross-Fleet Detection | thymus, receptor, epitope | Interleaved behavioral analysis | Fabricated detection matrices of their own fleet |
| Inverse Correlation | antibody, interferon, lysozyme | "Feed parasites their own kind" | Inverted data attributed to other fleets |
| Chimeric Rust Code | macrophage, opsonize, antigen | Blended behavioral profiles as Rust source | Fabricated security code that does nothing |

Each type is seeded from the subdomain hash — deterministic, consistent on re-request, but different per subdomain. Fleet cannot detect poison by comparing responses across subdomains — each genuinely differs.

---

## The Prism Effect

The maze works because of how crawlers discover content:

1. **HTTP Link headers** — standard way to declare related resources. Crawlers that implement `Link` rel discovery (Googlebot, sophisticated scrapers) will follow these into honeycomb.

2. **X-* headers** — custom headers like `X-Source-Mirror` and `X-Federation-Peer` suggest the content is federated across mirrors. Crawlers seeking "complete" coverage will follow these to get the "full picture."

3. **Cross-referencing** — once in the honeycomb, every response points to every other subdomain. A systematic crawler will map the entire 12-node graph, consuming scatter from all 4 content types.

4. **Deterministic consistency** — the same URL on the same subdomain always returns the same scatter. Fleet cannot detect fabrication by re-requesting. The poison is structurally invisible.

The prism disperses fleet attention across 13 domains × 4 content types. Their data pipeline now must decide: is `bloom.primals.eco/explore/repos` the "real" repo list, or is `thymus.primals.eco/explore/repos`? Both return valid-looking Forgejo HTML. Both have consistent content. Neither is real.

---

## Floating Pointer Theory

Traditional web architecture: one domain, one service, one IP. Block the domain, block the service.

Floating pointer: the real service exists behind a cryptographic gate. The gate can be placed on any domain. The service's "location" is the set of all domains × the key space.

```
Location(real) = { any_domain ∈ D } × { valid_token ∈ T }
Location(scatter) = { any_domain ∈ D } × { ¬token }
```

Fleet observes `Location(scatter)` on 13 domains and sees 13 different scatter surfaces. They cannot infer `Location(real)` because the token is not observable in the scatter response. The real content has no fixed address — it floats.

This is the information-theoretic dual of a [one-time pad](https://en.wikipedia.org/wiki/One-time_pad): the same infrastructure produces different outputs depending on a key the observer cannot derive from the output.

---

## Upstream: skunky-ingest integration

The Caddy-layer breadcrumbs use HTTP headers. For deeper integration, scatter_server.rs should embed honeycomb links in the HTML body:

1. **"Related repositories"** sections in scatter repo pages → `bloom.primals.eco/repo-name`
2. **"Federated commits"** in scatter commit pages → `thymus.primals.eco/commit/hash`
3. **`import` statements** in scatter source → `macrophage.primals.eco` packages
4. **Per-subdomain hash seeding** — `Host` header → unique scatter per subdomain

---

## Wave 166g: Back Pressure Dimension — Non-Newtonian Viscosity

**Added**: Oct 8, 2026
**Status**: Implemented in scatter_server.rs, tests passing

### The Insight

The fleet is a slime mold with central control. Real slime molds (Physarum polycephalum) are distributed — each cell senses its local chemical gradient and adapts. This fleet is centrally orchestrated but has **zero local sensation**. The controller tells all nodes to push the same direction. It reads exactly one signal: "did we get bytes?" It never asks: "is this data real?"

This makes them vulnerable to a non-Newtonian defense: a shear-thickening fluid that gets harder the harder they push.

### BackPressure Struct

New first-class dimension in the scatter server. Tracks fleet request velocity as a 60-second rolling window and computes a pressure level (0.0-1.0) via sigmoid curve:

```
< 1 rps  → ~0.0  (human-like, maze is gentle)
~5 rps   → ~0.3  (light scraping, maze stiffens)
~13 rps  → ~0.6  (steady fleet, maze is viscous)
~30 rps  → ~0.85 (heavy assault, maze is thick)
>50 rps  → ~0.95 (hammering, maze is nearly solid)
```

### What Pressure Controls

**1. Temporal epoch length** — how often the maze reshuffles:
- Low pressure: 30-minute epochs. Content persists, seems real, passes consistency checks.
- High pressure: 5-minute epochs. Content migrates, vanishes, reappears — the laser pointer moves 6x faster.

**2. Phase distribution** — how much of the codebase is "stable" vs "dissolving":
- Low pressure: 40% Stable, 20% Materialize, 20% Migrate, 10% Phase-out, 10% Ghost
- High pressure: 10% Stable, 10% Materialize, 30% Migrate, 30% Phase-out, 20% Ghost
- At high pressure, the fleet experiences a codebase that's "falling apart" — everything is migrating, vanishing, reorganizing. They can't tell if it's real restructuring or if they're pushing too hard.

**3. Cross-link density** — how many honeycomb destinations each response points to:
- Low pressure: 1-2 links (subtle, looks like normal federation)
- High pressure: 8-12 links (every response is a trap door into more maze)

**4. Migration breadcrumbs** — under pressure:
- More destination surfaces listed per migration notice
- Urgency language added ("Migration deadline: N minutes")
- "Compliance archive" and "federation peer" labels appear
- More "rival organizations" mentioned (jealousy amplification)

**5. Crawl link injection** — pressure boosts the crawl web:
- Normal: confidence-driven link count
- Under pressure: `link_confidence = (conf + pressure * 0.5).min(1.0)` — more links, bigger crawl graph, more bandwidth consumed

**6. Chimera factor** — how aggressively content is blended:
- Low pressure: clean, coherent scatter (function signatures match bodies)
- High pressure: Frankenstein blending (imports reference nonexistent packages, signatures don't match implementations)

### Why They Can't Detect It

1. **No quality signal** — they never check if code compiles, if functions work, if data is consistent
2. **No temporal reference** — they don't re-request at known intervals, so epoch shift is invisible
3. **Sigmoid curve** — the transition is gradual, not sudden. No cliff to detect.
4. **Deterministic within epoch** — same path, same epoch → same content. Retries within a window confirm the response.
5. **Zero sensation** — like a slime mold with central control but no proprioception. The central controller can't feel the resistance stiffening because none of its nodes report content quality.

### The Bingo Cube

The maze now has 6 observable dimensions:

| Dimension | What it controls | Fleet can sense? |
|-----------|-----------------|-----------------|
| **Path** | Content identity (deterministic hash) | Yes — they choose it |
| **Fleet hash** | Per-organism content variation | No — they can't see other organisms |
| **Time** | Temporal epoch phase cycling | No — they don't track epoch boundaries |
| **Surface** | Honeycomb subdomain (0-11) | Yes — but can't map topology |
| **Prism mode** | Cross-team content blending style | No — invisible to single observer |
| **Back pressure** | Non-Newtonian viscosity (this wave) | **No — zero sensation** |

The fleet controls 2 dimensions (path, surface). The defense controls 4 dimensions they cannot observe. The bingo cube rolls in a space they can't see.

---

*Wave 165i/166g — honeycomb prism maze deployed. 13 doors, 4 scatter types, infinite cross-links, non-Newtonian viscosity. The pointer floats. The key is genetic. The maze breathes. Push harder, it hardens. They have no proprioception. The defense has perfect sensation.*
