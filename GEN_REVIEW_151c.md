# Generational Review — Wave 151c

**Date**: July 26, 2026
**Scope**: Full gen0–gen5 assessment, reprofiled toward Gonzales NF as gen5 JOSS proof case
**Trigger**: Publication strategy pivot — NF pipeline becomes live system JOSS submission

---

## Executive Summary

The whitePaper generational arc (gen0–gen5) is structurally sound. The Gonzales NF
drug discovery pipeline is correctly positioned as the gen5 proof case. However,
gen5's operational evidence is thin (no artifact delivered, no data ingested, no live
NF composition), and the JOSS publication path is entirely absent from the corpus.
The scientific spine (Anderson localization → QS → Fajgenbaum MATRIX → Gonzales G1-G6 →
NF extension) is well-documented in gen3/baseCamp but disconnected from gen3's main
methodology paper and thesis.

**Key finding**: gen5 has the conceptual framing but not the deliverables. The JOSS
paper will document a live system — that system requires Nest and Node Atomics to
function. This review establishes what exists, what's missing, and what must be built.

---

## Per-Generation Assessment

### gen0 — Origin Lore (8 files, ~47K)

| Dimension | Status |
|-----------|--------|
| Purpose | Timeless origin material — ethos, methodology, artisan witness |
| Gonzales/NF relevance | Conceptual only (sovereignty, knowledge commons) |
| README | Missing |
| Action needed | None — do not rewrite to center NF |

gen0 is correctly timeless. THE_SEED.md establishes the mission; GAIA_AWAKENING.md
frames emergence. No domain-specific content should be injected.

### gen1 — AI Swarm: "Can We Build It?" (6 files, ~212K)

| Dimension | Status |
|-----------|--------|
| Purpose | Hardware feasibility — $11K cluster, NestGate, Squirrel |
| Gonzales/NF relevance | Infrastructure lineage only (biomeGate ancestors) |
| README | Missing |
| Action needed | Optional historical footnote linking to gen5 |

The AI Swarm whitepaper proved sovereign HPC is feasible. NestGate and Squirrel are
direct ancestors of gen5 infrastructure. The cluster design now serves collaborator
science, but gen1 never anticipated that role.

### gen2 — Sovereignty Protocol: "What Should We Build?" (7 files, ~89K)

| Dimension | Status |
|-----------|--------|
| Purpose | Protocol definition — 8 primals, SOVEREIGN SCIENCE, AGPL trust |
| Gonzales/NF relevance | Strongest architectural alignment of gen0-2 |
| README | Missing |
| Action needed | Light cross-reference to gen5 as first SOVEREIGN SCIENCE instantiation |

gen2's SOVEREIGN SCIENCE concept maps directly to gen5: sweetGrass provenance →
compound lineage, Philosophy of Forgetting → session DAGs, biomeOS composition →
multi-product NF pipeline. The vocabulary gen5 uses originated here.

### gen3 — Constrained Evolution: "Does It Work?" (109 files)

| Dimension | Status |
|-----------|--------|
| Purpose | Scientific proof layer — methodology, validation, faculty network |
| baseCamp spine | Strong: Papers 01→06→12→13 anchor Anderson-QS-Fajgenbaum-Gonzales |
| Methodology disconnect | High: CONSTRAINED_EVOLUTION_FORMAL.md doesn't cite Papers 01/12/Fajgenbaum |
| Two Andersons | Rika Anderson (evolution, gen3 flagship) vs Philip Anderson (localization, baseCamp) |
| Gonzales profile | Missing from data/FACULTY_SPRING_PROFILES.md as standalone entry |
| Thesis coverage | No dedicated chapter for Paper 12 or drug discovery arc |
| NF/GPS | Absent — correctly lives in gen5 |

**Critical gap**: The Anderson-QS-Fajgenbaum chain that Gonzales NF runs on is
well-documented in baseCamp Paper 12 (782+ checks) but isolated from gen3's main
narrative. A reader following the thesis chapters encounters Rika Anderson
(population genomics) but never meets Philip Anderson (localization → QS → drug
repurposing) until baseCamp.

**Recommended**: Add a SCIENTIFIC_SPINE.md bridge document connecting baseCamp
01→06→12→13 to the main methodology, disambiguating the two Andersons. Do NOT
inject NF/GPS into gen3 — that is gen5 scope.

### gen4 — Composition & Deployment: "Who Uses It?" (55 files)

| Dimension | Status |
|-----------|--------|
| Purpose | Products from primals — esotericWebb, helixVision, initioChem, blueFish |
| GPS/tideGlass | Absent from product layer (zero references) |
| Fajgenbaum/MATRIX | Absent from gen4 (lives in springs, tideGlass scope) |
| lithoSpore product doc | Missing from products/ despite being a shipped artifact |
| Cross-product composition | Identified as gap in THE_GEN5_TRANSITION.md, unresolved |
| README | Exists but stale (wrong versions, phantom directories) |

**Critical gap**: tideGlass is the primary Gonzales deliverable but has no whitePaper
product documentation. It exists as implementation (`protists/tideGlass/`) and contact
prep (`attsi/.../gonzales/gps/`) but not as a gen4 product entry. This is the largest
documentation debt for the NF pipeline narrative.

### gen5 — External Science: "Does Someone Else's Science Come Out?" (32 files on disk)

| Dimension | Status |
|-----------|--------|
| Conceptual framing | Strong — NF is explicitly THE proof case |
| Gonzales NF docs | GONZALES_NF.md + NF_CASE_STUDY.md — detailed but divergent |
| tideGlass/NF split | NF_CASE_STUDY.md ignores tideGlass; GONZALES_NF.md makes it primary |
| JOSS publication | Absent — only SHOW_HN_PUBLICATION.md exists for dissemination |
| Missing files | 12 of 32 README-listed files don't exist on disk |
| Operational evidence | None — no data ingested, no pseudoSpore, no live composition |
| Status drift | README says Wave 139a; current is Wave 151c |

**Critical gaps**:
1. No JOSS thesis document (parallel to SHOW_HN_PUBLICATION.md)
2. tideGlass and NF product composition not reconciled
3. 12 missing planned files (journey docs, collaborator profiles)
4. Status frozen at Wave 139a

---

## Sibling Directories

### waterFall/ (11 files, Wave 66)

Architecturally current concepts, stale wave references. The SYNC domain of the
coordination triad. Production implementation in cellMembrane. `07_ROADMAP.md`
contradicts README (bash-only claims vs Rust production reality).

### RootPulse/ (16 files, Wave 66)

ACTION domain. Provenance trio composition graphs defined but `rootpulse` CLI not
implemented. Fossil subdirectory from gen4 era. Implementation status table stale.

### subGen/ (6 files, Wave 150x)

Most current sibling. Documents realized security architecture — BTSP, Tower Atomic,
genetic enrollment, 197 scenarios. Matches Wave 150 close-out.

### Terminology tension

GLOSSARY says rootPulse "replaces waterFall." waterFall/RootPulse/gen5 foundations
say they are complementary triad members (SYNC vs ACTION). This needs reconciliation.

### Wave 151c Currency Assessment

| Directory | Last Updated | Wave Ref | Currency |
|-----------|-------------|----------|----------|
| subGen | Jul 25, 2026 | 150x | HIGH — matches Tower Atomic close-out |
| waterFall | Jun 1, 2026 | 66+ | MEDIUM — concepts valid, wave refs stale |
| RootPulse | Jun 1, 2026 | 66 | MEDIUM — triad/trio vocab current, impl table stale |
| neuralAPI | May 14, 2026 | Phase 32 | LOW — pre-BTSP, pre-Tower Atomic |
| coralForge | Feb 28, 2026 | — | STABLE — science docs, not wave-tracked |

### How Coordination Patterns Map to NF Pipeline

| Pattern | NF Pipeline Use | Status |
|---------|-----------------|--------|
| waterFall SYNC | Cross-gate sync of NF data (eastGate ↔ flockGate) | Production |
| rootPulse ACTION | pseudoSpore provenance for NF analysis artifacts | Graphs defined, CLI pending |
| Neural API | Deploy graphs orchestrating multi-spring pipeline | Atomic signals unwired |
| Nest Atomic CAS | Storage for NF pseudoSpore outputs | LIVE membranes, BTSP pending |
| subGen security | BTSP-secured IPC between pipeline primals | 11/13 shipped |

### waterFall/RootPulse Verdict

These directories document architecturally current patterns with stale wave labels.
The concepts are correct and production-deployed (waterFall SYNC runs in cellMembrane).
The main debt is wave-reference refreshing and the GLOSSARY terminology reconciliation.
No structural changes needed for the NF pipeline — these are consumed indirectly
through biomeOS composition graphs and cellMembrane's temporal cascade engine.

---

## Nest Atomic Readiness for NF Pipeline

The Gonzales NF pipeline requires Nest Atomic for:
- CAS storage of pseudoSpore outputs (nestGate)
- DAG lineage for analysis artifacts (loamSpine)
- Ephemeral provenance (rhizoCrypt)
- Semantic attribution (sweetGrass)

**Current state**: Provenance trio membranes LIVE on cellMembrane VPS since Wave 38.
All four services running. loamSpine, rhizoCrypt, sweetGrass are BTSP-compliant (151c).

**Blocker**: nestGate BTSP ClientHello — last outstanding BTSP gap. Per-object
encryption and petalTongue StaticSite CAS serving depend on this.

---

## JOSS Publication Path

### What JOSS requires

| Requirement | gen5 state | Gap |
|-------------|-----------|-----|
| Focused software scope | 13-service mesh narrative | Need: single-system paper, not ecosystem whitepaper |
| Reproducible examples | groundSpring cold-clone works | wetSpring `nautilus` dep blocks public reproduction |
| Test coverage / CI | 14K+ checks; 197 primalSpring scenarios | Need: documented CI pipeline |
| Documentation | primals.eco Lab section | sporePrint needs CAS serving for evidence pages |
| Versioned release | Not done | crates.io releases required |
| Real-world usage | Gonzales NF = proof case | No artifact delivered yet |
| Statement of need | Implicit in NF_CASE_STUDY | No JOSS-format paper.md |

### Strategy: NF Pipeline as Live System Paper

The JOSS paper documents the live Gonzales NF pipeline — not a standalone crate.
This requires:
1. tideGlass as primary deliverable with reproducible validation
2. Tower Atomic transport as demonstrated infrastructure
3. Nest Atomic CAS for data storage and provenance
4. At least one NF pseudoSpore output
5. Andrea Gonzales as co-author (domain expertise)

### Dependencies

```
                   JOSS Paper
                      │
         ┌────────────┼────────────┐
         │            │            │
    tideGlass     Tower Atomic   Nest Atomic
    (GPS rebuild)  (COMPLETE)    (Phase 0 blocked)
         │                            │
    NF Data Portal              nestGate BTSP
    ingestion                   ClientHello
```

Tower Atomic is complete (353x LAN, 1.7x WAN). Nest Atomic Phase 0 is blocked on
nestGate BTSP ClientHello. tideGlass GPS rebuild is assigned but Phase 0 not started.
The JOSS paper is the end-goal motivator for Nest and Node Atomic development.

---

## Recommended Actions (Priority Order)

### P0 — Unblock JOSS Path

1. **Create gen5/thesis/JOSS_PUBLICATION.md** — parallel to SHOW_HN, documenting the
   JOSS strategy with Gonzales NF as the live system paper
2. **Reconcile tideGlass + NF** in NF_CASE_STUDY.md — tideGlass is Thread 0 (primary),
   multi-product composition is Thread 1
3. **Update gen5/README.md** — Wave 151c, add missing files to tree, JOSS as
   dissemination track

### P1 — Strengthen Scientific Spine

4. **gen3: SCIENTIFIC_SPINE.md** — bridge baseCamp 01→06→12→13 to main methodology,
   disambiguate Rika vs Philip Anderson
5. **gen3: Gonzales faculty profile** in data/FACULTY_SPRING_PROFILES.md
6. **gen4: tideGlass product entry** — even a stub linking to protists/tideGlass/
   and attsi/.../gonzales/gps/

### P2 — Documentation Debt

7. **gen5: Update wave reference** throughout (139a → 151c)
8. **waterFall/RootPulse: reconcile terminology** with GLOSSARY
9. **gen0-gen2: Add READMEs** with forward pointers to gen5

### P3 — Operational (required for JOSS submission, not for planning)

10. **nestGate BTSP ClientHello** — Phase 0 blocker
11. **tideGlass Phase 0** — GPS reproduction begins
12. **crates.io releases** — versioned artifacts for citation
13. **NF Data Portal ingestion** — first external data
