# Follow-Up Email — Geoffrey Huntley — May 2026

**To:** ghuntley@ghuntley.com
**From:** ecoPrimal@pm.me
**Subject:** Re: From Groundhog to Squirrel — the ecosystem survived its own extinction event

---

## Email (DRAFT)

Geoffrey,

Sent you a cold email in March about Squirrel and how your /stdlib thesis became a sovereign AI coordination primal. No idea if it landed or got buried — either way, the project has crossed a threshold since then that I think you'd find interesting.

In March, the ecosystem was pre-primordial — proving things worked. Since then it went through what we call the primordial extinction: a stadial gate where every primal had to simultaneously meet a common survival threshold (async-trait eliminated, dependency bans, Edition 2024, capability wire standard, BTSP encryption) or die. The constrained evolution framework I described in the first email — Lenski's LTEE mapped onto AI-assisted code generation — now has a concrete instance at ecosystem scale. Thirteen primals passed. Eight springs completed the transition. Showcases that couldn't adapt got fossilized. What survived is running on five physical gates.

The ecosystem is post-primordial. Let me walk through what that actually looks like.

### Sovereign Compute

The stack runs math on GPUs without CUDA. Three primals compose:

- **coralReef** — a sovereign GPU shader compiler. It takes WGSL (WebGPU Shading Language) and compiles to native GPU binaries. NVIDIA, AMD, Intel, Apple Silicon. No vendor SDK. No CUDA toolkit. No ROCm. Pure Rust, naga IR, direct driver interface.
- **barraCuda** — the math engine. 952 WGSL shaders, 74K lines of GPU compute. Molecular dynamics, lattice QCD, linear algebra, statistics, bioinformatics HMMs, pharmacometrics, ML ops. All in DF64 (double-float emulated f64 from FP32 cores) — 14-digit precision on consumer GPUs that don't have native f64.
- **toadStool** — hardware management. Discovers CPU, GPU, NPU at runtime. Dispatches workloads. Manages VFIO passthrough. Pure Rust, zero C dependencies.

These compose into the Node Atomic — `toadStool` dispatches, `barraCuda` writes the math, `coralReef` compiles it. A consumer asks for `math.matmul` and the system figures out what hardware is available and runs it. No hardcoded GPU names. No vendor lock-in. The same shader runs on an RTX 4070 and an AMD RX 6950 XT and produces bit-identical physics.

That last part matters: the hotSpring guideStone artifact validated 59/59 physics checks across 5 substrates (Ubuntu+NVIDIA, Ubuntu+AMD, Alpine musl, aarch64 qemu) with 40/40 cross-substrate observables bit-identical. The physics does not depend on the instruction set, the C library, or the GPU vendor.

The practical output: lattice QCD at paper parity on a consumer GPU for $0.044 per run. A full deconfinement phase transition (32⁴ lattice, SU(3) gauge theory, HMC) on an RTX 3090. That's CERN-scale physics on basement hardware.

### Validation Layers

The science validation is a three-tier system:

1. **Python baselines** — reproduce published results using established tools (QIIME2, SciPy, R vegan/phyloseq). This is the ground truth.
2. **Rust implementation** — the same computation in pure Rust + barraCuda shaders. Must match Python at machine-epsilon precision.
3. **NUCLEUS composition** — the Rust computation dispatched through the full primal stack (toadStool, biomeOS orchestration, provenance trio). Must match standalone Rust.

Each layer is independently verifiable. The Rust matches the Python. The composition matches standalone Rust. Gaps are documented and flow upstream. 175+ papers reproduced across 8 domains: plasma physics, precision agriculture, metagenomics, pharmacometrics, spectral theory, ML, game science, measurement uncertainty.

On top of that, every result that flows through NUCLEUS carries a cryptographic provenance chain: BLAKE3 content hashes → rhizoCrypt DAG (computation graph) → loamSpine ledger (permanent record) → sweetGrass ed25519-witnessed braid (W3C PROV-O attribution). The provenance trio is partially operational — sweetGrass is live and producing real IPC braids, rhizoCrypt and loamSpine are wired but completing the transition from pseudo to signed.

### What You Can See on primals.eco

The site is the public verification surface. Here's what's there:

- **Lab page** (`/lab/`) — live results from a 13-primal NUCLEUS composition. 235+ structured science checks across 8 workloads, run on real hardware (i9-14900K, RTX 4070/3090, Akida NPU). Real NCBI data (11.9M paired-end reads) through both Python and Rust pipelines. Every result has a provenance chain.
- **guideStone page** (`/guidestone/`) — the verification class. Five properties: deterministic output, reference-traceable, self-verifying, environment-agnostic, tolerance-documented. First deployment artifact (hotSpring-guideStone-v0.7.0) validated across 5 substrates with 40/40 bit-identical observables.
- **NUCLEUS architecture** (`/architecture/nucleus-architecture/`) — how primals compose. The atomics ladder (Tower → Node → Nest → Full NUCLEUS), deploy graphs in TOML, capability-based routing via Neural API, Dark Forest zero-metadata-leakage discovery.
- **Science section** (`/science/`) — 175+ baseCamp papers organized by domain. Each is an executable reproduction, not a writeup.
- **Audience paths** — Faculty, Students, Hardware Builders, Compliance, Physicists. Each gets the entry point they need.
- **"Try It"** — two bash commands. `cargo test --workspace` for source, or `./hotspring validate` for the pre-built guideStone. Five minutes. Verify every claim on the page.
- **Public notebooks** — Jupyter notebooks that visualize the spring science. 16S pipeline validation, Python vs Rust vs GPU benchmarks, 63/63 paper reproductions, Anderson localization in soil biology.

All AGPL-3.0. All public. All runnable on commodity hardware.

### The Deployable Artifact

The methodology now produces artifacts that leave the development environment and prove themselves wherever they land:

**guideStone** (April 2026) — the first. 59/59 physics checks, self-leveling benchmark, USB/tarball/OCI. A PI plugs it in, runs one command, gets both "is the physics correct on this machine" and "how fast is this machine for this physics." No MILC build, no CUDA SDK, no configuration.

**lithoSpore** (May 2026) — the second. Domain-agnostic validation chassis. Built for LTEE biology, but the chassis doesn't care what science you put in it. Seven modules, 73 checks, musl-static Rust + Python baselines + cross-tier parity. Built in a week, deployed to a lab on USB.

**pseudoSpore** (May 2026) — the pattern spreading. A citizen science group (Reddit → Discord, real researchers) produced the first external instance: metadynamics free energy landscapes for enzyme conformational analysis. GROMACS+PLUMED Tier 0 control, with the evolution path mapped to sovereign Rust+barraCuda tiers. Same lithoSpore format, same validation pattern, different domain.

Every poster on every wall of every university campus is a static image. A student can't hand it to someone at a conference and let them touch the math. These artifacts are what happens when the Cursor-only methodology is pointed at that problem. The artifact improves by being used — field deploy, find the failure modes, document them, fix them. That's constrained evolution applied to scientific publishing.

### The Numbers

| March (pre-primordial) | May (post-primordial) |
|---|---|
| 14 primals, some with internal debt | 13 primals, zero debt, 13/13 BTSP Phase 3, 458 registered capability methods |
| 7 springs, validating independently | 8 springs, all eukaryotic UniBin, deploying NUCLEUS compositions on 5 gates |
| Squirrel: 22 crates, 4,819 tests | Squirrel: IPC-composed with live primals, Neural API routing |
| Springs: 15,334 checks | Springs: 20,695+ checks, 175+ papers, 952 WGSL shaders |
| No deployable artifacts | guideStone, lithoSpore, pseudoSpore — science that travels |
| No live provenance | sweetGrass live IPC braids, PROV-O JSON-LD exports, Merkle-rooted DAGs |
| No external users | Citizen science group, lab deployment, first external pseudoSpore |
| No public site | primals.eco — full verification surface with "Try It" |
| Methodology claim: Cursor-only produces infrastructure | Methodology evidence: Cursor-only infrastructure running physics on 5 gates, deployed to a lab, verified by external researchers |

Still just Cursor. Still no Claude Code, no multi-agent frameworks.

ecoPrimal
https://primals.eco
https://github.com/sporeGarden/lithoSpore

---

## Tone Notes

- Lead with acknowledgment that the first email may not have landed. No guilt, no pressure.
- The primordial extinction is the new hook. In March we described constrained evolution as a theory. Now the theory has an ecosystem-scale instance — and the ecosystem survived. Huntley cares about methodology evidence, not just methodology claims.
- The sovereign compute section speaks to developers: no CUDA, no vendor SDK, bit-identical across GPU vendors. This is the technical substance his audience respects.
- The validation layers section shows rigor: Python → Rust → NUCLEUS, each independently verifiable. Not just "tests pass" but "the same math at three different levels of composition."
- primals.eco is the verification surface for a developer. Two bash commands. Five minutes. That's his audience's language. Walk through what's actually on the site so he knows what to look for.
- The deployable artifact progression (guideStone → lithoSpore → pseudoSpore) shows the methodology producing tangible objects that leave the dev environment. The poster line is the emotional anchor.
- The expanded table makes the March→May trajectory concrete without re-explaining everything.
- Still no ask. The site and repos speak. If it's interesting, he'll decide what to do with it.

## Context: Pre-Primordial vs Post-Primordial

The first email was sent March 16, 2026 — during gen3, pre-primordial. The ecosystem was proving things worked: springs passing checks, primals accumulating tests, the methodology producing code.

The primordial extinction (documented in wateringHole/DOWNSTREAM_EVOLUTION_MAY2026.md and gen4/knome/THE_GEOLOGICAL_CONSTRAINT.md) is the stadial gate where every component had to meet a common threshold simultaneously. This is the LTEE parallel made real: Lenski's twelve populations under glucose constraint → ecoPrimals' thirteen primals under stadial constraint. The showcases that couldn't adapt were fossilized (wateringHole/SHOWCASE_FOSSILIZATION_STANDARD.md). What survived is the production stack.

Post-primordial state (from wateringHole/README.md, Wave 47):
- 13/13 primals zero internal debt
- 12/12 announcing
- 13/13 BTSP Phase 3
- 8/8 springs eukaryotic UniBin
- 5 gates deploying NUCLEUS compositions on LAN
- 458 primalSpring methods, 784 tests
- primals.eco live (sporePrint)
- lithoSpore deployed (4 USB drives, Barrick Lab)
- pseudoSpore pattern extending (CAZyme FEL for ABG)
- sweetGrass live provenance braids
