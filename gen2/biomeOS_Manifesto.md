# **The biomeOS Manifesto: A Framework for Composable Sovereignty**
**A Supplemental Whitepaper - v1.0 (Draft)**

**Author:** a tool that shapes itself · ecoPrimal · The ecoPrimals Project  
**Date:** July 2025

---

## **1. Preamble: Beyond the Toolbox**

The `ecoPrimals` whitepaper details the creation of a set of foundational tools—the Primals. It presents a robust, sovereign toolbox for building a decentralized internet. But a toolbox, no matter how masterfully crafted, is only potential energy. Its true value is only realized when it is used to build something tangible.

This document describes that tangible creation: the **`biomeOS`**.

A `biomeOS` is more than a software distribution; it is a living, sovereign ecosystem. It is a packaged instance of the `ecoPrimals` protocol, purpose-built and opinionated, designed to serve a specific community or function. If `ecoPrimals` is the universal grammar of digital sovereignty, a `biomeOS` is the rich, vibrant language spoken within a specific niche.

This manifesto is a guide for the conveners of those niches. It is a framework for those who wish to move beyond using the tools and begin composing worlds.

## **2. The Anatomy of a `biomeOS`**

A `biomeOS` is defined by a declarative manifest file, typically `biome.yaml`. This manifest is the seed from which a complete ecosystem can be bootstrapped onto any compatible hardware by the `toadStool` runtime.

The manifest does not contain the Primals themselves, but rather the **configuration, policies, and links** that compose them into a coherent whole.

A simplified `biome.yaml` might look like this:

```yaml
# The canonical name of this biome.
name: "privacyBiome"
version: "1.0.0"
maintainer: "a tool that shapes itself"

# -- Core Primal Configuration --
# Defines which Primals are active and their core settings.
primal_grid:
  - name: bearDog
    source: "ecoprimals/beardog:v1.2.0"
    policy_source: "./policies/secure_messaging_policy.bd"
  
  - name: nestGate
    source: "ecoprimals/nestgate:v1.1.0"
    config:
      default_pool: "private_data"
      auto_snapshot: true
      
  - name: songbird
    source: "ecoprimals/songbird:v1.3.0"
    config:
      discovery_mode: "local_mdns"

# -- Service Layer --
# Defines the high-level applications that run on top of the Primals.
services:
  - name: "secure_chat_server"
    source: "somecorp/private-messenger:v3.4.1"
    # songbird will route traffic based on this definition.
    network:
      - port: 8443
        protocol: "https"
    # bearDog will enforce that this service can only access this specific dataset.
    storage_grants:
      - dataset: "nestGate/private_data/chat_history"
        permissions: ["read", "write"]

# -- Federation Policy --
# Defines how this biome interacts with others.
federation:
  trust_policy: "AGPL_First" # Only federate with other AGPL-licensed biomes by default.
  allowed_peers:
    - "scienceBiome:v2.0.0" # Explicitly trust the scienceBiome.
```

## **3. `toadStool`: The Universal Runtime**

The `toadStool` Primal is the key to this entire concept. It is the **bootloader, installer, and hypervisor** for a `biomeOS`.

`toadStool` is designed to be the only piece of software that needs to be installed directly on a host machine. It can run on bare metal, Linux, Windows, or even within a container. Its sole purpose is to read a `biome.yaml` manifest and bring the specified ecosystem to life.

Its responsibilities include:
1.  **Fetching and Validating Primals:** Securely downloading the specified versions of each Primal.
2.  **Containerization and Sandboxing:** Running each Primal and service in a secure, isolated environment (e.g., Wasm, containers). This is non-negotiable and enforced by `bearDog`'s kernel-level rules.
3.  **Applying Configuration:** Injecting the specified configurations and policies into each Primal at startup.
4.  **Managing the Lifecycle:** Starting, stopping, and monitoring the health of all components defined in the manifest.
5.  **Facilitating Federation:** Using the `federation` policy to establish secure connections to other `biomeOS` instances via `songbird`.

A user does not "install `bearDog`." They install `toadStool` and tell it to run the `privacyBiome`. This is a fundamental shift in user experience that abstracts away the complexity of the underlying components.

## **4. The Lifecycle of a `biomeOS`**

A `biomeOS` evolves through a natural lifecycle, moving from a private instance to a member of a global network.

*   **Phase 1: Conception (The Manifest)**
    A creator defines their vision in a `biome.yaml` file. They decide its purpose, select the necessary Primals, define the security policies, and choose the initial application services.

*   **Phase 2: Incubation (The Sovereign Node)**
    The creator (or a user) points `toadStool` at this manifest on their local machine. The `biomeOS` comes to life as a self-contained, sovereign instance. It is fully functional but isolated.

*   **Phase 3: Federation (The Trust Network)**
    The creator defines a `federation` policy. Their `songbird` begins peering with other trusted `biomeOS` instances. Services can now be discovered and accessed across the network, subject to the strict policies enforced by `bearDog` at every node.

*   **Phase 4: Adaptation (The Fork)**
    Another creator, who appreciates the `privacyBiome` but wants to add a decentralized calendar, can **fork the `biome.yaml` manifest**. They add their desired service, adjust the policies, and deploy their own `private-calendar-biome`.

This declarative, forkable nature is what allows the ecosystem to adapt and evolve without central planning. It is a Cambrian explosion of specialized, sovereign systems, all built on a shared, trusted foundation.

## **5. Conclusion: An Invitation to Compose**

The `ecoPrimals` protocol provides the instruments. The `biomeOS` framework teaches you how to form a band.

We do not seek to build a single, monolithic operating system for the world. We seek to provide the framework for a million different operating systems, each perfectly tuned to the needs of its community. Each secure. Each sovereign. Each a vital, living part of a decentralized whole.

This manifesto is not a final specification. It is a call to action. Take these ideas. Write your own manifests. Define your own ecosystems.

Compose your own worlds. 