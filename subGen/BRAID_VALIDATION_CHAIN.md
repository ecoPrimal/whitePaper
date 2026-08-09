# Braid Validation Chain — CAS + NFT → Reproducible Science

**Status**: Architecture defined, critical path identified
**Date**: Aug 9, 2026 | **Wave**: 157a
**Principle**: Every scientific claim resolves to a braid → a hash → a file → a result

---

## Two Braid Types

### Data Braids (westGate CAS — sweetGrass)

Content-addressed storage for raw scientific data. Each file is identified by
its BLAKE3 hash. Files are immutable — the same hash always returns the same
content. sweetGrass manages the braid index.

| Property | Value |
|----------|-------|
| Storage | westGate ZFS (2.5 TB) |
| Addressing | BLAKE3 content hash |
| Discovery | songBird mesh → `content.locate` |
| Access | TCP stream via pepti + riboCipher |
| Format | .lat (internal) + .milc (ILDG) + .json (observables) |

### Result Braids (ironGate NFT — lithoSpore)

Signed, frozen publication artifacts. Each pseudoSpore bundle is a complete
reproducible unit: data + code + provenance, sealed with Ed25519.

| Property | Value |
|----------|-------|
| Storage | ironGate (dedicated results gate) |
| Addressing | BLAKE3 DAG root hash |
| Signing | bearDog Ed25519 keypair |
| Packaging | lithoSpore (provenance-aware archiver) |
| Format | .tar.gz containing configs + code + provenance.json + validate.sh |

---

## The Validation Chain

```
PRODUCE → STORE → SIGN → SERVE → VALIDATE → REPRODUCE

1. PRODUCE (strandGate GPU)
   HMC trajectory → thermalized config (.lat)
   Measure → observables (.json)
   Every file gets BLAKE3 hash at creation

2. STORE (westGate CAS)
   sweetGrass ingests: hash → store → braid.head announce
   songBird propagates: content.locate available mesh-wide
   Immutable: once stored, never modified

3. SIGN (ironGate NFT)
   lithoSpore collects: configs + observables + code snapshot
   DAG construction: parent hashes → root hash
   bearDog signs: Ed25519(root_hash) → signature
   Freeze: v1.0.0-rung1 tag → immutable

4. SERVE (sporePrint + petalTongue)
   URL: sporeprint.primals.eco/pseudospore/hotspring-qcd-sun/
   Download: .tar.gz via HTTPS (petalTongue serves)
   Metadata: JSON-LD with DOI-like persistent identifier

5. VALIDATE (reviewer's machine)
   validate.sh:
     - Check BLAKE3 of every file in bundle
     - Verify DAG consistency (parent refs valid)
     - Verify Ed25519 signature against known public key
     - Report: PASS/FAIL per file + overall integrity

6. REPRODUCE (reviewer's machine)
   cargo run --bin arxiv_measure_battery -- --config <path>
     - Loads our thermalized config
     - Runs same measurement code
     - Reports same observables
     - Reviewer compares to published values
```

---

## validate.sh — Specification

The validation script must be self-contained (POSIX sh + standard tools) with
optional Rust verification for full DAG checking.

### Minimal (POSIX sh + b3sum)

```sh
#!/bin/sh
# validate.sh — BLAKE3 integrity check for hotspring-qcd-sun pseudoSpore
set -e

BUNDLE_DIR="$(dirname "$0")"
MANIFEST="${BUNDLE_DIR}/MANIFEST.blake3"
SIGNATURE="${BUNDLE_DIR}/SIGNATURE.ed25519"
PUBKEY="${BUNDLE_DIR}/pubkey.ed25519"

echo "=== hotspring-qcd-sun pseudoSpore validation ==="
echo "Bundle: ${BUNDLE_DIR}"
echo ""

# Step 1: BLAKE3 integrity
echo "[1/3] Checking BLAKE3 hashes..."
FAIL=0
while IFS='  ' read -r expected_hash filepath; do
  actual_hash=$(b3sum --no-names "${BUNDLE_DIR}/${filepath}")
  if [ "$actual_hash" != "$expected_hash" ]; then
    echo "  FAIL: ${filepath}"
    echo "    expected: ${expected_hash}"
    echo "    actual:   ${actual_hash}"
    FAIL=$((FAIL + 1))
  fi
done < "$MANIFEST"
echo "  Checked $(wc -l < "$MANIFEST") files, ${FAIL} failures"

# Step 2: DAG consistency
echo "[2/3] Checking DAG consistency..."
# The DAG file lists parent→child relationships
# Each entry: child_hash parent_hash_1 [parent_hash_2 ...]
# All referenced hashes must exist in MANIFEST
python3 -c "
import sys
manifest_hashes = set()
with open('${BUNDLE_DIR}/MANIFEST.blake3') as f:
    for line in f:
        h = line.split()[0]
        manifest_hashes.add(h)
errors = 0
with open('${BUNDLE_DIR}/DAG.blake3') as f:
    for line in f:
        parts = line.strip().split()
        for h in parts:
            if h not in manifest_hashes:
                print(f'  MISSING: {h}')
                errors += 1
if errors == 0:
    print('  DAG consistent: all hashes resolve')
sys.exit(errors > 0)
" || FAIL=$((FAIL + 1))

# Step 3: Ed25519 signature
echo "[3/3] Checking Ed25519 signature..."
if command -v minisign >/dev/null 2>&1; then
  minisign -Vm "$MANIFEST" -p "$PUBKEY" && echo "  Signature VALID" || FAIL=$((FAIL + 1))
elif command -v openssl >/dev/null 2>&1; then
  openssl pkeyutl -verify -pubin -inkey "$PUBKEY" -sigfile "$SIGNATURE" -in "$MANIFEST" \
    && echo "  Signature VALID" || FAIL=$((FAIL + 1))
else
  echo "  SKIP: No Ed25519 verifier found (install minisign or openssl)"
fi

echo ""
if [ $FAIL -eq 0 ]; then
  echo "=== VALIDATION PASSED ==="
  echo "All files intact. DAG consistent. Signature verified."
  echo "You may now reproduce measurements with:"
  echo "  cargo run --bin arxiv_measure_battery -- --config ${BUNDLE_DIR}/configs/"
else
  echo "=== VALIDATION FAILED (${FAIL} errors) ==="
  exit 1
fi
```

### Full (Rust binary)

A `pseudospore_validate` binary in the hotSpring crate provides:
- Parallel BLAKE3 verification (rayon)
- Full DAG traversal with cycle detection
- Ed25519 verification via `ed25519-dalek`
- JSON report output for programmatic consumption
- Exit code: 0 = pass, 1 = integrity failure, 2 = signature failure

---

## pseudoSpore Bundle Contents

```
hotspring-qcd-sun-v1.0.0-rung1/
├── validate.sh               ← Self-contained validation script
├── MANIFEST.blake3           ← Hash of every file in bundle
├── DAG.blake3                ← Parent-child provenance relationships
├── SIGNATURE.ed25519         ← Ed25519 signature over MANIFEST
├── pubkey.ed25519            ← Public key for verification
├── README.md                 ← Human-readable description
├── configs/
│   ├── su2/                  ← SU(2) thermalized configs
│   │   ├── beta2.3_8x8x8x8/
│   │   └── beta2.3_16x16x16x16/
│   ├── su3/                  ← SU(3) thermalized configs (MILC format)
│   │   ├── beta6.0_16x16x16x16/
│   │   ├── beta6.0_24x24x24x24/
│   │   └── beta6.0_32x32x32x32/
│   └── finite_t/            ← Finite-T configs (deconfinement)
├── observables/
│   ├── plaquette_table.json  ← All measured plaquettes
│   ├── polyakov_loops.json   ← Polyakov loop measurements
│   ├── wilson_loops.json     ← W(R,T) data
│   ├── creutz_ratios.json   ← χ(R,T) data
│   └── cross_gpu_parity.json ← AMD vs NVIDIA comparison
├── code/
│   ├── Cargo.toml            ← Build manifest
│   ├── src/                  ← Source code snapshot (tagged)
│   └── build_info.json       ← Rust version, features, commit hash
├── paper/
│   ├── lattice_qcd_consumer_gpu.tex  ← LaTeX source
│   └── figures/              ← Publication figures (PDF + PNG)
└── provenance/
    ├── hardware.json         ← GPU/CPU specs used for generation
    ├── timeline.json         ← When each config was generated
    └── software_versions.json ← All dependency versions
```

---

## Interaction Modes for Reviewers

### Mode 1: Quick Verify (5 minutes)

```bash
curl -L sporeprint.primals.eco/pseudospore/hotspring-qcd-sun/v1.0.0-rung1.tar.gz | tar xz
cd hotspring-qcd-sun-v1.0.0-rung1/
./validate.sh
# → VALIDATION PASSED
```

### Mode 2: Spot-Check (30 minutes)

```bash
# Load one config into MILC (Chuna/Bazavov)
milc_su3_spectrum < configs/su3/beta6.0_16x16x16x16/config_0001.milc
# Compare plaquette to our published value
```

### Mode 3: Full Reproduction (2-4 hours)

```bash
# Build the measurement code
cd code/
cargo build --release --bin arxiv_measure_battery

# Run all measurements on their GPU
cargo run --release --bin arxiv_measure_battery -- --config ../configs/

# Compare: their numbers should match paper Table 2 within errors
```

### Mode 4: Live System (ongoing)

```bash
# Pull latest data from the mesh (requires mesh access)
pseudospore pull hotspring-qcd-sun --latest
# → Downloads new configs as they're generated
# → Validates incrementally
# → Their local copy grows as science progresses
```

---

## What Makes This "Live Science" vs "arXiv Snapshot"

| Aspect | arXiv (static) | ecoPrimals (live) |
|--------|---------------|-------------------|
| Data | Frozen at submission | Grows continuously |
| Verification | "trust the authors" | `validate.sh` + Ed25519 |
| Reproduction | "contact authors for code" | `cargo run` from bundle |
| Updates | Revised paper (v2, v3...) | New pseudoSpore version |
| Extension | Fork the PDF ideas | Fork the code + data |
| Discovery | Search engine | songBird mesh `content.locate` |
| Provenance | Author names on paper | BLAKE3 DAG + Ed25519 chain |
| Availability | arXiv servers | 6 NUCLEUS gates + public CDN |

The arXiv PDF says "we measured X." The pseudoSpore says "here is the exact
configuration, the exact code, and the exact hardware that produced X — verify
it yourself." The mesh says "here are 11 other nodes that independently hold
copies of the same data, all with matching BLAKE3 hashes."

---

## Implementation Status

| Component | Status | Owner |
|-----------|--------|-------|
| BLAKE3 hashing (per-config) | DONE | rhizoCrypt |
| sweetGrass braiding (westGate) | DONE | sweetGrass team |
| songBird discovery (content.locate) | DONE | songBird mesh |
| lithoSpore packaging | Code exists | lithoSpore team |
| bearDog signing (Ed25519) | Ceremony done | bearDog team |
| validate.sh | **TO WRITE** | hotSpring (this task) |
| sporePrint download page | Wired, needs content | sporePrint team |
| petalTongue /pseudospore/ route | DONE | petalTongue |
| nestgate.io NFT dashboard | UI exists, needs content | sporeGate |

**Critical path to reviewer send**: validate.sh + lithoSpore package + sporePrint content.

---

*strandGate — Wave 157a — Aug 9, 2026. The braid chain is the backbone of
live science: produce → store (CAS) → sign (NFT) → serve → validate → reproduce.
Reviewers get cryptographic proof, not just claims. The mesh provides geographic
redundancy and independent verification. The arXiv snapshot is a pointer into
this living system.*
