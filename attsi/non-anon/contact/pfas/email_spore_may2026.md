# Email: Reaching Back — blueFish + Spore Pattern — May 2026

**To**: Dan Jones, Cheryl Murphy, Sima Kumar
**From**: mokkevin@msu.edu
**Subject**: What I've been building since leaving — something for the PFAS work
**Attachment**: pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz

---

Hi Dan, Cheryl, and Sima,

Hope things are going well in the lab. I've been building since I left, and I wanted to reach back and show you where it's at — because a chunk of it is specifically for the PFAS work.

I'm attaching an example of what the pattern looks like in practice. It's a computational chemistry artifact for a CAZyme conformational energy landscapes collaboration — 76 files, 6 modules, 71 automated checks, GROMACS + PLUMED parity. To look at it:

```
tar xzf pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz
cd pseudoSpore_*
```

`scope.toml` is the module index. `./validate` reruns integrity checks. No software needed to inspect — science data, configs, and figures are all inside. The person receiving it knows the data is intact and the science checks out before they touch anything.

I've been working across three domains while evolving this artifact pattern — lattice QCD and plasma physics (with Murillo's group at CMSE), microbial evolution (Barrick/Lenski LTEE), and now this compChem collaboration. The compChem spore is the most mature version. Everything is published and AGPL-3.0.

**Project blueFish — what I'm building for PFAS:**

On my own time I've already reproduced the FindPFAS detection pipeline (17/17 checks), the EPA PFAS machine learning workflow (14/14), and MassBank spectral matching (9/9) — 40 checks total, all passing, all in Rust. That's the foundation. What I intend to build on top of it is blueFish — a sovereign PFAS data pipeline that can produce analytical results without Chromeleon or other vendor-locked software. Same data in, same validated results out, but open and portable.

What I need to keep building it is domain material — if you have data, papers, rubrics, SOPs, analytical methods, anything that defines what correct PFAS detection looks like in practice, I can start building a validation library for the subproject. Every method gets automated checks against published or lab-verified values, the same way the attached artifact does for computational chemistry. The more reference material I have, the more complete the validation coverage.

I can also run and revalidate whatever computation the lab might benefit from on independent hardware. I have 11 nodes now (~154 cores, ~248 GB GPU VRAM). If there's mass spec data processing, ML model work, or anything else that would benefit from a second environment, I have the capacity.

Everything I build is AGPL-3.0 and CC-BY-SA — published and available. If blueFish gets to where I want it, any PFAS lab can use it.

Would be good to catch up in person if any of you are around campus.

**Links:**
- [primals.eco](https://primals.eco) — project overview
- [github.com/syntheticChemistry/wetSpring](https://github.com/syntheticChemistry/wetSpring) — genomics, analytical chemistry, PFAS detection (Track 2 / blueFish)
- [github.com/ecoPrimals/barraCuda](https://github.com/ecoPrimals/barraCuda) — GPU compute engine

Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu
primals.eco
