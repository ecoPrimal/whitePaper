# Email: Revalidation Addendum Offer — May 2026

**To**: jeaves@msu.edu
**From**: mokkevin@msu.edu
**Subject**: Quick thought + an example of what I've been building
**Attachment**: pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz

---

Hi Joelle,

Hope the writing is moving well. I don't want to get in the way of the home stretch — just a quick thought that came back to me from our Zoom, and something concrete to look at.

You mentioned that when you dug into the literature for your domain, only a fraction of the published results were actually reproducible. That stuck with me, because I've been doing exactly that kind of work across other fields.

I'm attaching the latest version of an artifact pattern I've been evolving. It's a computational chemistry spore for a CAZyme conformational energy landscapes collaboration — 76 files, 6 modules, 71 automated checks, GROMACS + PLUMED parity. To look at it:

```
tar xzf pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz
cd pseudoSpore_*
```

`scope.toml` is the module index, `./validate` reruns integrity checks. No software needed to inspect. I've been working across three domains while building this pattern — lattice QCD, microbial evolution, and now this compChem collaboration. The compChem spore is the most mature version. Everything is published and AGPL-3.0 — the infrastructure to build these for any domain already exists.

If it would be useful, I'd be happy to put together a small addendum for your dissertation — an independent revalidation of the upstream results you built on, especially the ones that turned out fragile. Not a new chapter or a detour. Just a supplementary artifact: here's what reproduced, here's what didn't, here's the discrepancy. Something your committee can see without you having to restructure anything. If you'd want to connect on building one for your domain, the pattern is there.

The non-replicable gaps you found are a strength. Documenting them rigorously from an independent source only makes your work look more thorough.

And separately — if you or anyone in the lab has computation that would benefit from a second run on independent hardware, the offer still stands. I can run and revalidate whatever math and computation makes sense.

No disruption intended. If the timing isn't right, no worries — finish the dissertation first.

**Links:**
- [primals.eco](https://primals.eco) — project overview
- [github.com/syntheticChemistry/wetSpring](https://github.com/syntheticChemistry/wetSpring) — genomics and biology pipelines
- [github.com/syntheticChemistry/neuralSpring](https://github.com/syntheticChemistry/neuralSpring) — ML pipelines
- [github.com/sporeGarden/lithoSpore](https://github.com/sporeGarden/lithoSpore) — the artifact chassis

Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu
primals.eco
