# Ira Zibbu — Barrick Lab

**Role**: Cell & Molecular Biology Graduate Student (Jan 2025–)
**Degrees**: BS-MS Biology with Data Science minor, IISER Thiruvananthapuram (India)
**Email**: irazibbu@utexas.edu
**GitHub**: [github.com/ira-zibbu](https://github.com/ira-zibbu)
**Website**: [ira-zibbu.github.io](https://ira-zibbu.github.io/) (template, not populated)
**Interview**: Mon May 18, 3:00–3:30 PM, BPS 6199 (with Pranesh Rao)

---

## Research

### LTEE Genome Rearrangements

Ira studies **large-scale structural variation** in the LTEE — inversions, deletions, duplications, translocations — and how they evolve over 75,000+ generations. This is a different layer than point mutations (breseq territory): these are events that rearrange hundreds of kilobases, change gene order, alter replichore balance, and can have dramatic fitness consequences.

**Key finding (LTEE blog post, 2023)**: Long-read sequencing (Oxford Nanopore) of clones from all 12 populations at 75,000 generations revealed:
- Deletions in almost all populations
- Inversions and duplications in some
- **Ara+1**: Most extensive changes — complex rearrangements from successive inversions
- **Ara+4**: No rearrangements at all
- Most events mediated by **insertion sequence (IS) element** recombination
- Open question: which rearrangements are adaptive vs. neutral vs. hitchhiking?

### seabreeze — Structural Variation Pipeline

Ira built **seabreeze** (Zibbu, Wilke & Barrick 2025, *JOSS*), a Python/Snakemake pipeline for comparing bacterial genome assemblies:

| Capability | What it does |
|-----------|-------------|
| Genome size differences | Compute overall size changes |
| IS element prediction | Locate insertion sequences |
| Structural mutation prediction | Inversions, deletions, translocations, duplications |
| Synteny plots | Visualize genome-vs-genome alignment |
| Replichore balance | Analyze symmetry of replication origin |
| Mechanism prediction | Infer how inversions/deletions occurred |
| Gene annotation | Which genes are in mutated regions |

**Tech**: Python 90.9%, Snakemake workflow, bioconda installable, MIT license, 6 releases (v1.5.0 latest)
**GitHub**: [barricklab/seabreeze](https://github.com/barricklab/seabreeze)

### IS Elements in the LTEE

IS-mediated mutations are ~35% of high-frequency mutations in LTEE populations (Papadopoulos et al. 2021, *Nature Communications*). IS elements both **promote** evolution (creating beneficial deletions, regulatory changes) and **constrain** it (the same IS elements mediate rearrangements that can be deleterious). This dual role is exactly the constrained evolution framework — the constraint (IS distribution) shapes the evolutionary landscape.

### Undergrad Background

Unusually broad: insect ecology, differential equation models of chemotaxis, synthetic biology, and ML for protein-ligand affinity predictions. The ML/protein-ligand work overlaps with Eaves/Woldring (HOLIgraph) and coralForge.

---

## What She Needs (Wet Lab)

- **Long-read sequencing**: Nanopore library prep and sequencing for new LTEE timepoints
- **Clone isolation**: Picking and growing clones from LTEE populations for genome assembly
- **PCR validation**: Confirming structural variants predicted computationally

## What She Needs (Dry Lab)

- **Assembly speed**: Long-read assembly (Flye, Canu, etc.) is slow on large genomes — GPU acceleration helps
- **Connecting structure to function**: Which rearrangements change protein folding? Gene expression? Fitness?
- **Temporal tracking**: How do rearrangements accumulate over time? seabreeze compares two assemblies — extending to full time series is the next frontier
- **Interactive visualization**: Synteny plots are static 2D images. Animated or interactive rearrangement visualizations over evolutionary time would be a game-changer
- **IS element dynamics**: Modeling IS element copy number, transposition rates, and their interaction with selection

## How We Multiply Her Work

| Her Need | Our Tool | Impact |
|----------|----------|--------|
| Protein structural consequences of rearrangements | coralForge (AlphaFold2/3, 154 checks) | Predict fold changes from inversions, chimeric gene products |
| Assembly acceleration | wetSpring GPU alignment | Speed up Nanopore assembly pipeline |
| Temporal rearrangement modeling | neuralSpring LSTM | Predict rearrangement trajectories from time-series data |
| IS element dynamics | groundSpring stochastic models | Poisson process modeling of IS transposition rates |
| Regime detection | neuralSpring ESN | Classify evolutionary regimes: is a rearrangement sweeping? |
| Visualization | petalTongue / interactive dashboards | Animated synteny + rearrangement over evolutionary time |
| Anderson framework | wetSpring Anderson model | IS elements as "disorder" in the genome lattice — rearrangement hotspots correlate with high-disorder regions |

**The pitch to Ira**: "I saw your seabreeze paper and your LTEE blog post — the structural variation work is fascinating. I've been building GPU-accelerated genomics pipelines and a sovereign protein structure prediction engine. Two things I think could help: (1) predicting the protein structural consequences of the rearrangements you're finding — does an inversion change how a protein folds? — and (2) interactive visualization of how rearrangements accumulate over time. I'd also love to talk about how IS elements create disorder in the genome that maps to a physics framework I've been working with."

---

## Personal

Gym, biking (beloved cycle), musical theater, philosophy of science, contemporary fiction, cooking. Strongly believes in removing barriers to scientific participation. She performed the 11,682nd transfer of the LTEE during her summer 2023 visit and left a poem ("The Fly" by Ogden Nash, modified). The philosophy-of-science interest means guideStone (reproducible, self-proving artifacts) may genuinely resonate.
