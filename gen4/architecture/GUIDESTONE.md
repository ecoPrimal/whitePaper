# guideStone

**The Verification Class: How Computation Becomes Proof**

**Date**: March 31, 2026 (updated: April 3, 2026 — first deployment artifact)
**Status**: Ecosystem Standard — first gen4 architecture concept, first deployment artifact shipped
**Lineage**: gen3/about/SOVEREIGN_SCIENCE → gen3/atlasHugged/08_DISCOVERY_IS_LOCAL → gen4

---

## The Problem gen4 Creates

gen3 proved the infrastructure computes correctly. gen4 composes that
infrastructure into products where the consumer never sees a primal. The
consumer sees a game, a health dashboard, a field genomics kit. The
primals are the plumbing.

This creates a trust problem that gen3 did not have.

In gen3, the scientist runs the spring and reads the output. They see
41/41 checks pass. They see the energy drift at 0.000%. They see the
plaquettes match strong-coupling expansion. They are the verifier.

In gen4, the consumer runs a product built on primals. They see a
genomics report, a game session trace, a QCD gauge configuration. They
did not build the primals. They did not write the springs. They need to
know: **is this output real?**

guideStone answers that question.

---

## What guideStone Is

guideStone is a **verification class** — a quality grade for any ecoBin
in the ecosystem that certifies the artifact produces reproducible,
self-proving results.

It is not a binary type. The binary ladder (UniBin → ecoBin → genomeBin)
describes structure. It is not a deployment class. fieldMouse describes
where things run. guideStone describes **what the output means** — that
the computation's results are the proof of their own correctness.

Any ecoBin can be a guideStone. A spring, a primal, a composition, a
sporeGarden product. The classification is orthogonal:

```
Binary ladder (structure):     UniBin → ecoBin → genomeBin
Deployment class (where):      NUCLEUS → Niche → fieldMouse
Verification class (rigor):    guideStone
```

A hotSpring guideStone is an ecoBin that produces MILC-compatible ILDG
gauge configurations with named tolerances, paper-traceable observables,
and self-verifying checksums. A bearDog guideStone is a reference
edition with fully open cryptographic internals so a third party can
validate what happens when they create their own ephemeral seed. An
esotericWebb guideStone is a build whose provenance pipeline produces
verifiable creative NFTs traceable through the full anchoring chain.

The guideStone is not the product. It is what the product carries when
its output needs to stand on its own.

---

## Why "guideStone"

The name comes from two roots in the ecosystem's vocabulary.

**Guide** — the artifact points toward truth. Not by argument or
authority, but by being the thing itself. A guideStone does not claim
the lattice QCD observable is correct. It produces the observable, and
anyone with the same binary on any hardware gets the same number. The
guide is the computation. The stone is the result.

**Stone** — the substrate is real and unchanging. Discovery Is Local
(atlasHugged/08) established that mathematical and physical structure
exists independent of the discoverer. The wolf was always falling.
Calculus was always the inverse of differentiation. The gauge
configuration's plaquette value is a property of the mathematical
substrate, not of the person who computed it. guideStone names that
relationship: a living computation (the guide) touching an invariant
substrate (the stone).

The companion concept is **guidePost** — the planned repository for
the philosophical and ethical layer (atlasHugged, Sovereign Science,
K-NOME). guidePost points the way in human terms. guideStone is the
demonstrable proof in computational terms. One is the argument; the
other is the artifact.

---

## The Sovereign Science Connection

Sovereign Science (gen3/about/SOVEREIGN_SCIENCE) established the
principle: reality owns itself. The energy drift is 0.000% or it isn't.
No reviewer changes what the code outputs.

guideStone is how that principle scales to gen4.

In gen3, sovereignty was implicit — a scientist runs the spring and
checks the output against the paper. The scientist is the validator.
In gen4, the primals are invisible. The consumer sees a product. The
guideStone certification means: **this product's output is self-proving
in the same way the spring's output was self-proving.** The sovereignty
transfers through the composition layer.

This is the critical distinction between guideStone and conventional
software quality metrics. Code coverage, linting, CI/CD — those measure
the code. guideStone measures the **output**. The output is the science.
The science is the proof. The proof does not require trust in the
producer.

---

## What Makes Something a guideStone

### The Five Properties

A guideStone-certified artifact satisfies five properties. Each is
necessary. Together they are sufficient.

**1. Deterministic Output**

Same input, same binary, any hardware → same output within named
tolerances. "Works on my machine" is a disqualifying statement. The
binary detects its substrate (CPU, GPU, memory) at runtime and adapts
its execution path, but the mathematical result is invariant.

This does not mean bitwise identical. Floating-point arithmetic on
different architectures produces different rounding. guideStone requires
that every deviation from exact is bounded by a named tolerance with a
derivation — not a magic number chosen to make a test pass, but a bound
derived from the mathematics of the computation.

**2. Reference-Traceable**

Every numeric claim in the output traces to a source: a published paper,
a mathematical proof, a physical constant, or a standard (ILDG, MILC,
FAO-56, DADA2). The guideStone does not produce numbers that float in
space. It produces numbers that connect to the substrate — the pre-
existing mathematical and physical structure that Discovery Is Local
describes.

**3. Self-Verifying**

The artifact carries its own integrity. CHECKSUMS validated before
execution. CRC or hash on data payloads. Merkle roots when the
provenance trio is wired. The consumer does not need to trust the
transfer channel. The artifact proves it arrived intact.

**4. Environment-Agnostic**

No hardcoded paths. No "install X first." No platform assumptions.
The artifact is an ecoBin — Pure Rust, static musl, cross-arch — and
it runs wherever the binary runs. The External Validation Artifact
Standard (wateringHole) already requires this for spring artifacts.
guideStone extends the same requirement to any ecoBin carrying
verifiable output.

**5. Tolerance-Documented**

No magic numbers. Every threshold, every epsilon, every convergence
criterion has a derivation. The derivation lives in the output metadata,
not in a comment buried in the source.

```json
{
  "name": "gradient_flow_w7_8x8x8x8",
  "measured": 2.08,
  "threshold": 1.5,
  "comparison": "greater_than",
  "tolerance_justification": "finite-size suppressed from nominal 3; >1.5 confirms correct order",
  "paper": "Bazavov & Chuna, arXiv:2101.05320"
}
```

The justification is the proof. Not "we chose 1.5 because the test
passes" but "the theoretical order is 3, finite-size effects suppress
this on an 8^4 lattice, >1.5 confirms the correct convergence regime."
A physicist reads the justification and knows whether the tolerance is
physically meaningful.

---

## guideStone in Practice

### Spring guideStone: hotSpring Chuna Engine

The Chuna Engine is a composition of six binaries (`chuna_generate`,
`chuna_flow`, `chuna_measure`, `chuna_convert`, `chuna_benchmark_flow`,
`chuna_matrix`) that produce MILC-compatible lattice QCD data. Its
guideStone properties:

| Property | How |
|----------|-----|
| Deterministic | Same beta, same lattice size, same seed → same plaquette, same Polyakov loop within named tolerance |
| Reference-traceable | Every observable traces to Bazavov/Chuna papers. ILDG metadata follows QCDml 2.0 schema |
| Self-verifying | ILDG CRC on gauge configurations. SHA-256 checksums on the artifact directory |
| Environment-agnostic | Runs CPU-only or GPU. Detects hardware at runtime. Static musl binary |
| Tolerance-documented | Every convergence criterion derived from finite-size scaling, not from tuning |

The Chuna Engine guideStone is what TC Chuna carries to LANL. Bazavov's
group receives gauge configurations with full QCDml provenance. The
configurations are reproducible — same binary, same parameters, same
result. The guideStone is the bridge between sovereign home-cluster
computation and institutional HPC consumption.

### Primal guideStone: bearDog Reference Edition

bearDog has 14,201 tests. But a guideStone edition is more than passing
tests. It is the **reference implementation** — the pinned version where
every cryptographic primitive has its output validated against known test
vectors from standards bodies (NIST, RFC, IETF).

A bearDog guideStone means: when someone creates their own ephemeral
seed, they can trace every step — key derivation, entropy mixing, Ed25519
signing — against the reference edition's documented outputs. The
cryptography is not a black box. The reference edition opens it.

This matters for gen4 products. esotericWebb's `PrimalBridge` calls
`crypto.sign` and trusts the result. The guideStone edition of bearDog
is what makes that trust auditable by anyone, not just the developer.

### Composition guideStone: helixVision Genomics

helixVision composes wetSpring genomics pipelines into a sovereign
genomics tool. A guideStone-certified helixVision build means: the
variant calls produced from a MinION run are reproducible. Same raw
reads, same pipeline, any hardware → same variants within documented
statistical bounds. The bounds are derived from sequencing error models,
not from "it looks about right."

A field biologist at a wastewater treatment plant runs helixVision on a
laptop. The variants they report are guideStone-grade — reproducible,
reference-traceable, self-verifying. The lab that receives the data
trusts it because the artifact proves itself, not because they trust
the field biologist's computer.

### Product guideStone: esotericWebb Creative Provenance

A game is not science. But creative provenance has the same structural
requirement. An esotericWebb guideStone build means: every narrative
event in a game session has a DAG vertex signed by bearDog, timestamped,
and traceable through the provenance trio. The creative NFT minted from
that session is not a claim — it is a mathematical proof that the game
events occurred in that order, on that hardware, at that time.

This is guideStone applied to art. The "substrate" is not physics — it
is the mathematical structure of the DAG itself. The Merkle root is as
deterministic for a game session as for a lattice QCD measurement. The
verification is the same: anyone with the DAG data can recompute the
root and confirm the certificate.

---

## guideStone and the Provenance Trio

guideStone and the provenance trio are complementary, not redundant.

guideStone certifies the **computation** — that the binary produces
reproducible, reference-traceable, self-verifying output. This is a
property of the artifact itself. A guideStone artifact on a USB stick
with no network, no trio, no blockchain still produces guideStone-grade
output.

The provenance trio certifies the **event** — who ran it, when, on what
hardware, with what attribution. rhizoCrypt records the DAG. bearDog
signs it. loamSpine stores the certificate. sweetGrass records the braid.
The anchoring pipeline writes it to Bitcoin/Ethereum.

When both are present, the result is a Novel Ferment Transcript backed
by guideStone-grade computation:

```
guideStone artifact (reproducible computation)
    + provenance trio (who, when, where, attribution)
    + anchoring pipeline (public chain proof)
    = Novel Ferment Transcript
        (self-proving, attributed, permanently anchored)
```

A guideStone without the trio is reproducible but anonymous. An NFT
without a guideStone is attributed but not necessarily reproducible.
Both together are the full sovereign science stack.

---

## guideStone and the External Validation Artifact

The External Validation Artifact Standard (wateringHole) already defines
much of what a spring guideStone looks like: `./run`, static musl
binaries, `expected/` reference data, CHECKSUMS, plain-text README,
JSON output with named tolerances.

guideStone generalizes that standard to any ecoBin, not just spring
validation artifacts. The Validation Artifact Standard is a specific
instantiation of guideStone for springs. guideStone is the class; the
validation artifact is one member.

| Scope | Validation Artifact | guideStone |
|-------|--------------------|-----------:|
| Applies to | Springs (science validation) | Any ecoBin |
| Primary output | Check results (PASS/FAIL) | Any reproducible structured output |
| Audience | Scientists validating papers | Anyone consuming verifiable data |
| Trio required | No | No (complementary) |
| Anchoring required | No | No (complementary) |
| Determinism | Required | Required |
| Reference-traceability | Papers and named tolerances | Papers, standards, proofs, or mathematical derivations |

---

## The Orthogonal Dimension

The ecosystem now has three independent classification axes:

### Structure: What Is It Built From?

```
UniBin → ecoBin → genomeBin
```

Describes how the binary is constructed. Pure Rust, static linking,
cross-compilation, deployment wrapper. Defined in gen3.

### Deployment: Where Does It Run?

```
NUCLEUS → Niche → fieldMouse
```

Describes the composition context. Full primal orchestration, biomeOS
deploy graph, or minimal chimera. Defined in gen3 and gen4.

### Verification: What Does Its Output Mean?

```
guideStone
```

Describes the quality of the output. Reproducible, reference-traceable,
self-verifying, environment-agnostic, tolerance-documented. Defined in
gen4.

These axes are independent. A fieldMouse sensor node can be a guideStone
(its soil pH readings are calibrated against NIST standards with derived
tolerances). A full NUCLEUS can produce output that is not guideStone
(exploratory computation with heuristic thresholds). The verification
class is orthogonal to both structure and deployment.

---

## The Metrological Analogy

Before 2019, the kilogram was defined by a physical artifact — Le Grand K,
a platinum-iridium cylinder in a vault in Paris. Every measurement of
mass on Earth traced back to that one object. If Le Grand K changed
(and it did — it lost approximately 50 micrograms over a century), every
kilogram on Earth drifted with it.

In 2019, the kilogram was redefined in terms of the Planck constant —
a mathematical relationship that does not change, does not drift, and
does not depend on any physical object. The measurement became
self-proving. Any laboratory with the right equipment can realize the
kilogram independently, and the results agree because the mathematics
agrees.

guideStone is the ecoPrimals equivalent of that redefinition. Instead
of trusting an artifact because of who produced it (Le Grand K, the
journal, the institution), the consumer trusts the output because it is
**reproducible from the mathematics**. The binary is the instrument. The
output is the measurement. The mathematics is the invariant substrate.

This is the "e=mc^2 of the system" — not because the artifact is as
important as mass-energy equivalence, but because it has the same
structural property: the equation is true regardless of who writes it
down, where they write it, or what credentials they hold. A guideStone
output is true regardless of who runs the binary, where they run it, or
what institution they belong to.

Reality owns itself. guideStone is how computation proves that.

---

---

## The First Deployment Artifact (April 2026)

Everything above was conceptual when written on March 31. Five days later,
the first guideStone deployment artifact — `hotSpring-guideStone-v0.7.0` —
was built, deployed to USB, validated across 5 substrates and 2
architectures, containerized, and shipped with cross-OS launchers. This
section documents what the five properties look like when they hit reality.

### What Was Built

A self-contained directory (`validation/`) with:

- Dual-architecture binaries: `bin/x86_64/{static,gpu}/` + `bin/aarch64/static/`
- Unified entry point: `./hotspring validate` (shell wrapper dispatching to Rust binaries)
- OCI container image: `container/hotspring-guidestone.tar` (Docker/Podman)
- Windows launcher: `hotspring.bat` (WSL2 → Docker fallback)
- Integrity manifest: `CHECKSUMS` (SHA-256)
- Self-knowledge: `liveSpore.json` (tracks every machine the artifact visits)
- Reference data: `expected/validate_chuna_reference.json`
- Plain-text documentation: `README`, `GUIDESTONE.md`

Total artifact: ~80 MB (dual binary + container), ~40 MB (static only).

### How the Five Properties Manifested

**Property 1 (Deterministic)** was tested on 5 substrates:

| Substrate | Arch | GPU | Checks | Result |
|-----------|------|-----|--------|--------|
| Ubuntu 22.04 | x86_64 | None | 59/59 | PASS |
| Ubuntu 22.04 | x86_64 | NVIDIA RTX 3090 | 59/59 | PASS |
| Ubuntu 22.04 | x86_64 | AMD RX 6950 XT | 59/59 | PASS |
| Alpine 3.19 | x86_64 | None | 59/59 | PASS |
| Ubuntu 22.04 | aarch64 (qemu-user) | None | 59/59 | PASS |

Cross-substrate observable comparison: **40/40 bit-identical**. The physics
does not depend on the instruction set, the C library, the GPU vendor, or
the operating system. The computation touches the same mathematical
substrate regardless of hardware — the concrete realization of Property 1.

**Property 2 (Reference-Traceable)** carried through to JSON output. Every
check in the validation suite includes `paper`, `measured`, `threshold`,
`tolerance_justification`, and `comparison` fields. Chuna can `diff` the
output against his MILC runs.

**Property 3 (Self-Verifying)** caught real problems during development.
When `validate_chuna_overnight.rs` was modified for GPU streaming HMC, the
CHECKSUMS verification failed immediately on the next USB run. The
integrity pipeline is genuine, not decorative.

**Property 4 (Environment-Agnostic)** was the hardest. Three failures:

1. **FAT32 permissions**: USB formatted as FAT32 silently ignores `chmod +x`.
   Fixed by: ext4 for Linux, exFAT + tmpdir fallback for universal.
2. **Static musl + Vulkan**: `dlopen("libvulkan.so.1")` fails in static-pie
   musl binaries. Fixed by: dual-binary strategy (static CPU + glibc GPU).
3. **macOS/Windows**: No native Linux execution. Fixed by: OCI container
   image + platform-specific launchers.

Each failure taught something about what "environment-agnostic" actually
means. The theoretical definition ("runs anywhere") collapsed into an
engineering reality ("runs anywhere with the right substrate detection and
fallback strategy"). The artifact is environment-agnostic not because it
avoids complexity, but because it detects and adapts.

**Property 5 (Tolerance-Documented)** survived cross-architecture testing.
The same tolerances derived for x86_64 held on aarch64 — confirming they
are mathematical properties of the computation, not artifacts of the
platform. This is the strongest test: if a tolerance only holds on one
architecture, it is not mathematically derived.

### What Was Learned

**The artifact is the proof.** Not the paper, not the test suite, not the
CI badge. The USB drive itself — plug it in, `./hotspring validate`, 59/59
pass. The artifact carries its own validation, its own reference data, its
own integrity, and its own documentation. It does not need a network, a
package manager, or a conversation about dependencies.

**Cross-architecture parity is the strongest determinism test.** x86_64
and aarch64 have different floating-point rounding behavior, different SIMD
paths, different instruction scheduling. If the same tolerances hold on
both architectures, they are properties of the mathematics, not the
silicon.

**The dual-binary strategy is fundamental.** Static musl binaries (CPU-only,
zero deps, any Linux since 2014) and dynamic glibc binaries (GPU via Vulkan
dlopen) are complementary, not competing. The entry point detects which to
use. This should be a standard pattern for any ecoBin that touches GPU
hardware.

**Container images are the universal substrate fallback.** When native
execution is not possible (macOS, Windows without WSL2, NFS noexec), an
OCI container with the full artifact provides identical behavior. The
container is not a development tool — it is a deployment substrate.

**Self-knowledge is operationally useful.** `liveSpore.json` tracks every
machine the USB visits: hostname, date, GPU/CPU mode, checks passed,
duration. When the drive comes back from a collaborator, you can see
exactly what happened on their hardware.

### guideStone as Hardware Benchmark

An unexpected property emerged: the guideStone artifact doubles as a
hardware benchmark. When plugged into unknown hardware, `./hotspring
benchmark` profiles GPU throughput, precision capabilities, and physics
performance. The artifact does not just validate physics — it
characterizes the machine.

This makes the guideStone a **self-leveling** tool. It tells the user:
"your hardware can do this" alongside "the physics is correct." The
benchmark and the validation are the same computation seen from two
perspectives — one measures the substrate, the other measures the output.

### Implications for gen4

The first deployment artifact proves that guideStone is not a theoretical
classification. It is a concrete engineering practice with specific
patterns:

1. **Unified entry point** (`./hotspring`) with subcommands
2. **Arch-first binary layout** (`bin/<arch>/{static,gpu}/`)
3. **Shared library** (`_lib.sh`) for detection and dispatch
4. **Dual binary** (static CPU + glibc GPU) for hardware coverage
5. **Container fallback** for non-Linux substrates
6. **Cross-OS launchers** (.bat for Windows, auto-dispatch for macOS)
7. **Integrity manifest** (CHECKSUMS validated before execution)
8. **Self-knowledge** (liveSpore.json for operational tracking)

These patterns are reusable. esotericWebb, helixVision, or any gen4
product that produces verifiable output can follow the same structure.
The guideStone is not domain-specific. The deployment artifact is the
pattern; the physics/genomics/gaming content is the payload.

---

*The wolf was always falling. The plaquette was always 0.59. The
guideStone does not create the truth. It makes the truth portable.*
