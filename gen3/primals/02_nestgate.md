# NestGate — Universal Storage and Discovery

## Identity

| Field | Value |
|-------|-------|
| Phase | 1 (Foundation) |
| Domain | Storage, content addressing, model cache |
| Rust lines | 645,445 |
| Tests | 14,807 |
| Crates | 13 |
| AGPL-3.0 | Yes |

## What It Is

NestGate is the data layer. Content-addressed storage (BLAKE3), ZFS integration, model caching, quota management. If data needs to persist across sessions, it goes through NestGate.

NestGate is one of the two **original primals** — it existed before the word "primal" did. In gen1, it was the Rust-based ZFS storage manager for the AI Swarm HPC cluster. In gen2, it became a sovereign storage primitive. In gen3, it's the storage component of the NUCLEUS Nest Atomic.

## Why It Exists

The gen1 HPC cluster needed a storage layer that understood ZFS, handled tiered storage (cold archive on HDDs, hot cache on NVMe), and provided NFS/SMB access for compute nodes. NestGate was purpose-built for this.

As the ecosystem grew, NestGate absorbed additional responsibilities: model caching for Squirrel's AI inference, content-addressed blob storage for rhizoCrypt, and discovery services for the ecosystem.

## Key Capabilities

### Storage

- **Content-addressed blobs**: BLAKE3 hash → blob. Deduplication by content, not name.
- **ZFS integration**: Snapshots, compression, quota, pool management
- **Tiered storage**: Cold (HDD) → warm (SSD) → hot (NVMe) → cache (RAM)
- **Model cache**: JSON-RPC endpoints for AI model download, storage, and retrieval (used by Squirrel)

### Discovery

- **Isomorphic IPC**: NestGate discovers other primals and is discovered by them using a 4-tier fallback: Try → Detect → Adapt → Succeed
- **MCP provider**: Exposes storage capabilities via Model Context Protocol
- **Multi-family sockets**: Like BearDog, supports multiple independent instances

## How It Connects

```
Squirrel ──model.cache──▶ NestGate ◀──blob.store── rhizoCrypt
                              │
biomeOS ──health.nest──▶     │     ◀──content.get── sweetGrass
                              │
LoamSpine ──anchor──▶        │
                         ZFS pools
```

NestGate is primarily a **server**: other primals store and retrieve data through it. The socket lives at `$XDG_RUNTIME_DIR/biomeos/nestgate.sock`.

### Key Relationships

- **Squirrel** uses NestGate to cache AI models locally (avoiding repeated downloads)
- **rhizoCrypt** stores content-addressed blobs through NestGate
- **LoamSpine** anchors permanent entries through NestGate's ZFS snapshots
- **biomeOS** monitors NestGate health as part of the Nest Atomic
- **sweetGrass** stores provenance records through NestGate

## Internal Architecture

13 crates:

- `nestgate-core` — Storage traits, content addressing, blob management
- `nestgate-api` — REST API (Axum)
- `nestgate-zfs` — ZFS pool and dataset management
- `nestgate-mcp` — Model Context Protocol provider
- `nestgate-rpc` — JSON-RPC server and isomorphic IPC

## What Makes It Interesting

NestGate has the second-highest test count of any primal (14,807). Its isomorphic IPC pattern — the same connection logic works over Unix sockets, TCP, and abstract sockets, auto-detecting the best transport — was independently adopted by other primals after NestGate proved the pattern.

The gen1 lineage is visible in the codebase: ZFS management code that predates the primal architecture sits alongside content-addressed blob storage that was added in gen2. The archaeological layers are readable.
