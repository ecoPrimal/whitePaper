# coralForge Evolution Roadmap

## Where We Are

```
Phase A: Primitives     ████████████████████  DONE (154 checks)
Phase B: GPU shaders    ████████████████████  DONE (15 df64 WGSL, 37/37)
Phase C: BarraCUDA CPU  ████░░░░░░░░░░░░░░░░  Next — wire to barracuda::ops
Phase D: Full pipeline  ░░░░░░░░░░░░░░░░░░░░  Planned — MSA → structure → confidence
Phase E: LTEE analysis  ░░░░░░░░░░░░░░░░░░░░  Target — frozen fossil structural evolution
```

---

## Phase C: BarraCUDA CPU Integration

Wire coralForge primitives to BarraCUDA's existing operations. Most primitives already have upstream equivalents:

| coralForge Function | BarraCUDA Target | Complexity |
|--------------------|-----------------|:----------:|
| `gelu()` | `Tensor::gelu()` | Trivial |
| `layer_norm()` | `Tensor::layer_norm_wgsl()` | Trivial |
| `softmax_rows()` | `Tensor::softmax_dim(1)` | Trivial |
| `sdpa_full()` | `ops::mha::MultiHeadAttention` | Low (reshape) |
| `triangle_mul_*()` | Compose: `Tensor::matmul()` + `sigmoid()` | Medium |
| `triangle_attention_scores()` | MHA + custom mask | Medium (mask API) |
| `ipa_scores()` | MHA + `PairwiseL2Gpu` | Medium |
| `pairformer_block()` | Composition of above | High (orchestration) |
| `diffusion_reverse_*()` | `StatefulPipeline` sequential | Medium |
| `confidence_*()` | `UnidirectionalPipeline` parallel | Low |

**Estimated effort**: 3–5 sessions. The primitives are validated; this phase is wiring, not discovery.

---

## Phase D: End-to-End Pipeline

### MSA Database Integration

See `neuralSpring/coral_forge/MSA_DATABASE_PLAN.md` for the full database inventory:

| Database | Size (compressed) | Purpose |
|----------|:-----------------:|---------|
| UniRef90 | ~100 GB | Primary MSA, 90% identity clusters |
| BFD | ~1.7 TB | Extended MSA, metagenome-derived |
| UniProt | ~50 GB | Annotation + templates |
| PDB mmCIF | ~60 GB | Experimental structures (templates) |

**Sovereign approach**: Download once to local NVMe. Index with sovereign tools (no BLAST dependency — use MMseqs2 or sovereign k-mer index). MSA construction runs on CPU; structure prediction runs on GPU.

### Pipeline Architecture

```
Input: FASTA sequence
    │
    ├── MSA search (MMseqs2 or sovereign k-mer)
    │       → [N_seq × L] alignment
    │
    ├── Template search (PDB90)
    │       → template coordinates
    │
    ├── Feature embedding
    │       → MSA representation + pair representation
    │
    ├── Evoformer × 48 (coralForge GPU pipeline)
    │       → refined MSA + pair
    │
    ├── Structure module × 8 (coralForge GPU pipeline)
    │   OR Diffusion × T (AlphaFold3 mode)
    │       → 3D coordinates
    │
    └── Confidence heads
            → pLDDT, PAE, pDE, ranking score
```

### Performance Targets

| Stage | Current (Python/CUDA) | Target (coralForge/BarraCUDA) |
|-------|-----------------------|-------------------------------|
| MSA search | minutes (JackHMMER) | seconds (sovereign k-mer) |
| Evoformer × 48 | ~30s (A100) | ~2min (RTX 4070, df64) |
| Structure module | ~5s (A100) | ~30s (RTX 4070) |
| Total per sequence | ~5min (cloud) | ~3min (consumer GPU) |

The performance target is not parity with A100 — it is *acceptable latency on hardware the scientist already owns*.

---

## Phase E: LTEE Structural Evolution Analysis

### The Science Question

How do protein structures evolve under sustained environmental constraint?

The LTEE provides a unique dataset: 12 replicate populations of *E. coli* evolving under glucose-minimal constraint for 75,000+ generations, with frozen samples every 500 generations.

### What coralForge Enables

Given whole-genome sequences from LTEE timepoints (Chapter 14, baseCamp Paper 02):

1. **Predict structure at every timepoint**: For each protein-coding gene at each sequenced generation, predict the 3D structure using coralForge
2. **Track structural evolution**: Compute pairwise structural distances (RMSD, TM-score) between timepoints to measure structural drift
3. **Detect convergent structural solutions**: Across the 12 populations, identify cases where different amino acid sequences converge to the same structural fold — phenotype-convergent evolution at the structural level
4. **Correlate with fitness**: Overlay structural evolution trajectories with the power-law fitness dynamics (Wiser et al., 2013) to test whether structural innovation events coincide with fitness jumps
5. **Predict the Ara-3 precursor**: The citrate innovation in population Ara-3 (Blount et al., 2008) required potentiating mutations. coralForge can predict whether these mutations altered protein structure before the phenotypic innovation appeared

### The Sovereign Advantage

This analysis would be infeasible with cloud AlphaFold:
- **Scale**: ~4,600 genes × 150 timepoints × 12 populations = ~8.3M structure predictions
- **Rate limits**: Cloud APIs cannot sustain this throughput
- **Cost**: At $0.01/prediction, this would cost $83,000
- **Data ownership**: LTEE genome sequences are valuable; they should not leave MSU's network

On a single RTX 4070 running coralForge at ~3 min/sequence:
- **Time**: ~17,000 GPU-hours ≈ 2 years on one GPU, 6 months on four
- **Cost**: ~$1,000 in electricity
- **Data**: Never leaves the lab

For a targeted analysis (essential genes only, key timepoints):
- ~500 genes × 30 timepoints × 12 populations = 180,000 predictions
- ~9,000 GPU-hours ≈ 3 months on four consumer GPUs
- $60 in electricity

---

## Phase F: Beyond LTEE

### Extremophile Structural Adaptation

Rika Anderson's *Sulfolobus* population genomics in Yellowstone hot springs (the same environment where Taq polymerase was discovered) provides a natural experiment in structural adaptation to extreme heat constraint. coralForge can predict how thermophilic proteins maintain structural stability at 80°C+ — connecting directly to the constrained evolution thesis.

### Soil Microbiome Structural Diversity

baseCamp Paper 06 (no-till Anderson) documents how tillage destroys the 3D pore network that enables quorum sensing. coralForge extends this: do soil bacteria under sustained no-till constraint evolve structurally distinct signaling proteins compared to tilled controls? The 60-year Wooster dataset provides the time series.

### Coral Reef Metagenomics

The name is aspirational. Coral reef ecosystems face environmental constraint (warming, acidification). Structural prediction of metagenomic sequences from reef microbiomes — comparing healthy vs. degraded reefs — tests whether structural evolution signatures correlate with ecosystem health.

### Drug Repurposing

wetSpring baseCamp Paper 05 documents cross-species signaling. coralForge enables structure-based drug repurposing: predict the structure of a target protein, then dock existing approved drugs against the binding pocket. No cloud, no proprietary docking software — sovereign from sequence to candidate.

---

*Evolution: from validated primitives to structural biology at scale.*
