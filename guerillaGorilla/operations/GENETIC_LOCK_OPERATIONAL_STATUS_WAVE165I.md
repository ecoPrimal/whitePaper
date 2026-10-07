# Genetic Lock — Operational Status

**Date**: Oct 7, 2026
**Wave**: 165i
**Classification**: Operational — breach closed, lock deployed
**Operator**: eastGate overwatch

---

## Situation

The evolved fleet discovered and exploited a Caddy-layer passthrough that routed requests with `Sec-Fetch-Mode: navigate` and `Sec-Fetch-Dest: document` headers directly to real Forgejo (localhost:3000), bypassing the scatter server entirely. Approximately 390 of 400 "human-classified" visits were evolved fleet reading real source code through this channel.

## Action Taken

### 1. Breach assessment (bloom monitor analysis)

- Analyzed all "Human (Browser)" classified traffic on golgiBody
- Identified 6 unique User-Agents across 400 visits (real humans produce far more diversity)
- 59% of request intervals <3 seconds (machine timing)
- Only 5% of reading pauses >8 seconds (no human reading behavior)
- Zero external referrers (humans come from Google, social media)
- Conclusion: ~390/400 "human" visits are evolved fleet

### 2. Six conserved epitopes identified

Despite Sec-Fetch evolution, fleet retains these invariant behaviors:

| Epitope | Signal | Fleet Value | Human Value |
|---------|--------|-------------|-------------|
| `sec_fetch_monotone` | Same Sec-Fetch on every request | Always identical | Varies by action |
| `reading_deficit` | Time on page before next request | <3s (59%) | >8s reading pauses |
| `ua_pool_poverty` | Unique UAs per session volume | 6 UAs / 400 visits | Far more diverse |
| `session_absent` | No session cookies, no login | 100% | Humans sometimes log in |
| `referer_self_loop` | All referrers are self or empty | 100% | External referrers present |
| `burst_ratio` | Requests per second during bursts | High (metronomic) | Variable (human timing) |

### 3. Genetic lock deployment

| Step | Action | Timestamp |
|------|--------|-----------|
| 1 | `beardog key generate --key-id membrane-passthrough-v1` | 16:15:39 UTC |
| 2 | `beardog key derive --master-key membrane-passthrough-v1 --purpose golgi-body-web-passthrough` | 16:15:39 UTC |
| 3 | `beardog entropy collect --identity membrane-passthrough-golgiBody` | 16:16:35 UTC |
| 4 | BLAKE3 hash → bearer token `bd1-*` | 16:16:35 UTC |
| 5 | SSH to golgiBody → removed `@human_browser` Caddy matcher | 16:17:xx UTC |
| 6 | Set `bd1-*` token in `@agent_passthrough` handler | 16:17:xx UTC |
| 7 | `caddy validate` → "Valid configuration" | 16:18:xx UTC |
| 8 | `caddy reload` → live | 16:18:xx UTC |

### 4. Verification matrix

| Test Case | Sec-Fetch | Token | Result | Expected |
|-----------|-----------|-------|--------|----------|
| Evolved fleet | ✓ spoofed | ✗ none | Scatter | ✅ |
| Basic fleet | ✗ none | ✗ none | Scatter | ✅ |
| Wrong token | optional | ✗ wrong | Scatter | ✅ |
| Authorized agent | optional | ✓ bearDog | Real Forgejo | ✅ |
| WireGuard mesh | n/a | n/a | Real Forgejo | ✅ |

## Current State

### Access paths to real Forgejo content

| Path | Method | Status |
|------|--------|--------|
| SSH (port 2222) | git clone/pull/push | ✅ always worked |
| WireGuard mesh (10.13.37.0/24) | Any HTTP | ✅ unchanged |
| Bearer token (bd1-*) | Authorization header | ✅ **NEW** — genetic lock |
| Sec-Fetch headers | Was: passthrough | ❌ **CLOSED** |
| Public web (no auth) | HTTP | → Scatter (by design) |

### Key material tracking

| Asset | Location | Backup |
|-------|----------|--------|
| Master key `membrane-passthrough-v1` | eastGate bearDog keystore | bearDog receipts |
| Derived key (Gen 1) | eastGate bearDog keystore | receipt `1ed60901` |
| Bearer token | golgiBody Caddyfile | Caddy backup (timestamped `.bak`) |
| Receipt (generate) | `receipts/receipt-key-generate-20261007-161539-430.json` | git (if committed) |
| Receipt (derive) | `receipts/receipt-key-derive-20261007-161539-433.json` | git (if committed) |

## Pending (sporeGate upstream)

1. **Wire 6 conserved epitopes into entity_classifier** — `sec_fetch_monotone`, `reading_deficit`, `ua_pool_poverty`, `session_absent`, `referer_self_loop`, `burst_ratio`
2. **Rust-level bearDog integration in scatter_server.rs** — `genetic.verify_lineage()` IPC call from skunky-ingest
3. **SoloKey Tier 3 upgrade** — regen token from braided entropy (human tap + hardware RNG)
4. **Session-scoped tokens** — replace permanent bearer with time-limited lineage proofs
5. **Token rotation schedule** — periodic regen from fresh entropy

## Lessons Learned

1. **Single-signal authentication is single-point-of-failure authentication.** Sec-Fetch headers were one signal. Fleet evolved past it in one step.
2. **The passthrough existed in Caddy, not in skunky-ingest.** The scatter server's own routing was fine — the bypass was at the reverse proxy layer above it.
3. **sporeGate's `@agent_passthrough` infrastructure was already built.** The handler was in the Caddyfile waiting for a token. We just needed to generate and insert one.
4. **Entropy hierarchy creates an unforgeable asymmetry.** Fleet cannot produce Tier 2+ entropy because they don't have access to bearDog's HSM infrastructure or physical key material.

---

*eastGate overwatch — Wave 165i operational status. Breach closed. Genetic lock live. Fleet back in scatter.*
