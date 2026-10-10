# STUDY: Tommy Boy SEO + BingoCube Crawler Training Loop
## October 9, 2026

---

## THE CONCEPT

The bingoCube currently classifies visitors on three axes (Attention/Curiosity/Interaction) to separate Fleet from Humans. That's the DEFENSE use.

The OFFENSE use is the inverse: watch **legitimate search crawlers** (Googlebot, Bingbot, DuckDuckBot, YandexBot, Baidu) discover and index the Tommy Boy page, then adjust SEO signals to maximize the association between Barrett-related search terms and the page.

### Input → Output → Train

```
┌─────────────────────────────────────────────────┐
│                  INPUT LAYER                     │
│                                                  │
│  SEO Metadata ──── JSON-LD Structured Data       │
│  Keywords ──────── Internal Cross-Links          │
│  Headings ──────── External Citation Links       │
│  Description ───── OpenGraph / Twitter Cards     │
│  Sitemap ───────── robots.txt Allow              │
│  Content Density ─ Concept Term Frequency        │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│              OBSERVATION LAYER                   │
│           (bloom + bingoCube on golgi)           │
│                                                  │
│  Which crawlers hit /analysis/tommy-boy/ ?       │
│  What User-Agent strings? (Googlebot, Bingbot)   │
│  How deep do they crawl? (follow internal links?)│
│  Do they fetch CSS/JS? (render = deeper index)   │
│  What referer data leaks through?                │
│  Crawl frequency? (re-crawl = priority signal)   │
│  Which linked pages do they visit FROM tommy-boy?│
│  Time between first crawl and SERP appearance?   │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│                 TRAINING LOOP                    │
│                                                  │
│  IF Googlebot hits tommy-boy frequently:         │
│    → content is being indexed, maintain          │
│  IF Googlebot hits tommy-boy but NOT related:    │
│    → strengthen internal links TO related pages  │
│  IF Googlebot skips tommy-boy:                   │
│    → check: sitemap present? canonical correct?  │
│    → increase inbound links from indexed pages   │
│  IF SERP query data shows wrong terms ranking:   │
│    → adjust H2 headings to match target terms    │
│    → densify target terms in first 200 words     │
│  IF new Barrett news cycle:                      │
│    → append timely update section to page        │
│    → re-submit sitemap to Google Search Console  │
└─────────────────────────────────────────────────┘
```

---

## TARGET CONCEPT CLUSTER

Every search term that should resolve to Tommy Boy. Organized by priority:

### Tier 1 — Direct Barrett Searches (highest value)

| Target Term | Current Competition | Our Advantage |
|-------------|-------------------|---------------|
| "Tom Barrett convicted felon" | MLive, WWMT articles | We have the FEC/LARA inversion they don't |
| "Tom Barrett Dykema" | Nothing exists | ZERO competition — we own this term |
| "Barrett wrong election date" | CNN, NYT (2024 articles) | We connect it to the SAME strategist |
| "who funds Tom Barrett" | FEC raw data | We make it readable + connect to dark money |
| "Tom Barrett MI-7 donors" | FEC raw data | Same — we're the human-readable version |
| "Tom Barrett campaign donors 2026" | FEC, OpenSecrets | We add the entity analysis layer |

### Tier 2 — Entity Association (medium value, high SEO impact)

| Target Term | Why It Matters |
|-------------|---------------|
| "Dykema Gossett Federal PAC" | Anyone researching Dykema PAC finds our entity chain |
| "Jason Roe strategist Michigan" | $782K consultant — anyone Googling him finds Barrett connection |
| "Save Detroit Jobs Kenneth Daniels" | The dark money entity + convicted felon president |
| "Dykema dark money Michigan" | Already in our OS page — Tommy Boy adds the Barrett node |
| "NRCC socialist felon Lawrence" | Direct NRCC quote — anyone seeing the NRCC label and Googling it |

### Tier 3 — Concept Searches (long-tail, high intent)

| Target Term | Search Intent |
|-------------|--------------|
| "Michigan 7th district race 2026" | Voters researching their race |
| "William Lawrence MI-7" | Lawrence supporters/researchers |
| "Rent Is Too Damn High Michigan" | Tenant advocates finding the connection |
| "Barrett voter suppression" | Researchers connecting the wrong-date ad |
| "Tom Barrett campaign finance" | Journalists following the money |
| "Michigan Clean Slate Act convicted felon" | Policy researchers |
| "Tom Barrett AIPAC" | AIPAC tracking community |

### Tier 4 — November Surge Terms (time-sensitive)

| Target Term | When It Peaks |
|-------------|--------------|
| "Tom Barrett" | Oct-Nov 2026 (election cycle) |
| "Michigan 7th district" | Oct-Nov 2026 |
| "vote November 3 Michigan" | Late Oct 2026 |
| "MI-7 candidates" | Oct-Nov 2026 |

---

## INPUT LAYER — WHAT TO CHANGE

### 1. Enhanced Page Keywords (already done — verify)

The Tommy Boy page front matter currently has:
```
keywords = "Tom Barrett convicted felon, William Lawrence MI-7, Dykema Gossett Federal PAC Barrett, Jason Roe strategist Barrett, Save Detroit Jobs Kenneth Daniels, Barrett wrong election date Michigan Bulletin, NRCC socialist felon, Rent Is Too Damn High Barrett, Tenant Resource Center Mid Michigan, Barrett voter suppression Black voters, Clean Slate Act Michigan, Barrett Dykema dark money, MI-7 congressional race 2026, Barrett campaign FEC filings"
```

This is good but could be expanded. The keywords meta tag has diminishing SEO value (Google largely ignores it), but Bing still reads it, and it helps with concept clustering.

### 2. JSON-LD Structured Data (NEW — template change needed)

Add to `page.html` template — structured data for search engines:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{{ page.title }}",
  "description": "{{ page.description }}",
  "url": "{{ page.permalink }}",
  "datePublished": "2026-10-09",
  "dateModified": "2026-10-09",
  "publisher": {
    "@type": "Organization",
    "name": "Tuebor — Michigan Public Record",
    "url": "https://barry.primals.eco"
  },
  "author": {
    "@type": "Organization",
    "name": "Citizens of Michigan"
  },
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-sa/4.0/"
}
</script>
```

For Tommy Boy specifically, we can add **ClaimReview** structured data — Google surfaces these in search results as fact-check labels:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ClaimReview",
  "claimReviewed": "Tom Barrett called his opponent William Lawrence a 'convicted felon'",
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": 2,
    "bestRating": 5,
    "worstRating": 1,
    "alternateName": "Mostly False"
  },
  "itemReviewed": {
    "@type": "Claim",
    "author": {
      "@type": "Person",
      "name": "Tom Barrett",
      "jobTitle": "U.S. Representative, Michigan 7th District"
    },
    "datePublished": "2026-08-13",
    "appearance": {
      "@type": "OpinionNewsArticle",
      "url": "https://www.mlive.com/politics/2026/08/us-rep-tom-barrett-labels-opponent-convicted-felon-stemming-from-protest-arrest.html"
    }
  },
  "author": {
    "@type": "Organization",
    "name": "Tuebor — Michigan Public Record",
    "url": "https://barry.primals.eco"
  },
  "reviewBody": "Barrett's claim is misleading. Lawrence's 2013 felony conviction was expunged under Michigan's Clean Slate Act (MCL 780.623). Meanwhile, Barrett's campaign received $4,000 from Dykema Gossett Federal PAC, which incorporated Save Detroit Jobs — an entity whose president Kenneth Daniels is an actual convicted federal felon (DEA, May 12, 2014)."
}
</script>
```

**ClaimReview is powerful** — if Google picks it up, search results for "Tom Barrett convicted felon" could show a fact-check label linking to Tommy Boy.

### 3. OpenGraph + Twitter Cards (template enhancement)

Current template has basic OG tags. Add:

```html
<meta property="og:image" content="...">  <!-- if we create a social share image -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{ page.title }}">
<meta name="twitter:description" content="{{ page.description }}">
```

### 4. Internal Link Density

Every page on tuebor that mentions Barrett, Dykema, or dark money should link to Tommy Boy. Current cross-links:

| Page | Links TO Tommy Boy? | Action |
|------|---------------------|--------|
| Homepage `_index.md` | YES (added) | ✅ |
| `analysis/_index.md` | YES (added) | ✅ |
| `how-to-build-an-os.md` | NO | Add "See also: Tommy Boy" in Related Pages |
| `infrastructure-grid.md` | NO | Add cross-link |
| `cross-subgraph-patterns.md` | NO | Add Barrett connection node |
| detroit.primals.eco Dykema pages | NO | Add cross-site link |

**Internal links = highest-value SEO signal.** Every inbound link from an already-indexed page tells crawlers "this new page is connected and important."

### 5. Sitemap Optimization

Zola auto-generates `sitemap.xml`. After rebuild, verify Tommy Boy appears in it with current `<lastmod>` date. Fresh lastmod = priority crawl signal.

### 6. External Citation Links (outbound)

The page already links to MLive, CNN, NYT, C-SPAN, FEC.gov, LARA, DEA.gov, Ballotpedia, etc. These are AUTHORITY signals — linking OUT to high-authority sources tells search engines this page participates in the legitimate information ecosystem, not a spam/scraper ring.

---

## OBSERVATION LAYER — BINGOCUBE CRAWLER CLASSIFICATION

### Current BingoCube Axes for Legitimate Crawlers

When Googlebot visits Tommy Boy, its bingoCube profile would look like:

```
Googlebot (typical behavior):
  Attention:   MEDIUM (systematic, not bursty)
  Curiosity:   HIGH (follows internal links, diverse paths)
  Interaction: ZERO (never visits /contribute, /contact)
  → Current class: "Crawler" ✓
```

### What We Need to ADD to bingoCube

A new observation dimension for **search crawlers specifically**:

```rust
// In dashboard_writer.rs or a new module
struct CrawlerSEOProfile {
    // Which search engine?
    engine: CrawlerEngine,  // Google, Bing, DuckDuckGo, Yandex, Baidu, Other
    
    // What pages did it index?
    indexed_paths: Vec<String>,
    
    // Did it follow internal links FROM tommy-boy to other pages?
    tommy_boy_outlinks_followed: Vec<String>,
    
    // Did it render (fetch CSS/JS)?
    rendered: bool,
    
    // First seen on tommy-boy?
    first_crawl: DateTime,
    
    // Crawl frequency (re-visits)?
    revisit_count: u32,
    revisit_interval_avg: Duration,
}

enum CrawlerEngine {
    Googlebot,       // "Googlebot" in UA
    GooglebotMobile, // "Googlebot-Mobile" or "Googlebot; Mobile"
    Bingbot,         // "bingbot" in UA
    DuckDuckBot,     // "DuckDuckBot" in UA
    YandexBot,       // "YandexBot" in UA
    Baidu,           // "Baiduspider" in UA
    AppleBot,        // "Applebot" in UA
    Other(String),
}
```

### Dashboard Output

Add a new section to the bloom dashboard:

```json
{
  "crawler_seo": {
    "tommy_boy": {
      "googlebot": {
        "first_crawl": "2026-10-09T14:22:00Z",
        "last_crawl": "2026-10-09T18:45:00Z", 
        "total_visits": 3,
        "rendered": true,
        "outlinks_followed": ["/analysis/how-to-build-an-os/", "/analysis/infrastructure-grid/"]
      },
      "bingbot": {
        "first_crawl": null,
        "total_visits": 0
      }
    },
    "pages_indexed": {
      "/analysis/tommy-boy/": ["googlebot", "bingbot"],
      "/analysis/how-to-build-an-os/": ["googlebot"],
      "/analysis/infrastructure-grid/": []
    }
  }
}
```

### How This Becomes Input for Training

```
OBSERVE: Googlebot crawled tommy-boy 3x in 24 hours
  → SIGNAL: Google considers the page important enough to re-crawl
  → ACTION: maintain current content, no changes needed

OBSERVE: Bingbot hasn't visited tommy-boy after 48 hours
  → SIGNAL: Bing hasn't discovered it yet
  → ACTION: Submit URL to Bing Webmaster Tools, or create
    an inbound link from an already-Bing-indexed page

OBSERVE: Googlebot visited tommy-boy but NOT how-to-build-an-os
  → SIGNAL: Internal link from tommy-boy to OS page not followed
  → ACTION: Move the "Related Pages" section higher on tommy-boy,
    or make the links more prominent in page body

OBSERVE: Googlebot fetched CSS (rendered the page)
  → SIGNAL: Google is doing full render — structured data,
    table layouts, and visual hierarchy will be evaluated
  → ACTION: Ensure tables are clean HTML, not just markdown
```

---

## IMPLEMENTATION PLAN

### Phase 1: Template Upgrades (blueGate — now)

1. Add JSON-LD Article support to `page.html` template
2. Add Twitter Card meta tags to `base.html`  
3. Add `date` field to Tommy Boy front matter
4. Add cross-links from OS + Grid pages back to Tommy Boy

### Phase 2: Content Optimization (blueGate — now)

1. Ensure H2 headings contain target terms
2. First paragraph should contain primary target terms naturally
3. Expand the `description` field for maximum snippet coverage
4. Add `date = 2026-10-09` to front matter for datePublished

### Phase 3: Crawler Observation (sporeGate — next session)

1. Add CrawlerEngine classification to skunky-ingest
2. Track per-page crawler visits in bloom dashboard
3. Add tommy-boy-specific observation counters
4. Wire crawler SEO data into dashboard JSON output

### Phase 4: SERP Monitoring (any gate — ongoing)

Manual or automated checks:
```bash
# Check if Google has indexed tommy-boy
curl -s "https://www.google.com/search?q=site:barry.primals.eco/analysis/tommy-boy" | grep -c "tommy-boy"

# Check Barrett-related SERP position
curl -s "https://www.google.com/search?q=tom+barrett+dykema" | grep -c "barry.primals.eco"

# Check Bing indexing
curl -s "https://www.bing.com/search?q=site:barry.primals.eco/analysis/tommy-boy" | grep -c "tommy-boy"
```

### Phase 5: Training Adjustments (continuous)

Based on Phase 3 + 4 observations:
- Adjust heading keywords
- Add/remove internal links
- Update content with timely additions (new Barrett news)
- Re-submit sitemap after changes

---

## BINGOCUBE EXTENSION — CRAWLER INPUT/OUTPUT MODULE

The existing bingoCube classifies on Attention/Curiosity/Interaction to detect adversarial fleet.

The proposed extension adds a FOURTH dimension for legitimate crawlers:

```
Current:  bingoCube = (Attention, Curiosity, Interaction) → Fleet/Human/Crawler
Proposed: bingoCube = (A, C, I, Indexation) → Fleet/Human/Crawler/SearchEngine

Where Indexation =
  - UA matches known search engine? (binary)
  - Follows sitemap.xml links? (observed behavior)
  - Respects robots.txt? (observed behavior)  
  - Fetches /atom.xml? (feed discovery)
  - Revisits at regular intervals? (re-index pattern)
  - Follows structured data URLs? (JSON-LD processing)
```

This gives us two observation planes from one sensor:
1. **Defense plane** (existing): detect fleet, classify threats, generate scatter
2. **Offense plane** (new): track search engine crawler behavior, optimize SEO signals

Same bingoCube. Two outputs. The defense data funds the offense strategy.

---

## TIMELINE OPPORTUNITY

Barrett is on the ballot **November 3, 2026** — 25 days away.

Search volume for all Barrett-related terms will SPIKE in October. The Tommy Boy page needs to be indexed and ranking BEFORE the surge. Google typically indexes a new page within 2-7 days of crawl discovery if the site already has authority (tuebor does — it's been live since early October with daily content updates).

**Critical path:**
1. Rebuild sites on golgiBody (sporeGate) → Tommy Boy goes live
2. Googlebot discovers via sitemap.xml + internal links → 2-7 days to index
3. Google surfaces in SERP for target terms → ~1-2 weeks after index
4. October search surge begins → Tommy Boy is positioned

The 25-day window is tight but achievable if sporeGate rebuilds this week.

---

*This study lives in siltPond because it contains operational SEO strategy.
The page content itself is public. The optimization strategy is not.*
