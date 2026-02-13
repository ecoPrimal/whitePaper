# genomeBin - Technical Specification

**Category**: Deployment Standard  
**Status**: Active Ecosystem Standard  
**Version**: 1.0.0  
**Adopted**: January 19, 2026

---

## Abstract

genomeBin defines the autonomous deployment standard for ecoPrimals. A genomeBin is an ecoBin wrapped with deployment machinery that creates a complete, self-installing organism. It auto-detects the target system (OS, architecture, init system), extracts the correct binary, configures services, validates health, and supports lifecycle management - all from a single executable archive requiring zero manual configuration.

---

## Problem Statement

An ecoBin is universally portable - it can run anywhere. But getting it running still requires manual steps: detect the target architecture, download the correct binary, set permissions, create service files, write configuration, enable auto-start, and verify health. For an ecosystem of 10+ primals across diverse deployment targets, this manual process does not scale.

genomeBin eliminates this gap by wrapping the ecoBin with the intelligence to deploy itself.

---

## The Three Evolutionary Stages

genomeBin is the third stage in the binary standards ladder:

| Stage | Metaphor | What It Adds |
|-------|----------|-------------|
| **UniBin** | DNA strand | Binary structure: one binary, multiple modes |
| **ecoBin** | Double helix | Universal portability: Pure Rust, cross-compilation, platform-agnostic IPC |
| **genomeBin** | Living cell | Autonomous deployment: self-detection, service integration, health monitoring |

Each stage inherits all requirements from the previous. A genomeBin is an ecoBin is a UniBin.

The biological principle: DNA (ecoBin) contains the genetic code, but a living cell (genomeBin) also has a membrane (deployment wrapper), mitochondria (service management), ribosomes (configuration), lysosomes (health monitoring), and an endoplasmic reticulum (update system).

---

## Specification

### Prerequisites

A primal must be a certified ecoBin before becoming a genomeBin. This means:
- All UniBin requirements satisfied
- 100% Pure Rust application code
- Cross-compilation matrix validated
- Static linking confirmed
- Platform-agnostic IPC implemented

### File Format

A genomeBin is a self-extracting archive: an executable shell script concatenated with a compressed payload.

```
<primal>.genome (executable)
  |
  +-- Deployment wrapper (bash/sh script)
  |     +-- System detection logic
  |     +-- Installation procedures
  |     +-- Service integration templates
  |     +-- Health validation
  |
  +-- Compressed payload (tar.gz)
        +-- ecobins/
        |     +-- <primal>-x86_64-linux-musl
        |     +-- <primal>-aarch64-linux-musl
        |     +-- <primal>-x86_64-macos
        |     +-- <primal>-aarch64-macos
        +-- configs/
        |     +-- config.toml.template
        +-- services/
        |     +-- systemd.service.template
        |     +-- launchd.plist.template
        |     +-- rc.d.template
        +-- scripts/
              +-- health-check.sh
              +-- update.sh
```

Typical size: 6-15 MB (4 architecture binaries at 2-5 MB each, compressed).

### System Detection (Tier 2)

The deployment wrapper must auto-detect:

- **Operating system**: Linux, macOS, BSD, Windows WSL
- **Architecture**: x86_64, aarch64, armv7, riscv64
- **Init system**: systemd, launchd, rc.d, openrc
- **Privilege level**: root, sudo available, user-only
- **Environment type**: development, production, embedded

Detection uses standard system introspection (`uname`, filesystem probes) with no external dependencies.

### Binary Selection and Installation (Tier 2)

The wrapper selects the correct ecoBin from the embedded payload based on detected OS and architecture, verifies its checksum, and installs it:

- Root install: `/usr/local/bin/<primal>`
- User install: `~/.local/bin/<primal>` (fallback)
- Permissions: `755`

Existing installations are detected. The wrapper prompts for upgrade/reinstall and backs up the current version.

### Service Integration (Tier 3)

The wrapper creates native service configuration for the detected init system:

**systemd** (Linux):
```ini
[Unit]
Description=<Primal> Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/<primal> serve
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

**launchd** (macOS): plist with `RunAtLoad` enabled.  
**rc.d** (BSD): rc script with `enable` flag.

Service is enabled for auto-start and started immediately. Status is validated before reporting success.

### Configuration Management (Tier 3)

Smart defaults are generated based on environment detection:
- System config: `/etc/<primal>/config.toml`
- User config: `~/.config/<primal>/config.toml`
- Runtime: `~/.cache/<primal>/`
- Data: `/var/lib/<primal>/` or `~/.local/share/<primal>/`

Configuration is templated - environment-specific values (log level, data directories, socket paths) are populated automatically.

### Health Monitoring (Tier 4)

Every genomeBin leverages the UniBin `doctor` subcommand:

```bash
<primal> doctor
```

The doctor checks: binary version, configuration validity, data directory integrity, socket connectivity, memory and CPU usage, uptime, and integration with other primals.

Output supports both human-readable (default) and JSON (for automation) formats. Exit code reflects overall health: 0 = healthy, 1 = issues.

The genomeBin wrapper adds scheduled health checks, alerting, and log aggregation.

### Lifecycle Management (Tier 5)

**Updates**: Check for new versions, download, verify signature/checksum, backup current, stop service, replace binary, restart, health check, auto-rollback on failure.

**Rollback**: Last 3 versions retained. Manual rollback or automatic on health check failure after update.

**Uninstall**: Stop service, remove service files, remove binary, optionally remove data and config. `--purge` for complete removal, `--dry-run` to preview.

---

## Certification Levels

| Level | Requirements |
|-------|-------------|
| **Bronze** | Tiers 1-3: ecoBin foundation + deployment wrapper + service integration |
| **Silver** | Tiers 1-4: + health monitoring |
| **Gold** | Tiers 1-5: + full lifecycle management (updates, rollback, uninstall) |
| **Platinum** | All tiers + exceptional user experience |

---

## User Experience

The transformation genomeBin achieves:

**Before** (ecoBin, manual deployment):
```bash
uname -m                                    # Detect architecture
wget .../primal-aarch64-musl               # Download correct binary
sudo install -m 755 primal /usr/local/bin/ # Install
sudo nano /etc/systemd/system/primal.service  # Create service
sudo nano /etc/primal/config.toml          # Configure
sudo systemctl enable --now primal         # Enable and start
```

**After** (genomeBin):
```bash
curl -sSf https://install.primal.dev/genome | sh
```

Seven manual steps become one automated command. The genomeBin handles everything the operator would have done, but does it correctly and consistently every time, on every system.

---

## Tooling

The `sourDough` primal provides standardized genomeBin scaffolding. 80-90% of genomeBin creation is templated:

```bash
sourDough/genomebin/scripts/create-genomebin.sh \
    --primal <name> \
    --version <semver> \
    --ecobins plasmidBin/primals/<name>/<version>/ \
    --output <name>.genome
```

Primal teams customize the remaining 10-20% (primal-specific health checks, configuration templates, domain-specific setup).

---

## Ecosystem Status

| Primal | genomeBin Ready | Notes |
|--------|----------------|-------|
| **BearDog** | Ready | Recommended first genomeBin |
| **NestGate** | Ready | 5 Linux + 2 macOS targets validated |
| **ToadStool** | Ready | 5 targets validated |
| **biomeOS** | Ready | Orchestrator genomeBin |
| **Squirrel** | Pending ecoBin | Build cleanup needed |
| **petalTongue** | Pending | Hybrid strategy (headless + CLI first) |

---

## Rationale

Sovereign computing requires sovereign deployment. If installing a primal requires following a multi-step guide, consulting platform-specific documentation, and manually configuring services, then the promise of "runs everywhere" is theoretical rather than practical.

genomeBin closes the gap between portability (ecoBin can run anywhere) and accessibility (genomeBin actually runs anywhere, for anyone, with one command). It is the difference between shipping DNA and shipping a living organism.

The competitive frame: easier than Docker (no daemon required), simpler than Snap (no store dependency), more universal than Homebrew (works on any system, not just macOS). One file, one command, zero configuration.
