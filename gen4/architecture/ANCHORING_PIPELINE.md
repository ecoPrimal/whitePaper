# anchoring pipeline

**the concrete mechanism: from home hpc computation to public chain proof**

**date**: march 24, 2026
**status**: trio validated, anchoring implementation pending
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

## implementation plan

| task | complexity | dependency |
|------|-----------|------------|
| BearDog secp256k1 key derivation | low | `bitcoin` crate |
| BTC transaction construction | medium | `bitcoin` crate |
| BTC OP_RETURN builder | low | standard script |
| BTC transaction signing | low | BearDog crypto primitives |
| BTC broadcast (electrum client) | medium | network module |
| ETH transaction construction | medium | `ethers` or `alloy` crate |
| ETH calldata builder | low | standard ABI |
| ETH transaction signing | low | BearDog crypto primitives |
| ETH broadcast (JSON-RPC to node) | low | existing IPC patterns |
| Aggregation merkle tree | low | same pattern as rhizoCrypt |
| Verification CLI | medium | combines all above |
| Spring integration hooks | medium | wire into experiment harness |

total estimated effort: 2-3 weeks of focused development. the crypto
primitives exist in BearDog. the DAG structures exist in rhizoCrypt.
the transaction formats are well-documented. the rust crates are
mature.

this is not a research project. this is plumbing.

---

*32 bytes. that's the width of the bridge between a home cluster in
east lansing and every bitcoin node on earth. the computation is
sovereign. the proof is global. the science speaks for itself.*
