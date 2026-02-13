
ecoPrimals Node inventory. ~$15k in cost. Westgate was a tower I built while in the service. Southgate was my recent gaming tower but was upgraded for the mesh. Northgate was all new parts, everything else was Facebook Marketplace finds and Newegg sales.

## Towers

| Node | CPU | GPU | NPU | RAM | Storage | OS | Primary Role / Notes |
|------|-----|-----|-----|-----|---------|----|--------------------|
| **Northgate** | Intel **i9-14900K** | **RTX 5090** | — | **192GB DDR5** | 1TB 990 Pro + 4TB 990 EVO | (TBD) | Flagship AI/LLM compute, main hub |
| **Southgate** | Ryzen **5800X3D** | **RTX 3090** | — | **128GB DDR4** | 1TB 990 EVO (Win) + 4TB 990 EVO (Linux) | Win + Linux | Gaming + heavy compute |
| **Eastgate** *(upgraded)* | Intel **i9-12900** | **RTX 4070** | **1x Akida NPU** | **32GB DDR5-4800** | 2TB 990 EVO Plus | (TBD) | Utility compute + neuromorphic |
| **Strandgate** | **Dual EPYC 7452** (64 cores) | **RTX 3090** + **RX 6950 XT** | **2x Akida NPU** (PCIe) | **256GB ECC DDR4** | 2×2TB NVMe + 4×4TB NVMe (Hyper M.2) + HDD/SSD pool | Pop!_OS *(likely)* | Bioinformatics powerhouse, multi-GPU + neuromorphic |
| **Westgate** *(former Nestgate tower)* | Intel **i7-4771** | **RTX 2070 SUPER** | — | **32GB DDR3** | ~76TB HDD ZFS + 2TB NVMe cache | (TBD) | Cold storage, NAS, caching layer |
| **Swiftgate** | Ryzen **5800X** | **RTX 3070 FE** | — | **64GB DDR4** | NVMe | (TBD) | Mobile/compact compute node |
| **FlockGate** | Intel **i9-13900K** | **RTX 3070 Ti** | — | **64GB DDR5** | 2TB NVMe (Gamestop) | Ubuntu 24.04.3 | Brother's node / flock compute |
| **KinGate** | Intel **i7-6700K** | **RTX 3070** | — | **32GB DDR4** (2×16 @ ~3400) | SATA / NVMe (PCIe 3.0) | Pop!_OS | Rebuild tower / staging / utility compute |
| **BlueGate** | (TBD) | — *(none currently)* | — | **128GB DDR4** | 2TB NVMe | Windows | General compute / expansion node |

## Small Form Factor

| Node | CPU | RAM | Storage | OS | Role |
|------|-----|-----|---------|----|----|
| **GMKtec NucBox M6** | (integrated) | **32GB** | (TBD) | (TBD) | Compact node / edge compute |
| **Intel NUC (NUC6CAY) x3** | Intel Celeron J3455 | (stock) | (TBD) | (TBD) | Lightweight relay / discovery nodes |

## Mobile & Security

| Node | SoC / Type | Role |
|------|-----------|------|
| **Pixel 8a** | Google Tensor G3 | Mobile BearDog / HSM seed carrier / mesh node |
| **SoloKeys x4** | FIDO2 / WebAuthn (USB) | Physical roots of trust for BearDog key hierarchy |

## Networking

| Component | Specification | Status |
|-----------|--------------|--------|
| **10G Switch** | 10 Gigabit Ethernet | Acquired |
| **10G NICs (copper) x4** | Northgate, Southgate, Eastgate, Westgate | Installed |
| **10G Cables** | Cat6a / DAC | Pending purchase |

## Neuromorphic

| Component | Location | Count |
|-----------|----------|-------|
| **BrainChip Akida NPU** (PCIe) | Strandgate | 2 |
| **BrainChip Akida NPU** | Eastgate | 1 |
| **Total NPUs detected** | — | 160 (across 3 cards) |

