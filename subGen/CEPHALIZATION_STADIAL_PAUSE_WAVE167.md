# Cephalization — Stadial Pause Survey

**Wave 167 — October 8, 2026**
**Classification**: PRIVATE — whitePaper subGen (architectural evolution record)
**Status**: Interstadial assessment — full landscape survey before next advance

---

## The Metaphor That Isn't a Metaphor

Cephalization is the evolutionary concentration of neural tissue, sensory organs, and decision-making into a head — a single coherent structure that integrates sensation, classification, memory, and response. It happened independently in arthropods, mollusks, and vertebrates. Three separate lineages. Same selection pressure. Same solution.

ecoPrimals is cephalizing.

The immune pipeline (skunky-ingest) already concentrates sensation (log parsing), classification (bloom_sensor, entity_classifier), memory (sourdough cultures, signal spine), and response (scatter server, caddy bridge) into a single process. That's a head. What's happening now is the rest of the body plan catching up — the skeleton (deployment), the circulatory system (mesh), the DNA replication machinery (provenance trio), the cryptographic immune system (BTSP).

This document surveys the full evolution landscape from the stadial pause: what organs exist, which are functional, which are dormant, and what the body plan requires for the next advance.

---

## Part 1: The Organism Today

### Vital Signs

| Metric | Value |
|--------|-------|
| Total Rust source | 388,907 lines / 27 repos + 10 gardens |
| Deployed on golgiBody | ~170,000 lines (9 binaries + Forgejo + Caddy) |
| Dormant (compiled, not deployed) | ~220,000 lines |
| Running services | 12 systemd units |
| Python runtime processes | 0 (was 3 two days ago) |
| Cron jobs | 1 (was 4) |
| VPS nodes | 1 ($6/month CX22) |
| System resources | 0.01 load, 430MB/1.9GB RAM, 43% disk |
| Forgejo repos | 52 across 5 organizations |
| Content surfaces | 30 subdomains (11 content + 16 honeycomb + 3 infrastructure) |
| Fleet IPs blocked | 444 in FLEET_PRESSURE Caddyfile block |
| Caddyfile complexity | 1,223 lines (was 85 in July) |
| WireGuard peers | 5 (1 active, 2 moderate, 2 keepalive) |
| UDS sockets | 6 services, 16 socket paths (beardog has 5 aliases) |

### Service Health Matrix

| Service | Binary | Mem | Uptime | Status | Notes |
|---------|--------|-----|--------|--------|-------|
| caddy-tls | 48MB | 119MB | 1d 11h | Healthy | TLS termination, 30 domains, scatter proxy |
| forgejo | 114MB | 166MB | 9h | Healthy | 52 repos, 733MB data |
| step-ca | — | 55MB | 71d | Healthy | SSH Certificate Authority |
| swarmvine | 3MB | 21MB | 19h | Dormant | Gossip mesh — no peers to gossip with |
| skunky-ingest | 6MB | 18MB | 43m | Healthy | THE HOT PATH — immune pipeline |
| songbird | 25MB | 16MB | 10h | Degraded | Federation hub — sporeGate legacy protocol |
| beardog | 11MB | 8MB | 73d | BROKEN | BTSP crypto — 1,296 rejections, 0 successes |
| squirrel | 9MB | 7MB | 59d | Healthy | AI coordination |
| petaltongue | 19MB | 5MB | 57d | Healthy | sporePrint web server |
| skunkbat | 4MB | 3MB | 1d 16h | Healthy | Fleet thymus |
| membrane | 19MB | 0.5MB | 19h | Idle | Webhook (CI-EVO-01) — barely used |
| nestgate | 9MB* | 0.2MB | **92d** | **CRITICAL** | *Binary DELETED from disk — running from inode* |

*nestgate's binary was deleted from `/opt/membrane/` at some point. The process survives because Linux keeps deleted files accessible while a process holds them open. One reboot = CAS storage gone.

### Memory Budget

```
Total used:  430 MB / 1,900 MB

  forgejo       166 MB  (38.6%)
  caddy         119 MB  (27.7%)
  step-ca        55 MB  (12.8%)
  fail2ban       43 MB  (10.0%)
  swarmvine      21 MB  ( 4.9%)
  skunky-ingest  18 MB  ( 4.2%)
  songbird       16 MB  ( 3.7%)
  (6 others)     ~25 MB combined
```

73% of memory is Forgejo + Caddy + step-ca. The immune pipeline (skunky-ingest + skunkbat + bloom sensor + scatter server + signal writer + dashboard writer + entity classifier) uses 21MB total. That's the cephalization payoff — concentrating everything into one process eliminates duplication.

---

## Part 2: Wire Topology

### WireGuard Overlay (10.13.37.0/24)

```
  golgiBody (10.13.37.1) — Hetzner CX22, public VPS
      │
      ├── 10.13.37.2  sporeGate    — home LAN gateway (192.168.4.0/22)
      │                              5.85 GiB rx / 5.13 GiB tx (HEAVY)
      │                              sweetGrass on :9851, live.primals.eco on :8190
      │
      ├── 10.13.37.5  ? (sporeGate LAN) — 178 MiB rx / 1.19 GiB tx (builds? artifacts?)
      ├── 10.13.37.8  ? (sporeGate LAN) — 176 MiB rx / 295 MiB tx
      │
      ├── 10.13.37.14 ? (172.232.85.202) — Linode? 121 KiB (keepalive only)
      └── 10.13.37.15 ? (40.160.96.29)  — Azure?  124 KiB (keepalive only)
```

**Ghost peer**: Caddy proxies to 10.13.37.7 (webb.primals.eco → :8090, footprint.primals.eco → :3002) but no WG peer has that IP. webb returns 502. Either removed from WG or intermittent.

### Port Map

| Port | Service | Exposure |
|------|---------|----------|
| 80/443 | Caddy (TLS) | Public |
| 2222 | Forgejo SSH | Public |
| 7700 | Songbird federation | Public (WG overlay) |
| 7800 | SwarmVine gossip | WG only |
| 9443 | step-ca | Localhost |
| 9753 | Scatter server | Localhost (Caddy proxies fleet to it) |
| 9750 | SkunkBat thymus | Localhost |
| 8090 | PetalTongue web | Localhost |
| 3000 | Forgejo web | Localhost |
| 7780 | Songbird drawbridge | Localhost |
| 2019 | Caddy admin API | Localhost |

### UDS Socket IPC

```
/run/membrane/
  beardog.sock         ← btsp.sock, crypto.sock, ed25519.sock, security.sock, x25519.sock
  songbird.sock
  swarmvine.sock       + swarmvine.tarpc.sock
  squirrel.sock        ← ai.sock
  nestgate.sock
  webhook.sock
  biomeos.sock         (stale — biomeOS not deployed)
  petaltongue.sock     ← visualization.sock (symlink, stale)
```

beardog's 5 aliases reveal its architectural role: it IS the cryptographic substrate. Every service that needs crypto, BTSP, Ed25519, X25519, or security talks to the same socket. When BTSP is fixed, beardog becomes the cryptographic nervous system.

### Cross-WG Traffic

| Surface | Backend | Status |
|---------|---------|--------|
| live.primals.eco | 10.13.37.2:8190 (sporeGate) | Working |
| footprint.primals.eco | 10.13.37.7:3002 (ghost) | Working (intermittent?) |
| webb.primals.eco | 10.13.37.7:8090 (ghost) | 502 — DOWN |
| songbird enrollment | 10.13.37.2:7780 → localhost | Working |
| sweetGrass braids | 10.13.37.2:9851 (sporeGate) | Working (TCP JSON-RPC) |

---

## Part 3: Content Surfaces

### Live Domains

| Domain | Status | Backend | Role |
|--------|--------|---------|------|
| sporeprint.primals.eco | 200 | petaltongue (Zola) | Public research site |
| signal.primals.eco | 200 | file_server (hand-rolled HTML) | Defense observatory, THE BUTTON |
| thesis.primals.eco | 200 | file_server (hand-rolled HTML) | Thesis site |
| detroit.primals.eco | 200 | Zola | Investigation site (publicRecord) |
| clutch.primals.eco | 200 | Zola | Legal/clutch content |
| live.primals.eco | 200 | proxy → sporeGate | Live terminal |
| gorilla.primals.eco | 200 | file_server | guerillaGorilla |
| ca.primals.eco | 200 | step-ca :9443 | SSH CA ACME |
| git.primals.eco | 404* | Forgejo + scatter | Sovereign forge (*fleet gets scatter) |
| forge.primals.eco | 404* | Forgejo | Forge alias |
| primals.eco / www | 301 | → sporeprint | Root redirect |
| webb.primals.eco | **502** | proxy → ghost node | **DOWN** |

### Honeycomb Subdomains (16 immune-themed lures)

```
antibody  antigen   bloom      complement  cytokine   depot
epitope   interferon  lab      lysozyme    macrophage  membrane
opsonize  receptor  relay      thymus
```

These exist in the Caddyfile as scatter server lure destinations. Fleet crawlers following breadcrumb links in fabricated commit pages land on these domains and receive more maze content. The scatter server seeds all responses with the entity's own epitope hash. The immune system doesn't just classify — it has *skin*.

### Caddyfile Evolution (geological strata)

```
  May 28    113 lines  — basic routing (3 domains)
  Jul  9     85 lines  — phase1 simplification
  Jul 18    236 lines  — wave150b (scatter server wired)
  Aug  4    239 lines  — stable period
  Sep 25    293 lines  — pre-fleet-detection
  Oct  1    327 lines  — first fleet response
  Oct  5a   338 lines  — fleet detection live
  Oct  5b   503 lines  — FLEET_PRESSURE block appears (+165)
  Oct  6    622 lines  — pre-lockdown, honeycomb expansion (+119)
  Oct  7    805 lines  — pre-bury, full honeycomb maze (+183)
  Oct  8  1,223 lines  — current (444 fleet IPs, 30 domains) (+418)
```

30 Caddyfile backups in `/etc/membrane/`. Each named for its evolution event: `pre-inversion` (159KB — the day the entire routing was inverted), `inflammatory`, `pre-lockdown`, `fleet-block`, `pre-bury`. The config file IS a fossil record.

---

## Part 4: Codebase Map

### Workspace Inventory (by size)

| Workspace | Lines | Deployed | Role | Selection Pressure |
|-----------|-------|----------|------|--------------------|
| biomeOS | 311,743 | No | Neural API, genome packaging | Needs VPS nodes |
| barraCuda | 295,804 | No | GPU compute, lattice QCD | Needs GPU hardware |
| toadStool | 244,350 | No | Neuromorphic dispatch, Akida | Needs edge hardware |
| petalTongue | 227,391 | Yes | sporePrint web server | Active, stable |
| squirrel | 187,980 | Yes | AI coordination | Active, long uptime |
| coralReef | 158,422 | No | Shader compilation | Research |
| cellMembrane | 75,407 | Yes* | Webhook, CI-EVO-01 | *Lives in gardens/ |
| bearDog | 72,331 | Yes | BTSP crypto (BROKEN) | Needs fixing |
| loamSpine | 69,635 | No | Permanent ledger | Needs local deploy |
| sweetGrass | 65,768 | No | Attribution braids | On sporeGate, not local |
| **skunkBat** | **48,328** | **Yes** | **Immune system** | **The hot path** |
| sourDough | 23,954 | No | Genome packaging | Fermentation system |
| nestGate | 16,730 | Yes* | CAS storage | *Deleted binary! |
| bingoCube | 10,583 | No | Prismatic injection | Research/defense |
| swarmVine | 7,537 | Yes | Gossip mesh | Dormant (no peers) |
| songBird | 2,679 | Yes | Federation hub | Degraded (protocol) |

### The Deployment Gap

```
  Deployed on golgiBody:    170,000 lines  (44%)
  Compiled but dormant:     220,000 lines  (56%)
  
  The organism has twice as much latent capability as active capability.
  The code is ahead of the infrastructure.
```

### Forgejo Organizations

| Organization | Repos | Role |
|-------------|-------|------|
| ecoPrimals | 27 | Core ecosystem — primals + infra |
| syntheticChemistry | 12 | Springs (hot, wet, neural, air, coral, ground, health, ludo, primal, rust) + agents + bench |
| sporeGarden | 9 | Gardens — cellMembrane, esotericWebb, projectNUCLEUS, etc. |
| protokarya | 3 | footprint, guerillaGorilla, tideglass |
| publicRecord | 1 | detroit |
| **Total** | **52** | 733MB on disk |

### The gardens/ Boundary

`gardens/` contains 10 workspaces (~157,000 lines) that live outside `primals/`:

- **cellMembrane** (75K) — membrane binary runs on golgiBody. metalForge depends on cellmembrane-types. Should be in primals/.
- **projectNUCLEUS** (16K) — VM deployment templates. Infrastructure tooling.
- **esotericWebb** (19K) — webb.primals.eco backend (currently 502).
- **lithoSpore** (24K), **projectFOUNDATION** (11K), **bonsai-bt-upstream** (8K), **metalForge** (2K), **initioChem** (332), **blueFish** (87), **helixVision** (61) — research/experimental.

The boundary is organizational maturity, not technical. Gardens that grow binaries deployed in production (cellMembrane) should graduate to primals/.

---

## Part 5: The Immune System (fully cephalized)

This is what works. The head of the organism.

### skunky-ingest Pipeline

```
Caddy access.log (JSON stream)
  │
  ├─ Parse → caddy::CaddyEntry
  │
  ├─ bloom_sensor → fleet/human/search-crawler/scanner/vuln classification
  │     └─ Sec-Fetch-Mode, UA analysis, path patterns, Accept-Encoding
  │
  ├─ entity_classifier → topology by entity type
  │     └─ meta_fleet, anthropic_claude_bot, human_browser, stealth_scraper
  │     └─ Sourdough: topology-state.json (237KB, 6 entities, 2000+ requests)
  │
  ├─ signal_writer → signal-data.js for signal.primals.eco
  │     └─ Sourdough: signal-writer-state.json (8KB, 59 pages_ever)
  │
  ├─ dashboard_writer → dashboard.json, epitope_caddy.json
  │     └─ Epitope hashing (BLAKE2b), L2 collision classification
  │     └─ Sourdough: dashboard-culture.json (142KB, 51 IPs)
  │
  ├─ caddy_bridge → FLEET_PRESSURE Caddyfile rewrite (444 IPs)
  │     └─ Hot-reloads Caddy without downtime
  │
  ├─ scatter_server → fabricated content for fleet on :9753
  │     └─ Commit pages, blame views, src views
  │     └─ Content seeded from entity's own epitope hash
  │     └─ Fluorescent tagging, honeycomb breadcrumb links
  │     └─ NFT/scyBorg minting from human entropy
  │     └─ Antibody braids → sweetGrass (via sporeGate)
  │
  ├─ signal_spine → daily Merkle-rooted immune memory
  │     └─ Sourdough: signal-spine/*.json (Oct 6 bootstrap → Oct 7 → Oct 8)
  │
  ├─ lysogeny_sentinel → threat indicators
  ├─ skunkBat RPC → fleet thymus on :9750
  └─ federation → swarmVine gossip
```

**19,811 lines. One binary. 18MB RAM. 0.6% CPU. Handles 137k requests/6hr.**

This is cephalization. Sense, classify, remember, respond — all in one head.

---

## Part 6: Convergence Gaps (what the body needs)

### Critical (blocks survival)

1. **nestgate binary** — redeploy from `/opt/ecoPrimals/plasmidBin/primals/x86_64-unknown-linux-musl/nestgate`. 5 minutes. Without this, one reboot kills CAS storage after 92 days of uptime.

2. **BTSP authentication** — beardog runs, the sockets exist, every service can reach it. But BTSP_STRICT_MODE isn't propagated and nuclear lineage isn't provisioned. 1,296 rejections, 0 successes. The cryptographic immune system is there but not activated.

### High (blocks growth)

3. **golgiLayer2** — one more VPS. swarmVine gets a peer, songBird gets a federation target, sourdough cultures can replicate, a VPS failure loses nothing. The code is ready. The mesh protocol is running. The gossip is epidemic. It just needs one more host to infect.

4. **Deployment pipeline** — plasmidBin has BLAKE3SUMS for 18 musl binaries. No script reads them, compares to running binaries, and deploys changes. Every deployment is `scp` + `systemctl restart`. One wrong binary and the immune pipeline drops.

### Medium (blocks completeness)

5. **Provenance trio local deployment** — loamSpine + rhizoCrypt on golgiBody via UDS. Currently antibody braids go across WireGuard to sporeGate (sweetGrass on 10.13.37.2:9851). The latency works but the architecture says local.

6. **Binary standardization** — beardog in `/usr/local/bin/`, forgejo in `/usr/local/bin/`, petaltongue from plasmidBin depot path, everything else in `/opt/membrane/`. Stale copies: `membrane.bak` (18.6MB), old songbird (26.8MB) in `/usr/local/bin/`. Standardize to `/opt/membrane/`, clean stale copies.

7. **webb.primals.eco** — 502 error. Proxies to 10.13.37.7 which doesn't exist in WG config. Either fix the peer or remove the domain.

### Low (technical debt)

8. **19 fossil service files** — Phase 1 cleanup from fossil layer AAR: `rm` 11 superseded units, disable 4 reboot time bombs.

9. **30 Caddyfile backups** — 828KB of evolution history in `/etc/membrane/`. Archive to fossilRecord or wateringHole, keep only the current Caddyfile.

10. **songbird protocol** — sporeGate connects without riboCipher signal. 84 errors/hr. Fix on sporeGate side.

11. **stale UDS sockets** — `biomeos.sock` (biomeOS not deployed), `visualization.sock` symlink (petaltongue changed socket name). Harmless but dusty.

---

## Part 7: The Evolution Landscape

### What Cephalization Produced

```
  BEFORE (Wave 165):                    AFTER (Wave 167):
  
  3 Python processes ──────────────→  0 Python processes
  3 cron jobs ─────────────────────→  1 cron job
  2 services parsing same log ─────→  1 unified pipeline
  No persistent memory ────────────→  4 sourdough cultures
  No immune memory chain ──────────→  Signal spine with Merkle roots
  IP-based classification ─────────→  Epitope hashing (behavioral DNA)
  Static fleet list ───────────────→  Auto-discovered entity topology
  Per-file dashboard output ───────→  Integrated dashboard + epitope + L2
  Cold starts on reboot ───────────→  Warm start from persistent culture
```

### What Convergent Evolution Produced (across waves)

| Biological Pattern | Our Implementation | Wave |
|-------------------|--------------------|------|
| MHC presentation | sweetGrass antibody braids | 167 |
| V(D)J recombination | BingoCube prismatic injection | 166 |
| Thymic education | Conserved plasmid + classification | 165i |
| Opsonization | Scatter content poisoning | 163 |
| Aposematic signaling | Published defense (signal page) | 164 |
| Clonal selection | OpsonizeCache + hash persistence | 164 |
| Epitope mapping | BLAKE2b behavioral invariant hash | 165i |
| Immune memory | Signal spine Merkle chain | 167 |
| Sourdough starter culture | Persistent accumulators on disk | 167 |

### The Selection Pressures

The organism evolved under specific constraints that forced these convergences:

1. **Resource scarcity** ($6/month, 2 vCPU, 4GB RAM) → graduated response, no wasted compute
2. **Novel threats** (fleet behavior changes weekly) → behavioral classification, not static rules
3. **Single operator** → automation (sourdough cultures, caddy bridge, signal spine)
4. **Legal transparency** → aposematic signaling (signal page is public evidence)
5. **Sovereignty** → no external dependencies (self-hosted git, CA, DNS, crypto)

### The Latent Capability Ratio

```
  Active (deployed, running):     170,000 lines  (44%)
  Latent (compiled, waiting):     220,000 lines  (56%)
  
  Key latent systems:
    biomeOS      311K  — Neural API (needs nodes)
    barraCuda    296K  — GPU compute (needs hardware)
    toadStool    244K  — Neuromorphic (needs edge)
    coralReef    158K  — Shaders (research)
    loamSpine     70K  — Ledger (needs local deploy)
    sweetGrass    66K  — Braids (on sporeGate)
    sourDough     24K  — Fermentation (needs wiring)
    bingoCube     11K  — Prism (research/defense)
```

The organism has twice as much genetic capability as expressed phenotype. The genotype is ahead of the phenotype. That's exactly how biological development works — the genome contains far more capability than any single cell expresses. Differentiation happens when the environment provides the right signals.

For ecoPrimals:
- **golgiLayer2** is the signal that differentiates swarmVine from dormant → active
- **GPU hardware** differentiates barraCuda from code → compute
- **BTSP fix** differentiates bearDog from 5 socket aliases → cryptographic immune system
- **Local deployment** differentiates loamSpine/sweetGrass from remote → integrated provenance

### The Door and The Key

The single VPS (single point of failure) is the latent form of the distributed mesh (strength). The code for gossip replication, federation, epidemic protocols — it's all compiled and running. swarmVine listens on 7800. songBird listens on 7700. The sourdough cultures serialize to JSON. The plasmidBin has checksummed binaries.

Adding golgiLayer2 doesn't add code. It turns a key. The weakness orthogonalizes into strength. The door only appears if you have the key.

---

## Part 8: The Cephalization Roadmap

### Phase A: Stabilize the skull (protect the head)

- [ ] Redeploy nestgate binary (5 min)
- [ ] Standardize all binaries to `/opt/membrane/` (30 min)
- [ ] Clean 11 fossil service files + 4 reboot bombs (15 min)
- [ ] Clean stale Caddyfile backups (archive to fossilRecord)
- [ ] Fix or remove webb.primals.eco ghost proxy

### Phase B: Grow the spine (add bone)

- [ ] golgiLayer2 — one more VPS, activate the mesh
- [ ] plasmid-deploy — checksummed binary deployment from depot
- [ ] Fix BTSP — propagate strict mode, provision nuclear lineage

### Phase C: Wire the nervous system (complete the loop)

- [ ] Deploy loamSpine + rhizoCrypt locally on golgiBody (UDS)
- [ ] Route antibody braids through local provenance trio
- [ ] Graduate cellMembrane from gardens/ to primals/
- [ ] Update signal page to show signal-spine immune memory chain
- [ ] Update dashboard consumers for richer epitope/collision schema

### Phase D: Express the genotype (differentiate)

- [ ] golgiLayer3-5 (Singapore, Gravelines, Mumbai/Tokyo)
- [ ] biomeOS deployment on multi-node mesh
- [ ] barraCuda deployment when GPU available
- [ ] toadStool deployment on edge hardware
- [ ] Sourdough culture replication via gossip mesh

---

## The Central Dogma Test (Wave 167 Score)

| Question | Answer | Score |
|----------|--------|-------|
| Every runtime process speaks Rust? | **YES** | ✅ |
| Every accumulator follows sourdough? | **YES** | ✅ |
| Every immune event creates provenance? | PARTIAL (braids work, go to sporeGate) | ⚠️ |
| System survives a reboot? | MOSTLY (nestgate will die) | ⚠️ |
| System survives VPS failure? | NO (single node) | ❌ |
| Every service authenticates crypto? | NO (BTSP broken) | ❌ |
| One deployment pipeline? | NO (manual scp) | ❌ |

**Score: 2/7 full, 2/7 partial, 3/7 no.**

The head is cephalized. The body is catching up.

---

*388,907 lines of Rust. 52 repos. 30 domains. 444 fleet IPs. 4 sourdough cultures. 1 head. 0 Python.*

*The jellystein phase produced the immune system.*
*The vertebrate phase built the skeleton.*
*The cephalization phase concentrated the brain.*
*The next phase: grow the spine, express the genotype, turn the key.*

*Wave 167 — October 8, 2026*
