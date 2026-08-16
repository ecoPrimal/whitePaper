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

---

## Codebase Assessment (Aug 2026)

| Metric | Value |
|--------|-------|
| Created | 2021 (rewrite v2.0 in 2022) |
| Latest version | 4.1.0.20260526 |
| GitHub | github.com/xnx3/translate — 3,049 stars, 477 forks |
| Gitee | gitee.com/mail_osc/translate — 2,002 stars |
| npm | `i18n-jsautotranslate` (~436/week) |
| Core LOC | ~14,349 (single JS file) |
| Dependencies | **0** (pure vanilla ES5 JS) |
| Bundle (unminified) | 584 KB |
| Bundle (minified) | ~157 KB |
| Tests | **None** (`npm test` = "no test specified") |
| CI | Minimal (publish + release only, no test/lint) |
| TypeScript | Minimal (Vue3 wrapper only, ~80 lines) |
| Contributors | 20 (primary: 管雷鸣/Guan Leiming `xnx3` = 1,045/~98%) |
| License | **MIT** |
| Coverage | Unknown (no test infrastructure) |

### How It Works

Runtime DOM machine-translation engine — NOT a traditional i18n framework. No `.json` locale files, no `t('key')` API.

1. Walks live DOM recursively (`childNodes`)
2. Extracts translatable text (respects `notranslate` class, `translate="no"` attr)
3. Hash-deduplicates translation units
4. Calls translation backend (configurable: Edge browser API, hosted service, self-hosted, AI)
5. **Mutates DOM in place** with translated strings
6. MutationObserver for SPA/dynamic content

### Translation Backends

| Channel | Description |
|---------|-------------|
| `client.edge` | Browser-side Edge translation API — free, no server |
| `translate.service` | Author's hosted API (default fallback) |
| Self-hosted | Java `translate.core`, `translate100` HuggingFace model |
| AI backends | SiliconFlow, Qwen3, enterprise configs |

### Up to ecoPrimals Standards?

**Strengths**: Zero deps, MIT license, 4+ years production hardened, massive scale (author claims billions of API calls), extensive Chinese documentation, DOM edge-case coverage (iframes, Vue, meta tags, SSE streaming).

**Critical gaps**: **No automated tests whatsoever**. No TypeScript types. Monolithic 14K-line single file. Single-author bus factor. Code quality is integration-tested-by-fire, not test-driven. Chinese-primary documentation.

**This is NOT up to ecoPrimals code standards for primal integration.** But it doesn't need to be — it's an **external consumer** for validation, not internal infrastructure.

### Can We RustScript the Translator?

**Partially.** ~40% of the logic is portable to Rust/WASM:
- Text tokenization + grouping
- Language detection
- Cache key hashing (BLAKE3 instead of their hash)
- Batch translation request planning
- Invariant validation

**~60% is inherently browser-bound:**
- DOM tree walking (needs `web-sys` bindings)
- MutationObserver lifecycle
- DOM text replacement / render-back
- Framework integration (Vue/React)

**Better path**: petalTongue renders locale-aware HTML **server-side** (true semantic i18n from Rust). Use translate.js client-side only as an **external validation fuzz tester**. If we want RustScript translation, implement the semantic boundary + invariant checking in Rust/WASM, keep a thin JS shim (~500 lines) for DOM access.

**What RustScript translation enables:**
- BLAKE3-hashed translation cache (provenance-aware)
- Translation units as sweetGrass-braided artifacts (who translated what, when, verified by whom)
- petalTongue serves translation as a capability (`translate.text`, `translate.semantic`) via Neural API
- Any gate can serve multilingual content through the mesh
- Jargon translation becomes a capability — same pipeline translates "sweetGrass attribution braid" → "cryptographically signed provenance chain" for external audiences
- Machine-to-machine translation: primal signals → external API formats (OpenAPI, GraphQL, MCP)

### Recommendation: Take As-Is vs Fork

**Take as-is for Validation Class V.** Do NOT fork or integrate into the codebase. The value is as an **independent external consumer** testing petalTongue's semantic boundary. Forking destroys the independence that makes the validation meaningful.

If multilingual is needed in production: build server-side locale rendering in petalTongue (Rust-native). translate.js stays as the external validator that proves the semantic surface is correct.

If Guan responds positively: define a minimal petalTongue semantic fixture, hand it to him without ecosystem internals, see if translate.js can consume it. Document successes AND failures.

---

*Public contact. Source: email outreach from translate.js maintainer (Guan Leiming / xnx3). No prior relationship. Evaluated for external semantic validation of petalTongue presentation boundary.*
