# Email: Touch-Base Before Coffee (March 2026)

**Context**: Coffee meeting Tuesday March 4. Repo link already shared. Previous emails covered Sarkas reproduction (131 checks) and neuromorphic benchmarks. Since then: 22 papers reproduced, lattice QCD production runs, DF64 discovery, live NPU. Attached data sheet covers the QCD results specifically — shareable with Bazavov. **Update Feb 27**: dynamical fermion run starting tonight — first dynamical QCD at 32⁴ on consumer GPU. Results will be available by Tuesday.

---

**Subject:** Quick check-in — still good for Tuesday?

---

Hi Professor Murillo,

Hope you're doing well. Just wanted to confirm we're still on for coffee Tuesday — looking forward to it.

Since we last talked, I've been running production lattice QCD on my workstation alongside the plasma MD work. I've put together a short results summary that covers the GPU lattice calculations and a few things I found along the way. I've attached it here in case you want to glance at it beforehand.

I'm also starting a dynamical fermion run tonight — same 32⁴ lattice, but now with staggered quarks and a CG solver on the GPU. The quenched runs showed β_c ≈ 5.69 for the deconfinement transition; with dynamical fermions we expect the transition to soften into a crossover with a shifted critical coupling. The NPU coprocessor is now running 11 inference heads in parallel with the GPU, including adaptive scan steering and quenched-phase monitoring. Should have results by the weekend.

If any of this overlaps with Professor Bazavov's work, please feel free to share — some of the lattice results reproduce his group's published calculations, and the dynamical run follows the same pseudofermion HMC approach as in his 2014 EOS paper.

See you Tuesday.

Kevin
mokkevin@msu.edu

---

## Notes

- **Attachment:** `LATTICE_QCD_RESULTS_FEB2026.md` (the QCD-focused data sheet — updated with Section 10 dynamical preview)
- Tone: short, no overselling, lets the data sheet do the work
- Bazavov mention is natural — they're in the same department and Bazavov's papers are what we reproduced
- The dynamical run mention is factual — by Tuesday we'll have data
- Don't mention ecoPrimals, constrained evolution, or the broader project architecture
- The repo is already shared; he can dig as deep as he wants
