# External Sovereignty Pattern — Collaborator Gate Routing

**Wave 60 — PostPrimordial (May 28, 2026)**

---

## What This Document Is

This describes how the ecosystem's sovereignty infrastructure enables
external collaboration. When a collaborator syncs with the ecosystem,
they use the same WaterFall pipeline that internal gates use — just
with a different gate profile.

Sovereignty is not isolation. It is the ability to collaborate on your
own terms, through your own infrastructure, with full provenance.

---

## The Collaborator Gate Model

Internal gates (eastGate, ironGate, strandGate, etc.) sync through
the periplasm via `cascade-pull.sh --gate auto`. External collaborators
follow the same pattern:

```
External collaborator workstation
    ↓  git clone from Forgejo (HTTPS or SSH)
    ↓  cascade-pull --gate collaborator --source forgejo
    ↓  evolve locally
    ↓  git push forgejo
Forgejo (golgiBody VPS)
    ↓  WaterFall distributes to internal gates
Internal gates
```

### Gate Profile for Collaborators

A collaborator gets a manifest gate profile scoped to their domain:

```toml
[gates.gonzales_nf]
repos = [
    "wateringHole",
    "helixVision", "initioChem", "blueFish",
    "wetSpring", "hotSpring",
    "projectFOUNDATION",
]
```

They only pull repos relevant to their science. They never need
core NUCLEUS primals, infra repos, or unrelated springs. The
WaterFall pipeline handles scoping automatically.

### SSH Key Registration

Collaborators register their SSH public key with Forgejo (the same
process documented in `GOLGIBODY_GATE_ONBOARDING_MAY28_2026.md`):

1. Copy public key to VPS Forgejo UI or API
2. Add `forgejo` remote to repos
3. `cascade-pull --source forgejo` to validate

No VPN, no Cloudflare tunnel, no proprietary tooling. SSH + Git is
the universal protocol.

---

## Sovereignty Enables Collaboration

| Without sovereignty | With sovereignty |
|--------------------|--------------------|
| Collaborator pushes to GitHub; we grant org access | Collaborator pushes to our Forgejo; we control the gate |
| GitHub controls access policies, rate limits, privacy | We control access policies on our infrastructure |
| CI runs on GitHub Actions; vendor lock-in | CI runs on sovereign hardware (plasmidBin validate) |
| No provenance chain; trust is social | Full BLAKE3 provenance chain; trust is cryptographic |
| Single point of failure (GitHub outage = no work) | VPS Forgejo + local repos = work continues regardless |

The key insight: sovereignty doesn't exclude external contributors.
It gives them a better collaboration surface — one where the
provenance chain is real, the infrastructure is auditable, and the
science they produce is genuinely theirs.

---

## The Spore Cycle Through Sovereign Infrastructure

gen5's core question — "does someone else's science come out the
other end?" — requires sovereign infrastructure to answer properly.

### Without Sovereignty
```
Collaborator → GitHub PR → Our CI validates → Paper cites GitHub URL
```
The science lives on vendor infrastructure. The provenance chain
has a vendor-controlled link.

### With Sovereignty
```
Collaborator → Forgejo push → WaterFall distributes → NUCLEUS validates
    → sweetGrass braid created → BLAKE3 provenance chain → Artifact ships
```
The science lives on sovereign infrastructure from ingestion to
artifact. The provenance chain is end-to-end on hardware we control.

### The Spore Returns

When a collaborator's science validates new computational results:
1. Their results become new validation targets for springs
2. Springs evolve from external demand (gen5 pattern)
3. The evolved springs produce better infrastructure
4. The next collaborator gets better tools

This is the spore cycle: external science feeds back into the
ecosystem, which produces better tools for the next external scientist.
Sovereignty ensures the cycle operates on infrastructure the ecosystem
controls.

---

## Implementation Status

| Component | Status | Role |
|-----------|--------|------|
| Forgejo on VPS | LIVE | Periplasmic sync point for all gates |
| SSH key registration | LIVE | Gate onboarding for any contributor |
| `cascade-pull --gate` | LIVE | Profile-scoped sync |
| `cascade-pull --gate auto` | LIVE | Hostname/env auto-detection |
| Collaborator gate profiles | PLANNED | Per-collaborator manifest profiles |
| Forgejo fine-grained permissions | PLANNED | Repo-level access control per collaborator |
| sweetGrass braid on Forgejo push | PLANNED | Provenance chain starts at push |

---

## Connecting to gen5 Collaborators

Each gen5 collaborator maps to this pattern:

| Collaborator | Potential Gate Profile | Products |
|-------------|----------------------|----------|
| Gonzales (NF) | `gonzales_nf` | helixVision + healthSpring + initioChem |
| ABG community | `abg_science` | initioChem + hotSpring |
| Jones (PFAS) | `jones_pfas` | blueFish + wetSpring |
| Barrick (LTEE) | `barrick_ltee` | lithoSpore + wetSpring |
| Murillo students | `murillo_physics` | hotSpring + pseudoSpore |
| Chuna (QCD) | `chuna_qcd` | hotSpring workbench |

Each gets: SSH access to Forgejo, a scoped gate profile in the manifest,
and access to the WaterFall sync pipeline. No GitHub org membership
required. No vendor intermediary.

---

## Key Files

| File | Role |
|------|------|
| `wateringHole/GATE_SPRING_OWNERSHIP.md` | Gate-spring routing SSOT |
| `wateringHole/WATERFALL_PATTERN.md` | WaterFall sync specification |
| `wateringHole/cascade-pull.sh` | Sync orchestrator |
| `wateringHole/ecosystem_manifest.toml` | Repo catalog + gate profiles |
| `wateringHole/handoffs/GOLGIBODY_GATE_ONBOARDING_MAY28_2026.md` | Gate onboarding steps |
| `gen4/architecture/SOVEREIGNTY_EVOLUTION_NARRATIVE.md` | How we got here |
| `gen5/foundations/PUBLIC_DATA_SYSTEMS.md` | Data systems for collaborator science |

---

*Sovereignty is not a wall. It is a gate — one you control, one that
opens to anyone whose science you want to support, on infrastructure
neither party needs permission to use.*
