# Anthony VanDieren — Barrick Lab

**Role**: Microbiology Graduate Student (Apr 2023–)
**Degrees**: BS Entomology + BS Biological Science + BS Chemistry, University of Georgia
**Email**: avandieren@utexas.edu
**Interview**: Mon May 18, 12:00–1:30 PM (lunch, with Kathleen Sotelo)

---

## Research

### Engineering Aphid Endosymbionts

Anthony works on engineering **Serratia symbiotica** strains that colonize the aphid gut, with the long-term goal of **pest control via symbiont-mediated RNAi** (same concept as the bee work, different insect).

The *S. symbiotica* system is scientifically rich because it spans the pathogen-symbiont continuum:
- **Free-living strains**: Culturable, can be engineered (CWBI-2.3T)
- **Gut colonizers**: Facultative symbionts that colonize the aphid gut from ingestion
- **Intracellular obligates**: Live inside aphid cells (bacteriocytes), vertically inherited, massively reduced genomes

The lab showed that cultured strains achieve **maternal (transovarial) transmission** — they can pass from mother to embryo via injection. This means free-living strains have a **latent capacity** to evolve long-term symbiosis.

### Prophage-Mediated Virulence Attenuation

**VanDieren & Barrick 2024 (bioRxiv)** — Anthony's most recent work:
- Evolved laboratory populations of culturable *S. symbiotica* (CWBI-2.3T) through 15–30 serial passages
- Prophage activation triggered evolutionary changes that **attenuated virulence**
- This is evolution in response to an internal genomic perturbation (prophage induction) — the bacterium evolves to reduce the cost of the phage

This connects directly to the phage contingency loci work (Barrick & Waters 2025, bioRxiv) — phages use hypermutable loci as bet-hedging, and the host bacterium evolves in response.

### The Endosymbiont Transition

The big conceptual question: how does a free-living bacterium become an obligate intracellular symbiont? This is one of the deepest transitions in biology:
1. **Contact**: Free-living bacterium encounters insect
2. **Colonization**: Gut colonization (extracellular)
3. **Vertical transmission**: Passes to offspring
4. **Internalization**: Moves inside cells
5. **Genome reduction**: Loses genes no longer needed inside the cell
6. **Obligate dependence**: Can no longer survive outside the host

Anthony is studying steps 2–3 with the culturable strains. The genome reduction (step 5) is extreme: obligate *S. symbiotica* genomes are ~2.8 Mb vs. ~5.2 Mb for free-living strains — nearly half the genome lost.

### Background

- **Three BS degrees** from UGA — Entomology, Biological Science, Chemistry
- Analytical chemistry lab tech at **Henkel** (industrial experience)
- Staff entomologist at **Cranbrook Institute of Science** (Michigan — local connection)
- Undergrad research on **kissing bugs and gut symbionts** (UGA)

---

## What He Needs (Wet Lab)

- **Aphid colony maintenance**: Rearing pea aphids (*Acyrthosiphon pisum*) under controlled conditions
- **Bacterial culture**: Growing *S. symbiotica* (fastidious — specialized media)
- **Microinjection**: Injecting engineered bacteria into aphid hemocoel for transovarial transmission experiments
- **Conjugation/electroporation**: Transforming *S. symbiotica* with engineered constructs
- **Fitness assays**: Measuring aphid fecundity, survival, with/without engineered symbiont
- **Sequencing**: Tracking symbiont genome evolution across aphid generations

## What He Needs (Dry Lab)

- **Comparative genomics**: Free-living vs. gut-colonizing vs. obligate *S. symbiotica* — what genes are lost, when, why?
- **Prophage dynamics**: Modeling prophage induction, lysis-lysogeny decision under different conditions
- **Symbiont genome evolution**: Tracking gene loss, pseudogenization, IS activity across passages
- **Vertical transmission modeling**: What determines whether a strain achieves maternal transmission?
- **Population genetics under bottleneck**: Transovarial transmission = extreme bottleneck (~100-1000 cells). Selection vs. drift at tiny N_e

## How We Multiply His Work

| His Need | Our Tool | Impact |
|----------|----------|--------|
| Comparative genomics | wetSpring sovereign pipeline | Process *S. symbiotica* genomes — diversity metrics, gene loss tracking |
| Prophage dynamics | groundSpring stochastic models | Poisson process for prophage induction rate, lysis-lysogeny decision modeling |
| Drift vs. selection at small N_e | groundSpring Exp 014 + Exp 017 | Wright-Fisher at N_e ~ 100-1000; quasispecies threshold for when mutation overwhelms selection |
| Genome reduction trajectory | neuralSpring LSTM | Predict gene loss order from partial time-series |
| Anderson-QS in aphid gut | wetSpring Anderson model | Aphid gut geometry → Anderson prediction for coordinated symbiont gene expression |
| Cross-species signaling | Paper 05 predictions | Aphid-Serratia system is a test case for cross-species Anderson-QS predictions |
| Structural prediction | coralForge | How does gene loss affect remaining protein structures? Do retained proteins adapt structurally? |
| Phage contingency loci | wetSpring HMM | Identify hypermutable regions in *S. symbiotica* prophages |

**The pitch to Anthony**: "The endosymbiont transition is one of the most fascinating things in biology — watching a free-living bacterium evolve toward obligate intracellular life. Your prophage work adds another layer: the symbiont is evolving in response to its own selfish genetic elements while simultaneously adapting to the host. I've been building tools for population genetics under extreme bottleneck (the kind you get with transovarial transmission — N_e in the hundreds) and comparative genomics for tracking gene loss over time. I also have a 16S/WGS pipeline that might help with tracking the symbiont population inside the aphid across generations. And — local connection — I grew up in Michigan and know Cranbrook."

---

## Personal

Serious entomologist — finds, rears, and preserves exotic insects and arachnids outside of lab. Michigan connection via Cranbrook Institute of Science. Three degrees suggests someone who is thorough and genuinely curious across domains.
