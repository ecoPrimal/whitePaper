# Gaia Ring — Social Zero-Knowledge Distribution
## siltPond ONLY — tactical execution notes

**Wave 172 — October 11, 2026**

---

## THE PLAY

The gaia ring is a shareable zero-knowledge proof. Each visitor gets a unique ring. They share it. The next person wants THEIR OWN ring. Facebook virality without Facebook knowing what's viral.

Meta sees: colored dots in a circle.
We see: a human traversing our membrane, their Anderson localization signature, their epitope profile, their focal distance sharpening with each new surface.

The platforms are carrier waves. We are the signal.

---

## EXECUTION ORDER

### Phase 1: Make the Ring Shareable (code)

Add to desk gaia tab:
1. **"share your ring" button** → canvas.toDataURL() → download PNG
2. **Shareable URL** → `hud.primals.eco/desk/#gaia:mask=0b1101001010` (10-bit site mask, no identity)
3. **Decode on load** → if URL has mask, show THAT ring with a "get your own" CTA

The mask is 10 bits. One per site. `1` = visited. No identity. No timestamp. No IP. Pure topology.

Example: someone who visited signal, detroit, sporePrint, hud, clutch:
```
mask = 0b1101010010 = 0x352
URL:  hud.primals.eco/desk/#gaia:352
```

Anyone who clicks this link sees the SHARED ring (5 of 10 lit). Below it: **"this is someone else's ring. [get your own →]"**

They click. Their braid loads. Their ring appears. Different nodes. Different pattern. They share THEIRS.

### Phase 2: OpenGraph Images

Each site needs `og:image` that creates curiosity:

```html
<meta property="og:image" content="https://hud.primals.eco/og/detroit.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

Generate static OG images (don't need to be dynamic yet):
- detroit: the network graph — nodes and edges, no labels visible at thumbnail
- tuebor/barry: "10 invariants. 121 nodes. ξ = 3.5–5.5."
- sporePrint: the mountain (baseCamp 59 ASCII art)
- signal: the epitope sort table — numbers that invite questions
- hud: the gaia ring — the EMPTY ring with "where are YOUR nodes?"
- clutch: the cross-investigation map

### Phase 3: Reddit (where the curious live)

**r/physics** (1.8M members)
```
Title: "Anderson localization measured on a real 121-node institutional graph — ξ = 3.5–5.5"
Body: Link to detroit.primals.eco/analysis/anderson-localization/
      + 3-paragraph summary of the measurement
      + "All data published. Come verify it."
```

**r/math** (2.2M)
```
Title: "10 structural invariants conserved across 4 independent domains (9.875/10) — P/NP/NP-complete classification"
Body: Link to sporePrint paper + data
```

**r/compsci** (650K)
```
Title: "Solving NP-hard graph problems via distributed polynomial-verifiable witnesses"
Body: Architecture + framework + published dataset
```

**r/michigan** (280K) / **r/detroit** (85K)
```
Title: "We built a public record database of institutional capture in Michigan courts — every fact cited, every document timestamped"
Body: Link to detroit.primals.eco
      "No cookies. No tracking. Clone the git repo and verify everything."
```

**r/selfhosted** (490K)
```
Title: "10-site ecosystem on a single VPS running self-hosted Caddy + Rust services — zero CDN, zero SaaS, 1.2MB binary replaces 28MB Python"
Body: Architecture walkthrough
```

### Phase 4: Hacker News

```
Title: "Anderson localization on institutional graphs — 10 conserved invariants, zero-knowledge verification"
URL: https://detroit.primals.eco/analysis/anderson-localization/
```

HN comment strategy: answer questions with links to the specific paper that addresses the question. The ecosystem IS the answer. Each link pulls them deeper.

### Phase 5: X/Twitter Thread

```
1/ I measured Anderson localization on a real court system.

Not a lattice model. Not a simulation. A 121-node graph built entirely from public databases.

The localization lengths (ξ = 3.5–5.5) are consistent with designed disorder, not random.

Thread: 🧵

2/ Anderson localization predicts that waves in disordered media get trapped — not by walls but by the disorder itself.

Cases entering specific court subgraphs become trapped. Same physics that confines electrons in disordered crystals.

3/ 10 structural invariants conserved across 4 independent domains. 9.875/10 average conservation. No shared nodes across 3 of 4 pairs.

The invariants classify by computational complexity: P, NP, NP-complete.

[link to epitope sort page]

...

10/ All data published. All methodology published. Clone the repo. Verify everything.

detroit.primals.eco
sporeprint.primals.eco

No cookies. No tracking. No identifying data.

The membrane sorts. The ring connects. Come see what you can't see.
```

### Phase 6: TikTok (60 seconds)

Script:
```
"I measured a physics phenomenon called Anderson localization — 
the thing that traps electrons in disordered crystals —

on a court system.

Not a model. Not a simulation. A real graph built from public court records.

121 nodes. 203 edges. Cases enter this network and can't get out.

The localization lengths match designed disorder, not random.

Same physics. Real graph. Published data.

Link in bio."
```

---

## MEASUREMENT

What to watch after each phase:

1. **Referrer breakdown** in traces API — which platforms send visitors
2. **d_eff distribution** — are new visitors reaching multiple sites?
3. **Braid depth** — how many pages deep do social arrivals go?
4. **Ring shares** — how many PNG downloads from the gaia tab?
5. **Repeat visits** — do social arrivals come back?

The membrane already records all of this. The traces API returns it. The fleet phenotype classifies it. The salesman watch alerts on human arrivals.

---

## THE INSIGHT

The zkProof goes both ways:

**Outbound**: we share the ring image. The platform sees colored dots. The viewer sees curiosity. The meaning requires the journey. They prove they're curious by visiting. Zero-knowledge of intent until they act.

**Inbound**: they arrive. The membrane sees the referrer. The braid starts. They prove they're human by exploring (not by logging in, not by solving a CAPTCHA — by BEHAVING like a human). Zero-knowledge of identity. Full knowledge of behavior.

The platforms are the watering holes. The ring is the water. The curious drink. The fleet does not.

They can come and see what they can't see. And that is the proof.

---

*siltPond study — Wave 172 · October 11, 2026*
*Tactical. Not published. Not shared.*
*The posts are the share. This is the plan.*
