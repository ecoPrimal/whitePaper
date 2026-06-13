# riboCipher Signal Evolution — From Peek-and-Guess to Codon Reading

**Gen5 Foundation** (evolved from BTSP + genetic encryption)  
**Standard:** `wateringHole/RIBOCIPHER_TRANSPORT_SIGNAL_STANDARD.md`  
**Relationship:** Extends `TRANSPORT_EVOLUTION.md` (connection-level) and `BTSP_PROTOCOL_STANDARD.md` (security layer)

---

## Evolutionary Context

The ecoPrimals ecosystem's IPC security evolved through distinct eras:

| Era | Pattern | Problem |
|-----|---------|---------|
| **Pre-BTSP** | Plaintext JSON-RPC over UDS | Zero authentication, zero confidentiality |
| **BTSP** | Handshake-first, family seed auth | Secure but required knowing which protocol to expect |
| **Peek-and-Guess** | First byte determines protocol | Fragile — encrypted bytes look like noise |
| **riboCipher** | Intentional signal before payload | Deterministic routing, tiered security |

---

## The Biological Model

### Signal Peptide + Ribosome

In molecular biology, protein routing follows a precise signaling system:

1. **mRNA carries a signal codon sequence** at the 5' end
2. **The ribosome** translates this into a signal peptide
3. **The Signal Recognition Particle (SRP)** reads the signal peptide
4. The SRP **pauses translation** and routes the ribosome to the correct membrane
5. The protein is **translocated** to the target organelle

riboCipher maps this process to IPC:

| Biology | riboCipher |
|---------|------------|
| mRNA signal sequence | First 2-7 bytes on wire |
| Signal peptide | Tier prefix (0xEC/0xED/0xEE) + protocol type |
| Ribosome | Accept loop in primal server |
| SRP | Signal detection logic |
| Target membrane | Protocol handler (JSON-RPC, BTSP, HTTP, etc.) |
| Translation paused | No data consumed before routing decision |

### Why "Cipher"

In genetics, the genetic code is a **cipher** — a mapping from 3-nucleotide
codons to amino acids. It is:
- Fixed (same codons always map to same amino acids)
- Universal (all life uses it)
- Degenerate (multiple codons can map to the same amino acid)

riboCipher's protocol type table has the same properties:
- Fixed byte → protocol mapping
- Universal across the ecosystem (all primals read the same table)
- The three tiers can signal the same protocol type (redundant encoding)

---

## Relationship to BTSP

BTSP (BearDog-to-SongBird Transport Protocol) was the first primal-originated
security protocol. Named for the two primals that co-evolved it, BTSP provides:

- Family seed authentication (HKDF-SHA256 key derivation)
- Session key negotiation
- Encrypted frame transport (ChaCha20-Poly1305)
- PQC upgrade path (ML-KEM-768 hybrid)

**BTSP does not go away.** It remains the security handshake protocol for
authenticated/encrypted sessions. What changes is how a connection *declares*
that it wants to speak BTSP:

```
Before riboCipher:
  connect() → peek first byte → if '{' then JSON-RPC, else assume BTSP

After riboCipher:
  connect() → [0xEC][0x02] → server KNOWS client wants BTSP Binary
  connect() → [0xEC][0x01] → server KNOWS client wants NDJSON JSON-RPC
```

The signal is **intentional**, not inferred. The server never has to guess.

---

## Relationship to Genetic Encryption

The ecosystem's cryptographic genetics operate at three tiers:

| Tier | Key Material | Scope | riboCipher Mapping |
|------|-------------|-------|-------------------|
| **Mitochondrial** | `FAMILY_SEED` / mitoBeacon | All family members | Tier 2 signal (0xED) — HMAC tag derived from family seed |
| **Nuclear** | Nuclear lineage per-peer keys | Specific peer pairs | Tier 3 signal (0xEE) — encrypted with nuclear key |
| **Epigenetic** | Runtime session keys (BTSP negotiated) | Single connection | Post-signal, BTSP handshake establishes session |

riboCipher's tiered signals directly map to the existing genetic model:

- **Clear (0xEC)**: No genetic material needed. Local same-machine IPC where
  filesystem permissions provide authentication (the cell membrane itself).

- **Mito-obfuscated (0xED)**: Uses mitochondrial genetics (family seed) to
  prove family membership. The 4-byte HMAC tag is derived the same way as
  mitoBeacon group authentication. An outsider sees random bytes; family
  members can decode the protocol intent.

- **Nuclear-sealed (0xEE)**: Uses nuclear genetics (per-peer lineage keys)
  for full confidentiality of the signal itself. Even other family members
  cannot see what protocol two specific peers are negotiating.

### HKDF Domain Separation

riboCipher reuses the ecosystem's established HKDF pattern with new info strings:

```
// Existing genetics patterns
mitoBeacon_key = HKDF(salt="birdsong_beacon_v1", ikm=family_seed, info="beacon-auth")
btsp_key       = HKDF(salt="btsp-v1",            ikm=family_seed, info="session-key")

// riboCipher additions (same family_seed, new domains)
mito_signal    = HKDF(salt="ribocipher-v1",       ikm=family_seed, info="mito-signal")
nuclear_signal = HKDF(salt="ribocipher-v1",       ikm=nuclear_seed, info="nuclear-signal")
```

This is convergent evolution: the same cryptographic primitive (HKDF-SHA256),
the same root key material (family/nuclear seeds), different info strings
for domain separation. No new cryptographic dependencies introduced.

---

## The Jelly-Sting Problem (Why Peek Failed)

The peek-and-guess pattern emerged organically as primals independently
solved the "what does this connection want?" problem:

| Primal | Peek Logic | Failure Mode |
|--------|-----------|--------------|
| bearDog | `read_exact(1)`: `{` = JSON-RPC, else BTSP binary | BTSP ciphertext can start with `{` (probability 1/256) |
| songBird | `fill_buf()`: `{` = NDJSON, else BTSP | Same as bearDog + whitespace sensitivity |
| biomeOS | `fill_buf()`: `{`/`[` = JSON-RPC, else HTTP | Encrypted frames misrouted as HTTP |
| sweetGrass | `read_exact(1)` with whitespace skip | Most robust but still guessing |

**The critical failure**: When ironGate deployed full NUCLEUS with BTSP
encryption active, the first byte of an encrypted frame is
**indistinguishable from noise**. A peeked `0x7B` (`{`) in ciphertext
triggers JSON-RPC parsing of binary ciphertext → hung connection.

This is the "jelly-sting" pattern: a fragile solution that works in calm
waters but fails under stress. The system needed to evolve **intention**
where it previously relied on **inference**.

---

## Convergent Evolution

riboCipher was designed for convergent evolution, not imposed uniformity:

1. **Standard published** in wateringHole (the ecosystem's shared knowledge base)
2. **Each primal team independently evolves** their implementation
3. **No shared crate** — violates interprimal sovereignty
4. **sourDough accelerates** — new primals are born compliant, existing primals are audited
5. **Deprecation timeline** provides evolutionary pressure (warn → error → reject → remove)

The result: 9/9 primals converged within a single wave (Wave 111), each with
their own idiomatic Rust implementation. The implementations differ in detail
but share the same wire behavior — exactly like how different species evolve
convergent solutions (eyes, wings, echolocation) independently.

---

## Wire Format Summary

```
Tier 1 (Clear):    [0xEC][protocol_type: u8]           = 2 bytes
Tier 2 (Mito):     [0xED][hmac_tag: [u8; 4]]          = 5 bytes
Tier 3 (Nuclear):  [0xEE][encrypted_payload: [u8; 6]]  = 7 bytes
Legacy:            anything else → WARN + old behavior (deprecation period only)
```

Signal prefix bytes chosen to never collide with valid JSON (`{`=0x7B),
HTTP verbs (`G`=0x47, `P`=0x50), or NUL (0x00).

---

## Deprecation Timeline

| Wave | Behavior |
|------|----------|
| 111 | Standard published. All 9 primals SHIPPED. WARN on unsignalled. |
| 112 | ERROR on unsignalled. All clients must signal. |
| 113 | REJECT unsignalled connections (JSON-RPC error -32002). |
| 114 | Remove all legacy peek code. riboCipher-only. |

---

## Key Files

| File | Location | Purpose |
|------|----------|---------|
| `RIBOCIPHER_TRANSPORT_SIGNAL_STANDARD.md` | wateringHole | Ecosystem standard (normative) |
| `BTSP_PROTOCOL_STANDARD.md` | wateringHole | Security protocol (rides on riboCipher) |
| `TRANSPORT_EVOLUTION.md` | whitePaper/gen5/foundations | Topology-level evolution (nanowire → quorum) |
| This document | whitePaper/gen5/foundations | Connection-level signal evolution |
| `src/ribocipher.rs` | cellMembrane | Mito-tier reference (HKDF + HMAC) |
| `peek.rs` | sweetGrass | Convergence reference (signal-first, legacy-fallback) |
