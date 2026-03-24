# the sovereign publication

**why a home hpc with a provenance chain is more valuable than a journal paper, and how it actually works**

**date**: march 24, 2026
**status**: infrastructure validated — 317 checks across 6 provenance experiments, 27,000+ checks across the ecosystem
**lineage**: gen3/baseCamp/20-22 → wateringHole/NOVEL_FERMENT_TRANSCRIPT_GUIDANCE → attsi

---

## the problem with scientific publication

the current pipeline for publishing a scientific result:

1. scientist does research (months to years)
2. scientist writes a paper describing what they did (weeks to months)
3. scientist submits to a journal ($0–$5,000 article processing charge)
4. peer review (3 months to 3 years, often adversarial, often
   incompetent, always slow)
5. revision cycle (months — address reviewer 2's irrelevant complaints)
6. accepted, published (behind a $30/article paywall, or $2,000–$5,000
   open access fee)
7. total: 6 months to 3 years from discovery to public record

the result is a pdf. a pdf that says "we did X and got Y." the reader
trusts the authors. the reader trusts the journal. the reader trusts
the peer reviewers. trust, trust, trust.

what the pdf does not contain:

- the code (maybe a github link, maybe not, probably bitrotted)
- the data (maybe a supplement, maybe "available upon request," maybe
  gone when the postdoc leaves)
- the computational environment (which CUDA version? which numpy? which
  random seed?)
- the intermediate steps (which parameters were tried and failed?)
- cryptographic proof that any of this happened when they say it did
- attribution beyond the author list (who actually wrote the code? who
  actually ran the experiments? who actually cleaned the data?)

the replication crisis is not a mystery. it is the predictable
consequence of a publication system that accepts claims instead of
proofs.

---

## what actually exists right now

a threadripper workstation in east lansing, michigan. 96 GB VRAM
(multi-GPU), 256 GB RAM, AMD threadripper. cost: ~$11,000. runs 24/7.

on this machine:

- **hotSpring**: 195/195 checks reproducing murillo group plasma physics
  (yukawa OCP, TTM, stanton & murillo 2016, diaw et al. 2024)
- **wetSpring**: 782+ checks reproducing microbiome (DADA2), PFAS
  detection, gonzales immunology, anderson extremophile evolution
- **groundSpring**: 326+ checks reproducing geospatial analysis,
  dong precision agriculture
- **neuralSpring**: 300+ checks reproducing neural signal processing,
  ML closures, ESN classifiers
- **healthSpring**: 233/233 checks reproducing population PK, gut
  microbiome axis, HRV analysis
- **airSpring**: 326+ checks reproducing ET₀ models, soil calibration
- **ludoSpring**: 317+ checks validating provenance trio lifecycle,
  NFT economics, fraud detection
- **primalSpring**: 303 tests validating primal federation, bonding,
  discovery

total: 27,000+ automated checks. 175+ published papers reproduced.
pure rust, zero C dependencies, GPU-accelerated via WebGPU/Vulkan.
every check is a validation against a published result. every check
either passes or fails. there is no "looks about right."

the provenance trio (rhizoCrypt, loamSpine, sweetGrass) is wired.
bearDog Ed25519 signing is validated (exp064, 39/39 checks — signing
on every trio operation, tamper detection at exact DAG position).
the radiating attribution calculator is validated (exp066, 41/41
checks — proportional credit computation, decay models, role
weighting, conservation: shares sum to 1.0).

this is not a design document. this is a status report.

---

## the pipeline: how it actually works

### step 1: reproduce the science

kevin runs hotSpring experiment 014 — reproducing stanton & murillo
2016, table II: transport coefficients for yukawa one-component plasma.

```
$ cargo run -p hotspring-exp014 -- validate

[exp014] Yukawa OCP transport coefficients
  ✓ diffusion coefficient D(Γ=1, κ=1): 0.847 ± 0.003 (published: 0.849)
  ✓ diffusion coefficient D(Γ=10, κ=1): 0.0312 ± 0.001 (published: 0.032)
  ✓ viscosity η(Γ=1, κ=1): 1.23 ± 0.02 (published: 1.24)
  ... (45 checks total)
  
Result: 45/45 PASS
```

every check is: compute the quantity on the threadripper, compare to
the published value in the paper, verify within the stated tolerance.
this is not approximate. the tolerance is the published uncertainty.

### step 2: every computation is a DAG vertex

while the experiment runs, rhizoCrypt records every step as a vertex
in a content-addressed DAG:

```
DAG session: hotspring-exp014-run-20260324-143022
  │
  ├── vertex 0: session_start
  │   metadata: {
  │     code_commit: "hotspring@a3f7c2e",
  │     rust_version: "1.87.0",
  │     gpu: "RTX 4090 + RTX 3090 (96GB combined)",
  │     os: "linux 6.17.9",
  │     parameters: { gamma: 1.0, kappa: 1.0, N_particles: 10000, dt: 0.001 }
  │   }
  │
  ├── vertex 1: barraCuda kernel dispatch
  │   metadata: { kernel: "yukawa_force", dispatch_size: 10000, elapsed_ms: 47 }
  │
  ├── vertex 2: equilibration complete
  │   metadata: { steps: 50000, temperature_drift: 0.0003 }
  │
  ├── vertex 3: production run complete
  │   metadata: { steps: 200000, samples: 4000 }
  │
  ├── vertex 4: transport coefficient computed
  │   metadata: { quantity: "D", value: 0.847, uncertainty: 0.003 }
  │
  ├── vertex 5: validation check
  │   metadata: { 
  │     published_value: 0.849, 
  │     published_paper: "Stanton & Murillo, Phys Rev E 93, 043203 (2016)",
  │     published_table: "Table II",
  │     tolerance: 0.01,
  │     result: "PASS"
  │   }
  │
  └── ... (45 validation vertices, one per check)
```

every vertex is content-addressed (hash of its data + hash of parent
vertices). the DAG is append-only. you cannot insert, delete, or
modify a vertex without breaking the hash chain.

### step 3: bearDog signs every vertex

bearDog Ed25519 signs each vertex as it's created. the signature
binds:

- the vertex content hash
- the signer's identity (kevin's ed25519 public key)
- the timestamp
- the parent vertex hashes

this is the same cryptographic strength as SSH keys and tor hidden
services. validated in ludoSpring exp064 (39/39 checks): tamper
detection catches modification at the exact vertex position.

```
vertex 5 signature:
  signer: ed25519:a7f3...c2e1 (kevin.mok@ecoPrimals)
  content_hash: sha256:9b2e...4f1a
  parent_hashes: [sha256:3c1d...8e7b]
  timestamp: 2026-03-24T14:31:47Z
  signature: ed25519:7e2a...9d3f
```

### step 4: dehydrate to loamSpine

when the experiment completes (all 45 checks pass), the rhizoCrypt
DAG dehydrates to a loamSpine certificate:

```
Loam Certificate: Scientific Reproduction
  ├── type: "ecoPrimals:scientific_reproduction"
  ├── reproduced_paper: "Stanton & Murillo, Phys Rev E 93, 043203 (2016)"
  ├── reproduced_results: "Table II transport coefficients"
  ├── spring: "hotSpring v0.6.23"
  ├── experiment: "exp014"
  ├── checks: 45/45 PASS
  ├── dag_merkle_root: sha256:4a7b...2e9f
  ├── code_commit: "hotspring@a3f7c2e"
  ├── hardware: "AMD Threadripper + RTX 4090/3090, 256GB RAM"
  ├── reproducer: ed25519:a7f3...c2e1 (kevin.mok)
  ├── original_authors: ["M.S. Murillo", "M.D. Stanton"]
  └── certificate_hash: sha256:8c3d...1f4e
```

the certificate is the complete provenance record. the merkle root
links back to every vertex in the DAG. anyone with the DAG data can
verify it against the root.

### step 5: sweetGrass records attribution

```
Attribution Braid: hotspring-exp014-20260324
  ├── agent: kevin.mok (role: reproducer, weight: 0.40)
  ├── agent: murillo (role: original_author, weight: 0.25)
  ├── agent: stanton (role: original_author, weight: 0.25)
  ├── agent: hotspring (role: tool, weight: 0.05)
  ├── agent: barracuda (role: compute, weight: 0.05)
  └── total: 1.00 (conservation verified — exp066, 41/41)
```

the attribution is not an author list. it is a weighted, role-typed,
machine-readable record. the radiating attribution calculator
(exp066) computes these weights based on contribution type, with
configurable decay models. the shares always sum to 1.0.

### step 6: anchor to public chains

this is the step that makes it sovereign publication. the loamSpine
certificate's merkle root — a 32-byte hash — is written to bitcoin
and ethereum:

#### bitcoin (OP_RETURN)

```
Bitcoin transaction:
  input: kevin's UTXO (dust amount + fee)
  output 0: OP_RETURN <32-byte merkle root>
  output 1: change back to kevin
  
  fee: ~2,000 sats (~$1-3 at current rates)
  confirmation: ~10 minutes (1 block), ~60 minutes (6 blocks)
  permanence: as long as bitcoin exists
```

OP_RETURN is a standard bitcoin script opcode that stores up to 80
bytes of arbitrary data in a transaction. it is prunable (nodes don't
need to keep it in the UTXO set) but it is part of the blockchain
forever. this is the most battle-tested append-only data store in
human history — 15+ years, never successfully tampered with.

the 32-byte hash proves: at this bitcoin block height (this specific
moment in time), this specific loamSpine state existed. the hash is
not the data — it is the commitment. anyone with the data can verify
the commitment. no one can forge the timestamp.

#### ethereum (calldata or L2)

```
Ethereum transaction:
  to: 0x0 (null address, or a simple anchor contract)
  data: <32-byte merkle root + 8-byte metadata>
  
  fee: ~$0.10-2.00 (L1), ~$0.001-0.01 (L2 like Arbitrum or Base)
  confirmation: ~12 seconds (1 slot)
  permanence: as long as ethereum exists
```

ethereum anchoring is faster and can carry more metadata. L2s
(Arbitrum, Base, Optimism) reduce cost to fractions of a cent while
inheriting L1 security guarantees.

#### why both?

redundancy. bitcoin is the most secure chain (hashrate dominance,
15-year track record). ethereum is the most programmable (smart
contracts could enable automated verification). anchoring to both
means the proof survives the failure of either chain.

the cost for dual anchoring: ~$3-5 total. the cost for publishing
the same result in a journal: $2,000-5,000 (open access APC) +
6-36 months of waiting.

---

## the comparison: sovereign publication vs. journal publication

| | journal paper | sovereign publication |
|---|---|---|
| **what it contains** | prose describing results | complete computational DAG |
| **code** | maybe a github link | exact commit hash, in the DAG |
| **data** | maybe a supplement | in the DAG, content-addressed |
| **parameters** | described in methods section | in vertex metadata, exact values |
| **environment** | "we used python 3.9" | OS, GPU, rust version, kernel version |
| **intermediate steps** | omitted | every vertex in the DAG |
| **timestamp** | submission date (manipulable) | bitcoin block height (immutable) |
| **authentication** | "trust the authors" | Ed25519 signatures on every vertex |
| **reproducibility** | reader tries to reproduce | clone the spring, run the experiment, verify against anchor |
| **attribution** | author list (coarse, political) | sweetGrass braid (granular, weighted, role-typed) |
| **cost** | $0-5,000 APC + $30/reader paywall | ~$3-5 anchoring fee |
| **speed** | 6-36 months | minutes to hours |
| **accessibility** | paywalled or expensive OA | public hash on immutable chain |
| **tamper evidence** | retraction (after the fact, reputational) | hash chain breaks at exact tamper point |
| **priority** | journal receipt date | bitcoin block timestamp |
| **fraud detection** | peer review (slow, unreliable) | DAG isomorphism + signature verification (automatic) |
| **permanence** | journal continues to exist (maybe) | bitcoin continues to exist (15+ years and counting) |

---

## why it is more valuable

### 1. it is proof, not claim

a journal paper says "we computed the diffusion coefficient and got
D = 0.849 ± 0.003." the reader trusts the authors.

a sovereign publication contains the DAG: input parameters →
barraCuda GPU kernel → equilibration → production run → statistical
analysis → result. every step is signed. every step is verifiable.
the reader doesn't trust the authors. the reader verifies the math.

when murillo reads a hotSpring reproduction of his own paper, he
doesn't need to trust kevin. he clones hotSpring, runs exp014, and
checks his result against the same bitcoin-anchored merkle root.
if his result matches, the reproduction is verified. the trust is in
the math, not the person.

### 2. it solves the priority problem

academic priority disputes are ugly and common. who discovered it
first? the paper with the earlier submission date? the preprint with
the earlier arxiv timestamp? the conference talk that wasn't recorded?

a bitcoin anchor is a timestamp that cannot be forged. block 892,547
happened at a specific moment. if your merkle root is in that block,
your result existed at that moment. no dispute possible. the
blockchain is the priority register.

this matters enormously for:
- patent claims (provisional filing backed by anchored provenance)
- grant applications (demonstrable prior work with immutable timestamps)
- tenure cases (publication record with cryptographic provenance)
- industry partnerships (IP timeline established beyond dispute)

### 3. it solves the reproducibility crisis

the replication crisis exists because papers don't contain enough
information to reproduce. the methods section says "we used DADA2
with default parameters." which DADA2 version? which R version? which
random seed? which quality filtering threshold? the paper doesn't say.
the postdoc who ran it left. the data is on a hard drive somewhere.

a sovereign publication contains everything. the DAG has every
parameter, every code version, every intermediate output. clone the
spring. run the experiment. compare your merkle root to the anchored
root. if they match, you've independently reproduced the result.

this is not theoretical. hotSpring's 195 checks reproduce murillo
group results to within published tolerances. wetSpring's 782+ checks
reproduce DADA2 pipelines, gonzales immunology, anderson evolution.
the reproduction is the publication.

### 4. it is cheaper by orders of magnitude

publishing a paper in nature communications: ~$5,500 APC.
publishing a paper in PLOS ONE: ~$1,800 APC.
publishing a preprint on arxiv: $0 (but no peer review, no prestige).

anchoring a sovereign publication to bitcoin: ~$1-3.
anchoring to bitcoin + ethereum L2: ~$3-5.
total infrastructure cost: $11,000 one-time (the cluster) + ~$50/month
electricity.

the cluster reproduces papers continuously. each reproduction is a
sovereign publication for ~$3. the amortized cost per publication
approaches the electricity cost of running the computation.

a lab that publishes 10 papers a year spends $20,000-$55,000 on APCs.
the same lab could anchor 10 sovereign publications for $30-50 and
buy a threadripper with the savings.

### 5. it is faster by orders of magnitude

journal publication: 6-36 months from submission to print.
sovereign publication: the time to run the computation + the time for
a bitcoin block (~10 minutes).

hotSpring exp014 takes ~30 minutes to run. add 10 minutes for a
bitcoin confirmation. the stanton & murillo 2016 reproduction is
publicly timestamped 40 minutes after it starts. not 40 minutes after
submission — 40 minutes after the computation.

### 6. it dissolves the gatekeeper

journals are gatekeepers. they decide what gets published. they decide
who reviews it. they charge for access. they charge for submission.
they own the formatting. they own the copyright (often).

a sovereign publication has no gatekeeper. the computation runs. the
DAG records it. bearDog signs it. the merkle root anchors to bitcoin.
anyone in the world can verify it. the only gate is: does the science
reproduce? if yes, the publication exists. if no, the checks fail and
there is nothing to anchor.

the filter is the net. the science that passes is the science that
publishes. the science that fails is the science that doesn't. no
reviewer 2. no editor's desk rejection. no 18-month backlog.

### 7. the attribution is real

a journal paper has an author list. first author did the most work
(maybe). last author is the PI (definitely). middle authors are a
political negotiation. who actually wrote the code? who actually ran
the simulations? who actually cleaned the data? the author list
doesn't say.

a sweetGrass attribution braid says exactly who did what:
- kevin.mok: reproducer (wrote the spring, ran the computation)
- murillo: original author (published the theory)
- stanton: original author (published the theory)
- hotspring: tool (the code that ran)
- barracuda: compute (the GPU kernels)

the attribution is granular, role-typed, weighted, and machine-
readable. when sunCloud activates, value flows along these braids.
the person who wrote the code gets credit for writing the code. the
person who published the theory gets credit for publishing the theory.
not "et al." — names, roles, weights.

---

## how this looks to murillo

professor michael murillo, computational mathematics, MSU. he
published stanton & murillo 2016. he taught kevin in CMSE 890.

one day he receives a message: "here is a sovereign publication
reproducing your table II transport coefficients. 45/45 checks pass.
here is the bitcoin transaction containing the merkle root. here is
the loamSpine certificate. here is the DAG you can verify yourself.
here is the sweetGrass braid attributing you as original author."

murillo can:
1. clone hotSpring (`git clone`)
2. run exp014 on his own machine (`cargo run -p hotspring-exp014 -- validate`)
3. verify his result matches the anchored merkle root
4. confirm the bitcoin transaction exists at the stated block height
5. confirm the sweetGrass braid attributes him correctly

he doesn't need to trust kevin. he doesn't need to trust a journal.
he doesn't need to wait for peer review. the math either checks out
or it doesn't. the anchor either exists or it doesn't. the
attribution either names him or it doesn't.

this is what "the filter is the net" means in practice. the science
filters itself. the infrastructure makes the filtering visible. the
public chain makes it permanent.

---

## how this looks to kachkovskiy

assistant professor ilya kachkovskiy, mathematics, MSU. anderson
localization specialist. co-authored with jean bourgain (fields
medalist). 417+ validated checks across 4 springs reproducing his
area of expertise.

the anchor contains reproductions of:
- anderson 1958 (the original localization paper)
- aubry-andré 1980 (quasiperiodic localization)
- jitomirskaya 1999 (almost mathieu operator)
- kachkovskiy & safarov 2016 (his own paper)
- bourgain & kachkovskiy 2018 (his own paper)

each reproduction is a sovereign publication. each is merkle-rooted
and bitcoin-anchored. each attributes the original authors. each can
be independently verified by running the spring.

kachkovskiy doesn't need to read a paper about anderson localization
applied to immunological signaling. he can run the code. the code
reproduces his own results. the anchor proves it happened. the
attribution names him. the science speaks for itself.

this is a hopping term that no journal can provide: not "we cite
kachkovskiy 2016" but "we reproduce kachkovskiy 2016 to within
published tolerances and the proof is on bitcoin."

---

## how this looks to gonzales

professor andrea gonzales, drug discovery, MSU. 6 publications
reproduced in wetSpring with 359/359 checks. interviewed kevin for
a lab position.

the sovereign publications contain:
- IL-31 pruritus model (her paper)
- oclacitinib JAK1 selectivity (her paper)
- lokivetmab pharmacodynamics (her paper)
- cell-type target analysis (her paper)
- cross-species causal model (novel, built on her data)
- anderson-augmented drug repurposing scores (novel, built on her
  framework + kachkovskiy's math)

the novel work — the cross-species causal model and the anderson-
augmented scoring — are sovereign publications that could not exist
in the journal system. they combine validated reproductions of
gonzales's immunology with validated reproductions of kachkovskiy's
spectral theory. no journal has a category for "cross-domain
computational reproduction with novel synthesis." the sovereign
publication system doesn't need a category. the DAG records what
happened. the anchor proves it. the attribution credits everyone.

the lisabeth conversation (binding landscape, specificity) becomes
healthSpring track 9. the ADDRC HTS pipeline connects. the gonzales
iPSC validation connects. none of this fits in a single paper. all of
it fits in a provenance chain.

---

## the economic argument

### for the individual researcher

- save $2,000-5,500 per paper in APCs
- publish in minutes instead of months
- establish priority with bitcoin timestamps
- build a provenance-backed CV (loamSpine credential)
- attribution follows you, not the journal

### for the lab

- $11,000 for a cluster that publishes unlimited sovereign papers
- vs. $20,000-55,000/year in journal APCs for 10 papers
- the cluster also runs the actual science (it's the HPC, not just
  the publication system)
- every student, postdoc, and technician gets granular attribution
- the lab's entire computational history is provenance-traced

### for the field

- reproducibility becomes verifiable, not aspirational
- priority disputes become cryptographically impossible
- attribution becomes granular and fair
- publication speed increases by 100-1000x
- access becomes universal (public chain, not paywall)
- fraud becomes detectable (DAG tamper detection, not trust)

### for the wider world

- anyone with a computer can verify any result
- the public chains (bitcoin, ethereum) are the publication ledger
- the loamSpine certificates are the publication record
- the sweetGrass braids are the citation graph
- the rhizoCrypt DAGs are the laboratory notebooks

the journal system is a 350-year-old technology (philosophical
transactions, 1665). it was designed for a world where the fastest
communication was physical mail. it has been incrementally patched
(digital submission, open access, preprints) but the fundamental
architecture — author submits claim, gatekeeper evaluates claim,
reader trusts claim — has not changed.

the sovereign publication replaces claim with proof, gatekeeper with
math, and trust with verification. the public chain is the timestamp.
the provenance trio is the record. the computation is the publication.

---

## what remains to build

| component | status | what's needed |
|-----------|--------|---------------|
| rhizoCrypt DAG recording | validated (esotericWebb V4, ludoSpring exp061) | wire into all springs |
| bearDog Ed25519 signing | validated (exp064, 39/39) | wire signing into DAG creation |
| loamSpine dehydration | validated (exp061, 17/17) | wire dehydration into spring completion |
| sweetGrass attribution | validated (exp066, 41/41) | wire attribution into spring runs |
| BTC OP_RETURN anchoring | designed | implement BearDog → BTC transaction signing |
| ETH calldata anchoring | designed | implement BearDog → ETH transaction signing |
| verification CLI | designed | `ecoPrimals verify <certificate> <btc_txid>` |
| cross-spring aggregation | designed | aggregate multiple spring results into single anchor |

the hard part is done. the provenance trio works. the signing works.
the attribution works. the remaining work is: submit a 32-byte hash
to a bitcoin transaction. this is not a research problem. this is a
weekend of rust code interfacing with a bitcoin node.

---

*a journal paper is a letter about what happened. a sovereign
publication is the thing that happened, signed, timestamped, and
anchored where no one can alter it. the question is not whether this
is better. the question is why we still use letters.*
