# fEAR + STRIDe Integration — guerillaGorilla's Core Loops

**How the sensing and motion layers operate within the legal primal.**
**Cross-references:** `../subGen/FEAR_CONCEPT.md`, `../subGen/STRIDE_CONCEPT.md`,
`../subGen/PURSUIT_PREDATION_CONCEPT.md`

---

## THE TWO LOOPS

guerillaGorilla runs two concurrent loops. They are not sequential.
They are the two legs of the gait.

```
fEAR (exteroception — what is the ADVERSARY doing?)
  flow → Evolution → Adversarial → Response
  |                                        |
  └─── senses the world ──── evolves ──────┘

STRIDe (proprioception + locomotion — where are WE?)
  Strategy → Tactics → R ⇄ I → Deployment → execution
  |                    |   |                        |
  └── plans ───────── senses self ── stages ── steps┘
```

fEAR is the ear. STRIDe is the stride. Together: the system hears
the world and knows where it is within it.

---

## fEAR WITHIN GUERILLAGORILLA

fEAR was conceived as a general adversarial sensing framework. Within
guerillaGorilla, each fEAR component maps to specific legal operations:

### flow — Establish Information Channels

| Channel | What it senses | guerillaGorilla subsystem |
|---|---|---|
| PACER | Federal court filings, bankruptcy schedules, case status | Finance, Accountability |
| Wayne County ROD | Property transfers, liens, mortgages, tax certifications | Finance, Accountability |
| LARA | Entity filings, professional licenses, annual reports | Accountability |
| Court dockets | Motions, orders, hearing dates, case assignments | Navigation, Rights |
| Certified mail tracking | Delivery confirmation, refusal documentation | Navigation (proof of service) |
| Social media / LinkedIn | Self-incriminating statements, network connections | Accountability (OSINT) |
| News archives | Historical reporting, investigative journalism | Accountability (evidence) |
| Agency responses | JTC, State Bar, MDE, AG, MDHHS acknowledgments | Accountability |

Flow is always-on. The channels don't close between filings. Every
channel continuously feeds the R⇄I loop within STRIDe.

### Evolution — Case Mutation

Each new data point mutates the case. Within guerillaGorilla, mutation
follows the domain taxonomy:

| New data | Mutation type | Subsystem affected |
|---|---|---|
| Banks says "I'm a lawyer" | New count: UPL (MCL 450.681) | Accountability |
| Leon + Shayla assault DaSean | New protective instruments: 4 PPOs | Protection |
| Marquita intercepts mail | New referral: OIG (18 USC 1708) | Protection, Finance |
| Perkins = Miller's attorney | New RICO connection: shared counsel | Accountability |
| Charter contract pulled | New violations: §§ 3.06, 10.07 | Accountability |
| Moreland = Asst. AG | New defendant + AG conflict | Accountability |
| DaSean reveals car + house | New custody evidence: stable housing | Rights, Identity |
| Partner finishes MCAT | Team capacity increase | All subsystems |

The case does not grow randomly. It grows in **response to the adversary's
behavior.** Every mutation is triggered by something the adversary did,
filed, said, or revealed. The adversary IS the fuel.

### Adversarial — The Adversary as Input Source

guerillaGorilla's most distinctive feature: the system is designed for
opposition. It does not require cooperation. The adversary's resistance
generates the very evidence that strengthens the case.

| Adversary action | What it generated | Why it's worse for them |
|---|---|---|
| Banks rejected parental authorization | Standing for civil suit | He created Kevin's injury |
| Banks claimed to be a lawyer | UPL count + AG referral | A new felony in front of a witness |
| Shayla filed 192 pages of exhibits | Self-incriminating evidence | She formalized her own exploitation under oath |
| Leon assaulted DaSean | PPOs + criminal referral + custody evidence | Documented violence on Ring camera |
| Marquita intercepted mail | Federal mail fraud referral | At a federal facility (USPS), documented |
| Banks called a parent post-service | Witness tampering exhibit (BB) | Documented in real-time |
| Network stayed silent | Information quarantine | Can't coordinate defense |
| Network contacted each other | Potential evidence of enterprise coordination | Any contact is discoverable |

**The adversary is in a bind:** acting generates evidence; not acting
generates default. There is no move that doesn't feed the system.

### Response — Calibrated Output

Every response is documentation, never argument. Within guerillaGorilla:

| Trigger | Response | Channel |
|---|---|---|
| Banks claims J.D. | State Bar search → zero results → Exhibit C | Filing |
| Banks says "I'm a lawyer" | UPL complaint filed next business day | Regulatory |
| Miller on PCA dev team | JTC complaint filed with certified mail | Regulatory |
| Yancey is Board Chair | JTC complaint filed with certified mail | Regulatory |
| Marquita intercepts mail | OIG referral with tracking data | Federal |
| Leon assaults DaSean | PPOs + emergency custody + video analysis | Protection + Filing |
| Charter contract found | OCR → analysis → violations identified | Intelligence |

The response is always proportionate, documented, and filed. Never verbal.
Never threatening. Never emotional. The system responds with paper.

---

## STRIDe WITHIN GUERILLAGORILLA

STRIDe was conceived as a universal motion framework. Within guerillaGorilla,
each component has legal-domain-specific instantiation:

### S — Strategy

The overarching plan. Set once, revised rarely.

**Current strategy (Sep 5, 2026):**
- Three-case structure: Smith (custody/tort), Banks (civil), RICO (federal)
- No single point of failure — any one case can be lost without losing the campaign
- Custody first (children's safety), RICO when evidence is complete
- Multi-venue force multiplier (different courts, different agencies, different jurisdictions)
- Termination condition: operator's satisfaction (not a dollar amount)

Strategy constrains all other STRIDe components. Every tactical decision
is evaluated against: "Does this serve the three-case structure?"

### T — Tactics

Specific decisions within the strategy. Changes with conditions.

**Tactical decisions made this week:**
- File regulatory complaints BEFORE civil suit (persistent effects)
- Serve Banks BEFORE amendment (information asymmetry)
- Hold judges for post-Labor Day (prevent coordination)
- File emergency custody in Wayne (jurisdiction over children)
- File PPOs in Ingham (Kevin's residence for DaSean's PPOs)
- Notify trustee via email AND mail (dual channel, timestamped)
- Deliver Nolan packet physically (personal touch with federal firm)
- Build PACER API before manual pulls (automation pays forward)

### R ⇄ I — Reconnaissance ⇄ Intelligence (The Neural Loop)

This is the proprioceptive feedback layer. It runs continuously.

```
R: Pull PACER for Marquita Smith
I: 3 bankruptcies found — 3rd is ACTIVE (24-50247). Undisclosed Jeep.
R: Pull ROD for Marquita / Leon addresses
I: Dresden is NOT on the bankruptcy filing. Address fraud?
R: Check PCA enrollment — children's address?
I: Children enrolled from Bradford, then Dresden. Neither matches BK filing.
R: Pull PACER for Simone Smith
I: Student loans listed — but Simone never attended college.
R: Verify: did Shayla attend college?
I: Bowling Green + Western Michigan. Student loans should be HERS.
R: Cross-reference Simone's address with household map
I: Simone's car observed at Dresden. Three-household shell game.
  ↻ (the loop does not terminate)
```

The R⇄I loop is where squirrel provides its highest value:
cross-referencing at machine speed, recalling bankruptcy schedules,
mapping addresses, identifying anomalies. The operator directs
("check Simone's student loans"), squirrel processes, the result
redirects the next reconnaissance pass.

### D — Deployment (Mise en Place)

Everything staged before execution. The legal mise en place:

| Staged item | When prepared | Used when |
|---|---|---|
| 5 regulatory complaints printed | Sunday night | Monday morning filing route |
| Notary appointment confirmed | Saturday | Monday before State Bar |
| Route mapped (State Bar → MDE → AG → USPS) | Sunday | Monday execution |
| Subpoenas prefilled (18 forms) | Week 1 | Ready for service whenever needed |
| FOIA letters drafted (6 agencies) | Saturday morning | Sent when strategic timing is right |
| PACER API tool built | Saturday | Ready for batch execution |
| Emergency custody motion formatted | Tuesday night | Filed Wednesday morning via 3rdcc |
| PPO forms completed (4 respondents) | Tuesday-Wednesday | Filed Thursday |
| Exhibit binders assembled | Sunday | Served with complaint Monday |

Deployment is where most pro se litigants fail — not because the
filing is hard, but because the printer is out of ink, the notary is
closed, the form is wrong, the copies aren't made. guerillaGorilla
treats deployment as a first-class subsystem.

### e — execution (lowercase)

The foot hits the ground. Walk in. Hand over documents. Walk out.

The intellectual work was Strategy through Deployment. execution
has one degree of freedom: forward.

**Monday's route:**
1. Drive to Lansing courthouse → file complaint → receipt
2. Drive to State Bar office → file UPL complaint → receipt
3. Drive to post office → certified mail JTC complaints → tracking
4. Drive home → scan all receipts → update tracking database
5. Total execution time: ~3 hours. Total planning time: ~30 hours.

The ratio (10:1 planning to execution) is the signature of a
well-prepared STRIDe.

---

## THE CONCURRENT OPERATION

fEAR and STRIDe don't take turns. They run simultaneously.

**While fEAR processes the Sep 2 assault:**
- flow: Ring video received, eyewitness statements collected
- Evolution: Case mutates — new PPOs, new counts, new urgency
- Adversarial: Leon's violence is the input that generates protective orders
- Response: PPOs drafted, emergency custody motion prepared

**STRIDe is simultaneously:**
- R: Researching Wayne County vs. Ingham County jurisdiction for emergency orders
- I: Processing — Wayne for custody (children's residence), Ingham for PPOs (Kevin files for DaSean)
- T: Filing emergency motion via 3rdcc (Wayne), PPOs via Ingham clerk
- D: Printing forms, confirming correct court addresses, preparing exhibits
- e: Filing next morning

The two loops share the R⇄I feedback layer:
- fEAR's "flow" feeds STRIDe's "Reconnaissance" (new data in)
- STRIDe's "Intelligence" feeds fEAR's "Evolution" (processed data mutates the case)
- fEAR's "Response" IS STRIDe's "execution" (the calibrated output is the step forward)

```
fEAR:    flow ──→ Evolution ──→ Adversarial ──→ Response
                      ↕                            ↕
STRIDe:  S → T → R ⇄ I ────────────────→ D ──→ e
```

The vertical arrows are the integration points. Evolution and Intelligence
share data. Response and execution are the same act viewed from different
frames — fEAR sees it as a calibrated response to adversary input; STRIDe
sees it as a prepared step in the operational process.

---

## PURSUIT PREDATION AS THE EVOLUTIONARY ANCHOR

The full framework:

```
       Pursuit Predation
       (WHY — metabolic asymmetry, sustained pace, convergent evolution)
            /          \
           /            \
      f(EAR)          STRIDe
   (the ear)        (the gait)
   sensing           motion
   hearing           walking
        \            /
         \          /
      guerillaGorilla
      (the legal primal — the body that hears and walks)
            |
         squirrel
      (the AI compute — the brain it borrows)
            |
         OPERATOR
      (the one who decides where to walk)
```

The persistence hunter walks. The antelope sprints. The hunter's cost
per cycle is constant. The adversary's cost per cycle escalates.

In guerillaGorilla terms:
- Operator cost per filing: ~10 hours + filing fee (constant)
- Adversary cost per response: ~$5,000-10,000 attorney time (escalating)
- Adversary's metabolic reserve: limited (broke defendants, conflicted attorneys)
- Operator's metabolic reserve: sustainable (dopamine, not cortisol; 6 months at tempo)

The hunt terminates when the adversary's cumulative cost exceeds their reserves.
The operator is still walking.

---

## MULTI-OPERATOR EXTENSION: SHARED fEAR

When two operators share the fEAR sensing layer (Mode 2: cross-protected pair),
the pursuit predation model gains a new property: **redundant persistence.**

A single persistence hunter can be tripped. If the hunter falls, the antelope
escapes. But two hunters on converging vectors create a system where one can
stumble without the quarry gaining distance — because the other is still walking.

In guerillaGorilla terms:
- Operator cost per cycle: ~10 hours + filing fee (constant per operator)
- Combined operator cost: ~20 hours (still far below $10K attorney response)
- Adversary faces TWO concurrent fEAR streams sensing their behavior
- Silencing one operator = still one hunter walking + retaliation evidence
- Silencing both = coordinated attack = enterprise evidence (RICO element)

The adversary's metabolic problem doubles. The operators' metabolic reserves
remain sustainable — because mutualism, like pursuit predation, is designed
for efficiency, not sprinting.

See `CROSS_PROTECTION.md` for the full framework including Mutual Assured
Documentation, retaliatory filing detection, and the three operational modes.

---

*fEAR + STRIDe integration for guerillaGorilla. Wave 0.*
*Part of the K-NOME / ecoPrimals architecture.*
*Kevin Mok, September 5, 2026*
