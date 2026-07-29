# Kevin Mok — Resume for Inkfish / Marine Research

**This is the version of Kevin's resume tailored for Inkfish expedition
scientist positions. It leads with wet lab microbiology and frames
ecoPrimals as a tool Kevin brings, not the point of the application.**

---

## Kevin Mok

eco.primal@pm.me | Michigan, USA
LinkedIn: linkedin.com/in/ecoprimal
GitHub: github.com/ecoPrimals
Steam: 76561198002558137 (since 2007, Orange Box)

---

## Summary

Microbiologist and data scientist with 5+ years of wet lab experience
(BSL2 fermentation, microbial assays, DNA extraction, spore trapping,
eDNA sampling protocols) and a self-built sovereign GPU compute stack
for on-site genomics analysis. Seeking expedition scientist roles where
bench work and bioinformatics converge — particularly marine microbiome,
eDNA metabarcoding, and coral holobiont research aboard research vessels.

I bring both the hands and the compute. My pipelines run 16S/ITS/metagenomic
analysis on any Vulkan GPU without cloud or CUDA dependency — designed for
disconnected operation in field environments.

---

## Education

**Michigan State University**, East Lansing, MI
- **MS Data Science** (2023–2025)
  - Bioinformatics, machine learning, statistical modeling
- **BS Microbiology** (2018), Minor: Bioethics

---

## Wet Lab Experience

**PFAS Research Lab** — Michigan State University
*Research Specialist* | Oct 2024 – Present
- Environmental sample processing for PFAS ("forever chemicals") detection
- EPA SOP implementation for sample consistency and regulatory compliance
- Biomolecular methods + data science techniques for PFAS research
- Interdisciplinary collaboration on remediation strategies

**MSU Bioeconomy Institute (MSUBI)** — Michigan State University
*Biotechnician* | Jan 2019 – May 2024 (5 years)
- Contract lab: fungi, mycobacteria, anaerobes, aerobes, GMOs
- Bench-scale fermentation in BSL2: media prep, growth optimization
- Aseptic technique, vessel sterility, contamination control
- Quantitative microbial analysis: viable cell counts, spore counts,
  microscopic ID, isolation on selective media, OD measurements
- Chemical assays: PO₄, NH₃, mass spectrometry, HPLC, enzyme kinetics
- Automated data collection (Visual Basic, Excel macro systems)
- Trained new hires on aseptic technique and analytical methods

**Hausbeck Plant Pathology Lab** — Michigan State University
*Research Assistant* | May 2018 – Jan 2019
- Hirst-type spore trap preparation and field deployment (BSL2)
- Wet-mount slide preparation for spore counting and DNA extraction
  (cucurbit downy mildew — *Pseudoperonospora cubensis*)
- Microscopic spore identification and quantification
- Field work: crop disease survey, sample collection, farmer liaison

**ROME Lab** — Michigan State University
*Undergraduate Research Assistant* | Jan 2018 – May 2018
- Rumen microbiome: serial enrichment and dilution for bacterial isolation
- Selective media preparation for carbon degrader biodiversity
- Sequence analysis using Ribosomal Database Project (RDP)
- Presented at University Undergraduate Research and Arts Forum (UURAF)

---

## Computational Research

**Sandia National Laboratories**, Albuquerque, NM
*Research Fellow* | Summer 2024
- Bacterial toxin effects on raceway algae via high-throughput sequencing
- Bioinformatics pipeline design for microbial interaction analysis
- Computational integration of sequencing data into biotech frameworks
- DOE national lab environment, multidisciplinary collaboration

**ecoPrimals** — Self-built sovereign scientific computing platform
*Founder & Lead Architect* | May 2025 – Present (14 months, ongoing)
- 3.6 million lines of Rust, 105,000+ tests, AI-assisted development
- **GPU-accelerated bioinformatics**: DADA2 16S pipeline running on
  any Vulkan GPU (no CUDA). Reproduced 63 published papers computationally
- **Sovereign mesh networking**: encrypted peer-to-peer transport stack
  running on 8+ physical nodes (353× faster than WireGuard on LAN)
- **Content-addressed storage**: BLAKE3-hashed, deduplicated, with
  cryptographic provenance chains — designed for field data integrity
- **Disconnected operation**: syncs on reconnect, runs fully offline
  on laptop-class hardware, 30MB RSS edge profile
- **Open source**: AGPL-3.0, all data CC-BY-SA
- **Live site**: sporeprint.primals.eco | **Repos**: github.com/ecoPrimals

---

## Relevant Skills for Expedition Science

### Wet Lab (Hands-On)
- Aseptic technique (5 years BSL2)
- Microbial culture: isolation, enumeration, identification
- DNA extraction and sample preservation
- Fermentation: batch, fed-batch, parameter control
- Chemical assays: HPLC, mass spec, enzyme kinetics, colorimetric
- Spore trapping and microscopy
- Environmental sampling (PFAS, algae, rumen, plant pathology)
- SOP development and regulatory compliance (EPA)

### Bioinformatics (Compute)
- 16S/ITS amplicon analysis (DADA2, taxonomic classification)
- Metagenomic analysis and diversity indices
- GPU-accelerated pipeline execution (Vulkan/WGSL, no CUDA)
- Phylogenetics, UniFrac, alpha/beta diversity
- Custom pipeline development in Rust (not just running tools)
- Sovereign data infrastructure (runs on vessel hardware, no internet required)

### Field & Logistics
- U.S. Army veteran (Infantryman, 2012–2015): leadership under
  austere conditions, communications equipment management ($2M inventory),
  intelligence analysis, briefing/debriefing 130+ personnel
- Field sample collection across Michigan agriculture
- Equipment troubleshooting and field maintenance
- Training and mentorship of new personnel

---

## What I Bring to an Expedition

1. **Both the hands and the compute**: I can do the bench work (DNA
   extraction, eDNA filtration, sample preservation, culture) AND
   run the bioinformatics (16S, metagenomics, phylogenetics) on the
   same hardware that's already aboard.

2. **Sovereign data pipeline**: My compute stack runs offline, on any
   GPU, with cryptographic provenance from sample to analysis output.
   No cloud upload required. No CUDA dependency. Same-day results
   from same-day samples.

3. **Low cost, high output**: My development costs are near-zero
   (AI-assisted, personal hardware). A patron/sponsor arrangement
   for wet lab work and expedition berth is dramatically cheaper
   than traditional compute infrastructure or contracted bioinformaticians.

4. **Military discipline in austere environments**: 3 years active duty
   infantry. Comfortable in confined spaces, extended deployments,
   strict protocols, and high-accountability environments.

5. **Microbiology perspective on marine ecosystems**: Coral holobionts
   are microbial ecosystems. Deep-sea chemosynthetic communities are
   microbiology. eDNA is microbiology. I see the organisms that the
   macroecologists sample around.

---

## Expedition Science Fit — Marine Microbiology

**Inkfish generates exactly the kind of data my tools process:**

| Inkfish Activity | Kevin's Capability |
|-----------------|-------------------|
| Coral tissue sampling (>1,200/expedition) | DNA extraction, preservation, sample QC |
| eDNA water column sampling | Filtration protocols, Sterivex/membrane handling |
| Metabarcoding (16S, 18S, COI) | GPU-accelerated DADA2 pipeline, taxonomic classification |
| Photogrammetry (AUV 3D models) | GPU compute for image processing (Vulkan) |
| Sample provenance and chain of custody | BLAKE3 hashing, content-addressed storage, attribution chains |
| Data transfer ship-to-shore | Mesh networking, sync-on-reconnect, offline operation |
| Open data repository contribution | All tools AGPL-3.0, all data CC-BY-SA |

---

## Publications & Presentations

- University Undergraduate Research and Arts Forum (UURAF), MSU — rumen microbiome research
- ecoPrimals: 313-page public site with 99 rendered notebooks,
  63 paper reproductions, benchmark data (sporeprint.primals.eco)
- Lattice QCD consumer GPU validation (hotSpring) — quark-gluon
  deconfinement detected on $4K consumer hardware

---

## References

Available on request. Academic references from MSU Microbiology,
MSU Data Science, PFAS Lab, Bioeconomy Institute, and Sandia
National Laboratories.

---

*Resume version: Inkfish/Marine Research — July 29, 2026*
*This resume emphasizes wet lab biology and expedition readiness.*
*For software/infrastructure emphasis, see LINKEDIN_PROFILE_CONTENT.md*
