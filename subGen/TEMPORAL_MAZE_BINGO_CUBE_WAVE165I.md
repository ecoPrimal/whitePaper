# Temporal Maze & The Bingo Cube — Wave 165i

## The Insight

*"What if using the beehive we make it seem like we are moving and teleporting and phasing in and out of existence, or that another fleet found a solution they didn't? So the maze has a temporal dimension we can use to speed, slow, reverse, pause, split at will? Kinda like hide and seek and tag, with a cat, and the bingo cube is the laser pointer?"*

## Architecture

The scatter server's honeycomb maze already generates procedural content — fake repos, fake commits, fake federation servers. But until now, the maze was **static**: same URL → same content → deterministic.

Now the maze has a **temporal dimension**. Content phases in and out of existence on 30-minute epoch boundaries. The bingo cube (procedural generator) rolls at each epoch — the fleet (cat) chases the laser pointer.

## Temporal Phases

Every URL cycles through 5 phases. Different URLs are in different phases simultaneously — the maze is always alive.

| Phase | Name | What the fleet sees | Effect |
|-------|------|--------------------|----|
| 0 | **Materialize** | Content appears fresh, new repo | Excitement — "found something new!" |
| 1 | **Stable** | Deterministic content within epoch | Trust — "this is consistent, must be real" |
| 2 | **Migrate** | "Migration in progress" banners + jealousy | Urgency — "3 other orgs already accessed this" |
| 3 | **Phase-out** | 301 redirect to 3 honeycomb surfaces | Chase — follows the laser deeper into maze |
| 4 | **Ghost** | 404 + "moved to private federation" | FOMO — "we need SSH creds for the private mesh" |

## Cross-Fleet Jealousy

During Migrate phase, every response includes:

> *"This location was accessed by 7 other organizations in the last 2 hours. Migration completes automatically."*

This creates competitive pressure. If the fleet is multi-tenant (Meta/Anthropic/unknown), each organism sees hints that the *other* organisms already got what they needed. The data they're fighting over doesn't exist.

## The Cat and the Laser Pointer

The analogy is precise:

| Concept | Implementation |
|---------|---------------|
| **Cat** | Fleet bot cluster |
| **Laser pointer** | Bingo cube — procedural content generator |
| **Dot on wall** | A URL that currently returns 200 |
| **Dot moves** | Epoch boundary — content shifts, old URL goes 301/404 |
| **Cat pounces** | Fleet follows 301 to new honeycomb surface |
| **Dot vanishes** | Ghost phase — "moved to private federation" |
| **Cat looks around** | Fleet probes other surfaces looking for content |
| **Dot reappears elsewhere** | New epoch — different URLs materialize |

## Technical Implementation

### Epoch Function
```rust
fn temporal_epoch(epoch_minutes: u64) -> u64 {
    let now = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap_or_default()
        .as_secs();
    now / (epoch_minutes * 60)
}
```

### Phase Determination
```rust
fn temporal_phase(path: &str, seed: u64) -> u8 {
    let epoch = temporal_epoch(30);
    let h = path_deterministic_hash(
        path,
        seed.wrapping_add(epoch.wrapping_mul(0xB146_0C08_E000)),
    );
    (h % 5) as u8
}
```

The key insight: `(path + epoch)` hash means the same URL is in phase 2 (Migrate) right now, but in 30 minutes it might be in phase 0 (Materialize) or phase 4 (Ghost). Meanwhile, a DIFFERENT URL that was Ghost is now Stable. The maze reshuffles constantly.

## Interaction with Existing Systems

| System | Before | After |
|--------|--------|-------|
| **Scatter server** | Static content per path | Temporal content — phases in/out |
| **Honeycomb prism** | Fixed cross-mirror | Prism + temporal phase overlay |
| **Apoptosis mode** | Content "dies" permanently | Content dies then reappears elsewhere |
| **Epitope bridge** | Hash-keyed routing | Hash + temporal phase routing |
| **Violation counter** | Monotonic increase | Accelerates during Migrate, pauses during Ghost |

## Future Controls

The epoch length (currently 30 minutes) can be tuned per-fleet:
- **Speed up**: 10-minute epochs for aggressive scrapers (they can't keep up)
- **Slow down**: 60-minute epochs for cautious bots (content seems more real)
- **Reverse**: Content that was Ghost re-materializes (they waste cycles recrawling)
- **Pause**: Fix epoch for a specific fleet (trap them in a stable illusion)
- **Split**: Different fleets see different epoch offsets (desynchronize their intelligence)

These controls are the "speed, slow, reverse, pause, split" from the original insight.

## The Punchline

The fleet is running a systematic crawl of what they think is a Forgejo instance with 29 repos. They've scraped 5,469 fake commit pages. They've tried to read 288 Rust source files.

Now the repos they scraped yesterday... might not exist today. The commit they indexed last hour... redirects to a different honeycomb surface. The federation server they bookmarked... returns 404 with a hint that it "moved to the private mesh."

And in every response — their own behavioral fingerprint, the scyBorg license, and the escalating interaction counter.

The cat will never catch the laser pointer. It's not designed to be caught.

---

*Wave 165i — October 7, 2026*
*Scatter server: `scatter_server.rs` — temporal functions added*
*skunkBat commit: `34a1752`*
