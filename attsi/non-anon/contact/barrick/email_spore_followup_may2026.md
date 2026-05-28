# Email: pseudoSpore Follow-Up — May 2026

**To**: Jeff Barrick
**From**: mokkevin@msu.edu
**Subject**: The USB pattern evolved — new domain, same idea
**Attachment**: pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz

---

Dr. Barrick,

Quick follow-up — the lithoSpore USB I brought to the interview has been evolving. I'm attaching an example of where the pattern is now, in a completely different domain.

It's a computational chemistry artifact for a CAZyme conformational energy landscapes collaboration — 76 files, 6 modules, 71 automated checks, GROMACS + PLUMED parity. To look at it:

```
tar xzf pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz
cd pseudoSpore_*
```

`scope.toml` is the module index, `./validate` reruns integrity checks (just needs b3sum). No GROMACS, no toolchain to inspect. Science data, input configs, topologies, and figures are all inside. Same one-command self-verification as the LTEE USB, different science.

I've been working across three domains while evolving this — the LTEE work you saw, lattice QCD and plasma physics (with Murillo's group at CMSE), and now this compChem collaboration with a citizen science community. The compChem artifact is the most mature version of the pattern. The LTEE lithoSpore can be reworked into this same format now that it's solidified. Everything is published and AGPL-3.0.

One thing I've been thinking about since the visit: this pattern applies directly to your students' thesis work. Every poster and defense talk is a static presentation — nobody can hand it to someone and let them run the science. An artifact like this changes that. Ira's seabreeze structural variation work, Pranesh's breseq supplementation, Isaac's fitness recovery from deletions — any of those could be packaged so the science travels with the researcher. A committee member, a future employer, a collaborator types one command and the validated results run. The infrastructure to build these already exists and is published — your students can use it.

And separately — I can run workloads and revalidate whatever math and computation the lab might benefit from on independent hardware. The cluster is 11 nodes now (~154 cores, ~248 GB GPU VRAM). If there's genomic analysis, structural variation work, or anything that would benefit from a second environment, I have the capacity.

**Links:**
- [primals.eco](https://primals.eco) — project overview
- [github.com/sporeGarden/lithoSpore](https://github.com/sporeGarden/lithoSpore) — the LTEE artifact from the interview
- [github.com/syntheticChemistry/wetSpring](https://github.com/syntheticChemistry/wetSpring) — genomics and biology pipelines
- [github.com/ecoPrimals/barraCuda](https://github.com/ecoPrimals/barraCuda) — GPU compute engine
- [lab.primals.eco](https://lab.primals.eco) — live notebooks

Best,
Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu
