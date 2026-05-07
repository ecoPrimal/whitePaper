# ABG Outreach Strategy

**Date**: May 3, 2026
**Status**: Phase 1 — Recon (active)
**Engagement mode**: Human-first. Tamison the microbiologist, not ecoPrimals.
**PII scope**: Contains real-name identity mappings and ABG member
Discord handles with strategic assessments. Internal planning only.

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

ABG interaction is as **Tamison** — the personal online handle. Not as
ecoPrimal (the dev-space identity), not as attsi (the philosopher-space
identity).

| Space | Handle | ABG? | Discoverable? |
|-------|--------|------|--------------|
| Personal | **Tamison** | **Yes** | Volunteered |
| Dev | ecoPrimal | No | Via GitHub if they look |
| Philosophical | attsi | No | Via whitePaper if they dig |

**The framing**:
- "I'm Tamison, a microbiologist with an MS in data science"
- "I built some Rust bioinformatics tools"
- "Happy to help — what are you working on?"

**The medium**: Voice chat, real conversation, human velocity. Text when
appropriate but voice when possible. This is peer interaction, not
documentation.

**The test**: If the science stands on its own when Tamison explains it to
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
- BS Microbiology (Michigan State University)
- MS Data Science
- Army infantry → bench scientist → data scientist → scientific computing
- Extensive research experience across microbiology, genomics, data science
- Strong technical ability (Rust, GPU compute, bioinformatics pipelines)

**Admission message**: See `ABG_INTRO_DRAFTS.md` for the current
version. Short form:
> Hi, I'm Tamison. BS Microbiology and MS Data Science, both
> from Michigan State. Built Rust bioinformatics tools — self-hosted
> pipelines for 16S, metagenomics, GPU-accelerated genomics on consumer
> hardware. Interested in field genomics and environmental eDNA.
> Happy to help where I can.

Keep it short. Don't mention 4.5M lines. Don't mention K-NOME. Don't
mention primals or springs. Be a person.

### Phase 3: Contribute as Tamison

Offer help on their terms, in their language.

**Immediate contributions**:

| Opportunity | ABG Member | What Tamison Offers |
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
  without the name — "AGPL for code, ORC for system mechanics,
  Creative Commons for docs — three independent nonprofits enforce them"
- Only use the term "scyBorg" if they ask what the license is called

### Phase 5: Deeper Collaboration

Joint projects that compose ABG expertise with ecoPrimals validation:

| Project | ABG Members | ecoPrimals Coverage |
|---------|------------|-------------------|
| **PfAAT1 drug resistance (MD + Anderson)** | **Mark, Alistaire, LinearParadox** | **Anderson disorder→transport framework, GPU compute for MD, eigenmode analysis of trajectories, population genetics correlation** |
| **HS-Crohn's immune transcriptomics** | **Jeremy, LinearParadox, Tiptop10** | **Paper 12 Anderson immunological signaling, Fajgenbaum MATRIX scoring, compute for scRNA-seq** |
| Fungal genomics pipeline | BenDiskords + iaacornus | wetSpring WGS/annotation + Rust tooling |
| LTEE structural evolution | Anyone interested in evo bio | Paper 02 + helixVision (8.3M structure predictions) |
| Ocean/cold seep eDNA | Environmental genomics people | Paper 05 + Paper 09 + deep-sea lander architecture |
| Drug discovery on consumer GPU | lilK, MrKostraboski | barraCuda GPU math + docking acceleration |
| Biobank provenance | Nevada | NestGate CAS + loamSpine chain-of-custody |

The **bolded entries** are live proposals from `#project-proposals` where
Tamison can contribute immediately. The others are potential future projects.

These are **joint projects**, not ecoPrimals projects with ABG labor. The
science belongs to everyone involved. Published under AGPL/scyBorg.

### NUCLEUS Gaps Exposed by Active Proposals

Every ABG proposal is expressible as a NUCLEUS composition. The gaps are
at the edges — specific tool integrations and the visualization surface:

| Gap | Exposed By | NUCLEUS Evolution Target |
|-----|-----------|--------------------------|
| GROMACS/OpenMM workloads | Mark's PfAAT1 | toadStool: new workload type |
| 3D molecular visualization | Mark's PfAAT1, bake3011's AF | petalTongue: molecular renderer |
| Live data visualization | ALL proposals | petalTongue: core thesis |
| R runtime dispatch | Jeremy's HS-Crohn's | toadStool: same pattern as Python |
| Large blob storage | Jeremy's ependymoma (h5ad) | NestGate: `storage.store_blob` |
| AlphaFold inference | bake3011's AF | toadStool: inference workload |

These gaps are evolution targets, not blockers. Every workflow can run
today through standard tools on the cluster. The NUCLEUS expression
(toadStool dispatch + NestGate storage + provenance trio + petalTongue
visualization) evolves as each proposal progresses.

---

## sporePrint Refinement Loop

ABG interactions are a live tractability test for primals.eco.

### Tracking Protocol

After each significant ABG interaction, log:

1. **What concept was discussed?**
2. **Did the ABG member understand it from primals.eco?** (Y/N)
3. **Did Tamison have to explain it from scratch?** (Y/N)
4. **What language did Tamison use that worked?** (capture the phrasing)
5. **What primals.eco page should have done this job?** (URL)

### Candidate Pages for Tractability Audit

| Concept | Current Page | Predicted Failure Mode | Status (May 2026) |
|---------|-------------|----------------------|-------------------|
| scyBorg | Knowledge Commons + dedicated page | Name is opaque. "Triple license" means nothing to a grad student. | **Fixed** — dedicated `/methodology/scyborg-licensing/` page, footer shows all 3 licenses |
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
- ABG member uses a tool without Tamison guiding them through it
- ABG member proposes a project that composes ecoPrimals tools

### Failure Signals

- Tamison has to explain the same concept repeatedly in voice
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
2. System mechanics published under **ORC** (Open RPG Creative — irrevocable)
3. Documentation and papers under **CC-BY-SA 4.0**

Effect: Anyone (including SEER) who builds on community work must share
their modifications. The more they extract, the more they must contribute.
The commons gets stronger from every commercial actor that touches it.

### How to Raise This

- Wait for trust. Don't bring it up on day one.
- Frame as community protection, not ecoPrimals promotion
- Use SEER as a concrete, non-confrontational example
- Offer to help set up AGPL licensing for community projects
- If pressed on specifics, point to primals.eco/methodology/scyborg-licensing/
  (dedicated page now live — explains orthogonal triple with plain language)

---

## What Tamison Gains

- **New evolution ecosystem**: ABG members become selective pressure on
  ecoPrimals tools. If they can't use it, it needs to evolve.
- **Peer validation**: Real bioinformaticians testing real tools on real
  problems. This is external validation that no amount of internal testing
  replaces.
- **sporePrint signal**: Every confusion point surfaces documentation gaps.
  The website gets better from every failed explanation.
- **Human disentanglement**: Testing whether the science stands without
  the AI development methodology framing. If Tamison-the-human can
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
- Let the science and tools speak. Offer help. Be Tamison.

---

## Design Insight: The Work Is the Presentation (May 5, 2026)

ABG's `#project-proposals` channel (6 proposals captured in
`ABG_thread3.md`) reveals a pattern: every methodology section ends with
"make clean figures and release code" as a final step. This is backwards.

**The petalTongue thesis**: If every computation runs through NUCLEUS and
renders live through petalTongue, there is no separate figure-making step.
The scRNA-seq UMAP renders as it clusters. The DEG volcano plot updates as
each dataset processes. The MD simulation trajectory is visible as it runs.
The provenance chain is visible alongside the data. The work itself IS the
presentation.

This matters for ABG because:

1. **Figures become live views**: A paper figure is a screenshot of the
   live computation surface, not a matplotlib plot generated after the fact
2. **"Released code" becomes a deploy graph**: The TOML that describes the
   computation is the reproduction artifact. Anyone with a NUCLEUS can
   re-run it.
3. **Computation is connectable**: petalTongue doesn't just show results —
   it shows the connections between computations. Click a gene in a volcano
   plot, see its expression across all datasets, see the pathway it belongs
   to, see the provenance chain that produced it.

This is not an outreach pitch. It is a design target for NUCLEUS. When ABG
members eventually use the compute, they experience the visualization
naturally — not because they were told about petalTongue, but because the
computation surface is inherently visual.

### Social Solves vs. Structural Solves

Every ephemeral social solution ABG uses has a permanent structural
equivalent:

| Social Solve (ephemeral) | Structural Solve (permanent) |
|--------------------------|------------------------------|
| Google Colab subscription | toadStool dispatch on sovereign hardware |
| Google Docs for plans/methods | loamSpine certificates for methodology |
| Discord `#project-proposals` | biomeOS deploy graphs |
| Manual authorship agreement | sweetGrass radiating attribution braids |
| "Make figures" as final step | petalTongue: computation IS the figure |
| bioRxiv preprint for priority | loamSpine timestamp + sweetGrass witness |
| Channel per project | Composition per project (NUCLEUS deploy graph) |
| rosie reviewing proposals | primalSpring validating compositions |

The social solutions are valuable — Discord is real coordination, Google
Docs are real collaboration. But they don't persist, aren't verifiable,
aren't composable, and don't scale. The structural equivalents do all four.

**The strategy implication**: Don't pitch the structural solutions. Let ABG
members experience the social solutions hitting their limits — and when
they do, the structural alternative already exists, proven and waiting. The
compute comes first. The visualization comes with it. The provenance and
attribution emerge as needs surface.

---

## Timing Update (May 5, 2026)

The `#general` thread (captured in `ABG_thread2.md`, analyzed in
`ABG_ANALYSIS.md`) shows the community actively forming project
directions and hitting compute/infrastructure walls in real time.

**Key developments**:
- rosie set a **~May 9 AoE deadline** for project proposals
- Jeremy and bake3011 are actively scoping scRNA-seq and HD biomarker projects
- Vividshades wants pathway discovery collaborators
- Compute question was raised and answered with "Google Colab" — the exact
  dependency that sovereign compute sharing eliminates
- LinearParadox (5-year drug lab practitioner, scRNA-seq/ATAC-seq experience)
  is in the community but hasn't connected to the value proposition — a
  sporePrint communication signal

**Timing implication**: Phase 2 (join legitimately) should happen before
the proposal deadline. Joining after proposals are locked reduces the
compute contribution opportunity. The `#general` intro draft in
`ABG_INTRO_DRAFTS.md` is already responsive to the compute question.

**Provenance pipeline relevance**: The just-completed provenance pipeline
elevation (Nest Atomic, 9 primals, BLAKE3 → rhizoCrypt → loamSpine →
sweetGrass) is now operational evidence that could be shared when
ABG members hit reproducibility or attribution problems. This is a
Phase 4-5 card, not a Phase 2-3 card — don't lead with provenance
architecture. But when bake3011 worries about scooping, or when the
group debates authorship rules, the structural solution exists and
is proven.

---

---

## gen4 Unified Foundation Backing (May 2026)

ABG is connected to the gen4 **unified foundation** — one interconnected
lineage of 28 baseCamp papers, 8 springs, and 12+ contacts mapped in
`gen4/foundations/THE_UNIFIED_LINEAGE.md`. The whole-cell modeling
rebuild (`gen4/foundations/ABG_WHOLE_CELL_REBUILD.md`) is **Thread 1**
of this foundation — the first expression document.

**Outreach implication**: The unified foundation means every ABG
proposal connects to validated infrastructure, not just whole-cell
modeling. Mark's MD proposal connects to Thread 2 (plasma physics —
hotSpring 195+ checks, same barraCuda GPU kernels). Jeremy's
transcriptomics connects to Thread 4 (environmental genomics —
wetSpring 6,656+ checks). bake3011's AlphaFold connects to Thread 5
(evolutionary biology — coralForge 154 checks). The foundation is one
graph; ABG proposals are entry points into different threads.

**Timing**: The unified lineage map and Thread 1 expression are
analysis-complete. Spring experiments implementing the blueprints are
the next phase. Tamison can reference specific validated patterns for
any ABG proposal — not just whole-cell modeling.

---

*Strategy is a living document. Update after each significant ABG
interaction with observed friction points and sporePrint refinement
targets.*
