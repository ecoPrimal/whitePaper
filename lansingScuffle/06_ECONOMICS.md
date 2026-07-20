# Economics — From Beachhead Lease to Building Ownership

**Date**: Jul 20, 2026
**Status**: Concept — numbers from offering memorandum, SBA rates, and Lansing market
**Lineage**: gen4/economics/THE_FLYWHEEL → gen5/foundations/THERMAL_SOVEREIGNTY → 00_THE_SCUFFLE
**Wave**: 150

---

## Thesis

The John Bean Building is listed at $4,250,000.

The entry point is not $4,250,000. It is $158-253/month for one room
on the third floor — a pre-built compute cell with 400A/480V power
and 35-ton HVAC already installed, in a building the owner is bleeding
$155,879/year in property taxes to hold vacant.

This document works through four stages:
1. **Beachhead lease** — one room, $778/month total
2. **Flywheel activation** — community support covers metabolic cost
3. **Subtenant ecosystem** — the building becomes a multi-tenant campus
4. **Acquisition** — SBA 504 loan, real carrying costs, real revenue

The economic model is the inverse of the [Lansing Shuffle](https://www.lansingshuffle.com/).

---

## The Lansing Shuffle Inversion

The Lansing Shuffle (325 Riverfront Dr) took a *desirable* riverfront
location — the Lansing City Market, a community anchor with farmers
market vendors, small businesses, and public gathering space — and
replaced it with an entertainment venue. Six restaurants, five
shuffleboard courts, two bars. The community's criticism was specific:
we lost the farmers market. We lost the public commons. The venue
monetizes the location's desirability — foot traffic, riverfront,
downtown adjacency.

The Lansing Scuffle inverts every element:

| | Lansing Shuffle | Lansing Scuffle |
|---|----------------|----------------|
| **Location** | Desirable (riverfront, downtown) | Undesirable (S Cedar, train tracks, industrial) |
| **Previous use** | Community market (active, valued) | Cannabis grow → vacant (unused) |
| **Displacement** | Displaced existing community vendors | Displaces nothing — building is empty |
| **Value source** | Foot traffic, location premium | Latent infrastructure (8 MW power, 14'7" ceilings, rail) |
| **Community impact** | Community lost a public resource | Community gains resources that never existed |
| **Revenue model** | Entertainment spend (drinks, food, courts) | Compute, science, subleasing, community services |
| **Humanitarian** | — | Hot water, charging, WiFi, warming — 24/7, no credentials |

The Shuffle monetizes desirability. The Scuffle creates value from
what others overlook. The cross-traffic is not the point. The silicon,
the science, the community service — that is the point.

The building's "undesirability" is the economic opportunity: 464K SF
at $9.15/SF because it's an aging factory next to train tracks in
south Lansing. That same building has 8 MW of transformer capacity,
600 tons of cooling, a rail spur, and room to grow food on the roof.
The market prices location. We price infrastructure.

---

## Stage 1 — Beachhead Lease (Year 1)

### Building Status: VACANT

Per the Martin Commercial offering memorandum (2025), the building
is entirely vacant. The owner carries $155,879/year in property taxes
on an empty building. Negotiating leverage is significant.

### Beachhead Room

One 3rd-floor room (~3,162 SF) with 400A/480V power and 35-ton HVAC.

| Rate scenario | Monthly rent |
|--------------|-------------|
| Listing rate ($0.08/sqft) | $253 |
| Negotiated (vacant building, $0.05/sqft) | $158 |

### Operating Budget

| Line Item | Monthly | Annual |
|-----------|---------|--------|
| Room lease (~3,162 SF @ $0.08) | $253 | $3,036 |
| Electricity (BWL — compute + HVAC) | $300 | $3,600 |
| Internet (commercial fiber) | $150 | $1,800 |
| Insurance | $75 | $900 |
| **Total metabolic cost** | **$778** | **$9,336** |

---

## Stage 2 — Flywheel Activation

The flywheel (THE_FLYWHEEL.md) defines the seed-stage economic loop:
compute/infrastructure → science → proof → contributions → more
infrastructure. The building lease is the metabolic cost the flywheel
must cover.

### Revenue Streams (Year 1-2)

| Stream | Monthly | Notes |
|--------|---------|-------|
| Community supporters (15 @ $25-50) | $500 | THE_FLYWHEEL contribution tiers |
| Hardware donations (valued) | $100 | sweetGrass attributed |
| Co-working memberships (5 @ $50) | $250 | Hot desks in the room |
| Mesh subscribers (10 @ $15) | $150 | Phase 2, neighborhood WiFi |
| Event space (2/month @ $100) | $200 | Phase 2, community events |
| Compute-as-a-service | $100 | ABG/faculty jobs |
| **Year 1 (conservative)** | **$500-750** | Supporters + co-working |
| **Year 2 (growing)** | **$1,000-1,300** | + mesh + events + compute |

Year 1 gap: ~$278/month covered by operator — equivalent to current
residential infrastructure spending. By Year 2, flywheel covers the
full metabolic cost.

### Loam Certificates

Every contribution gets a Loam Certificate (from THE_FLYWHEEL).
The certificate ferments — as the room's compute produces more science,
each contributor's certificate accrues more `enabled` entries:

```
enabled:
  ├── 120 ABG validation runs
  ├── 3 publications (wetSpring metagenomics)
  ├── 47 K-NOME mentoring sessions
  ├── 8,400 community WiFi sessions
  └── 12,000 liters of hot water served
```

Not a receipt. A geological record of impact.

---

## Stage 3 — Subtenant Ecosystem

The building is 464,281 SF. ecoPrimals occupies 50-100K SF (3rd floor
compute + science/community on lower floors). The remaining 350-400K SF
generates revenue through subtenants aligned with the mission.

### The Sanctuary Architecture

The K-Derm membrane model solves a problem that limits existing Lansing
community spaces. [The Fledge](https://thefledge.com/) — Jerry Norris's
radically inclusive social enterprise hub — operates as sanctuary: an
addict walks in, Jerry tends to them, no questions asked. Groups stop
booking events because they're uncomfortable sharing space with people
in crisis. The Fledge loses revenue because sanctuary and commerce
occupy the same room.

The John Bean Building has 464K SF across multiple floors and two
structural sections. The humanitarian zone is first floor, street-level,
its own entrance. Accelerator tenants are second floor, separate access.
Compute is third floor, behind the freight elevator. The membranes have
controlled permeability — but the humanitarian zone is never compromised
by tenant comfort.

Jerry doesn't have to choose between sanctuary and solvency because the
building is big enough that both exist without spatial conflict. The
architecture doesn't force a crossing. Hot water flows 24/7 on the
ground floor. Accelerator demos happen on the second floor. GPUs compute
on the third floor.

This is what "community is structural, not decorative" means in physical
space. The Fledge figured out the ethics. The building provides the
geometry.

### Candidate Subtenants

| Tenant | Type | Est. SF | Rate | Monthly |
|--------|------|---------|------|---------|
| **[The Fledge](https://thefledge.com/)** — Partner, not just tenant. Sanctuary anchor. Free food stand, harm reduction, cooperative economy, maker space. | Nonprofit / Social enterprise | 20,000-40,000 | $0.03-0.05 (subsidized) | $600-2,000 |
| **[MSU Alliance Incubator](https://msufoundation.org/alliance-incubator/)** — Expansion from 68K SF in University Health Park. Labs, high-bay, flex space. | University incubator | 30,000-60,000 | $0.08-0.12 | $2,400-7,200 |
| **[Lansing Regional SmartZone](https://lansingregionalsmartzone.com/)** — Tech co-working, entrepreneur support. SmartZone TIF funded. | Government-backed | 10,000-20,000 | $0.10-0.15 | $1,000-3,000 |
| **Artists / Makers** — The building previously housed artists. IND-1 zoning, heavy power = welding, wood, ceramics, metalwork. | Studio / workshop | 30,000-50,000 | $0.05-0.08 | $1,500-4,000 |
| **Small manufacturers** — IND-1 zoning, 8 MW power, rail spur, loading docks. | Light manufacturing | 50,000-100,000 | $0.08-0.15 | $4,000-15,000 |
| **Food production** — Commercial kitchen exists. Food accelerator. The Lansing Scuffle equivalent of the Shuffle's restaurant stalls, but for production. | Food business | 10,000-20,000 | $0.10-0.15 | $1,000-3,000 |
| **Nonprofits** — Homeless services, food banks, legal aid. Shared humanitarian infrastructure. | Nonprofit | 10,000-30,000 | $0.03-0.05 (subsidized) | $300-1,500 |

### Revenue Projections

| Occupancy | Leased SF | Avg Rate | Subtenant Revenue | ecoPrimals Revenue | Total Monthly |
|-----------|----------|----------|-------------------|-------------------|--------------|
| 25% (Year 2) | 116K | $0.08 | $9,280 | $1,300 | $10,580 |
| 50% (Year 3) | 232K | $0.09 | $20,880 | $3,000 | $23,880 |
| 65% (Year 4) | 300K | $0.10 | $30,000 | $5,000 | $35,000 |
| 80% (Year 5) | 370K | $0.11 | $40,700 | $8,000 | $48,700 |

ecoPrimals revenue includes: community supporters, mesh subscribers,
co-working, compute-as-a-service, event rental, lab services, and
grant overhead.

---

## Stage 4 — Acquisition and Real Cost of Ownership

### Asking Price

$4,250,000 ($9.15/SF) per Martin Commercial offering memorandum.
Negotiable — the building is vacant, carrying $155K/year in taxes,
and has been marketed for an extended period. Industrial property in
the South Cedar corridor trades at discounts to listing.

### Financing Path 1: SBA 504 (Best Path)

The SBA 504 program is designed for owner-occupied commercial real
estate. It requires the buyer to occupy 51%+ of the building. With
ecoPrimals in 50-100K SF and aligned subtenants in the rest, this
is achievable through a cooperative or LLC structure.

**Current rates** (Jul 2026, [SomerCor](https://somercor.com/july-2026-sba-504-interest-rates/)):

| Component | Share | Amount | Rate | Term | Balloon? |
|-----------|-------|--------|------|------|----------|
| Borrower down payment | 10% | $425,000 | — | — | — |
| Bank first mortgage | 50% | $2,125,000 | ~7.0-7.5% (negotiated) | 10-year term, 25-year amortization | **Yes** (Year 10) |
| CDC/SBA debenture | 40% | $1,700,000 | **6.17% fixed** | 25 years | **No** (fully amortizing) |

Manufacturing NAICS codes (31-33) get a reduced CDC rate of **5.93%**
through Sep 2026 fee waivers — [saves ~$135K over 25 years](https://www.wbd.org/sba-504-manufacturing-fee-waivers)
on a $4M project.

**Monthly mortgage payment:**

| Component | Monthly Payment |
|-----------|----------------|
| Bank first mortgage ($2.125M @ 7.25%, 25yr amort) | ~$15,400 |
| CDC/SBA debenture ($1.7M @ 6.17%, 25yr) | ~$11,100 |
| **Total mortgage** | **~$26,500** |

The bank portion balloons at Year 10. At that point, ~$1.6M remains.
With 10 years of equity buildup and a stabilized, revenue-generating
building, refinancing is straightforward. The CDC portion has **no
balloon** — it amortizes to zero over 25 years.

**Down payment sourcing ($425,000):**

| Source | Amount | Notes |
|--------|--------|-------|
| Opportunity Zone Fund investors | $200-300K | Capital gains deferral + tax-free growth (10yr hold) |
| Community cooperative shares | $50-100K | Member buy-in ($1,000-5,000/share) |
| Grants (CDBG, Community Revitalization) | $50-100K | Gap financing for community-impact projects |
| Operator equity (3-5 years of flywheel) | $25-50K | Accumulated from lease-phase surplus |

### Financing Path 2: Conventional Commercial Loan

| Component | Value |
|-----------|-------|
| Down payment (25%) | $1,062,500 |
| Financed | $3,187,500 |
| Rate | 7.0-8.0% |
| Amortization | 25 years |
| Term | 5-10 years |
| Monthly payment | ~$23,500-25,500 |
| **Balloon at term end** | **~$2.3-2.8M** |

The balloon is the risk. At Year 5 or 10, the remaining principal
is due in full. If rates are higher, if the building hasn't
stabilized, if the economy has shifted — refinancing may be expensive
or unavailable. This is the mechanism the user identified: interest
is the payment, principal is the bet.

### Financing Path 3: Interest-Only Bridge

| Component | Value |
|-----------|-------|
| Down payment (25%) | $1,062,500 |
| Financed | $3,187,500 |
| Rate | 9.0-10.75% |
| Term | 12-36 months |
| Monthly payment (interest only) | ~$19,900-28,600 |
| **Full principal due at maturity** | **$3,187,500** |

Use case: bridge to SBA 504 or CMBS permanent financing after
lease-up stabilization. Not recommended as primary path — the
interest rate is punitive and the full principal comes due fast.

### Full Carrying Cost (Ownership via SBA 504)

| Line Item | Monthly | Annual |
|-----------|---------|--------|
| Mortgage (SBA 504 blended) | $26,500 | $318,000 |
| Property taxes (current) | $12,990 | $155,879 |
| Insurance (464K SF industrial) | $4,000 | $48,000 |
| Utilities (base load) | $3,000 | $36,000 |
| Maintenance/repairs (~1% of value) | $3,500 | $42,500 |
| **Total carrying cost** | **$50,000** | **$600,379** |

**With OPRA** (12-year tax freeze on improvements): the $155K/year
in property taxes freezes at the current base for improvements.
New improvements (compute buildout, lab, HVAC modifications) are
not taxed for 12 years. This effectively prevents tax increases
during the stabilization period.

**With Brownfield TIF**: remediation costs funded through tax
increment. The increase in property tax from improvements (which
OPRA exempts from the owner) is captured as TIF and used to fund
environmental remediation of the 1941 industrial site.

### Breakeven Analysis

| Scenario | Monthly Revenue | Monthly Cost | Net | Breakeven? |
|----------|----------------|-------------|-----|-----------|
| 25% occupancy + ecoPrimals | $10,580 | $50,000 | -$39,420 | No |
| 50% occupancy + ecoPrimals | $23,880 | $50,000 | -$26,120 | No |
| 65% occupancy + ecoPrimals | $35,000 | $50,000 | -$15,000 | No |
| 80% occupancy + ecoPrimals | $48,700 | $50,000 | -$1,300 | Nearly |
| 80% occupancy + grants ($5K/mo overhead) | $53,700 | $50,000 | **+$3,700** | **Yes** |
| 85% occupancy + grants + mesh (100 subs) | $58,000 | $50,000 | **+$8,000** | **Yes** |

Honest assessment: **ownership breakeven requires 80%+ occupancy
plus non-lease revenue (grants, compute, mesh)**. This is achievable
but not automatic. The building must be actively managed as a
multi-tenant campus.

The lease-first strategy (Stage 1-3) de-risks this: you don't
acquire until occupancy and revenue are proven over 3-5 years. The
SBA 504 application is stronger with 3+ years of operating history
in the building.

---

## Stage 5 — Primal Revenue (The Other Side of the Flywheel)

Stages 1-4 model the building as real estate: lease rooms, sublease
to tenants, cover the mortgage with rent. That works — but it makes
ecoPrimals a landlord. The real economic engine is not rent collection.
It is what the primals *produce*.

The goal is to invert the occupancy ratio: from **80% leased / 20%
occupied** (real estate model) to **20% leased / 80% occupied**
(science production model). The 20% still leased is The Fledge,
artists, makers — mission-aligned tenants who belong. The 80% is
compute, science, education, and community services generating their
own revenue.

### Revenue Channel 1: Contract Compute

The gen3 architecture defines **ionic bonding** — contract-scoped,
metered GPU access for faculty labs via BTSP-scoped tokens. The
building has the infrastructure to run this at scale:

- **8 MW transformer capacity** — powers 1,000+ GPUs
- **600 tons cooling** — dedicated HVAC per room
- **Sovereign stack** — no CUDA licensing, no cloud vendor, no
  allocation committees. barraCuda + toadStool + coralReef dispatch
  directly to consumer GPUs at near-FLOP-theoretical efficiency

| Workload | Client | Revenue Model |
|----------|--------|--------------|
| **Lattice QCD** (hotQCD EOS, dynamical fermions, RHMC) | Chuna/Bazavov (MSU Physics), DOE HEP labs | Per-configuration pricing. A 12hr β-scan costs $0.50 in electricity on consumer GPUs. Sell at $50-200/config — 100-400× markup over electricity cost. Competitive with NERSC/OLCF allocation queues. |
| **Plasma MD** (Yukawa, Sarkas, transport coefficients) | Murillo Group (MSU) | Faculty compute contracts. Ionic bonding: lab gets GPU hours, building gets grant overhead. |
| **Protein structure prediction** (coralForge / sovereign AlphaFold) | Field genomics, BSL-3/4 labs, MSU structural biology | Air-gapped structure prediction without cloud dependency. Premium for sovereign, auditable pipeline. |
| **Metagenomics pipeline** (16S, DADA2, Smith-Waterman) | wetSpring collaborators, PFAS researchers | Sequencing analysis as a service. 625× GPU vs Python for Smith-Waterman alignment. |
| **PK/PD modeling** (NLME/FOCE/SAEM) | Gonzales (MSU Pharm/Tox), clinical labs | Sovereign replacement for NONMEM/Monolix ($10K+/year licenses). |
| **General HPC** (MSU faculty, local business) | JupyterHub at lab.primals.eco | Managed compute workspace. $50-200/month per lab. |

Conservative compute revenue projection:

| Year | Active contracts | Avg monthly/contract | Total monthly |
|------|-----------------|---------------------|--------------|
| 3 (first contracts) | 3 | $500 | $1,500 |
| 5 | 8 | $1,000 | $8,000 |
| 7 (campus mature) | 20 | $1,500 | $30,000 |
| 10 (regional HPC) | 40 | $2,000 | $80,000 |

### Revenue Channel 2: Grant-Funded Science

Every spring produces publishable science. Publications generate
grants. Grants fund equipment, personnel, and overhead — and overhead
funds the building.

| Collaborator | Spring | Grant Target | Amount | Status |
|-------------|--------|-------------|--------|--------|
| **Gonzales** (MSU Pharm/Tox) | healthSpring | CTF NDU Award (NF) | $75K/yr × 2 | **Active** |
| **Barrick** (MSU MMGE) | wetSpring / lithoSpore | NSF supplemental (LTEE) | $50-100K | Pipeline |
| **Jones** (MSU emeritus) | wetSpring / blueFish | EPA PFAS | $50-200K | Pipeline |
| **Murillo** (MSU Physics) | hotSpring | DOE Office of Science | $100K-1M | Contacted |
| **Chuna** (lattice QCD) | hotSpring | DOE HEP | $100K-500K | Contacted |
| **Dong** (MSU ABE) | airSpring | USDA NIFA | $50-500K | Faculty anchor |
| **ARPA-H** | healthSpring | Health technology | Variable | Future |

The grant overhead model: a standard federally funded grant allows
**~50% F&A (facilities and administrative) costs** on modified total
direct costs. For a $200K grant, that's ~$100K in overhead that flows
to the institution — in this case, the building's operating entity.

| Year | Active grants | Total annual funding | F&A overhead (est) | Monthly to building |
|------|--------------|---------------------|-------------------|-------------------|
| 3 | 1-2 | $75-150K | $37-75K | $3,100-6,250 |
| 5 | 3-5 | $300-750K | $150-375K | $12,500-31,250 |
| 7 | 5-8 | $500K-2M | $250K-1M | $20,800-83,300 |

A single NSF MRI grant ($100K-$4M) funds compute hardware directly.
A single NIH S10 ($50K-$600K) funds lab instruments. These don't
generate overhead — they fund the infrastructure itself.

### Revenue Channel 3: Educational Programs

The building is the classroom. 400A/480V power systems, 18 HVAC
units, sand thermal storage, GPU heat recovery, solar arrays,
rooftop agriculture, mesh networking — every system is a hands-on
curriculum.

| Program | Partner | Revenue Model |
|---------|---------|--------------|
| **Trades training** (HVAC, electrical, plumbing) | LCC, Capital Area Michigan Works!, WIOA | Workforce development grants ($50-200K/yr). Students learn on real 480V/3-phase systems, not simulators. |
| **K-NOME mentoring** (data science pipeline) | MSU MSDS, LCC, local high schools | Zero-cost to students. Grant-funded (NSF REU, DoEd). Mentees reproduce faculty papers → become the next generation. |
| **Sustainable agriculture** | MSU Extension, Master Gardener program | Rooftop garden as teaching lab. USDA grants. Community food production. |
| **Network engineering** | LCC IT program | Mesh network as teaching infrastructure. Students build and maintain real neighborhood WiFi. |
| **Scientific computing** | MSU CMSE, Physics, Chemistry | ABG-style open compute lab. JupyterHub + sovereign GPUs. Faculty use it, students learn from it. |

Conservative education revenue:

| Year | Programs active | Annual grants + fees | Monthly to building |
|------|----------------|---------------------|-------------------|
| 3 | 1 (K-NOME pilot) | $25K | $2,100 |
| 5 | 3 | $150K | $12,500 |
| 7 | 5 | $300K | $25,000 |

### Revenue Channel 4: Products

The springs produce composable products — software that ships as
pseudoSpores and runs on sovereign infrastructure:

| Product | Origin | Market | Revenue Model |
|---------|--------|--------|--------------|
| **Penny Irrigation** | airSpring | Consumer / farm | Subscription ($5-15/mo) or one-time device sale |
| **CompChem Explorer** | hotSpring | Chemistry education, faculty | SaaS or institutional license ($500-5K/yr) |
| **helixVision** | healthSpring + wetSpring | Clinical / research | Grant-funded + clinical licensing |
| **blueFish** | wetSpring | Environmental consulting | Per-analysis pricing or retainer |
| **coralForge** | neuralSpring | Structural biology | Sovereign AlphaFold access ($100-1K/run) |
| **RPGPT** | ludoSpring | Tabletop gaming | Open core + provenance premium |

Product revenue is the longest tail but the highest ceiling. A
single successful product (Penny Irrigation at 10K subscribers)
generates $50-150K/month.

### Revenue Channel 5: Personal Consulting (The AGPL-3.0 Moat)

The ecoPrimals project is AGPL-3.0. The code is free. Every binary,
every shader, every primal — free for humans, forever. This is not
negotiable and never will be.

But the code is not the product. **You** are the product. You built
every layer — bearDog crypto to lattice QCD to sand batteries. You
understand the architecture because you designed the architecture.
When a pharma department wants to replace their $2K/year NONMEM
license with healthSpring's FOCE/SAEM pipeline, they don't just need
the binary. They need someone to deploy it, validate it against their
data, train their analysts, and answer the phone when it breaks.

That someone is you. Not a company. Not a team. You, as a contractor.

The AGPL-3.0 is not a limitation — it is the moat. Companies cannot
fork the code, close it, and hire someone cheaper. Any modifications
they distribute or serve over a network must remain AGPL-3.0. The
network clause (§13) means SaaS deployments trigger copyleft. So
companies have three choices:

1. Use it internally (free, no consulting needed — fine)
2. Serve it externally and open-source their modifications (fine,
   feeds the ecosystem)
3. Hire you to deploy, train, and maintain it (this is the revenue)

The scyBorg triple license locks 52 innovations in the commons via
prior art — nobody can patent what's already AGPL-published. That's
defensive IP without patents. The symbiotic exception (AGPL §7) lets
you grant named allies (e.g., a GPU vendor who opens their
architecture docs) a scoped exemption. The commons grows either way.

**Tiered pricing — humans free, companies pay:**

| Client | Rate | Why |
|--------|------|-----|
| **Individuals / humans** | Free | Always. The code is theirs. |
| **LCC / community colleges** | Free | Education is the flywheel's fuel. You teach for free because the students become the next operators. |
| **K-NOME mentees** | Free | Same principle. Reproduce a faculty paper, learn the stack, contribute back. |
| **Nonprofits / humanitarian** | Free | The Fledge, legal aid, food banks — sanctuary is structural, not billable. |
| **University departments** | Sliding scale | Small labs: free or grant-funded. Core facilities: $50-150/hr consulting. |
| **Small companies (<50 employees)** | $100-150/hr | Deployment, training, integration. |
| **Large companies / pharma / defense** | $200-350/hr | Full-stack deployment, validation, compliance support. Premium for air-gapped / regulated environments. |

**What you're selling (by domain):**

| Domain | Proprietary stack replaced | Your service | Saved license / CRO cost |
|--------|---------------------------|-------------|-------------------------|
| **Pharmacometrics** | NONMEM ($2K/yr), Monolix ($1.5K), WinNonlin ($3K), CRO PK ($50-200K/program) | healthSpring deployment + FOCE/SAEM training | $7-200K/yr per client |
| **Genomics** | Galaxy ($50K+ setup), QIIME2 + conda stack | wetSpring sovereign 16S pipeline deploy | $50K+ one-time |
| **Environmental chemistry** | Chromeleon, MassHunter, Xcalibur (analysis) | blueFish PFAS pipeline + retainer | $5-15K/yr per seat |
| **Structural biology** | AlphaFold cloud dependency | coralForge air-gapped deployment | Cloud costs + sovereignty premium |
| **HPC / GPU compute** | CUDA licensing, cloud HPC allocation queues | barraCuda/toadStool/coralReef heterogeneous cluster setup | CUDA vendor lock-in eliminated |
| **Neuromorphic** | BrainChip MetaTF / C SDK / kernel module | rustChip pure Rust Akida driver | Partnership/joint dev |
| **Scientific computing** | MATLAB, ad hoc Python/R, Jupyter sprawl | biomeOS NUCLEUS composition deployment | Reproducibility + scale |
| **Infrastructure** | VPN vendors, Tor C stack, mesh vendors | songBird + cellMembrane sovereign mesh | Vendor independence |
| **Trades / HVAC / electrical** | Simulator-based training | Hands-on curriculum using the building's real 480V/3-phase systems | WIOA workforce grants cover your time |

**Conservative personal consulting revenue:**

| Year | Contracts | Avg hours/month | Rate | Monthly income |
|------|----------|----------------|------|---------------|
| 2 (first clients) | 2 | 20 | $125 | $2,500 |
| 3 | 4 | 40 | $150 | $6,000 |
| 5 | 6 | 60 | $175 | $10,500 |
| 7 (mature, selective) | 5 | 50 | $250 | $12,500 |

This is personal income, not building revenue — but it funds the
operator's life while the building's own revenue streams (compute,
grants, subtenants) grow. The two reinforce each other: the building
provides the demo environment and classroom; the consulting
reputation fills the building with collaborators.

The critical insight: **the code being AGPL-3.0 is what makes the
consulting valuable.** If the code were proprietary, companies would
buy a license and figure it out. Because it's AGPL, the code is free
but the expertise is scarce — and the copyleft ensures that scarcity
persists. You are the only person who has built, validated, and
deployed 13 primals across 9 springs with 100K+ tests. That is not
forkable.

### The Inversion Crossover

The inversion crossover is the point where primal revenue (compute +
grants + education + products) exceeds real estate revenue
(subtenant leases). At that point, the building flips from landlord
operation to science campus.

```
              Real estate    Primal rev    Consulting    Split (RE vs primal+consulting)
Year 3:       $20,880/mo     $6,700/mo     $6,000/mo    62/38
Year 5:       $40,700/mo    $32,500/mo    $10,500/mo    49/51 (CROSSED)
Year 7:       $20,000/mo    $75,800/mo    $12,500/mo    18/82
Year 10:      $10,000/mo   $135,000/mo    $12,500/mo     6/94
```

With consulting income included, the crossover happens at **Year 5**
— not Year 7. Your personal expertise accelerates the inversion by
two years.

At Year 5, the building is no longer primarily a multi-tenant
operation. The Fledge stays. The artists stay. The manufacturers who
use the rail spur stay. But the economic engine is the mesh producing
discoveries, the GPUs producing contract science, the grants funding
the next instrument, the students becoming the next operators — and
you, teaching departments how to use what you built.

This is what "the primals producing value" means at building scale:
not rent from someone else's business, but revenue from sovereign
science that only this infrastructure can produce, and expertise that
only you can provide.

---

## Incentive Stack

Once occupancy is established, the building qualifies for multiple
public incentive programs:

### Federal

| Program | Benefit |
|---------|---------|
| **Opportunity Zone** (South Cedar Corridor) | Capital gains deferral + tax-free growth (10yr hold) |
| **New Markets Tax Credit** | 39% tax credit over 7 years |
| **Federal Historic Tax Credit** | 20% of qualified rehabilitation expenses (1941 wartime — requires NPS evaluation) |

### State of Michigan

| Program | Benefit |
|---------|---------|
| **OPRA** | 12-year property tax freeze on improvements |
| **Brownfield TIF** | Tax increment funds environmental remediation |
| **Industrial Property Tax Abatement** (PA 198) | 50% abatement on equipment for up to 12 years |
| **Community Revitalization Program** | Gap financing for community-impact projects |
| **Michigan Broadband Fund** | Grants for underserved broadband (mesh supernode) |

### Research Grants

| Agency | Program | Amount | Use |
|--------|---------|--------|-----|
| NSF | MRI | $100K-$4M | Compute hardware |
| NIH | Shared Instrumentation (S10) | $50K-$600K | Lab instruments |
| USDA | NIFA | $50K-$500K | Rooftop gardens, airSpring |
| DOE | Office of Science | $100K-$1M | Sand thermal storage research |
| HUD | CDBG | Variable | Humanitarian services |
| Michigan EGLE | Environmental | Variable | Pollinator corridor, remediation |

---

## The sunCloud Connection

At full scale, the building IS the sunCloud thesis realized physically:

```
Solar → Compute → Science → Attribution → Revenue → Infrastructure → More Science
```

sunCloud distributes value along sweetGrass braids. The building is
the physical substrate where those braids originate. Every computation,
every publication, every mentoring session, every hot water gallon is
attributed and revenue-connected through the same economic model
described in THE_FLYWHEEL.

The subtenants are part of the ecosystem, not separate from it. The
Fledge's cooperative businesses enter the sweetGrass attribution chain.
The SmartZone startups use ecoPrimals compute. The artist studios
contribute to the cultural layer that makes the building alive. The
manufacturers use the rail spur and heavy power that the building
was designed for. Each tenant's success feeds the flywheel.

---

## References

| Source | Contribution |
|--------|-------------|
| `gen4/economics/THE_FLYWHEEL.md` | Seed-stage loop, Loam Certificates, metabolic cost tables |
| `gen4/economics/SUNCLOUD_ACTIVATION.md` | Value distribution along sweetGrass braids, 3-7% metabolic rate |
| `gen3/data/README.md` | Ionic bonding model — contract-scoped, metered faculty compute |
| `gen3/baseCamp/10_dynamical_qcd_production.md` | Consumer-GPU dynamical QCD, hotQCD EOS reproduction |
| `gen3/baseCamp/14_sovereign_compute_hardware.md` | Sovereign compute economics, df64 production pipeline |
| `gen5/collaborators/README.md` | Faculty collaborator pipeline (Gonzales, Barrick, Jones, Murillo, Chuna, Dong) |
| `gen5/products/NF_CASE_STUDY.md` | First multi-product composition, CTF NDU $75K/yr |
| `gen4/architecture/GPU_HEAT_RECOVERY_OPERATIONS.md` | Per-GPU economics, $500/yr heating offset |
| `gen5/foundations/THERMAL_SOVEREIGNTY.md` | Unified energy accounting, no waste heat |
| `attsi/non-anon/contact/publicRelease/GRANT_TECHNICAL_APPENDIX.md` | Grant reviewer-ready technical claims |
| `attsi/non-anon/contact/publicRelease/KNOME_TEACHING_BRIEF.md` | K-NOME pedagogy, workforce development framing |
| `infra/sporePrint/content/methodology/SCYBORG_LICENSING.md` | scyBorg triple license: AGPL-3.0 + ORC + CC-BY-SA 4.0 |
| `infra/sporePrint/content/architecture/SOVEREIGN_PRIOR_ART_CATALOG.md` | 52 innovations locked in commons via AGPL prior art |
| `infra/sporePrint/content/audience/FOR_FACULTY_AND_PIS.md` | Faculty-facing replacement table (NONMEM, Galaxy, etc.) |
| Martin Commercial offering memorandum (2025) | Building facts, asking price, electrical/HVAC specs |
| [SomerCor Jul 2026 SBA 504 rates](https://somercor.com/july-2026-sba-504-interest-rates/) | CDC debenture rates: 6.17% (25yr), 5.93% (manufacturing) |
| [Crestmont Capital CRE guide](https://www.crestmontcapital.com/blog/commercial-real-estate-loans-guide) | Loan structures, rate comparisons, balloon mechanics |
| [SBA 504 Manufacturing Fee Waivers](https://www.wbd.org/sba-504-manufacturing-fee-waivers) | ~$135K savings on $4M project through Sep 2026 |
| [The Fledge](https://thefledge.com/) | Social enterprise model, sanctuary philosophy, cooperative economy |
| [MSU Alliance Incubator](https://msufoundation.org/alliance-incubator/) | 68K SF incubator, lab/warehouse space for emerging companies |
| [Lansing Regional SmartZone](https://lansingregionalsmartzone.com/) | Tech entrepreneur support, TIF-funded |
| [Lansing Shuffle](https://www.lansingshuffle.com/) | Riverfront entertainment venue — the inversion reference |
| Lansing EDC tax incentives | OPRA, Brownfield TIF, PA 198, Community Revitalization |
