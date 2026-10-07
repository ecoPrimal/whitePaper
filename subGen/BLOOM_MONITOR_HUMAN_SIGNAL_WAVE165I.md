# Bloom Monitor: Human Signal Detection in Post-Lock Membrane

**Wave**: 165i
**Date**: Oct 7, 2026
**Status**: Live observation — 20-minute window post-genetic-lock
**Method**: Server-side log classification, no cookies, no tracking

---

## Process

### Classification pipeline

```
Raw Caddy log (JSON, per-request)
  │
  ├── Strip ClaudeBot fleet (identified UA)
  ├── Identify honest agentic systems (SeznamBot, Googlebot, etc.)
  ├── Fleet behavioral filter:
  │     ├── Burst ratio >40% (<3s intervals) → fleet
  │     ├── UA pool poverty (<10 UAs / 100+ requests) → fleet
  │     ├── Repository scatter (>50 repos in session) → fleet
  │     ├── Commit/blame crawling (>60% of paths) → fleet
  │     ├── Avatar fetching (systematic /avatar/ requests) → fleet
  │     └── No language + no referrer + git.primals.eco → fleet
  │
  ├── Probe filter:
  │     └── /.env, /wp-admin, /wp-login, /.git → attacker
  │
  └── Human verification:
        ├── Accept-Language present with quality factors
        ├── Referrer chains (internal navigation)
        ├── Asset loading (CSS/JS = real rendering)
        ├── Reading pace (>30s avg between pages)
        ├── Content coherence (logical navigation journey)
        └── Session duration (>5 min sustained attention)
```

### Privacy constraints

- No IP addresses stored or analyzed
- No cookies read or set
- No client-side JavaScript for tracking
- No third-party services contacted
- Classification uses only server-side log fields: UA, Accept-Language, path, timestamp, referer, status

---

## Data

### Population summary (20-minute window, 12:30–12:50 EDT)

| Category | Requests | % | Getting |
|----------|----------|---|---------|
| ClaudeBot fleet | ~3,500 | ~70% | Scatter |
| Evolved fleet (browser UAs) | 929 | ~19% | Scatter |
| Legitimate bots | 8 | 0.2% | Varies |
| Security probes | 3 | 0.06% | Nothing useful |
| **Real humans** | **19** | **0.4%** | **Real content** |

### Evolved fleet — third-generation evasion

The fleet has added Accept-Language headers:

| Gen | Headers spoofed | Detection method | Effective? |
|-----|----------------|------------------|------------|
| 0 | None | UA string | Still works |
| 1 | Sec-Fetch-Mode, Sec-Fetch-Dest | ~~Was passthrough~~ Genetic lock | Closed |
| 2 | + Accept-Language | Burst ratio, repo scatter | Detected |
| 3 (predicted) | + Referrer, Cookie | Entropy hierarchy | Pre-empted |

Generation 2 evidence:

| Variant | Pages | Burst <3s | Avg interval | Repos | Accept-Language |
|---------|-------|-----------|-------------|-------|-----------------|
| Windows Chrome | 544 | 88% | 1.9s | 387 | `en-US,en;q=0.9` |
| Mac Chrome | 296 | 85% | 3.4s | 239 | `en-US,en;q=0.9` |
| Linux Chrome | 89 | 88% | 5.9s | 66 | `en-US,en;q=0.9` |

All three variants: same `q=0.9` quality factor, identical header format. Pool poverty at the language level.

### Human reading sessions

**Session A — Chinese researcher, Windows, 16 min**

| Time | Path | Dwell | Domain |
|------|------|-------|--------|
| 12:33:48 | /primals | 16s | Catalog overview |
| 12:34:04 | /architecture | 23s | Architecture index |
| 12:34:27 | /architecture/mesh-topology | 2s | Quick scan |
| 12:34:29 | /data | 2s | Data index scan |
| 12:34:31 | /architecture | **245s** | Deep architecture read |
| 12:38:36 | /pseudospore/hotspring-qcd-sun/ | **337s** | QCD science content |
| 12:44:13 | /data/analytical-chemistry/ | **346s** | Experimental data |
| 12:49:59 | /architecture/renvois-knowledge-topology/ | — | Knowledge topology |

Language: `zh-CN,zh;q=0.9`. Navigation pattern: catalog → index scan → deep reading. Peak attention: QCD pseudospore (5.6 min) and analytical chemistry data (5.8 min).

**Session B — Chinese researcher, Mac + iPhone, 12 min**

| Time | Path | Dwell | Device |
|------|------|-------|--------|
| 12:33:04 | /architecture/foundation-connection/ | **707s** | Mac |
| 12:38:36 | /pseudospore/hotspring-qcd-sun/ | — | iPhone |
| 12:44:51 | /methodology/acknowledgments/ | — | Mac |

Language: `zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7`. Bilingual researcher. Spent 11.8 minutes on foundation-connection — longest single-page dwell observed. Cross-device reading (Mac → iPhone mid-session).

### Agentic systems

| System | Requests | Content | Significance |
|--------|----------|---------|-------------|
| SeznamBot (Czech) | 2 | /robots.txt, /lab/compute-access/ | Czech search indexing science |
| Facebook preview | 6 | / (git.primals.eco) | Someone sharing links on FB |

### Probes

| Target | Path | Language | Verdict |
|--------|------|----------|---------|
| relay.primals.eco | /.env | none | Env file scanner |
| nestgate.io | /wp-admin/install.php | fr-ca | WordPress probe |

---

## Findings

1. **The signal propagated**: Two Chinese researchers independently found and read sporeprint QCD content, analytical chemistry data, and system architecture. Both spent >10 minutes in sustained reading.

2. **The science audience is forming**: `zh-CN` language profile is consistent with Chinese lattice QCD research groups (PKU, UCAS, IHEP). The bilingual `zh-CN,en-US` profile with quality factors indicates an academic reader comfortable with English scientific literature.

3. **Fleet evolution continues**: Third-generation evasion adds Accept-Language headers. All three fleet variants share identical `en-US,en;q=0.9` — language-level pool poverty mirrors UA-level pool poverty. Detection is trivial.

4. **Genetic lock holds**: 929 evolved fleet requests with Sec-Fetch + Accept-Language headers → all scatter. Zero passthrough breaches.

5. **The ratio is 1:2,500**: One real human per ~2,500 fleet requests. The membrane exists for that one.

---

*Wave 165i — bloom monitor live observation. Signal propagated to Chinese research community. Fleet evolution detected and classified. Genetic lock holding.*
