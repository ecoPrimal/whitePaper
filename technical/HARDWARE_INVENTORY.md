# Hardware Inventory — ecoPrimals Sovereign Cluster

**Last updated**: Jul 13 2026 | **Wave**: 138a
**Location**: 4422 Southgate Ave / 641 Samantha Ave, Lansing MI
**Total Investment**: ~$15,000

**Canonical source**: This file is the single source of truth for all physical
hardware in the ecosystem. `gen3/about/HARDWARE.md` is the historical snapshot
(May 2026) — refer here for current state.

---

## K-Derm Layer Mapping

Each physical device maps to a position in the K-Derm cell envelope model
(see `gen5/foundations/KDERM_DIDERM_ENVELOPE.md`, `cellMembrane/specs/K_DERM_TOPOLOGY.md`).

```
 Extracellular          ATT BGW320 (WAN boundary) ── Internet
       │                    │
 Outer Membrane         golgi VPS (Forgejo, relay, Caddy TLS)
       │                    │
 Periplasm              WireGuard overlay, RustDesk relay, cascade pipeline
       │                    │
 ╔═══════════════════════════════════════════════════════════════════╗
 ║ PLASMA MEMBRANE      sporeGate (nftables, NAT, DHCP, DNS)       ║
 ║                      ─── composition-deterministic firewall ──── ║
 ║                      cellMembrane/crates/.../firewall.rs         ║
 ╚═══════════════════════════════════════════════════════════════════╝
       │
 Cytoplasm              Hub 1: CRS310 (L2) — sporeGate, eastGate, northGate
                        Hub 2: Omada (L2+) — towers, TL-SG605S, Flint 2 (AP)
                        All NUCLEUS processes, UDS IPC
```

---

## Sovereignty Boundary (Router)

| Field | Value |
|-------|-------|
| **Device** | GMKtec NucBox M6 ("sporeGate") |
| **CPU** | AMD Ryzen 5 6600H (6C/12T, 4.5GHz boost) |
| **RAM** | 28 GB DDR5 (measured; spec sheet says 32 GB) |
| **Storage** | 929 GB NVMe |
| **NIC WAN** | 2.5G RJ45 (enp1s0) |
| **NIC LAN** | 2.5G RJ45 (eno1) |
| **WiFi** | Wi-Fi 6E (wlp3s0) — OOB fallback |
| **OS** | Pop!_OS 22.04 |
| **Role** | NAT router, firewall, DHCP, DNS, NUCLEUS (13 primals), build authority, depot signer |
| **LAN IP** | 192.168.4.1 / 192.168.4.3 |
| **WireGuard** | 10.13.37.2 |

---

## Internet Gateway

| Field | Value |
|-------|-------|
| **Device** | AT&T BGW320-500 |
| **Type** | Fiber ONT + Router |
| **Admin URL** | http://192.168.1.254 |
| **WAN** | AT&T Fiber |
| **LAN IP** | 192.168.1.254 |
| **Mode** | NAT router (target: IP passthrough to sporeGate) |

---

## L2 Backbone Switch (10G)

| Field | Value |
|-------|-------|
| **Device** | MikroTik CRS310-8G+2S+IN |
| **Ports** | 8x 2.5G RJ45 + 2x 10G SFP+ |
| **Mode** | Pure L2 bridge |
| **Management IP** | 192.168.4.2 |
| **RouterOS** | 7.19.6 |

---

## L2 Distribution Switch (10G SFP+)

| Field | Value |
|-------|-------|
| **Device** | TP-Link Omada SX3008F |
| **Type** | 8-Port 10GE SFP+ L2+ Managed Switch |
| **Connection** | sfp-sfpplus1 on CRS310 (10G trunk) |
| **LAN IP** | 192.168.4.111 (confirmed Jun 20 via sporeGate probe) |

---

## Local Expansion Switch (2.5G)

| Field | Value |
|-------|-------|
| **Device** | TP-Link TL-SG605S-M2 |
| **Type** | 5-Port 2.5G Multi-Gigabit Desktop Switch |
| **Management** | Unmanaged |

---

## WiFi AP — Hub 2

| Field | Value |
|-------|-------|
| **Device** | GL.iNet Flint 2 (GL-MT6000) |
| **Chipset** | MediaTek MT7986A (Filogic 830) |
| **WiFi** | Wi-Fi 6 (AX6000): 2.4GHz + 5GHz + 6GHz-ready |
| **Ports** | 1x 2.5G WAN + 4x 1G LAN |
| **Firmware** | OpenWrt (GL.iNet fork) |
| **Mode** | AP bridge (no NAT, transparent to sporeGate DHCP) |
| **Connection** | Omada SX3008F (house2 zone) |
| **Role** | Human WiFi at hub 2 + swiftGate connectivity |

Eero 6 retired (bridge mode collapse Jun 17-18).

---

## Compute Nodes — Towers

### eastGate — Overwatch + Neuromorphic (PRIMARY)

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel i9-12900 |
| **Display GPU** | NVIDIA RTX 4070 |
| **NPU** | 1× BrainChip Akida AKD1000 |
| **RAM** | 32 GB DDR5-4800 |
| **Storage** | 2 TB 990 EVO Plus |
| **Network** | 10G NIC (copper), CRS310 sfp-sfpplus2 |
| **LAN IP** | 192.168.4.244 (DHCP) |
| **OS** | Pop!_OS 22.04 |
| **Role** | Overwatch, primalSpring (BTSP validation), neuromorphic, compute |
| **Hardware trust** | SoloKey USB (FIDO2 ceremony, Tier 2 entropy) |

Phase C sovereign Akida driver achieved (Feb 2026): 3 ESN classifiers at 18.8K Hz,
online (1+1)-ES evolution at 136 gen/sec.

### northGate — Personal Gaming + Remote Compute + AlphaFold Data

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Ryzen 9 9950X3D |
| **GPU** | NVIDIA RTX 5090 |
| **RAM** | 96 GB DDR5 (2×48 GB) |
| **Storage** | 1 TB NVMe (OS) + 4 TB NVMe (games) + ~1 TB AlphaFold data |
| **Network** | 10G NIC (copper), CRS310 backbone (house1 MikroTik) |
| **OS** | Windows |
| **Role** | Gaming primary, remote access hub, mesh target, AlphaFold staging |
| **RustDesk** | Sovereign relay |
| **Data** | ~1 TB AlphaFold — pending move to westGate + reverse provenance trace |

Primary remote access point for all other gates. Mesh target for songBird
(Windows enrollment). AlphaFold data needs migration to westGate cold storage
when westGate comes back online, with reverse provenance tracing through
loamSpine to establish data lineage.

### ironGate — Agentic Development + Composition Validation

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel i9-14900K (RMA replacement — 3rd unit) |
| **Display GPU** | NVIDIA RTX 5070 |
| **RAM** | 96 GB DDR5 (2×48 GB) |
| **Storage** | 3.6 TB NVMe |
| **OS** | Pop!_OS 22.04 |
| **Role** | Agentic development, composition validation, JupyterHub v5.4.5 |
| **Hardware trust** | SoloKey USB (Phase 1 secondary) |
| **RustDesk** | Sovereign relay |

Node Atomic. Owns primalSpring (composition + deploy quality, shared with
eastGate for BTSP). 13/13 primals active.

### southGate — Gaming + Heavy Compute

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Ryzen 5800X3D |
| **Display GPU** | NVIDIA RTX 4060 |
| **RAM** | 128 GB DDR4 |
| **Storage** | 1 TB 990 EVO (Windows) + 4 TB 990 EVO (Linux) |
| **Network** | 10G NIC (copper) |
| **OS** | Dual boot (Windows/Linux) |
| **Role** | Gaming + heavy compute |
| **RustDesk** | Needs sovereign push |

### strandGate — Bioinformatics Powerhouse (enrollment pending)

| Component | Specification |
|-----------|---------------|
| **CPU** | Dual AMD EPYC 7452 (64 cores / 128 threads) |
| **GPU** | NVIDIA RTX 3090 + AMD RX 6950 XT |
| **NPU** | 1× BrainChip Akida AKD1000 (PCIe) |
| **RAM** | 256 GB ECC DDR4 |
| **Storage** | 2× 2 TB NVMe + 4× 4 TB NVMe (Hyper M.2) |
| **Connection** | Omada SX3008F (house2 zone) |
| **OS** | Pop!_OS |
| **Role** | Bioinformatics, multi-GPU + neuromorphic |
| **Status** | Offline (enrollment pending) |
| **RustDesk** | Needs sovereign push |

### biomeGate — HBM2 Test Bench

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Threadripper 3970X (32 cores / 64 threads) |
| **Display GPU** | NVIDIA RTX 5060 |
| **Work GPUs** | 1× Titan V (12 GB HBM2) + 1× Tesla K80 (24 GB GDDR5). Float: 2nd Titan V + 2× MI50 |
| **NPU** | 1× BrainChip Akida AKD1000 (moved from strandGate) |
| **RAM** | 256 GB DDR4 (non-ECC) |
| **Storage** | 1 TB NVMe (boot) + 2× 2 TB NVMe (work) |
| **PCIe** | 3-card limit (display + 2 work) |
| **Role** | HBM2 sovereign compiler development (hotSpring team) |

### westGate — Cold Storage Archive

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel i7-4771 |
| **GPU** | NVIDIA RTX 2070 Super |
| **RAM** | 32 GB DDR3 |
| **Storage** | ~76 TB HDD (ZFS) + 2 TB NVMe cache |
| **Network** | 10G NIC (copper) |
| **Role** | Cold storage, NAS, caching layer |

nestGate on westGate manages content-addressed blob storage with ZFS snapshots.

### swiftGate — Mobile Compute

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Ryzen 5800X |
| **GPU** | NVIDIA RTX 3070 FE |
| **RAM** | 64 GB DDR4 |
| **Storage** | NVMe |
| **Connection** | WiFi via Flint 2 AP |
| **Role** | Mobile/compact compute node |
| **RustDesk** | Needs sovereign push |

### flockGate — Remote Covalent Mesh (NYC WAN)

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel i9-13900K |
| **GPU** | NVIDIA RTX 3070 Ti |
| **RAM** | 64 GB DDR5 |
| **Storage** | 2 TB NVMe |
| **OS** | Ubuntu 24.04.3 |
| **WireGuard** | 10.13.37.6 (29ms to golgi) |
| **Role** | Validation (primalSpring: 122 scenarios / 1,095+ tests), covalent mesh |

### kinGate — Staging / Utility

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel i7-6700K |
| **GPU** | NVIDIA RTX 3070 |
| **RAM** | 32 GB DDR4 (2×16 @ ~3400) |
| **Storage** | NVMe (PCIe 3.0) |
| **OS** | Pop!_OS |
| **Role** | Staging / utility compute |

### blueGate — Expansion

| Component | Specification |
|-----------|---------------|
| **CPU** | TBD |
| **GPU** | None currently |
| **RAM** | 128 GB DDR4 |
| **Storage** | 2 TB NVMe |
| **OS** | Windows |
| **Role** | General compute / expansion |

---

## Small Form Factor Nodes

### Intel NUC (NUC6CAY) ×3

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel Celeron J3455 |
| **Role** | Lightweight relay / discovery nodes (songBird, STUN, Dark Forest beacons) |

### fieldGate (canary NUC — OFFLINE)

| Field | Value |
|-------|-------|
| **Type** | DDR3 NUC (legacy gen) |
| **Status** | Dead CMOS, open-air surgery |
| **LAN IP** | 192.168.4.36 (was) |

---

## Security & Mobile Hardware

### SoloKey ×4 — Hardware Roots of Trust

| Field | Value |
|-------|-------|
| **Type** | FIDO2 / CTAP2 / WebAuthn |
| **Interface** | USB |
| **Protocol** | CTAP2 with hmac-secret extension |
| **Role** | Physical roots of trust for bearDog key hierarchy |
| **Placement** | eastGate (primary), ironGate (secondary), 2× reserve |
| **bearDog IPC** | `beardog.fido2.discover`, `beardog.fido2.register`, `beardog.fido2.authenticate` |
| **Wave 138 focus** | Tier 2 entropy ceremony activation |

### Pixel 8a — grapheneGate (Mobile Mesh Node)

| Field | Value |
|-------|-------|
| **SoC** | Google Tensor G3 |
| **Security** | Titan M2 (StrongBox HSM) |
| **OS** | Android (GrapheneOS) |
| **Connectivity** | ADB from eastGate, WiFi mesh |
| **Role** | Mobile bearDog, HSM seed carrier, FAMILY_SEED store |
| **bearDog IPC** | TCP-only (13/13 primals), `BindMode::Auto` abstract sockets |
| **Tower** | Live (grapheneGate in ecosystem manifest) |
| **Wave 138 focus** | StrongBox → bearDog keystore, biometric entropy |

---

## VPS (WAN — Outer Membrane)

| Node | IP | CPU | RAM | Storage | Role |
|------|-----|-----|-----|---------|------|
| **golgi** | 157.230.3.183 | 1 vCPU | 2 GB | 50 GB SSD | Caddy TLS, Forgejo (21 repos full-depth), hbbs/hbbr relay, mesh hub |
| **pepti** | 157.230.209.218 | 2 vCPU | 4 GB | — | Build authority (cargo cross-compile), depot staging |

**WireGuard**: golgi (10.13.37.1), sporeGate (10.13.37.2, 71ms), eastGate (10.13.37.3, 35ms), flockGate (10.13.37.6, 29ms).

**Provider**: DigitalOcean NYC1.

---

## Neuromorphic

| Component | Location | Notes |
|-----------|----------|-------|
| BrainChip Akida AKD1000 | eastGate | Phase C sovereign driver (pure Rust, zero vendor SDK) |
| BrainChip Akida AKD1000 | strandGate (PCIe) | Enrollment pending |
| BrainChip Akida AKD1000 | biomeGate | Moved from strandGate |
| **Total** | **3 cards** | |

---

## Work Card Pool

Large GPUs that float between gates based on current workload.

| Card | Qty | VRAM | Type | Current Location |
|------|-----|------|------|------------------|
| RTX 3090 | 2 | 24 GB GDDR6X each | GDDR work | strandGate (1 resident) + 1 float |
| Titan V | 2 | 12 GB HBM2 each | HBM2 work | Float (1 at biomeGate when slotted) |
| MI50 | 2 | 16 GB HBM2 each | HBM2 work | Float pool |
| Tesla K80 | 1 | 24 GB GDDR5 (2×12 GB) | Kepler GK210 | biomeGate |

**Total work pool**: 8 cards, 128 GB aggregate VRAM (48 GB GDDR6X + 56 GB HBM2 + 24 GB GDDR5).

---

## Physical Topology

```
AT&T Fiber ──► BGW320-500 (192.168.1.254)
                  │ 1G RJ45
                  ▼
              sporeGate enp1s0 (192.168.1.233)
              sporeGate eno1 (192.168.4.1) ──2.5G──► CRS310 ether8
                                                       │
              ┌────────────────┬───────────────────────┼──────────────────┐
              │                │                       │                  │
        etherX (2.5G)    etherX (2.5G)          sfp+1 (10G)        sfp+2 (10G)
        northGate        (spare)                Omada SX3008F      eastGate
        (Win/5090)                              (L2+ → house2)     (i9/4070/Akida)
                                                      │
                                                 ┌────┼────────────────┐
                                                 │    │                │
                                               towers strandGate  TL-SG605S  Flint 2
                                              biomeGate southGate  (2.5G)    (WiFi AP)
                                                                              │
                                                                         swiftGate (WiFi)

Hub 1 (backbone/CRS310): sporeGate, eastGate, northGate
Hub 2 (house2/Omada):    strandGate, biomeGate, southGate, TL-SG605S, Flint 2
WAN:                     flockGate (NYC), golgi (DO NYC1), pepti (DO NYC1)
WiFi:                    Flint 2 → swiftGate, grapheneGate (Pixel 8a)
```

---

## Aggregate Capabilities

| Resource | Total |
|----------|-------|
| **Towers** | 11 |
| **Small form factor** | 4 (1× NucBox M6 + 3× Intel NUC) |
| **Mobile** | 1 (Pixel 8a / grapheneGate) |
| **CPU Cores** | 154+ |
| **System RAM** | ~1.0 TB |
| **GPU VRAM (display)** | ~72 GB |
| **GPU VRAM (work pool)** | 128 GB (8 cards) |
| **HBM2** | 56 GB (2× Titan V + 2× MI50) |
| **Storage** | ~122 TB (46 TB NVMe + 76 TB HDD ZFS) |
| **NPU** | 3× BrainChip Akida AKD1000 |
| **HSM** | 4× SoloKey FIDO2 + Titan M2 StrongBox (Pixel 8a) |
| **Network** | 10G backbone (4 towers) + 2.5G/1G mesh + WireGuard overlay |
| **GPU Vendors** | NVIDIA + AMD |
| **CPU Vendors** | Intel + AMD |
| **Memory Types** | DDR3, DDR4, DDR4 ECC, DDR5 |

---

## Changelog

- **Jul 13, 2026 (Wave 138a)**: Reconciled with gen3/about/HARDWARE.md. Added full
  tower specs, security/mobile hardware (SoloKey ×4, Pixel 8a), neuromorphic
  placements, work card pool, aggregate capabilities. Resolved sporeGate RAM
  discrepancy (28 GB measured vs 32 GB spec). Updated flockGate test counts to
  canonical (122 scenarios / 1,095+ tests). Added WireGuard overlay IPs. Removed
  credentials (see vault). This file is now canonical single source of truth.
- **Jun 18, 2026 (Wave 116)**: Initial network topology document.
