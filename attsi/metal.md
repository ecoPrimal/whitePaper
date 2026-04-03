# ecoPrimals Node Inventory

**Total Investment**: ~$15,000
**Last Updated**: April 3, 2026

## Topology

Each gate has a **display GPU** (small, permanent) for desktop/lightweight ML,
plus **PCIe slots for swappable work cards** (3090s, HBM2 cards, K80). biomeGate is
the HBM2 test bench (3-card limit: display + 2 work slots until PCIe extension).

## Towers

| Node | CPU | Display GPU | Work GPU / HBM2 | NPU | RAM | NVMe | Role |
|------|-----|-------------|-----------------|-----|-----|------|------|
| **northGate** | Intel i9-14900K | — | RTX 5090 | — | 192 GB DDR5 | ~8 TB | Flagship AI/LLM compute |
| **southGate** | Ryzen 5800X3D | RTX 4060 | swappable | — | 128 GB DDR4 | ~5 TB | Gaming + heavy compute |
| **eastGate** | Intel i9-12900 | RTX 4070 | — | 1× Akida | 32 GB DDR5 | 2 TB | Utility + neuromorphic |
| **strandGate** | Dual EPYC 7452 (64c) | — | RTX 3090 + RX 6950 XT | 1× Akida | 256 GB ECC DDR4 | ~20 TB | Bioinformatics, multi-GPU |
| **biomeGate** | Threadripper 3970X (32c) | RTX 5060 | 1× Titan V + 1× Tesla K80 † | 1× Akida | 256 GB DDR4 | ~5 TB | HBM2 test bench |
| **westGate** | Intel i7-4771 | RTX 2070 Super | — | — | 32 GB DDR3 | 2 TB | Cold storage / NAS |
| **swiftGate** | Ryzen 5800X | RTX 3070 FE | — | — | 64 GB DDR4 | ~2 TB | Mobile compute |
| **flockGate** | Intel i9-13900K | RTX 3070 Ti | — | — | 64 GB DDR5 | 2 TB | Flock compute / covalent mesh |
| **kinGate** | Intel i7-6700K | RTX 3070 | — | — | 32 GB DDR4 | ~1 TB | Staging / utility |
| **blueGate** | TBD | — | — | — | 128 GB DDR4 | 2 TB | Expansion node |

† biomeGate fits 3 cards (display + 2 work). The 2nd Titan V and 2× MI50 are in the float pool, swappable into those slots.

## Work Card Pool (Swappable)

| Card | Qty | VRAM | Type | Current Location |
|------|-----|------|------|------------------|
| RTX 3090 | 2 | 24 GB GDDR6X each | GDDR | strandGate (1 resident) + 1 float |
| Titan V | 2 | 12 GB HBM2 each | HBM2 | biomeGate (1) + 1 float |
| MI50 | 2 | 16 GB HBM2 each | HBM2 | Both float |
| Tesla K80 | 1 | 24 GB GDDR5 (2×12) | Kepler | biomeGate |

## Storage

| Type | Location | Capacity |
|------|----------|----------|
| **NVMe** | All gates | ~49 TB total |
| **HDD** | westGate only | ~76 TB ZFS |
| **Total** | | **~125 TB** |

## Small Form Factor

| Node | CPU | RAM | Role |
|------|-----|-----|------|
| GMKtec NucBox M6 | integrated | 32 GB | Edge compute |
| Intel NUC (NUC6CAY) ×3 | Celeron J3455 | stock | Relay / discovery |

## Mobile & Security

| Node | SoC / Type | Role |
|------|-----------|------|
| Pixel 8a | Google Tensor G3 | Mobile gate / HSM seed carrier |
| SoloKeys ×4 | FIDO2 / WebAuthn (USB) | Physical roots of trust |

## Networking

| Component | Status |
|-----------|--------|
| 10G Switch | Acquired |
| 10G NICs (copper) ×4 | Installed (north, south, east, west) |
| 10G Cables (Cat6a / DAC) | Pending |

## Neuromorphic

| Akida AKD1000 | Location |
|---------------|----------|
| Card 1 | strandGate |
| Card 2 | eastGate |
| Card 3 | biomeGate |

## Aggregates

| Metric | Value |
|--------|-------|
| Towers | 10 |
| SFF nodes | 4 (1× NucBox + 3× NUC) |
| CPU cores | 130+ |
| GPU VRAM (total) | ~188 GB installed + 68 GB float pool |
| HBM2 | 56 GB (2× Titan V + 2× MI50) |
| System RAM | ~1.2 TB |
| NVMe storage | ~49 TB |
| HDD storage | ~76 TB (westGate ZFS) |
| NPUs | 3× BrainChip Akida AKD1000 |
| HSMs | 4× SoloKey FIDO2 + Android StrongBox |
