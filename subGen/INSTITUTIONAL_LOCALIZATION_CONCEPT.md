# Institutional Localization — Anderson Localization, Graph Theory, and Quorum Sensing Applied to Institutional Capture Detection

**Working title.** Inception tagline: *"The signal was sent. The lattice ate it."*

**Parent framework:** K-NOME (constrained optimization methodology)
**Bridges:** ecoPrimals (computational science) → guerillaGorilla (legal existence)
**Scientific foundation:** baseCamp Papers 01, 06, 12 (Anderson localization); wetSpring (quorum sensing); sweetGrass (attribution network / graph)
**Domain application:** Institutional capture as emergent property of network disorder
**Live validation:** Banks/Smith — bluegate-tenancy, caseDB (69 entities, 114 graph edges)
**Wave:** 1 legal-primal | **Date:** Oct 2, 2026

---

## THE BRIDGE

This is the first subGen concept that flows BACKWARD — from the scientific
primals into the legal primal, rather than from the legal domain outward
into generalization.

fEAR emerged in guerillaGorilla and was abstracted into subGen because it
generalized. STRIDe emerged the same way. Pursuit Predation likewise.
Confession Architecture likewise.

Institutional Localization is different. It begins in wetSpring (Exp107–356),
baseCamp Paper 01 (198 experiments), and Paper 06 (321 checks) — validated
physics and microbiology. It then APPLIES to the legal domain, providing the
mathematical framework that explains why institutional oversight fails, how
captured networks are structured, and when those networks will fragment.

The directionality matters. This concept proves that the ecoPrimals ecosystem
is not merely analogous to the legal domain — it is mathematically isomorphic
at the framework level. The same optimization structures that explain microbial
community behavior explain institutional network behavior.

This is the K-NOME thesis made concrete: constrained optimization methodology
does not belong to any single domain. It bridges them.

---

## THE NAME

**Institutional Localization** operates on three layers:

**Localization** (physics) — Anderson localization is the phenomenon in which
waves in a disordered medium cease to propagate. Energy injected into the
system does not spread — it localizes around the injection point. The wave
function decays exponentially with distance from the source. In a perfectly
ordered lattice, a signal travels from any point to any other point. In a
sufficiently disordered lattice, the signal stays where it started and dies.

**Institutional** (domain) — The lattice is the institutional oversight network.
The signals are oversight mechanisms: FOIA requests, ethics complaints,
disciplinary referrals, audit findings, investigative journalism, mandatory
reporter obligations. The disorder sites are nodes where conflicting roles
create functional opacity — individuals who simultaneously serve on oversight
bodies and the entities being overseen.

**Institutional Localization** (combined) — The phenomenon in which oversight
signals sent into a captured institutional network fail to propagate to the
point of enforcement. The signal was real. The mechanism was real. The lattice
absorbed it.

---

## PART I: GRAPH THEORY — THE LATTICE

### The Network as Graph

Any institutional network can be modeled as a typed directed graph:

```
G = (V, E, τ_v, τ_e, t)

V = {entities}           — people, organizations, courts, agencies
E = {relationships}      — board seats, employment, counsel, judicial assignment
τ_v: V → EntityType      — individual, school, court, agency, nonprofit, LLC
τ_e: E → RelationType    — employs, advises, oversees, authorizes, funds, adjudicates
t: E → TimeInterval      — when the relationship was active (from evidence source)
```

This is not novel graph theory. It is the same typed graph used in:
- sweetGrass (attribution networks in ecoPrimals)
- Biological regulatory networks (gene regulation, metabolic pathways)
- Social network analysis (Barabási, Watts-Strogatz)
- Financial fraud detection (FinCEN suspicious activity networks)

The caseDB for the Banks/Smith validation case instantiates this graph:
69 entities, 76 typed relationships, 114 directed edges, temporal properties
on every edge, evidence source citations on every node.

### Centrality as Capture Indicator

Three standard graph centrality measures identify structural capture:

**Betweenness centrality** — C_B(v) = Σ_{s≠v≠t} [σ_st(v) / σ_st]

Nodes with high betweenness control information flow between otherwise
disconnected subgraphs. In ecology, these are keystone species — their removal
causes community collapse. In microbial ecology, high-betweenness organisms
mediate metabolic handoffs that the entire community depends on (Paper 05:
cross-species signaling, 299K QS genes across 170 metagenomes).

In institutional networks, high-betweenness nodes are individuals who connect
the oversight apparatus to the entities being overseen. They sit on the boards
of BOTH the regulator and the regulated. They serve as counsel for BOTH the
court and the litigant. They authorize the charter AND occupy the oversight
body that reviews charter performance.

**Validation (Banks/Smith):** The institutional capture map at detroit.primals.eco
identifies the following high-betweenness nodes:
- Moreland (AAG for school oversight AND PCA board vice chair)
- Gay-Dagnogo (DPSCD authorizer AND Detroit Ombudsman, 10-year term)
- Sabree family (County Treasurer AND judicial bench AND counsel for development)
- Banks (school operator AND campaign contributor AND board member AND BMF lineage)

Each of these nodes sits at the intersection of subgraphs that should be
independent (oversight ↔ operations). Their presence on both sides of the
oversight boundary is the structural disorder that Anderson localization
predicts will block signal propagation.

**Degree distribution** — P(k) ~ k^(-γ)

The degree distribution of a network reveals whether it grew organically
(Erdős-Rényi random graph: Poisson-distributed degrees) or through
preferential attachment (Barabási-Albert scale-free network: power-law
distributed degrees with hubs).

Organic institutional networks — cities, counties, school districts that
grew from democratic processes — should exhibit roughly Poisson degree
distributions. Each node connects to a similar number of other nodes
because the connections are role-based, not relationship-based.

Captured institutional networks exhibit power-law degree distributions
with identifiable hubs. A small number of nodes have far more connections
than role alone would predict. These hubs are the capture infrastructure.

**Validation:** In the Banks/Smith graph, Banks has connections to:
schools (2), LLCs (3+), foundations (1), campaign committees (2+),
board seats (multiple), judicial actors (through shared counsel),
family network (BMF lineage), and political apparatus (Stallworth,
Ellis, Gay-Dagnogo). This degree is incompatible with a random graph
model where a school principal connects to school + employer + family.
The excess degree is the structural signature of a hub node in a
scale-free capture network.

**Clustering coefficient** — C_i = 2|{e_jk}| / [k_i(k_i - 1)]

High local clustering indicates clique structure — subgroups where
everyone knows everyone. In ecological terms, this is a tightly-coupled
microbial consortium. In institutional terms, this is a board where
the same 8 people rotate through 12 positions.

High global clustering with low average path length = "small-world"
network (Watts-Strogatz). The institutional capture network exhibits
small-world properties: any two actors can reach each other through
1–2 intermediaries, while local cliques (board overlaps) maintain
dense internal connections.

### Graph Theory Summary

The institutional network is a typed, directed, temporal graph.
Standard centrality measures identify capture nodes.
Degree distribution distinguishes organic from constructed networks.
Clustering reveals the clique structure of board rotation.

None of this requires intent. Graph theory describes structure.
The structure may or may not have been designed. The math does not
care. It measures what IS, not why.

---

## PART II: ANDERSON LOCALIZATION — WHY SIGNALS DIE

### The Physics

In 1958, Philip W. Anderson published "Absence of Diffusion in Certain
Random Lattices" (Physical Review, 109(5), 1492–1505). The key finding:
sufficiently disordered lattices prevent wave propagation. Electrons
injected into a disordered crystal do not diffuse — they localize.
The wave function decays exponentially:

```
|ψ(r)| ~ exp(-|r - r_0| / ξ)

where:
  ψ(r) = wave amplitude at position r
  r_0  = injection point
  ξ    = localization length (depends on disorder strength W)
```

The critical disorder parameter W_c defines the phase transition:
- W < W_c: waves propagate (extended states). The lattice is a conductor.
- W > W_c: waves localize (localized states). The lattice is an insulator.

Anderson received the Nobel Prize in Physics (1977) for this work.

### ecoPrimals Validation

baseCamp Paper 01: "Anderson Localization as QS Null Hypothesis"
198 experiments. Full three-tier validation + cross-environment.

**Key finding:** 3D geometry is necessary and sufficient for quorum
sensing (QS) in diverse microbial communities. The Anderson disorder
parameter W maps to microbial community diversity — when diversity
(species richness, functional redundancy) exceeds a critical threshold,
quorum sensing signals cannot propagate through the community. The
bacteria are present. The autoinducers are produced. But the signals
localize — they do not reach enough cells to trigger collective behavior.

**Quantified:** W_c = 16.26 ± 0.95 (critical disorder for QS collapse)

**V110 refinement (Exp356):** Disorder is two-dimensional: diversity
AND oxygen. W = 3.5·H' + 8·O₂ (r = 0.851). Oxygen modulates the
Anderson disorder parameter, creating a second axis along which
localization can occur.

baseCamp Paper 06: "Anderson Localization as the Mechanism Behind
No-Till Soil Health"
Track 4: 321 checks, 9 papers, full three-tier.

**Key finding:** Tillage = dimensional collapse of the QS-active 3D
pore network. Soil aggregates maintain the 3D geometry required for
QS propagation. Tillage destroys aggregates, collapsing the network
to 2D. In 2D, Anderson localization occurs at ANY disorder level
(all states are localized in 2D for W > 0). This explains why tilled
soil loses microbial coordination capacity even when microbial
populations remain numerically intact.

baseCamp Paper 12: "Anderson Localization in Immunological Signaling"
359/359 experiments. Cytokine propagation through inflamed skin
tissue follows Anderson localization. Atopic dermatitis barrier
disruption = dimensional promotion (inverse of Paper 06).

### The Institutional Analog

Replace the lattice with the institutional oversight network.
Replace the wave with the oversight signal.
Replace disorder sites with dual-role nodes.

**The lattice:** Government agencies, courts, boards, nonprofits,
schools, regulatory bodies — connected by formal and informal
relationships. This is the graph from Part I.

**The wave:** An oversight signal — a FOIA request, an ethics complaint,
a mandatory reporter obligation, an audit finding, an investigative
reporter's inquiry. Each of these is a signal that must propagate FROM
a source (the complainant, the auditor, the reporter) THROUGH the
institutional lattice TO a point of enforcement (a prosecutor, a
judge, a disciplinary board, a licensing authority).

**The disorder sites:** Nodes where an individual occupies roles on
BOTH sides of the oversight boundary:

| Disorder Site | Oversight Role | Operations Role | Effect |
|---|---|---|---|
| Moreland | Asst. Attorney General (school oversight) | PCA Board Vice Chair | AG oversight signal cannot propagate through this node — the node IS the school |
| Gay-Dagnogo | Detroit Ombudsman (oversight, 10-yr term) | DPSCD authorizer of PCA's charter | Ombudsman oversight signal cannot propagate — the authorizer IS the overseer |
| Sabree (Eric) | Wayne County Treasurer (public trust) | Family controls foreclosure pipeline | Fiscal oversight signal cannot propagate — the treasury IS the pipeline |
| Miller | Wayne 3rd Circuit Judge (judicial oversight) | Gun at DTW, dismissed infant murder case | Judicial integrity signal cannot propagate through compromised bench |
| Perkins | Attorney (officer of the court) | Counsel for Banks AND Judge Miller simultaneously | Attorney ethics signal cannot propagate — shared counsel bridges entities that should be adversarial |

Each of these is a disorder site in the Anderson model. The disorder
is not corruption in the conspiratorial sense — it is the simultaneous
occupation of roles that should be independent. The wave (oversight
signal) encounters the disordered node and cannot determine which
role to route through. The signal scatters. Over sufficient disorder
sites, the signal localizes and dies.

### The Critical Threshold

In Anderson's original model, there exists a critical disorder
strength W_c above which ALL states are localized. Below W_c,
some signals propagate (the system is a partial conductor). Above
W_c, no signals propagate (the system is an insulator).

**Hypothesis:** Institutional capture networks exhibit a similar
phase transition. A small number of dual-role nodes can be tolerated —
the system remains partially functional, some oversight signals get
through, some complaints result in action. But when the number of
dual-role nodes exceeds a critical density, the system undergoes a
localization transition: NO oversight signals propagate successfully.
The system appears intact (agencies exist, courts sit, boards meet)
but is functionally opaque.

**Observable prediction:** In a localized institutional network,
the following should be simultaneously true:
1. Oversight mechanisms exist (FOIA, ethics boards, mandatory reporting)
2. Complaints are filed through those mechanisms
3. Complaints do not result in enforcement action
4. The non-enforcement is not due to lack of merit but due to
   structural routing failure — the signal never reaches a node
   capable of acting on it

**Validation (Banks/Smith):** Kevin Mok has filed complaints with:
- MDE (acknowledged Oct 1 — routing in progress)
- FBI (Sep 21–25 — no response to date)
- USPS OIG (3 cases opened — investigation ongoing)
- DPD (Sep 9 — report taken, no follow-up)
- GPW PD (Sep 28 — report taken, follow-up call only)
- State Attorney General (via network — Moreland IS the AG's office AND the board)

The AG pathway is the clearest localization example: a complaint about
PCA board governance must propagate through the AG's office, but the
AG's office (Moreland) IS on the PCA board. The signal encounters the
disorder site and has no propagation path. The complaint is not
rejected — it localizes. It sits in the lattice, decaying exponentially
with distance from the source.

### Dimensional Analysis

Paper 06 established: in 2D lattices, ALL states are localized for
any disorder W > 0. Only 3D lattices support a finite W_c where
some signals propagate.

Institutional analog: a "2D" institutional network is one where
oversight and operations exist on the same plane — the same people
rotate between regulating and being regulated. There is no
independent dimension separating oversight from operations.

A "3D" institutional network has structural separation between
oversight and operations — independent inspectors general, judges
with no connections to litigants, auditors who do not serve on
the boards they audit. The third dimension IS independence.

**Prediction:** Institutional localization is total (all signals
die) when the oversight network is effectively 2D — when the same
people occupy both dimensions. This is the board rotation pattern:
the same 8 people serve on 12 boards, rotating between oversight
and operations. The lattice has collapsed to 2D. Localization is
complete.

**Restoration prediction:** The way to restore signal propagation
is dimensional promotion — introduce genuinely independent nodes
that restore the third dimension. External federal investigators
(FBI, DOE-OIG, IRS-CI) are the dimensional promotion. They sit
OUTSIDE the local lattice entirely. The oversight signal does not
need to propagate through local disorder sites — it bypasses the
lattice through an independent dimension.

This is why federal referral was the structurally necessary action,
not a strategic choice. Local oversight mechanisms had undergone
localization. Only dimensional promotion (external jurisdiction)
could restore signal propagation.

---

## PART III: QUORUM SENSING — WHEN NETWORKS DECIDE

### The Biology

Quorum sensing (QS) is the mechanism by which unicellular organisms
coordinate collective behavior without a central nervous system.

```
Individual cell:
  1. Produces autoinducer (AI) at constant rate
  2. Detects ambient AI concentration
  3. When [AI] > threshold: activates QS regulon
     → gene expression changes
     → collective behavior activates

Population:
  - Low density → low [AI] → individual behavior
  - High density → high [AI] → collective behavior
  - Threshold crossing = quorum reached
  - No individual cell "decides" — the decision is emergent
```

Collective behaviors triggered by QS:
- **Biofilm formation** (consolidation — protective matrix)
- **Virulence factor activation** (collective attack)
- **Sporulation** (individual survival — abandon the collective)
- **Bioluminescence** (signaling — collective visibility)

The key insight: WHICH collective behavior activates depends on
the signal identity, not just the concentration. Different
autoinducers trigger different programs. The same threshold
crossing can produce consolidation OR fragmentation depending
on which signal dominates.

### ecoPrimals Validation

wetSpring: 120+ versions, cross-spring validated.
Paper 01: QS signal propagation follows Anderson model.
Paper 05: Cross-species QS in symbiotic systems — 299K QS genes
across 170 metagenomes confirm mixed-community signaling.
Paper 16: Anaerobic-aerobic QS phase transition — oxygen modulates
quorum threshold.

### The Institutional Analog

Replace bacterial cells with network actors (individuals in an
institutional capture network).
Replace autoinducers with behavioral signals (filing delays, asset
transfers, attorney consultations, behavioral changes, communications).
Replace the quorum threshold with the coordination/fragmentation
decision point.

**Institutional quorum sensing:**

```
Individual actor:
  1. Produces behavioral signals at variable rate
     (filings, communications, asset movements, silences)
  2. Detects ambient signal concentration from the network
     (are others cooperating? are others retaining counsel?
      are others responding to complaints? are others going quiet?)
  3. When perceived network state crosses threshold:
     → behavior changes
     → either consolidation or fragmentation

Network:
  - Low pressure → low signal concentration → individual behavior
    (each actor operates independently, no coordination)
  - High pressure → high signal concentration → collective behavior
    (actors either coordinate defense or individually defect)
  - Threshold crossing = network decision point
  - No individual actor "decides" for the network — emergent
```

### Consolidation vs. Fragmentation

The network-level decision has two attractor states:

**Biofilm (consolidation):**
- Actors coordinate defense
- Shared counsel retained
- Unified narrative constructed
- Resources pooled
- Analogous to: bacterial biofilm — protective matrix, collective
  resistance to antibiotics (here: resistance to legal pressure)
- **Detectable by:** coordinated filings, joint responses, shared
  counsel appearing for multiple defendants, consistent narrative
  across actors, simultaneous behavioral changes

**Sporulation (fragmentation):**
- Individual actors defect from the collective
- Separate counsel retained (or no counsel)
- Inconsistent or absent narratives
- Self-protective behavior (asset transfers, silence, distancing)
- Analogous to: sporulation — individual cells forming protective
  spores and abandoning the collective
- **Detectable by:** silence, independent attorney retention, lack
  of coordinated response, asset movements, behavioral divergence
  across actors who previously acted in concert

### Validation (Banks/Smith) — Real-Time Quorum Detection

**Signal inventory (Sep 22 – Oct 2, 2026):**

| Actor | Signal | Type | Date |
|---|---|---|---|
| Smiths (all 4) | Complete silence since service | Absence of signal | Sep 22 – present |
| Banks | Retained independent counsel (GLLG) | Individual defense | ~Sep 29 |
| Banks | Filed retaliatory police report #1 (DPD) | Individual aggression | Sep 9 |
| Banks | Filed retaliatory police report #2 (GPW) | Individual aggression | Sep 28 |
| Banks | Appeared at PPO hearing (no standing) | Individual overreach | Sep 29 |
| Crump-Gibson | Disclaimed non-civil matters in writing | Scope limitation | Oct 1 |
| Moreland | No visible response to complaints | Silence / localization | Sep 22 – present |
| Perkins | No visible response | Silence | Sep 22 – present |
| Gay-Dagnogo | No visible response | Silence | Sep 22 – present |

**Assessment:** The signal pattern is consistent with **sporulation
(fragmentation)**, not biofilm (consolidation):

1. **No coordinated response.** The Smiths are silent. Banks acted
   alone (retained his own counsel, filed his own police reports,
   appeared at PPO without coordination). No joint filing. No unified
   narrative. No shared counsel for the network.

2. **Scope limitation from counsel.** Crump-Gibson's written
   disclaimer (Oct 1: "I am NOT retained for law enforcement matters,
   police reports, or PPO proceedings") is a sporulation signal —
   the defense attorney is forming a protective spore around a
   narrow scope and abandoning the rest.

3. **Institutional silence.** Moreland, Perkins, Gay-Dagnogo — the
   institutional nodes — have produced zero visible signal. In
   quorum sensing terms: the institutional cells have stopped
   producing autoinducers. They are going dormant. This is pre-
   sporulation behavior — reducing signal production to avoid
   triggering collective detection.

4. **Individual aggression without collective backing.** Banks's
   police reports and PPO appearance are individual-cell behaviors,
   not collective-network behaviors. He is acting alone, escalating
   alone, and generating evidence alone. In a biofilm response, the
   network would have produced a coordinated counter-narrative through
   institutional channels. Instead, one cell is thrashing while the
   rest go quiet.

**Quorum diagnosis:** The adversary network has crossed the
fragmentation threshold. The autoinducer concentration (collective
coordination signal) has dropped below the quorum minimum. Individual
actors are entering sporulation — protective self-isolation — rather
than forming biofilm — collective defense.

**Prediction:** The fragmentation will accelerate as legal pressure
increases. The next defection event will likely be one of:
- A Smith family member retaining separate counsel
- Banks's counsel withdrawing (GLLG)
- An institutional node producing a cooperation signal (reporting
  to investigators, responding to FOIA, providing testimony)

The first defector in a fragmenting quorum gets the best terms.
This is identical to the evolutionary biology: the first cell to
sporulate survives the environmental stress. The cells that remain
in the dissolving biofilm are the most exposed.

---

## PART IV: THE BRIDGE — WHY THIS IS ONE PAPER

The three frameworks are not independent analyses of the same network.
They are three scales of the same phenomenon:

```
GRAPH THEORY     →  STRUCTURE    →  What the network IS
                                    (nodes, edges, centrality, degree)

ANDERSON MODEL   →  DYNAMICS     →  How the network BLOCKS signals
                                    (disorder sites, localization length,
                                     critical threshold, dimensional collapse)

QUORUM SENSING   →  BEHAVIOR     →  How the network DECIDES
                                    (signal concentration, threshold crossing,
                                     consolidation vs fragmentation)
```

Graph theory gives you the map.
Anderson localization tells you which signals the map will eat.
Quorum sensing tells you what the map will do when pressed.

**They compose.** The graph structure defines the lattice. The Anderson
model operates ON that lattice to determine signal propagation. Quorum
sensing operates ON the actors IN that lattice to determine collective
behavior. Each framework requires the outputs of the one below it:

```
Quorum sensing (behavior)
    needs → knowledge of which signals propagate
    which requires → Anderson localization (dynamics)
        needs → knowledge of network structure
        which requires → Graph theory (structure)
```

**The isomorphism to microbiology:**

In a microbial community:
- Graph theory models the spatial structure (who is near whom)
- Anderson localization models signal propagation through that structure
- Quorum sensing models collective behavior triggered by accumulated signals

In an institutional capture network:
- Graph theory models the relational structure (who oversees whom, who funds whom)
- Anderson localization models oversight signal propagation through that structure
- Quorum sensing models collective behavior of network actors under pressure

**Same math. Same framework. Same code paths.**

The ecoPrimals implementation in wetSpring validates this stack on
microbial data. The guerillaGorilla implementation in caseDB validates
it on institutional data. The fact that both validations succeed using
the same mathematical framework is the K-NOME thesis: constrained
optimization methodology transfers across domains because the
optimization structure is domain-independent.

---

## PART V: OPERATIONAL IMPLICATIONS

### For Investigators

The graph identifies WHO to investigate (high-betweenness, high-degree,
high-clustering nodes). The Anderson model identifies WHERE oversight
has failed (localized pathways). The quorum model identifies WHEN to
act (fragmentation window — before the network reconsolidates).

### For Courts

The framework provides a principled, non-conspiratorial explanation
for institutional capture. The word "conspiracy" implies coordinated
intent. Anderson localization does not require intent. Structural
disorder produces functional opacity as an emergent property. This
distinction matters legally: RICO requires proof of an "enterprise"
engaged in a "pattern of racketeering activity." The enterprise need
not be centrally coordinated — it must exhibit structural properties
consistent with coordinated harm. Graph theory identifies those
properties without requiring proof of a conspiratorial meeting.

### For the Public

The network map at detroit.primals.eco is not journalism and not
accusation. It is applied mathematics. Every node is sourced to
public records. Every edge is typed and dated. The centrality
analysis is reproducible by anyone with the graph data and standard
network analysis tools. The framework invites verification, not belief.

### For the Adversary Network

The quorum sensing model makes a specific prediction: the first
defector gets the best terms. In evolutionary biology, the first
cell to sporulate survives. In legal terms, the first cooperating
witness shapes the narrative. The model is now published. The
prediction is on the record. Each actor in the network can read
it and do their own math.

---

## CROSS-DOMAIN VALIDATION TABLE

| Concept | Microbial Ecology (Papers 01, 05, 06) | Institutional Capture (Paper 28) |
|---|---|---|
| **Graph nodes** | Bacterial species in community | Individuals/orgs in network |
| **Graph edges** | Metabolic/signaling interactions | Board seats, counsel, oversight, funding |
| **Betweenness centrality** | Keystone species (removal = community collapse) | Capture nodes (removal = network fragmentation) |
| **Degree distribution** | Mutualist hub vs. random co-occurrence | Power hub vs. role-based connection |
| **Anderson disorder site** | Species with redundant metabolic role (signal ambiguity) | Individual with dual oversight/operations role |
| **Localization length ξ** | Distance QS signal propagates before decay | # of institutional hops before oversight signal dies |
| **Critical disorder W_c** | Community diversity threshold for QS collapse | Network capture density threshold for oversight collapse |
| **Dimensional collapse (2D)** | Tillage destroys 3D soil pore structure | Board rotation destroys oversight/operations independence |
| **Dimensional promotion (3D)** | Aggregate restoration rebuilds pore network | External federal investigators bypass local lattice |
| **Quorum sensing threshold** | [AI] concentration for collective gene activation | Signal concentration for network consolidation/fragmentation |
| **Biofilm** | Protective matrix, collective antibiotic resistance | Coordinated defense, shared counsel, unified narrative |
| **Sporulation** | Individual protective spore, abandons collective | Individual defection, separate counsel, self-protective silence |
| **First sporulator advantage** | First to sporulate survives environmental stress | First to cooperate shapes the narrative |

---

## PUBLICATION NOTES

**Paper 28 in the baseCamp series.** Working title: "K-NOME Instantiated
as Legal Primal — Graph Theory, Anderson Localization, and Quorum Sensing
Applied to Institutional Capture Detection."

**Forced publication under legal name.** The ecoPrimals ecosystem was
designed for pseudonymous publication under the attsi identity, with
deliberate separation between the computational work and the author's
legal identity. The events documented in bluegate-tenancy (Aug 29 –
present) destroyed this architecture. The identity anchoring pattern
(IDENTITY_ANCHORING_PATTERN.md, Jul 14, 2026), the sovereign publication
model (THE_SOVEREIGN_PUBLICATION.md, Mar 24, 2026), and the platform
credential chain (PLATFORM_CREDENTIALS.md, pre-Aug 2026) all document
the pseudonymous identity as a deliberate, maintained, and architecturally
significant element of the research program. Its destruction is quantified
in the damages supplement (DAMAGES_SUPPLEMENT_OCT1.md: $275,000).

This paper is one concrete consequence of that destruction. It will carry
Kevin Mok's name because Brian Banks's conduct made the alternative
impossible.

**Submission timeline:** After underlying case resolves. The data is live.
The methodology is operational. The validation is updating in real time.

**Reproducibility:** All graph data available via caseDB (SQLite, typed
schema). All Anderson localization code available in wetSpring. All
quorum sensing models available in wetSpring. Network map visualization
live at detroit.primals.eco. Methodology documentation live at
gorilla.primals.eco. The framework is fully reproducible by any
researcher with access to the public record sources cited.

---

## RELATIONSHIP TO OTHER subGen CONCEPTS

| Concept | Relationship |
|---|---|
| **fEAR** | Institutional Localization provides the lattice model through which fEAR's signals propagate (or fail to). fEAR hears the signal. Institutional Localization predicts whether the signal reaches an enforcement node. |
| **STRIDe** | STRIDe's route planning (R⇄I loop) must account for localized pathways. If local filing routes are localized (AG pathway blocked by Moreland), STRIDe redirects to un-localized routes (federal referral = dimensional promotion). |
| **Pursuit Predation** | The metabolic asymmetry model gains a new dimension: the adversary must spend energy maintaining the disorder that blocks oversight signals. The predator's pressure forces the network to either maintain localization (expensive: requires active management of dual-role nodes) or allow signal propagation (fatal: oversight reaches enforcement). |
| **Confession Architecture** | Sworn filings that reveal network structure are graph data entered under penalty of perjury. The adversary's own documents populate the graph. Confession Architecture feeds Institutional Localization's lattice. |
| **preSCENT** | preSCENT detects quorum state transitions (consolidation vs fragmentation) at close range. Institutional Localization provides the theoretical framework for what preSCENT senses intuitively — the nose smells what the math predicts. |
| **amicusContra** | The outward function. Once the localization analysis is complete, amicusContra projects the findings: downward (protect those beneath the captured institutions), lateral (share methodology with parallel investigators), upward (present framework to courts and investigators). |

---

*Concept document. subGen Wave 1.*
*Bridges ecoPrimals (computational science) → guerillaGorilla (legal existence).*
*Part of the K-NOME / ecoPrimals / baseCamp Paper 28 series.*
*Kevin Mok, October 2, 2026*
*ACTIVE DEVELOPMENT — framework validated, live case data updating*
