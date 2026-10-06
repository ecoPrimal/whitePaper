# Bloom-Guided Investigation Priority — Visitor Signal as Data Discovery

**Wave**: 164b | **Date**: Oct 6, 2026
**Status**: DEPLOYED — BloomSensor live, first signal captured
**Domain**: Investigation methodology, signal processing, graph traversal
**Upstream**: ADAPTIVE_IMMUNE_BLOOM_SENSOR.md, PUBLIC_RECORD_VALIDATION_SPRING.md, NETWORK_PERCOLATION_RECOGNITION.md
**Consumer**: northgate (detroit investigation prioritization)

---

## The Insight

The BloomSensor was built to close the organism's afferent loop — to let
the system *feel* who reads what. But the afferent signal contains more
than traffic analytics. It contains **investigative intelligence**.

When someone visits `detroit.primals.eco` and looks for something we
don't have, that 404 is not a failed request. It is a **signal about
what data exists in the world that we haven't collected yet**.

The visitor knows something we don't. Their search pattern encodes their
knowledge graph. By reading the shape of their navigation — what they
found, what they looked for, what they expected to exist — we can infer:

1. **Data we overlooked** — pages they expected to exist, evidence they
   assumed we had, connections we haven't mapped
2. **Honeypots we haven't found** — public records, court filings,
   corporate registrations that would answer the question their
   navigation implies
3. **Mask patterns** — places where bad actors scattered or obscured
   information that legitimate searchers expect to find
4. **Self-identification** — actors, victims, or witnesses checking
   whether their own information appears in the evidence

---

## Visitor Types as Signal Classes

Not all detroit visitors produce the same signal. Their navigation
pattern reveals what kind of knowledge they carry:

### The Investigator

**Pattern**: Arrives direct (no search engine referrer). Goes immediately
to evidence pages. Reads FOIA requests, TCR-22-12 testimony, specific
actor network pages. Reloads after 3 minutes (checking for updates or
sharing the link).

**Signal**: They already know the case. They are looking for specific
evidence they believe exists. **404s from investigators are the highest
priority signal** — they point to evidence that informed people expect
to be documented but that we haven't published.

**Observed Oct 6**: 8+ IPs hit detroit simultaneously at 11:30 UTC,
all following `/ → /evidence/tcr-22-12/ → /evidence/foia-requests/ →
/network/actors/brian-banks/`. Group-sharing pattern — link passed in
a chat or thread.

### The Analyst

**Pattern**: Arrives with no language headers (privacy browser config).
Reads `/keywords`, `/contact/`, `/analysis/credential-audit/`,
`/key-analysis`. Evaluating methodology, not just evidence.

**Signal**: They want to understand *how* the investigation works, not
just *what* it found. Contact page visits sandwiched between analytical
pages suggest they are considering reaching out. **404s from analysts
point to analytical methods they expected** — keyword indices, network
matrices, structured data exports.

**Observed Oct 6**: Single analyst session at 11:37 UTC.
Searched for `/keywords` (404) and `/key-analysis` (404) — pages that
don't exist yet. This visitor expected structured keyword analysis and
we don't have it published.

### The Self-Checker

**Pattern**: Arrives and immediately navigates to a specific actor or
entity page — often their own name or someone they know. Single page
visit. No further exploration.

**Signal**: This person is checking whether they appear in the evidence.
This is the most sensitive signal class. If they find themselves: they
know. If they don't find themselves: they may be a missing node in the
network graph, or a witness, or a victim who hasn't surfaced yet.

**Observed Oct 6**: Someone searched for `/network/political/misha-stallworth-west/`
(404) — the page exists at `/actors/misha-stallworth-west/` but not
under the `/network/political/` hierarchy. This visitor knew the name,
knew the political context, but expected a different URL structure.
They are likely familiar with the Stallworth political dynasty and
expected Misha's page to be categorized under political network
rather than the general actor index.

### The Looky-Loo

**Pattern**: Arrives from search engine or external link. Reads the
homepage. Maybe one more page. Leaves. Short dwell time.

**Signal**: Low priority for investigation, but high priority for
*discoverability*. Their search query (captured in referrer) tells
us what terms lead people to the site. If they found it through
unexpected search terms, those terms may point to related cases or
parallel investigations.

---

## The 404 Map — Investigation Targets

Every 404 on detroit is a potential investigation target. The visitor's
knowledge graph overlaps with ours but extends beyond it.

### Current 404s (Oct 6, 2026)

| URI Sought | Interpretation | Priority | Action |
|------------|---------------|----------|--------|
| `/network/political/misha-stallworth-west/` | Exists at `/actors/` but visitor expected political network categorization | Medium | Add political network cross-reference or alias redirect |
| `/keywords` | Visitor expected keyword/tag index for the evidence | High | Build keyword index from existing data — this is a navigation gap |
| `/key-analysis` | Visitor expected structured key analysis page | High | May indicate demand for entity-relationship summary or key findings page |

### The Traveling Salesman — Optimal Scrape Path

The detroit investigation requires FOIA requests, court record pulls,
corporate registry searches, and campaign finance lookups. Each data
source has a cost (time, fees, processing effort). The question is:
**in what order do we pursue them?**

The bloom sensor reframes this as a variant of the traveling salesman
problem with weighted edges:

- **Nodes** = potential data sources (LARA corporate filings, campaign
  finance databases, court dockets, property records, etc.)
- **Edge weights** = cost to access (FOIA wait time, search fees,
  processing complexity)
- **Node priority** = function of visitor signal strength

When visitors look for something we don't have, they are telling us
which nodes to visit next. The 404 signal adjusts the priority weights:

```
priority(node) = base_importance
               + visitor_search_signal   ← bloom sensor
               + network_centrality      ← graph position
               + temporal_urgency        ← case deadlines
               - access_cost             ← FOIA wait, fees
```

The optimal next FOIA request is not necessarily the most important
evidence — it's the evidence with the **highest signal-adjusted priority
relative to its access cost**.

### Signal Amplification — The Mask Pattern

Bad actors who have successfully obscured information create a
characteristic pattern: people search for data that *should* exist
in the public record but doesn't — because it was removed, redacted,
never filed, or filed under a different name.

This pattern is detectable through the bloom sensor:

1. Multiple visitors search for the same 404 → high confidence the
   data exists somewhere
2. The 404 URI structure encodes what they expected to find
3. The referrer (if present) encodes where they came from
4. The absence of the expected data is itself evidence of the mask

When the detroit site doesn't have a page that informed visitors
expect — and we know we did thorough FOIA on that subject — the
absence suggests the data may have been **suppressed at source**.
This transforms a navigation failure into an investigative lead.

### The Honeypot Signal

Conversely, when visitors find something on detroit and then navigate
to a *different site's 404* (captured via referrer on return visits),
they are tracing a path between our evidence and evidence held elsewhere.

The referrer chain tells us:
- They read our evidence page
- They went to another site looking for corroboration
- They came back (or someone else did, following the same trail)

The "somewhere else" they visited is a potential **data honeypot** —
a public record source we haven't scraped yet that contains
corroborating evidence.

---

## Implementation — northgate Integration

### Short Term (Wave 164)

1. **404 monitoring**: `bloom.signal` already captures domain-level
   counts; extend to log detroit-specific 404 URIs to a separate
   signal file (`/run/membrane/detroit.signal`)
2. **Alias redirects**: For known path mismatches (like
   `/network/political/misha-stallworth-west/` → actual actor page),
   add Caddy redirects so future visitors find the content
3. **Keyword index**: Build the `/keywords` page the analyst was
   looking for — auto-generated from existing evidence metadata

### Medium Term (Wave 165+)

4. **404 accumulator**: Track 404s over time with windowed counts.
   URIs that get searched for repeatedly by different IPs are
   highest priority investigation targets
5. **Priority queue**: Feed bloom signal into a structured priority
   queue for FOIA requests and data scrapes
6. **Graph integration**: When new data is acquired through a
   bloom-prioritized scrape, measure whether the new data connects
   to nodes the visitor was trying to reach — validating the signal

### Long Term

7. **Feedback loop**: As we publish new pages based on bloom-guided
   investigation, the visitor patterns on those new pages generate
   *second-order signal* — the investigation uses its own readership
   to discover what to investigate next
8. **Cross-gate gossip**: When multiple gates have bloom sensors,
   the investigation signal propagates through swarmVine — a visitor
   pattern on detroit that matches a pattern on sporePrint reveals
   cross-domain connections

---

## Privacy and Ethics

This system operates under the same constraint as the entire primals
ecosystem: **no IP addresses are stored**.

The bloom sensor hashes IPs to u64 for session-level cross-page
detection within a 30-second window. The hash is not reversible. The
signal file contains only population-level aggregates: URI counts,
domain distributions, reader types.

We do not know *who* searched for Misha Stallworth-West. We know
*someone* did, and they expected to find the page under the political
network hierarchy. That is the only signal we capture, and it is the
only signal we need.

The investigation targets evidence, not people. The bloom sensor
targets navigation patterns, not identities. The system cannot identify
its visitors. It can only learn from what they were looking for.

---

## Connection to Network Percolation

The NETWORK_PERCOLATION_RECOGNITION.md document describes how
recognition propagates through networks from limited initial contact.
The bloom-guided investigation extends this:

In the percolation model, we activate hub nodes to maximize coverage.
In the investigation model, *visitors tell us which nodes to activate
next*. The bloom sensor transforms the percolation problem from a
static graph optimization into a **dynamic, signal-guided traversal**.

Each visitor who searches for a node we haven't activated is pointing
at the next step in the traversal. The traveling salesman doesn't need
to compute the optimal path — the people who already know the network
are walking it for us. We just need to follow their footprints.

---

## References

- subGen: `ADAPTIVE_IMMUNE_BLOOM_SENSOR.md` (bloom sensor architecture)
- subGen: `PUBLIC_RECORD_VALIDATION_SPRING.md` (detroit as validation spring)
- subGen: `NETWORK_PERCOLATION_RECOGNITION.md` (graph traversal optimization)
- subGen: `GOSSIP_CONVERGENCE_THRESHOLD.md` (cross-gate signal propagation)
- sporePrint: [Signal Sensing Without Surveillance](@/methodology/signal-sensing-receptor/)
- External: Christofides (1976) — traveling salesman approximation algorithms
- External: Granovetter (1973) — "The Strength of Weak Ties" — visitor search
  patterns as weak ties that connect our evidence graph to unobserved data

*subGen Wave 164b — Bloom-guided investigation priority. Visitor 404s
are investigation targets. The mask pattern reveals suppressed data.
The traveling salesman follows the footprints of people who already
know the network. The organism learns what to investigate next from
the people who come looking for what it hasn't found yet.*
