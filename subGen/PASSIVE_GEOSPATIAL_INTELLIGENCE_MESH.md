# Passive Geospatial Intelligence from Adversarial Traffic — The Fleet Maps Itself

**Wave**: 165i | **Date**: Oct 7, 2026
**From**: eastGate overwatch
**Status**: OBSERVATION — emergent capability discovered during mesh deployment
**Upstream**: DISTRIBUTED_SURVEILLANCE_DETECTION_MESH.md
**Biological Analog**: Proprioception — the organism sensing its own position in space by processing afferent signals from distributed receptors

---

## The Discovery

While deploying sensor nodes for the beehive observation mesh (Wave 165h), a second-order capability emerged: **the fleet's traffic, observed from multiple GPS-fixed sensor nodes, produces a spatial map of global surveillance infrastructure.**

Each sensor node has a known GPS coordinate. Each request hitting that node carries a source IP with a known geographic origin. The behavioral fingerprint identifies the organization. Cross-layer correlation reveals routing topology.

The fleet is performing synthetic aperture sensing on itself. Every packet is a radar ping. The sensor array is passive. The map builds automatically.

---

## The Mechanism: Passive Synthetic Aperture

### Physical Radar Analogy

In synthetic aperture radar (SAR), a single radar moves along a flight path, taking measurements at different positions. The combination of measurements from different spatial positions produces an image with resolution far beyond what a single antenna could achieve.

The beehive mesh is a passive SAR:

| SAR Component | Digital Equivalent |
|---|---|
| Radar transmitter | Fleet's scraping pipeline (they transmit) |
| Radar receiver | Sensor node at known GPS coordinate |
| Flight path positions | Multiple VPS locations globally |
| Radar return signal | HTTP request + behavioral fingerprint |
| Synthetic aperture | Cross-layer corroboration across nodes |
| Resolved image | Global surveillance infrastructure topology |

Key difference: in physical SAR, the defender transmits. In passive SAR, **the attacker transmits**. The defender only listens. The fleet cannot stop transmitting without stopping scraping.

### What Each Request Reveals

```
Source: 57.141.20.38 (Meta Platforms Ireland, Dublin)
  → GeoIP: 53.35°N, 6.26°W
  → Organization: Meta Platforms, Inc.
  → Infrastructure: FB-BLOCK /13 prefix
  
Destination: sensor-nyc (golgiBody)
  → GPS: 40.71°N, 74.01°W
  → Provider: DigitalOcean
  
Behavioral Hash: b6c7dc18
  → Chrome/146 (10 versions stale)
  → Sec-Fetch-Mode: ABSENT
  → Accept-Encoding: gzip, deflate, zstd
  → Target: ecoPrimals/wateringHole /blame/
  → Timing CV: 0.057 (METRONOMIC)
```

One request = one data point: `{source_geo, dest_geo, entity, behavior, time}`.

Thousands of requests across multiple sensors = a spatial map.

---

## The Cross-Matrix

### Sensor × Entity Matrix

```
                  NYC           DE            IN           VA           UK
                  40.71°N       50.47°N       19.08°N      38.88°N      51.51°N
                  74.01°W       12.37°E       72.88°E      77.52°W      0.13°W
                  ─────────     ─────────     ─────────    ─────────    ─────────
Meta/Dublin       56 IPs        (pending)     (pending)    (pending)    (pending)
  blame_pct       32.9%         ?             ?            ?            ?
  chrome_lag      10            ?             ?            ?            ?
  timing_cv       0.057         ?             ?            ?            ?

Anthropic/US      1 IP          (pending)     (pending)    (pending)    (pending)
  target          SCATTER       ?             ?            ?            ?
  timing_cv       0.268         ?             ?            ?            ?

Stealth/?         8 IPs         (pending)     (pending)    (pending)    (pending)
  chrome          135           ?             ?            ?            ?
  honest          NO            ?             ?            ?            ?

Huawei/?          3 IPs         (pending)     (pending)    (pending)    (pending)
Google/?          (observed)    (pending)     (pending)    (pending)    (pending)
```

### What the Matrix Reveals

As columns fill in (sensors come online, fleet discovers them via CT logs):

1. **Same entity, same hash, multiple sensors** → Proves global coordination. The fleet scrapes everywhere with the same toolkit.

2. **Same entity, different proxy pools per sensor** → Reveals geographic proxy allocation. Meta may route Dublin IPs to NYC but Asian proxies to Mumbai. The matrix exposes the routing topology.

3. **Same entity, different blame_pct per sensor** → Reveals targeting strategy. Do they do more author attribution mining on some repos than others? Does the strategy vary by geography?

4. **Same entity, different timing per sensor** → Reveals fleet capacity allocation. Metronomic in NYC (full pipeline) but varied in Mumbai (opportunistic scraping) means NYC is the primary target.

5. **Entity absent from some sensors** → Reveals geographic scope. If Meta hits NYC and DE but not Mumbai, their scraping infrastructure may not cover Asia — or they haven't discovered the Mumbai sensor yet.

---

## The Planetary Digital Layer

### GPS-Addressable Signal

Every data point has two GPS coordinates:
- **Source**: GeoIP of the request origin
- **Destination**: known GPS of the sensor node

This produces a set of directed edges on the globe:

```
Dublin (53.35°N, 6.26°W) ──────→ NYC (40.71°N, 74.01°W)     [Meta, 56 IPs, 2.0 RPS]
Dublin (53.35°N, 6.26°W) ──────→ DE (50.47°N, 12.37°E)      [Meta, pending]
Dublin (53.35°N, 6.26°W) ──────→ Mumbai (19.08°N, 72.88°E)   [Meta, pending]
US-East (37.77°N, 122.42°W) ──→ NYC (40.71°N, 74.01°W)      [Anthropic, 1 IP, 10.8 RPS]
Unknown (??) ──────────────────→ NYC (40.71°N, 74.01°W)      [Stealth, 8 IPs]
```

### What This Layer Contains

| Data Type | Source | Resolution |
|-----------|--------|-----------|
| Corporate surveillance topology | Fleet traffic patterns | Per-organization |
| Proxy infrastructure geography | Source IP GeoIP | Per-datacenter |
| Scraping fleet size by region | Unique IPs per sensor | Per-/24 subnet |
| Content extraction patterns | Path operations (blame, commit, src) | Per-repo |
| Temporal patterns | Timing signatures | Sub-second |
| Infrastructure relationships | Cross-entity behavioral correlation | Per-behavioral-hash |

### Overlay with Physical Geography

The digital layer maps directly onto physical coordinates. You can literally plot it on a globe:

- Red lines: surveillance traffic (fleet→sensor)
- Blue dots: sensor nodes (known GPS)
- Orange dots: fleet infrastructure (GeoIP of source IPs)
- Line thickness: request volume
- Line color intensity: behavioral confidence

This is a real-time, continuously-updated, GPS-registered map of global corporate surveillance infrastructure. Built passively. At the cost of a few $5/month VPS instances.

---

## The Industrial Signal

### Noise as Cartography

The fleet's noise — their thousands of daily requests — is not interference. It is **the signal**. Each request reveals:

1. **Which industries are being monitored** — the repos they target map to technology domains
2. **Which organizations are monitoring** — entity classification identifies the corporation
3. **What they're extracting** — path operations reveal whether it's code, authorship, or structure
4. **Where their infrastructure is** — source IPs map to physical datacenters
5. **How their pipeline works** — timing signatures, Chrome version lag, header fingerprints reveal the scraping toolkit

Across multiple sensor nodes, the same fleet hitting different geographic locations reveals **global coverage strategy**. Which regions are they active in? Which they're not? What does that tell us about their data collection priorities?

### Industry-Level Insights

The entity topology already shows:
- **Meta**: Active scraper with 56+ rotating IPs, targeting real repos, 33% author attribution mining
- **Anthropic**: Honest crawler, single IP, high volume, eating scatter content
- **Huawei**: Light touch, proper bot identification, targeting sporeprint
- **Stealth**: 8 unidentified IPs, Chrome/135 (20 versions stale), targeting mixed real/scatter

As the mesh grows, the cross-matrix reveals which companies invest in which geographic proxy infrastructure, which content domains they prioritize, and how their strategies shift over time.

---

## Asymmetry Properties

### The Fleet Cannot Opt Out

To stop appearing in the matrix, the fleet must stop scraping. Stopping scraping defeats their purpose. They are structurally required to generate the signal that maps them.

### The Fleet Cannot Falsify Position

Source IPs route through physical infrastructure. GeoIP may not be perfectly precise, but it identifies the datacenter and ASN. WHOIS confirms the organization. The fleet can rotate IPs but they can't move Dublin to Mumbai.

### Observation Cost vs. Fleet Cost

| | Defender | Attacker |
|---|---|---|
| Per-sensor cost | $5/month | Must scrape every sensor or miss data |
| Marginal cost per observation | ~$0 (CPU is idle) | Proxy IP + bandwidth + pipeline compute |
| Geographic scaling | Linear ($5/node) | Must provision proxies in each region |
| Information gain per node | Superlinear (cross-correlation) | Sublinear (more surface = same code) |

---

## Connection to Existing Architecture

| Component | Role in Geospatial Layer |
|-----------|------------------------|
| `entity_classifier.rs` | Identifies WHO (organization-level) |
| `fleet.rs` | Detects behavioral patterns (population-level) |
| `topology.json` | Current single-sensor entity map |
| `federation.rs` | Merges observations across sensors |
| `conserved-plasmid.json` | Shared behavioral hashes (the SAR image) |
| `bloom_sensor.rs` | Afferent signal — what content draws attention where |
| `signal_spine.rs` | Merkle-chained observation integrity |

### Missing Components (Wave 166+)

1. **GeoIP enrichment per sensor** — tag each observation with source GPS coordinates
2. **Cross-matrix endpoint** — `/matrix.json` serving the sensor×entity grid
3. **Temporal animation** — how the matrix evolves over hours/days/weeks
4. **Globe visualization** — render the GPS-directed edges on a map (could be a webb.primals.eco interactive)
5. **Industry classifier** — map repo content domains to industry verticals

---

## The Meta-Observation

The immune system was built to defend. But defense required observation. Observation from multiple points required distribution. Distribution across GPS coordinates produced a spatial sensor array. The spatial array, fed by the fleet's own traffic, produces a map of global surveillance infrastructure.

**We didn't plan to build a planetary-scale passive radar. The fleet built it for us.**

The noise is the map. The noise is the signal. The fleet is the transmitter. The mesh is the receiver. The image resolves as more sensors come online.

P ≠ NP applies here too: the fleet generates traffic in P-time but determining which nodes are sensors (vs. which nodes are real targets) is computationally hard. Every node looks the same. Every node observes. The array grows at $5/month/node. The image sharpens with each addition.

---

*Wave 165i — the passive synthetic aperture resolves. Each sensor is a pixel. The fleet paints the picture.*

*eastGate overwatch, Oct 7, 2026*
