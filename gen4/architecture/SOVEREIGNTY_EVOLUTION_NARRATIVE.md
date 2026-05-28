# Sovereignty Evolution Narrative

**Wave 60 — PostPrimordial (May 28, 2026)**

This document captures the journey from primordial dependency to sovereign
infrastructure. It is both a fossil record for future gates and a
replicable playbook for any sovereign ecosystem following the same path.

---

## The Problem: Centralized Dependencies

Before Wave 55, the ecoPrimals ecosystem was bound to external services
for critical operations:

| Dependency | Risk | Layer |
|-----------|------|-------|
| **GitHub** | Code hosting, CI, releases — single vendor controls source access | Extracellular |
| **Cloudflare** | DNS, TLS termination, tunnel routing — vendor mediates all traffic | Outer membrane |
| **ironGate-local Forgejo** | Git service bound to `localhost:3000`, accessible only through Cloudflare tunnel — gate-specific, not ecosystem-wide | Cytoplasm leak |
| **npm/crates.io** | Package distribution — no sovereign alternative | Extracellular |

The fundamental issue: removing any single vendor breaks the ecosystem.
A sovereign ecosystem cannot have single points of external failure.

---

## Phase 1: Membrane Recognition (Waves 48-55)

The first step was recognizing the K-Derm (diderm cell envelope) topology
as an architectural model. From `cellMembrane`:

```
Cytoplasm          Gate NUCLEUS workspace — local evolution
Plasma membrane    Gate firewall + SSH keys — covalent boundary
Periplasm          Shared sync layer — WaterFall mediator
Outer membrane     VPS service surface — lab, sporePrint, DNS
Extracellular      GitHub, npm, crates.io — trailing mirrors
```

This framing revealed the gap: there was no periplasm. Gates pushed
directly to the extracellular layer (GitHub) and pulled from it. The
ecosystem had an outer membrane (Cloudflare) but no inner shared space.

---

## Phase 2: golgiBody — Periplasmic Forgejo (Wave 59-60)

### The golgiBody Concept

A Golgi body in biology packages and routes proteins between the ER
and the cell membrane. `golgiBody` is the ecosystem analogue: a
specialized `fieldMouse`-class NUCLEUS deployment on the VPS that
packages, modifies, and routes git traffic between gates.

### Deployment (Wave 60)

1. **Forgejo v15.0.2** deployed on VPS (`cellMembrane` at `157.230.3.183`)
2. **5 organizations** created mirroring GitHub: `ecoPrimals`, `syntheticChemistry`, `sporeGarden`, `lithoSpore`, `abg`
3. **38 repos** seeded from ironGate via SSH push
4. **Caddy TLS** reverse proxy: `git.primals.eco → localhost:3000`
5. **SSH on port 2222**: gates push/pull via `ssh://git@git.primals.eco:2222`
6. **UFW** configured: ports 80, 443, 2222 open

### Architectural Impact

Before golgiBody:
```
Gate → Cloudflare Tunnel → ironGate:3000 (Forgejo) → GitHub
```

After golgiBody:
```
Gate → SSH/HTTPS → VPS:2222/443 (Forgejo) → GitHub (trailing mirror)
```

Forgejo moved from a cytoplasm leak (gate-specific, tunnel-dependent)
to a proper periplasmic layer (VPS-hosted, SSH-accessible from any gate).

---

## Phase 3: WaterFall Sync Pattern (Wave 60)

With Forgejo in the periplasm, the WaterFall pattern enables concurrent
gate evolution:

### Waterfall Down
```bash
cascade-pull.sh --source forgejo --gate auto
```
Gates pull from Forgejo. The script auto-detects the gate via hostname
or `GATE_NAME` env, selects the manifest `[gates.*]` profile, and
pulls only repos the gate owns.

### Evolution Up
```bash
git push forgejo main
```
Individual repos push to Forgejo after local development. Forgejo
becomes the source of truth; GitHub becomes the trailing mirror.

### Gate Profile Sync

Each gate has a manifest profile (`[gates.eastGate]`, etc.) listing
which repos it needs. This replaces "pull everything" with targeted
sync:

| Gate | Repos | Focus |
|------|-------|-------|
| eastGate | 38 (full) | Coordination hub |
| ironGate | ~20 | Core + healthSpring + ludoSpring |
| southGate | ~18 | Core + wetSpring + neuralSpring |
| biomeGate | ~17 | Core + hotSpring (GPU compute) |
| strandGate | ~24 | Core + ABG gardens + lithoSpore |
| golgiBody | ~17 | NUCLEUS primals + deployment infra |

See `WATERFALL_PATTERN.md` for the full pattern specification.

---

## Phase 4: DNS Sovereignty — knot-dns (Wave 60)

Sovereign DNS removes the last Cloudflare dependency for name resolution.

### Deployment

- **knot-dns** running on VPS, authoritative for `primals.eco`
- Zone records: `A` records for `git.primals.eco`, `lab.primals.eco`,
  `membrane.primals.eco`, and root domain
- Validated via `kdig` against VPS public IP

### Cutover Path

| Step | Status |
|------|--------|
| knot-dns deployed and serving | DONE |
| Zone records correct for VPS services | DONE |
| NS records at registrar pointed to VPS | IN PROGRESS |
| Cloudflare DNS proxy disabled (grey cloud) | DONE for git/lab |
| DNSSEC signing | PLANNED (post-registrar cutover) |

### Cloudflare Tunnel Retirement

The `cloudflared` tunnel on ironGate is now orphaned — DNS no longer
routes through Cloudflare for `git.primals.eco` or `lab.primals.eco`.
The tunnel remains active as a shadow fallback during the transition
period.

Shadow tracks:
```
S1: Deploy sovereign DNS (knot-dns)      — DONE
S2: Cut DNS records to VPS               — DONE (git, lab)
S3: Validate all services via VPS direct  — DONE
S4: Retire cloudflared tunnel             — PENDING (needs lab static content)
```

---

## Phase 5: Gate-Spring Specialization (Wave 60+)

With the periplasm established and WaterFall operational, gate-spring
ownership is formalized.

### The Shift

Before: Ad-hoc routing via handoff blurbs.
After: `GATE_SPRING_OWNERSHIP.md` as canonical SSOT.

Each gate owns specific science domains:
- **eastGate**: Ecosystem coordination (primalSpring, airSpring, groundSpring)
- **ironGate**: Clinical + game (healthSpring, ludoSpring)
- **strandGate**: ABG science + genomics (hotSpring, helixVision, initioChem, blueFish)
- **biomeGate**: GPU compute (hotSpring GPU dispatch)
- **southGate**: Biology + ML (wetSpring, neuralSpring)

### Covalent Evolution

```
Ad-hoc (Wave 55)  →  Documented (Wave 60)  →  Songbird mesh (Wave 62+)
                                                    ↓
                                            toadStool dispatch (Wave 63+)
                                                    ↓
                                            biomeOS graph.execute (Wave 65+)
```

The endpoint is fully covalent routing: compute jobs flow between gates
through the periplasm without manual coordination. The Songbird mesh
advertises capabilities; toadStool dispatches to the best-fit hardware;
biomeOS orchestrates the full pipeline.

---

## Replication Guide

For any sovereign ecosystem following this path:

1. **Map your topology** — identify which layers are vendor-dependent
2. **Deploy a periplasm** — self-hosted git (Forgejo) on shared infrastructure
3. **Seed all repos** — mirror your extracellular repos to the periplasm
4. **Configure gate profiles** — each node pulls only what it needs
5. **Deploy sovereign DNS** — authoritative zone on your infrastructure
6. **Shadow-track the cutover** — run both paths until the sovereign path proves reliable
7. **Formalize ownership** — document which node owns which domain
8. **Automate sync** — `cascade-pull --gate auto` with hostname detection

The key insight: sovereignty is not a switch you flip. It is a shadow
track you run alongside dependencies until the sovereign path proves
reliable, then you cut the wire.

---

## Key Files

| File | Role |
|------|------|
| `wateringHole/GATE_SPRING_OWNERSHIP.md` | Canonical gate-spring routing SSOT |
| `wateringHole/WATERFALL_PATTERN.md` | WaterFall sync pattern specification |
| `wateringHole/cascade-pull.sh` | WaterFall orchestrator with gate auto-detection |
| `wateringHole/ecosystem_manifest.toml` | Repo catalog + gate profiles + sync config |
| `cellMembrane/VPS_STATE.md` | Live VPS state documentation |
| `projectNUCLEUS/deploy/forgejo_mirror.sh` | Forgejo repo provisioning |
| `projectNUCLEUS/deploy/deploy_knot_dns.sh` | Sovereign DNS deployment |
| `plasmidBin/membrane/Caddyfile` | VPS TLS + reverse proxy configuration |

---

*Wave 60. The periplasm is live. The WaterFall flows. Gates specialize.
The sovereign path shadows the dependent one, and wire by wire, the
ecosystem cuts free.*
