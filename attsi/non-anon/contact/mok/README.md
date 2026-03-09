# Dr. Charles Mok — Contact & Work Log

**Position:** Founder / Medical Director, Allure Medical (Shelby Township, MI)
**Background:** Emergency Medicine (~10 years) → Vascular / Laser Vein Treatment → Cosmetic Surgery → TRT / Hormone Optimization
**Book:** *If Your Testosterone Is Low, You're Gonna Get Fat* (Allure Medical Publishing, 2018, 196 pages)
**Domain:** Testosterone replacement therapy, cosmetic surgery, vascular (endovenous laser ablation), anti-aging medicine

---

## Clinical Philosophy

"Fix the underlying problem, don't manage symptoms."

This runs through every branch of his career:

- **ER → Vascular:** Endovenous laser ablation kills varicose veins in place — the vein reabsorbs, blood reroutes through healthy vessels. Compare to vein stripping: general anesthesia, surgical wound, compression stockings, weeks of recovery. Laser: local anesthetic, walk out same day. Massively better outcomes. The economics follow the medicine — higher throughput, lower complication rates, happier patients.
- **Cosmetic surgery:** Breast augmentation on conscious patients. Outpatient procedures that traditionally require general anesthesia and extended recovery. Reduces risk, reduces cost, increases patient control.
- **TRT:** Low testosterone is a treatable root cause behind weight gain, metabolic syndrome, cardiovascular risk, cognitive decline, and loss of quality of life. Don't manage obesity, don't manage diabetes symptoms — normalize the hormone and the downstream metrics improve. His book aggregates ~200 published studies supporting this position.

The pattern: identify the root cause, apply the most direct intervention, minimize recovery, measure outcomes.

---

## ecoPrimals Connection — Sub-Thesis 04 (Paper 13, Track 4: Endocrinology)

His book is the primary driver for healthSpring's Track 4. The "claim verification pipeline" extracts quantifiable claims from the book's 11 chapters, maps them to the ~200 cited primary sources, and builds computational models that validate each claim against published data.

**9 experiments validated: Exp030–038**
**Total checks: 96 Python + 86 Rust binary + 51 lib unit tests = 233**

| Exp | Title | Book Chapter | Primary Source | Python | Rust |
|-----|-------|:------------:|----------------|:------:|:----:|
| 030 | IM injection PK: weekly vs biweekly steady-state | Ch. 11 | Ross 2004, Shoskes 2016 | 12 | 11 |
| 031 | Pellet depot PK: 5-month sustained release | Ch. 11 | Cavender 2009, Testopel PI | 10 | 10 |
| 032 | Age-related testosterone decline | Ch. 3 | Harman 2001 (BLSA, n=890), Feldman 2002 (MMAS, n=1,709) | 10 | 8 |
| 033 | TRT metabolic response: weight/BMI/waist | Ch. 4 | Saad 2013 (n=411, 5yr, mean -16kg) | 10 | 7 |
| 034 | TRT cardiovascular: lipids + CRP + BP | Ch. 6 | Sharma 2015 (VA, n=83,010, HR=0.44) | 10 | 10 |
| 035 | TRT diabetes: HbA1c + insulin sensitivity | Ch. 5 | Kapoor 2006 (RCT), Dhindsa 2016 | 10 | 10 |
| 036 | Population TRT Monte Carlo (10K virtual patients) | Ch. 11 | Population PK simulation | 12 | 10 |
| 037 | Testosterone–gut axis (cross-track D1/D2) | Novel | Pielou evenness → Anderson disorder → metabolic response | 12 | 10 |
| 038 | HRV × TRT cardiovascular (cross-track D3) | Novel | Kleiger 1987 (HRV + cardiac mortality) | 10 | 10 |

### Cross-Track Hypotheses (Novel Predictions)

| # | Hypothesis | Clinical Translation |
|---|-----------|---------------------|
| D1 | Gut microbiome diversity predicts TRT metabolic response | Patients with healthier gut flora lose more weight on TRT |
| D2 | Anderson gut confinement correlates with metabolic syndrome | Gut microbiome disruption (e.g., from antibiotics, poor diet) reduces TRT effectiveness |
| D3 | HRV improvement tracks TRT cardiovascular benefit | Heart rate variability is a biomarker for whether TRT is improving cardiac health |
| D4 | Population PK with microbiome covariate | Combine patient variation + gut health to predict who responds best |

---

## Relationship

**Father.**

This shapes the communication strategy fundamentally. The goal is not to land a job, secure a reviewer, or propose a collaboration in the academic sense. The goal is to bridge understanding — to translate what the computational work means in terms he can engage with as a clinician.

The challenge: his son's primary collaboration medium is AI-assisted semantic conversation. His primary medium is clinical practice and patient interaction. The output encoding must change to match his intake channel. See `translation_guide.md` (personal, not sendable) for the practical framework.

---

## Book Structure

| Ch | Title | Key Quantifiable Claims |
|----|-------|------------------------|
| 1 | How the FDA Changed Everything | TRT prescription rates, FDA BRUDAC 2014 rule change |
| 2 | What the FDA Doesn't Want You to Know | Flawed study methodology (Vigen 2013, Finkle 2014) |
| 3 | How to Diagnose Low T | Threshold levels (280/200 ng/dL), free T vs total T |
| 4 | T and Weight Gain | TRT → sustained weight loss, Saad 2013/2016 registries |
| 5 | T and Type 2 Diabetes | TRT → HbA1c reduction, insulin sensitivity |
| 6 | T and Cardiovascular Disease | TRT → reduced MI/stroke, lipid/CRP/BP improvement |
| 7 | T and Urinary Tract | TRT and BPH/LUTS improvement |
| 8 | T and Musculoskeletal | Bone density, muscle mass, sarcopenia |
| 9 | T and Sexual Function | IIEF scores, libido, ED improvement |
| 10 | T and Mood/Brain | Depression scores, cognitive function |
| 11 | Treating Low T | Pellet/injection/gel PK, dosing, steady-state |

---

## Documents

| File | Purpose | Audience |
|------|---------|:--------:|
| `clinical_brief.md` | **Sendable** — validates his book's claims in clinical language. Zero programming terms. | Him |
| `practice_brief.md` | **Sendable** — what the computational validation means for his practice (stratification, dosing, regulatory, data opportunity). | Him (business side) |
| `translation_guide.md` | **Personal** — maps technical concepts to clinical equivalents. Conversation starters. Not for sending. | Kevin |
| `mokTestosterone.pdf` | Source: the book itself (PDF). | Reference |

---

## Interaction Log

| Date | Type | Notes |
|------|------|-------|
| 2018 | Book published | *If Your Testosterone Is Low, You're Gonna Get Fat* (Allure Medical Publishing, 196 pages) |
| March 2026 | healthSpring validation | Sub-Thesis 04 complete: 9 experiments (Exp030–038), 233 checks, all passing |
| March 2026 | Contact package created | Clinical brief, practice brief, translation guide drafted |
