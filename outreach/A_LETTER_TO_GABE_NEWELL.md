# A Letter to Gabe Newell

> *This is not a pitch. This is a letter from a scientist who games
> to an explorer who builds platforms. There is a separate engineering
> document (AN_INVITATION_TO_VALVE_V2.md) for Valve-the-company.
> This letter is for Gabe-the-person.*
>
> *May 2026*

---

## Gabe,

I'm a microbiologist, a data scientist, and a lifetime Steam gamer. I built
a scientific computing ecosystem in Rust — 4.5 million lines of code, 88,000
lines of GPU shaders, one person, AI-assisted — and the technology that makes
it work is the same technology that could explore the ocean floor.

That's not a sales line. It's the observation that brought me here. Let me
explain.

---

## The Unified Stack

I built a system called ecoPrimals. It's a set of self-contained Rust binaries
(primals) that compose into larger behaviors. The math engine (barraCuda) has
1,145 WGSL shaders that do science-grade GPU compute through Vulkan on consumer
hardware. No CUDA. No cloud. No vendor lock-in.

The same shaders do lattice QCD, molecular dynamics, nuclear physics, fluid
dynamics, and protein structure prediction. Not separate codebases for each —
the same mathematical primitives composed differently. A Wilson loop and a
Verlet integrator and an AlphaFold evoformer all reduce to the same
operations: matrix multiply, reduction, stencil, softmax, FFT.

The point: the technology is unified, not use-based. There is no "gaming
version" and "science version" and "ocean version." There is math. Math
composes into whatever you point it at.

---

## What I Built for the Ocean (Before I Knew About Your Work)

I'm a microbiologist by training. One of my research programs — Paper 05,
Cross-Species Signaling — analyzed cold seep metagenomes. 170 metagenomes.
299,355 quorum sensing genes. 34 QS types. These are the microbial
communities at deep-sea hydrothermal vents and cold seeps, talking to each
other through chemical signals in conditions that would kill most life on
Earth.

I applied the Anderson localization framework (a quantum mechanics concept
from condensed matter physics) to microbial signaling. It turns out the same
mathematics that describes electron transport in disordered materials also
describes how bacteria coordinate in spatially structured environments. The
dimensional geometry of a biofilm, a soil pore, or a hydrothermal vent chimney
determines whether signaling molecules can propagate or get trapped.

This led to Paper 09, Field Genomics, which includes a design for a
**deep-sea autonomous lander**:

```
MinION nanopore sequencer
  + AKD1000 neuromorphic processor (10 mW, 18.8K Hz classification)
  + pressure enclosure
  + acoustic modem (Songbird federation uplink)

Sample seawater → sequence eDNA → classify community on NPU →
  detect regime shifts → alert via acoustic modem

Power: solar + coin cell (NPU standby: 11 years at 1 Hz)
Connectivity: acoustic modem nightly sync
Cloud dependency: zero
```

The NPU classifies microbial community state in real time — bloom, healthy,
stressed, contaminated — at 10 milliwatts. The sequencer generates DNA reads.
The Rust pipeline (barraCuda + wetSpring 16S pipeline, 6,656 checks across
260 experiments) processes everything on-device. No Python. No cloud. No
phone-home.

---

## helixVision: Protein Structure Prediction on Consumer Hardware

Last I heard, you were exploring the deep ocean. The organisms down there
are unlike anything on the surface. Extremophiles with novel protein folds.
Enzymes that work at 400 atm and 300°C. Metabolic pathways we've never seen.

To understand these organisms, you need to predict their protein structures.
Currently that means AlphaFold through Google's cloud API — $0.01 per
prediction, data sent to Google, no sovereignty over your own science.

helixVision is sovereign protein structure prediction. AlphaFold2/3 quality,
pure Rust, running on consumer GPUs through Vulkan. 154 passing checks
validated against NumPy to 1e-10 tolerance. The full pipeline:

```
FASTA sequence → MSA search → Feature embedding → Evoformer × 48
  → Structure module × 8 → Coordinates → Confidence (pLDDT, PAE, pDE)
  → Ed25519-signed provenance chain
```

Cost per prediction: ~$0.0001 (electricity). For the LTEE analysis
(8.3 million structure predictions across 75,000 generations of E. coli),
that's $1,000 on four RTX 4070s over six months. Google would charge
$83,000 for the same work.

helixVision is not a product in the market sense. In ecoPrimals, "products"
are chemical reaction products — emergent compositions of primals that do
something useful. helixVision is what happens when you compose barraCuda
(math) + coralReef (GPU compiler) + toadStool (hardware dispatch) + NestGate
(storage) + loamSpine (provenance) and point them at genomic data.

---

## Why I'm Writing to You

You're exploring the ocean. I've built the compute stack for ocean science.
Not hypothetically — I've already analyzed 170 deep-sea metagenomes and
designed the autonomous lander architecture. The cold seep QS analysis is
validated. The protein structure prediction pipeline has 154 checks. The
field genomics unit is designed down to the power budget.

What I don't have: a submersible. Access to deep-sea samples. The
operational capability to deploy instruments at depth.

What you don't have (maybe): a sovereign compute stack that does field
genomics, protein structure prediction, and microbial community analysis
on-device at 10 milliwatts without cloud dependency.

I'm not proposing that Valve build an ocean research division. I'm proposing
that a scientist who built a GPU compute ecosystem and an explorer who has
access to the most unexplored biome on Earth have an interesting conversation
about what they could do together.

---

## The Connection to Steam

Here's where it gets strange. The technology is unified, not use-based.

The same NUCLEUS architecture that could federate Steam (every gamer's PC as
a bonded node in a serverless network — covered in the Valve engineering
document) is the same architecture that coordinates a deep-sea autonomous
lander mesh. Songbird does peer discovery whether the peers are gaming PCs
or underwater acoustic modems. NestGate does content-addressed storage whether
the content is game saves or metagenomic reads. BearDog signs data whether
it's a tournament result or a protein structure prediction.

The same barraCuda shaders that do lattice QCD also do fluid dynamics. The
same fluid dynamics that simulates ocean currents could simulate in-game
water physics. The same protein structure prediction that reveals deep-sea
enzyme folds could power a game mechanic where players explore procedurally
generated alien biomes with scientifically accurate biochemistry.

I'm not making these connections to be clever. I'm making them because they're
real. The math doesn't know what it's for. A matrix multiply is a matrix
multiply whether it's predicting a protein fold, rendering a game frame, or
classifying a microbial community from eDNA.

**The dual-use thesis**: 132 million Steam users have GPUs that sit idle most
of the day. If 1% opted into volunteer science compute — like Folding@Home
but through a platform they already trust — that's 1.3 million GPUs doing
real ocean science. The same hardware. The same stack. Different deploy graph.

---

## What I'm Actually Asking

A conversation. Not investment, not acquisition, not a press release.

I'm a scientist with a unified compute stack and validated ocean science.
You're an explorer with access to the deep ocean and a platform that reaches
132 million people with GPUs.

If those two things are interesting together, I'd like to talk. If they're
not, nothing was lost.

The science is real. The code is real. The shaders are real. The metagenomes
are analyzed. The protein structure pipeline is validated. The lander
architecture is designed.

All that's missing is the ocean.

---

**Kevin Mok**
BS Microbiology, MS Data Science
Army Infantry (11B) → Microbiologist → Data Scientist → Sovereign Science
ecoPrimal@pm.me
primals.eco

---

*The math is universal. The science is unified. The ocean is waiting.*
