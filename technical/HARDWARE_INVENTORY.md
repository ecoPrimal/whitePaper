# Hardware Inventory — ecoPrimals Sovereign Mesh

**Last updated**: Oct 20 2026 | **Wave**: 193+
**Author**: Kevin Mok / ecoPrimal / attsi | **ORCID**: [0009-0004-2141-0321](https://orcid.org/0009-0004-2141-0321)
**Location**: House 1 + House 2, Lansing MI (10G fiber interconnect)
**Total Investment**: ~$17,000 | **Metabolic Budget**: $485/month
**Topology**: Klein bottle (WAN membrane = LAN cytoplasm, non-orientable)
**Architecture Families**: 9 compile targets across 8 ISA families

**Prior relics** (cited, not canonical):
- `attsi/metal.md` (Jul 30, 2026) — earliest personal inventory, pre-membrane
- `gen3/about/HARDWARE.md` (May 2026) — historical snapshot
- `wateringHole/HARDWARE.md` (Sep 27, 2026, Wave 158+) — most detailed relic, includes ISA landscape and SteamOS matrix
- `sporePrint/content/science/14_sovereign_compute_hardware.md` — science paper mapping three-tier precision model to hardware

---

## The Principle: Membrane Changes Everything

Before the Klein bottle topology (Oct 20, 2026), VPS nodes ran heavy compute:
bloom classification, Forgejo, neural APIs. The membrane was 885 MB thick on a
2 GB VPS. Swap at 51%. Services choking.

**The insight**: VPS = membrane (thin surface). LAN = cytoplasm (heavy compute).
A membrane is the thinnest possible surface between inside and outside. On a
Klein bottle, there IS no inside/outside — ingress = egress. Traffic exits
through the WAN membrane and folds back to the LAN through the same surface.

**What this means for hardware**:
- The LAN fleet is the REAL compute. 200+ cores, 1.4 TB RAM, 244 GB GPU VRAM.
- The VPS is just the routing surface. Caddy, opsonize, skunkbat. 196 MB total.
- Gates are SIBLING NODES, not subordinates. BirdSong auto-discovers peers.
- Progressive reveal: visitors see the membrane first, then the science, then
  the hardware. The bingo card fills in as trust builds.
- pepti (VPS) is the refraction point — the 0d topological pinch where the
  Klein bottle folds. It's not broken; it's where the surface inverts.

---

## Live Mesh — Oct 20, 2026 Probe

14 hosts alive on `192.168.4.0/24`:

| IP | Gate | Status | OS | Notes |
|----|------|--------|----|-------|
| 192.168.4.1 | **sporeGate** | ✅ UP | Linux | Router, NAT, DHCP, DNS, NUCLEUS |
| 192.168.4.2 | **CRS310** | ✅ UP | RouterOS | MikroTik 10G backbone switch |
| 192.168.4.3 | **sporeGate-alt** | ✅ UP | Linux | Secondary IP |
| 192.168.4.103 | **eastGate-2nd** | ✅ UP | Linux | 2nd NIC or WireGuard |
| 192.168.4.107 | **graftGate** | ✅ UP | macOS | Apple M4 Mac Mini (!) |
| 192.168.4.111 | **Omada SX3008F** | ✅ UP | L2+ | TP-Link 10G SFP+ switch |
| 192.168.4.147 | **northGate** | ✅ UP | Windows | RTX 5090, 96 GB DDR5 |
| 192.168.4.154 | **unknown-1** | ✅ UP | Linux | ac:41:6a MAC — tower? |
| 192.168.4.163 | **unknown-2** | ✅ UP | Linux | Randomized MAC — Pi 500? |
| 192.168.4.170 | **unknown-3** | ✅ UP | Linux | Intel NIC (e8:38:a0) — tower? |
| 192.168.4.197 | **unknown-4** | ✅ UP | Linux | HP/Aruba MAC (a0:d0:dc) |
| 192.168.4.200 | **epson-et2400** | ✅ UP | Linux | Printer |
| 192.168.4.244 | **eastGate** | ✅ UP | Linux | i9-12900K, RTX 4070, 128 GB DDR5 |
| 192.168.4.250 | **Flint 2** | ✅ UP | OpenWrt | WiFi AP (GL.iNet MT6000) |

**Resolved but DOWN** (DNS exists, no ping):
- ironGate (192.168.4.237), strandGate (192.168.4.169), blueGate (192.168.4.210)

**Unresolved** (no DNS, offline):
- westGate, southGate, biomeGate, swiftGate, kinGate

---

## Gate Fleet — Full Hardware

### ONLINE — Active Development

#### eastGate — Overwatch + Primary Development (THIS MACHINE)

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel i9-12900K (16C/32T, P+E cores) |
| **GPU** | NVIDIA RTX 4070 (12 GB GDDR6X, Ada Lovelace) |
| **NPU** | BrainChip Akida AKD1000 (Phase C sovereign — zero vendor SDK) |
| **RAM** | 128 GB DDR5 |
| **Storage** | 1.8 TB NVMe (836 GB free) |
| **Network** | 10G SFP+ (fiber to House 2 backbone) |
| **OS** | Pop!_OS 22.04 (kernel 6.17.9) |
| **WireGuard** | 10.13.37.3 |
| **Vulkan** | 1.3.280, NVIDIA driver 580.126.18 |
| **Steam** | Installed, logged in |
| **Role** | LAN HPC anchor, daily driver, development, gaming, cytoplasm hub |

**Membrane role**: This is the cytoplasm. All heavy compute that was on
the VPS (skunky-ingest, biomeos, Forgejo, neutron-burst) belongs here.
The Klein bottle folds back to this machine.

#### northGate — Gaming Primary + Strongest Single GPU

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Ryzen 9 9950X3D (16C/32T, 3D V-Cache) |
| **GPU** | NVIDIA RTX 5090 (32 GB GDDR7, Blackwell SM120) |
| **RAM** | 96 GB DDR5 |
| **Storage** | 5 TB NVMe (1 TB OS + 4 TB games) |
| **Network** | 10G NIC (copper, CRS310 backbone) |
| **OS** | Windows 11 |
| **LAN IP** | 192.168.4.147 |
| **Services** | SMB open, SSH/RDP closed |
| **Role** | Gaming primary, strongest single GPU in fleet, sibling mesh node |

**Membrane role**: Sibling peer, not subordinate. When gaming = gaming.
When available = most powerful single GPU for compute dispatch. The
5090 at 32 GB GDDR7 is the fleet's heaviest hitter for df64 and ML.

#### sporeGate — Sovereignty Boundary (Router)

| Component | Specification |
|-----------|---------------|
| **Device** | GMKtec NucBox M6 |
| **CPU** | AMD Ryzen 5 6600H (6C/12T) |
| **RAM** | 27 GB DDR5 |
| **Storage** | NVMe |
| **NIC WAN** | 2.5G RJ45 |
| **NIC LAN** | 2.5G RJ45 |
| **OS** | Pop!_OS 22.04 |
| **WireGuard** | 10.13.37.2 |
| **Role** | NAT router, firewall, DHCP, DNS, NUCLEUS, build foreman, depot signer |

**Membrane role**: The plasma membrane — the actual boundary between
LAN and WAN. All traffic crosses sporeGate. nftables rules = the
composition-deterministic firewall. This is the ONLY gate that touches
both the internet and the internal mesh simultaneously.

#### graftGate — Darwin Builder (Apple Silicon) — ALIVE ON MESH

| Component | Specification |
|-----------|---------------|
| **SoC** | Apple M4 (10C: 4P+6E, 10-core GPU, 16-core Neural Engine) |
| **RAM** | 16–24 GB unified LPDDR5 |
| **Storage** | NVMe (internal) |
| **Network** | 1G Ethernet |
| **OS** | macOS (Sequoia) |
| **LAN IP** | 192.168.4.107 |
| **Role** | Sole Darwin compilation authority. 16/16 aarch64-apple-darwin depot. |

**Discovered alive on today's probe.** Was listed as OFFLINE in prior
inventories. The M4 is running on the LAN mesh.

### OFFLINE — Power Rebalance (House 2)

These gates have DNS records but did not respond to ping. They are physically
present on the 10G backbone in House 2.

#### ironGate — Primal Workhorse

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel i9-14900K (24C/32T, P+E cores) |
| **GPU** | NVIDIA RTX 5070 (12 GB, Blackwell SM120) |
| **RAM** | 96 GB DDR5 |
| **Storage** | 3.6 TB NVMe |
| **Role** | Agentic development, composition validation, aarch64-linux cross-builder |
| **LAN IP** | 192.168.4.237 (DOWN) |

#### strandGate — Bioinformatics Powerhouse

| Component | Specification |
|-----------|---------------|
| **CPU** | Dual AMD EPYC 7452 (64C/128T total) |
| **GPUs** | NVIDIA RTX 3090 (24 GB) + AMD RX 6950 XT (16 GB) |
| **NPU** | BrainChip Akida AKD1000 |
| **RAM** | 256 GB DDR4 ECC |
| **Storage** | 18 TB NVMe (2×2TB + 4×4TB Hyper M.2) |
| **Role** | HPC, dual-vendor GPU validation, lattice QCD production |
| **LAN IP** | 192.168.4.169 (DOWN) |

**Key asset**: The ONLY gate with both NVIDIA and AMD GPUs — dual-vendor
sovereign compute path. RX 6950 XT has 1:16 f64 rate (vs 1:64 on NVIDIA
consumer cards). Critical for coralReef cross-vendor validation.

#### westGate — Sovereign Data NAS

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Ryzen 7 5700X (8C/16T) |
| **GPU** | NVIDIA RTX 3070 (8 GB) |
| **RAM** | 64 GB DDR4 |
| **Storage** | **50.7 TB ZFS raidz1** (5×14TB) + 2TB SSD cache + 1.8TB NVMe boot |
| **Role** | Cold storage archive, provenance data root, 153 datasets |

**The biggest single storage node.** 50.7 TB ZFS is where loamSpine's
permanence data lives at rest. AlphaFold data (~1 TB) pending move here.

#### southGate — Full NUCLEUS + Canary

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Ryzen 7 5800X3D (8C/16T, 3D V-Cache) |
| **GPU** | NVIDIA RTX 4060 (8 GB, Ada Lovelace) |
| **RAM** | 128 GB DDR4 |
| **Storage** | 4.5 TB NVMe |
| **Role** | Full NUCLEUS deployment, validation canary |

#### biomeGate — HBM2 Test Bench

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Threadripper 3970X (32C/64T) |
| **Display GPU** | NVIDIA RTX 5060 (8 GB GDDR7) |
| **Work GPUs** | 2× Titan V (12 GB HBM2 ea) + 2× MI50 (16 GB HBM2 ea) |
| **NPU** | BrainChip Akida AKD1000 |
| **RAM** | 256 GB DDR4 |
| **Storage** | 5 TB NVMe |
| **Role** | HBM2 sovereign compiler dev, hotSpring team home |

**The HBM2 fortress.** 56 GB of high-bandwidth memory across 4 work cards.
Titan V at 1:2 f64 rate = the only fleet cards where native f64 is faster
than df64. The sovereign NVIDIA path runs through these Titan Vs.

#### blueGate — Windows Expansion

| Component | Specification |
|-----------|---------------|
| **RAM** | 128 GB DDR4 |
| **Storage** | 2 TB NVMe |
| **OS** | Windows |
| **LAN IP** | 192.168.4.210 (DOWN) |

#### swiftGate, kinGate — Utility

| Gate | CPU | GPU | RAM | Storage | Role |
|------|-----|-----|-----|---------|------|
| swiftGate | Ryzen 5800X | RTX 3070 FE | 64 GB DDR4 | NVMe | Mobile compute |
| kinGate | i7-6700K | RTX 3070 | 32 GB DDR4 | NVMe | Staging/utility |

### NEW HARDWARE — Bring-up Pending

#### Jupiter 2 — RISC-V Pioneer

| Component | Specification |
|-----------|---------------|
| **SoC** | SpacemiT K3 (RVA23) — 8× X100 @ 2.4 GHz + 8× A100 @ 2.0 GHz |
| **GPU** | IMG PowerVR BXM-4-64-MC1 (Vulkan 1.3) |
| **AI** | Up to 60 TOPS (A100 + IME2 matrix engine) |
| **RAM** | 32 GB LPDDR5 |
| **Network** | **10GbE SFP+** + 1GbE RJ45 + Wi-Fi 6 |
| **Role** | 9th ISA family. RISC-V native builder. Vector compute (1024-bit VLEN). |
| **Power** | 11W idle, 22W load |

The first RVA23-compliant board. Mandatory vector extensions, mandatory
hypervisor. The 10GbE SFP+ is the fastest NIC in House 1.

#### 3× Raspberry Pi 500 — ARM64 Cluster

| Component | Specification |
|-----------|---------------|
| **SoC** | BCM2712 (Cortex-A76 4C @ 2.4 GHz) |
| **RAM** | 8 GB LPDDR4X each |
| **Power** | ~5W idle each |
| **Role** | Mesh gossip peers, site hosts, aarch64 validation fleet |

All 15 aarch64 primal binaries already exist in the depot. Zero
compilation needed — just deploy. Three run 24/7 at ~15W total.

### REMOTE

#### flockGate — Brother's Node (NYC)

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel i9-13900K (24C/32T) |
| **GPU** | NVIDIA RTX 3070 Ti (8 GB) |
| **RAM** | 64 GB DDR5 |
| **Storage** | 2 TB NVMe |
| **WireGuard** | 10.13.37.6 (29ms to golgi) |
| **Role** | Remote covalent mesh node |

### MOBILE + SECURITY

| Device | SoC/Type | Role |
|--------|----------|------|
| **Pixel 8a** (grapheneGate) | Google Tensor G3, GrapheneOS | Mobile bearDog, HSM seed carrier |
| **iPhone XS** (iosGate) | Apple A12 Bionic | iOS deploy target (pending signing cert) |
| **SoloKey ×4** | FIDO2 / WebAuthn USB | Physical roots of trust for bearDog |

### STEAM / GAMING HARDWARE

| Device | SoC | Role | Status |
|--------|-----|------|--------|
| **Steam Deck Gen 1** (LCD, 512GB) | AMD Aerith (Zen 2 + RDNA 2) | Portable SteamOS gate | 🔧 Battery + boot repair |
| **Steam Frame** | Snapdragon 8 Gen 3 (ARM64!) | VR gate, ARM SteamOS | 📦 Incoming |
| **Steam Controllers ×2** | TMR trackpads | VR/gaming input | ✅ Operational |
| **Steam Link** | Marvell ARMADA 1500 | Legacy stream relay | ✅ Operational |

### CLOUD (WAN Membrane — Thin Surface Only)

| Node | Provider | vCPU | RAM | Role | Status |
|------|----------|------|-----|------|--------|
| **golgi** | DO NYC1 | 1 | 2 GB | Caddy TLS, opsonize, skunkbat, songbird | ✅ THIN (196 MB) |
| **golgi-ext** | DO NYC1 | ? | ? | Nucleus mirror, Circle of Willis sync | ✅ UP |
| **pepti** | DO NYC1 | 2 | 4 GB | Refraction point (0d Klein fold) | ⏰ TIMEOUT |

**Membrane rule**: VPS services must stay under 200 MB RSS total.
Heavy compute refracts back to LAN through the Klein bottle.

---

## Work Card Pool (Swappable GPUs)

| Card | Qty | VRAM | Type | Current Home |
|------|-----|------|------|-------------|
| RTX 3090 | 3 | 24 GB GDDR6X each | Compute | strandGate (1) + float (2) |
| Titan V | 2 | 12 GB HBM2 each | HBM2 (1:2 f64!) | biomeGate |
| MI50 | 2 | 16 GB HBM2 each | HBM2 (sovereign amdgpu) | biomeGate |
| Tesla K80 | 1 | 24 GB GDDR5 (2×12) | Legacy Kepler | biomeGate |

**128 GB aggregate work pool VRAM** (48 GB GDDR6X + 56 GB HBM2 + 24 GB GDDR5).

---

## Neuromorphic (3× Akida AKD1000)

| Card | Location | Status |
|------|----------|--------|
| AKD1000 | eastGate | Phase C sovereign (pure Rust, zero vendor SDK, 18.8K Hz) |
| AKD1000 | biomeGate | PCIe |
| AKD1000 | strandGate | PCIe |

rustChip: 367 tests, 10 undocumented hardware discoveries. First non-Python
path to the hardware. Sub-milliwatt ESN phase classification.

---

## Physical Topology

```
AT&T Fiber ──► BGW320-500 (WAN boundary)
                  │
              sporeGate (NAT/FW/DHCP/DNS)
                  │ 2.5G
                  ▼
              CRS310 10G backbone
              ┌─────┬─────┬──────────┐
              │     │     │          │
        northGate  (spare)  sfp+1    sfp+2
        (Win/5090)         Omada     eastGate
                           SX3008F   (i9/4070/Akida)
                           (House 2) ← 10G fiber → (House 1)
                              │
                    ┌─────────┼────────────┐
                    │         │            │
              strandGate  southGate    TL-SG605S
              biomeGate   ironGate     Flint 2 (WiFi)
              westGate    blueGate        │
                                     swiftGate (WiFi)
                                     grapheneGate (WiFi)

House 1: eastGate(10G), sporeGate(2.5G), Jupiter 2(10G SFP+), Pi 500s(1G),
          graftGate(1G), NUCs(1G), biomeGate(1G)
House 2: ALL towers on 10G via MikroTik CRS310 + Omada SX3008F
WAN:     golgi(VPS), golgi-ext(VPS), pepti(VPS), flockGate(NYC)
WiFi:    Flint 2 → swiftGate, grapheneGate
```

---

## Aggregates

| Resource | Total |
|----------|-------|
| **Named gates** | 20+ |
| **ISA families** | 8 (x86-64, ARMv8, ARMv9, Apple Silicon, RISC-V, WASM, SteamOS x86, SteamOS ARM) |
| **CPU cores** | 200+ |
| **System RAM** | **~1.4 TB** |
| **GPU VRAM (display)** | ~80 GB |
| **GPU VRAM (work pool)** | ~128 GB |
| **GPU VRAM (total)** | **~244 GB** |
| **HBM2** | 56 GB (2× Titan V + 2× MI50) |
| **Storage (NVMe)** | ~46 TB |
| **Storage (HDD/ZFS)** | ~51 TB |
| **Storage (total)** | **~97 TB** |
| **NPU** | 3× Akida AKD1000 + Apple Neural Engine + SpacemiT IME2 |
| **HSM** | 4× SoloKey FIDO2 + Android StrongBox + Apple Secure Enclave |
| **10G nodes** | 8+ (House 2 all-10G + eastGate fiber + Jupiter 2 SFP+) |
| **Compile targets** | 9 |
| **GPU vendors** | NVIDIA + AMD + IMG PowerVR |
| **CPU vendors** | Intel + AMD + Apple + Google + SpacemiT + Broadcom + Qualcomm |
| **Memory types** | DDR3, DDR4, DDR4 ECC, DDR5, LPDDR4X, LPDDR5, LPDDR5X, HBM2 |

---

## How the Membrane Changes How We Use It

### Before (overpacked VPS, Feb–Oct 2026)

The VPS tried to be everything: Forgejo, bloom classification, neural API,
web terminals, log ingestion. 885 MB on a 2 GB box. Swap at 51%. Services
crashing. The membrane was too thick — cytoplasmic machinery packed into
the lipid bilayer.

### After (Klein bottle, Oct 20 2026)

| Layer | Where | What | RSS |
|-------|-------|------|-----|
| **Membrane (VPS)** | golgi | Caddy, opsonize, skunkbat, songbird, fail2ban | ~196 MB |
| **Cytoplasm (LAN)** | eastGate + fleet | skunky-ingest, biomeos, Forgejo, heavy compute | unlimited |
| **Refraction** | pepti | 0d Klein fold — signal bends back | N/A |

### What Each Gate Becomes

| Gate | Before | After (Klein bottle) |
|------|--------|---------------------|
| **eastGate** | Dev machine | **Cytoplasm anchor** — heavy compute, gaming, daily driver |
| **northGate** | Remote compute | **Gaming primary + strongest GPU peer** — sibling, not subordinate |
| **golgi** | Overpacked VPS | **Thin membrane** — routing only, 196 MB |
| **strandGate** | Offline | **HPC when powered** — dual-vendor QCD production |
| **westGate** | Offline | **Cold storage** — 50.7 TB ZFS, loamSpine permanence |
| **biomeGate** | Offline | **HBM2 lab** — sovereign driver development |
| **graftGate** | "Offline" | **Alive!** — Darwin builder, on mesh right now |

### Progressive Reveal (Bingo Card = QR Identity)

The hardware IS the identity. Each gate is a cell on the bingo board.
Trust level determines what's visible:

| Trust Level | What You See |
|-------------|-------------|
| 0 (stranger) | primals.eco — the membrane surface |
| 1 (curious) | sporePrint papers — the science |
| 2 (engaged) | detroit data, classification — the evidence |
| 3 (trusted) | Hardware topology — the metal |
| 4 (bonded) | attsi — the human behind the membrane |

The bingo card fills in through interaction. Each cell revealed is a
hardware capability proven by the visitor's own engagement. You don't
TELL them you have 200 cores and 1.4 TB RAM — they DISCOVER it by
interacting with the membrane until the trust threshold exposes the
next layer.

---

## Identification Needed

5 alive hosts on the LAN mesh that need physical walk-up identification:

| IP | MAC | Likely |
|----|-----|--------|
| 192.168.4.154 | ac:41:6a:* | Unknown tower |
| 192.168.4.163 | 92:8a:a8:* (randomized) | Pi 500? |
| 192.168.4.170 | e8:38:a0:* (Intel) | Tower with Intel NIC |
| 192.168.4.197 | a0:d0:dc:* (HP/Aruba) | Unknown |
| 192.168.4.103 | (unknown) | eastGate 2nd NIC? |

---

## Changelog

- **Oct 20, 2026 (Wave 193+)**: Full rewrite to modern surface. Klein bottle
  membrane topology. Live LAN probe (14 hosts). graftGate discovered alive.
  Progressive reveal / bingo card identity model. Cited prior relics
  (attsi/metal.md, wateringHole/HARDWARE.md, HARDWARE_INVENTORY.md Jul 2026).
  Membrane thickness rule: VPS < 200 MB RSS. Heavy compute → LAN cytoplasm.
- **Sep 27, 2026 (Wave 158+)**: wateringHole/HARDWARE.md — ISA landscape,
  SteamOS matrix, Jupiter 2, Pi 500s, Steam Frame. Most detailed prior relic.
- **Jul 30, 2026**: attsi/metal.md — personal voice, origin story of the metal.
- **Jul 13, 2026 (Wave 138a)**: This file's previous version — K-Derm layer
  mapping, full tower specs, security/mobile, work card pool.
- **Jun 18, 2026 (Wave 116)**: Initial network topology document.

---

*Built from scratch. Consumer hardware and old datacenter tech. Two houses,
one fiber link, one brother. A Steam Deck with a bad battery. An Army vet
who went from infantry to microbiology to data science to building a
sovereign compute mesh in a basement. The metal is real.*
