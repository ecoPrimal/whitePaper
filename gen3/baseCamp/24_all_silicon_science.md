# Sub-Thesis 24: All-Silicon Science — Repurposing Every GPU Hardware Unit for Computational Physics

**Date:** March 26, 2026
**Status:** First non-shader-core experiment complete (TMU, Exp 096). 4 of 9 units tested.
**Domain:** GPU hardware architecture × computational physics × all-silicon pipeline
**Novelty:** No prior work systematically maps computational physics operations to
all 9 GPU silicon unit types with empirical throughput measurements and tolerance
characterization, nor proposes a tolerance-based routing system that automatically
selects hardware units based on mathematical precision requirements.
**Cross-Spring:** hotSpring × barraCuda × toadStool × coralReef × ALL springs

---

## Abstract

Modern GPU dies contain at least 9 distinct hardware units: shader cores, tensor
cores, RT cores, texture units, ROPs, rasterizer, depth buffer, tessellator, and
video encoder. Each was designed for a specific graphics operation but computes a
general mathematical function. The DF64 discovery proved the pattern: fp32 ALUs
"designed for pixel colors" emulate fp64 at 8-16x throughput. This sub-thesis
extends that discovery systematically across every unit on the die.

We map 11 QCD operations to their optimal silicon units, empirically validate the
TMU pathway (1.89x throughput for table lookup on RTX 3090), discover that AMD
RDNA2 outperforms NVIDIA Ampere on DF64 arithmetic by 38%, and propose a
tolerance-based routing system where the mathematical precision requirement — not
the programmer's hardware choice — determines which silicon executes the work.

## Key Results

### TMU Table Lookup (texture_unit)

Precomputed exp(x) in a 1024-entry texture. Compute shader accesses via
`textureLoad`. TMU hardware performs the memory fetch through its spatial cache,
bypassing the general-purpose memory hierarchy.

- **RTX 3090 (328 TMUs):** 1.89x throughput over compute exp()
- **RX 6950 XT (96 TMUs):** 1.24x throughput
- **llvmpipe (0 TMUs):** 0.92x (CPU emulation, no hardware TMU)

Speedup correlates with TMU count ratio: NVIDIA has 3.4x more TMUs.

### AMD DF64 Advantage

AMD RDNA2 produces 38% better DF64 throughput (23.4M vs 16.9M ops/s) and
higher DF64 fidelity than NVIDIA Ampere. This is a genuine architectural
advantage for double-float science computing that no existing framework
exploits.

### The Hidden Computers

Each GPU unit computes a specific mathematical function at silicon speed:

| Unit | Mathematical Function | Science Application |
|------|----------------------|-------------------|
| Shader Core | FP arithmetic (add, mul, fma) | All compute (baseline) |
| Texture Unit | 2D interpolated lookup | EOS tables, exp/log |
| Tensor Core | Matrix multiply-accumulate | CG solver, FFT butterfly |
| RT Core | BVH traversal + intersection | MD neighbor search |
| ROP | Per-pixel scatter-add | Force accumulation |
| Rasterizer | Point-in-polygon + interpolation | Particle binning |
| Depth Buffer | Per-pixel min reduction | Voronoi diagrams |
| Tessellator | Adaptive mesh subdivision | AMR |
| Video Encoder | Block transform + entropy | Trajectory compression |

## Architectural Contribution

### Tolerance-Based Routing

The key insight: barraCuda specifies tolerance (e.g., 1e-14 relative error),
not hardware (e.g., "use fp64"). toadStool maps tolerance to hardware based
on measured performance surface data from spring experiments.

```
Application: barraCuda.math.pairwise.yukawa(particles, tolerance=1e-14)
                         │
                   toadStool routing (measured performance surface)
                         │
         ┌───────────────┼───────────────────┐
    shader_core     texture_unit          tensor_core
    (DF64 force)    (EOS lookup)      (CG preconditioner)
```

A new hardware unit requires only: coralReef learns to emit its instructions,
toadStool learns to discover and route to it. barraCuda and all springs are
unchanged.

### The Compound Effect

If each of the 8 non-shader-core units yields even 3-5x improvement on the
operations it accelerates:

| Configuration | Effective TFLOPS | Source |
|--------------|-----------------|--------|
| Native fp64 only | 0.33 | RTX 3090 fp64 rate |
| + DF64 | 3.24 | fp32 ALU double-float |
| + TMU tables | ~5 | Table lookup offloads transcendentals |
| + Tensor CG | ~20 | TF32 MMA for solver |
| + RT neighbors | ~25 | BVH spatial queries |
| + ROP scatter | ~30 | Hardware accumulation |
| + Full pipeline | ~50-100 | All units running in parallel |

A single consumer GPU running the all-silicon pipeline could match a small
HPC cluster for science throughput.

## Relation to Constrained Evolution Thesis

The GPU's hardware units evolved under the constraint of real-time graphics:
rasterizers for triangles, depth buffers for occlusion, TMUs for textures.
The science adapts to these constraints — mapping physics operations onto the
I/O contracts that already exist in silicon. This is constrained evolution at
the hardware level: the "organism" (scientific computation) doesn't redesign
the "environment" (GPU silicon) but finds unexpected fitness in the existing
landscape.

## Open Questions

1. Does TMU linear filtering (`textureSampleLevel`) close the accuracy gap
   to sub-0.1% while maintaining the throughput advantage?
2. Can the rasterizer's spatial query throughput exceed compute-shader
   binning by 10-50x for particle methods as hypothesized?
3. Does the depth buffer Voronoi trick work for distance fields in 3D
   (using multi-view rendering)?
4. Can tensor core MMA at TF32 serve as a CG preconditioner while DF64
   handles the refinement — mixed-precision CG across silicon units?
5. What is the overhead of mixed command streams (compute + draw + RT)
   versus sequential dispatch?

## References

- hotSpring Exp 096: `experiments/096_SILICON_SCIENCE_TMU_QCD_MAPPING.md`
- wateringHole: `GPU_FIXED_FUNCTION_SCIENCE_REPURPOSING.md`
- toadStool: `specs/ALL_SILICON_PIPELINE.md`
- Sub-thesis 14: `14_sovereign_compute_hardware.md`
- Dekker, T. J. (1971). "A floating-point technique for extending the available precision"
