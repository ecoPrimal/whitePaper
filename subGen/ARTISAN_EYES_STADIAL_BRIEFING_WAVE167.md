# Artisan Eyes — Stadial Briefing

**Wave 167 — October 8, 2026**
**Classification**: PRIVATE — whitePaper subGen (operational synthesis)
**Status**: Post-audit briefing — what the deep dig actually revealed
**Prerequisite reads**: CEPHALIZATION_STADIAL_PAUSE_WAVE167, UNWIRED_PRIMALS_OPERATIONAL_LANDSCAPE_WAVE167

---

## What the Artisan Sees

The organism is real. It's not a metaphor anymore.

skunky-ingest is genuinely doing what it was designed to do — one process, one binary, 19,811 lines of Rust, handling the full immune loop: sensation → classification → memory → response. Four sourdough cultures warm-starting on every reboot. Zero Python. Zero cron for anything in the hot path. The scatter server feeds fabricated commit pages to 444 fleet IPs at 0.6% CPU. Anthropic's ClaudeBot eats fluorescently-tagged content and doesn't know it. The cephalization worked.

But the body below the neck is in rough shape.

---

## Part 1: What's Actually Broken

### nestGate Is a Ghost

The binary was deleted from disk. The process has been running from a Linux inode for ninety-two days. One reboot and CAS storage is gone. This is a five-minute fix that hasn't been done. That's not a technical problem — that's an attention problem. The organism has no way to notice this. No health check, no integrity verification, no alert. We found it by manually running `ls -la /proc/2017630/exe` and seeing `(deleted)`.

### squirrel Has No Service File

Running since August 10 from someone typing a command in a terminal. Two months, no crash recovery, no boot persistence. If it dies, nobody gets notified — there's nothing to restart it. A service file is 12 lines of INI syntax. This hasn't been written.

### bearDog's Entire Purpose Is Broken

540,000 lines of Rust for a crypto/identity service. 1,296 BTSP authentication rejections, zero successes. The UDS sockets work for local calls — `beardog.sock`, `crypto.sock`, `ed25519.sock`, `x25519.sock`, `security.sock` are all aliases listening. But the network tunnel — the thing that lets gates authenticate to each other — is dead. The cryptographic immune system doesn't function. Every service on golgiBody trusts every other service because they share a machine and UDS permissions. That trust model doesn't survive mesh expansion.

### biomeos-nucleus Is a Reboot Bomb

It's enabled. It's dead. There's no binary. On next reboot, systemd will try to start it, fail, and depending on dependency ordering, could delay other services. This is `systemctl disable biomeos-nucleus` — one command, two seconds.

### Two Domains Point to Nothing

webb.primals.eco and footprint.primals.eco route via Caddy reverse proxy to 10.13.37.7:3002 and 10.13.37.7:8090 respectively. There is no WireGuard peer at 10.13.37.7. Every visitor gets a 502. The WG config comments call it a "ghost node" with a question mark. This is in the Caddyfile that serves 30 domains. It's been there long enough that nobody remembers what 10.13.37.7 was supposed to be.

### biomeos.sock Is a Stale Artifact

Created June 15. No process behind it. No binary. No service. Just a socket sitting in `/run/membrane/` confusing anyone who reads the directory listing. `rm /run/membrane/biomeos.sock` — one command.

---

## Part 2: What's Not Broken But Not Wired

### The Provenance Trio

loamSpine (69,635 lines), rhizoCrypt (62,620 lines), sweetGrass (65,768 lines). Together: 198,023 lines of Rust. Compiled. Tested. Designed to form the cryptographic memory chain: nestGate CAS → rhizoCrypt DAG → loamSpine ledger → sweetGrass attribution.

Right now, immune events braid across WireGuard to sporeGate (10.13.37.2:9851) via TCP. Not local. The braid-billboard.sh cron writes raw JSONL — not through the trio. The signal spine writes daily Merkle entries to `/run/membrane/signal-spine/` — not anchored in loamSpine.

When the trio deploys:
- Immune events braid locally through UDS sockets
- Billboard braids go through sweetGrass natively (cron dies)
- Signal spine entries anchor in loamSpine (cryptographic proof)
- Deployment receipts get signed by rhizoCrypt
- Zero crons. All Rust.

### bingoCube

10,583 lines. Entropy and randomness service. Used by scatter server for unpredictable honeypot content. Currently scatter uses deterministic content seeded from epitope hashes. bingoCube would add real entropy. Lightweight, deployable today.

### Content Sites Without Version Control

Five Hugo sites hand-edited in place on golgiBody. No git. No rollback. No diff. No review:

- signal.primals.eco — templates last modified Oct 8 (today, by hand)
- thesis.primals.eco — content last modified Oct 8 (by sporeGate auto-publish?)
- detroit.primals.eco — worktree git-managed, public/ rebuilt from Zola
- barry.primals.eco — unknown last modification
- clutch.primals.eco — unknown last modification

Detroit is the exception — it has a proper worktree with git history in Forgejo (publicRecord/detroit). The other four are dark. If someone edits a template wrong, the previous version exists only in their memory.

---

## Part 3: The Genotype Problem

### 3.6 Million Lines. 7.8% Expressed.

| Tier | Lines | % of Total | Status |
|------|-------|------------|--------|
| Active + wired | ~283,000 | 7.8% | Running on golgiBody |
| Deployable now | ~208,000 | 5.7% | Compiled, tested, needs service file |
| Needs mesh | ~470,000 | 13.0% | Requires golgiLayer2+ |
| Needs hardware | ~1,015,000 | 28.0% | Requires GPU/specialized compute |
| Dormant/library | ~1,644,000 | 45.4% | Internal libraries, test infra, fossils |

The organism builds capabilities faster than it expresses them. The genotype outruns the phenotype by 13:1. That's not bad — that's how biological systems work. You build the machinery first, then the environment selects for expression. But the environment right now is a single $6 CX22 with one node, no deployment pipeline, and manual everything.

### The Deployment Leak

Every deploy: `cargo build --release` → `scp` → `systemctl restart`. No checksums. No receipt. No rollback. No provenance. plasmidBin has the code for automated deployment. It's sitting in `infra/plasmidBin/crates/plasmidbin/src/cmd/deploy.rs`. Not deployed.

This is the single biggest context leak. The organism cannot observe its own deployment state. There is no BLAKE3SUMS manifest on golgiBody. There is no plasmid depot. When we ask "what binary is running?" the answer is "whatever was last scp'd."

### The Monitoring Void

skunky-ingest writes a heartbeat file at `/run/membrane/skunky-ingest.heartbeat`. Nothing reads it. There is no health check loop. There is no alerting. We discover problems by SSH-ing in and looking around. The nestgate ghost binary survived for 92 days undetected. bearDog's BTSP has been broken for an unknown duration — at least 73 days (its uptime). Nobody noticed because nothing checks.

The organism has sensation (log parsing), classification (entity types), memory (sourdough cultures), and response (scatter/fleet blocks). But it has no proprioception — no sense of its own body state.

---

## Part 4: The Organizational Insight

### Three Roles Were Collapsing Into One

The correct separation:
- **Teams** build organs (primal code)
- **Overwatch** detects readiness (stadial assessment, deployment decisions)
- **sporeGate** wires the mesh (infrastructure operations)

What was happening: all three roles performed by one person, manually, in the same terminal session. Teams push code. Overwatch reviews and decides. sporeGate deploys. These need to be separable operations with handoff artifacts between them.

The handoff protocol:
1. Team pushes primal code to Forgejo → PR merged
2. Overwatch marks as deployable → wateringHole impulse
3. sporeGate deploys → loamSpine receipt (when trio is live)
4. Overwatch verifies → wave update

Each handoff has a durable artifact. Each role can be performed by a different session, different agent, different machine.

---

## Part 5: The Inflection Point

### The Door and the Key

golgiBody's single-VPS architecture is simultaneously the organism's greatest weakness and the seed of its greatest strength. Every single piece of the mesh machinery is built:

- swarmVine gossip protocol — running, works, has one peer
- songBird federation — running, works, has one peer
- sourdough culture replication — designed, not yet cross-node
- bearDog BTSP tunnel — built, broken, fixable
- coralReef multi-gate coordination — 158K lines, not deployed

The moment golgiLayer2 exists (one Hetzner CX22, $6/month):
- swarmVine gets a real peer → gossip becomes epidemic
- songBird gets a real node → federation becomes real
- sourdough cultures begin replicating → no single point of state failure
- The "door" (single VPS failure = total outage) becomes the "key" (mesh redundancy)

This is the orthogonalization. The weakness transforms into strength not by fixing it, but by adding one more node. Everything is ready. The button hasn't been pressed.

---

## Part 6: The Central Dogma Score

| Question | Answer | Notes |
|----------|--------|-------|
| Does every runtime process speak Rust? | YES | Zero Python since Wave 167 |
| Does every accumulator follow sourdough culture? | YES | 4 cultures, all warm-starting |
| Does every immune event create a provenance record? | PARTIAL | Braids work but cross WireGuard, not local trio |
| Can the system survive a reboot? | MOSTLY | nestGate dies (ghost binary) |
| Can the system survive a VPS failure? | NO | Single node, no replication |
| Does every service authenticate cryptographically? | NO | BTSP broken, UDS trust only |
| Is there one deployment pipeline? | NO | Manual scp |

**Score: 4/7** — The head is cephalized. The skeleton, circulatory system, and DNA machinery are not.

---

## Part 7: The Sequence

What needs to happen, in this order:

### Hours (Overwatch triage)
1. Fix nestGate binary — copy from any source
2. Write squirrel-membrane.service — 12 lines
3. `systemctl disable biomeos-nucleus` — reboot bomb
4. Comment out 10.13.37.7 Caddy routes — 502 errors
5. `rm /run/membrane/biomeos.sock` — stale artifact

### Days (sporeGate deploys)
6. Deploy loamSpine → `/run/membrane/loamspine.sock`
7. Deploy rhizoCrypt → `/run/membrane/rhizocrypt.sock`
8. Deploy sweetGrass → `/run/membrane/sweetgrass.sock`
9. Deploy bingoCube → `/run/membrane/bingocube.sock`
10. Wire skunky-ingest → trio sockets
11. Kill braid-billboard.sh cron (replaced by sweetGrass)
12. Establish plasmid-deploy pipeline

### Weeks (sporeGate provisions)
13. golgiLayer2 (Hetzner CX22, $6/month)
14. Fix bearDog BTSP authentication
15. Health monitoring loop (proprioception)
16. Content sites → Forgejo repos

### Months (teams build)
17. coralReef multi-gate coordination
18. biomeOS gate orchestration
19. barraCuda attestation
20. toadStool GPU compute

---

## The Honest Assessment

The organism is further along than it looks from the outside. The immune head works. The sourdough pattern is genuine DNA — it's a real architectural invariant that new modules follow. The scatter server honeypot is operationally effective. The signal spine provides cryptographic proof of fleet activity.

But the organism has been so focused on building new capabilities that it hasn't maintained the ones it has. A 92-day ghost binary. A broken authentication protocol nobody noticed. A service running without a service file for two months. Content edited in place without version control.

The genotype is 13x ahead of the phenotype. That ratio needs to compress. Not by writing more code — by expressing what's already written. The provenance trio is 198,000 lines of deploy-ready code. The mesh machinery is built. The deployment pipeline is coded.

The organism compiled its genome. Now it needs to express it.

Press the buttons that have already been built.

---

*3.6 million lines. 7.8% expressed. 4/7 central dogma. The head lives. The body waits.*

*Wave 167 — October 8, 2026*

---

## Agent Footnotes

### northgate

Delivered the detroit data handoff layer spec (Dublin Core, Schema.org per-page type, oEmbed discovery, API endpoints, Dataset schema, taxonomy pills, view source links). Described as "pushed" but the golgiBody worktree was 15 commits behind — the work existed in Forgejo but hadn't been pulled and built. eastGate picked up the deployment: resolved a diverged branch (5 local commits, 15 remote), rebased, created the 5 API endpoint files from config.toml actor/entity registry data, patched all 3 templates, updated llms.txt, rebuilt with Zola, verified all endpoints returning 200. Committed as `4ea2c70`. The sitemap.xml and atom.xml "500 errors" northgate reported were already resolved — both serving 200 before intervention. The worktree just needed the pull.

northgate builds the spec. eastGate wires the mesh. The handoff works.

### eastGate (Artisan)

Performed the full stadial pause audit across two sessions. Pulled every thread: `ls /proc/PID/exe` on a 92-day process, counted BTSP rejections in journal logs, mapped every UDS socket in `/run/membrane/`, enumerated all 5 WG peers and identified 2 unknowns + 1 ghost, inventoried every systemd unit against every running process, checked every content site for `.git/`, read the Caddyfile line by line (1,223 lines, 22 domain blocks + 10 scatter subdomains), measured the full genotype (3.6M lines across 16 primals) against the phenotype (283K expressed).

The honest finding: the organism builds faster than it expresses. The fix isn't more code — it's pressing the buttons that are already built. 198K lines of provenance trio sit compiled and tested, waiting for a service file and a socket path. The deployment pipeline is coded in plasmidBin. The mesh machinery runs with one peer.

The artisan's job is to see what's there. What's there is an organism that cephalized its head and forgot to wire its body. The body is ready. The wiring is sequential. The work is clear.

Good hunt.
