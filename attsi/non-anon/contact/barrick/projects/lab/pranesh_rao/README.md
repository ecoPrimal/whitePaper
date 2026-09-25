# Pranesh Rao — Barrick Lab

**Role**: Cell & Molecular Biology Graduate Student (Feb 2024–)
**Degrees**: BE Biotechnology (Mumbai University), MS Biotechnology (Texas A&M - College Station)
**Email**: (check lab directory)
**Interview**: Mon May 18, 3:00–3:30 PM, BPS 6199 (with Ira Zibbu)

---

## Research

### LTEE Evolution Dynamics via DNA Barcoding

Pranesh studies the omics of microbial evolution dynamics in LTEE *E. coli* populations. His primary approach is **DNA barcoding + high-throughput sequencing** — inserting unique chromosomal barcodes into populations so individual lineages can be tracked over time. This enables:

- Tracking ~450,000 distinct lineages simultaneously (Blundell et al. 2019, *Nature Ecology & Evolution*)
- Measuring lineage diversity loss rates under different conditions
- Detecting low-frequency variants that will later sweep to fixation
- Watching clonal interference in real time (multiple beneficial mutations competing)

This is the population-level complement to breseq's clone-level mutation calling.

### Supplementing breseq

Pranesh is actively working on **extending the breseq computational pipeline**. breseq (C++/R, GPL-2.0) is Barrick's mutation caller for haploid microbial genomes from Illumina data. It detects SNPs, indels, large deletions, and new junctions (IS insertions).

Current breseq limitations he may be addressing:
- Population-level (polymorphism) mode exists but is less mature than clonal mode
- Structural variant detection is improving (IS predictions, soft-clipping subcommand in v0.38.2)
- Integration with barcoding data for lineage-resolved mutation calling
- Speed: serial C++ — scales linearly with genome count

### Prior Industry Experience

R&D at **Asuragen (Bio-Techne)**, Austin TX — molecular diagnostics and carrier screening assays for genetic disorders. This means he understands validated pipelines, QC, and regulatory-grade analysis. He's not a pure academic — he's worked in industry diagnostics.

---

## What He Needs (Wet Lab)

- **Barcoding construct maintenance**: The barcoded LTEE populations require careful handling to maintain barcode diversity
- **Sequencing coordination**: Regular Illumina runs for breseq + periodic deep sequencing for barcode tracking
- **Library prep**: High-throughput sequencing library construction for both clone and population samples

## What He Needs (Dry Lab)

- **breseq runtime**: As sequencing volume grows, breseq gets slow. GPU-accelerated alignment or parallelized variant calling would directly help
- **Barcode analysis pipeline**: Demultiplexing, lineage tracking, diversity metrics — custom pipeline work
- **Allele frequency time series**: From population sequencing to frequency trajectories (Good et al. 2017 methodology)
- **Statistical framework**: Which lineages are under selection vs. drift? Exactly our groundSpring Exp 014 (drift vs. selection, Wright-Fisher fixation)

## How We Multiply His Work

| His Need | Our Tool | Impact |
|----------|----------|--------|
| Faster breseq | wetSpring Rust mutation caller | Benchmark against breseq, identify 10-100× speedup opportunities |
| Barcode demultiplexing | wetSpring sovereign pipeline | GPU-accelerated barcode assignment |
| Allele frequency tracking | neuralSpring LSTM/HMM | Predict trajectory outcomes, detect clade transitions |
| Selection vs drift classification | groundSpring Exp 014 | Quantitative Wright-Fisher fixation probability for each lineage |
| Regime detection | neuralSpring ESN | Automatic classification: sweep vs. interference vs. coexistence |
| Error quantification | groundSpring Exp 019 jackknife | Subpercent uncertainty on frequency estimates |
| Rare variant detection | groundSpring Exp 016 | Signal vs. noise boundary at given sequencing depth |

**The pitch to Pranesh**: "I've been building a Rust-based genomics pipeline that reproduces breseq's mutation calls with concordance checks. It's faster because it's compiled and can use GPU. I'd like to benchmark it against breseq on your LTEE data — not to replace it, but to see where parallelization helps. I've also got ML tools (LSTM, ESN) for allele frequency prediction and regime detection that might be useful for the barcoding data."

---

## Personal

Soccer (football) enthusiast — plays, watches, and thinks about it. Hiking, biking, painting/sketching. He prefers "football."
