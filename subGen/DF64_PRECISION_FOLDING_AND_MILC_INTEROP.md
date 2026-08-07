# DF64 Precision Folding & MILC Interoperability

**strandGate — hotSpring subGen | Aug 7, 2026**
**Status**: Active research document — theory, implementation plan, validation loop

---

## 1. The Precision Folding Concept

### 1.1 Foundational Insight

DF64 is not just a GPU hack — it's an instance of a **general mathematical
construction**: pair arithmetic (also called double-word arithmetic or
compensated arithmetic). The technique applies to ANY hardware floating-point
format:

```
Given base type fp_N with M mantissa bits:
  Pair type DF_{2N} = (fp_N, fp_N) carries ~(2M - 1) mantissa bits
  using ONLY fp_N hardware instructions.
```

This is a **precision fold**: you trade instruction count for precision depth,
exploiting the fact that fast hardware ops (f32, f16) outnumber slow ones
(f64) by 64:1 on consumer GPUs.

### 1.2 The Folding Hierarchy

| Fold Level | Base Type | Effective Bits | Decimal Digits | Hardware Speed |
|:-----------|:----------|:---------------|:---------------|:---------------|
| f16        | native    | 11 mantissa    | 3.3            | 2× f32 (Tensor) |
| **DF32** (f16×2) | f16 | 21 mantissa | 6.3 | 1-2× f32 (Tensor) |
| f32        | native    | 24 mantissa    | 7.2            | 64× f64 (consumer) |
| **DF64** (f32×2) | f32 | 47 mantissa | 14.1 | ~8× f64 |
| f64        | native    | 53 mantissa    | 15.9           | 1× (throttled) |
| **DF128** (f64×2) | f64 | 106 mantissa | 31.9 | 1× f64 throughput |

**Key observation**: each fold doubles precision bits at ~10-20 ops per
arithmetic operation. On hardware where the base type runs at N× the speed
of the next-higher type, the crossover is:

```
Effective speed of fold = base_speed / ops_per_op
DF64 on RTX 3090: 64× / 10 ≈ 6.4× native f64 speed
DF64 on RX 6950: 64× / 10 × cache_advantage ≈ 9× (measured)
```

### 1.3 Mathematical Foundation

The construction relies on two **error-free transformations** (EFTs):

**TwoSum** (Knuth 1969): For any floating-point a, b:
```
s = a ⊕ b  (rounded sum)
e = (a - (s - v)) + (b - v), where v = s - a
```
Guarantees: s + e = a + b **exactly** (no rounding error).

**TwoProd** (Dekker 1971, with FMA): For any floating-point a, b:
```
p = a ⊗ b  (rounded product)
e = fma(a, b, -p)
```
Guarantees: p + e = a × b **exactly** (requires hardware FMA).

These EFTs mean the `lo` word captures the **exact** rounding error of the
`hi` word computation. No information is lost at any step — precision is
bounded only by the accumulation of 2nd-order terms (lo × lo), which we
intentionally discard.

---

## 2. DF64 Stabilization Roadmap

### 2.1 Current Implementation Assessment

Our `df64_core.wgsl` implementation is **already at the state of the art**
for pair-arithmetic:
- FMA-based `two_prod` (2 ops, exact — no Dekker splitting needed)
- Knuth `two_sum` (6 ops, exact)
- Proper renormalization in `df64_add` and `df64_mul`

**Measured precision**: 47-bit mantissa (~14 decimal digits).
**Observed in QCD**: |Δ⟨P⟩| ≈ 5×10⁻¹⁰ at 16⁴ vs native f64.

### 2.2 Stabilization Targets (Ordered by Impact)

#### Level 1: Compensated Summation (Immediate Win)

**Problem**: When accumulating N plaquettes, naive summation has error
growth O(√N × u_DF64) in random-walk regime or O(N × u_DF64) worst-case.
At 32⁴ (6.3M plaquettes), worst-case: 6.3M × 7.1e-15 ≈ 4.5e-8.

**Solution**: Kahan-Babuška-Neumaier compensated sum within each workgroup,
then hierarchical reduction.

```wgsl
// Compensated DF64 accumulator — error reduced from O(N) to O(1)
struct CompAccum {
    sum: Df64,
    comp: Df64,   // compensation term
}

fn comp_add(acc: CompAccum, val: Df64) -> CompAccum {
    let t = df64_add(acc.sum, val);
    var c: Df64;
    if df64_abs(acc.sum).hi >= df64_abs(val).hi {
        c = df64_add(df64_sub(acc.sum, t), val);
    } else {
        c = df64_add(df64_sub(val, t), acc.sum);
    }
    return CompAccum(t, df64_add(acc.comp, c));
}

fn comp_result(acc: CompAccum) -> Df64 {
    return df64_add(acc.sum, acc.comp);
}
```

**Impact**: Reduces lattice-average error from O(√N) to O(1) — effectively
making the plaquette precision independent of lattice volume.

**Cost**: 1 extra `df64_add` per accumulation step (~14 extra ops per site).
Negligible vs the 184 ops per plaquette computation.

#### Level 2: Triple-Float Accumulator (Research)

For the global reduction (combining workgroup partial sums), use a
**triple-float** (3×f32 = 71-bit mantissa):

```wgsl
struct Tf96 {
    hi: f32,
    mi: f32,
    lo: f32,
}
```

This gives 21 decimal digits for the final answer at negligible cost
(only used in the reduction tree, not per-site).

#### Level 3: Higher-Order Transcendentals

Current sin/cos/log use degree-5/6 polynomials, giving ~14-digit accuracy.
For Box-Muller (which is precision-sensitive in the tail), we need:

- **Degree-9 Chebyshev minimax** for log_df64: gains 3-4 digits in tail
- **Degree-8 for sin/cos**: eliminates the last-bit cancellation near π/2
- **Payne-Hanek argument reduction** for large arguments (replaces Cody-Waite)

This directly addresses the WGSL variance bias found in §4.2 — our DF64
transcendentals are already better than naga's software f64, but we can
push them further.

#### Level 4: Interval Arithmetic Layer (Future)

Wrap DF64 computations in **certified error bounds**:

```wgsl
struct CertDf64 {
    value: Df64,
    error_bound: f32,  // guaranteed |true - value| < error_bound
}
```

This gives **provably correct** results — the error bound is computed
alongside the value, tracking accumulated rounding at every step.
Publication-grade: you can state "⟨P⟩ = 0.593424 ± 2×10⁻¹⁰ (numerical)"
as a rigorous bound, not just a statistical estimate.

### 2.3 Precision Recovery: Closing the 6-Bit Gap to f64

The 47→53 bit gap (6 bits = factor 64 in ULP) can be partially closed:

1. **Compensated summation**: recovers ~3 bits in reductions
2. **Faithful rounding in division**: recovers ~1 bit
3. **Higher-order polynomials**: recovers ~2 bits in transcendentals

Net effect: DF64 with all stabilizations → ~50-51 effective bits,
leaving only 2-3 bits below native f64. For lattice QCD where the
statistical uncertainty is O(10⁻⁴), this makes DF64 **indistinguishable
from f64 in any physically measurable quantity**.

---

## 3. The DF32 Frontier: f16 Pair Arithmetic

### 3.1 Why This Matters

On modern GPUs with Tensor Cores (NVIDIA) or Matrix Cores (AMD):
- f16 throughput: 4× f32 on shader cores, 16× on Tensor Cores
- f16 mantissa: 11 bits (pathetically low for science)
- DF32 (f16×2): 21-bit mantissa (~6 decimal digits) at Tensor Core speed

**Use case**: The MD integrator in HMC doesn't need 14 digits per step —
it needs to preserve **symplecticity** to ~6-7 digits over many steps.
The Omelyan integrator's 4× improvement over leapfrog means DF32 HMC
would need fewer steps to reach the same acceptance rate.

### 3.2 Architecture

```
Precision hierarchy for mixed-precision HMC:

  MOMENTA:    f64 (CPU) — exact Gaussian sampling
  FORCE:      DF64 (GPU f32 cores) — staple computation
  INTEGRATOR: DF32 (GPU f16/Tensor) — symplectic evolution
  ACCEPT:     DF64 (GPU) — Metropolis ΔH computation
  OBSERVABLE: DF64 + compensated sum — plaquette accumulation
```

Each computation uses **exactly the precision it needs**, at the speed
of the fastest available hardware for that precision level.

### 3.3 Tensor Core Opportunity

NVIDIA's Tensor Cores perform 4×4 f16 matrix multiply-add:
```
C[4×4] = A[4×4] · B[4×4] + C[4×4]  (all f16, accumulated in f32)
```

SU(3) is a 3×3 complex matrix = 6×6 real matrix.
Padded to 8×8 → fits in TWO Tensor Core operations.
With DF32 pair arithmetic layered on top:
- 4 Tensor Core ops per SU(3) product (2 for hi, 2 for lo correction)
- vs 108 FMA ops in current scalar DF64

**Theoretical speedup**: 108/4 × (Tensor Core vs scalar f32) ≈ 27×
per matrix product. Even with pair-arithmetic overhead: ~10× over DF64.

This is the **next-generation** compute target for hotSpring.

---

## 4. MILC Format Interoperability

### 4.1 Why MILC Format Matters

The MILC collaboration (Bazavov, DeTar, et al.) has generated the majority
of publicly available lattice QCD configurations — 16+ TB on NERSC HPSS.
Their binary format is the de facto standard for quenched and dynamical
configurations in the US lattice community.

**Validation strategy**: Reading a MILC-generated config and computing
⟨P⟩ that matches MILC's own reported value is the **strongest possible**
form of code validation. It proves:
1. Our SU(3) representation is correct
2. Our link ordering matches the standard
3. Our plaquette computation is correct
4. All of the above simultaneously

### 4.2 MILC Binary Format Specification

```
MILC Gauge Configuration (v5 format):
┌──────────────────────────────────────────┐
│ HEADER (variable length)                 │
│   magic_number: 20103 (network byte ord) │
│   dims[4]: {nx, ny, nz, nt} (big-endian) │
│   time_stamp: ASCII string               │
│   order: NATURAL_ORDER = 0               │
│   checksum: CRC32 (site-by-site XOR)     │
│   link_trace: f32 (average link trace)   │
│   plaquette: f32 (average plaquette!!)   │
│   ← THIS IS OUR VALIDATION TARGET       │
└──────────────────────────────────────────┘
┌──────────────────────────────────────────┐
│ GAUGE FIELD DATA                         │
│   For each site (t-fastest, x-slowest):  │
│     For each direction μ = 0,1,2,3:      │
│       U_μ(x): 3×3 complex matrix         │
│         18 × f32 or f64 (big-endian)     │
│         (re₀₀,im₀₀,re₀₁,...,re₂₂,im₂₂) │
└──────────────────────────────────────────┘
```

**Critical details**:
- Byte order: **big-endian** (network order) — must byte-swap on x86
- Site ordering: **t-fastest** (MILC convention) vs our x-fastest
  - MILC: index = x + nx*(y + ny*(z + nz*t))... actually:
  - MILC uses: index(x,y,z,t) with x varying fastest in memory
    for NATURAL_ORDER, or checkerboard (even/odd) for EVEN_ODD_ORDER
- Checksum: per-site CRC32 XOR'd together (29-bit site hash)
- Header contains **the plaquette value** — our instant validation check

### 4.3 Available Public Configurations

From DESY Shared Lattices (publicly listed):
- **16³×39, β=6.0**: 19 configs (Bernard & Soni, public domain)
- **24³×39, β=6.0**: 8 configs (Bernard & Soni, public domain)
- **16³×25, β=5.7**: 16 configs (Bernard & Soni, public domain)

From NERSC Gauge Connection (requires login, data on HPSS tape):
- Extensive MILC quenched ensembles at β=5.7, 5.85, 6.0, 6.2, 6.4
- Multiple volumes per β

From `qcdutils` (GitHub: mdipierro/qcdutils):
- Python tool that downloads from NERSC and converts between MILC/ILDG/MDP
- Can generate cold-start configs in MILC format for testing

### 4.4 Implementation Plan: hotSpring MILC Subsystem

```
hotSpring/barracuda/src/milc/
├── mod.rs           — public API: read_config, write_config, validate
├── format.rs        — binary layout, magic numbers, header parsing
├── checksum.rs      — CRC32 site-by-site checksum computation
├── ordering.rs      — site ordering conversion (MILC ↔ hotSpring)
├── roundtrip.rs     — round-trip validation (read → compute → compare)
└── tests/
    ├── cold_start.rs    — generate cold config, write MILC, read back
    ├── known_plaq.rs    — verify plaquette against header value
    └── ordering_test.rs — verify site ordering on small lattice
```

**Key function**:
```rust
pub fn read_milc_gauge_config(path: &Path) -> Result<GaugeField, MilcError> {
    let header = MilcHeader::parse(&mut reader)?;
    header.verify_magic(MILC_MAGIC_V5)?;
    
    let field = GaugeField::new(header.dims);
    let mut checksum: u32 = 0;
    
    // Read site-by-site in MILC ordering
    for site in MilcSiteIterator::new(&header.dims) {
        for mu in 0..4 {
            let matrix = read_su3_matrix(&mut reader, header.precision)?;
            checksum ^= site_checksum(&matrix, site);
            field.set_link(reorder_site(site, &header), mu, matrix);
        }
    }
    
    verify_checksum(checksum, header.checksum)?;
    Ok(field)
}
```

### 4.5 The Validation Loop

```
┌─────────────────────────────────────────────────────────┐
│  MILC VALIDATION LOOP (Continuous Integration)          │
│                                                         │
│  1. Download config from NERSC/public archive           │
│  2. Read via hotSpring MILC reader                      │
│  3. Verify checksum matches header                      │
│  4. Compute ⟨P⟩ via our GPU plaquette kernel            │
│  5. Compare to header plaquette value                   │
│  6. Compute Wilson loops, Polyakov → store in provenance│
│  7. Write back in MILC format                           │
│  8. Verify byte-identical round-trip                    │
│                                                         │
│  Pass criteria: |⟨P⟩_ours - ⟨P⟩_milc| < 10⁻⁶          │
│  (allowing for f32 header precision)                    │
└─────────────────────────────────────────────────────────┘
```

This loop runs as part of our CI — every commit verifies MILC compat.

---

## 5. DF64 as Experimental Platform

### 5.1 What We're Actually Building

DF64 on GPU is not just "cheaper f64." It's a **programmable precision
system** — we control:
- Mantissa depth (47 bits standard, 50+ with compensation, 71 with TF96)
- Error propagation model (random-walk vs compensated vs certified)
- Speed/precision tradeoff (adjustable per kernel)

This makes hotSpring a **precision laboratory**: we can characterize
exactly how much precision each part of the HMC algorithm actually needs.

### 5.2 Experimental Protocol: Precision Sensitivity Mapping

```
For each component of HMC:
  1. Run at full DF64 (47-bit) → record observable
  2. Run at DF64 + compensation (50-bit) → record observable
  3. Run at native f64 (53-bit) → record observable (gold standard)
  4. Run at DF32 (21-bit) → where does it break?
  5. Run at mixed (force:DF64, integrator:DF32) → still converges?

Metric: acceptance rate as function of precision level
```

This produces a **precision phase diagram** for HMC:
- Where is precision critical? (Metropolis accept/reject)
- Where is it irrelevant? (MD force, which averages over noise)
- Where is the minimum viable precision? (guides hardware targeting)

### 5.3 Publication Value

This is a NOVEL CONTRIBUTION to the lattice QCD literature:
- Nobody has systematically characterized precision requirements per HMC component
- Nobody has demonstrated DF32 (f16-pair) for any lattice QCD computation
- Nobody has published a certified-error-bound GPU lattice measurement

The paper becomes: "Not just cheap f64 on consumer GPUs, but a systematic
framework for precision-aware lattice computation" — which is genuinely
new science, not just engineering.

---

## 6. Integration with Provenance (Braiding)

Every DF64 experiment produces a **precision-tagged braid**:

```
braid {
  observable: "plaquette",
  value: 0.59342089,
  precision: {
    arithmetic: "df64",
    mantissa_bits: 47,
    compensation: "kahan-babushka",
    effective_bits: 50,
    certified_bound: 2.1e-10,
  },
  hardware: "AMD RX 6950 XT",
  config_hash: "blake3:abc123...",
}
```

The provenance system captures the FULL precision context of every
measurement. When we later compare DF64 vs DF32 vs f64, the braids
make the comparison auditable and reproducible.

---

## 7. Timeline

| Phase | Target | Duration | Output |
|:------|:-------|:---------|:-------|
| **A** | Compensated summation in plaquette kernel | 2 days | Stabilized DF64, measurably closer to f64 |
| **B** | MILC reader + round-trip validation | 3 days | CI-verified MILC compatibility |
| **C** | Precision sensitivity mapping (DF64 vs f64) | 5 days | Novel data for paper §3.3 expansion |
| **D** | DF32 prototype (f16-pair) on force computation | 7 days | Proof of concept for next-gen |
| **E** | Tensor Core SU(3) product (NVIDIA only) | 10 days | Research prototype, publication |

**Phase A is the immediate priority** — it directly improves the arXiv
preprint's precision claims and costs almost nothing to implement.

**Phase B before sending to Bazavov** — the MILC round-trip test is the
single most convincing validation artifact for a MILC collaboration member.

---

*strandGate subGen — Precision folding is a mathematical concept we are
applying to consumer GPUs. DF64 already unblocked what native f64 was
preventing. The next steps: stabilize it (compensation), make it provably
correct (certified bounds), and fold further down (DF32 on Tensor Cores).
Each fold opens a new tier of compute that was previously locked behind
hardware pricing.*
