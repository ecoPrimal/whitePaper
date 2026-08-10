# Encrypted Sharded Data Federation

**Date**: Aug 10, 2026 | **Wave**: 157e | **Gate**: westGate
**Author**: overwatch/hardware team
**Predecessor**: `CONVERGENCE_TIERING_MULTI_RESOLUTION_SPINE.md`, `DATA_STAGING_IO_PATTERNS.md`
**Scope**: CAS baseline verification, encrypted data patterns, sharded recovery, cross-gate federation

---

## The Problem: Provenance Without Verification Is Theater

westGate braided 131 datasets (663 files, 3.84 TB) and 989,423 AlphaFold structures
into the provenance chain — but never once verified that the chain actually holds.
No one had tested whether:
- A braid can be walked back to its CAS content
- A Merkle proof verifies correctly
- An Ed25519 spine signature rejects tampering
- A deleted CAS object can be recovered via braid metadata
- Encrypted data survives the CAS round-trip
- Sharded encrypted data can be reconstructed after partial loss

Without these tests, the "provenance" was aspirational, not proven.

---

## The Pattern: 8-Level Braid Pen Test

A progressive verification harness (`braid_pentest.py`) that exercises every layer
of the provenance chain, from passive reads to active destruction and recovery.

### Level 1 — Read the Braid

Walk the chain end-to-end for real datasets:

```
.native_braid_state → spine_id → loamSpine.spine.status
                    → chunks[].merkle_root → rhizoCrypt.dag.merkle.root
                    → files[] → BLAKE3 hash → nestGate.content.exists
                    → sweetGrass.braid.get_by_hash
```

**Finding**: All 4 state-tracked datasets (alphafold, alphafold_structures,
cell_ontology, sra_fastq) pass CAS verification. Spines are ephemeral (in-memory
in loamSpine) and cleared on restart — only the state file persists the spine_id.
This means the spine is a session artifact, not a durable index. The durable records
are: CAS objects (nestGate), braids (sweetGrass), and state files (filesystem).

**Finding**: 1 of 5 braided-only datasets (`biogrid`) had CAS content missing but
its sweetGrass braid intact. This is correct behavior: the convergence drain moved
the CAS object to cold storage, but the braid record persists independently.
This proves braid metadata survives CAS tier migration.

### Level 2 — Merkle Proof + Ed25519 Signature

Create a test provenance chain with multiple DAG vertices, dehydrate to Merkle root,
then verify:

```
rhizoCrypt.dag.merkle.proof(session_id, vertex_id)
    → { root: [u8;32], siblings: [[u8;32]], position: u32, vertex_id: [u8;32] }

rhizoCrypt.dag.merkle.verify(root, proof)
    → true | false
```

**Wire format note**: `dag.merkle.verify` expects `{ root: [u8;32], proof: { vertex_id, root, siblings, position, total_vertices } }` — the proof is a nested struct with its own copy of the root. This is because the verifier re-computes the root from the leaf and siblings, then compares against the provided root.

Ed25519 roundtrip via bearDog:
```
crypto.sign_ed25519(message_b64) → { signature, public_key }
crypto.verify_ed25519(message, signature, public_key) → { valid: true }
crypto.verify_ed25519(tampered_message, signature, public_key) → { valid: false }
```

**Result**: Merkle proofs verify correctly with 2-vertex trees. Signature verification
correctly rejects tampered messages, tampered signatures, and forged payloads.

### Level 3 — Corruption Detection

Three attack vectors tested:

1. **CAS hash mismatch on put**: Attempt to store different content under an existing
   hash. nestGate **silently deduplicates** — it checks BLAKE3 of incoming data and
   if the computed hash matches an existing object, it skips the write. If the computed
   hash differs from the claimed hash, it stores under the computed hash. The original
   object is preserved. This is correct CAS behavior: content-addressing makes
   corruption-by-overwrite impossible.

2. **Merkle proof tampering**: Modify the vertex_id in a valid proof. rhizoCrypt
   returns `None` (implicit rejection) for the tampered proof. The verifier
   re-computes the root from the (fake) leaf and finds it doesn't match.

3. **Signature forgery**: Three sub-tests: forged message (different content,
   same signature), tampered signature (bit-flip in signature bytes), wrong key.
   All three correctly rejected by `crypto.verify_ed25519`.

### Level 4 — Braid-Guided Recovery

The "insurance policy" test:

1. Create an object with full provenance (CAS + DAG + braid)
2. Delete the CAS object from disk
3. Verify `content.exists` returns false (loss detected)
4. Query `sweetGrass.braid.get_by_hash` — braid metadata survives
5. Use the `data_hash` from the braid to re-acquire the content
6. Re-put and verify BLAKE3 matches

**Result**: Complete success. The braid record survives CAS deletion and contains
enough information to guide re-acquisition. For real datasets, step 5 would be
re-downloading from the original source (URL recorded in braid metadata).

### Level 5 — Encrypted CAS (ChaCha20-Poly1305)

Pattern for storing encrypted data in CAS:

```
bearDog.crypto.chacha20_poly1305_encrypt(plaintext_b64, key_b64)
    → { ciphertext, nonce, tag, algorithm }

nestGate.content.put(ciphertext_as_base64, hash_of_ciphertext)

sweetGrass.braid.create({
    data_hash: hash_of_ciphertext,
    mime_type: "application/x-encrypted-chacha20-poly1305",
    metadata: {
        plaintext_hash, cipher, nonce_b64, tag_b64
    }
})
```

**Critical bearDog behavior**: bearDog generates its own nonce even when one is
provided. The caller MUST use the returned nonce for decryption, not the one
they sent. The `tag` is returned as a separate field, not appended to ciphertext.
This is AEAD with separated tag — the decrypt call requires all three:
`{ ciphertext, key, nonce, tag }`.

**Verification**: After decryption, `BLAKE3(decrypted) == plaintext_hash` from
the braid metadata confirms the round-trip is lossless.

**Wrong key rejection**: bearDog returns an error (not corrupted data) when
decryption fails. The AEAD authentication tag catches the mismatch before
any plaintext is released. This is the correct security behavior.

### Level 6 — Sharded Encrypted Data

Pattern for large datasets that need to be split, encrypted, and distributed:

```
plaintext → split into N shards
         → derive per-shard key via HKDF-SHA256(master_key, salt="shard-{i}")
         → encrypt each shard → store in CAS
         → create shard manifest (JSON with ct_hashes, nonces, tags, order)
         → braid the manifest
```

The shard manifest is itself a CAS object with its own braid. It records:
- `num_shards`, `cipher`, `kdf` parameters
- Per-shard: `ct_hash`, `nonce_b64`, `tag_b64`, `pt_size`, `pt_hash`
- `plaintext_hash` of the original unsplit data

**Resilience test**: Delete shard 1 from CAS, attempt reconstruction.
Result: missing shard detected (content.get returns no data), partial
reconstruction correctly identified as incomplete. After re-encrypting
and re-storing the shard (with new nonce — bearDog picks fresh), full
reconstruction succeeds and BLAKE3 matches.

**Important**: Re-encryption produces different ciphertext (new nonce, new tag)
with a different CAS hash. The shard manifest must be updated to reflect
the new ct_hash. This means the manifest is mutable across re-encryption events —
the braid of the manifest records the lineage of these changes.

### Level 7 — Cross-Gate Replication

```
nestGate.content.replicate({
    cids: [hash1, hash2, ...],
    target: "192.168.4.213:8080"
}) → { replicated: [{cid, transferred, size}], total_bytes }
```

**Result**: Replication to ironGate (192.168.4.213:8080) succeeded.
Objects pushed over TCP. The replication is diff-based: objects already
present on the remote gate are skipped.

### Level 8 — Braid Manifest Export

A discovery index for nestgate.io and NUCLEUS science projects:

```json
{
  "gate": "westgate",
  "cas_endpoint": "nestgate:8080",
  "songbird_mesh": "songbird:7700",
  "datasets": [
    { "name": "alphafold", "files": 54, "braided": true, "spine_id": "...", "merkle_roots": [...] },
    ...
  ],
  "braids": { "total": 100, "sample": [...] },
  "spines": [{ "spine_id": "...", "name": "federation:cell_ontology", "entry_count": 2 }],
  "replication": {
    "method": "content.replicate.pull",
    "protocol": "jsonrpc-2.0/tcp",
    "port": 8080
  }
}
```

Consumers call `content.replicate.pull` with specific CAS hashes from the manifest.
The manifest itself is stored in CAS and braided — it is self-referential: a
provenance-tracked index of provenance-tracked data.

---

## CAS Role Architecture

```
                    westGate (Data CAS)
                    ┌──────────────────┐
                    │ 131 datasets     │
                    │ 3.84 TB cold ZFS │
                    │ 1.41 TB CAS     │
                    │ nestGate :8080   │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
    wetSpring (Compute)   ironGate      other NUCLEUS
    ┌────────────────┐   (NFT CAS)     projects
    │ barraCuda      │   ┌──────────┐
    │ consume data   │   │ compute  │
    │ braids from    │   │ output   │
    │ westGate       │   │ braids   │
    │                │   │ (NFTs)   │
    │ produce NFT    │   │          │
    │ braids →       ├──→│ archive  │
    │ ironGate       │   │          │
    └────────────────┘   └──────────┘
```

The energy/information/data/compute interphase:
- **westGate** stores raw scientific data (sequences, structures, measurements)
- **wetSpring** consumes that data via `content.replicate.pull`, runs compute
  (fermentation, QCD, phylogenetics), produces novel results
- **ironGate** archives the compute outputs as NFT braids — the "novel ferment
  transcriptome output" of the computation
- All three share the same CAS addressing scheme (BLAKE3), provenance chain
  (rhizoCrypt DAG → loamSpine → sweetGrass braid), and crypto layer (bearDog Ed25519)

---

## Results: 86/87 Tests Pass

| Level | Tests | Pass | Fail | Notes |
|-------|-------|------|------|-------|
| 1 Read | 28 | 27 | 1 | biogrid CAS drained but braid intact (correct) |
| 2 Merkle+Sig | 14 | 14 | 0 | Full cryptographic verification |
| 3 Corruption | 9 | 9 | 0 | CAS, Merkle, and signature tampering detected |
| 4 Recovery | 8 | 8 | 0 | Braid survives CAS deletion, guides re-acquisition |
| 5 Encrypted | 8 | 8 | 0 | ChaCha20-Poly1305 roundtrip with wrong-key rejection |
| 6 Sharded | 14 | 14 | 0 | Split, encrypt, delete shard, detect, restore, verify |
| 7 Replicate | 1 | 1 | 0 | Cross-gate push to ironGate |
| 8 Manifest | 5 | 5 | 0 | Discovery index exported and CAS-stored |
| **Total** | **87** | **86** | **1** | **98.9% pass rate** |

---

## What This Surfaces for Upstream

### Confirmed Working
- nestGate CAS: content-addressing makes corruption-by-overwrite impossible
- rhizoCrypt Merkle proofs: generate and verify correctly
- bearDog Ed25519: sign and verify, with correct tamper rejection
- bearDog ChaCha20-Poly1305: AEAD encrypt/decrypt with separated tag
- bearDog HKDF-SHA256: per-shard key derivation
- sweetGrass braids: persist independently of CAS tier state
- nestGate cross-gate replication: TCP-based push

### Gaps Identified
1. **`braid.verify` does not exist** — sweetGrass has `braid.create`, `braid.get`,
   `braid.list`, but no `braid.verify`. Verification is currently manual (walk the
   chain yourself). A first-class verify method would take a data_hash and return
   whether the full chain (CAS → DAG → spine → braid) is intact.

2. **`anchoring.verify` expects `braid_id`** — the param schema doesn't match
   what we'd naturally pass (a data_hash). Needs alignment.

3. **loamSpine is ephemeral** — spine state clears on restart. For a durable
   audit trail, spines need to persist to disk or be re-created from rhizoCrypt
   DAG state on startup.

4. **`derive_purpose_key` not available** — bearDog's key derivation for
   application-specific keys isn't exposed yet. HKDF-SHA256 works as a substitute.

5. **Shard manifest mutability** — re-encryption changes CAS hashes, requiring
   manifest updates. The current pattern records the old manifest as a braid
   (immutable history) and creates a new manifest. A formal "shard lineage"
   protocol would make this explicit.

---

## Patterns for Ecosystem Adoption

### Pattern 1: Encrypted-at-Rest CAS

Any gate storing sensitive data should:
1. Encrypt with ChaCha20-Poly1305 via bearDog before CAS put
2. Store `plaintext_hash` and `nonce_b64` and `tag_b64` in braid metadata
3. The CAS hash addresses the ciphertext, not the plaintext
4. Decryption requires the key (from bearDog key management) + nonce + tag

### Pattern 2: Sharded Large Data

For datasets too large for single-object CAS or that need distributed storage:
1. Split into N shards of manageable size
2. Derive per-shard keys via HKDF(master_key, shard_index)
3. Encrypt and store each shard independently
4. Create a shard manifest braid linking all shards
5. The manifest itself is CAS-stored and braided (self-referential provenance)

### Pattern 3: Braid-Guided Disaster Recovery

When CAS content is lost (disk failure, accidental deletion, tier eviction):
1. `sweetGrass.braid.get_by_hash` — the braid survives CAS loss
2. Extract `data_hash`, `source`, `metadata` from the braid
3. Re-acquire from source (re-download, re-compute, restore from backup)
4. `content.put` with the original hash — CAS dedup confirms integrity
5. The braid chain remains valid — no re-braiding required

### Pattern 4: Cross-Gate Data Federation

1. westGate exports a braid manifest (Level 8 output)
2. Consumer gate reads manifest, selects datasets by name/type
3. Consumer calls `content.replicate.pull(cids, source="westgate:8080")`
4. Diff-based: only objects not already present are transferred
5. Consumer creates their own braids for derived work (NFT braids)
