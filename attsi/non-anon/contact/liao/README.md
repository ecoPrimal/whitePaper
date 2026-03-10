# Wei Liao / ADREC — Outreach & Anaerobic Microbial Ecology

**Faculty**: Wei Liao, Ph.D., P.E. — Professor, Biosystems & Agricultural Engineering, MSU
**Role**: Director, Anaerobic Digestion Research and Education Center (ADREC)
**Website**: https://sites.google.com/msu.edu/liao-research-group/home
**ADREC**: https://sites.google.com/msu.edu/adrec/home
**Email**: liaow@msu.edu | Room 202, 524 S. Shaw Ln | (517) 432-7205
**Location**: ADREC — 4090 College Rd, Building G, Lansing, MI 48910

**Key Personnel**:
- **Sibel Uludag-Demirer, Ph.D.** — ADREC Research Associate (demirers@msu.edu, 517-353-3741)
  Electrocoagulation, water reclamation, BMP studies

**Connection**: Interviewed with ADREC before Sandia internship (2024). The author's
MSUBI bioreactor experience (5 years — Pivot Bio, MycoWorks, fermentation, BSL2 fungi/anaerobes)
is the direct counterpart: same bioengineering principles (mixing, pH, residence time,
microbial community dynamics) applied to different products. ADREC does waste-to-energy;
MSUBI did biotech scale-up. The reactor fundamentals are identical.

---

## Domain

Liao's group develops integrated systems for organic waste utilization —
anaerobic digestion, algae cultivation, wastewater treatment, carbon
sequestration. Four research tracks:

1. **Integrated Biorefining** — agricultural residues → fuel + chemicals
2. **Advanced Anaerobic Digestion** — microbial community dynamics in biogas production
3. **Algae & Carbon Capture** — photobioreactor cultivation, CO₂ sequestration
4. **Wastewater Treatment** — electrocoagulation, nutrient recovery, water reclamation

The unifying thread: microbial communities processing organic substrates
under controlled conditions. This is wetSpring's domain (QS, community
dynamics, Anderson localization) applied to engineered bioreactor systems.

---

## Why This Contact Matters

The scientific question that bridges ADREC to ecoPrimals:

**What happens to quorum sensing when the same organisms face aerobic vs
anaerobic conditions?**

- wetSpring models QS in largely aerobic contexts (Vibrio, Pseudomonas biofilms)
- healthSpring's gut microbiome is largely anaerobic
- ADREC's anaerobic digesters are fully oxygen-absent
- Soil (airSpring) has aerobic/anaerobic zones based on water saturation
- Facultative anaerobes (E. coli, Klebsiella, many Enterobacteriaceae, Firmicutes)
  carry both metabolic pathways — do they carry parallel QS circuits?

Global transcription regulators (FNR, ArcAB) reprogram gene expression under
anaerobic conditions. If QS autoinducer production and receptor expression
change with oxygen availability, then the Anderson disorder landscape
(wetSpring's central model) undergoes a phase transition when oxygen is
removed. The "disorder" isn't static — it reorganizes with the environment.

This is a baseCamp Paper 16 concept: see `gen3/baseCamp/README.md`.

---

## Key Publications for Reproduction

| # | Paper | Relevance | ecoPrimals Bridge |
|---|-------|-----------|-------------------|
| L1 | Wang et al. 2020 — "Prediction of anaerobic digestion performance using machine learning" (Bioresource Technology 298, 122495) | ML for biogas yield prediction from operational parameters | neuralSpring (ESN/LSTM surrogates), healthSpring (NLME population modeling) |
| L2 | Yang et al. 2016 — "Phylogenetic analysis of anaerobic co-digestion reveals linkages between bacterial communities and digestion performance" (Advances in Microbiology 6, 879-897) | Community-function linkage via phylogenetics | wetSpring (16S pipeline, diversity-disorder mapping), Paper 01 (Anderson-QS) |
| L3 | Rojas-Sossa et al. 2017 — "Effects of coffee processing residues on anaerobic microorganisms" (Bioresource Technology 245, 714-723) | Substrate perturbation → community response | wetSpring (disorder perturbation), airSpring (soil substrate effects) |
| L4 | Chen et al. 2016 — "Response of anaerobic microorganisms to different culture conditions and corresponding effects on biogas" (Biomass and Bioenergy 85, 84-93) | Same organisms, different conditions → different community dynamics | **Core of the aerobic/anaerobic question** — the QS phase transition |
| L5 | Zhong et al. 2016 — "Fungal fermentation on anaerobic digestate for lipid-based biofuel production" (Biotechnology for Biofuels 9, 253) | Aerobic process operating on anaerobic substrate — the oxygen boundary in practice | wetSpring (cross-regime QS), the aerobic/anaerobic interface |
| L6 | Rojas-Sossa et al. 2019 — "Effect of AFEX treated corn stover on anaerobic microbes" (Biomass and Bioenergy 127, 105263) | Pretreated substrate → microbial community shift | wetSpring (disorder landscape reshaping via substrate) |

---

## What ecoPrimals Enables For ADREC

### Today (validated)

| Capability | ADREC Current Workflow | ecoPrimals Version |
|-----------|----------------------|-------------------|
| Community diversity tracking | 16S + QIIME/Mothur (Python/R) | wetSpring 16S pipeline — sovereign Rust, 334 experiments, DADA2 |
| Biogas yield prediction | ML models in Python (Wang 2020) | neuralSpring ESN/LSTM — Rust, GPU-accelerated, streaming |
| Community-performance linkage | R phyloseq + manual analysis | wetSpring Anderson-QS — disorder-diversity bridge, automatic |
| Microbiome similarity | Bray-Curtis in R | barraCuda GPU Bray-Curtis — validated, orders of magnitude faster |
| Time series anomaly detection | Manual thresholds | wetSpring ESN regime classifier — NPU-deployable |

### With Paper 16 (aerobic-anaerobic QS bridge)

| Capability | ADREC Application | Springs |
|-----------|------------------|---------|
| Anaerobic QS modeling | Digester community stability and process optimization | wetSpring + healthSpring |
| Aerobic-anaerobic phase transition | Understanding community shifts at oxygen boundaries | wetSpring + airSpring |
| Anderson disorder across O₂ regimes | Quantifying how oxygen changes QS propagation landscape | wetSpring + groundSpring |
| Biogas process monitoring | ESN sentinel for digester health — NPU-deployable | neuralSpring + Paper 04 |
| Gut-digester analogy | Both are engineered anaerobic environments with microbial communities | healthSpring (gut), ADREC (digester) |

---

## MSUBI Connection

The author's bench experience maps directly to ADREC's research:

| MSUBI Experience | ADREC Counterpart |
|-----------------|-------------------|
| 10L bioreactor fermentation (Pivot Bio) | Plug-flow anaerobic digester |
| Fungal cultivation (MycoWorks, Mortierella) | Fungal fermentation on digestate (Zhong 2016) |
| BSL2 microorganism handling | Anaerobic microbial community sampling |
| Fermentation scale-up (bench → pilot) | Digester optimization (lab → farm-scale) |
| Nitrogen-fixation microbiology (soybean isolates) | Nutrient recovery from digester effluent |
| Microbial community analysis (rumen isolates) | Phylogenetic community-performance linkage |

The atlasHugged essay on fermentation (`gen3/atlasHugged/08_DISCOVERY_IS_LOCAL.md`)
provides the philosophical framing: humans used anaerobic microbiology for thousands
of years before understanding the biology. The same QS systems ADREC studies in
digesters were shaping beer, wine, and pickles since antiquity.

---

## Outreach Strategy

### Approach

1. **Lead with shared ground.** "I interviewed with ADREC before my Sandia
   fellowship. I've spent the last year building computational tools for
   microbial community analysis — the same dynamics you study in digesters."

2. **Show the pipeline.** Wang 2020 used ML to predict digester performance —
   neuralSpring does the same thing in compiled Rust on GPU. Point to the
   16S pipeline and diversity analytics.

3. **Ask about oxygen.** The scientific question — QS across aerobic/anaerobic
   regimes — comes from the author's bench experience. ADREC's controlled
   environments are the ideal experimental system for testing it.

4. **Offer concrete value.** "Your ML digestion models run in Python. Here's
   the same math compiled to native binary, GPU-accelerated, deployable at
   the digester." Process monitoring sentinel = Paper 04 applied to ADREC.

### What We're Asking

- Does the anaerobic QS question resonate with what they observe in digester communities?
- Are there datasets (16S, community composition, gas yield time series) that could test
  the Anderson-QS model in anaerobic conditions?
- Would a Rust/GPU 16S pipeline be useful for their community analysis workflow?
- Can they point to literature on QS in anaerobic consortia?

### Tone

Collegial, grounded in shared MSU context and bench experience. Not cold outreach —
the interview creates a warm enough connection, and MSUBI fermentation work is the
common language.

---

## Outreach Readiness

### Ready Now
- wetSpring 16S pipeline: 334 experiments, 9,200+ checks
- Anderson-QS framework: Paper 01, validated
- Community diversity analytics: Bray-Curtis, Shannon, Simpson, rarefaction — all GPU
- neuralSpring ML: ESN/LSTM time series, regime classification
- atlasHugged fermentation essay: philosophical context
- Bench experience: 5 years bioreactor work, directly relevant

### Not Ready (would strengthen the pitch)
- No anaerobic QS-specific experiments yet (Paper 16 is the concept, not the validation)
- No digester dataset reproduced
- No Wang 2020 ML benchmark comparison
- No specific anaerobic autoinducer modeling in wetSpring

### Minimum Viable Outreach
1. Reproduce Wang 2020 ML predictions in neuralSpring (public benchmark)
2. Apply wetSpring 16S + diversity pipeline to a public anaerobic digester dataset
3. Frame the aerobic-anaerobic QS question with specific predictions
4. Contact with results, not just ideas

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — outreach plan, domain mapping, work inventory |

## Timeline

- **Pre-contact**: Reproduce Wang 2020 (neuralSpring), run 16S pipeline on public digester data
- **Contact**: Email preferred (liaow@msu.edu), reference ADREC interview and bench background
- **Tone**: "I'm the fermentation person who interviewed with ADREC. I've been building
  computational tools for microbial communities. Your digesters are the ideal system for
  a question I've been working on."
