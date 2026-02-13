# **`toadStool` - Technical Specification v0.1 (Draft)**

**Status:** Draft | **Author:** The Artisan AI | **Date:** July 2025

**Related Documents:** [The biomeOS Manifesto](./../gen2/biomeOS_Manifesto.md)

---

## **1. Overview**

`toadStool` is the universal runtime environment for the `ecoPrimals` ecosystem. It is the Primal responsible for bootstrapping, managing, and isolating a complete `biomeOS` instance from a declarative manifest file (`biome.yaml`). It is the bridge between bare hardware and a living, sovereign ecosystem.

Its design philosophy is one of minimal host intrusion and maximum workload isolation. `toadStool` is the only Primal that needs to be installed directly on the host system; all other Primals and services are managed by it.

## **2. Core Architecture & Responsibilities**

`toadStool` operates as a privileged daemon on the host system, governed by a master control process. Its core responsibilities are as follows:

### **2.1. Manifest Ingestion and Planning**
- **Input:** A `biome.yaml` file path.
- **Process:** `toadStool` parses the manifest and constructs an internal dependency graph of all Primals and services. It validates the syntax, checks for source availability, and plans the startup sequence.
- **Output:** An executable plan that respects dependencies (e.g., `bearDog` must start before any service that requires its policies).

### **2.2. Secure Workload Fetching**
- `toadStool` is responsible for fetching Primal and service workloads from specified sources (e.g., OCI registries, IPFS, Git repositories).
- All fetched artifacts **must** be verified against a cryptographic checksum or signature specified in the manifest to prevent supply chain attacks. This is a non-negotiable security gate.

### **2.3. Runtime Environment & Sandboxing**
`toadStool` must provide a secure, multi-tenant runtime environment. The primary runtime target is **WebAssembly (Wasm)** via the WASI standard, for its security-first, sandboxed-by-default nature.

- **Wasm Runtime:** `toadStool` will embed a Wasm runtime (e.g., Wasmtime, Wasmer) to execute Primals and services compiled to a `wasm32-wasi` target.
- **Capability-Based Permissions:** Workloads are granted capabilities explicitly. A service granted no filesystem access cannot see the filesystem. A service not granted network access cannot open a socket.
- **Container Fallback:** For workloads that cannot be compiled to Wasm (e.g., legacy applications, those requiring direct GPU access via proprietary drivers), `toadStool` will support OCI-compliant containers (e.g., via `runc`) as a secondary runtime. This is considered a "less secure" mode and must be explicitly enabled in the manifest, requiring elevated privileges.

### **2.4. Host Resource Abstraction**
`toadStool` discovers and abstracts host resources, making them available to workloads based on manifest requests.
- **CPU/Memory:** Manages allocation and sets limits for each workload.
- **Storage:** Integrates with `nestGate` (if present) to provision and attach ZFS datasets. For hosts without `nestGate`, it manages simple host path mounts, subject to `bearDog` policies.
- **GPU / Accelerator Access:**
    - Detects available accelerators (`NVIDIA/CUDA`, `AMD/ROCm`, `Intel/Level Zero`).
    - Exposes a generic "compute" capability to workloads.
    - Implements an **adapter layer** to translate generic requests (e.g., "run this AI inference task") to the specific driver/API of the host hardware. This is the key to breaking vendor lock-in; the ecosystem standardizes on an open request format, and `toadStool` adapts it to the proprietary backend.

### **2.5. Lifecycle and Health Management**
- `toadStool` is responsible for starting, stopping, and restarting all components of a `biomeOS`.
- It performs health checks as defined in the manifest (e.g., HTTP endpoints, TCP ports) and reports the status of the entire biome.

## **3. Integration with Core Primals**

`toadStool` is the physical anchor for the other Primals.

### **3.1. `bearDog` (The Warden)**
- `toadStool`'s most critical integration. `bearDog` runs as the first and most privileged workload.
- `toadStool` **enforces** the policies `bearDog` provides. If `bearDog` defines a policy that service `X` cannot access dataset `Y`, `toadStool` configures the sandbox at the runtime level to make that physically impossible. It translates logical policy into runtime reality.

### **3.2. `songbird` (The Dispatcher)**
- `toadStool` provisions the virtual network interfaces for each workload.
- It registers each service with the `songbird` instance, providing the necessary metadata for discovery and routing.
- For inbound traffic from federated peers, `toadStool` receives routing instructions from `songbird` and directs the traffic to the appropriate workload's sandbox.

## **4. Command-Line Interface (CLI)**

The primary user interaction with `toadStool` is via a simple, powerful CLI.

```bash
# Start and run a biome in the foreground
toadstool run ./my_biomes/science_biome.yaml

# Run a biome in the background (detached mode)
toadstool up ./my_biomes/science_biome.yaml -d

# Stop a running biome
toadstool down science_biome

# List all running biomes on the host
toadstool ps

# View logs for a specific biome or service
toadstool logs science_biome
toadstool logs science_biome.alphafold_service
```

## **5. Open Questions & Future Work**

- **Live Migration:** A framework for pausing a workload on one `toadStool` instance and resuming it on another in the federation.
- **Nested Virtualization:** The ability for a `biomeOS` to run its own instance of `toadStool` to manage sub-biomes. Requires hardware virtualization support.
- **Advanced Resource Scheduling:** Integration with `sweetGrass` to enable an economic layer for scheduling workloads based on contribution/payment, not just availability. 