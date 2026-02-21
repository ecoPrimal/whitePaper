# rhizoCrypt — Ephemeral Working Memory

## Identity

| Field | Value |
|-------|-------|
| Phase | 2 (Post-NUCLEUS) |
| Domain | Content-addressed DAG, session memory, ephemeral state |
| Rust lines | 27,565 |
| Tests | 278 |
| Crates | 3 |
| Grade | A (95/100) |

## What It Is

rhizoCrypt is the scratch pad. Content-addressed DAG (BLAKE3) for session state, working memory, intermediate computation results. Lock-free concurrency (DashMap). Six slice modes for data sharing. Designed to be discarded — ephemeral by intent.

## Why It Exists

Not everything should go to permanent storage. Conversation context, intermediate ML results, draft documents, exploration state — these need fast, concurrent access and zero persistence guarantees. rhizoCrypt provides exactly that: high-performance ephemeral storage that can be dehydrated to LoamSpine when permanence is needed.

The name: rhizomes are underground root networks that connect plants. "Crypt" for the encrypted content-addressing. The working memory of the ecosystem, spreading connections between active sessions.

## Key Capabilities

- **Content-addressed DAG**: BLAKE3 hash → node. Deduplication by content.
- **Lock-free concurrency**: DashMap for zero-contention concurrent access
- **Merkle trees**: Integrity verification of session state
- **6 slice modes**: Copy, Loan, Escrow, Mirror, Consignment, Provenance — different sharing semantics for different use cases
- **Dehydration**: Convert ephemeral sessions to permanent LoamSpine entries

## How It Connects

- **NestGate** — Content-addressed blob storage backend
- **LoamSpine** — Dehydration target for permanent records
- **sweetGrass** — Session-level provenance events
- **BearDog** — Signing for authenticated sessions (via capability-based SigningProvider trait)

3 crates: `rhizo-crypt-core`, `rhizo-crypt-rpc`, `rhizocrypt-service`.

## What Makes It Interesting

The six slice modes are a nuanced model of data sharing that goes beyond read/write permissions. "Loan" means temporary access with automatic revocation. "Escrow" means conditional release. "Consignment" means delegated custody with provenance tracking. These map to real-world data relationships that traditional access control can't express.

rhizoCrypt's low test count (278) relative to its grade (A 95/100) reflects its focused scope: the core DAG operations are small and well-defined. The lock-free design means most concurrency bugs are prevented structurally rather than caught by tests.
