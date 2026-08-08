# Neural API as Provenance Routing Substrate

**Status**: Stage 1 complete (direct primal sockets); Stage 2 in progress
(capability.call routing through biomeOS neural-api)

## From Concept to Primals to Reality

The ecoPrimal architecture posits that no consumer should know where a
primal lives — only what it can do. The biomeOS neural-api embodies this
principle: it maintains a capability registry of 2,088+ capabilities across
14+ primals, and offers `capability.call` and `graph.execute` as the
universal dispatch surface.

The journey from concept to reality exposed three layers of topology that
each had measurable impact on correctness and performance.

### Primal Topology

The provenance chain involves five primals operating in strict order:

1. **nestGate** — CAS storage, content-addressed by BLAKE3 hash
2. **rhizoCrypt** — DAG construction, Merkle-tree session commits
3. **loamSpine** — Append-only spine, cryptographic proof of ordering
4. **sweetGrass** — Attribution in W3C PROV JSON-LD format
5. **bearDog** — Ed25519 signatures on every commit

The ordering is critical: CAS first (content exists before provenance
references it), DAG second (events reference CAS hashes), spine third
(commits reference DAG Merkle roots), attribution fourth (links content
to actors), signing last (seals everything).

This ordering was originally expressed in Python orchestration code across
five scripts ("jelly strings"). Each script implemented its own partial
version of this ordering, introducing subtle inconsistencies (e.g., one
script signed before attribution, another skipped DAG entirely).

### Hardware Topology

The 4-tier storage hierarchy (T0-RAM, T1-NVMe, T2-SSD, T3-HDD) intersects
with primal topology through I/O patterns:

- **CAS ingestion** (nestGate) is bandwidth-bound: sequential reads through
  large files. NVMe delivers 2.1 GB/s; HDD delivers 180 MB/s.
- **DAG construction** (rhizoCrypt) is latency-bound: many small JSON-RPC
  calls building the Merkle tree. Processing time is dominated by RPC
  overhead, not storage speed.
- **Spine commits** (loamSpine) are single-write operations per session.
  Hardware tier is irrelevant (microseconds either way).

The staging experiment quantified this: braiding from NVMe is 3.9x faster
than braiding from HDD for small-file datasets (Type A: many small files),
and 1.8x faster for large-file datasets (Type D: tarballs >1 GB). The
automated staging method selector (`choose_staging_method`) applies these
findings at runtime.

### Interaction Topology

This is where the neural-api enters. The interaction topology defines how
consumers find and call primals:

**Stage 1 (current)**: Direct UDS socket connections.
```
native_braid.py → /run/user/1000/membrane/nestGate.sock → nestGate
native_braid.py → /run/user/1000/membrane/rhizoCrypt.sock → rhizoCrypt
```
Each consumer hardcodes socket paths. Gate-portable code is impossible.
But it works, and response times are <200ms.

**Stage 2 (in progress)**: Neural-api capability routing.
```
native_braid.py → /run/user/1000/membrane/biomeos-api.sock
  → capability.call("content.ingest", target="nestGate", ...)
  → neural-api routes to correct primal socket
```
The consumer knows only the capability name. The neural-api resolves the
target primal from the capability registry and proxies the call. Same code
works on any gate.

**Stage 3 (future)**: Graph execution.
```
pipeline.yaml → graph.execute(nodes=[
  {name: "ingest", capability: "content.ingest", ...},
  {name: "dag",    capability: "dag.event.append_batch", depends: ["ingest"]},
  {name: "commit", capability: "dag.session.commit", depends: ["dag"]},
  {name: "sign",   capability: "key.sign", depends: ["commit"]},
  {name: "braid",  capability: "braid.batch_create", depends: ["commit"]},
])
```
The entire provenance chain becomes a declarative graph. The neural-api
handles ordering, parallelism, and error propagation. `native_braid.py`
reduces to a graph definition, and eventually dissolves entirely.

## What the Neural API Provided

### Capability Discovery

The capability registry (`/run/user/1000/membrane/capability-registry.json`)
provided a machine-readable map of the entire primal surface area. During
the braiding work, this was critical for:

- Discovering that `content.ingest` is a nestGate capability (not a
  generic CAS method)
- Finding `dag.event.append_batch` for bulk DAG operations (vs. the
  single-event `dag.event.append` that jelly scripts were using)
- Confirming `braid.batch_create` exists for bulk attribution

Without the registry, the jelly scripts had been using the slow,
single-event paths because nobody knew the batch RPCs existed.

### Architecture Forcing Function

The neural-api's existence forced a clean separation between "what should
happen" (provenance chain) and "how to get there" (socket paths, RPC
framing, ribocipher encryption). The jelly scripts conflated both, making
each one a mini-integration project. By targeting neural-api routing, the
new `native_braid.py` separates orchestration logic from transport.

## Where the Neural API Needs Evolution

### 1. capability.call Proxy Timeout

Current behavior: calling `capability.call` with valid parameters through
`biomeos-api.sock` times out after 30 seconds. Direct primal socket calls
with the same parameters complete in <200ms.

Hypothesis: the neural-api process may not be fully initializing its
proxy routes for all capabilities, or the ribocipher framing between
neural-api and backend primals may have a handshake issue.

Impact: Stage 2 migration is blocked. Every consumer must remain at Stage 1.

### 2. sweetGrass Registry Gap

sweetGrass responds on its direct socket (`sweetGrass.sock`) and serves
W3C PROV braids. But it's absent from the capability registry's 2,088
entries. Without registry presence, the neural-api can't route
`braid.query` or `braid.batch_create` calls.

This may indicate sweetGrass was deployed after the last registry
announcement cycle, or its announcement module isn't configured.

### 3. No Method Introspection

None of the 14 primals support `rpc.discover` or equivalent. The capability
registry lists capability names but not parameter schemas. Consumers must
read source code or AAR documents to learn method signatures.

Adding `rpc.discover` to the ribocipher framing layer (not per-primal) would
make the registry self-documenting.

### 4. Graph Executor Not Yet Wired

`graph.execute` is advertised by the neural-api but has not been tested with
a real provenance pipeline graph. The transition from "script calls primals
in order" to "graph executor runs provenance DAG" requires:

- A graph definition format (YAML or JSON)
- Error propagation semantics (does a failed `content.ingest` cancel the
  entire graph, or just dependent nodes?)
- Partial result handling (if 47 of 48 files ingest successfully, does the
  graph commit what it has?)

### 5. content.ingest Streaming

The 256 MB ceiling on `content.ingest` was discovered during this work.
The neural-api could abstract this away by splitting large files into
streaming chunks and reassembling them at the CAS layer. This would be
transparent to consumers.

## Patterns for the Ecosystem

### Pattern: Experiment-Driven Architecture

The staging experiment wasn't planned in the original architecture. It
emerged from a performance anomaly (18-hour braiding runs on cold storage)
and produced quantified results that changed the pipeline:

- tar-pipe beats rsync for small files (1.6x)
- NVMe staging is non-optional for CAS ingestion (3.9x)
- L2ARC warming is a viable alternative for read-heavy validation

Other gates can replicate this experiment with `staging_experiment.py` to
calibrate their own tier boundaries.

### Pattern: Atomic Ingress

The principle "no data without braids" is generalizable. Any gate
downloading external data should braid at the ingress boundary, not
as a post-processing step. The `braid_now()` function pattern
(call braider after each download phase) is 12 lines of bash.

### Pattern: Incremental Braiding

The `--incremental` mode pattern (detect chunk growth, re-braid only
changed chunks) enables continuous provenance for streaming datasets.
Gates receiving real-time sensor data, event streams, or ongoing
downloads can use this pattern without re-processing historical data.

### Pattern: Primal-Native Bulk RPCs

The single biggest performance win was switching from Python-computed
BLAKE3 hashes to `content.ingest` (Rust-native CAS ingestion). The
general principle: if a primal can do it natively, never reimplement
in the orchestration layer. The capability registry makes these
native RPCs discoverable.

## Conclusion

The neural-api is the correct abstraction layer for provenance routing.
Its capability registry already proved its value by revealing batch RPCs
that eliminated jelly string overhead. The gap is in execution: the
routing proxy (Stage 2) and graph executor (Stage 3) need to become
operational to complete the architecture's promise of gate-portable,
declaratively-orchestrated provenance chains.

The work on this gate demonstrates the pattern works end-to-end with
direct primal connections. The 990,648 provenance events committed to
the spine prove the model. What remains is lifting that proven model
from hardcoded socket paths into the neural-api routing layer, making
it portable across the federation.
