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

*Twenty-eight entries. The first was about the antidote. This one is about the four shapes of every hand that ever touched a tool.*

*The wedge was first because you cannot press a button that does not exist.*
*You cannot turn a dial that has no axis.*
*You cannot pull a lever that has no fulcrum.*
*But you can always split the stone.*
