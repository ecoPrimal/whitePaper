# skunkBat — Defensive Network Security

## Identity

| Field | Value |
|-------|-------|
| Phase | 2 (Post-NUCLEUS) |
| Domain | Threat detection, graduated response, metadata-only analysis |
| Rust lines | 7,366 |
| Tests | 48 |
| Crates | 2 |

## What It Is

skunkBat is the immune system. Threat detection across five categories, graduated response from monitoring through quarantine to blocking, statistical baseline analysis. All based on metadata only — skunkBat never inspects content.

The name: a skunk's defense is warning before escalation. A bat's defense is echolocation — sensing the environment without touching it. skunkBat warns and senses; it does not attack.

## Why It Exists

A sovereign system that connects to the internet needs defense. But defense in a sovereign system has a constraint: the defender must not become a surveillance tool. skunkBat enforces this by design: it analyzes connection metadata (source, frequency, timing, patterns) but never reads message content.

## Key Capabilities

### Five Threat Types

| Type | Detection Method | Example |
|------|-----------------|---------|
| Genetic | Lineage verification via BearDog | Unknown family attempting connection |
| Topology | Network graph analysis | Unusual connection patterns |
| Behavioral | Statistical baseline deviation | Sudden traffic spike |
| Intrusion | Connection pattern matching | Port scanning signatures |
| Resource | Resource consumption monitoring | Memory/CPU/bandwidth abuse |

### Graduated Response

1. **Monitor** — Log and baseline (default for unknown entities)
2. **Warn** — Alert biomeOS of suspicious activity
3. **Throttle** — Rate-limit suspicious connections
4. **Quarantine** — Isolate to sandboxed interaction
5. **Block** — Drop connections (last resort)

**User authority**: skunkBat never blocks without user confirmation at the quarantine stage. The user is sovereign, not the security system.

## How It Connects

- **BearDog** — Lineage verification for genetic threat detection
- **Songbird** — Federation metadata for topology analysis
- **ToadStool** — Resource monitoring (GPU/CPU utilization)
- **NestGate** — Storage usage monitoring
- **biomeOS** — Receives threat alerts, coordinates response

2 crates: `skunk-bat-core`, `skunk-bat-integrations`.

## What Makes It Interesting

skunkBat is the smallest primal (7,366 lines, 48 tests). Its small size is intentional: a security system should be simple enough to audit completely. The metadata-only constraint means skunkBat can be fully reviewed — every line of code can be verified to never touch content.

The "user authority" principle means skunkBat cannot escalate to blocking autonomously. This prevents the security system from becoming an autonomous censor — a common failure mode in corporate security products.
