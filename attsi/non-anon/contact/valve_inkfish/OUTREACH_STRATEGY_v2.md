# Outreach Strategy v2 — The Pivot

**Previous strategy**: Software pitch. "Here's my platform, let's talk."
**New strategy**: Scientist application. "I'm a microbiologist who brings
his own compute. Let me aboard."

---

## The Realization

The original pitch framed Kevin as a software developer reaching out to
Valve about infrastructure. That's backwards. Kevin is a **microbiologist
with 5 years of wet lab experience** who happens to have also built the
most complete sovereign genomics platform on Earth.

The pitch should be: "I want to do science on your vessels. I bring my
own compute."

---

## Why This Works

1. **Inkfish needs scientists, not software vendors.** They have 74 employees
   but only 3 in "Research." Most science is done by external collaborators.
   With RV6000 (70 berths, 2028) and RV11000 (130 berths, 2030), they're
   about to have massive capacity for more scientists.

2. **Kevin's wet lab skills are directly relevant.**
   - Microbial ecology (rumen, algae, plant pathology, PFAS)
   - BSL2 aseptic technique, DNA extraction, sample preservation
   - eDNA sampling is microbiology — filtration, preservation, QC
   - Coral holobionts ARE microbial ecosystems
   - Deep-sea chemosynthetic communities ARE microbiology

3. **The compute is a bonus, not the pitch.**
   Every other bioinformatician needs shore-side HPC access and weeks of
   turnaround. Kevin can run DADA2 on the vessel's own hardware. That's
   not the reason to bring him — it's the reason to bring him first.

4. **The cost is absurd.** Kevin's ongoing development costs are near-zero
   (AI-assisted, personal hardware). A patron/sponsor arrangement —
   berth + wet lab access + consumables — is cheaper than a single
   contracted bioinformatician AND provides ongoing platform evolution.

5. **Military background matters for expedition life.** Three years active
   duty infantry. Comfortable in confined spaces, extended deployments,
   strict chain of command, austere conditions.

---

## Approach Paths (Ranked)

### Path 1: Direct to Gabe (Preferred)

**Channel**: gaben@valvesoftware.com
**Why**: Gabe reads email. He's accessible. He cares about the science.
He's the decision-maker for Inkfish's direction.

**Email structure**:
- Lead: "I'm a microbiologist. I want to do science on your vessels."
- Middle: "I built my own compute stack — it runs on any GPU, offline."
- Close: "I cost less than your current shore-side HPC bill."
- P.S.: Kevin's Steam ID

### Path 2: Through Pim Bongaerts

**Channel**: LinkedIn InMail or Cal Academy email
**Why**: Pim is the lead scientist. He decides who's on his team.
He'd immediately understand the value of on-vessel bioinformatics.

**Email structure**:
- Lead: "I'm a microbiologist (MSU) following your mesophotic work."
- Middle: "I built a GPU-accelerated 16S pipeline for field conditions."
- Close: "Could your team use a microbiologist who brings compute?"

### Path 3: Both simultaneously

**Email to Gabe with Pim in CC.** This is risky (Pim might not
appreciate being CC'd on a cold email to the owner) but signals
confidence and shows homework.

### Path 4: LinkedIn engagement first

**Build relationship with Pim** by commenting substantively on his
expedition posts (he's active on LinkedIn). Build visibility before
the cold email. Slower but more likely to get a warm reception.

---

## What Kevin Is Asking For

Be explicit and specific:

1. **A berth on an upcoming expedition** — as a wet lab scientist
   focused on marine microbiome/eDNA sampling
2. **Access to wet lab facilities** — DNA extraction, eDNA filtration,
   sample preservation, microbial analysis
3. **Permission to run bioinformatics on vessel hardware** — demo
   the GPU pipeline on real expedition data
4. **Patron/sponsor arrangement** — not a salary, not a contract.
   Support for a scientist who brings his own tools.

What Kevin is NOT asking for:
- Investment in ecoPrimals
- A job at Valve
- Help selling software
- A press release

---

## The Underwater Computing Vision

This is the moonshot that Kevin should NOT lead with, but should have
ready if the conversation goes well:

- songBird mesh networking works at the transport level — TCP, UDS,
  abstract sockets. Acoustic underwater transport is just another
  transport adapter.
- nestGate CAS works with any storage substrate — ZFS, HDD, even
  flash arrays in underwater housings.
- Tower Atomic's edge profile (30MB RSS) could run on embedded
  hardware in buoys, autonomous underwater vehicles, or submersible
  sensor packages.
- The deployment fabric (cellMembrane) handles arbitrary hardware
  enrollment — including hardware that comes and goes as vessels
  transit.

**Sovereign underwater mesh computing** is not a marketing fantasy.
It's the logical extension of what's already running on 8+ gates.
The ocean is just another network topology.

---

## Timeline

| Phase | Action | When |
|-------|--------|------|
| **NOW** | Build out Inkfish profiles, research their science | July 2026 |
| **NOW** | Prepare resume (Inkfish-targeted version) | July 2026 |
| **SOON** | Engage Pim Bongaerts on LinkedIn (comment, follow) | Aug 2026 |
| **SOON** | Identify a public Inkfish dataset for demo processing | Aug 2026 |
| **SEND** | Email to Gabe (and/or Pim) with demo results | Sep 2026 |
| **FOLLOW** | If positive: propose expedition berth for 2027 or 2028 | Oct 2026 |

RV6000 delivers Q2 2028. That's the inflection point when Inkfish
dramatically increases their scientist capacity. Getting in before
that — on Hydra or Dagon — is the goal.

---

## What Makes This Different From Every Other Pitch Gabe Gets

Gabe Newell receives pitches from:
- VCs who want to invest
- Startups who want Steam distribution
- Researchers who want funding
- Journalists who want access

Kevin's pitch is none of these:
- **Not asking for money** — asking for a berth and wet lab access
- **Not selling software** — bringing tools as a scientist, not a vendor
- **Not asking for distribution** — the code is AGPL, anyone can use it
- **Not asking for press** — asking for work

The differentiation is: "I'm a scientist who wants to do science. The
compute is just what I happen to bring, like a diver bringing their own
rebreather."

---

*Strategy v2 created July 29, 2026. Previous strategy preserved in README.md.*
