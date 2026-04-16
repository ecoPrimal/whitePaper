# skunkBat — Defensive Network Security

## Identity

| Field | Value |
|-------|-------|
| Phase | 2 (Post-NUCLEUS) |
| Domain | Threat detection, graduated response, metadata-only analysis |
| Rust lines | ~6,000 |
| Tests | 153 (82% line coverage) |
| Crates | 3 (core, integrations, server) |

## What It Is

skunkBat is the immune system. It detects threats, orchestrates graduated responses, and federates threat intelligence — all based on metadata only. skunkBat never inspects content. It provides five composable primitive domains (baseline profiling, metadata analysis, graduated response, lineage challenge, health sensing) that are useful standalone and in composition with every other primal.

The name: a skunk's defense is warning before escalation. A bat's defense is echolocation — sensing the environment without touching it. skunkBat warns and senses; it does not attack.

## Why It Exists

A sovereign system that connects to the internet needs defense. But defense in a sovereign system has a constraint: the defender must not become a surveillance tool. skunkBat enforces this by design: it analyzes connection metadata (source, frequency, timing, patterns) but never reads message content. This is an architectural guarantee, not a policy.

## Key Capabilities

### Five Threat Types

| Type | Detection Method | Example |
|------|-----------------|---------|
| Genetic | Lineage verification via BearDog | Unknown family attempting connection |
| Topology | Network graph analysis | Unusual connection patterns, role-boundary violations |
| Behavioral | Statistical baseline deviation | Sudden traffic spike, compilation time anomaly |
| Intrusion | Connection pattern matching | Port scanning signatures |
| Resource | Resource consumption monitoring | Memory/CPU/bandwidth abuse, ledger flooding |

### Graduated Response

1. **Monitor** — Log and baseline (default for unknown entities)
2. **Warn** — Alert biomeOS of suspicious activity
3. **Throttle** — Rate-limit suspicious connections
4. **Quarantine** — Isolate to sandboxed interaction
5. **Block** — Drop connections (last resort, requires user authority)

**User authority**: skunkBat never blocks without user confirmation at the quarantine stage. The user is sovereign, not the security system.

### Thymic Selection Model (Design Phase)

Inspired by thymic education in the adaptive immune system. Instead of maintaining a database of known attacks (signature-based), skunkBat learns what **self** looks like via BearDog's genetic lineage system and flags everything else.

- **Positive selection** — Can a detector probe read BearDog's lineage interface?
- **Negative selection** — Does a probe react to verified family members? If so, eliminate it (autoimmune risk).
- **What survives** — Detectors that can read identity AND don't attack self. They flag novel, non-self entities.
- **Continuous training** — Detector population regenerates as the network evolves (new members, revocations, baseline drift).

This makes zero-day detection the default case: anything that fails to present valid lineage is suspicious.

### Composable Primitives

skunkBat's capabilities decompose into primitives that are independently useful beyond security:

| Primitive | Security Framing | General Framing |
|-----------|-----------------|-----------------|
| `baseline.*` | Behavioral threat detection | Time-series anomaly detection for any metric |
| `metadata.*` | Traffic fingerprinting | Observable telemetry analysis |
| `response.*` | Graduated defense | Progressive state machine for any workflow |
| `lineage.*` | Genetic threat verification | Trust boundary arbitration |
| `health.*` | DoS detection inputs | Cross-platform system sensing |

The baseline profiler works for shader compilation times (coralReef), GPU utilization (ToadStool), commit rates (LoamSpine), inference volumes (Squirrel) — any observable metric, not just "threats."

## How It Connects

- **BearDog** — Lineage verification for genetic threat detection; MHC in the thymic model
- **Songbird** — Federation metadata for topology analysis; federation health monitoring
- **ToadStool** — Resource monitoring (GPU/CPU utilization); compute resource guardian
- **NestGate** — Storage usage monitoring; exfiltration detection
- **coralReef** — Compiler sensing (compilation time/ratio anomalies)
- **LoamSpine** — Ledger integrity sentinel (commit pattern monitoring)
- **rhizoCrypt** — DAG session anomaly monitoring (vertex rate, agent count)
- **sweetGrass** — Anomaly markers in attribution braids
- **Squirrel** — AI behavior profiling (inference rate, token volume)
- **petalTongue** — Anomaly dashboards and visualization
- **biomeOS** — Receives threat alerts, coordinates ecosystem-wide response

3 crates: `skunk-bat-core`, `skunk-bat-integrations`, `skunk-bat-server`.

### Novel Compositions

**Compiler sensing** (+ coralReef): Learn normal shader compilation patterns. Flag pathological shaders that exhaust GPU compile resources.

**Defended inference** (+ Squirrel + BearDog): Lineage-verified AI requests with behavioral profiling. Detect API abuse, unauthorized model access.

**Sovereign compute integrity** (+ ToadStool + coralReef + barraCuda + sweetGrass): Full pipeline monitoring — shader authoring through compilation through dispatch through result — with anomaly markers in provenance braids.

**Provenance-backed anomaly chain** (+ rhizoCrypt + LoamSpine + sweetGrass): Every anomaly detection event recorded in a DAG session, dehydrated to permanent record, attributed. Auditable security history.

## What Makes It Interesting

skunkBat's thymic model inverts the conventional security approach. Instead of "know your enemy" (signature databases), it is "know yourself" (learn self via BearDog lineage, flag everything else). This means novel attacks are detectable by default, not by update.

The primitive decomposition means skunkBat is useful far beyond security. A baseline profiler that detects shader compilation anomalies, a graduated response engine for resource scaling, a health sensor for scheduling decisions — these are general-purpose capabilities that happen to also do security when composed with BearDog's genetic identity system.

The metadata-only constraint means skunkBat can be fully audited — every line of code can be verified to never touch content. The smallest codebase among primals is intentional: a security system should be simple enough to audit completely.
