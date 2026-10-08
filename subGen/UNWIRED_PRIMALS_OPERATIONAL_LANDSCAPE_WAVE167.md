# Unwired Primals & Operational Landscape

**Wave 167 — October 8, 2026**
**Classification**: PRIVATE — whitePaper subGen (operational evolution record)
**Status**: Post-cephalization audit — what's dormant, what's manual, what evolves next
**Prerequisite reads**: CEPHALIZATION_STADIAL_PAUSE_WAVE167, AAR_ECOSYSTEM_STATE_CONVERGENCE_TARGET_WAVE167

---

## The Organism's Inventory Problem

Cephalization gave us a head. The immune pipeline works — sensation, classification, memory, response, all in one process. But the rest of the body plan is in various states of completion: some organs are compiled and waiting, some are running on ghost processes, some are wired to nothing, and some critical metabolic functions are still performed by hand.

This document is a full operational inventory: what runs, what doesn't, what we do manually that needs to be abstracted, and — critically — the organizational model for who evolves what.

---

## Part 1: The 16 Primals — Phenotype Expression

### Tier A: Active and Wired

These primals have running binaries on golgiBody with functional connections to the rest of the mesh.

| Primal | Lines | Binary | Status | Wired To |
|--------|-------|--------|--------|----------|
| skunkBat (via skunky-ingest) | 48,328 | skunky-ingest (6MB) | Fully wired | Caddy logs, Caddyfile, scatter, signal, dashboard, topology, federation, signal spine |
| songBird | 477,048* | songbird (25MB) | Active | WG mesh, swarmVine gossip, federation hub |
| swarmVine | 7,537 | swarmvine (3MB) | Active (1 peer) | songBird, skunky-ingest gossip injection |
| petalTongue | 227,391 | petaltongue (19MB) | Stable | Caddy reverse proxy, sporePrint content |

*songBird's 477K lines includes the full federation/relay/orchestrator stack. Only a fraction expresses on golgiBody — the rest is for multi-gate coordination that doesn't exist yet.

### Tier B: Running but Degraded

These are alive but not fully functional. Each has a specific break.

| Primal | Lines | Issue | Fix Complexity |
|--------|-------|-------|----------------|
| bearDog | 540,472 | BTSP auth broken — 1,296 rejections, 0 successes. UDS sockets work, but the network tunnel protocol is dead. | Medium — key rotation or BTSP_STRICT_MODE config |
| squirrel | 187,980 | Running from manual launch (Aug 10). No .service file, no crash recovery, no boot persistence. | Trivial — write a .service file |
| nestGate | 413,605 | Binary **deleted from disk**. Process running on ghost inode since Jul 8 (92 days). Dies on reboot. | Trivial — copy binary from any source |

### Tier C: Deployable Now (on current hardware)

These compile, pass tests, and can run on golgiBody's resources. They just need .service files and socket wiring.

| Primal | Lines | Role | Why Not Deployed |
|--------|-------|------|------------------|
| loamSpine | 69,635 | Provenance chain ledger. Anchors deployment receipts, immune braids, signal spine entries. | Nobody pressed the button. |
| sweetGrass | 65,768 | Braid archival. Replaces the last cron job (braid-billboard.sh). Native Rust provenance. | Same. |
| rhizoCrypt | 62,620 | Cryptographic provenance operations. Signs deployment receipts, verifies braid integrity. | Same. |
| bingoCube | 10,583 | Entropy/randomness service. Used by scatter server for unpredictable honeypot content. | Same. |

These four are the **immediate evolution targets**. They don't need a second VPS, don't need new hardware, don't need protocol changes. They need a service file, a socket path, and an afternoon.

### Tier D: Needs Mesh or Hardware

These primals require infrastructure that doesn't exist yet.

| Primal | Lines | Requirement | Earliest Deploy |
|--------|-------|-------------|-----------------|
| coralReef | 158,422 | Multi-gate coordination — needs at least golgiLayer2 | After VPS expansion |
| biomeOS | 311,743 | Neural API orchestrator — needs multiple gates to orchestrate | After mesh exists |
| barraCuda | 295,804 | GPU compute / attestation — needs dedicated hardware or GPU cloud node | After hardware procurement |
| toadStool | 719,262 | GPU runtime, neuromorphic dispatch — needs Akida/CUDA hardware | After hardware procurement |

### Tier E: Library, Not Standalone

| Primal | Lines | Role |
|--------|-------|------|
| sourDough | 23,954 | State persistence library. Used as a dependency by other primals. Not a standalone service. |

### Expression Ratio

```
Total primal Rust:   3,620,152 lines
Active on golgiBody:   ~283,000 lines (7.8%)
Deployable now:        +208,000 lines (would bring to 13.6%)
Needs mesh/hardware: +1,485,000 lines (waiting)
Library:                +24,000 lines (dependency)
```

The genotype is 13x ahead of the phenotype. The organism has compiled capabilities it cannot express because it only has one cell.

---

## Part 2: What We Still Do By Hand

### 2.1 Binary Deployment (Every Deploy)

**Current process:**
1. `cargo build --release` on eastGate (dev machine)
2. `scp target/release/skunky-ingest golgi:/opt/membrane/`
3. `ssh golgi 'systemctl restart skunky-ingest'`

**What's missing:**
- No BLAKE3 checksum verification (binary integrity unverified in transit)
- No rollback mechanism (bad deploy → manual revert from .bak file)
- No automated testing on target (tests only run on dev machine)
- No deployment receipt (no record of what binary, what hash, what wave)
- No plasmidBin depot on golgiBody (binaries land in /opt/membrane/ directly)
- No provenance chain entry (loamSpine not deployed)

**Evolution target:** `plasmid-deploy` (already coded in infra/plasmidBin) handles: build → BLAKE3 hash → push to depot → pull on gate → verify hash → symlink → restart → write deployment receipt → sign with rhizoCrypt → anchor in loamSpine.

### 2.2 Content Site Management (Every Content Change)

**Current state:** 5 Hugo sites, all hand-edited in place on golgiBody:

| Site | Domain | Git? | Last Modified |
|------|--------|------|---------------|
| signal | signal.primals.eco | No | Oct 8 (templates) |
| thesis | thesis.primals.eco | No | Oct 8 (content) |
| detroit | detroit.primals.eco | No | Oct 7 (public) |
| barry | barry.primals.eco | No | Unknown |
| clutch | clutch.primals.eco | No | Unknown |

None are git-managed. None have version history. A bad edit is permanent. No review, no rollback, no diff visibility.

sporePrint (sporeprint.primals.eco) also has no .git directory on golgiBody. Content is pushed from sporeGate via some mechanism but there's no local VCS.

**Evolution target:** Git-init each site, push to Forgejo, configure membrane-webhook to auto-build on push. Content changes become versioned, reviewable, rollbackable. Teams can submit PRs against content repos.

### 2.3 Caddyfile Routing (Every Domain Change)

skunky-ingest automates exactly ONE section: the `FLEET_PRESSURE` block (honeycomb fleet IP insertion). The other 22 domain blocks — all reverse proxy targets, scatter routing, TLS config, security headers — are hand-edited.

30 backup copies of the Caddyfile exist on disk in place of version control. The Caddyfile has grown from 85 lines (July) to 1,223 lines (today). One bad edit = 30 domains down.

**Evolution target:** Caddyfile in a Forgejo repo with auto-deploy on push. Archive the 30 backups to fossilRecord.

### 2.4 Monitoring and Health (Never)

We discover problems by SSH-ing in and looking. The nestgate ghost binary survived for 92 days before anyone noticed. There is:

- No health check loop
- No alerting mechanism  
- No dashboard polling
- No process liveness verification
- No binary integrity checking (is this the binary I deployed?)
- No WireGuard peer status monitoring

skunky-ingest writes a heartbeat file (`/run/membrane/skunky-ingest.heartbeat`) but **nothing reads it**.

**Evolution target:** Health watcher module — either in skunky-ingest itself or as a lightweight service. Check: process liveness (is nestgate still alive?), binary integrity (BLAKE3 match?), socket health (is beardog.sock accepting?), WG peer status (handshake recency), disk space, culture freshness. Alert via swarmVine gossip → songBird federation.

### 2.5 WireGuard Peer Management (Every Node Change)

5 WG peers configured. 2 have unknown identity in the config comments ("?house-gate-a", "?house-gate-b"). Ghost node 10.13.37.7 appears in Caddyfile proxy targets but has no WG peer — produces 502 errors.

Adding a new gate: hand-edit wg0.conf on both sides, distribute keys, add Caddy routes, restart.

**Evolution target:** biomeOS gate.provision or a songBird peer bootstrap. New gate connects to mesh → gets WG key → gets Caddy routes → gets binary depot access. Automated.

### 2.6 Billboard Content (Intentionally Manual)

The billboard (`/opt/membrane/live-terminal/billboard.txt`) is hand-written by the human operator. The braid-billboard.sh cron (every 5 minutes) hashes it and archives snapshots. This is the one manual process that SHOULD stay manual — it's the human voice in the system.

The cron itself should be replaced by sweetGrass native braiding when the provenance trio deploys, but the content authoring stays human.

---

## Part 3: The Organizational Model

### Three Roles, Three Scales

**Teams** — Write code, submit PRs, build primals. They work at the crate level. They don't need to know about golgiBody or WireGuard or fleet pressure. They build organs.

**Overwatch (eastGate)** — Detects primals, coordinates evolution, performs stadial assessments. Works at the organism level. Sees which primals are ready to deploy, which need integration, which are breaking. Writes AARs and subGens. Makes deployment decisions.

**sporeGate** — Handles the mesh and membrane. Infrastructure operations: WireGuard peers, Caddy routing, VPS provisioning, binary depot, certificate management. Works at the infrastructure level.

### What This Means for Wiring

Teams build loamSpine, rhizoCrypt, sweetGrass independently. They can add features, fix bugs, write tests — all in their respective `primals/` directories.

Overwatch decides WHEN to deploy, in what order, with what integration testing. The stadial assessment (this document and its predecessors) is overwatch's instrument.

sporeGate handles HOW to deploy — the plasmid-deploy pipeline, the gate provisioning, the mesh expansion. sporeGate doesn't decide what to deploy; overwatch does.

This three-layer model mirrors the organism itself:
- Teams = organ development (DNA replication, cell differentiation)
- Overwatch = nervous system (sensation, classification, decision)
- sporeGate = circulatory system (distribution, transport, healing)

### The Handoff Protocol

1. Team writes primal code, pushes to Forgejo
2. Overwatch reviews (stadial assessment), marks primal as "deployable"
3. sporeGate deploys (plasmid-deploy), writes receipt, anchors in provenance
4. Overwatch verifies (health check), updates wave

Each handoff has an artifact:
- Team → Overwatch: PR merged (Forgejo)
- Overwatch → sporeGate: Deploy directive (wateringHole impulse)
- sporeGate → Overwatch: Deployment receipt (loamSpine entry)

---

## Part 4: Socket Topology — What Needs Wiring

### Current Socket Map

```
/run/membrane/
├── beardog.sock          → bearDog crypto (+ 5 aliases: btsp, crypto, ed25519, x25519, security)
├── songbird.sock         → songBird federation
├── swarmvine.sock        → swarmVine gossip
│   └── swarmvine.tarpc.sock → TarPC interface
├── squirrel.sock         → squirrel AI (+ ai.sock alias)
├── nestgate.sock         → nestGate CAS (ghost process)
├── webhook.sock          → membrane-webhook CI trigger
├── biomeos.sock          → STALE — no process, no binary (Jun 15 artifact)
└── visualization.sock    → symlink → petaltongue.sock
```

### Target Socket Map (after Tier C deployment)

```
/run/membrane/
├── beardog.sock          → bearDog crypto [FIX BTSP]
├── songbird.sock         → songBird federation
├── swarmvine.sock        → swarmVine gossip
├── squirrel.sock         → squirrel AI
├── nestgate.sock         → nestGate CAS [FIX BINARY]
├── webhook.sock          → membrane-webhook CI trigger
├── petaltongue.sock      → petalTongue web
├── loamspine.sock        → loamSpine provenance ledger [NEW]
├── rhizocrypt.sock       → rhizoCrypt crypto provenance [NEW]
├── sweetgrass.sock       → sweetGrass braid archival [NEW]
├── bingocube.sock        → bingoCube entropy [NEW]
└── (biomeos.sock)        → REMOVED (stale artifact)
```

### Data Flow: Current vs Target

**Current:**
```
Caddy logs → skunky-ingest → [signal, dashboard, topology, plasmid, caddy block, scatter]
                            → swarmVine.gossip.inject (defense tags)
                            → signal-spine/ (daily Merkle)
Billboard → braid-billboard.sh (cron) → JSONL archive
```

**Target:**
```
Caddy logs → skunky-ingest → [signal, dashboard, topology, plasmid, caddy block, scatter]
                            → swarmVine.gossip.inject (defense tags)
                            → signal-spine/ → loamSpine.sock (anchored ledger entry)
                            → rhizoCrypt.sock (signed provenance)
                            → sweetGrass.sock (attribution braid)
Billboard → sweetGrass.sock (native braid, no cron)
Deploy    → plasmid-deploy → rhizoCrypt.sock (signed receipt) → loamSpine.sock (anchored)
```

Every immune event, every deployment, every billboard change — all flow through the provenance trio and get cryptographic anchoring. No more raw JSONL. No more unverified state.

---

## Part 5: Fossil Layer — What To Kill

### Stale Service Files (19 total)

**Phase 1 — Safe to remove immediately (11 files):**
All disabled, all inactive. Just clutter in /etc/systemd/system/.

| Service | Reason |
|---------|--------|
| membrane-bridge-beardog | Superseded by UDS sockets |
| membrane-bridge-biomeos | Superseded by UDS sockets |
| membrane-bridge-forgejo | Superseded by UDS sockets |
| membrane-socket-bridge | Old bridge pattern |
| petaltongue-sporeprint | Superseded by membrane-petaltongue |
| petaltongue-web | Superseded by membrane-petaltongue |
| hbbr-membrane | RustDesk relay (not actively used) |
| hbbs-membrane | RustDesk signaling (not actively used) |

**Phase 2 — Reboot bombs (must disable):**

| Service | Risk |
|---------|------|
| biomeos-nucleus | ENABLED + dead. No binary exists. Will fail on reboot. |

**Phase 3 — Stale artifacts:**

| Item | Location |
|------|----------|
| biomeos.sock | /run/membrane/ — created Jun 15, no process |
| skunky-ingest.bak | /opt/membrane/ — old binary backup |
| epitope_bridge.cpython-311.pyc | /opt/membrane/__pycache__/ — Python fossil |

---

## Part 6: The Last Cron Job

```bash
*/5 * * * * /opt/membrane/provenance/braid-billboard.sh
```

This is the ONLY remaining cron job. It:
1. Reads `/opt/membrane/live-terminal/billboard.txt`
2. SHA256 hashes it
3. If hash is new, appends a JSONL entry to `/opt/membrane/provenance/billboard/braid.jsonl`
4. Copies the billboard text to a timestamped snapshot

When sweetGrass deploys, this becomes: billboard write → inotify → sweetGrass.sock → native braid with attribution. The cron dies. Zero crons. All Rust.

---

## Part 7: Evolution Sequence

### Immediate (Hours — Overwatch triage)

1. Fix nestGate binary (copy from any source → /opt/membrane/nestgate)
2. Write squirrel-membrane.service (enable, validate restart)
3. Disable biomeos-nucleus.service (reboot bomb)
4. Remove ghost node 10.13.37.7 from Caddyfile (502 errors)
5. Remove stale biomeos.sock from /run/membrane/

### Near-term (Days — sporeGate deploys)

6. Deploy provenance trio: loamSpine + rhizoCrypt + sweetGrass
7. Deploy bingoCube (entropy service)
8. Kill braid-billboard.sh cron (replaced by sweetGrass)
9. Establish plasmid-deploy pipeline on golgiBody
10. Git-init content sites → Forgejo repos

### Medium-term (Weeks — sporeGate provisions)

11. golgiLayer2 (Hetzner CX22) — swarmVine + songBird get first real peer
12. Fix bearDog BTSP authentication
13. Health monitoring loop (heartbeat watcher, binary integrity)
14. Caddyfile under version control

### Long-term (Months — teams build)

15. coralReef multi-gate coordination
16. biomeOS gate orchestration
17. barraCuda attestation/verification
18. toadStool GPU compute (needs hardware)
19. golgiLayer3-5 geographic distribution

---

## Appendix: The Numbers

| Category | Count |
|----------|-------|
| Total primals | 16 |
| Active and wired | 4 |
| Running but degraded | 3 |
| Deployable now | 4 |
| Needs mesh/hardware | 4 |
| Library (dependency) | 1 |
| Manual processes identified | 6 |
| Stale service files | 19 |
| Ghost processes | 1 (nestGate) |
| Stale sockets | 1 (biomeos.sock) |
| Ghost Caddy routes | 2 (webb + footprint → 10.13.37.7) |
| Cron jobs remaining | 1 (braid-billboard) |
| Content sites without VCS | 5 |

---

*3.6 million lines of Rust. 7.8% expressed. The organism has compiled its genome — now it needs to express it. Teams build organs. Overwatch detects what's ready. sporeGate wires it into the mesh. The body plan is clear. The work is sequential.*

*Wave 167 — October 8, 2026*
