# Isaac Gifford — Barrick Lab

**Role**: Postdoctoral Fellow (Jan 2020–)
**Degrees**: BS Microbiology (UT Austin), PhD Microbiology (UC Davis)
**Interview**: Mon May 18, 2:30–3:00 PM, BPS 6150

---

## Research

### Horizontal Gene Transfer and Genome Evolution in *A. baylyi*

Isaac's primary research focuses on mechanisms of **horizontal gene transfer (HGT)** and its role in genome evolution, using *Acinetobacter baylyi* ADP1 — a naturally competent soil bacterium that takes up DNA from its environment without conjugation machinery.

Key questions:
- How do horizontally acquired genes become "domesticated" after incorporation?
- How does gene acquisition affect the rest of the genome?
- What determines whether acquired DNA becomes nutrition vs. genetic information?

### ADP1-ISx: The Clean-Genome Platform

The lab built **ADP1-ISx** by deleting all six copies of the IS1236 transposon (Suárez et al. 2017, *Applied Environmental Microbiology*):
- Mutation rates reduced **7–21 fold** (fewer IS-mediated large deletions)
- Unexpectedly **increased transformability** (possibly less autolysis/aggregation)
- Provides a stable platform for synthetic biology — introduced genes don't get knocked out by transposon insertions

### Fitness Recovery from Large Deletions (PLOS Genetics 2024)

**Gifford, Suárez & Barrick 2024** — the headline paper:
- Evolved 8 *A. baylyi* strains with engineered deletions (22–293 kb) for ~300 generations in minimal and complex media
- Fitness recovered in nearly all cases through two mechanisms:
  1. **Deletion-specific compensatory mutations** in 9 protein-coding genes + 2 sRNAs
  2. **Global regulatory adjustments** in post-transcriptional regulators (*rnd*, *csrA*, *hfq*)
- The *rnd/csrA/hfq* network was hit repeatedly across all strains — a convergent regulatory solution
- Demonstrates that fitness costs of genome streamlining are typically recoverable

This is **constrained evolution in a tube**: organism constrained by deletion → evolves compensatory mutations → convergent regulatory solutions across independent replicates. Same statistical signature as the LTEE (convergent pathways, not identical mutations).

### Bartonella Parasites — Negev Desert

Collaboration with the Hawlena Lab (Ben-Gurion University, Israel):
- Multiple *Bartonella* species infect gerbil populations vectored by fleas
- Genome evolution within and across infection cycles
- Contingency loci (hypermutable regions), gene accordions, recombination during co-infections
- Published: Rodríguez-Pastor et al. 2024, *PLoS Pathogens*

### Genome Streamlining

Ongoing work on engineering minimal *A. baylyi* genomes:
- Deleting non-essential regions to create a minimal chassis for synthetic biology
- Studying limits to how much genome you can remove before fitness becomes irrecoverable
- The 293 kb deletion strain in the PLOS Genetics paper represents ~7% of the genome removed

---

## What He Needs (Wet Lab)

- **Evolution experiments**: Setting up, maintaining, and sampling serial passage experiments
- **Competition assays**: Measuring relative fitness of evolved vs. ancestor strains
- **Transformation assays**: Testing DNA uptake efficiency in engineered strains
- **Sequencing**: Whole-genome sequencing of evolved isolates

## What He Needs (Dry Lab)

- **Mutation classification**: Which compensatory mutations are beneficial vs. hitchhiking vs. neutral? Currently done by manual inspection + breseq
- **Convergence analysis**: Quantifying how often the same genes/pathways are hit across independent replicates
- **Fitness trajectory modeling**: Power-law vs. exponential vs. asymptotic fits to fitness recovery curves
- **Structural consequences**: Do large deletions change the 3D organization of the remaining genes? Do compensatory mutations restore protein structures?
- **Gene essentiality prediction**: Before making a deletion, predict fitness cost computationally

## How We Multiply His Work

| His Need | Our Tool | Impact |
|----------|----------|--------|
| Beneficial vs. hitchhiker classification | groundSpring Exp 014 (drift vs. selection) | Quantitative Wright-Fisher fixation probability per mutation |
| Convergence scoring | neuralSpring parallel evolution detector | Automated detection of independently hit genes across replicates |
| Fitness trajectory modeling | groundSpring jackknife + AIC/BIC model comparison | Power-law vs. alternatives with proper uncertainty |
| Structural consequences of deletions | coralForge (AlphaFold2/3) | Predict protein fold changes from genomic deletions |
| Gene essentiality prediction | neuralSpring ML | Train on deletion fitness data → predict costs of novel deletions |
| Regulatory network analysis | neuralSpring GNN | Model the rnd/csrA/hfq network as a graph — predict compensatory targets |
| Anderson framework | The convergent *rnd/csrA/hfq* hits map to Anderson disorder theory — deletion = increased disorder in gene expression lattice → system evolves toward same regulatory "extended state" solution |

**The pitch to Isaac**: "Your PLOS Genetics paper is one of the cleanest constrained evolution examples I've seen — independent replicates under identical constraint converging on the same regulatory network. I've been building tools that quantify exactly that: drift-vs-selection classification for each mutation, convergence scoring across replicates, and power-law fitness modeling with proper uncertainty. Also — do the large deletions change protein folding in the remaining genes? I have a structure prediction engine that could check."

---

## Personal

Game design and 21st century sequential art (comics/graphic novels). The game design interest is genuinely shared territory — your esotericWebb work is literally a game engine built on scientific infrastructure. Could be a natural conversation starter.
