# Squirrel — AI Coordination (Sovereign MCP)

## Identity

| Field | Value |
|-------|-------|
| Phase | 1 (Foundation) |
| Domain | AI inference, model routing, MCP coordination |
| Rust lines | 681,933 |
| Tests | 25,359 |
| Crates | 20+ |
| AGPL-3.0 | Yes |

## What It Is

Squirrel is the AI brain. Vendor-agnostic model routing across OpenAI, Anthropic, Ollama, and local models. Multi-MCP coordination. Context management. Cost/quality/latency routing. If anything in the ecosystem needs AI inference, it asks Squirrel.

Squirrel is the **largest primal by test count** (25,359) and the **second-largest by Rust volume** (681,933 lines). It is also one of the two original primals — in gen1, it was the "fault-tolerant compute orchestration platform" for the AI Swarm.

## Why It Exists

In gen1, Squirrel was the HPC job scheduler: checkpoint/restart, circuit breakers, "ant-model" orchestration across multiple compute nodes. Its job was to keep GPU workloads running despite hardware instability.

As AI models became the primary workload (not just one of many), Squirrel evolved from a general job scheduler into a dedicated AI coordination layer. The Model Context Protocol (MCP) gave it a standard way to discover and invoke AI capabilities across providers.

The name stuck: squirrels cache things (model weights), they're fast (low-latency routing), and they coordinate complex foraging patterns across large areas (multi-provider inference).

## Key Capabilities

### Model Routing

- **Multi-provider**: OpenAI, Anthropic, Ollama, HuggingFace, local GGUF models
- **Cost/quality/latency**: Routes to the cheapest provider that meets quality thresholds within latency budget
- **Fallback chains**: If primary provider is down, automatic fallback to secondary
- **Vendor-agnostic**: No compile-time coupling to any provider

### MCP Coordination

- **Multi-MCP**: Coordinates multiple MCP servers simultaneously
- **Tool discovery**: Automatically discovers and exposes tools from all connected MCP servers
- **Context management**: Maintains conversation context across provider switches

### Sovereign Inference

- **Local models**: Ollama integration for fully offline inference
- **Model caching**: Coordinates with NestGate to cache model weights locally
- **No telemetry**: No usage data leaves the machine unless explicitly configured

## How It Connects

```
biomeOS ──capability.call("ai.chat")──▶ Squirrel
                                            │
                    ┌───────────────────────┼───────────────────────┐
                    │                       │                       │
              ┌─────▼─────┐          ┌─────▼─────┐          ┌─────▼─────┐
              │  Ollama   │          │  OpenAI   │          │ Anthropic │
              │  (local)  │          │  (cloud)  │          │  (cloud)  │
              └───────────┘          └───────────┘          └───────────┘

Songbird provides the HTTP transport for cloud providers.
NestGate caches model weights for local providers.
BearDog signs requests and manages API key encryption.
```

### Key Relationships

- **biomeOS** routes all AI requests through Squirrel via the Neural API
- **Songbird** provides HTTP transport for cloud AI providers (via the AI Bridge)
- **NestGate** caches downloaded model weights
- **BearDog** encrypts and manages API keys in the secret store
- **ToadStool** provides GPU compute for local model inference

## Internal Architecture

The largest and most complex primal by crate count:

- `squirrel-core` — MCP client, provider routing, context management
- `squirrel-auth` — API key management (via BearDog)
- `squirrel-context` — Conversation state, token counting, context windowing
- `squirrel-plugins` — Provider-specific adapters (OpenAI, Anthropic, Ollama)
- `squirrel-tools` — MCP tool registry, tool invocation
- `squirrel-services` — Health monitoring, cost tracking, usage analytics
- `squirrel-sdk` — Client library for other primals

## The TRUE PRIMAL Pattern

Squirrel follows the TRUE PRIMAL pattern: no compile-time coupling to external services, capability-based discovery of providers, and isomorphic IPC. Adding a new AI provider (e.g., Google Gemini) requires a new plugin crate, not changes to core logic.

## What Makes It Interesting

Squirrel's evolution from HPC job scheduler (gen1) to sovereign AI coordinator (gen3) is the clearest example of constrained evolution in the primal ecosystem. The same codebase was reshaped by changing selective pressure: when the workload shifted from "distribute GPU jobs" to "route AI inference," the architecture specialized. The checkpoint/restart logic from gen1 evolved into context management and conversation state persistence. The circuit breakers evolved into provider fallback chains.

25,359 tests — more than any other primal — reflect the complexity of coordinating multiple AI providers with different APIs, pricing models, rate limits, and failure modes. Every provider quirk that was discovered became a test.
