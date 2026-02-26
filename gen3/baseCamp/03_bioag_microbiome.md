# Sub-Thesis 03: Precision Microbiome Engineering for Perennial Tree Crops

**Date:** February 26, 2026
**Status:** Proposal with Anderson-derived predictions. Track 4 validates the soil QS framework (9 papers, Exp170-182, 321 checks, full three-tier). Rhizosphere W ≈ 6.7 confirmed deep in extended regime (Exp129). R:P eavesdropper ratio = 2.3:1 in rhizosphere (Exp142). Correlated disorder (biofilm clustering) strengthens QS (Exp151)
**Domain:** Agricultural microbiology, soil science
**Novelty:** Anderson localization model applied to orchard microbiome design;
geometry-aware inoculant selection for pistachio and almond

---

## Abstract

We apply the Anderson localization framework to agricultural microbiome
engineering for perennial tree crops (pistachio, almond). The model provides
geometry-specific predictions for where quorum sensing (QS) — and therefore
coordinated microbial phenotypes like N-fixation regulation, biocontrol
agent expression, and mycorrhizal helper functions — will succeed or fail.
The central prediction: inoculant strategies that promote 3D biofilm formation
on root surfaces will outperform broadcast soil inoculation, because Anderson
localization suppresses QS in dilute 3D or 2D-surface geometries while
sustaining it in structured 3D biofilms.

---

## 1. The Problem: Tree Crop Microbiome Engineering

### 1.1 Context

California's Central Valley produces 99% of U.S. pistachios and 80% of global
almonds. Both crops face compounding pressures:

- Water scarcity (overdraft of Central Valley aquifer)
- Soil salinization from poor drainage and evaporation
- Nitrogen costs ($200-400/acre/yr for synthetic fertilizer)
- Disease pressure: Verticillium wilt (pistachio), Hull rot (almond)
- Regulatory pressure on synthetic inputs (CA Sustainable Groundwater Management Act)

A healthy soil microbiome can address all five: water-efficient mycorrhizal
networks, salt-tolerant rhizobacteria, biological N-fixation, pathogen
suppression via antibiotic QS circuits, and reduced synthetic input dependency.

### 1.2 The Gap

Current inoculant strategies (broadcast application, seed coatings, drip-line
injection) have inconsistent field results. Meta-analyses show 40-60% of
inoculant field trials show no significant benefit (Kaminsky et al. 2019).

Why? We propose: **geometry determines whether the inoculant can coordinate
its beneficial phenotype.** An N-fixing consortium that cannot maintain QS
cannot regulate nitrogenase expression. A biocontrol agent that cannot signal
its neighbors cannot mount a coordinated antibiotic response.

## 2. Anderson Model Applied to Orchard Soil

### 2.1 Geometry Zones in an Orchard

| Zone | Geometry | Anderson prediction | QS status |
|------|----------|--------------------|-----------| 
| Bulk soil (inter-row) | 3D pore network, moderate-high diversity | W < W_c in 3D → QS-active | Coordinated community |
| Root surface (rhizoplane) | 2D → 3D biofilm | Depends on biofilm thickness — 3D biofilm = QS-active | QS active if biofilm > 64 cells thick (Exp138) |
| Root interior (endosphere) | 3D, low diversity | W very low (few species) → deep extended regime | Strong QS |
| Canopy drip zone | 3D soil, disturbed | 3D → QS-active but seasonal disruption resets community | Periodic QS |
| Irrigation line surface | 2D film | Anderson: QS fails in 2D | Biofilm without coordination |

### 2.2 The Rhizosphere Prediction

Orchard root systems create a 3D geometry gradient:

```
Bulk soil (3D, diverse)   →   Rhizosphere (3D, enriched)   →   Rhizoplane (2D→3D)   →   Endosphere (3D, sparse)
  W ~ 13, QS active           W ~ 8-10, QS active               W varies                   W ~ 2-4, QS active
```

The **rhizoplane** is the critical interface. If the inoculant can establish
a 3D biofilm here, Anderson predicts QS success. If it remains as a 2D
monolayer, QS fails.

### 2.3 Inoculant Design Rules from Anderson

1. **Select biofilm-formers**: inoculant strains MUST form 3D biofilm
   on root surfaces. Non-biofilm strains will lose QS regulation.
2. **Monoculture inoculants have lowest disorder**: a single-species
   inoculant has J = 0 → W = 0.5 → deep in extended regime even in 2D.
   But monocultures are ecologically fragile.
3. **Defined consortia (3-5 species) are optimal**: J ~ 0.5-0.8 →
   W ~ 7.75-12 → comfortably QS-active in 3D, QS-suppressed in 2D.
   Ecologically robust + geometry-dependent coordination.
4. **Avoid planktonic inoculation**: drip-line injection into saturated
   soil → planktonic dispersion → dilution → W_eff >> W_c (Exp137).
   Instead: apply to root zone as paste, gel carrier, or seed coating.

## 3. Pistachio-Specific Applications

### 3.1 Verticillium Wilt Suppression

Verticillium dahliae enters through roots and colonizes xylem. Biocontrol
agents (Trichoderma, Bacillus) suppress it via antibiotic production, which
is QS-regulated in many species.

Anderson prediction: biocontrol agents applied as root-zone biofilm will
coordinate antibiotic production. Agents applied as soil drench will NOT
coordinate, despite equivalent cell counts.

### 3.2 Mycorrhizal Network Optimization

Pistachio forms arbuscular mycorrhizal (AM) associations. Mycorrhizal helper
bacteria (MHB) facilitate the association via QS-mediated signaling.

Anderson prediction: MHB effectiveness depends on achieving 3D biofilm at the
mycorrhizal interface. Inoculants that promote AM colonization should include
MHB strains selected for biofilm formation, not just AM spore counts.

### 3.3 Salinity Tolerance

Halotolerant rhizobacteria produce ACC deaminase and exopolysaccharides under
QS regulation. In saline Central Valley soils, these traits are essential for
root health.

Anderson prediction: salt-tolerant biofilm-formers should be selected for
inoculants in saline orchards. Their QS-regulated EPS production will be
maintained only if they form 3D structure on root surfaces.

## 4. Almond-Specific Applications

### 4.1 Hull Rot Management

Hull rot (Rhizopus stolonifer, Monilinia fructicola) is exacerbated by
nitrogen excess in hull tissue. Reducing synthetic N via biological N-fixation
would reduce hull rot susceptibility.

Anderson prediction: N-fixing inoculants applied as root-zone biofilm should
reduce the need for synthetic N. But N-fixation regulation (nif genes) is
QS-dependent in many diazotrophs — the regulation only works if the biofilm
maintains QS coordination.

### 4.2 Water-Efficient Root Architecture

Some rhizobacteria produce auxin and other phytohormones under QS regulation,
promoting deeper root growth. In drought-stressed almonds, deeper roots access
water reserves.

Anderson prediction: hormone-producing inoculants must be in 3D biofilm to
coordinate hormone production. Root-zone application > broadcast.

## 5. The Pivot Bio Parallel

### 5.1 Annual Crops (Corn, Soybean)

Pivot Bio's PROVEN and RETURN products use engineered Klebsiella variicola
(corn) and Kosakonia sacchari (soybean) as seed-coat N-fixation inoculants.
The seed coat places the inoculant directly on the root surface — exactly
the geometry Anderson predicts will sustain QS.

Pivot Bio's field results (10-15 lbs N/acre replacement) may represent the
Anderson-allowed maximum for a single-strain 2D→3D transition on root surface.

### 5.2 Perennial Adaptation

For perennial tree crops, seed coating is not possible (no annual replanting).
Alternatives:

| Method | Geometry | Anderson prediction |
|--------|----------|-------------------|
| Root dip at transplant | 3D biofilm on young root | QS-active, establishes early |
| Drip injection (dilute) | Planktonic in bulk soil → hope for root colonization | QS fails during transit; may recover on root |
| Gel carrier on root zone | 3D matrix embedding inoculant near roots | QS-active in gel → transfers to root biofilm |
| Mycorrhizal co-inoculation | 3D within AM network structure | QS-active in hyphal network |

Gel carrier application emerges as the Anderson-optimal method: it maintains
3D geometry during the critical establishment period.

## 6. Experimental Design

### 6.1 Computational Validation (wetSpring)

- Extend Exp127-130: model orchard rhizosphere as concentric 3D/2D shells
- Parameterize with real rhizosphere diversity data (Bulgarelli et al. 2012)
- Predict QS-active/suppressed transitions along root-soil gradient
- Compare inoculant formulations (monoculture vs consortium vs soil drench)

### 6.2 Bench Validation (Proposed)

- GFP-tagged QS reporter strains in root-zone microcosms
- Compare biofilm vs planktonic geometry for QS activation threshold
- Use pistachio rootstock (UCB-1) in growth chamber

### 6.3 Field Validation (Proposed)

- Partner with KBS (Kellogg Biological Station) LTAR or UC Davis extension
- Compare gel-carrier vs drip-injection vs broadcast for N-fixing inoculant
  on almond trees
- Measure: QS gene expression (RT-qPCR for luxI/luxR), root colonization
  density, N-fixation (acetylene reduction), yield

## 7. neuralSpring Connections

neuralSpring's transfer learning framework (Exp 004) applies directly to
inoculant response prediction:

- **Cross-climate transfer**: Michigan → California parallels neuralSpring's
  pistachio → almond climate transfer learning. Train on KBS (Kellogg
  Biological Station) Michigan soil data, predict inoculant success in
  California almond orchards
- **LSTM time series** (Study 004, NSE=0.849): Predict seasonal QS regime
  dynamics from soil parameters (moisture, temperature, diversity index)
- **HMM for introgression**: Detect horizontal gene transfer of QS genes
  in inoculant strains post-application — does the inoculant's QS circuit
  persist or get displaced by native community HGT?

## 8. Connection to Constrained Evolution

Orchard soil is a constrained environment: water-limited, salinized,
pathogen-pressured. The microbiome evolves under these constraints toward
whatever community can persist. The Anderson model predicts WHICH evolved
communities can coordinate. The inoculant engineer's job is to select strains
whose evolved QS circuits will work in the geometry available.

This is constrained evolution applied as engineering: understanding the
constraint landscape to design interventions that work with the physics
rather than against it.

## 8. PFAS Monitoring Angle

Agricultural soils near military installations and wastewater application sites
accumulate PFAS. The Anderson model predicts that PFAS contamination disrupts
soil community structure → diversity shifts → Anderson regime changes →
detectable via QS gene expression monitoring.

This connects to Sub-thesis 04 (Microbial Sentinels) and the A. Daniel Jones
lab (BMB/Chemistry, MSU) PFAS research program.
