# LoamSpine — Immutable Permanent Ledger

## Identity

| Field | Value |
|-------|-------|
| Phase | 2 (Post-NUCLEUS) |
| Domain | Permanent records, Loam certificates, federation |
| Rust lines | 44,453 |
| Tests | 1,952 |
| Crates | 3 |
| Version | 0.7.0 |

## What It Is

LoamSpine is the permanent ledger. Spines (sovereign append-only logs), Loam certificates (digital ownership, lending, provenance), recursive stacking, waypoint anchoring, inclusion proofs. If something needs to be permanent and verifiable, it goes to LoamSpine.

## Why It Exists

rhizoCrypt handles ephemeral working memory — session state that can be discarded. But some things must persist: identity chains, ownership records, scientific provenance, license attestations. LoamSpine provides the immutable complement to rhizoCrypt's ephemeral storage.

Together they implement the gen2 **"philosophy of forgetting"**: not everything should be remembered forever, but some things must never be forgotten. rhizoCrypt forgets; LoamSpine remembers.

## Key Capabilities

- **Spines**: Append-only ledgers with 15+ entry types
- **Loam certificates**: Digital ownership with lending, provenance tracking, recursive stacking
- **Waypoint anchoring**: Pin-to-time proofs against trusted external anchors
- **Inclusion proofs**: Merkle-based proof that an entry exists in a spine
- **Federation**: DNS SRV + mDNS discovery for remote Loam nodes (via Songbird)
- **Zero-copy**: Efficient serialization for large records

## How It Connects

- **BearDog** — Signs all ledger entries (CLI-based Ed25519, any signing provider)
- **Songbird** — Universal adapter for O(n) discovery; federation with remote LoamSpine nodes
- **rhizoCrypt** — Dehydrates ephemeral sessions into permanent LoamSpine entries
- **sweetGrass** — Anchors provenance chains

3 crates: `loam-spine-core`, `loam-spine-api`, `loamspine-service`.

## What Makes It Interesting

LoamSpine uses Pure Rust RPC (tarpc + JSON-RPC), not gRPC. The Infant Discovery pattern — Songbird as a central hub that reduces O(n²) discovery to O(n) — was pioneered in LoamSpine and adopted across the ecosystem.

Loam certificates with recursive stacking allow complex ownership structures: a certificate can reference other certificates, creating a DAG of provenance. This enables "digital lending" — temporary transfer of rights with automatic reversion.
