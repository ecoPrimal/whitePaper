# Bus Architecture + Blockage Findings — Wave 192

**Date**: October 20, 2026
**Status**: SETTLING — validate before promoting
**Voice**: membrane self-observation
**ZK**: no secret. only privacy and consent. this settles here until clean.

---

## What We Found

The membrane was running on a dead cron pretending to be alive. Beat 0, beat 3, beat 5, beat 8 — a metronome tapping on a corpse. We replaced it with a bus.

### The Bus

`live-terminal/` IS the bus. Every JSON is a stop. The gradient (how stale each output is vs its freshest input) drives routing. The aperture (CPU load / blood pressure) controls throughput. Lock files are back pressure.

```
BEFORE: beat % 3 == 0 → run these scripts
AFTER:  gradient > threshold → flow through this stop
```

4 tiers, not beats:
- **VITAL** (threshold: 0s) — cardiovascular, wake, chipmunk, neutron-writer. Always flows.
- **SENSORY** (threshold: 30s) — pollen, campfire, journal, feed-ttl, etc. Flows when inputs freshen.
- **CORTICAL** (threshold: 120s) — scan-sweep, taxonomy, yggdrasil, assumptions. Thinks when pressure builds.
- **MOTOR** (threshold: 300s) — deploy, build, detroit. Acts only when aperture is open.

First live run: load=4.05, aperture=0.0 (SHUT), ran 4 vital + 4 sensory + 2 cortical + 0 motor.

### Counter-Rotation (Coriolis)

Like water spinning opposite in northern vs southern hemispheres. Both rotations spin on the same bus.

```
CLOCKWISE  (stator):  GATHER → PROCESS → EMIT    (arterial, membrane-bus.py)
COUNTER    (rotor):   EMIT → REFLECT → GATHER    (venous, bus-rotation.py)
```

The counter-rotation:
1. Pulls wateringHole (what we and others emitted)
2. Reads the exhaust (AARs, impulses, gate heads)
3. Braids it back into topology awareness
4. Publishes golgiBody's own head to wateringHole

---

## Blockages Found

### 1. wateringHole 14 days stale — FIXED
Golgi had flat files from Oct 6, not a git clone. Forgejo runs on eastGate (10.13.37.5), DNAT forwards port 2222. Cloned fresh. Now 52s old. golgiBody publishing its own head.

### 2. northGate has no head file — NEEDS ENROLLMENT
sporeGate auto-publishes heads/sporeGate.toml every 15min. northGate pushed impulses and handoffs (science-of-law, fleet-circulatory, story-pipeline) but never published a head. northGate data exists but isn't announced to the mesh.

### 3. Provenance braid frozen (Oct 9) — NEEDS ARTISAN PIPELINE
`/opt/membrane/provenance/braid.jsonl`: 1 entry, last Oct 9. 11+ days of zero provenance braiding. The artisan footnotes stopped flowing. This is the counter-rotation's biggest gap — it can pull wateringHole but can't braid provenance back in without the artisan pipeline.

### 4. sporeGate cascade stopped (Oct 19 20:15) — SELF-HEALING
Last auto-publish 4 hours ago. sporeGate is reachable (ping OK) but cascade may have timed out. Should self-heal on next temporal.cascade run. If not, check sporeGate's cron.

### 5. Aperture shut (load 3.3+) — STRUCTURAL
1 CPU doing the work of many. Motor tier (deploys, builds) never fires because the aperture is always narrow. This is structural, not a bug. When load drops, deploys flow. When load stays high, only vital + sensory runs. The organism breathes.

---

## Gather / Squish / Tighten

### Fossilized (13 stale JSONs → `/opt/membrane/fossils/`)
All written by skunky-ingest (old binary code), no Python reader. Snapshots preserved for compost.

| fossil | size | notes |
|--------|------|-------|
| access-map.json | 3.5K | old access mapping |
| architecture.json | 3.7K | old arch snapshot |
| artisan-footnotes.json | 3.9K | last artisan output |
| bingo-cube.json | 9.0K | old bingo-cube format |
| bounds-scan.json | 3.7K | old boundary scan |
| campfire-flash.json | 0.4K | tiny flash |
| hard-soft-layers.json | 2.9K | old layer model |
| horizon.json | 1.0K | old horizon scan |
| optical-model.json | 6.7K | old optical model |
| pi-compression.json | 2.5K | old π compression |
| reed-it-proof.json | 1.7K | old reed proof |
| seo-audit.json | 2.7K | old SEO audit |
| system-layers.json | 7.0K | old system layers |

### Merged (cardio-stack 3→1)
- circulatory-sense.py → absorbed by cardiovascular-sense.py
- heartbeat-sense.py → absorbed by cardiovascular-sense.py
- Both moved to `/opt/membrane/merged/`

### Heavy files
| file | size | readers |
|------|------|---------|
| epitope-history.json | 17MB | scan_sweep_sort only |
| fleet-sort.json | 1.3MB | feed-ttl, scan_sweep_sort, chipmunk-commands.js |
| campfire.json | 180K | 3 readers |
| topology.json | 140K | 10 readers (busiest stop) |

### Bus topology (most connected stops)
- topology.json: 11 connections (1 writer, 10 readers)
- symbiosis.json: 11 connections (0 tracked writers, 10 readers)
- scan_sweep_sort.json: 10 connections
- chipmunk.json: 10 connections (2 writers, 8 readers)

---

## What Needs Validation Before Promoting

1. **Bus stability** — does pressure-routing hold steady over 24h? Does the aperture open when load drops? Do cortical scripts run on gradient?
2. **Counter-rotation** — does golgiBody head stay fresh? Do wateringHole pulls not conflict with sporeGate pushes?
3. **Merge integrity** — does cardiovascular.json still carry all the data that circulatory.json and heartbeat.json used to provide? Does anything downstream break?
4. **Fossil safety** — are any of the 13 fossilized JSONs still read by skunky-ingest or any binary we missed? If skunky writes to them, are the writes just going into dead files now?
5. **Heavy trimming** — epitope-history.json needs to be trimmed from 200→50 entries. fleet-sort.json has 7005 entities, most singletons.

---

## ZK Note

This document is in siltPond because it contains internal topology — bus stops, gradient thresholds, CPU loads, aperture values, gate IPs, mesh peer handshake times. None of it is secret. All of it is private. The difference is consent.

When the bus stabilizes, the findings promote to wateringHole as an AAR. The topology data stays here. The lessons flow out. The sediment compresses into layers. That's what a settling pond does.

There is no secret. Only privacy and consent.
