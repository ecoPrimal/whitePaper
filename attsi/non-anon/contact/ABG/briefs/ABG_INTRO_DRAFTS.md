# ABG Introduction Drafts

**Date**: May 3, 2026
**Status**: Draft — review before sending
**PII scope**: This document contains real-name-to-handle mappings and
personal credentials. It is internal planning only — never share this
file or its contents outside the `non-anon` context. The intro blurb and
DM are the shareable artifacts; the notes and identity table are not.

---

## Identity Context

| Space | Handle | What it sees | ABG? |
|-------|--------|-------------|------|
| **Personal** | Tamison | The human on the internet. Discord, Reddit, voice. | **Yes** |
| **Dev** | ecoPrimal | Tamison + K-NOME. GitHub, code, technical. | No — too close to ecosystem name |
| **Philosophical** | attsi | "a tool that shapes itself." whitePaper, outreach. | No — too abstract for bioinformatics |

ABG interaction is as **Tamison** — the personal handle. The other two
identities are not introduced unless a conversation naturally leads there.
If someone finds the GitHub org, the connection is discoverable but not
volunteered.

---

## Admissions Channel Blurb

```
Hey everyone, I'm Tamison.

BS Microbiology and MS Data Science, both from Michigan State. 5+ years
on the bench — fermentation lab (fungi, mycobacteria, anaerobes, GMOs),
PFAS research, and a summer at Sandia National Labs working on algal
bioinformatics with high-throughput sequencing. Army infantry before
all of that.

I've been building bioinformatics and scientific computing tools in
Rust — sovereign pipelines for 16S analysis, metagenomics, and
GPU-accelerated genomics that run on consumer hardware through Vulkan.
No CUDA dependency, no cloud, no Python runtime. I run everything on
a home cluster of ~11 machines with RTX 3090s and other consuemr cards, Titan Vs, EPYC, and
neuromorphic chips, all under AGPL-3.0 (open source, copyleft — anyone
can use and build on it, but modifications stay open).

Research interests: environmental eDNA, cold seep metagenomics, field
genomics with nanopore sequencing, protein structure prediction on
consumer GPUs, and microbial quorum sensing.

Some of the work is written up at primals.eco/science/ if you want
to see the research side.

Happy to help with anything compute, pipeline, or Rust related. Also
happy to just talk science.
```

**Notes**:
- Leads with bench science and credentials (what ABG screens for)
- "Army infantry before all of that" — humanizes, doesn't dwell
- Hardware described as aggregate, no gate names, no ecosystem jargon
- "sovereign" used once, in a clear context ("sovereign pipelines").
  primals.eco uses "self-hosted" on key pages, but "sovereign
  pipelines" is fine in conversational context — it's descriptive here
- AGPL explained inline ("open source, copyleft — modifications stay open")
- No mention of: ecoPrimals, primals, springs, NUCLEUS, K-NOME, barraCuda,
  coralReef, 4.5M LOC, 1,145 shaders, Valve, NVIDIA, or AI-assisted development
- Research interests map directly to papers 01, 02, 05, 09 without naming them
- `primals.eco/science/` linked — points to research papers, not architecture
  or ecosystem overview. Bioinformaticians care about the science, not the
  infrastructure. Glossary link omitted from blurb (it's for people already
  exploring the site). GitHub omitted (org name reveals ecoPrimals branding).
- "Happy to help" — contribution posture, not pitch
- If someone follows to primals.eco, the site has:
  - Glossary (first sidebar item) — plain definitions for all terms
  - scyBorg licensing page — explains orthogonal triple in plain language
  - "Self-hosted" language throughout key pages
  - Products section — disambiguates "chemical reaction product"

---

## DM to rosie

```
Hey rosie — Tamison here, just dropped my intro in admissions.

Wanted to give you a bit more context on what I bring. I've been doing
bench microbiology for years (fermentation, PFAS, algal bioinformatics
at Sandia) and pivoted hard into computational work through my MS in
data science. Since then I've built a fairly substantial set of Rust
bioinformatics tools:

- A sovereign 16S pipeline (DADA2-equivalent, validated with 6,600+
  automated checks against standard tools) — no QIIME2, no Python
- GPU-accelerated genomics on consumer hardware through Vulkan — the
  idea is that a grad student's gaming GPU can do real science without
  HPC allocation
- Metagenomics work — I've analyzed 170 cold seep metagenomes
  (299,000+ quorum sensing genes, 34 QS types) using an Anderson
  localization framework from condensed matter physics
- Working on protein structure prediction in pure Rust — math
  primitives validated to 1e-10 against NumPy, targeting consumer
  GPU inference so you don't need Google's API
- I run this on a home cluster (~11 machines, heterogeneous —
  consumer GPUs, server-grade EPYC, neuromorphic NPUs for edge
  classification)

Everything is licensed under a triple copyleft (code is AGPL-3.0,
system mechanics under ORC, docs are CC-BY-SA 4.0). Three
independent nonprofits enforce the three licenses — no single
entity can revoke any of them. The short version: all of it is
permanently open, anyone can use it, but if you build on it
commercially you have to share your modifications. I think this
matters for a research community — I noticed a commercial AI
startup (Seer) in the admissions channel, and copyleft is how you
make sure community work stays in the commons even when commercial
entities are watching.

I'm not here to pitch anything — I genuinely want to help people
who are doing the science but hitting compute walls or pipeline
limitations. If you have members working on nanopore, metagenomics,
or structure prediction, I'd love to connect. Also happy to help
with any Rust or GPU compute questions.

The project site is primals.eco if you're curious, but honestly
the best way to see the work is to clone a repo and run the tests.

Looking forward to contributing.
— Tamison
```

**Notes**:
- More detail than the public blurb, but still not the full hand
- Specific check counts (6,600+), metagenome numbers (170, 299K QS genes)
  are validated completed work — credibility signals for a researcher
- Structure prediction is framed as "working on" with validated math
  primitives, not as a finished AlphaFold replacement. No cost projection
  — that's aspirational until inference pipeline is end-to-end
- Triple copyleft explanation is practical, not ideological: "this is how
  you protect community work from commercial extraction"
- "Three independent nonprofits" — conveys irrevocability without jargon
- SEER mentioned obliquely: "I noticed a commercial AI startup in the
  admissions channel" — plants the seed without being confrontational
- primals.eco linked but downplayed: "honestly the best way is to clone
  and run the tests" — executable proof over website polish. If they do
  visit, the site has:
  - **Glossary** (first sidebar item) — plain definitions for all terms
  - **scyBorg licensing page** — dedicated orthogonal triple explanation
  - **Products section** — disambiguates "chemical reaction product"
  - **helixVision page** — says "self-hosted" not "sovereign"
  - **Science papers** — cleaned-up status blocks, human-readable summaries
  - **Footer** — shows all three licenses (AGPL, ORC, CC-BY-SA)
- No mention of: ecoPrimals by name, primal/spring terminology, NUCLEUS,
  K-NOME, AI-assisted development, 4.5M LOC, 1,145 shaders, Valve, NVIDIA
- "I'm not here to pitch anything" — explicitly anti-pitch posture
- Ends with contribution offer and a sign-off

---

## #general Introduction (Post-Admission)

```
Hey all — Tamison, just got admitted. Catching up on the thread.

(This message was drafted with AI — almost all my long-form
writing goes through AI tools. I'm here as a human though, happy
to voice chat or pair on problems anytime.)

Saw the compute question come up. I have a LAN cluster I can put
toward group projects — all local, no cloud:

- Dual EPYC 7452 (64c/128t, 256 GB ECC) — eats scRNA-seq,
  alignment, Kraken2
- Threadripper 3970X (32c/64t, 256 GB) + Titan Vs (HBM2) —
  heavy matrix ops, structure prediction
- GPU pool: RTX 5090, 3090s, MI50s, etc. — ~248 GB VRAM total,
  cards move between machines based on workload
- 3× BrainChip Akida NPUs — edge inference, adaptive sampling
- 76 TB ZFS cold storage + ~46 TB NVMe, 2G backbone (10G backbone in progress)
- Total: 11 machines, ~154 cores, ~1 TB RAM

Happy to run whatever standard tools your projects need — QIIME2,
DESeq2, Scanpy, Snakemake, AlphaFold, whatever. Use the tools
you know.

The transparent part: I also build Rust bioinformatics pipelines,
and my pattern is to reproduce published results in Python /
standard tools first, then reimplement in Rust. Examples:

- 16S: reproduced DADA2 in Python, then Rust — 6,600+ checks
  (primals.eco/science/, papers 01, 05)
- Immunological signaling: reproduced Gonzales (MSU Pharmacology)
  PK/dose-response in Python, then Rust — 329 checks
  (primals.eco/science/, paper 12)
- Metagenomics: 170 cold seep metagenomes, standard tools first,
  then Rust — 299K QS genes, 34 types (paper 05)

So your projects on this hardware produce the first stage of my
pipeline — your QIIME2 run becomes ground truth for my Rust 16S,
your DESeq2 output becomes a validation target. You get compute,
I get real-world data to evolve my tools. Your science drives the
direction. Mutual.

AGPL-3.0 — not worried about citation or scooping, the license
handles it structurally.

DM me if you need compute.
```

**Notes**:
- Responds directly to the compute thread (bake3011 line 51: "is the
  resource available though", rosie line 77-78: "your responsibility
  to get funding for compute ... Google Colab")
- **Hardware profiled by role** — not just specs but what each tier
  does. "This machine eats scRNA-seq" tells a bioinformatician more
  than "Dual EPYC" alone. Organized: bioinformatics workhorse, heavy
  compute/HBM2, GPU pool, edge/neuromorphic, storage. Cards move
  between machines — the heterogeneity is the feature.
- **"Run whatever standard tools you know"** — critical framing. Not
  asking anyone to switch to Rust. QIIME2, DESeq2, Scanpy, Snakemake,
  AlphaFold — all named explicitly. Use your tools, I provide hardware.
- **Springs reframed as validation targets**: "every result you
  produce in standard tools becomes a validation target for my Rust
  equivalents." This is literally what springs do — but described as
  a natural consequence, not a framework. Their QIIME2 runs become
  wetSpring ground truth. Their DESeq2 output becomes healthSpring
  test data. Their science drives the evolution direction.
- **AI disclosure** moved to top of message, before hardware.
- **LAN cluster concept**: "all local, LAN-networked, no cloud."
- Gate names still omitted (strandGate → "bioinformatics workhorse",
  biomeGate → "heavy compute / HBM2", westGate → "cold storage on
  ZFS"). Gate names come out when someone asks about the architecture.
- "DM me" still the Phase 3 funnel.

---

## #project-proposals Contribution (Response to Active Proposals)

```
(AI-drafted, as with my other posts — I'm the human behind it.)

Not submitting a standalone proposal yet, but wanted to flag some
overlap with what's already on the table. I have prior work and
compute that could contribute to existing proposals:

**@Mark — MD simulation of PfAAT1 / chloroquine resistance**
This one's exciting. I have a physics framework from condensed
matter — Anderson localization — that models how disorder affects
transport. The mutations in PfAAT1 that confer resistance are
literally introducing disorder into a transport channel. The
framework maps directly:

- Disorder parameter (W) = mutation load in the transporter
- Transport = drug flux through the channel
- Localization transition (W_c) = the threshold where
  accumulated mutations block drug transport entirely

I've validated this framework for cytokine transport through skin
tissue (IC50 curves map to Anderson barrier heights) and can offer
both the physics analysis and the compute for MD. My GPU pool
(RTX 5090, 3090s, Titan Vs with HBM2) can run GROMACS/OpenMM
without needing Colab or HPC allocation. Also have eigenmode
decomposition tools that could analyze MD trajectories for the
open/closed channel modes — the spectral signatures should
distinguish resistant vs. sensitive conformations.

The population genetics angle is interesting too — the critical
disorder threshold W_c should predict which mutation combinations
confer resistance, and that should correlate with the field
epidemiology data you mentioned. Would love to discuss.

Write-up: primals.eco/science/ (papers 01, 12 — Anderson
framework applied to microbial signaling and immunological drug
transport)

**@Mark — PTP expression in metastatic cancers**
I can contribute compute for the transcriptomics screening and
have pipelines for large-scale gene expression analysis. Happy
to help parallelize the work across cancer types.

**@Jeremy — HS-Crohn's shared transcriptomic programs**
I have validated work applying the same Anderson localization
framework to immunological signaling — specifically cytokine
propagation through tissue (IL-4, IL-13, IL-31, Th2 pathways).
It includes a drug repurposing scoring pipeline validated against
published data. The immune pathway overlap with IL-17/TNF in your
proposal is significant — the Anderson framework could add a
spatial/physics layer to the standard DESeq2 + pathway enrichment
approach. LinearParadox's suggestion to use scRNA-seq instead of
deconvolution is right — I can offer compute for that.

Write-up: primals.eco/science/ (paper 12, immunological Anderson)

**@Jeremy — ependymoma scRNA-seq meta-analysis**
I can offer compute — dual EPYC (64 cores, 256 GB ECC RAM)
handles scRNA-seq workloads without Colab. Happy to run jobs.

**@bake3011 — TMS/Huntington's biomarker prediction**
Solid proof-of-concept project. LinearParadox's LASSO suggestion
is good — I have GPU-accelerated L1-regularized optimization
that could speed up the feature selection across the full
transcriptome. Happy to contribute compute and methodology.

**@bake3011 — AlphaFold / large protein structures**
I've been building protein structure prediction math in Rust —
GPU-accelerated primitives validated to 1e-10 against NumPy.
Not a finished AlphaFold replacement but the math layer is solid
and I have consumer GPUs that can run inference without API costs.
Alistaire's domain-splitting approach is smart — I could
contribute to the compute side of that.

**General offer**
I have validated pipelines across microbiology, genomics, physics,
and immunology — ~6,600 automated checks on the 16S pipeline
alone, 329 checks on the immunological work. I also have 170
analyzed cold seep metagenomes (299K quorum sensing genes across
34 QS types) if anyone's interested in environmental genomics.

All of this is AGPL-3.0 — use it, build on it, no restrictions
except sharing modifications back. Compute is available for any
approved project.
```

**Notes**:
- **AI disclosure** repeated — consistent with #general post.
- **Mark's MD proposal leads** — this is the most distinctive,
  non-substitutable contribution. Anderson disorder→transport
  framework is genuinely novel for drug resistance analysis.
  Nobody else in ABG can offer this physics lens.
- **Anderson explained in their language**: "mutations introduce
  disorder into a transport channel" — not "the disorder parameter
  W in a tight-binding Hamiltonian." Meet them where they are.
- **GPU pool described by capability**, not gate names. "RTX 5090,
  3090s, Titan Vs with HBM2" — hardware bioinformaticians
  understand. No mention of metalMatrix, strandGate, etc.
- **LinearParadox's scRNA-seq suggestion for HS-Crohn's** is
  acknowledged — shows Tamison is reading the thread and agrees
  with the strongest technical voice in the room.
- **primals.eco/science/** linked for the Anderson papers. Points
  to specific papers by content description, not ecosystem numbers.
- **Credibility numbers**: 1e-10 validation, 6,600 checks, 329
  checks, 170 metagenomes, 299K QS genes.
- **Contribution posture** throughout — "happy to contribute,"
  "would love to discuss," "I'd want to understand your methodology."
- Still no mention of: ecoPrimals, primals, springs, NUCLEUS,
  K-NOME, helixVision, barraCuda, gate names, petalTongue. The
  NUCLEUS capability is delivered without the NUCLEUS branding.
- The **petalTongue vision** (computation as live visualization)
  is not mentioned in the public post — it's a design target for
  NUCLEUS, not an outreach pitch. When ABG members eventually use
  the compute, they'll experience the visualization naturally.

---

## What's Held Back (for Later Interactions)

These are cards not played in the intro. They come out naturally as
conversations deepen:

| Card | When to Play |
|------|-------------|
| Full ecosystem scale (4.5M LOC, 1,145 shaders) | When someone asks "how much have you built?" |
| K-NOME methodology | **Partially played** — "I use AI tools heavily for development" disclosed. K-NOME name and full methodology still held. |
| ecoPrimals ecosystem name and architecture | When someone visits primals.eco and asks about the structure |
| NVIDIA sovereign dispatch (coralReef) | When someone hits CUDA dependency pain |
| helixVision by name | **Partially played** — structure prediction math described without the name. Full helixVision branding still held. |
| Valve/Gabe outreach | Never in ABG context — separate track entirely |
| metalMatrix cluster detail | **Played** — full specs shared in #general (154 cores, 1 TB RAM, 248 GB VRAM, 76 TB storage, 10G backbone). Gate names and metalMatrix branding still held. |
| NPU/AKD1000 work | **Partially played** — "3× neuromorphic chips" mentioned. Specific validation results (18.8K Hz, coin-cell 11 years) still held. |
| Deep-sea autonomous lander | When ocean/marine eDNA comes up |
| LTEE structural evolution project | When evolutionary biology comes up |
| Spring names and catalog | **Partially played** — "validation environments that validate against published results" disclosed. Spring names (hotSpring, wetSpring, etc.) and catalog still held. |
| scyBorg by name | When someone asks what the license model is called. primals.eco/methodology/scyborg-licensing/ now live — link if asked |
| NUCLEUS as compute substrate | When ABG members experience the compute working and ask how it's organized. Not pitched — experienced. |
| Provenance pipeline | When bake3011 worries about scooping, or when authorship rules hit limits. The structural solution (loamSpine timestamps, sweetGrass braids) exists and is proven. Phase 4-5 card. |
| petalTongue live visualization | When someone says "make figures." The computation IS the figure — but don't explain this abstractly. Show it working. |
| Anderson for Mark's PfAAT1 | **Played in proposals draft** — disorder→transport framework explained in their language. Full Paper 01/12 depth still held for deeper conversation. |
