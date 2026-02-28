# coralForge for LTEE Wet Lab Genetic Analysis

## Overview

The Lenski Long-Term Evolution Experiment (LTEE) is the longest-running controlled evolution experiment in history: 75,000+ generations of *Escherichia coli* under glucose-minimal constraint, maintained at Michigan State University since 1988. The frozen fossil record preserves samples from every 500 generations across 12 replicate populations.

This document describes how coralForge enables sovereign structural analysis of LTEE genomic data — connecting the computational constrained evolution thesis (Chapters 3–13) to biological evidence (Chapter 14) through protein structure prediction.

---

## The Pipeline

### From Frozen Stock to Structural Trajectory

```
┌──────────────────────────────────────────────────────────┐
│                    WET LAB (MSU)                          │
│                                                          │
│  Frozen stock (generation N) → Revival → Culture → DNA   │
│                                                          │
└──────────────────────┬───────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────┐
│                 SEQUENCING (Sovereign)                     │
│                                                          │
│  DNA → Library prep → MinION/Illumina → FASTQ            │
│                                                          │
│  wetSpring 16S pipeline: quality → chimera → taxonomy     │
│  wetSpring WGS pipeline: assembly → annotation → genes    │
│                                                          │
└──────────────────────┬───────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────┐
│              STRUCTURAL PREDICTION (coralForge)           │
│                                                          │
│  Gene → protein sequence → MSA → Evoformer → IPA/Diff    │
│      → 3D coordinates + pLDDT + PAE + pDE                │
│                                                          │
│  Per gene, per generation, per population                 │
│                                                          │
└──────────────────────┬───────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────┐
│              STRUCTURAL EVOLUTION ANALYSIS                 │
│                                                          │
│  Compare structures across generations:                   │
│    • RMSD trajectory: how much does each protein move?   │
│    • TM-score: do folds change or just wiggle?           │
│    • Contact map evolution: which interactions break/form?│
│    • pLDDT trajectory: does confidence change over time? │
│                                                          │
│  Compare across populations:                              │
│    • Convergent structures from divergent sequences       │
│    • Population-specific structural innovations           │
│    • Correlation with fitness trajectories                │
│                                                          │
└──────────────────────┬───────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────┐
│          CONSTRAINED EVOLUTION VALIDATION                  │
│                                                          │
│  Thesis predictions (Ch. 14):                             │
│    □ Phenotype-convergent > sequence-identical across pop │
│    □ ~30-50% hitchhiker fraction in fixed mutations      │
│    □ Power-law structural divergence over generations     │
│    □ Structural precursors before phenotypic innovation   │
│    □ Genome streamlining = fold simplification in late gen│
│                                                          │
│  Anderson-QS layer (baseCamp 01):                         │
│    □ Biofilm LTEE populations show different QS disorder  │
│    □ W parameter correlates with structural diversity     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## Key Analyses

### 1. Structural Convergence Across Populations

**Question**: When multiple LTEE populations independently improve the same function (e.g., glucose transport), do they converge to the same protein structure?

**Method**:
- Identify homologous mutations in the same gene across populations
- Predict structures for each variant using coralForge
- Compute pairwise TM-scores between population-specific variants
- Classify as: structurally identical (TM > 0.9), similar fold (TM > 0.5), or divergent (TM < 0.5)

**Thesis prediction**: Phenotype-convergent (same function, different structure) should outnumber sequence-identical (same mutation). This parallels the IPC convergence in Chapter 13 — all primals converge on JSON-RPC through different implementations.

### 2. Structural Trajectory Analysis

**Question**: Does protein structural evolution follow the same power-law dynamics as fitness?

**Method**:
- For each essential gene, predict structures at every 500-generation interval
- Compute cumulative RMSD from ancestor structure
- Fit power-law model: RMSD(t) ~ t^β
- Compare β exponents to the fitness power-law exponents from Wiser et al. (2013)

**Thesis prediction**: If constrained evolution operates on structure as it does on fitness, the power-law exponents should be correlated. Structural innovation should decelerate in the same pattern as fitness gain.

### 3. The Ara-3 Citrate Precursor

**Question**: Did the potentiating mutations for the Ara-3 citrate innovation (Blount et al., 2008, 2012) produce detectable structural changes before the phenotypic innovation appeared?

**Method**:
- Identify the known potentiating mutations from published LTEE data
- Predict structures at timepoints before, during, and after potentiation
- Compare to non-citrate-evolving populations at the same timepoints
- Look for: binding pocket changes, domain rearrangements, flexibility shifts

**Significance**: If structural precursors are detectable, coralForge becomes a tool for predicting evolutionary innovations from genomic data — before the phenotype manifests.

### 4. Hitchhiker Structural Impact

**Question**: Do hitchhiker mutations (neutral, dragged to fixation by linkage) produce structural changes?

**Method**:
- Classify fixed mutations as beneficial or hitchhiker (per Ch. 14.3.2)
- Predict structures for both classes
- Compare RMSD between beneficial and hitchhiker mutations

**Thesis prediction**: Hitchhiker mutations should produce smaller structural changes than beneficial mutations. If some hitchhikers produce large structural changes despite being selectively neutral, this suggests structural buffering — the protein fold absorbs sequence changes without functional consequence.

### 5. Genome Streamlining and Fold Simplification

**Question**: As LTEE populations lose non-essential genes in late generations, do remaining proteins simplify structurally?

**Method**:
- Track pseudogene accumulation per 500-generation interval
- For remaining functional genes, predict structures over time
- Measure structural complexity: number of domains, contact order, secondary structure content
- Correlate structural simplification with genome streamlining

---

## Hardware Requirements

### Minimal Setup (Targeted Analysis)

| Component | Specification | Cost |
|-----------|-------------|------|
| GPU | RTX 4070 12 GB | $600 |
| CPU | i5-13600K or equivalent | $300 |
| RAM | 32 GB DDR5 | $100 |
| Storage | 2 TB NVMe (sequences + databases) | $150 |
| **Total** | | **$1,150** |

Sufficient for: 500 essential genes × 30 timepoints × 12 populations = 180,000 predictions over ~3 months.

### Production Setup (Full Analysis)

| Component | Specification | Cost |
|-----------|-------------|------|
| GPU | 4× RTX 4070 12 GB | $2,400 |
| CPU | i9-14900K | $600 |
| RAM | 128 GB DDR5 | $400 |
| Storage | 8 TB NVMe (full MSA databases) | $600 |
| **Total** | | **$4,000** |

Sufficient for: 4,600 genes × 150 timepoints × 12 populations = 8.3M predictions over ~6 months.

Compare to cloud AlphaFold: $83,000 at $0.01/prediction, data leaves the lab, rate limits, availability risk.

---

## Integration with Other Springs

| Spring | Contribution |
|--------|-------------|
| **wetSpring** | 16S/WGS pipeline: FASTQ → quality → assembly → genes. Sovereign Rust, no Python at runtime |
| **neuralSpring** | coralForge structure prediction + Anderson spectral analysis of structural evolution |
| **hotSpring** | BarraCUDA GPU infrastructure, df64 core streaming, ToadStool Sovereign Compiler |
| **airSpring** | If agricultural LTEE equivalents exist (long-term soil trials), apply same pipeline |
| **groundSpring** | Uncertainty quantification on structural predictions (pLDDT calibration) |

---

## Timeline

| Phase | Target | Dependencies |
|-------|--------|-------------|
| **Now** | Primitives validated (154 checks) | Done |
| **Q2 2026** | BarraCUDA CPU wiring (Phase C) | ToadStool absorption |
| **Q2 2026** | MSA database download + indexing | Storage hardware |
| **Q3 2026** | End-to-end pipeline on synthetic data | Phase C + databases |
| **Q3 2026** | LTEE sample acquisition (collaboration with Lenski lab) | MSU collaboration |
| **Q4 2026** | First 100 structural predictions on real LTEE data | Pipeline + samples |
| **2027** | Full targeted analysis (180K predictions) | 4-GPU setup |
| **2027–2028** | Complete analysis (8.3M predictions) + manuscript | Production hardware |

---

*From frozen *E. coli* to structural evolution trajectories — sovereign, reproducible, open.*
