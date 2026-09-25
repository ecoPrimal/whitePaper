# K-NOME vs The Autonomous Agent Loop

**Context**: Alistair shared a flowchart of a typical coding agent optimization loop and asked if that's how I run things. Short answer: no. This document characterizes what the flowchart describes, what K-NOME actually is, and maps the ecoPrimals subsystems that achieve each piece.

**Date**: June 2026
**For**: ABG / Discord / anyone who asks "is that how your AI system works?"

---

## What the Flowchart Describes

```
program.md → Coding Agent (Claude Code / Codex)
  → Edit train.py
  → Train 5 min on GPU
  → Measure metric → results.tsv
  → Improved? → Yes: git commit / No: git reset
  → Loop back
```

This is an **autonomous optimization loop**. The agent:
- Reads a spec (`program.md`)
- Edits code autonomously
- Runs the code
- Measures a single fitness metric
- Commits if improved, resets if not
- Repeats without human intervention

It's automated hyperparameter search with an LLM as the code editor. The human writes the spec, walks away, and comes back to a results file. The agent is autonomous. The metric is the selector. Git is the checkpoint.

This is useful for narrow optimization problems. It is not how ecoPrimals works.

---

## What K-NOME Actually Is

**K-NOME** (Knowledge-Numeric Observed & Mentored Evolutionary) is a human-in-the-loop methodology where:

- The **human** is the selective pressure (not a metric)
- The **compiler** (Rust type system) is blind natural selection
- The **AI** is the mutation operator (generates candidates at speed)
- The **conversation** is the medium (not a spec file)
- The **observation** is bidirectional (the human learns the system as it grows)

### The Core Difference

| Dimension | Agent Loop (Flowchart) | K-NOME (ecoPrimals) |
|-----------|----------------------|---------------------|
| **Who decides** | A metric (results.tsv) | The human (domain expertise) |
| **Human role** | Write spec, walk away | Mentor every cycle — analogy, correction, redirection |
| **AI role** | Autonomous agent | Candidate generator under mentoring |
| **Selection** | Metric improves? Commit. | Compiler rejects unsound code. Human evaluates fitness. |
| **What improves** | One metric | The system AND the human's understanding of the system |
| **Constraint** | Training loss | Rust type system (compile-time soundness guarantee) |
| **Scope** | One file, one model | 14 primals, 7 springs, 27,000+ tests across 7 domains |
| **Memory** | git commit / reset | Provenance trio (rhizoCrypt + loamSpine + sweetGrass) + context braids + handoffs + fossilRecord |
| **Output** | results.tsv | Self-verifying artifact (pseudoSpore / guideStone) |
| **Tool** | Claude Code / Codex | Cursor IDE (only) — no multi-agent, no orchestrator |
| **Autonomy** | Agent runs unsupervised | Human mentors every substantive decision |

### The Evolutionary Framing

The flowchart is **Darwinian only** — blind metric selection, random edit variation, no inheritance of acquired characteristics.

K-NOME is **Darwinian + Lamarckian**:
- The compiler is Darwinian — it rejects what doesn't fit, blind and indifferent
- The human is Lamarckian — they acquire understanding through observation and transmit it directly into the next generation through mentoring
- The goals evolve — gen1 asked "can we build HPC?", gen5 asks "does someone else's science come out the other end?"

There is no Weismann barrier in software. What the human learns IS heritable.

---

## The ecoPrimals Subsystems That Replace Each Box

### Instead of `program.md` → **Context Braids + Handoffs + whitePaper**

The agent loop starts with a static spec file. K-NOME starts with living context:

| Subsystem | What It Does | gen |
|-----------|-------------|-----|
| **Context braids** (sweetGrass external) | Ephemeral developer state — focus, breadcrumbs, next steps. Woven via `membrane context.weave`, consumed by the AI at session start | gen5 |
| **Handoffs** (wateringHole) | Session continuity documents — what was done, what broke, what's next. The working memory between sessions | gen3+ |
| **whitePaper** (metaPrimal) | The strategic and scientific record — theses, architecture decisions, evolution narrative. The "why" layer | gen2+ |
| **Impulses** (rhizoCrypt external) | Event-driven coordination between gates — pending actions, cross-gate state changes | gen5 |

The AI doesn't read a spec. It reads the evolved state of the project — context braids, recent handoffs, open impulses — and the human mentors from there.

### Instead of `Coding Agent (Claude Code / Codex)` → **Cursor IDE + K-NOME Conversation**

| Subsystem | What It Does | gen |
|-----------|-------------|-----|
| **Cursor IDE** | The only tool. AI-integrated editor with agent mode, file access, terminal access. One human-AI relationship per session | gen1+ |
| **K-NOME methodology** | Mentored conversation — analogy, correction, narrative, taste, redirection. The human's domain expertise IS the program | gen3+ |

No Claude Code. No Codex. No multi-agent frameworks. No `@pm` or `@architect` roles. The human IS all roles. The AI is the generalist collaborator. The methodology IS the orchestrator.

### Instead of `Edit train.py` → **Primal / Spring / Garden Code Evolution**

| Subsystem | What It Does | gen |
|-----------|-------------|-----|
| **Primals** (14 Rust binaries) | Self-contained capabilities — one domain each. barraCuda (math), toadStool (hardware), songBird (networking), etc. | gen2+ |
| **Springs** (7 validation environments) | Compose primals and validate science against published papers. Each spring has numbered experiments and counted checks | gen3+ |
| **Gardens** (5 user-facing products) | Compose primals into tools people use — esotericWebb, lithoSpore, initioChem, blueFish, helixVision | gen4+ |

The agent loop edits one file. K-NOME evolves an ecosystem of composable binaries across 7 scientific domains.

### Instead of `Train 5 min on GPU` → **The Sovereign Compute Triangle**

| Subsystem | What It Does | gen |
|-----------|-------------|-----|
| **barraCuda** (primal) | Pure math — 712+ WGSL f64 shaders. Writes the computation | gen3+ |
| **coralReef** (primal) | Sovereign shader compiler — WGSL → native GPU binary without vendor SDKs | gen4+ |
| **toadStool** (primal) | Hardware infrastructure — discovers CPUs/GPUs/NPUs, dispatches workloads, manages node atomic | gen2+ |
| **Sovereign mesh** (11 gates) | Physical hardware — no cloud, no queue, no shared anything. biomeOS orchestrates across gates | gen1+ |

The agent loop trains on one GPU. K-NOME dispatches across 11 gates with hardware-aware routing, vendor-independent shader compilation, and multi-architecture GPU support (Kepler through Blackwell + AMD).

### Instead of `Measure metric → results.tsv` → **Paper Parity + Counted Checks**

| Subsystem | What It Does | gen |
|-----------|-------------|-----|
| **Paper parity** (standard) | Rust output must match published paper results within named tolerances — not "close enough", reviewer-would-accept-it | gen3+ |
| **Counted checks** (per experiment) | Each spring experiment has explicit pass/fail/skip counts. 12,510+ checks across ecosystem | gen3+ |
| **guideStone** (verification class) | Self-proving output — deterministic, reference-traceable, self-verifying, environment-agnostic, tolerance-documented | gen4+ |

The agent loop measures one metric. K-NOME validates against entire published papers — figures, statistical claims, computational results — across 70+ reproduced papers.

### Instead of `Improved? → git commit / git reset` → **Provenance Trio + fossilRecord**

| Subsystem | What It Does | gen |
|-----------|-------------|-----|
| **rhizoCrypt** (primal) | Ephemeral memory — working DAG, fast, lock-free. The "present" | gen3+ |
| **loamSpine** (primal) | Permanent memory — immutable linear history, certificates. The "past" | gen3+ |
| **sweetGrass** (primal) | Attribution — semantic provenance, W3C PROV-O braids. The "always" | gen3+ |
| **fossilRecord** (archive) | Geological record — 3,831+ documents, never deleted, only accumulated | gen4+ |
| **Git** (outer membrane) | Standard version control — but git is just the outer membrane mirror. Forgejo on sovereign VPS is the inner membrane | gen1+ |

The agent loop does git commit or git reset. K-NOME tracks provenance at every layer — who computed what, on which hardware, from which data, with what attribution chain — and archives everything into the fossilRecord. Git is one of six provenance mechanisms, not the only one.

### Instead of the **output** → **pseudoSpore / lithoSpore**

| Subsystem | What It Does | gen |
|-----------|-------------|-----|
| **pseudoSpore** | Self-verifying portable artifact — all code, data, validation, provenance in one package. "Run this, see what passes" | gen4+ |
| **lithoSpore** | USB-deployable guideStone — offline, self-proving, physically portable. The ultimate verification artifact | gen4+ |
| **plasmidBin** | Binary distribution — pre-built musl-static binaries, checksummed, signed | gen4+ |

The agent loop produces a results.tsv. K-NOME produces pseudoSpores — self-contained verification artifacts that carry their own provenance chain, validation suite, and attribution braids. Hand one to a reviewer, a student, or a skeptic. They don't need to trust you. They run it.

---

## The Full Picture

```
                    ┌─────────────────────────────────┐
                    │         The Human (K-N)          │
                    │  Domain expertise + observation  │
                    │  Analogy, correction, narrative  │
                    │    taste, redirection, goals     │
                    └──────────┬──────────────────┬────┘
                               │ mentors          │ observes
                               ▼                  │
                    ┌──────────────────────┐       │
                    │   Cursor IDE (only)  │       │
                    │   K-NOME conversation│       │
                    └──────────┬───────────┘       │
                               │ generates         │
                               ▼                  │
                    ┌──────────────────────┐       │
                    │  Rust type system    │       │
                    │  (blind Darwinian    │       │
                    │   selection)         │       │
                    └──────────┬───────────┘       │
                               │ compiles          │
                               ▼                  │
              ┌────────────────────────────────┐   │
              │         Ecosystem              │   │
              │  14 primals × 7 springs        │   │
              │  11 gates × sovereign mesh     │   │
              │  barraCuda + coralReef +        │   │
              │  toadStool compute triangle    │   │
              └────────────────┬───────────────┘   │
                               │ validates         │
                               ▼                  │
              ┌────────────────────────────────┐   │
              │      Paper Parity              │   │
              │  12,510+ checks, 70+ papers    │   │
              │  Named tolerances, guideStone  │   │
              └────────────────┬───────────────┘   │
                               │ packages          │
                               ▼                  │
              ┌────────────────────────────────┐   │
              │      pseudoSpore / lithoSpore  │◄──┘
              │  Self-verifying artifact        │
              │  Provenance trio embedded       │
              │  sweetGrass attribution braids  │
              │  "run this, see what passes"    │
              └────────────────────────────────┘
```

The human never leaves the loop. The system never runs unsupervised. The output is not a metric — it's a proof.

---

## For Alistair Specifically

The GROMACS work (conformational dynamics, QM/MM, PDB structures) uses the same methodology:

1. Published paper = validation target (paper parity standard)
2. Python/GROMACS baseline = the reproduction (industry tools, existing code)
3. Rust rebuild = the evolution (barraCuda shaders, toadStool dispatch)
4. pseudoSpore = the artifact (portable, self-verifying, carries provenance)

His PDB 3HZ3 question (N1025D mutation, wild-type transition state via OPES QM/MM) would be an extended project following this exact pattern — reproduce the known baseline, validate against published results, then evolve the computation through the ecosystem.

The AI doesn't simulate the protein. The AI helps build the pipeline that simulates the protein. The computation runs on the sovereign mesh. The human mentors the architecture. The result is a self-verifying artifact that anyone can run.
