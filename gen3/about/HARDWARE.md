# Basement HPC - Node Inventory

**Total Investment**: ~$15,000  
**Location**: Basement, Lansing MI area  
**Network**: Local ethernet mesh with 10 Gigabit backbone (switch acquired, NICs installed, cables pending)  
**Last Updated**: February 2026

---

## Overview

The ecoPrimals ecosystem runs on a heterogeneous cluster of physical machines, purchased and assembled over several years. Westgate was originally built during Army service (2012-2015). Southgate was a gaming tower upgraded for the mesh. Northgate was all new parts. Everything else was Facebook Marketplace finds and Newegg sales.

This is the physical reality that the NUCLEUS architecture and bonding model were designed for. The hardware is heterogeneous by nature - DDR3 to DDR5, RTX 2070 to RTX 5090, 32GB to 256GB RAM - and the architecture treats this heterogeneity as a feature. Each gate runs the NUCLEUS atomics that match its hardware, and biomeOS coordinates the mesh so workloads land on the right gate.

---

## Towers

### Northgate - Flagship AI/LLM Compute

| Component | Specification |
|-----------|--------------|
| **CPU** | Intel i9-14900K |
| **GPU** | NVIDIA RTX 5090 |
| **RAM** | 192GB DDR5 |
| **Storage** | 1TB Samsung 990 Pro + 4TB Samsung 990 EVO |
| **Network** | 10G NIC (copper) |
| **Role** | Primary AI/LLM compute, main hub |

Heavy Node Atomic. This is where Squirrel routes large inference jobs and ToadStool runs GPU-intensive BarraCUDA workloads. The RTX 5090 is the most capable GPU in the mesh.

### Southgate - Gaming + Heavy Compute

| Component | Specification |
|-----------|--------------|
| **CPU** | AMD Ryzen 5800X3D |
| **GPU** | NVIDIA RTX 3090 |
| **RAM** | 128GB DDR4 |
| **Storage** | 1TB 990 EVO (Windows) + 4TB 990 EVO (Linux) |
| **Network** | 10G NIC (copper) |
| **Role** | Gaming + heavy compute |

Balanced Node Atomic. Originally a gaming tower, upgraded for the mesh with 128GB RAM. Dual boot for gaming (Windows) and compute (Linux).

### Eastgate - Utility Compute + Neuromorphic

| Component | Specification |
|-----------|--------------|
| **CPU** | Intel i9-12900 |
| **GPU** | NVIDIA RTX 4070 |
| **NPU** | 1x BrainChip Akida |
| **RAM** | 32GB DDR5-4800 |
| **Storage** | 2TB 990 EVO Plus |
| **Network** | 10G NIC (copper) |
| **Role** | Utility compute, neuromorphic workloads |

Node Atomic with neuromorphic capability. The Akida AKD1000 NPU handles ToadStool's neuromorphic inference workloads alongside traditional GPU compute. **V60 (Feb 2026):** First live AKD1000 validation via pure Rust `akida-driver` — 3 ESN classifiers (QS/Bloom/Disorder) at 18.8K Hz, online (1+1)-ES evolution at 136 gen/sec, 12.9K Hz temporal streaming (p99=76 µs), PUF fingerprint (6.34 bits), coin-cell 11 years. Phase C sovereign driver achieved — zero vendor SDK dependency.

### Strandgate - Bioinformatics Powerhouse

| Component | Specification |
|-----------|--------------|
| **CPU** | Dual AMD EPYC 7452 (64 cores / 128 threads total) |
| **GPU** | NVIDIA RTX 3090 + AMD RX 6950 XT |
| **NPU** | 2x BrainChip Akida (PCIe cards) |
| **RAM** | 256GB ECC DDR4 |
| **Storage** | 2x 2TB NVMe + 4x 4TB NVMe (Hyper M.2) + HDD/SSD pool |
| **OS** | Pop!_OS |
| **Role** | Bioinformatics, multi-GPU + neuromorphic |

Heavy Node Atomic, the most capable multi-substrate compute node. The 64-core dual EPYC with 256GB ECC handles CPU-bound bioinformatics (Kraken2, alignment). The RTX 3090 + RX 6950 XT provide dual-vendor GPU compute - BarraCUDA's WGSL shaders run on both NVIDIA and AMD, validating the universal compute claim. The 2x Akida PCIe cards handle neuromorphic workloads (k-mer filtering benchmarks: 2.3x faster, 53x power efficiency vs CPU).

### biomeGate - Semi-Mobile Mini HPC

| Component | Specification |
|-----------|--------------|
| **CPU** | AMD Threadripper 3970X (32 cores / 64 threads) |
| **GPU** | NVIDIA RTX 3090 + NVIDIA Titan V |
| **NPU** | 1x BrainChip Akida |
| **RAM** | 256GB DDR4 (non-ECC) |
| **Storage** | 1TB NVMe (boot) + 2x 2TB NVMe (work/scratch) |
| **Role** | Semi-mobile heavy compute, lab-deployable mini HPC |

Heavy Node Atomic, designed for portability to labs and extended compute runs. The Threadripper 3970X provides 32 cores for CPU-parallel baselines and verification. The RTX 3090 (24 GB GDDR6X) is the primary GPU compute target — 2× the VRAM of the RTX 4070, enabling 24⁴ dynamical fermion lattices GPU-resident. The Titan V (12 GB HBM2) runs NVK for driver-independent verification (validated on Eastgate, same setup). The Akida NPU handles real-time phase screening. The 5 TB NVMe scratch pool supports large-lattice checkpointing. PCIe lanes are expandable — future additions possible as bandwidth and streaming pipelines mature.

### Westgate - Cold Storage Archive

| Component | Specification |
|-----------|--------------|
| **CPU** | Intel i7-4771 |
| **GPU** | NVIDIA RTX 2070 Super |
| **RAM** | 32GB DDR3 |
| **Storage** | ~76TB HDD (ZFS) + 2TB NVMe cache |
| **Network** | 10G NIC (copper) |
| **Role** | Cold storage, NAS, caching layer |

Heavy Nest Atomic. The oldest gate - built during Army service, still running. The 76TB ZFS pool is the cold storage archive for the entire mesh. NestGate on Westgate manages content-addressed blob storage with ZFS snapshots (100 snapshots in 0.17s). DDR3 and an i7-4771 are not fast, but cold storage needs reliable and big, not fast.

### Swiftgate - Mobile Compute

| Component | Specification |
|-----------|--------------|
| **CPU** | AMD Ryzen 5800X |
| **GPU** | NVIDIA RTX 3070 FE |
| **RAM** | 64GB DDR4 |
| **Storage** | NVMe |
| **Role** | Mobile/compact compute node |

Balanced Node Atomic. Compact form factor for deployments that need to move.

### FlockGate - Flock Compute

| Component | Specification |
|-----------|--------------|
| **CPU** | Intel i9-13900K |
| **GPU** | NVIDIA RTX 3070 Ti |
| **RAM** | 64GB DDR5 |
| **Storage** | 2TB NVMe |
| **OS** | Ubuntu 24.04.3 |
| **Role** | Brother's node / flock compute |

Node Atomic operated by a family member. Connected to the mesh via covalent bonding (shared family seed). Demonstrates the multi-household covalent mesh pattern.

### KinGate - Staging / Utility

| Component | Specification |
|-----------|--------------|
| **CPU** | Intel i7-6700K |
| **GPU** | NVIDIA RTX 3070 |
| **RAM** | 32GB DDR4 (2x16 @ ~3400) |
| **Storage** | SATA / NVMe (PCIe 3.0) |
| **OS** | Pop!_OS |
| **Role** | Staging / utility compute |

Light Node Atomic. Staging and testing node for primal deployments before promotion to production gates.

### BlueGate - Expansion

| Component | Specification |
|-----------|--------------|
| **CPU** | TBD |
| **GPU** | None currently |
| **RAM** | 128GB DDR4 |
| **Storage** | 2TB NVMe |
| **OS** | Windows |
| **Role** | General compute / expansion node |

Future expansion. Windows-primary for testing cross-platform ecoBin deployments. GPU pending.

---

## Small Form Factor Nodes

### GMKtec NucBox M6

| Component | Specification |
|-----------|--------------|
| **RAM** | 32GB |
| **Role** | Compact node / edge compute |

Mini PC for lightweight NUCLEUS deployments - Tower Atomic relay, discovery node, or edge compute.

### Intel NUC (NUC6CAY) x3

| Component | Specification |
|-----------|--------------|
| **CPU** | Intel Celeron J3455 |
| **Role** | Lightweight relay / discovery nodes |

Three low-power NUCs for always-on Tower Atomic deployments: BirdSong relay, STUN server, Dark Forest beacon nodes. These demonstrate that Tower Atomic runs on minimal hardware - the same Pure Rust HTTPS stack that runs on the i9-14900K runs on a Celeron.

---

## Mobile & Security Hardware

### Pixel 8a - Mobile Mesh Node

| Component | Specification |
|-----------|--------------|
| **SoC** | Google Tensor G3 |
| **OS** | Android |
| **Role** | Mobile BearDog / HSM seed carrier / mesh node |

The mobile device described in the bonding model's "HSM-Anchored Composition" pattern. Carries the hardware seed (SoloKey authentication) and runs BearDog for cryptographic operations. Validated with Android StrongBox HSM and SELinux-enforced abstract socket IPC.

### SoloKeys x4 - Hardware Security Modules

| Component | Specification |
|-----------|--------------|
| **Type** | FIDO2 / WebAuthn |
| **Interface** | USB |
| **Role** | Physical roots of trust for BearDog key hierarchy |

Four SoloKey FIDO2 devices provide the physical anchor for the genetic trust model.

---

## Networking

| Component | Specification | Status |
|-----------|--------------|--------|
| 10G Switch | 10 Gigabit Ethernet | Acquired |
| 10G NICs (copper) x4 | Northgate, Southgate, Eastgate, Westgate | Installed |
| 10G Cables (Cat6a / DAC) | — | Pending purchase |

The 10G backbone connects the four primary towers. Once cabled, the covalent mesh's inter-gate bandwidth jumps from 1Gbps to 10Gbps - relevant for NestGate blob replication, ToadStool distributed compute, and Songbird federation traffic.

---

## Aggregate Capabilities

| Resource | Total |
|----------|-------|
| **Towers** | 10 |
| **Small form factor** | 4 (1x NucBox + 3x Intel NUC) |
| **CPU Cores** | 130+ (across all gates) |
| **GPU VRAM** | ~176GB (RTX 5090 + 3x RTX 3090 + Titan V + RX 6950 XT + RTX 4070 + RTX 3070 Ti + 2x RTX 3070 + RTX 2070S) |
| **System RAM** | ~1.2TB (across all gates) |
| **Storage** | ~105TB+ (76TB ZFS cold + NVMe hot across nodes) |
| **GPU Vendors** | NVIDIA + AMD (BarraCUDA universal compute validated on both) |
| **GPU Generations** | RTX 2070 through RTX 5090 (4 NVIDIA generations) + Titan V (Volta) + RX 6950 XT (AMD RDNA 2) |
| **CPU Vendors** | Intel + AMD (i7-4771 through i9-14900K, 5800X through Threadripper 3970X through Dual EPYC 7452) |
| **Memory Types** | DDR3, DDR4, DDR4 ECC, DDR5 |
| **NPU** | 4x BrainChip Akida (213 NPUs total) |
| **HSM** | 4x SoloKey FIDO2 + Android StrongBox |
| **Network** | 10G backbone (4 towers) + 1G mesh (remaining) |

---

## The Heterogeneity Principle

A traditional HPC deploys identical nodes and distributes identical workloads. That's metallic bonding in the NUCLEUS model: delocalized, homogeneous, sub-specialized.

This basement HPC is the opposite. Every gate is different. DDR3 sits next to DDR5. A 12-year-old i7 sits next to a brand-new i9. NVIDIA sits next to AMD. A Celeron NUC runs the same primal binaries as a 64-core EPYC. That's covalent bonding: heterogeneous hardware, united by genetic trust, each specializing in what it does best.

The NUCLEUS architecture handles heterogeneity because the hardware demanded it. The architecture emerged from the constraint of the hardware, just as the Tower Atomic pattern emerged from the constraint of Pure Rust.

---

**Built from scratch. Assembled in a basement. 6 production primals across 14 nodes. ~$15,000. One developer. The metal is real.**
