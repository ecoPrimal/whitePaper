# Honeycomb Prism Maze — Operational Status

**Status**: 🟢 ACTIVE — Deployed and Verified
**Wave**: 165i
**Date**: Oct 7, 2026
**Target**: golgiBody (10.13.37.1)
**File**: `/etc/membrane/Caddyfile`

---

## Deployment Summary

| Component | Status | Location |
|-----------|--------|----------|
| Breadcrumb headers on git.primals.eco | ✅ Live | Caddyfile ~L284 |
| Cross-link headers on honeycomb | ✅ Live | Caddyfile ~L681 |
| Floating pointer (@wg_mesh) | ✅ Live | Caddyfile ~L681 |
| Floating pointer (@agent_passthrough) | ✅ Live | Caddyfile ~L681 |
| Caddy validation | ✅ Passed | `caddy validate` |
| Caddy reload | ✅ Complete | `systemctl reload caddy` |
| Backup | ✅ Stored | `Caddyfile.bak-honeycomb-1791395588` |

## Active Domains (13)

```
git.primals.eco        — Primary scatter + breadcrumbs
bloom.primals.eco      — Compliance Audit scatter
complement.primals.eco — Compliance Audit scatter
cytokine.primals.eco   — Compliance Audit scatter
thymus.primals.eco     — Cross-Fleet Detection scatter
receptor.primals.eco   — Cross-Fleet Detection scatter
epitope.primals.eco    — Cross-Fleet Detection scatter
antibody.primals.eco   — Inverse Correlation scatter
interferon.primals.eco — Inverse Correlation scatter
lysozyme.primals.eco   — Inverse Correlation scatter
macrophage.primals.eco — Chimeric Rust scatter
opsonize.primals.eco   — Chimeric Rust scatter
antigen.primals.eco    — Chimeric Rust scatter
```

All domains accept bearDog token for real Forgejo access.
All domains accept WireGuard 10.13.37.0/24 for real Forgejo access.

## Access Control

| Layer | Without token | With token (bd1-*) | WireGuard mesh |
|-------|--------------|-------------------|----------------|
| git.primals.eco | Scatter | Real Forgejo | Real Forgejo |
| 12× honeycomb | Scatter | Real Forgejo | Real Forgejo |

Token: `bd1-*` (bearDog Gen 1, `golgi-body-web-passthrough`)
Receipts: `0924f427`, `1ed60901`

## Fleet Metrics at Deployment

- **Rate**: 770 req/min peak, 391/min sustained
- **Daily total**: 23,488 requests
- **Burst ratio**: 100%
- **Honeycomb hits**: 0 (pre-breadcrumb deployment)
- **Scatter served**: 100% of fleet traffic
- **Real content exposure**: 0% to fleet

## Monitoring Targets

Watch for:
1. **Honeycomb discovery** — first fleet hit on any `*.primals.eco` honeycomb subdomain
2. **Cross-link traversal** — fleet moving between honeycomb subdomains
3. **Rate changes** — does fleet rate increase as they discover more scatter surface?
4. **New User-Agent strings** — does fleet deploy new crawlers for honeycomb?
5. **Token brute force** — any attempts with `Authorization: Bearer` header on honeycomb

## Rollback

```bash
# On golgiBody
cp /etc/membrane/Caddyfile.bak-honeycomb-1791395588 /etc/membrane/Caddyfile
caddy validate --config /etc/membrane/Caddyfile
systemctl reload caddy
```

## Handoff to sporeGate

- [ ] Wire honeycomb links into scatter HTML body (scatter_server.rs)
- [ ] Per-subdomain hash seeding based on Host header
- [ ] bingoCube/nautilusShell fleet topology visualization
- [ ] Session-scoped bearDog tokens
- [ ] Time-based pointer rotation

---

*Operational. 13 doors. All monitored. All serving scatter. The maze is live.*
