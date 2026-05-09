# For Builders

**How Developers Compose Primals Into Their Own sporeGarden Products**

**Date**: March 24, 2026 (updated May 8, 2026)
**Audience**: Rust developers, indie game devs, tool builders, infrastructure engineers

---

## What You're Building On

The ecoPrimals ecosystem provides 14+ primals — sovereign Rust binaries
that communicate via JSON-RPC 2.0 over TCP. Each primal handles one
domain: AI, provenance, visualization, game science, storage, compute,
security, discovery, attribution, lineage.

You don't import their crates. You don't link their binaries. You talk
to them over TCP. They are services, but sovereign ones — no cloud, no
platform, no accounts.

---

## The Minimal Composition

The smallest possible gen4 product is a Rust binary that connects to
one primal and does something useful:

```rust
use serde_json::json;
use std::io::{BufRead, BufReader, Write};
use std::net::TcpStream;

fn main() {
    let mut stream = TcpStream::connect("127.0.0.1:9100").unwrap();

    let request = json!({
        "jsonrpc": "2.0",
        "method": "dag.session.create",
        "params": { "metadata": { "app": "my-tool" } },
        "id": 1
    });

    writeln!(stream, "{}", request).unwrap();

    let mut reader = BufReader::new(&stream);
    let mut response = String::new();
    reader.read_line(&mut response).unwrap();

    println!("Session created: {response}");
}
```

That's a gen4 product. It composes a primal (rhizoCrypt) into a tool.
The primal handles provenance. Your tool handles whatever you're
building.

---

## The Full Composition (esotericWebb Pattern)

For a real product, you want the full pattern:

### 1. PrimalBridge

A connection pool that manages TCP connections to all primals:

```rust
pub struct PrimalBridge {
    connections: HashMap<String, TcpStream>,
    capabilities: HashMap<String, Vec<String>>,
    circuit_breakers: HashMap<String, CircuitBreaker>,
}

impl PrimalBridge {
    pub fn call(&self, method: &str, params: Value) -> Result<Value> {
        let domain = method.split('.').next().unwrap();
        if self.circuit_breakers[domain].is_open() {
            return self.fallback(method, params);
        }
        match self.send_rpc(method, params) {
            Ok(response) => Ok(response),
            Err(_) => {
                self.circuit_breakers[domain].record_failure();
                self.fallback(method, params)
            }
        }
    }
}
```

### 2. Deploy Graph

A TOML file declaring your primal topology:

```toml
[primals.rhizoCrypt]
binary = "plasmidBin/rhizoCrypt/rhizo_crypt"
port = 9100
capabilities = ["dag.session", "dag.event", "dag.merkle"]

[primals.squirrel]
binary = "plasmidBin/squirrel/squirrel"
port = 9200
capabilities = ["ai.chat", "ai.summarize"]
```

### 3. PrimalLauncher

Reads the deploy graph, topologically sorts by dependencies, spawns
binaries in wave order:

```rust
pub fn launch(graph: &DeployGraph) -> Result<PrimalBridge> {
    let waves = graph.topological_waves();
    let mut bridge = PrimalBridge::new();

    for wave in waves {
        for primal in wave {
            spawn_binary(&primal.binary)?;
            poll_tcp_ready(&primal.port, Duration::from_secs(10))?;
            bridge.connect(&primal.name, &primal.port)?;
        }
    }

    Ok(bridge)
}
```

### 4. Graceful Degradation

Every bridge call has a fallback. Your product never crashes because a
primal is absent:

```rust
fn narrate(&self, action: &str, state: &WorldState) -> String {
    // Tier 1: domain engine
    if let Ok(narration) = self.bridge.call("game.narrate_action", json!({
        "action": action, "state": state
    })) {
        return narration["text"].as_str().unwrap().to_string();
    }

    // Tier 2: general AI
    if let Ok(response) = self.bridge.call("ai.chat", json!({
        "prompt": format!("Narrate: {action}")
    })) {
        return response["text"].as_str().unwrap().to_string();
    }

    // Tier 3: local template
    format!("You {action}.")
}
```

---

## Available Primals

| Primal | Domain | Key methods | What it does |
|--------|--------|-------------|-------------|
| rhizoCrypt | dag | `dag.session.*`, `dag.event.*`, `dag.merkle.*` | Append-only provenance DAGs |
| loamSpine | lineage | `certificate.mint` | Permanent hash-chained certificates |
| sweetGrass | attribution | `attribution.record` | Radiating attribution braids |
| BearDog | security | `security.sign`, `security.verify` | Cryptographic identity and signing |
| Squirrel | ai | `ai.chat`, `ai.summarize` | Sovereign AI coordination |
| petalTongue | visualization | `visualization.render.*`, `interaction.poll` | Universal UI rendering |
| ludoSpring | game | `game.evaluate_flow`, `game.npc_dialogue` | Game science and DDA |
| toadStool | compute | `compute.dispatch.submit` | GPU compute dispatch |
| nestGate | storage | `storage.store`, `storage.retrieve` | Key-value persistence |
| Songbird | discovery | `system.capabilities` | Primal capability discovery |

Full method catalogs are in the wateringHole leverage guides.

---

## What You Get for Free

By composing primals, your product inherits:

### Provenance (rhizoCrypt)

Every action in your product is traceable. You don't build a logging
system — you append events to a DAG. The DAG is Merkle-rooted,
content-addressed, and cryptographically verifiable.

### Attribution (sweetGrass)

Every contribution to your product is credited. Users, creators, AI
models — all tracked. When value flows (sunCloud), it flows along
these braids.

### AI (Squirrel)

Sovereign AI without cloud dependency. Squirrel routes to the best
available model (local GPU, remote sovereign, fallback). Your product
calls `ai.chat` and gets text back. Where the model runs is Squirrel's
problem.

### Security (BearDog + darkforest)

14,201 tests, 91+ JSON-RPC methods, production-grade cryptography.
Your product calls `security.sign` and gets a signed payload. Key
management, identity, verification — BearDog handles it.

The ecosystem includes **darkforest** (pure Rust, 939 KB), a security
validator that pen-tests, fuzzes, and crypto-audits the full stack:
181 checks, 175 PASS, 0 FAIL. Your product inherits a validated
security posture.

### Game Science (ludoSpring)

If you're building anything interactive, ludoSpring provides validated
models for flow state, engagement, DDA, NPC dialogue, and narration.
These are peer-reviewed HCI models (baseCamp 17), not ad hoc heuristics.

### Sovereign Compute (toadStool)

If you need GPU: toadStool dispatches jobs to barraCuda math kernels.
Your product submits a compute job and gets results. The GPU pipeline
(barraCuda → coralReef → toadStool) is the ecosystem's sovereign
compute substrate.

---

## Architecture Decisions

### TCP vs. Unix Domain Sockets

gen3 used UDS (localhost only). gen4 uses TCP (platform-agnostic, works
across network boundaries, works on GrapheneOS). Use TCP for new
products. UDS remains supported for local-only deployments.

### Language Independence

The bridge is JSON over TCP. Your product can be written in any
language. esotericWebb uses Rust because the ecosystem is Rust-native,
but Python, Go, TypeScript — anything that can send JSON over TCP can
compose primals.

### License Boundary

Your product's license is yours. The primals are AGPL. The composition
is via TCP (not linking). The scyBorg exception protocol
(wateringHole/SCYBORG_EXCEPTION_PROTOCOL.md) clarifies: TCP
composition does not create a derivative work under AGPL. Your product
can use any license.

### Standalone Mode

Your product should work with zero primals available. This is a design
requirement, not optional. Creators develop content offline. Users play
without network. Primals enrich the experience; they don't gatekeep it.

---

## Building a New sporeGarden Product

### Step 1: Identify Your Domain

What does your product do? Health dashboard? Music tool? Field
genomics kit? Data visualization? Educational game?

### Step 2: Map Primals to Needs

Which primals does your domain need?

| Need | Primal |
|------|--------|
| Track history | rhizoCrypt |
| Permanent records | loamSpine |
| Credit contributors | sweetGrass |
| AI assistance | Squirrel |
| User interface | petalTongue |
| Secure identity | BearDog |
| GPU compute | toadStool |
| Persistent storage | nestGate |
| Interactive science | ludoSpring |
| Find primals | Songbird |

### Step 3: Write Your Bridge

Use the PrimalBridge pattern. Start with one primal. Add more as
needed. Every call degrades gracefully.

### Step 4: Write Your Engine

Your product's core logic. This is what makes your product unique.
esotericWebb has GameSession + NarrativeGraph + WorldState. Your
product has whatever your domain needs.

### Step 5: Write Your Content Surface

The creator-facing interface. YAML, TOML, GUI, CLI — whatever makes
sense for your audience. This is the dual surface: developers interact
via Rust, creators interact via your content format.

### Step 6: Deploy

Use deploy graphs to declare your primal topology. Use PrimalLauncher
to spawn primals. Package your product with primals from plasmidBin/.

---

## Standards to Follow

| Standard | Where | Why |
|----------|-------|-----|
| SEMANTIC_METHOD_NAMING | wateringHole/ | Consistent method names |
| CAPABILITY_BASED_DISCOVERY | wateringHole/ | Primal-agnostic wiring |
| ECOBIN_ARCHITECTURE | wateringHole/ | Binary compatibility |
| PRIMAL_IPC_PROTOCOL | wateringHole/ | Wire format compatibility |
| SCYBORG | wateringHole/ | License compliance |
| PUBLIC_SURFACE | wateringHole/ | API stability guarantees |

---

## The esotericWebb Reference

esotericWebb V4 is the reference implementation for gen4 composition
patterns. Its source is the most detailed example of:

- PrimalBridge with 23 methods across 8 domains
- Deploy graph with wave-ordered spawning
- Graceful degradation at every level
- PrimalEnrichment composition result
- Tiered narration (domain → AI → template)
- Provenance lifecycle in a game loop

Read the code. Follow the patterns. Build your own garden.

---

*The primals are the ingredients. The bridge is the recipe. Your
product is the meal. Make something people want to eat.*
