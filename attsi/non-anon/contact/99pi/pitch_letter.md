# Pitch Letter — 99% Invisible

**To:** Roman Mars / 99% Invisible editorial team
**From:** Kevin Mok
**Subject:** The most important enzyme in molecular biology came from near-boiling water — I used the same principle to build software

---

## Letter

Dear Roman and team,

The enzyme that made modern genomics possible — Taq polymerase, the
foundation of PCR and every COVID test on Earth — evolved in a
bacterium called *Thermus aquaticus*, which lives in near-boiling
water in Yellowstone hot springs. The extreme heat didn't destroy
life. It produced the single most useful protein in molecular biology.

The constraint was the design.

I'm a microbiologist and data scientist (MS, Michigan State, 2025),
and I spent the last 10 months applying that principle to software.
Not as metaphor — as methodology.

Here's what I did: I gave an AI the ability to write code, then I
gave it the most aggressive constraints I could find. A programming
language (Rust) where the compiler rejects anything that might
corrupt memory, crash at runtime, or access data it shouldn't. A
rule that forbids every line of code written in C — the language
behind almost every major security vulnerability of the last 30
years, including Heartbleed, which compromised two-thirds of the
internet's encrypted traffic. A requirement that every piece of
physics the code computes must match published scientific results.

Then I let evolution run.

69,000 iterations. 10 months. One person, working alone in a
basement in Michigan with $15,000 worth of used computer hardware
bought off eBay and Craigslist.

The result: 14 independent software services that discover and
coordinate with each other using a universal standard — like the
shipping container standard that transformed global trade, but for
computing. An AI coordination system. A GPU shader compiler written
entirely without the GPU manufacturer's official tools. Seven
science validation suites that reproduce published physics. And a
$4,000 machine, assembled from secondhand graphics cards, that
detects the same phase transition in quark matter that was first
observed at Brookhaven National Laboratory's Relativistic Heavy Ion
Collider — a $2 billion facility.

Everything is open-source under a license (AGPL-3.0) that functions
like a building code: you can build anything you want with it, but
whatever you build must remain open and inspectable. The license
isn't legal boilerplate. It's a load-bearing structural element, the
way a building code isn't a bureaucratic constraint but the reason
your apartment doesn't collapse.

I've listened to 99% Invisible for most of a decade. Your show
taught me to look for the design decisions that are more interesting
than the things they produce. I believe this is one of those stories.

Not because the technology is impressive — though it is — but because
every powerful decision in the system is invisible:

- A universal capability API that lets 14 services discover each
  other at runtime, the way the shipping container standard lets any
  ship dock at any port without negotiation.

- A single line of code — `#![forbid(unsafe_code)]` — that makes an
  entire class of security vulnerability structurally impossible, the
  way banning asbestos doesn't limit what you build but eliminates a
  category of failure.

- A methodology borrowed from evolutionary biology that says: don't
  design the solution, design the constraint, and let the solution
  emerge — the way desire paths emerge from pedestrians navigating a
  lawn, not from a landscape architect's blueprint.

The story I'd like to tell your listeners is not about software. It's
about what happens when you take the 99% Invisible thesis — that the
invisible is where the true power lies — and apply it as an
engineering principle.

The full codebase is public. The commit history records every one of
the 69,000 iterations. The physics reproductions are being reviewed
by the researchers whose papers I reproduced, at Michigan State.
Everything is verifiable.

I'm available at your convenience. Happy to talk by phone, video,
or in person.

Kevin Mok
Michigan State University, MS Data Science (2025)
https://github.com/ecoPrimals
https://github.com/syntheticChemistry

---

## Pitch Notes (internal — not sent)

### What to include in submission

- This letter (adapted for their submission form or email)
- Links to 2-3 public repos as evidence (Squirrel, hotSpring, BarraCuda)
- A one-paragraph bio
- No attachments — let them explore the repos

### Follow-up angles if they express interest

- Offer a 20-minute call to walk through the invisible architecture
- Offer access to the white paper (private repo, can grant read access)
- Offer to demonstrate the $4K lattice QCD machine live

### Why this pitch vs. the old one

The old pitch (`outreach/AN_INVITATION_TO_99_PERCENT_INVISIBLE.md`)
was anonymous, flowery, and abstract. It talked about "a new kind of
digital universe" and offered to "break my anonymity." It had no
specifics, no credentials, no verifiable claims.

This pitch is:
- **Named and credentialed** (Kevin Mok, MS Michigan State)
- **Factual** (69,000 iterations, $4,000 machine, 14 services)
- **Grounded in their language** (shipping containers, building
  codes, desire paths, maintenance — all 99pi episode concepts)
- **Verifiable** (public repos, commit history, Cursor receipt)
- **Structured as a story** (Taq polymerase -> constraint -> result)
  rather than a sales pitch

### 99pi episodes to reference in conversation (not in the letter)

- Episode 218: The Shipping Container (capability API parallel)
- Episode 181: Desire Lines (constrained evolution parallel)
- Episode 194: The Landlord's Game (rules creating systems)
- Episode 307: Curb Cuts (small decisions, cascading consequences)
- Episode 160: The Nutshell Studies (one person, alone, building
  something that becomes foundational)

---

*Pitch letter prepared March 16, 2026. Send after Squirrel public + Chuna validation.*
