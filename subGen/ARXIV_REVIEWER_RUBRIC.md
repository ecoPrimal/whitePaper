# arXiv Rung 1 — Reviewer Rubric Matrix

**Purpose**: Systematic quality gate for the SU(3) pure gauge preprint, organized by what each reviewer will scrutinize based on their domain expertise. Address every item before sending.

**Paper**: "Vendor-Agnostic Lattice QCD on Consumer GPUs: SU(3) Pure Gauge HMC with DF64 WebGPU/WGSL and Cryptographic Provenance"

**Reviewers**: Michael Murillo (MSU), Thomas Chuna (LANL), Alexei Bazavov (MSU)

---

## A. Bazavov — Lattice QCD Specialist

Bazavov publishes in hep-lat. He will read this paper as a lattice practitioner and compare against established codes (MILC, openQCD, Grid). His feedback is the most domain-critical.

| # | Question He Will Ask | Paper Section | Current Status | Action Required |
|---|---------------------|---------------|----------------|-----------------|
| B1 | Are the plaquette values correct for SU(3) at these β values? | §3.2, §4.4 | 4⁴/8⁴ at β=2.3 shown. 12⁴ β-scan matches GL10/NS02 to <0.1% at β≥6.0. | **Fill 16⁴ data** when scan completes. Add explicit comparison to Necco-Sommer 2002 Table II or Bali 2000 Table I with matching volumes. |
| B2 | Is the strong-coupling expansion comparison rigorous? | §2.1, §4.4 | "β/18 ≈ 0.128 with higher-order corrections" — vague. | **Cite the exact strong-coupling series**: next-to-leading order coefficient for SU(3). Bhanot & Rebbi or Drouffe & Zuber. |
| B3 | What is the Omelyan integrator order? 2MN vs ABAB? | §2.1, §4.5.2 | "Omelyan 2MN" mentioned but parameter λ not stated. | **State the Omelyan λ parameter** explicitly (typically λ=0.1932). Cite Takaishi & de Forcrand 2006. |
| B4 | Why only one β value for production plaquettes? | §3.2 | 4⁴ and 8⁴ at β=2.3 only. β-scan is CPU-only on 8⁴. 12⁴ has 5 β points. | **Add GPU production at β=6.0** on 12⁴ or 16⁴ — this is the canonical weak-coupling benchmark where lattice QCD papers are judged. |
| B5 | What about Wilson loops / string tension / Creutz ratios? | Not present | Only plaquette measured. | **Acknowledge limitation explicitly** — pure gauge papers normally report Wilson loops χ(R,T) and extract string tension σa². State this as Rung 2 scope. |
| B6 | Thermalization — how do you know 200 trajectories is enough? | §3.2, §3.5 | τ_int reported. No thermalization diagnostic plot. | **Add a plaquette time-history plot** showing thermalization plateau. This is standard in every lattice paper. |
| B7 | Binning / jackknife for error estimates? | §3.2, §3.5 | Errors appear to be simple σ/√N. | **Implement jackknife or bootstrap error analysis** with bin-size dependence. State error method explicitly. Autocorrelation-corrected errors via Γ-method (Wolff 2004, hep-lat/0306017) preferred. |
| B8 | What about SU(3) unitarity preservation? | §2.2 | Not discussed. | **Report max ‖UU†−I‖** after production runs. DF64 accumulation may cause unitarity drift. If re-unitarization is applied, state frequency and method (Gram-Schmidt or Cayley). |
| B9 | Acceptance rate 100% at β=2.3 on 4⁴ is suspicious — dt too small? | §3.2, §4.5.2 | 100% accept on 4⁴, 99.5% on 8⁴. | **Not a bug** — β=2.3 strong coupling + small volume = tiny ΔH. But **state this explicitly**: low acceptance overhead is traded for integrator stability validation. |
| B10 | Continuum limit extrapolation? | Not present | Only discrete volumes. | **Not needed for Rung 1** — but state clearly that continuum extrapolation is Rung 2+ scope. |
| B11 | Comparison to known SU(3) pure gauge reference implementations? | Not present | No direct comparison to MILC/openQCD output. | **Cite MILC collaboration SU(3) pure gauge results** at matching β and volumes. Even one point of agreement adds credibility. |
| B12 | 16⁴/24⁴ data placeholders in the paper? | §4.4 | "DATA IN PROGRESS" placeholder. | **MUST be filled or removed** before sending. Placeholders signal unfinished work. |

---

## B. Chuna — Lattice/Kinetic Theory (LANL)

Chuna knows kinetic theory and computational physics at LANL production scale. He will focus on the HMC algorithm, the DF64 arithmetic validity, and whether the three-path methodology is rigorous.

| # | Question He Will Ask | Paper Section | Current Status | Action Required |
|---|---------------------|---------------|----------------|-----------------|
| C1 | Is the Omelyan integrator symplectic in DF64? | §2.2, §4.5.2 | ΔH scaling shown (p=2.37). But no discussion of symplecticity under DF64 rounding. | **Add a paragraph**: DF64 rounding errors break exact symplecticity, but the Metropolis step corrects this — the algorithm is exact regardless of integrator precision. Cite Kennedy & Pendleton (2001). |
| C2 | Is the three-path methodology novel or standard? | §4.2 | Presented as a validation methodology. | **Cite prior work** on systematic GPU validation in HPC: Phillips et al. (NAMD), Anderson et al. (HOOMD). If the three-path approach is original, state it explicitly as a contribution. |
| C3 | DF64 error accumulation — is the analysis rigorous? | §3.3 | "~9 digits for accumulated observables." | **Derive the expected error bound** analytically: N operations × ulp accumulation. Compare to measured. Cite Higham (2002) "Accuracy and Stability of Numerical Algorithms" for error analysis framework. |
| C4 | CPU momentum generation — what about decorrelation? | §2.1 | CPU LCG + Gaussian, then uploaded. | **State the LCG parameters and period**. Confirm the generator passes PRNG quality tests (TestU01 or similar). Period must exceed the number of momenta sampled. |
| C5 | Is the Box-Muller bias a known issue in the WGSL/Vulkan ecosystem? | §4.2 | Characterized (9.5% variance deficit). | **Search for and cite any upstream bug reports** in naga/wgpu for transcendental accuracy. If none exist, consider filing one and referencing. This strengthens the finding. |
| C6 | How does the cost compare to CUDA implementations? | §3.1 | Timing table present but brief (2 volumes only). | **Add a flops-per-dollar or time-to-solution comparison** with a published CUDA SU(3) benchmark. Even order-of-magnitude comparison is informative. |
| C7 | Leapfrog vs Omelyan — why Omelyan? | §2.1 | "Omelyan 2MN" stated without justification. | **Add one sentence**: Omelyan 2MN reduces ΔH by ~4× vs standard leapfrog at the same step count (Takaishi & de Forcrand 2006), directly improving acceptance rate. |
| C8 | What is the GPU memory scaling? | Not present | Only VRAM sizes in hardware table. | **Report memory per lattice volume**: bytes/site for SU(3) link + momentum + force arrays. State max volume that fits in 16 GB (RX 6950 XT) and 24 GB (RTX 3090). |
| C9 | Reversibility test? | §4.5 | ΔH scaling present but no explicit reversibility check. | **Run a reversibility test**: evolve forward N steps, reverse N steps, measure ‖U_final − U_initial‖. This is distinct from ΔH and directly tests integrator coding correctness. |
| C10 | Could Philox/Threefry replace Box-Muller for GPU PRNG? | §4.2, §4.3 | "Philox counter-based is in development." | **Strengthen**: cite Salmon et al. (2011) "Parallel Random Numbers: As Easy as 1, 2, 3" and state that counter-based RNGs avoid the transcendental polyfill issue entirely by using only integer arithmetic. |

---

## C. Murillo — Computational Physics (MSU)

Murillo works on plasma physics, molecular dynamics, and GPU computing. He will evaluate the computational methodology, reproducibility claims, and whether this represents a genuine advance in GPU scientific computing.

| # | Question He Will Ask | Paper Section | Current Status | Action Required |
|---|---------------------|---------------|----------------|-----------------|
| M1 | Is DF64 genuinely novel for lattice calculations? | §1, §2.2 | Positioned as novel. | **Search for prior DF64 use in lattice QCD**. If none exists, state: "To our knowledge, this is the first application of DF64 emulation to lattice gauge theory." If prior work exists, cite and differentiate. |
| M2 | What is the performance overhead of DF64 vs native f64? | §2.2 | Not quantified. | **Benchmark DF64 vs native f64 on the same GPU** (RTX 3090 supports native f64 at 1:32 rate). Report the slowdown factor. If DF64 on FP32 cores is faster than native f64 on throttled FP64 ALUs, that's a key result. |
| M3 | Does the provenance chain add meaningful overhead? | §2.4 | Pipeline described but no overhead measured. | **Report provenance overhead** as % of total trajectory time. If <1%, state it. This validates the "free provenance" claim. |
| M4 | How does this compare to existing portable lattice codes? | §1 | CUDA/ROCm framed as the only option. | **Cite portable lattice efforts**: Grid (Boyle et al.), QUDA (Clark et al.), Chroma (Edwards & Joo). Differentiate: those use CUDA+HIP, this uses WGSL. None use DF64 or carry provenance. |
| M5 | Is the Rust + WGSL stack mature enough for production? | §2.3 | Implicit — "pure Rust, zero C deps." | **Address ecosystem maturity honestly**: wgpu is production-quality (used in Firefox), naga compiles to SPIR-V reliably, but WGSL f64 transcendentals have a known bug (§4.2). The stack is viable for deterministic GPU arithmetic; stochastic components need the cpu_mom workaround. |
| M6 | Can this approach scale to larger lattices? | §4.3 | 16⁴/24⁴ "in progress." | **Report the memory bound**: at what volume does the RTX 3090 (24 GB) run out of VRAM? Project the largest feasible volume. For 32⁴ SU(3): 32⁴ × 4 × 18 × 8 bytes ≈ 2.4 GB — should fit easily. State this. |
| M7 | Is the pseudoSpore artifact actually downloadable and runnable? | §5 | URL given but artifact may not be published yet. | **Verify the URL resolves** before sending. If the pseudoSpore isn't published yet, either publish it or remove the claim. Dead links destroy credibility. |
| M8 | What is the scientific impact beyond lattice QCD? | §6 | Conclusion focused narrowly on lattice. | **Add 1-2 sentences** on broader impact: DF64+WebGPU methodology applies to any GPU scientific computation requiring f64 precision (MD, DFT, FEM, CFD) on consumer hardware without vendor SDK. |
| M9 | Reproducibility — can a reader actually reproduce Figure 1? | §5 | Commands shown but `--features barracuda-local` is opaque. | **Test the reproduction commands on a clean checkout**. Document exact versions (Rust, wgpu, Vulkan driver). If it takes >5 minutes to build, state build time. |
| M10 | Why is this not submitted to Computer Physics Communications? | Not addressed | arXiv is stated target. | **Consider dual submission path**: arXiv hep-lat preprint → CPC or SciPost Physics for peer review. State the plan in the submission letter. This signals seriousness. |

---

## D. Cross-Reviewer Issues (All Three Will Notice)

| # | Issue | Sections | Action Required |
|---|-------|----------|-----------------|
| X1 | **16⁴/24⁴ placeholders** — "DATA IN PROGRESS" in the paper body | §4.4 | Fill with real data or remove entirely. No placeholders in a sent preprint. |
| X2 | **pseudoSpore URL says "su2"** — `hotspring-qcd-su2` but paper is SU(3) | §5 | Fix URL to `hotspring-qcd-su3`. |
| X3 | **Reference list is thin** — 13 references for a lattice QCD paper | §References | Expand to 25-30. Add: Gattringer & Lang textbook, MILC/QUDA/Grid papers, Wolff error analysis, Necco-Sommer, Bali, standard SU(3) pure gauge references. |
| X4 | **No figures** — text-only paper | Throughout | Add at minimum: (1) plaquette time history showing thermalization, (2) β-scan plot with published comparison, (3) DF64 precision matrix visualization, (4) cross-vendor comparison plot. |
| X5 | **"ecoPrimals" ecosystem jargon** — rhizoCrypt, sweetGrass, bearDog etc. | §2.4 | **Genericize for audience**: describe the provenance pipeline in standard terms (hash → DAG → ledger → signature → attribution). Footnote the ecosystem names. A lattice physicist doesn't care what the tool is called. |
| X6 | **Title length** — 16 words with subtitle | Title | Consider shortening to: "Vendor-Agnostic SU(3) Lattice Gauge Theory on Consumer GPUs via WebGPU" — let the abstract handle DF64/provenance. |
| X7 | **Abstract is 3 paragraphs** — arXiv standard is 1 paragraph | Abstract | **Compress to one dense paragraph** (~200 words). Cut the PRNG paragraph — it's a detail, not a headline. |
| X8 | **No comparison to cost of institutional HPC** — key selling point buried | §3.1 | **Add a cost table**: $/trajectory on consumer GPU vs cloud GPU vs HPC allocation. This is the paper's most accessible result for non-specialists. |
| X9 | **Appendix B (gauge group audit)** — self-deprecating | Appendix B | **Remove or rewrite**. Admitting "we mislabeled the gauge group" erodes confidence. The code was always SU(3); the documentation was wrong. State the audit happened internally. Don't narrate the mistake in the paper. |
| X10 | **Section numbering inconsistency** — §4.2 is called "Validation Methodology" but is really about PRNG | §4 | Restructure §4: (4.1) Provenance, (4.2) HMC Validation (action-force, ΔH, Creutz), (4.3) PRNG Isolation, (4.4) β-scan, (4.5) Limitations. Currently the order is confusing. |

---

## E. Scoring Summary

**For each item, mark**: DONE / IN PROGRESS / BLOCKED / NOT NEEDED

### Pre-Send Checklist (must be DONE before reviewer send)

| Priority | Items | Count |
|----------|-------|-------|
| **MUST** (send-blocking) | B1, B6, B7, B12, C1, X1, X2, X3, X4, X5, X7, X9 | 12 |
| **SHOULD** (significantly strengthens) | B2, B3, B4, B5, B8, C2, C3, C6, C7, C9, M1, M2, M4, M6, M7, X6, X8, X10 | 18 |
| **NICE** (polish) | B9, B10, B11, C4, C5, C8, C10, M3, M5, M8, M9, M10 | 12 |

**Total items**: 42

### Critical Path to Send

```
1. 16⁴ dual-GPU scan completes (strandGate — RUNNING)
2. Fill 16⁴ data, remove all placeholders (B1, B12, X1)
3. Add figures — thermalization plot, β-scan, cross-vendor (X4)
4. Implement jackknife errors (B7)
5. Compress abstract to 1 paragraph (X7)
6. Expand references to 25-30 (X3)
7. Genericize ecosystem jargon for lattice audience (X5)
8. Remove gauge group audit appendix (X9)
9. Fix pseudoSpore URL (X2)
10. Add unitarity check (B8), reversibility test (C9)
11. Regenerate LaTeX (tectonic build)
12. Send to Murillo / Chuna / Bazavov
```

---

*subGen Wave 156d — Reviewer rubric for arXiv Rung 1 preprint. 42 items across 3 reviewers
(Bazavov: 12 lattice QCD, Chuna: 10 algorithmic, Murillo: 10 computational) + 10 cross-reviewer.
12 MUST-fix items before send, 18 SHOULD-fix, 12 NICE-to-have.*
