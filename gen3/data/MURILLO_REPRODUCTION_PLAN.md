# Murillo Group Reproduction Studies

**Status**: Research plan  
**Purpose**: Reproduce published computational physics work from the Murillo Group (MSU) on the basement HPC, then re-execute the core computation on BarraCUDA's Pure Rust vendor-agnostic GPU compute layer  
**Last Updated**: February 7, 2026

---

## The Two-Phase Approach

Every reproduction study follows the same pattern:

1. **Phase A - Reproduce in Python**: Run the original code (Sarkas, mystic, etc.) on our hardware to validate correctness. Match published results. This proves the HPC produces correct physics and gives us a performance baseline using the traditional scientific Python stack (NumPy, Numba, SciPy).

2. **Phase B - Execute on BarraCUDA**: Re-implement the compute-intensive kernels as WGSL shaders running through ToadStool's BarraCUDA engine. Same physics, same math, but in Pure Rust with GPU execution on **any vendor** - NVIDIA, AMD, Intel, whatever has a WebGPU-compatible driver. No CUDA lock-in. No Python interpreter. No Numba JIT. No C/Fortran FFI. Just Rust dispatching WGSL shaders to whatever GPU is available.

**Why this matters**: Scientific computing is overwhelmingly locked to Python + CUDA. Sarkas itself acknowledges this - it's "entirely written in Python without calls to C/Fortran hence avoiding a two-language problem." But it still depends on NumPy (C underneath), Numba (LLVM underneath), and FFTW3 (C/Fortran). BarraCUDA actually solves the problem Sarkas is trying to solve: a single-language compute stack that runs on any hardware. And it does it in a compiled, memory-safe language.

The Phase A → Phase B comparison is itself a research contribution: **can a Pure Rust GPU compute layer match or exceed the performance of the established Python scientific stack for real plasma physics workloads?**

---

## BarraCUDA: What We Have

ToadStool's BarraCUDA submodule has evolved into a comprehensive GPU compute engine. Current inventory from the latest `git pull`:

| Category | Count | Key Operations |
|----------|-------|----------------|
| **Rust ops** | 165+ | Compute modules with CPU fallback |
| **WGSL shaders** | 226+ | GPU compute kernels via WebGPU |
| **Core math** | ~30 | sin, cos, exp, sqrt, pow, log, erf, erfc, lgamma, frac, acos, asin, atan, sinh, cosh, acosh, etc. |
| **Linear algebra** | ~15 | matmul (including fp64), einsum, inverse, determinant, matrix_power, outer_product, tensor_dot, cross_product |
| **Reductions** | ~20 | sum, mean, std, variance, min, max, norm, prod, cumsum, cumprod, logsumexp, prefix_sum, argmin, argmax |
| **Distance/search** | ~8 | cdist, pairwise_distance, cosine_similarity, searchsorted, sort, argsort, unique, histc |
| **Convolution/pooling** | ~20 | conv2d, deformable_conv2d, gated_conv2d, octave_conv2d, grouped_conv2d, separable_conv2d, avg_pool, max_pool, etc. |
| **Attention/transformers** | ~8 | flash_attention, scaled_dot_product, multi_head, grouped_query, local_attention, cross_attention, sparse_attention |
| **Graph neural networks** | ~8 | gcn_conv, gat_conv, gin_conv, sage_conv, edge_conv, graph_norm, graph_batch_norm, message_passing |
| **FHE operations** | ~8 | NTT, INTT, key_switch, modulus_switch, pointwise_mul, extract, rotate, fast_poly_mul |
| **Infrastructure** | 3 | `unified_hardware.rs` (device abstraction), `unified_math.rs` (op dispatch), `scheduler.rs` (workload routing) |

**Key for MD physics**: pairwise_distance, cdist, sum/mean reductions, sort/searchsorted (neighbor lists), einsum (tensor contractions), matmul_fp64 (double precision forces), cumsum/prefix_sum (integration), erf/erfc (Coulomb screening functions), histc (radial distribution g(r)).

**Key for surrogate learning**: full neural network stack (linear, conv, attention, normalization, activation functions, optimizers including SGD/Adam/NAdam/RMSProp/AdaBound/AdaFactor/RAdam/LAMB), loss functions, graph neural networks.

---

## Background

Professor Michael Murillo leads the Murillo Group in MSU's Department of Computational Mathematics, Science and Engineering (CMSE). His research spans computational plasma physics (strongly coupled Coulomb systems, inertial confinement fusion, warm dense matter) and agent-based modeling (infectious disease dynamics). He is a Fellow of the American Physical Society with 80+ peer-reviewed publications and a career that began at Los Alamos National Laboratory.

He taught Applied Machine Learning (CMSE 890, Spring 2025), where a conversation about reservoir computing, echo state machines, and neuromorphic hardware led directly to the BrainChip Akida work in ToadStool. The neuromorphic benchmark datasheet was shared with him in early 2026. An in-person conversation (February 2026) confirmed mutual interest in collaboration; he is currently traveling to California for a talk at an ignition-related conference (likely ICF/NIF community, consistent with his plasma physics work).

**Murillo Group resources (all open source)**:
- **Sarkas**: Pure Python molecular dynamics for dense plasmas (MIT License) - [github.com/murillo-group/sarkas](https://github.com/murillo-group/sarkas)
- **Dense Plasma Properties Database**: Open repository of plasma simulation data (VACF, g(r), EOS, ionization states) - [github.com/MurilloGroupMSU/Dense-Plasma-Properties-Database](https://github.com/MurilloGroupMSU/Dense-Plasma-Properties-Database)
- **Two-Temperature Model**: UCLA-MSU collaboration for plasma equilibration modeling - [github.com/MurilloGroupMSU/Two-Temperature-Model](https://github.com/MurilloGroupMSU/Two-Temperature-Model) (updated January 2025)
- **BIM_HNC**: Binary Ionic Mixture structure in modified Hypernetted Chain approximation (Fortran)
- **Thomas-Fermi Multispecies Ionization**: Jupyter notebook-based ionization calculations

**Key publication**: "Efficient learning of accurate surrogates for simulations of complex systems" - *Nature Machine Intelligence*, May 2024. Introduces optimizer-driven sampling for training ML surrogates of expensive simulations, demonstrated on nuclear equation-of-state models.

---

## Reproduction Study 1: Sarkas Molecular Dynamics

### What

Reproduce Sarkas plasma simulations on the basement HPC, then port the core MD compute kernels to BarraCUDA for vendor-agnostic GPU execution.

### Phase A: Python Reproduction (Validate Correctness)

Run Sarkas examples (Yukawa potentials, Coulomb systems, binary ionic mixtures, ultracold neutral plasmas) on the basement HPC. Validate results against the Dense Plasma Properties Database reference data. Benchmark CPU performance across architectures.

**Sarkas computational pipeline** (what we need to understand before porting):
1. **Initialization**: Particle positions/velocities from configuration
2. **Force calculation**: Pairwise particle interactions (Coulomb, Yukawa, screened potentials) - **the hot loop**
3. **Long-range forces**: PPPM/Ewald via FFT (uses FFTW3/pyfftw) - **most compute-intensive**
4. **Neighbor lists**: Cell-linked lists or Verlet lists (sort/search)
5. **Integration**: Velocity-Verlet time stepping (basic arithmetic)
6. **Diagnostics**: VACF, g(r), structure factors, EOS (reductions + FFT)

The Python stack for each: NumPy arrays → Numba JIT for loops → pyfftw for FFTs → SciPy for special functions.

**Hardware targets**:

| Gate | CPU | Role |
|------|-----|------|
| Strandgate | Dual EPYC 7452 (64c) | Primary MD, massive parallelism baseline |
| Northgate | i9-14900K | Fast single-thread comparison |
| Southgate | 5800X3D | 3D V-Cache neighbor list performance |

**Deliverables**:
- Sarkas tutorials validated against published reference data
- CPU performance comparison: EPYC 64c vs i9-14900K vs 5800X3D (same simulation, same parameters)
- Profiling data: where does Sarkas spend time? (force calc vs FFT vs neighbor list vs integration)

### Phase B: BarraCUDA Port (Vendor-Agnostic GPU Physics)

Take the profiled hot paths from Phase A and implement them as WGSL shaders dispatched through BarraCUDA. The goal is a Pure Rust MD engine that runs on any GPU.

**Kernel mapping** (Sarkas Python → BarraCUDA WGSL):

| MD Operation | Sarkas (Python) | BarraCUDA (WGSL) | Status |
|-------------|-----------------|-------------------|--------|
| Pairwise forces | NumPy broadcasting + Numba | `pairwise_distance.wgsl` + `cdist.wgsl` + custom force shader | Distance ops exist, force shader needed |
| Coulomb screening | SciPy `erfc()` | `erfc.wgsl` + `erf.wgsl` | **Ready** |
| Neighbor lists | NumPy sort + cell lists | `sort.wgsl` + `searchsorted.wgsl` + `argsort.wgsl` | **Ready** |
| Velocity-Verlet | NumPy arithmetic | `unified_math.rs` basic ops | **Ready** |
| Reductions (energy, pressure) | NumPy `sum()`, `mean()` | `sum_reduce.wgsl` + `mean_reduce.wgsl` | **Ready** |
| Radial distribution g(r) | NumPy `histogram()` | `histc.wgsl` + `bincount.wgsl` | **Ready** |
| Structure factors | pyfftw FFT | NTT/INTT shaders exist; true FFT shader needed | **Partial** (NTT ≠ FFT, but structure exists) |
| Tensor contractions | NumPy `einsum()` | `einsum.wgsl` | **Ready** |
| Double-precision forces | NumPy float64 | `matmul_fp64.wgsl` + u64 emulation (`u64_emu.wgsl`) | **Ready** |

**Key engineering challenge**: FFT. Sarkas uses FFTW3 for Particle-Particle Particle-Mesh (PPPM) long-range force decomposition. BarraCUDA has NTT/INTT (number theoretic transform - for FHE), but a true complex FFT shader is needed for PPPM. This is the primary new development required.

**Hardware targets** (Phase B runs on GPUs):

| Gate | GPU | Role |
|------|-----|------|
| Northgate | RTX 5090 | Primary BarraCUDA execution, best single-GPU |
| Strandgate | RTX 3090 + RX 6950 XT | Cross-vendor comparison (NVIDIA vs AMD, same shader) |
| Eastgate | RTX 4070 | Mid-tier comparison |

**Deliverables**:
- Pure Rust MD force kernel running on GPU via WGSL
- Same physics producing identical results to Sarkas Python (bit-for-bit or within float tolerance)
- Performance comparison: Python/NumPy/Numba on 64 CPU cores vs BarraCUDA on RTX 5090 vs RTX 3090 vs RX 6950 XT
- **The headline result**: same plasma simulation running on NVIDIA and AMD from the same shader, no CUDA, no ROCm, no vendor SDK
- NPU exploration: can Akida accelerate any subproblem (force classification, surrogate potential)?

### Available Data

- **Sarkas examples**: Yukawa potentials, Coulomb systems, binary ionic mixtures, ultracold neutral plasmas
- **Dense Plasma Properties Database**: Reference VACF, g(r), EOS data for validation (14+ subdirectories)
- **Two-Temperature Model**: Jupyter notebooks with UCLA collaboration data

---

## Reproduction Study 2: Surrogate Learning (Nature Machine Intelligence 2024)

### What

Reproduce the optimizer-driven sampling method from "Efficient learning of accurate surrogates for simulations of complex systems" on our hardware, then train the same surrogates entirely through BarraCUDA's neural network stack.

### Phase A: Python Reproduction (Validate Results)

Run the Code Ocean capsule on our hardware. Reproduce the key figures. Benchmark training on consumer GPUs vs the original compute environment.

The paper uses:
- **mystic** optimizer for directed sampling (constrained optimization framework)
- Standard ML training: RBF networks, neural networks
- Nuclear EOS models (from CompOSE database and published tables)

**Available Data (Open Access)**:

| Resource | URL | Format |
|----------|-----|--------|
| **Paper** | [Nature Machine Intelligence, May 2024](https://doi.org/10.1038/s42256-024-00839-1) | Journal article |
| **Datasets** | [Zenodo: 10.5281/zenodo.10908462](https://doi.org/10.5281/zenodo.10908462) | Directed sampling datasets |
| **Code** | [Code Ocean: 10.24433/CO.1152070.v1](https://doi.org/10.24433/CO.1152070.v1) | Reproducible capsule |
| **Optimizer** | [mystic](https://pypi.org/project/mystic/) (`pip install mystic`) | Python package |

**Deliverables**:
- Reproduction of paper's key figures on consumer GPU hardware
- Training time comparison: RTX 5090 vs RTX 3090 (Python/PyTorch baseline)

### Phase B: BarraCUDA Surrogate Training (Pure Rust ML)

Re-implement the surrogate training pipeline entirely in BarraCUDA. The neural network components already exist:

| Surrogate Component | Python Stack | BarraCUDA | Status |
|--------------------|-------------|-----------|--------|
| Linear layers | PyTorch `nn.Linear` | `linear.wgsl` | **Ready** |
| Activation functions | PyTorch GELU/ReLU/etc. | `gelu.wgsl`, `silu.wgsl`, `mish.wgsl`, etc. (30+ activations) | **Ready** |
| Loss computation | PyTorch loss functions | `l1_loss.wgsl`, `kldiv_loss.wgsl`, `nll_loss.wgsl`, etc. | **Ready** |
| Optimizers | PyTorch Adam/SGD | `nadam/`, `sgd/`, `rmsprop/`, `adabound.wgsl`, `adafactor.wgsl`, `radam.wgsl`, `lamb.wgsl` | **Ready** |
| Normalization | PyTorch LayerNorm/BatchNorm | `layer_norm.wgsl`, `batch_norm2d.wgsl`, `group_norm.wgsl`, `instance_norm.wgsl` | **Ready** |
| Reductions/statistics | NumPy/PyTorch | Full reduction stack (sum, mean, std, variance, min, max, norm) | **Ready** |
| Attention (if needed) | PyTorch MHA | `flash_attention.wgsl`, `scaled_dot_product_attention/`, `multi_head_attention/` | **Ready** |
| RBF networks | SciPy/custom | Custom kernel needed (but `pairwise_distance.wgsl` + `exp.wgsl` = RBF basis) | **Composable** |
| Graph nets (if needed) | PyG | `gcn_conv.wgsl`, `gat_conv.wgsl`, `sage_conv.wgsl`, `message_passing.wgsl` | **Ready** |

The optimizer-driven sampling loop itself (mystic) is CPU-side logic. The compute-intensive part - training the neural surrogate on each batch of directed samples - is what moves to BarraCUDA.

**Hardware targets** (Phase B runs on GPUs):

| Gate | GPU | Role |
|------|-----|------|
| Northgate | RTX 5090 | Primary BarraCUDA surrogate training |
| Strandgate | RTX 3090 + RX 6950 XT | Cross-vendor: same training, NVIDIA vs AMD |
| Eastgate | RTX 4070 | Mid-tier comparison |

**Deliverables**:
- Same surrogate model trained via BarraCUDA producing equivalent accuracy to Python/PyTorch
- Training time comparison: PyTorch on RTX 5090 vs BarraCUDA on RTX 5090 vs BarraCUDA on RX 6950 XT
- **The headline result**: scientific ML surrogate trained entirely in Pure Rust, running on any GPU vendor, no Python, no PyTorch, no CUDA
- Cross-vendor accuracy validation: NVIDIA-trained surrogate vs AMD-trained surrogate produce identical predictions

---

## Reproduction Study 3: Agent-Based Modeling (Infectious Disease)

### What

Run Murillo Group's agent-based influenza models on the basement HPC, then explore BarraCUDA GPU-accelerated agent simulation.

### Phase A: Python Reproduction (CPU Scaling)

Agent-based models are inherently parallelizable and memory-intensive. Strandgate's 64-core EPYC with 256GB ECC is purpose-built for this.

**Why this study matters beyond benchmarks**:
- Agent-based modeling of infectious disease has structural similarities to the primal coordination model in ecoPrimals. Agents interact through local rules (like primals coordinating through IPC), and macro behavior emerges from micro interactions (like NUCLEUS emerging from primal composition). This is the same computational paradigm.
- The author's microbiology training (Medical Microbiology, Virology, Molecular Pathogenesis) provides domain knowledge that most computational physicists don't have. Understanding influenza dynamics at the cellular level can inform model validation and parameterization.

**Available Data**:
- Murillo Group publications on agent-based influenza modeling
- Standard epidemiological datasets for validation (CDC FluView, WHO)
- Specific code/data to be requested from Murillo Group
- **Note**: Agent-based model code may not be open-source. This study depends on collaboration access.

**Deliverables**:
- Large-scale agent simulation runs on 64-core EPYC
- CPU scaling: how does performance change from 8 → 16 → 32 → 64 cores?
- Comparison vs i9-14900K (fewer cores, higher clock)

### Phase B: BarraCUDA Agent Simulation (GPU-Parallel Agents)

Agent-based models map naturally to GPU compute: each agent is an independent work item, interactions are local (pairwise distance), and state updates are parallel. BarraCUDA already has the primitives:

| ABM Operation | BarraCUDA | Notes |
|--------------|-----------|-------|
| Agent distance/contact | `pairwise_distance.wgsl`, `cdist.wgsl` | Spatial proximity = contact network |
| State transitions | `masked_fill.wgsl`, `where_op.wgsl` | Conditional state updates (S→I→R) |
| Population statistics | `sum_reduce.wgsl`, `mean_reduce.wgsl`, `histc.wgsl` | Epidemic curves, age distributions |
| Stochastic events | Existing random ops | Infection probability, recovery timing |
| Spatial grid | `scatter.wgsl`, `gather.wgsl` | Agent-to-grid mapping |
| Graph structure | `message_passing.wgsl`, `gcn_conv.wgsl` | Contact network as graph |

**The question**: can hundreds of thousands of agents be simulated per GPU dispatch, with contact networks evaluated via `message_passing.wgsl`? If so, BarraCUDA turns ABMs from a CPU-scaling problem into a GPU-throughput problem.

**Hardware targets**:

| Gate | Specs | Role |
|------|-------|------|
| Strandgate | 64c EPYC + RTX 3090 | CPU baseline + GPU comparison on same node |
| Northgate | i9-14900K + RTX 5090 | Best GPU execution |
| Strandgate | RX 6950 XT | Cross-vendor ABM on AMD |

**Deliverables**:
- GPU-accelerated agent simulation via BarraCUDA
- Population scaling: how many agents can BarraCUDA handle per timestep on RTX 5090 vs 64 CPU cores?
- Cross-domain analysis: structural parallels between ABM and primal coordination
- NPU exploration: can Akida's spiking networks model agent decision-making (state transition as spike event)?

---

## Timeline

### Pre-NUCLEUS (Now)

| Task | Status |
|------|--------|
| ToadStool benchmark data collection (NPU/GPU/FHE) | **In progress** |
| BarraCUDA op inventory and capability mapping | **Done** (this document) |
| Identify all Murillo Group repos and data sources | **Done** (see `MISE_EN_PLACE.md`) |
| Locate Zenodo datasets + Code Ocean capsule | **Done** |
| Document BarraCUDA → Sarkas kernel mapping | **Done** (this document) |
| Read Sarkas docs/tutorials thoroughly | Planned |
| Read Nature MI paper in full | Planned |
| Download Zenodo datasets locally | Planned |
| Clone all Murillo Group repos for review | Planned |
| Identify FFT gap in BarraCUDA (needed for PPPM) | **Identified** |

### Post-NUCLEUS (Phase A - Python Reproduction)

| Task | Depends On |
|------|-----------|
| Sarkas quickstart validation | NUCLEUS stable, Westgate cold storage online |
| Sarkas CPU benchmarks (EPYC vs i9 vs 5800X3D) | Sarkas validated |
| Sarkas profiling (where does time go?) | Sarkas benchmarks |
| Surrogate learning Code Ocean reproduction | Zenodo data downloaded |
| Surrogate learning GPU benchmarks (PyTorch) | Code Ocean validated |
| Agent-based model code acquisition | Murillo collaboration |
| Agent-based model CPU scaling | ABM code available |

### Post-NUCLEUS (Phase B - BarraCUDA Execution)

| Task | Depends On |
|------|-----------|
| MD force kernel WGSL shader | Sarkas profiling (know the hot path) |
| FFT WGSL shader (for PPPM) | New BarraCUDA development |
| MD validation (BarraCUDA vs Sarkas results match) | Force kernel + FFT ready |
| MD cross-vendor benchmark (NVIDIA vs AMD) | MD validation |
| Surrogate training via BarraCUDA neural stack | Phase A surrogate results |
| Surrogate cross-vendor training (same model, different GPU) | BarraCUDA surrogate working |
| ABM GPU agent simulation | Phase A ABM results |
| ABM population scaling on GPU vs CPU | ABM GPU working |

---

## Infrastructure Dependencies

This is a long-term, whole-ecosystem project. The reproduction studies require a working NUCLEUS deployment before execution can begin at scale.

### Blocking Requirements

1. **NUCLEUS stability**: Tower, Node, and Nest Atomics must be reliably composing before we route data and compute across the mesh.
2. **Westgate as cold data hub**: NestGate must be managing Westgate's 76TB ZFS pool via content-addressed storage. All raw data, simulation output, and datasets land on Westgate. Compute nodes pull data over the mesh.
3. **10G backbone**: The copper 10G NICs are installed on North/South/East/Westgate. Switch is acquired. Cables are the remaining bottleneck. Large MD simulation output and dataset transfers need the bandwidth.
4. **biomeOS coordination**: Workload routing (MD to Strandgate, surrogate training to Northgate, visualization to any available gate) requires biomeOS's Neural API to be functional.

### What Can Be Done Now (Pre-NUCLEUS)

See `MISE_EN_PLACE.md` for the full checklist. Key items:
- Clone repos locally for review
- Download Zenodo datasets
- Install Sarkas on one gate for tutorial validation
- Read the Nature paper thoroughly
- Review Sarkas documentation and tutorials

---

## The Bigger Picture

Sarkas solved one problem: making MD accessible by writing it in pure Python instead of C/Fortran. But it still depends on NumPy (C underneath), Numba (LLVM underneath), pyfftw (FFTW3, C/Fortran underneath), and it's locked to CPUs.

BarraCUDA solves the next problem: making GPU compute accessible by writing it in Pure Rust with WGSL shaders that run on **any** GPU vendor. No CUDA. No ROCm. No HIP. No OpenCL. No vendor SDK. One set of shaders, every GPU.

If we can demonstrate that real plasma physics (Sarkas-equivalent simulations) and real scientific ML (surrogate training) run correctly and competitively on BarraCUDA, that's not just a reproduction study - it's a demonstration that **scientific computing doesn't have to be locked to interpretive languages or proprietary GPU stacks**.

This connects directly to the ecoPrimals thesis: sovereignty through constraint. BarraCUDA constrained itself to WGSL/WebGPU (portable, vendor-neutral) and emerged with 226+ shaders that can run plasma physics on an AMD card or an NVIDIA card from the same binary. The same pattern that produced Taq polymerase from a hot spring produces universal GPU compute from a portability constraint.

---

## Notes

- Professor Murillo is in California this week (ignition conference talk). Follow up when he returns.
- The neuromorphic benchmark datasheet (v1) has already been shared. Updated benchmarks from ToadStool's current runs will be shared as v2 when available.
- All reproduction studies should be documented with sufficient detail for publication or inclusion in a joint paper.
- The FFT gap in BarraCUDA is the primary technical blocker for Phase B of Study 1. NTT/INTT exist for FHE. A complex FFT shader for scientific simulation is the natural next evolution.
- BarraCUDA's `unified_hardware.rs` + `scheduler.rs` already handle device detection and workload routing. The infrastructure for "run this kernel on whatever GPU is available" already exists.
