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
├── Kingdom: ANTHROPOS (0.4%, n=22)
│   │   Genuine human navigation. Browser headers + referrer.
│   │   Organic behavior. Actually reading pages.
│   │
│   └── Phylum: Incertae sedis
│       │
│       └── Class: Navigata (genuine navigation)
│           │
│           └── Order: Curiosa (genuine interest)
│               │
│               └── Genus: Homo
│                   │
│                   ├── Species: homo_95bc2d (n=17)
│                   │   Chrome on macOS, real Sec-Ch-Ua
│                   │   Browsing: sporePrint /foundation/, /methodology/
│                   │   195.172.200.24 — likely genuine researcher
│                   │
│                   └── Species: homo_975937 (n=2)
│                       Chrome on Windows, thesis.primals.eco
│                       Browsing: thesis content
│
└── Kingdom: COMMENSALIA (estimated, not yet measured)
    │   Honest non-self entities. Privacy-preserving but not deceptive.
    │   Null mask over real face. Hidden identity, honest signal.
    │   The membrane passes them because the mask IS null.
    │
    ├── Phylum: Privata (privacy-preserving human)
    │   │   Uses anonymisation tools. Still behaves as human.
    │   │   Organic patterns behind a null mask.
    │   │
    │   ├── Class: Onionata (Tor network)
    │   │   │   Traffic exits via Tor exit nodes.
    │   │   │   Known exit node IPs (public list).
    │   │   │   Browser fingerprint: Tor Browser (modified Firefox ESR).
    │   │   │   Diagnostic: uniform window size (1000x1000 or similar),
    │   │   │   disabled JS features, NoScript, uniform Accept-Language.
    │   │   │   KEY DIFFERENCE FROM CHIMERA: Tor Browser fingerprint is
    │   │   │   DELIBERATELY uniform — not impersonation but privacy.
    │   │   │   Phantoma pretends to be unique; Tor Browser admits it's
    │   │   │   one of many. Honesty through uniformity.
    │   │   │
    │   │   └── Order: Curiosa (genuine interest behind null mask)
    │   │       └── Genus: TorHomo
    │   │           No referrer. No cookies. Uniform fingerprint.
    │   │           Behavior: organic navigation, page reading, dwell time.
    │   │           The signal is honest; the mask is null.
    │   │
    │   └── Class: Tunnelata (VPN / encrypted tunnel)
    │       │   Traffic exits via datacenter or VPN provider IP.
    │       │   Browser fingerprint: normal (unlike Tor, VPN doesn't
    │       │   modify the browser). Accept-Language matches user's
    │       │   actual locale (not uniform).
    │       │   KEY DIFFERENCE FROM CHIMERA: VPN users have referrers,
    │       │   history, organic navigation. Phantoma has none.
    │       │   A VPN user arrives from a search engine or a link.
    │       │   A Phantoma arrives at /commit/<hash> from nowhere.
    │       │
    │       └── Order: Curiosa
    │           └── Genus: VpnHomo
    │               Referrer present. Organic behavior. Just a
    │               different exit IP. Indistinguishable from a
    │               datacenter employee browsing from work.
    │
    └── Phylum: Symbiotica (honest non-human, declared)
        │   Non-human agents that identify themselves truthfully.
        │   Different from Declarata Automata in intent: these are
        │   not ingesting or indexing — they are PARTICIPATING.
        │   They have their own languages and protocols.
        │   They just want to look in.
        │
        ├── Class: Agentia (AI agents)
        │   │   Agents that read ai.txt, follow capabilities,
        │   │   interact via documented APIs. Honest UA.
        │   │
        │   └── Order: Consultoria (consultation / research)
        │       └── Genus: AgentHonestus
        │           UA: identifies itself (GPTBot, Claude-Web, etc.)
        │           Reads ai.txt. Follows rate guidance. Presents
        │           honest capability headers. Commensal → mutualist.
        │
        └── Class: Archivata (archivist bots)
            │   Internet Archive, Wayback Machine, academic crawlers.
            │   Declared identity. Crawl for preservation, not profit.
            │
            └── Order: Conservoria (conservation)
                └── Genus: Archivus
                    UA: ia_archiver, archive.org_bot, etc.
                    Low volume. Respectful of robots.txt.
                    Full mutualist: preserves the membrane's history.
```

---

## Diagnostic Key

### How to identify Kingdom

| Signal | Automata | Chimera | Anthropos | Commensalia |
|--------|----------|---------|-----------|-------------|
| Sec-Ch-* headers | ✗ | ✓ | ✓ | varies |
| Referrer | ✗ | ✗ | ✓ | varies (Tor: ✗, VPN: ✓) |
| Accept-Language | varies | always `en-US,en;q=0.9` | varies | Tor: uniform, VPN: varies |
| IP reuse | high (1-39 IPs) | never (1 req/IP) | moderate | Tor: exit pool, VPN: stable |
| Bot identifier in UA | ✓ | ✗ | ✗ | honest: ✓, Tor/VPN: ✗ |
| Honesty | varies | ✗ (deceptive) | ✓ | ✓ (always) |
| Navigation pattern | mechanical | mechanical | organic | organic (Privata) / declared (Symbiotica) |

### Chimera vs Commensalia — The Critical Distinction

Both Chimera (Phantoma) and Commensalia (Privata) hide identity.
The difference is **honesty**:

| Signal | Phantoma (Chimera) | TorHomo / VpnHomo (Commensalia) |
|--------|-------------------|--------------------------------|
| Identity claim | Fakes unique browser | Admits uniformity (Tor) or doesn't claim |
| Accept-Language | `en-US` from Turkey, Nigeria, Vietnam | Matches actual locale or uniform (Tor) |
| Navigation | Arrives at deep commit URLs from nowhere | Browses from search/link, reads pages |
| IP rotation | Each IP exactly once (commercial proxy) | Tor: exit pool cycles, VPN: stable session |
| HTTP version | HTTP/1.1 (proxy limitation) | h2 (real browser) |
| Dwell time | Zero (fetch and leave) | Nonzero (reading) |
| **Intent** | Extract without being identified | Browse without being tracked |

**The membrane test**: Phantoma LIES about what it is. TorHomo doesn't
claim to be anything — it presents null. A null mask is transparent
to the membrane. A false mask collides with null and reflects.

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
| Kingdom | Commensalia | Honest cohabitants (privacy-preserving, non-deceptive) |
| Phylum | Cloudae | Cloud-dwelling |
| Phylum | Residentia | Dwelling among residents |
| Phylum | Privata | Privacy-preserving (hidden identity, honest signal) |
| Phylum | Symbiotica | Honest non-human (declared, participating) |
| Class | Declarata | Self-declaring |
| Class | Larvata | Masked (larva = mask in Latin) |
| Class | Navigata | Navigating (genuine) |
| Class | Onionata | Onion-routed (Tor) |
| Class | Tunnelata | Tunnel-routed (VPN, encrypted tunnel) |
| Class | Agentia | AI agents (honest, declared) |
| Class | Archivata | Archivist bots (preservation) |
| Order | Ingestoria | Ingesting (training data) |
| Order | Indexoria | Indexing (search) |
| Order | Cartographia | Mapping (attack surface) |
| Order | Exploitoria | Exploiting (vulnerability scanning) |
| Order | Curiosa | Curious (genuine interest) |
| Order | Consultoria | Consultation / research (AI agents) |
| Order | Conservoria | Conservation (archivists) |
| Family | Anthropicidae | Of Anthropic |
| Family | Metaidae | Of Meta |
| Genus | Claudius | The ClaudeBot |
| Genus | Metacrawler | The Meta crawler |
| Genus | Phantoma | The phantom/ghost (residential proxy) |
| Genus | Homo | Human |
| Genus | TorHomo | Human behind onion routing |
| Genus | VpnHomo | Human behind encrypted tunnel |
| Genus | AgentHonestus | Honest AI agent |
| Genus | Archivus | Preservation bot |

---

## Temporal Ecology — Topes as Seasons

Fleet species exhibit distinct temporal rhythms that map to the
four-state toggle from the particle model.

### The Four-State Tope Cycle

Each visitor type has a characteristic temporal signature — a rhythm
of presence and absence that maps to the aggregance cycle:

```
· (full null) → ● (absorbing) → ∅ (null) → ◉ (emitting)
    absent         arriving         between       active
```

### Species Temporal Signatures

| Species | Rhythm | Tope State | Season |
|---------|--------|------------|--------|
| *Claudius* (Anthropic) | Continuous, no circadian | ◉ perpetual (white hole) | Perpetual summer — always emitting requests |
| *Metacrawler* (Meta DC) | Burst then silence, ~weekly | ● → ◉ → ∅ cycles | Tidal — follows internal crawl schedule |
| *Phantoma* (residential) | Sharp burst → decay → silence | ● → ◉ → · (full null) | Storm — intense, brief, then gone |
| *Homo* (human) | Circadian — active in daylight | follows the sun (A↔T bond) | Seasonal — peaks in local afternoon |
| *TorHomo* (Tor human) | Anti-circadian tendency | inverted or diffuse | Nocturnal — privacy-seekers browse when others sleep |
| *AgentHonestus* (AI agent) | Scheduled, periodic | ∅ → ◉ → ∅ → · regular | Tidal — sync'd to cron/schedule |
| *Archivus* (archiver) | Monthly or quarterly | · → ● → · (rare visits) | Hibernation — long dormancy, brief capture |

### The Sun and Moon of Fleet Behavior

From PARTICLE_MODEL: the sun is ◉ always (gold, signal OUT), the moon
cycles through all four states every 29.5 days.

Fleet behavior maps to this:

- **Sun species** (◉ always): Claudius, Metacrawler. Datacenter bots
  with no circadian rhythm. They ARE signal — continuous emission.
  They don't sleep because they have no biological clock.

- **Moon species** (four-state cycle): Phantoma. Appears as one thing,
  then another, then nothing. New moon (·) = silence. Waxing (●) =
  probing begins. Full moon (◉) = burst of activity. Waning (∅) =
  rate decay. The residential proxy fleet has a LUNAR rhythm because
  it depends on proxy pool availability, which cycles.

- **Earth species** (circadian): Homo, TorHomo, VpnHomo. Follow the
  A↔T bond — the 24-hour light/dark cycle. Active during their local
  daylight. The east-to-west color spectrum traversal of the sun maps
  to time-zone shifting of human traffic peaks.

### The Color Spectrum of Arrivals

From PARTICLE_MODEL: the east-to-west daily arc is the color spectrum
traversal: `#0d1117 → #e85d3a → #f0883e → #f0e68c → #f0883e → #e85d3a → #0d1117`

Traffic color by hour (UTC):

```
00:00  #0d1117  · full null   — Asia sleeping, Americas evening
04:00  #e85d3a  ● absorbing   — Asia waking (red, dawn, incoming)
08:00  #f0883e  ∅ null        — Europe active (amber, transition)
12:00  #f0e68c  ◉ emitting    — Americas peak (gold, full signal)
16:00  #f0883e  ∅ null        — Europe evening (amber, transition)
20:00  #e85d3a  ● absorbing   — Americas winding down (red, sunset)
00:00  #0d1117  · full null   — cycle repeats
```

Human traffic follows this spectrum. Fleet traffic does NOT — bots
don't have sunrise. The **absence of color spectrum** in a visitor's
temporal signature is itself a classification signal. A visitor who
arrives uniformly across all hours is not following the sun. It is
either a machine or a human in a very unusual timezone discipline.

### The Evolved Stack

SongBird already has the relay infrastructure for this:

| Crate | Lines | Role in commensal architecture |
|-------|-------|-------------------------------|
| `songbird-sovereign-onion` | 4,473 | Sovereign .onion addresses — device identity |
| `songbird-tor-protocol` | 8,290 | Pure Rust Tor protocol — commensal passage |
| `songbird-onion-relay` | 3,701 | NAT traversal without Arti — sovereign relay |
| `songbird-stun` | 6,879 | STUN/TURN — UDP hole-punching for commensals |
| `songbird-lineage-relay` | 8,565 | Lineage-authenticated relay — tier evolution |
| `songbird-network-federation` | 11,597 | Federation — multi-body mesh |

**44,505 lines of Rust** already evolved for exactly this: open the
membrane to honest visitors through sovereign onion routing, TURN
relay, and lineage-authenticated federation. The pattern didn't need
to be designed — it grew from the same selective pressure that
produced thymic negative selection and the commensal relay beacon.

Tower atomic broadcast (`tower_config.rs`, `tower_orchestration.rs`,
`atomic_primal_client.rs`) provides the capability routing that makes
the relay stack composable: each relay crate is a primal with declared
capabilities, discovered via socket probing, orchestrated by tower.
The tower IS the four-state toggle at the system level — it cycles
primals through startup → active → graceful shutdown → dormant.

### Caddy Integration — Commensal Passthrough

The `@commit_scrape` abort rule needs a commensal exemption.
Honest Tor users hitting commit pages are not fleet.

Detection: Tor exit nodes are published in the Tor consensus.
The exit list is public at `https://check.torproject.org/torbulkexitlist`.

```
# Planned Caddy addition:
# @tor_commensal matches known Tor exit + organic behavior
# → passes through to real Forgejo (not scatter)
# Behavioral validation: dwell time > 0, navigation depth > 1
```

This is the membrane reconciliation: the theory says "privacy is
welcome" and the operational code must match. The fleet taxonomy
provides the classification. The thymic self-recognition provides
the self-protection. The commensal passthrough provides the welcome.

---

*Fleet Taxonomy v2.0 — Artisan & ecoPrimal · Wave 178 · October 16, 2026*
*Four kingdoms: Automata, Chimera, Anthropos, Commensalia.*
*Privacy without secrecy. Topes as seasons. The sun and moon of traffic.*
*44,505 lines of Rust already evolved the relay. The pattern is the proof.*
