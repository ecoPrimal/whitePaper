# subGen — Primal Security & Intersystem Architecture

**Status**: Living documentation — evolves with primal implementations
**Scope**: Security systems, defense in depth, intersystem trust, and transport
security as they exist in deployed code. Not vision — realized architecture.

---

## Why subGen?

The generational arc tells a story of increasing abstraction:

- **gen4** asks "Who uses it?" — compositions, products, economics
- **gen5** asks "Does someone else's science come out?" — external
  collaboration, spore germination

Both treat security as *architectural context* — referenced, assumed, but
never the primary subject. Meanwhile, the security systems are live:

- Tower Atomic exceeds WireGuard (353× LAN, 1.7× WAN)
- Genetic enrollment deployed (mito gate + nuclear lineage → trust tiers)
- 7-category threat detection operational
- BTSP Phase 3 cipher negotiation with bond-type enforcement and cipher floor
- MethodGate RPC authorization across 13 primals
- Dark Forest validation suite (197 scenarios, all PASS)

**subGen** documents the realized security architecture — the substrate that
gen4 compositions and gen5 collaborator workflows depend on but don't describe.
These are living documents that evolve with the code, not frozen vision papers.

---

## Reading Order

### Layer 1 — Doctrine

1. **[DEFENSE_IN_DEPTH.md](DEFENSE_IN_DEPTH.md)** — The layered security
   model as implemented: network binding → transport encryption → RPC
   authorization → threat detection → behavioral baseline → quarantine →
   audit trail. How layers compose and where each enforces.

### Layer 2 — Transport & Trust

2. **[TOWER_ATOMIC_SECURITY.md](TOWER_ATOMIC_SECURITY.md)** — BTSP protocol
   specification as implemented: Phase 1–3 handshake, cipher negotiation,
   bond-type enforcement, cipher floor policy, session key derivation, wire
   format. The protocol that replaces WireGuard.

3. **[INTERSYSTEM_TRUST.md](INTERSYSTEM_TRUST.md)** — How primals discover,
   verify, and communicate: JSON-RPC 2.0 contracts, capability routing via
   songBird, genetic lineage verification via bearDog, covalent/metallic/ionic
   bond types, trust-on-first-use, and revocation.

### Layer 3 — Detection & Response

4. **[THREAT_DETECTION_ARCHITECTURE.md](THREAT_DETECTION_ARCHITECTURE.md)** —
   skunkBat's 7-category detection system: port scan, brute force, DDoS,
   data exfiltration, protocol violation, behavioral anomaly, process spawn
   anomaly. Statistical baseline, confidence scoring, graduated response.

### Layer 4 — Topology

5. **[MEMBRANE_SECURITY_MODEL.md](MEMBRANE_SECURITY_MODEL.md)** — K-Derm
   cell envelope mapped to network topology: inner membrane (LAN mesh),
   periplasmic space (golgiBody VPS), outer membrane (public surface).
   How security posture differs at each layer and how bonds traverse
   membrane boundaries.

---

## Relationship to Other Documentation

| Source | Role | Relationship |
|--------|------|--------------|
| gen4 `architecture/` | Vision | subGen documents what gen4 envisioned |
| gen5 `foundations/` | Forward design | subGen documents what gen5 assumes |
| Primal READMEs | Implementation notes | subGen explains the cross-cutting architecture |
| primalSpring scenarios | Validation | subGen describes what the scenarios test |
| wateringHole standards | Policy | subGen explains how standards are enforced |

## Cross-References

- gen4: `NUCLEUS_SOVEREIGNTY_ARCHITECTURE.md`, `SOVEREIGN_COMPOSITION_EVOLUTION.md`,
  `K_DERM_RECONCILIATION.md`, `CONTRACT_TESTING_THESIS_SKETCH.md`
- gen5: `COVALENT_MESH_TRUST_VALIDATION.md`, `RIBOCIPHER_SIGNAL_EVOLUTION.md`,
  `SOVEREIGNTY_SHADOW_EVOLUTION.md`, `TRANSPORT_EVOLUTION.md`
- specs: `skunkBat/specs/RECONNAISSANCE_SPEC.md`, `skunkBat/specs/BTSP_TRANSPORT_SPEC.md`
- live: `wateringHole/STANDARDS_AND_EXPECTATIONS.md`

---

*subGen Wave 150x: Initial corpus — 5 documents covering realized security
architecture from network layer through application layer.*
