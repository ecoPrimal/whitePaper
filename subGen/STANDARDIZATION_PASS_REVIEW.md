# Full Standardization Pass — Publish Pipeline, Caddy Deploy, SEO Surface

**Status**: Proven on live infrastructure  
**Wave**: 157  
**Date**: September 25, 2026  
**Scope**: sporeGate (local authority) + golgiBody (outer membrane)  
**Site under test**: https://detroit.primals.eco

---

## What Was Proven

Wave 157 completed a **Full Standardization Pass** on the webhook publish pipeline.
Three layers — artifact generation, Caddy vhost provisioning, and SEO notification —
were codified in membrane-shadow and validated against live detroit.primals.eco endpoints.

Before this pass, machine-readable artifacts drifted from HTML, Caddy vhosts were
hand-edited over SSH, and SEO surfaces were incomplete. After standardization, a
single git push triggers the full 6-step pipeline with consistency verification.

---

## What Was Standardized

### Track 1 — Publish Pipeline

| Aspect | Before | After |
|--------|--------|-------|
| Build tool | Webhook ran bare `zola build` | Step 2.5 invokes site-specific `artifact_command` |
| Artifacts | `site.json`, `llms.txt`, `graph.json`, `content-manifest.toml` updated only by manual local `detroit-build` + commit | Auto-generated on every publish |
| Consistency | No cross-check between sitemap and site.json | Step 5 flags extreme drift (>10× ratio) |
| Failure mode | N/A | Non-fatal — logs warning if build tool fails |

**Problem**: Webhook ran bare `zola build`, not `detroit-build`. Machine-readable
artifacts only updated when someone manually ran `detroit-build` locally and committed
to `site/static/`.

**Solution**:

- Added `publish_artifacts` module to membrane-shadow — invokes site-specific build
  tools as subprocesses
- Added `artifact_command` field to `PublishSite` registry; for detroit:
  `detroit-build --root .`
- Wire point: **Step 2.5** (post-zola, pre-evidence). Non-fatal — logs warning if
  build tool fails
- Added `verify_consistency` module — cross-checks sitemap URL count vs site.json
  page counts; flags extreme drift (>10× ratio). Runs as **Step 5** (final)

**Source**:

- [`gardens/cellMembrane/crates/membrane-shadow/src/webhook/publish_artifacts.rs`](../../../gardens/cellMembrane/crates/membrane-shadow/src/webhook/publish_artifacts.rs)
- [`gardens/cellMembrane/crates/membrane-shadow/src/webhook/verify_consistency.rs`](../../../gardens/cellMembrane/crates/membrane-shadow/src/webhook/verify_consistency.rs)

---

### Track 2 — Caddy Deploy

| Aspect | Before | After |
|--------|--------|-------|
| Vhost management | Hand-managed on golgiBody via SSH + manual sed | `generate_static_site_block()` from `PublishSite` fields |
| Evidence routes | Manual intervention | Template includes evidence depot handles when configured |
| Security headers | Inconsistent | HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy |
| Deploy command | Ad hoc SSH edits | `membrane caddy.deploy <site>` — block-replace, validate, reload, rollback on failure |
| Pre-publish check | None | `vhost_exists()` wired into pipeline Step 0 |

**Problem**: Static site vhosts (detroit, sporeprint) were hand-managed on golgiBody
via SSH + manual sed. Evidence routes, security headers, and landing pages required
manual intervention.

**Solution**:

- `generate_static_site_block()` template renderer produces complete Caddy vhost blocks
  from `PublishSite` fields
- Includes evidence routes (if configured), security headers, SEO handles, SPA fallback,
  404 handler
- `caddy.deploy` command: SSH to golgiBody, block-replace existing vhost (Python
  regex), validate + reload, rollback on failure
- `vhost_exists()` check wired into pipeline Step 0 (pre-publish idempotency)

**Source**: [`gardens/cellMembrane/crates/membrane-shadow/src/caddy/mod.rs`](../../../gardens/cellMembrane/crates/membrane-shadow/src/caddy/mod.rs)

**Tested**:

```bash
membrane caddy.deploy detroit --dry-run   # generates correct block
membrane caddy.deploy detroit             # replaces live Caddyfile block
```

All endpoints verified **200**.

---

### Track 3 — SEO Surface

| Gap | Fix |
|-----|-----|
| `braids.json`, `cas-manifest.json` served but not listed in llms.txt | `llms-editorial.md` updated with evidence depot section, provenance trio, machine-readable endpoint list |
| No `identity.json` for detroit | Created at `detroit/site/static/identity.json` — Schema.org `@graph` with WebSite, DataCatalog (evidence depot), SoftwareSourceCode, provenance endpoints |
| No Google Indexing API | `seo.url_notify` command — `urlNotifications:publish` with `URL_UPDATED` type; separate OAuth scope from GSC |
| Count drift (32 pages vs 120 sitemap URLs) | Documented; Step 5 consistency check flags extreme ratios |

**Problem**: braids.json and cas-manifest.json served but not listed in llms.txt. No
identity.json for detroit. No Google Indexing API. Count drift between site.json
(32 pages) and sitemap (120 URLs).

**Solutions**:

1. `identity.json` created at `detroit/site/static/identity.json` — Schema.org
   `@graph` with WebSite, DataCatalog (evidence depot), SoftwareSourceCode, provenance
   endpoints
2. `llms-editorial.md` updated with evidence depot section, provenance trio,
   machine-readable endpoint list
3. `seo.url_notify` command: Google Indexing API `urlNotifications:publish` with
   `URL_UPDATED` type. Separate OAuth scope from GSC. Wired as third channel in
   `notify_crawlers()` (IndexNow + GSC sitemap + URL Notify)

**Source**:

- [`gardens/cellMembrane/crates/membrane-shadow/src/seo/gsc.rs`](../../../gardens/cellMembrane/crates/membrane-shadow/src/seo/gsc.rs) (`url_notify` function)
- [`gardens/cellMembrane/crates/membrane-shadow/src/seo/mod.rs`](../../../gardens/cellMembrane/crates/membrane-shadow/src/seo/mod.rs) (dispatch + notify wiring)

---

## Pipeline Architecture (Proven)

The full pipeline order after standardization:

```
Step 0:   Caddy vhost check     — idempotent, warns if missing
Step 1:   Git fetch + reset     — worktree on golgiBody
Step 2:   Zola build            — generates HTML from content/
Step 2.5: Artifact generation   — detroit-build (graph, site-api, llms, manifest)
Step 3:   Evidence push         — SCP local evidence to golgiBody depot
Step 3b:  Evidence braid        — provenance trio (rhizoCrypt + loamSpine + sweetGrass)
Step 4:   SEO notify            — IndexNow + GSC sitemap + Google URL Notify
Step 5:   Verify consistency    — sitemap vs site.json cross-check
```

---

## Caddy Block Generation (Proven Pattern)

The generated Caddy block for a site with evidence:

```
{host} {
    root * {public_dir}
    encode gzip
    handle /sitemap.xml { file_server }
    handle /robots.txt { file_server }
    handle /evidence/ { try_files /evidence/index.html; file_server }
    handle /evidence/* { uri strip_prefix /evidence; root * {evidence_dir}; file_server browse }
    handle { try_files {path} {path}/index.html /index.html; file_server }
    handle_errors { @404 expression `{http.error.status_code} == 404`; rewrite @404 /404.html; file_server }
    header { HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy }
}
```

---

## SEO Triple Notification (Proven)

```
Channel 1: IndexNow    → Bing, DuckDuckGo, Yandex (POST sitemap URLs)
Channel 2: GSC Submit  → Google Search Console (POST sitemap location)
Channel 3: URL Notify  → Google Indexing API (POST each URL as URL_UPDATED)
```

---

## PublishSite Registry Pattern

Each site is a static entry with all publish-time fields:

```rust
PublishSite {
    repo_name: "detroit",
    host: "detroit.primals.eco",
    worktree: "/opt/ecoPrimals/detroit/worktree",
    public_dir: "/opt/ecoPrimals/detroit/public",
    build_subdir: Some("site"),
    seo: SiteConfig { host, sitemap, indexnow_key },
    evidence_dir: Some("/home/sporegate/Development/detroit/evidence"),
    artifact_command: Some(&["detroit-build", "--root", "."]),
}
```

---

## Verification Results (Sep 25, 2026)

| Endpoint | Status | Notes |
|----------|--------|-------|
| detroit.primals.eco/ | 200 | Main site |
| detroit.primals.eco/evidence/ | 200 | Zola HTML landing page |
| detroit.primals.eco/sitemap.xml | 200 | 120 URLs |
| detroit.primals.eco/robots.txt | 200 | |
| detroit.primals.eco/api/site.json | 200 | 32 pages, auto-generated |
| detroit.primals.eco/llms.txt | 200 | Template-expanded |
| detroit.primals.eco/graph.json | 200 | 43 nodes, 57 edges |
| detroit.primals.eco/identity.json | 200 | Schema.org structured data |
| Security headers | 5/5 | HSTS, nosniff, DENY, strict-origin, permissions-policy |

---

## Deployment

| Component | Version / Ref | Location |
|-----------|---------------|----------|
| `membrane` | `0.1.0 (5b2a8a4)` | sporeGate + golgiBody (immutable `chattr +i` on golgiBody) |
| `detroit-build` | `0.1.0` | sporeGate at `/usr/local/bin/detroit-build` |
| Git commit | `84f04b1` | Pushed to Forgejo `sporeGarden/cellMembrane.git` |

---

## What This Enables

1. **Any git push to detroit** now auto-generates all machine-readable artifacts
   alongside HTML
2. **New sites** can be provisioned with `membrane caddy.deploy <site>` instead of
   manual SSH
3. **Pipeline consistency** is verified automatically (sitemap vs site.json cross-check)
4. **SEO surface** is complete — 3 notification channels, structured data, provenance
   endpoints documented

---

## Cross-References

| Document | Path |
|----------|------|
| Publish pipeline spec (wateringHole) | [`../../wateringHole/specs/PUBLISH_PIPELINE_SPEC.md`](../../wateringHole/specs/PUBLISH_PIPELINE_SPEC.md) |
| Caddy deploy protocol (wateringHole) | [`../../wateringHole/protocols/CADDY_DEPLOY_PROTOCOL.md`](../../wateringHole/protocols/CADDY_DEPLOY_PROTOCOL.md) |
| Site architecture (detroit) | `detroit/specs/SITE_ARCHITECTURE.md` |
| Build pipeline (detroit) | `detroit/specs/BUILD_PIPELINE.md` |
| Evidence provenance (detroit) | `detroit/specs/EVIDENCE_PROVENANCE.md` |
| Validation spring (subGen) | [PUBLIC_RECORD_VALIDATION_SPRING.md](PUBLIC_RECORD_VALIDATION_SPRING.md) |

---

*subGen Wave 157 — standardization pass proven on live infrastructure.
sporeGate local authority + golgiBody outer membrane.
6-step publish pipeline. Caddy vhost generation.
SEO triple notification. Consistency verification.
detroit.primals.eco: 120 URLs, 32 content pages, 43 graph nodes, 57 edges, 5/5 security headers.*
