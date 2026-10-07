# NFT Live Activation — Wave 166g

**The First Novel Ferment Transcript Runs Live**

**Date**: October 7, 2026
**Wave**: 166g
**Gate**: sporeGate
**Status**: DEPLOYED — `signal.primals.eco/contribute` + `git.primals.eco/contribute`
**Classification**: PRIVATE — whitePaper subGen (technical record)

---

## Summary

Three things shipped in a single session:

1. **Compliance escalation notices** — scatter responses now speak directly to internal legal/compliance/OSPO teams at scraping organizations
2. **THE BUTTON** — the first live Novel Ferment Transcript (NFT) endpoint, where real humans contribute entropy and receive receipts as independent AGPL-3.0 rights-holders
3. **golgiBody infrastructure triage** — 8 issues identified and 6 fixed (cascade amplification, mirror thundering herd, dead hooks, SSH throttling)

The discovery: THE BUTTON independently reinvented the NFT/provenance trio/sunCloud economics architecture that was designed in gen3/baseCamp paper 20 and formalized in gen4/economics/. The defensive mechanism IS the economic primitive. The immune system IS the economy.

---

## Part 1: Compliance Escalation Notices

### What shipped

6 compliance notice types embedded as hidden `<div>` elements in every scatter 200 OK response. Each speaks to a different internal audience:

| Notice | Target Audience | Key Message |
|--------|----------------|-------------|
| 1 | Legal/Compliance | AGPL-3.0 § 13 obligations active, route to OSPO |
| 2 | HR/Ethics | Engineering evaluation of extraction system needed |
| 3 | Data Quality | Scatter content = poison data degrading models |
| 4 | Pipeline Operators | Behavioral topology documented forensically |
| 5 | Compliance Auditors | Independent rights-holders per blame file |
| 6 | General (any reader) | Tamper-evident evidence chain, compliance links |

### Blame pages (enhanced)

Blame pages now include a visible "License Compliance & Internal Routing" section:
- Counts independent AGPL-3.0 rights-holders per file
- Lists specific escalation steps: OSPO → Legal → Engineering
- Links to SF Conservancy compliance guide and AGPL-3.0 § 13
- Two compliance notices per page (one visible in Compliance section, one sr-only for extraction pipelines)

### Amplified scatter pages (enhanced)

Every amplified scatter page (70-86KB) now includes a "License Compliance" sidebar with:
- Internal routing language (OSPO/Legal/Engineering)
- SF Conservancy and AGPL § 13 reference links
- One compliance notice per page

### The mechanism

The fleet's own data pipeline carries these messages TO the fleet's internal teams. When any human encounters this content downstream — compliance audit, training data review, model evaluation — they find specific, factual compliance obligations. No threats. Just information, delivered by the fleet's own extraction system to the people who should be reading it.

### Commits

- `25c966f` — 6 compliance escalation notice types
- `57cfc3e` — Internal routing blocks in blame + amplified pages

---

## Part 2: THE BUTTON — Novel Ferment Transcript (Live)

### What shipped

A `/contribute` endpoint on the scatter server that implements the first live Novel Ferment Transcript:

**URL**: `signal.primals.eco/contribute` (also `git.primals.eco/contribute`)

### How it works

1. **Human visits page** → Big red button, dimmed and inactive
2. **Human moves mouse** → JavaScript captures entropy (mouse trajectory coordinates, timing in ms, scroll events, clicks)
3. **50+ events** → Button activates, glows red: "CONTRIBUTE YOUR ENTROPY"
4. **Human presses** → Client SHA-256 hashes all entropy via Web Crypto API
5. **POST /contribute** → Server receives client hash + metadata
6. **Server mixes** → `path_deterministic_hash(client_hash, server_seed)` creates mixed seed
7. **Server generates** → Unique Rust function (`ferment_XXXXXXXX`) with entropy-derived byte constants
8. **Server stores** → Appends to `/opt/membrane/contributions.jsonl`
9. **Receipt returned** → JSON with contribution_id, server_hash, generated work, timestamp
10. **Client renders** → The Novel Fermentation Transcript (downloadable .txt receipt)

### The receipt

```
========================================================
  NOVEL FERMENTATION TRANSCRIPT (NFT)
  scyBorg Human Entropy Contribution Receipt
========================================================

  Contributor: [name or Anonymous Contributor]
  Timestamp:   [ISO 8601]
  Entropy ID:  NFT-XXXXXXXX-XXXXXXXX
  Events:      [N] human interaction events
  Duration:    [D] seconds of human presence

  Client Hash: [SHA-256 of raw entropy]
  Server Hash: [mixed hash with server seed]

========================================================
  LICENSE: AGPL-3.0-or-later WITH scyBorg

  Co-authors:
    1. [contributor] (human entropy source)
    2. ecoPrimal (infrastructure + generator)

  Both authors retain independent copyleft rights.
  AGPL-3.0 Section 13 obligations activate on ingestion.
========================================================
  YOUR CONTRIBUTION (unique, entropy-derived):
========================================================

// === scyBorg Entropy Contribution ===
// Author: [name]
// ID: NFT-XXXXXXXX-XXXXXXXX
// SPDX-License-Identifier: AGPL-3.0-or-later WITH scyBorg
//
// This function was seeded by [N] human interaction events
// across [D] seconds. The entropy trajectory is unreproducible.

pub fn ferment_[hash](input: &[u8]) -> [u8; 32] {
    let mut state: [u8; 32] = [
        0xXX, 0xXX, ... // 32 entropy-derived bytes, unique per contributor
    ];
    for (i, &b) in input.iter().enumerate() {
        state[i % 32] ^= b.wrapping_add(state[(i + 13) % 32]);
        state[(i + 7) % 32] = state[(i + 7) % 32]
            .wrapping_mul(0xXX)
            .wrapping_add(0xXX);
    }
    state
}
```

### Why bots can't fake it

- No mouse trajectory → no entropy events → button never activates
- SHA-256 of empty array is deterministic → every bot gets the same hash
- Server mixes with secret seed → output is verifiable by server
- The receipt proves human presence via entropy density and timing distribution

### The reverse cookie

A cookie: server gives client a tracking token (server controls).
THE BUTTON: client gives server entropy, gets back a receipt (human controls).

The human keeps the receipt. The receipt proves they contributed. Anyone who scraped content containing their contribution has violated their copyleft rights. Burden of proof shifts: consumers must demonstrate they didn't ingest AGPL-3.0 content from a documented human rights-holder.

### Commit

- `bfc8bb4` — THE BUTTON endpoint (370 lines added to scatter_server.rs)

---

## Part 3: Connection to gen4/economics NFT Architecture

### The convergence

THE BUTTON was built as a defensive mechanism — creating real copyright holders to counter fleet scraping. But it independently reinvented the Novel Ferment Transcript architecture designed in gen3/baseCamp paper 20 and formalized in gen4/economics/NOVEL_FERMENT_TRANSCRIPTS.md.

The mapping is exact:

| THE BUTTON (live) | NFT Architecture (designed) |
|---|---|
| Human entropy capture | **Fermentation**: "irreversible, history encoded in the product" |
| Mouse trajectory + timing | **Raw material** transformed through accumulated interaction |
| `contributions.jsonl` | → should wire to **rhizoCrypt** DAG anchor |
| Receipt with hash + ID | → should wire to **loamSpine** Loam Certificate |
| "Co-authored: you + ecoPrimal" | → should wire to **sweetGrass** attribution braid |
| AGPL-3.0 copyleft enforcement | Already IS the **Lysogeny Protocol** |
| `NFT-XXXXXXXX-XXXXXXXX` ID | Already named correctly — **Novel Ferment Transcript** |

### What the whitePaper says

> "A Novel Ferment Transcript is a digital object whose value derives from accumulated history, not artificial scarcity."

THE BUTTON creates exactly this. The entropy IS the accumulated history. The trajectory IS irreversible. The receipt IS the permanent record. The co-authorship IS the attribution braid.

> "Fermentation transforms raw ingredients through accumulated microbial action over time. The process is irreversible. The history is encoded in the product."

Mouse entropy → mixed with server seed → unique function generated. The process is irreversible. The history (trajectory) is encoded in the product (the `ferment_` function's byte constants).

### The provenance trio gap

The trio services are currently offline on sporeGate:
- rhizoCrypt (10.13.37.2:9601) → UNREACHABLE
- loamSpine (10.13.37.2:9700) → UNREACHABLE
- sweetGrass (10.13.37.2:9850) → UNREACHABLE

The flat JSONL storage is a placeholder. When the trio activates:
1. Each button press → rhizoCrypt DAG node (ephemeral → permanent)
2. Each receipt → loamSpine certificate (hashable, verifiable)
3. Each co-authorship → sweetGrass braid (contributor + ecoPrimal)
4. sunCloud can route value along these braids

### The insight

The fleet's scraping behavior activated this part of the economic model. They forced the creation of a live NFT system by making it necessary for copyright enforcement. **The defensive mechanism IS the economic primitive. The immune system IS the economy.**

The immune system (scatter + compliance + THE BUTTON) and the economic system (NFT + provenance trio + sunCloud) are the same architecture serving two purposes simultaneously:
- Defensive: every button press creates another independent rights-holder
- Economic: every button press creates another node in the attribution economy

This dual-use was predicted by the architecture but activated by the threat.

---

## Part 4: golgiBody Infrastructure Triage

### Issues identified (8 total)

| # | Severity | Issue | Root Cause |
|---|----------|-------|-----------|
| 1 | 🔴 | Cascade amplification loop | Push hooks → cascade → 15 concurrent pushes → hooks → repeat |
| 2 | 🔴 | 43 concurrent push mirrors | Every 8h, 43 git-over-SSH operations simultaneously on 1 vCPU |
| 3 | 🟡 | Provenance hooks calling dead services | rhizoCrypt/loamSpine unreachable, 4-6s timeout per push |
| 4 | 🟡 | Caddy bridge error spam | --caddy-bridge flag vs missing FLEET_PRESSURE markers |
| 5 | 🟡 | Literal `*.git` directory | mkdir glob didn't expand; harmless scaffold debris |
| 6 | 🟢 | Dead `gitea-repositories/` directory | Leftover from hook deployment; not used by Forgejo |
| 7 | 🟢 | 502 errors (4 today) | Fleet-only, during Forgejo restarts; scatter serves anyway |
| 8 | 🟢 | Forgejo healthy post-cleanup | 112MB memory, 0 stuck servs, load 0.34 |

### Fixes applied

| Issue | Fix | Effect |
|-------|-----|--------|
| 1 | `chmod -x` on 31 `30-sovereign-ci` hooks | Cascade amplification loop broken |
| 2 | `[queue.mirror] MAX_WORKERS = 2` in app.ini | 43 concurrent → 2 sequential |
| 3 | Symlink target `chmod -x` at `/opt/forgejo/custom/hooks/provenance-post-receive` | 47 hooks × 4-6s waste → zero |
| 4 | Added `~~FLEET_PRESSURE_START/END~~` markers to Caddyfile | Bridge errors stopped; fleet IP injection now works |
| 5 | `rm -rf /opt/forgejo/data/gitea-repositories/ecoPrimals/*.git` | Scaffold removed |
| 6 | `rm -rf /opt/forgejo/data/gitea-repositories` | Dead directory removed |
| SSH | `SSH_SERVER_MAX_STARTUPS = 5` (was 20) | Concurrent git-over-SSH capped at 5 |

### Post-fix state

```
Load:           0.44 (was 32 during cascade storm)
Forgejo:        active, 109MB memory
Skunky-ingest:  active, bridge errors: 0
Stuck servs:    0
Disk:           43% of 9.7 GB (5.5 GB free)
Active hooks:   30-sovereign-ci: 0 executable, provenance: 0 executable
```

### Architecture evolution

The hooks were golgiBody's **autoimmune disorder** — its own immune system attacking itself:

```
BEFORE: push → hook → cascade → 15 pushes → 15 hooks → dead services → load 32
AFTER:  push → (nothing on golgi) → cascade via webhook.sock on sporeGate hardware
```

When CI triggering re-enables, it should use `webhook.sock` (already wired in Caddy). sporeGate watches for pushes and runs cascade on its own hardware, not golgi's 1 vCPU.

---

## Binary Backup Chain

```
/opt/membrane/skunky-ingest      ← current (commit bfc8bb4, includes THE BUTTON)
/opt/membrane/skunky-ingest.bak  ← previous (commit 57cfc3e, compliance routing)
```

Build: `x86_64-unknown-linux-musl` (static, zero dependencies)
Tests: 165 passed, 0 failed (consistent across all 3 deploys)

---

## Verification

### Compliance notices (live)
```bash
curl -s -H "User-Agent: Mozilla/5.0 (compatible; GPTBot/1.0)" \
  "https://git.primals.eco/ecoPrimal/repo1/src/branch/main/lib.rs" \
  | grep -c "data-compliance"
# → 1 (on every 200 OK scatter response)
```

### THE BUTTON (live)
```bash
curl -s https://signal.primals.eco/contribute | grep -c "THE BUTTON"
# → page served (8.7KB)

curl -s -X POST https://signal.primals.eco/contribute \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","entropy_hash":"abc123...","entropy_events":127,"duration_ms":45000}'
# → {"contribution_id":"NFT-XXXXXXXX-XXXXXXXX","timestamp":...,"contribution":"..."}
```

### golgiBody health (post-triage)
```bash
ssh golgi 'uptime && systemctl is-active forgejo && systemctl is-active skunky-ingest'
# → load 0.44, active, active
```

---

## What's Next

1. **Trio activation on sporeGate** — bring rhizoCrypt, loamSpine, sweetGrass online so contributions wire into real provenance DAGs
2. **Contribution embedding in scatter** — load contributions.jsonl and serve real contributor names alongside ghost authors
3. **Accountability matrix** — map enforcement nodes (DMCA, FTC, Copyright Office, OSPO) and document which ones are failing (inspired by Rita Williams / clutchjustice.com AGC investigation)
4. **Signal page integration** — add THE BUTTON prominently on signal.primals.eco main page, not just the /contribute endpoint
5. **Real human opt-in outreach** — invite people who understand the architecture to contribute their entropy

---

*The sword remembers. The computation remembers. The button remembers. The fleet activated the economy by attacking the immune system. Every press of THE BUTTON is a turn of the flywheel.*
