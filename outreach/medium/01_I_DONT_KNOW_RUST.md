# I Don't Know Rust

*How a microbiologist built a scientific computing ecosystem through conversation*

**By**: attsi | ecoPrimal
**Status**: Draft — evolving document
**Published**: [pending]

---

I don't know Rust. It's not on my resume. I have a BS in microbiology and an
MS in data science. My programming background is logic, algorithms, and
pseudocode — Java in a previous life, Python for data science, nothing
systems-level.

I chose Rust *because* I didn't know it.

Over the past two years, working entirely through conversation with AI
instances in a code editor, I've built: 14 composable services. 8 scientific
validation frameworks. 27,000+ tests. 70+ published scientific papers
reproduced from scratch. A cryptographic provenance pipeline that traces
every computation from raw data to attributed result. A security validator
that pen-tests, fuzzes, and crypto-audits its own ecosystem. A multi-user
compute platform serving real researchers.

Every function, every trait implementation, every test, every GPU shader,
every build script — all of it was produced by AI, mentored through
conversation by a person who does not know the language the code is written in.

This is not a technicality. It is the design.

---

## Why Not Know the Language

When I started this project, I was looking for a systems language. I'd read a
developer's argument that Rust's compiler is the most aggressive constraint
available — it catches categories of bugs that other languages allow to exist.
Memory safety without a garbage collector. Ownership semantics that enforce
discipline at compile time. If the code compiles, entire classes of runtime
failure simply cannot occur.

I realized I would be *better off* in a language I didn't know. The
unfamiliarity would force me to stay in conversation rather than reaching into
the code to fix things manually. Every instinct to open a file and tweak a
variable would be blocked by the fact that I couldn't read the syntax well
enough to know what I was changing. The only path forward was to describe what
I wanted and let the AI find the implementation.

The constraint was chosen deliberately. It could have been any language. Rust
was ideal because its compiler is the strictest available teacher. Every
compilation error is a lesson in systems thinking, delivered to the AI, which
I then evaluate for correctness of *intent* rather than correctness of *syntax*.

I am the selection pressure. The AI is the generator. The compiler is the
environment. This is not metaphor — this is literally how constrained
evolution works in biology: environmental pressure (the compiler) shapes the
fitness landscape, selection pressure (human direction) determines what
survives, and the generator (AI) produces variation.

The project's methodology is an instance of its own theory.

---

## What "Conversation" Means in Practice

I do not type code. I do not debug in a terminal. I do not use IDE refactoring
tools. Every interaction with the codebase passes through conversation with an
AI instance.

A typical session: I describe a goal ("we need a security validator that runs
pen tests against all 13 services, fuzzes their protocols, and checks crypto
strength"). The AI proposes an architecture. I evaluate the architecture
against my domain knowledge — not Rust knowledge, but knowledge of what
security validation means, what threat actors look like, what a rigorous check
proves. I redirect. The AI implements. The compiler catches the mechanical
errors. The tests catch the logical errors. I catch the conceptual errors.

The human contribution is direction, taste, domain knowledge, and quality
judgment. The AI contribution is implementation, pattern recognition, and
tireless generation. Neither half works alone. The conversation is the
development environment.

This is not "vibecoding" — the term Andrej Karpathy coined for prompting
loosely and accepting whatever the AI outputs. There is nothing loose about
this. Every architecture decision is debated. Every test is evaluated for what
it actually proves. Every security check is assessed against real threat
models. The human doesn't need to know Rust to know whether a pen test is
rigorous, whether a provenance chain is sound, or whether a scientific
computation reproduces a published result.

---

## What Came Out

The numbers tell one story. The coherence tells another.

**14 services** — composable "primals" that communicate over a custom encrypted
protocol (BTSP, using ChaCha20-Poly1305 AEAD). Each is a single static Rust
binary with no runtime dependencies. They compose into configurations:
a "Tower" handles identity and networking, a "Node" handles compute, a "Nest"
handles storage and provenance. Full stack is all three plus AI coordination
and orchestration.

**8 scientific validation frameworks** ("springs") — each reproduces published
science in a specific domain: microbiology and metagenomics (1,902 tests),
plasma physics and lattice QCD (990 tests), agricultural hydrology (1,364
tests), machine learning and surrogates (1,403 tests), uncertainty
quantification (1,050 tests), human health and pharmacometrics (940 tests),
game science and HCI (791 tests), and a master coordination framework (404
tests).

**70+ published papers reproduced** — not "our tests pass" but "we get the same
numbers as the published science." Anderson localization in microbial
communities. Dynamical lattice QCD on consumer GPUs. FAO-56
evapotranspiration across 100 Michigan weather stations. Drug repurposing
pipelines. Neuromorphic edge inference on real BrainChip hardware. Each
reproduction deposits a cryptographic layer of provenance: what data went in,
what computation ran, what result came out, who was involved, when it happened.

**175 PASS, 0 FAIL, 6 DARK_FOREST** — the security validator (darkforest,
v0.2.0, pure Rust, 939KB) runs 181 checks against the live system: pen tests
simulating three threat actors (external attacker, authorized user, restricted
observer), protocol fuzzing for all 13 services plus JupyterHub, and 13
cryptographic strength checks (cookie entropy, shadow hashing, token
tampering, cipher negotiation, file permissions). It produces structured JSON
reports for audit.

**Real users** — a multi-user JupyterHub serves an external bioinformatics
research group through a Cloudflare tunnel. Four tiers of access (admin,
compute, reviewer, observer), each with mechanism-level enforcement — not
configuration flags, but filesystem permissions, kernel blocking, iptables
rules, and ACLs. The reviewer can see published dashboards but cannot execute
code. The compute user can run science but cannot access the internet. Every
restriction is enforced by the operating system, not by trust.

---

## What It Costs

This runs on consumer hardware in a basement. The primary node is an
i9-14900K with an RTX 4070 and 96 GB of DDR5. The full cluster is about $15K
in hardware accumulated over two years.

There is no VC funding. No grant. No institutional backing. One person pays
the electricity. The economics are designed to change — the system includes
an attribution pipeline so that when community contributions start flowing,
credit and eventually value flow back to contributors. But right now, the
honest answer is: one person pays.

---

## The Recursive Part

Here is what I find genuinely interesting about this project, and why I'm
writing about it rather than just releasing the code:

The methodology used to build the system is an instance of the theory the
system embodies. The theory says: environmental constraints reshape fitness
landscapes and drive specialization. Organisms don't evolve randomly — they
evolve under pressure, and the pressure determines the shape of what
emerges.

Rust's compiler is the environmental pressure. My domain knowledge (five
years of bench microbiology, fermentation, BSL2 work, bioreactors, a
Master's in data science) is the selection pressure. The AI is the
generator. What emerged is a scientific computing ecosystem that couldn't
have been designed top-down — it was grown under constraint, and the
constraints gave it its shape.

This is not a proof of the theory. But it is a worked example, running in
production, serving real users, with every line of code traceable to a
conversation between a human who doesn't know the language and an AI that
doesn't know the science.

---

## Try It

Everything is public. Everything is AGPL-3.0.

- **Deployment repo**: github.com/sporeGarden/projectNUCLEUS
- **All services**: github.com/ecoPrimals
- **Live JupyterHub**: lab.primals.eco
- **Security results**: 175 PASS, available as structured JSON

If you have hardware and curiosity, you can deploy it. If you find something
wrong, the attribution system will record your contribution. If you reproduce
a paper on your own machine and get the same numbers, that's another layer of
validated computation added to the geological record.

The repos are open. The provenance is transparent. Run it yourself.
