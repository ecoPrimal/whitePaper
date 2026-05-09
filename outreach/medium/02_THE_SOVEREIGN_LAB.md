# The Sovereign Lab

*$15K in consumer hardware. 13 services. No cloud. No SaaS. No permission required.*

**By**: attsi | ecoPrimal
**Status**: Draft — evolving document
**Published**: [pending]

---

There is a cluster in my basement that runs science.

Ten towers. Four small-form-factor nodes. 130 CPU cores. 188 GB of GPU VRAM
across NVIDIA cards spanning four generations — a Kepler-era Tesla K80, Pascal
Titan Vs with HBM2, Ampere 3090s, Ada RTX 4070, and a Blackwell RTX 5090.
Three BrainChip Akida neuromorphic processors. 1.2 terabytes of system RAM.
125 terabytes of storage. A 10-gigabit backbone.

Total cost: about $15,000, accumulated over two years. Most of it bought
used. The K80 was $50. The Titan Vs were $400 each. The 3090s were $700. The
entire network switch was $120. This is not a rich person's hobby. This is
a bench scientist's stubbornness applied to hardware acquisition.

This cluster runs 13 composable Rust services that together form a sovereign
scientific computing platform. Researchers connect through a JupyterHub
interface. Their computations are tracked with cryptographic provenance. Their
results are attributed. And none of it touches the cloud.

---

## What Sovereignty Actually Means

"Sovereign" is an overloaded word. In this context it means something
specific and testable:

**You own the hardware.** The CPUs, GPUs, NVMe drives, and network switch are
physical objects in a physical room. Nobody can revoke access, raise prices,
change terms of service, or shut down an API endpoint. The services run as
systemd processes on Linux. If the internet disappears, the science still
works.

**You own the data.** Every dataset fetched from NCBI, UniProt, or KEGG is
hashed with BLAKE3 at download time and stored locally with provenance
metadata. The fetch is a one-time event. After that, the data is yours. It
does not expire. It does not require a subscription. If NCBI changes an
assembly, your local copy preserves the version you validated against, and
the provenance record shows both states.

**You own the compute.** No metered API calls. No GPU-hour billing. No
throttled free tiers. The RTX 4070 in the primary node runs Vulkan f64 GPU
compute through DF64 double-float emulation — the same mathematical precision
that NVIDIA reserves for their datacenter cards, unlocked through a sovereign
shader compilation pipeline (coralReef) that bypasses CUDA entirely.

**You own the provenance chain.** Every computation produces a DAG entry
(rhizoCrypt), committed to a permanent ledger (loamSpine), and attributed
via Ed25519-signed braids (sweetGrass). The chain is not stored in a
database — it is a cryptographic structure where each entry's integrity is
guaranteed by the entry before it. You can verify any result without trusting
anyone. The math proves it.

---

## The Dependency Map

Sovereignty is a direction, not a binary state. Today the system has 40+
external dependencies mapped across 7 clusters:

**Cloudflare** — DNS, TLS termination, tunnel for external access. The biggest
single dependency. Replacement path specified: BearDog TLS (ChaCha20-Poly1305
with ACME), Songbird NAT traversal, self-hosted authoritative DNS. Baselines
are capturing hourly for parity comparison.

**GitHub** — source hosting, CI, binary releases, Pages for the website.
Forgejo is installed as a calibration instrument. 74 workflow files to port.
The long pole.

**Package registries** — crates.io, PyPI, Conda. Low urgency. Vendor escape
hatch exists (cargo vendor, pip download, conda pack).

**AI APIs** — Anthropic, OpenAI. Optional. Ollama works locally as fallback.
Long-term path is sovereign inference through barraCuda WGSL compute.

**Science data APIs** — NCBI, UniProt, KEGG. Irreplaceable external data
sources, but once fetched, the data is local forever. This is not a
service dependency — it is a data dependency with caching.

**Internal primal gaps** — 5 of 6 resolved by upstream Phase 60. MethodGate
enforced on 10/13 services. Ionic token auth live. Resource envelopes
enforced.

And then the **irreducible externals** — things that will never be sovereign:
the domain registrar, the Linux kernel, NVIDIA GPU drivers, the Let's Encrypt
certificate chain, a $5/month VPS for NAT relay. These are accepted
constraints, not gaps.

The honest assessment: sovereignty is about 20% by service count but 80% by
criticality. Everything that touches the science — the compute, the data, the
provenance, the attribution — is fully sovereign today. What remains external
is infrastructure plumbing: DNS, TLS, NAT traversal. Important but not
existential.

---

## The ABG Model

The system serves a real external research group — a bioinformatics community
that connected through a Discord for accelerated biology and genomics. They
access the cluster through a JupyterHub at lab.primals.eco, routed through a
Cloudflare tunnel.

Four tiers of access, modeled on scientific peer review:

**Admin** — full control, all services, hardware access. 48 GB RAM, 16 cores.

**Compute** — kernels, workload dispatch, shared workspace. 32 GB RAM, 8 cores.
Can install Python packages offline via a local wheelhouse. Per-user scratch
space (private, chmod 700). Gets a Welcome notebook explaining the workspace.

**Reviewer** — no kernel, no terminal, no code execution. Sees only curated
dashboards in a showcase directory (symlink-level isolation). Can interact with
Voila widgets that run server-side. This is the peer-review tier: you read the
code, you see the results, you interact with the pipeline through a fixed
interface. Like submitting to a journal: the reviewer reads your methods and
can test a data point, but the system runs the fixed pipeline on their input.

**Observer** — read-only rendered output plus provenance chains. No execution.
The public window.

Every restriction is enforced at the mechanism level: filesystem permissions
(root-owned, chmod 550), kernel blocking (NoKernelManager), network isolation
(iptables owner match drops all outbound internet for restricted users,
localhost and LAN preserved), process hiding (hidepid=2), and ACLs on system
binaries. There are no convention flags. If it matters, it is enforced by a
gate.

---

## The Flywheel

The economics are honest: one person pays the electricity. Nobody pays them.

The system is designed for a different state. The provenance pipeline includes
an attribution chain — sweetGrass braids track who contributed what. When
value eventually flows through the system (publications, validated results,
community contributions), the attribution is already in place. The
infrastructure for fair distribution exists before the distribution begins.

The flywheel model:

```
Offer compute and infrastructure
  → Community produces science on it
    → Science proves the ecosystem works
      → Proof attracts contributions (hardware, time, science)
        → Contributions grow the infrastructure
          → More infrastructure → more science → more proof
```

The first turn is in progress. Real users are doing real science on the
cluster. The provenance pipeline records their work. The results are
verifiable. If the science is good, the proof accumulates.

This is not venture capital economics. There is no equity, no token, no
extraction. The goal is not exit — it is sustainability. The flywheel turns
because the science is worth doing, and the infrastructure makes it possible
to do it without institutional permission.

---

## What It Costs to Run

Electricity: roughly $80-120/month depending on workload. The i9-14900K and
RTX 4070 are the primary consumers when idle. Heavy GPU workloads (lattice
QCD, large DF64 computations) push higher.

Internet: standard residential. The Cloudflare tunnel is free tier. No
outbound costs.

Maintenance: occasional NVMe replacement, thermal paste, fan cleaning. The
hardware is consumer-grade with consumer-grade failure modes.

Time: the most expensive input. Two years of conversation-based development.
Thousands of sessions. The codebase is the artifact; the conversations are
the labor.

---

## Try It

The system is live. The repos are public. The JupyterHub is accessible.

If you have consumer hardware and want to run science on it without asking
anyone's permission — without institutional accounts, without cloud billing,
without GPU-hour meters — the deploy tools exist. They have been tested on
one machine. They need to be tested on more.

- **Deployment repo**: github.com/sporeGarden/projectNUCLEUS
- **All services**: github.com/ecoPrimals
- **Live system**: lab.primals.eco
- **License**: AGPL-3.0-or-later

The sovereignty thesis is simple: if you can't own the hardware, own the data,
own the compute, and verify the provenance, you don't own the science. This is
a working proof that you can.
