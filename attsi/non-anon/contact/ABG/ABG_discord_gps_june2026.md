# ABG Discord Post — GPS Platform / Drug Discovery + Cross-Species

**Channel**: #general or #compute (wherever drug discovery / transcriptomics fits)
**Date**: June 2026
**Context**: Post-meeting with Gonzales lab (MSU Pharmacology & Toxicology). Assigned to rebuild the GPS platform as a pseudoSpore.

---

## Draft Post (under 2000 chars)

New target dropped. Got assigned a real one from an MSU drug discovery lab.

**GPS** (Gene expression Profile-based Screening) — a deep learning platform that predicts drug-induced gene expression changes from chemical structures alone, then screens compound libraries for molecules that *reverse* disease transcriptomic signatures. Three components:

1. **RCL** — collaborative learning to clean noisy drug-induced expression profiles
2. **GPS4Drug** — predict expression changes from SMILES, run virtual screens
3. **MolSearch** — multi-objective lead optimization via Monte Carlo Tree Search

Paper validated in hepatocellular carcinoma (novel compound, IC50 improved 4 µM → 0.5 µM) and idiopathic pulmonary fibrosis (repurposing + novel anti-fibrotic from single-cell signatures).

**The problem**: 10+ years of accumulated code. Python 2. Fortran. Pinned dependencies. Web portal barely alive. 713 MB on Zenodo. Exactly the kind of legacy scientific infrastructure that dies when the grad student who wrote it leaves.

**The plan**: Full lineage trace, reproduce every figure, then rebuild sovereign. The output is a pseudoSpore — self-verifying, portable, no dead environments. Same pattern as the compChem GuideStone but for transcriptomic drug screening.

**Why this connects to ABG**: The platform uses LINCS/L1000 drug perturbation signatures. Same data layer Mark's cancer project touches. The cross-species angle (dog skin ≠ human skin ≠ cat skin — tissue geometry determines signal propagation, not species extrapolation) is directly relevant to anyone doing comparative transcriptomics. If you're working on expression data in any disease context, this tool generates candidates.

Zenodo: https://zenodo.org/records/17653393
GitHub: https://github.com/Bin-Chen-Lab/GPS
Web portal: http://apps.octad.org/GPS/

Will share progress as modules reproduce. First target: get RCL running and validate against their published VCAP profiles.

---

## Internal Notes (not for Discord)

### Why this matters for the ecosystem

| Connection | Detail |
|-----------|--------|
| **healthSpring** | GPS4Drug's expression prediction maps to healthSpring's drug repurposing scoring. Anderson-augmented MATRIX + GPS reversal scoring = complementary approaches |
| **wetSpring** | RCL operates on gene expression matrices — same data type as wetSpring's differential expression pipeline |
| **neuralSpring** | The deep learning models (collaborative learning, MCTS) are neuralSpring validation targets |
| **hotSpring** | MolSearch's compound optimization connects to conformational dynamics — predicted binders need FEL validation |
| **One Health / Anderson** | Cross-species tissue geometry determines WHY the same drug works differently. GPS gives you WHAT reverses the disease signature. Anderson tells you WHERE it will propagate. Together: species-specific drug predictions from causal mechanisms, not empirical curve fitting. |

### The Anderson + GPS synthesis

```
GPS says: "This compound reverses the NF disease signature"
Anderson says: "In this tissue geometry, the drug signal propagates to targets"
Together: "This compound reverses NF in human nerve sheath geometry
           but NOT in dog skin geometry because d_eff differs"
```

This is the One Health computational framework Andrea described wanting — not "dogs model humans" but "dogs model dogs, humans model humans, and the computation exposes WHY they differ."

### Rebuild plan (pseudoSpore target)

| Phase | What | Validation |
|-------|------|-----------|
| 1 | Reproduce RCL on VCAP_t1 (Python 2 → modern) | Match published cleaned profiles |
| 2 | Reproduce GPS4Drug predictions | Match Zenodo figure data |
| 3 | Reproduce MolSearch optimization | Match HCC IC50 improvement claim |
| 4 | Package as pseudoSpore | 71+ automated checks, all figures reproducible |
| 5 | Extend to NF signatures | Screen against NF Data Portal transcriptomic data |
| 6 | Cross-species Anderson extension | Predict species-specific responses |

### Data dependencies (all public)

| Dataset | Role | Where |
|---------|------|-------|
| LINCS L1000 | Drug perturbation signatures (1.3M profiles) | clue.io |
| GEO (various) | Disease expression signatures | NCBI GEO |
| NF Data Portal | NF-specific transcriptomic signatures | nf.synapse.org |
| ChEMBL | Compound structures + activity | EBI |
| PubChem | Compound structures + BioAssay | NCBI |
| TCGA | Pan-cancer expression (NF1 subset) | GDC |

### Key insight from the meeting

Andrea's framing: "We normally use animal models for human models, but this leaves massive gaps and bad assumptions. Rather, examine the dog model in dogs and the cat model in cats — trace underlying causal mechanisms."

Kevin's response: "Applying animal models to humans is a tactic of the bench to overcome the lack of humans to experiment on, not because dogs are a better model."

This is the Anderson framework stated in pharmacology language. The computation doesn't need animal models for human disease — it needs the causal geometry. GPS provides the drug-transcriptome link. Anderson provides the tissue-propagation link. Together they bypass the species-extrapolation problem entirely.
