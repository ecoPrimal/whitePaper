# Email Draft to Professor Murillo (Concise Version)

---

**Subject:** Neuromorphic computing follow-up - hardware acquired!

---

Hi Professor Murillo,

I hope you're doing well! I graduated from the MSDS program last year, and wanted to reach out because our conversation about reservoir computing, echo state machines, and neuromorphic chips at the end of Applied Machine Learning really stuck with me.

Great news: I now have the hardware to test these ideas! I've acquired 3x BrainChip Akida neuromorphic chips (PCIe boards with 80 NPUs each) along with substantial GPU/CPU infrastructure (~$15k across multiple nodes). 

I've been building an open-source project that orchestrates workloads across CPUs, GPUs, and neuromorphic hardware, with comprehensive benchmarking showing some interesting results:
- K-mer filtering for Kraken2 pipelines: 2.3x throughput, 53x power efficiency vs CPU
- LLM intent classification: <1ms latency, 100x better power efficiency than GPU
- Image classification: 53x better energy efficiency than GPU for MNIST
- Event-based vision: 384x power efficiency gains with native spike processing

I've attached a detailed data sheet with all the benchmark comparisons.

Would you be interested in discussing this? I'm still in the Lansing area, and I'd love to get your thoughts on:
- Applying reservoir computing principles to heterogeneous workload scheduling
- Potential research collaborations or student projects using this hardware
- Practical neuromorphic applications beyond computer vision

Happy to meet for coffee or meet up on campus call if you have time.

Thanks for the inspiration!

Best,
Kevin Mok
mokkevin@msu.edu | (586) 453-7233
