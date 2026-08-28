# Email Draft — Kevin → Joelle Eaves

**To**: jeaves@msu.edu
**From**: mokkevin@msu.edu
**Subject**: Zoom this week?

---

Hi Joelle,

Good connecting on LinkedIn — wanted to follow up so we can get a Zoom on the calendar.

Short version: I've been building a sovereign ('basement HPC') compute cluster over the past few years and I'm looking for external workloads to validate it against institutional systems. It has spare capacity and I'd love to put it to work on real science.

The hardware: 11 nodes, ~154 CPU cores (dual EPYC 7452, Threadripper 3970X, Ryzen 9 9950X3D, i9-14900K, etc.), ~248 GB of GPU VRAM across NVIDIA and AMD cards (RTX 5090, 2× RTX 3090, 2× Titan V HBM2, RTX 5070, and others), about a terabyte of system RAM, 122 TB storage, and a 10G backbone. It runs a multi-user JupyterHub so I can grant remote compute access without anyone having to install anything.

On the software side, I've been writing validated scientific computing pipelines — genomics, structure prediction, ML, pharmacokinetics, GPU-accelerated math — and reproducing published papers to prove parity (175+ so far). The live environment is browsable at [lab.primals.eco](https://lab.primals.eco) (no login needed to see the notebooks and results), and the broader project is at [primals.eco](https://primals.eco).

The pitch: if you or your lab mates have any compute-hungry jobs — doesn't have to be related to your specific research — I'd like to run them. AlphaFold queued on HPCC, big sequencing alignments, ML training, whatever. I'm trying to demonstrate that this setup competes with institutional clusters on real workloads, and I have cycles to spare.

I'm flexible this week — mornings or afternoons. What works for you?

Best,
Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu
