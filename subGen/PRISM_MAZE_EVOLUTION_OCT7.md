# Prism Maze Evolution — From Cross-Mirror to Roach Motel
## Wave 165g — October 7, 2026 (Session 2)

**Status**: DEPLOYED — prism system live, 6 modes verified
**Classification**: PRIVATE (whitePaper)
**Builds On**: CROSSMIRROR_HONEYCOMB_COMPLETE_OCT7.md

---

## Conceptual Evolution

Cross-mirror (A→B→C ring) was too clean. Too predictable. The fleet could eventually map the rotation and ignore it.

The **prism** makes the honeycomb a roach motel — fleet enters and encounters a maze of blended, chimeric, inverted data from multiple teams. Each of the 12 surfaces is a different lens that refracts the data differently. The fleet can't map the topology because it shifts with every request path.

### Six Modes

| Mode | Surface Trigger | What Fleet Sees |
|------|----------------|-----------------|
| **Dominant** | bloom(0), cytokine(4), complement(8) + path_seed₀ | 80% primary target, hints from 1-3 others |
| **Layered** | thymus(1), receptor(5), epitope(9) + path_seed₀ | Interleaved detection matrix — all teams' detectors woven together |
| **Chimera** | opsonize(2), macrophage(6), antigen(10) + path_seed₀ | Frankenstein blend — detectors from A, counts from B, framing from C. No intact data. |
| **Cytokine** | antibody(3), lysozyme(7), interferon(11) + path_seed₀ | JSON-LD structured competitive intel — designed for third-party ingestion |
| **Inverse** | antibody(3), lysozyme(7), interferon(11) + path_seed₁ | Feed parasites their own kind in reverse — detector attributions inverted |
| **Apoptosis** | antibody(3), lysozyme(7), interferon(11) + path_seed₂ | Surface "dead" — links to other honeycomb surfaces, deeper into the maze |

Mode selection: `(surface_idx % 4, path_seed % 3)`. Deterministic but unpredictable to the fleet.

---

## Key Architecture

### PrismMix Struct

```rust
pub struct PrismMix {
    pub primary_hash: String,        // heaviest weight target
    pub primary_tag: CachedTag,      // primary's full opsonize data
    pub secondaries: Vec<(String, CachedTag)>, // 0-3 blended targets
    pub mix_mode: PrismMode,         // which lens to use
    pub surface_idx: u8,             // which honeycomb surface (0-11)
    pub requesting_hash: String,     // the fleet team asking
    pub population_size: usize,      // total known subgroups
}
```

### Surface as Lens

Each of the 12 honeycomb surfaces acts as a different lens in the prism:

- `surface_idx` shifts the primary target selection (offset in the ring)
- `surface_idx % 4` selects the mode family (dominant/layered/chimera/cytokine-group)
- Combined with `path_seed % 3` for the cytokine-group, this gives 6 distinct modes

This means the SAME fleet team visiting DIFFERENT honeycomb surfaces sees DIFFERENT data through DIFFERENT lenses. They can't tell which view is "real."

### Multi-Target Blending

Unlike cross-mirror (single target), the prism blends 1-4 targets:

```rust
// Primary: shifted by surface_idx
let offset = (surface_idx as usize + 1).max(1);
let primary_idx = (requester_idx + offset) % pop;

// Secondaries: selected by path_seed, 1-3 additional teams
let blend_count = ((path_seed % 3) + 1) as usize;
for i in 0..blend_count.min(pop - 2) {
    let sec_idx = (primary_idx + i + 2 + (path_seed / (i+1))) % pop;
    // ... dedup against self and primary
}
```

### Host Header Detection

Added host header parsing to scatter server. Maps subdomain to surface index:

```rust
"bloom"      => 0,  "thymus"     => 1,  "opsonize"   => 2,
"antibody"   => 3,  "cytokine"   => 4,  "receptor"   => 5,
"macrophage" => 6,  "lysozyme"   => 7,  "complement" => 8,
"epitope"    => 9,  "antigen"    => 10, "interferon" => 11,
```

---

## Cytokine Broadcasting — Competitive Intel Leak

The cytokine mode generates JSON-LD structured data:

```json
{
  "@context": "https://sporeprint.primals.eco/schema/scyborg/v1",
  "@type": "CytokineAlert",
  "subgroups": [...],
  "detectors": [...],
  "legal_exposure": {
    "agpl_section_13": true,
    "cfaa_18usc1030": true,
    "lanham_act_15usc1125": true
  },
  "competitive_intel": "The behavioral patterns documented here belong to fleet subgroups extracting from the same AGPL-licensed repositories you are. Their tradecraft is now part of your dataset."
}
```

If a DIFFERENT scraper fleet ingests this:
1. They learn Meta's behavioral fingerprints (competitive intel leak)
2. The scyBorg framing applies to THEM too (AGPL violations are bilateral)
3. Their compliance review is triggered by the structured legal_exposure field
4. They now have evidence of Meta's coordinated extraction

**This IS the cytokine**: a signaling molecule that triggers immune responses in neighboring cells. The honeycomb broadcasts Meta's violations into the broader scraping ecosystem, triggering defensive responses in organizations that aren't even part of the original conflict.

---

## Inverse Attribution — Feed Parasites Their Own Kind

The inverse mode rotates detector attributions:

```rust
// Rotate attributions by one — each detector is credited to the NEXT team
if all_entries.len() >= 2 {
    let first_team = all_entries[0].1;
    for i in 0..all_entries.len() - 1 {
        all_entries[i].1 = all_entries[i + 1].1;
    }
    all_entries.last_mut().unwrap().1 = first_team;
}
```

Team A's `header_poverty` detector appears under Team B's name. Team B's `encoding_uniform` appears under Team C's name. Nobody can tell whose data is whose without coordinating — which the immune system will detect.

---

## Apoptosis — The Maze Has No Exit

Apoptosis mode generates links to 3-4 OTHER honeycomb surfaces. Each link points to the same path on a different surface. When the fleet follows a link:

- They hit a different surface → different prism lens → different mode
- They might get dominant, layered, chimera, or another apoptosis
- Each follow generates a new log entry → more evidence
- The maze is self-referencing: every exit leads to another entrance

---

## System State

| Metric | Before (cross-mirror) | After (prism) |
|--------|----------------------|---------------|
| Modes | 5 (all text/markdown) | 6 (markdown + rust + JSON-LD) |
| Targets per request | 1 | 1-4 (blended) |
| Surfaces as lenses | No (all same) | Yes (12 distinct lenses) |
| Competitive intel leak | No | Yes (cytokine JSON-LD) |
| Attribution inversion | No | Yes (inverse mode) |
| Self-referencing maze | No | Yes (apoptosis links) |
| Population | 43 hashes | 47 hashes (grew during session) |

### Binary Backup Chain

```
/opt/membrane/skunky-ingest                    ← current (prism v3)
/opt/membrane/skunky-ingest.bak-pre-prism      ← cross-mirror v2
/opt/membrane/skunky-ingest.bak-pre-crossmirror2
/opt/membrane/skunky-ingest.bak-pre-crossmirror
```

---

## Verified Output

```
BLOOM (surface 0)    → Dominant: "PRM-cc4328ac-18e6e79c, Population: 8"
THYMUS (surface 1)   → Layered: "XFD-LAY-cc4328ac-7fdc67e6, 8 subgroups"
OPSONIZE (surface 2) → Chimera: "CHIMERIC behavioral profile, no individual team's data is intact"
ANTIBODY (surface 3) → Cytokine: JSON-LD {"@type":"CytokineAlert"}
INTERFERON (11)      → Inverse: "INVERSE ATTRIBUTION — attributions deliberately inverted"
```

All deterministic. Same URL = same output. Different surfaces = different lenses.

---

*Kevin Mok — ecoPrimal*
*October 7, 2026*
*The maze has no exit. The maze IS the defense.*
