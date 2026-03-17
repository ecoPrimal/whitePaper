# ecoPrimals Licensing Strategy

**Purpose**: The complete licensing and intellectual property strategy for the
ecoPrimals ecosystem — what we publish, how we protect it, why we own nothing,
and how symbiotic exceptions create positive feedback loops.

**Last Updated**: March 16, 2026

---

## 1. The Core Principle

**We own nothing. Knowledge that can't be un-known.**

Every line of code, every mechanical interaction, every document, every reverse
engineering finding, every methodology — published under copyleft licenses
governed by independent nonprofits. No single entity (including the author)
can close, revoke, or restrict the work after publication.

This is not idealism. It is strategy. By owning nothing, we are untargetable.
There is no revenue to disrupt, no corporate entity to sue, no publisher to
pressure, no platform to suppress. The value is in the knowledge being public,
and public knowledge cannot be un-published.

---

## 2. scyBorg: The Triple Copyleft

Every artifact in ecoPrimals falls under scyBorg:

```
scyBorg = AGPL-3.0 (code) + ORC (mechanics) + CC-BY-SA 4.0 (creative/docs)
```

| Layer | License | Covers | Governing Body | Can Be Revoked? |
|-------|---------|--------|----------------|-----------------|
| Code | AGPL-3.0-or-later | Rust source, WGSL shaders, tools, infrastructure | FSF (nonprofit) | No |
| Mechanics | ORC | Primal interactions, IPC patterns, deploy graphs, atomics, game rules | Open RPG Creative Foundation (nonprofit) | No |
| Creative | CC-BY-SA 4.0 | Papers, docs, handoffs, baseCamp, methodology, reverse engineering findings | Creative Commons (nonprofit) | No |
| Reserved | ORC Reserved Material | ecoPrimals name, primal names, logos, trade dress | Author retains | N/A |

### Why Three Layers

AGPL alone doesn't cover game mechanics or documentation. ORC alone doesn't
cover source code. CC-BY-SA alone doesn't cover software. scyBorg closes every
gap. There is no artifact in the ecosystem that lacks copyleft protection.

### Why ORC for Primal Interactions

The ORC license was created when Wizards of the Coast tried to revoke the Open
Gaming License and retroactively claim ownership of game mechanics. The tabletop
community's response: **mechanics are unownable**.

We apply the same principle to software architecture. The way toadStool
discovers hardware is a mechanical interaction. The way bearDog and songBird
compose into Tower Atomic is a mechanical interaction. The way biomeOS reads a
deploy graph and germinates primals is a mechanical interaction. ORC makes the
unownability explicit, irrevocable, and governed by a nonprofit.

If anyone claims "the method of composing primals via IPC" is proprietary
intellectual property, ORC-licensed documentation of the mechanical process
stands as a published counter-claim that the method is in the commons.

---

## 3. Lysogeny: Area Denial Through Prior Art

Lysogeny is the offensive strategy within scyBorg. It targets proprietary
systems by publishing open implementations of the same mathematics.

### The Three Layers of Protection

Every lysogeny target establishes:

1. **Prior art**: The math exists in published, peer-reviewed literature
   predating the proprietary implementation. Every equation traces to a
   specific citation.

2. **Cross-domain generality**: The same math is validated in at least two
   distinct domains. This proves it's general-purpose, not a domain-specific
   reimplementation of the proprietary system.

3. **Independent derivation**: The implementation derives entirely from
   published research. No proprietary code, APIs, or documentation referenced.

### Current Targets

| Domain | Proprietary Gate | Springs | Status |
|--------|-----------------|---------|--------|
| Game mechanics | WB Nemesis patent, Pokemon capture, gacha | ludoSpring | 6 targets, 237 checks |
| Pharmaceutical | NONMEM ($50K/seat), Monolix, WinNonlin | healthSpring | Implemented, provenance chain pending |
| GPU compute | NVIDIA CUDA lock-in, cuBLAS, f64 pricing | barraCuda + coralReef + toadStool | Active development |
| Bioinformatics | Galaxy/QIIME2 platform lock-in | wetSpring | Sovereign pipelines implemented |
| Data platforms | Palantir Ontology, Neo4j Enterprise | provenance trio | Graph fraud detection validated |

Full protocol: `wateringHole/LYSOGENY_PROTOCOL.md`

---

## 4. The Suppression Inversion

Companies suppress threatening work through three vectors. scyBorg neutralizes
all three.

### Vector 1: Direct Legal

**Traditional**: Patent infringement claims, trade secret misappropriation,
copyright on APIs/interfaces.

**scyBorg response**: Lysogeny establishes prior art predating patents.
Independent derivation from published research — no trade secrets accessed.
ORC explicitly protects mechanical interactions. *Sega v. Accolade* and
*Oracle v. Google* establish reverse engineering and API fair use precedents.
coralReef targets GPU ISAs through legitimate reverse engineering of owned
hardware, with zero vendor SDK code.

### Vector 2: Platform Suppression

**Traditional**: Pressure the hosting provider. "We aren't suppressing YOUR
first amendment — we're just telling YouTube/GitHub they can't host it."

**scyBorg response**: No single publisher to pressure. Code lives on sovereign
hardware (gates). Git is distributed — every gate has a full clone. All springs
are public repos across multiple platforms. There is no single throat to choke.
Even if all hosting platforms complied (they won't — AGPL code is legal), the
knowledge is replicated across 10+ physical machines in a basement.

### Vector 3: Commercial Pressure

**Traditional**: Target revenue, partnerships, employment. "Nice job — shame
if your employer heard you were reverse-engineering our GPU architecture."

**scyBorg response**: No revenue stream to disrupt. No corporate entity to
sue. No employer to pressure (independent). No investors to scare. No
contracts to cancel. An individual publishing AGPL open-source research from
sovereign hardware has no commercial attack surface.

### The Fourth Dimension: Diplomatic Incentive

scyBorg adds a fourth channel that lysogeny alone doesn't provide: **symbiotic
exceptions**. Instead of pure area denial, exceptions offer a path from
adversary to ally. A vendor doesn't have to fight or ignore — they can engage
and benefit.

This converts suppression targets into cooperation opportunities. See Section 5.

---

## 5. Symbiotic Exceptions

The scyBorg Exception Protocol grants additional permissions beyond the default
license to named organizations based on reciprocal benefit.

### Exception Tiers

| Tier | Who | What They Get | What ecoPrimals Gets |
|------|-----|---------------|----------------------|
| **Public** | Everyone | Full scyBorg (AGPL + ORC + CC-BY-SA) | Prior art, community, lysogeny protection |
| **Symbiotic** | Named allies | May use author's contributions under their own license | Tools, hardware, knowledge, deeper relationship |
| **Reciprocal Open** | Orgs willing to open their work | May use author's contributions under their own license | They publish their specs/docs/code under AGPL |

### Legal Basis

AGPL-3.0 Section 7 explicitly permits additional permissions. As copyright
holder, the author may grant named organizations broader rights to specific
contributions. The exception covers only the author's original code — never
upstream AGPL code from other projects.

### Key Properties

- **Not for sale**: Exceptions are granted based on symbiotic value, not payment
- **Non-exclusive**: The same code remains available to everyone under AGPL
- **Revocable**: If the reciprocal relationship ends, the exception may be revoked
- **No sublicense**: Grantee may not sublicense to third parties (default)
- **No IP entanglement**: Partners don't need MOUs, tech transfer offices, or
  legal departments to engage

### Active Candidates

**RustDesk**: ecoPrimals' remote access tool since gen2. Fork improvements
flow back under their AGPL-3.0. Symbiotic: we improve their tool, they
maintain the infrastructure we depend on.

**BrainChip (Akida)**: rustChip (pure Rust AKD1000 driver) is 100%
author-owned code. Exception lets BrainChip use it in proprietary products.
Symbiotic: they make the NPU hardware, we make a driver they didn't build.

**GPU Vendor (precedent-setting)**: If a vendor publishes their GPU
architecture documentation under AGPL, they receive an exception to use
coralReef's sovereign compiler in their toolchain. The incentive: openness
earns openness.

### The Positive Feedback Loop

```
Publish under AGPL → Partner provides value → Grant exception →
Partner improves → ecoPrimals benefits → Publish more → Cycle deepens
```

Each successful exception validates the model for the next potential partner.
The pattern creates a growing ecosystem of symbiotic relationships, all
anchored to the AGPL commons.

Full protocol: `wateringHole/SCYBORG_EXCEPTION_PROTOCOL.md`

---

## 6. Self-Publication Model

ecoPrimals is already published. Every spring is a public GitHub repository
under AGPL-3.0. The code is the publication — reproducible by definition
because it IS the implementation.

### The Inverted Pipeline

| Traditional | ecoPrimals |
|-------------|-----------|
| Write paper → submit → wait 6mo → revise → resubmit → wait → paywall | Publish code + data + methodology → seek review → reviewer validates output |
| Reviewer sees claims | Reviewer runs code |
| Publication costs $2,000+ in APCs | Publication costs $0 (git push) |
| Paper behind paywall after publication | Code permanently open under AGPL |
| Reviewers donate labor to publisher | Reviewers' cost reduced to curiosity |

### Faculty Review as Validation

The faculty anchor strategy reduces the cost of external review to curiosity:

- The work already exists and runs
- The reviewer doesn't need to co-author, supervise, or allocate grant money
- They check whether a Rust implementation reproduces their published results
- An afternoon of verification, not months of collaboration
- scyBorg licensing means zero IP entanglement for their university

Each faculty anchor validates a domain slice. The aggregate creates a
multi-domain validation record that no single reviewer could provide:

| Faculty Anchor | Domain | Spring | What They Validate |
|----------------|--------|--------|-------------------|
| TC Chuna | Gradient flow (physics) | hotSpring | Whether the Rust implementation reproduces published gradient flow results |
| Michael Murillo | Plasma physics | hotSpring | Yukawa MD, Ewald sums, pair distribution functions |
| Alexei Bazavov | Lattice QCD | hotSpring | Wilson gauge action, HMC algorithm, lattice measurements |
| Chris Waters | Quorum sensing | wetSpring | LuxR/LuxI dynamics, biofilm formation models |
| Ilya Kachkovskiy | Spectral theory | groundSpring | Anderson localization, spectral measures |
| Andrea Gonzales | Pharmacology | healthSpring | PK/PD models, dose-response curves |
| Younsuk Dong | Precision agriculture | airSpring | Soil models, crop response functions |

---

## 7. The Complete Defense Architecture

Five layers, each independent, together comprehensive:

```
Layer 1: LYSOGENY (Math)
    Prior art → independent derivation → cross-domain proof
    Result: Math cannot be patented

Layer 2: SCYBORG (Implementation)
    AGPL-3.0 + ORC + CC-BY-SA 4.0
    Result: Code, mechanics, docs cannot be closed

Layer 3: PROVENANCE TRIO (Evidence)
    sweetGrass (attribution) + rhizoCrypt (derivation) + loamSpine (certificates)
    Result: Violations are provable, attribution is automatic

Layer 4: SOVEREIGNTY (Infrastructure)
    Sovereign hardware + no platform dependency + no corporate entity
    Result: No attack surface for suppression

Layer 5: TRANSPARENT AI AUTHORSHIP
    Full disclosure + copyleft + no revenue dependency
    Result: Copyright uncertainty becomes an asset, not a liability
```

An attacker must defeat all five layers simultaneously. No single vector
(legal, platform, commercial, or copyright) is sufficient because no single
layer is the sole defense. Layer 5 is unique: an attacker who *succeeds* in
defeating the copyright basis (proving AI work is not copyrightable) has
pushed the work into public domain — a stronger form of openness than
copyleft itself.

### The Immunological Metaphor

- **AGPL**: Adaptive immune response — forces openness of derivatives
- **ORC**: Innate immune response — mechanical concepts constitutionally unownable
- **CC-BY-SA**: Memory B-cells — documentation persists and propagates
- **Lysogeny**: The viral DNA that integrates and can't be removed
- **Sovereignty**: The skin — no external surface to penetrate
- **Exceptions**: Symbiotic organisms — allies that strengthen the host
- **AI Transparency**: The fever — attacking it makes the host stronger

---

## 8. AI-Assisted Authorship: The Copyright Paradox

Every line of code, every document, every essay in ecoPrimals was produced
through AI-assisted constrained evolution. 69,000 agent invocations. 51
billion tokens. The methodology is described in `about/README.md` and
formalized in `CONSTRAINED_EVOLUTION_FORMAL.md`. This is not hidden. It is
stated openly, with a receipt.

This transparency creates a legal paradox — but only for other people.

### The Unsettled Law

Copyright law in most jurisdictions requires human authorship. The U.S.
Copyright Office has stated that works generated by AI without significant
human creative input may not be copyrightable. The boundary between
"AI-generated" and "AI-assisted with human direction" is legally undefined
and actively contested (Thaler v. Perlmutter, 2023; ongoing Copyright Office
rulemaking, 2024–2026).

The key ambiguity: if a human directs the AI extensively — providing
architecture, constraints, selective pressure, domain knowledge, and iterative
refinement — is the result copyrightable? Nobody knows yet. The courts and
regulators are still working it out.

### Why This Is Everyone Else's Problem

Consider two parties:

| | ecoPrimals | A Proprietary Competitor |
|---|---|---|
| **Uses AI?** | Yes, openly documented | Yes (probably), undisclosed |
| **Claims copyright?** | Applies copyleft (AGPL, CC-BY-SA) | Claims exclusive copyright |
| **Revenue from copyright?** | None, by design | Entire business model |
| **If AI work is copyrightable** | AGPL applies, copyleft propagates, commons protected | Their copyright holds, business continues |
| **If AI work is NOT copyrightable** | Work enters public domain — which is what we wanted anyway | Their copyright claims collapse, business model fails |
| **Worst case** | Exactly the same outcome we intended | Total loss of IP portfolio |

ecoPrimals is positioned to win either way the law lands:

- **If AI-assisted work IS copyrightable**: The AGPL, ORC, and CC-BY-SA
  licenses are valid. The copyleft propagates. The commons is legally
  protected. Business as usual.

- **If AI-assisted work is NOT copyrightable**: The work enters the public
  domain. It cannot be enclosed, cannot be licensed, cannot be restricted.
  This is *a stronger version of what we already wanted*. Public domain is
  even more unencloseable than AGPL.

The only party harmed by a ruling that AI-assisted work is not copyrightable
is a party that depends on copyright exclusivity for revenue. ecoPrimals has
no such dependency.

### The Disclosure Advantage

Most companies using AI for development are quiet about it. They have to be —
acknowledging AI assistance raises questions about the copyrightability of
their output, which threatens their IP portfolio.

ecoPrimals discloses everything. The Cursor receipt. The agent invocation
count. The methodology paper describing how AI fits into constrained
evolution. This disclosure is not a vulnerability. It is a moat:

1. **No hypocrisy to expose**: There is no hidden AI usage to reveal.
   Investigative journalism, litigation discovery, or competitive attack
   cannot produce a scandal because the information is already public.

2. **Precedent positioning**: If courts do rule on AI-assisted copyrightability,
   ecoPrimals is the rare case with full documentation of exactly how the
   human directed the AI. The constrained evolution methodology — human
   provides the constraint environment and selective direction, AI provides
   the mutation, compiler provides natural selection — is a stronger case for
   human creative input than "I prompted ChatGPT."

3. **Suppression inversion (again)**: Anyone who attacks ecoPrimals' copyright
   status on AI grounds is arguing that the work is public domain. That
   argument *helps* us. The attacker would be spending legal resources to
   achieve the outcome we already chose.

### The Industry's Problem

The broader AI-assisted development ecosystem faces a reckoning that
ecoPrimals has already resolved:

- **Corporations** using AI for code generation are building IP portfolios on
  legally uncertain foundations. Every AI-assisted patent, every copyrighted
  AI-assisted codebase, every proprietary AI-trained model is vulnerable to a
  future ruling that undermines the copyright basis.

- **Open-source projects** using AI assistance face the same question but with
  lower stakes — if the copyright is invalid, the permissive license doesn't
  matter anyway (the work is public domain regardless).

- **Copyleft projects** (like ecoPrimals) face effectively zero risk. The
  copyleft either applies (copyright valid) or is unnecessary (public domain).
  Either outcome keeps the knowledge in the commons.

The entities with the most to lose are the ones claiming exclusive ownership
of AI-assisted output. ecoPrimals claims no exclusive ownership of anything.
The legal uncertainty is structural risk for the tollbooth economy and
structural irrelevance for the commons.

### Layer 5: Transparent AI Authorship

This adds a fifth layer to the defense architecture:

```
Layer 5: TRANSPARENT AI AUTHORSHIP
    Full disclosure + copyleft + no revenue dependency
    Result: Copyright uncertainty becomes an asset, not a liability
```

An attacker now faces five independent layers. Even if they defeat the
copyright basis entirely (Layer 5 scenario: AI work not copyrightable), they
have achieved public domain — which is a stronger version of the commons we
already built.

---

## 9. What This Means Practically

### For the Author

- Everything published is permanently open
- No revenue from licensing, by design
- No institutional dependency for publication
- No platform dependency for distribution
- Credibility earned through running code + faculty validation, not journal prestige
- Symbiotic exceptions create relationships that deepen the work

### For Faculty Anchors

- Zero cost to engage (review existing work, not build new work)
- Zero IP entanglement (AGPL + ORC + CC-BY-SA, no MOU needed)
- Their published results validated independently in a new language/platform
- Citation of their work propagates through the ecosystem

### For Potential Partners (RustDesk, BrainChip, etc.)

- Free improvements to their tools/hardware from a power user
- Exception removes AGPL friction for their use case
- No contract, no negotiation, no legal department
- Reciprocal relationship that deepens over time

### For Large Vendors (NVIDIA, AMD, etc.)

- Sovereign implementations of their abandoned hardware architectures
- A Rust-native compiler for hardware they stopped supporting
- Path to engagement (reciprocal open exception) rather than confrontation
- Precedent: openness earns openness

### For the Commons

- Every publication is permanent and unencloseable
- Every exception increases the ecosystem's value without reducing the commons
- Every faculty validation increases credibility without institutional gatekeeping
- Every symbiotic relationship creates incentive for the next

---

## References

### Internal
- `wateringHole/SCYBORG_PROVENANCE_TRIO_GUIDANCE.md` — triple license framework
- `SCYBORG_EXCEPTION_PROTOCOL.md` — symbiotic exception protocol (this directory)
- `OWN_NOTHING.md` — the ownership inversion (this directory)
- `wateringHole/LYSOGENY_PROTOCOL.md` — area denial strategy
- `wateringHole/GLOSSARY.md` — ecosystem terminology
- `atlasHugged/09_I_OWN_NOTHING.md` — philosophical companion essay

### External
- AGPL-3.0: https://www.gnu.org/licenses/agpl-3.0.html
- AGPL-3.0 Section 7 (additional permissions): https://www.gnu.org/licenses/agpl-3.0.html#section7
- ORC License: https://azoralaw.com/orclicense/
- CC-BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/
- *Sega v. Accolade* (reverse engineering for interoperability): 977 F.2d 1510 (9th Cir. 1992)
- *Oracle v. Google* (API fair use): 593 U.S. 1 (2021)
