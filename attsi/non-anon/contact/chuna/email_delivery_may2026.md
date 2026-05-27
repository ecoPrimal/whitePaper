# Email: QCD Spore + Compute Offer — May 2026

**To**: TC Chuna
**CC**: Murillo
**From**: mokkevin@msu.edu
**Subject**: Re: Gradient flow — where the pattern went, and an example attached
**Attachment**: pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz

---

Hi Thomas,

Hope Germany and the LANL prep are going well. Wanted to follow up on where things have gone since our April meeting.

The artifact pattern we started with your gradient flow work has been evolving. I'm attaching the latest version — a computational chemistry spore for a CAZyme conformational energy landscapes collaboration. 76 files, 6 modules, 71 automated checks, GROMACS + PLUMED parity. To look at it:

```
tar xzf pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz
cd pseudoSpore_*
```

`scope.toml` is the module index, `validation.json` has the check results, `./validate` reruns integrity checks (just needs b3sum). No GROMACS, no PLUMED, no toolchain to inspect. Science data, input configs, topologies, and figures are all inside.

I've been working across three domains while evolving this — your gradient flow and Murillo group work, the Barrick/Lenski LTEE, and now this compChem collaboration. The compChem spore is the most mature version. Your papers are the ones that started the pattern. Everything is published — hotSpring, barraCuda, the validation infrastructure are all AGPL-3.0 on GitHub.

What I'd like to do next is rework the QCD work into this same format — something that carries your integrators, produces measurement output in formats your pipeline can ingest, and runs on whatever hardware you land on at LANL. The Chuna Engine (8 binaries, Python reader, TSV export, CG convergence history) is the foundation. MILC-compatible output and ILDG/LIME interop would make it something Bazavov's group can consume.

If you have specific integrator/lattice configurations that matter for your current work, or a representative MILC gauge config I can match output against, I can shape it around what you need.

More broadly — I can run workloads and revalidate whatever math and computation you'd like verified on independent hardware. The cluster is 11 nodes now (~154 cores, ~248 GB GPU VRAM, dual-vendor). If there's lattice work or anything else you'd want a second run on, I have the capacity.

No rush — the offer stands whenever it's useful.

**Links:**
- [primals.eco](https://primals.eco) — project overview
- [github.com/syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring) — physics validation (your papers live here)
- [github.com/ecoPrimals/barraCuda](https://github.com/ecoPrimals/barraCuda) — GPU compute engine (WGSL, no CUDA)

Best,
Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu
