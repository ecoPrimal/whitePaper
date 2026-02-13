# UniBin - Technical Specification

**Category**: Architecture Standard  
**Status**: Active Ecosystem Standard  
**Version**: 1.0.0  
**Adopted**: January 16, 2026

---

## Abstract

UniBin defines the binary structure standard for every primal in the ecoPrimals ecosystem. The core principle is one binary per primal, with multiple operational modes accessed via subcommands. This eliminates binary naming fragility, deployment ambiguity, and variant proliferation - replacing them with a single, self-documenting executable per primal.

---

## Problem Statement

Without a structural standard, primal binaries proliferate into variants: `beardog-server`, `beardog-client`, `beardog-daemon`. Each variant requires its own build target, deployment path, and documentation. Deployment graphs become fragile because they reference specific binary names rather than capabilities. Operators must learn different naming conventions per primal.

This creates compounding maintenance burden as the ecosystem grows.

---

## Specification

### Binary Naming

Every primal produces exactly one executable binary named after itself:

- `beardog` (not `beardog-server`)
- `songbird` (not `songbird-orchestrator`)
- `nestgate` (not `nestgate-daemon`)

No suffixes, no variants, no exceptions.

### Subcommand Architecture

The single binary accepts subcommands to select operational mode:

```
<primal> <subcommand> [options]
```

Required subcommands:
- At least one operational mode (typically `server` or `service`)
- `--help` providing complete usage documentation
- `--version` displaying version information

Standard subcommand names across the ecosystem:
- `server` - long-running service mode
- `client` - interactive client mode
- `doctor` - health diagnostics
- `daemon` - background execution

Primal-specific subcommands are encouraged for domain operations.

### CLI Requirements

Every UniBin provides:
- Comprehensive `--help` output listing all subcommands with descriptions
- `--version` flag with at minimum `<primal> <semver>`
- Actionable error messages for unrecognized subcommands
- Structured logging with `RUST_LOG` support

### Configuration Hierarchy

Standard priority order, consistent across all primals:
1. Command-line arguments (highest precedence)
2. Environment variables
3. Configuration file
4. Compiled defaults (lowest precedence)

### Signal Handling

All server modes handle `SIGTERM` and `SIGINT` gracefully, logging shutdown reason and cleaning up resources (socket files, temporary state).

### Exit Codes

- `0` - Success
- `1` - General error
- `2` - Configuration error
- `3` - Network error
- `130` - Interrupted (Ctrl+C)

---

## Implementation

The recommended implementation uses the `clap` crate with derive macros:

```rust
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "primal", version, about)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Server { /* ... */ },
    Doctor { /* ... */ },
}
```

Cargo configuration:

```toml
[[bin]]
name = "primal"
path = "src/main.rs"
```

No multiple `[[bin]]` entries. One binary, one entry point.

---

## Deployment Integration

Deployment graphs reference the primal name and specify the mode:

```toml
[nodes.config]
primal_name = "beardog"
mode = "server"
args = ["server", "--daemon"]
```

This decouples deployment from binary naming - the graph specifies what to do, not which variant to find.

---

## Relationship to ecoBin and genomeBin

UniBin is the foundation of the binary standards ladder:

- **UniBin** defines structure (this specification)
- **ecoBin** adds portability (Pure Rust, cross-compilation)
- **genomeBin** adds deployment (auto-detection, service integration)

Each stage inherits all requirements from the previous. Every ecoBin is a UniBin. Every genomeBin is an ecoBin.

---

## Reference Implementation

NestGate serves as the reference implementation. It provides:
- Single binary: `nestgate`
- Multiple subcommands: `service`, `doctor`, `storage`
- Comprehensive `--help` and `--version`
- Structured error messages
- Professional CLI experience

---

## Compliance

All new primals must implement UniBin from inception. Existing primals follow the documented migration path (assessment, implementation, testing, deployment) over 4-6 weeks.

Compliance verification:
1. Single binary named after primal (no suffixes)
2. At least one operational subcommand
3. `--help` and `--version` functional
4. Error messages actionable
5. Signal handling implemented

---

## Rationale

The single-binary-with-subcommands pattern is proven at scale by `kubectl`, `docker`, `cargo`, and `git`. It provides discoverability (users explore via `--help`), consistency (same patterns across tools), and robustness (deployment graphs reference one name, not many).

For an ecosystem of 10+ primals, the alternative - variant proliferation - would create 30-50+ separate binaries to manage, name, deploy, and document. UniBin keeps it to one per primal.
