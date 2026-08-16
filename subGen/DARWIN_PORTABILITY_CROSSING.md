# Darwin Portability Crossing — graftGate Proves the Thesis

**Status**: CROSSED | **Wave**: 157i | **Date**: Aug 11, 2026
**Gate**: graftGate (M4 Mac Mini, `aarch64-apple-darwin`, Apple Silicon)

---

## What Crossed

gen0 said "sovereign on any hardware." gen2 defined cellMembrane as the platform
abstraction layer (TargetOs, CpuArch, LinkModel). gen4 proved the pattern on Windows
(blueGate) and Android (grapheneGate).

Wave 157i proved **darwin** — the 5th OS family, the 2nd ISA beyond x86_64 to run
the full stack. graftGate compiled 15/15 primals on first attempt with only 4
one-liner fixes. WireGuard mesh joined the organism within hours.

This is not a story about cross-compilation. It is the proof that the organism is
**portable by construction** — cellMembrane's abstractions carry the full stack to
new silicon without advance preparation or architectural rework.

---

## Hardware

| Attribute | Value |
|-----------|-------|
| Device | Mac Mini (2024) |
| SoC | Apple M4 |
| ISA | `aarch64-apple-darwin` |
| CPU | 10-core (4P + 6E) |
| Memory | 24 GB unified |
| Storage | 512 GB NVMe |
| Network | Gigabit Ethernet |
| WireGuard IP | `10.13.37.13` |
| Peers reachable | 6 |
| RTT to golgiBody | 38ms |

---

## Compilation Results

**15/15 primals compiled** on `aarch64-apple-darwin`:

| Primal | Result | Binary Size |
|--------|--------|-------------|
| bearDog | PASS | Mach-O arm64 |
| songBird | PASS | Mach-O arm64 |
| skunkBat | PASS | Mach-O arm64 |
| cellMembrane | PASS | Mach-O arm64 |
| toadStool | PASS | Mach-O arm64 |
| barraCuda | PASS | Mach-O arm64 |
| coralReef | PASS | Mach-O arm64 |
| nestGate | PASS | Mach-O arm64 |
| rhizoCrypt | PASS | Mach-O arm64 |
| loamSpine | PASS | Mach-O arm64 |
| sweetGrass | PASS | Mach-O arm64 |
| swarmVine | PASS | Mach-O arm64 |
| petalTongue | PASS | Mach-O arm64 |
| squirrel | PASS | Mach-O arm64 |
| biomeOS | PASS | Mach-O arm64 |

Total payload: **~98.1M** Mach-O arm64

---

## The Four Fixes

All four required fixes were one-liners. All merged upstream within hours.

| Fix | Primal | Commit | Nature |
|-----|--------|--------|--------|
| 1 | bearDog | `24dd74d` | Darwin conditional in platform detection |
| 2 | toadStool | `e172eb0c3` | macOS sandbox path adjustment |
| 3 | squirrel | config update | Architecture-specific config path |
| 4 | petalTongue | `4d46f3e3` | Darwin signal handling compatibility |

Four fixes out of 15 primals × thousands of modules = the abstraction layer works.
The ratio of "touch" to "total surface area" is vanishingly small.

---

## cellMembrane Proven

cellMembrane (`TargetOs`, `CpuArch`, `LinkModel`) now demonstrated on:

| ISA | OS | Gate | Wave |
|-----|----|------|------|
| `x86_64` | Linux (musl) | eastGate, sporeGate, westGate, strandGate, ironGate, southGate | gen3+ |
| `x86_64` | Linux (glibc) | strandGate (GPU), southGate | gen4+ |
| `x86_64` | Windows | blueGate | 152+ |
| `aarch64` | Linux | golgiBody (VPS) | 153+ |
| **`aarch64`** | **darwin** | **graftGate** | **157i** |

The 4th ISA-OS combination. The 5th OS family. The 2nd non-Linux desktop OS.

---

## What This Proves

### 1. Portability by Construction

cellMembrane is not a portability shim bolted on after the fact. It is
the foundational abstraction that every primal builds atop. graftGate proves
this: no architectural rework was needed. Four one-liners — all platform-detection
edge cases, not structural failures.

### 2. Organism, Not Binary

The 15 primals don't just compile — they compose on the new platform. Tower Atomic
(songBird + swarmVine + skunkBat + cellMembrane), the communication layer, carries
to darwin unchanged. The composition model is silicon-agnostic.

### 3. WireGuard Mesh in Hours

graftGate joined the organism's WireGuard mesh (`10.13.37.13`) and reached 6 peers
within hours of first compilation. RTT to golgiBody: 38ms. The gate isn't just
compiled — it's **enmeshed**.

### 4. piGate/riscGate Credibility

The same patterns that carried ecoPrimals to darwin will carry to:
- **piGate** — Raspberry Pi 500, `aarch64-unknown-linux-gnu` ($190, classroom deployment)
- **riscGate** — Milk-V Jupiter 2, `riscv64gc-unknown-linux-gnu` ($300+, 60 TOPS NPU)

cellMembrane already handles the ISA (`aarch64` proven). The Linux kernel already
runs on both. The remaining work is link-model validation, not architectural.

---

## The Generational Arc

```
gen0:  "Sovereign on any hardware" (philosophy)
gen2:  cellMembrane TargetOs/CpuArch/LinkModel (design)
gen3:  x86_64-linux validated across 5+ gates (engineering)
gen4:  Windows (blueGate 10/10) + Android (grapheneGate) (expansion)
157i:  darwin (graftGate 15/15) — nearly without issue (proof)
next:  aarch64-linux (piGate) + riscv64-linux (riscGate) (deployment)
```

The portability thesis is no longer a claim. It is a measured, operational crossing.
Five OS families. Two ISAs proven (third on order). The organism goes where
the silicon is, not where the vendor allows.

---

## Remaining

- **Forgejo SSH key registration**: graftGate needs depot push access for full CI participation
- **Depot build**: darwin binaries need BLAKE3-verified depot entry
- **GPU validation**: M4 Metal/MPS shader testing (barraCuda darwin path) not yet exercised
- **songBird MeshRelay**: Full gossip participation blocked without relay (same as all non-Linux gates)

---

*subGen Wave 157i — Darwin portability crossed. graftGate: M4 Mac Mini,
aarch64-apple-darwin, 15/15 primals, 4 one-liner fixes, WireGuard LIVE at
10.13.37.13, 6 peers, 38ms RTT. cellMembrane proven on 4th ISA-OS combination.
Portability thesis: operational, not theoretical.*
