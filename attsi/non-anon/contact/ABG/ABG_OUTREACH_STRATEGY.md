# ABG Outreach Strategy

**Date**: May 3, 2026
**Status**: Phase 1 — Recon (active)
**Engagement mode**: Human-first. Kevin the microbiologist, not ecoPrimals.

---

## Two Purposes, One Interaction

ABG serves dual roles:

1. **Outreach target** — Early-career bioinformaticians who can use, test,
   and validate ecoPrimals tools against real research problems
2. **sporePrint mirror** — Real humans who will surface every place where
   primals.eco concepts are opaque, jargon-laden, or inaccessible

Every ABG interaction generates signal in both directions.

---

## The Human-First Principle

Kevin joins ABG as **Tamison** — his personal online handle. Not as
ecoPrimal (the dev-space identity), not as attsi (the philosopher-space
identity). Tamison is Kevin the human on the internet.

| Space | Handle | Used in ABG? |
|-------|--------|-------------|
| Personal / online | **Tamison** | Yes — this is the ABG identity |
| Dev space | ecoPrimal | No — too close to ecosystem name |
| Philosopher space | attsi | No — too abstract for bioinformatics |

**The framing**:
- "I'm Kevin (Tamison), a microbiologist with an MS in data science"
- "I built some Rust bioinformatics tools"
- "Happy to help — what are you working on?"

**The medium**: Voice chat, real conversation, human velocity. Text when
appropriate but voice when possible. This is peer interaction, not
documentation.

**The test**: If the science stands on its own when Kevin explains it to
a grad student in voice, the stack is real. If it requires ecosystem
jargon to explain, sporePrint needs work.

**The rule**: Every concept that needs explaining in voice is a sporePrint
page that needs rewriting.

---

## Phased Approach

### Phase 1: Recon (Current)

- Read and analyze the Discord (done — see ABG_ANALYSIS.md)
- Understand community norms, project proposals, and technical gaps
- Identify which members are working on problems that overlap
- Do not engage yet

### Phase 2: Join Legitimately

Admission qualifications (all met):
- BS Microbiology (University of Michigan)
- MS Data Science
- Army infantry → bench scientist → data scientist → scientific computing
- Extensive research experience across microbiology, genomics, data science
- Strong technical ability (Rust, GPU compute, bioinformatics pipelines)

**Admission message** (draft — adapt to community tone):
> Hi, I'm Kevin. BS Microbiology, MS Data Science. Built sovereign
> bioinformatics tools in Rust — 16S pipelines, metagenomics,
> GPU-accelerated genomics on consumer hardware. Interested in
> field genomics and environmental eDNA. Happy to help where I can.

Keep it short. Don't mention 4.5M lines. Don't mention K-NOME. Don't
mention primals or springs. Be a person.

### Phase 3: Contribute as Kevin

Offer help on their terms, in their language.

**Immediate contributions**:

| Opportunity | ABG Member | What Kevin Offers |
|------------|-----------|------------------|
| Basecall-free Nanopore enrichment | Everett | Direct overlap with NPU adaptive sampling work. Share approach, discuss architecture. |
| Consumer GPU for genomics | Anyone hitting HPC walls | "You already have the GPU — here's how to use it for science through Vulkan" |
| Rust in bioinformatics | iaacornus | Rare shared skillset. Natural collaboration on fungal genome + Rust tooling. |
| Metagenomics | Anyone doing environmental work | Cold seep analysis (299K QS genes, 170 metagenomes) — share methods, not branding. |
| HPC orchestration pain | HudoGriz, tdmedina | Discuss alternatives to Snakemake/Nextflow. Let them discover the limitations. |
| Structure prediction costs | WillyP, anyone using AlphaFold API | "What if you could run that locally for $0.0001/prediction?" |

**How to share tools**: Point to specific capabilities, not the ecosystem.
"I have a Rust 16S pipeline" not "I have a sovereign scientific computing
ecosystem with 15 primals and 8 springs." Let them pull, don't push.

### Phase 4: Raise the Commons Question

When trust is established (weeks, not days):

- Raise licensing as a genuine community concern, not an ecoPrimals pitch
- Point to SEER as the concrete pattern: "did you notice that startup that
  joined? They're learning what problems you have so they can build
  proprietary solutions"
- Introduce AGPL concept: "if you publish under AGPL, anyone who builds on
  your work has to share modifications back"
- If asked about licensing model: explain scyBorg triple in plain language
  without the name — "AGPL for code, open research commitment for methods,
  Creative Commons for docs"
- Only use the term "scyBorg" if they ask what the license is called

### Phase 5: Deeper Collaboration

Joint projects that compose ABG expertise with ecoPrimals validation:

| Project | ABG Members | ecoPrimals Coverage |
|---------|------------|-------------------|
| Fungal genomics pipeline | BenDiskords + iaacornus | wetSpring WGS/annotation + Rust tooling |
| LTEE structural evolution | Anyone interested in evo bio | Paper 02 + helixVision (8.3M structure predictions) |
| Ocean/cold seep eDNA | Environmental genomics people | Paper 05 + Paper 09 + deep-sea lander architecture |
| Drug discovery on consumer GPU | lilK, MrKostraboski | barraCuda GPU math + docking acceleration |
| Biobank provenance | Nevada | NestGate CAS + loamSpine chain-of-custody |

These are **joint projects**, not ecoPrimals projects with ABG labor. The
science belongs to everyone involved. Published under AGPL/scyBorg.

---

## sporePrint Refinement Loop

ABG interactions are a live tractability test for primals.eco.

### Tracking Protocol

After each significant ABG interaction, log:

1. **What concept was discussed?**
2. **Did the ABG member understand it from primals.eco?** (Y/N)
3. **Did Kevin have to explain it from scratch?** (Y/N)
4. **What language did Kevin use that worked?** (capture the phrasing)
5. **What primals.eco page should have done this job?** (URL)

### Candidate Pages for Tractability Audit

| Concept | Current Page | Predicted Failure Mode | Status (May 2026) |
|---------|-------------|----------------------|-------------------|
| scyBorg | Knowledge Commons | Name is opaque. "Triple license" means nothing to a grad student. | **Fixed** — leads with license names, scyBorg parenthetical |
| NUCLEUS | Architecture page | Composition model sounds like enterprise Java, not biology. | Glossary has plain definition |
| "primals" | Primal catalog | The word itself — does anyone outside the ecosystem know what it means? | **Fixed** — plain-English intro + glossary page |
| "springs" | Spring catalog | Sounds like Java Spring Framework. Bioinformaticians will flinch. | Glossary defines; catalog intro still dense |
| "gates" | Hardware page | Networking term collision (logic gates, network gateways). | **Fixed** — glossary defines as "machine/node" |
| "niches" | Deployment model | Ecological term, but overloaded in CS (niche market, niche product). | Glossary defines |
| Sovereign | Throughout site | Loaded political term. Some will hear "sovereign citizen." | **Fixed** — key pages use "self-hosted", glossary disambiguates |
| "products" | Products section | Sounds commercial. ABG hears "selling something." | **Fixed** — chemical-reaction-product disambiguation |
| Hardware atheist | NVIDIA outreach | Clever internally, may confuse in mixed company. | whitePaper-internal, not on site |

### Success Signals

- ABG member visits primals.eco unprompted and understands a page
- ABG member explains an ecoPrimals concept to another member correctly
- ABG member uses a tool without Kevin guiding them through it
- ABG member proposes a project that composes ecoPrimals tools

### Failure Signals

- Kevin has to explain the same concept repeatedly in voice
- ABG member visits primals.eco and leaves confused
- ABG member asks "but what IS a primal?" after reading the catalog
- ABG member conflates ecoPrimals with blockchain/crypto because of
  sovereignty language

---

## SEER and the AGPL Inversion

### The Pattern

SEER (Seer.host) is a commercial entity that joined ABG's admissions channel
on day one. Their pitch: "compact predictive AI for complex physical systems"
applied to bioinformatics. They want to learn what problems researchers face
so they can adapt their proprietary technology.

This is not unique to SEER. Any open research community producing valuable
problem definitions will attract commercial intelligence gathering. Blocking
it is futile — you can't distinguish genuine contributors from scouts, and
attempting to do so destroys the open culture that makes the community
valuable.

### The Inversion

Instead of preventing extraction, make extraction into contribution:

1. Community work published under **AGPL-3.0-or-later** (code)
2. Methods documented under **CC-BY-SA 4.0** (docs/papers)
3. Research commitment via **ORC** (Open Research Commitment)

Effect: Anyone (including SEER) who builds on community work must share
their modifications. The more they extract, the more they must contribute.
The commons gets stronger from every commercial actor that touches it.

### How to Raise This

- Wait for trust. Don't bring it up on day one.
- Frame as community protection, not ecoPrimals promotion
- Use SEER as a concrete, non-confrontational example
- Offer to help set up AGPL licensing for community projects
- If pressed on specifics, point to primals.eco licensing page

---

## What Kevin Gains

- **New evolution ecosystem**: ABG members become selective pressure on
  ecoPrimals tools. If they can't use it, it needs to evolve.
- **Peer validation**: Real bioinformaticians testing real tools on real
  problems. This is external validation that no amount of internal testing
  replaces.
- **sporePrint signal**: Every confusion point surfaces documentation gaps.
  The website gets better from every failed explanation.
- **Human disentanglement**: Testing whether the science stands without
  the AI development methodology framing. If Kevin-the-human can
  accelerate this group, the stack works for humans.
- **Potential collaborators**: Especially Everett (Nanopore), iaacornus
  (Rust), BenDiskords/Apep (academic credibility for publications).

---

## What NOT to Do

- Don't lead with ecoPrimals branding or the 4.5M LOC number
- Don't pitch NUCLEUS to people who use Snakemake
- Don't overwhelm a 36-hour-old community with ecosystem architecture
- Don't explain K-NOME unless directly asked about development methodology
- Don't use ecosystem jargon (primals, springs, gates, niches) without
  first testing if it communicates
- Don't treat ABG members as labor for ecoPrimals projects
- Don't mention AI-assisted development unless the conversation goes there
  naturally — it will distract from the science
- Don't bring up Valve, NVIDIA, or Gabe Newell — those are separate tracks
- Let the science and tools speak. Offer help. Be Kevin.

---

*Strategy is a living document. Update after each significant ABG
interaction with observed friction points and sporePrint refinement
targets.*
