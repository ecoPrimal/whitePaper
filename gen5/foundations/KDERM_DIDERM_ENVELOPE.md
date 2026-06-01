# K-Derm Diderm Envelope — Multi-Membrane Sovereign Infrastructure

**Gen5 Foundation** (evolved from gen4 `K_DERM_RECONCILIATION.md`)

---

## Evolution from Gen4

Gen4 introduced the K-Derm topology as a naming reconciliation — resolving
"inner" vs "outer" membrane ambiguity across ecosystem documents. Gen5
graduates K-Derm to a physical deployment topology with three independently
provisioned VPS nodes forming a diderm cell envelope.

### Gen4 Contribution
- Named envelope layers from inside out (cytoplasm → plasma membrane → periplasm → outer membrane → extracellular)
- Established monoderm/diderm classification for deployment topologies
- Introduced channel protein model for K-Derm boundary crossings (TLS, NAT, content, auth)

### Gen5 Extension
- Physical deployment of diderm topology across three VPS nodes
- Peptidoglycan as a distinct structural layer with its own node
- Bond-type degradation model (covalent → metallic → ionic → weak) across layers
- Multi-golgiBody architecture: inner (cis), structural (peptidoglycan), outer (trans)
- K-Derm relay chain with proper bonding at each boundary

---

## Physical Topology (Wave 63+)

```
                    GitHub (extracellular)
                         │ weak bond
              ┌──────────┴──────────┐
              │   golgiBody-ext     │  ← outer membrane (trans face)
              │   137.184.197.151   │     Caddy TLS, sporePrint, DNS ns2
              │   ext-github-push   │     Ships to extracellular
              └──────────┬──────────┘
                         │ ionic bond (SSH relay)
              ┌──────────┴──────────┐
              │   peptidoglycan     │  ← structural layer
              │   157.230.209.218   │     Build hub, temporal sync convergence
              │   pepti-sync-relay  │     Mediates inner↔outer flow
              └──────────┬──────────┘
                         │ metallic bond (webhook/SSH)
              ┌──────────┴──────────┐
              │   golgiBody-inner   │  ← inner membrane (cis face)
              │   157.230.3.183     │     Forgejo, NUCLEUS primals, DNS ns1
              │   receives pushes   │     Sovereign periplasm
              └──┬─────┬─────┬─────┘
                 │     │     │  covalent bonds (SSH + Forgejo)
              ┌──┴─┐ ┌┴──┐ ┌┴──┐
              │east│ │bio│ │flo│   ← cytoplasm (gates)
              │Gate│ │me │ │ck │     Local NUCLEUS workspaces
              └────┘ └───┘ └───┘
```

### Bond-Type Degradation

Each layer transition involves a weaker bond type — this is by design.
Sovereignty is strongest at the core and degrades outward:

| Transition | Bond Type | Transport | Trust Level |
|------------|-----------|-----------|-------------|
| Gate → golgiBody-inner | Covalent | SSH + Forgejo push | Full mutual trust |
| golgiBody-inner → peptidoglycan | Metallic | Webhook / SSH | Structural mediation |
| peptidoglycan → golgiBody-ext | Ionic | SSH relay | Directed, asymmetric |
| golgiBody-ext → GitHub | Weak | `git push` over HTTPS | External, append-only |

---

## Multi-golgiBody Architecture

The three-node design separates concerns that were conflated in a
single-VPS architecture:

### golgiBody-inner (cis face)
- **Role**: Receives, stores, coordinates
- Forgejo instance (sovereign git forge)
- NUCLEUS primal services
- DNS primary (ns1.primals.eco)
- Accepts pushes from gates

### peptidoglycan (structural)
- **Role**: Builds, validates, mediates
- Rust/Zola toolchain
- Full 39-repo workspace for builds
- `pepti-sync-relay.sh` — metallic→ionic mediator
- Temporal sync convergence point

### golgiBody-ext (trans face)
- **Role**: Ships, serves, faces external
- Caddy TLS termination
- sporePrint static site
- DNS secondary (ns2.primals.eco)
- `ext-github-push.sh` — ionic→weak shipper
- GitHub SSH credentials (only node with write access)

---

## Evolution to Multi-Vendor Peptidoglycan

The peptidoglycan layer is designed for replication across providers:

1. **Current**: Single DO droplet (nyc1)
2. **Next**: Additional node on Hetzner/Vultr as redundant peptidoglycan
3. **Future**: Quorum-based sync across peptidoglycan nodes replaces
   single-point relay

This enables sovereignty even against a single cloud provider's failure
— the structural layer redistributes across providers while inner and
outer membranes maintain their roles.

---

## Cost Model

| Node | Spec | Monthly |
|------|------|---------|
| golgiBody-inner | s-2vcpu-4gb | $24 |
| peptidoglycan | s-2vcpu-4gb | $24 |
| golgiBody-ext | s-1vcpu-1gb | $6 |
| **Total** | | **$54/mo** |

The complete sovereign diderm envelope costs less than a single
commercial CI runner.

---

## Key Files

| File | Purpose |
|------|---------|
| `wateringHole/K_DERM_TOPOLOGY_STANDARD.md` | Canonical topology spec |
| `wateringHole/BONDING_MODEL_STANDARD.md` | Bond-type definitions |
| `wateringHole/hooks/forgejo/pepti-sync-relay.sh` | Peptidoglycan relay |
| `wateringHole/hooks/forgejo/ext-github-push.sh` | Trans-face shipper |
| `wateringHole/ecosystem_manifest.toml` `[topology]` | Layer declarations |
| `cellMembrane/crates/cellmembrane-types/src/envelope.rs` | Rust types |
