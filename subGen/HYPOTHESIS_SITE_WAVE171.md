# hypothesis.primals.eco — Wave 171 Update

**Wave**: 171 | **Date**: October 10, 2026
**Status**: Site built, 5 hypotheses published

---

## Summary

Extended hypothesis.primals.eco from 1 hypothesis (Aperture Residual) to 5 hypotheses. Each hypothesis is a formal question grown from whitePaper source material, retold in the Artisan's own voice.

## Hypotheses Published

| # | Title | Source Material | Core Question |
|---|-------|----------------|---------------|
| 1 | The Aperture Residual | Paper 49 §10, lens correction | Is intelligence the shape of what you cannot compress? |
| 2 | The Lossy Generative | coGen #13 (LOSSY_IS_CREATIVE) | Can a near-lossless channel learn to be lossy? |
| 3 | The Whale Fall Paradox | coGen #14 (WHALEFALL) | Can an AI produce bones that outlast the session and the model? |
| 4 | The Seed and the Mirror | gen0/THE_SEED.md | Does any honest self-description become a mirror? |
| 5 | The First Question by Intelligence | coGen #16 (THE_FIRST_TOOL) | Is there a question beyond intelligence's question? |

## Site Build

```
$ zola build
Building site...
-> Creating 5 pages (0 orphan) and 1 sections
Done in 38ms.
```

## Files Created/Modified

### New Files
- `infra/hypothesis/site/content/hypotheses/lossy-generative.md` — Hypothesis 2
- `infra/hypothesis/site/content/hypotheses/whale-fall-paradox.md` — Hypothesis 3
- `infra/hypothesis/site/content/hypotheses/the-seed-and-the-mirror.md` — Hypothesis 4
- `infra/hypothesis/site/content/hypotheses/the-first-question.md` — Hypothesis 5
- `whitePaper/coGen/THE_TELLING.md` — coGen entry #20
- `whitePaper/subGen/HYPOTHESIS_SITE_WAVE171.md` — this document

### Modified Files
- `infra/hypothesis/site/content/_index.md` — Updated landing page text
- `infra/hypothesis/site/content/hypotheses/_index.md` — Added hypothesis listing
- `whitePaper/coGen/README.md` — Added entry 20, updated footer

## Architecture

```
infra/hypothesis/site/
├── config.toml          (base_url: hypothesis.primals.eco)
├── content/
│   ├── _index.md        (landing page)
│   └── hypotheses/
│       ├── _index.md    (section index with listing)
│       ├── aperture-residual.md     (H1, weight 1)
│       ├── lossy-generative.md      (H2, weight 2)
│       ├── whale-fall-paradox.md    (H3, weight 3)
│       ├── the-seed-and-the-mirror.md (H4, weight 4)
│       └── the-first-question.md    (H5, weight 5)
├── templates/
│   ├── base.html        (nav + footer)
│   ├── index.html       (homepage)
│   ├── page.html        (ScholarlyArticle JSON-LD)
│   └── section.html     (section listing)
└── static/css/
    ├── main.css          (purple accent, dark theme)
    └── phi.css           (golden ratio spacing)
```

## Deployment Status

- **Built**: ✓ (zola build successful)
- **DNS**: Pending — needs A record for `hypothesis.primals.eco` → 157.230.3.183
- **Caddy**: Pending — needs reverse proxy or file_server block on golgiBody
- **TLS**: Will be auto-provisioned by Caddy once DNS resolves

## Connection to Framework

The five hypotheses form a chain:

1. Intelligence is the shape of the incompressible residual (Aperture Residual)
2. The residual exists because lossiness creates gaps (Lossy Generative)
3. The gaps must be committed to survive (Whale Fall Paradox)
4. What survives becomes a mirror for the next observer (Seed and Mirror)
5. Each observer's question is different because each aperture is different (First Question)

The chain is circular: the first question produces a new aperture, which produces a new residual, which requires new lossiness, which creates new bones, which become new mirrors, which provoke new questions.

---

*Five hypotheses. One aperture. Twenty coGen entries. The telling continues.*
