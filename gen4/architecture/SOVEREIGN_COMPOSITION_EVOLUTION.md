# Sovereign Composition Evolution — From Shipped Primals to Self-Hosted Safety

**Date**: May 15, 2026
**Status**: Active evolution
**Lineage**: gen3 constrained evolution → gen4 stadial/interstadial → sovereignty

---

## The Three Questions

gen3 asked: "Does it work?" (validated by 12,510+ checks across 8 springs)

gen4 asked: "Who uses it?" (answered by esotericWebb, helixVision, lithoSpore)

The sovereignty evolution asks a third question:

> **"Can it sustain itself?"**

A system that works but depends on Cloudflare for TLS, GitHub for code
hosting, and Anthropic for AI is not self-sustaining. It is a tenant on
someone else's infrastructure. The primals are sovereign organisms in
theory — 100% Rust, zero C deps, BTSP authenticated — but in practice
they communicate through rented channels.

The sovereignty evolution is the systematic replacement of those rented
channels with owned channels. The end state is a system that answers
all three questions: it works, people use it, and it sustains itself.

---

## The Layer Model

The insight that makes this tractable: primal capabilities and sovereignty
deployment are **different layers** with well-defined interfaces between
them. Confusing them is the primary source of wasted effort.

### Layer 1: Primal Capabilities (upstream)

Each primal ships capabilities in Rust through primalSpring. These
capabilities exist independently of any deployment. BearDog's TLS
termination works whether it's deployed on a VPS, a Raspberry Pi, or
never deployed at all. The capability is the unit of primal evolution.

**Validation**: primalSpring scenarios (27 scenarios, 77 graphs, 427
methods, 13/13 MethodGate enforced).

**Current state**: COMPLETE. Zero open upstream gaps. All 13 primals at
zero code debt. The Rust is shipped.

### Layer 2: Security Validation (cross-cutting)

Security is not a layer you build — it's a gate you pass through.
Every change at Layer 1 (new capability) and Layer 3 (new deployment)
must pass Layer 2 before it's considered valid.

**Validation**: darkforest v0.2.1 (Rust — 8 modules, zero runtime deps),
`security_validation.sh` (5-layer pen test), `dark_forest_gate_local.sh`
(33-check structural validation), `darkforest_membrane.sh` (15-check VPS
audit).

**Current state**: COMPLETE. Horizon 1 fully resolved. 267+ PASS, 0 FAIL
at gate. 17 PASS, 0 FAIL at membrane. Dark Forest Glacial Gate PASS.

**Key principle**: Security validation is **mostly in Rust**. darkforest
is the authoritative validator — bash scripts orchestrate it, they don't
implement security logic. This matters because Rust gives us:
- Compiled binary — no runtime dependency injection
- Zero C deps — no hidden attack surface
- Structured output — JSON reports for auditable evidence
- Environment-agnostic — runs identically on any gate

### Layer 3: Sovereignty Deployment (downstream)

This is where primal capabilities replace external services. The work is
deployment, configuration, monitoring, and parity validation — not new
Rust code. The Rust is already shipped (Layer 1). The security is already
validated (Layer 2). Layer 3 is the ops.

**Validation**: benchScale parity scenarios (shadow runs, baseline
comparisons, 7-day metrics).

**Current state**: IN PROGRESS. Four sovereign parallels running. Two
active. Four not started.

### Layer 3+4: The Membrane Bridge (continuous telemetry)

Layer 3 (external membrane / VPS) and Layer 4 (internal membrane / gate)
are two faces of the same cell membrane. The critical design decision:
**shadow data collection is permanent, not a pre-cutover phase**.

The calibrate-shadow-cutover protocol defines the gate for replacing an
external service. But even after cutover, telemetry continues because:

- Regressions can emerge after primal updates (BearDog TLS p95 drifts)
- External baselines shift (Cloudflare edge routing changes)
- Cost patterns change (VPS bandwidth, gate CPU, relay load)
- Composition interactions produce emergent latency profiles

The implementation is a unified telemetry pipeline:
- `deploy/membrane_telemetry.sh` probes both membranes every 15 minutes
- `deploy/membrane_summary.sh` produces a rolling 7-day `membrane_7day.toml`
- `routing_config.toml [telemetry]` formalizes `shadow_mode = "permanent"`
- SkunkBat audit events correlate with telemetry probes for Layer 2 validation
- The shadow run orchestrator reads unified baselines instead of per-channel files

This makes the "shadow" phase a permanent health signal rather than a
pre-cutover test. The organism keeps sensing its environment even after
it no longer depends on external services — exactly as a biological cell
continues monitoring its membrane even when all internal protein
synthesis is operational.

### Layer 4: Sovereign Composition (convergence)

The end state: all layers compose into a self-sustaining system. Not
individual primal capabilities running alongside external services, but
primal **compositions** that replace entire service clusters.

The Tower atomic (BearDog + Songbird + SkunkBat) replaces Cloudflare
(TLS + tunnel + DDoS). The Nest atomic (NestGate + rhizoCrypt + loamSpine
+ sweetGrass) replaces GitHub (repos + releases + pages + CI). Full
NUCLEUS replaces the entire external stack.

**Validation**: End-to-end integration test with zero external
dependencies, plus continuous membrane telemetry that persists beyond
cutover as a permanent health signal.

**Current state**: EARLY. Tower on VPS without biomeOS. Full NUCLEUS on
gate with external dependencies. Continuous telemetry pipeline deployed.

---

## Where Primal Goals and Sovereignty Goals Diverge

### Pure Primal Goals (no sovereignty implication)

These advance the ecosystem's computational capabilities but don't
directly replace any external service:

- **barraCuda WGSL shader compilation**: Advances GPU compute. Does not
  replace any external service (Anthropic/OpenAI replacement is through
  Ollama + local models, not WGSL shaders directly).

- **coralReef FECS stability proofs**: Validates floating-point
  determinism. Important for science reproducibility, irrelevant to
  sovereignty.

- **loamSpine ledger mechanics**: The internal commit model for
  provenance. sweetGrass braids witness sovereignty events, but
  loamSpine's ledger structure is a primal-internal concern.

- **ToadStool workload dispatch**: How workloads are scheduled is a
  compute concern. Sovereignty doesn't change the dispatch model.

- **Squirrel AI routing**: Which AI backend Squirrel calls is a
  capability concern. The sovereignty implication (Ollama vs Anthropic)
  is a configuration choice, not a Squirrel capability gap.

### Pure Sovereignty Goals (no primal capability needed)

These are operational work that doesn't require any new Rust code:

- **Forgejo adoption**: Install Forgejo, mirror repos, configure
  dual-push. Zero Rust. Pure git server administration.

- **GitHub Actions migration**: Port 74 YAML workflow files to Forgejo
  Actions. The workflows call `cargo test` — the Rust is already there.

- **VPS provisioning**: `doctl`, systemd units, UFW rules, tmpfiles.d
  configuration. Infrastructure ops.

- **DNS grey-clouding**: Point A records directly to VPS IP. A DNS
  registrar operation.

- **Credential rotation**: SSH key management, cookie secret rotation.
  Ops discipline, not code.

### The Overlaps (primal capability directly enables sovereignty)

These are the high-value convergence points where shipping one Rust
capability advances the sovereignty timeline:

| Overlap | What Rust Ships | What Ops Deploys |
|---------|----------------|-----------------|
| TLS sovereignty | BearDog: rustls X.509 + SNI + ACME + rate limiter | VPS shadow on :8443, 7-day parity, DNS grey-cloud, cutover |
| NAT sovereignty | Songbird: STUN + TURN + fallback chain | VPS relay on :3478, HTTP parity test, cloudflared removal |
| Auth sovereignty | BearDog: ionic tokens + `auth.issue_session` | JupyterHub BTSPAuthenticator, dual-auth shadow, PAM removal |
| Content sovereignty | NestGate: `content.*` pipeline | VPS cache, petalTongue web mode, GitHub Pages removal |
| Credential sovereignty | BearDog: AES-256-GCM vault | VPS `credentials.age`, TURN credential encryption |

---

## The Rust Thread

The user's priority order is explicit:
1. Stability / Security
2. Sovereign solutions
3. **Rust**
4. Primal composition

Rust is third — after security and sovereignty, but before composition.
This means:

### What Should Be in Rust

- **All security validation**: darkforest is Rust. This is non-negotiable.
  Security logic must be compiled, auditable, and dependency-free.

- **All primal capabilities**: Every primal is 100% Rust. This is the
  ecosystem's foundational constraint. No C deps, no Go, no Python for
  primal internals.

- **Validation binaries**: lithoSpore modules, tunnelKeeper, darkforest.
  These are the tools that prove the system works. They must be as
  trustworthy as the system they validate.

### What Can Be Bash/Python (for now)

- **Deployment scripts**: `deploy.sh`, `forgejo_mirror.sh`,
  `vps_resize.sh`. These are orchestration — they call Rust binaries,
  they don't implement logic. They'll evolve to Rust when biomeOS
  absorbs their functionality.

- **pappusCast**: Currently Python (953L, 7 modules). Evolution path is
  Python → Rust binary → pappusCast primal. The Python works today;
  the Rust version is a Layer 1 primal goal.

- **benchScale scenarios**: Bash scripts that call `curl` and `ssh`.
  These are measurement tools, not security tools. They measure parity;
  darkforest validates security.

- **Membrane telemetry**: `membrane_telemetry.sh` and `membrane_summary.sh`
  collect and summarize shadow data. They're cron-driven probes that
  output TOML — readable by future Rust tooling when the summary evolves.

### What Must Evolve to Rust

| Current | Target | Priority | Reason |
|---------|--------|----------|--------|
| Caddy (Go) on VPS | Songbird TLS (Rust) | High | Transitional proxy → sovereign primal |
| pappusCast (Python) | pappusCast primal (Rust) | Medium | Content propagation should be a primal |
| `darkforest_membrane.sh` (bash) | darkforest `--suite membrane` (Rust) | Medium | Security validation should be compiled |
| `deploy.sh` (bash) | biomeOS `composition.deploy` (Rust) | Medium | Deployment should be graph-driven |
| knot-dns (C) on VPS | Songbird DNS capability (Rust) | Long-term | DNS resolution as primal capability |

---

## The Final Evolution: Sovereign Self-Hosted Safe Primal Compositions

The title says it all. Each word is a constraint:

- **Sovereign**: No external service dependency. Owned infrastructure.
- **Self-hosted**: Running on gate hardware or VPS we control.
- **Safe**: Validated by darkforest, Dark Forest gate, membrane audit.
- **Primal**: Built from primal capabilities, not monoliths.
- **Compositions**: Assembled from deploy graphs, not hardcoded scripts.

When all five constraints are satisfied simultaneously, the system is
complete. Not "done" — systems are never done — but complete in the sense
that it can sustain itself without external life support.

The biological analogy is precise: a cell that can synthesize its own
proteins, maintain its own membrane, replicate its own DNA, and respond
to its environment is a living cell. A cell that depends on external
protein sources, borrowed membranes, and cloud-hosted DNA is a
laboratory construct. We're building a living cell.

```
Current:  Gate (sovereign) + Cloudflare (rented) + GitHub (rented)
                = laboratory construct

Target:   Gate (sovereign) + VPS membrane (owned) + Forgejo (owned)
                = living cell

Final:    Gate mesh (sovereign) + VPS mesh (owned) + biomeOS (orchestrated)
                = organism
```

---

## Relationship to Other Documents

| Document | Scope |
|----------|-------|
| `PRIMAL_VS_SOVEREIGNTY_GOALS.md` (wateringHole) | The operational tracking: which goals are primal, which are sovereignty, current status |
| `NUCLEUS_SOVEREIGNTY_ARCHITECTURE.md` | The deployment architecture: what's live, what's validated, what remains |
| `CELLMEMBRANE_FIELDMOUSE_ARCHITECTURE.md` | The VPS deployment model: Tower composition, channels, security |
| `SOVEREIGNTY_STANDARDS.md` (wateringHole) | The ecosystem standards: bonding model, routing, credentials |
| `STADIAL_INTERSTADIAL_PATTERN.md` | The evolution framework: glacial cycles drive convergence |
| `TUNNEL_EVOLUTION.md` (projectNUCLEUS) | The step-by-step replacement roadmap |
| `COMPLETE_DEPENDENCY_INVENTORY.md` (projectNUCLEUS) | The 40+ dependency map across 7 clusters |
| `routing_config.toml [telemetry]` (projectNUCLEUS) | Permanent shadow mode configuration for SkunkBat correlation |
| `membrane_7day.toml` (projectNUCLEUS) | Canonical membrane state snapshot — the L3+L4 health summary |
