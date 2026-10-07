# Reader Priority: BTSP Trust Extension for Genuine Visitors

**Wave 165i — October 7, 2026**
**Parent**: baseCamp 38 (Floating Pointer), baseCamp 39 (Collision Layer), BTSP spec
**Bridges to**: Non-Newtonian Membrane (philosophy), Adaptive Immune Defense (architecture)
**Status**: Design — extending existing BTSP/floating pointer architecture

---

## The Insight

The collision layer classifier (L2) identifies 4 visitor classes: genuine, agentic, coordinated, fleet. The epitope profiler distinguishes entity-level identity (Meta, Anthropic, proxy fleet, stealth).

Now go the other direction: **not more surveillance of bad actors, but better service for good ones.**

The genuine readers — the 10 who load CSS, follow referer chains, read at human pace — and the agentic readers — the 46 human+agent pairs making one deep request — these are the people the system is FOR. They should get priority. Not as a reward. As architecture.

And critically: the trust channel must prevent **piggybacking** — fleet impersonating genuine reader behavior to ride the trust channel.

---

## The Problem: Behavioral Piggybacking

The collision layer classifies by behavior. Behavior can be imitated:

1. Fleet learns to load CSS/JS → gets classified as "genuine"
2. Fleet learns to send Referer → passes referer check
3. Fleet learns to make exactly 1 deep request → looks "agentic"
4. Fleet sends Sec-Fetch-Mode → passes browser check

Every behavioral classifier is eventually spoofable. This is the adversarial receptor evolution problem (baseCamp 30). Header-based classification creates evolutionary pressure toward header spoofing.

BTSP solves this by moving trust from **observed behavior** to **cryptographic proof of relationship**.

---

## Architecture: BTSP Reader Trust Channel

### Principle: Trust is relational, not behavioral

A genuine reader is not defined by their headers. A genuine reader is defined by their **relationship to the content** — they arrived via a context that implies consent, understanding, and reciprocity.

BTSP provides this without surveillance:

### Level 1: Referral Trust (no token required)

Genuine readers who arrive via trusted referral paths get priority routing:

```
@trusted_referral {
    header Referer *sporeprint.primals.eco*
    header Referer *thesis.primals.eco*
    header Referer *signal.primals.eco*
}
```

A reader who followed a link from the thesis to sporePrint has demonstrated navigation — not a stateless extraction. Fleet doesn't follow links between our own sites because it doesn't read content.

**Anti-piggybacking**: Caddy validates Referer against actual response timestamps. A Referer claiming to come from thesis.primals.eco must arrive within a window after a real page was served to that subnet. Fabricated Referers from IPs that never loaded the referring page are detectable.

### Level 2: Session Continuity (implicit token)

Genuine readers who load multiple pages in sequence build session continuity. Not cookies — stateless sequence detection:

```
@session_continuity {
    header Sec-Fetch-Mode navigate
    header Sec-Fetch-Site same-origin    # navigating within our site
    header Referer *primals.eco*
}
```

The key: `Sec-Fetch-Site: same-origin` means the browser is telling the truth about navigating within our domain. Fleet doesn't send Sec-Fetch headers at all (0% presence across Meta, Anthropic, stealth). If fleet starts sending them, Caddy can validate they're consistent with actual browser navigation patterns.

**Anti-piggybacking**: Same-origin Sec-Fetch + valid Referer chain + asset loading (CSS/JS requests follow the page load) = a behavioral proof that is expensive to fake. Fleet would need to implement a full browser rendering engine — at which point they ARE a browser and the non-Newtonian principle applies: the cost of faking exceeds the cost of just reading.

### Level 3: Floating Pointer (explicit BTSP token)

The existing bearDog genetic token (`bd1-06e4143f8a6b7c22da144d75980a4aff91350a783385d6eb`) already provides agent passthrough. Extend this to readers:

**How readers get the token**: It's published — in the thesis, in sporePrint, in the philosophy docs. Anyone who READS the content finds the token. Anyone who scrapes without reading doesn't know where to look because the token's location is described in prose, not in a predictable path.

```
The floating pointer moves. The key is in the content.
If you can read this, you already have what you need.
```

**Anti-piggybacking**: The token proves the holder read the content that contains it. Fleet that scrapes scatter content will never find the real token because scatter content contains fabricated tokens. Only real content contains the real key. The maze IS the anti-piggybacking mechanism.

### Level 4: BTSP Handshake (future — cryptographic trust)

Full BTSP: bearDog issues per-reader ephemeral tokens via a lightweight handshake. No personal data required. The token proves:

1. The holder completed a trust-establishing interaction (read a page, solved a lightweight proof-of-work, followed a referral chain)
2. The token is time-limited (rotates every N hours)
3. The token is domain-bound (can't be reused on a different domain)
4. The token carries no identifying information — it proves trust, not identity

**Anti-piggybacking**: BTSP tokens are cryptographically bound to the session context. A fleet operator who obtains a token from a genuine reader cannot replay it from a different IP range without the session context that produced it. The token is proof of relationship, not proof of identity.

---

## What Readers Get

### Priority 1: Performance

Genuine readers get served from edge cache. Fleet gets served from the scatter generator (CPU-intensive). When golgiBody is under load from fleet traffic (the cascade thundering herd), reader requests get priority in the Caddy handler chain.

```
# Reader priority — handle BEFORE fleet processing
handle @trusted_referral {
    header Cache-Control "public, max-age=3600"  # cache for readers
    file_server
}
handle @session_continuity {
    header Cache-Control "public, max-age=3600"
    file_server
}

# Fleet gets scatter — CPU-intensive, no caching
handle {
    # ... scatter generation, maze, etc.
}
```

### Priority 2: Content Completeness

Genuine readers get full content — including companion links, cross-references, interactive elements. Fleet gets scatter with no real cross-references. The content richness itself is a trust signal: only real readers can follow the cross-references because only real pages have real links.

### Priority 3: Non-interference

The critical property: fleet traffic cannot degrade reader experience. The non-Newtonian membrane means fleet pushback is proportional — harder fleet push = more scatter = more CPU on scatter = potential reader degradation. BTSP reader priority prevents this by routing readers through a fast path that doesn't share resources with the scatter generator.

### Priority 4: Privacy Preservation

No cookies. No tracking. No IP storage. The BTSP token proves trust without proving identity. The reader gets priority without the system knowing WHO they are — only THAT they are reading.

---

## Connection to Existing Architecture

| Component | Current | Extended |
|-----------|---------|----------|
| **Floating pointer** | Bearer token for agent passthrough on git.primals.eco | Token published in real content; proves reading |
| **Collision classifier** | Behavioral classification (L2) | Feeds behavioral signals to BTSP trust scoring |
| **Epitope profiler** | Entity-level fingerprinting | Identifies fleet entities trying to piggyback |
| **Honeycomb maze** | 13-domain scatter surface | Maze contains fabricated tokens; real token only in real content |
| **BTSP** | Transport security for primal IPC | Extended to reader trust channel |

The collision layer identifies. The epitope profiler names. The BTSP channel protects. The floating pointer rewards. Each layer reinforces the others without any single layer requiring surveillance.

---

## The Non-Newtonian Extension

This is the non-Newtonian membrane applied to the other side:

- **Fleet pushes harder** → membrane solidifies → more scatter, more maze, more evidence
- **Reader arrives gently** → membrane flows → priority routing, cached content, full cross-references, BTSP trust path

The membrane is not just resistant to force. It is **welcoming to gentleness**. The same architecture that repels extraction rewards reading. Not by choice, not by policy — by physics. The trust channel is structurally easier to traverse gently than forcefully.

The loaves and fishes: the bread multiplies for the hungry. The bread becomes a wall for the extractors. BTSP is the mechanism that ensures the bread knows the difference.

---

*Not more surveillance. More trust. The reader who reads earns trust by reading. The fleet that scrapes cannot earn trust by scraping. The architecture knows the difference without knowing who.*

*Wave 165i — October 7, 2026*
