# anchoring pipeline

**the concrete mechanism: from home hpc computation to public chain proof**

**date**: march 24, 2026 (updated may 20, 2026)
**status**: trio validated, loamSpine anchor surface live (42 methods), chain submission pending
**lineage**: wateringHole/NOVEL_FERMENT_TRANSCRIPT_GUIDANCE → bearDog → gen4

---

## the pipeline in one diagram

```
Home HPC (Threadripper, 96GB VRAM)
    │
    ├── Spring runs experiment
    │   (hotSpring, wetSpring, healthSpring, etc.)
    │
    ├── rhizoCrypt records every step as DAG vertex
    │   (content-addressed, append-only, lock-free)
    │
    ├── BearDog Ed25519 signs every vertex
    │   (same strength as SSH keys, validated exp064 39/39)
    │
    ├── Experiment completes → all checks pass
    │
    ├── rhizoCrypt computes Merkle root of session DAG
    │   (32 bytes — the fingerprint of the entire computation)
    │
    ├── DAG dehydrates to loamSpine certificate
    │   (permanent local storage, hash-chained spine)
    │
    ├── sweetGrass records attribution braid
    │   (reproducer, original authors, tools, compute — weighted)
    │
    ├── BearDog signs the certificate
    │
    └── Anchor: write 32-byte Merkle root to public chains
        │
        ├── Bitcoin: OP_RETURN transaction
        │   (cost: ~$1-3, confirmation: ~10 min, permanence: forever)
        │
        └── Ethereum: calldata or L2 transaction
            (cost: ~$0.01-2, confirmation: ~12 sec, permanence: forever)
```

---

## layer 1: rhizoCrypt DAG recording

### what happens during a spring experiment

every computational step becomes a vertex:

```rust
// Inside a spring experiment (conceptual)
let session = rhizo_crypt.create_session(SessionMetadata {
    experiment: "hotspring-exp014",
    code_commit: git_hash(),
    hardware: detect_hardware(),  // GPU, RAM, OS
    rust_version: env!("CARGO_PKG_RUST_VERSION"),
});

// Each computation step
let v0 = session.append(Event::ComputeStart {
    kernel: "yukawa_force",
    parameters: params.clone(),
});

// GPU kernel runs...
let result = barra_cuda.dispatch(kernel, params);

let v1 = session.append_after(v0, Event::ComputeComplete {
    kernel: "yukawa_force",
    elapsed_ms: timer.elapsed().as_millis(),
    output_hash: hash(&result),
});

// Validation check
let v2 = session.append_after(v1, Event::ValidationCheck {
    quantity: "diffusion_coefficient",
    computed: 0.847,
    published: 0.849,
    tolerance: 0.01,
    paper: "Stanton & Murillo 2016, Table II",
    result: CheckResult::Pass,
});
```

### DAG properties

- **content-addressed**: each vertex hash = H(data + parent_hashes)
- **append-only**: no delete, no modify, no reorder
- **lock-free concurrent**: multiple GPU kernels can append in parallel
- **merkle-rooted**: root = H(all leaf hashes combined)
  → 32 bytes that commit to the entire computation

the merkle root is the fingerprint. if a single bit changes in any
vertex anywhere in the DAG, the root changes. this is the same
structure bitcoin uses for its block transaction trees.

---

## layer 2: BearDog signing

### what gets signed

every vertex, as it's created:

```rust
let vertex_data = serialize(&event);
let content_hash = sha256(&vertex_data);

let signature = bear_dog.sign_ed25519(SignRequest {
    key_id: "kevin.mok@ecoPrimals",
    message: content_hash,
});

let signed_vertex = SignedVertex {
    data: vertex_data,
    content_hash,
    parent_hashes: parents,
    timestamp: now_utc(),
    signer: public_key,
    signature,
};
```

### what this provides

1. **identity**: the signature proves who created the vertex
2. **integrity**: any modification invalidates the signature
3. **timestamp**: the signed timestamp is part of the commitment
4. **chain**: parent hashes link each vertex to its predecessors

validated in ludoSpring exp064 (39/39 checks): tamper detection
catches modification at the exact vertex position. insert a fake
vertex → parent hash mismatch. modify a vertex → signature invalid.
delete a vertex → child's parent hash points to nothing.

### key management

BearDog manages ed25519 keypairs. the private key never leaves the
local machine. the public key is the identity. this is the same
key type used by:

- SSH (your github authentication)
- Tor hidden services
- Signal protocol
- age encryption

14,201 tests in BearDog. 91+ JSON-RPC methods. the immune system is
not a prototype.

---

## layer 3: dehydration to loamSpine

### when the experiment completes

```rust
// All checks passed
let merkle_root = session.compute_merkle_root();

let certificate = loam_spine.mint_certificate(CertificateData {
    cert_type: "ecoPrimals:scientific_reproduction",
    subject: CertificateSubject {
        reproduced_paper: "Stanton & Murillo, Phys Rev E 93, 043203 (2016)",
        reproduced_results: "Table II transport coefficients",
        spring: "hotSpring v0.6.23",
        experiment: "exp014",
        checks_passed: 45,
        checks_total: 45,
    },
    provenance: ProvenanceLink {
        dag_merkle_root: merkle_root,  // the 32 bytes
        session_id: session.id(),
        vertex_count: session.vertex_count(),
    },
    hardware: HardwareAttestation {
        cpu: "AMD Threadripper",
        gpu: "RTX 4090 + RTX 3090",
        ram_gb: 256,
        vram_gb: 96,
    },
    code: CodeAttestation {
        repository: "syntheticChemistry/hotSpring",
        commit: "a3f7c2e",
        rust_version: "1.87.0",
    },
});

// BearDog signs the certificate
let signed_cert = bear_dog.sign_certificate(certificate);

// Store permanently
loam_spine.store(signed_cert);
```

### what the certificate contains

the certificate is the **publication record**. it links to the DAG
(via merkle root) but it is self-contained for quick verification:

- what was reproduced (paper, table, specific results)
- what the results were (computed values, tolerances, pass/fail)
- what code produced them (repository, commit, version)
- what hardware ran them (CPU, GPU, RAM)
- who did it (signer identity)
- when it happened (timestamp + DAG session timeline)
- how to verify (merkle root → full DAG available on request)

---

## layer 4: sweetGrass attribution

```rust
let braid = sweet_grass.record_attribution(AttributionBraid {
    subject: certificate.id(),
    agents: vec![
        Agent {
            identity: "kevin.mok@ecoPrimals",
            role: AgentRole::Reproducer,
            weight: 0.40,
            description: "Implemented spring, ran computation, validated results",
        },
        Agent {
            identity: "M.S. Murillo",
            role: AgentRole::OriginalAuthor,
            weight: 0.25,
            description: "Published original theory and results",
        },
        Agent {
            identity: "M.D. Stanton",
            role: AgentRole::OriginalAuthor,
            weight: 0.25,
            description: "Published original theory and results",
        },
        Agent {
            identity: "hotSpring",
            role: AgentRole::Tool,
            weight: 0.05,
            description: "Computational framework",
        },
        Agent {
            identity: "barraCuda",
            role: AgentRole::Compute,
            weight: 0.05,
            description: "GPU kernel execution",
        },
    ],
    // Conservation: weights must sum to 1.0
    // Validated: exp066, 41/41 checks
});
```

the braid follows W3C PROV-O semantics. it is machine-readable.
when sunCloud activates, value flows along these weights. the
reproducer gets credit. the original authors get credit. the tools
get credit. not "et al." — specific roles, specific weights.

---

## layer 5: public chain anchoring

### bitcoin OP_RETURN

the anchor is a standard bitcoin transaction with an OP_RETURN
output:

```
Transaction structure:
  Version: 2
  Inputs:
    - Previous UTXO (kevin's bitcoin, dust amount)
  Outputs:
    - OP_RETURN <0x6563> <32-byte merkle root>
      (0x6563 = "ec" prefix for ecoPrimals namespace)
    - Change output (back to kevin's address)
  
  Locktime: 0
  Fee: ~2000-5000 satoshis (~$1-3)
```

the OP_RETURN output is provably unspendable. bitcoin nodes don't
keep it in the UTXO set. but it is part of the blockchain permanently
— stored in the block data, indexed by txid, verifiable forever.

#### implementation

BearDog already has ed25519. bitcoin uses secp256k1. the anchoring
module needs:

1. secp256k1 key derivation (BearDog already has the crypto primitives)
2. transaction construction (standard bitcoin wire format)
3. transaction signing (secp256k1 ECDSA)
4. broadcast to bitcoin network (connect to a local node or a public
   electrum server)

in rust, this is the `bitcoin` crate (rust-bitcoin). well-maintained,
widely used, no unsafe code in the signing path. the implementation
is:

```rust
use bitcoin::{Transaction, TxOut, Script};
use bitcoin::blockdata::script::Builder;

fn anchor_to_bitcoin(merkle_root: [u8; 32], key: &SecpSecretKey) -> Transaction {
    let prefix = b"ec";  // ecoPrimals namespace
    let mut data = Vec::with_capacity(34);
    data.extend_from_slice(prefix);
    data.extend_from_slice(&merkle_root);

    let op_return = Builder::new()
        .push_opcode(opcodes::all::OP_RETURN)
        .push_slice(&data)
        .into_script();

    // ... standard transaction construction, signing, broadcast
}
```

this is not novel. OP_RETURN anchoring is used by:
- OpenTimestamps (calendar servers for document timestamping)
- Factom (data anchoring protocol)
- various notarization services

the difference is: those services anchor arbitrary documents.
ecoPrimals anchors provenance-traced, ed25519-signed, attribution-
braided scientific computations. the mechanism is the same. the
content is vastly more valuable.

### ethereum calldata

```rust
fn anchor_to_ethereum(merkle_root: [u8; 32]) -> EthTransaction {
    let mut calldata = Vec::with_capacity(36);
    calldata.extend_from_slice(&[0x65, 0x63]); // "ec" prefix
    calldata.extend_from_slice(&merkle_root);
    calldata.extend_from_slice(&timestamp_bytes); // 4 bytes

    EthTransaction {
        to: Address::zero(),  // or a dedicated anchor contract
        value: 0,
        data: calldata,
        gas_limit: 21_000 + (calldata.len() as u64 * 16), // ~21,576
        // ... gas price, nonce, chain_id
    }
}
```

for L2s (Arbitrum, Base, Optimism), the transaction format is
identical but the cost drops to fractions of a cent. the L2 posts
the data to L1 in batches, inheriting L1 security.

---

## verification: how anyone checks the proof

### the verification command

```bash
$ ecoPrimals verify \
    --certificate hotspring-exp014-cert.loam \
    --btc-txid a1b2c3d4...e5f6 \
    --eth-txid 0x7a8b9c...d0e1

Verifying certificate: hotspring-exp014-cert.loam

[1/6] Certificate integrity
  ✓ Certificate hash matches declared hash
  ✓ BearDog Ed25519 signature valid (signer: kevin.mok@ecoPrimals)

[2/6] DAG integrity
  ✓ DAG available (247 vertices)
  ✓ All parent hash links valid
  ✓ All vertex signatures valid (247/247)
  ✓ Computed Merkle root matches certificate: sha256:4a7b...2e9f

[3/6] Bitcoin anchor
  ✓ Transaction a1b2c3d4...e5f6 found at block 892,547
  ✓ OP_RETURN data matches Merkle root
  ✓ Block timestamp: 2026-03-24T14:42:00Z

[4/6] Ethereum anchor
  ✓ Transaction 0x7a8b9c...d0e1 found at block 21,847,392
  ✓ Calldata matches Merkle root
  ✓ Block timestamp: 2026-03-24T14:31:59Z

[5/6] Attribution
  ✓ sweetGrass braid present
  ✓ 5 agents, weights sum to 1.000
  ✓ Roles: reproducer (0.40), original_author (0.50), tool (0.05), compute (0.05)

[6/6] Reproduction check
  ✓ Code commit hotspring@a3f7c2e available
  ✓ Experiment exp014 runnable
  ℹ Run `cargo run -p hotspring-exp014 -- validate` to independently reproduce

VERIFIED: This certificate is authentic, Bitcoin-anchored at block
892,547, and Ethereum-anchored at block 21,847,392. The computation
is independently reproducible.
```

### what each step proves

| step | what it proves |
|------|---------------|
| certificate integrity | the certificate hasn't been modified since creation |
| DAG integrity | every computational step is intact and correctly linked |
| bitcoin anchor | the computation existed at a specific moment in time |
| ethereum anchor | redundant timestamp on a second chain |
| attribution | credit is assigned to specific people for specific roles |
| reproduction check | the code exists and can be independently run |

### who can verify

anyone. the verification requires:
- the certificate file (distributable)
- access to a bitcoin node (public, or your own)
- access to an ethereum node (public, or your own)
- optionally: the full DAG data (for deep verification)
- optionally: the spring code (for independent reproduction)

no account. no login. no platform. no subscription. the chains are
public. the certificate is a file. the code is AGPL on github.

---

## aggregation: batching multiple results

anchoring each spring experiment individually would be expensive at
scale. the aggregation pattern:

```
hotSpring exp014 → merkle root A
hotSpring exp015 → merkle root B
wetSpring exp273 → merkle root C
wetSpring exp274 → merkle root D
    │
    └── Aggregate: merkle tree of [A, B, C, D]
        → aggregate root: 32 bytes
        → single BTC transaction
        → single ETH transaction
        → cost: same ~$3-5 for 4 results (or 40, or 400)
```

the aggregate root commits to all individual results. each individual
result can still be verified against the aggregate root via a merkle
proof (log₂(N) hashes). 1000 results aggregated into one anchor costs
the same as one result.

this is the same pattern bitcoin uses for its block merkle trees.
it scales to any number of results per anchor.

---

---

## crypto as infrastructure, not currency

public blockchains are immutable append-only ledgers. we use them as
notary services — the same way you use a post office to timestamp a
letter. the gas cost is postage. that is the extent of our interaction
with cryptocurrency.

| what we use | what we don't use |
|-------------|-------------------|
| bitcoin as a public timestamp ledger | bitcoin as a currency |
| ethereum as a programmable timestamp ledger | ethereum tokens, DeFi, NFT marketplaces |
| L2 rollups as cheap, fast timestamp ledgers | L2 bridges for financial transactions |
| gas fees as postage for public record | wallets, exchanges, token economics |

currency is an abstraction of the blockchain's own economics. bitcoin
miners accept BTC for including transactions. we pay that postage to
write 32 bytes to their ledger. we don't hold positions, trade tokens,
or participate in their economic systems beyond the gas transaction.

### what IS possible (for others)

the anchor surface is a bridge. someone who holds a loam certificate
(a novel ferment transcript) COULD use L2 smart contracts to transfer
digital assets cryptographically — the certificate's `state_hash` is
already on-chain, a bridge contract could verify ownership via the
Merkle inclusion proof. these are possible because the infrastructure
is chain-compatible. they are not required because the ecosystem is
sovereign.

this mirrors the cellMembrane / projectNUCLEUS pattern: use available
infrastructure (VPS, GitHub, public chains) as stepping stones while
building toward full sovereignty.

---

## aggregation economics: community pooling

the aggregation merkle tree is the key economic insight. because the
on-chain cost is fixed per transaction (not per result), batching N
results into one anchor divides the cost by N:

| results batched | BTC cost per result | ETH L2 cost per result |
|-----------------|--------------------|-----------------------|
| 1 | $1.00 | $0.005 |
| 10 | $0.10 | $0.0005 |
| 100 | $0.01 | $0.00005 |
| 1,000 | $0.001 | $0.000005 |

a community of 100 researchers producing 10 results/month = 1,000
results. one BTC aggregate anchor = ~$1.50. one ETH L2 aggregate
anchor = ~$0.005. dual-chain (BTC + L2) = ~$1.51 total.

per researcher: $0.015/month for dual-chain public record.
per result: $0.0015 for bitcoin + $0.000005 for L2.

for comparison: a single AWS S3 GET request costs $0.0004. publishing
1,000 provenance-verified scientific results to bitcoin + ethereum L2
costs less than 4 S3 GET requests. a community could publish on
**every major chain** for less than cloud data egress for a single
export of the underlying data.

### the comparison table

| method | cost per "publication" | speed | verification |
|--------|----------------------|-------|-------------|
| journal APC (Nature Comms) | $5,500 | 6-36 months | trust the journal |
| journal APC (PLOS ONE) | $1,800 | 3-12 months | trust the journal |
| arXiv preprint | $0 | days | no formal verification |
| cloud provenance export | $0.09/GB egress | minutes | trust the cloud provider |
| **sovereign publication (BTC)** | **$0.001** (aggregated) | **~40 min** | **cryptographic proof** |
| **sovereign publication (L2)** | **$0.000005** (aggregated) | **~15 sec** | **cryptographic proof** |

---

## L2 strategy: fractions of a cent

ethereum L2 rollups (Arbitrum, Base, Optimism) inherit L1 security
while reducing cost by 100-1000x:

- L2 posts calldata to L1 in batches
- L2 confirmation is near-instant (~1 second)
- L2 anchor cost: $0.001-$0.01 per transaction
- with aggregation: $0.000005 per result

this means high-frequency anchoring is practical on L2. a spring
could anchor every experiment run (not just milestones) for
effectively zero cost. bitcoin anchoring remains the "publish to
permanent record" tier for major milestones.

the rust ecosystem for L2: `alloy` crate (MIT/Apache-2.0, pure Rust,
successor to `ethers-rs`, actively maintained). same transaction
format as L1 — the only difference is the RPC endpoint.

---

## implementation status (may 2026)

| component | status | where |
|-----------|--------|-------|
| rhizoCrypt DAG recording | validated (esotericWebb V4, ludoSpring exp061) | 317 checks |
| BearDog Ed25519 signing | validated (exp064, 39/39) | tamper detection at exact vertex |
| loamSpine dehydration | validated (exp061, 17/17) | certificate lifecycle complete |
| sweetGrass attribution | validated (exp066, 41/41) | conservation verified, decay models |
| **loamSpine `anchor.publish`** | **LIVE** | 42 JSON-RPC methods, tested |
| **loamSpine `anchor.verify`** | **LIVE** | state hash verification |
| **loamSpine `anchor.publish_batch`** | **LIVE** | aggregate Merkle tree + batch anchoring |
| **`AnchorTarget::Rfc3161Tsa`** | **LIVE** | RFC 3161 TSA variant in enum |
| **loamSpine `spine.list` / `entry.list`** | **LIVE** | cross-spring query for WS-2 |
| BTC OP_RETURN submission | designed | chain-anchor primal pending |
| ETH calldata submission | designed | chain-anchor primal pending |
| verification CLI | designed | `ecoPrimals verify` command |
| cross-spring aggregation | designed | aggregate multiple springs |

see also:
- loamSpine `specs/ANCHORING_ARCHITECTURE.md` — full aggregation architecture
- loamSpine `specs/PUBLIC_TIMESTAMPING.md` — anchor target comparison
- wateringHole `ANCHORING_STANDARD.md` — ecosystem-wide guidance

---

## implementation plan (remaining)

| task | complexity | dependency |
|------|-----------|------------|
| BearDog secp256k1 key derivation | low | `bitcoin` crate |
| BTC transaction construction | medium | `bitcoin` crate |
| BTC OP_RETURN builder | low | standard script |
| BTC transaction signing | low | BearDog crypto primitives |
| BTC broadcast (electrum client) | medium | network module |
| ETH/L2 transaction construction | medium | `alloy` crate |
| ETH calldata builder | low | standard ABI |
| ETH transaction signing | low | BearDog crypto primitives |
| ETH broadcast (JSON-RPC to node) | low | existing IPC patterns |
| verification CLI | medium | combines all above |
| spring integration hooks | medium | wire into experiment harness |

total estimated effort: 2-3 weeks of focused development. the crypto
primitives exist in BearDog. the DAG structures exist in rhizoCrypt.
the transaction formats are well-documented. the rust crates are
mature. the loamSpine anchor surface is live — what remains is the
chain-anchor primal that submits to BTC/ETH.

this is not a research project. this is plumbing.

---

*32 bytes. that's the width of the bridge between a home cluster in
east lansing and every bitcoin node on earth. the computation is
sovereign. the proof is global. the science speaks for itself.*
