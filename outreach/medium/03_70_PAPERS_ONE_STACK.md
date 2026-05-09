# 70 Papers, One Stack

*Reproducing published science across eight domains on consumer hardware — with cryptographic provenance*

**By**: attsi | ecoPrimal
**Status**: Draft — evolving document
**Published**: [pending]

---

There is a specific moment in computational science where trust breaks.

It happens when someone downloads a published dataset, writes a pipeline to
reproduce a result, runs it on different hardware than the original authors
used — and gets the same number.

That moment is unreasonably rare. Not because the science is bad, but because
the infrastructure makes reproduction unnecessarily hard. The original code
has undocumented dependencies. The dataset has been updated since publication.
The GPU gives different floating-point rounding. The version of Python has
changed. The specific conda environment the authors used is a tarball on a
grad student's decommissioned workstation.

We've spent two years trying to make that moment routine. Over 70 published
papers across eight scientific domains, reproduced from scratch on consumer
hardware, with every computation cryptographically traced from raw data to
final result.

This is what the stack looks like.

---

## The Domains

Eight validation frameworks — called "springs" — each covering a scientific
domain. Each spring is a standalone Rust binary with its own test suite, its
own validation experiments, and its own set of reproduced published results.

**wetSpring** — Microbiology, metagenomics, environmental genomics. 1,902+
tests, 379 experiments, 5,700+ checks. Reproductions include 16S rRNA
pipelines, quorum sensing gene quantification across 170 metagenomes
(299,000+ checks on a single dataset), Rika Anderson's deep-sea vent
metagenomics (6 papers), and Waters' quorum sensing lineage (7 papers). This
is the most mature spring — it started because the author's background is
bench microbiology.

**hotSpring** — Plasma physics, warm dense matter, lattice QCD. 990+ tests,
176 experiments. Murillo's Yukawa one-component plasma (5 papers reproduced,
195/195 checks). Bazavov's SU(3) Wilson gauge lattice QCD (12/12 target
values). Abelian Higgs model (17/17). Dynamical QCD with RHMC rational
approximation on consumer GPUs — computations that typically run on
institutional HPC clusters.

**airSpring** — Agricultural hydrology, precision irrigation, environmental
monitoring. 2,631+ checks, 57 papers. FAO-56 Penman-Monteith
evapotranspiration validated across 100 Michigan weather stations using five
independent methods (Hargreaves-Samani, Makkink, Turc, Hamon, Priestley-Taylor).
Dong et al. precision irrigation soil moisture models.

**groundSpring** — Measurement science, uncertainty quantification, error
propagation. 236+ checks, 21 papers. The cross-cutting spring: validates the
statistical foundations that the other springs depend on. Error propagation
through the FAO-56 chain. Uncertainty bounds on Anderson localization
parameters. Monte Carlo convergence verification.

**neuralSpring** — Machine learning, surrogate models, AI-assisted science.
3,200+ checks, 25+ papers. Dolson's digital evolution experiments (46/46).
Neural network surrogates for expensive physics computations. Edge inference
on BrainChip Akida neuromorphic hardware (physical NPU, not simulation).

**healthSpring** — Human health, pharmacometrics, clinical science. 940+
tests, 83 experiments. Mok's testosterone replacement pharmacokinetics
(233/233 checks), population PK modeling, gut-brain axis, heart rate
variability. 9 clinical tracks with 113/113 cross-validation.

**ludoSpring** — Game science, HCI, interactive systems. 791+ tests, 75
experiments. Fitts' Law, Hick's Law, flow state models. This spring exists
because game design is applied cognitive science, and the same measurement
rigor that validates a drug PK model should validate a player interaction
model.

**primalSpring** — Master coordination, integration testing. 404+ tests.
Validates that the springs compose correctly, that inter-service communication
works, and that the full deployment graph holds under load.

Total: **12,510+ quantitative checks**. **70+ published papers reproduced**.
**27,000+ tests**. Built over approximately 69 days of active development.

---

## What "Reproduced" Means

Reproducing a paper is not running the authors' code and confirming it still
compiles. It is:

1. Reading the paper's methods section
2. Identifying the quantitative claims (specific numbers, with error bounds
   when reported)
3. Implementing the methodology independently, from the equations
4. Fetching the same input data (or generating synthetic data matching the
   paper's description)
5. Running the computation
6. Comparing the output to the published values
7. Determining whether the difference is within the reported uncertainty

When we say "Bazavov SU(3) Wilson gauge 12/12," we mean: we independently
implemented the lattice QCD computation described in Bazavov's paper, ran it
on a consumer RTX 4070 using DF64 double-float emulation through a Vulkan
compute pipeline, and obtained 12 out of 12 target values within the
published error bars.

When we say "FAO-56 across 100 stations," we mean: we independently
implemented the Penman-Monteith reference evapotranspiration equation from
FAO Irrigation and Drainage Paper 56 (Allen et al. 1998), fetched weather
data from 100 Michigan stations, computed ET₀ using five independent methods,
and verified cross-method agreement within known model tolerances.

The implementations are Rust. The science is published. The gap between them
is the reproduction.

---

## The Thread That Connects Everything

There is a mathematical phenomenon called Anderson localization that appears
in nearly every domain this project touches.

Philip Anderson described it in 1958: in disordered systems, wave propagation
can be exponentially suppressed. A wave entering a sufficiently disordered
medium doesn't propagate — it localizes. The disorder traps it.

This was originally about electron transport in doped semiconductors. But the
mathematics is universal. The same equations describe:

- **Microbial ecology**: quorum sensing signals in spatially heterogeneous
  biofilms exhibit localization-like behavior. The disorder is the
  heterogeneous extracellular matrix. The "wave" is the signaling molecule
  diffusion gradient.

- **Plasma physics**: wave propagation in warm dense matter shows
  Anderson-like localization when the plasma coupling parameter exceeds
  critical thresholds.

- **Immunology**: cytokine propagation through tissue can be modeled as
  wave transport through a disordered medium. Paper 12 in our baseCamp
  series frames this explicitly.

- **Lattice QCD**: confinement in gauge theories has deep structural
  parallels to Anderson localization in condensed matter.

- **Agricultural hydrology**: error propagation through the FAO-56 chain
  exhibits localization-length-like behavior — uncertainty doesn't spread
  uniformly but concentrates in specific parameter regimes.

This is not a metaphor stretched to fit. The mathematical formalism — transfer
matrices, Lyapunov exponents, localization lengths — applies identically
across these domains. Our groundSpring measurement framework computes
localization parameters (W_c = 16.26 ± 0.95 for the critical disorder
strength in 3D Anderson models) and then traces the same mathematics through
biological, physical, and agricultural systems.

The eight springs are not eight unrelated science projects. They are eight
views of a connected mathematical landscape, validated independently,
cross-linked through a shared formalism.

---

## Provenance: The Geological Record

Every computation in this system produces a cryptographic trace.

**Content addressing** — Raw data, intermediate results, and final outputs are
hashed with BLAKE3 at creation time. The hash is the identifier. If the data
changes by a single bit, the hash changes. There is no "version 2" of a
dataset — there is a different dataset with a different hash.

**DAG tracking** (rhizoCrypt) — Each computation records its inputs and
outputs as nodes in a directed acyclic graph. The DAG is a Merkle structure:
every node's integrity is verifiable from its children's hashes. You can
trace any result backward through the full chain of computations that
produced it.

**Permanent ledger** (loamSpine) — DAG entries are committed to an
append-only ledger, Ed25519-signed by the node that produced them. The
ledger is permanent. Entries cannot be edited or deleted. The cryptographic
chain means any tampering is detectable.

**Attribution braids** (sweetGrass) — Every computation carries attribution
metadata: who provided the data, who wrote the pipeline, who ran it, who
reviewed the result. Attribution follows W3C PROV conventions and is
cryptographically bound to the computation.

The metaphor we use internally is geological. Each validated computation is a
sedimentary layer. Over time, layers accumulate into a stratigraphic record.
When the same result is reproduced by different pipelines, different
hardware, different springs, the layers compress — metamorphic confidence.
Cross-spring overlap (Anderson localization appearing in wetSpring, hotSpring,
airSpring, and groundSpring) creates fold patterns that increase confidence
beyond what any single reproduction provides.

This is not blockchain. There are no tokens, no consensus mechanisms, no
distributed ledger. It is a local cryptographic audit trail, run on sovereign
hardware, producing structured JSON reports that any auditor can verify
independently.

---

## darkforest: The System That Tests Itself

The security validator for this ecosystem is called darkforest. It is a single
Rust binary (939 KB) that runs 181 checks against the live system:

- **Pen tests** — Simulates three threat actors: an external attacker (no
  credentials, probing from outside), an authorized user (valid compute
  credentials, testing privilege escalation), and a restricted observer
  (minimal access, testing lateral movement). Each actor attempts specific
  attack patterns against all 13 services.

- **Protocol fuzzing** — Generates malformed inputs for every service's
  JSON-RPC and BTSP endpoints. Tests boundary conditions, oversized payloads,
  invalid authentication tokens, type confusion, and deserialization edge
  cases.

- **Crypto strength** — Validates cookie entropy, shadow hash algorithms,
  token tamper resistance, cipher negotiation, TLS certificate chain, file
  permission enforcement, and key rotation hygiene.

Latest run: **175 PASS, 0 FAIL, 6 DARK_FOREST** (informational findings — no
exploitable vulnerabilities). The DARK_FOREST classifications are expected
conditions that are noted for visibility: Cloudflare's TLS termination (not
our cert), systemd service presence checks (informational), and similar
environmental observations.

darkforest tests the system that tests the science. The science validates
published results. The provenance chain validates the science. darkforest
validates the provenance chain, the services, and the security boundaries.
It is turtles, but each turtle is cryptographically signed.

---

## What This Proves and What It Doesn't

This project does not prove that our reproductions are correct. It proves that
they are *verifiable*. Every input is content-addressed. Every computation is
DAG-tracked. Every result is attributed and ledger-committed. If we got a
number wrong, the provenance chain tells you exactly where the error entered
and what it affected.

The 70+ reproductions are evidence that the methodology works across domains.
But the real contribution is the infrastructure: a system where reproducing a
published paper is a routine operation rather than a heroic effort. Fetch the
data. Run the pipeline. Compare the numbers. Record the provenance. Move on.

Reproducibility is not a virtue. It is a minimum standard. The question is
whether the infrastructure makes meeting that standard easy or hard. We built
the infrastructure that makes it easy, and then proved it works across plasma
physics, microbiology, agricultural science, drug discovery, game design,
clinical pharmacology, machine learning, and fundamental mathematics.

The repos are public. The provenance is transparent. The science is published.
Run it yourself.

---

## Links

- **Deployment**: github.com/sporeGarden/projectNUCLEUS
- **All services**: github.com/ecoPrimals
- **Scientific domains**: github.com/sporeGarden/foundation
- **Live system**: lab.primals.eco
- **License**: AGPL-3.0-or-later
