# K-Derm Reconciliation — From Gram-Staining to Cell Envelope Architecture

**Date**: May 26, 2026
**Status**: Active
**Purpose**: Bridge the gram-negative/gram-positive framing in gen4 architecture documents to the canonical K-Derm cell envelope model
**Canonical spec**: `gardens/cellMembrane/specs/K_DERM_TOPOLOGY.md`
**Wire contract**: `infra/wateringHole/K_DERM_TOPOLOGY_STANDARD.md`
**Bonding model**: `infra/wateringHole/BONDING_MODEL_STANDARD.md`

---

## Why This Document Exists

Gen4 architecture documents use **gram-negative** and **gram-positive** as
the primary membrane topology vocabulary (see `SOVEREIGN_HPC_EVOLUTION.md`,
`SOVEREIGN_TRANSACTION_MEMBRANE.md`, `THE_GOLDEN_CAGE.md`,
`INFRASTRUCTURE_RECREATION_AND_OUTAGE_PLAYBOOK.md`). Three documents
also use conflicting **inner/outer** labels for the VPS:

| Document | "Inner membrane" | "Outer membrane" |
|----------|------------------|------------------|
| `SOVEREIGN_HPC_EVOLUTION.md` | Gate firewall | VPS channels |
| `CELLMEMBRANE_FIELDMOUSE_ARCHITECTURE.md` | VPS relay | GitHub/CDN |
| `CELLMEMBRANE_ARCHITECTURE.md` | (avoided — uses intra/extracellular) | (avoided) |

This is the **Franklin's Current problem** (K-Derm spec §1): two valid
reference frames produce opposite labels for the same component, like
conventional current vs electron flow. The gram-staining vocabulary
compounds it — gram-negative/gram-positive encode a **staining technique**,
not the membrane architecture itself.

K-Derm resolves this with **absolute positions** named from inside out,
and **structural** topology names (monoderm/diderm) that describe actual
architecture. This document maps every gen4 concept to the K-Derm model.

**Gen4 documents are not modified** — they are fossil record. This
reconciliation is the bridge.

---

## Terminology Mapping

### Topology Labels

| Gen4 Term | K-Derm Canonical | Why K-Derm is Better |
|-----------|------------------|----------------------|
| Gram-positive | **Monoderm** | Describes structure (single membrane), not a staining result |
| Gram-negative | **Diderm** | Describes structure (double membrane + periplasm) |
| Three-layer membrane model | **Diderm envelope** | Same concept, precise vocabulary |
| Inner membrane (SOVEREIGN_HPC) | **Plasma membrane** | Absolute position: always the gate boundary |
| Outer membrane (SOVEREIGN_HPC) | **Outer membrane** | Correct — retained as absolute name |
| Inner membrane (FIELDMOUSE) | **Periplasm + outer membrane** | Was "inner" relative to GitHub; K-Derm resolves by absolute naming |
| Cell wall | (no equivalent) | Substrate provider is not a membrane layer |
| Intracellular | **Cytoplasm** | More specific — the NUCLEUS process space |
| Extracellular | **Extracellular** | Same — retained unchanged |

### Layer Labels

| Gen4 Layer | K-Derm Layer | What Occupies It |
|------------|--------------|------------------|
| Gate internal / intracellular mesh | **Cytoplasm** | NUCLEUS processes, UDS IPC, shared memory |
| Gate firewall | **Plasma membrane** | UFW/nftables, covalent + metallic bonds |
| VPS routing / periplasm (when named) | **Periplasm** | Relay, routing, telemetry, attribution |
| VPS channels to internet | **Outer membrane** | Signal / Relay / Surface channels |
| Public internet | **Extracellular** | Dark Forest, weak bonds |

---

## Bonding Model Reconciliation

Gen4 documents define four bond types: **covalent, ionic, metallic, weak**.
Some also reference **ceremony** (time-bound decay). The unified bonding
model adds the **OrganoMetalSalt** composite and maps every bond to a
K-Derm envelope layer.

### Gen4 → K-Derm Bonding Placement

| Gen4 Concept | K-Derm Mapping |
|--------------|----------------|
| "Covalent = aquaporin" (SOVEREIGN_TRANSACTION_MEMBRANE) | Covalent bond at cytoplasm + plasma membrane, aquaporin channel protein |
| "Ionic = gated ion channel" (SOVEREIGN_TRANSACTION_MEMBRANE) | Ionic bond at periplasm + outer membrane, gated ion channel protein |
| "Ceremony = voltage-gated" (SOVEREIGN_TRANSACTION_MEMBRANE) | Ceremony bond at any layer (decaying), voltage-gated channel protein |
| "Weak = passive diffusion" (SOVEREIGN_TRANSACTION_MEMBRANE) | Weak bond at outer membrane + extracellular, passive diffusion channel protein |
| "Porins as VPS nodes" (SOVEREIGN_HPC_EVOLUTION) | Outer membrane channels — gated ion + passive diffusion per channel policy |
| "Periplasm routing" (SOVEREIGN_HPC_EVOLUTION) | Periplasm layer — `routing_config.toml` dispatch, ionic + metallic bonds |
| "Ionic surface" (SOVEREIGN_HPC_EVOLUTION) | Ionic bonds at outer membrane — BTSP scoped tokens for external partners |
| Content-aware routing (CELLMEMBRANE_FIELDMOUSE) | Periplasm routing — braid policy = Verify, bond classification at boundary |

### Bonding × BTSP × K-Derm Layer

| Bond Type | BTSP Cipher | K-Derm Layer | Channel Protein | Braid Policy |
|-----------|-------------|--------------|-----------------|--------------|
| Covalent | `BTSP_NULL` | Cytoplasm, Plasma | Aquaporin | Pass-through |
| Metallic | `BTSP_HMAC_PLAIN` | Plasma, Periplasm | Aquaporin | Pass-through |
| Ionic | `BTSP_CHACHA20_POLY1305` | Periplasm, Outer | Gated ion | Verify |
| Ceremony | (follows decay phase) | Any (decaying) | Voltage-gated | Verify |
| Weak | `BTSP_CHACHA20_POLY1305` / TLS 1.3 | Outer, Extracellular | Passive diffusion | Block |
| OrganoMetalSalt | Per-scope composite | Crosses multiple layers | Per-boundary | Per-boundary |

---

## NUCLEUS Atomics in the Envelope

Gen4 documents establish the particle model across multiple files
(`SOVEREIGN_COMPUTE_TRIO_SKETCH.md`, `BIOMEOS_OS_TRAJECTORY.md`,
`DEPLOY_GRAPH_COMPOSITION.md`). K-Derm gives it topological placement.

### Particle Model (from gen4, unchanged)

| Atomic | Particle | Primals |
|--------|----------|---------|
| Tower | Electron | BearDog + Songbird + skunkBat |
| Node | Proton | Tower + ToadStool + barraCuda + coralReef |
| Nest | Neutron | Tower + NestGate + rhizoCrypt + loamSpine + sweetGrass |
| NUCLEUS | Atom | Tower + Node + Nest (9 unique primals) |
| Desktop NUCLEUS | Full 13 | All atomics + meta (biomeOS + Squirrel + petalTongue) |

### K-Derm Topological Placement (new)

All atomics live in the **cytoplasm** — the gate's interior. The
particle model describes capability groupings, not layer placement.
The key insight is how atomics interact with the envelope:

| Atomic | Cytoplasm Role | Boundary Role |
|--------|---------------|---------------|
| **Tower (electron shell)** | Security, federation, identity | **Mediates all plasma membrane crossings** — no Node/Nest primal communicates directly with the periplasm |
| **Node (proton)** | Compute, sandboxing, GPU dispatch | Internal only — heavy compute stays in cytoplasm |
| **Nest (neutron)** | Storage, provenance, attribution | Internal only — data stays in cytoplasm, braid metadata verified at boundary |
| **Meta-tier** | Orchestration, AI, interface | biomeOS controls periplasm routing via configuration |

The electron shell analogy is precise: in an atom, the electron shell
mediates all interactions with other atoms. In NUCLEUS, Tower mediates
all interactions with the periplasm and beyond. BearDog authenticates at
the plasma membrane, Songbird federates through the periplasm (TURN
relay), skunkBat provides telemetry correlation across boundaries.

### Bonding Between NUCLEUS Instances (Plasmodium)

When multiple NUCLEUS instances bond (Plasmodium mesh), the bonding
model determines how the envelopes interact:

| Mesh Type | Bonding | Topology |
|-----------|---------|----------|
| Same-family LAN (eastGate ↔ ironGate) | Covalent | Monoderm → monoderm, Songbird TCP federation |
| Same-family WAN (eastGate ↔ flockGate) | Covalent via Metallic relay | Diderm → diderm, Songbird TURN through periplasm |
| Cross-family (lab ↔ campus) | Ionic | Nested diderm — lab outer = campus periplasm |
| Public (any → membrane-relay) | Weak → Ionic | Extracellular → outer membrane → periplasm routing |

---

## Sovereignty Layers → K-Derm Layers

Gen4 sovereignty documents use a Layer 1–4 model (`SOVEREIGN_COMPOSITION_EVOLUTION.md`,
`NUCLEUS_SOVEREIGNTY_ARCHITECTURE.md`). These map to K-Derm:

| Sovereignty Layer | K-Derm Layer(s) | Gen4 Source |
|-------------------|-----------------|-------------|
| Layer 1: Primal capability | Cytoplasm | All primals running, full IPC |
| Layer 2: Security | Plasma membrane | BTSP, family seed, firewall |
| Layer 3: Membrane bridge | Periplasm + Outer membrane | VPS relay, channels |
| Layer 4: Self-hosted forge | Plasma membrane (Forgejo = inner mirror) | Forgejo as periplasmic service |
| Horizon 1: LAN sovereign | Monoderm envelope | Gate directly on LAN |
| Horizon 2: WAN sovereign | Diderm envelope | Gate + VPS relay |
| Horizon 3: Fully sovereign | Multi-diderm / Nested | Multiple VPS, Forgejo primary, no GitHub |

### Shadow Tracks → Envelope Boundaries

The Calibrate → Shadow → Cutover protocol from `SOVEREIGNTY_STANDARDS.md`
applies at each K-Derm boundary:

| Shadow Track | Boundary Being Replaced | K-Derm Layer |
|-------------|------------------------|--------------|
| S1: TLS termination | Cloudflare → BearDog ACME | Outer membrane |
| S2: NAT traversal | Tailscale → Songbird TURN | Periplasm |
| S3: Content hosting | GitHub Pages → NestGate | Outer membrane (Surface channel) |
| S4: Authentication | GitHub OAuth → BearDog/Squirrel | Plasma membrane |
| CI sovereignty | GitHub Actions → Forgejo Actions | Periplasm (inner mirror) |

Each shadow track is a sovereignty evolution at a specific envelope
boundary. The K-Derm model makes the boundary explicit.

---

## Document-by-Document Reconciliation

### `SOVEREIGN_HPC_EVOLUTION.md`

**Gen4 framing**: Three-layer gram-negative membrane model.

**K-Derm reading**: The document's membrane layers map directly:
- "Inner membrane" → **Plasma membrane** (gate firewall)
- "Periplasm" → **Periplasm** (correct — already used this term)
- "Outer membrane" → **Outer membrane** (VPS channels)
- "Intracellular" → **Cytoplasm**
- "Extracellular" → **Extracellular**

The "three-layer gram-negative" model is the **diderm** topology. The
document's substance is correct; only the taxonomy label changes.

### `SOVEREIGN_TRANSACTION_MEMBRANE.md`

**Gen4 framing**: Gram-negative model with channel protein mapping.

**K-Derm reading**: The channel protein taxonomy is preserved exactly:
- Aquaporin → Covalent (correct)
- Gated ion → Ionic (correct)
- Voltage-gated → Ceremony (correct)
- Passive diffusion → Weak (correct)

K-Derm adds **per-layer** channel protein specificity — the document
applies them to "the membrane" as a single boundary; K-Derm applies
them at each boundary in the envelope independently.

### `CELLMEMBRANE_FIELDMOUSE_ARCHITECTURE.md`

**Gen4 framing**: VPS as "inner membrane" (relative to GitHub/CDN).

**K-Derm reading**: VPS is periplasm + outer membrane. GitHub/CDN is
extracellular. The "inner" label was relative to an outer reference
(GitHub) rather than the core (gate). K-Derm eliminates this by using
absolute positions from the cytoplasm outward.

### `THE_GOLDEN_CAGE.md`

**Gen4 framing**: GitHub as "outer membrane," LAN as "inner membrane."

**K-Derm reading**: GitHub is extracellular. Forgejo (LAN mirror) is a
periplasmic service. The "golden cage" is the extracellular dependency
on GitHub; the "chrysalis" is the construction of a diderm envelope that
makes GitHub optional (outer membrane channels served by primals).

### `INFRASTRUCTURE_RECREATION_AND_OUTAGE_PLAYBOOK.md`

**Gen4 framing**: Layer 0–5 cold-start with "gram-negative" outage scenarios.

**K-Derm reading**: Layer 3 (cellMembrane VPS) = periplasm + outer membrane.
Layer 4 (Forgejo inner-membrane Git) = periplasmic service behind plasma
membrane. Each outage scenario describes failure at a specific K-Derm layer.

### `SOVEREIGN_COMPUTE_TRIO_SKETCH.md`

**Gen4 framing**: Tower/Node/Nest particle model without membrane topology.

**K-Derm reading**: No changes needed — the atomic model is topology-independent.
K-Derm adds the insight that Tower is the electron shell mediating all
boundary crossings, but the particle assignments are unchanged.

---

## K-Derm Extensions Not in Gen4

These concepts from `K_DERM_TOPOLOGY.md` extend beyond what gen4
documents cover:

| Extension | Summary | Gen4 Closest Concept |
|-----------|---------|----------------------|
| **Recursive nesting** | Every administrative domain is its own K-Derm system, nested recursively | "Nested diderm" hinted in HPC evolution but not formalized |
| **Endosymbiosis** | External systems progressively internalize (Weak → Ionic → Metallic → Covalent) | Bonding escalation in sovereignty standards |
| **Gatehouse bond escalation** | The gatehouse (bearDog + drawbridge) is the bond escalation broker — validates weak interactions and promotes to ionic/metallic/covalent as trust is established, while the darkforest boundary prevents leakage | Implicit in Tower mediation role, formalized in Wave 133d `GATEHOUSE_DARKFOREST_STANDARD.md` |
| **Vesicle transport** | Braid as membrane coat — provenance attribution as SNARE protein targeting | sweetGrass attribution in transaction membrane |
| **Membrane potential** | Resource load creates osmotic pressure across boundaries | Implicit in compute dispatch but not formalized |
| **OrganoMetalSalt** | Composite bond type spanning multiple layers | Referenced in BTSP standard but not gen4 architecture |

---

## What Does NOT Change

- The **particle model** (Tower=electron, Node=proton, Nest=neutron, NUCLEUS=atom) is unchanged
- The **bonding model** (covalent, ionic, metallic, weak, ceremony) is unchanged
- The **three channels** (Signal, Relay, Surface) are unchanged
- The **sovereignty standards** (Calibrate → Shadow → Cutover) are unchanged
- The **BTSP protocol** is unchanged
- All gen4 documents remain as written — this reconciliation bridges vocabulary

What changes is the **topology vocabulary** (gram-staining → structural)
and the **layer naming** (relative inner/outer → absolute positions).
The substance was always correct; K-Derm gives it unambiguous labels.

---

## Cross-References

| Document | Location | Relationship |
|----------|----------|--------------|
| K-Derm canonical spec | `gardens/cellMembrane/specs/K_DERM_TOPOLOGY.md` | Source of truth |
| K-Derm wire contract | `infra/wateringHole/K_DERM_TOPOLOGY_STANDARD.md` | Ecosystem standard |
| Bonding model standard | `infra/wateringHole/BONDING_MODEL_STANDARD.md` | Unified bonding reference |
| BTSP protocol | `infra/wateringHole/BTSP_PROTOCOL_STANDARD.md` | Cipher enforcement per bond |
| NUCLEUS spring alignment | `infra/wateringHole/NUCLEUS_SPRING_ALIGNMENT.md` | Atomic model + genetics |
| Sovereignty standards | `infra/wateringHole/SOVEREIGNTY_STANDARDS.md` | Trust layers |
| Membrane channels | `infra/wateringHole/MEMBRANE_CHANNEL_ARCHITECTURE.md` | Channel architecture |
| K-NOME methodology | `infra/whitePaper/gen3/about/K_NOME_PROGRAMMING.md` | Parallel: K-NOME=how, K-Derm=shape |
| Envelope types | `gardens/cellMembrane/crates/cellmembrane-types/src/envelope.rs` | Rust implementation |
| Gatehouse bond escalation | `infra/wateringHole/GATEHOUSE_DARKFOREST_STANDARD.md` | Bond escalation broker pattern (Wave 133d) |
| K-Derm diderm deployment | `infra/whitePaper/gen5/foundations/KDERM_DIDERM_ENVELOPE.md` | Physical diderm + bond degradation model |
