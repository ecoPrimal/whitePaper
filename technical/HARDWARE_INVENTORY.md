# Hardware Inventory — ecoPrimals Physical Topology

**Last updated**: Jun 17 2026 | **Wave**: 115
**Location**: 4422 Southgate Ave / 641 Samantha Ave, Lansing MI

---

## K-Derm Layer Mapping

Each physical device maps to a position in the K-Derm cell envelope model
(see `gen5/foundations/KDERM_DIDERM_ENVELOPE.md`, `cellMembrane/specs/K_DERM_TOPOLOGY.md`).

```
 Extracellular          ATT BGW320 (WAN boundary) ── Internet
       │                    │
 Outer Membrane         golgi VPS (Forgejo, relay) + pepti VPS (builds)
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
                        Hub 2: Omada (L2+) — fieldGate, towers, Eero, TL-SG605S
                        All NUCLEUS processes, UDS IPC
```

**Key insight**: L2 switches (CRS310, Omada, TL-SG605S) are *cytoplasm
infrastructure* — they move packets within the trust boundary but enforce
no security policy. sporeGate's nftables IS the plasma membrane. The
`FirewallRuleset::for_composition()` in cellMembrane already generates
these rules programmatically from the membrane composition.

---

## Sovereignty Boundary (Router)

| Field | Value |
|-------|-------|
| **Device** | GMKtec NucBox M6 ("sporeGate") |
| **CPU** | AMD Ryzen 5 6600H (6C/12T, 4.5GHz boost) |
| **RAM** | 28 GB DDR5 |
| **Storage** | 929 GB NVMe |
| **NIC WAN** | 2.5G RJ45 (enp1s0) |
| **NIC LAN** | 2.5G RJ45 (eno1) |
| **WiFi** | Wi-Fi 6E (wlp3s0) — OOB fallback |
| **OS** | Pop!_OS 22.04 |
| **Role** | NAT router, firewall, DHCP, DNS, NUCLEUS (13 primals) |
| **LAN IP** | 192.168.4.1 / 192.168.4.3 |

---

## Internet Gateway

| Field | Value |
|-------|-------|
| **Device** | AT&T BGW320-500 |
| **Type** | Fiber ONT + Router |
| **WiFi SSID** | ATTypcbDby |
| **WiFi Password** | t8k2d4zkbawy |
| **Device Access Code** | #283>#66<> |
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
| **Default Login** | admin / admin |
| **MAC** | EC-75-0C-4C-98-08 |
| **Device Key** | 1E73-A4FF-F547-8EC5-8000 |
| **S/N** | Y24C041000089 |
| **Connection** | sfp-sfpplus1 on CRS310 (10G trunk) |
| **LAN IP** | 192.168.4.115 |

---

## Local Expansion Switch (2.5G)

| Field | Value |
|-------|-------|
| **Device** | TP-Link TL-SG605S-M2 |
| **Type** | 5-Port 2.5G Multi-Gigabit Desktop Switch |
| **Management** | Unmanaged (no config interface) |
| **S/N** | Y24S123000043 |
| **Power** | 9V 0.6A |
| **Role** | Local desktop expansion (additional 2.5G ports) |

---

## WiFi Mesh

| Field | Value |
|-------|-------|
| **Device** | Eero 6 (base station) |
| **Model** | N010001 |
| **FCC ID** | 2AEM4-61704 |
| **Serial** | ND3S-O15V-4SFF-XZPH |
| **Power** | 5.0V 3.0A |
| **Connection** | Omada SX3008F (house2 zone) |
| **NAT subnet** | 10.0.7.x (Eero's own NAT) |
| **Mode** | NAT router for human WiFi at house2 |
| **Extends to** | House 2 (Samantha Ave) coverage via satellite |
| **Role** | Human WiFi only — no compute gates. Collapsing to bridge mode (future). |

---

## Compute Nodes

### eastGate (primary tower)

| Field | Value |
|-------|-------|
| **MAC** | 1C:86:0B:37:63:19 (enp5s0) |
| **Connection** | CRS310 sfp-sfpplus2 (10G) |
| **LAN IP** | 192.168.4.244 (DHCP) |
| **Hostname** | pop-os (needs rename to eastGate) |
| **Role** | Overwatch, primalSpring, compute (Galaxy :8080) |
| **OS** | Pop!_OS |

### northGate (gaming/idle compute)

| Field | Value |
|-------|-------|
| **OS** | Windows |
| **GPU** | NVIDIA RTX 5090 |
| **LAN IP** | TBD (on CRS310 backbone zone) |
| **Connection** | CRS310 (backbone, hub 1) |
| **RustDesk** | ✅ Sovereign relay |
| **SSH** | Windows OpenSSH (needs: Settings → Optional Features → OpenSSH Server) |
| **Role** | Gaming primary. Idle compute (GPU workloads via NUCLEUS). Future: toadStool/barraCuda GPU dispatch. |

### ironGate

| Field | Value |
|-------|-------|
| **RustDesk** | ✅ Sovereign relay |
| **Connection** | TBD |
| **Role** | projectNUCLEUS/ABG compute. Reassigned from cellMembrane ownership. |

### strandGate (on Omada/house2)

| Field | Value |
|-------|-------|
| **RustDesk** | Public relay (needs sovereign push) |
| **Connection** | Omada SX3008F (house2 zone, via TL-SG605S) |

### southGate (on Omada/house2)

| Field | Value |
|-------|-------|
| **RustDesk** | Public relay (needs sovereign push) |
| **Connection** | Omada SX3008F (house2 zone, via TL-SG605S) |

### swiftGate (on Eero WiFi)

| Field | Value |
|-------|-------|
| **RustDesk** | Public relay (needs sovereign push) |
| **Connection** | Eero 6 WiFi (house2 zone, bridged) |

### fieldGate (canary NUC — OFFLINE)

| Field | Value |
|-------|-------|
| **Type** | DDR3 NUC (legacy gen) |
| **Status** | Dead CMOS, open-air surgery |
| **LAN IP** | 192.168.4.36 (was) |
| **Role** | Future: repurpose as old-gen test node |

---

## VPS (WAN)

| Node | IP | CPU | RAM | Role |
|------|-----|-----|-----|------|
| **golgi** | 157.230.3.183 | 1 vCPU | 2 GB | Forgejo, hbbs/hbbr relay, mesh hub |
| **pepti** | 157.230.209.218 | 2 vCPU | 4 GB | Build authority (cargo), depot |

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
        (Win/5090)                              (L2+ → house2)     (compute)
                                                      │
                                                 ┌────┼────┼────────┐
                                                 │    │    │        │
                                               fieldGate towers  TL-SG605S  Eero 6
                                               (offline)         (2.5G)     (WiFi/NAT)

Hub 1 (backbone/CRS310): sporeGate, eastGate, northGate
Hub 2 (house2/Omada):    fieldGate, towers, TL-SG605S, Eero 6 (human WiFi)
WAN:                     flockGate (offsite, public relay)
WiFi coverage:           Eero 6 on Omada → satellite (House 2 humans, NAT 10.0.7.x)
```

---

## Access Credentials Summary

| Device | URL/Method | Username | Password |
|--------|-----------|----------|----------|
| ATT BGW320 | http://192.168.1.254 | — | Device Access Code: #283>#66<> |
| CRS310 | 192.168.4.2 (SSH/HTTP/Winbox) | admin | (set during setup) |
| Omada SX3008F | LAN IP (TBD, likely 192.168.4.115) | admin | admin |
| sporeGate | ssh sporeGate (192.168.4.3) | sporegate | SSH key |
| golgi | ssh root@157.230.3.183 | root | SSH key |
| pepti | ssh root@157.230.209.218 | root | SSH key |
