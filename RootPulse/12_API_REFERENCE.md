# RootPulse API Reference

**Concrete JSON-RPC Calls for the Commit Workflow**

**Version**: 1.0.0  
**Date**: March 13, 2026  
**Status**: Technical Reference (tested)

---

## Protocol

All inter-primal communication uses JSON-RPC 2.0 over HTTP (JSON-RPC) or tarpc (binary). BearDog uses Unix socket IPC.

---

## Phase 1: Health Checks

### rhizoCrypt (JSON-RPC on port 9401)

```json
{"jsonrpc":"2.0","method":"system.health","params":{},"id":1}
```

Response:

```json
{"healthy":true,"state":"running","active_sessions":1,"total_vertices":0,"uptime_seconds":0}
```

### sweetGrass (HTTP GET on port 8302)

```
GET /health
```

Response:

```json
{"status":"healthy","version":"0.7.3","service":"sweetgrass","uptime_secs":191,"store":{"available":true,"braid_count":0,"backend":"sled"}}
```

---

## Phase 2: Session and Dehydration (rhizoCrypt)

### Create Session

```json
{"jsonrpc":"2.0","method":"dag.session.create","params":{"name":"rootpulse-commit-test"},"id":10}
```

Response:

```json
{"result":"019ce915-c46f-79d3-8d50-99e67cec98fb"}
```

### Append Events

| Event Type | Payload |
|------------|---------|
| SessionStart | `{"event_type":"SessionStart"}` |
| DataCreate | `{"event_type":{"DataCreate":{"schema":null}}}` |
| DataModify | `{"event_type":{"DataModify":{"delta_type":"patch"}}}` |
| AgentAction | `{"event_type":{"AgentAction":{"action":"commit rootpulse test"}}}` |
| SessionEnd | `{"event_type":{"SessionEnd":{"outcome":"Success"}}}` |

### Dehydrate

```json
{"jsonrpc":"2.0","method":"dag.dehydrate","params":{"session_id":"SESSION_ID"},"id":20}
```

Response:

```json
{"result":"b4af34d8aa1a96426e9908164cf3168bddb15dee0da461152be9185eba7a5ac8"}
```

---

## Phase 3: Sign (BearDog via Unix Socket)

```json
{"jsonrpc":"2.0","method":"crypto.sign","params":{"message":"MERKLE_ROOT","key_id":"birdsong_master"},"id":30}
```

Response:

```json
{"result":{"algorithm":"Ed25519","key_id":"birdsong_master","signature":"base64..."}}
```

---

## Phase 4: Store (NestGate — Optional)

Method: `storage.store`  
Params: `{key, value, family_id}`

---

## Phase 5: Commit to LoamSpine

```json
{"jsonrpc":"2.0","method":"permanence.commit_session","params":{"request":{"session_id":"SESSION_ID","merkle_root":"MERKLE_ROOT","summary":{"session_type":"General","vertex_count":5,"leaf_count":1,"started_at":1710316800000000000,"ended_at":1710316801000000000,"outcome":"Success"},"committer_did":"did:key:test-agent"}},"id":50}
```

Response:

```json
{"result":{"accepted":true,"commit_id":"17f721c7...","spine_entry_hash":"17f721c7...","entry_index":1,"spine_id":"019ce919-3716-..."}}
```

### Verify

`permanence.verify_commit` returns `true` on success.

---

## Phase 6: Attribute (sweetGrass)

### Record Dehydration

```json
{"jsonrpc":"2.0","method":"contribution.recordDehydration","params":{...},"id":60}
```

Response:

```json
{"result":{"session_id":"...","braids_created":1,"braid_ids":["urn:braid:b4af34d8..."]}}
```

### Create Braid

```json
{"jsonrpc":"2.0","method":"braid.create","params":{"data_hash":"MERKLE_ROOT","mime_type":"application/x-rootpulse-commit","size":512},"id":61}
```

Response: W3C PROV-O entity with `@context`, `@id`, `@type`, `signature`, etc.

---

## Service Endpoints

| Primal | Protocol | Port | Path |
|--------|----------|------|------|
| rhizoCrypt | JSON-RPC | 9401 | /rpc |
| rhizoCrypt | tarpc | 9400 | - |
| LoamSpine | JSON-RPC | 8301 | / |
| LoamSpine | tarpc | 9001 | - |
| sweetGrass | HTTP+JSON-RPC | 8302 | /jsonrpc, /health |
| sweetGrass | tarpc | 8091 | - |
| BearDog | Unix Socket | - | /tmp/.../beardog.sock |

---

## Next Reading

1. [06_COORDINATION_PATTERNS.md](./06_COORDINATION_PATTERNS.md) — Workflow graphs
2. [08_SEMANTIC_ATTRIBUTION.md](./08_SEMANTIC_ATTRIBUTION.md) — sweetGrass integration
3. [02_ARCHITECTURE.md](./02_ARCHITECTURE.md) — System design
