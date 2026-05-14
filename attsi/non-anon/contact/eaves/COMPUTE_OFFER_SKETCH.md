# Compute Access — For Woldring Lab, CMSE Students, and Friends/Colleagues of Joelle

**From**: Kevin Mok (BS Microbiology, MS Data Science — MSU)
**Contact**: mokkevin@msu.edu
**Live environment**: [lab.primals.eco](https://lab.primals.eco) — static page auto-published from the hub. Browse notebooks, validations, and benchmarks without logging in. Still rough in places — work-in-progress published as it develops.
**Project site**: [primals.eco](https://primals.eco)
**Date**: May 2026

---

## The short version

I have a home 'basement HPC' cluster with spare capacity. I'm looking for real workloads from real researchers to prove it competes with institutional systems. You get free compute. I get external validation. Everybody's science moves faster.

Joelle and I connected through CMSE 890 (Murillo's Applied ML, Spring 2025). She thought some of you might have jobs that take too long on HPCC or a laptop. This doc explains what's available and how to ask for it.

---

## What's available

**Hardware summary** — 11 physical nodes, reconfigurable:

| Resource | Total | Notes |
|----------|-------|-------|
| CPU cores | ~154 | Dual EPYC 7452 (64c), Threadripper 3970X (32c), Ryzen 9950X3D, i9-14900K, and others |
| GPU VRAM | ~248 GB | RTX 5090, 2× RTX 3090 (24 GB each), 2× Titan V (12 GB HBM2 each), RTX 5070, RTX 4070, AMD MI50, and others |
| System RAM | ~1 TB | 256 GB ECC on the big nodes, 96–128 GB on the rest |
| Storage | 122 TB | 76 TB ZFS cold + ~46 TB NVMe scratch |
| Network | 10G backbone | Nodes talk fast; internet is residential (big pulls staged overnight) |

GPU cards float between machines. Need a 3090 next to 64 cores and 256 GB RAM for a big alignment? I can make that happen.

**Access**: JupyterHub — per-user accounts, browser-based, nothing to install on your end. You get a notebook environment with the tools you need pre-loaded. Work done in the hub feeds into a pipeline (pappusCast) that publishes rendered notebooks to the public-facing static page at [lab.primals.eco](https://lab.primals.eco). The public page showcases the [syntheticChemistry](https://github.com/syntheticChemistry) springs' validated work and will continue to grow as more science runs through it.

---

## What kinds of jobs fit well

This is roughly sized to the Woldring Lab / CMSE intersection, but anything compute-hungry is welcome:

| Your problem | What helps | Which node |
|-------------|-----------|------------|
| AlphaFold / structure prediction queue | GPU VRAM (3090 or Titan V handles most single chains) | biomeGate or strandGate |
| ML training (GNN, transformers, LSTM) | GPU + large RAM for batches | ironGate (RTX 5070) or northGate (RTX 5090) |
| Protein-ligand docking (AutoDock, Vina, etc.) | CPU cores for parallel runs, GPU for rescoring | strandGate (64 cores) |
| Sequence alignment (STAR, BLAST, HMMER) | RAM-hungry, scales with cores | strandGate (256 GB, 64 cores) |
| scRNA-seq (Scanpy, Seurat, 50K+ cells) | 32–64 GB RAM minimum | strandGate or biomeGate |
| MD simulations (GROMACS, OpenMM) | GPU-bound, HBM2 bandwidth helps | biomeGate (Titan V — HBM2) |
| Big data pulls from SRA/GEO/NCBI | Staged overnight to ZFS cold storage | westGate (76 TB) |
| "My laptop ran out of memory" | Literally any node here | ironGate is the easy on-ramp |

**What doesn't fit**: HIPAA/PHI data (no compliance infrastructure), proprietary/NDA work (see openness section below), or multi-hundred-TB raw genomics (we'll talk first).

---

## How to ask for compute

Send me an email (mokkevin@msu.edu) or message me. Include whatever you know from this list — rough is fine, we'll figure it out together:

1. **What you're trying to do** — one sentence ("run AlphaFold on 200 sequences," "train a GNN on OATP binding data," "my Seurat pipeline dies at the clustering step")
2. **Data source + rough size** — "3 GEO datasets, ~20 GB" or "SRA PRJNA_____, ~500 GB raw" or "I have CSVs on my laptop, 2 GB total"
3. **Software / tools** — what you already use (Python packages, R packages, command-line tools, containers)
4. **What's slow right now** — the bottleneck. Is it RAM? GPU? Queue time on HPCC? This tells me which node to set you up on

Don't overthink it. "I have a thing that's slow and here's roughly what it is" is a perfectly fine starting point.

---

## What I'm building and what I get out of this

I've spent the past year+ building validated scientific computing pipelines in Rust — genomics (16S/WGS, 1,368 validation checks), protein structure prediction (AlphaFold2/3 primitives, 154 checks), ML (1,800+ checks across 25 papers), pharmacokinetics, and GPU-accelerated math across all of it. The tools reproduce published papers and pass quantitative checks against known answers.

But it's all self-validated so far. When independent researchers run real workloads on this infrastructure and get real results, that's external proof the system works. That's the trade: you get compute, I get evidence that the infrastructure holds up under workloads I didn't design.

I'm not looking for authorship, co-PI status, or to steer anyone's research. Your work is your work. I'm the infrastructure person.

**My background**: bench microbiology (fermentation, PFAS, algal bioinformatics at Sandia), MS in Data Science (MSU), then the computational work above. I understand both the biology and the compute side.

---

## Environments — use what you know

You don't need to learn anything new to use this. I set up whatever you're already comfortable with:

- **Python** — conda, pip, Jupyter, PyTorch, TensorFlow, JAX
- **R** — RStudio Server, Bioconductor, Seurat, DESeq2
- **Command-line tools** — BLAST, HMMER, GROMACS, AutoDock, breseq, Kraken2, STAR
- **Containers** — Docker, Singularity/Apptainer (bring your existing container images)
- **Fortran / C / C++** — if you have legacy code, bring it
- **MATLAB** — via Octave (free, compatible for most scripts)

Got an old pipeline that "only works on my old laptop"? That's exactly the kind of thing I like setting up.

---

## Openness and terms

Work done on this infrastructure is open. This is a feature, not a catch:

- **Code and pipelines**: AGPL-3.0 — open source, modifications shared back
- **Results and data**: CC-BY-SA 4.0 — shareable with attribution
- **You keep full credit** for your analysis, your interpretation, your publications

In practice, if you're doing open science on public data (GEO, SRA, NCBI, PDB, UniProt), nothing changes about how you work. Your inputs are already public. Your novel contribution is the analysis. Here, that analysis gets timestamped and backed up from the moment you run it.

**What this prevents**: nobody — including me — can lock up what gets produced. I can't privatize your results. You can't privatize mine. Proprietary or NDA-bound work should stay on your own resources.

**Why this is actually good for you**: timestamped, visible work on a shared system is stronger priority protection than a laptop and a prayer. Your analysis is hashed the moment you run it. If you're worried about getting scooped, structural proof of priority beats secrecy.

---

## Relevant to Woldring Lab specifically

I've read the published work from the lab and built tools that intersect directly:

- **Protein structure prediction** — I have a sovereign AlphaFold2/3 engine (pure Rust, GPU-accelerated, 154 validation checks). No HPCC queue, no cloud dependency. Single-chain predictions in minutes on a 3090.
- **ML for protein-ligand (HOLIgraph-style)** — I have GPU-accelerated GNN, LSTM, and ESN inference pipelines. If you want to run inference faster or train on larger datasets, the hardware is here.
- **Library design** — I've been working on a framework (from condensed matter physics) that predicts which protein positions tolerate randomization vs. which need conservation. Happy to explain over coffee or Zoom — it maps surprisingly well to the sitewise diversity work.
- **Yeast display / directed evolution** — my thesis work uses the same fitness landscape physics that governs directed evolution, just applied to microbial evolution and computational systems. Same math, different organisms.

None of this requires you to care about my tools. If you just want a fast machine to run your existing Python pipeline on, that works too.

---

## FAQ

**Q: Is this real?**
A: Yes. Browse [lab.primals.eco](https://lab.primals.eco) — that's a static page auto-published from the hub by a pipeline called pappusCast. It shows pre-rendered notebooks: pipeline validations, paper reproductions, benchmarks, and a data registry. The content is still rough in places — this is work-in-progress being published as it develops, not a polished product. It will continue to evolve as the syntheticChemistry springs produce more validated work. Or just ask Joelle about the Zoom call.

**Q: What's the catch?**
A: The work is open (see terms above). If that works for your project, there's no catch. I need external validation for my infrastructure; you need compute. Fair trade.

**Q: How fast can I get access?**
A: About a week. I need to set up your account, configure the right node for your workload, and install any tools or environments you need. Not instant, but not a semester either.

**Q: Can I use this for coursework / class projects?**
A: Yes, if the work is open (no proprietary datasets from a company). CMSE projects on public data are a great fit. But think bigger, deeper, and wider than Kaggle — summer is the time for real projects.

**Q: What if I break something?**
A: You won't break the cluster. JupyterHub accounts are sandboxed. Worst case, your notebook kernel crashes and you restart it. And I get to find edge cases that stress-test my system — that's useful too.

**Q: What if I need something weird?**
A: Ask. I enjoy weird. "Can you compile this 2003 Fortran code and hook it up to my Python notebook?" is a fun Tuesday for me.

---

**Next step**: email mokkevin@msu.edu with what you're working on. Even "I might have something but I'm not sure" is fine. We'll figure it out.

— Kevin
