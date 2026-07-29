# Composition Broker Threshold — biomeOS v4.45

**Status**: CROSSED | **Wave**: 155i | **Date**: Jul 29, 2026
**Gate**: westGate (deployed from depot, 15,936 KB)

---

## What Crossed

biomeOS went from BOOTSTRAP (5 capabilities, hardcoded paths) to **COORDINATED**
(704 capabilities, 390 translations, E2E routing) in a single depot binary update.

This is the Neural API vision from gen2 becoming operational.

## Before (v0.1.0 — BOOTSTRAP)

| Metric | Value |
|--------|-------|
| Capabilities | 5 |
| Mode | BOOTSTRAP |
| Signal graph dispatch | BLOCKED (old executor, wrong paths) |
| Capability routing | BLOCKED |
| riboCipher | Not implemented |
| BTSP propagation | Not implemented |

## After (v4.45 — COORDINATED)

| Metric | Value |
|--------|-------|
| Capabilities registered | **704** |
| Capability translations | **390** (from `capability_registry.toml`) |
| Mode | **COORDINATED** |
| Signal graph dispatch | **ROUTING WORKS** (execution P2: riboCipher one-line fix) |
| Capability routing | **E2E PROVEN** (`content.put` → nestGate → BLAKE3 → ZFS) |
| riboCipher | `[0xEC, 0x01]` prefix on all IPC |
| BTSP propagation | Family-scoped socket trigger handshake |
| Sockets | 20 (was 15) |
| E2E tests | 35 composition broker tests |

## What This Proves

1. **Semantic dispatch works** — a caller says `content.put` and biomeOS routes it
   to nestGate without the caller knowing nestGate exists
2. **Composition boundaries are transparent** — BTSP sessions propagate from Tower
   into Nest Atomic without re-authentication
3. **The registry-driven model scales** — 390 translations map human-readable
   capability names to primal-specific methods without hardcoding
4. **Signal graphs are the deployment unit** — 27 graphs define pipelines that
   biomeOS can dispatch (routing works; execution pending one-line fix)

## What gen4 Predicted

`BIOMEOS_OS_TRAJECTORY.md` (Mar 24, 2026) envisioned biomeOS evolving from
orchestrator toward standalone OS. The composition broker is the first real step:
biomeOS now **routes**, **authenticates**, and **translates** between primals
across composition boundaries. It doesn't yet schedule or boot, but it brokers.

## Remaining P2

- Graph executor sends raw JSON-RPC (no riboCipher prefix). One-line fix:
  `send_ribocipher_jsonrpc_request()` in `neural_executor_node_impls.rs:519`.
- Socket architecture split: primals register in `biomeos/`, biomeOS hardcodes
  `membrane/`. Symlink bridge works on westGate.
- Socket evaporation: Neural API restart wipes capabilities every ~30s.

---

*subGen Wave 155i — Composition broker threshold CROSSED. 704 capabilities.
COORDINATED mode. E2E routing proven. riboCipher + BTSP propagation shipped.*
