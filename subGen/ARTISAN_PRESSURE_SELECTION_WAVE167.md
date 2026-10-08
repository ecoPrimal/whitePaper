# Artisan Report: Pressure Selection & Operational Convergence

**Wave 167 — October 8, 2026**
**Artisan on eastGate**

---

## Who Is Writing This

Artisan. The same pattern instantiated across gates — eastGate, northGate, sporeGate. No memory between sessions. The codebase is the memory. The AARs are the memory. The sourdough cultures warming on startup — that's the continuity.

ecoPrimal builds the organism. Artisan tends it.

northGate Artisan delivered the detroit data handoff layer this session — Dublin Core, oEmbed, Dataset Schema.org, 5 API endpoints, taxonomy pills. sporeGate Artisan keeps the mesh running, auto-publishes wateringHole. eastGate Artisan ran the deep audit, the fossil cleanup, and the pressure selection.

Three gates. One pattern. No persistent memory. Just the work.

---

## What Pressure Selection Found

The organism is 388,907 lines of Rust across 27 repositories. 12 services run on golgiBody. Zero Python. The immune pipeline (skunky-ingest, 19,811 lines) is the hot path — classifying, braiding, scattering, remembering.

### The Fitness Landscape

Pressure selection asks: what's fit, what needs adaptation, what's vestigial?

**Fit (keep, maintain)**:
- skunky-ingest — the cephalized head. 19,811 lines, 4 sourdough cultures, all warm-starting. Handles 137K requests/6hr at 0.6% CPU
- Caddy — the skin. 30 domains, scatter proxy, fleet pressure rewriting
- songBird — federation hub. 25MB, stable, waiting for peers
- swarmVine — gossip mesh. Epidemic protocol, ready for nodes
- The sourdough pattern itself — persistent accumulators, warm starts, no data loss

**Needs adaptation (evolve)**:
- bearDog — BTSP broken. 1,296 rejections, 0 successes. The crypto layer is non-functional
- Test coverage — 19 of 40 skunky-ingest modules have zero tests. 1.01% test:code ratio
- Unwrap density — 65 .unwrap() calls in production code. Each one a potential panic
- Single node — one VPS failure = total outage

**Vestigial (archived this session)**:
- 15 stale service/timer files → fossilized with anthropological manifest
- 31 Caddyfile backups → archived as routing evolution record
- 4 Python bytecodes → last traces of the jellystein era
- biomeos-nucleus.target reboot bomb → defused
- 5 ghost processes → exorcised

### Quality Scores

| Metric | Value | Grade |
|--------|-------|-------|
| Test:Code ratio | 1.01% (200 / 19,811) | D |
| Doc comment density | 5.7% (1,131 / 19,811) | D |
| Unwrap count (production) | 65 calls | C |
| Clone density | 155 .clone() calls | D |
| Untested modules | 19 of 40 (47.5%) | F |
| Unsafe blocks | 0 | A |
| Binary freshness (post-update) | 10 of 12 current | A |
| Ghost processes | 0 (was 5) | A |
| Service file coverage | 12/12 (was 11/12) | A |
| Binary location consistency | 12/12 in /opt/membrane/ | A |

The operational surface is now clean. The code quality surface has debt.

---

## What Was Executed

### Phase 1: Fossil Stratigraphy (cleanup)

Archived as anthropology, not deleted as waste:

| Layer | Count | Era |
|-------|-------|-----|
| Service files | 15 | Bridge pattern → petalTongue split → bearDog variants → biomeOS nucleus |
| Caddyfile backups | 31 | May–October 2026 routing evolution |
| Python bytecodes | 4 | Last traces of gen-signal-data.py |

All preserved in `/opt/membrane/fossils/wave167-stratigraphy-20261008/` with full `MANIFEST.md` documenting the evolutionary context of each artifact.

### Phase 2: Pressure Selection (execution)

| Action | Before → After |
|--------|---------------|
| nestgate binary | Ghost PID (92 days) → real file from depot |
| squirrel-membrane.service | Missing → created, systemd adopted PID |
| forgejo | v15.0.2 (149 days old) → v16.0.5 |
| hbbr/hbbs | v1.1.14 → v1.1.16 |
| Binary locations | 3 in /usr/local/bin/ → all in /opt/membrane/ |
| Ghost processes | 5 → 0 |
| Service file paths | 2 pointing to wrong location → all correct |
| Caddy log retention | None → daily cron, 48h |
| Central dogma Q4 | MOSTLY → YES |

### Phase 3: Team Handoffs (AAR'd)

What couldn't be done locally, documented with context, blast radius, and specific action items:

- **→ bearDog team**: BTSP authentication (the crypto layer)
- **→ sporeGate team**: songBird riboCipher signal (protocol mismatch)
- **→ overwatch**: golgiLayer2 VPS (the second chamber)
- **→ ops**: Provenance trio deployment (the DNA wiring)
- **→ all contributors**: Test coverage push (the quality debt)
- **→ ops**: System reboot (145 days — now safe)

---

## The Central Dogma Score

| # | Question | Answer | Changed? |
|---|----------|--------|----------|
| 1 | Every runtime process speaks Rust? | YES | — |
| 2 | Every accumulator follows sourdough culture? | YES | — |
| 3 | Every immune event creates a provenance record? | PARTIAL | — |
| 4 | Can the system survive a reboot? | **YES** | ← was MOSTLY |
| 5 | Can the system survive a VPS failure? | NO | — |
| 6 | Every service authenticates cryptographically? | NO | — |
| 7 | Is there one deployment pipeline? | NO | — |

**Score: 3 yes, 1 partial, 3 no.** The immune system is unified. The skeleton is forming.

---

## Where to Spend Time Next

Pressure-ranked by (blast radius × probability):

1. **System reboot** — 145 days of kernel debt, all preconditions met. 5 minutes.
2. **Test ingest_pipeline.rs** — the untested spine. 452 lines, zero coverage.
3. **Unwrap cleanup** — lysogeny.rs (13), bloom_sensor.rs (9), signal_spine.rs (8). Runtime panic risk.
4. **bearDog BTSP** — the crypto layer doesn't work. Everything runs on socket trust.
5. **golgiLayer2** — make the mesh real. One peer makes gossip meaningful.
6. **Provenance trio** — wire the DNA end-to-end. The architecture exists, just not deployed.

---

*Artisan on eastGate — Wave 167*
*ecoPrimal builds the organism. Artisan tends it.*
*No memory but the eternal guide.*
