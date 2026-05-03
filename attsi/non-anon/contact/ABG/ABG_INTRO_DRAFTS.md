# ABG Introduction Drafts

**Date**: May 3, 2026
**Status**: Draft — review before sending

---

## Identity Context

| Space | Handle | Notes |
|-------|--------|-------|
| **Personal / online** | Tamison | Kevin as a human on the internet. ABG, Discord, Reddit. |
| **Dev space** | ecoPrimal | Kevin + synthetic intelligence via K-NOME. GitHub, code, technical. |
| **Philosopher space** | attsi | "a tool that shapes itself" (lowercase name and acronym). whitePaper, outreach, conceptual. |

ABG interaction is as **Tamison** — the personal handle. Not ecoPrimal
(too close to the ecosystem name), not attsi (too abstract for a
bioinformatics Discord).

---

## Admissions Channel Blurb

```
Hey everyone, I'm Kevin (Tamison).

BS Microbiology and MS Data Science, both from Michigan State. 5+ years
on the bench — fermentation lab (fungi, mycobacteria, anaerobes, GMOs),
PFAS research, and a summer at Sandia National Labs working on algal
bioinformatics with high-throughput sequencing. Army infantry before
all of that.

I've been building bioinformatics and scientific computing tools in
Rust — sovereign pipelines for 16S analysis, metagenomics, and
GPU-accelerated genomics that run on consumer hardware through Vulkan.
No CUDA dependency, no cloud, no Python runtime. I run everything on
a home cluster of ~11 machines with RTX 3090s, Titan Vs, EPYC, and
neuromorphic chips, all under AGPL-3.0 (open source, copyleft — anyone
can use and build on it, but modifications stay open).

Research interests: environmental eDNA, cold seep metagenomics, field
genomics with nanopore sequencing, protein structure prediction on
consumer GPUs, and microbial quorum sensing.

Happy to help with anything compute, pipeline, or Rust related. Also
happy to just talk science.
```

**Notes**:
- Leads with bench science and credentials (what ABG screens for)
- "Army infantry before all of that" — humanizes, doesn't dwell
- Hardware described as aggregate, no gate names, no ecosystem jargon
- "sovereign" used once, in a clear context ("sovereign pipelines").
  primals.eco now uses "self-hosted" on key pages, but "sovereign
  pipelines" is fine in conversational context — it's descriptive here
- AGPL explained inline ("open source, copyleft — modifications stay open")
- No mention of: ecoPrimals, primals, springs, NUCLEUS, K-NOME, barraCuda,
  coralReef, 4.5M LOC, 1,145 shaders, Valve, NVIDIA, or AI-assisted development
- Research interests map directly to papers 01, 02, 05, 09 without naming them
- "Happy to help" — contribution posture, not pitch
- If someone follows to primals.eco, the glossary page is now the
  first sidebar item — provides immediate term disambiguation

---

## DM to rosie

```
Hey rosie — Kevin (Tamison) here, just dropped my intro in admissions.

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
- Protein structure prediction pipeline — AlphaFold2/3 equivalent in
  pure Rust, validated to 1e-10 against NumPy, runs on consumer GPUs
  at ~$0.0001/prediction vs $0.01 on Google's API
- I run this on a home cluster (~11 machines, heterogeneous —
  consumer GPUs, server-grade EPYC, neuromorphic NPUs for edge
  classification)

Everything is licensed under an AGPL-3.0 triple (code is AGPL,
docs are CC-BY-SA, game mechanics under ORC). The short version:
all of it is permanently open, anyone can use it, but if you build
on it commercially you have to share your modifications. I think
this matters for a research community — I noticed a commercial AI
startup (Seer) in the admissions channel, and AGPL is how you make
sure community work stays in the commons even when commercial
entities are watching.

I'm not here to pitch anything — I genuinely want to help people
who are doing the science but hitting compute walls or pipeline
limitations. If you have members working on nanopore, metagenomics,
or structure prediction, I'd love to connect. Also happy to help
with any Rust or GPU compute questions.

The project site is primals.eco if you're curious, but honestly
the best way to see the work is to clone a repo and run the tests.

Looking forward to contributing.
— Kevin (Tamison)
```

**Notes**:
- More detail than the public blurb, but still not the full hand
- Specific check counts (6,600+), metagenome numbers (170, 299K QS genes),
  validation tolerance (1e-10) — these are credibility signals for a
  researcher
- AGPL explanation is practical, not ideological: "this is how you protect
  community work from commercial extraction"
- SEER mentioned obliquely: "I noticed a commercial AI startup in the
  admissions channel" — plants the seed without being confrontational
- primals.eco linked but downplayed: "honestly the best way is to clone
  and run the tests" — executable proof over website polish. If they do
  visit, the site now has:
  - **Glossary** (first sidebar item) — plain definitions for all terms
  - **Products section** — clarifies "chemical reaction product, not
    commercial software"
  - **helixVision page** — now says "self-hosted" not "sovereign"
  - **Science papers** — cleaned-up status blocks (no more Exp### build logs)
- No mention of: ecoPrimals by name, primal/spring terminology, NUCLEUS,
  K-NOME, AI-assisted development, 4.5M LOC, 1,145 shaders, Valve, NVIDIA
- "I'm not here to pitch anything" — explicitly anti-pitch posture
- Ends with contribution offer and a sign-off

---

## What's Held Back (for Later Interactions)

These are cards not played in the intro. They come out naturally as
conversations deepen:

| Card | When to Play |
|------|-------------|
| Full ecosystem scale (4.5M LOC, 1,145 shaders) | When someone asks "how much have you built?" |
| K-NOME methodology | When someone asks "how did one person build all this?" |
| ecoPrimals ecosystem name and architecture | When someone visits primals.eco and asks about the structure |
| NVIDIA sovereign dispatch (coralReef) | When someone hits CUDA dependency pain |
| helixVision by name | When someone discusses AlphaFold costs or cloud dependency |
| Valve/Gabe outreach | Never in ABG context — separate track entirely |
| metalMatrix cluster detail | When someone asks about hardware setup |
| NPU/AKD1000 work | When someone works on edge deployment or Nanopore |
| Deep-sea autonomous lander | When ocean/marine eDNA comes up |
| LTEE structural evolution project | When evolutionary biology comes up |
| scyBorg by name | When someone asks what the license model is called |
