# Email: GPS Platform Progress & NF Preparation — June 2026

**To**: Andrea Gonzales
**From**: mokkevin@msu.edu
**Subject**: GPS platform — progress update + thoughts ahead of Bin Chen introduction
**Attachment**: GPS_Revalidation_Plan.md

---

Hi Andrea,

Thank you for connecting me with the GPS work and for offering the introduction to Bin Chen. Our conversation about the interconnected models problem and One Health really stuck with me — the issues between human and animal models, why dog skin is used as a proxy for human pruritus, and the fundamental question of whether animal models tell us about the animal or about the human. I've been thinking about that since we spoke.

I went through the GPS preprint and wanted to share where my thinking is.

**What I've been doing:**

I traced the full lineage — from Lamb's Connectivity Map (2006, 164 compounds, 3 cell lines) through the NIH LINCS program ($150M, 3 million profiles), the RGES metric (Chen 2017, 66,000 compound profiles, 4 HCC compounds validated in vivo), OCTAD (Zeng 2021, 19,127 patients across 50+ cancer types), and the current GPS pipeline published in Cell. That's 20 years of work, 164 compounds to 750 million. Every paper in the chain is documented as a revalidation target — the goal is paper parity on each claim, then rebuild the entirety of it so it's transmissible and reproducible as a self-verifying artifact. It's 10+ years of accumulated code — Python 2, Fortran, pinned dependencies — exactly the kind of problem I like to resolve.

**The scale of the problem has changed:**

When Lamb published in 2006, the Connectivity Map was 164 compounds and fit on a laptop. The GPS platform screens 750 million. The data grew three orders of magnitude; the infrastructure most labs have access to didn't. Full reproduction requires about 35 GB. Full validation is 49 GB. Ground-truth archaeology — going back to raw L1000 fluorescence to verify every processing step — is 317 GB. I have more than enough room. I own a sovereign mesh — 11 gates, ~1 TB system RAM, ~248 GB GPU VRAM across NVIDIA and AMD (including 56 GB HBM2), 122 TB storage, 10G backbone, 3 neuromorphic chips, no queue times, no cloud, no shared anything. The full breakdown is in the attached plan. GPS4Drug training, MCTS tree search, and screening across 750M compounds all fit comfortably on a single gate. Once I have the pipeline revalidated, that compute is available for running additional experiments — new disease signatures, larger screening libraries, parameter sweeps that would queue for days on shared university infrastructure.

I've attached a plan document with the full technical details, data inventory, hardware specs, and the infrastructure I've already built. Feel free to share it with Bin Chen or anyone else you think would benefit from seeing it.

**A few thoughts from the preprint:**

The iterative cycle — data science to characterize the problem, wetlab to test predictions, computation to refine, wetlab again — is exactly the kind of work I want to support, both as a scientist and with my infrastructure. That loop is where discovery happens.

One thing that struck me: the paper calls the system "GPS" and talks about an "Atlas" of metabolic signatures. Good metaphors, but they undersell the problem. An atlas is a static projection of something dynamic — CMAP flattened 3 million profiles into similarity scores, OCTAD compressed 19,127 transcriptomes into summaries. Each step loses information the biology carries. And GPS is a route finder between known points — it predicts along paths the training data defines, but doesn't map the terrain between them.

What the biology demands is full topographic maps of a dark system — metabolic landscapes we can't directly observe — with a pathfinder that uses GPS-like feedback to explore and update as it learns. I spent years in the Army building terrain models from topographic maps — translating contour lines and elevation data into three-dimensional pictures of ground you couldn't see yet, so that when you got there, you already understood the landscape. The expression data is the contour lines. The diseases are the terrain. The compounds are the routes. The current platform gets the direction right. The question is how far we can push it toward mapping the actual terrain.

That's part of what makes the revalidation valuable. By rebuilding from the methods rather than running their code, I can see where the compression happens — where the pipeline flattens information the biology needs. That's where the evolution starts. And once the revalidated platform is packaged as a pseudoSpore — a self-verifying portable artifact — it becomes something anyone can hand to a reviewer, a student, or a collaborator and say "run this, see what passes."

**NF while we wait:**

While the Bin Chen introduction develops, I'll be applying the GPS reversal screening to NF transcriptomic signatures from the Data Portal. Same methods, different disease, and directly relevant to your group's work. It also produces computational preliminary data for the CTF NDU.

I'm also sharing this work with the citizen science community I mentioned — it's excellent teaching material for new scientists learning to read a preprint lineage, trace data dependencies, and evaluate computational claims. The GPS paper chain is a 20-year case study in how a hypothesis (Lamb 2006) becomes a platform (Xing 2026).

**For the Bin Chen introduction:**

What I'd most want to understand from him is which results he trusts most, which modules he's seen break, and what validation would convince him the rebuild is correct. Also want to clarify the source situation — the GitHub repo lists Apache 2.0 and the Zenodo artifact says GPL-3.0, so I'd like to know which is authoritative before building on it. And whether there are unpublished preprocessing steps or weights not in the public artifact.

Happy to walk through any of this in person whenever it's useful.

Best,
Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu
