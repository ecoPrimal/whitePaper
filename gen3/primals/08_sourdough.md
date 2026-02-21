# sourDough — Starter Culture / Primal Scaffolding

## Identity

| Field | Value |
|-------|-------|
| Phase | 2 (Post-NUCLEUS) |
| Domain | Primal scaffolding, core traits, genomeBin |
| Rust lines | 50,746 |
| Tests | 3,622 |

## What It Is

sourDough is the starter culture. It defines the core traits that every primal must implement and provides scaffolding to create new primals:

```
sourdough scaffold new-primal --name myPrimal
```

### Core Traits

| Trait | Purpose |
|-------|---------|
| `PrimalLifecycle` | Start, stop, health check |
| `PrimalHealth` | Readiness, liveness probes |
| `PrimalIdentity` | Name, version, capabilities |
| `PrimalDiscovery` | Registration with Songbird/biomeOS |
| `PrimalConfig` | Configuration loading and validation |

## Why It Exists

By primal #8, the pattern for creating a new primal was clear: implement JSON-RPC, register with Songbird, expose capabilities, handle health checks. Rather than copy-paste this boilerplate into each new primal, sourDough codifies it.

The name: a sourdough starter is a living culture you use to begin new bread. sourDough is the living culture you use to begin new primals.

## How It Connects

sourDough doesn't run as a service. It's a library crate and CLI tool. New primals depend on `sourdough-core` for trait definitions. The scaffolding generates a properly structured primal with BearDog integration (identity), Songbird integration (discovery), and the Universal Adapter pattern.

## What Makes It Interesting

sourDough is ecoBin #3 — the third binary certified as a proper ecoPrimals citizen. It also generates genomeBin packages: deployment-ready primal binaries with system detection, service integration, and health validation built in.
