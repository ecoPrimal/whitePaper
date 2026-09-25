# Kevin Mok — Introduction

**Date**: June 2026
**Contact**: mokkevin@msu.edu | (586) 453-7233
**Infrastructure**: [primals.eco](https://primals.eco) | [lab.primals.eco](https://lab.primals.eco)

---

## The Short Version

I'm a substrate builder. I work in the layer underneath the science — the hardware, the math, the pipelines, the provenance — so that domain experts can focus on their questions instead of fighting their tools. I own and operate a sovereign compute mesh, I write GPU shaders and validation pipelines in Rust, and I reproduce published science from scratch to prove the infrastructure actually works. Everything I build is open source, everything is published, and everything runs on hardware I own.

What I'm looking for are scientists with domain expertise and curiosity. I bring the substrate. You bring the science.

---

## Background

### Education

**Michigan State University** — MS Data Science, College of Natural Science (2025, 3.9 GPA)

Graduate coursework: Foundations of Data Science, Computational Optimization, Big Data Analysis, Computational Foundations in AI, Data Mining, Machine Learning, Applied Machine Learning (Professor Murillo), Deep Learning, Design & Theory of Algorithms, Applied Statistical Modeling, Mathematical Statistics.

**Michigan State University** — BS Microbiology, Minor Bioethics (2018)

Upper-division coursework: Microbial Genetics, Prokaryotic Cell Physiology, Medical Microbiology, Virology, Molecular Pathogenesis, Fundamental Genetics, Comprehensive Biochemistry.

Programming started with AP Computer Science (Java) sophomore year of high school — a decade before the Data Science degree. The two degrees are the two halves of what I build: microbiology is the science that informs the architecture, data science is the computation that executes it.

### The Arc

There's a 5-year gap in the transcript. I enlisted after my first two years at MSU, as I found myself floundering. When I came back from the Army in 2015, my first semester was a 4.0 with Dean's List. I made Dean's List in 4 of my last 5 undergraduate semesters. The graduate record was near-4.0 across 36 credits. The trajectory matters more than the starting point — the discipline to focus under constraint is something the Army teaches and the lab reinforces.

### Bench Experience

**Sandia National Laboratories** (Summer 2024) — Research Fellow. High-throughput sequencing and bioinformatics. Investigated bacterial toxin effects on raceway algae. This is where the sequencing pipeline experience comes from.

**PFAS Research Lab, Michigan State University** (October 2024 – Present) — Research Specialist. Environmental chemistry and biomolecular methods for PFAS detection and remediation. EPA SOPs, sample processing, data science applied to "forever chemicals."

**MSU Bioeconomy Institute** (January 2019 – May 2024) — Biotechnician. Five years in a contract lab. Fungi, mycobacteria, anaerobes, aerobes, GMOs. Bench-scale fermentation in BSL2 — shake flask to 10L reactor (pilot plant ran ~3,000L). Culture media preparation, aseptic technique, viable cell counts, spore counts, microscopic identification, isolation on selective media, optical density, contaminant ID. Chemical assays: PO₄, NH₃, mass spectrometry, HPLC, enzyme kinetics. Clients included [Pivot Bio](https://www.pivotbio.com/) (nitrogen-fixing microbes) and [MycoWorks](https://www.mycoworks.com/) (mycelium materials).

**Hausbeck Plant Pathology Lab, MSU** (2018–2019) — Research Assistant. Spore capture, DNA extraction, microscopy. Field liaison for spore trapping across Mid-Michigan farms.

**ROME Lab, MSU** (2018) — Undergraduate Research. Bacterial isolation from rumen samples. Serial enrichment, selective media, sequence analysis via the Ribosomal Database Project.

### Military Service

**U.S. Army** (2012–2015) — Infantryman, 25th Infantry Division, Schofield Barracks, HI

Company Intelligence Support Team (COIST): Intelligence reporting, terrain modeling from topographical maps and satellite imagery, briefing/debriefing personnel. Radio Transmission Operator (RTO): Supervised communications equipment and managed cryptographic keys for secure telecommunications.

The terrain modeling experience directly informs how I think about biological data — translating contour lines and elevation data into three-dimensional pictures of ground you can't see yet. The expression data in a drug discovery pipeline is the same problem at a different scale.

---

## Why the Substrate Matters

Most computational science breaks at the infrastructure layer. Dependencies rot. Code that worked on Python 2.7 with a pinned NumPy doesn't run five years later. Results that were "reproducible" require a specific grad student's laptop. Data that was "available" lives behind a login that expired.

I build infrastructure that doesn't have these problems. Every computation is provenance-tracked — who ran it, when, on what hardware, from what data, with what parameters. Every pipeline is self-verifying — it checks its own output against named tolerances derived from the original publication. Every artifact is portable — hand someone a USB drive or a pseudoSpore, and they can reproduce the result without installing anything or trusting anyone.

This is what I mean by working in the substrate. I don't pick the biological question. I build the ground the question stands on, and I make sure it holds.

---

## Why I Can Work Across Domains

The same reason I can work across terrain. In the Army, the skill wasn't knowing the geography — it was reading the abstraction layer and building something navigable from it.

Science has the same structure. A published paper is a topographic map. The data is the contour lines. The methods are the legend. The results are the terrain. If you can read the abstraction layer — trace a data dependency, understand a statistical claim, reproduce a computational pipeline — you can navigate any domain. You won't be the person who designs the next experiment. But you'll be the person who makes sure the last experiment's results are solid before the next one runs.

In the wetlab, the same principle applies. I can grow cultures, run assays, set up models, and design experiments — not because I specialize in any one organism or pathway, but because I understand the substrate: sterile technique, growth kinetics, measurement principles, experimental controls. Five years at MSUBI across fungi, mycobacteria, anaerobes, aerobes, and GMOs. Sandia for sequencing. PFAS lab for environmental chemistry. The microbiology degree is the foundation. The data science degree is the computational mirror.

I'm a generalist by design, not by default. Jack of all trades, aiming to be a sage of many paths.

---

## Proof of Work

The way I introduce myself to a scientist is by reproducing their published work. Not by citing it — by running it, validating the results on my own hardware, and showing them what passes.

| Faculty | Domain | What Was Reproduced | Result |
|---------|--------|---------------------|--------|
| Murillo (MSU) | Plasma physics, MD | Sarkas Yukawa OCP MD, TTM, surrogate learning | 195/195 checks, 0.000% energy drift on $600 GPU |
| Dong (MSU) | Precision agriculture | FAO-56, sensor calibration, IoT irrigation | 326 checks, R²=0.967 across 918 station-days |
| Waters (MSU) | Quorum sensing | 7 papers: QS, c-di-GMP, phage defense | ODE models, signaling networks reproduced |
| Liu (MSU) | Phylogenetics | PhyloNet-HMM, SATé, introgression | 42+ checks, phylogenetic pipelines reproduced |
| Bazavov (MSU) | Lattice QCD | SU(3) Wilson, Abelian Higgs, QCD EOS | 29+ checks, lattice QCD on consumer GPU |
| Dolson (MSU) | Evolutionary computation | Counterdiabatic driving, MODES, directed evolution | 46 checks |
| Kachkovskiy (MSU) | Spectral theory | Anderson localization (11 papers) | Spectral methods on GPU |
| Anderson (MSU) | Extremophile evolution | 6 papers on metagenomics, pangenomics | 133+ checks |
| Jones (MSU, emeritus) | Analytical chemistry | PFAS detection, mass spec pipelines | 40+ checks, 926× GPU speedup |

When you've reproduced a professor's life work on consumer hardware and the results pass, the introduction is the artifact — not a letter.

---

## How One Person Builds This

AI-assisted constrained evolution. The methodology is published in the ecosystem, but the short version:

The AI is the **mutation operator** — it generates candidate code at high frequency. The Rust compiler is **natural selection** — it eliminates unsound candidates at compile time. I provide the **environmental design** — the constraints, the architecture, the selective pressure that shapes what the AI produces.

69,000 agent invocations. 51 billion tokens processed in 2025 alone. Top <0.1% of all Cursor IDE users. One person with a microbiology degree, a data science degree, and hardware purchased from Facebook Marketplace and Newegg sales. The methodology is the bridge between the background and the output.

The ecosystem is not a team effort in the traditional sense. It's one scientist using AI as an evolutionary search tool within a constraint environment (Rust's type system, Pure Rust mandate, primal isolation). The architecture, the biological analogies, the scientific direction — those are mine. The AI generates candidates. The compiler selects. I design the environment.

---

## What ecoPrimals Is

ecoPrimals is the ecosystem I've built over the past two years. It's three things:

**Hardware** — A sovereign mesh of 11 gates (physical computers I own), ~1 TB system RAM, ~248 GB GPU VRAM across NVIDIA and AMD, 122 TB storage, 10G backbone, 3 neuromorphic chips. No cloud. No queue times. No shared anything. ~$15K total investment, assembled from consumer and secondary market hardware. Every watt and every piece of silicon is mine to point at whatever the science needs.

**Software** — 14 composable primals (self-contained Rust binaries), each solving one domain well. barraCuda writes the math (712+ GPU shaders). toadStool discovers and dispatches to hardware. coralReef compiles shaders to native GPU binaries without vendor SDKs. The provenance trio — rhizoCrypt, loamSpine, sweetGrass — tracks every computation from input to output. biomeOS orchestrates the whole thing.

**Validated Science** — 7 springs (validation environments), each anchored to a scientific domain and a faculty collaborator. 12,510+ automated science checks across 70+ reproduced papers. Drug discovery, genomics, molecular dynamics, microbial evolution, environmental chemistry, machine learning, game design. Every spring validates that the primals produce correct science for its domain.

The naming is biological because the architecture is biological. Primals are like enzymes — small, specific, composable. Springs are like ecosystems — they test whether the enzymes work together in a real environment. Gates are the physical substrate everything runs on. The vocabulary is ours, and it's consistent across the project.

---

## What I Bring to a Collaboration

| What | Specifically |
|------|-------------|
| **Compute** | Dedicated sovereign mesh — your workloads don't queue behind anyone else's |
| **Reproducibility** | Every result is a self-verifying artifact. Hand it to a reviewer, a student, or a skeptic — "run this, see what passes" |
| **Lineage tracing** | I go back to the original papers, not just the latest code. 20-year paper chains become validation targets |
| **Infrastructure** | GPU shaders, provenance tracking, data pipelines, cryptographic attribution — already built and tested |
| **Bench + computation** | Microbiology, data science, terrain analysis, hardware — I can read across domains and build the connective tissue |
| **Independence** | No institutional overhead. No approval chains. No grant cycles to wait on. I can start work today |

---

## What I'm Looking For

Domain experts with questions that matter to them.

I don't need to own the science. I need scientists who know what the right question is, who can evaluate whether a computational result makes biological sense, and who can design the next experiment when the computation says something surprising. The iterative cycle — data science to characterize the problem, wetlab to test, computation to refine, wetlab again — is where discovery happens. I want to be the substrate that makes that cycle fast, reproducible, and permanent.

The GPS revalidation is the first instance of this pattern. Andrea Gonzales connected me with the work; Bin Chen's lab built the 20-year lineage. I'm rebuilding it from the methods to understand where it holds, where it compresses, and where the next evolution starts. The NF extension applies the same methods to a different disease. The infrastructure handles both.

If you have a biological question, a dataset, or a computational pipeline that needs to be more reproducible, more scalable, or more honest about what it actually proves — that's what I build for.

---

## Links

- [primals.eco](https://primals.eco) — project overview, published papers, validated pipelines
- [lab.primals.eco](https://lab.primals.eco) — live computational environment (browsable, no login)
- [github.com/ecoPrimals](https://github.com/ecoPrimals) — infrastructure primals (14 repos, all AGPL-3.0)
- [github.com/syntheticChemistry](https://github.com/syntheticChemistry) — science validation springs (7 repos)
- [github.com/sporeGarden](https://github.com/sporeGarden) — user-facing products (5 repos)
