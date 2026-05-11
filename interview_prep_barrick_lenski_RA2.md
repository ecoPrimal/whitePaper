# Interview Prep: Barrick & Lenski Labs — Research Assistant II
**Interview with: Dr. Jeffrey Barrick**
**Date: Monday, May 11, 2026 (Zoom)**
**Position: Research Assistant II — Microbiology, Genetics, & Immunology**

---

## I. DR. JEFFREY BARRICK — WHO HE IS

### Career Arc
- **PhD**: Biochemistry (likely computational/molecular focus)
- **Postdoc**: With Richard Lenski at MSU — this is where he entered the LTEE world
- **Faculty**: University of Texas at Austin (2010–2025) — built independent lab
- **Current**: **Hannah Distinguished Professor**, MSU (returned Nov 2025)
  - Joint appointment: Dept. of **Microbiology, Genetics & Immunology** + **Entomology**
  - Brought the LTEE back to MSU from UT Austin
  - 10th PhD student recently defended

### Personality Signals
- Lenski hand-picked him as successor to lead the LTEE — deep trust
- Develops computational tools (breseq) — values computation alongside bench work
- Publishes in *Nature Communications*, *PNAS*, open-source tools
- Lab has a substack for news — values science communication
- Returned to MSU voluntarily — committed to the institution and LTEE legacy

---

## II. BARRICK'S FOUR RESEARCH PILLARS

### 1. LTEE — Long-Term Evolution Experiment
- **The crown jewel**: 12 populations of *E. coli*, running since 1988, now **82,000+ generations**
- Daily serial transfers (1% into fresh glucose minimal medium, ~6.67 generations/day)
- Frozen fossil record every 500 generations at –80°C
- **Key findings**: Power-law fitness (no asymptote), parallel evolution across replicates, Ara-3 citrate innovation (historical contingency), genome streamlining, hypermutator lineages
- **Barrick's contribution**: Applied whole-genome sequencing to LTEE (~2005), built breseq, maintains the experiment
- **The RA2 will maintain this experiment daily** — this is central

### 2. breseq — Computational Genomics Tool
- **What**: Command-line pipeline (C++ and R) for identifying mutations from resequencing data
- **Predicts**: SNPs, indels, large deletions, new junctions in haploid microbial genomes
- **Open source**: GPL-2.0, GitHub (barricklab/breseq), 39 releases, v0.39.0 (July 2024)
- **Used by**: Labs worldwide for evolution experiments, strain QC, pathogen tracking
- **LTEE-Ecoli repo**: Curated mutation database with interactive web interface
- **Why it matters for you**: Shows Barrick deeply values computational + bioinformatics alongside wet lab

### 3. Insect Symbiont Engineering
- **Honey bee gut engineering**: Bee microbiome toolkit (BTK)
  - Engineered *Snodgrassella alvi* for symbiont-mediated RNAi
  - Gene knockdown in bees via engineered gut bacteria
  - Protection from viral pathogens and parasites
  - One-step chromosomal engineering (no exogenous recombinase needed) — published 2024
- **Aphid symbionts**: Engineering *Serratia symbiotica* strains
  - Colonize aphid gut
  - Maternal transmission within aphids
  - Related to intracellular *Buchnera* endosymbionts
- **Buchnera genomes**: 29 newly sequenced genomes published 2024 (*Scientific Data*)

### 4. Synthetic Biology Reliability
- BioBrick burden study (2024, *Nature Communications*): Measured metabolic burden of 301 BioBrick plasmids
  - 19.6% were burdensome (deplete gene expression resources)
  - No BioBrick reduced growth >45% (aligns with population genetic models)
- Engineering naturally transformable bacteria (*Acinetobacter baylyi*)
- Preventing evolutionary failure by engineering cellular differentiation

---

## III. WHAT THE RA2 POSITION ACTUALLY IS

From the posting:

1. **Maintaining general laboratory operations and organization**
2. **Sustaining the LTEE** (daily transfers, frozen fossil record)
3. **Experimentally characterizing phenotypic and genomic changes** in evolving populations
4. **Utilizing synthetic biology and computational approaches** to analyze evolutionary dynamics
5. Engaging in other ongoing projects (insect symbionts, etc.)

**Desired qualifications:**
- Propagating bacteria
- Managing strain collections (databases, MTAs, sharing materials)
- Cloning and genetic engineering
- **Programming; bioinformatics; statistics**
- Analyzing data and **writing scientific papers**
- **Preparing proposals and project reports**
- Training and mentoring students
- Maintaining lab equipment, ordering supplies
- Lab safety oversight

---

## IV. YOUR STRONGEST CONNECTIONS

### A. Direct Bench Experience (5+ years)

| Your Experience | Their Need |
|----------------|-----------|
| 5 years MSUBI: bacteria, fungi, mycobacteria, anaerobes, GMOs in BSL2 | Propagating bacteria, BSL2 work |
| Daily fermentation maintenance, sterility, media prep | **LTEE daily transfers** (same discipline) |
| Aseptic technique, contamination prevention | Critical for LTEE (contamination = population loss) |
| Viable cell counts, spore counts, OD measurements | Characterizing evolved populations |
| HPLC, mass spec, enzyme kinetics | Phenotypic characterization |
| Training new hires on lab protocols | Training and mentoring students |
| Lab equipment maintenance, SOPs | Lab operations management |

**Key talking point**: *"The daily discipline of maintaining long-running fermentation cultures at MSUBI is exactly the same discipline the LTEE requires — you cannot skip a day, contamination is catastrophic, and the consistency of technique over time is what makes the data valuable."*

### B. Computational & Bioinformatics

| Your Experience | Their Need |
|----------------|-----------|
| M.S. Data Science (4.0 GPA through 3 semesters) | Programming, bioinformatics, statistics |
| Python, R, SQL | Data analysis, statistical modeling |
| Machine learning, deep learning coursework | Analyzing evolutionary dynamics |
| High-throughput sequencing analysis (Sandia) | breseq-adjacent genomics work |
| Bioinformatics pipeline development | Computational approaches to evolution |

**Key talking point**: *"Most lab managers can do the bench work OR the computation. I can do both. My Data Science M.S. means I can run breseq, analyze mutation trajectories, build statistical models of evolutionary dynamics, and contribute to papers — not just maintain the experiment."*

### C. Microbiology Education

| Your Coursework | Relevance |
|----------------|-----------|
| Microbial Genetics (MMG 431) | Directly relevant to LTEE mutation analysis |
| Prokaryotic Cell Physiology (MMG 421) | Understanding *E. coli* physiology |
| Advanced Microbiology Lab (MMG 408) | Bench technique training |
| Molecular Pathogenesis (MMG 461) | Understanding bacterial adaptation |
| Virology (MMG 413) | Phage-bacteria interactions in LTEE |
| Fundamental Genetics (IBIO 341) | Genetic engineering foundations |
| Machine Learning (CSE 847) | Computational analysis of evolution |
| Deep Learning (CSE 849) | Advanced analytical methods |
| Data Mining (CSE 881) | Pattern discovery in genomic data |
| Algorithms (CSE 830) | Computational pipeline design |

### D. baseCamp Paper 02 — LTEE Extensions

**This is your nuclear weapon for the interview.** You have already written a computational paper that:

- Makes **specific, falsifiable predictions** for LTEE populations using your Anderson localization framework
- Proposes testing **biofilm vs planktonic** LTEE growth to measure sdiA expression differences
- Integrates wetSpring (16S/WGS pipeline), neuralSpring (HMM introgression, ESN regime classifier), groundSpring (drift vs selection, quasispecies threshold)
- Connects to permafrost communities and agricultural time series
- References LTEE literature correctly (Lenski et al. 1991, Wiser et al. 2013, Blount et al. 2008/2012, Tenaillon et al. 2016)

**How to present this**: Don't overwhelm. Mention it naturally:
> *"I've actually been developing computational tools that make predictions for LTEE populations — specifically, how spatial geometry (biofilm vs planktonic) affects quorum sensing signal propagation using an Anderson localization framework. I'd love to discuss how those predictions could be tested with existing LTEE strains."*

### E. Other Relevant baseCamp Work

| Paper | Connection to Barrick Lab |
|-------|--------------------------|
| 01 (Anderson-QS) | Core framework — microbial signaling governed by spatial geometry |
| 03 (Bioag Microbiome) | Soil microbiology, inoculant design — connects to Pivot Bio, agriculture |
| 04 (Sentinels) | ESN classification on NPU — computational monitoring of microbial communities |
| 05 (Cross-Species QS) | Multi-species signaling — directly relevant to symbiont engineering |
| 16 (Anaerobic-Aerobic) | Fermentation experience at MSUBI → Anderson framework for bioreactors |

---

## V. QUESTIONS BARRICK MAY ASK YOU

### Technical
1. **"Tell me about your experience propagating bacteria."**
   → MSUBI: 5 years daily culture maintenance, media prep, contamination control, BSL2 with diverse organisms

2. **"What's your computational background?"**
   → M.S. Data Science, Python/R/SQL, machine learning, sequencing analysis at Sandia, developed validated computational tools

3. **"Have you done any cloning or genetic engineering?"**
   → Undergraduate research at ROME lab (enrichment, selective media), familiar with techniques from coursework (Microbial Genetics, Advanced Micro Lab). Honest about needing training on specific modern methods

4. **"How comfortable are you with bioinformatics pipelines?"**
   → Very comfortable — built sovereign bioinformatics pipelines (16S, DADA2, taxonomy, NCBI queries) in Rust, analyzed high-throughput sequencing at Sandia

5. **"Tell me about managing a lab / strain collections."**
   → MSUBI: maintained cultures, databases (Excel/SharePoint), SOPs, trained new hires, maintained equipment

### Behavioral
6. **"Why this position? Why not a PhD?"**
   → Genuinely passionate about the LTEE — it's the most important evolution experiment in history. Want to contribute directly. PhD may follow, but this work matters now.

7. **"How do you handle the daily routine of LTEE transfers?"**
   → 5 years of daily fermentation at MSUBI — I understand the discipline required. Army background reinforces reliability.

8. **"How would you contribute beyond the basic duties?"**
   → Computational skills (breseq analysis, mutation trajectory modeling, statistical analysis), help write papers and proposals, train students, bridge bench and computation

---

## VI. QUESTIONS FOR BARRICK

**Scientific Curiosity (show you've done homework):**

1. *"The Ara-3 citrate innovation required potentiating mutations — are there other populations showing similar multi-step innovations that haven't been fully characterized yet?"*

2. *"With the LTEE now at 82,000+ generations, are you seeing any qualitative changes in the evolutionary dynamics compared to the first 50,000 generations, or is the power-law fitness trajectory still holding?"*

3. *"The hypermutator lineages — are they still evolving at elevated rates, or have any evolved compensatory mechanisms to reduce their mutation rates?"*

4. *"How do you see the insect symbiont engineering work connecting to the LTEE conceptually? Is there an evolutionary angle to engineering stable symbiont-host relationships?"*

**Practical / Role-Specific:**

5. *"What does a typical week look like for the RA2 — how is the time split between LTEE maintenance, characterization experiments, and computational work?"*

6. *"What's the current state of the strain collection and databases? Is there a modernization effort underway?"*

7. *"Are there opportunities to contribute to breseq development, or is that maintained separately?"*

8. *"You mentioned synthetic biology approaches — are there specific genetic engineering projects planned for the LTEE strains?"*

---

## VII. YOUR NARRATIVE ARC

**The story to tell:**

> I started as a microbiologist (B.S. Microbiology, MSU 2018). I spent 5 years doing daily bench work at the Bioeconomy Institute — fermentation, culture maintenance, analytical chemistry, training new hires. That's the same discipline the LTEE demands.
>
> Then I went to Sandia National Labs for high-throughput sequencing and bioinformatics. I realized computation was the missing piece, so I came back for a Data Science M.S. (3.92 GPA). Now I'm a microbiologist who can also write bioinformatics pipelines, do statistical analysis, and contribute to papers computationally.
>
> The LTEE is the experiment I've been thinking about since I started building computational models of microbial evolution. The chance to maintain this experiment, characterize the populations, and bring computational tools to bear on 82,000 generations of evolutionary data — that's exactly where my two backgrounds converge.
>
> And I'm a veteran. Reliability, showing up every day, attention to detail under pressure — that's not something I have to learn. It's something I've already proven.

---

## VIII. LOGISTICS

- **Position**: Research Assistant II (AP level 12)
- **Term**: 1 year from hire, possible extension contingent on funding
- **Department**: Microbiology, Genetics, & Immunology (College of Natural Science)
- **Hours**: Standard 8-5
- **Application closes**: May 12, 2026
- **Required materials**: 1-page cover letter, CV, 3 references

---

## IX. KEY REFERENCES TO KNOW

### Barrick Publications (mention casually if relevant)
- Barrick et al. (2009) "Genome evolution and adaptation in a long-term experiment with *E. coli*" — *Nature*
- Tenaillon et al. (2016) "Tempo and mode of genome evolution in a 50,000-generation experiment" — *Nature*
- Good et al. (2017) "The dynamics of molecular evolution over 60,000 generations" — *Nature*
- Deatherage & Barrick (2014) "Identification of mutations using breseq" — *Methods in Molecular Biology*
- Leonard et al. (2024) "One-step genome engineering in bee gut bacterial symbionts" — *mBio*
- Barrick lab (2024) "Measuring the burden of hundreds of BioBricks" — *Nature Communications*

### LTEE Essentials
- Lenski et al. (1991) founding paper
- Blount et al. (2008) citrate innovation in Ara-3
- Wiser et al. (2013) power-law fitness dynamics
- the-ltee.org — official website with 5 key takeaways

---

## X. WHAT TO AVOID

- **Don't oversell the computational work** — this is a lab management position first. Show you're excited about the bench work, then layer on computation as a bonus.
- **Don't imply the LTEE needs fixing** — it's run successfully for 37 years. You want to sustain and contribute, not overhaul.
- **Don't get lost in your Spring framework** — if you mention baseCamp Paper 02, keep it to 2-3 sentences. Let him ask follow-up questions.
- **Don't trash the 1-year term** — frame it as an opportunity, acknowledge funding realities.
- **Don't pretend you're an expert cloner** — be honest about genetic engineering experience and frame it as eager to learn.

---

## XI. THE 30-SECOND PITCH

> *"I'm a microbiologist with 5 years of daily bench experience and a Data Science M.S. from MSU. I've maintained long-running bacterial cultures, done analytical chemistry, high-throughput sequencing, and bioinformatics. The LTEE is the experiment I've been thinking about computationally — I've built models that make testable predictions for LTEE populations. I'm excited about the chance to sustain the experiment, characterize the evolving populations, and bring both bench and computational skills to the lab."*
