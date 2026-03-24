# RPGPT Engine

**Ingestible Rulesets, Living Game Systems, and the End of the Static Rulebook**

**Date**: March 24, 2026
**Status**: Conceptual — design validated by esotericWebb V4, promoted from gen3/baseCamp/18
**Lineage**: gen3/baseCamp/18 (RPGPT) → esotericWebb specs → gen4

---

## The Problem with Rulebooks

A tabletop RPG rulebook is a static document. It describes character
creation, skill checks, combat, magic, equipment, leveling. A human
game master (GM) reads the rulebook, internalizes the rules, and
**interprets** them in real time during play. The GM resolves ambiguity,
adjudicates edge cases, paces encounters, and adapts to player choices.

Digital adaptations of tabletop RPGs (Baldur's Gate, Pathfinder:
Kingmaker, Solasta) hard-code the rules. A team of developers
translates the rulebook into C++ or C#. Every edge case must be
anticipated. Every rule interaction must be manually implemented. When
the ruleset updates, the game requires patching by developers.

**RPGPT eliminates this bottleneck.** The rulebook becomes a machine-
readable document — a RulesetCert — that the engine ingests, validates,
and executes at runtime. The creator writes rules. The engine enforces
them. No developer translates.

---

## What a RulesetCert Is

A RulesetCert is a loamSpine certificate that encodes a complete RPG
ruleset:

```yaml
ruleset:
  name: "Thornwood System"
  version: "1.0"
  edition: "inaugural"
  provenance:
    author: "solo_creator_handle"
    derived_from: null
    license: "CC-BY-SA 4.0"

stats:
  - name: resolve
    range: [1, 20]
    default: 10
    description: "Mental fortitude and willpower"
  - name: perception
    range: [1, 20]
    default: 10
    description: "Awareness and sensory acuity"
  # ...

skills:
  - name: deception
    governing_stat: resolve
    check_formula: "d20 + resolve_modifier"
    opposed_by: "perception"
  - name: investigation
    governing_stat: perception
    check_formula: "d20 + perception_modifier + (has_tool ? 2 : 0)"
  # ...

dice:
  system: "d20_plus_modifier"
  critical_success: 20
  critical_failure: 1
  advantage: "roll_twice_take_higher"

combat:
  initiative: "d20 + perception_modifier"
  action_economy:
    actions_per_turn: 2
    movement_per_turn: "30ft"
    reaction_per_round: 1
  damage_types: [physical, fire, cold, psychic, radiant]
```

The RulesetCert is:
- **Hashable**: loamSpine gives it a content hash. Two games using the
  same ruleset can be verified to use the same rules.
- **Versioned**: Updates produce new certs with derivation chains.
- **Attributable**: sweetGrass records who created the ruleset and who
  derived from it.
- **Inspectable**: The player can read the cert — transparent dice,
  transparent rules. No hidden mechanics.

---

## The Ingestible Ruleset Pipeline

```
Creator writes RulesetCert (YAML)
    │
    ├── validate: engine checks consistency
    │   (stat ranges, formula syntax, skill references)
    │
    ├── mint: loamSpine certifies the ruleset
    │   (content hash, author attribution, version chain)
    │
    ├── load: engine ingests cert at runtime
    │   (stat definitions become live game mechanics)
    │
    ├── execute: engine evaluates skill checks, combat, leveling
    │   using the ingested rules — no hard-coded mechanics
    │
    └── trace: rhizoCrypt records every rule evaluation
        (which rule fired, what the roll was, what the outcome was)
```

### What This Means

A creator can design a complete RPG system — stats, skills, dice,
combat, magic, equipment, leveling — in YAML. They run
`esotericwebb validate` to check consistency. They run
`esotericwebb preview` to playtest. They share the RulesetCert with
other creators. Someone else writes a world that uses their ruleset.
Attribution flows via sweetGrass.

No one wrote Rust. No one compiled anything. The rules are live.

---

## The Living Game System

RPGPT is not a static engine running a static ruleset. It is a **living
system** where the game evolves during play:

### Dynamic Difficulty Adjustment (ludoSpring)

ludoSpring's `game.evaluate_flow` measures player engagement in real
time: action diversity, exploration rate, combat outcomes, dialogue
choices. If the player is in flow, the system maintains the challenge.
If the player is struggling, the system adjusts (easier encounters,
more hints, gentler skill DCs). If the player is bored, the system
escalates (harder encounters, more surprises, tighter deadlines).

This is the scientific foundation from baseCamp paper 17 (Game Design
as Rigorous Science): Csíkszentmihályi's flow theory operationalized
as game science, validated by ludoSpring, consumed invisibly by the
RPGPT engine.

### NPC Evolution

NPCs are not static dialogue trees. They are personality certificates
with:

- **Knowledge bounds**: what the NPC knows and doesn't know
- **Trust gates**: what the NPC reveals at different trust levels
- **Lie tables**: what the NPC lies about, and the detection DC
- **Arc phases**: how the NPC's personality shifts through story events
- **Voice personality**: how the NPC speaks (formal, casual, archaic)

When the player interacts with an NPC, the engine evaluates the NPC's
personality cert against the current world state. Squirrel generates
dialogue constrained by the cert. ludoSpring evaluates the game-science
implications (flow, engagement, pacing). The result is a conversation
that feels authored but is genuinely responsive to the player's unique
state.

### Rule Emergence

The combinatorial interaction of rules creates emergent gameplay that
the creator didn't explicitly author:

- A character with high deception and low perception can lie effectively
  but misses environmental clues
- A character who invested in crafting can create items that bypass
  combat encounters
- A character who earned an NPC's trust can access information locked
  behind knowledge gates

The rules are bounded (authored in the RulesetCert). The interactions
are infinite (combinatorial state space). The emergence is real but
constrained. This is the Bounded Infinite Architecture applied to game
mechanics.

---

## The GM Problem

Traditional digital RPGs need developers to replace the GM. RPGPT uses
a composition of primals:

| GM function | Primal composition |
|-------------|-------------------|
| Rule interpretation | Engine + RulesetCert (deterministic) |
| Narration | ludoSpring → Squirrel (tiered, constrained) |
| NPC roleplaying | Squirrel + personality certs (bounded AI) |
| Pacing | ludoSpring flow evaluation (DDA) |
| Adjudication | Engine predicate evaluation (transparent) |
| World building | Creator content (YAML) |
| Memory | rhizoCrypt DAG (provenance) |
| Fairness | Transparent dice (the player sees the system) |

The primals replace the GM's computational functions. The creative
functions (world design, story crafting, NPC characterization) remain
with the human creator. The AI (Squirrel) operates within authored
constraints — it is a tool, not a replacement.

---

## Sovereignty and the "No Dungeon Master as a Service" Principle

RPGPT does not require a cloud service. It does not phone home. It
does not extract data. The engine runs locally. The primals run locally
(or on the player's own server). The content is the creator's. The
playthrough data is the player's.

This is sovereignty applied to interactive entertainment:

- **No platform rent**: The engine is AGPL. The content is CC-BY-SA.
  The rules are the creator's.
- **No data extraction**: The provenance DAG is local. rhizoCrypt does
  not upload. The player's choices are the player's.
- **No AI dependency**: The engine runs without Squirrel (template
  fallback). Squirrel runs locally when available (sovereign AI).
- **No always-online**: Everything works offline. Standalone mode is a
  first-class feature.

---

## The Games@Home Extension (baseCamp 19)

baseCamp paper 19 describes "Games@Home" — distributed human
computation where gameplay generates scientifically useful data. RPGPT
is the substrate for this:

- **Protein folding as puzzle mechanics**: The combinatorial search
  space of card games mirrors molecular assembly. Player solutions to
  in-game puzzles can map to real optimization problems.
- **Tournament memory**: rhizoCrypt DAGs trace tournament brackets.
  Every game is provenance-tracked. The tournament itself is a Novel
  Ferment Transcript.
- **AR card systems**: loamSpine certificates for physical cards.
  NFC/QR bridge between physical and digital. The card's provenance
  includes every tournament it was played in.

---

## Relationship to esotericWebb

esotericWebb is the first implementation of RPGPT principles. The
RPGPT Engine, as a standalone product, would be esotericWebb with:

1. **Ruleset ingestion as primary feature** (not just one ruleset)
2. **Community ruleset sharing** via Songbird
3. **Ruleset derivation tracking** via sweetGrass
4. **Multi-system support** (D&D-like, PbtA, Fate, custom, etc.)
5. **Tabletop mode** (shared screen, turn-based, dice visible)

esotericWebb V4 validates the architecture. RPGPT Engine would
generalize it for any tabletop-inspired system.

---

*The rulebook is dead. Long live the RulesetCert.*
