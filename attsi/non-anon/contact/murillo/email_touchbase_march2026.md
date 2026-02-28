# Email: Touch-Base Before Coffee (March 2026)

**Context**: Coffee meeting Tuesday March 4. Repo link already shared. Previous emails covered Sarkas reproduction (131 checks) and neuromorphic benchmarks. Since then: 22 papers reproduced, lattice QCD production runs, DF64 discovery, live NPU. First email (Feb 27) sent with quenched QCD data sheet. **Update Feb 28**: dynamical production complete — 1,071 trajectories, 17 NPU-steered β points, crossover confirmed. Brain architecture built. Second data sheet ready to send Sunday/Monday.

---

## Email 1 (SENT Feb 27)

**Subject:** Quick check-in — still good for Tuesday?

Hi Professor Murillo,

Hope you're doing well. Just wanted to confirm we're still on for coffee Tuesday — looking forward to it.

Since we last talked, I've been running production lattice QCD on my workstation alongside the plasma MD work. I've put together a short results summary that covers the GPU lattice calculations and a few things I found along the way. I've attached it here in case you want to glance at it beforehand.

I'm also starting a dynamical fermion run tonight — same 32⁴ lattice, but now with staggered quarks and a CG solver on the GPU. The quenched runs showed β_c ≈ 5.69 for the deconfinement transition; with dynamical fermions we expect the transition to soften into a crossover with a shifted critical coupling. The NPU coprocessor is now running 11 inference heads in parallel with the GPU, including adaptive scan steering and quenched-phase monitoring. Should have results by the weekend.

If any of this overlaps with Professor Bazavov's work, please feel free to share — some of the lattice results reproduce his group's published calculations, and the dynamical run follows the same pseudofermion HMC approach as in his 2014 EOS paper.

See you Tuesday.

Kevin
mokkevin@msu.edu

**Attachment:** `LATTICE_QCD_RESULTS_FEB2026.md`

---

## Email 2 (DRAFT — send Sunday Mar 1 or Monday Mar 2)

**Subject:** Re: Quick check-in — dynamical results in

---

Hi Professor Murillo,

Quick follow-up — the dynamical fermion run finished overnight. Attaching a progress report with the full results.

The short version: 1,071 trajectories across 17 β points on the 8⁴ lattice. The NPU expanded a 4-seed scan to 17 points autonomously — it bracketed the crossover from both sides before filling in. The transition is smooth (no first-order jump), and β_c has shifted down to around 5.0–5.5, consistent with fermion backreaction softening the quenched first-order transition.

CG iterations track the Anderson localization prediction — more gauge disorder at low β means more localized modes and slower CG convergence. This connection is well-established theoretically (Kovács, Giordano et al.), but we're using it computationally as a cheap proxy to predict solver cost before each trajectory.

Since the last email I've also built a concurrent pipeline where the Titan V, CPU, and NPU all run alongside the RTX 3090 during the dynamical HMC. The details are in Section 6 of the attached sheet.

Next step is scaling to 16⁴ and 32⁴. Happy to walk through any of this Tuesday.

Kevin
mokkevin@msu.edu

**Attachment:** `DYNAMICAL_QCD_PROGRESS_FEB2026.md`

---

## Notes

- Email 1 was sent Feb 27 with the quenched data sheet
- Email 2 shows 24-hour turnaround from "starting tonight" to "finished overnight" — demonstrates velocity
- Both data sheets are shareable with Bazavov
- The dynamical doc now has plaquette curves with seed vs NPU-inserted annotations
- Don't mention ecoPrimals, constrained evolution, or the broader project architecture
- The repo is already shared; he can dig as deep as he wants
