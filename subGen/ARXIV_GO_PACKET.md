# arXiv QCD Rung 1 — GO PACKET

**Status:** Data complete. 41/42 rubric items done. LaTeX stale. Reviewers identified.
**Estimated remaining effort:** ~2-3 days assembly + review cycle
**Target:** arXiv hep-lat (primary), cs.DC (cross-list)
**Date:** August 25, 2026

---

## What's Done (41/42)

- 32⁴ production: 57 configs measured, 0.3% literature agreement
- 16⁴ cross-vendor: 6 ppm at β=6.2
- AMD ~20× advantage documented
- All Bazavov items (B1-B12): DONE
- All Murillo items (M1-M10): DONE
- 9/10 Chuna items: DONE
- All cross-reviewer items (X1-X10): DONE
- pseudoSpore URL verified (M7)
- Appendix B rewritten (X9)
- §4 restructured (X10)

## What's Open (1/42)

**C5 — Box-Muller upstream bug report** (NICE-TO-HAVE, not blocking)
- 9.5% variance deficit in WGSL Box-Muller is characterized
- Action: Search gfx-rs/wgpu + gfx-rs/naga issue trackers
- If no existing issue: file minimal repro
- Cite issue number in §4.2
- ~1 hour effort

---

## Submission Sequence

### Step 1: Confirm 24⁴ production status
- Check westGate for 24⁴ thermalization completion
- If complete: merge cross-vendor numbers into §3.2, §3.4, §4.4
- If incomplete: submit with 16⁴ + 32⁴ only (sufficient for Rung 1)

### Step 2: Regenerate LaTeX
- Current `.tex` is STALE (still SU(2) title/abstract)
- Source of truth: markdown sections in subGen/
- Pipeline: sporePrint → tectonic build
- Verify: title updated to SU(N), all volumes current, figures regenerated

### Step 3: Freeze pseudoSpore v1.0.0
- Node Atomic owner responsibility
- Sign bundle with bearDog Ed25519
- Ingest to NestGate CAS
- Verify: `validate.sh` downloads + checks BLAKE3 hashes
- URL: `primals.eco/pseudospore/hotspring-qcd-sun/` must resolve

### Step 4: Pre-submission review
- Send PDF + pseudoSpore artifact link to:

| Reviewer | Email/Contact | Focus areas |
|----------|--------------|-------------|
| **Michael Murillo** (MSU) | — | Computational methodology, GPU scaling, reproducibility |
| **Thomas Chuna** (LANL) | — | HMC correctness, DF64 precision, algorithmic rigor |
| **Alexei Bazavov** (MSU) | — | Lattice QCD physics — plaquettes, β-scan, Wilson loops |

- Ask for: technical feedback, factual errors, missing citations
- Timeline: request 2-week turnaround

### Step 5: Incorporate feedback
- Address reviewer comments
- Update LaTeX
- Final proofread

### Step 6: Submit to arXiv
- Primary: **hep-lat**
- Cross-list: **cs.DC**
- ORCID: `0009-0004-2141-0321`
- Verify: all figures render, bibliography complete, abstract ≤ 300 words
- Note: first arXiv submission requires endorsement (Murillo or Bazavov can endorse)

### Step 7: Post-submission
- Update sporePrint with arXiv ID
- Notify collaborators
- Begin peer review journal submission (CPC or SciPost Physics per M10)

---

## Known Issues to Reconcile

| Issue | Resolution |
|-------|-----------|
| LaTeX stale (SU(2) vs SU(N)) | Regenerate from current markdown |
| Status doc headers stale | Update ARXIV_RUNG1_STATUS.md after submission |
| REMAINING_WORK vs EXTERNAL_ACTIONS divergence | REMAINING_WORK is more current; reconcile pseudoSpore URL status |
| §5.3 Large-N scope | SU(2)+SU(3) complete; N≥4 deferred to Rung 2 (acceptable per Option A) |

---

## Checklist

- [ ] 24⁴ production status confirmed
- [ ] LaTeX regenerated from current markdown
- [ ] Title/abstract updated to SU(N)
- [ ] All figures regenerated with current data
- [ ] pseudoSpore v1.0.0 frozen and signed
- [ ] pseudoSpore URL resolves end-to-end
- [ ] validate.sh works on fresh download
- [ ] C5 upstream bug filed or noted (optional)
- [ ] PDF sent to Murillo
- [ ] PDF sent to Chuna
- [ ] PDF sent to Bazavov
- [ ] Reviewer feedback incorporated
- [ ] arXiv endorsement secured (Murillo or Bazavov)
- [ ] Submitted to hep-lat + cs.DC
- [ ] sporePrint updated with arXiv ID
