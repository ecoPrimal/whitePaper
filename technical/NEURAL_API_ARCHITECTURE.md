# Neural API - Adaptive Orchestration Through Capability Routing

**Category**: Orchestration Architecture  
**Status**: Production  
**Last Updated**: February 6, 2026

---

## Abstract

The Neural API is biomeOS's orchestration layer. It provides semantic capability routing - the ability for any primal to request a capability by meaning rather than by implementation. A primal calls `capability.call("crypto.sign", ...)` without knowing which primal provides signing, what method name that primal uses, or where its socket is. The Neural API discovers the provider, translates the request, routes it, and returns the result.

This is the mechanism that enables primals to remain autonomous while participating in composed systems. No primal imports another primal's code. No primal hardcodes another primal's name or address. The Neural API is the connective tissue that makes coordination possible without coupling.

---

## The Problem

An ecosystem of 10+ autonomous primals creates a coordination challenge. If Songbird needs cryptographic operations, it could import BearDog's client library - but that creates compile-time coupling, violating the autonomy principle. It could hardcode BearDog's socket path - but that creates deployment rigidity. It could implement its own crypto - but that creates redundancy and inconsistency.

The fundamental tension: primals must coordinate to produce complex behavior, but coordination must not compromise autonomy.

---

## Architecture

The Neural API operates in three layers:

### Layer 1: Primals (Capabilities)

Each primal provides a set of atomic capabilities and advertises them at startup. BearDog advertises `crypto.sign`, `crypto.encrypt`, `crypto.hash`, etc. Songbird advertises `tls.handshake`, `http.request`, `discovery.broadcast`, etc. NestGate advertises `storage.put`, `storage.get`, `storage.list`, etc.

Primals register capabilities dynamically - not at compile time, not in a static configuration file, but at runtime when they start and connect to biomeOS. If a primal goes down, its capabilities are deregistered. If a new primal comes up, its capabilities are added.

### Layer 2: biomeOS (Orchestration)

biomeOS maintains a capability registry that maps semantic capability names to provider primals and their specific method signatures. When a request arrives for `crypto.sign`, biomeOS:

1. Looks up which primal(s) provide the `crypto.sign` capability
2. Selects the best provider (health, load, proximity)
3. Translates the semantic method name to the provider's actual method name
4. Routes the request to the provider's socket
5. Returns the response to the caller

### Layer 3: Niche APIs (Domain Patterns)

Higher-order coordination patterns are defined as Niche APIs. RootPulse (version control), Loam Certificates (ownership), and other domain-specific patterns are expressed as sequences of capability calls that biomeOS orchestrates.

A Niche API is not a service - it is a graph of capability calls. "Commit a file" becomes: `storage.put` (NestGate stores the content) → `crypto.sign` (BearDog signs the commit) → `persistence.append` (LoamSpine records the permanent entry) → `attribution.record` (sweetGrass logs the contribution). Each step is a capability call that the Neural API routes independently.

---

## Capability Translation

The translation layer is what makes the Neural API more than a service registry. Primals use their own internal method names - they were built independently and do not follow a universal naming scheme. The Neural API translates between the ecosystem's semantic vocabulary and each primal's native vocabulary.

**Translation table (examples)**:

| Semantic Capability | Provider | Translated Method |
|--------------------|----------|-------------------|
| `crypto.generate_keypair` | BearDog | `x25519_generate_ephemeral` |
| `crypto.ecdh_derive` | BearDog | `x25519_derive_secret` |
| `crypto.sign` | BearDog | `ed25519_sign` |
| `crypto.hash_sha256` | BearDog | `sha256_digest` |
| `http.request` | Songbird | `secure_http_request` |
| `tls.handshake` | Songbird | `tls13_connect` |
| `storage.put` | NestGate | `storage.put` |
| `compute.execute` | ToadStool | `workload.submit` |

Translations are defined in deployment graphs (TOML) and loaded at deploy time:

```toml
[nodes.capabilities_provided]
"crypto.generate_keypair" = "x25519_generate_ephemeral"
"crypto.ecdh_derive" = "x25519_derive_secret"
"crypto.sign" = "ed25519_sign"
```

This means primals never need to change their internal APIs to participate in the ecosystem. BearDog's method is `ed25519_sign` because that's what makes sense for a crypto library. The ecosystem calls it `crypto.sign` because that's what makes sense for a caller. The Neural API bridges the gap.

---

## Graph-Based Orchestration

Complex operations are expressed as TOML deployment graphs that the Neural API executes:

```toml
[graph]
id = "tower_atomic_bootstrap"
coordination = "Sequential"

[[nodes]]
id = "start_security"
primal = { by_capability = "security" }
operation = { name = "start" }
depends_on = []

[[nodes]]
id = "start_discovery"
primal = { by_capability = "discovery" }
operation = { name = "start" }
depends_on = ["start_security"]

[[nodes]]
id = "verify_tower"
operation = { name = "health_check" }
depends_on = ["start_security", "start_discovery"]
```

Key properties:
- **Primals referenced by capability**, not by name (`by_capability = "security"` not `primal = "beardog"`)
- **Dependencies are explicit** (`depends_on` creates execution order)
- **Coordination modes**: Sequential (one at a time), Parallel (independent nodes simultaneously)
- **Health validation**: Graphs include verification steps to confirm the composition is healthy

The graph executor performs topological sorting to determine execution order, respects dependencies, and monitors health at each step. If a node fails, the executor can retry, skip (if optional), or abort the graph.

---

## Neural API Methods

### Graph Management

| Method | Description |
|--------|-------------|
| `neural_api.list_graphs` | List all available deployment graphs |
| `neural_api.get_graph` | Get details of a specific graph |
| `neural_api.execute_graph` | Execute a graph (async, returns execution ID) |
| `neural_api.get_execution_status` | Query execution progress |
| `neural_api.cancel_execution` | Cancel a running graph execution |

### Capability Routing

| Method | Description |
|--------|-------------|
| `capability.call` | Call a capability with automatic translation and routing |
| `capability.discover` | Find which primals provide a specific capability |
| `capability.discover_translation` | Inspect how a semantic name maps to provider methods |
| `capability.list_translations` | List all registered capability translations |

### Mesh and NAT (delegated to Songbird)

| Method | Description |
|--------|-------------|
| `mesh.status` | Mesh network status |
| `mesh.find_path` | Find route to a peer |
| `mesh.announce` | Announce relay availability |
| `punch.request` | Initiate NAT hole punch |
| `stun.discover` | Discover public address |
| `relay.serve` | Start relay service |

---

## Bidirectional Learning

The Neural API is designed for adaptive optimization. The forward pass routes requests from callers to providers. The backward pass collects feedback from providers about performance, latency, and success rates. Over time, the system learns:

- Which provider is fastest for a given capability
- Which capability sequences are commonly chained (and can be optimized)
- Which compositions are most reliable
- When to preemptively start primals based on usage patterns

This is conceptual architecture currently - the learning loop is designed but pathway optimization is implementation-planned. The immediate system uses static routing based on graph definitions and capability registration.

---

## TRUE PRIMAL Pattern

The Neural API enforces what the ecosystem calls the TRUE PRIMAL pattern:

1. **Self-knowledge only**: A primal knows its own capabilities. It does not know what other primals exist or what they can do.

2. **Zero hardcoding**: No primal contains another primal's name, socket path, or method signature in its source code.

3. **Runtime discovery**: All coordination happens through capability registration and the Neural API routing layer.

4. **Capability-based**: Requests are expressed as "I need X done" not "call primal Y's method Z."

This pattern is not optional - it is the architectural invariant that makes the ecosystem composable. If any primal hardcodes another primal's details, the composition model breaks. New primals cannot be substituted, deployments cannot be reconfigured, and testing requires the full ecosystem rather than mock capabilities.

---

## Implementation

The Neural API is implemented across several biomeOS crates:

- **`biomeos-atomic-deploy`**: Neural API server, router, graph executor
- **`biomeos-graph`**: Graph parser, validator, topological sorting, node handlers
- **`biomeos-core`**: Capability registry, socket discovery, atomic client
- **`biomeos-nucleus`**: NUCLEUS secure discovery protocol (5 layers)
- **`neural-api-client`**: Client library for primals to call the Neural API

The server runs as a JSON-RPC service over Unix sockets, following the same IPC pattern used by every primal. biomeOS is itself a primal - it just happens to specialize in coordination.

---

## Relationship to NUCLEUS

NUCLEUS is deployed via the Neural API. The three atomics (Tower, Node, Nest) are expressed as deployment graphs that the Neural API executes. Capability translation, health monitoring, lifecycle management, and dependency resolution all flow through the Neural API.

The Neural API is not separate from NUCLEUS - it is the orchestration mechanism within NUCLEUS. It is how biomeOS composes primals into atomics, how atomics compose into a full NUCLEUS, and how higher-order patterns like RootPulse are expressed as sequences of capability calls.

---

## Rationale

Service meshes, orchestration platforms, and API gateways all solve variations of the routing problem. The Neural API differs in one fundamental way: it operates at the **semantic capability level** rather than at the service or endpoint level.

A service mesh routes to "BearDog instance at 10.0.0.5:9000." The Neural API routes to "whatever provides crypto.sign." This abstraction means the system works regardless of how many instances exist, where they are deployed, what they're named, or how their internal APIs are structured.

For an ecosystem built on autonomous primals that evolve independently, this level of abstraction is not a luxury - it is the only way the system remains composable as it grows.
