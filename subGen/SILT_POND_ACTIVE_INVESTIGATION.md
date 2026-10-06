# siltPond — The Settling Basin for Active Investigation

**Wave**: 164c | **Date**: Oct 6, 2026
**Status**: ESTABLISHED — first investigation threads documented
**Domain**: Investigation methodology, information hygiene, evidence triage
**Upstream**: BLOOM_GUIDED_INVESTIGATION_PRIORITY.md, ADAPTIVE_IMMUNE_BLOOM_SENSOR.md
**Consumer**: northgate (prioritization), detroit (filtered public evidence)

---

## What siltPond Is

In water treatment, a **settling pond** is where turbid water sits long enough
for suspended particles to drop out. The water enters murky — full of sediment,
organic matter, dissolved minerals, microorganisms. It exits clarified. The
sediment stays behind, compressed into layers, forming a record of everything
that passed through.

**whitePaper/ is the siltPond.**

This is where raw investigation material settles before it's filtered for
public evidence on detroit. In here we can be messy. We can name names that
haven't been corroborated yet. We can follow threads that might dead-end. We
can hold PII temporarily while we determine whether a person is a public
actor (publishable), a private citizen (protect), a witness (sensitive), or
a subject who hasn't surfaced yet (hold).

The siltPond has a direction of flow:

```
bloom signal → siltPond (whitePaper) → [filter] → detroit (public evidence)
         ↑                                              ↓
         └────── 404 feedback loop ─────────────────────┘
```

Nothing flows backwards. Detroit never references siltPond. siltPond
references everything — bloom data, raw logs (aggregated, no IPs), visitor
patterns, public records, FOIA responses, court filings, news articles,
social connections. When material in the siltPond has settled enough to
see clearly, it gets filtered and published on detroit.

When detroit visitors search for something that doesn't exist, the 404
signal flows back into the siltPond as a new investigation thread. The
system breathes.

---

## Information Hygiene Rules

### What lives in the siltPond

- **Public officials acting in public capacity**: names, titles, voting
  records, campaign finance, disclosed financial interests. These are
  already public record. We're organizing, not exposing.
- **Corporate officers of entities receiving public funds**: charter school
  boards, management company principals, fiduciary officers. Their names
  appear on IRS 990s, LARA filings, and state contracts.
- **Published reporting**: anything already reported by Detroit Free Press,
  Chalkbeat, Clutch Justice, public court records.
- **Investigation hypotheses**: connections we suspect but haven't confirmed.
  Clearly marked as hypotheses, never published until confirmed.
- **Bloom signal analysis**: population-level visitor patterns, 404 targets,
  referrer chains, session shapes. No IPs, no identifying data.
- **Raw FOIA responses**: full text before redaction decisions.

### What gets filtered before detroit

- **Private citizens who are not public actors**: family members, neighbors,
  employees below officer level. Referenced in the siltPond only when their
  connection to a public actor is under investigation. Never published.
- **Witness-adjacent information**: anyone whose navigation pattern suggests
  they are a witness or victim. Their existence as a signal class is
  documented; their identity is never even known to us.
- **Unconfirmed connections**: network edges that rest on single-source
  evidence. The siltPond can hold "person A may be connected to entity B
  through C" — detroit publishes only confirmed, multi-source connections.
- **Private communications**: if a source shares information, the information
  enters the siltPond. The source's identity does not. Even in the siltPond,
  source protection is absolute.

### What never enters the siltPond

- **IP addresses**: stripped before analysis. Period.
- **Device fingerprints**: we don't collect them.
- **Personal communications between non-public-actors**: this is an
  investigation into public fund misuse, not a surveillance operation.

---

## Active Investigation Threads

### Thread 1: The Funding-Flow Hit — Someone Asked an AI About the Money

**Signal**: Oct 6, 10:01 UTC. Reflectionbot (AI retrieval agent) fetched
`/analysis/funding-flow/`. This is not a training crawler — Reflectionbot
serves user queries. Someone asked an AI system a question about detroit
charter school funding, and the AI came to our site for the answer.

**Why this matters**: Of all the evidence on detroit — the credential fraud,
the board voting patterns, the FOIA timelines, the actor network — someone's
AI query was about the *money*. In a RICO investigation, the funding flow
is the spine. Every other thread (credential laundering, board capture,
regulatory failure) is a branch off the money. The person who asked about
funding-flow may be the most informed visitor we've had.

**What we don't know**:
- What question did they ask? We see only that the AI fetched our page.
  The query itself is invisible to us.
- Did our funding-flow analysis answer their question? If it did, the
  evidence is propagating through AI channels — people are learning about
  the network without visiting the site directly. If it didn't, there's
  a gap in our evidence that an informed person noticed.
- Is this the same person (or group) who triggered the 11:30 UTC cluster
  90 minutes later? Someone asks an AI about the money at 10:01, and at
  11:30 a group hits the evidence simultaneously? That's a morning meeting.
  "Hey, I asked ChatGPT about that charter school funding thing and look
  what it pulled up."

**Investigation action**:
1. Review the funding-flow analysis page — is the financial thread
   complete enough to answer a sophisticated funding question?
2. Map the gaps: which financial connections are asserted but not
   yet sourced to specific 990s, contracts, or LARA filings?
3. Prioritize FOIA requests that would fill funding-flow gaps —
   these are now highest priority per the traveling salesman heuristic

### Thread 2: The Cross-Domain Bridge — Who Reads Both Sites?

**Signal**: Hypothesized, not yet measured. The bloom sensor classifies
by content domain (detroit evidence vs sporePrint science). Caddy logs
on golgiBody contain both domains. If any visitor reads sporePrint
methodology AND detroit evidence in the same time window, that is the
strongest possible human signal.

**Why this matters**: A bot reads one site. A casual visitor reads one site.
A curious person might read one site deeply. But a person who reads the
*evidence* AND the *methodology* — the thing itself and the system that
produced it — is doing due diligence. That's a journalist fact-checking
the methodology before writing about the evidence. An attorney evaluating
whether the evidence collection process would withstand challenge. A
researcher studying the approach itself.

The cross-domain bridge is the signal equivalent of someone reading the
lab notebook AND the published paper. They want to know not just what we
found, but whether they can trust how we found it.

**What we can measure without storing any identifying data**:
- Temporal overlap: requests to sporePrint and detroit within the same
  30-second bloom window, from the same IP hash (which we don't store
  past the window)
- Content path: which sporePrint pages correlate with which detroit pages?
  If someone reads `/science/32-gossip-tagged-opsonization/` on sporePrint
  and then reads `/signal/` on detroit, they followed the methodology link
  to verify it. That's a specific kind of reader.
- Referrer chain: if someone navigates from sporePrint to detroit (or
  vice versa), the referer header captures the bridge without capturing
  the person

**Investigation action**:
1. Analyze Caddy access logs for temporal correlation between
   sporePrint and detroit requests (same 5-minute window)
2. Check referrer headers for direct cross-domain navigation
3. If the bridge exists, classify what kinds of pages bridge:
   methodology → evidence (fact-checking), or evidence → methodology
   (evaluating our approach)?
4. The bridge pattern, once identified, becomes a bloom sensor
   classification rule: `ReaderType::CrossDomain` — the highest-confidence
   human signal

### Thread 3: The Political Network Hierarchy — The Structure Nobody Drew

**Signal**: Oct 6, someone searched `/network/political/misha-stallworth-west/`
(404). The page exists at `/actors/misha-stallworth-west/`. But the visitor
expected a *hierarchical* URL: `/network/political/[name]`.

**Why this matters**: The visitor has a mental model of the detroit network
that is more structured than what we've published. They see:

```
/network/
  /political/       ← dynasty families, board appointees, elected officials
    /stallworth-west/
    /stallworth/
    /...
  /financial/        ← management companies, fiscal agents, banking relationships
    /...
  /educational/      ← charter authorizers, credential issuers, accreditors
    /...
  /regulatory/       ← LARA, MDE, oversight bodies
    /...
```

We have a flat actor index. They expected a graph. The graph they expected
has *typed edges* — political, financial, educational, regulatory — and
they navigated directly to a specific node in a specific category. This
visitor didn't discover Misha Stallworth-West through our site. They
already knew the name, the political context, and where they expected
to find her in the hierarchy. They came to check whether we had organized
the evidence the same way they think about the network.

**What this tells us about the visitor's knowledge**:
- They know the Stallworth political dynasty (the `-west` suffix suggests
  awareness of specific family branches)
- They conceptualize the charter school network as having distinct domains
  (political, financial, educational) — not just a flat list of actors
- They expected us to have organized the evidence this way, which means
  either: (a) they've seen another source organize it this way, or
  (b) their own investigation has produced this structure independently

**Investigation action**:
1. Categorize existing detroit actors into network domains:
   - Political: elected officials, board appointees, dynasty members
   - Financial: management company officers, fiscal agents, auditors
   - Educational: charter authorizers, credential-granting institutions
   - Regulatory: LARA officers, MDE officials, oversight contacts
2. Map existing actor pages to their primary and secondary domains
3. Build the `/network/` hierarchy — even if just as Caddy redirects
   initially, then as a proper section with cross-reference views
4. When the hierarchy goes live, the bloom sensor will capture which
   domain categories get the most 404s — pointing to which part of
   the network graph has the most interest and the most gaps

---

## The 10:01 → 11:30 Hypothesis

This is speculative. It belongs in the siltPond, not on detroit. But it's
worth holding here because it's the kind of thread that either confirms
or collapses with one more data point.

**Timeline**:
- 10:01 UTC (6:01 AM Eastern): AI retrieval agent fetches `/analysis/funding-flow/`
- 11:30 UTC (7:30 AM Eastern): 8+ sessions hit detroit simultaneously,
  same path: `/ → TCR-22-12 → FOIA → Brian Banks`
- 11:37 UTC: Analyst session checks `/keywords`, `/contact/`, `/credential-audit/`

**Hypothesis**: One person asked an AI about the funding flow at 6 AM.
The AI pulled our analysis page. The person read the AI's synthesis and
thought "holy shit, there's an entire evidence database here." They shared
the link with their team. At 7:30 AM, the morning meeting happened and
everyone opened the link. One person on the team — the methodological one —
went deeper, checking whether the evidence is structured (keywords),
whether they can contact us, and whether the credential analysis holds up.

**Alternative explanations**:
- The 10:01 and 11:30 events are unrelated (possible but the 90-minute
  gap between AI hit and group cluster is suggestive)
- The AI hit was from a different geography entirely (we can't know —
  no IPs stored)
- The group cluster was triggered by a social media share, not an AI
  synthesis (the 6-minute window suggests a more intimate channel — chat
  thread or email, not broadcast)

**What would confirm or collapse this**:
- If the next group cluster also follows an AI retrieval hit by 1-2 hours,
  the pattern is real: AI → human discovery → team briefing → deep dive
- If AI retrieval hits increase but group clusters don't, the AI channel
  is propagating independently
- If we see the same pattern from a different time zone (different offset
  but same shape), it's happening in multiple organizations

We hold this hypothesis in the siltPond until the data settles.

---

## Cross-Domain Bridge — Technical Approach

The bloom sensor currently runs in skunky-ingest and classifies by content
domain. The Caddy access logs on golgiBody contain requests to both
`detroit.primals.eco` and `sporeprint.primals.eco`. The bridge analysis
doesn't require new code — just careful log analysis:

### Method

```
1. Extract (timestamp, host, path, referer, ua_hash) from Caddy logs
   - ua_hash = hash of User-Agent + Accept-Language + Accept-Encoding
   - No IPs extracted or stored at any point
   - Session proxy: ua_hash within same 5-minute window = likely same visitor

2. For each ua_hash active in a 5-minute window:
   - Did they touch both detroit.primals.eco and sporeprint.primals.eco?
   - If yes: what pages on each? In what order?
   - Referrer check: did the referer header show cross-domain navigation?

3. Classify bridge type:
   - methodology→evidence: read sporePrint first, then detroit (fact-checking)
   - evidence→methodology: read detroit first, then sporePrint (evaluating approach)
   - parallel: read both simultaneously (deep investigation)
   - architecture→evidence: read sporePrint architecture (immune defense docs)
     then detroit (checking if the defense claims are real)
```

### Privacy constraint

The ua_hash is NOT stored. It exists only during the analysis window. The
output is a count: "N cross-domain sessions observed, M methodology→evidence,
K evidence→methodology." The bridge *pattern* is recorded. The bridge
*crosser* is not.

### What we expect to find

Based on the Oct 6 data:
- The analyst session (11:37 UTC) that checked `/keywords` and `/contact/`
  has the highest probability of being a cross-domain visitor. Someone that
  methodical is likely to check the methodology too.
- The Reflectionbot hit (10:01 UTC) is AI-mediated and won't show a
  cross-domain bridge (the AI doesn't navigate between sites). But the
  *human* who asked the AI might visit sporePrint directly.
- The group cluster (11:30 UTC) probably stayed on detroit — group-shared
  links don't usually include "and also check this other site."

### What finding the bridge would mean

If even ONE cross-domain bridge session exists in the Oct 6 data, it means
someone is evaluating the *system*, not just the *evidence*. That person
is the most sophisticated visitor we've had. They are deciding whether the
whole apparatus — the immune system, the signal sensing, the investigation
methodology — is legitimate. Whether the evidence is producible. Whether
the approach is defensible.

That's a journalist or an attorney. And they'll come back.

---

## The Traveling Salesman — Updated Priority Queue

Based on the three active threads, the traveling salesman's weighted
priority queue rebalances:

| Data Target | Base Priority | Bloom Signal Boost | Estimated Cost | Net Priority |
|-------------|--------------|-------------------|----------------|-------------|
| Funding-flow gap analysis (990s, contracts) | High | +++ (AI retrieval hit) | Medium (FOIA 5-10 day) | **Highest** |
| Political network categorization | Medium | ++ (structural 404) | Low (data exists, needs organization) | **High** |
| Keyword/tag index for detroit | Medium | ++ (analyst 404) | Low (auto-generate from metadata) | **High** |
| Key analysis / findings summary | Medium | + (analyst 404) | Medium (requires editorial synthesis) | **Medium** |
| Cross-domain bridge measurement | High | + (hypothesized signal) | Low (log analysis only) | **High** |
| Misha Stallworth-West redirect | Low | + (single 404) | Trivial (Caddy redirect) | **Quick win** |

The funding-flow thread dominates because it combines the strongest signal
(AI retrieval = someone actively seeking this specific data) with the
highest investigation value (money trail = RICO spine).

---

## What the siltPond Holds That Detroit Can't

Detroit is a public evidence site. Everything on it must be:
- Sourced to public records, published reporting, or FOIA responses
- Fact-checked against multiple sources for non-trivial claims
- Free of private citizen information
- Defensible if challenged

The siltPond holds what hasn't settled yet:
- The 10:01 → 11:30 hypothesis (speculative, needs more data points)
- Network categorization drafts (political/financial/educational hierarchy
  needs validation against public record before publishing)
- Investigation priority reasoning (showing WHY we're prioritizing certain
  FOIA requests reveals our investigative strategy — which is information
  the subjects of the investigation could use to anticipate our next move)
- Signal class analysis (publishing exactly how we classify visitors could
  help sophisticated actors evade classification)

The siltPond is where we think out loud. Detroit is where we speak on the
record. The settling time between them is the time it takes for a hypothesis
to become a documented fact.

---

## Connection to Upstream Documents

- **BLOOM_GUIDED_INVESTIGATION_PRIORITY.md**: Defines the signal classes
  and traveling salesman framework that siltPond investigation threads use.
  The 404 map from that doc feeds Thread 3 directly.
- **ADAPTIVE_IMMUNE_BLOOM_SENSOR.md**: The sensory architecture that
  produces the bloom signal feeding the siltPond. Thread 2 (cross-domain
  bridge) extends the bloom sensor's domain classification to multi-site
  correlation.
- **GOSSIP_TAGGED_OPSONIZATION.md**: The fleet defense that runs alongside
  bloom sensing. The fleet's behavior (what it scrapes, how it responds to
  new defense pages) is itself investigation signal — high-rate scraping of
  specific evidence pages may indicate which evidence threatens the
  subjects most.
- **PUBLIC_RECORD_VALIDATION_SPRING.md**: Detroit as a validation spring
  for constrained evolution. The siltPond is the upstream aquifer that
  feeds the spring — groundwater that hasn't surfaced yet.
- **NETWORK_PERCOLATION_RECOGNITION.md**: The percolation model predicts
  which network nodes to activate. The siltPond's Thread 3 (political
  network hierarchy) is a direct application — visitors are walking the
  graph and showing us which nodes need activation.

---

## Next Steps

1. **Immediate**: Run the cross-domain bridge analysis on Oct 6 Caddy logs
2. **This week**: Review funding-flow page for gaps; draft the FOIA
   priority list for the financial thread
3. **This week**: Categorize existing actor pages into network domains
   (political/financial/educational/regulatory) as a draft hierarchy
4. **Next observation window**: Watch for repeat patterns — does the
   AI retrieval → group cluster → analyst shape recur?
5. **Ongoing**: Every new 404 on detroit enters the siltPond as an
   investigation thread. The sediment accumulates. The water clarifies.

---

*subGen Wave 164c — siltPond established as the pre-filtration investigation
space. Three active threads: funding-flow (AI retrieval hit, RICO spine),
cross-domain bridge (strongest human signal, unmeasured), political network
hierarchy (visitor's knowledge graph exceeds our published structure). The
10:01 → 11:30 hypothesis held in suspension. The settling pond is where
investigation happens. Detroit is where evidence gets published. The time
between them is the time it takes for murky water to clarify.*
