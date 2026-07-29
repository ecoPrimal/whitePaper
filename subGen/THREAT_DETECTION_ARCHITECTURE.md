# Threat Detection Architecture — skunkBat

**Status**: Living document — reflects deployed detection engine
**Primal**: skunkBat 0.2.18
**Categories**: 8 (7 inner membrane + 1 outer membrane)
**Tests**: 586, all pass

---

## Design Philosophy

skunkBat detects threats through **metadata analysis only**. It never
inspects payload content — it observes connection patterns, rates,
identity claims, configuration state, and system metrics. This is a
deliberate constraint:

1. **Privacy**: No deep packet inspection, no content logging
2. **Performance**: Metadata analysis is O(1) per observation, not O(n)
   on payload size
3. **Composability**: Any system that can emit structured observations
   can feed skunkBat's baseline, regardless of the underlying protocol

The detection engine separates three concerns:
- **Observation**: Raw telemetry collection (rates, counts, distributions)
- **Baseline**: Statistical profiling (rolling-window mean/σ)
- **Detection**: Threat classification (deviation → threat type → severity)

---

## Detection Categories

### 1. Behavioral Anomaly

**Signal**: Connection rate, traffic volume, port diversity
**Method**: Rolling-window σ-deviation from baseline
**Trigger**: Any dimension exceeds `sigma_threshold` standard deviations
**Confidence**: Based on observation window depth and deviation magnitude

The baseline profiler maintains per-dimension statistics (`DimensionStats`:
mean + standard deviation) over a configurable rolling window. New
observations update the window. When any dimension's current value exceeds
`mean ± (sigma_threshold × std_dev)`, an anomaly is flagged.

This is the most general detector — it catches any sustained deviation
from established norms without requiring specific attack signatures.

### 2. Intrusion Attempt

**Signal**: Attack type + signature patterns
**Method**: Pattern matching + rate correlation
**Trigger**: Known attack signatures (brute force, scanning) at elevated rates

Detects active intrusion attempts by combining signature recognition with
rate analysis. A single SSH login failure is noise. 50 failures per minute
from the same source is a brute-force attack. The detector correlates
pattern matches with temporal density.

Fed with real attacker data: 122 SSH brute-force and HTTP scanning IPs
from live gate logs (Wave 137b THREAT-ACTIVATE).

### 3. Denial of Service

**Signal**: Resource exhaustion indicators
**Method**: Threshold + rate of change
**Trigger**: Resource usage exceeds `dos_load_threshold` with sustained
rate of increase

Monitors resource consumption dimensions (CPU load, connection count,
memory pressure) and flags when usage crosses the configured threshold
*and* the rate of increase suggests intentional exhaustion rather than
organic load.

### 4. Unknown Lineage (Genetic Threat)

**Signal**: Peer identity verification failure
**Method**: bearDog lineage verification via `lineage.verify` RPC
**Trigger**: Peer fails genetic verification with confidence above
`genetic_confidence` threshold

When a peer connects and claims identity, skunkBat delegates verification
to whatever primal announces the `lineage-verification` capability
(typically bearDog). Verification failure — peer is "not family" — produces
an `UnknownLineage` threat.

Graceful degradation: when no lineage provider is available, unknown peers
are conservatively treated as unverified. The system doesn't panic — it
assumes the worst and logs accordingly.

### 5. Topology Violation

**Signal**: Layer path traversal
**Method**: Expected path comparison
**Trigger**: Actual path differs from configured `expected_topology_path`

The K-Derm membrane model defines expected traffic paths through membrane
layers. A connection that bypasses a layer (e.g., reaching the inner
membrane without traversing the periplasmic space) indicates either
misconfiguration or an attack attempting to circumvent outer defenses.

Detected by comparing the `actual_path` (sequence of layers traversed)
against the `expected_path` (configured per deployment topology).

### 6. Configuration Drift

**Signal**: Runtime configuration mutation
**Method**: Startup snapshot comparison
**Trigger**: Any security-relevant config field changes without a
corresponding config-reload IPC call

At startup, skunkBat captures a `ConfigSnapshot` of security-relevant
fields:
- Feature flag states (JSON-serialized for stable comparison)
- Lineage ID binding
- Topology validation state
- Detection threshold fingerprint

On each detection cycle, the current config is compared against the
snapshot. Any change that wasn't explicitly triggered by a config-reload
IPC call is flagged as `ConfigurationDrift` — potential indicator of
runtime tampering.

### 7. Process Spawn Anomaly

**Signal**: System-wide process fork rate
**Method**: `/proc/stat` sampling + rate calculation
**Trigger**: Fork rate exceeds `spawn_rate_threshold` (default: 50/sec)

Added in response to Wave 150x crash-loop divergence, where systemd's
`Restart=always` on broken services caused 11,161 restarts, consuming
resources and masking real failures.

The `SpawnRateTracker` reads `processes` count from `/proc/stat` at
intervals, computes the rate, and fires when the rate exceeds the
threshold. This catches crash loops, fork bombs, and runaway service
restarts at the OS level.

Platform-aware: returns 0.0 on non-Linux systems (where `/proc/stat`
doesn't exist), degrading gracefully rather than failing.

### 8. HTTP Anomaly (Outer Membrane)

**Signal**: HTTP request rate, path diversity, error rates, payload sizes,
method diversity
**Method**: Outer membrane baseline σ-deviation
**Trigger**: Any HTTP dimension exceeds baseline threshold

Extension of the behavioral anomaly detector to HTTP-specific telemetry,
fed by the Tower HTTP Gateway via `baseline.observe` with `HttpObservation`
data:

| Dimension | What It Catches |
|-----------|----------------|
| `request_rate` | Volumetric attacks, scraping |
| `path_diversity` | Directory traversal scanning |
| `error_rate_4xx` | Credential stuffing, path probing |
| `error_rate_5xx` | Triggered crash attacks |
| `avg_payload_bytes` | Payload-based attacks |
| `method_diversity` | Method probing (PUT/DELETE/PATCH) |

This category bridges inner and outer membrane security: external HTTP
traffic is analyzed by the same statistical engine that monitors internal
IPC patterns.

---

## Threat Data Model

Every detection produces a `Threat` struct:

| Field | Type | Purpose |
|-------|------|---------|
| `id` | String | Unique identifier for correlation |
| `threat_type` | ThreatType | Category enum (variants above) |
| `severity` | Severity | Low / Medium / High / Critical |
| `source` | String | Origin address or identifier |
| `target` | String | Target address or resource |
| `detected_at` | SystemTime | Detection timestamp |
| `description` | String | Human-readable description |
| `confidence` | f64 | Detection confidence (0.0–1.0) |

Severity is ordered: `Low < Medium < High < Critical`. This ordering is
used in graduated response selection.

---

## Threshold Configuration

All detection thresholds are environment-configurable:

| Variable | Default | Controls |
|----------|---------|----------|
| `SKUNKBAT_SIGMA_THRESHOLD` | 2.5 | Behavioral anomaly σ-deviation |
| `SKUNKBAT_DOS_THRESHOLD` | 0.8 | DoS resource exhaustion level |
| `SKUNKBAT_GENETIC_CONFIDENCE` | 0.7 | Lineage verification confidence |
| `SKUNKBAT_SPAWN_RATE_THRESHOLD` | 50.0 | Process fork rate (per second) |
| `SKUNKBAT_CIPHER_FLOOR` | (none) | Minimum cipher suite |

No threshold is compiled into the binary as a constant. The code defines
the detection *mechanism*; the operator defines the trigger points. This
separation ensures that:

1. Source code inspection cannot reveal deployment-specific thresholds
2. Thresholds can be tuned per-gate without recompilation
3. Different deployment topologies (LAN vs VPS) can have different
   sensitivity profiles

---

## Observation Pipeline

```
                    ┌─────────────┐
  Caddy logs ──────►│skunky-ingest│──► baseline.observe (inner)
                    └─────────────┘
                    ┌─────────────┐
  Tower HTTP GW ───►│ HTTP obs    │──► baseline.observe (outer)
                    └─────────────┘
                    ┌─────────────┐
  /proc/stat ──────►│SpawnTracker │──► detect_spawn_anomalies
                    └─────────────┘
                           │
                    ┌──────▼──────┐
                    │  Baseline   │ Rolling-window statistics
                    │  Profiler   │ (mean, σ per dimension)
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Threat    │ Category classification
                    │  Detector   │ (severity, confidence)
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         ┌────────┐  ┌─────────┐  ┌────────┐
         │Response│  │  Audit  │  │Advisory│
         │Evaluate│  │  Trail  │  │(Gateway│
         └────────┘  └─────────┘  │ inform)│
                                  └────────┘
```

The pipeline is unidirectional: observations flow in, threats flow out.
No component in the pipeline can modify observations or suppress threats.
The audit trail records everything regardless of response decisions.

---

---

## Wave 155i Updates

- **9th threat category**: `ConnectivityAnomaly` added — detects network fabric
  degradation (correlates with K-Derm peptidoglycan failures, NAT rate-limit
  collapses, dead dnsmasq). Outer→inner correlation.
- **Real attacker data expanded**: 122 SSH brute-force + HTTP scanning IPs
  from live gate logs (Wave 137b THREAT-ACTIVATE) — baseline calibrated against
  production traffic.
- **Process spawn tracker validated**: The Wave 150x crash-loop incident (11,161
  systemd restarts) was the event that motivated `SpawnRateTracker`. Now validated
  in production: catches crash loops, fork bombs, and runaway service restarts.
- **Platform degradation**: Windows returns 0.0 for `/proc/stat` (as designed).
  blueGate Tower 3/3 on Windows — skunkBat operates in degraded mode without
  spawn-rate monitoring. Accepted trade-off.
- **Composition broker telemetry**: biomeOS v4.45 feeds `baseline.observe` with
  composition-level events (capability registration, signal graph dispatch,
  BTSP session propagation). New observation dimensions for inner membrane
  profiling.

*subGen Wave 155i — 9-category detection. Metadata-only. ConnectivityAnomaly
added. Spawn tracker production-validated. Composition broker telemetry live.
Windows graceful degradation.*
