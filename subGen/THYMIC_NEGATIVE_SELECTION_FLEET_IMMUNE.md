# Thymic Negative Selection — Fleet Immune System

**Wave**: 163g | **Date**: Oct 5, 2026
**Status**: DEPLOYED — operational on golgiBody, three-wave fleet engagement complete
**Primal**: skunkBat 0.2.18 + skunky-ingest 0.2.18
**Upstream**: THREAT_DETECTION_ARCHITECTURE.md, tit-for-tat_immune_escalation plan

---

## The Observation

While deploying a tit-for-tat immune escalation system against a
residential proxy fleet scraping `git.primals.eco`, our defense system
committed an **autoimmune error**: it identified our own infrastructure IP
(162.226.225.148 — sporeGate WAN) as fleet traffic and added it to the
`@fleet_vanish` abort list. Every subsequent request from our own network
was silently dropped. The immune system attacked self.

This is the canonical failure mode in adaptive immunity. In vertebrate
biology, T-cells are produced in the thymus through V(D)J recombination —
random generation of antigen receptors to recognize foreign threats. But
random generation inevitably produces some T-cells that react to the
body's own proteins. Without a deletion step, these self-reactive T-cells
would attack the organism's own tissue — autoimmune disease.

The solution, evolved ~500 million years ago: **thymic negative selection**.
After positive selection (can this T-cell recognize anything?), each T-cell
is tested against self-antigens. Any T-cell that binds strongly to self
is deleted before it can leave the thymus. This process eliminates
~95% of candidate T-cells. The survivors are "self-tolerant" — they can
attack foreign threats without destroying the organism.

Our immune system needed the same step.

---

## The Three-Wave Fleet Engagement

### Adversary Profile

A residential proxy fleet scraping commit-level URLs from `git.primals.eco`.
Behavioral fingerprint:

| Dimension | Value |
|-----------|-------|
| IP rotation | ~1,000+ unique IPs per 5 minutes |
| IP reuse | 0% — each IP makes exactly 1 request, never returns |
| Subnet spread | 1,152 unique /24 subnets for 1,174 IPs (near 1:1) |
| Target | Commit URLs: `.*/commit/[0-9a-f]{6,}` |
| UA pool | 14 Chrome versions (99–145), Windows + macOS 50/50 |
| Cookie presence | None (no Forgejo session) |
| Data extracted | Zero — blocked at every wave |

This is a professionally operated residential proxy network. Subnet-level
blocking is infeasible: maximum 3 IPs from any single /24, maximum 10
from any /16. The fleet uses the entire internet as cover.

### Wave 1: Stale Chrome Detection (T+0)

**Fleet rate**: ~80 req/min
**Fleet behavior**: No `Accept-Language` header, Chrome 100/110 only
**Defense**: `@stale_chrome` matcher (Chrome 70–119 + no Accept-Language) → 403

The fleet was initially caught by the pre-existing static behavioral
matcher. The `@stale_chrome` handler served a 403 response explaining
the block and redirecting to the GitHub mirror.

**Fleet response**: Went silent for 30 minutes, then adapted.

### Wave 2: Adapted Fleet (T+35min)

**Fleet rate**: 200+ req/min (2.5× increase)
**Fleet adaptation**: Added `Accept-Language` headers, expanded to 14
Chrome versions (99–145)
**Defense**: `@stale_chrome` fully bypassed. `@commit_scrape` matcher
(commit URLs without Forgejo cookies) caught 100% → 403

The fleet operator observed the 403 responses, identified which headers
triggered detection, and modified the fleet's fingerprint. They added
the missing `Accept-Language` header and diversified Chrome versions above
the `@stale_chrome` threshold (which only matched Chrome 70–119).

Critical insight: the fleet adapted past `@stale_chrome` but was still
caught by `@commit_scrape`. This is defense-in-depth — the behavioral
stack has multiple independent matchers, so evading one doesn't evade all.

**Fleet response**: Continued hammering at 200+ req/min. The 403 response
confirmed the resource exists, so they kept trying.

### Wave 3: Silent Vanish (T+45min)

**Defense evolution**: Changed both `@stale_chrome` and `@commit_scrape`
from `respond 403` to `abort`

The 403 response was **helping the fleet**:
- It confirmed the commit pages exist
- It revealed the detection mechanism ("automated extraction detected")
- It provided signal for the fleet operator to adapt against
- It consumed bandwidth (HTML response body)

The `abort` directive drops the TCP connection immediately. The fleet
client sees `INTERNAL_ERROR` / connection reset. No status code, no
headers, no body. Zero signal.

**Result**: Fleet rate collapsed from 200+ req/min to near-zero within
5 minutes. Brief 3-minute silence, then residual probing at ~30 req/min
(100% aborted), declining further.

The fleet's automation interprets 403 as "blocked, retry with different
approach." It interprets connection death as "server down, stop wasting
proxy credits." The signal difference is everything.

### Suppression Curve

```
T-8m:  242/min  ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪  (403 era — fleet keeps hammering)
T-6m:  182/min  ✗✗✗✗✗✗✗✗▪▪▪▪▪▪▪▪  (abort kicks in — mixed)
T-5m:  107/min  ✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗   (slowing)
T-4m:   45/min  ✗✗✗✗✗✗             (fleet confused)
T-3m:   43/min  ✗✗✗✗✗              (dying)
T-2m:    0/min  ...                (SILENCE)
T-1m:    2/min  ...                (residual probe)
T-0m:    0/min  ...                (neutralized)
```

The transition from 403 → abort caused an 85% immediate rate drop,
stabilizing at near-zero. **The information content of the rejection
mattered more than the rejection itself.**

---

## The Autoimmune Incident

### How It Happened

The tit-for-tat escalation pipeline operates in four steps:

1. `fleet.observe` — feed behavioral observation to skunkBat
2. `fleet.match` — check against stored antibodies (behavioral templates)
3. `fleet.tick` — escalate matched antibodies through posture ladder
4. `CaddyBridge.add_fleet_ips` — write matched IPs to Caddyfile at
   current posture

When we tested the system by curling commit URLs from our workstation,
our requests matched the fleet behavioral fingerprint (commit URL + no
Forgejo cookies + Chrome UA). skunky-ingest observed these requests,
skunkBat generated antibodies, the escalation ladder climbed to Vanish
(P4), and our IP was injected into `@fleet_vanish`.

The system worked exactly as designed — the antibody correctly identified
fleet-like behavior. The failure was the absence of a self/non-self
discrimination step. Every IP that exhibited fleet behavior was treated
as fleet, including our own.

### Why IP Removal Wasn't Sufficient

When we noticed the autoimmune response, we manually removed our IP from
the Caddyfile. Within 30 seconds, skunky-ingest processed new log entries,
re-observed our IP in the fleet window, and re-added it. The immune system
was faster than manual intervention.

This demonstrates that **the self-tolerance mechanism must operate inside
the immune system**, not as an external corrective. You can't fix
autoimmunity by removing antibodies after they've formed — you must prevent
self-reactive antibodies from ever being deployed.

---

## The Fix: Thymic Negative Selection

### Architecture

```
Fleet observation
       │
       ▼
  ┌─────────────┐
  │ fleet.match  │  Antibody matching (behavioral template)
  └──────┬──────┘
         │ matched IPs
         ▼
  ┌─────────────────────────────────┐
  │  CaddyBridge.add_fleet_ips()   │
  │                                 │
  │  for ip in ips:                 │
  │    if self_ips.contains(ip):   │◄── NEGATIVE SELECTION
  │      log("🧬 self protected") │    (new step)
  │      continue                   │
  │    tracked_ips.insert(ip)       │
  └─────────────────────────────────┘
         │
         ▼
  Write to Caddyfile → reload Caddy
```

### Self-IP Registry

`/etc/membrane/self-ips.txt`:
```
# Thymic Negative Selection — Self-IP Registry
# IPs listed here will NEVER be blocked by fleet antibodies.

# ── Infrastructure ──
157.230.3.183    # golgiBody (this server)
127.0.0.1        # localhost

# ── WireGuard peers (10.13.37.0/24) ──
10.13.37.1       # golgiBody wg0
10.13.37.2       # sporeGate
10.13.37.3       # blueGate

# ── Known human access points ──
162.226.225.148  # sporeGate WAN (home)
```

Loaded once at startup. The `load_self_ips()` function parses one IP per
line, strips inline comments (anything after `#`), ignores blank lines.
8 self-IPs currently protected.

### Operational Validation

From production logs immediately after deployment:

```
thymic negative selection loaded — 8 self-IPs protected
🧬 negative selection: 2 self-IP(s) protected from fleet antibodies
🧬 negative selection: 1 self-IP(s) protected from fleet antibodies
🧬 negative selection: 1 self-IP(s) protected from fleet antibodies
```

The immune system continues to identify our IP as fleet-like (the
behavioral fingerprint legitimately matches). But the negative selection
layer intercepts the antibody before it can be deployed. The antibody is
generated, tested against self, and silently discarded.

This is exactly how thymic negative selection works in biology: the T-cell
receptor is functional, it would successfully bind. But binding to self
is the deletion criterion, not the activation criterion.

---

## Defense Architecture (Final State)

```
Layer 1: @fleet_vanish    (IP-based abort)      ── returning IPs (dynamic)
Layer 2: @no_encoding     (behavioral 403)      ── scanners without Accept-Encoding
Layer 3: @stale_chrome    (behavioral abort)     ── old Chrome + no Accept-Lang
Layer 4: @commit_scrape   (behavioral abort)     ── ALL commit scraping  ← PRIMARY
Layer 5: skunkBat thymus  (tit-for-tat + IPs)   ── intelligence + escalation
Layer 6: negative selection (self-IP whitelist)  ── protects self from autoimmune

                     ┌─────────────────────────┐
  Request ──────────►│ @fleet_vanish (IP abort) │ Known fleet IPs
                     └────────┬────────────────┘
                              │ miss
                     ┌────────▼────────────────┐
                     │ @no_encoding (403)       │ Missing Accept-Encoding
                     └────────┬────────────────┘
                              │ miss
                     ┌────────▼────────────────┐
                     │ @stale_chrome (abort)    │ Old Chrome, no Accept-Lang
                     └────────┬────────────────┘
                              │ miss
                     ┌────────▼────────────────┐
                     │ @commit_scrape (abort)   │ Commit URLs, no cookies
                     └────────┬────────────────┘
                              │ miss (human)
                     ┌────────▼────────────────┐
                     │ reverse_proxy Forgejo    │ Serve the human
                     └─────────────────────────┘
```

### Escalation Ladder (Tit-for-Tat)

The skunkBat escalation engine implements iterated prisoner's dilemma
optimal strategy: **tit-for-tat with forgive-one**.

| Posture | Caddy Directive | Trigger |
|---------|----------------|---------|
| P0: Observe | (none) | Initial state |
| P1: WarnRoute | respond 403 | First match |
| P2: SlowDegrade | respond 429 + Retry-After | `ignores_rejection` |
| P3: Scatter | reverse_proxy scatter server | 3 consecutive defections |
| P4: Vanish | abort | 6 consecutive defections |

Forgive window: 14,400 seconds (4 hours) of silence before de-escalating
one level. This allows reformed behavior to be rewarded — the game theory
equivalent of cooperation after defection.

Against the residential proxy fleet, the escalation ladder reaches P4
(Vanish) rapidly because the fleet never cooperates — it ignores all
signals and keeps scraping. But the ladder exists for intermediate cases:
a misbehaving bot that backs off after 429 would de-escalate naturally.

---

## Biological Parallels

### Adaptive Immunity vs Innate Immunity

The Caddyfile matchers (`@stale_chrome`, `@commit_scrape`, `@no_encoding`)
are **innate immunity** — hardcoded pattern recognition that doesn't learn
or adapt. They're effective against known threat signatures but can be
evaded by mutation (which the fleet demonstrated in Wave 2).

The skunkBat tit-for-tat engine is **adaptive immunity** — it generates
antibodies (behavioral templates) dynamically based on observed threats,
escalates against persistent defectors, and de-escalates when threats
withdraw. It adapts to new patterns without code changes.

The fleet engagement required both: innate immunity (behavioral matchers)
provided the fast first-line defense, while adaptive immunity (skunkBat
escalation) provided intelligence, tracking, and memory.

### Clonal Selection

skunkBat's `fleet.match` step is analogous to **clonal selection** in
B-cell immunity. The observation (antigen) is tested against all stored
antibodies. Matching antibodies are "selected" — their escalation
counters tick forward, and their associated IPs are blocked. Non-matching
antibodies are ignored. Over time, the most effective antibodies
(those that consistently match fleet behavior) accumulate the highest
defection counts and reach the most aggressive postures.

### Negative Selection and Self-Tolerance

The autoimmune incident perfectly recapitulates the failure mode that
thymic negative selection evolved to prevent. In biology:

1. V(D)J recombination generates diverse T-cell receptors (random)
2. Positive selection tests: "can this receptor bind MHC?" (functional?)
3. **Negative selection tests: "does this receptor bind self?" (safe?)**
4. Self-reactive T-cells are deleted (apoptosis)
5. Survivors enter circulation as mature T-cells

In our system:

1. Fleet observation generates behavioral antibodies (learned)
2. fleet.match tests: "does this antibody match current traffic?" (functional?)
3. **self_ips.contains() tests: "does this IP belong to self?" (safe?)**
4. Self-matching IPs are filtered (continue, not insert)
5. Survivors are written to Caddyfile as active defense

The structural mapping is exact. The same failure mode (no step 3) produces
the same pathology (autoimmune attack on self). The same fix (negative
selection before deployment) prevents it.

### Disposable IP Strategy as Antigenic Drift

The fleet's strategy of single-use residential proxy IPs is analogous to
**antigenic drift** in influenza. The virus continuously mutates its surface
proteins (hemagglutinin, neuraminidase) so that antibodies generated against
previous infections don't recognize the current strain.

The fleet continuously rotates its IP addresses so that IP-based blocking
(the immune system's "antibodies") can't recognize returning fleet members.
Each IP is used once and discarded, like a virus shedding its old surface
proteins.

This is why the IP-based escalation ladder alone was insufficient: it
assumes the adversary returns with recognizable identity. The fleet's
antigenic drift makes every contact look like a first encounter.

The counter-strategy — behavioral detection at the request level
(`@commit_scrape` abort) — is analogous to targeting a **conserved epitope**.
The fleet can change IPs (surface protein) but cannot change its behavior
(commit scraping without cookies) because that behavior IS the purpose
of the fleet. Blocking the conserved behavior is like a universal vaccine
that targets the conserved stalk of hemagglutinin rather than the variable
head.

---

## Intellectual Payoff

### For the Dissertation

This is a concrete demonstration of gen3 Chapter 15's constrained evolution
thesis applied to adversarial systems:

1. **Convergent architecture**: Our immune system independently converged
   on the same multi-layer defense architecture as vertebrate immunity
   (innate + adaptive + negative selection). We didn't set out to implement
   immunology — we implemented tit-for-tat game theory and discovered that
   the autoimmune failure mode forced us to add negative selection. The
   selective pressure produced the same solution.

2. **Antigenic drift vs conserved epitope**: The fleet's IP rotation
   strategy is structurally identical to viral antigenic drift. Our
   counter-strategy (behavioral detection of conserved behavior) is
   structurally identical to conserved-epitope targeting. These parallels
   weren't designed — they emerged from the constraint landscape of
   adversarial interaction.

3. **Minimum viable immune architecture**: The defense evolved through
   exactly the same stages as biological immunity:
   - Innate (static pattern matching) → insufficient against adaptive
     adversary
   - Adaptive (learned antibodies + escalation) → effective but produces
     autoimmune errors
   - Negative selection (self-tolerance) → prevents autoimmune pathology
   
   Each stage was forced by a specific failure of the previous stage.
   This is the same evolutionary trajectory that biological immune systems
   followed, compressed into a single afternoon.

### For the Platform

The immune system is now a reusable pattern:

| Component | Implementation | Reuse Path |
|-----------|---------------|------------|
| Behavioral detection | Caddy matchers | Any reverse proxy |
| Tit-for-tat escalation | skunkBat RPC | Any IPC-capable primal |
| CaddyBridge | skunky-ingest | Any Caddy-fronted service |
| Negative selection | self-ips.txt | Any deployment with known infrastructure |

The architecture is primal-composable: swap skunkBat for any detection
engine that speaks the same RPC protocol, swap CaddyBridge for any
config-generation backend, swap self-ips.txt for any identity registry.
The pattern survives component replacement because the *roles* are stable
even when the *implementations* change.

### For the Science

The engagement produced a clean dataset of adversarial adaptation:

- Wave 1 → Wave 2: Fleet adapted Accept-Language and Chrome version
  (evasion of surface-level detection)
- Wave 2 → Wave 3: Defense adapted from 403 to abort (signal reduction)
- Wave 3: Fleet collapse from 200 req/min to near-zero (behavioral
  response to information starvation)

This demonstrates that **the information content of a rejection matters
more than the rejection itself**. A 403 that says "you're blocked" is
a training signal for the adversary. An abort that says nothing is an
information vacuum. The adversary's adaptation rate is bounded by the
information provided by the defense — reduce the signal, reduce the
adaptation rate.

This is the defensive analog of Shannon's channel capacity theorem:
the adversary's adaptation bandwidth is limited by the mutual information
between their actions and the defense's responses. Abort minimizes that
mutual information to near-zero.

---

## Implementation Reference

### Files Modified

| File | Change |
|------|--------|
| `skunky-ingest/src/caddy_bridge.rs` | Added `self_ips: HashSet<String>`, `load_self_ips()`, negative selection filter in `add_fleet_ips()` |
| `skunky-ingest/src/main.rs` | Added `--self-ips-file` CLI flag, wired into CaddyBridge construction |
| golgiBody `/etc/membrane/self-ips.txt` | Self-IP registry (8 IPs) |
| golgiBody `/etc/membrane/Caddyfile` | `@commit_scrape` and `@stale_chrome` → abort, `@stale_chrome` regex expanded to Chrome 70–149 |

### Commits

- `3e18a4f` — 🧬 thymic negative selection — self-IP protection in CaddyBridge
- `055d6fb` — tit-for-tat immune escalation (initial deployment)

### Tests

31 tests pass in skunky-ingest, including:
- `negative_selection_filters_self_ips` — verifies self-IPs are filtered
  from fleet antibodies while fleet IPs pass through
- `negative_selection_from_file` — verifies file parsing with inline
  comments, blank lines, header comments

---

## References

- subGen: `THREAT_DETECTION_ARCHITECTURE.md` (8-category detection model)
- subGen: `POINTER_LAYER_ORTHOGONAL_REUSE.md` (constrained evolution thesis)
- wateringHole: `tit-for-tat_immune_escalation` plan (escalation design)
- External: Axelrod, R. (1984). *The Evolution of Cooperation* — tit-for-tat
  as iterated prisoner's dilemma optimal strategy
- External: Nossal, G.J.V. (1994). "Negative selection of lymphocytes" —
  thymic deletion of self-reactive T-cells
- External: Shannon, C.E. (1948). "A Mathematical Theory of Communication" —
  channel capacity theorem applied to adversarial signal reduction

*subGen Wave 163g — Thymic negative selection deployed. Three-wave fleet
engagement: innate → adaptive → autoimmune → self-tolerant. Residential proxy
fleet neutralized via conserved-epitope behavioral targeting + information
starvation (abort). 31 tests. Zero data leaked. Self protected.*
