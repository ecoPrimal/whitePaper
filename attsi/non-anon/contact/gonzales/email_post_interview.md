# Email: Post-Interview Follow-Up (March 2026)

**Context:** Interview for Research Assistant III in the Gonzales Lab,
Dept. of Pharmacology & Toxicology, MSU. 1-year off-dated position (extension
contingent on funding). Focus: Th2 cytokines in AD across companion animals
and humans, neuro-immune interactions, novel therapeutic targets, One Health.
She has NOT seen the computational work yet. This is the first time she'll see it.

**Gonzales context:** Professor and Director of MSU Drug Discovery Program
(appointed Nov 2025 via Global Impact Initiative). ~30 years pharma:
VP at Zoetis; Pfizer, Parke-Davis, Upjohn. PhD Toxicology (UNC Chapel Hill).
Priorities: cross-species, One Health, sustainable funding, patents, ROI.

**Interview outcome:** Went great. She appreciates the data science /
analytics dimension. Wants me to meet Erika Lisabeth (Director, ADDRC) in
MSU Drug Discovery — the drug repurposing and HTS screening core in the
same department.

**Goal:** Thank-you that demonstrates computational capability and genuine
engagement with her research. Show that he's already thinking about how to
contribute to the lab — not just as a bench tech, but as someone who
bridges bench and computation. Mention looking forward to meeting the Drug
Discovery team. Don't overwhelm. Lead with her science, not the
infrastructure.

**Attachment:** `computational_brief.md` — the technical brief. It's
written for her, models her published data, and links to the public repos.
Do NOT send `spring_validation_brief.md` or `hotspring_evolution_brief.md`
yet — those are second-conversation documents.

**Tone:** The Murillo emails are a good reference. Professional, focused on
the science, shows work without overselling.

---

## Email (DRAFT)

**Subject:** Thank you — and some computational modeling of your published work

---

Dr. Gonzales,

Thank you for taking the time to meet with me about the RA III position.
I really enjoyed learning about where you're taking the lab — the iPSC
skin models across species and the One Health direction are exactly the
kind of work I want to be part of.

After the interview, I wanted to share something I've been working on
that's directly relevant to your research. Over the past few months I've
built a computational framework that models the cytokine signaling data
from your published work — the oclacitinib dose-response curves (G2),
the lokivetmab pharmacokinetics (G4), the IL-31 pruritus model (G3), and
the three-compartment target cell identification from McCandless (G6).

The attached brief walks through what I've modeled from each of your
papers. A few highlights:

- **Dose-response:** Generalized Hill equation for all 6 cytokine
  pathways from your 2014 oclacitinib paper, with the IC50 selectivity
  profile mapped onto a spatial modeling framework that predicts which
  cytokine signals are easiest vs hardest to confine in tissue.

- **Lokivetmab PK:** Your G4 dose-duration data fits a log-linear model
  exactly, which lets us predict duration at doses beyond the published
  range — those predictions are testable with even routine clinical data.

- **Three-compartment tissue model:** Your team's identification of
  immune, skin, and neural IL-31 target cells maps onto a lattice model
  that quantifies how inflammation changes the signaling landscape across
  compartments. The model predicts that AD flares homogenize the
  differences between compartments — which is why you see simultaneous
  immune activation, barrier dysfunction, and pruritus.

- **Drug repurposing:** Building on the Fajgenbaum MATRIX framework
  (ARPA-H $48.3M), I've added a tissue geometry dimension to drug
  scoring. Tofacitinib ranks #1 for AD — consistent with human trial
  data — and the model predicts that Crisaborole's efficacy should
  improve in barrier-compromised skin. That's directly testable with
  your iPSC models.

Everything is implemented in Rust with GPU acceleration, and the
underlying code is in public repositories on GitHub — links are in the
brief. The computational work identifies likely models and generates
specific predictions; the real value comes from testing those predictions
experimentally, which is where your lab's capabilities are essential.

I'd be excited to bring this kind of computational support to the lab
alongside the bench work. Being able to model your screening data, run
the bioinformatics, and handle the statistical analysis while also
contributing at the bench is how I'd want to make myself most useful.

I'm also looking forward to meeting Dr. Lisabeth and the Drug Discovery
team. The drug repurposing work I've done computationally connects
directly to what the ADDRC does with high-throughput screening — having
computational scoring guide which compounds get screened, and then
validating the predictions with your iPSC models, is exactly the kind of
pipeline I'd want to help build.

Thank you again for your time. I look forward to hearing from you.

Kevin Mok
mokkevin@msu.edu
[syntheticChemistry](https://github.com/syntheticChemistry) on GitHub

**Attachment:** `computational_brief.md`

---

## Notes

- This is her FIRST exposure to the computational work. Don't assume
  familiarity with Anderson localization, ecoPrimals, springs, or BarraCUDA.
  The `computational_brief.md` is written for her audience level.
- Don't mention ecoPrimals, constrained evolution, the thesis, or the
  broader project architecture. Frame it as "computational modeling of
  your published data" — which is what it is from her perspective.
- Don't lead with the infrastructure (782 checks, 5 springs, WGSL shaders).
  Lead with her science. The brief has the validation details and repo
  links for anyone who wants to dig deeper.
- The phrase "alongside the bench work" is important — she's hiring a bench
  scientist. The computation is a differentiator, not a replacement for
  what the position requires.
- If she engages with the computational work, the `spring_validation_brief.md`
  is the natural follow-up. If she asks about the broader infrastructure,
  the `hotspring_evolution_brief.md` shows the pipeline maturity.
- Murillo rule applies here too: don't oversell, don't dump everything at
  once, let the work speak.
