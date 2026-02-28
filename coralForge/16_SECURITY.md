# coralForge Security & Data Sovereignty

## Threat Model

coralForge is designed for scientists who need to predict protein structures on data they cannot or should not upload to a cloud service. The threat model centers on **data sovereignty** — maintaining physical control of biological sequence data throughout the analysis pipeline.

---

## Who Needs This

| User | Concern | coralForge guarantee |
|------|---------|---------------------|
| LTEE researcher | Unpublished genomic data from competitive research | Data never leaves the local machine |
| Clinical lab | Patient-derived sequences under HIPAA/GDPR | No external API calls, no cloud storage |
| Biosecurity analyst | Pathogen sequences requiring containment | Air-gapped operation possible |
| Field biologist | Remote sequencing with no internet | Offline-first by design |
| Sovereign state | National genomic infrastructure | Full source code ownership |

---

## Architecture Guarantees

### No network calls at runtime

coralForge makes zero network calls during structure prediction. There is no telemetry, no license check, no API call, no model download. The binary runs entirely on local compute.

**Verification**: `strace -e trace=network cargo run --bin validate_coral_forge` shows zero socket syscalls.

### No proprietary dependencies

The full dependency chain is open-source with auditable source:

```
coralForge source    → AGPL-3.0-or-later (you own it)
  └── Rust std       → MIT/Apache-2.0
  └── serde/json     → MIT/Apache-2.0 (validation only)
  └── wgpu           → MIT/Apache-2.0 (GPU, via BarraCUDA)
```

No NVIDIA CUDA SDK. No Intel MKL. No Google JAX/TPU runtime. No PyTorch. Nothing that phones home.

### No cloud inference

AlphaFold Server, ESMFold API, and similar services require uploading your sequence to a third-party server. coralForge never does this. The entire pipeline runs on hardware physically controlled by the scientist.

### Reproducible builds

```bash
rustup install 1.82.0
rustup default 1.82.0
cargo build --release
sha256sum target/release/neuralspring
```

Same compiler version + same source = same binary. No hidden downloads, no JIT compilation, no version-dependent behavior.

---

## Supply Chain Analysis

### Rust Crate Dependencies

| Crate | Source | Audit Status |
|-------|--------|:------------:|
| `serde` 1.x | crates.io | Widely audited, >1B downloads |
| `serde_json` 1.x | crates.io | Widely audited |
| `wgpu` 24.x | crates.io | Mozilla-maintained, gfx-rs ecosystem |

All dependencies are fetched from crates.io with Cargo.lock pinning exact versions. `cargo audit` is run periodically.

### Python (Baseline Generation Only)

Python and NumPy are used only to generate baselines, never at runtime. The committed JSON baselines can be audited without running Python.

### GPU Drivers

WGSL shaders run via the system GPU driver (Vulkan, Metal, or DX12). The driver is the only closed-source component in the stack, and it is the same driver used by the OS for display — no additional vendor software is installed.

---

## Data Flow

```
Sequence (FASTA)                    coralForge (local)
      │                                  │
      ▼                                  ▼
  ┌──────┐    ┌──────────┐    ┌────────────────┐
  │ File │───>│ MSA      │───>│ Evoformer +     │──→ Predicted structure (PDB)
  │ read │    │ search   │    │ Structure Module│      │
  └──────┘    │ (local   │    │ (local GPU/CPU) │      ▼
              │ database)│    └────────────────┘   ┌──────────┐
              └──────────┘                         │ Analysis │
                                                   │ (local)  │
                                                   └──────────┘

Network boundary: ───── (none) ─────
```

At no point does data cross a network boundary. The MSA database is a local copy of UniRef/BFD. The GPU shader runs on the local GPU. The output stays on local disk.

---

## Air-Gapped Operation

coralForge can run on a fully air-gapped machine:

1. **Build offline**: `cargo vendor` creates a local copy of all crate dependencies. Build with `--offline`.
2. **MSA database**: Download UniRef90/BFD once, copy to air-gapped machine via physical media.
3. **Model weights**: Copy AF2 weights once (3.5 GB), store locally.
4. **GPU drivers**: Install from vendor media; no runtime updates needed.

The only network-dependent step is the initial setup (downloading dependencies, databases, and weights). After that, the system operates indefinitely offline.

---

## Comparison with Alternatives

| Property | coralForge | AlphaFold Server | ColabFold (Colab) | ESMFold API |
|----------|:----------:|:----------------:|:-----------------:|:-----------:|
| Data leaves your machine | **No** | Yes (Google) | Yes (Google) | Yes (Meta) |
| Requires internet | **No** | Yes | Yes | Yes |
| Open source | **Yes** (AGPL) | No (server) | Partial | Yes |
| Proprietary runtime | **None** | TPU, Google infra | CUDA, Google Colab | PyTorch, CUDA |
| Air-gap capable | **Yes** | No | No | No |
| GPU vendor lock-in | **None** (WGSL) | TPU only | NVIDIA only | NVIDIA only |
| Audit: can you read all code? | **Yes** | No | Partially | Yes |

---

## Responsible Use

coralForge is a scientific tool. Like any structure prediction system, it can be used for beneficial research (drug discovery, evolutionary biology, agriculture) or potentially misused (bioweapons design).

The AGPL-3.0-or-later license requires that derivative works be open-source, providing transparency for how the tool is being used and modified. This is a deliberate choice: sovereign computing means you own the tool, but the community can see what you build with it.

For biosecurity-sensitive applications, the air-gapped operation mode ensures that neither the input sequences nor the predicted structures are exposed to any external system.

---

*Security: the strongest protection is physical custody. coralForge keeps your data where you are.*
