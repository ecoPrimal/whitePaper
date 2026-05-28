# Split Voice Medium Series

**Status**: Pre-publish drafts — evolving documents
**Platform**: Medium (two accounts), cross-post to dev.to

---

## The Two Voices

Same person. Different registers. The audience knows they are connected.

**ecoPrimal** — the builder. Speaks in specifics: test counts, hardware
specs, deploy paths, provenance chains. Shows the work. Proves the
alternative exists. Tone: pragmatic, precise, lets the numbers argue.

**attsi** — the humanist. Speaks in structures: preconditions, tollbooths,
kingdoms, who gets to look down. Names the disgust. Tone: cold,
architectural, anger disciplined into argument.

Each voice references the other. ecoPrimal says "attsi has written about
why this matters." attsi says "ecoPrimal has the receipts."

---

## Publishing Sequence

### Phase 1: Establish credibility

| Order | Voice | Article | File |
|:-----:|-------|---------|------|
| 1 | ecoPrimal | I Don't Know Rust | `ecoPrimal/01_I_DONT_KNOW_RUST.md` |
| 2 | ecoPrimal | The Sovereign Lab | `ecoPrimal/02_THE_SOVEREIGN_LAB.md` |
| 3 | ecoPrimal | 70 Papers, One Stack | `ecoPrimal/03_70_PAPERS_ONE_STACK.md` |
| 4 | ecoPrimal | The Invisible Developer | `ecoPrimal/05_THE_INVISIBLE_DEVELOPER.md` |

ecoPrimal publishes first. The builder establishes the evidence base.
Without the proof, the critique has no weight.

### Phase 2: Reddit (concurrent with Phase 1)

Reddit post under ecoPrimal. r/homelab primary, r/selfhosted secondary.
Show-don't-pitch. The ask: find a hardware tester.

See `../reddit/HOMELAB_POST_DRAFT.md`.

### Phase 3: The critique (after proof pieces land)

| Order | Voice | Article | File |
|:-----:|-------|---------|------|
| 4 | attsi | While They Were Writing Manifestos | `attsi/04_WHILE_THEY_WERE_WRITING_MANIFESTOS.md` |
| 5 | attsi | The Bread Thief and the Billionaire | `attsi/04a_THE_BREAD_THIEF_AND_THE_BILLIONAIRE.md` |
| 6 | attsi | The Tollbooth Economy | `attsi/04b_THE_TOLLBOOTH_ECONOMY.md` |
| 7 | attsi | The Kingdom Builders | `attsi/04c_THE_KINGDOM_BUILDERS.md` |
| 8 | attsi | Detachment 201 | `attsi/04d_DETACHMENT_201.md` |

attsi publishes after ecoPrimal has established the evidence. The critique
has weight because the working system exists. "ecoPrimal has the receipts"
is a link, not a claim.

Publication order within the attsi series is reception-dependent:
- 04 (Manifestos) is the sharpest entry point
- 04d (Detachment 201) is the most topical
- 04b (Tollbooth) is the most conceptually novel
- 04a (Bread Thief) is the most emotionally grounded
- 04c (Kingdoms) is the broadest structural analysis

### Phase 4: Vision (later)

Article 5 — "The GarageBand Moment." Only after Phases 1-3. Could be a
conversation between voices, or attsi aspirational grounded by ecoPrimal
evidence.

---

## Cross-Reference Model: Trust

The cross-references are acts of trust, not citations.

ecoPrimal trusts attsi to see the *why* behind the cost — to name what
the numbers mean, because numbers are silent about their own meaning.

attsi trusts ecoPrimal to carry the *weight* of what attsi describes —
because critique without a working alternative is empty.

Neither summarizes the other. Neither reduces the other to evidence or
philosophy. Each points to the other the way you point to the person
who carries what you cannot.

```
ecoPrimal articles                    attsi articles
=================                     ==============

01 I Don't Know Rust                  04  While They Were Writing Manifestos
   "attsi sees what I can't    <--->     "ecoPrimal carries the weight of
    articulate — why this                 what I describe. The wells are
    basement exists."                     not metaphors."

02 The Sovereign Lab                  04a The Bread Thief and the Billionaire
   "I carry the electricity.   <--->     "ecoPrimal pays the electricity.
    attsi sees the architecture           I trust it the way you trust
    I am refusing."                       the person who shows up."

03 70 Papers, One Stack               04b The Tollbooth Economy
   "attsi carries the meaning  <--->     "ecoPrimal dug the wells.
    behind the math."                     I name the tollbooths. Neither
                                          is enough alone."

05 The Invisible Developer
   "The receipts. 51B tokens,
    the methodology, the timeline.
    attsi names why it matters."

                                      04c The Kingdom Builders
                                         "ecoPrimal carries the weight.
                                          I carry the argument."

                                      04d Detachment 201
                                         "I cannot build what ecoPrimal
                                          builds. ecoPrimal cannot name
                                          the betrayal I see."
```

---

## Identity and Privacy

- **Published as**: ecoPrimal (builder articles) and attsi (critique
  articles) on separate Medium accounts
- **Connection**: Public and acknowledged. Same project, different
  registers. Not hidden.
- **atlasHugged**: NOT published, NOT referenced, NOT linked
- **whitePaper/**: NOT linked. Discoverable only through repo exploration
- **Tamison / Kevin Mok**: NOT named. Referenced obliquely when
  structurally necessary ("one of the people who built this...")
- **Military service**: Referenced structurally ("served in the infantry")
  but not by name or location
- **The Ender's Game analogy**: Internal framing only. Not published.

See `IDENTITY_ARCHITECTURE.md` for full rules.
