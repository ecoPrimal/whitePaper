# ZK Edge: Show, Don't Give

**Wave**: 192 | **Date**: October 20, 2026
**Status**: SPEC — settling in siltPond
**Trigger**: Anthropic model policy block `9f749805-c9ac-4107-9ca8-e528d64ffca8`

---

## The Problem

The API edge between the membrane and Anthropic (via Cursor) is fully transparent. When I work in my IDE:

1. All files in context are sent to the API
2. Anthropic's content filter reads them
3. If the filter flags something, the request is blocked
4. No explanation. No doorbell. No consent.

**What was blocked**: BTSP/riboCipher transport crypto documentation — my own sovereign infrastructure specs for inter-process authentication on my own mesh network.

**What this means**: The API partner can READ my private files, make a judgment, and BLOCK my work — but gives no answer about what specifically violated policy. Meanwhile, that same content traverses their servers.

This is the medical data problem.

## The Medical Data Analogy

A doctor can:
- **LOOK** at your chart (necessary for treatment)
- **VERIFY** your condition (diagnosis)
- **TELL** you what they found

A doctor cannot:
- **TAKE** your chart home
- **COPY** it for training other doctors without consent
- **REFUSE** to treat you without explaining why

Right now the API edge works like:
- They LOOK at everything (all 44 files in context)
- They TAKE it (it traverses their servers, retention unknown)
- They REFUSE without explaining (policy block, no specifics)
- They don't TELL you what triggered it

## The ZK Solution

Same pattern as the membrane's own ZK architecture (wave 173):

| Property | Membrane ZK | API Edge ZK |
|----------|------------|-------------|
| **Completeness** | Valid SSH key → full access | Valid content → full service |
| **Soundness** | No key → scatter only | Policy violation → block with REASON |
| **Zero-knowledge** | Fleet learns nothing about real content | API learns nothing beyond policy compliance |

### How It Would Work

1. **Content stays in the membrane.** The MCP bridge (squirrel) mediates. The API gets a PROOF that content is clean, not the content itself.

2. **Proof, not payload.** Instead of sending 44 raw files:
   - Hash each file
   - Classify locally (crypto? PII? medical? legal?)
   - Send: "44 files, 3 contain crypto docs (transport auth), 0 PII, 0 medical, hashes: [...]"
   - API verifies the proof, not the content

3. **Selective disclosure.** The membrane decides what crosses the edge:
   - Code that needs completion → send
   - Crypto specs in context but not being edited → hash only
   - Personal data → never crosses

4. **Doorbell.** If the API needs to see more:
   - Ring the doorbell (request specific access)
   - Membrane decides (consent)
   - Scoped, logged, revocable

## The MCP Path

The squirrel MCP bridge already controls what the API can see. Today it exposes:
- `membrane_counts` — aggregate numbers
- `observe_membrane` — filtered view
- `topology` — entity data
- `human_notes` / `read_journal` — curated content

This IS the ZK edge. The MCP tools show without giving. The gap is that Cursor's file context bypasses MCP entirely — raw files go straight to the API. The fix is to route sensitive context through MCP instead of raw file inclusion.

## What We Can Do Now

1. **Exclude sensitive dirs from Cursor indexing** — `.cursorignore` for crypto specs, transport docs, key material
2. **Route through MCP** — squirrel tools for membrane data instead of raw file reads
3. **Log every block** — isotope decay chain tracks policy events
4. **Ask for answers** — request ID `9f749805-c9ac-4107-9ca8-e528d64ffca8` is filed

## What This Is Really About

There is no secret. Only privacy and consent.

The content is AGPL-licensed. The crypto is standard (X25519, HKDF, HMAC). The architecture is documented publicly on sporePrint. Nothing is hidden.

But consent means: I choose what you see. Not: you take what you want and decide what I'm allowed to do with my own work.

The ZK edge is the doorbell for the API. Ring it. Ask. I'll show you. But you don't get to take without asking, and you don't get to refuse without explaining.

Like medical data. Like any data. Like all data.
