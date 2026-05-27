# Email: The Poster That Follows the Student — May 2026

**To**: murillo@msu.edu
**From**: mokkevin@msu.edu
**Subject**: A poster that runs — something your students can use
**Attachment**: pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz

---

Hi Professor Murillo,

Quick follow-up on the compute offer from my last email. I've been thinking about something more specific for your students, and I wanted to run it by you.

I'm attaching the latest version of an artifact pattern I've been evolving. It's a computational chemistry spore for a CAZyme conformational energy landscapes collaboration — 76 files, 6 modules, 71 automated checks, GROMACS + PLUMED parity. To look at it:

```
tar xzf pseudoSpore_hotSpring-CompChem-GuideStone_v1.6.1.tar.gz
cd pseudoSpore_*
```

`scope.toml` is the module index. `./validate` reruns integrity checks. No software needed to inspect — science data, input configs, and figures are all inside.

I've been working across three domains while building this pattern — Chuna's gradient flow and your group's plasma physics, the Barrick/Lenski LTEE, and now this compChem collaboration. The compChem spore is the most mature version. Everything is published — springs, infrastructure, all of it is AGPL-3.0 on GitHub.

**What this means for your students:**

Every poster on this campus is a static image. Nobody can hand it to someone and let them run the math. This pattern changes that. A student's validated thesis work — Sarkas simulations, dielectric function checks, transport coefficients, whatever their science proves — gets packaged into an artifact that travels. A committee member, a future employer, a collaborator at a conference types one command and the science runs. When the student graduates and leaves, the artifact stays alive. Anyone can verify the work years later without the student being present.

The infrastructure to build these already exists and is published. I built it so that anyone — your students included — can package their validated results into this format. If a student has thesis work at or near completion, I'd be happy to work with them on defining the validation checks and getting it into shape. And if anyone is bottlenecked on HPCC or wants their computation revalidated on independent hardware, I can run whatever math they need.

Coffee sometime this week?

**Links:**
- [primals.eco](https://primals.eco) — project overview
- [github.com/syntheticChemistry/hotSpring](https://github.com/syntheticChemistry/hotSpring) — physics validation (Sarkas, QCD, your group's work)
- [github.com/ecoPrimals/barraCuda](https://github.com/ecoPrimals/barraCuda) — GPU compute engine
- [github.com/sporeGarden/lithoSpore](https://github.com/sporeGarden/lithoSpore) — the artifact chassis (LTEE instance)

Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu
primals.eco
