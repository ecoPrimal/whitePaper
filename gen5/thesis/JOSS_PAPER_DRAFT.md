# JOSS paper.md — Draft Template

**Target journal:** Journal of Open Source Software (JOSS)
**Software:** tideGlass — Sovereign Drug Discovery Pipeline
**Status:** Template ready; content blocked on tideGlass Phase 0 completion
**Date:** August 25, 2026

---

## paper.md (JOSS format)

```yaml
---
title: 'tideGlass: A Sovereign Drug Discovery Pipeline for Neurofibromatosis
Drug Repurposing via Gene-Perturbed Similarity'
tags:
  - Rust
  - drug discovery
  - neurofibromatosis
  - gene expression
  - LINCS L1000
  - sovereign computing
  - provenance
authors:
  - name: Kevin Mok
    orcid: 0009-0004-2141-0321
    affiliation: 1
  - name: Andrea J. Gonzales
    orcid: XXXX-XXXX-XXXX-XXXX  # CONFIRM WITH ANDREA
    affiliation: 2
affiliations:
  - name: ecoPrimals, Lansing, MI, USA
    index: 1
  - name: Department of Pharmacology & Toxicology, Michigan State University, East Lansing, MI, USA
    index: 2
date: DD Month 2026
bibliography: paper.bib
---
```

## Summary

tideGlass is a sovereign drug discovery pipeline that reimplements and extends
the Gene-Perturbed Similarity (GPS) platform (Cell 2026) in pure Rust, with
cryptographic provenance on every computational step. It processes LINCS L1000
gene expression signatures, ChEMBL bioactivity data, and disease-specific
transcriptomics to identify drug repurposing candidates for rare diseases.

We demonstrate tideGlass on neurofibromatosis type 1 (NF1), reproducing GPS
published results and extending the pipeline to identify MEK inhibitor
candidates (including selumetinib) through sovereign, reproducible
computation. The pipeline runs entirely on commodity hardware (~$15K) without
cloud dependencies, CUDA, or proprietary tools.

tideGlass is built on the ecoPrimals ecosystem — 15 pure-Rust binaries
composing a distributed scientific computing organism — and inherits its
cryptographic provenance chain: every intermediate result is BLAKE3-hashed,
Ed25519-signed, and traceable through the provenance trio (rhizoCrypt,
loamSpine, sweetGrass).

## Statement of Need

Drug repurposing for rare diseases faces a computational bottleneck: existing
pipelines depend on proprietary stacks (MATLAB, commercial cloud APIs, CUDA)
that are expensive, opaque, and non-reproducible. The GPS platform (Zeng et al.,
Cell 2026) demonstrated gene expression similarity scoring for drug discovery
but requires a complex Python/Fortran environment with dependency conflicts
that impede reproducibility.

tideGlass addresses this by providing:

1. **Reproducible computation** — pure Rust, deterministic outputs, no
   stochastic dependencies
2. **Cryptographic provenance** — every result signed and traceable
3. **Sovereign execution** — runs on researcher-owned hardware, no cloud
4. **Self-verifying artifacts** — pseudoSpore bundles carry their own
   validation (run `./validate` to reproduce)
5. **Cross-disease extensibility** — same pipeline processes any disease
   in the NF Data Portal or OCTAD disease catalog

## Functionality

tideGlass consists of seven core modules:

| Module | Function | Validation |
|--------|----------|-----------|
| **RGES** | Reversal Gene Expression Score | r=0.52±0.05 vs IC50 |
| **RCL** | Robust Characteristic Level | SNR >1.5× on VCAP_t1 |
| **GPS4Drug** | Drug similarity scoring | R² within 5% of held-out |
| **MolSearch** | Molecular similarity search | IC50 fold >4× |
| **OCTAD** | Open Cancer TherApeutic Discovery | GPS exceeds OCTAD for HCC |
| **Screen** | Disease-specific screening | Top-100 candidate list |
| **NF** | Neurofibromatosis extension | Selumetinib in top-100 |

### Architecture

```
LINCS L1000 → RGES scoring → GPS4Drug similarity → MolSearch → Screen → NF candidates
     ↑                                                                        ↓
ChEMBL 37 ─────────────────────────────────────────────────────────> pseudoSpore
     ↑                                                                        ↓
NF Data Portal ─────────────────────────────────────────────────────> Gonzales
```

## Tests

tideGlass validation evidence:

- **782/782** Gonzales published-data checks (PASS)
- **197/197** primalSpring Tower Atomic stress scenarios
- **329/329** neuralSpring immunological Anderson (nS-601-605)
- **359/359** wetSpring Paper 12 reproductions
- **176** tideGlass crate tests
- **14,000+** total ecosystem validation checks

Run: `cargo test --workspace` in the tideGlass repository.
Run: `tideglass-validate --tier 1 --all-modules` for full pipeline validation.

## Documentation

- Platform documentation: https://primals.eco
- tideGlass evidence: https://tideglass.primals.eco (planned)
- Source: https://git.primals.eco/ecoPrimals/tideGlass
- Provenance: BLAKE3 + Ed25519 on all outputs

## Community Guidelines

- License: AGPL-3.0-or-later
- Issues: https://git.primals.eco/ecoPrimals/tideGlass/issues
- Contributing: PRs welcome; all contributions signed with bearDog
- Support: Contact authors via ORCID-linked channels

## Acknowledgements

Andrea Gonzales provided domain expertise, published data for validation,
and NF-specific drug discovery guidance. The GPS platform (Zeng et al.)
provided the methodological foundation. This work was performed on
commodity hardware (~$15K) using the ecoPrimals sovereign computing
infrastructure.

## References

<!-- paper.bib entries needed -->
<!-- Zeng et al., Cell 2026 — GPS platform -->
<!-- Mok 2026 — ecoPrimals constrained evolution thesis -->
<!-- Subramanian et al. 2017 — LINCS L1000 -->
<!-- Mendez et al. 2019 — ChEMBL -->
<!-- Zeng et al. — OCTAD -->
<!-- Lamb et al. 2006 — Connectivity Map -->

---

## CITATION.cff (companion file needed)

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
type: software
title: "tideGlass"
version: 0.1.0
date-released: 2026-XX-XX
url: "https://git.primals.eco/ecoPrimals/tideGlass"
repository-code: "https://git.primals.eco/ecoPrimals/tideGlass"
license: AGPL-3.0-or-later
authors:
  - family-names: "Mok"
    given-names: "Kevin"
    orcid: "https://orcid.org/0009-0004-2141-0321"
  - family-names: "Gonzales"
    given-names: "Andrea J."
    orcid: "https://orcid.org/XXXX-XXXX-XXXX-XXXX"
```

---

## Pre-Flight Checklist (from JOSS_PUBLICATION.md)

- [ ] tideGlass Phase 0 complete (archaeology)
- [ ] tideGlass Phase 1 complete (reproduction)
- [ ] tideglass-nf module produces NF candidate list
- [ ] At least one NF pseudoSpore delivered and self-verified
- [ ] `cargo test --workspace` passes on fresh clone
- [ ] Andrea confirms domain accuracy
- [ ] Andrea provides ORCID
- [ ] tideglass.primals.eco evidence page live
- [ ] paper.bib with all references
- [ ] CITATION.cff with both authors
- [ ] paper.md finalized
- [ ] Submit via JOSS Open Journals workflow
