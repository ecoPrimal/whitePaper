# Cold Outreach — Geoffrey Huntley

**To:** Geoffrey Huntley (via https://ghuntley.com/contact/)
**From:** Kevin Mok
**Subject:** Where your Cursor thesis ended up — 69K invocations later

---

## Draft

Geoffrey,

I read your "You are using Cursor AI incorrectly" post about 10 months ago
and took it somewhere you probably haven't seen.

Background: microbiologist (BS) and data scientist (MS), not a systems
programmer. Your insight about treating Cursor as an autonomous agent and
programming LLM outcomes became the foundation for a formal methodology I
call constrained evolution — AI as mutation operator, Rust's type system as
natural selection, physics validation as fitness function.

10 months later, the result:

- 11 production Rust services — crypto, networking, storage, GPU compute,
  AI orchestration, neuromorphic NPU driver
- 6 science validation suites — 27,000+ passing checks reproducing published
  physics (lattice QCD, plasma physics, drug discovery, bioinformatics,
  environmental monitoring, neuromorphic computing)
- A GPU shader compiler that compiles WGSL → native NVIDIA SASS and AMD GFX
  ISA — pure Rust, zero C, no vendor SDK
- Lattice QCD detecting the quark-gluon deconfinement phase transition on a
  $4,000 basement machine built from used parts
- One developer. 69,000 Cursor agent invocations. 51 billion tokens consumed.
  185 consecutive day streak. Top <0.1% of all Cursor users.

Everything is AGPL-3.0 and public. The Cursor receipt is the evidence for
the methodology.

I wrote a formal paper grounding this in evolutionary biology — the same
principles that gave us Taq polymerase from Yellowstone hot springs apply to
AI-assisted code generation under Rust's type system. The theoretical
framework connects:

- Lenski's Long-Term Evolution Experiment (E. coli, 75,000 generations)
  → AI agent invocations as mutation-selection cycles
- Rust's borrow checker + type system → environmental constraint
  (analogous to thermal/pH selection in extremophile evolution)
- Physics validation → fitness function (does the QCD reproduce or not?)

The codebase isn't a prototype. Researchers at Michigan State are reviewing
the physics reproductions against their production MILC/ICER runs.

Thought you'd want to see where your insight ended up. Happy to discuss
the methodology in detail — the formal framework might interest your
audience as a theoretical backing for the practical approach you described.

Kevin Mok
https://github.com/syntheticChemistry

---

## Repos (public)

| Repository | What It Does |
|------------|-------------|
| hotSpring | Lattice QCD, plasma physics, nuclear EOS — 848 tests |
| wetSpring | Bioinformatics, PFAS detection, phage ecology — 8,400+ checks |
| airSpring | Environmental monitoring, precision agriculture — 326+ checks |
| neuralSpring | NPU driver, ESN, LSTM, surrogate learning — 5,200+ checks |
| healthSpring | Clinical pharmacology, gut microbiome — 233+ checks |
| groundSpring | Anderson localization, spectral theory, uncertainty — 4,900+ checks |
| barraCuda | 767+ WGSL shaders, DF64, GPU math engine — pure Rust |
| coralReef | WGSL → native SASS/GFX compiler, BAR0 GPU driver — pure Rust |
| toadStool | Hardware management, VFIO, NPU driver, hw-learn — pure Rust |

## Key Artifacts

| File | What It Shows |
|------|--------------|
| `gen3/thesis/03_theoretical_framework.md` | Formal constrained evolution framework |
| `gen3/about/README.md` | Author background + Cursor receipt |
| `gen3/about/HARDWARE.md` | $15K basement HPC: 10 nodes, 12 GPUs, 4 NPUs |
| `gen3/about/SOVEREIGN_SCIENCE.md` | Why open code + consumer hardware changes science |

---

## Tone Notes

- Lead with his insight. He wrote the post; we evolved it.
- No flattery. Facts and numbers. He'll appreciate directness.
- Don't oversell the ecosystem — let the repo links speak.
- Don't ask for anything specific. The implicit ask is "write about this"
  but don't say that. If the work is interesting, he'll decide what to do.
- Keep it concise. He's a developer, not an academic. No abstract.
- The subject line should make him click: specific number (69K) + his
  own concept (thesis) + curiosity gap (ended up).

## Timing

Send after Chuna validates physics. The pitch is strongest as:

> "...and the physics was independently validated by researchers
> whose papers we reproduced."

Without that: "someone claims they built something."
With that: "someone built something and the scientists confirmed it works."

If Chuna validates quickly (next 2 weeks), this email can go out
late March 2026.
