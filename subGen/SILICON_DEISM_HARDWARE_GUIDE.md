# Silicon Deism Hardware Guide — Build, Test, Deploy Anywhere

**Status**: ACTIVE | **Wave**: 155n | **Date**: Jul 31, 2026
**Audience**: eastGate (user) — hardware research and acquisition guide

---

## Current Coverage

The ecosystem has proven primals on two OS families and one CPU architecture.
Silicon deism (gen4's `SILICON_DEISM.md` Tier 1: "atheistic — no vendor-specific
APIs") is operationally validated on x86_64. To reach Tier 2 ("deistic — only
math, energy, silicon") requires proving multiple ISAs and deployment topologies.

### What's Proven (Wave 155n)

| Target Triple | Gate | ISA | OS | NUCLEUS | Sub-Builder |
|---|---|---|---|---|---|
| `x86_64-unknown-linux-musl` | sporeGate | x86_64 | Linux (musl) | 13/13 | Foreman |
| `x86_64-unknown-linux-gnu` | westGate, strandGate | x86_64 | Linux (glibc) | Yes | — |
| `x86_64-pc-windows-gnu` | blueGate | x86_64 | Windows | 13/13 | Sub-builder (J12 live) |

### What's Missing

| Gap | Why It Matters |
|---|---|
| **No ARM** | Single ISA. Can't claim hardware-agnostic. |
| **No macOS** | Two OS families (Linux, Windows). Darwin is the third major. |
| **No cloud/WAN gate** | Every gate is LAN mesh. No proof of WAN enrollment or trust boundary crossing. |
| **No RISC-V** | Open ISA — the checkmate for vendor independence claims. |
| **No resource-constrained** | All gates are beefy towers. No proof biomeOS works on $80 hardware. |

---

## Tier 1 — Acquire Now

### Mac Mini M4 (appleGate)

**Role**: Production gate + ARM macOS sub-builder + Darwin validation
**Target triple**: `aarch64-apple-darwin`
**Why M4 over M2**: More current to the fleet. The M4 is the latest Apple Silicon
(Oct 2024), so hardware knowledge and toolchain support will be most relevant
for the project's lifespan. It can serve as both a remote gate AND a builder,
which the M2 could do but with less headroom.

| Spec | Mac Mini M4 (base) | Mac Mini M4 (recommended) |
|---|---|---|
| **CPU** | 10-core (4P + 6E), 4.4 GHz boost | Same |
| **GPU** | 10-core, hardware ray tracing | Same |
| **Neural Engine** | 16-core | Same |
| **RAM** | 16 GB unified | **24 GB unified** (biomeOS + primals + builds) |
| **Storage** | 256 GB SSD | **512 GB SSD** (depot mirror + source trees) |
| **Memory bandwidth** | 120 GB/s | Same |
| **Network** | Gigabit Ethernet (configurable 10GbE) | Gigabit is fine |
| **Ports** | 3x TB4 (back) + 2x USB-C (front) + HDMI | Same |
| **WiFi** | Wi-Fi 6E, Bluetooth 5.3 | Same |
| **Size** | 5" x 5" x 2", 0.67 kg | Same |
| **Price** | ~$799 new / ~$679 refurb | ~$999 new (24/512) |

**What to configure**: Get the **24 GB / 512 GB** model. 16 GB is tight if running
biomeOS + 13 primals + Rust compilation simultaneously. 512 GB gives room for
a depot mirror. Skip 10GbE — Gigabit is fine for a validation gate and the
Thunderbolt ports can do 10G via adapter if needed later.

**What it proves for silicon deism**:
- `aarch64-apple-darwin` — new ISA (ARM) + new OS (Darwin) in one device
- `Platform::detect()` works on a third OS family
- biomeOS orchestration on ARM silicon
- songBird IPC on Darwin Unix domain sockets
- Sub-builder capability: native `aarch64-apple-darwin` builds
- Can cross-compile `aarch64-unknown-linux-gnu` (with target added)
- Rosetta 2 can test `x86_64-apple-darwin` binaries (universal builds)

**Familiarization tasks** (do before the hardware arrives):
1. Read the Rust `aarch64-apple-darwin` platform support page
2. Check which primals use `#[cfg(target_os)]` — those need audit
3. Review cellMembrane `Platform::detect()` for Darwin support
4. Check if any primal uses Linux-specific syscalls (epoll vs kqueue)
5. Review songBird transport — Darwin uses UDS like Linux, but paths differ

**Where to buy**: Apple refurb store, or new at apple.com. The 24/512 config
shows up on refurb periodically at ~$850.

---

## Tier 2 — Acquire Next Wave

### Raspberry Pi 5 (piGate)

**Role**: ARM Linux validation + edge/resource-constrained proof
**Target triple**: `aarch64-unknown-linux-gnu`
**Why**: Proves primals run on $80 hardware. ARM Linux is the most important
cloud target (AWS Graviton, Oracle Ampere, all ARM servers). Also proves
biomeOS doesn't assume beefy resources.

| Spec | Value |
|---|---|
| **CPU** | Broadcom BCM2712, quad-core Cortex-A76 @ 2.4 GHz |
| **RAM** | 8 GB LPDDR4X-4267 (get the 8 GB model) |
| **Storage** | microSD + **NVMe via M.2 HAT** (get this — SD is too slow for Rust builds) |
| **Network** | Gigabit Ethernet, Wi-Fi 5 (802.11ac), Bluetooth 5.0 |
| **GPU** | VideoCore VII (Vulkan 1.2 — barraCuda could theoretically run) |
| **PCIe** | Gen 2 x1 via M.2 HAT (395 MB/s NVMe reads) |
| **Power** | 5V/5A USB-C (27W max) |
| **Price** | ~$80 (8 GB) + ~$15 M.2 HAT + ~$30 NVMe = ~$125 total |

**What it proves for silicon deism**:
- ARM Linux native — the most important cross-arch target
- Resource-constrained: Can biomeOS + 13 primals fit in 8 GB with 4 cores?
- Rust compiles natively on ARM (2x faster than QEMU on x86, per benchmarks)
- Edge/field deployment proof — imagine a primal node in a remote location
- $80 → $3000+ cost spread: same primals, same depot, wildly different silicon

**Familiarization tasks**:
1. **Get an NVMe + M.2 HAT** — Rust compilation on microSD is unusable
2. Install Raspberry Pi OS 64-bit (Debian Bookworm based) or Ubuntu 24.04 ARM
3. Install Rust via rustup — `aarch64-unknown-linux-gnu` is Tier 1 (fully supported)
4. Try `cargo build` on a medium-complexity Rust project to gauge compile times
5. Review biomeOS memory footprint — does it fit in 8 GB with all primals?

**Where to buy**: raspberrypi.com approved resellers, Adafruit, Micro Center.
Get the official active cooler (~$5) — sustained Rust compilation hits 85C
without cooling and throttles.

### Oracle Cloud ARM VM (cloudGate)

**Role**: WAN enrollment + cloud deployment + trust boundary validation
**Target triple**: `aarch64-unknown-linux-gnu` (same as Pi 5, but cloud)
**Why**: Proves the golgi depot → gate enrollment → mitoBeacon flow works over
WAN. Tests latency tolerance, NAT traversal, and stateless bootstrap.

| Spec (Always Free tier, as of Jul 2026) | Value |
|---|---|
| **Shape** | VM.Standard.A1.Flex (Ampere Altra) |
| **CPU** | 2 OCPUs (ARM Neoverse N1) |
| **RAM** | 12 GB |
| **Storage** | 200 GB block volume (Always Free) |
| **Network** | Cloud VCN, public IP, configurable security lists |
| **OS** | Oracle Linux or Ubuntu |
| **Price** | **$0/mo** (Always Free, life of account) |

**NOTE**: Oracle quietly halved the free tier from 4 OCPU / 24 GB to 2 OCPU /
12 GB on Jun 15, 2026. Still generous vs other cloud providers, and plenty
for a validation gate.

**What it proves for silicon deism**:
- **WAN enrollment**: Gate enrolls from the internet, not LAN
- **Trust boundary**: mitoBeacon genetics across networks you don't control
- **Latency tolerance**: songBird IPC, health pings over 50ms+ RTT
- **NAT traversal**: Does the membrane work behind cloud NAT?
- **Stateless bootstrap**: Fresh VM → point at golgi → self-enroll to NUCLEUS
- **ARM Linux in cloud**: Same target triple as Graviton, Ampere everywhere

**This is your southGate validation gate concept**, but free and cloud-hosted.

**Familiarization tasks**:
1. Sign up for Oracle Cloud free tier (requires credit card, but Always Free never charges)
2. Spin up a `VM.Standard.A1.Flex` with Ubuntu 22.04
3. Install Rust, clone ecoPrimals, try a basic primal build
4. Test connectivity to golgi (HTTP, SSH, WireGuard)
5. Attempt manual enrollment: pull depot binaries, start biomeOS, check health

**Where**: [cloud.oracle.com/free](https://cloud.oracle.com/free)

---

## Tier 1b — Deploy From Existing Hardware

### Steam Deck OLED (steamGate)

**Role**: Handheld NUCLEUS + immutable OS deployment proof + portable compute
**Target triple**: `x86_64-unknown-linux-musl` (static, already in depot)
**Why**: SteamOS 3 is Arch Linux with a **read-only root filesystem**. The primals
must run entirely from user-space paths (`~/.local/bin/`). This is the same
deployment pattern that proved G17 on southGate — but on a handheld with an
immutable OS. It proves primals don't need root, don't need systemd, don't need
a writable rootfs.

| Spec | Steam Deck OLED |
|---|---|
| **CPU** | AMD Zen 2, 4C/8T, 2.4/3.5 GHz |
| **GPU** | RDNA2 8 CUs (800 MHz), Vulkan 1.3 |
| **RAM** | 16 GB LPDDR5 |
| **Storage** | 512 GB / 1 TB NVMe |
| **Network** | WiFi 6E, Bluetooth 5.3 |
| **OS** | SteamOS 3 (Arch Linux, read-only rootfs) |
| **Price** | ~$449 (512 GB) / ~$549 (1 TB) |

**Deployment pattern** (identical to southGate):

```bash
# Desktop Mode → terminal
mkdir -p ~/.local/bin
for primal in bearDog songBird skunkBat nestGate rhizoCrypt loamSpine sweetGrass \
  petalTongue squirrel biomeOS toadStool barraCuda coralReef; do
  curl -sL "https://depot.primals.eco/musl/${primal}" -o ~/.local/bin/${primal}
  chmod +x ~/.local/bin/${primal}
done
# Run NUCLEUS from user script — no systemd needed
~/.local/bin/biomeOS nucleus --user-space
```

**Key facts**:
- **NOT like grapheneGate** — no ADB, no Termux. It's regular Linux.
- musl binaries from the depot are statically linked — zero glibc dependency,
  immune to SteamOS version skew.
- Home directory (`/home/deck/`) persists across SteamOS updates.
- No `pacman` (wiped on updates). Use Flatpak or Distrobox for tools.
- RDNA2 GPU: coralReef/barraCuda could dispatch Vulkan compute shaders.
- Autostart via `~/.config/autostart/` for persistence across reboots.

**What it proves for silicon deism**:
- Immutable OS deployment — rootfs is read-only, primals don't care
- Handheld form factor — same NUCLEUS, pocket-sized
- AMD GPU compute on a portable device (Vulkan 1.3)
- $449-549 cost point — wildly different from tower gates

### reefGate — NUC + Synology Storage Pair

**Role**: Specialized data results depot + G23 fractional replication target
**Target triple**: `x86_64-unknown-linux-musl` (NUC runs primals)
**Why**: Separates intelligence (primals on NUC) from storage (RAID on Synology).
The Synology DS224+ is a 2-bay NAS with RAID management, SMART monitoring,
and 24/7 low-power operation. The DDR3-era NUC is the "owner" gate that runs
Tower + Nest Atomic primals and treats the Synology as a network-attached
storage volume via NFS.

**Architecture**:

```
DDR3 NUC (reefGate)          Synology DS224+ (storage)
┌─────────────────────┐      ┌──────────────────┐
│ Tower Atomic (3)    │      │ Intel J4125 x86_64│
│   bearDog           │      │ 2 GB DDR4         │
│   songBird          │      │ 2× SATA bays      │
│   skunkBat          │      │ RAID-managed       │
│                     │      │ SMART monitoring   │
│ Nest Atomic (4)     │ NFS  │ Always-on (24/7)   │
│   nestGate ─────────┼──────┤ /volume1/cas/      │
│   rhizoCrypt        │      │ /volume1/results/  │
│   loamSpine         │      │                    │
│   sweetGrass        │      └──────────────────┘
└─────────────────────┘
```

**The "tug and pull" pattern**: Other NUCLEUS gates push science data results
to reefGate via songBird IPC. nestGate addresses and deduplicates into CAS.
Provenance Trio signs and attests. Data lands on the Synology-backed NFS mount.
Any gate can pull results back via `nest.get`. The Synology never runs primals —
it handles drives, RAID, power. The NUC handles trust, provenance, addressing.

| Component | Spec | Role |
|---|---|---|
| **Dell OptiPlex 3020M (D08U)** | Haswell i3/i5, 16 GB DDR3 (2×8), **Samsung 870 EVO 2 TB** (local SATA SSD), GbE, ~35W | Runs 7 primals (Tower + Nest Atomic). 870 EVO = hot tier (CAS index, recent results, primal bins). Synology = cold tier (archive, bulk, replicated). Same architecture as westGate but purpose-oriented for data results. |
| **DS224+** | Celeron J4125, 2 GB, 2× SATA bays | NFS-exported RAID volume for CAS storage |
| **Intel NUC6CAY** (spare) | Celeron J3455, 16 GB DDR3L, WiFi, 10W | Reserved for future role: canary gate, friendGate (remote WAN), or steamGate companion. |

**Setup**:
1. Synology: Enable NFS (Control Panel → File Services → NFS). Export `/volume1/cas/`.
2. NUC: Minimal Linux (Debian server). Mount NFS share. Deploy musl bins from depot.
3. Enrollment: songBird discovers mesh. nestGate advertises CAS. biomeOS routes `nest.store`/`nest.get`.

**What it proves for silicon deism**:
- Paired-device deployment — intelligence and storage separated
- NAS appliance as ecosystem storage (no primals on locked-down DSM)
- G23 fractional replication — westGate primary CAS, reefGate replica on separate hardware + drives
- Legacy hardware reuse — DDR3 NUC is otherwise idle

---

## Tier 3 — Glacial (Research + Familiarize Now, Acquire When Ready)

### RISC-V Board

**Role**: Third ISA proof — the open instruction set
**Target triple**: `riscv64gc-unknown-linux-gnu` (Rust Tier 2 with Host Tools)
**Why**: RISC-V is the only major ISA not controlled by a single vendor (Intel owns
x86, ARM Holdings licenses ARM). Proving primals on RISC-V is the "checkmate"
for silicon deism — three ISAs, all open or commodity, same binaries from the
same depot.

#### Board Comparison (Jul 2026)

| Board | SoC | Cores / Freq | RAM | Storage | Price | Best For |
|---|---|---|---|---|---|---|
| **StarFive VisionFive 2** | JH7110 | 4x SiFive U74 @ 1.5 GHz | 8 GB LPDDR4 | NVMe (M.2) + microSD | ~$65 | **Best first board.** Most mature Linux ecosystem. NVMe slot. Debian, Ubuntu, openSUSE all supported. Mesa Vulkan drivers mainlined. |
| **Milk-V Mars** | JH7110 | 4x SiFive U74 @ 1.5 GHz | 8 GB LPDDR4 | eMMC + microSD | ~$70 | Same SoC as VF2 in Pi 3B form factor. Good if you want compact. No NVMe. |
| **Banana Pi BPI-F3** | SpacemiT K1 | 8x X60 @ 1.6 GHz | 16 GB | eMMC + microSD | ~$80 | 8 cores, RVV 1.0 vector extension, 2 TOPS NPU. Better compute, younger ecosystem. |
| **Milk-V Jupiter** | SpacemiT M1 | 8x X60 @ 1.6 GHz | 16 GB | Mini-ITX, NVMe | ~$90 | Mini-ITX form factor — fits in a PC case. Same SoC as BPI-F3. |
| **Sipeed LicheePi 4A** | T-Head TH1520 | 4x C910 @ 2.0 GHz | 16 GB | eMMC + microSD | ~$130 | Fastest single-core. 4 TOPS NPU. |
| **Milk-V Pioneer** | SOPHON SG2042 | **64x C920 @ 2.0 GHz** | Up to 128 GB DDR4 | PCIe x16, 5x SATA, 2x M.2 | ~$300 (board) / ~$1300 (box) | Workstation-grade. mATX. PCIe x16 slot for GPU. Native RISC-V development machine. |

#### Recommendation

**Start with the StarFive VisionFive 2** ($65). Rationale:
- Most mature Linux support (Debian 13 Trixie, kernel 6.6+)
- Has an NVMe M.2 slot (critical for Rust compilation — same lesson as Pi 5)
- Rust `riscv64gc-unknown-linux-gnu` is Tier 2 with Host Tools — full rustup,
  cargo, clippy, rust-analyzer all available natively (checked: all present as
  of Jul 28, 2026)
- ~60-70% of a Raspberry Pi 4's single-threaded speed. Slow but functional.
- GPU has mainline Vulkan drivers (could test barraCuda shader compilation)

**If you want more headroom later**: The Banana Pi BPI-F3 or Milk-V Jupiter give
you 8 cores and RVV 1.0 for $80-90. The Milk-V Pioneer ($300+) is only worth
it if RISC-V becomes a production gate, not just a validation target.

**Key RISC-V Rust facts**:
- `riscv64gc-unknown-linux-gnu`: Tier 2 with Host Tools (official binaries, can
  compile Rust ON the board, not just cross-compile TO it)
- `riscv64gc-unknown-linux-musl`: Tier 2 without Host Tools (cross-compile only)
- Cross-compilation from sporeGate works TODAY via `cross-rs` + QEMU
- QEMU riscv64 user-mode emulation is mature for unit tests; less battle-tested
  for socket/IPC integration tests

**Familiarization tasks** (can do now without hardware):
1. On sporeGate: `rustup target add riscv64gc-unknown-linux-gnu`
2. Try cross-compiling a primal: `cross build --target riscv64gc-unknown-linux-gnu`
3. Run unit tests under QEMU: `cross test --target riscv64gc-unknown-linux-gnu`
4. Note what breaks — this tells you what needs fixing before real hardware
5. Read the VisionFive 2 getting-started guide and Debian image install docs
6. Check which primals use architecture-specific code (`#[cfg(target_arch)]`)

### Other Architectures (Awareness Only)

These are not acquisition targets but worth understanding for completeness:

| Architecture | Rust Target | Status | Hardware | Notes |
|---|---|---|---|---|
| **ARM 32-bit** | `armv7-unknown-linux-gnueabihf` | Tier 2 | Pi Zero 2W ($15) | Increasingly irrelevant. 64-bit ARM covers this. |
| **PowerPC** | `powerpc64le-unknown-linux-gnu` | Tier 2 | Talos II ($3000+) | Open firmware, open ISA. Too expensive for validation. |
| **s390x** | `s390x-unknown-linux-gnu` | Tier 2 | IBM Z (cloud only) | Mainframe. Cross-compile only unless you rent cloud time. |
| **WASM** | `wasm32-wasi` | Tier 2 | Any (wasmtime) | Browser/edge runtime. Not relevant for gate deployment but interesting for primal portability. |
| **LoongArch** | `loongarch64-unknown-linux-gnu` | Tier 2 | Loongson boards ($100+) | Chinese ISA. Interesting geopolitically but very niche ecosystem. |

---

## Build + Test Matrix After Full Acquisition

With Mac Mini M4 + Pi 5 + Oracle Cloud + VisionFive 2, the coverage is:

### Native Build + Native Test (Gold)

| Target | Gate | ISA | OS | Deployment Type |
|---|---|---|---|---|
| `x86_64-unknown-linux-musl` | sporeGate | x86_64 | Linux | Sovereign CI builder |
| `x86_64-unknown-linux-gnu` | westGate | x86_64 | Linux | Data federation root |
| `x86_64-pc-windows-gnu` | blueGate | x86_64 | Windows | Sub-builder |
| `x86_64-unknown-linux-musl` | **steamGate (Deck)** | x86_64 | SteamOS (immutable) | Handheld, user-space only |
| `x86_64-unknown-linux-musl` | **reefGate (NUC+Synology)** | x86_64 | Linux + NAS storage | Paired-device, tug-and-pull |
| `aarch64-apple-darwin` | appleGate (M4) | ARM64 | macOS | Darwin validation |
| `aarch64-unknown-linux-gnu` | piGate (Pi 5) | ARM64 | Linux | Resource-constrained |
| `aarch64-unknown-linux-gnu` | cloudGate (Oracle) | ARM64 | Linux (cloud) | WAN enrollment |
| `riscv64gc-unknown-linux-gnu` | riscGate (VF2) | RISC-V | Linux | Third ISA proof |

### Cross-Compile + Emulated Test (Silver)

| Target | Build On | Test Via |
|---|---|---|
| `aarch64-unknown-linux-gnu` | sporeGate | QEMU aarch64 (mature) |
| `riscv64gc-unknown-linux-gnu` | sporeGate | QEMU riscv64 (good for unit tests) |
| `x86_64-apple-darwin` | appleGate | Rosetta 2 (excellent) |
| `armv7-unknown-linux-gnueabihf` | sporeGate | QEMU arm (mature) |

### Summary

| Dimension | Count |
|---|---|
| **ISAs** | 3 (x86_64, ARM64, RISC-V) |
| **OS families** | 3 (Linux, Windows, macOS) |
| **Deployment topologies** | 3 (LAN mesh, WAN cloud, WAN friend) |
| **Cost spread** | $0 (Oracle) → $80 (Pi) → $65 (RISC-V) → $800 (M4) → $15K+ (strandGate) |
| **Native test targets** | 9 |
| **Cross + emulated targets** | 4 |
| **Rust tier coverage** | Tier 1 (x86 Linux/Mac/Win, ARM Linux) + Tier 2 (RISC-V, musl, ARM Mac) |

---

## Acquisition Timeline

```
TOMORROW (Aug 2 — planned service interruption):
  ☐ Move ATT gateway + Synology DS224+ to basement (house 1)
    → Planned eth disruption window for troubleshooting + validation
    → All hardware in house 1 localized (basement + 1st floor)
  ☐ steamGate: Deploy musl bins from depot on Steam Deck    → EXISTING HARDWARE
  ☐ reefGate: DDR3 NUC + DS224+ NFS pair                   → EXISTING HARDWARE

NOW (this wave):
  ☐ Mac Mini M4 24GB/512GB (~$999)        → appleGate
  ☐ Oracle Cloud free tier ARM VM ($0)     → cloudGate

NEXT WAVE (springs+gardens prep):
  ☐ Raspberry Pi 5 8GB + NVMe kit (~$125)  → piGate
  ☐ StarFive VisionFive 2 8GB (~$65)       → riscGate

TOTAL: ~$1,190 new + existing fleet (Steam Deck + DS224+ + DDR3 NUC)
```

## What You (the User) Should Start Familiarizing With

### Immediate (this week)

1. **macOS Rust development** — Install Xcode Command Line Tools awareness.
   Know that macOS uses `kqueue` not `epoll`, Mach ports not Linux capabilities,
   and `launchd` not `systemd`. These are the three system-level differences
   that will surface first.

2. **Darwin IPC differences** — UDS works the same as Linux, but abstract
   sockets (`\0` prefix) don't exist on macOS. songBird needs `bind_mode: tcp`
   or filesystem UDS paths. Check if any primal uses abstract sockets.

3. **Oracle Cloud Console** — Sign up, explore the dashboard. The Ampere A1
   shape requires navigating the "create instance" flow and selecting the
   `VM.Standard.A1.Flex` shape with 2 OCPU / 12 GB. It's not obvious in the UI.

### Near-Term (before hardware arrives)

4. **RISC-V cross-compilation** — Run `cross build` and `cross test` for
   `riscv64gc-unknown-linux-gnu` on sporeGate. Find what breaks before you
   have to debug it on slow hardware.

5. **Pi 5 NVMe setup** — Read the M.2 HAT+ installation guide. Know that
   you need to update the Pi 5 bootloader (via microSD) to boot from NVMe.
   The default bootloader only boots from SD.

6. **VisionFive 2 Debian image** — Download the latest Debian 13 image from
   StarFive's GitHub releases. Flash to microSD, boot, verify. The first boot
   experience is less polished than Raspberry Pi.

### Ongoing

7. **`#[cfg]` audit** — Any primal code using `#[cfg(target_os = "linux")]`
   or `#[cfg(target_arch = "x86_64")]` is a silicon deism gap. The cellMembrane
   `Platform::detect()` fix (d7026d7) established the pattern — these should
   all flow through cellMembrane's abstractions.

8. **Depot multi-arch** — Think about how golgi depot serves binaries for 7+
   target triples. Current depot structure is `{primal}-{triple}`. This scales,
   but the builder pipeline needs to know which sub-builders can produce which
   targets.

---

*subGen Wave 155n — Silicon Deism Hardware Guide. 3 ISAs × 3 OS families ×
3 deployment topologies. Acquisition path: Mac Mini M4 + Oracle Cloud (now),
Pi 5 + VisionFive 2 (next wave). ~$1,190 total. Familiarization tasks for
macOS, RISC-V cross-compilation, and cloud enrollment provided.*
