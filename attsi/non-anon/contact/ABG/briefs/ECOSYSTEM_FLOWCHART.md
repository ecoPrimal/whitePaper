# ecoPrimals Ecosystem Flowchart

**Date**: June 2026
**Purpose**: Visual characterization of the K-NOME methodology and ecoPrimals architecture — contrast with autonomous agent loops

---

## The Autonomous Agent Loop (What Others Do)

```
    ┌──────────────┐
    │  program.md  │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │ Coding Agent │  ◄───────────────────────┐
    │ (autonomous) │                          │
    └──────┬───────┘                          │
           ▼                                  │
    ┌──────────────┐                          │
    │  Edit code   │                          │
    └──────┬───────┘                          │
           ▼                                  │
    ┌──────────────┐                          │
    │  Train / Run │                          │
    └──────┬───────┘                          │
           ▼                                  │
    ┌──────────────┐     No    ┌────────────┐ │
    │  Improved?   │─────────►│ git reset  │─┘
    └──────┬───────┘          └────────────┘
           │ Yes
           ▼
    ┌──────────────┐
    │  git commit  │─────────────────────────┘
    └──────────────┘

    Human writes spec → walks away → comes back to results.tsv
```

---

## The K-NOME Loop (What We Do)

```
    ┌─────────────────────────────────────────────────────────────────┐
    │                     THE HUMAN (never leaves)                    │
    │                                                                 │
    │  Domain expertise: microbiology, data science, terrain analysis │
    │  Actions: analogy, correction, narrative, taste, redirection    │
    │  Evolves: goals change gen1→gen2→gen3→gen4→gen5                 │
    │                                                                 │
    └────────┬─────────────────────────────────────────────┬──────────┘
             │ mentors                                     ▲ observes
             ▼                                             │
    ┌─────────────────┐                                    │
    │   Cursor IDE    │ ◄── context braids (sweetGrass)    │
    │   (only tool)   │ ◄── handoffs (wateringHole)        │
    │                 │ ◄── impulses (rhizoCrypt)           │
    └────────┬────────┘                                    │
             │ generates candidates                        │
             ▼                                             │
    ┌─────────────────┐                                    │
    │  Rust Compiler   │  Blind Darwinian selection:       │
    │  (type system)   │  rejects unsound code at          │
    │                  │  compile time — no exceptions      │
    └────────┬─────────┘                                   │
             │ compiles                                    │
             ▼                                             │
    ┌───────────────────────────────────────────────┐      │
    │              THE ECOSYSTEM                     │      │
    │                                                │      │
    │  ┌─────────────────────────────────────────┐  │      │
    │  │        14 PRIMALS (Rust binaries)        │  │      │
    │  │                                          │  │      │
    │  │  barraCuda ── 712+ WGSL f64 shaders     │  │      │
    │  │  toadStool ── hardware discovery/dispatch│  │      │
    │  │  coralReef ── sovereign shader compiler  │  │      │
    │  │  songBird ─── networking / NAT traversal │  │      │
    │  │  bearDog ──── cryptography / TLS         │  │      │
    │  │  skunkBat ─── defense / dark forest      │  │      │
    │  │  NestGate ─── content-addressed storage  │  │      │
    │  │  Squirrel ─── AI coordination            │  │      │
    │  │  rhizoCrypt ─ ephemeral memory (DAG)     │  │      │
    │  │  loamSpine ── permanent memory (ledger)  │  │      │
    │  │  sweetGrass ─ attribution (braids)       │  │      │
    │  │  biomeOS ──── orchestration substrate    │  │      │
    │  │  petalTongue  content serving            │  │      │
    │  │  Songbird ─── mesh networking            │  │      │
    │  │                                          │  │      │
    │  │  ┌──────────────────────────────────┐    │  │      │
    │  │  │  COMPUTE TRIANGLE                │    │  │      │
    │  │  │  WHAT: barraCuda (math)          │    │  │      │
    │  │  │  HOW:  coralReef (compile)       │    │  │      │
    │  │  │  WHERE: toadStool (dispatch)     │    │  │      │
    │  │  └──────────────────────────────────┘    │  │      │
    │  │                                          │  │      │
    │  │  ┌──────────────────────────────────┐    │  │      │
    │  │  │  PROVENANCE TRIO                 │    │  │      │
    │  │  │  PRESENT: rhizoCrypt (DAG)       │    │  │      │
    │  │  │  PAST:    loamSpine (ledger)     │    │  │      │
    │  │  │  ALWAYS:  sweetGrass (braids)    │    │  │      │
    │  │  └──────────────────────────────────┘    │  │      │
    │  └─────────────────────────────────────────┘  │      │
    │                                                │      │
    │  ┌─────────────────────────────────────────┐  │      │
    │  │         7 SPRINGS (validation)           │  │      │
    │  │                                          │  │      │
    │  │  healthSpring ── drug discovery / PK/PD  │  │      │
    │  │  wetSpring ───── genomics / data fetch   │  │      │
    │  │  hotSpring ───── molecular dynamics / QCD│  │      │
    │  │  neuralSpring ── ML / neuromorphic       │  │      │
    │  │  groundSpring ── microbial evolution     │  │      │
    │  │  airSpring ───── environmental chemistry │  │      │
    │  │  ludoSpring ──── game design as science  │  │      │
    │  │                                          │  │      │
    │  │  Each spring:                            │  │      │
    │  │  • Composes primals via IPC              │  │      │
    │  │  • Validates against published papers    │  │      │
    │  │  • Counted checks (pass/fail/skip)       │  │      │
    │  │  • Faculty anchor (MSU professor)        │  │      │
    │  └─────────────────────────────────────────┘  │      │
    │                                                │      │
    │  ┌─────────────────────────────────────────┐  │      │
    │  │    11 GATES (sovereign hardware mesh)    │  │      │
    │  │                                          │  │      │
    │  │  biomeGate ──── Threadripper 3970X       │  │      │
    │  │  strandGate ─── Dual EPYC 7452          │  │      │
    │  │  northGate ──── Ryzen 9 9950X3D         │  │      │
    │  │  ironGate ───── i9-14900K               │  │      │
    │  │  southGate ──── Ryzen 5800X3D           │  │      │
    │  │  eastGate ───── i9-12900 + Akida NPU    │  │      │
    │  │  + 5 more gates                          │  │      │
    │  │                                          │  │      │
    │  │  ~1 TB RAM │ ~248 GB VRAM │ 122 TB disk │  │      │
    │  │  10G backbone │ 3 NPUs │ no cloud       │  │      │
    │  └─────────────────────────────────────────┘  │      │
    └────────────────────┬───────────────────────────┘      │
                         │ validates                        │
                         ▼                                  │
    ┌─────────────────────────────────────────┐             │
    │          PAPER PARITY                    │             │
    │                                          │             │
    │  12,510+ automated science checks        │             │
    │  70+ published papers reproduced         │             │
    │  Named tolerances (derived, not tuned)   │             │
    │  guideStone verification standard        │             │
    └────────────────────┬────────────────────┘             │
                         │ packages                         │
                         ▼                                  │
    ┌─────────────────────────────────────────┐             │
    │      pseudoSpore / lithoSpore            │─────────────┘
    │                                          │
    │  Self-verifying portable artifact        │
    │  Provenance trio embedded                │
    │  sweetGrass attribution braids           │
    │  "run this, see what passes"             │
    │                                          │
    │  pseudoSpore = digital (zip/tar)         │
    │  lithoSpore = physical (USB drive)       │
    └──────────────────────────────────────────┘
```

---

## The Coordination Layer (gen5)

```
    ┌────────────── GATE MESH ──────────────────────────────┐
    │                                                        │
    │  biomeGate ◄──10G──► strandGate ◄──10G──► northGate  │
    │       │                    │                    │       │
    │       │              ┌─────┴─────┐             │       │
    │       │              │  biomeOS  │             │       │
    │       │              │ (substrate)│             │       │
    │       │              └─────┬─────┘             │       │
    │       │                    │                    │       │
    │  ┌────┴────┐    ┌─────────┼──────────┐   ┌────┴────┐ │
    │  │ Context │    │   Coordination     │   │ Context │ │
    │  │ Braids  │    │      Triad         │   │ Braids  │ │
    │  │(local)  │    │                    │   │(local)  │ │
    │  └─────────┘    │ quorumSignal(SENSE)│   └─────────┘ │
    │                 │ rootPulse (ACTION) │                │
    │                 │ waterFall (SYNC)   │                │
    │                 └────────────────────┘                │
    │                                                        │
    │  ┌─────────────────────────────────────────────────┐  │
    │  │            MEMORY ARCHITECTURE                   │  │
    │  │                                                  │  │
    │  │  Context braids ── ephemeral state (auto-decay) │  │
    │  │  Impulses ──────── event-driven coordination    │  │
    │  │  Handoffs ──────── session continuity docs      │  │
    │  │  Git (Forgejo) ─── inner membrane (sovereign)   │  │
    │  │  Git (GitHub) ──── outer membrane (mirror)      │  │
    │  │  fossilRecord ──── geological archive (3,831+)  │  │
    │  └─────────────────────────────────────────────────┘  │
    │                                                        │
    │  ┌─────────────────────────────────────────────────┐  │
    │  │           SOVEREIGNTY SHADOW LAYER               │  │
    │  │                                                  │  │
    │  │  BearDog TLS ──── shadow for Cloudflare :443    │  │
    │  │  Songbird TURN ── shadow for cloudflared relay  │  │
    │  │  Caddy surface ── shadow for GitHub Pages       │  │
    │  │  Forgejo ──────── shadow for GitHub repos       │  │
    │  │                                                  │  │
    │  │  Each runs alongside external, proves parity,   │  │
    │  │  then cuts over. The cage becomes the outer      │  │
    │  │  membrane when the inner membrane is ready.     │  │
    │  └─────────────────────────────────────────────────┘  │
    └────────────────────────────────────────────────────────┘
```

---

## The Generational Stack

```
    gen5 (now)    ── Does someone else's science come out?
                     External collaborators: Gonzales (NF/GPS),
                     ABG (compChem), Jones (PFAS), Barrick (LTEE)
                     Context braids, impulses, mesh coordination
                  │
    gen4 (spring '26) ── Who uses it?
                     5 products: esotericWebb, lithoSpore,
                     initioChem, blueFish, helixVision
                     BYOB composition, guideStone verification,
                     pseudoSpore/lithoSpore artifacts
                  │
    gen3 (early '26) ── Does the science work?
                     12,510+ checks, 70+ papers, 7 springs
                     14 primals, paper parity standard
                     baseCamp (18 papers), fossilRecord
                  │
    gen2 (2025)   ── What should the architecture be?
                     Composable protocol, 8 primals
                     biomeOS, primal autonomy, sovereignty
                  │
    gen1 (2024)   ── Can we build sovereign HPC?
                     $15K mesh, 11 gates, first primals
                     AI-assisted constrained evolution
```

---

## HOW / WHERE / WHAT — The Composition Principle

The same three-question decomposition appears at every scale:

```
    ┌─────────────────────────────────────────────────────┐
    │            HOW / WHERE / WHAT                        │
    │                                                      │
    │  COMPUTE TRIANGLE:                                   │
    │    WHAT: barraCuda  (math — 712+ shaders)           │
    │    HOW:  coralReef  (compile WGSL → native GPU ISA) │
    │    WHERE: toadStool (dispatch to GPU/NPU/CPU)       │
    │                                                      │
    │  PROVENANCE TRIO:                                    │
    │    WHAT: sweetGrass (attribution — who did what)     │
    │    HOW:  rhizoCrypt (DAG — event hashing)           │
    │    WHERE: loamSpine (ledger — permanent record)     │
    │                                                      │
    │  COORDINATION TRIAD:                                 │
    │    WHAT: rootPulse  (action — fire impulses)        │
    │    HOW:  quorumSignal (sense — read mesh state)     │
    │    WHERE: waterFall (sync — converge workspace)     │
    │                                                      │
    │  K-NOME:                                             │
    │    WHAT: AI         (candidates — generate code)    │
    │    HOW:  Compiler   (selection — reject unsound)    │
    │    WHERE: Human     (direction — mentoring)         │
    └─────────────────────────────────────────────────────┘
```

---

## Side-by-Side Summary

```
    THEIR SYSTEM                         OUR SYSTEM
    ────────────                         ──────────

    program.md                           context braids + handoffs
    (static spec)                        + whitePaper + impulses
                                         (living, evolving state)

    Claude Code / Codex                  Cursor + K-NOME conversation
    (autonomous agent)                   (mentored, human-in-loop)

    Edit train.py                        14 primals + 7 springs
    (one file)                           (ecosystem of composable binaries)

    Train 5 min on GPU                   barraCuda + coralReef + toadStool
    (one GPU, one metric)                (sovereign compute triangle,
                                          11 gates, multi-vendor)

    results.tsv                          12,510+ checks, 70+ papers
    (one metric)                         paper parity + guideStone

    git commit / reset                   provenance trio + fossilRecord
    (binary checkpoint)                  + context braids + handoffs
                                         (layered memory architecture)

    output: results file                 output: pseudoSpore / lithoSpore
                                         (self-verifying portable artifact
                                          with attribution braids)

    Human: absent                        Human: never leaves the loop
```
