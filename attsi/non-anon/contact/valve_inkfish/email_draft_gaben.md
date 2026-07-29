# Draft Email — Gabe Newell / Inkfish

**Status**: DRAFT — needs attsi review, timing dependent on published release
**From**: eco.primal@pm.me (or eco.primal@primal.eco when live)
**To**: gaben@valvesoftware.com (or Inkfish contact form)
**CC**: Dr. Pim Bongaerts (via CalAcademy or LinkedIn InMail)
**Subject**: GPU-accelerated coral genomics on expedition hardware — from a microbiologist

---

## Draft v1

Gabe,

I'm a microbiologist who spent the last 14 months building GPU-accelerated
genomics pipelines in Rust that run on any Vulkan GPU — no CUDA, no cloud,
no vendor lock-in. The same Vulkan substrate you funded for gaming.

I'm writing because Inkfish generates exactly the kind of data these tools
were built to process, and because we share the same thesis: build your own
infrastructure instead of renting someone else's.

**What the tools do:**

- DADA2 16S pipeline on consumer GPUs (reproduced 63 published papers)
- Metagenomic analysis, diversity indices, phylogenetics — all GPU-accelerated
- Runs on a laptop GPU, a Steam Deck, or an RTX 5090 — anything with Vulkan
- Content-addressed storage with cryptographic provenance chains
- Works offline, syncs on reconnect — designed for disconnected operation

**Why this matters for Inkfish expeditions:**

Dr. Bongaerts' team sequences >1,200 coral genomes per expedition. Right now,
that data likely waits weeks for shore-side HPC time. With these tools, preliminary
analysis could run on vessel hardware during the expedition — same-day results from
same-day samples, with cryptographic provenance from tissue sample to analysis output.

**What I'm asking:**

Not investment. Not acquisition. A conversation about whether sovereign
GPU compute fits Inkfish's science program. I can process a test dataset
from any published expedition to demonstrate the pipeline.

**About me:**

- BS Microbiology, MS Data Science
- One person, AI-assisted development (Cursor), 14 months, 3.6 million lines of Rust
- 105,000+ tests, 197 validation scenarios, all passing
- AGPL-3.0 — same open commitment as Inkfish's open-source data repositories
- The project: https://sporeprint.primals.eco

**About the biology:**

Mesophotic coral holobionts are microbial ecosystems. The bacterial communities
in coral tissue respond to depth, temperature, and light gradients — the same
environmental variables Dr. Bongaerts maps across the reef slope. If Inkfish
ever adds 16S/ITS amplicon sequencing to their coral sampling protocol, the
bioinformatics pipeline already exists and runs on the hardware already aboard.

A human reads and responds to every message at this address.

— eco Primal

---

## Notes for attsi review

1. **Tone**: Technical but warm. Microbiologist-to-marine-biologist, not
   startup-to-investor. The letter should read like a colleague offering tools.

2. **The "Steam Deck" mention**: Deliberate. Gabe knows the Steam Deck's
   GPU capability. Saying "runs on a Steam Deck" is more meaningful to him
   than any benchmark table.

3. **CC to Bongaerts**: He's the person who would actually evaluate the tools.
   Gabe will likely forward internally anyway, but CC'ing shows we did our
   homework and respect the science team.

4. **"Not investment"**: Same language as the site's Steam invitation page.
   Gabe gets pitched constantly. This needs to be clearly not that.

5. **The holobiont angle**: This is where Kevin's microbiology becomes
   genuinely relevant. Coral holobionts ARE microbial ecosystems. If Inkfish
   adds 16S to their workflow, ecoPrimals is the only sovereign GPU pipeline
   that could run it on-vessel.

6. **Steam ID**: Consider including Kevin's Steam ID as a P.S. — Gabe is
   famously accessible through Steam and it signals "I'm in your community."

7. **Length**: Currently ~300 words body. Could be shorter. Gabe reads email
   fast. The link to sporeprint.primals.eco does the heavy lifting.

---

## Prerequisites before sending

- [ ] barraCuda or wetSpring published (crates.io, JOSS, or Zenodo)
- [ ] ecoPrimal LinkedIn established and populated
- [ ] Kevin has Steam account details ready for P.S.
- [ ] attsi tone review complete
- [ ] One Inkfish expedition dataset identified for demo (public data)
- [ ] Verify gaben@valvesoftware.com is still responsive (check recent reports)
