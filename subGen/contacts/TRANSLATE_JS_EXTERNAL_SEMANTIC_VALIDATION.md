# Translate.js: External Semantic Validation via Translation

**Source**: Email outreach from Guan (translate.js maintainer)
**Date**: Aug 2026
**Relevance**: petalTongue semantic boundary validation, sporePrint multilingual science reports, Validation Class V

---

## Core Insight

Translation is not the primary value here. **External semantic validation** is.

The contact offers a translation/localization engine. The deeper opportunity: use an independently developed system as a **fuzz tester for petalTongue's semantic boundary**.

If translate.js can consume petalTongue's exposed semantics and generate usable multilingual presentation **without knowing anything about songBird, toadStool, barraCuda, NUCLEUS, or the underlying Rust types**, then petalTongue's abstraction is doing its job.

If it can't, the failure tells you something.

That's exactly what the springs already do — but applied to the presentation layer.

---

## The Experiment: Semantic Surface Contract

Expose only what an external renderer is supposed to understand:

```
ecoPrimals internals
      │ private implementation
      ▼
petalTongue
      │ semantic presentation contract
      ▼
┌──────────────────────────────┐
│ Semantic surface             │
│                              │
│ kind: status                 │
│ intent: success              │
│ text: "Computation complete" │
│ locale: en-US                │
│ translatable: true           │
│                              │
│ value: 0.0044                │
│ unit: USD                    │
│ translatable: false          │
└──────────────────────────────┘
              │
              ▼
       UNKNOWN EXTERNAL RENDERER
```

Translation is destructive if semantic boundaries are wrong. This makes it an unusually good first test.

---

## Bidirectional Invariant Testing

Don't merely check whether Chinese output looks good. Test invariants:

```
         PETALTONGUE SEMANTIC OBJECT
                    │
         ┌──────────┼──────────┐
         ▼          ▼          ▼
       en-US      zh-CN      de-DE
         │          │          │
         ▼          ▼          ▼
     renderer  translate.js  renderer
         │          │          │
         └──────────┼──────────┘
                    ▼
            semantic comparison
```

**Must NEVER change** (invariants):
- capability identity, node identity
- numeric values, units
- provenance hashes, URLs, file paths
- error codes, scientific notation
- chemical names (where marked invariant)
- command syntax, method identifiers
- confidence/tolerance, semantic intent

**SHOULD change** (translations):
- natural-language labels, sentence structure
- pluralization, date presentation
- human-readable units, tooltips
- descriptions, instructions, accessibility text

---

## Hostile Language Testing

Language is incredibly hostile to accidental assumptions:

- **Mandarin**: exposes presentation leakage English hides
- **German**: long compound words expose layout assumptions
- **Arabic**: exposes directionality assumptions
- **Japanese**: exposes segmentation assumptions
- **Plural-heavy languages**: expose grammatical-number assumptions
- **Different date/number conventions**: expose formatting assumptions

This tests: **semantic petalTongue → arbitrary human representation**, not just petalTongue → English web dashboard.

---

## Validation Class V: External Semantic

Extends the existing validation progression:

```
I    Numerical          Does computation reproduce known results?
II   Cross-substrate    CPU == GPU == NPU within tolerance?
III  Compositional      Can independent primals discover and use capabilities?
IV   Reproducibility    Can another machine reproduce the artifact?
V    External Semantic  Can independently developed software correctly
                        consume a public semantic contract?
```

translate.js becomes **External Semantic Validation #001**.

---

## Evidence Package Structure

```
petalTongue fixture v1
├── semantic.json
├── semantic.schema.json
├── expected-invariants.toml
├── BLAKE3
├── renderer/
│   ├── native-en
│   └── translate-js-adapter
└── validation/
    ├── zh-CN
    ├── de-DE
    ├── ja-JP
    └── ar
```

Publish failures too — they're evidence the validation process works, just like wetSpring finding the toadStool `log_f64` bug.

---

## Methodology: Don't Adapt First

Critical constraint: **do not adapt petalTongue specifically for translate.js initially.**

1. Freeze a semantic contract
2. Hash it
3. Publish the fixture
4. Integrate translate.js
5. Record what works and what breaks

Otherwise you're testing whether you can make two pieces of software work together (trivially true). What you want to test:

> Did the existing petalTongue abstraction contain enough information for an unforeseen external consumer?

This is the software-architecture analogue of the science thesis: **the abstraction is not a claim — an independent implementation consumed it.**

---

## Multi-Language Science Reports

In theory, this is how you build a multi-language science report:

```
semantic data object
      │
      ├── English renderer  → en-US report
      ├── Chinese renderer  → zh-CN report
      ├── German renderer   → de-DE report
      └── Arabic renderer   → ar report
```

The meaning remains invariant. Only presentation changes. The DOM walker allows testing what gets shown and what gets translated.

---

## Future Generalization

Today:
```
petalTongue semantics → translate.js
```

Tomorrow:
```
petalTongue semantics
    ├── translation engine
    ├── screen reader
    ├── terminal renderer
    ├── VR interface
    ├── scientific notebook
    ├── game engine
    ├── LLM agent
    ├── tactile interface
    └── something unimagined
```

If these consume the same semantic exposure without changing the primals, petalTongue is a **semantic presentation boundary** rather than a frontend framework. Proven by software somebody else wrote showing up and fitting the interface.

---

## Engagement Strategy

1. **Respond to Guan** expressing interest in interoperability experiment (not just "add translation")
2. **Define smallest stable semantic surface** that should be sufficient
3. **Ask whether translate.js can render/translate it** without internal knowledge
4. **Document results** — successes AND failures
5. If successful: first unsolicited external interoperability experiment

---

*Public contact. Source: email outreach from translate.js maintainer (Guan). No prior relationship. Evaluated for external semantic validation of petalTongue presentation boundary.*
