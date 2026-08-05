# Infectious Science — What Happens When Anyone Can Run This

**Status**: Strategic thesis | **Wave**: 156e | **Date**: Aug 5, 2026
**Context**: Post SU(N) generalization, pre arXiv submission
**Posture**: Opportunity, not outcome. Build quality. Let it spread.

---

## Thesis

ecoPrimals does not need adoption campaigns, enterprise sales, or institutional
partnerships to spread. It needs to work. If a physicist in Bogotá can download
a binary, point it at a $650 GPU, and reproduce 45 years of lattice gauge theory
results in an afternoon — the adoption takes care of itself.

The organism is not trying to replace Frontier. It is trying to make Frontier
optional for 90% of the physics that currently requires it.

---

## The Field Today

Lattice QCD is a $600M/year computational enterprise. The software stack:

| Framework | Language | GPU | Who | Dependency |
|-----------|----------|-----|-----|------------|
| MILC | C | CUDA (via QUDA) | US national labs | NVIDIA |
| Grid | C++14 | CUDA / HIP / SYCL | UK/US universities | NVIDIA primary |
| openQCD | C | CPU only | European collaborations | No GPU at all |
| QUDA | C++ | **CUDA** | Everyone's GPU layer | **Single vendor capture** |
| QDP-JIT | C++ | CUDA | JLab | NVIDIA |
| CL2QCD | C++ | OpenCL | Frankfurt — abandoned | Dead |

Every GPU-accelerated lattice simulation in the world routes through QUDA, which
is CUDA, which is NVIDIA. The entire field's GPU capability depends on one
company's proprietary API.

The hardware to play:

| Resource | Cost | Access |
|----------|------|--------|
| Leadership Computing Facility allocation | $0 (if approved) | 6-12 month proposal cycle, peer review, institutional affiliation required |
| NERSC allocation (USQCD) | $0 (if member) | US institution required, annual renewal |
| University HPC cluster | $50-500K/yr | Faculty appointment required |
| Cloud GPU (A100 spot) | ~$1.50/hr | Credit card, ~$13K/year for 24/7 |

A physics department in a developing country — or a motivated individual — cannot
participate. The floor to do GPU lattice QCD is institutional access plus NVIDIA
hardware plus a C/C++ codebase with decades of accumulated complexity.

---

## The Historical Achievement Ladder

What the field has accomplished, at what cost, and what we reproduce:

| Year | Achievement | Who | Hardware Cost | Lattice | ecoPrimals Equivalent |
|------|-------------|-----|---------------|---------|----------------------|
| 1980 | First numerical proof of confinement | Creutz (BNL) | ~$5M (CDC 7600) | 4⁴–8⁴ SU(2) | < 1 second on CPU |
| 1984 | First SU(3) quenched spectrum | Cray users | ~$10M | 8⁴–16⁴ | Minutes on CPU |
| 1993 | Quenched proton mass ±6% | GF11 (IBM) | ~$10M custom | 16³×32 | Hours on CPU |
| 1996 | Continuum-extrapolated spectrum | CP-PACS | **$50M dedicated** | 32³×64 | **RX 6950 XT has more FP64 FLOPS than their entire machine** |
| 2003 | First <1% QCD predictions | HPQCD+MILC | ~$10M/yr alloc | 20³×64 | Code path implemented |
| 2008 | Ab initio hadron masses (Science) | BMW | ~$100M (BlueGene) | 48³×96 | Our VRAM ceiling, not our compute ceiling |
| 2012 | QCD crossover temperature | HotQCD | ~$50M+/yr | 32³×8 | ~18 hours on one GPU card |
| 2014 | First consumer GPU lattice QCD | Wuppertal-Budapest | ~$5M (GTX Titans) | 48³×12 | CUDA-only. We do it vendor-agnostic. |
| 2024 | Sub-percent CKM, muon g-2 | FLAG/MILC/RBC | $600M+ (Frontier) | 96³×192 | Not our target. Frontier is real. |
| **2026** | **SU(N=2,3,4,5,6,8) on consumer GPUs** | **ecoPrimals** | **~$5K** | **16⁴ validated, 32⁴ target** | **This is us.** |

The volume we validated (16⁴) is where Cray supercomputers operated in the 1980s.
Our target (32⁴) is where CP-PACS and early BMW operated. We reach it on a desktop
that costs less than one month's electricity bill for those machines.

We are not at the frontier. We are at the **threshold of meaningful physics** — the
volume where continuum extrapolations begin, string tension is measurable, and
deconfinement transitions are resolvable. That threshold is where the field
produced its first important results. Making it universally accessible is the point.

---

## What ecoPrimals Provides That the Field Lacks

### 1. Vendor-Agnostic GPU Compute

WGSL shaders compile to Vulkan (NVIDIA, AMD, Intel) and Metal (Apple). Proven:
16⁴ SU(3) cross-vendor parity at 6 ppm between RTX 3090 and RX 6950 XT. Same
source code, different silicon, identical physics.

No CUDA. No HIP. No vendor SDK. WebGPU is a W3C standard backed by every
browser and GPU vendor. It is the one API nobody has incentive to kill.

### 2. Gauge Group Generality

One `GaugeGroup` trait. One `GenericLattice<G>`. SU(2) through SU(8) — same HMC,
same observables, same provenance. The large-N community (Lucini, Teper,
Gonzalez-Arroyo, Okawa) currently writes separate codes per gauge group. We
parameterize over the group and let the compiler monomorphize.

A theorist interested in SU(5) grand unification, SU(2) electroweak simulations,
or large-N universality changes one parameter. They do not write a new codebase.

### 3. Computational Provenance

BLAKE3 content-addressed configurations. Every cached config has a deterministic
hash derived from: gauge group, volume, β, seed, trajectory count, integrator.
The hash IS the identity. Reproduce the run, get the same hash. No trust required.

The field's current provenance (ILDG) is XML metadata attached to configurations
by human convention. There is no content-addressing. There is no cryptographic
verification. A configuration labeled "beta6.0_32x32x32x32_config.1000" is
trusted because the collaboration says so.

### 4. Rust Safety

The lattice QCD field has a quiet, persistent problem: buffer overruns, data races,
and memory corruption in C/C++ codes that produce physics results published in
Physical Review Letters. These bugs are usually silent — they don't crash, they
subtly bias results. The field deals with this through code review and redundant
computation, not through language-level guarantees.

Rust eliminates entire categories of these bugs at compile time. Thread safety
is structural, not conventional. The 652 library tests are not just physics
validation — they are proof that the code cannot data-race, double-free, or
buffer-overrun its way to a wrong answer.

---

## Deployment Surfaces — How It Spreads

The organism does not need to be installed in one way. It runs everywhere
the hardware exists, at every level of commitment.

### Tier 1: Single Binary, Single GPU

A physics student downloads `arxiv_thermalize_sun` and `arxiv_measure_battery`.
They have a gaming PC with an RX 7900 XT or an RTX 4070. They run:

```
SUN_GROUP=3 cargo run --release --bin arxiv_thermalize_sun
cargo run --release --bin arxiv_measure_battery
```

They reproduce SU(3) plaquette values at β=6.0 to <0.1% of published data.
They have their first lattice QCD result. Total cost: the GPU they already own.

### Tier 2: Lab Desktop, Multiple Groups

A research group buys a workstation ($5-10K). Dual GPU. They run the full
SU(N) thermalization grid, measure observables, produce Creutz ratios and
Polyakov loops. They have data for a paper. They did not write a grant
proposal for compute allocation. They did not wait 6 months.

### Tier 3: University Cluster

A department with 10-50 GPU nodes (common — most universities bought these
for ML) runs the same binaries across nodes. Content-addressed configs
federate naturally: node A thermalizes SU(3) 32⁴ β=6.0, node B thermalizes
β=6.2. Configs are BLAKE3-addressed. No central coordinator needed.

### Tier 4: Cloud Burst

A collaboration needs 100 configurations at 48⁴ for a systematic study.
They rent spot instances ($0.30-1.50/hr per GPU) for a weekend. The same
Rust binaries compile and run on cloud GPU instances. Content-addressed
results download to local CAS. No long-term cloud commitment.

### Tier 5: Full Ecosystem (strandGate Pattern)

The full primal stack: nestGate (CAS), sweetGrass (provenance braids),
bearDog (cryptographic signatures), songBird (mesh federation), biomeOS
(composition). Sovereign infrastructure on hardware you own. Data flows
between gates with content-addressing and provenance. This is what
strandGate runs today. It is not required for the physics to work — it
is what you build when you want the physics to be part of a larger
sovereign system.

### Each Tier Feeds the Next

A student at Tier 1 produces a config. Its BLAKE3 hash is deterministic.
If a lab at Tier 3 produces the same config, the hashes match. They know
they agree without communicating. If a cloud burst at Tier 4 produces a
large ensemble, a Tier 5 ecosystem can ingest those configs into its CAS
by hash alone.

The provenance system does not require the full ecosystem. But the full
ecosystem makes provenance automatic. Each tier of adoption makes the
next tier more valuable.

---

## What We Build Toward (Not What We Sell)

There is no sales motion. There is no adoption target. There is no
enterprise tier. The AGPL-3.0 license ensures the code stays open.
The sovereign infrastructure ensures no vendor can capture the platform.

What we do:

### Quality of Deployment

Every binary must produce correct physics. Every measurement must match
published literature within stated tolerances. Every provenance chain must
be cryptographically verifiable. The quality of the deployment is the
adoption strategy.

If the results are wrong, nothing else matters. If the results are right,
adoption is a consequence.

### Quality of Publication

The arXiv paper must meet the standard of the field. The reviewer rubric
(42 items, 12 MUST-fix) exists because we hold ourselves to the same
standard as a MILC or BMW publication. Jackknife errors. Continuum
extrapolation. Published comparison points with citations. Proper LaTeX.

The paper is not marketing. It is a peer-reviewed physics result that
happens to demonstrate what consumer hardware can do.

### Quality of Code

The codebase must be readable, tested, and maintainable by someone who
is not us. The GaugeGroup trait is documented. The generic lattice has
14 unit tests. The measurement battery outputs JSON that any analysis
tool can consume. A physicist who reads the code should understand the
physics, not fight the infrastructure.

### Quality of Provenance

Every computation must be reproducible. Same code + same seed + same
parameters = same BLAKE3 hash. This is not a feature — it is a
constraint. If a result cannot be independently verified by re-running,
it is not a result.

---

## The Infectious Property

A biological organism spreads when three conditions are met:
1. It can survive in the new host (runs on available hardware)
2. It provides benefit to the host (produces correct, publishable physics)
3. It transmits efficiently (open source, single-binary deployment, no dependencies)

ecoPrimals satisfies all three. The organism does not need anyone's permission
to run. It does not need institutional approval. It does not need a vendor
relationship. It needs a GPU and a physicist with a question.

The lattice QCD field has ~2,000 active researchers worldwide. Perhaps 500
have convenient access to GPU computing. The other 1,500 — at smaller
universities, in developing countries, between grants, early in their
careers — currently cannot do GPU lattice physics. They are the hosts
waiting for an organism that can run on what they have.

If the deployment quality is high enough, transmission is automatic.

---

## What We Do Not Do

- We do not claim to replace exascale machines for frontier physics
- We do not claim consumer GPUs match HPC for 96³×192 ensembles
- We do not claim our results are better than MILC or BMW
- We do not criticize existing frameworks — they work, and they produced
  the results we validate against
- We do not evangelize — the paper and the code speak for themselves

We claim that meaningful lattice gauge theory — the kind that produced
important physics results throughout the 1980s, 1990s, and 2000s — is
now accessible to anyone with consumer hardware and an internet connection
to download the source code.

The opportunity is not that we win. The opportunity is that the floor
disappears and everyone can play.

---

*subGen Wave 156e — Infectious Science. Opportunity, not outcome. Quality
of deployment is the adoption strategy. The organism runs at every tier
from a single GPU to a sovereign ecosystem. Each tier feeds the next.
Provenance is structural, not conventional. The AGPL ensures the code
stays open. The physics ensures the code is worth running.*
