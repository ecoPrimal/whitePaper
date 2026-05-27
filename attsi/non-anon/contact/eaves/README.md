# Joelle Eaves — Contact Notes

**Name**: Joelle Eaves (She/They)
**Email**: jeaves@msu.edu
**LinkedIn**: https://www.linkedin.com/in/joelle-eaves/
**Role**: PhD Student (NSF Graduate Research Fellow), Michigan State University
**Department**: Chemical Engineering and Materials Science
**Status**: Writing dissertation (as of May 2026)

---

## Background

- **B.S. Chemical Engineering**, Michigan State University, 2022
- **NSF GRFP awardee** — prestigious competitive fellowship
- Started in **Woldring Lab** (Daniel Woldring, protein engineering, yeast display, directed evolution)
- Moved to **Gilad Lab** (Assaf Gilad, synthetic biology, IQ) in 2022 as incoming doctoral student
- Now listed as **Gilad Lab alumni** — currently writing up dissertation
- 2024-25 departmental nominee for Three Minute Thesis (3MT) competition (advisor: Woldring)

## Research Focus

- High-throughput **directed evolution** workflows
- **Protein engineering** — characterization and activity tuning
- **Machine learning** for protein prediction and binder discovery
- Electromagnetic perceptive gene (EPG) from glass catfish — Gilad Lab focus
- Phytochemical drug discovery for COVID-19 (computational docking + ML binder prediction)
- Yeast surface display (Woldring Lab methods)

## PI: Daniel Woldring
- Assistant Professor, Chemical Engineering & Materials Science, MSU
- Member, Institute for Quantitative Health Sciences and Engineering (IQ)
- Research: high-performance therapeutics/diagnostics via protein engineering
- Methods: directed evolution, yeast display, high-throughput sequencing, ancestral sequence reconstruction
- Background: BS ChE (Michigan Tech), PhD ChE (U Minnesota), Postdoc HHMI (Brandeis)
- Also studies: continuous growth bioreactors for enzyme evolution under harsh conditions

## PI: Assaf Gilad
- Chief, Division of Synthetic Biology and Regenerative Medicine, IQ at MSU
- Professor, Biomedical Engineering and Radiology
- Research: synthetic biology circuits, MRI reporter genes, EPG protein, magnetobiomanipulation
- Background: BS (Technion), PhD (Weizmann), Faculty (Johns Hopkins → MSU)

---

## Connection to Our Work

### Intersection Points
1. **Protein engineering + ML** — her core expertise overlaps with coralForge (structure prediction), neuralSpring (ML pipelines), and healthSpring (drug discovery)
2. **Directed evolution** — isomorphic to the constrained evolution thesis. Woldring's work on "how ancestral enzymes efficiently evolve under harsh conditions within continuous growth bioreactors" is literally constrained evolution in a tube
3. **High-throughput screening + computation** — same dual bench/computation integration we bring to any lab
4. **Drug discovery pipeline** — Woldring Lab develops therapeutics; connects to Gonzales/ADDRC work
5. **Yeast display libraries** — Anderson localization framework could model binding landscape diversity as disorder parameter

### What She Might Need
- **Compute and pipeline bottlenecks** — she mentioned her lab mates might have compute needs
- **Protein modeling** — ML-assisted binding prediction is directly in our wheelhouse
- **Reproducible compute** — Rust-based scientific workflows vs Python notebook fragility
- **GPU acceleration** — protein structure prediction and docking are GPU-hungry

### What We Bring
- Spare GPU/CPU capacity on ironGate
- Rust-based tooling for scientific workflows
- coralForge: sovereign structure prediction engine (AlphaFold2/3 primitives, 154 checks)
- neuralSpring: ML pipelines for protein sequence analysis
- Reproducible, validated compute with provenance tracking

---

## Communication Thread

### May 10, 2026 — Kevin → Joelle (LinkedIn)
Reached out noting shared connection from Murillo's Applied ML class (CMSE 890, Spring 2025). Highlighted protein engineering / ML intersection. Mentioned local compute stack with GPU/CPU capacity, Rust-based scientific tooling. Offered to explore compute/pipeline bottlenecks or non-sensitive test cases.

### May 10, 2026 — Joelle → Kevin (LinkedIn)
Positive response. Currently writing dissertation, not much on her plate but lab mates might have needs. Interested in learning more. Suggested a Zoom call. Provided MSU email (jeaves@msu.edu) and asked for availability this week.

### May 11, 2026 — Kevin → Joelle (Email)
Sent follow-up to jeaves@msu.edu. Pitched the cluster: 11 nodes, 154 cores, 248 GB VRAM, 1 TB RAM, 122 TB storage. Linked lab.primals.eco and primals.eco. Framed as "looking for external workloads to prove parity — any domain." Proposed Zoom this week.

### May 13, 2026 — Zoom Call (Kevin ↔ Joelle)
**Very receptive.** Outcome:
- Will talk to **grad students** in the lab about compute needs and forward them
- Will also connect with **CMSE undergrads** working on projects who may benefit
- Contacts will be sent to Kevin's **MSU email** (mokkevin@msu.edu)
- Casual, positive tone — genuine interest in the compute offer

---

## Next Steps

1. ✅ ~~Email jeaves@msu.edu with availability~~ (done May 11)
2. ✅ ~~Zoom call~~ (done May 13 — very receptive)
3. **Wait for inbound contacts** from grads and CMSE undergrads via mokkevin@msu.edu
4. **Prepare onboarding** — ready to spin up reviewer/user accounts on lab.primals.eco for anyone she sends
5. **Have a demo-ready workload** — something visual they can see immediately (16S dashboard, paper reproductions, benchmark comparison)
6. **Dissertation revalidation offer** — drafted `email_revalidation_offer_may2026.md`. Offer to independently revalidate her dissertation work and confirm/document non-replicable gaps in the literature she built on. She's the rigor & reproducibility contact — she discovered only a fraction of papers in her domain are reproducible.
7. Potential gateway to Woldring and/or Gilad as faculty contacts once students are engaged

---

## Context: Murillo's Applied ML Class (CMSE 890, Spring 2025)

Kevin and Joelle were both in Professor Michael Murillo's Applied Machine Learning course. Murillo is one of Kevin's references and has seen the computational work (hotSpring papers reproduced, 195/195 checks). This shared class provides the warm connection.
