# Constrained Evolution: Environmental Pressure, Sovereign Computing, and the Convergence of Biological and Computational Systems

## PhD Thesis — Working Draft

**Author**: Kevin Mok  
**Degrees**: BS Microbiology (Michigan State University, 2018), MS Data Science (Michigan State University, 4.0, 2025)  
**Status**: Actively evolving — chapters at varying levels of completeness  
**License**: AGPL-3.0  
**Last Updated**: February 2026

---

## Thesis Statement

Strategic environmental constraints — in both biological and computational systems — do not merely accelerate convergence to known solutions. They reshape fitness landscapes, driving specialization toward constraint-specific optima through independent evolutionary trajectories. This principle, observed in thermophilic adaptation, controlled laboratory evolution, natural population genomics, and AI-assisted software development within a strong type system, constitutes a general theory of constrained evolution applicable across domains.

This thesis presents the theory, the computational system built under its principles (757,000 lines of Rust, 914 WGSL shaders, 104,000+ tests across 11 primals), and the empirical scientific validation proving the system computes real physics, biology, chemistry, and mathematics correctly (11,161+ quantitative checks across 70+ papers in 8 scientific domains in ~69 days).

---

## Structure

### Part I — Foundations

| Chapter | Title | Status |
|---------|-------|--------|
| 00 | [Front Matter](00_front_matter.md) | Draft |
| 01 | [Introduction](01_introduction.md) | Draft |
| 02 | [Literature Review](02_literature_review.md) | Draft |

### Part II — Theory

| Chapter | Title | Status |
|---------|-------|--------|
| 03 | [Theoretical Framework: Constrained Evolution](03_theoretical_framework.md) | Draft |
| 04 | [Accept and Generate — Nature's Strategy for Hard Problems](04_pnp_enzyme.md) | Draft |

### Part III — The System

| Chapter | Title | Status |
|---------|-------|--------|
| 05 | [System Architecture: Sovereign Scientific Computing](05_system_architecture.md) | Draft (data populated) |
| 06 | [BarraCUDA: Vendor-Agnostic GPU Compute](06_barracuda.md) | Draft (data populated) |

### Part IV — Experimental Validation

| Chapter | Title | Status |
|---------|-------|--------|
| 07 | [Experimental Methodology: The Spring Framework](07_experimental_methodology.md) | Draft |
| 08 | [Results: Computational Plasma Physics (hotSpring)](08_results_hotspring.md) | Draft (all tables populated) |
| 09 | [Results: Precision Agriculture (airSpring)](09_results_airspring.md) | Draft (all tables populated) |
| 10 | [Results: Life Science & Analytical Chemistry (wetSpring)](10_results_wetspring.md) | Draft (all tables populated) |
| 11 | [Results: Measurement Noise & Uncertainty (groundSpring)](11_results_groundspring.md) | Draft (all tables populated) |
| 12 | [Results: Machine Learning Primitives (neuralSpring)](12_results_neuralspring.md) | Draft (all tables populated) |

### Part V — Analysis

| Chapter | Title | Status |
|---------|-------|--------|
| 13 | [Quantitative Evidence for Constrained Evolution](13_quantitative_evidence.md) | Draft |
| 14 | [Biological Validation: The LTEE Sequencing Proposal](14_biological_validation.md) | Draft |

### Part VI — Synthesis

| Chapter | Title | Status |
|---------|-------|--------|
| 15 | [Discussion](15_discussion.md) | Draft |
| 16 | [Contributions, Future Work, and Conclusion](16_conclusion.md) | Draft |

### Back Matter

| Document | Title | Status |
|----------|-------|--------|
| A | [References](references.md) | Active |
| B | Appendix: Hardware Inventory | See `gen3/about/HARDWARE.md` |
| C | Appendix: AI Methodology Receipt | See `gen3/about/README.md` |
| D | Appendix: Spring Validation Data | See `gen3/SPRING_CATALOG.md` |

---

## Lineage

This thesis evolved from two prior documents in `gen3/`:

1. **`constrained_optimization_ai.md`** — The inoculum. First formulation of the constrained optimization idea, written during the ecoPrimals build. Rough metrics, illustrative analogies, no empirical validation.

2. **`CONSTRAINED_EVOLUTION_FORMAL.md`** — The working paper. Reframed from "optimization" to "evolution" after engaging with the biological literature. Added Lenski LTEE, Taq polymerase, Anderson population genomics, and the firefly/symbiotic composition arguments. Still a single document, not thesis-structured.

The thesis expands this into a full academic work with:
- Comprehensive literature review spanning evolutionary biology, type theory, evolutionary computation, and AI-assisted development
- Formal mathematical framework for the constrained evolution principle
- Five chapters of empirical results (one per spring domain)
- Proposed biological validation via LTEE frozen fossil record sequencing
- Honest discussion of limitations, including the AI-generation question

---

## How to Read This

**If you are a committee member**: Start with Chapter 01 (Introduction) for the thesis statement and scope, then Chapter 03 (Theoretical Framework) for the core argument, then Chapter 07 (Methodology) and any results chapter in your domain.

**If you are evaluating the science**: Start with Chapter 07 (Methodology) and the results chapter for your domain. Each spring is a self-contained validation study with public repositories you can clone and run.

**If you are evaluating the system**: Start with Chapter 05 (System Architecture) and Chapter 06 (BarraCUDA), then Chapter 13 (Quantitative Evidence) for the NTT→FFT constrained evolution case study.

**If you are interested in the biology**: Start with Chapter 03 (Theoretical Framework) sections on Taq, Lenski, and Anderson, then Chapter 14 (Biological Validation) for the LTEE sequencing proposal.

---

## A Note on AI-Assisted Writing

This thesis, like the system it describes, was produced with AI assistance (Cursor IDE, Claude). The methodology section (Chapter 07) documents this explicitly. The AI is the mutation operator; the author provides constraint and selection. The thesis is itself a product of the constrained evolution methodology it formalizes — an observation that is not a weakness but a feature of the argument.

The public spring repositories contain runnable experiments that verify every quantitative claim. The science stands independent of how it was written.
