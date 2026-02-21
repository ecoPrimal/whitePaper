# About the Author and the Lab

**Purpose**: Context for understanding who built this system, with what tools, and on what hardware  
**Audience**: Anyone reading the gen3/ papers who wants to know the background

---

## Kevin Mok

Microbiologist turned data scientist turned systems architect. The biological analogies in these papers are not borrowed metaphors - they come from years of bench work with microbial populations under selective pressure.

### Academic Background

**High School** - AP Computer Science (Java, sophomore year), AP Calculus AB, AP Calculus BC. Programming and math started early - a decade before the Data Science degree.

**Michigan State University** - BS Microbiology, Minor Bioethics (2018)

Upper-division coursework in Microbial Genetics (MMG 431), Prokaryotic Cell Physiology (MMG 421), Medical Microbiology (MMG 365), Virology (MMG 413), Molecular Pathogenesis (MMG 461), Fundamental Genetics (IBIO 341), and Comprehensive Biochemistry (BMB 401). This is the training that produced the Lenski LTEE parallels, the Taq polymerase constraint argument, and the enzyme thesis for P != NP. These are not analogies looked up for a paper - they are the foundational science of the author's education.

**Michigan State University** - MS Data Science, College of Natural Science (2025, 4.0 GPA through 27 credits)

Graduate coursework: Foundations of Data Science (CMSE 830), Computational Optimization (CMSE 831), Big Data Analysis (CSE 482), Computational Foundations in AI (CSE 840), Data Mining (CSE 881), Machine Learning (CSE 847), Applied Machine Learning (CMSE 890 - Professor Murillo's course), Deep Learning (CSE 849), Design & Theory of Algorithms (CSE 830), Applied Statistical Modeling (STT 811), Mathematical Statistics for Data Scientists (STT 810).

The constrained evolution methodology emerged from the intersection of these two degrees: microbiology's understanding of evolution under constraint, and data science's computational optimization and machine learning frameworks. The `CONSTRAINED_EVOLUTION_FORMAL.md` paper is not a software engineering document that borrows from biology - it is a biology-informed framework applied to computation.

Full transcript: `TRANSCRIPT.md`

### Bench Experience

**Sandia National Laboratories** (Summer 2024) - Research Fellow  
High-throughput sequencing and bioinformatics. Investigated bacterial toxin effects on raceway algae. This is where the sequencing and bioinformatics pipeline experience that informs the "Sequencing the Lenski Library" proposal comes from.

**PFAS Research Lab, Michigan State University** (October 2024 - Present) - Research Specialist  
Environmental chemistry and biomolecular methods for PFAS ("forever chemicals") detection and remediation.

**MSU Bioeconomy Institute** (January 2019 - May 2024) - Biotechnician  
Five years in a contract lab working with fungi, mycobacteria, anaerobes, aerobes, and GMOs. Bench-scale fermentation (shake flask to 10L reactor; pilot plant did ~3,000L). Culture media preparation, BSL2 work, aseptic technique, viable cell counts, spore counts, microscopic identification, isolation on selective media, optical density, contaminant ID. Chemical assays: PO4, NH3, mass spectrometry, HPLC, enzyme kinetics.

Projects included work for [Pivot Bio](https://www.pivotbio.com/blog/seedsafety) (nitrogen-fixing microbes), [MycoWorks](https://www.mycoworks.com/scientificresources) (mycelium materials), and the [MSU Center for PFAS Research](https://www.canr.msu.edu/news/center-for-pfas-research-faculty-spotlight-a-daniel-jones).

This is the lab background that makes the constrained evolution analogy concrete: five years of watching microbial populations adapt to selective media, seeing how environmental constraints shape what organisms become.

**ROME Lab, Michigan State University** (January - May 2018) - Undergraduate Research Assistant  
Bacterial isolation from rumen samples. Serial enrichment and dilution. Selective media for specific carbon degraders. Sequence analysis via the Ribosomal Database Project (RDP). This is where the "sequence the Lenski library" idea started forming - analyzing bacterial diversity from environmental samples using sequencing pipelines.

**Hausbeck Plant Pathology Lab, Michigan State University** (May 2018 - January 2019) - Research Assistant  
Spore capture, DNA extraction, microscopy. Field liaison for spore trapping across Mid-Michigan farms.

### Military Service

**U.S. Army** (2012 - 2015) - Infantryman, 25th Infantry Division, Schofield Barracks, HI

Company Intelligence Support Team (COIST): Intelligence reporting, terrain modeling from topographical maps and satellite imagery, briefing/debriefing 130 personnel. Radio Transmission Operator (RTO): Supervised $2M in communications equipment with zero loss. Managed cryptographic keys for secure telecommunications. Created troubleshooting guides for field communications.

The military background is relevant to ecoPrimals in two ways: (1) the Dark Forest security model and genetic trust hierarchy are informed by experience with military communications security and need-to-know access control, and (2) the discipline of maintaining complex systems under constraint (field communications equipment, BSL2 lab protocols, now a basement HPC) is the same discipline applied to different hardware.

---

## The Hardware

The ecoPrimals ecosystem runs on a basement HPC cluster. Not a cloud deployment. Not rented compute. Physical machines purchased, assembled, and networked by the author. Total investment: ~$15,000.

This is the "covalent mesh" described in `ECOSYSTEM_ARCHITECTURE.md` - physical computers bonded by genetic trust, each running its own NUCLEUS optimized for its hardware profile.

Full hardware inventory: `HARDWARE.md`

**Highlights**:
- **Northgate**: i9-14900K, RTX 5090, 192GB DDR5 - Flagship AI/LLM compute
- **Southgate**: 5800X3D, RTX 3090, 128GB DDR4 - Gaming tower upgraded for the mesh
- **Strandgate**: Dual EPYC 7452 (64 cores), 256GB ECC DDR4 - Alignment, Kraken2, bioinformatics
- **Westgate**: i7-4771, RTX 2070 Super, 76TB ZFS - Cold storage (built during Army service, still running)
- **6 additional gates** + Pixel 8a mobile node + 4x SoloKeys for HSM

The heterogeneous hardware is a feature, not a limitation. Each gate specializes in what its hardware does best. The NUCLEUS atomic model and bonding architecture emerged from the practical reality of coordinating DDR3-to-DDR5, RTX 2070-to-RTX 5090, 32GB-to-256GB across one network.

---

## The AI-Assisted Methodology

This project was built using AI-assisted constrained evolution. The methodology is described formally in `CONSTRAINED_EVOLUTION_FORMAL.md`. Here is the practical receipt.

### Model Usage

![Cursor 2025 Usage Statistics](cursor-2025-receipt.png)

**Cursor IDE** - AI-integrated development environment  
- **Usage**: Top <0.1% of all Cursor users
- **Models**: Claude 4 Sonnet (primary), Claude 4.5 Sonnet, Claude 3.7 Sonnet
- **Agent invocations**: 69,000
- **Tokens processed**: 51.07 billion
- **Streak**: 185 consecutive days
- **Period**: ~10 months (299 days since joining)

These numbers represent the "iterative generation" component of the constrained evolution methodology: 69,000 agent invocations generating candidate solutions, each tested against Rust's type system (the constraint), each guided by architectural direction (the selective pressure). 51 billion tokens is the raw evolutionary search through the solution space.

### What "AI-Assisted" Means Here

The AI did not design the architecture. The AI did not choose Rust, or the Pure Rust constraint, or the primal isolation model, or the capability-based coordination pattern. The AI did not write the biological analogies or propose the P != NP thesis.

The AI was the **mutation operator**. It generated candidate code within the constraint environment. The Rust compiler was **natural selection** - it eliminated unsound candidates. The developer provided **environmental design** - the constraints and selective direction that shaped what the AI produced.

This is the methodology described in `CONSTRAINED_EVOLUTION_FORMAL.md` §3.1: Environmental Constraint (Rust), Selective Direction (the developer's architectural vision), Iterative Generation (AI-assisted code generation at high frequency). The 69,000 agent invocations are 69,000 cycles of generate-compile-test-select.

A single developer with a microbiology degree and a data science degree built a 6-primal production sovereign computing ecosystem (with 5 more started) in ~6-8 months. That is the claim. The Cursor receipt is the evidence for the scale of AI involvement. The architecture and methodology papers are the evidence for how that involvement was structured.

### Why This Matters for Evaluation

An academic evaluator may assume this project involved a team of experienced systems programmers. It did not. It involved one person with bench science and data science training, using AI as a constrained evolutionary search tool, on hardware purchased from Facebook Marketplace and Newegg sales.

The methodology is the point. If the architecture is coherent, the tests pass, and the benchmarks are real - and they are - then the constrained evolution methodology works as described. The author's background is not traditional for systems programming. The results are not traditional for a single developer. The methodology is what bridges the gap.

---

## Contact

Kevin Mok  
mokkevin@msu.edu  
(586) 453-7233  
Lansing, MI area

---

## Document Index

- `README.md` - This file (author background, education, bench experience, AI methodology)
- `FACULTY.md` - Faculty interaction profiles — personal connections to each professor, their papers reproduced in the springs, what those reproductions validated
- `SOVEREIGN_SCIENCE.md` - The philosophical frame: why open publication + named review + consumer hardware changes the game. Artificial scarcity in journals, PhD programs, and HPC allocation. Proof of work over citation-sitting.
- `TRANSCRIPT.md` - Academic transcript (cleaned, organized)
- `HARDWARE.md` - Basement HPC inventory
- `cursor-2025-receipt.png` - Cursor IDE usage receipt (source: cursor.com/2025)

Related: `attsi/non-anon/contacts.md` has the contact directory. `gen3/thesis/references.md` has the formal bibliography. `FACULTY.md` connects the two — it's the narrative of how the author's life intersected with the science in the springs. `SOVEREIGN_SCIENCE.md` is why it's structured this way.
