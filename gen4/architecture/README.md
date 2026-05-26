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

9. **SOVEREIGN_COMPOSITION_EVOLUTION.md** — The evolution from shipped
   primals to sovereign self-hosted safe primal compositions. Separates
   primal goals (Layer 1) from sovereignty goals (Layer 3), maps the
   overlaps, defines the Rust thread, and charts the final convergence.
   **Start here if you want to understand the full sovereignty arc.**

### K-Derm Topology and Bonding

10. **K_DERM_RECONCILIATION.md** — Bridges the gram-negative/gram-positive
    framing in gen4 documents to the canonical K-Derm cell envelope model.
    Resolves Franklin's Current (conflicting inner/outer labels), maps every
    gen4 concept to K-Derm absolute layers (cytoplasm/plasma/periplasm/outer/
    extracellular), connects NUCLEUS atomics to envelope placement, and aligns
    sovereignty layers with K-Derm boundaries. **Start here if you want to
    understand how gen4 membrane vocabulary maps to the K-Derm standard.**

### Sovereignty and Infrastructure Cluster

11. **SOVEREIGN_HPC_EVOLUTION.md** — From basement cluster to gram-negative
    organism. Three-layer membrane model, bonding at each layer, full
    hardware inventory, 10G backbone plan, multi-VPS future architecture.

12. **SOVEREIGN_COMPUTE_TRIO_SKETCH.md** — coralReef + toadStool + barraCuda
    IPC split, degradation tiers, absorption path for compute sovereignty.

13. **SOVEREIGN_TRANSACTION_MEMBRANE.md** — NFT fermentation, Tier 2
    ceremony, NestGate/Steam federation, economics through the membrane.

14. **GPU_HEAT_RECOVERY_OPERATIONS.md** — Science-as-heating, seasonal
    dispatch bias, thermal zone telemetry integration with gate TOMLs.

### Validation and Lifecycle Cluster

15. **CONTRACT_TESTING_THESIS_SKETCH.md** — Wire format as contract,
    transport parity across tiers, implications for validation pipelines.

16. **GUIDESTONE_LTEE.md** — Concept for Barrick/Lenski LTEE-focused
    verification artifact using hotSpring and wetSpring modules.

17. **DEPLOY_GRAPH_COMPOSITION.md** — BYOB schema for session-as-primal,
    deploy graph declaration, ecosystem flywheel for new products.

18. **STADIAL_INTERSTADIAL_PATTERN.md** — Ecosystem convergence/divergence
    cycles, fossil record, Tier 1/2 gate criteria, selection under constraints.

### Operations and Resilience

19. **INFRASTRUCTURE_RECREATION_AND_OUTAGE_PLAYBOOK.md** — Cold-start
    rebuild from bare metal to full composition. Outage simulation catalog
    (VPS loss, WAN loss, gate power loss, LAN partition, Forgejo down,
    full site power loss). Acceptance criteria for each scenario.
    **Start here if you need to understand how to recreate or test
    the infrastructure.**

### Hardware Sovereignty

20. **SOVEREIGN_WARM_KEEPALIVE.md** — 183ms GPU initialization on sovereign
    hardware. Falcon warm preservation eliminates ACR re-boot, systemd fd
    store keeps GPUs warm across daemon restarts, cold early-exit skips
    doomed training. The hardware management layer that makes GPU compute
    invisible in gen4 products. **Start here if you want to understand
    sovereign GPU latency and the warm/cold boundary.**

21. **SILICON_DEISM.md** — The abstraction elimination thesis. The
    evolution ladder: vendor agnostic → vendor atheistic → silicon deistic.
    There is only math, energy, and silicon — everything else is a
    temporary scaffolding. Rust→binary eliminates the CPU abstraction stack.
    WGSL→native ISA eliminates the GPU abstraction stack. VFIO eliminates
    the vendor driver. The sovereignty tier model (Tier 0–3) maps the
    remaining distance. **Start here if you want to understand the
    philosophical target of sovereign compute.**

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
