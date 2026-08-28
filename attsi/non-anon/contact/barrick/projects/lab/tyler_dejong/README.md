# Tyler de Jong — Barrick Lab

**Role**: Microbiology, Genetics & Immunology Graduate Student (Jan 2024–)
**Degree**: BS Biochemistry, University of Texas at Austin
**Email**: tylerdejong@austin.utexas.edu
**Interview**: Mon May 18, 2:00–2:30 PM, BPS 6150 (tentative)

---

## Research

### Gene Accordions

Tyler studies **gene accordions** — adaptation systems in bacteria where tandem gene duplications arise (via RecA-dependent or independent recombination), then expand and contract at high rates. The mechanism:

1. Initial duplication creates tandem repeats
2. Long perfect repeats enable RecA-dependent amplification or loss (segregation) at high frequency
3. Copy number fluctuates — "accordion-like" expansion and contraction
4. Creates **genotypic and phenotypic heterogeneity in clonal populations**

This is not random mutation — it's a structured mechanism that generates diversity at specific loci. The LTEE populations show evidence of accordion-like dynamics, and *Bartonella* parasites use similar mechanisms to evade host immune responses (contingency loci).

### Directed Evolution of Fluorescent Proteins in ADP1

Tyler replicates the accordion process through **directed evolution of fluorescent proteins** in naturally competent *Acinetobacter baylyi* ADP1. This is elegant experimental design:
- Start with a fluorescent protein gene in ADP1
- Select for fluorescence under constraint (e.g., different substrates, temperatures)
- Watch the gene accordion process create copy number variants and sequence diversification
- Characterize the resulting evolutionary dynamics

Natural competence means ADP1 constantly takes up DNA from its environment, so the evolutionary dynamics include both accordion-driven internal diversification and external DNA acquisition.

### The EASy Method Connection

The Barrick lab developed **EASy (Evolution by Amplification and Synthetic biology)** — using gene amplification in ADP1 to promote copy number variation of genomic segments for metabolic engineering. Tyler's work builds on this by studying the fundamental dynamics of the accordion process rather than applying it to engineering.

### Prior Experience

Before grad school: clinical reference lab processing COVID-19 tests, then research associate in **Nancy Moran's lab** (honeybee gut microbiome). He bridges the bee symbiont work and the *A. baylyi* work through his Moran lab experience.

---

## What He Needs (Wet Lab)

- **Evolution experiments**: Maintaining serial passage experiments with ADP1 under fluorescence selection
- **Flow cytometry / fluorescence assays**: Quantifying fluorescence distribution in populations (accordion copy number → fluorescence intensity)
- **Plating and screening**: Identifying copy number variants
- **Sequencing**: Both short-read (breseq for point mutations) and long-read (seabreeze for structural changes)

## What He Needs (Dry Lab)

- **Copy number variant calling**: Detecting accordion expansions/contractions from sequencing data
- **Fluorescence-fitness correlation**: Mapping copy number → fluorescence → fitness
- **Population dynamics modeling**: How fast do accordions expand/contract? What determines the equilibrium distribution?
- **Distinguishing adaptive from neutral CNVs**: Is the 3-copy variant selected or drifting?
- **Structural prediction**: How does copy number affect protein folding? Do tandem duplicates interact?

## How We Multiply His Work

| His Need | Our Tool | Impact |
|----------|----------|--------|
| Copy number calling | wetSpring pipeline + seabreeze integration | GPU-accelerated CNV detection from long reads |
| Population dynamics | groundSpring stochastic models | Poisson process for accordion rate, Wright-Fisher for CNV fixation |
| Adaptive vs. neutral | groundSpring Exp 014 drift vs. selection | Quantify selection coefficient on each CNV |
| Regime detection | neuralSpring ESN | Classify: is the population in expansion phase, contraction phase, or equilibrium? |
| Protein structure of tandem repeats | coralForge | Do adjacent copies interact? Predict multimer structures |
| Fluorescence prediction | neuralSpring ML | Train on sequence → fluorescence; predict mutant properties before building |
| Anderson connection | Gene accordions create high-copy-number disorder at specific loci — the accordion rate maps to effective W at that locus. Positions with active accordions are "high-disorder" sites in the genome lattice |

**The pitch to Tyler**: "The accordion dynamics are really interesting — it's a structured mechanism for generating diversity at specific loci, not random mutation. I've been building tools for detecting evolutionary regime shifts from time-series data (ESN reservoir computing) and quantifying whether copy number variants are under selection or drift. If you have fluorescence time-series data from your ADP1 experiments, I could model the accordion expansion/contraction dynamics and try to predict when a new expansion event is about to take off."

---

## Personal

Walks in Austin greenbelts (now Lansing parks?), cat person. Came from Moran lab → shared ground with Kathleen and the bee symbiont work.
