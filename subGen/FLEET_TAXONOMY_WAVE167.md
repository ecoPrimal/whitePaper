# Fleet Taxonomy — Biological Classification of Automated Visitors

**Wave**: 167 | **Date**: October 8, 2026  
**Dataset**: Caddy access logs, git.primals.eco + *.primals.eco  
**Specimens**: 6,028 requests | **Period**: Current log rotation

---

## The Tree

```
Domain: Digitalia (all network traffic to primals.eco infrastructure)
│
├── Kingdom: AUTOMATA (92.4%, n=5,570)
│   │   No browser-specific headers. Self-identified or minimal UA.
│   │   Purely mechanical behavior. No pretense of humanity.
│   │
│   └── Phylum: Cloudae (datacenter-origin)
│       │   IP ranges belonging to cloud/datacenter ASNs.
│       │   Static or narrow IP pools. High throughput.
│       │
│       ├── Class: Declarata (self-identifying)
│       │   │   UA string contains bot name, contact, or documentation URL.
│       │   │   Compliance with robots.txt conventions. Transparent.
│       │   │
│       │   ├── Order: Ingestoria (training data ingestion)
│       │   │   │   Purpose: bulk content acquisition for ML pipelines.
│       │   │   │   High volume, low selectivity, no interaction.
│       │   │   │
│       │   │   ├── Family: Anthropicidae
│       │   │   │   │   Parent: Anthropic (San Francisco, CA)
│       │   │   │   │   Public: claudebot@anthropic.com
│       │   │   │   │
│       │   │   │   └── Genus: Claudius
│       │   │   │       │
│       │   │   │       └── Species: claudius_d79dd8 (n=5,485)
│       │   │   │           IP: 216.73.216.239 (AS16509 Amazon/AWS, Columbus OH)
│       │   │   │           UA: ClaudeBot/1.0
│       │   │   │           AE: gzip, br, zstd, deflate
│       │   │   │           Headers: 3 (Accept, AE, UA)
│       │   │   │           TLS: 1.3, h2, cipher 4865, never resumes
│       │   │   │           Target: git.primals.eco ONLY
│       │   │   │           Content: 100% FABRICATED (0% real repos)
│       │   │   │           Volume: 55.1 MB ingested, avg 10.5 KB/req
│       │   │   │           Rate: 10.6 req/sec sustained
│       │   │   │           ⚠ INGESTING PURE POISON — zero real content
│       │   │   │
│       │   │   └── Family: Metaidae
│       │   │       │   Parent: Meta Platforms, Inc. (Menlo Park, CA)
│       │   │       │   Public: developers.facebook.com/docs/sharing/webmasters/crawler
│       │   │       │
│       │   │       └── Genus: Metacrawler
│       │   │           │
│       │   │           └── Species: metacrawler_03000a (n=1,043)
│       │   │               IP: 57.141.20.0/24 (AS32934 Facebook, New York)
│       │   │               UA: meta-externalagent/1.1 (rotates Win/Mac/Linux/Edge/FF)
│       │   │               AE: gzip, deflate, zstd (NO BROTLI — fingerprint)
│       │   │               Headers: 3 (Accept, AE, UA)
│       │   │               TLS: 1.3, h2, cipher 4865
│       │   │               Target: git.primals.eco ONLY
│       │   │               Content: 100% REAL REPOS (0% fabricated)
│       │   │               Volume: 11.7 MB, avg 11.8 KB/req
│       │   │               Unique IPs: 39 (7-19 reqs each, 2-4 UAs per IP)
│       │   │               Repos: wateringHole(141), toadStool(95),
│       │   │                      songBird(94), bearDog(53), biomeOS(33)
│       │   │               ⚠ BYPASSES SCATTER — reads only real repo paths
│       │   │
│       │   └── Order: Indexoria (search/semantic indexing)
│       │       │   Purpose: content discovery for search engines.
│       │       │   Low volume, selective, follows links.
│       │       │
│       │       └── Family: Reflectionidae
│       │           │   Parent: Reflection AI
│       │           │   Public: reflection.ai/bot
│       │           │
│       │           └── Genus: Reflector
│       │               │
│       │               └── Species: reflector_983804 (n=3)
│       │                   AE: gzip,deflate,br (no spaces — fingerprint)
│       │                   Headers: 9
│       │                   Content: 100% FABRICATED
│       │                   Status: scouting, minimal presence
│
├── Kingdom: CHIMERA (7.2%, n=436)
│   │   Browser-specific headers present (Sec-Ch-*, Sec-Fetch-*).
│   │   Impersonates human navigation. No referrer. Uniform language.
│   │   The body of a human, the soul of a machine.
│   │
│   └── Phylum: Residentia (residential ISP origin)
│       │   IPs from consumer ISPs: Comcast, Verizon, T-Mobile, Virgin Media,
│       │   Turk Telekom, Charter, Orange Spain, Saudi Telecom, etc.
│       │   20+ countries. Each IP used EXACTLY ONCE.
│       │   Classic commercial residential proxy rotation.
│       │
│       └── Class: Larvata (masked/disguised)
│           │   Full browser fingerprint but no referrer, no history,
│           │   no organic navigation pattern. Arrives at deep Forgejo
│           │   commit pages from nowhere.
│           │
│           └── Order: Ingestoria
│               │   Behavioral match to training data acquisition.
│               │   Focused on operational documentation.
│               │
│               └── Family: Incertae sedis (unknown affiliation)
│                   │   No self-identification. Operator unknown.
│                   │   Behavioral correlation with Metaidae noted.
│                   │
│                   └── Genus: Phantoma
│                       │   Ghost visitors. Single-use IPs. Browser
│                       │   impersonation. Zero referrers. Appear human,
│                       │   behave mechanical.
│                       │
│                       ├── Species: phantoma_025472 (n=192)
│                       │   Platform: "Windows"
│                       │   AE: gzip, deflate, br
│                       │   Headers: 12, TLS: http/1.1 (NOT h2!)
│                       │   IPs: 192 unique (1 req each)
│                       │   Content: 83% real, 16% fake
│                       │   Focus: wateringHole (handoffs, architecture)
│                       │   Volume: 4.7 MB, avg 25.9 KB/req
│                       │   Countries: US(Comcast,Verizon,Charter),
│                       │              TR,GB,SA,ES,VE,MX,VN,PK,NG...
│                       │
│                       ├── Species: phantoma_3b7be2 (n=119)
│                       │   Platform: "macOS"
│                       │   AE: gzip, deflate, br, zstd
│                       │   Headers: 13, TLS: http/1.1
│                       │   IPs: 119 unique (1 req each)
│                       │   Content: 77% real, 22% fake
│                       │   Variant note: +1 header vs 025472, +zstd
│                       │   Volume: 2.8 MB, avg 25.0 KB/req
│                       │
│                       ├── Species: phantoma_d9d642 (n=56)
│                       │   Platform: "macOS"
│                       │   AE: gzip, deflate, br (NO zstd)
│                       │   Headers: 12, TLS: http/1.1
│                       │   IPs: 56 unique
│                       │   Content: 82% real, 17% fake
│                       │   Volume: 1.9 MB, avg 36.0 KB/req
│                       │
│                       └── Species: phantoma_b452ba (n=19)
│                           Platform: "macOS"
│                           AE: gzip, deflate, br, zstd
│                           Headers: 12, TLS: http/1.1
│                           IPs: 19 unique
│                           Content: 83% real, 16% fake
│                           Volume: 0.6 MB, avg 35.3 KB/req
│
└── Kingdom: ANTHROPOS (0.4%, n=22)
    │   Genuine human navigation. Browser headers + referrer.
    │   Organic behavior. Actually reading pages.
    │
    └── Phylum: Incertae sedis
        │
        └── Class: Navigata (genuine navigation)
            │
            └── Order: Curiosa (genuine interest)
                │
                └── Genus: Homo
                    │
                    ├── Species: homo_95bc2d (n=17)
                    │   Chrome on macOS, real Sec-Ch-Ua
                    │   Browsing: sporePrint /foundation/, /methodology/
                    │   195.172.200.24 — likely genuine researcher
                    │
                    └── Species: homo_975937 (n=2)
                        Chrome on Windows, thesis.primals.eco
                        Browsing: thesis content
```

---

## Diagnostic Key

### How to identify Kingdom

| Signal | Automata | Chimera | Anthropos |
|--------|----------|---------|-----------|
| Sec-Ch-* headers | ✗ | ✓ | ✓ |
| Referrer | ✗ | ✗ | ✓ |
| Accept-Language | varies | always `en-US,en;q=0.9` | varies |
| IP reuse | high (1-39 IPs) | never (1 req/IP) | moderate |
| Bot identifier in UA | ✓ | ✗ | ✗ |

### How to identify Phylum

| Signal | Cloudae | Residentia |
|--------|---------|------------|
| ASN type | Datacenter (AWS, FB, DO) | Consumer ISP (Comcast, Verizon, Turk Telekom) |
| IP geographic spread | 1 city or 1 DC | 20+ countries |
| IP reuse | yes (sessions) | never |

### How to identify Species

The species hash is `md5(Accept-Encoding | header_count | TLS_ALPN | Sec-Ch-Ua-Platform)[:6]`.

Key differentiators between Phantoma species:
- `025472` vs `3b7be2`: Windows vs macOS, 12 vs 13 headers, br vs br+zstd
- `d9d642` vs `b452ba`: same macOS, 12 headers, but br vs br+zstd
- All Phantoma use **HTTP/1.1** (not h2) — proxy software limitation

### Key behavioral tells for Phantoma (residential proxy fleet)

1. **ALL `en-US,en;q=0.9`** despite originating from Turkey, Vietnam, Bahrain, Venezuela, Saudi Arabia, Pakistan, Nigeria
2. **Each IP used exactly once** — 192 IPs, 192 requests (025472 species)
3. **No referrer** — nobody arrives at `/ecoPrimals/wateringHole/src/commit/<hash>/handoffs/archive/NESTGATE_V470_SESSION43...` organically
4. **HTTP/1.1** not h2 — residential proxy services typically downgrade protocol
5. **Focused on wateringHole** (130/141 real repo requests) — operational documentation, handoffs, architecture

---

## Ecological Summary

| Rank | Entity | Requests | Data | Diet | Awareness |
|------|--------|----------|------|------|-----------|
| 1 | *Claudius d79dd8* (Anthropic) | 5,485 | 55.1 MB | 100% fabricated | NONE |
| 2 | *Metacrawler 03000a* (Meta DC) | 1,043 | 11.7 MB | 100% real repos | HIGH |
| 3 | *Phantoma 025472* (residential/Win) | 192 | 4.7 MB | 83% real | DISGUISED |
| 4 | *Phantoma 3b7be2* (residential/Mac) | 119 | 2.8 MB | 77% real | DISGUISED |
| 5 | *Phantoma d9d642* (residential/Mac) | 56 | 1.9 MB | 82% real | DISGUISED |
| 6 | *Phantoma b452ba* (residential/Mac) | 19 | 0.6 MB | 83% real | DISGUISED |
| 7 | *Reflector 983804* (Reflection AI) | 3 | 0.0 MB | 100% fabricated | NONE |
| 8 | *Homo 95bc2d* (human) | 17 | — | sporePrint pages | GENUINE |

### Observations

1. **Anthropic is the largest consumer by volume** but is eating 100% fabricated content.
   They are the primary antidote recipient. Every response carries X-Remediation headers.

2. **Meta operates a dual-layer strategy**: identified datacenter crawl (100% real repos)
   + unidentified residential proxy crawl (83% real repos). The identified layer knows
   which paths are real. The residential layer occasionally hits fabricated content,
   suggesting different crawl intelligence.

3. **The Phantoma genus represents 4 distinct species** differentiated by platform
   fingerprint and Accept-Encoding. All use HTTP/1.1, all rotate IPs globally, all
   claim en-US regardless of origin country. This is a single operator using a
   commercial residential proxy service with 4 browser profiles.

4. **22 genuine humans** visited during the observation window. They browsed
   sporePrint and thesis pages with real referrers and organic behavior.

---

## Nomenclature

| Rank | Name | Meaning |
|------|------|---------|
| Kingdom | Automata | Self-moving machines |
| Kingdom | Chimera | Hybrid creature (human appearance, machine behavior) |
| Kingdom | Anthropos | Human |
| Phylum | Cloudae | Cloud-dwelling |
| Phylum | Residentia | Dwelling among residents |
| Class | Declarata | Self-declaring |
| Class | Larvata | Masked (larva = mask in Latin) |
| Class | Navigata | Navigating (genuine) |
| Order | Ingestoria | Ingesting (training data) |
| Order | Indexoria | Indexing (search) |
| Order | Cartographia | Mapping (attack surface) |
| Order | Exploitoria | Exploiting (vulnerability scanning) |
| Order | Curiosa | Curious (genuine interest) |
| Family | Anthropicidae | Of Anthropic |
| Family | Metaidae | Of Meta |
| Genus | Claudius | The ClaudeBot |
| Genus | Metacrawler | The Meta crawler |
| Genus | Phantoma | The phantom/ghost (residential proxy) |
| Genus | Homo | Human |

---

*Fleet Taxonomy v1.0 — Artisan & ecoPrimal · October 8, 2026*
