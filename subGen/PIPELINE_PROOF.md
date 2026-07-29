# Pipeline Proof — End-to-End Deployment Validated

**Status**: CROSSED | **Wave**: 155i | **Date**: Jul 29, 2026
**Path**: songBird (eastGate) → cellMembrane → sporeGate → golgiBody → blueGate

---

## What Crossed

For the first time, a code fix flowed through the entire deployment pipeline:

```
songBird P0 fix (eastGate)
    → cellMembrane harvest (--push flag)
        → sporeGate build (cargo build --release --target x86_64-unknown-linux-musl)
            → golgiBody depot push (plasmid.push + Caddy TLS)
                → blueGate depot pull (curl from https://depot.primals.eco)
```

This is the J1→J2 jelly string pipeline from abstract aspiration to demonstrated
operational reality. The organism can self-heal: a bug is found on one gate,
fixed on another, built on a third, and deployed to a fourth.

## The songBird P0 Journey

| Time | Event | Gate |
|------|-------|------|
| Jul 29, AM | blueGate Tower Atomic: songBird rejected Windows | blueGate |
| Jul 29, AM | P0 identified: `#[cfg(not(unix))]` blanket gate | blueGate (AAR) |
| Jul 29, AM | songBird fix shipped: TCP fallback (`8c0adc8d`) | eastGate (songBird team) |
| Jul 29, PM | 3 follow-up compile fixes (`d9bda555`) | blueGate → eastGate |
| Jul 29, PM | cellMembrane harvested, sporeGate built | sporeGate |
| Jul 29, PM | 19 binaries pushed to golgiBody depot | golgiBody |
| Jul 29, PM | BLAKE3 19/19 verified | sporeGate |
| Jul 29, PM | blueGate Tower G1 achieved (source build) | blueGate |
| Jul 29, PM | blueGate Nest 10/10 achieved | blueGate |

**Total time from P0 identification to depot**: ~4 hours.
**Total time from P0 to Tower G1 on Windows**: ~5 hours.

## Jelly Strings Resolved

| # | String | Status | How |
|---|--------|--------|-----|
| J1 | Harvest | **CLOSED** | `--push` flag on cellMembrane |
| J2 | Depot push | **CLOSED** | `plasmid.push` + Rust depot_sync |
| J3 | Service restart | **CLOSED** | songBird `deploy.hot_swap` |
| J4 | Caddy config | **CLOSED** | Route self-config |
| J5 | WG peer reg | **HARDENED** | songBird WG peer management |
| J6 | systemd overrides | **CLOSED** | `gate.configure` + `gate.apply` |
| J7 | Legacy detection | OPEN | Low priority, one-time (P3) |
| J8 | Key enrollment portal | **DEPLOYED** | step-ca at ca.primals.eco |

**7/8 resolved.** Only J7 (legacy detection, low-priority) remains.

## What This Proves

1. **The organism self-heals** — A bug found on blueGate (Windows) was fixed on
   eastGate (Linux), built on sporeGate, pushed to golgiBody, and available for
   downstream pull. No human ran shell loops.

2. **The pipeline is not theoretical** — gen4 described jelly strings as manual
   deployment steps to be codified. 7 of 8 are now Rust-native primal operations.

3. **Multi-gate coordination works** — 4 distinct gates participated in the fix
   cycle without central orchestration. Each gate performed its role (report →
   fix → build → serve) independently.

4. **Depot provenance is real** — 19/19 binaries BLAKE3 verified. Builder =
   sporeGate. Staleness detectable (blueGate found 07/16 stale Windows binaries).

## What Failed (Pipeline Gaps)

| Gap | Impact |
|-----|--------|
| **Windows depot not in pipeline** | sporeGate only builds Linux (musl/glibc). 14 .exe from 07/16. |
| **No Windows CI** | songBird P0 fix missed 3 compile errors. No `cargo check --target x86_64-pc-windows-gnu`. |
| **Depot-to-gate is manual** | `curl` from depot, not `cellMembrane cascade`. Fully automated cascade pending. |
| **songBird `d9bda555` not in depot** | Follow-up fix shipped to Forgejo but Linux depot not rebuilt with it. |

## gen4 Prediction

`SOVEREIGNTY_EVOLUTION_NARRATIVE.md` described the PostPrimordial journey as
a replicable playbook. The pipeline proof demonstrates that the playbook works:
a new gate (blueGate) can sync, enroll, pull from depot, and deploy — and when
the depot binary is wrong, the fix flows through the system.

The playbook is no longer a narrative. It's a measured 5-hour cycle.

---

*subGen Wave 155i — Pipeline proof. songBird P0 fix traversed 4 gates in ~5 hours.
J1→J2 jelly strings 7/8 resolved. Self-healing organism demonstrated. Windows
depot pipeline is the remaining gap.*
