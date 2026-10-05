# Gossip-Tagged Opsonization — Adaptive Immune Identity Through Behavioral Fingerprinting

**Wave**: 163h | **Date**: Oct 5, 2026
**Status**: DEPLOYED — opsonize tags flowing on golgiBody, adaptive scatter live
**Primal**: skunkBat 0.2.18 + skunky-ingest 0.2.18 + cellMembrane types
**Upstream**: THYMIC_NEGATIVE_SELECTION_FLEET_IMMUNE.md, THREAT_DETECTION_ARCHITECTURE.md

---

## The Problem with Abort

The previous defense (Wave 163g) achieved fleet suppression through information
starvation: `abort` on fleet-detected requests drops the TCP connection with
zero signal. The fleet's automation interprets connection death as "server down"
and stops wasting proxy credits. Fleet rate collapsed from 200+ req/min to
near-zero.

But abort has a structural limitation: **it is a binary signal that reveals
detection**. The fleet eventually distinguishes "server down" from "server
detects me" by comparing connection behavior across IPs. An IP that always
connects successfully (human browsing) vs an IP that always gets reset (fleet
scraping from the same source) leaks one bit of information: you are classified
differently.

The information-theoretic analysis:

| Response | Mutual Information | Fleet Learning Rate |
|----------|-------------------|-------------------|
| 403 (block) | High — confirms resource exists, reveals detection | Fast — adapt headers |
| abort (drop) | Low — ambiguous "server down" | Slow — can't tell why |
| scatter (poison) | **Negative** — fleet ingests false data | **Negative** — corrupts pipeline |

Abort minimizes mutual information to near-zero. But we can do better:
**negative mutual information**. Serve the fleet content that is plausible
but fabricated. The fleet's data pipeline ingests it, trusts it, and acts
on corrupted data. The defense doesn't just deny — it actively degrades
the adversary's dataset.

This is the biological strategy of **opsonization**.

---

## Biological Parallel: Opsonization and the Complement Cascade

In immunology, opsonization is the process of coating a pathogen with
molecules (opsonins — typically antibodies or complement proteins) that
mark it for phagocytosis. The pathogen isn't destroyed by the antibody
itself — the antibody *tags* it, and the tag is what triggers the
destructive response.

The complement cascade amplifies this: C3b binds the pathogen surface →
recruits C5b → assembles the membrane attack complex → lysis. Each stage
requires the previous stage's tag. More tags = higher confidence = more
aggressive response.

Our opsonization system follows the same architecture:

```
Request arrives
    │
    ▼
┌────────────────┐
│  stale_chrome   │──── antibody binding (innate)
│  content_gate   │──── antibody binding (innate, broad-spectrum)
│  fleet.match    │──── antibody binding (adaptive)
└───────┬────────┘
        │ detectors accumulate
        ▼
┌────────────────────────┐
│  behavioral_hash()     │  Compute conserved epitope
│  extract_invariants()  │  Structured behavioral profile
│  OpsonizeTag           │  Gossip-propagable tag
└───────┬────────────────┘
        │ tag emitted
        ▼
┌────────────────────────┐
│  scatter server        │  Delivers poison based on tag confidence
│  (127.0.0.1:9753)      │  More tags = higher ratio = richer content
└────────────────────────┘
```

Each detector that fires is an antibody binding to the pathogen. The more
antibodies bound, the higher the confidence, the richer the poison delivered.
This is the complement cascade: stale_chrome binds → content_gate binds →
fleet_aggregator binds → scatter server delivers the membrane attack complex.

---

## The Behavioral Hash — Conserved Epitope

The residential proxy fleet's strategy (antigenic drift) renders IP-based
identification useless: ~1,000 unique IPs per 5 minutes, 0% reuse. Each
IP makes exactly 1 request and is never seen again. The fleet sheds its
surface proteins on every request.

But the fleet's *behavior* cannot change without changing its purpose.
The fleet scrapes commit-level URLs from `git.primals.eco`. This requires:
- Requesting deep-content paths (commit, src, raw, blame, etc.)
- No Forgejo session cookies (the bot has no login)
- A narrow User-Agent pool (shared residential proxy profiles)
- Metronomic request timing (automated scheduling)
- IP rotation (each proxy used once)

These behavioral dimensions are the **conserved epitope** — the molecular
structure the pathogen cannot mutate without losing function. A virus
that mutates its hemagglutinin stalk stops binding cells. A scraper that
stops requesting commits stops being a scraper.

### Quantization: From Continuous to Hashable

Raw behavioral metrics are continuous (e.g., commit_url_pct = 0.73). Minor
variations across observation windows would produce different hashes, defeating
stability. We quantize each dimension into discrete bands:

```
commit_url_pct:   <10%  <30%  <60%  <80%  ≥80%   (5 bands)
single_page_pct:  <10%  <30%  <60%  <80%  ≥80%   (5 bands)
referrer_pct:     <10%  <30%  <60%  <80%  ≥80%   (5 bands)
ua_count:         0-5   6-20  21+                 (3 bands)
top_ua_pct:       <10%  <30%  <60%  <80%  ≥80%   (5 bands)
interval_cv:      <0.3  <1.0  ≥1.0               (3 bands: metronomic/moderate/organic)
```

Plus 4 boolean deception flags: hides_identity, rotates_ips, ignores_rejection,
encoding_uniform. These are all hashed together via `DefaultHasher` → 16 hex
chars.

**Key property**: The hash depends on behavioral *bands*, not exact values.
The fleet's commit_url_pct varying between 0.71 and 0.76 across windows
produces the same band (≥60%), and therefore the same hash. But a human's
commit_url_pct of 0.05 produces a different band (<10%) and a different hash.

**Tested invariants**:
- Minor variations in request count, IP count, timing → hash unchanged ✅
- Major behavioral shift (commit-heavy → diverse browsing) → hash changes ✅
- Wildly different IP count (997 vs 5000) → hash unchanged ✅

The hash is truly IP-independent. **No IP address enters the hash computation.**

### Live Hash Clusters (Oct 5, 2026)

From golgiBody production logs:

| Hash | Frequency | Likely Interpretation |
|------|-----------|----------------------|
| `49e77ea75aa7666e` | Dominant (60%+ of windows) | Primary fleet behavioral mode |
| `087ef04a48f7b1ca` | Secondary (~25%) | Slightly shifted timing/path mix |
| `44a5368cb70323e1` | Occasional (~15%) | Third behavioral cluster |

Three distinct behavioral fingerprints from a fleet using ~1,000 unique IPs
per window. The IPs are disposable; the behavior is conserved.

---

## The OpsonizeTag — Gossip-Propagable Identity

```rust
pub struct OpsonizeTag {
    pub behavioral_hash: String,      // 16 hex chars — the conserved epitope
    pub detectors: Vec<String>,       // Which antibodies bound
    pub confidence: f64,              // 0.0-1.0 — how many flags triggered
    pub origin_gate: String,          // Which gate emitted this tag
    pub invariants: BehavioralInvariants,  // Structured profile for downstream
    pub response: OpsonizeResponse,   // What to do with tagged traffic
    pub created_epoch: u64,           // First observation
    pub last_confirmed_epoch: u64,    // Most recent match
    pub match_count: u64,             // Accumulated observations
}
```

The tag carries everything a downstream gate needs to recognize and respond
to the fleet pattern without having observed it directly. When propagated
via swarmVine's `defense` gossip topic as a `defense.opsonize:{hash}` entry,
every gate in the mesh can participate in the defense even if the fleet
hasn't reached them yet.

### Confidence Computation

Confidence is the fraction of deception flags that trigger:

| Flag | Weight | Triggered by Fleet? |
|------|--------|-------------------|
| `hides_identity` | 0.25 | ✅ Usually (stealth UA) |
| `rotates_ips` | 0.25 | ✅ Always (residential proxies) |
| `ignores_rejection` | 0.25 | Sometimes (depends on posture) |
| `encoding_uniform` | 0.25 | Sometimes |

Current fleet confidence: **25%** (1 of 4 flags). This is appropriate for
the current engagement — the fleet is relatively unsophisticated. A more
aggressive fleet that ignores rejections AND uses uniform encoding would
reach 75% confidence and trigger a higher scatter ratio.

### Gossip Validation

Before swarmVine accepts a `defense.opsonize:` entry, `gossip_analysis.rs`
validates:

1. `behavioral_hash` is exactly 16 hex characters
2. `detectors` is non-empty (at least one antibody bound)
3. `confidence` is in [0.0, 1.0]
4. `origin_gate` is non-empty

This prevents malformed or poisoned opsonize tags from propagating. The
validation is lightweight — it checks structural integrity, not semantic
correctness. Semantic validation (is this behavioral hash actually correct?)
is left to each gate's local observations.

---

## Adaptive Scatter — Confidence-Scaled Poison

The scatter server doesn't use a fixed poison ratio. It reads a
`SharedConfidence` atomic value that the opsonize pipeline updates on
every fleet match:

```
SharedConfidence (AtomicU32, fixed-point × 1000)
    │
    │ read on every connection
    ▼
effective_ratio = base_ratio + confidence × (max_ratio - base_ratio)
```

| Confidence | Base Ratio | Effective Ratio | Meaning |
|------------|-----------|-----------------|---------|
| 0% | 30% | 30% | No tags — use base ratio |
| 25% (current) | 30% | **42%** | 1 deception flag — moderate |
| 50% | 30% | 55% | 2 flags — escalating |
| 75% | 30% | 67% | 3 flags — aggressive |
| 100% | 30% | **80%** | All flags — maximum poison |

The maximum is capped at 80% — always keep some 404s for plausible
deniability. If 100% of responses returned 200 with rich content, the
fleet could diff against a known baseline and detect the fabrication.
The 20% 404 floor creates uncertainty: "maybe those paths just don't
exist."

### Current Live State (Oct 5, 2026)

```
🏷️ opsonize tag emitted — behavioral hash 49e77ea75aa7666e
   hash=49e77ea75aa7666e detectors=2 confidence=25% effective_ratio=42%
```

42% of fleet requests get plausible poison content (fake commit pages,
fabricated file views, synthetic issues). 58% get realistic Gitea 404
pages. Both are zero-signal — the fleet cannot distinguish poison from
real without an external oracle.

---

## Progressive Identity Accumulation

The gossip-tagged model enables a key capability that per-gate detection
cannot: **progressive identification through independent observation**.

### Single-Gate Observation

A single gate sees one window of fleet behavior. It can compute the
behavioral hash and emit a tag with its local detectors and confidence.
But one gate's observation is limited: maybe the behavior it saw was
coincidental, maybe the fleet was just warming up.

### Multi-Gate Accumulation (via swarmVine)

When multiple gates observe the same behavioral hash and emit independent
tags, the mesh accumulates evidence:

```
golgiBody observes hash 49e77ea75aa7666e → emits tag (detectors: [content_gate, ip_rotation], confidence: 25%)
sporeGate observes hash 49e77ea75aa7666e → emits tag (detectors: [stale_chrome, narrow_ua], confidence: 50%)
blueGate  observes hash 49e77ea75aa7666e → emits tag (detectors: [encoding_uniform], confidence: 25%)
```

Each gate saw different aspects of the fleet. Together they build a composite
identity: this behavioral pattern is recognized by 5 independent detectors
across 3 independent gates. The confidence cascades.

This is **clonal expansion** in immunology: a successful antibody (behavioral
hash) is amplified across the immune system (gate mesh). The more cells that
produce the antibody, the faster the response when the antigen is encountered.

### The Intruder's Dilemma

From the fleet's perspective, the defense is invisible. Each individual gate
looks like it's making independent decisions. But behind the mesh, the
behavioral hash propagates, detectors accumulate, confidence scales, and
the scatter ratio climbs. The fleet doesn't see this happening. All it sees
is that some requests return content and some return 404.

By the time the fleet realizes the content is poisoned (if it ever does),
its data pipeline has ingested weeks of fabricated commit pages, fake file
contents, and synthetic issues. The cost of cleaning the dataset exceeds
the cost of scraping from scratch — and scraping from scratch will encounter
the same defense.

---

## Implementation Reference

### Files Modified/Created

| File | Change |
|------|--------|
| `cellmembrane-types/src/fleet.rs` | `OpsonizeTag`, `BehavioralInvariants`, `OpsonizeResponse`, `behavioral_hash()`, `extract_invariants()`, quantization functions |
| `skunk-bat-core/src/gossip_analysis.rs` | `check_defense_opsonize()` validation, `defense.opsonize:` routing |
| `skunky-ingest/src/main.rs` | Opsonize emission on fleet match, SharedConfidence wiring |
| `skunky-ingest/src/scatter_server.rs` | `SharedConfidence` type, `effective_ratio()`, adaptive poison ratio |
| `skunky-ingest/src/rpc.rs` | `call_raw()` for gossip injection |

### Commits

- cellMembrane `34941aa` — 🏷️ OpsonizeTag types + behavioral hash — gossip-tagged fleet identity
- skunkBat `5683c75` — 🏷️ gossip-tagged opsonization pipeline — adaptive scatter + behavioral identity

### Tests (11 new)

| Test | What It Verifies |
|------|-----------------|
| `behavioral_hash_stable_across_minor_variation` | Minor metric changes don't alter hash |
| `behavioral_hash_changes_on_major_shift` | Major behavioral change produces different hash |
| `behavioral_hash_ignores_ip_count` | Hash is truly IP-independent |
| `extract_invariants_fleet_pattern` | Structured invariants correctly extracted |
| `opsonize_tag_serde_roundtrip` | Tags survive JSON serialization/deserialization |
| `defense_opsonize_entry_valid` | Gossip validation accepts well-formed tags |
| `defense_opsonize_invalid_hash_warns` | Short/malformed hash rejected |
| `defense_opsonize_no_detectors_warns` | Empty detector list rejected |
| `shared_confidence_effective_ratio` | Ratio scales correctly with confidence |
| `shared_confidence_clamps` | Out-of-range values clamped to [0.0, 1.0] |

---

## Biological Architecture Summary

The immune system has evolved through four stages, each forced by a specific
failure of the previous:

| Stage | Biological Analog | Failure That Forced It | Wave |
|-------|------------------|----------------------|------|
| Static matchers | Innate immunity (TLRs) | Fleet adapts past static signatures | 163a-b |
| Tit-for-tat escalation | Adaptive immunity (T-cells) | Produces autoimmune errors | 163c-d |
| Negative selection | Thymic deletion | Self-IP attacked by own antibodies | 163e-f |
| **Opsonization + scatter** | **Complement cascade** | **Abort leaks detection signal** | **163g-h** |
| **Gossip-tagged identity** | **Clonal expansion** | **Single gate has limited view** | **163h** |

Each stage recapitulates a biological immune evolution that took hundreds
of millions of years, compressed into a single engineering engagement.
The convergence is not designed — it is forced by the constraint landscape
of adversarial interaction. The same problems produce the same solutions.

---

## Intellectual Payoff

### For the Dissertation

1. **Negative mutual information as defense**: Scatter moves beyond
   information starvation (abort) to information corruption (poison).
   This is a novel contribution to adversarial defense theory — the
   response actively degrades the adversary's dataset rather than
   merely denying access.

2. **Behavioral hash as conserved epitope**: Demonstrating that a
   stable fingerprint can be computed from behavioral invariants
   (not identity) proves that antigenic drift (IP rotation) does not
   defeat adaptive immunity when the detection targets conserved
   behavior. This maps directly to the viral immunology literature.

3. **Gossip-propagated identity accumulation**: Independent observers
   building composite identity through epidemic gossip is a concrete
   implementation of distributed consensus for threat detection —
   no central authority, no shared state, just convergent observation
   propagated through a mesh.

### For the Platform

The opsonization pipeline is composable:

| Component | Swap Path |
|-----------|-----------|
| Behavioral hash | Any fleet fingerprinting that produces stable hashes |
| OpsonizeTag | Any gossip-compatible tag format |
| Scatter server | Any content generation backend |
| SharedConfidence | Any atomic signal between detection and response |
| SwarmVine gossip | Any epidemic propagation protocol |

The pattern survives component replacement. The *roles* (detect, tag,
propagate, respond) are stable even when implementations change.

---

## References

- subGen: `THYMIC_NEGATIVE_SELECTION_FLEET_IMMUNE.md` (autoimmune incident + negative selection)
- subGen: `THREAT_DETECTION_ARCHITECTURE.md` (8-category detection model)
- subGen: `GOSSIP_CONVERGENCE_THRESHOLD.md` (swarmVine convergence properties)
- sporePrint: baseCamp 30 — Adversarial Receptor Evolution (stealth fleet fingerprinting)
- sporePrint: baseCamp 31 — The Lysogeny Protocol (license-as-phage)
- External: Axelrod, R. (1984). *The Evolution of Cooperation*
- External: Janeway, C.A. (2001). "How the immune system works to protect the host from infection" — complement cascade
- External: Shannon, C.E. (1948). "A Mathematical Theory of Communication" — negative mutual information

*subGen Wave 163h — Gossip-tagged opsonization deployed. Behavioral hash
49e77ea75aa7666e tracks fleet across ~1,000 rotating IPs. Adaptive scatter:
42% poison at 25% confidence, scaling to 80% at full confidence. 11 new tests.
Three hash clusters identified. Complement cascade architecture:
detect → tag → propagate → poison. Zero IPs stored. The fleet's data
pipeline is now a liability.*
