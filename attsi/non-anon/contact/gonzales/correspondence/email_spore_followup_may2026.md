# Email: pseudoSpore Follow-Up — AI Workflow + Artifact Pattern — May 2026

**To**: Andrea Gonzales
**From**: mokkevin@msu.edu
**Subject**: Re: Following up — an example of the AI workflow and what it produces
**Attachment**: pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz

---

Hi Andrea,

Following up on our last exchange — I wanted to show you something concrete rather than just describe it. I'm attaching an artifact that demonstrates both the AI-accelerated workflow I mentioned and what it produces at the end.

It's a computational chemistry data package for a CAZyme conformational energy landscapes collaboration — 76 files, 6 modules, 71 automated checks, GROMACS + PLUMED parity. To look at it:

```
tar xzf pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz
cd pseudoSpore_*
```

`scope.toml` is the module index. `./validate` reruns integrity checks. No software needed to inspect — the science data, input configs, and figures are all inside.

**Why I'm showing you this:**

This artifact was built using the AI-accelerated workflow I described — the tool-building side where AI coordinates the pipeline, extracts metadata from source files, cross-checks every value, and produces validated output. Every metadata field in this package was pipeline-derived, not hand-authored. 71 checks ran automatically and passed. The collaborator receiving it types one command and knows the data is intact and the science checks out. That's the pattern I'd bring to compound registration and data management — AI doing the bookkeeping, validation built in, the human stays on the science.

The same pattern applies to your lab's work. Dose-response curves, screening results, compound metadata — packaged into self-verifying artifacts where the data travels with provenance and validates itself. Every poster and presentation on this campus is a static image. This is science that runs.

I've been working across three domains while evolving this — lattice QCD and plasma physics (Murillo's group), microbial evolution (Barrick/Lenski LTEE), and now this compChem collaboration with a citizen science community. The compChem artifact is the most mature version. Everything is published and AGPL-3.0.

I'm also showing this to Murillo's students and the Barrick lab with the same pitch — validated science that travels with the researcher. If you'd want to connect on what one of these looks like for drug discovery data, the infrastructure is there.

**Links:**
- [primals.eco](https://primals.eco) — project overview
- [lab.primals.eco](https://lab.primals.eco) — live notebooks
- [github.com/syntheticChemistry/wetSpring](https://github.com/syntheticChemistry/wetSpring) — genomics and biology pipelines
- [github.com/syntheticChemistry/healthSpring](https://github.com/syntheticChemistry/healthSpring) — pharmacology and drug discovery pipelines
- [github.com/ecoPrimals/barraCuda](https://github.com/ecoPrimals/barraCuda) — GPU compute engine

Still open to meeting whenever works — your office or a call.

Best,
Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu
