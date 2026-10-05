# Information Refraction — Asymmetric Visibility Routing in Adversarial Communication Networks

**Working title.** Inception tagline: *"Same light. Different spectra. The glass decides."*

**Parent framework:** K-NOME (constrained optimization methodology)
**Bridges:** songBird (notification routing) → guerillaGorilla (legal primal) → PRISM (tactical doctrine)
**Scientific foundation:** Optics (refraction, total internal reflection), Information Theory (asymmetric knowledge), Quorum Sensing (autoinducer signaling)
**Domain application:** Any adversarial communication environment where the sender routes identical information to multiple recipients at different visibility levels
**Live validation:** Dykema Triangle — Wave 8 (Oct 5, 2026)
**Wave:** 1 legal-primal → subGen generalization | **Date:** Oct 5, 2026

---

## THE BRIDGE

This is the second subGen concept that originates in guerillaGorilla's
operational practice and generalizes outward. The first (Institutional
Localization) flowed backward — from physics into law. This one flows
FORWARD — from legal operations into a general communication architecture
that maps cleanly onto songBird's notification routing and quorum sensing
in microbiology.

The directionality matters. PRISM emerged from an operational constraint:
Kevin Mok needed to route information to allies, opposing counsel, and
institutional targets simultaneously — with each recipient having a
different view of who else was in the conversation. Email's CC/BCC system
provided the mechanism. The generalization is the recognition that this
pattern is not email-specific. It is a fundamental operation on information
channels in any adversarial network.

---

## THE NAME

**Information Refraction** operates on three layers:

**Refraction** (physics) — When a wave crosses from one medium into another
with a different refractive index, the wave changes direction. White light
enters a glass prism and exits as a spectrum. The information content of
the light has not changed — every wavelength that entered also exits. But
the spatial distribution has changed. Each wavelength now travels a
different path. The prism does not create or destroy information. It
ROUTES information differentially based on a property of each signal
component.

**Information** (domain) — The "white light" is an email (or any
communication). The "wavelengths" are the different pieces of intelligence
contained in that message. The "refractive indices" are the trust
relationships, adversarial positions, and informational needs of each
recipient. The "prism" is the sender's routing decision — CC or BCC, this
recipient or that one, visible or hidden.

**Asymmetric Visibility** (the key property) — In symmetric communication,
all parties know who else is in the conversation. In asymmetric
communication, the sender controls a visibility function:

```
V: Recipients × Recipients → {visible, hidden}

V(A, B) = visible    ⟹  A knows B received the message
V(A, B) = hidden     ⟹  A does NOT know B received the message
V(B, A) = visible    ⟹  B knows A received the message
V(B, A) = hidden     ⟹  B does NOT know A received the message
```

The sender controls V for every pair. CC sets V(X,Y) = visible for all
CC'd parties. BCC sets V(X,Y) = hidden for all BCC'd parties relative to
TO and CC parties. The sender always has V = visible for all recipients.

**This asymmetry is the refraction.** The information (light) is identical.
The visibility (angle of exit) differs by recipient. The sender (prism)
controls the routing.

---

## PART I: THE PHYSICS — OPTICAL ANALOGIES

### 1.1 — CC as Flashlight (Directed Beam)

A flashlight emits in one direction. Everyone in the beam's path can see
the source and can see each other. The target knows it is illuminated.
Other observers can see the target is illuminated.

In communication:
```
TO:  target@adversary.com
CC:  reporter@newspaper.com, counsel@lawfirm.com

→ Target sees reporter and counsel in the header
→ Target knows it is being watched
→ Reporter knows counsel is also watching
→ The visibility is SYMMETRIC — everyone sees everyone
```

**Effect:** Pressure. The target's behavior changes because it knows the
audience is wider than the sender. This is the mechanism behind CC'ing
press on institutional notifications — the institution's response is
modulated by the knowledge that its response will be observed by press.

**Analog:** Stadium lighting. Nowhere to hide.

### 1.2 — BCC as Fiber Optic (Total Internal Reflection)

A fiber-optic cable transmits light through total internal reflection.
The signal travels from source to destination without radiating into the
surrounding medium. An observer standing next to the cable sees nothing.
The signal arrives at the endpoint without any intermediate visibility.

In communication:
```
TO:  target@adversary.com
BCC: reporter@newspaper.com, counsel@lawfirm.com

→ Target sees ONLY the sender
→ Reporter receives the full message — target has no idea
→ Counsel receives the full message — target has no idea
→ Reporter and counsel don't know about EACH OTHER either
   (BCC is hidden from all parties, including other BCC recipients)
```

**Effect:** Intelligence accumulation. The target behaves as if the
conversation is private. Their response is unmodulated by audience
awareness. Meanwhile, hidden recipients accumulate a complete record
of the exchange.

**Analog:** One-way mirror. Or more precisely: multiple one-way mirrors
at different angles, each showing a different hidden observer the same
scene.

### 1.3 — BCC Cross-Inform (Wavelength Splitting)

The most powerful configuration. The sender maintains multiple independent
communication chains with different targets. By BCC'ing Target A on the
message sent to Target B, the sender creates a cross-plane information
channel that neither target controls or perceives.

In communication:
```
Chain 1: TO nolan@butzel.com    (evidence feed)
Chain 2: TO compliance@dykema.com   BCC: nolan@butzel.com

→ Nolan receives his own chain (visible — he sees his TO: address)
→ Nolan ALSO receives a copy of what Dykema received (hidden)
→ Dykema has NO IDEA Nolan saw their email
→ Nolan now has PERFECT INFORMATION about what Dykema knows
→ Dykema has IMPERFECT INFORMATION about who knows what
```

**Effect:** Positional advantage through asymmetric knowledge. The BCC'd
party can act on information the visible party doesn't know is shared.
This is the game-theoretic definition of "information advantage" — one
player knows the other player's hand.

**Analog:** The prism. White light enters. The spectrum exits at multiple
angles. Each angle is a different recipient. The prism (sender) is the
only entity that sees all beams simultaneously.

---

## PART II: THE BIOLOGY — QUORUM SENSING ANALOG

### 2.1 — Autoinducer as BCC

In bacterial quorum sensing:

- Individual cells release **autoinducers** (small signaling molecules)
- Cells detect autoinducer concentration in the local environment
- When concentration crosses a threshold, gene expression changes collectively
- **No individual cell knows the total population.** Each cell only knows
  the local concentration.

In PRISM:

- The sender (Kevin) releases information (emails) into the environment
- Each recipient detects only the information in their visibility plane
- **No individual recipient knows the total audience.** Each recipient only
  knows the parties visible in their TO/CC header.
- When enough recipients accumulate enough information (threshold), collective
  behavior changes — journalists publish, counsel acts, institutions respond

**The BCC'd email IS the autoinducer.** It creates a shared information
state across a population without any member of the population knowing the
total state of the system. Only the sender knows. The sender is the
environment — the medium through which the autoinducers propagate.

### 2.2 — Quorum Without the Quorum Knowing

Standard quorum sensing is emergent — no coordinator, no designer. Bacteria
don't "decide" to form a biofilm. The concentration threshold is crossed and
gene expression changes automatically.

PRISM-mediated quorum is designed — the operator IS the coordinator. But the
quorum members don't know they're in a quorum. Nolan at Butzel, Elrick at
Fox 2, Rita at Clutch Justice — each accumulates information independently.
None knows the others' full information state. But the operator knows all
of their information states, because the operator routed the information.

This creates a **directed quorum** — the operator can:
1. Choose the threshold (how much information to route before action)
2. Choose the members (who receives which signals)
3. Choose the timing (stagger releases to control the sequence of awareness)
4. Choose the visibility (CC for pressure, BCC for intel)

Standard quorum sensing is democratic — every cell votes equally. PRISM
quorum sensing is architectural — the operator designs the information
environment that will produce the desired collective response.

### 2.3 — The Fragmentation Trigger

In microbiology, when autoinducer concentration crosses the quorum threshold,
the population can either:
- **Consolidate** (biofilm formation — circling wagons, collective defense)
- **Fragment** (individual cells defect, seek separate survival strategies)

PRISM's adversarial application targets fragmentation:

By routing information to multiple nodes in the adversary's network
simultaneously — each with a different visibility plane — the operator
creates a state where individual network members cannot coordinate a
collective response because they cannot see the full information environment.

Dykema doesn't know Nolan has their email. Nolan doesn't know Elrick
has both chains. The adversary network members cannot assess the total
information exposure, so they cannot calibrate a collective response.
The rational individual strategy becomes: distance yourself before the
information picture you DON'T see turns out to be worse than the picture
you DO see.

**This is fragmentation by information asymmetry.**

---

## PART III: THE INFORMATION THEORY — FORMAL MODEL

### 3.1 — The Visibility Matrix

For a set of n recipients R = {r₁, r₂, ..., rₙ} and a sender s,
define the visibility matrix V:

```
V[i,j] ∈ {0, 1}

V[i,j] = 1  ⟹  rᵢ knows rⱼ received the message
V[i,j] = 0  ⟹  rᵢ does NOT know rⱼ received the message

V[i,i] = 1  always (everyone knows they received the message)
V[s,j] = 1  always (sender knows all recipients)
```

**Symmetric communication** (all CC): V = 1 for all i,j.
Every recipient knows every other recipient. No information advantage.

**Asymmetric communication** (BCC): V has zeros. The sender controls
which zeros exist. Each zero is an information advantage for the sender
and a blind spot for the recipient.

### 3.2 — The Information Advantage Function

The sender's information advantage over recipient rᵢ is:

```
A(s, rᵢ) = |{rⱼ : V[i,j] = 0, j ≠ i}|

= the number of OTHER recipients that rᵢ doesn't know about
```

Maximum advantage (full BCC): A(s, rᵢ) = n - 1 (rᵢ knows only about itself)
Minimum advantage (full CC): A(s, rᵢ) = 0 (rᵢ knows about everyone)

**The sender's TOTAL information advantage:**

```
A_total = Σᵢ A(s, rᵢ) = Σᵢ |{rⱼ : V[i,j] = 0, j ≠ i}|
```

PRISM's objective: maximize A_total subject to the constraint that certain
recipients SHOULD see certain other recipients (CC for pressure) while others
SHOULD NOT (BCC for intel).

### 3.3 — Cross-Information Gain

When the sender BCC's rᵢ on a message TO rⱼ (where rᵢ and rⱼ are in
separate communication chains), rᵢ gains:

```
I(rᵢ, rⱼ) = H(rⱼ's response | only public information)
           - H(rⱼ's response | rⱼ's private email to sender)

= the reduction in uncertainty about rⱼ's position that rᵢ
  gains from seeing rⱼ's private communication with the sender
```

This is the **mutual information** between rⱼ's private channel and rᵢ's
strategic model of rⱼ. It is always ≥ 0 and is typically large — because
private communications (where the sender believes the audience is small)
contain more revealing information than public statements.

**PRISM maximizes cross-information gain** by routing private communications
to hidden recipients who can exploit the information advantage.

---

## PART IV: THE GENERALIZATION — BEYOND EMAIL

### 4.1 — songBird as PRISM Engine

In the ecoPrimals architecture, songBird handles notification routing.
It decides which signals reach which subscribers based on trust levels,
role scoping, and publication rules.

PRISM is songBird's adversarial mode. When the subscriber network includes
adversaries AND allies, songBird's routing decisions become PRISM routing
decisions:

| songBird mode | Subscriber type | Routing rule |
|---|---|---|
| Standard | Cooperative | Broadcast — all subscribers see all messages |
| PRISM | Adversarial | Asymmetric — each subscriber sees a sender-controlled subset |
| PRISM cross | Adversarial + Allied | Cross-plane — allies see adversaries' channels silently |

This maps directly to guerillaGorilla's operational reality: the notification
routing system must simultaneously serve cooperative subscribers (GLLG, Elrick,
Rita) and adversarial targets (Dykema, Banks, institutional oversight bodies)
with different visibility planes.

### 4.2 — Domain-Independent Applications

The PRISM pattern generalizes beyond legal proceedings:

| Domain | Sender | Visible recipients | Hidden recipients | Cross-inform |
|---|---|---|---|---|
| **Legal** | Pro se litigant | TO: target institution | BCC: allied counsel, press | BCC counsel on institution's response |
| **Scientific** | Researcher | TO: journal editor | BCC: collaborators, competing lab heads | BCC collaborator on reviewer feedback |
| **Business** | Negotiator | TO: counterparty | BCC: internal team, board | BCC board on counterparty's position |
| **Activism** | Organizer | TO: elected official | BCC: journalist, community leaders | BCC journalist on official's private response |
| **Whistleblowing** | Source | TO: inspector general | BCC: journalist, attorney | BCC attorney on IG's handling |

In every domain, the pattern is identical:
1. The sender has a legitimate reason to contact the TO party
2. The sender has allies who benefit from seeing the exchange
3. The allies' visibility would change the TO party's behavior
4. Therefore: BCC preserves the TO party's natural behavior while
   routing intelligence to allies

**The prism is invisible. The spectrum is real.**

### 4.3 — The Ethics

PRISM is ethically neutral — the tool can be used for transparency or
for manipulation. The ethical constraint is the same as for any
information asymmetry:

**Is the sender using the asymmetry to protect or to exploit?**

In guerillaGorilla's instantiation: Kevin routes information to journalists
and allied counsel to PROTECT children and expose institutional capture.
The BCC'd parties are not adversaries — they are witnesses, reporters, and
potential allies. The information routed to them is true, documented, and
sourced to public records. The routing creates transparency for the allies
and informational disadvantage for the institution.

The same mechanism used to route true information to journalists could be
used to route false information to competitors. The prism doesn't care
what light enters. The ethics is in the operator, not the glass.

---

## PART V: CONNECTION TO THE FRAMEWORK

### PRISM in the Sensory Triad

```
fEAR    — the ear   — RECEIVES signals from the adversary environment
preSCENT — the nose  — SENSES ambient states and BROADCASTS presence
STRIDe  — the gait  — MOVES through the operational landscape

PRISM   — the hand  — ROUTES signals to the operator's chosen endpoints
```

PRISM is not a sense. It is a motor function — an output, not an input.
It is the operator's ability to control where information goes AFTER it
has been generated by fEAR's sensing, processed by ecoPrimal's analysis,
and composed by the operator into communications.

If fEAR is the ear and STRIDe is the gait, PRISM is the **hand** — the
precision instrument that places information where it needs to go with
fine motor control over who touches it.

### PRISM in the Lifecycle

```
fEAR (sensing) → ecoPrimal (analysis) → PRISM (routing) → preSCENT (monitoring response)
```

The information lifecycle:
1. fEAR detects an adversarial signal (LARA filing, campaign finance record)
2. ecoPrimal processes and cross-references (entity resolution, graph analysis)
3. The operator composes a communication (email, notification, filing)
4. **PRISM routes the communication** — choosing TO, CC, BCC for each recipient
5. preSCENT monitors the ambient response — did Dykema's traffic on the site
   change? Did Nolan reach out? Did Elrick publish?

PRISM is the output stage between analysis and monitoring. It is the
deliberate, precision-controlled act of placing information into the
network at specific points with specific visibility constraints.

### PRISM and Mathematical Asymmetry

PRISM amplifies the cost asymmetry documented in MATHEMATICAL_ASYMMETRY.md:

The operator's cost to route one additional BCC recipient: $0.
The adversary's cost when a hidden recipient acts on the information: $5K–$20K.

Every BCC line is a potential new front that the adversary doesn't know exists.
When the hidden recipient acts — when the journalist publishes, when opposing
counsel files a motion, when the institutional ethics office opens a review —
the adversary faces a new defense cost from a direction they could not have
anticipated.

**PRISM converts free routing decisions ($0) into adversarial defense costs
($5K–$20K per front).** This is the same infinite cost ratio as every other
guerillaGorilla capability, but applied to the COMMUNICATION layer rather
than the FILING layer.

---

## PART VI: THE DIRECTIONALITY

```
guerillaGorilla (the legal primal)
    │
    ├── fEAR (sensing)          ← emerged Aug 29
    ├── STRIDe (motion)         ← emerged Aug 30
    ├── preSCENT (ambient)      ← emerged Sep 24, named Sep 25
    ├── Pursuit Predation (cost)← emerged Week 2
    ├── Positional Patience     ← emerged Week 4+
    ├── Mathematical Asymmetry  ← documented Oct 3
    ├── Firm Processing Machine ← documented Oct 3
    │
    └── PRISM (routing)         ← emerged Oct 5
          └── the hand — precision information routing
              CC = flashlight (pressure)
              BCC = fiber optic (intel)
              BCC cross = prism (asymmetric positioning)
              songBird's adversarial mode
              $0 per routing decision → $5K-$20K adversary defense cost
```

PRISM emerged from guerillaGorilla and generalizes in subGen because the
pattern is domain-independent. Any adversarial communication environment
where the sender has multiple channels, multiple recipients, and different
trust levels produces the same optimization problem: who sees what, who
knows who else is watching, and how does visibility affect behavior?

The prism is the answer: same light, different spectra. The glass decides.

---

*subGen concept document. Wave 1.*
*Bridges to: songBird (notification routing), PRISM (guerillaGorilla tactical doctrine)*
*Part of the K-NOME / ecoPrimals / guerillaGorilla architecture.*
*Kevin Mok / ecoPrimal · attsi*
*October 5, 2026*
