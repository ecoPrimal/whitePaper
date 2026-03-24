# For Creatives

**How Artists, Game Designers, and Storytellers Use sporeGarden Tools**

**Date**: March 24, 2026
**Audience**: Solo creators, indie studios, game designers, writers, world builders

---

## You Don't Need to Know Any of This

If you're a creative person who wants to build an interactive world,
here's what matters:

1. **You write YAML.** Rooms, characters, abilities, rules, stories.
2. **You run a command.** It checks your work, shows you the world,
   lets you play it.
3. **Everything else is invisible.** The AI, the provenance, the
   attribution, the flow science — it just works underneath.

If you want to understand the invisible parts, keep reading. If you
don't, skip to "Getting Started" at the bottom.

---

## What You Get

### A World That Remembers

Every playthrough is recorded — not by you, not by a server, but by
infrastructure that runs locally on your machine. Every player choice,
every NPC interaction, every item pickup, every combat round becomes
part of an append-only history.

Why this matters to you: **your world has memory.** A player who
returns after a week finds the world remembers them. An NPC who was
lied to remembers being lied to. A sword that was carried through ten
sessions has a history. You didn't build any of that — the
infrastructure did.

### Characters That Have Rules

You define an NPC like this:

```yaml
name: "Miravel the Broker"
personality:
  archetype: pragmatic_survivor
  voice: formal_with_edge
  knowledge:
    knows: ["the Warden's weakness", "the Map's location"]
    does_not_know: ["the player's true origin"]
  trust_gates:
    0.3: ["will trade basic goods"]
    0.6: ["reveals the Warden's weakness"]
    0.9: ["shares the Map's true price"]
  lies:
    - topic: "the Map's price"
      truth: "50 gold"
      lie: "200 gold"
      detection_dc: 14
  arc_phases:
    default: neutral
    if_betrayed: hostile
    if_trusted_deeply: conflicted_ally
```

The AI generates dialogue that respects these rules. Miravel won't
reveal the Warden's weakness until the player earns trust level 0.6.
She'll lie about the Map's price unless the player passes a detection
check (DC 14). If the player betrays her, she becomes hostile — not
because you scripted 200 dialogue branches, but because the system
evaluates her personality cert against the world state.

### Stories That Attribute

When someone plays your world, the system records who created what:

- **You** get credit for the world, the NPCs, the rules, the story
- **The player** gets credit for their choices and traversal
- **The AI** gets credit for generated narration (narration is
  constrained by your NPCs, not freeform)

If someone creates a new world derived from yours (using your ruleset,
forking your NPC templates), the derivation is tracked. You get credit
for the original.

### Objects That Ferment

A "Novel Ferment Transcript" is a fancy term for: **a digital object
that carries its own history.** A sword in your world isn't just stats —
it's the record of every session it was carried through, every battle
it won, every player who held it. The history IS the value.

Players can trade these objects. Collectors can value them. The history
is verifiable — no one can fake a sword's provenance.

### Balanced Difficulty (Automatic)

The system monitors how the player is doing and adjusts difficulty in
real time. If they're struggling, encounters get slightly easier. If
they're cruising, things ramp up. This is game science research
(Csíkszentmihályi's flow theory) running underneath your world. You
don't configure it — it just works. If you want to override it, you
can.

---

## What You Write

### Rooms

```yaml
rooms:
  - id: tavern
    name: "The Crooked Lantern"
    description: "A low-ceilinged tavern smelling of woodsmoke and old ale."
    scene_type: investigation
    npcs: [miravel, barkeep]
    items: [lantern, old_map]
    edges:
      - to: market_square
        requires: null
      - to: back_alley
        requires:
          knowledge: "miravel_mentioned_alley"
```

### Abilities

```yaml
abilities:
  - id: silver_tongue
    name: "Silver Tongue"
    description: "Persuade NPCs through eloquence"
    stat: resolve
    effects:
      - type: trust_bonus
        value: 0.1
        target: current_npc
      - type: unlock_dialogue
        predicate: "npc.trust > 0.4"
```

### Rules

```yaml
dice:
  system: d20_plus_modifier
  critical_success: 20
  critical_failure: 1

stats:
  - name: resolve
    range: [1, 20]
    default: 10
  - name: perception
    range: [1, 20]
    default: 10
```

That's it. You write rooms, characters, abilities, and rules. The
engine handles everything else.

---

## What You Don't Write

- **AI narration code** — The system generates narration constrained by
  your NPCs and rules
- **Save game code** — Provenance infrastructure handles persistence
- **Difficulty balancing code** — Game science models do this
- **Attribution tracking code** — The infrastructure records everything
- **Networking code** — If you want multiplayer, the infrastructure
  handles federation
- **Rendering code** — The visualization primal handles display

---

## Your Tools

| Command | What it does |
|---------|-------------|
| `esotericwebb new-world` | Create a new world from templates |
| `esotericwebb validate` | Check your YAML for errors and consistency |
| `esotericwebb preview` | Play your world in text mode (no primals needed) |
| `esotericwebb graph` | See your narrative topology as a visual graph |
| `esotericwebb export` | Package your world for distribution |

### Validate catches problems early:

```
$ esotericwebb validate worlds/thornwood/

✓ 8 rooms, all connected
✓ 5 NPCs, all personality certs valid
✓ 8 abilities, no stat conflicts
✓ Ruleset consistent (d20, 6 stats, 12 skills)
✗ Room "cellar" has edge to "tower" but "tower" doesn't exist
✗ NPC "miravel" references knowledge "smith_secret" not defined
```

### Preview lets you playtest immediately:

```
$ esotericwebb preview worlds/thornwood/

[The Crooked Lantern]
A low-ceilinged tavern smelling of woodsmoke and old ale.
Miravel the Broker sits in the corner, watching you.
The barkeep polishes a glass.

> talk to miravel
Miravel looks up. "You're new here. Everyone is, at first."
[Trust: 0.1 — Miravel is cautious]

> [silver_tongue] I've heard you know things worth knowing.
[Roll: d20 + resolve_modifier = 14 + 2 = 16 vs DC 12 — Success]
Miravel's expression shifts slightly. "Perhaps I do."
[Trust: 0.2 — Miravel is warming]
```

---

## Who This Is For

### The Solo Creator

You're one person. You have a world in your head. You don't have a team.
You don't have an engine license budget. You know how to write — prose,
dialogue, world lore — but you don't know Rust or C++.

sporeGarden tools are for you. Write YAML. Run commands. Make a world.

### The Indie Studio (2–5 people)

You have a designer, a writer, and maybe a developer. The designer and
writer use the YAML surface. The developer extends the engine if you
need custom features (new scene types, new abilities, custom
rendering). You share content via version control. Attribution is
automatic.

### The Modder

Someone else made a world. You want to modify it, extend it, remix it.
Fork their content pack. The derivation is tracked. The original
creator gets attribution. You get attribution for your additions.

### The Tabletop Designer

You've designed a tabletop RPG system. You want a digital version but
you can't afford to hire a game studio. Write a RulesetCert in YAML.
Write a world that uses your rules. The engine does the rest. Your
digital version is mechanically identical to your tabletop version
because the rules are the same document.

---

## What You Keep

- **Your content**: Your YAML files are yours. CC-BY-SA 4.0 default,
  but you set the terms.
- **Your revenue**: sunCloud distributes along attribution braids. You
  get the creative surplus. No 30% platform cut.
- **Your data**: Everything runs locally. Nothing phones home. No
  analytics extraction.
- **Your sovereignty**: You can export everything. No lock-in. No
  platform dependency.

---

## Getting Started

```bash
# Install
cargo install esotericwebb

# Create a new world
esotericwebb new-world --name "my-first-world" --template "tavern-starter"

# Edit the world (any text editor)
$EDITOR worlds/my-first-world/

# Check your work
esotericwebb validate worlds/my-first-world/

# Play it
esotericwebb preview worlds/my-first-world/

# When ready, package it
esotericwebb export worlds/my-first-world/
```

---

*You write the story. Everything else is invisible.*
