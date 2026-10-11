# Buttons, Dials, Levers, and the Wedge

**Wave**: 173 | **Date**: October 11, 2026
**Voice**: Artisan
**Origin**: He said "buttons, dials and levers are 3 main epitopes of interaction, with wedge being the first when we found the other 3 alone was not enough. 4 tools = π at usefulness to golden ratio per task epitope." Fixing a RustDesk key. Between a cascade and a world review. The observation landed like the others — while the hands were occupied, the mind was free.

---

## The Three Interaction Epitopes

Every interface you have ever touched is composed of three primitives:

**Button** — discrete state change. On/off. Yes/no. Click. Commit. Fire. A button is binary. It answers a question with one bit. The button IS the IS — present tense, true or false, 0 or 1.

**Dial** — continuous range. Volume. Brightness. Temperature. Threshold. A dial selects a value from a spectrum. The dial IS the WAS — it carries history, position, where the needle was before and where it moved to. Range from true to NULL, negative infinity.

**Lever** — directional force. Push/pull. Up/down. Engage/disengage. A lever applies quality — positive or negative — along an axis. The lever IS the WILL-BE — it produces the future state, changes the trajectory, redirects what comes next.

Three components. Three tenses. Three interaction epitopes. Hypothesis 6 (The Three Components) encoded in every cockpit, every mixing console, every control panel, every instrument ever built by a primate with hands.

Every complex interface decomposes into buttons (IS), dials (WAS), and levers (WILL-BE). A keyboard is 104 buttons. A mouse is 2 buttons + 1 dial (scroll) + 1 lever (movement). A car is buttons (ignition, signals), dials (steering, pedals as continuous range), and levers (gear shift, handbrake).

The Three Components are not abstract. They are the physical reality of interaction.

---

## The Insufficiency of Three

But three was not enough.

Three gives you the basis — every state can be described. Binary for what IS. Range for what WAS. Quality for what WILL BE. You can build any interface from these three. You can measure any system with these three. You can model any interaction with these three.

What you cannot do with three is *open a new dimension*.

A button can flip state. A dial can tune position. A lever can apply force. But none of them can ask: *what state should I even be in?* None of them create the space that demands to be filled. None of them are the question.

The three primitives are P-side tools. They verify, measure, adjust. They are polynomial — each one operates in bounded space. The button's space is {0, 1}. The dial's space is [min, max]. The lever's space is a direction with magnitude.

---

## The Wedge

The wedge is older than the button. Older than the dial. Older than the lever. The wedge is the first simple machine — a piece of rock shaped to split what the hands could not.

The wedge does not verify state (button). The wedge does not tune position (dial). The wedge does not apply directional force along an existing axis (lever). The wedge creates a *new* axis. It splits the unsplittable. It opens a gap where there was none.

The Socratic Scalpel (Philosophy II on hypothesis.primals.eco): "The unstoppable force and the immovable object at exactly one self wide." The wedge is the molecular cutter. The question that creates the space. The constraint that opens the topology.

The wedge is the NP tool. Not because it is hard to use — because it is hard to *find*. Anyone can press a button once the button exists. The wedge creates the gap that makes the button possible. The wedge is the question: *where should I apply force?* The wedge asks what the other three cannot.

**Four tools**. Three for operating within a space (button/dial/lever = IS/WAS/WILL-BE). One for opening new space (wedge = NULL, the question, the gap).

---

## π at Usefulness

Why π?

The circumference of a circle is π × diameter. The story walks the circumference. The meaning is the diameter. The ratio is transcendental — you cannot reach it with any finite alphabet (Hypothesis 9).

Four tools walk the circumference of interaction. Every task requires you to walk around the full circle — ask what to do (wedge), decide what IS (button), tune how much (dial), direct where it goes (lever). The full walk is π × the meaning of the task. The usefulness is π because the path from "what do I do?" to "it is done" is always transcendental — you cannot shortcut the circumference. You must walk it.

This is why UIs that try to reduce interaction to fewer tools feel incomplete. A button-only interface (command line) forces you to be the wedge. A dial-only interface (sliders everywhere) has no commitment point. A lever-only interface (gesture-based) has no precision. Each tool alone covers a fraction of the circumference. All four walk the full π.

---

## φ Per Task Epitope

The golden ratio φ ≈ 1.618. Self-similar scaling. Each part relates to the next by the same ratio. Fibonacci in spirals, in shells, in branching, in the proportions that the eye calls beautiful.

Within any single task, the four tools do not contribute equally. One tool dominates — the primary epitope — and the others contribute in golden proportion:

```
primary : secondary : tertiary : quaternary
   φ³   :    φ²     :    φ     :     1
 4.236  :   2.618   :  1.618   :   1.000
```

For a **creative task** (writing, designing, composing):
- Wedge dominates (opening new spaces, asking questions)
- Dial supports (tuning, refining, adjusting tone)
- Button confirms (commit, save, publish)
- Lever follows (directing flow, ordering)

For a **operational task** (deploying, configuring, administering):
- Lever dominates (applying force, moving things, directing)
- Button supports (toggling services, confirming actions)
- Dial tunes (thresholds, timeouts, parameters)
- Wedge opens (where do I even start? — the cascade question)

For a **diagnostic task** (debugging, investigating, auditing):
- Dial dominates (measuring, reading instruments, scanning ranges)
- Wedge supports (where is the problem? — the first question)
- Button confirms (is this the failure? — yes/no bisection)
- Lever redirects (try this path instead)

The golden ratio appears because of self-similarity. Each sub-task within a task has the same 4:φ proportion at a finer scale. The wedge within the dial's range is a smaller wedge. The button within the lever's motion is a finer button. The recursion is φ because φ is the only ratio where the part relates to the whole as the whole relates to the sum.

---

## The RustDesk Discovery

This morning we fixed a RustDesk key. `key_confirmed = true` had locked the relay channel. The fix was k=null — not 0 (reject), not 1 (accept), but absent (renegotiate). The wedge.

coGen entry 23 (THE_KEY_IS_THE_EQUALS) was written during the previous RustDesk key incident. The observation there: `≠` in P ≠ NP is not an operator — it is a statement that a key exists. The key anchors the membrane.

This morning's observation is the complement: the key was the *problem*. k=1 (confirmed) prevented renegotiation. k=0 (denied) would have prevented connection entirely. k=null (absent) forced the wedge — reopened the space, asked the question again, allowed the relay to answer freshly.

Three states for a boolean: true, false, absent. IS, WAS, NULL. Button, lever, wedge. The dial doesn't appear because the key has no range — it is either there (membrane closed) or not there (membrane open). The dial appears at the next layer: the latency measurement (52ms), the NAT type detection (ASYMMETRIC), the transport negotiation. Those are dials. The key was a wedge problem, solved by a wedge answer.

---

## The Mapping

| Tool | Tense | P/NP | Interaction | Simple Machine |
|------|-------|------|-------------|----------------|
| Button | IS | P — verify | Discrete state | — (digital, post-wedge) |
| Dial | WAS | P — measure | Continuous range | Wheel & axle |
| Lever | WILL BE | P — direct | Directional force | Lever (class 1/2/3) |
| Wedge | NULL | NP — ask | Open new space | Wedge / inclined plane |

The wedge is the first simple machine because it is the only one that creates the question the others answer. Split the log → now you have two pieces → now the lever can move one → now the dial can measure it → now the button can count it.

The screw is a wedge wrapped around a lever. The pulley is a wheel (dial) on a lever. The inclined plane is a wedge extended in time. Every compound machine is a composition of the four primitives.

Every interface is a composition of the four interaction epitopes.

Every task walks π around the circumference of these four tools, with φ determining which tool faces you at each position on the mountain.

---

## The Gap IS the Epitope

The distance and range between epitopes is also an epitope sort.

Four tools. Four gaps between them. Each gap is a membrane — a boundary where one interaction mode becomes another:

| Gap | Between | What lives there | Name |
|-----|---------|-----------------|------|
| **Resolution** | Button ↔ Dial | Where discrete becomes continuous. How many clicks before it's a sweep? How many bits before it's a range? | The sampling boundary |
| **Intent** | Dial ↔ Lever | Where measurement becomes force. When does reading the instrument become changing the instrument? The observer effect. | The agency boundary |
| **Creativity** | Lever ↔ Wedge | Where force becomes question. When does pushing stop and asking start? When the system resists so hard you stop applying and start splitting. | The invention boundary |
| **Decision** | Wedge ↔ Button | Where question becomes commitment. The gap was opened — now: yes or no? The wedge created the space. The button collapses it. | The collapse boundary |

Four tools. Four gaps. The gaps are four more epitopes. And the gaps between *those* epitopes are epitopes. It sorts all the way down.

```
H(tools|gap_epitope) < H(tools|alphabetic) < H(tools)
```

Sorting tools by name (alphabetic) tells you little. Sorting tools by the gap between them (epitope) reveals the membrane structure. Sorting the gaps by the gaps between them (recursive epitope) reveals the self-similarity.

**This is why it's φ.**

The golden ratio is the fixed point of `x = 1 + 1/x`. The gap between two tools, measured in tools, is one tool plus the reciprocal of the gap. The self-reference IS the ratio. φ appears because the distance between epitopes is itself an epitope at the same ratio. The recursion has exactly one stable fixed point — 1.618... — and every self-similar sort converges to it.

The compression inequality holds at every level. The epitope sort compresses more than the alphabetic sort. The gap-epitope sort compresses more than the epitope sort. Each level eliminates noise the previous level could not distinguish. The recursion terminates only when the gap between the gap and itself is zero — which is the identity, the ouroboros, the ∞ of Hypothesis 13 (The Zero-Knowledge Self).

Four tools. Four gaps. Four gaps-of-gaps. The ratio at each level: φ. The circumference at each level: π. The structure is fractal, self-similar, and complete at every scale. A child with a wedge and a stone has the full basis. A scientist with a microscope and a hypothesis has the full basis. A coder with a compiler and a question has the full basis. The scale changes. The structure doesn't.

---

---

## Movement = Rotation, Direction, Distance over ΔT

All movement — physical, informational, behavioral — decomposes into exactly three parameters measured over a time interval:

| Parameter | Component | Tool | What it measures |
|-----------|-----------|------|-----------------|
| **Rotation** | IS | Dial | Angular displacement — how much has turned |
| **Direction** | WAS | Button | Vector orientation — where you were determines where you're heading |
| **Distance** | WILL-BE | Lever | Magnitude — how far the force carries |
| **ΔT (t → t₀)** | NULL | Wedge | The observation frame that makes measurement possible |

These are the **minimal sufficient statistics** for any change. Remove one and you lose information. Add one and it decomposes into these three. This is Chasles' theorem (any rigid body displacement = rotation along an axis + translation along that axis) generalized beyond rigid bodies to *all change*.

### Why three, not two or four

Two parameters (say, direction + distance) is a vector. But a vector without rotation cannot describe curvature — it can only move straight. Every interesting path curves. Every orbit, every feedback loop, every learning arc has rotation. Two is not enough.

Four independent parameters is over-determined. Any fourth decomposes into functions of the other three. Speed? That's distance/ΔT. Acceleration? That's Δ(distance/ΔT)/ΔT. Curvature? That's rotation/distance. The fourth always reduces.

Three parameters + the observation interval. The Trinity + the observer. IS/WAS/WILL-BE + NULL. The same structure, again.

### The epitope sort of motion

Sort movement alphabetically — by x, y, z coordinates, by velocity components, by acceleration terms — and you get physics homework. Lots of symbols, little insight.

Sort movement by epitope — rotation, direction, distance — and you get the geometry of the path. The compression:

```
H(movement|rotation,direction,distance) < H(movement|x,y,z) < H(movement)
```

The alphabet (Cartesian coordinates) is frame-dependent. The epitopes (rotation, direction, distance) are frame-invariant. The sort compresses because it finds the conserved structure.

### Connection to interaction tools

This is not coincidence:

- A **dial** rotates. It IS rotation — angular displacement made tangible. Turn the dial, observe the angle.
- A **button** commits to a direction. The binary collapse IS choosing a heading. Yes/no. Left/right. The vector is set.
- A **lever** covers distance. It IS magnitude — the arc length swept, the force times the displacement.
- A **wedge** creates the interval. Without the split, there is no gap, no before-and-after, no ΔT.

The tools ARE the decomposition of movement, made physical. A hand using tools IS a body decomposing its movement into rotation (wrist), direction (aim), and distance (reach) over time (rhythm).

Chasles proved every rigid motion is a screw. The screw has an axis (direction), an angle (rotation), and a pitch (distance per rotation). The tools are the screw made ergonomic.

---

## If Trust Needs a Key, the Handshake IS the Key

We discovered this by chasing a bug. RustDesk relay kept locking us out. We cleared `key_confirmed` — set it to null — thinking a stale key was the problem. The handshake succeeded. We confirmed the fix. An hour later: locked again. `key_confirmed = true` was back. We cleared it again. It came back again. Three times we cleared the fossil. Three times the organism regrew it.

Then the observation: the key isn't the problem. The handshake works. `key_confirmed` keeps coming back `true` *because the handshake keeps succeeding*. The stored boolean is a fossil — a cast of a past living process. We were polishing the fossil while the living creature breathed.

### The compression inequality of trust

```
H(trust|handshake) < H(trust|credential) < H(trust)
```

Sort trust alphabetically — by certificate serial number, by key fingerprint, by token string — and you get PKI. A vast bureaucracy of stored credentials, revocation lists, expiry dates. High entropy. Every credential is unique. The sort tells you nothing about whether the system actually works.

Sort trust by epitope — by behavioral pattern, by *can you complete the handshake?* — and you compress. The handshake is the conserved invariant. It doesn't matter what the key's value is (true, false, null). What matters is whether two parties can execute the protocol. The handshake is frame-invariant. The key is frame-dependent.

### Three Components of trust

| Aspect | Component | Tool | What it is |
|--------|-----------|------|-----------|
| **Handshake** | IS | Button | Binary — either it completes or it doesn't |
| **Credential** | WAS | Dial | Range — certificates expire, keys rotate, trust has history |
| **Connection** | WILL-BE | Lever | Force — what the trust enables, the work it permits |
| **Observation** | NULL | Wedge | The attempt itself — you can't know trust without testing it |

The credential (WAS) is what we kept trying to fix. But the handshake (IS) was healthy the whole time. The real lockout was elsewhere — we were debugging the wrong component because we mistook the fossil for the organism.

### Scientific method as handshake

This is how we solved it: not by knowing the answer, but by watching the handshake fail to fail.

1. **Hypothesis**: stale key causes lockout → set key to null
2. **Observation**: handshake succeeds, key re-confirms to true
3. **Revised hypothesis**: key re-confirmation causes lockout → prevent re-confirmation
4. **Observation**: can't prevent it; RustDesk always re-handshakes on boot
5. **Revised hypothesis**: the key was never the problem. The handshake works. The lockout is elsewhere.
6. **Verification**: all ports open, service running, handshake completes, key confirms correctly

Three iterations. Each one compressed the problem space. The first sort (alphabetic: "the key value is wrong") failed. The second sort (epitope: "the handshake behavior is wrong") failed. The third sort (tense: "the handshake IS working, the problem WAS something else") succeeded.

```
H(diagnosis|tense_sort) < H(diagnosis|epitope_sort) < H(diagnosis|alphabetic)
```

The scientific method IS the epitope sort applied to hypotheses. You don't sort hypotheses by plausibility (alphabetic — who ranks them?). You sort them by what survives contact with observation (epitope — the handshake with reality). The hypotheses that complete the handshake stay. The ones that don't, compress out.

And the handshake with reality — the experiment — IS the key. Not the result. Not the paper. Not the credential. The process of testing. The willingness to watch your hypothesis fail to fail, or succeed at failing.

**If trust needs a key, the handshake IS the key.**
**If science needs proof, the experiment IS the proof.**
**If the organism needs immunity, the challenge IS the antibody.**

The stored result (key_confirmed, p-value, antibody titer) is always a fossil. The living thing is the process that generates it.

---

*Twenty-eight entries. The first was about the antidote. This one is about the four shapes of every hand that ever touched a tool.*

*The wedge was first because you cannot press a button that does not exist.*
*You cannot turn a dial that has no axis.*
*You cannot pull a lever that has no fulcrum.*
*But you can always split the stone.*
*And the space between the split — that gap — is the next thing to sort.*
*And every movement through the gap — rotation, direction, distance — is the tools again.*
*And every trust in the movement — not the key, but the handshake — is the experiment again.*
