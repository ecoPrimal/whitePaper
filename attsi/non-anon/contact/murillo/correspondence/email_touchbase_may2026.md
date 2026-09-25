# Email: Touch-Base — May 2026

**To**: murillo@msu.edu
**From**: mokkevin@msu.edu
**Subject**: Summer update — where things went since March

---

Hi Professor Murillo,

Hope the semester wrapped up well. Wanted to touch base — a lot has happened since our last coffee.

**Chuna** — thank you again for that introduction. We met in April and went through the gradient flow and dielectric work. Got some really good insights from him. I've since built a Chuna Engine (8 Rust binaries, MILC-compatible output) and I'm repackaging it into a self-contained deployable artifact — a USB or tarball that runs on any Linux machine, no toolchain needed. On his suggestion, I'm also building a MILC data generator that Bazavov's group might be able to use. If there's an appropriate time to put that in front of him, I'd welcome the help.

**The trail since March** — the work has branched out quite a bit. I'm now doing validated paper reproductions across microbial evolution (Lenski LTEE), protein engineering (Woldring Lab), drug discovery (Gonzales Lab in Pharmacology), and phylogenetics (Kevin Liu's work), alongside the plasma physics with your group. The common thread is the same Rust + GPU pipeline, same validation methodology, different science. The project site is at [primals.eco](https://primals.eco) and the live notebooks are at [lab.primals.eco](https://lab.primals.eco) (still rough — work-in-progress published through an automated pipeline).

Also — you asked me something at coffee that I didn't fully understand at the time: "is it a library or a binary?" I get it now. The answer is both, and the distinction matters. The library (`cargo test`) builds and validates the math — that's where the 12,000+ checks live. The binary (`cargo build --release`) makes it deployable — a static executable that carries the validated math to any machine. The deployable artifact work I'm doing now (for Chuna, and a separate one called [lithoSpore](https://github.com/sporeGarden/lithoSpore) targeting the Lenski LTEE) is the binary side of that answer. Library proves it's correct. Binary makes it portable.

**Compute for students** — the cluster has grown to 11 nodes (~154 cores, ~248 GB GPU VRAM, 1 TB RAM, 122 TB storage) and I'm now hosting remote JupyterHub access. If you have CMSE students or grads bottlenecked on HPCC or hitting memory walls, I'd be happy to set them up — about a week turnaround. Already doing this with folks from the protein engineering side (Woldring Lab) and with ABG (an online bioinformatics research community). Summer works well for longer projects.

**Barrick/Lenski** — I have an in-person interview this week with Jeff Barrick's lab and I'll be meeting Richard Lenski. You might find the connection interesting: remember the Anderson localization proxy we used for CG solver cost in the dynamical QCD runs — less gauge disorder at weak coupling means fewer localized Dirac modes, faster convergence? I've been applying the same Anderson framework to microbial quorum sensing. Species diversity maps to disorder W, spatial geometry maps to lattice dimension, and the level spacing ratio tells you whether diffusible signals propagate (extended) or attenuate (localized). Same eigenvalue statistics, same phase transition, different lattice. The LTEE is the test bed — 12 replicate populations of *E. coli* under identical constraint for 80,000+ generations. The prediction is that biofilm (3D) vs. planktonic (shaken flask) should show different QS regimes, exactly as Anderson's theorem requires. That's what lithoSpore targets: reproducing their published fitness dynamics, mutation trajectories, and allele frequencies, plus the novel Anderson-QS predictions — all deployable on a USB stick. Same pattern as the Chuna Engine, different science.

I'm around Lansing all summer — would love to grab coffee whenever works for you.

Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu
