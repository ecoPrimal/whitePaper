# Deployable Artifact Standard

**How guideStone Becomes a Self-Leveling Benchmark and Portable Science**

**Date**: April 3, 2026
**Status**: First instantiation complete (hotSpring-guideStone-v0.7.0)
**Lineage**: gen4/architecture/GUIDESTONE → this document
**Priors**: infra/wateringHole/EXTERNAL_VALIDATION_ARTIFACT_STANDARD, UNIFIED_ARTIFACT_EVOLUTION

---

## The Concept

A guideStone artifact that sits in a repository certifies the code.
A guideStone artifact on a USB drive certifies the universe.

The Deployable Artifact Standard describes what happens when a
guideStone-certified ecoBin leaves the development environment and enters
the world: handed to a collaborator, plugged into unknown hardware,
shipped to a foreign institution. The artifact must carry everything it
needs to validate itself, characterize the hardware it lands on, and
produce trustworthy output — with no network, no package manager, no
prior relationship with the machine.

This is not software distribution. Software distribution gets the binary
to the user. The Deployable Artifact Standard ensures that when the
binary arrives, **it knows what it is, proves it arrived intact, explains
what it does, validates itself, and benchmarks the machine** — all
before the user types a second command.

---

## Why This Is a gen4 Concept

gen3 solved "does the science work?" The answer was yes — 12,510+ checks,
70+ papers, 7 springs. But the validation lived inside the development
environment. You needed `cargo`, you needed the source tree, you needed
the right Rust toolchain. The science was correct; the science was not
portable.

gen4 asks "who uses it?" The answer requires the science to travel. A
physicist at LANL receives a USB drive. A grad student downloads a `.tar`.
A CI pipeline pulls a container image. In every case, the recipient has
never seen the source code, has never installed Rust, and has no reason
to trust the sender's build environment.

The Deployable Artifact Standard is how guideStone-grade science travels
between institutions, people, and machines without losing its rigor.

---

## Anatomy of a Deployable Artifact

### Layer 1: Entry Point

A single command at the root. No arguments required. No toolchain. No sudo.

```
./hotspring validate         # Linux (ext4, ext3, xfs, btrfs)
sh ./hotspring validate      # Linux (exFAT, FAT32, NFS noexec)
hotspring.bat validate       # Windows
```

The entry point is a shell wrapper that:
1. Validates CHECKSUMS before executing any binary
2. Detects the host OS and architecture
3. Probes GPU availability (Vulkan, /dev/dri, wgpu)
4. Selects the correct binary (static CPU vs. glibc GPU, x86_64 vs. aarch64)
5. Falls back to container execution when native is impossible
6. Dispatches to the selected binary with all arguments forwarded

The entry point absorbs platform complexity. The user types one command.
The artifact figures out the rest.

### Layer 2: Binary Layout

```
bin/
├── x86_64/
│   ├── static/          # musl, zero deps, any Linux since 2014
│   │   └── validate     # CPU-only, all checks
│   └── gpu/             # glibc, dlopen(libvulkan), GPU-accelerated
│       └── validate     # CPU + GPU dual-path
└── aarch64/
    └── static/
        └── validate     # Same physics, ARM architecture
```

The dual-binary strategy resolves a fundamental tension:

- **Static musl** binaries have zero runtime dependencies and run on any
  Linux distribution, any kernel >= 2.6.39, any container, any HPC node.
  But they cannot `dlopen` GPU libraries — Vulkan requires dynamic linking.

- **Dynamic glibc** binaries link against libc, libm, and libgcc_s, which
  exist on every modern Linux distribution. They can `dlopen` Vulkan at
  runtime, enabling GPU acceleration. But they fail on Alpine, older
  glibc, or stripped container images.

Both binaries produce identical physics output for the same input. The
entry point selects the right one. The user never chooses.

### Layer 3: Container Fallback

```
container/
└── hotspring-guidestone.tar    # OCI image, docker load -i
```

When native execution is impossible — macOS (no native Linux), Windows
without WSL2, NFS with noexec, or any environment where the binary
simply cannot run — the artifact ships a pre-built OCI container image.

The container contains: Ubuntu 22.04 base, Vulkan ICD loader, Mesa
drivers, the full artifact, and the same entry point. `docker load` +
`docker run` produces identical output to native execution.

The container is not a convenience. It is a substrate guarantee.

### Layer 4: Integrity

```
CHECKSUMS                  # SHA-256 of every file in the artifact
```

Validated before any binary executes. If a single byte changes — bit
rot on the USB, truncated transfer, cosmic ray — the artifact refuses
to run and reports which file is corrupted.

This is Property 3 (Self-Verifying) made operational. The checksums are
not optional metadata. They are a gate.

### Layer 5: Self-Knowledge

```
liveSpore.json             # Machine-readable deployment manifest
```

Tracks every machine the artifact has visited:

```json
{
  "artifact": "hotSpring-guideStone-v0.7.0",
  "created": "2026-04-02T12:00:00Z",
  "provenance": {
    "builder": "biomeGate.local",
    "git_commit": "abc1234",
    "build_date": "2026-04-02"
  },
  "run_history": [
    {
      "hostname": "biomeGate.local",
      "date": "2026-04-02T15:30:00Z",
      "mode": "gpu",
      "gpu": "NVIDIA RTX 3090",
      "checks": "59/59",
      "duration_s": 42
    },
    {
      "hostname": "lanl-workstation",
      "date": "2026-04-10T09:15:00Z",
      "mode": "cpu",
      "gpu": null,
      "checks": "59/59",
      "duration_s": 180
    }
  ]
}
```

When the drive returns from a collaborator, the `run_history` shows
what happened: which machines, which mode, which GPUs, how many checks,
how long. The artifact accumulates operational knowledge about itself.

### Layer 6: Documentation

```
README                     # Plain text, no renderer needed
GUIDESTONE.md              # Full certification checklist
```

Plain text README because not every machine has a Markdown renderer. The
documentation is part of the artifact, not a URL that might 404. A
physicist reading the USB in a terminal at 2 AM has everything they need.

---

## guideStone as Self-Leveling Benchmark

The deployable artifact has a property that was not designed but emerged:
**the validation is also a benchmark.**

When `./hotspring validate` runs on unknown hardware, it:

1. Discovers the CPU architecture and instruction set
2. Probes GPU adapters (Vulkan devices, memory, f64 capability)
3. Runs 59 physics checks across gradient flow, dielectric response,
   and kinetic-fluid coupling
4. Reports wall time, throughput (trajectories/sec, flow steps/sec),
   and GPU utilization

The physics is the benchmark. The benchmark is the physics. There is no
separate "benchmark mode" that runs synthetic workloads — the validation
suite itself stresses HMC trajectory generation, FFT-based dielectric
computation, explicit Runge-Kutta integration, and sparse linear algebra.
These are the same operations that production lattice QCD uses.

This means the artifact answers two questions simultaneously:

| Question | Answer |
|----------|--------|
| **Is the physics correct on this machine?** | Yes: 59/59 checks pass within derived tolerances |
| **How fast is this machine for this physics?** | Measured: N trajectories/sec, M flow steps/sec, P ms/config |

A PI evaluating a new GPU for their group plugs in the USB, runs one
command, and gets both answers. No installation, no configuration, no
MILC build, no CUDA SDK.

### The Self-Leveling Property

"Self-leveling" means the artifact establishes its own reference frame
on every machine it visits. It does not assume the hardware is correct.
It does not assume the floating-point is precise. It validates, measures,
and reports — then the user knows exactly where they stand.

This is the metrological analogy from GUIDESTONE.md made operational.
The Planck constant does not care which laboratory measures it. The
guideStone artifact does not care which machine runs it. Both produce
results that are properties of the mathematics, not properties of the
instrument.

The difference is that the guideStone artifact also **characterizes the
instrument** as a side effect of measuring the physics. The physicist
learns about their hardware by validating the science.

---

## The Onboarding Pattern

The Deployable Artifact Standard solves a specific human problem: how
do you bring a new collaborator into a computational physics workflow?

### Traditional Onboarding

1. Email back and forth about system requirements
2. Install toolchain (MILC, CUDA, MPI, Chroma, ...)
3. Debug build failures on their specific OS/compiler
4. Share input configurations
5. Run on their machine
6. Compare results via email or shared filesystem
7. Debug discrepancies (is it a bug or a platform difference?)
8. Repeat steps 2-7 until convergence

Elapsed time: days to weeks. Failure rate: high.

### Deployable Artifact Onboarding

1. Hand them the USB / send the tarball
2. They type `./hotspring validate`
3. 59/59 pass
4. They type `./hotspring benchmark`
5. They know their hardware's capability
6. They type `./hotspring generate --beta=6.0 --lattice=8x8x8x16`
7. They have ILDG gauge configurations

Elapsed time: minutes. Failure rate: zero (the artifact adapts to their
machine, or reports exactly what is missing).

This is the Chuna onboarding in practice. When TC Chuna receives the
artifact, he does not need to install Rust, build MILC, or configure
CUDA. He runs one command and validates his own published results on
his own hardware. The artifact is the conversation starter.

---

## Relationship to Other Standards

### ecoBin / genomeBin (Binary Structure)

The Deployable Artifact Standard builds on ecoBin's structural
requirements (Pure Rust, static musl, cross-arch) and adds deployment
machinery. An ecoBin is a correctly built binary. A Deployable Artifact
is a correctly built binary wrapped in detection, fallback, integrity,
self-knowledge, and documentation.

The relationship mirrors the binary ladder:

```
ecoBin (structure)
    + guideStone (verification)
    + Deployable Artifact Standard (portability)
    = Self-leveling science that travels
```

### External Validation Artifact Standard (wateringHole)

The wateringHole standard defines how spring validation artifacts are
structured: `./run`, static musl binaries, `expected/` reference data,
CHECKSUMS, JSON output. The Deployable Artifact Standard generalizes
this to any guideStone ecoBin and adds cross-architecture, cross-OS,
container fallback, and self-knowledge layers.

### liveSpore / ColdSpore (biomeOS Deployment)

biomeOS defines deployment modes: liveSpore (deployable spore),
ColdSpore (cold-start from removable media). The Deployable Artifact
Standard operates within the ColdSpore mode — the `.biomeos-spore`
marker identifies the artifact as biomeOS-aware, and the entry point
integrates with biomeOS's discovery protocols when available.

---

## Cross-Platform Deployment Matrix

| Platform | Method | GPU | Validated |
|----------|--------|-----|-----------|
| Linux (ext4) | Native shell | Yes (Vulkan) | 5 substrates |
| Linux (exFAT/FAT32) | tmpdir fallback | Yes (Vulkan) | Tested |
| Linux (HPC/Slurm) | `srun` with static binary | CPU-only | benchScale |
| Windows (WSL2) | Native Linux in WSL | Yes (GPU passthrough) | Designed |
| Windows (Docker) | Container | Limited | Designed |
| macOS (Docker) | Container | No | Designed |
| VM (agentReagents) | Gate template | CPU-only | benchScale |
| CI/CD | Container + benchScale | Per pipeline | Tested |

---

## Evolution Targets

The first artifact (hotSpring-guideStone-v0.7.0) instantiates the
standard. Future evolution:

| Target | Description | Owner |
|--------|-------------|-------|
| ARM GPU binaries | aarch64 + Vulkan (Apple Silicon via MoltenVK, ARM Mali) | toadStool |
| genomeBin manifest | `manifest.toml` with version, deps, update channel | primalSpring |
| bearDog artifact signing | Ed25519 signature on CHECKSUMS file | bearDog |
| helixVision artifact | Genomics pipeline as deployable guideStone | wetSpring |
| esotericWebb artifact | Creative provenance as deployable guideStone | sporeGarden |
| ILDG guided generation | Generate + validate + convert in single pipeline | hotSpring |
| Multi-artifact composition | Deploy graph with multiple guideStone artifacts | biomeOS |

---

## For esotericWebb and Future gen4 Products

The patterns extracted from hotSpring's deployment artifact are not
physics-specific. The eight-layer architecture (entry point, binary
layout, container fallback, integrity, self-knowledge, documentation,
reference data, cross-OS launchers) applies to any gen4 product that
needs to travel.

An esotericWebb deployable artifact might carry:
- `./webb validate` — runs provenance chain verification
- `./webb benchmark` — measures DAG throughput on local hardware
- Container fallback for non-Linux
- CHECKSUMS and liveSpore.json

A helixVision deployable artifact might carry:
- `./helix validate` — runs variant-calling reproducibility checks
- `./helix benchmark` — measures basecall throughput
- Reference genome data in `expected/`
- Container with MinKNOW integration

The content changes. The standard does not.

---

*The artifact is the argument. The machine is the witness. The
mathematics is the judge.*
