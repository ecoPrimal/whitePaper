# Infrastructure Recreation and Outage Playbook

**Date**: May 17, 2026
**Status**: Living document — evolves with sovereignty phases
**Lineage**: `CELLMEMBRANE_FIELDMOUSE_ARCHITECTURE.md`, `SOVEREIGN_HPC_EVOLUTION.md`,
`NUCLEUS_SOVEREIGNTY_ARCHITECTURE.md`, `REPO_MEMBRANE_BOUNDARY.md`

---

## Purpose

This document answers two questions:

1. **If everything was lost, how do we rebuild?** Cold-start from bare metal
   to full ecosystem composition.
2. **How do we test resilience before reality tests us?** Simulated outage
   patterns that prove recovery without waiting for actual failures.

The gram-negative architecture means we can lose any single layer and
recover. This playbook documents how.

---

## Part 1: Infrastructure Recreation — Cold Start

### Prerequisites

Before any gate or VPS can run primals:

| Requirement | Source | Notes |
|-------------|--------|-------|
| Hardware with Linux | Physical gates or VPS | Debian 12+ preferred |
| Internet access | ISP or VPS provider | NAT traversal handled by cellMembrane |
| SSH keys | Generated locally | Never committed — see `.gitignore` patterns |
| Git access | GitHub (outer) or Forgejo (inner) | Clone sources for all repos |
| Rust toolchain | `rustup` | `stable` for most, `nightly` for coralReef CUDA |
| plasmidBin binaries | `plasmidBin` repo releases | Pre-built musl-static x86_64/aarch64 |

### Layer 0: Single Gate Bootstrap

The minimal viable ecosystem is one gate running 13 primals on `127.0.0.1`.

```
1. Install Debian 12+ (or NixOS for reproducibility)
2. Install Rust: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
3. Clone infrastructure:
   git clone git@github.com:ecoPrimals/plasmidBin.git
   git clone git@github.com:ecoPrimals/wateringHole.git
4. Fetch pre-built binaries:
   cd plasmidBin && ./fetch_all.sh
5. Run composition:
   ./tools/composition_nucleus.sh
6. Validate:
   primalspring validate --all-scenarios
```

**What this gives you**: All 13 primals, MethodGate enforced, local UDS
sockets, JSON-RPC, BTSP AEAD authentication. No internet-facing services.

### Layer 1: Gate Hardening

Apply the Dark Forest Glacial Gate checks:

```
./gates/darkforest_membrane.sh          # 33 checks, 5 pillars
./gates/membrane_telemetry.sh           # baseline capture
./gates/dark_forest_gate_local.sh       # deploy graph validation
```

Configuration in `projectNUCLEUS/gates/*.toml`:
- `deny.toml`: banned crates (ring, openssl — sovereignty violations)
- `routing_config.toml`: membrane routing rules
- `membrane_7day.toml`: telemetry baseline template

### Layer 2: Multi-Gate Mesh (10G Backbone)

For sites with multiple gates:

| Step | Command / Config | Validates |
|------|-----------------|-----------|
| Physical cabling | 10G DAC/fiber between gates | Link speed (ethtool) |
| MTU 9000 | `ip link set <iface> mtu 9000` | Jumbo frames enabled |
| VLAN tags | `ip link add link <iface> name <vlan> type vlan id <N>` | Isolation |
| Songbird discovery | Each gate's `songbird` joins mesh via BirdSong | Peer count |
| Blob replication | `sweetGrass` braid sync across gates | DAG convergence |
| Workload dispatch | `toadStool` + `biomeOS` distribute compute | GPU/CPU utilization |

The intracellular mesh is **covalent** — full trust, shared family seed,
wire-speed data. See `SOVEREIGN_HPC_EVOLUTION.md` for the full hardware
composition map.

### Layer 3: cellMembrane VPS Deployment

The outer membrane connects the gate cluster to the internet:

```
cd cellMembrane
./deploy_membrane.sh                     # provisions VPS, deploys Tower
./status                                 # checks all services
```

**VPS components** (current: DigitalOcean nyc1, 2GB, Debian 12):

| Service | Port | Role |
|---------|------|------|
| Songbird TURN | 3478 | NAT traversal relay |
| RustDesk hbbs | 21115 | Remote desktop ID server |
| RustDesk hbbr | 21116-21117 | Remote desktop relay |
| Caddy | 80, 443 | TLS termination, content serving |
| BearDog | 9100 | Crypto/auth proxy |
| SkunkBat | 9140 | Audit trail |

**Recovery**: The VPS is stateless. If destroyed:
1. `doctl compute droplet create` (or provider equivalent)
2. `./deploy_membrane.sh` against new IP
3. Update DNS A records for `primals.eco`
4. Gate reconnects automatically via Songbird

Time to recovery: ~15 minutes.

### Layer 4: Forgejo (Inner Membrane Git)

```
# On a gate or dedicated NUC:
docker compose -f forgejo/docker-compose.yml up -d
# Configure orgs: sporeGarden, ecoPrimals, syntheticChemistry
# Mirror repos from GitHub: forgejo_mirror.sh
```

Forgejo is the declared inner-membrane primary Git host. All operational
repos should push to Forgejo first, with GitHub as the outer mirror.
See `REPO_MEMBRANE_BOUNDARY.md` for which repos are inner-only,
dual-push, or outer-only.

### Layer 5: Sovereign Services

Additional services on the gate cluster:

| Service | Gate | Port | Purpose |
|---------|------|------|---------|
| JupyterHub | ironGate | 8000 | PAM + BTSP dual-auth notebooks |
| NestGate | ironGate | 9120 | Content index, sporePrint |
| Cloudflare tunnel | ironGate | — | ABG access to JupyterHub |
| plasmidBin CI | (GitHub) | — | Binary harvest pipeline |

---

## Part 2: Outage Simulation Catalog

### Philosophy

The stadial will impose real constraints (power costs, bandwidth limits,
hardware failures). We prepare during the interstadial by simulating
failures deliberately. Each scenario has measurable acceptance criteria.

The gram-negative model provides a natural outage taxonomy: each membrane
layer can fail independently, and the organism should survive.

### Scenario 1: VPS Loss (Outer Membrane Down)

**Simulate**: `doctl compute droplet delete <id>` or power off VPS

**What breaks**:
- External relay (Songbird TURN) — external clients can't reach gates
- RustDesk remote access — remote desktop unavailable
- TLS termination — `primals.eco` HTTPS down
- Content serving — sporePrint/NestGate pages unreachable externally

**What survives**:
- All 13 primals on all gates (intracellular)
- 10G mesh, blob replication, workload dispatch
- Local JupyterHub (via LAN)
- All validation, science pipelines, provenance signing

**Recovery**: `./deploy_membrane.sh` against new VPS (~15 min)

**Acceptance criteria**:
- [ ] Gate primals report healthy throughout outage
- [ ] `primalspring validate --all-scenarios` passes during outage
- [ ] VPS reprovisioned and services restored within 20 minutes
- [ ] External clients reconnect automatically via Songbird

### Scenario 2: WAN Loss (ISP Down)

**Simulate**: Unplug WAN cable or disable WAN interface on router

**What breaks**:
- GitHub push/pull
- VPS tunnel (Cloudflare, SSH)
- External ABG access
- DNS resolution for external domains

**What survives**:
- All primals (127.0.0.1 / LAN)
- 10G mesh between gates
- Forgejo (if on LAN)
- All compute, validation, science
- `wetSpring` DAG checkpoint pattern: pipelines resume from last checkpoint

**Recovery**: Reconnect WAN. Songbird auto-reconnects. Git push queued changes.

**Acceptance criteria**:
- [ ] Multi-hour compute workloads survive WAN loss without data loss
- [ ] DAG checkpoints allow `wetSpring` pipeline resume
- [ ] Forgejo serves all inner-membrane repos during outage
- [ ] No primal restarts needed after WAN restoration

### Scenario 3: Single Gate Power Loss

**Simulate**: Power off one gate (e.g., northGate)

**What breaks**:
- Any primals hosted exclusively on that gate
- GPU workloads dispatched to that gate's hardware
- Local state (RAM, active sessions)

**What survives**:
- Other gates continue independently
- Songbird mesh heals around missing node
- Provenance braids eventually consistent (sweetGrass sync on reconnect)
- `wetSpring` DAG checkpoints survive — resume on any gate

**Recovery**: Power on gate. systemd restarts primals. Songbird rejoins mesh.

**Acceptance criteria**:
- [ ] Remaining gates report healthy within 60 seconds
- [ ] No data loss in provenance DAG
- [ ] Powered-on gate rejoins mesh and validates within 5 minutes
- [ ] In-flight workloads reschedule to surviving gates (future: biomeOS)

### Scenario 4: LAN Partition (Split Brain)

**Simulate**: Disconnect 10G link between two gate clusters

**What breaks**:
- Cross-gate workload dispatch
- Blob replication latency increases
- Songbird peer count drops on both sides

**What survives**:
- Each partition operates independently as a smaller NUCLEUS
- Local primals continue
- Provenance DAGs accumulate independently, merge on reconnect

**Recovery**: Reconnect 10G. sweetGrass DAG merge. Songbird mesh heals.

**Acceptance criteria**:
- [ ] Both partitions serve their local workloads
- [ ] DAG merge produces no conflicts (append-only provenance)
- [ ] Mesh peer count restores to baseline within 120 seconds

### Scenario 5: Forgejo Down

**Simulate**: `docker compose -f forgejo/docker-compose.yml down`

**What breaks**:
- Inner-membrane Git operations
- `git push forgejo` fails
- cellMembrane (if Forgejo-only) becomes unpushable

**What survives**:
- All deployed primals (binaries already on disk)
- `git push origin` to GitHub still works
- All validation, science, compute

**Recovery**: `docker compose up -d`. Repository state is on-disk.

**Acceptance criteria**:
- [ ] No primal downtime during Forgejo outage
- [ ] Pending pushes succeed after Forgejo restart
- [ ] No data loss in Forgejo repos

### Scenario 6: Full Site Power Loss

**Simulate**: Main breaker off (all gates lose power simultaneously)

**What breaks**:
- Everything intracellular
- VPS and external services remain up (independent power)

**What survives**:
- VPS (cellMembrane) continues serving cached content and relay
- GitHub repos remain accessible
- DNS continues resolving

**Recovery**:
1. Restore power
2. Gates boot, systemd starts primals
3. Songbird mesh reforms
4. sweetGrass DAG sync catches up
5. `primalspring validate --all-scenarios` confirms ecosystem health

**Acceptance criteria**:
- [ ] All 13 primals on all gates healthy within 10 minutes of power
- [ ] Provenance DAGs consistent after sync
- [ ] No manual intervention needed (systemd handles startup order)
- [ ] `wetSpring` resumes from DAG checkpoint, no science data loss

---

## Part 3: Validation Gate Cross-Reference

Each outage scenario maps to existing validation scripts:

| Scenario | Validation Gate | Script |
|----------|----------------|--------|
| VPS Loss | membrane_telemetry | `membrane_telemetry.sh` |
| WAN Loss | dark_forest_gate_local | `dark_forest_gate_local.sh` |
| Gate Power Loss | composition_health | `primalspring validate` |
| LAN Partition | songbird_mesh_health | `songbird --status` |
| Forgejo Down | (manual) | `git remote -v` check |
| Full Site | all gates | full `primalspring validate --all-scenarios` |

See `projectNUCLEUS/specs/EVOLUTION_GAPS.md` for the complete Validation
Gate Matrix mapping validation systems to sovereignty phase transitions.

---

## Part 4: Seasonal and Glacial Context

### Interstadial (current)

During the interstadial, outage simulation is **voluntary**. The purpose
is to build muscle memory and validate the recovery playbooks before
external pressure forces real cutovers.

Recommended cadence: one simulation per month, rotating through scenarios.

### Stadial (approaching)

The stadial imposes real constraints: power budgets, bandwidth caps,
hardware attrition. Recovery playbooks become survival protocols.

wetSpring's compute-aware pipeline (see `gen4_compute_aware_pipeline.md`)
provides the template: `substrate = f(data_size, latency_budget,
power_cost, cohabitant_load)`. When the stadial tightens power budgets,
the dispatch function naturally routes work to surviving or cheapest gates.

### Long-Term Glacial

Full sovereignty means surviving stadial without external dependency:
- Forgejo replaces GitHub for all Git operations
- cellMembrane runs on owned hardware (not rented VPS)
- Content serves from gate cluster via 10G + Caddy
- DNS authority on owned infrastructure
- All science pipelines produce provenance-signed results on sovereign compute

Each outage simulation is a rehearsal for this future.
