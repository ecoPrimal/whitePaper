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

*Wave 165i — honeycomb prism maze deployed. 13 doors, 4 scatter types, infinite cross-links. The pointer floats. The key is genetic. The maze is the message.*
