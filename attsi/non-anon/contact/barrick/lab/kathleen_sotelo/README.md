# Kathleen Sotelo — Barrick Lab

**Role**: Microbiology Graduate Student (Jan 2025–)
**Degree**: BS Biology (Microbiology & Infectious Diseases), University of Texas at Austin
**Email**: ksot6127@utexas.edu
**Interview**: Mon May 18, 12:00–1:30 PM (lunch, with Anthony VanDieren)

---

## Research

### Engineering Honeybee Gut Symbionts for Pathogen Protection

Kathleen is genetically manipulating **Snodgrassella alvi** (a core bee gut bacterium) to secrete **antimicrobial peptides** that protect honeybees from pathogens. This builds directly on the Barrick/Moran FUGUES system:

**FUGUES (Functional Genomics Using Engineered Symbionts)**:
- Engineer *S. alvi* to express dsRNA → triggers RNAi in the bee host
- Achieves **50–75% reduction** in targeted gene expression throughout the bee body within 5 days
- Published as a formal protocol in *Nature Protocols* (2022)
- The original *Science* paper (Leonard et al. 2020) showed engineered symbionts protect bees from DWV (deformed wing virus) and *Varroa* mites

Kathleen's extension: instead of (or in addition to) dsRNA for gene knockdown, she's engineering *S. alvi* to **secrete peptides directly** — moving from information-based (RNAi) to molecular-based (peptide) protection.

### The Bee Microbiome Toolkit (BTK)

The lab's genetic toolkit for bee symbionts includes:
- Electroporation of *S. alvi* for chromosomal integration (Leonard et al. 2024 *mBio* — "one-step genome engineering")
- No exogenous recombination machinery needed — uses natural recombination in *S. alvi*
- Same method works for *S. communis* and *Bartonella apis*
- Conjugation-based plasmid transfer from *E. coli* to *S. alvi*
- Golden Gate assembly for dsRNA expression plasmids

### Prior: Nancy Moran's Lab (UT Austin)

Kathleen spent years in Moran's lab:
- Honeybee gut microbiome characterization
- Characterized novel **Orbaceae** species in *Drosophila* gut
- **Lyophilization** of bacterial strains (preservation expertise — relevant to LTEE frozen stocks)
- Research Engineering Scientist Associate I at UT Austin (2023–2025) before starting grad school

The lyophilization experience is notable — freeze-drying bacterial cultures for long-term storage is operationally similar to the LTEE frozen fossil record glycerol stocks.

---

## What She Needs (Wet Lab)

- **Bee colonies**: Maintaining gnotobiotic (germ-free) and conventional bee colonies for experiments
- **Bacterial culture**: Growing *S. alvi* (microaerobic conditions), *E. coli* (donor strain for conjugation)
- **Construct engineering**: Cloning peptide-secretion cassettes, transforming into *S. alvi*
- **Colonization assays**: Quantifying engineered *S. alvi* in the bee gut over time (CFU counts, 16S, qPCR)
- **Pathogen challenge**: Infecting bees with viruses or mites, measuring protection from engineered symbionts
- **Gene expression**: RT-qPCR or RNA-seq to measure knockdown or peptide expression levels

## What She Needs (Dry Lab)

- **Colonization dynamics modeling**: Does the engineered strain establish reliably? What determines colonization density over time?
- **Gene expression quantification**: RNA-seq analysis from bee gut samples with engineered symbionts
- **Construct stability tracking**: Do the engineered cassettes persist over bee generations? Over bacterial generations in the gut?
- **Microbiome community analysis**: How does introducing an engineered strain affect the rest of the bee gut community?

## How We Multiply Her Work

| Her Need | Our Tool | Impact |
|----------|----------|--------|
| Colonization dynamics | healthSpring PK/PD (Hill equation) | Dose (inoculum) → response (colonization level) → effect (gene knockdown) |
| Anderson-QS prediction | wetSpring Anderson model | Bee gut is 3D biofilm → QS-active geometry. Engineered S. alvi in the gut maintains coordinated gene expression because the spatial geometry is 3D (extended regime). If the symbiont disperses or the gut community shifts geometry, coordination breaks. **Specific prediction: colonization density below a threshold → coordinated peptide secretion fails** |
| 16S community analysis | wetSpring sovereign pipeline (1,368 checks) | Process bee gut 16S from colonization experiments |
| Construct stability | breseq + wetSpring | Track mutations in the engineered cassette over passages |
| RNA-seq quantification | wetSpring + neuralSpring | GPU-accelerated alignment + ML for expression prediction |
| Peptide structure | coralForge | Predict secreted peptide structure, stability in gut conditions |
| Microbiome impact | wetSpring diversity metrics | Shannon/Simpson/Bray-Curtis before/after engineered strain introduction |

**The pitch to Kathleen**: "The colonization dynamics question is really interesting — it's basically a pharmacokinetics problem where the 'drug' is a bacterium and the 'dose' is colonization density. I've been building PK/PD models that map dose → response → effect, and I think that framework applies to your symbiont work. Also, I have a 16S pipeline that can process bee gut community data if you need to track how the engineered strain affects the rest of the microbiome. And — this is more speculative — I've been working on a framework from physics that predicts whether bacterial communication (quorum sensing) works based on the 3D geometry of the environment. The bee gut is a 3D biofilm, which means your engineered *S. alvi* should be able to coordinate gene expression even in a diverse community."

---

## Personal

Reading, video games, dog. Came to MSU from UT Austin with the lab move (Jan 2025).
