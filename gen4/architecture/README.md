# gen4/architecture/

**The structural patterns for composing primals into products.**

---

## Reading Order

1. **ANCHORING_PIPELINE.md** — The concrete mechanism: how a computation
   on a home HPC becomes a BTC/ETH-anchored proof. DAG recording,
   Ed25519 signing, dehydration, OP_RETURN anchoring, verification CLI.
   **Start here if you want to understand what the provenance trio
   actually does end-to-end.**

2. **COMPOSITION_PATTERNS.md** — The patterns discovered building
   esotericWebb V4: PrimalBridge, deploy graphs, graceful degradation,
   tiered narration, the zero-import principle. Start here if you are
   building a gen4 product.

3. **CREATIVE_SURFACE_ARCHITECTURE.md** — The sporeGarden organizational
   model, the four-layer product architecture, lean consumption vs. hard
   linking, federation, the content pipeline. Start here if you are
   designing a new gen4 product.

4. **GUIDESTONE.md** — The verification class: how computation becomes
   proof. Defines the quality grade that certifies an ecoBin produces
   reproducible, self-proving output. The five properties: deterministic,
   reference-traceable, self-verifying, environment-agnostic, tolerance-
   documented. Includes "The First Deployment Artifact" section documenting
   the v0.7.0 experience. Start here if you need to understand what makes
   gen4 output trustworthy when the primals are invisible.

5. **DEPLOYABLE_ARTIFACT_STANDARD.md** — How a guideStone-certified
   artifact becomes portable science. The eight-layer anatomy (entry
   point, binary layout, container fallback, integrity, self-knowledge,
   documentation, reference data, cross-OS launchers). Self-leveling
   benchmark: hardware characterization as a side effect of validation.
   The Chuna onboarding pattern. **Start here if you are shipping a
   guideStone artifact to a collaborator or institution.**

6. **BIOMEOS_OS_TRAJECTORY.md** — The long-term vision: biomeOS evolving
   from orchestrator to standalone sovereign operating system. The SteamOS
   analogy, layer architecture, deployment models, honest timeline. Start
   here if you want to understand where gen4 leads.

7. **NUCLEUS_SOVEREIGNTY_ARCHITECTURE.md** — The sovereignty evolution
   from calibration instruments to sovereign primals. What's evolved
   (Horizon 1 security, Horizon 2 parallels), what's validated as secure
   (darkforest, Dark Forest gate, membrane audit), what remains (DNS,
   content serving, CI/CD, package registries). The glacial metaphor:
   interstadial pre-wires, stadial validates under load. **Start here if
   you want to understand the current sovereignty posture.**

8. **CELLMEMBRANE_FIELDMOUSE_ARCHITECTURE.md** — The first primal
   deployment on external substrate. VPS as touchpoint, gate as source.
   Tower composition (BearDog + SkunkBat), three membrane channels,
   content-aware routing, credential encryption. The operational model
   for deploying NUCLEUS at scale. **Start here if you want to understand
   the inner membrane.**

---

## Relationship to gen3 Architecture

gen3's architecture papers (ECOSYSTEM_ARCHITECTURE, PRIMAL_CATALOG,
SPRING_CATALOG) describe the infrastructure. gen4's architecture papers
describe how to **consume** that infrastructure invisibly.

| gen3 architecture | gen4 architecture |
|-------------------|-------------------|
| PRIMAL_CATALOG | COMPOSITION_PATTERNS (how to wire them) |
| ECOSYSTEM_ARCHITECTURE | CREATIVE_SURFACE_ARCHITECTURE (how to organize around them) |
| SPRING_CATALOG | Product catalog in CREATIVE_SURFACE_ARCHITECTURE |
| NUCLEUS_ATOMICS | Deploy graph wave ordering |
| EXTERNAL_VALIDATION_ARTIFACT | GUIDESTONE (generalized verification class) |
| liveSpore / ColdSpore | DEPLOYABLE_ARTIFACT_STANDARD (portable science) |
| biomeOS manifesto | BIOMEOS_OS_TRAJECTORY (where the orchestrator is going) |

---

*gen3 describes the parts. gen4 describes the assembly. guideStone certifies the output. The Deployable Artifact carries it all.*
