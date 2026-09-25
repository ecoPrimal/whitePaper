# Paper 28 — sporePrint Publication Checklist

**Source:** `28_PUBLIC_ANONYMIZED.md` (anonymized, publication-ready)
**Target:** primals.eco / sporePrint evidence page
**Date:** August 25, 2026

---

## Publication Format

### For sporePrint (primals.eco)

The anonymized paper is ready at `28_PUBLIC_ANONYMIZED.md`. To publish:

1. **Convert to HTML** via sporePrint markdown pipeline
2. **URL:** `sporeprint.primals.eco/basecamp/28-constrained-evolution-legal/`
3. **Metadata:**
   - Title: "Constrained Evolution in Adversarial Legal Proceedings"
   - Author: Kevin Mok
   - Date: August 2026
   - License: AGPL-3.0-or-later
   - ORCID: 0009-0004-2141-0321
   - Keywords: K-NOME, constrained evolution, pro se, legal methodology,
     provenance, cross-domain transfer

### For Blog / Long-Form Post

Extract from the anonymized paper:

**Title options:**
- "A Scientist's Approach to Pro Se Litigation"
- "K-NOME Applied to Law: What Happens When a Bench Scientist Files a Lawsuit"
- "Constrained Evolution in the Courtroom"

**Format:** 2,000-3,000 word blog post condensing Sections 1, 2, 4, 7, and 10.
Focus on the mapping tables and quantitative results. Keep the Rust struct
analogies — they're the hook for the HN/technical audience.

### For arXiv (Deferred — post case resolution)

- Category: cs.CY (Computers and Society) or cs.AI (cross-list)
- Full anonymized version with complete methodology
- Wait until case has judicial outcome for validation evidence

---

## Cross-Promotion Path

```
sporePrint post → HN discussion → blog syndication → arXiv cs.CY
                                                          ↓
                                              law review submission
                                              (after case resolves)
```

---

## Checklist

- [x] Anonymized version written (`28_PUBLIC_ANONYMIZED.md`)
- [ ] sporePrint page generated via markdown pipeline
- [ ] URL configured in Caddy (golgiBody-ext wildcard)
- [ ] Blog post excerpt drafted (2-3K words)
- [ ] Cross-linked from baseCamp README
- [ ] Linked from sporePrint index/evidence page
- [ ] Social media summary (Mastodon, LinkedIn) drafted
