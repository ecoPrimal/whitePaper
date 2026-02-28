# coralForge Data Provenance

All coralForge validation uses computationally generated baselines from published algorithm specifications. No external datasets, no API dependencies, no proprietary model weights.

---

## Python Baselines

Every baseline is deterministically seeded, version-pinned, and stored as committed JSON.

| Baseline | Script | Output | Seed | NumPy | Checks |
|----------|--------|--------|:----:|:-----:|:------:|
| Evoformer primitives | `control/coral_forge/evoformer_primitives.py` | `evoformer_baselines.json` | 42 | 2.2.6 | 12 |
| Evoformer block | `control/coral_forge/alphafold2_evoformer_block.py` | `evoformer_block_baselines.json` | 42 | 2.2.6 | 19 |
| Diffusion | `control/coral_forge/alphafold3_diffusion.py` | `diffusion_baselines.json` | 42 | 2.2.6 | 29 |
| Pairformer | `control/coral_forge/alphafold3_pairformer.py` | `pairformer_baselines.json` | 42 | 2.2.6 | 14 |
| Confidence | `control/coral_forge/alphafold3_confidence.py` | `confidence_baselines.json` | 42 | 2.2.6 | 19 |

### Reproduction

```bash
cd neuralSpring
pip install numpy==2.2.6

python3 control/coral_forge/evoformer_primitives.py
python3 control/coral_forge/alphafold2_evoformer_block.py
python3 control/coral_forge/alphafold3_diffusion.py
python3 control/coral_forge/alphafold3_pairformer.py
python3 control/coral_forge/alphafold3_confidence.py

# Verify no drift from committed baselines:
bash control/check_drift.sh
```

### Environment

```
Python 3.10.12
NumPy 2.2.6
OS: Pop!_OS 22.04 (Ubuntu 22.04 LTS base)
CPU: Intel i9-12900K
```

No PyTorch, no JAX, no CUDA — pure NumPy for all baselines. This ensures the baselines test the *algorithms*, not framework-specific behavior.

---

## Provenance Constants

Each baseline has a `BaselineProvenance` record in `src/provenance.rs`:

```rust
pub const CORAL_FORGE_PROVENANCE: BaselineProvenance = BaselineProvenance {
    label: "nF-01 Phase B: Evoformer primitive baselines",
    script: "control/coral_forge/evoformer_primitives.py",
    commit: BASELINE_COMMIT,
    date: "2026-02-16",
    command: "python3 control/coral_forge/evoformer_primitives.py",
    environment: "Python 3.10.12, NumPy 2.2.6, seed=42",
    value: 1.0,
    unit: "baselines generated → evoformer_baselines.json",
};
```

This means for any check that fails, you can trace back to the exact script, commit, date, command, environment, and seed that produced the expected value.

---

## Algorithm References

coralForge implements published, peer-reviewed algorithms. No proprietary model weights are used.

| Algorithm | Paper | Year | DOI |
|-----------|-------|:----:|-----|
| AlphaFold2 Evoformer | Jumper et al., Nature 596:583-589 | 2021 | 10.1038/s41586-021-03819-2 |
| AlphaFold2 Structure Module (IPA) | Jumper et al., Supplementary Algorithm 22-23 | 2021 | (same) |
| AlphaFold3 Diffusion | Abramson et al., Nature 630:493-500 | 2024 | 10.1038/s41586-024-07487-w |
| AlphaFold3 Pairformer | Abramson et al., Supplementary | 2024 | (same) |
| AlphaFold3 Confidence (pLDDT, PAE, pDE) | Abramson et al., Methods | 2024 | (same) |
| OpenFold reference | Ahdritz et al., Nature Methods | 2024 | 10.1038/s41592-024-02272-z |
| GELU activation | Hendrycks & Gimpel | 2016 | arXiv:1606.08415 |
| Layer Normalization | Ba, Kiros & Hinton | 2016 | arXiv:1607.06450 |
| Scaled Dot-Product Attention | Vaswani et al. | 2017 | arXiv:1706.03762 |
| DDPM | Ho, Jain & Abbeel | 2020 | arXiv:2006.11239 |
| DDIM | Song, Meng & Ermon | 2020 | arXiv:2010.02502 |
| Cosine beta schedule | Nichol & Dhariwal | 2021 | arXiv:2102.09672 |

### What We Do NOT Use

- **Pre-trained model weights**: coralForge validates the *algorithms*, not a specific trained model. Random weights are used for Rust validation; real weights come later.
- **AlphaFold Server API**: We do not call any external API. The baselines are local NumPy.
- **Proprietary datasets**: No PDB structures, no UniRef MSAs, no BFD sequences are used during validation. Those are needed for *inference*, which is Phase D (see `05_EVOLUTION.md`).
- **OpenMM/RoseTTAFold/ESMFold**: No other structure prediction framework is used. coralForge is built from the published algorithm specifications.

---

## Drift Detection

The CI pipeline reruns all Python baselines and compares output against committed JSON:

```bash
bash control/check_drift.sh
```

If any baseline value changes (NumPy update, Python version change, seed behavior), the drift check fails. This has caught 2 real drifts in other neuralSpring baselines across Sessions 40–94.

---

## Future Data (Phase D+)

When coralForge moves to end-to-end inference, it will require sequence databases:

| Database | Size | Source | License |
|----------|------|--------|---------|
| UniRef90 | ~100 GB | UniProt Consortium | CC BY 4.0 |
| BFD | ~1.7 TB | Steinegger & Söding | CC BY 4.0 |
| PDB mmCIF | ~60 GB | RCSB PDB | CC0 1.0 |
| ColabFold databases | ~500 GB | Mirdita et al. | MIT |

All databases are public, open-license, and will be downloaded to local storage. No cloud dependency at runtime. See `neuralSpring/coral_forge/MSA_DATABASE_PLAN.md` for the acquisition plan.

---

*Provenance: every number traces to a script, a commit, a seed.*
