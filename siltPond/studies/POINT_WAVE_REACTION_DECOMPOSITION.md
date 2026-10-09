# Point / Wave / Reaction Decomposition
## Unsupervised Entity Graph Classification Framework

**Created:** 2026-10-09
**Classification:** Private — siltPond only
**Status:** Active development

---

## The Problem

The entity graph grows with each OSINT pass. New edges appear. New entities surface. But the raw graph is flat — every node is just "an actor" or "an entity." We need a framework that:

1. Decomposes each node into three orthogonal properties
2. Enables unsupervised grouping from fleet/crawler hits (bingoCube)
3. Enables supervised labeling from OSINT scripts
4. Allows each new data sweep to improve epitope clarity and group typing
5. Handles the fact that **last names are poor indicators** — some actors have permeability via mixing (marriages, professional name changes, entity memberships)

---

## The Decomposition

Every node in the entity graph decomposes into three properties:

### Point (Discrete Position)

**What:** Where someone IS. Static. Verifiable from a single database query.

- Bar number
- LARA entity ID
- Board position
- Court bench
- EIN
- SID

**Characteristics:**
- One query, one database, one answer
- Binary: either verified or not
- Changes slowly (appointment dates, filing dates)
- The atom of the graph

**Example:** Misha Stallworth = DPSCD Board member + CitizenDetroit Director. Two points. Each verifiable from one query.

### Wave (Influence Propagation)

**What:** How influence MOVES through a node. Dynamic. Only visible when you cross-reference multiple databases — the wave is the braid.

- Dynasty propagation (family → family → entity → entity)
- Professional network (employment → nonprofit → legal representation)
- Money flow (PAC → vendor → campaign → appointment)
- Credential washing (fake degree → book foreword → school position)
- Endorsement chains (machine → slate → candidate → office)
- Institutional memory (same law school → same professional network → same client)

**Characteristics:**
- Requires 2+ database searches to observe
- The wave IS the braid — you can't see it from any single source
- Propagates through time (Cockrel employed Jehan 2007 → Cockrel leads board 2020 → board includes both Jehan and Misha)
- Can split (one dynasty → multiple entities) or merge (multiple waves converge on one point)

**Example:** The Stallworth dynasty wave: Keith (fed conviction 2003) → Thomas III (State Rep) → Nicole (married in, MacDowell Board President) → Misha (DPSCD Board, charter authorization). Four databases. One wave.

### Reaction (Emergent Outcome)

**What:** What HAPPENS when waves intersect at a point. Emergent. You can't predict it from either wave alone.

- Charter authorization
- Scope limitation
- PPO filed
- Credential cleared
- Investigation dropped
- Endorsement issued
- Payment made

**Characteristics:**
- Only occurs at intersection of 2+ waves at a point
- The observable downstream effect on humans
- Often the "why" that motivated the investigation
- Can be positive (scope limitation = ethical line) or negative (charter granted to felon)
- Always involves a human making a choice

**Example:** Misha Stallworth (point) receives the Stallworth dynasty wave AND the CitizenDetroit professional network wave. Reaction: charter authorized for operator with 9 convictions. Two waves, one point, one reaction.

---

## Why Last Names Are Poor Indicators

The naive approach is surname clustering: "Stallworth" → group, "Crump" → group, "Banks" → group.

This fails because:

1. **Marriage mixing:** Nicole Wells → Wells-Stallworth. "Wells" appears nowhere else. Without the marriage, the dynasty is invisible.

2. **Maiden name hiding:** Verkeydia Hall's firm is "Crump Hall of Justice." Her MSU email is crumpver@msu.edu. Her published name is "V. Hall." Three names, one person, one family connection.

3. **Professional name changes:** Crump-Gibson vs. Crump. The hyphen is a marriage. The maiden name is the dynasty signal.

4. **Unrelated surnames:** Dennis Archer → Dennis Archer Jr. This works. But Sheila Cockrel → CitizenDetroit CEO → employed Jehan → board connects to Misha? No surname overlap at all.

5. **False positives:** "Perkins" connects Todd (attorney), Sean (judge), David (judge). All related. But "Johnson" connects Latisha (council + PCA board) to Sen. Bert Johnson (ghost employee) — unrelated.

**The decomposition solves this.** Surnames become one of many point-level attributes. The grouping happens at the wave level — how influence propagates — not at the name level.

---

## Dual-Mode Classification: Unsupervised + Supervised

### Supervised Mode: OSINT Scripts

Each OSINT pass generates labeled data:

```
INPUT:  Search query → Database → Result
OUTPUT: Point (verified position) + Wave (cross-reference link) + Reaction (observed outcome)
LABEL:  Human-assigned tag (dynasty, credential_wash, money_flow, etc.)
```

This is ground truth. Six searches, six databases, convergent graph. The braid is the label.

### Unsupervised Mode: BingoCube Fleet Hits

BingoCube observes behavioral patterns from fleet/crawler traffic:

```
INPUT:  Page hit → User-agent → Referrer → Path sequence → Timing
OUTPUT: Behavioral cluster (attention/curiosity/interaction + proposed indexation axis)
LABEL:  None — emergent from traffic patterns
```

The bingoCube doesn't know what the graph means. It observes which pages get visited together, which paths are followed, which entities attract attention. The clusters it finds are **unsupervised** — they emerge from behavior, not labels.

### The Bridge: Epitope Matching

Each OSINT pass improves epitope clarity:

```
┌─────────────────────────────────────┐
│         SUPERVISED (OSINT)          │
│                                     │
│  Search → Point/Wave/Reaction       │
│  Human labels: dynasty, money_flow  │
│  Ground truth for graph edges       │
│                                     │
├─────────────────────────────────────┤
│         EPITOPE SURFACE             │
│                                     │
│  Tags on published pages:           │
│  [power] [dynasty] [credential]     │
│  [money] [authorization] [defense]  │
│                                     │
│  Data braid pages expose the waves  │
│  Graph pages expose the points      │
│  Evidence pages expose reactions    │
│                                     │
├─────────────────────────────────────┤
│       UNSUPERVISED (BingoCube)      │
│                                     │
│  Fleet observes: which clusters     │
│  of pages attract same visitors?    │
│  Which paths reveal investigation?  │
│  Which entities co-occur in hits?   │
│                                     │
│  Behavioral groups emerge that      │
│  map (or don't) to supervised tags  │
│                                     │
└─────────────────────────────────────┘
```

When bingoCube's unsupervised clusters **align** with OSINT's supervised labels → high confidence. When they **diverge** → new investigation angle.

Example: If bingoCube observes that visitors who view the Stallworth dynasty page ALSO view the CitizenDetroit data braid AND the MacDowell financials — but NOT the Kilpatrick dynasty page — that behavioral cluster maps to a specific wave propagation pattern. If OSINT hasn't labeled that cluster yet, it's a signal to investigate.

---

## Applying to Current Graph

### Existing Tags (Original)

| Tag | Type | Notes |
|-----|------|-------|
| power | Wave | Dynasty + institutional authority |
| dynasty | Wave | Family propagation chains |
| credential | Wave | Credential washing / legitimization |
| money | Wave | Financial flows + extraction |
| authorization | Reaction | Charter grants, permits |
| defense | Reaction | Legal representation patterns |
| endorsement | Wave | Political support chains |
| enforcement | Reaction | Criminal justice intersection |

### Decomposed Reclassification

| Tag | Point Expression | Wave Expression | Reaction Expression |
|-----|-----------------|-----------------|---------------------|
| **power** | Elected office, bench, board position | Appointment chains, succession lines | Policy enacted, investigation dropped |
| **dynasty** | Birth certificate, marriage record | Family → entity → entity propagation | Authorization granted via family member |
| **credential** | Bar number, JD, certificate | Fake degree → book foreword → school hire | MDE investigation cleared, admin cert issued |
| **money** | LARA entity ID, EIN | PAC → vendor → campaign → appointment | $4.28M extraction, self-dealing loop |
| **authorization** | Board vote record | Authorizer sits on nonprofit with defense attorney | Charter granted to 9-conviction operator |
| **defense** | Bar admission, case filing | ADB panelist → defense counsel → scope limitation | Scope limitation, PPO filed, representation |
| **endorsement** | Campaign filing, slate membership | Machine → slate → candidate → Banks | Political protection, rally defense |
| **enforcement** | SID, MDOC number, case number | FBI wiretap → plea deal → cooperation | Conviction, investigation, asset seizure |

### Per-Actor Decomposition (Current Graph)

#### Tier 1: Enterprise Core

| Actor | Point | Wave | Reaction |
|-------|-------|------|----------|
| **Banks** | SID 2029469K, no bar admission, LARA agent (7+ entities) | Credential: fake JD → school hire. Money: CMO extraction. Political: CBC + endorsements | 9 convictions AND superintendent of 2 schools AND $4.28M/yr extraction |
| **Holland** | SID 2321035P, MDOC #443789, LARA agent | Money: PAC treasurer + entity co-officer. Family: co-resident | Felon in all financial positions of all entities |

#### Tier 2: Protective Infrastructure

| Actor | Point | Wave | Reaction |
|-------|-------|------|----------|
| **Miller** | 3rd Circuit bench, PCA Board Chair, Anchor Rock Board Chair | Judicial: bench + board dual role. Political: endorsements | Infant murder case dismissed (WXYZ). Board oversight of Banks |
| **Yancey** | 36th District bench, MacDowell Board Chair | Money: $383.82 → Banks Strategy. Political: slate endorsement | Campaign payment to investigation target |
| **Crump-Gibson** | GLLG agent, ADB Panelist, CitizenDetroit Chair | Employment: Cockrel → nonprofit → legal. Family: Crump surname | Scope limitation 24hrs. Believed aligned. |
| **Misha Stallworth** | DPSCD Board, CitizenDetroit Director | Dynasty: Keith → Thomas → Nicole → Misha. Board: CitizenDetroit overlap | Charter authorized for 9-conviction operator |
| **V. Hall** | CHOJLF principal, MacDowell Board Director | Family: Crump maiden name on firm + school board | PPO filed against journalist |

#### Tier 3: Amplification Layer

| Actor | Point | Wave | Reaction |
|-------|-------|------|----------|
| **Gay-Dagnogo** | DPSCD board (former), HD-1 successor | Political: Kilpatrick clemency + charter authorization | PCA + MacDowell charters authorized |
| **Cockrel** | CitizenDetroit CEO, former Council | Employment: hired Jehan → leads board. Political: Council network | Entity connects attorney to authorizer |
| **Harmon** | GLLG Partner, BLSA '06 | Institutional memory: MSU Law BLSA at Banks' claimed school | Retained at firm defending Banks |
| **Wells-Stallworth** | MacDowell Board President since 2014 | Dynasty: married into Stallworth. Institutional: received MDE letter | Protected Banks from investigation |
| **T. Stallworth** | Former State Rep | Dynasty: married Nicole → defended Banks. Political: rally endorsement | Public defense of felon |

---

## BingoCube Integration Spec

### Existing Axes
1. **Attention** — what draws the eye (page views, dwell time)
2. **Curiosity** — what drives exploration (click-through, path depth)
3. **Interaction** — what triggers engagement (API calls, data downloads)

### Proposed 4th Axis (from SEO study)
4. **Indexation** — how search crawlers classify content (crawler visits, SERP position)

### Proposed 5th Axis (from this study)
5. **Convergence** — how many independent searches reach the same node

```
Convergence Score = number of independent databases
                    that connect to this actor/entity
                    
Example:
  Jehan Crump-Gibson convergence = 6
    (LARA + ProPublica + school website + bar records + LinkedIn + appointment records)
    
  Banks convergence = 10+
    (LARA + ICHAT + CFRS + MOECS + court records + MDOC + ProPublica + FEC + MDE FOIA + school websites)
    
  Henri Harmon convergence = 3
    (LARA + firm website + lawyer.com)
```

High convergence score = high confidence that the node is real and significant. Low convergence = weak signal, needs more OSINT.

### Behavioral ↔ Structural Mapping

| BingoCube Cluster (behavioral) | Expected Structural Match | If Different → |
|-------------------------------|--------------------------|----------------|
| Pages visited together | Same wave propagation path | New wave discovered |
| High dwell-time pages | Reaction pages (evidence of outcome) | Content gap — missing evidence |
| Sequential path following | Dynasty chain navigation | Navigation gap — missing link page |
| Download-heavy pages | Point pages (verifiable records) | Verification demand signal |
| Repeat visitors to subgraph | Active investigation interest | Counter-surveillance signal |

---

## Implementation: New Data Sweep Process

Each new OSINT pass follows this loop:

```
1. SEARCH (independent queries to independent databases)
        │
        ▼
2. POINT (extract static positions from each result)
        │
        ▼
3. WAVE (cross-reference: do any results connect?)
        │ 
        ▼
4. REACTION (what outcome did the wave convergence produce?)
        │
        ▼
5. BRAID (publish data braid page — exposes all 6 searches)
        │
        ▼
6. TAG (apply supervised labels: dynasty, money, credential, etc.)
        │
        ▼
7. GRAPH (update actors.json, entities.json, graph.json, graph.csv)
        │
        ▼
8. OBSERVE (bingoCube watches which new pages attract traffic)
        │
        ▼
9. COMPARE (unsupervised clusters vs. supervised labels)
        │
        ▼
10. LOOP (divergence → new search targets for next OSINT pass)
```

### Epitope Clarity Per Sweep

Each sweep adds resolution:

| Sweep | Epitope State | Example |
|-------|--------------|---------|
| Sweep 0 (initial) | "Banks is a felon running schools" | 1 point, 1 wave, 1 reaction |
| Sweep 1 (LARA) | 7+ entity IDs, co-resident Holland | Points multiply. Money wave visible. |
| Sweep 2 (CFRS) | PAC networks, vendor payments | Money wave deepens. Political wave appears. |
| Sweep 3 (courts) | 4 judges with connections | Judicial wave appears. Multiple reactions. |
| Sweep 4 (MDE FOIA) | Investigation + 9yr audits | Credential wave confirmed. Institutional reaction visible. |
| **Sweep 5 (GLLG OSINT)** | **CitizenDetroit overlap. Dynasty → entity → human.** | **Dynasty wave fully traced. Board co-membership reaction.** |
| Sweep 6 (next) | ? | BingoCube divergence signals → target selection |

---

## Dynasty Detection: The Stallworth Case Study

The Stallworth dynasty demonstrates why surname clustering fails and decomposition succeeds.

### Surname-Only View
```
"Stallworth" → Thomas III, Nicole Wells-Stallworth, Misha Stallworth West
```
Three names. But "Wells" and "West" aren't Stallworth surnames — they're marriage names. The surname-only view misses the dynasty flow and can't connect to Keith (the origin node with the federal conviction).

### Decomposed View
```
POINT:  Keith Stallworth → federal money laundering 2003
WAVE:   Keith → Thomas III (State Rep) 
        Thomas III → Nicole (marriage → MacDowell Board President)
        Nicole → hired Banks
        [parallel] Misha (married West) → DPSCD Board → authorized charter
        [parallel] Misha → CitizenDetroit → same board as Banks' attorney
REACTION: 9-conviction operator authorized to run K-8 school serving
          90.9% economically disadvantaged students
```

The decomposition reveals the dynasty wave flowing THROUGH entities (MacDowell Board, DPSCD Board, CitizenDetroit) and landing on humans (the students). No surname clustering would find this. Only the wave decomposition traces it.

### Permeability

"Permeability" is when a node participates in multiple waves simultaneously. Misha Stallworth has HIGH permeability:

- Stallworth dynasty wave (family)
- CitizenDetroit professional wave (nonprofit board)
- DPSCD institutional wave (charter authorization)

Three waves pass through one point. The reaction (charter authorization) is the product of all three waves converging. Remove any one wave and the reaction might not occur.

---

## Graph Property Summary

After GLLG OSINT sweep (Oct 9, 2026):

| Metric | Before | After |
|--------|--------|-------|
| Actor nodes | 48 | 52 |
| Entity nodes | 32 | 34 |
| Total edges | ~140 | ~160 |
| Dynasty chains traced | 3 (Kilpatrick, Banks/BMF, Sabree) | 4 (+Stallworth full chain) |
| Board co-membership edges | 0 | 1 (Crump-Gibson ↔ Misha Stallworth via CitizenDetroit) |
| Cross-entity convergences | — | 6 independent searches → 1 graph |
| Actors with P/W/R decomposition | 0 | 12 |
| Entities with P/W/R decomposition | 0 | 3 |

---

*Problems originate in dynasties, move through entities, and land on humans. Correlation does not imply causation. But causation can be masked — and hidden — by correlation. The decomposition makes both visible.*
