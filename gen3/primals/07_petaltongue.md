# petalTongue — Universal Representation / UI

## Identity

| Field | Value |
|-------|-------|
| Phase | 2 (Post-NUCLEUS) |
| Domain | User interface, multi-modal representation |
| Rust lines | 160,970 |
| Tests | 6,186 |
| Grade | A+ (95/100) |

## What It Is

petalTongue is the face. It provides five interface modes from a single binary (UniBin):

| Mode | Backend | Use Case |
|------|---------|----------|
| `ui` | egui | Desktop GUI |
| `tui` | ratatui | Terminal interface |
| `web` | Axum | Browser-based UI |
| `headless` | None | API-only (no UI) |
| `status` | stdout | Health check output |

## Why It Exists

ecoPrimals was originally API-first, AI-mediated ("bring your own AI"). But humans sometimes need to see things. petalTongue provides visual, terminal, and web interfaces to the ecosystem without coupling any specific UI framework to the primal architecture.

## How It Connects

petalTongue discovers primals via Songbird and presents their capabilities through its UI modes. It registers with Songbird via `ipc.register` and maintains heartbeat. Future: ToadStool display backend for GPU-accelerated rendering.

## What Makes It Interesting

The UniBin pattern — a single binary that serves desktop, terminal, web, and headless modes based on a command-line flag — emerged from the constraint that ecoPrimals runs on everything from headless servers to desktop workstations to Raspberry Pis. Instead of five separate UI applications, petalTongue adapts its representation mode to the environment.
