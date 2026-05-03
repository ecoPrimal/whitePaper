# sporePrint Tractability Audit — ABG Mirror

**Date**: May 3, 2026
**Status**: Initial audit (pre-engagement). Will be updated as ABG
interactions surface real confusion points.
**Purpose**: Identify concepts on primals.eco that will confuse ABG
members and track what needs rewriting.

---

## The Test

If an ABG member — a grad student in bioinformatics who uses Python,
QIIME2, and Snakemake — visits primals.eco and can understand what
a tool does and how to use it without Kevin explaining it in voice,
the page passes. If Kevin has to translate, the page fails.

---

## Landing Page Assessment

**Page**: `content/_index.md` (primals.eco root)

**Strengths**:
- "Try It" in 5 minutes with `cargo test` — excellent. Executable proof.
- "Run real scientific pipelines locally" — clear value proposition
- "Use any GPU — NVIDIA, AMD, Intel — no CUDA lock-in" — speaks to a
  real pain point for students who can't afford CUDA hardware or HPC access
- "Own your data and compute — nothing leaves your machine" — clear

**Weaknesses**:
- "guideStone artifact" — what is a guideStone? A grad student expects
  a tar.gz with binaries and a README, not a branded verification concept
- "{{ entity(name="ecoprimals") }}" Tera template renders to a styled name on-site — may
  look like branding over substance to skeptical academics
- "175+ papers across 8 domains" — impressive but unverifiable from the
  landing page. Where are they? Peer-reviewed? Preprints? baseCamp papers?

**Verdict**: Passes for the "curious engineer" audience. Marginal for the
"skeptical academic" audience (which ABG includes: professors, PhD students).

---

## Concept Tractability Matrix

### Critical (Will Confuse ABG Members)

| Concept | Current Name | Problem | What a Bioinformatician Expects | Suggested Fix |
|---------|-------------|---------|-------------------------------|---------------|
| **License** | scyBorg | Name is opaque. No one outside the ecosystem knows what this means. Sounds like a cyborg. | "AGPL triple license" or just "AGPL-3.0 + CC-BY-SA" | Always lead with the components, use "scyBorg" parenthetically at most |
| **The binaries** | primals | "Primal" sounds like gaming/fantasy terminology. A bioinformatician expects "tools," "pipelines," or "binaries." | "Rust CLI tools" or "standalone binaries" | On bioinformatics-facing pages, use "tools" first, introduce "primals" as the ecosystem term |
| **Validation environments** | springs | Immediate collision with Java Spring Framework. Every software person will flinch. A bioinformatician expects "benchmarks," "test suites," or "validation sets." | "Validation environments" or "test domains" | On first reference, say "springs (domain-specific validation environments)" |
| **Machines / nodes** | gates | "Gate" means logic gate (EE), network gateway (IT), or security checkpoint (infosec). A bioinformatician expects "node," "machine," or "server." | "Node" or "machine" | Use "node" in external-facing docs, keep "gate" internally |
| **Sovereign** | Used pervasively | Politically loaded. "Sovereign citizen" connotations in US context. Some academics will assume conspiracy/libertarian framing. A bioinformatician expects "local," "self-hosted," or "no cloud dependency." | "Self-hosted," "local-first," or "cloud-independent" | Test in ABG conversations. If anyone flinches, rewrite. |

### Moderate (May Confuse, Testable)

| Concept | Current Name | Problem | Suggested Fix |
|---------|-------------|---------|---------------|
| **Composition model** | NUCLEUS | Sounds like an enterprise acronym. The Tower/Node/Nest atomic model is elegant but requires reading the architecture page to understand. | For ABG: don't mention NUCLEUS. Describe what the tools do, not how they compose. |
| **Self-verifying artifacts** | guideStone | Branded name for "reproducible build with embedded tests." ABG members expect "reproducible pipelines" or "Snakemake workflows." | "Self-verifying artifact" is fine; "guideStone" needs parenthetical explanation on first use |
| **Deploy configurations** | niches | Ecological metaphor, but overloaded in business/CS. | Use "deploy configuration" or "composition" externally |
| **Bonded collectives** | Plasmodium | Beautiful biological metaphor but requires mycology knowledge to appreciate. Also sounds like malaria parasite to a microbiologist. | Test with ABG — Bealzebuddy works on malaria and may react to this name |
| **AI-assisted development** | K-NOME | Opaque acronym. "Knowledge-Numeric Observed & Mentored Evolutionary Programming" is 7 words of jargon. | Don't mention unless asked. Say "I use AI tools to help write code." |

### Low Risk (Clear or Self-Explanatory)

| Concept | Current Name | Notes |
|---------|-------------|-------|
| **Math engine** | barraCuda | Name is a pun on CUDA but communicates "GPU compute." Clear enough. |
| **GPU compiler** | coralReef | Doesn't self-explain, but not misleading either. |
| **Networking** | songBird | Doesn't self-explain, but the mesh/federation metaphor works. |
| **Storage** | nestGate | "Nest" + "Gate" suggests protected storage. Reasonably intuitive. |
| **Crypto** | bearDog | Doesn't self-explain but names rarely do for crypto libraries. |

---

## Page-by-Page ABG Relevance

Pages an ABG member might visit, ranked by likelihood:

| Page | ABG Relevance | Tractability Risk |
|------|--------------|-------------------|
| **Landing page** | First impression | Low — "Try It" is strong |
| **helixVision product page** | High — structure prediction | Moderate — "product" means something different here |
| **Science papers (02, 05, 09)** | High — LTEE, cold seep, field genomics | Low — these are standard scientific writing |
| **Primal Catalog** | Medium — if exploring architecture | High — dense, ecosystem jargon throughout |
| **NUCLEUS Architecture** | Low — only if deeply curious | Very high — requires ecosystem context |
| **Knowledge Commons Targets** | Medium — if interested in licensing | Moderate — scyBorg name, but AGPL explanation is clear |
| **Ecosystem Architecture** | Low — deep dive | Very high — UniBin/ecoBin/genomeBin ladder is internal |

---

## The "Product" Disambiguation

ABG members (and Gabe, and NVIDIA engineers) will interpret "product"
as "thing you sell." In ecoPrimals, "product" means "chemical reaction
product" — an emergent composition of primals that does something
useful. helixVision is not a product to buy. It's what happens when you
compose barraCuda + coralReef + toadStool + NestGate + loamSpine and
point them at genomic data.

This distinction matters enormously for ABG engagement. If Kevin says
"I have a product called helixVision," the ABG grad student hears
"you're selling me something." If Kevin says "I built a protein
structure prediction pipeline in Rust that runs on your gaming GPU,"
the grad student hears "free tool that helps me."

**Recommendation**: On bioinformatics-facing pages and in ABG
conversations, never use "product" without immediately clarifying
the chemical reaction metaphor. Or just don't use the word at all.

---

## Tracking Log (Update After Each ABG Interaction)

| Date | Concept Discussed | Understood from Site? | Kevin Had to Explain? | What Phrasing Worked? | sporePrint Page Needing Work |
|------|------------------|----------------------|----------------------|----------------------|------------------------------|
| — | — | — | — | — | — |

*Fill in rows as ABG interactions occur. Each row is a data point for
sporePrint refinement.*

---

## Priority Refinement Targets

Based on this pre-engagement audit, the sporePrint pages most likely
to need rewriting for external tractability:

1. **scyBorg explanation** — ~~Needs a plain-language page~~ **DONE** (May 2026):
   Knowledge Commons page now leads with "AGPL-3.0 + ORC + CC-BY-SA 4.0"
   before introducing "scyBorg" parenthetically. Glossary has plain
   definition. "What this means in practice" paragraph added.
2. **helixVision page** — ~~Remove "product" framing~~ **DONE** (May 2026):
   Title changed to "Self-Hosted Structure Prediction." Products section
   now leads with chemical-reaction-product disambiguation.
3. **Primal Catalog introduction** — ~~Add a "What is a primal?"~~ **DONE**
   (May 2026): Plain-English intro added at top with link to glossary.
4. **Landing page "guideStone"** — ~~Add inline explanation~~ **DONE**
   (May 2026): Now reads "self-verifying build artifacts." Glossary link
   added after bullet list.
5. **"Sovereign" usage audit** — ~~Find every instance~~ **DONE** (May 2026):
   Key pages (landing, science index, helixVision, ecosystem architecture)
   now use "self-hosted" or "cloud-independent." Glossary explicitly
   disambiguates. Science index adds inline definition. Hero tagline
   kept as "Sovereign Scientific Computing" (brand identity).
6. **Glossary page** — **DONE** (May 2026): New `/glossary/` section with
   plain-language definitions for all ecosystem terms. First item in
   sidebar navigation.
7. **OG meta number drift** — **DONE** (May 2026): index.html OG/Twitter
   descriptions now pull from `config.extra.totals` instead of hardcoded
   stale numbers.
8. **Duplicate paper 24** — **DONE** (May 2026): esotericWebb renumbered
   to paper 28.
9. **Science paper status blocks** — **DONE** (May 2026): Papers 02, 05,
   09 (ABG-relevant) cleaned up from build-log density to human-readable
   summaries.

### Remaining (test with ABG interactions)

- Spring Catalog intro — still jargon-heavy for first-time readers
- NUCLEUS Architecture page — glossary helps but page itself is deep
- Plasmodium naming — malaria parasite collision untested
- "baseCamp" — not self-explanatory without glossary

---

*This document is a living audit. Pre-engagement predictions will be
confirmed or overturned by actual ABG interactions. The tracking log
is the ground truth.*
