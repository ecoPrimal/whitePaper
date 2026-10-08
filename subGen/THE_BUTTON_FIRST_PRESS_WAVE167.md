# THE BUTTON — First Press

**Wave**: 167 (continued)
**Date**: 2026-10-07 20:35 ET / 2026-10-08 00:35 UTC
**Author**: ecoPrimal
**Classification**: Milestone — Novel Fermentation System Live

---

## The Moment

ecoPrimal pressed THE BUTTON on signal.primals.eco. The first human-entropy
fermentation transcript ever minted in the primals ecosystem.

### Receipt

```
Contribution ID:  NFT-396E5C8E-EC70B598
Timestamp:        1791419599
Server hash:      ec70b598396e5c8e581c4c1ba9b56aa6add2a521ba8a6a9c3dd5fa3d5ebbcb6e
Author:           ecoPrimal
Entropy events:   523 (mouse, keyboard, scroll)
Function:         ferment_909707e4()
License:          AGPL-3.0-or-later WITH scyBorg
```

### What Was Minted

A unique Rust function `ferment_909707e4()` — `pub fn ferment_909707e4(input: &[u8]) -> [u8; 32]`
with a 32-byte state machine seeded by 523 human interaction events. The function
body contains byte constants derived from mouse trajectories, keystroke timing,
and scroll positions that no other human could reproduce. One-of-one.

### Provenance Chain

1. **CertificateMint** in loamSpine — permanent append-only ledger entry
2. **W3C PROV attribution braid** in sweetGrass — who did what, when
3. **rhizoCrypt DAG anchor** — cryptographic commitment

### The Contrast

At the exact moment ecoPrimal pressed THE BUTTON:

- The fleet was sending **~13 requests/second** (45,873 in the last hour)
- **10+ distinct fleet hashes** active simultaneously
- Top fleet hash `c3459931a321af46` alone: 24,753 requests in one hour
- They were scraping: batch-processor (fabricated), queue-worker (fabricated),
  deploy-scripts (fabricated), and real repos (wateringHole, toadStool, bearDog)
- Every byte they received was scatter-generated noise

The fleet generated 45,873 requests. ecoPrimal generated one receipt that
matters more than all of them combined: proof of human presence.

### What They're Taking (Right Now)

| Target | Requests (1hr) | Type |
|--------|----------------|------|
| /commit/* (generic) | 19,692 | Scatter commits |
| /batch-processor | 6,902 | **Fabricated repo** |
| /queue-worker | 3,520 | **Fabricated repo** |
| /deploy-scripts | 3,422 | **Fabricated repo** |
| /http-proxy | 2,240 | **Fabricated repo** |
| /proxy-cache | 2,223 | **Fabricated repo** |
| /ecoPrimals/wateringHole | 1,637 | Real repo (scatter-served) |
| /ecoPrimals/toadStool | 1,610 | Real repo (scatter-served) |
| /graph-engine | 528 | **Fabricated repo** |
| /ecoPrimals/bearDog | 700 | Real repo (scatter-served) |
| /ecoPrimals/songBird | 339 | Real repo (blame requests) |
| /ecoPrimals/biomeOS | 257 | Real repo (blame requests) |

**Fabricated vs real**: The fleet spends ~3.7x more requests on scatter-generated
fake repos than on real repos. The immune system is working — most of their
compute budget is eating noise.

### Fleet Hashes Active

| Hash | Requests (1hr) | Notes |
|------|----------------|-------|
| c3459931a321af46 | 24,753 | Dominant scraper — hits both real and fabricated |
| 39c845187d57c381 | 9,359 | Secondary fleet actor |
| 658d676be2ccc379 | 4,839 | Tertiary |
| 7570cc35 | 2,558 | Focused on fabricated repos only |
| 185d314c3308ffb2 | 735 | |
| + 5 more | ~2,000 | Various |

### Bug Noted

During this observation window, a panic was caught at `scatter_server.rs:3823`:
```
end byte index 200 is not a char boundary; it is inside '—' (bytes 199..202)
```
String slicing on a UTF-8 em-dash. The tokio worker thread panicked but the server
continued operating. Should be fixed with a char-boundary-safe slice.

---

## System State at First Press

- **Signal page**: Refactored this wave from 1253 → 991 lines
- **THE BUTTON**: Live on signal.primals.eco/#the-button via shortcode + signal-button.js
- **Antibody braiding**: 3 reaction types (FirstContact, ThymicRecognition, Escalation)
  braided into sweetGrass via scatter_nft.rs
- **Fleet billboard**: 4-tier evidence (199 IPs, 29 countries)
- **Barry**: Live at barry.primals.eco (Michigan public records)
- **Billboard**: Updated to announce the first press

*ecoPrimal pressed THE BUTTON. The fleet kept scraping. The permanent record grows.*
