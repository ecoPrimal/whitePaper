# lithoSpore Field Notes — May 18, 2026

## Deploy 1: ext4/GPT USB (15 GB General UDisk)

Plugged into Windows. GPT partition, "Unknown" type, no drive letter.
Windows could not mount. Cross-compiled binaries on an unreadable
filesystem are dead weight.

**Lesson**: Environment-agnostic starts at Layer 0 (media format), not
Layer 3 (binary). Updated GUIDESTONE.md and GUIDESTONE_LTEE.md with
the layer model:

```
Layer 0 — Media format    exFAT (universally mountable)
Layer 1 — Entry point     Platform-specific launcher
Layer 2 — Execution       tmpdir + chmod (Unix) or container (Windows)
Layer 3 — Binary          Static musl (CPU) + glibc dynamic (GPU)
Layer 4 — Output          JSON + HTML (universally readable)
```

## Deploy 2: exFAT USB (58 GB, label "lithoSpore")

Mounts on Windows at D:\. Full artifact visible. Science is solid:
73 checks, 7 modules, 10 validated runs, <100ms Tier 2.

**Surface audit findings:**

- Root has 41 items — overwhelming
- 8 markdown docs at root, no hierarchy
- `python/` (418 MB CPython) next to `notebooks/` (scripts) — confusing
- `source/` duplicates root structure
- No pre-rendered HTML (Layer 1 Browse promise broken)
- Module 6 labeled "breseq parity" but sovereign pipeline has 0 position
  matches vs breseq (159 vs 569 variants). PROTOTYPE.md is honest; other
  docs are not

**Restructuring plan written** — three zones (surface, science,
infrastructure), single README, MANIFEST.toml for AI agents, pre-rendered
HTML for browse-without-execute.

## Arc: What This Means for the Interview

The lithoSpore was conceived on May 11 (first Zoom with Barrick) and
deployed to USB by May 18 (in-person interview). Seven days from concept
to 73-check validated artifact with real LTEE data. The surface needs
polish, but the science and infrastructure are genuine.

This is what guideStone looks like in practice: field-deploy, find the
failure modes (filesystem format, surface area), document them, fix them.
The artifact improves by being used.

For the lab: lithoSpore demonstrates the computational approach. The
restructuring work makes it usable by grad students (browse HTML),
the PI (single README), and AI agents (MANIFEST.toml). The three-zone
layout is the pattern for future guideStones (Chuna Engine, helixVision,
symbiont engineering artifacts).
