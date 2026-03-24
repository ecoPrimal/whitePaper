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

---

*gen3 describes the parts. gen4 describes the assembly.*
