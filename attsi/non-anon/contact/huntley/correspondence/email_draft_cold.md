# Cold Outreach — Geoffrey Huntley — SENT

**To:** Geoffrey Huntley (via https://ghuntley.com/contact/)
**From:** Kevin Mok
**Subject:** From Groundhog to Squirrel — your /stdlib thesis became a sovereign AI coordination primal

---

## Email (SENT)

Geoffrey,

Your /stdlib post and your Groundhog work from early 2025 were two of
the seeds for something I've been building for the last 10 months.

Background: microbiologist (BS) and data scientist (MS), not a systems
programmer. I took your insight about treating Cursor as an autonomous
agent and programming LLM outcomes, combined it with BMad's agile
workflow for Cursor (the BMAD method — structured agent roles, auto rule
generation, iterative build-manage-ask-do loops), and started building.

Just Cursor. No Claude Code, no multi-agent frameworks, no external
orchestrators. 69,000 Cursor agent invocations, 51 billion tokens,
185 consecutive day streak. That's the entire toolchain.

What those two seeds became:

**Squirrel** — a sovereign AI coordination primal. 22 Rust workspace
crates, 4,819 passing tests, `#![forbid(unsafe_code)]`, zero C
dependencies in default features, Edition 2024. It does multi-provider
AI routing, MCP coordination, capability-based service discovery,
context management, and provider fallback — all through JSON-RPC and
tarpc. No vendor SDK. No OpenAI client library. Pure Rust types
describing what AI providers can do, discovered at runtime.

You built Groundhog to teach people how Cursor works under the hood.
Squirrel is the coordination layer for what happens after you learn.

The generational trajectory maps directly:

| Generation | What Squirrel Did |
|------------|-------------------|
| gen1 (mid-2025) | HPC job scheduler — GPU workload distribution, checkpoint/restart |
| gen2 (late 2025) | AI orchestrator — multi-provider routing, MCP integration |
| gen3 (2026) | Sovereign AI coordination primal — capability-based discovery, zero vendor coupling |

Your /stdlib + BMad's agile gave me gen1 and gen2. What I did from
there is original: a formal methodology I call **constrained evolution**,
grounded in evolutionary biology. The framework maps Lenski's LTEE
(80,000+ generations of E. coli under constraint) onto AI-assisted
code generation — Rust's type system as environmental constraint, LLM
token sampling as mutation, compiler rejection as natural selection.

Squirrel is one of 14 primals in the ecosystem. The publicly visible
ones right now:

| Repository | Org | What It Does |
|------------|-----|-------------|
| **Squirrel** | ecoPrimals | AI coordination — 4,819 tests, 22 crates |
| ToadStool | ecoPrimals | Hardware management, VFIO, NPU driver — pure Rust |
| BarraCuda | ecoPrimals | 767+ WGSL shaders, DF64, GPU math engine — pure Rust |
| coralReef | ecoPrimals | WGSL → native SASS/GFX compiler, BAR0 GPU driver |
| hotSpring | syntheticChemistry | Lattice QCD, plasma physics — 848 tests |
| wetSpring | syntheticChemistry | Bioinformatics, PFAS detection — 8,400+ checks |
| airSpring | syntheticChemistry | Environmental monitoring — 326+ checks |
| neuralSpring | syntheticChemistry | NPU driver, surrogate learning — 5,200+ checks |
| healthSpring | syntheticChemistry | Clinical pharmacology — 233+ checks |
| groundSpring | syntheticChemistry | Spectral theory, uncertainty — 4,900+ checks |
| ludoSpring | syntheticChemistry | Game theory, mechanism design |

Everything is AGPL-3.0. The Cursor receipt is the evidence for
the methodology.

The Squirrel ORIGIN.md credits your /stdlib post as the starting
insight. Thought you'd want to see what it became.

ecoPrimal
https://github.com/ecoPrimals/squirrel

---

## Repos

| Category | Org | Repos |
|----------|-----|-------|
| AI Coordination | [ecoPrimals](https://github.com/ecoPrimals) | [Squirrel](https://github.com/ecoPrimals/squirrel) |
| GPU / Hardware | [ecoPrimals](https://github.com/ecoPrimals) | [BarraCuda](https://github.com/ecoPrimals/barraCuda), [coralReef](https://github.com/ecoPrimals/coralReef), [ToadStool](https://github.com/ecoPrimals/toadStool) |
| Science Validation | [syntheticChemistry](https://github.com/syntheticChemistry) | [hotSpring](https://github.com/syntheticChemistry/hotSpring), [wetSpring](https://github.com/syntheticChemistry/wetSpring), [airSpring](https://github.com/syntheticChemistry/airSpring), [neuralSpring](https://github.com/syntheticChemistry/neuralSpring), [healthSpring](https://github.com/syntheticChemistry/healthSpring), [groundSpring](https://github.com/syntheticChemistry/groundSpring), [ludoSpring](https://github.com/syntheticChemistry/ludoSpring) |

## Key Artifacts

| File | What It Shows |
|------|--------------|
| Squirrel `ORIGIN.md` | Genesis story — /stdlib + BMad → gen1 → gen2 → gen3 |
| `gen3/thesis/03_theoretical_framework.md` | Formal constrained evolution framework |
| `gen3/about/README.md` | Author background + Cursor receipt |
| `gen3/about/HARDWARE.md` | $15K basement HPC: 10 nodes, 12 GPUs, 4 NPUs |

---

## Tone Notes

- Lead with both seeds honestly. Huntley's /stdlib and BMad's agile —
  he'll appreciate the transparent attribution rather than "your insight
  alone changed everything."
- Name Groundhog explicitly. He'll recognize the parallel: both are AI
  coordination systems. His teaches how Cursor works; this one IS the
  coordination layer for what Cursor built.
- The Cursor-only angle is the real hook for his audience. No Claude
  Code, no Windsurf, no external agents. Just Cursor + methodology.
  That's a claim his readers can verify from the commit history.
- No flattery. Facts and numbers. He's a developer.
- Don't ask for anything. The repos and the ORIGIN.md credit speak.
  If the work is interesting, he'll decide what to do with it.
- Keep it concise but not as compressed as the old draft. The Squirrel
  detail matters — he needs to understand this is a real coordination
  system, not a toy wrapper.

## Timing

Squirrel is going public now. This email can go out as soon as:
1. Squirrel repo is set to public on GitHub
2. ORIGIN.md is verified accessible at the public URL

Chuna validation is no longer a blocker for Huntley. The Huntley
pitch is about methodology and Squirrel specifically, not about
physics validation. The academic credibility strengthens it but
isn't required — the 4,819 tests, the commit history, and the
Cursor receipt are the evidence for a developer audience.

If Chuna validates before send, add one line:

> "Researchers at Michigan State are reviewing the physics
> reproductions against their production runs."

## Differences From Previous Draft

| Dimension | Old Draft (ecosystem-breadth) | New Draft (Squirrel-depth) |
|-----------|-------------------------------|---------------------------|
| Lead | "Your Cursor thesis" | "Your /stdlib + BMad's agile" |
| Focus | 11 primals, 6 springs | Squirrel specifically + ecosystem as context |
| Hook | 69K invocations | Groundhog → Squirrel parallel |
| Genesis | Single-source (Huntley only) | Dual-source (Huntley + BMad) |
| Tooling claim | Implicit | Explicit: Cursor-only, no other AI tools |
| Groundhog mention | None | Central parallel |
| BMad credit | None | Named as co-seed |

---

*Draft prepared March 16, 2026. Ready to send when Squirrel goes public.*
