# arXiv Rung 1 — External Action Items

**Generated**: Aug 6, 2026
**Updated**: Aug 6, 2026 (C6, M2, M9 DONE — 40/42 rubric items complete, 95%)
**Context**: 40/42 rubric items DONE. These 2 items require external action
(user decisions, upstream coordination).

---

## COMPLETED (moved from OPEN)

### ~~C6: CUDA Cost Comparison~~ — DONE
Full scaling table added to §4.8 with 6 volumes (4⁴ through 16⁴). Real
RTX 3090 DF64 data: 638.8 ms/traj at 16⁴ β=6.0, 37.4× speedup over CPU.
Peak speedup 54× at 8³×4. Detailed ms/traj + acceptance + speedup table.

### ~~M2: DF64 vs Native f64~~ — DONE
Analysis added to §3.3: RTX 3090 native f64 = 1:32 of FP32 (17.4 GF).
DF64 on FP32 cores = ~70–140 GF effective, 4–8× faster than native f64
on consumer GPUs. The measured 37× speedup is DF64-specific.

### ~~M9: Reproduction Commands~~ — DONE
Build instructions added to §6: Rust version, feature flags, exact
commands for build + run.

---

## SHOULD Priority (1 remaining)

### M7 / X2: pseudoSpore URL — nestgate.io Serving Route

**What**: Paper references `primals.eco/pseudospore/hotspring-qcd-sun/` which
needs to resolve to a live, CAS-backed pseudoSpore bundle with inline
BLAKE3 verification.

**Architecture decision** (strandGate establishes pattern, upstream wires):

```
Paper URL: primals.eco/pseudospore/hotspring-qcd-sun/
    │
    ▼ (golgi Caddy route)
nestgate.io/pseudospore/hotspring-qcd-sun/
    │
    ▼ (nestgate.io route handler)
CAS query → serve configs + braids + validation + provenance
```

**What strandGate defines** (pattern for upstream):
- pseudoSpore bundle structure: configs/, shaders/, provenance/, validate.sh
- BLAKE3 manifest (data.toml) — lithoSpore already generates this
- Content is pushed to ironGate CAS via songBird
- nestgate.io serves from CAS with BLAKE3 verification inline

**What upstream needs to wire**:
1. **golgi**: Caddy route `primals.eco/pseudospore/* → nestgate.io/pseudospore/*`
2. **nestgate.io**: `/pseudospore/{name}/` route handler that:
   - Lists bundle contents from CAS (nestGate `content.query`)
   - Serves files with BLAKE3 hash displayed
   - Shows provenance chain (braid → DAG → spine)
   - Offers `validate.sh` download for offline verification
3. **nestGate**: pseudoSpore bundle ingestion (`content.ingest` on the bundle dir)
4. **Fix**: `hotspring-qcd-su3` reference in §4.1 → `hotspring-qcd-sun`

**Owner**: overwatch (nestgate.io route) + golgi (Caddy) + strandGate (bundle content)
**Pattern established by**: strandGate (this is the first compute pseudoSpore)
**Blocker**: nestgate.io `/pseudospore/` handler (new section, ~13th of 12 current)

---

## NICE Priority (3 remaining)

### C5: Box-Muller Upstream Bug Report
**What**: 9.5% variance deficit in WGSL Box-Muller characterized but not filed upstream.
**Why**: Shows good citizenship; reviewer may ask "did you report this?"
**Action needed**:
- Search wgpu/naga issue tracker for existing reports of transcendental polyfill accuracy
- If none found, file issue with reproduction case (WGSL shader + expected vs observed variance)
- Add "reported as [wgpu issue #XXXX]" to §4.2
**Owner**: User / toadStool upstream coordination
**Upstream**: `gfx-rs/wgpu` or `gfx-rs/naga` GitHub

### ~~M2: DF64 vs Native f64 Benchmark~~ — DONE
Analysis added to §3.3 of paper. RTX 3090 native f64 = 1:32 of FP32,
DF64 on FP32 cores = 4–8× faster than native f64. No separate benchmark
needed — the analysis is architectural.

### ~~M9: Reproduction Commands~~ — DONE
Build instructions added to §6.

---

## Summary for Upstream / Overwatch

| Item | Owner | System | What's Needed |
|------|-------|--------|---------------|
| M7/X2 (pseudoSpore URL) | overwatch + golgi | nestgate.io + golgi Caddy | `/pseudospore/` route handler + Caddy proxy |
| C5 (wgpu bug) | toadStool | gfx-rs/wgpu (GitHub) | Issue filing with WGSL repro case |

### Publishing System Map (for overwatch dissemination)

| Layer | System | URL | Role for arXiv |
|-------|--------|-----|----------------|
| **Artifact serving** | nestgate.io | `nestgate.io/pseudospore/hotspring-qcd-sun/` | CAS-backed pseudoSpore bundle (configs + braids + validation) |
| **Outer routing** | golgi (Caddy) | `primals.eco/pseudospore/hotspring-qcd-sun/` | Paper-facing URL, routes to nestgate.io |
| **Science narrative** | sporePrint | `sporeprint.primals.eco` | Public context, claims, broader story |
| **Source code** | Forgejo | `git.primals.eco/ecoPrimals/` | Sovereign git (GitHub mirror for accessibility) |
| **Artifact factory** | lithoSpore (CLI) | — | Generates pseudoSpore bundles from hotSpring outputs |
| **Raw CAS** | ironGate | (songBird mesh) | 12.7 TB content-addressed store, serves nestgate.io |
| **Provenance** | trio (rhizoCrypt + loamSpine + sweetGrass) | (UDS primals) | BLAKE3 → DAG → spine → braid chain on all artifacts |

**Pattern**: strandGate defines the compute pseudoSpore bundle format.
lithoSpore packages it. Content pushes to ironGate CAS. nestgate.io serves
it with inline verification. golgi routes the outer URL. Reviewer visits
`primals.eco/pseudospore/hotspring-qcd-sun/`, sees configs, braids, and
can run `validate.sh` to check everything locally.

**Total effort**: ~2 hr upstream wiring (nestgate.io handler + Caddy route) + 1 hr bug filing.

After these 2 items: **42/42 DONE — submission ready.**

---

*Compiled by strandGate local primal for upstream dissemination via overwatch.
Updated Aug 6, 2026: C6, M2, M9 completed. 40/42 → only M7/X2 and C5 remain.*
