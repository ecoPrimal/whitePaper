# Evolution Strategy — Reaching Higher Rungs via Targeted Optimization

**Status**: Active roadmap | **Wave**: 157a | **Date**: Aug 9, 2026
**Gate**: strandGate (primary), biomeGate (coralReef), mesh-wide (distributed)
**Principle**: Every performance gap is an engineering target, not an irreconcilable limit.

---

## Thesis

The lattice QCD community's existing codes (QUDA, Grid, openQCD, MILC, SIMULATeQCD)
represent decades of CUDA/MPI optimization on homogeneous HPC clusters. Our
approach — vendor-agnostic WGSL on consumer hardware — starts at a throughput
disadvantage but holds structural advantages that compound at scale. The path to
higher rungs is not "catch QUDA" but "solve the same physics faster through
architectural innovation, distributed idle compute, and silicon diversity."

Every gap between barracuda and QUDA is an engineering problem with a known
solution path. None are fundamental physics limitations.

---

## The Competitive Landscape — Who Has What

### NVIDIA Ecosystem (CUDA)

| Code | Language | Target | Key Optimizations | Weakness |
|------|----------|--------|-------------------|----------|
| **QUDA** | CUDA C++ | NVIDIA only | Multigrid, mixed precision, tensor cores, shared mem, NVLink, multi-GPU MPI | Vendor-locked, requires HPC allocation |
| **Grid** | C++ (CUDA/HIP/SYCL) | Multi-vendor (partial) | Lattice-wide SIMD, expression templates, Grid-parallelism | Complex build, partial vendor support |
| **openQCD** | C (MPI+OpenMP) | CPU + NVIDIA | Martin Luscher's reference implementation, deflated solvers | CPU-primary, GPU port secondary |

### AMD Ecosystem (ROCm/HIP)

| Code | Language | Target | Key Optimizations | Status |
|------|----------|--------|-------------------|--------|
| **QUDA (HIP port)** | HIP C++ | AMD MI-series | hipify'd from CUDA, same algorithms | Works but second-class — tuned for NVIDIA |
| **Grid (HIP)** | C++ | AMD Instinct | SYCL backend exists, HIP path experimental | Functional, not optimized |
| **SIMULATeQCD** | C++ (HIP/CUDA) | Both (Bielefeld) | Multi-GPU, staggered HISQ, modern C++20 | Small team, less adoption |
| **AMD native lattice?** | None | — | — | AMD has no dedicated lattice QCD software investment |

### Intel Ecosystem (SYCL/oneAPI)

| Code | Language | Target | Status |
|------|----------|--------|--------|
| **Grid (SYCL)** | C++ | Intel GPUs (Ponte Vecchio, Flex) | Experimental, Aurora supercomputer target |
| **Dedicated Intel lattice** | None | — | No existing code |

### Our Position (barracuda/WGSL)

| Code | Language | Target | Key Advantages |
|------|----------|--------|----------------|
| **barracuda** | Rust + WGSL | Any Vulkan GPU (NVIDIA, AMD, Intel, mobile) | Zero vendor lock, DF64 innovation, silicon offloading, cryptographic provenance, runs on $200 gaming cards |

**Key observation**: There is NO production-quality lattice QCD code that is truly
vendor-agnostic at the shader level. Grid/SYCL is closest but requires explicit
backend selection at compile time. barracuda is the only implementation where
the *same compiled shader* runs on AMD and NVIDIA producing identical physics.

---

## Performance Gap Analysis — What QUDA Gets vs What We Get

### Current Measured Gaps

| Operation | QUDA on A100 | barracuda on RTX 3090 | Gap | Root Cause |
|-----------|-------------|----------------------|-----|-----------|
| HMC trajectory (32⁴ SU(3)) | ~0.8 s | ~9.8 s | 12× | Shared mem + tuned kernels |
| CG solve (32⁴, m=0.01) | ~50 ms | ~500 ms (est.) | 10× | Multigrid + deflation |
| Force computation | ~200 ms | ~2.5 s | 12× | Register tiling + shared mem |
| Memory throughput | 2039 GB/s (HBM2e) | 936 GB/s (GDDR6X) | 2× | Hardware (not software) |
| Global reduction | ~5 µs | ~50 µs | 10× | Warp shuffle + atomics |
| Multi-GPU scaling | Near-linear to 1000+ | 2 GPUs (PCIe) | 500× | MPI + NVLink vs PCIe pairs |

### What Closes Each Gap

| Gap | Engineering Solution | Difficulty | Timeline | Who |
|-----|---------------------|------------|----------|-----|
| Shared memory (12×) | WGSL workgroup memory + explicit tiling | Medium | Rung 3 | barracuda team |
| Multigrid (10×) | TMU-accelerated prolongation + algebraic multigrid | Hard | Rung 3-4 | hotSpring team |
| Register tiling | Larger workgroups + manual register pressure control | Medium | Rung 2-3 | barracuda team |
| HBM2 bandwidth (2×) | biomeGate Titan V/MI50 for BW-bound kernels | Done (hardware) | Now | Already owned |
| NVLink multi-GPU | PCIe Gen4 streaming (28 GB/s) + domain decomp | Hard | Rung 4-5 | toadStool team |
| Warp shuffle (10×) | Subgroup operations already partially used | Easy | Rung 2 | barracuda team |
| Tensor cores | coralReef SASS dispatch → HMMA instructions | Hard | Rung 4+ | coralReef (biomeGate) |

**None of these are physics limitations. All are engineering targets.**

---

## The coralReef Factor — Sovereign NVIDIA Dispatch

The coralReef team on biomeGate is building a sovereign NVIDIA shader dispatch
path: direct PTX/SASS emission without CUDA runtime dependency.

What this unlocks:
- **Tensor core access** via HMMA instructions (bypassing CUDA entirely)
- **Shared memory control** at the SASS level (not dependent on WGSL spec additions)
- **Register allocation** tuned for lattice stencil patterns
- **Cooperative groups** for cross-workgroup synchronization

This means the "QUDA advantages" (shared memory, tensor cores, register tiling)
become available to us *without CUDA*. coralReef's sovereign dispatch path means
we can emit the same PTX that QUDA emits, but from Rust, on our hardware, with
our provenance chain.

| coralReef Phase | What It Unlocks | Est. Speedup |
|-----------------|----------------|--------------|
| Phase 1: PTX emission (working) | Direct kernel launch, no wgpu overhead | 1.5-2× |
| Phase 2: Shared memory tiling | Stencil locality, reduced global memory traffic | 3-5× |
| Phase 3: Tensor core (HMMA) | SU(3) 3×3 matmul at 312 TFLOPS (A100) | 5-10× for matmul-bound |
| Phase 4: Register tiling | Optimal occupancy for lattice patterns | 1.5-2× |
| Combined | | 10-30× over current WGSL path |

With coralReef Phase 2-3, barracuda on the RTX 3090 could approach QUDA
throughput on the same hardware — while maintaining the vendor-agnostic WGSL
path as the portable fallback.

---

## Cross-System Comparison Strategy

We should benchmark against every available system:

### What We Can Compare Today

| System | Available? | How to Compare |
|--------|-----------|----------------|
| MILC (staggered, C/MPI) | Yes — Chuna has binaries | Same configs, same physics, wall-clock comparison |
| openQCD (Wilson, C) | Public source | Build on strandGate, run identical parameters |
| SIMULATeQCD (HIP/CUDA) | Public source | Build on strandGate (HIP → AMD), compare |
| Grid (C++/SIMD) | Public source | Complex build but possible on multi-arch |
| QUDA | Public but NVIDIA-only | Run on RTX 3090 via CUDA, compare same physics |

### Cross-Learning Targets

| From Code | Technique to Absorb | Implementation Path |
|-----------|-------------------|---------------------|
| QUDA | Adaptive multigrid for Wilson/clover | Port algorithm to WGSL compute |
| QUDA | Mixed-precision solver (FP16 outer + FP64 inner) | DF64 outer + f16 inner (our precision ladder) |
| QUDA | Domain decomposition (Schwarz preconditioner) | Multi-GPU via PCIe streaming |
| Grid | Expression templates for lattice-wide SIMD | Rust generics + WGSL codegen |
| Grid | Lattice parallelism abstraction | Already have this (GaugeGroup trait) |
| openQCD | Deflated SAP (domain decomposition) | SAP blocks map to workgroups naturally |
| openQCD | Twisted mass reweighting | Algorithm-level, silicon-independent |
| SIMULATeQCD | HaloExchange pattern | Adapt for PCIe (smaller halos than NVLink) |
| SIMULATeQCD | HISQ smearing on GPU | Port smearing kernels to WGSL |
| MILC | Rational function approximation tables | Already have (RHMC implemented) |
| MILC | HISQ action coefficients | Constants, trivial to port |

### What We Teach Them

| Our Innovation | What It Means for the Field |
|----------------|---------------------------|
| DF64 on FP32 hardware | 100× more hardware can do lattice QCD |
| Silicon offloading (ROP/TMU) | 23-27% free performance from unused silicon |
| Vendor-agnostic shaders | Reproducibility across hardware (science benefit) |
| Precision folding (f16 storage) | 4× VRAM reduction — larger volumes on same card |
| Cryptographic provenance per config | Reproducibility crisis prevention |
| Consumer GPU production | $2,250 vs $100K+ HPC allocation |
| Distributed idle compute | Queue time = 0 (always available) |
| Multi-vendor cross-check | Independent silicon validates physics |

---

## Distributed Compute — The "Idle Gaming Mesh" Advantage

### Queue Time vs Wall Clock: The Real Comparison

| Metric | HPC (NERSC/OLCF) | Our mesh (13 GPUs) |
|--------|-------------------|-------------------|
| Proposal writing | 3-6 months | 0 (our hardware) |
| Queue wait (typical) | 2-14 days | 0 |
| Allocation limits | 50K-500K GPU-hours/year | Unlimited (power bill only) |
| Available hours/day | ~4-8 hr (batch scheduler) | 24 hr (overnight idle) |
| Cost per GPU-hour | $3-5 (commercial cloud) | ~$0.15 (electricity) |
| Hardware refresh | When DOE buys new cluster | When eBay has good deals |
| Reproducibility | "Trust us" | Cryptographic proof |

### Effective Throughput at 32⁴ SU(3)

Assuming overnight runs (10 PM → 8 AM = 10 hours/day, weekdays; 24hr weekends):

| Configuration | Cards active | Traj/night (weekday) | Traj/weekend | Weekly total |
|---------------|-------------|---------------------|--------------|--------------|
| strandGate only (RX 6950 XT) | 1 | ~3,600 | ~17,280 | ~52,560 |
| + RTX 3090 | 2 | ~7,200 | ~34,560 | ~105,120 |
| + northGate RTX 5090 | 3 | ~12,000 | ~57,600 | ~175,200 |
| + swiftGate/kinGate/flockGate (16⁴) | 6 | + independent chains | + chains | + chains |
| Full mesh (all idle GPUs) | 10+ | Massive parallel | | 500K+/week |

At 500 trajectories for a production ensemble, a full mesh run generates
**1,000+ independent ensembles per week** at 32⁴. That's more than most HPC
allocations produce in a quarter.

### The Deep/Wide Strategy

| When | What Runs | Where |
|------|-----------|-------|
| Workday (gaming hours) | Nothing (or small 8⁴ validation) | — |
| Evenings (idle) | 32⁴ production on strandGate + northGate | 2 cards |
| Overnight (sleep) | Full mesh: 32⁴ + 48⁴ attempts + 16⁴ on small cards | All gates |
| Weekends (if not gaming) | 48⁴ long runs, finite-T temperature scans | Priority gates |

We run **wide** (many independent Markov chains simultaneously) rather than
**fast** (one chain as quickly as possible). Wide running:
- Produces better statistics (uncorrelated chains)
- Uses all available silicon (no card sits idle)
- Doesn't care about single-card throughput (parallelism compensates)
- Is what experimentalists actually need (ensembles, not single configs)

---

## Evolution Targets — Closing the QUDA Gap

### Phase 1: Already Done (Rung 1-2 publication)

| Achievement | Speedup vs naive | Status |
|-------------|-----------------|--------|
| DF64 on FP32 | Enabled GPU HMC (was CPU-only) | DONE |
| ROP force accumulation | -15% trajectory time | DONE (measured) |
| Subgroup reductions | -9% trajectory time | DONE (measured) |
| PCIe GPU-to-GPU streaming | 2× volume capacity | DONE (validated) |
| Precision folding (f16 storage) | 2.4× VRAM capacity | DONE (profiled) |
| Multi-vendor execution | Independent cross-check | DONE (AMD+NVIDIA) |

### Phase 2: Near-Term (Rung 3, within reach)

| Target | Expected Speedup | Implementation |
|--------|-----------------|----------------|
| WGSL workgroup memory for stencil | 2-3× force computation | Explicit tile loading, workgroup barriers |
| TMU multigrid prolongation | 5-10× solver (fermions) | Texture sampling for coarse→fine transfer |
| Adaptive step-size (NPU-guided) | 1.3× acceptance rate | ESN predicts optimal dt per config |
| Larger workgroups (256→1024) | 1.5× occupancy | Better ALU utilization at large volumes |
| Async compute (force + measurement overlap) | 1.2× pipeline | Non-blocking measurement during next force |

**Combined Phase 2**: ~5-10× speedup on fermion-dominated workloads.

### Phase 3: Medium-Term (Rung 4-5, coralReef dependency)

| Target | Expected Speedup | Implementation |
|--------|-----------------|----------------|
| coralReef PTX dispatch (NVIDIA) | 1.5-2× kernel launch overhead | Direct PTX emission, no wgpu |
| coralReef shared memory | 3-5× stencil locality | SASS-level smem control |
| coralReef tensor cores (HMMA) | 5-10× for SU(3) matmul | 3×3 complex matrix multiply via TC |
| Multi-GPU domain decomposition | Linear scaling to 4+ GPUs | PCIe halo exchange pattern |
| Deflated solver (low-mode projection) | 10-50× for light quarks | Lanczos eigenvectors + deflation |

**Combined Phase 3**: ~30-100× over current for fermion physics. This puts
barracuda on RTX 3090 within 2-3× of QUDA on A100 for the same physics.

### Phase 4: Long-Term (Rung 5+, mesh-scale)

| Target | Expected Impact | Implementation |
|--------|----------------|----------------|
| swarmVine compute gossip | Automatic work distribution | Idle GPU discovers → claims work |
| Cross-gate halo exchange (10G backbone) | Multi-node lattice splitting | songBird mesh + swarmVine routing |
| HBM2 precision oracle integration | Automated validation pipeline | V100/MI50 run f64, compare to DF64 |
| coralReef AMD GCN dispatch | Direct ISA on MI50 | Sovereign AMD path (mirrors NVIDIA) |
| Federated thermalization (pseudoSpore sharing) | Gates share configs directly | westGate CAS distributes thermalized configs |

---

## The "Shared Memory" Example — Engineering, Not Physics

QUDA's shared memory advantage is often cited as fundamental. It's not:

**What shared memory gives QUDA:**
- 48 KB per SM, ~100× faster than global memory
- Stencil halo cached: 6 neighbors preloaded, used 6× each
- Reduction within SM without global atomic

**What we have today (WGSL):**
- Subgroup shuffle: register-to-register, faster than shared memory
- Workgroup memory: exists in WGSL but limited (16 KB on some drivers)
- Texture cache (TMU): hardware-managed, automatic for read-only data

**What closes the gap (no CUDA required):**
1. WGSL workgroup memory for stencil halos (spec supports it, needs tuning)
2. Subgroup shuffle for reductions (already faster than shared memory)
3. TMU texture cache for read-only neighbor links (automatic, hardware-managed)
4. coralReef: direct SASS shared memory (bypasses WGSL limitations entirely)

The "shared memory gap" is ~3× at stencil operations. It's closable via (1)
alone, and entirely eliminated by coralReef Phase 2. **This is a 6-month
engineering target, not a fundamental architectural limitation.**

---

## Publication Size Targets by Rung

Based on mesh capacity and competitive analysis:

| Rung | Physics | Publish Volume | Why This Size | Draw |
|------|---------|---------------|---------------|------|
| 1-2 | SU(N) pure gauge | **32⁴** | Matches historical HPC production scale | CUDA-free + vendor-agnostic |
| 3 | Nf=2 dynamical | **32⁴** (possibly 48⁴) | Solver-dominated — 32⁴ is achievable with multigrid | First WGSL fermion code |
| 4 | Nf=2+1 | **48⁴** | With precision folding, fits on 24 GB cards | Physical-mass approach on consumer GPU |
| 5 | Finite-T | **48³×12** | Thermal lattices are 4-8× cheaper than symmetric | EOS on gaming hardware |

**The 48⁴ claim in Rung 3-4 is the "exceeding labs" marker.** At that volume
with dynamical fermions on consumer GPUs, we've matched what required
dedicated HPC clusters just 10 years ago — and our code is portable,
verifiable, and runs on hardware anyone can buy.

---

## Hardware Evolution (Science-Informed Acquisition)

Near-term acquisitions that directly impact publication volumes:

| Card | Cost | Impact on Publication | Priority |
|------|------|---------------------|----------|
| Tesla V100 32GB | $250-400 | Native FP64 oracle — validates DF64 claims in paper | 1 |
| RX 6900 XT (2nd AMD) | $280-380 | +22 DF64 TFLOPS, 3rd independent chain | 2 |
| RX 7900 XTX (24 GB) | $650-800 | 48⁴ on single card, 960 GB/s BW | 3 |
| Tesla P100 16GB | $80-150 | Cheap FP64 canary, cross-generation validation | 4 |

Total investment for full arsenal: ~$1,300-1,700.

**Return**: Publication-quality data at 48⁴, native FP64 validation table in
paper, 4+ simultaneous Markov chains, cross-generation reproducibility proof.

---

## The Structural Advantages That Compound

As we close the throughput gap, our structural advantages become dominant:

| Factor | QUDA (HPC model) | barracuda (sovereign mesh) | Who Wins at Scale |
|--------|-------------------|---------------------------|-------------------|
| Cost per config | $3-5/GPU-hr × queue overhead | ~$0.15/GPU-hr (power) | Us (20-30×) |
| Availability | Batch scheduler, quotas | 24/7 on owned hardware | Us (∞) |
| Reproducibility | "Download our configs" (if available) | pseudoSpore: hash + sign + serve | Us (cryptographic) |
| Vendor diversity | NVIDIA-only physics | Same physics on AMD + NVIDIA + NPU | Us (validation) |
| Verification | Internal review only | Multi-gate, multi-vendor, multi-precision | Us (trust) |
| Accessibility | Requires HPC proposal + allocation | cargo run on any Vulkan GPU | Us (1000× more users) |
| Evolution pace | Large team, slow releases | Single developer + agents, fast iteration | Us (agility) |
| Data sovereignty | DOE/NSF owns the allocation | You own the metal and the data | Us (always) |

**The throughput gap is closing. The structural gap is widening in our favor.**

---

## Cross-Comparison Experiment Plan

Concrete experiments to quantify and publish the comparison:

| Experiment | What We Compare | Publication Value |
|-----------|----------------|-------------------|
| MILC vs barracuda (same config) | Plaquette Δ, wall clock ratio | Paper Table: "Agreement and Performance" |
| openQCD vs barracuda (pure gauge) | Algorithm-level comparison, same β | CPU reference comparison |
| QUDA vs barracuda (RTX 3090) | Same card, same physics, throughput ratio | Honest performance gap quantification |
| barracuda WGSL vs coralReef PTX | Same card, same physics, dispatch overhead | Measures coralReef value |
| V100 native f64 vs RTX 3090 DF64 | Precision comparison (all observables) | Validates DF64 claim empirically |
| RX 6950 XT vs RTX 3090 (DF64) | Same physics, different silicon | Vendor-agnostic proof |
| Multi-card mesh vs single A100 | Total configs/day with queue modeling | Effective throughput comparison |

Each experiment produces a table in the paper. Each table strengthens the
publication. Each comparison teaches us something about the gap and how to close it.

---

*strandGate — Wave 157a — Aug 9, 2026. Every QUDA advantage is an engineering
target: shared memory (WGSL workgroup mem + coralReef SASS), multigrid (TMU
accelerated), tensor cores (coralReef HMMA), multi-GPU (PCIe streaming + mesh).
None are fundamental. The idle gaming mesh provides unlimited availability at
20-30× lower cost. Publication sizes: 32⁴ (Rung 1-2), 48⁴ (Rung 3-4), 48³×12
(Rung 5). coralReef sovereign NVIDIA dispatch is the force multiplier that could
close the remaining throughput gap entirely — sovereign PTX/SASS without CUDA.*
