# Email: arXiv Preprint — Pre-Submission Review Request (August 2026)

**To**: TC Chuna (LANL)
**CC**: Professor Murillo (MSU)
**From**: mokkevin@msu.edu
**Subject**: SU(N) lattice gauge paper — asking for your review before arXiv
**Attachment**: PDF of preprint + pseudoSpore artifact link

---

Hi TC,

Hope LANL is going well. Wanted to share something concrete — I have an
arXiv preprint ready for review and you're one of three people I'd like
feedback from before I submit.

**Paper**: "Vendor-Agnostic SU(N) Lattice Gauge Theory on Consumer GPUs:
Pure Gauge HMC for N=2,3,4,5,6,8 with DF64 WebGPU/WGSL and Cryptographic
Provenance"

**Target**: arXiv hep-lat, cross-list cs.DC

The scope grew since we last talked. It's no longer SU(3) only — the code
now covers SU(N) for N=2,3,4,5,6,8 through a generic gauge group trait,
all on the same volumes, same hardware, same provenance chain. Quick
summary of what's in the paper:

- **SU(N) ladder**: N=2,3,4,5,6,8 pure gauge HMC. Fixed-size SU(2) and
  SU(3) matrix types for production, heap-allocated SU(N) for N=4+
  (Cabibbo-Marinari subgroup decomposition). 652 library tests.
- **Cross-vendor parity**: NVIDIA RTX 3090 and AMD RX 6950 XT produce
  identical physics from the same WGSL shaders and same cached configs.
  Inter-GPU agreement: 6 ppm at β=6.2. No CUDA, no ROCm.
- **Plaquette values**: β=6.0 on 16⁴ matches Necco-Sommer to +0.01%.
- **HMC validation**: Action-force finite-difference to 6 significant
  figures. Creutz equality ⟨exp(−ΔH)⟩ = 0.999985. β-scan from 2.0 to
  6.5 matches published SU(3) literature.
- **Observables**: Plaquette, Polyakov loops, Wilson loops W(R,T), Creutz
  ratios χ(R,T), gradient flow scales.
- **Cost**: The machine that produced this data cost ~$1,100 in used parts
  (dual EPYC 7452, 256 GB ECC). GPUs are an RTX 3090 ($500 used) and an
  RX 6950 XT ($350 used).

There's also a neuromorphic coprocessor angle — a BrainChip AKD1000 ($300)
running real-time phase classification on the cached configurations at
2 µs per sample. It's in the paper as a demonstration of heterogeneous
compute, not a central claim.

This is Rung 1 of a 5-rung ladder — pure gauge execution and arithmetic
validation. Dynamical fermions (what you and I talked about in April) are
Rung 3. MILC-compatible output is now operational:

- **MILC v5 export**: `milc_validation_loop export-cached` writes our
  configs to MILC binary format (big-endian, CRC32 checksums).
- **Round-trip validated**: export → import → Δ⟨P⟩ = 3×10⁻⁹ (f32-limited).
- **Ready for you**: I have a 16⁴ β=6.0 config in MILC format — you can
  `su3_gauge_read` it and compare plaquettes. ⟨P⟩ = 0.5925.

The ILDG pipeline is also operational (14/14 configs round-trip at f64
bit-identical). The Chuna Engine foundation isn't just "planned" anymore —
the bidirectional exchange path works.

I wrote a 42-item reviewer rubric organized by what each of you three
(you, Professor Murillo, and Bazavov) would scrutinize. It's in the repo
at `whitePaper/subGen/ARXIV_REVIEWER_RUBRIC.md`. I've been working through
it — most items are resolved, a few are still in progress.

**What I'm asking**: Read the paper and tell me what's wrong. Anything
that looks suspicious, insufficiently justified, or that a hep-lat
referee would flag. Your LANL perspective on whether the HMC validation
methodology is rigorous enough is especially valuable. If the physics
checks out and you're willing, I'd welcome your name on the
acknowledgments.

The paper, source, data, and a reproducibility artifact are all at the
repo you already have:

  https://github.com/syntheticChemistry/hotSpring

The preprint markdown is `whitePaper/subGen/LATTICE_QCD_CONSUMER_GPU_ARXIV.md`.
LaTeX source is `lattice_qcd_consumer_gpu.tex` in the same directory.

If you want to run the validation: `cargo run --release --bin arxiv_measure_battery`
reproduces the full observable battery. Static binary available if you
prefer no toolchain.

No rush — I know LANL keeps you busy. Whatever timeline works.

Kevin

Kevin Mok
MS Data Science / BS Microbiology, MSU
(586) 453-7233 | mokkevin@msu.edu

---

## Notes

- **Use "TC"** — that's how he signs his emails and introduced himself.

- **Lead with the paper, not the project.** This is the first time we're
  sending a deliverable that looks like a physics paper, not a repo tour
  or an artifact demo. Let the paper do the talking.

- **The scope change is the headline.** He knew about SU(3). SU(N) for
  N=2 through 8 on the same code/hardware/provenance is genuinely novel —
  no prior study has done this. State it factually.

- **Acknowledge the gap.** Dynamical fermions (Rung 3) and MILC output
  were discussed in April. They aren't here. Name them explicitly and
  frame them as future rungs, not broken promises.

- **42-item rubric is the credibility signal.** It shows we anticipated
  their questions and are working through them systematically. TC will
  appreciate the rigor. Bazavov-specific items (B1–B12) are the most
  domain-critical.

- **NPU: mention, don't oversell.** TC is a terminal/SSH physicist.
  Neuromorphic hardware is interesting but peripheral to whether the
  HMC is correct. One sentence. The paper has the detail if he cares.

- **Cost: let the numbers speak.** $1,100 machine + $500 GPU + $350 GPU
  + $300 NPU = ~$2,250 total. Don't say "I replaced ICER." He'll draw
  the conclusion.

- **"Tell me what's wrong"** is the right ask. Not "validate my results"
  (which implies they should be right) and not "collaborate" (which is
  premature). He's a reviewer — give him a reviewer's mandate.

- **Acknowledgments, not co-authorship.** Co-authorship requires
  contribution to the work. Acknowledgment for review feedback is
  standard and appropriate. If his feedback leads to substantive changes,
  the conversation about co-authorship can happen naturally.

- **CC Murillo.** Established practice. Murillo has the computational
  physics context. He asked about Kokkos — the paper's vendor-neutrality
  story is effectively the answer to his question.

- **Bazavov contact.** Don't mention Bazavov in the email body beyond the
  rubric reference. TC said in April that Bazavov needs MILC data — that's
  a separate conversation for after the MILC generator exists. The rubric
  documents what Bazavov would ask; TC can share it with him if he chooses.

- **Don't attach the full PDF.** Point to the repo. TC is SSH-native —
  he'll clone or curl. If he asks for a PDF, generate one from the LaTeX
  and send it. But don't preload the attachment.

- **Timeline.** "No rush" is genuine. The paper isn't going stale — the
  SU(N) data is growing (thermalizers running 24/7). A 2-4 week review
  window is reasonable. One follow-up after 3 weeks if no response.
