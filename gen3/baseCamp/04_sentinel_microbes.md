# Sub-Thesis 04: Microbial Sentinels — Community Shifts as Biosensors for Contamination and Disease

**Date:** February 23, 2026
**Status:** Proposal with Anderson-derived detection framework
**Domain:** Environmental microbiology, biosensing, contamination monitoring
**Novelty:** Anderson regime shift as a measurable signal for environmental
perturbation; ESN/reservoir computing for real-time anomaly detection on
community time series

---

## Abstract

Microbial communities respond to environmental perturbation faster than any
chemical sensor. Changes in community structure — diversity, evenness,
functional gene expression — are early-warning indicators of contamination,
disease, and ecological disruption. We propose using the Anderson localization
framework to define a quantitative detection signal: environmental
perturbation shifts the community from one Anderson regime to another,
and this regime shift is detectable via the level spacing ratio (r) computed
from community composition data.

The framework connects three threads: (1) Anderson localization as a
community health metric, (2) echo state networks (ESN) / reservoir computing
(validated in wetSpring Exp114-119) for real-time anomaly detection on
community time series, and (3) specific applications to PFAS contamination,
harmful algal blooms, and pathogen emergence.

---

## 1. The Sentinel Concept

### 1.1 Why Microbes as Sensors

Microbes respond to environmental change on timescales of hours to days.
Chemical sensors detect only what they are designed to detect. A microbial
community responds to EVERYTHING — novel contaminants, pH shifts, nutrient
pulses, temperature changes, oxygen gradients — because the community
structure integrates all environmental pressures simultaneously.

The challenge: how to read the community signal and distinguish meaningful
perturbation from natural variation.

### 1.2 The Anderson Signal

A healthy, undisturbed microbial community has a characteristic diversity
profile (Pielou evenness J) that maps to an Anderson disorder level (W).
In 3D soil, the community sits in the extended regime (QS-active, r above
midpoint).

Perturbation changes the community:

| Perturbation | Effect on J | Effect on W | Anderson regime shift |
|-------------|-------------|-------------|----------------------|
| Contamination (PFAS, heavy metal) | J decreases (sensitive species die) | W decreases | Extended → deeper extended (fewer species, less disorder) |
| Nutrient pulse (fertilizer runoff) | J decreases (bloom species dominate) | W decreases | Extended → deeper extended |
| Chronic stress (salinity, drought) | J decreases slowly | W decreases slowly | Gradual shift toward monoculture |
| Acute toxicity | J drops sharply | W drops sharply | Sudden regime collapse |
| Recovery after perturbation | J increases (recolonization) | W increases toward pre-disturbance | Return to original regime |

The key insight: the DIRECTION and RATE of the Anderson regime shift encode
information about the perturbation type and severity.

### 1.3 Distinguishing Perturbation from Natural Variation

Natural community fluctuations produce small variations in J (and therefore W)
around a baseline. An anomaly detection algorithm (ESN/reservoir computing)
trained on the natural variation can flag perturbation-driven shifts that
exceed the natural envelope.

## 2. Application: PFAS Contamination Detection

### 2.1 Background

Per- and polyfluoroalkyl substances (PFAS, "forever chemicals") accumulate
in soil and water near military installations, airports, and wastewater
treatment plants. Current detection requires lab-based LC-MS/MS analysis
($200-500/sample, days turnaround).

### 2.2 PFAS and Microbial Communities

PFAS impacts on soil microbial communities are documented but poorly
systematized (Cai et al. 2023, Guo et al. 2022). Known effects:

- Decreased overall diversity at high PFAS concentrations (> 100 ng/g)
- Specific taxa respond: Sphingomonadaceae (PFAS-degrading) increase;
  many anaerobes decrease
- Functional shifts: membrane transport genes upregulated (efflux pumps
  for PFAS expulsion)

### 2.3 Anderson Detection Framework

Baseline sampling establishes community J and W for a site. PFAS
contamination produces:

1. **Diversity decrease** → J drops → W drops → Anderson regime shifts
   toward lower disorder
2. **Functional gene shift** → QS gene expression changes (PFAS-stressed
   communities may upregulate QS for coordinated efflux pump expression)
3. **Detectable via 16S time series** using wetSpring sovereign pipeline

Detection threshold: the Anderson regime shift becomes detectable before
PFAS reaches levels harmful to humans — microbial communities are more
sensitive than mammalian toxicity thresholds.

### 2.4 Jones Lab Connection

A. Daniel Jones (BMB/Chemistry, MSU) leads PFAS research. Pairing his
LC-MS/MS analytical capability with microbial community monitoring would
create a dual-sensor system: microbes for early detection, chemistry for
confirmation and quantitation.

## 3. Application: Harmful Algal Bloom Prediction

### 3.1 Background

Harmful algal blooms (HABs) in freshwater systems produce cyanotoxins
(microcystin, cylindrospermopsin) that contaminate drinking water. Current
monitoring relies on satellite imagery and grab sampling — reactive, not
predictive.

### 3.2 The Microbial Precursor Signal

Before a visible bloom, the microbial community shifts:

- Cyanobacterial OTUs increase in relative abundance
- Heterotrophic bacteria that associate with cyanobacteria increase
- Overall diversity (J) temporarily increases then crashes as bloom dominates

The pre-bloom community shift is detectable via 16S sequencing days to weeks
before the visible bloom.

### 3.3 Anderson Framework for Blooms

- Pre-bloom: high diversity → W high → 3D water column in extended regime
  but planktonic → dilution-suppressed QS (Exp137)
- Bloom onset: diversity crashes → W drops → surface mat forms (2D geometry)
- Full bloom: near-monoculture → J near 0 → W near 0.5 → QS active in the
  2D mat (low W overcomes 2D localization)

The regime transition from "diverse planktonic" to "mat-forming monoculture"
is the detectable signal.

### 3.4 Cahill/Smallwood Connection

Jesse Cahill and Chuck Smallwood (Sandia National Laboratories, Bioscience
Division) work on bacterial toxins in raceway algae systems. The HAB
prediction framework applies directly to their managed algae cultivation —
detecting contaminating cyanobacteria before they compromise the culture.

## 4. Application: Pathogen Emergence Monitoring

### 4.1 Concept

Hospital and wastewater environments harbor pathogenic bacteria that acquire
antibiotic resistance. Community monitoring can detect:

- Resistance gene enrichment (QS-regulated in many species)
- Community shifts toward opportunistic pathogens
- Biofilm formation on surfaces (Anderson: 3D → QS active → coordinated
  virulence factor production)

### 4.2 Anderson Prediction for Hospitals

Hospital surface biofilms (3D) → QS active → coordinated resistance expression.
Disinfection that reduces biofilm to 2D film → Anderson localization suppresses
QS → reduced coordinated virulence. But if biofilm re-establishes (3D) → QS
returns → virulence factors re-expressed.

Actionable insight: surface design that PREVENTS 3D biofilm formation
(textured surfaces maintaining 2D geometry) would use Anderson localization
to suppress pathogen coordination.

## 5. The Computational Framework

### 5.1 Community Monitoring Pipeline

```
Environmental sample (weekly 16S)
        │
  wetSpring sovereign pipeline
  (DADA2 → chimera → taxonomy)
        │
  Community composition (OTU table)
        │
  Pielou evenness J → Anderson disorder W
        │
  Level spacing ratio r (computed or estimated from lookup)
        │
  ESN/reservoir computing anomaly detector
  (trained on baseline natural variation)
        │
  Alert: regime shift detected
  (type: acute/chronic, direction: decreasing/increasing diversity)
```

### 5.2 ESN Anomaly Detection

The echo state network (ESN) approach validated in neuralSpring and wetSpring
(Exp114-119, reservoir computing primitives) is designed for exactly this
task: detecting anomalous patterns in time series without explicit model
specification.

Training: 12-24 months of baseline community sampling (monthly 16S)
establishes the natural variation envelope. The ESN learns the dynamics
of J, W, and r under normal conditions.

Detection: new community samples that push the ESN prediction error above
a calibrated threshold trigger an alert.

### 5.3 NPU Deployment

The ESN runs on the neuromorphic processing unit (NPU) at the edge — no cloud
dependency, no data exfiltration, real-time inference. This is the ecoPrimals
sovereign compute advantage: environmental monitoring that runs on local
hardware with no external dependencies.

## 6. Testable Predictions

| Prediction | Test | Expected result |
|-----------|------|----------------|
| PFAS contamination detectable via community shift before chemical threshold | Paired 16S + LC-MS/MS on contaminated vs clean sites | Community J drops at PFAS < 10 ng/g (below human health threshold) |
| HAB precursor community shift detectable 7-14 days before bloom | Weekly 16S sampling at bloom-prone lake | J and taxonomic composition shift before cyanobacteria dominate |
| Biofilm geometry determines pathogen coordination | 3D vs 2D surface microcosm with P. aeruginosa | QS gene expression (lasI, rhlI) higher on 3D surfaces |
| ESN detects regime shifts with > 90% recall | Simulated perturbation on baseline community time series | ROC analysis with ESN vs threshold detector |

## 7. Connection to Constrained Evolution

Environmental contamination is a NOVEL CONSTRAINT applied to an existing
community. The constrained evolution framework predicts the community will
evolve toward contamination-specific fitness peaks — the same process that
produces Taq in hot springs and streamlined genomes in the LTEE.

The sentinel concept turns this process into a measurement: the RATE and
DIRECTION of the community's evolutionary response to a novel constraint
IS the signal. Anderson localization provides the physics to quantify it.
