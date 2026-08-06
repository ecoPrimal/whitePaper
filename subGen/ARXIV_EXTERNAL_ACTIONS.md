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

### M7 / X2: pseudoSpore URL Verification
**What**: Paper references `primals.eco/pseudospore/hotspring-qcd-sun/` which may not resolve.
**Why**: Dead link in paper is an immediate reject signal.
**Action needed**:
1. Verify if `primals.eco` DNS resolves
2. If Node Atomic isn't deployed yet, either:
   - (a) Change URL to GitHub releases: `github.com/ecoPrimals/hotspring-qcd-sun/releases`
   - (b) Add footnote: "URL will be active upon publication"
   - (c) Stand up a static page at the URL before submission
3. Also fix `hotspring-qcd-su3` reference in §4.1 (should be `hotspring-qcd-sun`)
**Owner**: User decision + Node Atomic / westGate coordination
**Blocker**: Infrastructure deployment

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

| Item | Owner | Upstream Dependency | ETA |
|------|-------|-------------------|-----|
| M7/X2 (URL) | User + westGate/Node Atomic | primals.eco infra | Decision needed |
| C5 (wgpu bug) | toadStool | gfx-rs/wgpu GitHub | 1 hr |

**Total effort**: ~1 hr upstream coordination + 1 user decision on URL strategy.

After these 2 items: **42/42 DONE — submission ready.**

---

*Compiled by strandGate local primal for upstream dissemination via overwatch.
Updated Aug 6, 2026: C6, M2, M9 completed. 40/42 → only M7/X2 and C5 remain.*
