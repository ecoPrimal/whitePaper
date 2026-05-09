# r/homelab Post Draft

**Identity**: ecoPrimal
**Subreddit**: r/homelab (primary), r/selfhosted (cross-post candidate)
**Status**: Draft — do not post until prep checklist complete

---

## Post Title

**I built a 13-service sovereign compute stack in Rust that runs scientific workloads on consumer hardware. Looking for someone to try deploying it on different hardware.**

---

## Post Body

I've been building a set of composable services (we call them "primals") that
together form a sovereign scientific computing platform. Everything is Rust,
everything is AGPL-3.0, everything runs on localhost. No cloud. No SaaS. No
phone-home.

### What it is

13 services communicating over a custom protocol (BTSP — ChaCha20-Poly1305
AEAD), orchestrated by a coordinator (biomeOS), with a full cryptographic
provenance pipeline (content-addressed artifacts → DAG tracking → permanent
ledger → attribution braids). There's also a JupyterHub frontend for
multi-user notebook access.

### What it runs on

My primary node ("ironGate"):

- **CPU**: Intel i9-14900K (24c/32t)
- **GPU**: NVIDIA RTX 4070 (12 GB, Vulkan f64 via DF64 emulation)
- **RAM**: 96 GB DDR5
- **Storage**: 3.6 TB NVMe
- **OS**: Pop!_OS 22.04
- **Network**: Gigabit LAN, Cloudflare tunnel for external access

Total cluster is 10 towers + 4 SFF nodes, ~130 CPU cores, ~188 GB GPU VRAM,
~1.2 TB system RAM, ~125 TB storage, 3 BrainChip Akida NPUs. But the full
NUCLEUS stack (all 13 services) runs fine on the single node above.

### What it does

- **Science workloads**: 235+ validation checks across bioinformatics (16S
  pipeline, metagenomics), plasma physics, lattice QCD, drug discovery,
  agricultural hydrology — all reproduced from published papers
- **Multi-user JupyterHub**: 4-tier access (admin/compute/reviewer/observer)
  with PAM auth, Cloudflare tunnel, Voila dashboards
- **Security**: Pure Rust security validator (darkforest v0.2.0) runs 181
  checks — pen tests across 3 threat actors, protocol fuzzing for all 13
  services, 13 crypto strength checks. Latest run: **175 PASS, 0 FAIL, 6
  DARK_FOREST** (informational findings, no exploitable vulnerabilities)
- **Provenance**: Every computation is content-addressed (BLAKE3), tracked in a
  DAG, committed to a permanent ledger, and attributed via Ed25519-signed
  braids. You can trace any result back to its raw data

### The stack

All services are single static binaries. No containers, no VMs, no
interpreters. They run as systemd user services and communicate over localhost
TCP (JSON-RPC) or Unix domain sockets.

```
Service         Port    Role
beardog         9100    Identity, crypto, BTSP, Ed25519 keys
songbird        9200    Discovery, networking, NAT traversal
squirrel        9300    AI coordination (Ollama backend)
toadstool       9400    Workload dispatch, GPU math
nestgate        9500    Content-addressed storage, KV
rhizocrypt      9601    DAG tracking, Merkle roots
loamspine       9700    Permanent ledger, certificates
coralreef       9730    WGSL shader compilation (sovereign GPU pipeline)
barracuda       9740    Scientific math library (f64 GPU compute)
sweetgrass      9850    Attribution braids, W3C PROV
petaltongue     9860    Web serving, dashboards
skunkbat        9870    Anomaly detection, audit log
biomeos         9900    Orchestration, Neural API, composition graphs
```

### What I'm looking for

Someone willing to try deploying the stack on different hardware. Especially
interested in:

- **Blackwell Pro / RTX 5090** — our GPU math (barraCuda) uses Vulkan/WGSL
  with DF64 f64 emulation. Would love to know if SM120 changes anything
- **ARM** — the binaries are x86_64 today but everything is pure Rust with no
  C dependencies. Cross-compilation should work
- **Multi-node** — the bonding system supports covalent (LAN), ionic (metered),
  and metallic (institutional) patterns but I've only tested single-node so far
- **Anyone with HBM2 cards** — we have Titan Vs and MI50s, but more data points
  on HBM2 behavior with DF64 shaders would be valuable

I'd pair with you on setup. The deploy tooling is functional but hasn't been
tested by anyone who isn't me.

### Links

- **GitHub**: github.com/sporeGarden/projectNUCLEUS (deployment repo)
- **All primals**: github.com/ecoPrimals (org — primals are individual repos)
- **Live JupyterHub**: lab.primals.eco (observer account available)
- **License**: AGPL-3.0-or-later (code), ORC (system mechanics), CC-BY-SA 4.0 (docs)

Happy to answer questions about the architecture, the science workloads, or
the security model.

---

## Prep Checklist (before posting)

- [ ] Record asciinema terminal session: primal startup sequence + darkforest run
- [ ] Screenshot: `systemctl --user list-units | grep primal` showing all 13 healthy
- [ ] Screenshot: JupyterHub landing page at lab.primals.eco
- [ ] Screenshot: Voila validation dashboard
- [ ] Screenshot: darkforest summary output (175 PASS banner)
- [ ] Verify deploy/deploy.sh has clear first-time instructions
- [ ] Verify projectNUCLEUS README quick start section is accurate
- [ ] Create observer account credentials for anyone who wants to look
- [ ] Test that primals.eco/lab is accessible externally (Cloudflare tunnel up)

## Cross-post Notes

- r/selfhosted: emphasize the "no cloud, no SaaS" angle, mention JupyterHub as
  self-hosted alternative to Google Colab / institutional HPC
- r/rust: emphasize pure Rust, no C deps, WGSL GPU compute, darkforest
  validator. Different audience — they care about the code, not the hardware
- r/linux: Pop!_OS angle, systemd user services, sovereignty framing
