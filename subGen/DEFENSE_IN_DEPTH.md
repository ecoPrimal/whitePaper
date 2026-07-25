# Defense in Depth — Realized Security Architecture

**Status**: Living document — reflects deployed primal implementations
**Primals**: skunkBat (detection), bearDog (crypto), songBird (transport),
cellMembrane (orchestration), nestGate (content boundary)

---

## Doctrine

Security is not a feature — it is a property that emerges from independent,
composable layers. No single layer is trusted to be sufficient. Each layer
enforces its own invariant. Compromise of any one layer does not grant access
to the next.

This is the gram-negative membrane model applied to software: multiple
independent barriers with different enforcement mechanisms, different failure
modes, and no shared state between them.

---

## The Seven Layers

### Layer 0 — Network Binding

**Enforcer**: Every primal binary (via `PRIMAL_BIND_MODE`)
**Invariant**: Production services bind to `127.0.0.1` by default

The first layer is the simplest: don't listen on the network unless explicitly
configured. Every primal reads `PRIMAL_BIND_MODE` at startup:

| Mode | Binding | Use Case |
|------|---------|----------|
| `uds_and_tcp` | Unix socket + `127.0.0.1:PORT` | Default (LAN gate) |
| `tcp_only` | `127.0.0.1:PORT` only | Android/SELinux (no UDS) |
| `tcp_public` | `0.0.0.0:PORT` | Explicit external exposure |

No primal binds publicly without an explicit, auditable configuration change.
This is the "no listening ports" default that WireGuard pioneered, applied at
the application layer.

### Layer 1 — Transport Encryption (BTSP)

**Enforcer**: bearDog (key material) + skunkBat/songBird (negotiation)
**Invariant**: Non-null traffic is authenticated and encrypted

BTSP (Bio-Transport Security Protocol) provides three phases:

1. **Phase 1**: TCP/UDS connection + protocol peek (plaintext probe detection)
2. **Phase 2**: Handshake — mutual identity verification via bearDog
3. **Phase 3**: Cipher negotiation — ChaCha20-Poly1305 AEAD with HKDF-SHA256
   derived directional keys

The cipher floor policy prevents downgrade: a server-configured minimum
(`SKUNKBAT_CIPHER_FLOOR`) rejects connections that can't meet the floor,
independent of what the client offers. Bond types (Covalent/Metallic/Ionic)
provide application-level minimum requirements on top of the floor.

See: [TOWER_ATOMIC_SECURITY.md](TOWER_ATOMIC_SECURITY.md)

### Layer 2 — RPC Authorization (MethodGate)

**Enforcer**: Every primal with a JSON-RPC surface
**Invariant**: Protected methods require a capability token

MethodGate classifies every JSON-RPC method before it reaches the dispatch
table:

- **Public**: `health.*`, `btsp.*`, `identity.get`, `capabilities.list`,
  `lifecycle.*`, `auth.*`, `method_gate.status`, `baseline.query`,
  `baseline.anomaly`, `security.advisory`
- **Protected**: Everything else — `defense.quarantine`, `security.scan`,
  `baseline.observe`, `baseline.reset`, `response.evaluate`, etc.

Two modes:
- **Permissive** (default): Protected calls are logged but allowed. For
  bootstrapping and development.
- **Enforced**: Protected calls without a valid BTSP session token are
  rejected with `PERMISSION_DENIED` (-32001).

The public surface is deliberately minimal: health probes and capability
advertisement. Anything that mutates state or reveals security-sensitive
data is protected.

### Layer 3 — Threat Detection (skunkBat)

**Enforcer**: skunkBat threat detection engine
**Invariant**: Anomalous behavior is detected and classified

Seven independent detection categories, each with its own statistical model:

| Category | Signal | Detection Method |
|----------|--------|------------------|
| Behavioral anomaly | Connection rate, traffic volume, port distribution | Rolling-window σ-deviation |
| Intrusion attempt | Attack signatures, brute force patterns | Pattern + rate correlation |
| Denial of service | Resource exhaustion indicators | Threshold + rate of change |
| Unknown lineage | Unverified peer identity | Genetic verification failure |
| Topology violation | Layer-hopping, path bypass | Expected vs. actual path |
| Configuration drift | Runtime config mutation | Startup snapshot diff |
| Process spawn anomaly | System-wide fork rate | `/proc/stat` rate tracking |
| HTTP anomaly | Request rate, path diversity, error rates | Outer membrane baseline |

Each detection produces a `Threat` with severity (Low/Medium/High/Critical)
and confidence (0.0–1.0). Thresholds are environment-configurable, never
hardcoded — the code defines the detection *mechanism*, not the deployment-
specific trigger points.

See: [THREAT_DETECTION_ARCHITECTURE.md](THREAT_DETECTION_ARCHITECTURE.md)

### Layer 4 — Behavioral Baseline

**Enforcer**: skunkBat baseline profiler
**Invariant**: Deviations from established norms are flagged

The baseline profiler maintains rolling-window statistics (mean, standard
deviation) across multiple dimensions:

- **Inner membrane**: Connection rate, traffic volume, port diversity
- **Outer membrane**: HTTP request rate, path diversity, 4xx/5xx error rates,
  payload sizes, method diversity

Observations are fed via `baseline.observe` (inner: IPC telemetry from
skunky-ingest/Caddy logs; outer: Tower HTTP Gateway). Anomalies are detected
when any dimension exceeds `sigma_threshold` standard deviations from mean.

The profiler has no opinion about what constitutes an attack — it identifies
*statistical deviation*. The threat detector interprets deviations as threats.

### Layer 5 — Graduated Response

**Enforcer**: skunkBat defense subsystem
**Invariant**: Response is proportional to threat severity

Detected threats produce structured responses through the `response.evaluate`
composable primitive:

| Severity | Response |
|----------|----------|
| Low | Log + advisory (inform gateway) |
| Medium | Rate limit advisory + audit trail |
| High | Quarantine (IP isolation) + alert |
| Critical | Quarantine + immediate audit + alert escalation |

Quarantine is reversible (`defense.release`). The defense subsystem maintains
quarantine state and provides `defense.status` for introspection.

### Layer 6 — Audit Trail

**Enforcer**: skunkBat observability subsystem
**Invariant**: All security-relevant events are recorded immutably

Every threat detection, response action, and configuration change is written
to the audit log via `security.audit_log`. The audit trail provides:

- Forensic reconstruction of security events
- Compliance evidence for the `darkforest` validation suite
- Input for behavioral baseline calibration
- Correlation data for cross-gate security analysis

---

## Layer Independence

Critical design property: **no layer depends on another layer functioning
correctly**.

- If BTSP is bypassed (plaintext connection), MethodGate still enforces
  authorization.
- If MethodGate is in permissive mode, threat detection still fires on
  anomalous patterns.
- If threat detection misses an attack, the behavioral baseline still
  flags deviations.
- If the baseline is polluted, the audit trail still records events for
  forensic review.

This is defense in depth: the system degrades gracefully, and compromise
of a single layer does not cascade.

---

## Dark Forest Validation

The defense-in-depth posture is validated by the `darkforest` scenario suite
in primalSpring:

- **197 scenarios**, all PASS
- 5 invariant categories: identity, isolation, provenance, sovereignty,
  reversibility
- Tested against real attacker data (122 SSH brute-force + HTTP scanning IPs)
- Cross-gate validation on live mesh

The validation suite is not part of skunkBat — it is an independent primal
(primalSpring) that tests the ecosystem's security posture from the outside.
This separation ensures the test is not biased by the implementation.

---

*subGen Wave 150x — Defense in depth as realized across 7 layers,
validated by 197 scenarios.*
