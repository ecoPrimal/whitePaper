# Paper 13: Sovereign Human Health Computing — Per-Person Translation of PK/PD, Microbiome, Biosignal, and Endocrine Pipelines

**Spring**: healthSpring (V9)
**Domain**: Human Health × Pharmacology × Microbiome × Biosignal × Endocrinology × Clinical Translation
**License**: AGPL-3.0-or-later
**Date**: March 9, 2026
**Faculty**: Dr. Andrea J. Gonzales (MSU Pharmacology & Toxicology), Dr. Charles Mok (Allure Medical)
**Status**: **Validated** — Tier 0+1+2+3 complete (37 experiments, 4 tracks + diagnostics + GPU + visualization + clinical TRT + SAME DAVE integration). Patient-parameterized clinical scenarios (5 archetypes). petalTongue motor command channel + IPC bridge.

---

## Thesis

Sovereign scientific computing can replace Python/NONMEM/proprietary tool chains for human health applications — pharmacokinetics, microbiome analytics, real-time biosignal processing, and endocrine outcome modeling — using pure Rust validated against published data, **with live GPU acceleration** via barraCuda WGSL shaders and heterogeneous dispatch via toadStool/metalForge.

Population-level validation means nothing without per-person translation. V9 closes this loop: a `PatientTrtProfile` generates a patient-specific clinical scenario — parameterized by age, weight, testosterone level, comorbidities — rendered in petalTongue's clinical mode via the SAME DAVE motor command channel. The clinician sees the patient, not the infrastructure.

GPU-native execution is validated: a single consumer GPU handles population-scale health computations (10M elements, 207 M/s throughput) with the same WGSL shaders portable to edge devices, TPU, and NPU. Mixed hardware dispatch via NUCLEUS topology routes workloads to CPU, GPU, or NPU based on scale and substrate availability.

The springs validate science. healthSpring makes the drug.

---

## Tracks

### Track 1: Pharmacokinetic / Pharmacodynamic Modeling (Exp001–006)

Pure Rust PK/PD tools extending neuralSpring nS-601–605 (veterinary) to human therapeutics via allometric scaling.

| Exp | Title | Key Result |
|-----|-------|-----------|
| 001 | Hill dose-response (4 JAK inhibitors + canine reference) | 4-parameter Hill equation, IC50/EC50 validated |
| 002 | One-compartment PK (IV bolus + oral Bateman + multiple dosing) | AUC trapezoidal, steady-state accumulation ratio |
| 003 | Two-compartment PK (biexponential α/β phases) | Distribution/elimination phase separation |
| 004 | mAb PK cross-species transfer (lokivetmab → human) | Allometric scaling (BW^0.75 CL, BW^1.0 Vd) |
| 005 | Population PK Monte Carlo (1,000 virtual patients) | Lognormal IIV, CL-AUC correlation r = -0.92 |
| 006 | PBPK 5-tissue physiological compartments | Mass conservation, hepatic clearance, tissue Kp |

**Lineage**: Paper 12 veterinary→human bridge (Gonzales iPSC, Neubig drug discovery) → healthSpring human therapeutics.

### Track 2: Gut Microbiome and Colonization Resistance (Exp010–013)

Extends wetSpring's Anderson localization framework from soil to gut.

| Exp | Title | Key Result |
|-----|-------|-----------|
| 010 | Shannon/Simpson/Pielou/Chao1 diversity indices | Validated against SRA published data |
| 011 | Anderson localization in gut lattice (1D ξ) | Localization length predicts colonization resistance |
| 012 | C. difficile colonization resistance score | Composite: diversity + ξ + Firmicutes ratio |
| 013 | FMT microbiota transplant for rCDI | Engraftment fraction → diversity restoration via Bray-Curtis |

**Lineage**: Paper 01/06 Anderson QS framework → Paper 12 immunological Anderson → healthSpring gut colonization.

### Track 3: Biosignal Processing (Exp020–023)

Real-time physiological signal analysis on sovereign hardware.

| Exp | Title | Key Result |
|-----|-------|-----------|
| 020 | Pan-Tompkins QRS detection (ECG R-peak) | Bandpass + derivative + MWI + threshold |
| 021 | HRV metrics (SDNN, RMSSD, pNN50) | Time-domain HRV from R-peak intervals |
| 022 | PPG SpO2 R-value calibration | Beer-Lambert AC/DC ratio → SpO2 |
| 023 | Multi-channel fusion (ECG + PPG + EDA) | FusedHealthAssessment: HR + SpO2 + stress index |

**NPU target**: Pan-Tompkins is a streaming signal pipeline ideal for Akida AKD1000 (<1ms, microwatt).

### Track 4: Endocrinology — Testosterone PK and TRT Outcomes (Exp030–038)

Clinical claim verification pipeline: extracting quantifiable claims from Dr. Charles Mok's clinical reference and validating against published registry data.

| Exp | Title | Key Result |
|-----|-------|-----------|
| 030 | Testosterone PK: IM injection steady-state | Weekly vs biweekly, trough analysis |
| 031 | Testosterone PK: pellet depot (5-month) | Zero-order release, 10mg/lb dosing |
| 032 | Age-related testosterone decline | Harman 2001 BLSA: -1.6%/yr after 30 |
| 033 | TRT metabolic response: weight/BMI/waist | Saad 2013 registry (n=411) |
| 034 | TRT cardiovascular: lipids + CRP + BP | Sharma 2015 (VA, n=83,010) |
| 035 | TRT diabetes: HbA1c + insulin sensitivity | Kapoor 2006 RCT |
| 036 | Population TRT Monte Carlo (10K patients) | Lognormal IIV + age-adjusted decline |
| 037 | Testosterone-gut axis (cross-track 2×4) | Pielou evenness → Anderson ξ → metabolic response |
| 038 | HRV × TRT cardiovascular (cross-track D3) | SDNN improvement → composite cardiac risk |

**Novel contribution**: Exp037 bridges gut microbiome diversity with TRT metabolic outcomes via Anderson localization — a testable hypothesis for clinical investigation. Exp038 validates HRV as a surrogate endpoint for cardiovascular benefit of TRT.

### Validation Track (Exp040)

| Exp | Title | Key Result |
|-----|-------|-----------|
| 040 | barraCuda CPU parity (15 analytical contracts) | Hill, Bateman, allometric, Shannon, Simpson, population PK |

### CPU vs GPU Parity & Mixed Dispatch (Exp060–062)

| Exp | Title | Key Result |
|-----|-------|-----------|
| 060 | CPU vs GPU parity matrix (3 kernels × 3 scales) | 27/27 parity checks through toadStool Pipeline |
| 061 | Mixed hardware dispatch (NUCLEUS topology) | 22/22 dispatch route checks (CPU+GPU+NPU) |
| 062 | PCIe P2P transfer validation (Gen3/4/5) | 26/26 bandwidth and overhead checks |

### Clinical Translation (Exp063–064) — V9 NEW

| Exp | Title | Key Result |
|-----|-------|-----------|
| 063 | Patient-parameterized TRT scenarios (5 archetypes) | Per-person: 8 nodes + 8 edges, clinical mode preset, UiConfig |
| 064 | IPC push to petalTongue | Unix socket JSON-RPC, live scenario update without restart |

**Novel contribution**: Exp063 demonstrates the per-person translation pipeline — population models parameterized for an individual patient, rendered as a clinical scenario graph. This is the usable output of all upstream validation: the clinician sees a patient-specific trajectory, not a population average.

---

## Metrics

| Metric | Value |
|--------|-------|
| Experiments | 37 |
| Rust binary checks | 526+ |
| Rust unit tests | 221 (171 barracuda + 33 metalForge + 17 toadStool) |
| Cross-validation checks | 104 |
| GPU parity checks | 27/27 (Exp060) |
| GPU fused pipeline checks | 11/11 (Exp054) |
| Mixed dispatch checks | 22/22 (Exp061) |
| PCIe transfer checks | 26/26 (Exp062) |
| Patient archetypes | 5 (Exp063) |
| Unsafe blocks | 0 |
| Clippy warnings | 0 |

---

## GPU Pipeline (Tier 2) — LIVE

### WGSL Shaders (f64 precision)

| Shader | GpuOp | Pattern | Validated |
|--------|-------|---------|:---------:|
| `hill_dose_response_f64.wgsl` | HillSweep | Element-wise, power via f32 exp/log | Exp053 |
| `population_pk_f64.wgsl` | PopulationPkBatch | Embarrassingly parallel MC (u32 PRNG) | Exp053 |
| `diversity_f64.wgsl` | DiversityBatch | Workgroup-level reduction | Exp053 |

### Architecture

| Component | Purpose |
|-----------|---------|
| `GpuContext` | Persistent wgpu device/queue, eliminates per-dispatch init |
| `execute_fused()` | Unidirectional pipeline: upload → N compute passes → readback |
| `Pipeline::execute_gpu()` | toadStool dispatches stages via `GpuContext` |
| `Pipeline::execute_auto()` | metalForge routes per stage (GPU if element count > threshold) |

### Scaling (RTX 4070, release build)

| Operation | GPU Crossover | Peak Speedup | Peak Throughput |
|-----------|:------------:|:------------:|:---------------:|
| Hill dose-response | **100K** | 2.0x (5M) | 207 M/s |
| Population PK MC | **5M** | 1.15x (5M) | 365 M/s |
| Fused pipeline (overhead) | — | **31.7x** vs individual | — |

### Field Deployment Thesis

A single consumer GPU where people are — clinic laptop, Raspberry Pi + eGPU, edge node — handles population-scale health computations without cloud infrastructure. The same WGSL pipeline maps to TPU (Coral) and NPU (Akida) as hardware matures.

### metalForge NUCLEUS Atomics

Hierarchical compute topology: Tower (cluster) → Node (machine) → Nest (device). PCIe P2P DMA planning for GPU↔NPU bypass. 33 tests. `DispatchPlan` assigns stages to substrates with transfer planning.

### toadStool Pipeline

Stage-based compute pipeline: Generate → Transform (Hill, ExpDecay, Square) → Reduce (Sum, Mean, Max, Min, Variance) → Filter. CPU reference + GPU dispatch. 17 tests. `execute_auto()` routes per stage via metalForge.

---

## Per-Person Clinical Translation (V9)

The critical V9 addition: the pipeline from validated population models to individual patient scenarios.

### Pipeline

```
Published data → Computational model → Population validation
    → PatientTrtProfile (age, weight, T level, comorbidities)
        → trt_clinical_scenario() → 8-node graph + edges + channels + ranges
            → petalTongue clinical mode (motor commands: hide sidebars, skip awakening, fit view)
                → Clinician sees THIS patient's projected trajectory
```

### SAME DAVE Neuroanatomy (petalTongue Integration)

The SAME DAVE model (Sensory Afferent, Motor Efferent) provides self-aware control of the visualization system:

| Channel | Direction | healthSpring Use |
|---------|-----------|-----------------|
| Scenario load | Afferent | Patient scenario → graph topology |
| Mode preset | Efferent | `mode: "clinical"` → bundle of motor commands |
| Panel visibility | Efferent | `show_panels` → SetPanelVisibility motor commands |
| Awakening control | Efferent | `awakening_enabled: false` → skip startup animation |
| Zoom control | Efferent | `initial_zoom: "fit"` → FitToView motor command |
| IPC push | Afferent | JSON-RPC → scenario update without restart |

Classification nodes (analogous to nodes of Ranvier in Schwann cells) allow smart signal routing along unidirectional channels, enabling bidirectional system control through specialized afferent and efferent pathways.

---

## Cross-Paper Dependencies

```
Paper 01 (Anderson-QS) ──→ gut lattice model (Exp011, 037)
Paper 06 (No-Till)     ──→ Anderson framework for biological substrates
Paper 12 (Immunological Anderson) ──→ veterinary→human PK bridge (Exp004), allometric scaling
Paper 08 (NPU Edge IoT) ──→ biosignal NPU target (Exp020-023)
Paper 07 (Sovereign WDM) ──→ GPU dispatch methodology, metalForge architecture
```

---

## Reading Order

**Standalone**: Paper 13 is self-contained for anyone interested in computational pharmacology or clinical decision support.

**In context**: 12 (immunological Anderson, veterinary PK lineage) → 13 (human health applications) → 01 (Anderson framework)

**Biosignal focus**: 13 §Track 3 (sovereign biosignal) → 08 (NPU edge IoT) → 04 (sentinels)

**Microbiome focus**: 13 §Track 2 (gut Anderson) → 01 (Anderson-QS) → 06 (no-till Anderson) → 03 (bioag microbiome)

---

## Data Sources

All validation data derives from published, open-access sources:

- Harman 2001 (BLSA testosterone decline)
- Saad 2013/2016, Traish 2014 (TRT registries)
- Sharma 2015 (VA cardiovascular cohort)
- Kapoor 2006 (RCT diabetes)
- Kabashima 2020, Silverberg 2021 (mAb Phase III)
- Gabrielsson & Weiner (PBPK reference model)
- Kleiger 1987 (HRV mortality landmark study)
- SRA public 16S datasets for microbiome baselines

No proprietary clinical data is used. Mok clinical reference provides hypotheses; registry data provides validation.

---

**License**: AGPL-3.0-or-later
