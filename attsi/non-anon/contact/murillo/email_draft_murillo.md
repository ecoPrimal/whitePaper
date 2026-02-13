# Email Draft to Professor Murillo

---

**Subject:** Following up on neuromorphic computing - now with hardware!

---

Hi Professor Murillo,

I hope this email finds you well! I graduated from the MSDS program last year (2025), and I wanted to reach out because I remember our conversation at the end of Applied Machine Learning about reservoir computing, echo state machines, and neuromorphic chips. That discussion really stuck with me.

I'm excited to share that I've since acquired the hardware to actually test these concepts - specifically, I now have 3x BrainChip Akida neuromorphic chips across 2 computers in my home compute mesh. These are PCIe boards with 80 neural processing units each, designed for ultra-low-power spiking neural network inference.

Beyond the neuromorphic hardware, I've built out a pretty substantial ML infrastructure with various processing units:
- RTX 5090, multiple RTX 3090s, and RTX 3070s for GPU compute
- Dual EPYC 7452 server (64 cores total) with 256GB ECC RAM
- Multiple high-RAM workstations (up to 192GB DDR5)
- ~$15k invested total across the mesh

I've been working on an open-source project called ToadStool that orchestrates workloads across heterogeneous compute substrates - basically treating CPUs, GPUs, and neuromorphic chips as a unified resource pool. I've done extensive benchmarking and comparison work between different processing units, particularly focused on:

1. **Bioinformatics applications**: Using Akida chips for k-mer filtering in metagenomic pipelines (Kraken2) - achieved 2.3x throughput and 53x power efficiency vs CPU baseline
2. **LLM intent classification**: Sub-millisecond routing decisions at 100x better power efficiency than GPUs
3. **Performance comparisons**: Comprehensive benchmarking across CPU, GPU, and neuromorphic platforms showing 50-400x power efficiency gains for specific workload classes

I've attached a data sheet summarizing the benchmark results with detailed comparisons across all three architectures.

I'd love to discuss this work with you if you have any interest. I'm particularly curious about:
- How reservoir computing principles might apply to optimizing workload scheduling across these different substrates
- Whether there are research opportunities or student projects that could benefit from access to this hardware
- Your thoughts on the practical applications of neuromorphic computing beyond the typical computer vision use cases

I'm still in the Lansing area, so would you be open to meeting for coffee or a have time between classes on campus?

Thanks for the inspiration from that class discussion - it's been a fun journey from theory to hardware!

Best regards,
Kevin Mok
mokkevin@msu.edu
(586) 453-7233

---

## Notes for Revision:
- Education: Microbiology BS (MSU 2018), MSDS (MSU 2025)
- Previous experience: MSUBI Biotechnician (2019-2024), Sandia Fellow (Summer 2024)
- Military background: US Army Infantry, 2012-2015 (COIST/RTO)
- **Attachment:** neuromorphic_benchmark_datasheet.md
