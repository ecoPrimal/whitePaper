<!-- PII: Raw Discord capture. Contains Discord handles, opinions, and
     community governance discussions from ABG #general and DMs with rosīe.
     Internal reference only — do not redistribute.
     See ABG_ANALYSIS.md for structured summary. -->

## Server Governance Poll (May 6, 2026)

rosīe posted a poll: "Should ABG accept everyone, not just those with
skill / research experience in bioinformatics?"

Results (22 votes, multiple-select):
- Yes, everyone with full access: 1 vote (5%)
- Yes, everyone with #general only: 5 votes (23%)
- No, but loosen restrictions: 4 votes (18%)
- No, keep as-is: 10 votes (45%)
- No, tighten (must have papers): 2 votes (9%)

### Key community positions:

**Dennis**: BSc in CompSci or Bio minimum. In-progress degree fine. "People,
in general, are honest."

**Mark**: Lean towards admitting to #general with etiquette/guidelines.
Projects visible, contribution welcome.

**LinearParadox**: Curious people could join without project access or
proposing "completely out there" projects.

**HaRT [EPIC]**: "From the state of the subreddit, I think it'd quickly
become careers advice and homework help."

**bake3011**: Keep relatively close but loose. Already have Reddit for open
access. Current state is good. ~82 members, ~20-30 active daily.
Suggests holding off on growth advertising until 1-2 publications exist.
"If we tell people and have nothing to show, the hype die off fast."
Proposed beginner RNA-seq sample as onboarding exercise.

**Tamison**: Proposed read-only tier — newcomers can explore and learn,
interaction/access to incomplete work by admission. On board with no
changes for now, "fully open" as long-term goal.

**Jeremy**: Suggested read-only but can't see #project-proposals.

### Outcome: No changes for now. Consensus to focus on executing proposals
before expanding. Monthly proposal cycle instead of biweekly.

---

## Growth / Advertisement Discussion (May 8, 2026)

**bake3011**: Hold off on advertising until there are results to show.
"Once we have somethings then put a call out. It will be better for
server longevity." Suggested revisit in ~2 months.

**Jeremy**: Was about to post on biostars etc. Agreed to hold.

**HaRT**: "I think trying to spread too widely too early is not likely to
be much more productive. Already I think a lot of the people who have
joined are mostly curious."

### Outcome: No new advertising until at least 1 publication or progress
report exists.

---

## Proposal Review Process (May 8, 2026)

**rosīe**: Will review all project proposals. Contributors welcome to review
but cannot continue working on proposals they reviewed.

**bake3011** and **LinearParadox**: Volunteered as reviewers for next cycle.

**bake3011**: Only has capacity for 1 project this cycle. Suggests monthly
proposal cycle — biweekly is too rushed.

**rosīe**: Agreed on monthly cycle.

---

## Active Technical Discussions (May 7–8, 2026)

### ClinVar variant classification (swat_08 + LinearParadox + bake3011)

swat_08 training a pathogenicity classifier on ClinVar. Debated:
- Self-curated validation sets vs. holdout from ClinVar (bias concerns)
- LinearParadox: 1553 expert-reviewed missense variants, 2414 total 3-star+
- bake3011: Self-curated data carries unknown personal bias, will be
  flagged by reviewers. Recommended k-fold + 70/30 split.
- swat_08: Took all pathogenic + benign for training, tested on 50→100
  unseen samples (90%→98% acc). Now reclassifying 3-star+ VUS.
- LinearParadox: Hold out 30% of 3-star+ variants for testing.

### MD simulation of PfAAT1 drug resistance transporter (Mark + Alistaire)

Mark proposed modeling PfAAT1 mutations linked to chloroquine resistance
in P. falciparum. AF structure is poor (low confidence N-terminal).
Alistaire has molecular docking experience. LinearParadox flagged AF
structure quality. Community helping identify modeling approaches.

### TMS biomarker prediction (bake3011)

RNA-seq gene expression → TMS score prediction. Linear regression +
LASSO. Based on DOI:10.1038/ejhg.2014.281. Positioned as a
proof-of-concept for the group — small enough to finish, publishable.

---

## DM with rosīe — JupyterHub updates (May 7–8, 2026)

Tamison provided reviewer credentials:
- lab.primals.eco
- user: abgreviewer / pass: review
- Read-only early access for review of the hub
- Keep credentials private for now
- Per-user accounts coming in next couple days

rosīe shared JupyterHub link in server-updates (then removed per growth
discussion consensus).

Tamison reiterated credential tiers:
1. Full ABG member (individual credentials, shared workspace)
2. Read/download for public release (future)
3. Read-only for reviewers and PIs
