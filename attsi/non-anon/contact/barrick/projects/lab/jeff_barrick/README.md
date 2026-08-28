# Jeffrey E. Barrick — PI

**Title**: Hannah Distinguished Professor
**Departments**: Microbiology, Genetics & Immunology + Entomology (joint)
**Institution**: Michigan State University (returned Nov 2025; previously UT Austin 2011–2025)
**Education**: BS Math & Biology (University of Michigan), PhD Genetics (Yale, Ron Breaker lab — riboswitches)
**Postdoc**: Lenski Lab, MSU (where breseq was born)
**Lab**: https://barricklab.org/
**GitHub**: https://github.com/barricklab
**Substack**: https://barricklab.substack.com/
**Interview**: Mon May 18, 11:30–11:50 AM (lab tour/introductions) + 3:30–4:00 PM (wrap-up), BPS 6179

---

## The Three Pillars

Jeff's research sits at the intersection of three pillars, all connected by the question: **how does evolution shape (and constrain) biological systems?**

### Pillar 1: LTEE — Evolution Under a Microscope

The Long-Term Evolution Experiment, founded by Rich Lenski in 1988, now at 82,500+ generations across 12 replicate populations of *E. coli*. Jeff took over daily operations in 2015 when Lenski retired from bench work, moved the experiment to UT Austin in 2022, and brought it back to MSU in September 2025.

**Key contributions**:
- Built **breseq** — the mutation-calling pipeline that made LTEE genomics possible (originally for his postdoc work)
- Led the genome sequencing of clones at 50,000 and 60,000+ generations
- Discovered the 77,000-generation population switcheroo and Acinetobacter contamination via Nanopore QC — demonstrating the value of routine long-read sequencing as an integrity check
- The LTEE is now at MSU in the Biomedical Physical Sciences building

### Pillar 2: Synthetic Biology Reliability

How do engineered genetic constructs fail, and can we predict/prevent failure?

**BioBrick burden study** (McGuffie & Barrick, *Nature Communications* 2024):
- Measured metabolic burden of 301 BioBrick plasmids in *E. coli*
- 19.6% (59/301) were burdensome
- No construct reduced growth rate by more than 45% — a fundamental ceiling
- Above this ceiling, escape mutants dominate → construct becomes effectively unclonable
- Built a population genetic model predicting this limit: https://barricklab.org/burden-model

**Uncatalogued plasmid variants** (McGuffie & Barrick, *PLOS ONE* 2024):
- Screened 50,000+ plasmids in Addgene
- 3/5 contained at least one uncatalogued variant
- Reproducibility crisis in synthetic biology: the parts aren't what people think they are

**Anderson-QS connection**: The 45% burden ceiling is a **localization threshold** — above it, the "fitness signal" of the engineered construct is overwhelmed by the "noise" of escape mutations. This maps directly to Anderson's disorder parameter W: burden = disorder, fitness benefit of construct = hopping energy. Above W_c, the construct is "localized" (can't spread/maintain in the population).

### Pillar 3: Insect Symbiont Engineering

Engineering bacteria that live inside insect guts to deliver therapeutic payloads:
- **Honeybees**: *Snodgrassella alvi* for RNAi and peptide secretion (Kathleen's work, building on Moran collaboration)
- **Aphids**: *Serratia symbiotica* for paratransgenesis (Anthony's work)
- Both systems: how does evolution constrain the stability of engineered symbiont constructs in the gut?

The MSU Entomology joint appointment reflects this direction — insect microbiome engineering is a major growth area.

---

## ADP1 Ecosystem

Jeff built a complete genetic engineering platform around *Acinetobacter baylyi* ADP1:
- **ADP1-ISx**: Transposon-free, low-mutation-rate chassis
- **Golden Transformation**: One-step precise genome editing via natural competence
- **EASy (Evolution by Amplification and Synthetic biology)**: Gene accordion for metabolic engineering
- **Genome streamlining**: Systematic deletion of non-essential regions (Isaac's work)
- **Gene accordions**: Fundamental dynamics of copy number variation (Tyler's work)

---

## Management Style & Lab Culture

From the lab website, LTEE blog, and publications:
- Data-driven, computational mindset (built breseq himself — he codes)
- Values reproducibility intensely (the LTEE is literally a 37-year reproducibility experiment)
- Embraces open science (all tools MIT/GPL, public repositories, JoVE video protocols)
- Moved entire lab (people, equipment, 12 living E. coli populations, frozen fossil record) from Austin to East Lansing — massive logistics, shows commitment
- Maintains the LTEE blog and Substack — values science communication
- Joint Entomology appointment signals interdisciplinary ambition

---

## What He Needs From a Lab Manager / Research Assistant II

This is why the position exists. Based on the lab's current structure:

### Daily Operations
- **LTEE daily transfers**: 12 populations, 7 days/week, 365 days/year — this is the heartbeat of the lab
- **Archiving**: Every 500 generations, freeze glycerol stocks of all populations
- **Contamination monitoring**: Plating, Nanopore QC, visual inspection
- **Equipment maintenance**: Incubators, shakers, flow hoods, sequencing

### Sequencing Pipeline
- Library prep for Illumina (breseq) and Nanopore (seabreeze)
- Quality control across both platforms
- Coordinating with MSU Genomics Core

### Lab Infrastructure
- Ordering, inventory, budgets
- Training new grad students on protocols (Kathleen and Ira are both first-year)
- Maintaining the *A. baylyi* and insect systems alongside the LTEE
- Safety compliance, MSU regulatory requirements

### Computational Support
- Running breseq and seabreeze on new sequencing data
- Managing data storage (LTEE generates a lot of data over 37 years)
- This is where your skills become the force multiplier — not just running pipelines, but improving them

---

## How We Multiply His Lab

| Lab Need | Our Capability | Impact |
|----------|----------------|--------|
| breseq speed & features | Rust pipeline with concordance checks | Benchmark, identify speedups, contribute upstream |
| LTEE data management | JupyterHub + sovereign pipelines | Reproducible notebooks for every sequencing run |
| Contamination detection | wetSpring 16S pipeline | Automated community profiling of LTEE populations |
| BioBrick burden prediction | Anderson-QS framework | Predict which constructs will fail before building them |
| Construct stability tracking | breseq + neuralSpring | Track escape mutations in engineered constructs over time |
| Cross-project data integration | primals.eco infrastructure | One hub linking LTEE, ADP1, bee, aphid data |
| Lab training | Computational workshops | Train grad students on genomics, ML, reproducibility |
| lithoSpore artifact | guideStone for LTEE | Self-proving, reproducible analysis package for flagship data |

**The meta-pitch**: "I'm a force multiplier. I can do the wet lab work — transfers, preps, assays — and I can build the computational infrastructure that makes every experiment in the lab more productive. I've been building genomics pipelines, ML tools, and structure prediction engines specifically targeted at the kinds of questions your lab asks."

---

## Conversation Topics for the Interview

1. **breseq**: "I've been building a parallel mutation caller in Rust — I'd love to benchmark it against breseq on LTEE data. Not to replace it, but to find where parallelization helps."
2. **BioBrick burden**: "Your burden ceiling at 45% maps beautifully to a localization threshold from condensed matter physics. I've been working on formalizing that connection."
3. **LTEE frozen fossil record**: "The frozen fossil record is a biological time machine. I have specific hypotheses about convergent evolution and constrained pathways that I'd like to test on the archive data."
4. **The MSU move**: "How is the transition going? What are the biggest challenges in re-establishing the lab? I'm a Lansing local — anything I can help navigate."
5. **Long-read QC**: "The Acinetobacter catch at 77,000 generations was a great example of long-read sequencing as a surveillance tool. I've been thinking about automating that kind of QC."
