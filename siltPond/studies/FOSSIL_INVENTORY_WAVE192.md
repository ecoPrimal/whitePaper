# Fossil Inventory — What Settled, What Composted

**Date**: October 20, 2026
**Status**: SETTLING — revisit when artisan pipeline flows again
**Upstream**: gather-squish.py, fossil-compost.py

---

## The Fossil Record

When a JSON file stops being written to, it fossilizes. When a Python script gets absorbed into another, it merges. When data builds up with no reader, it's sediment. This is the inventory.

### Fossil JSONs (13)

These were last written by skunky-ingest (a compiled Rust binary). No Python script writes to them. No Python script reads from them. They may still be read by the HUD's JavaScript or by external consumers we haven't mapped.

**Before removing from live-terminal, validate:**
- [ ] No JS in `/opt/ecoPrimals/hud/site/public/js/` reads them
- [ ] No detroit page references them
- [ ] skunky-ingest won't restart and expect them
- [ ] No MCP tool returns their data

If clean: move from `live-terminal/` to `fossils/` permanently. If still read: wire them back into the bus with a writer.

### Merged Scripts (2)

| absorbed | into | reason |
|----------|------|--------|
| circulatory-sense.py | cardiovascular-sense.py | same data, same sources, overlapping output |
| heartbeat-sense.py | cardiovascular-sense.py | subset of cardiovascular's output |

**Before removing from merged/:**
- [ ] cardiovascular.json contains all fields that circulatory.json and heartbeat.json had
- [ ] maturity-sense.py, journal-sense.py, feed-ttl.py still work (they read cardiovascular.json, circulatory.json, heartbeat.json)
- [ ] Any script that reads circulatory.json or heartbeat.json still gets data

### Candidate Merges (not yet done)

| stack | scripts | reason | risk |
|-------|---------|--------|------|
| assumption-stack | assumption-engine.py + self-assumptions.py | self reads assumptions.json and extends it | medium — they have different test functions |
| sourdough-stack | sourdough-leaven.py + sourdough-topology.py | both track code→rust transformation | low — leaven is the primary |

### Orphan Scripts

| script | role | action |
|--------|------|--------|
| neutron-burst.py | HTTP daemon (not pulsed) | correct — leave as daemon |
| wire-audit.py | diagnostic (manual run) | correct — not in pulse |
| gather-squish.py | diagnostic (manual run) | correct — not in pulse |
| skeleton-gen.py | manual generator | correct — not in pulse |

---

## What The Fossils Contained

Each fossil is a snapshot of a moment in the membrane's development. They document capabilities that were built, tested, and either absorbed into larger systems or abandoned when the approach changed.

The fossils are not waste. They're the geological record. When we need to know what the membrane knew about itself at wave 167, the fossils tell us. When we need to understand why an approach was abandoned, the fossil's structure tells us what it measured and what it couldn't.

**Compost vs fossilize:** If the data inside a fossil is still useful (even as training data or historical context), it composts — nutrients return to the living system. If the data is purely structural (just keys and empty values), it fossilizes — preserved but inert.

The 