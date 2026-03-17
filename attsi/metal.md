
ecoPrimals Node inventory. ~$15k in cost. westGate was a tower I built while in the service. southGate was my recent gaming tower but was upgraded for the mesh. northGate was all new parts, everything else was Facebook Marketplace finds and Newegg sales.

## Topology

Each gate has a **display GPU** (small, permanent) for desktop/lightweight ML,
plus **PCIe slots for swappable work cards** (3090s, HBM2 cards). biomeGate is
the HBM2 test bench where the hotSpring team works.

## Towers

| Node | CPU | Display GPU | Work GPU / HBM2 | NPU | RAM | Storage | OS | Role |
|------|-----|-------------|-----------------|-----|-----|---------|----|----|
| **northGate** | Intel **i9-14900K** | — | **RTX 5090** | — | **192 GB DDR5** | 1 TB 990 Pro + 4 TB 990 EVO | (TBD) | Flagship AI/LLM compute, main hub |
| **southGate** | Ryzen **5800X3D** | **RTX 4060** | swappable | — | **128 GB DDR4** | 1 TB 990 EVO (Win) + 4 TB 990 EVO (Linux) | Win + Linux | Gaming + heavy compute |
| **eastGate** | Intel **i9-12900** | **RTX 4070** | — | **1× Akida** | **32 GB DDR5-4800** | 2 TB 990 EVO Plus | (TBD) | Utility compute + neuromorphic |
| **strandGate** | **Dual EPYC 7452** (64c) | — | **RTX 3090** + **RX 6950 XT** | **1× Akida** | **256 GB ECC DDR4** | 2×2 TB + 4×4 TB NVMe + HDD pool | Pop!_OS | Bioinformatics, multi-GPU |
| **biomeGate** | **Threadripper 3970X** (32c) | **RTX 5060** | **2× Titan V** + **2× MI50** | **1× Akida** | **256 GB DDR4** | 1 TB + 2×2 TB NVMe | (TBD) | HBM2 test bench, semi-mobile HPC |
| **westGate** | Intel **i7-4771** | **RTX 2070 Super** | — | — | **32 GB DDR3** | ~76 TB HDD ZFS + 2 TB NVMe | (TBD) | Cold storage, NAS |
| **swiftGate** | Ryzen **5800X** | **RTX 3070 FE** | — | — | **64 GB DDR4** | NVMe | (TBD) | Mobile compute |
| **flockGate** | Intel **i9-13900K** | **RTX 3070 Ti** | — | — | **64 GB DDR5** | 2 TB NVMe | Ubuntu 24.04.3 | Brother's node / flock compute |
| **kinGate** | Intel **i7-6700K** | **RTX 3070** | — | — | **32 GB DDR4** (2×16) | SATA / NVMe (PCIe 3.0) | Pop!_OS | Staging / utility |
| **blueGate** | (TBD) | — | — | — | **128 GB DDR4** | 2 TB NVMe | Windows | Expansion node |

## Work Card Pool (Swappable)

| Card | Qty | VRAM | Type | Current Location |
|------|-----|------|------|------------------|
| RTX 3090 | 3 | 24 GB GDDR6X each | GDDR | strandGate (1) + 2 float |
| Titan V | 2 | 12 GB HBM2 each | HBM2 | biomeGate |
| MI50 | 2 | 16 GB HBM2 each | HBM2 | biomeGate |

## Small Form Factor

| Node | CPU | RAM | Role |
|------|-----|-----|------|
| **GMKtec NucBox M6** | (integrated) | **32 GB** | Compact / edge compute |
| **Intel NUC (NUC6CAY) ×3** | Celeron J3455 | (stock) | Relay / discovery nodes |

## Mobile & Security

| Node | SoC / Type | Role |
|------|-----------|------|
| **Pixel 8a** | Google Tensor G3 | Mobile bearDog / HSM seed carrier |
| **SoloKeys ×4** | FIDO2 / WebAuthn (USB) | Physical roots of trust |

## Networking

| Component | Specification | Status |
|-----------|---------------|--------|
| **10G Switch** | 10 Gigabit Ethernet | Acquired |
| **10G NICs (copper) ×4** | northGate, southGate, eastGate, westGate | Installed |
| **10G Cables** | Cat6a / DAC | Pending |

## Neuromorphic

| Component | Location | Count |
|-----------|----------|-------|
| BrainChip Akida AKD1000 | strandGate | 1 |
| BrainChip Akida AKD1000 | eastGate | 1 |
| BrainChip Akida AKD1000 | biomeGate (from strandGate) | 1 |
| **Total** | | **3 cards** |
