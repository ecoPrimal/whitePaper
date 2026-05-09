# ABG Compute Thread — Discord Posts

Three posts, each under 2000 characters. Copy-paste ready.

---

## Post 1/3 — What's available

Hey all — Tamison here. Laying out what's available on the compute side.

**What's live now**
JupyterHub at lab.primals.eco — per-user accounts rolling out this week.

Dedicated ABG node (**ironGate**):
i9-14900K (24c) · 96 GB DDR5 · RTX 5070 (12 GB) · 3.6 TB NVMe · Pop!_OS
→ DESeq2, Seurat/Scanpy, lightweight alignment, visualization

**Heavier nodes I can bring online:**
**strandGate** — Dual EPYC 7452 (64c/128t) · 256 GB ECC · RTX 3090 24 GB + RX 6950 XT → STAR, Kraken2, large assemblies, RAM-hungry jobs
**biomeGate** — Threadripper 3970X (32c/64t) · 256 GB · Titan V 12 GB HBM2 → MD sims, structure prediction, HBM2-bandwidth GPU work
**southGate** — Ryzen 5800X3D · 128 GB · RTX 4060 (3090 slot available) → medium jobs, dual-boot if you need Windows
**westGate** — 76 TB ZFS cold storage. Your datasets live here.

GPU cards and HDDs float between machines. Need a 3090 next to 64 cores and 10 TB scratch? I can make that happen.

**Environments — use what you know**
Python (conda/pip/Jupyter), R (RStudio/Bioconductor), Fortran/C/C++ (BLAST, HMMER, GROMACS), MATLAB via Octave, Docker/Singularity. Got old Fortran from 2003? Bring it. Tell me what your pipeline needs and I'll set it up.

**Limits**
- One person — not 24/7 IT, reasonable turnaround
- 76 TB cold + ~46 TB NVMe total — 20 TB project = planned, 100 TB = we talk
- Residential bandwidth — big SRA pulls staged overnight
- No HIPAA/PHI — public data (GEO/SRA/NCBI) is the sweet spot
- Shared workspace = visible workspace (more on why in post 3)

Don't be shy on requests — I can refit and reorganize as needed.

---

## Post 2/3 — Project proposals + what I'm getting out of this

**What to include in proposals**
When scoping compute, it helps to include:
- **Data source + size** — "3 GEO datasets, ~20 GB" or "SRA PRJNA_____, ~500 GB raw"
- **Compute shape** — rough sizing:
  - Bulk RNA-seq DEG (DESeq2): 8–16 GB RAM, few cores
  - scRNA-seq (Scanpy/Seurat, 50K+ cells): 32–64 GB RAM
  - STAR alignment (large): 32+ GB RAM, scales with cores
  - MD sim (GROMACS): GPU-bound, HBM2 helps
  - Structure prediction: GPU VRAM bottleneck — 3090 handles most single chains
- **Past resource demands** — if you know the ballpark
- **Software/versions** — tools, containers, dependencies

Large pulls (>50 GB) go through me so I can stage to the right storage.

**What I'm getting out of this**
I'll be straightforward. I've spent the last year+ building computational tools — 16S pipeline (6,600+ validation checks), GPU-accelerated genomics via Vulkan, metagenomics (170 cold seep metagenomes, 299K+ QS genes), protein structure prediction in pure Rust on consumer hardware.

But it's all my own validation. When independent researchers use this infrastructure and produce real results, that's external proof the system works. That's what I need — not authorship, not steering your research. Your work validates my infrastructure. A contribution of compute for proof that it works.

**Me as a researcher**
My background is bench micro (fermentation, PFAS, algal bioinfo at Sandia), MS in data science, then the computational work above. My expertise is in substrate — hardware, systems, pipelines. I'm also here as a researcher at the same level as everyone else, same user tier, same visibility.

---

## Post 3/3 — Terms, openness, and good fences

**What this is**
This is a contribution, not a donation. I'm investing hardware and time into ABG because I get something real back (see post 2). Mutual exchange, not philanthropy.

I reserve the right to withdraw, modify, or limit access at any time — including removing users for abuse or shutting the infrastructure down. My hardware, my network, my choice to share it. That choice is ongoing.

I don't expect any of that to be relevant. Clear terms up front mean nobody guesses later.

**Terms of use**
Work produced on this infrastructure — code, data, results, docs — is licensed under triple copyleft:
- Code/pipelines: **AGPL-3.0** — open, modifications shared back
- Results/data/docs: **CC-BY-SA 4.0** — shareable with attribution
- Methods: **ORC** — system mechanics stay open

If it's on the JupyterHub, it's open. Proprietary work → your own resources. Boundary is the network — clean, no gray area.

**Day-to-day: probably nothing changes** if you're doing open science on public data. Your inputs are already public. Outputs become open with attribution. You publish wherever you want, keep full credit, take everything you learn with you.

What it prevents: nobody — including me — can lock up what the group produces. I can't privatize your results. You can't privatize mine. External companies can't extract without sharing modifications.

**Why visible = safe**
Plagiarism and scooping need obscurity. In a shared workspace, your analysis is timestamped and visible to 80+ members from the moment you start. That's stronger priority protection than a laptop and a prayer.

On public data, your novel contribution is the analysis. Here, that contribution is hashed the moment you run it. Structural proof of priority beats secrecy every time.

Good fences make good neighbors. Questions? Ask here or DM me. — Tamison

---

*Drafted: May 8, 2026 — for ABG #general or compute thread*
