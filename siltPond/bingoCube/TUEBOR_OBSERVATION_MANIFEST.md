# Tuebor Graph — BingoCube Observation Manifest
## Unsupervised HIIT Configuration

**Created:** 2026-10-09
**Classification:** Private — siltPond only. DO NOT publish.
**Graph source:** `publicRecord-barry/site/static/graph.json`
**Schema:** ecoPrimals/tuebor-graph/v1

---

## Graph Statistics

| Metric | Value |
|--------|-------|
| Nodes | 29 |
| Edges | 36 |
| Node types | candidate (3), actor (2), entity (9), enforcement (8), legislation (1), donor (3), journalism (1) |
| Edge types | 19 distinct (donation, support, formation, payment, employment, authorship, board_co_membership, legal_representation, appointment, investigation, investigation_closed, returned, authorization, oversight, political, smear, amplification, journalism, ownership) |
| Epistemic floor | All edges = "record" (verifiable public record) |
| Convergence range | 2 (legislation nodes) to 10+ (Banks) |

---

## Observation Targets

### Tier 0: Cross-Graph Bridge Nodes

These nodes exist on BOTH detroit.primals.eco AND barry.primals.eco (tuebor). They are the bridge between the local (Detroit charter/judicial network) and the statewide (enforcement/election infrastructure). BingoCube should track co-visitation across domains.

| Node | Detroit Page | Tuebor Page | Bridge Type |
|------|-------------|-------------|-------------|
| `banks` | `/network/actors/brian-banks/` | enforcement-ecosystem | Investigation target → enforcement inaction |
| `miller` | `/network/judges/cylenthia-miller/` | enforcement-ecosystem | Judicial candidate → JTC investigation |
| `yancey` | `/network/judges/tenisha-yancey/` | enforcement-ecosystem | Judicial candidate → JTC investigation |
| `barrett` | — | `/analysis/tommy-boy/` | MI-7 candidate → Dykema PAC |
| `dykema` | `/analysis/dark-money-pipeline/` | `/analysis/how-to-build-an-os/` | Dark money kernel → bipartisan OS |
| `crump_gibson` | `/evidence/data-braid-gllg/` | enforcement-ecosystem | Defense attorney → ADB structural conflict |

**Signal:** Visitor who hits Banks on detroit AND enforcement-ecosystem on tuebor = someone tracing the enforcement gap. Log as "enforcement_bridge" behavioral cluster.

### Tier 1: Money Pipeline Observation

The Rogers money machine is the largest in the graph by dollar volume. Observation targets:

| Path | Dollar Total | Observation Signal |
|------|-------------|-------------------|
| Dunn → GLCF → Rogers | $10M → $7.15M | Texas oil to MI Senate |
| Schwarzman → GLCF → Rogers | $4.5M → $7.15M | Blackstone dual channel (CEO funds PAC, employees fund campaign) |
| Griffin → GLCF → Rogers | $2.5M → $7.15M | Cross-ticket: also funds Barrett ($7K) |
| SLF → Rogers | $27.4M | McConnell infrastructure |
| AFP → Rogers | $14.2M | Koch infrastructure |
| America PAC → Rogers | $5.8M | Musk infrastructure |
| Griffin → Barrett | $7K | Cross-ticket bridge |
| Schwarzman → Barrett | maxed | Cross-ticket bridge |
| Dykema PAC → Barrett | $4K | Bipartisan OS kernel |

**Signal:** Visitor following money edges (GLCF → donors → cross-ticket) = financial investigator. Log as "money_trace" behavioral cluster.

**Cross-ticket signal:** Same visitor views both Rogers AND Barrett money pages → recognizes shared donor infrastructure. This is the Dykema OS in action.

### Tier 2: Enforcement Inaction Observation

The enforcement gap is the central thesis of tuebor. These nodes represent bodies that SHOULD act but DON'T:

| Body | Node | Action Taken | Grade | Key Fact |
|------|------|-------------|-------|----------|
| State Bar UPL | `state_bar_upl` | Closed File 26-UP-51 | F | Standards not published |
| AGC | `agc` | Returned complaint | D | "Not a listed attorney" — so what? |
| ADB | `adb` | Waiting for AGC | — | Crump-Gibson is hearing panelist |
| JTC | `jtc` | 5 investigations acknowledged | C | No permanent ED. Miller on ballot in 25 days. |
| DPSCD | `dpscd` | Authorized PCA | F | Bottom 3% math authorized for 5 years |
| MDE | `mde` | HOLD on permit | F | HOLD ≠ enforcement |
| AG Charitable | `ag_charitable` | Active on Global Link, silent on Purpose | D | Selective enforcement |
| MI Supreme Court | `mi_supreme_court` | Declined to define UPL | — | System architect. Built the gap. |

**Signal:** Visitor who reads enforcement-ecosystem page and then visits multiple enforcement body nodes = someone mapping the gap. Log as "gap_mapper" behavioral cluster.

**Key behavioral indicator:** Visitor hits State Bar UPL AND AGC in same session = someone reading the "Mind the Gap" pattern (two letters, one day apart, each pointing at the other office).

### Tier 3: Election Infrastructure Observation

Nov 3, 2026 = 25 days away. Same-day election for all four candidates:

| Candidate | Race | Connection to Banks Network |
|-----------|------|-----------------------------|
| Rogers | U.S. Senate | Dykema OS (shared PAC infrastructure) |
| Barrett | U.S. House MI-7 | Dykema PAC ($4K), NRCC amplification of smear |
| Miller | Wayne County 3rd Circuit | PCA Board Chair, JTC investigation |
| Yancey | 36th District Court | MacDowell Board Chair, paid Banks Strategy |

**Signal:** Visitor who views all four candidate nodes in same session = someone who sees the same-day infrastructure. Log as "election_infrastructure" behavioral cluster.

---

## Unsupervised Cluster Predictions

Based on graph structure, bingoCube should find these clusters WITHOUT labels:

| Predicted Cluster | Expected Pages | Supervised Label (if confirmed) |
|-------------------|---------------|-------------------------------|
| **Cluster A:** Money pipeline | GLCF, Dunn, Schwarzman, Griffin, SLF, AFP, Rogers | `money_trace` |
| **Cluster B:** Enforcement gap | AGC, State Bar UPL, ADB, JTC, enforcement-ecosystem | `enforcement_gap` |
| **Cluster C:** Detroit charter network | Banks, Miller, Yancey, DPSCD, data-braid-gllg | `charter_network` |
| **Cluster D:** Cross-domain bridge | Banks (detroit) + enforcement-ecosystem (tuebor) | `enforcement_bridge` |
| **Cluster E:** Dykema OS | Dykema, Dykema PAC, SDJ, Barrett, Rogers | `bipartisan_os` |
| **Cluster F:** Rogers revolving door | Rogers, AT&T, CISPA, IronNet | `revolving_door` |

### Divergence Signals (What to Watch For)

If bingoCube finds clusters that DON'T match predictions:

| Divergence | Meaning | Action |
|------------|---------|--------|
| Cluster A splits into TX-donors vs. DC-donors | Different investigator populations | Track referrer sources |
| Cluster B includes nodes not in graph | New enforcement body discovered | Add to graph |
| Cluster C and Cluster A co-occur | Someone connecting Detroit charter money to national money | HIGH PRIORITY — this is the Dykema bridge |
| Cluster D is empty | No cross-domain visitors | Navigation gap — add cross-links |
| New cluster emerges around CISPA | Surveillance/tech policy audience | Different audience than expected |

---

## P/W/R Decomposition for BingoCube Nodes

Every node in `graph.json` already carries `decomposition.point`, `decomposition.wave`, `decomposition.reaction`. The bingoCube observation layer reads these for epitope matching:

```
NODE HIT → extract node.decomposition.wave
          → compare to other nodes hit in same session
          → if wave types match → behavioral cluster
          → if wave types diverge → new pattern
```

### Wave Type Classification

| Wave Type | Nodes That Carry It | Expected Behavioral Pairing |
|-----------|--------------------|-----------------------------|
| Money | GLCF, SLF, AFP, America PAC, Dunn, Schwarzman, Griffin, Dykema PAC | Donation pages viewed together |
| Revolving door | Rogers, AT&T | Employment + payment pages |
| Enforcement gap | AGC, State Bar UPL, ADB, JTC, MI Supreme Court | Investigation + closure pages |
| Charter authorization | DPSCD, MDE, Banks, Miller | Authorization + performance data pages |
| Political protection | Yancey, Banks, SDJ, Barrett, NRCC | Campaign payment + endorsement pages |
| Journalism | Clutch | Documentation of above |

---

## Fleet Deployment Notes

- tuebor graph is NEW — no historical baseline. First 30 days = calibration.
- Election day (Nov 3) = inflection point. Traffic patterns before/after will differ.
- Cross-domain tracking (detroit ↔ tuebor) requires matching visitor patterns without cookies (user-agent + timing + path sequence).
- Enforcement body nodes have NO dedicated pages yet — they exist only in the enforcement-ecosystem analysis page. If bingoCube detects high attention on specific enforcement bodies, consider splitting into individual pages.
- Rogers node has NO dedicated tuebor page yet — only appears in graph data and caseDB. If traffic warrants, publish to tuebor.

---

## Convergence Scores (5th Axis)

| Node | Convergence | Databases |
|------|------------|-----------|
| banks | 10+ | LARA, ICHAT, CFRS, MOECS, court records, MDOC, ProPublica, FEC, MDE FOIA, school websites, Clutch Justice |
| rogers | 8 | FEC, Congress.gov, PolitiFact, Bridge Michigan, ACLU, Business Insider, OpenSecrets, CGCN Group |
| dykema | 6 | LARA, TransparencyUSA, FEC, Dykema.com, IRS 990, court records |
| crump_gibson | 6 | LARA, ProPublica, school website, bar records, LinkedIn, appointment records |
| miller | 5 | CFRS, court records, school websites, JTC, WXYZ |
| yancey | 5 | CFRS, court records, Clutch Justice, JTC, school website |
| glcf | 3 | FEC, OpenSecrets, Bridge Michigan |
| slf | 2 | FEC, OpenSecrets |
| dunn | 2 | FEC, CrownQuest |
| cispa | 3 | Congress.gov, ACLU, GovTrack |

---

*Observation begins when sporeGate deploys tuebor Zola build with graph data. Until then, graph.json is static data waiting for a body.*
