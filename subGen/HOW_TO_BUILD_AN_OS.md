# How To Build an OS

### A Study in Parasitic Infrastructure Using Dykema Gossett PLLC as Model Organism

*subGen #41 — October 9, 2026*
*Continuous work. Living document.*

---

## Abstract

An operating system mediates between hardware and applications.
A healthy OS allocates resources efficiently — applications innovate,
hardware performs, users benefit. A parasitic OS extracts resources
from both applications and hardware while presenting the appearance
of mediation. The applications starve. The hardware degrades. The
users lose access. Innovation dies.

This study uses the Michigan law firm Dykema Gossett PLLC as a
model organism for parasitic operating system architecture. All
data comes from public records: LARA business filings, IRS Form
990 filings, Michigan campaign finance records, WHOIS domain
registration data, MPSC utility registrations, FCC filings,
federal court documents (PACER), and published journalism.

Dykema is a corporate entity. Its filings are public. Its PAC
contributions are public. Its officers' roles on nonprofit boards
are public. This is not doxxing. This is entity accountability
through public record analysis.

---

## 1. What Is an Operating System?

In computing, an OS has three functions:

1. **Resource allocation** — CPU time, memory, disk, network
2. **Process management** — start, stop, schedule, prioritize
3. **Abstraction** — hide complexity, present clean interfaces

In an ecosystem, these functions map to:

| OS Function | Ecosystem Equivalent | Healthy | Parasitic |
|-------------|---------------------|---------|-----------|
| Resource allocation | Capital flow | Distributed to producers | Extracted to intermediary |
| Process management | Entity lifecycle | Organisms born, live, die naturally | Organisms created, used, dissolved on command |
| Abstraction | Identity | Transparent — entity = visible actor | Opaque — entity ≠ visible actor |

A healthy ecosystem has distributed resource allocation, natural
entity lifecycles, and transparent identity. A parasitic OS
centralizes allocation, manufactures entities on demand, and
hides identity behind abstraction layers.

---

## 2. The Dykema OS — Architecture

### 2.1 The Kernel: W. Alan Wilk

Every OS has a kernel — the privileged code that runs at the
lowest level and controls everything above it.

| Attribute | Detail | Source |
|-----------|--------|--------|
| Name | W. Alan Wilk | dykema.com |
| Title | Member; Team Leader, Political Compliance | dykema.com |
| Bar | Michigan, 1995 | State Bar records |
| Education | James Madison College (MSU), Boston College Law | dykema.com |
| Email | wawilk@dykema.com | dykema.com |
| Phone | 517-374-9122 | dykema.com |
| Recognition | Best Lawyers (Admin/Regulatory, 2011-2027) | dykema.com |
| Memberships | National Republican Lawyers Association | Deadline Detroit |

Wilk incorporates entities. He files their state paperwork. He
serves as their lawyer. He manages their compliance. He responds
(or doesn't) to press inquiries. When Deadline Detroit called,
Wilk said: **"I'm not authorized to speak to the press on this."**

The kernel doesn't speak to userspace.

### 2.2 The Scheduler: Renae Moore

A scheduler decides which processes run, when, and for how long.

| Attribute | Detail | Source |
|-----------|--------|--------|
| Name | Renae Moore | dykema.com |
| Title | Senior Compliance Specialist | dykema.com |
| Email | rmoore@dykema.com | dykema.com |
| Phone | 517-374-9121 | dykema.com |

Moore's simultaneous roles:

| Entity | Role | Status |
|--------|------|--------|
| Save Detroit Jobs / Detroit Leaders | Asst Secretary | Active |
| Our Neighborhoods First | Compliance Officer | Active |
| Detroit Jobs First | Compliance Officer | Active |
| RFFW LLC | Treasurer | Dissolved |
| Turn Around Wayne County PAC | Record Keeper | Active |
| Duggan Campaign | Compliance Officer | Active |
| Dykema Gossett PLLC | Senior Compliance Specialist | Employer |

One person. Seven entities. All scheduled from the same desk.

**Sources:** IRS 990 filings (ProPublica Nonprofit Explorer), Michigan
SOS campaign finance records (Meyers v RFFW complaint), Deadline
Detroit reporting (Steve Neavling), Dykema.com staff listing.

### 2.3 The Process Table: Entities as Spawned Processes

An OS spawns processes — discrete units of work that appear
independent but share the same kernel and scheduler.

| Process (Entity) | PID (EIN/LARA) | Created | Status | Function |
|-----------------|----------------|---------|--------|----------|
| Save Detroit Jobs | 81-3772058 | 2016 | Active (renamed) | Defeated community benefits ordinance |
| → renamed: Impact Detroit | same | 2021 | Active (renamed) | Transitional name |
| → renamed: Detroit Leaders | same | Aug 2021 | Active | Defeated journalist ML Elrick, elected Latisha Johnson |
| Our Neighborhoods First | (501c4) | Jul 30, 2020 | Active | Promoted Duggan's Prop N ($250M bond), attacked Duggan opponent |
| Detroit Jobs First | 81-3788427 | 2016 | Active | Defeated community benefits (Prop A) |
| RFFW LLC | (LLC) | Jul 14, 2022 | Dissolved | Passed $1M from Shery Cotton to Reproductive Freedom for All |
| Turn Around Wayne County PAC | (PAC) | — | Active | Funneled corporate money to SDJ |
| Detroit Forward Together | (SuperPAC) | — | Active | Shared PO Box with ONF, received $62K from Chamber PAC |

**The process lifecycle pattern:**
1. **spawn** — Wilk files paperwork, Moore assigned as compliance
2. **execute** — entity spends money, sends mailers, runs ads
3. **rename** — if entity draws attention, change name (SDJ → Impact Detroit → Detroit Leaders)
4. **dissolve** — if entity draws legal complaint, file dissolution (RFFW)
5. **respawn** — create new entity with same officers, same address, same function

This is `fork()` in political infrastructure.

**Source:** LARA entity search, IRS Form 990 filings, Michigan SOS
campaign finance records, Deadline Detroit, Metro Times, Motor
City Muckraker.

### 2.4 The Phone Number Test

The simplest proof that SDJ is not an independent entity:

| Entity | Phone on IRS Filing | Whose Phone Is That? |
|--------|--------------------|--------------------|
| Save Detroit Jobs | **517-374-9100** | **Dykema Gossett Lansing** |

If you call Save Detroit Jobs, you reach Dykema's receptionist.

The entity doesn't have its own phone number. It doesn't have
its own office. It doesn't have its own staff (Moore and Vykydal
ARE Dykema staff). It doesn't prepare its own taxes (Dykema's
Ann Arbor office files the 990EZ).

**SDJ is not an entity that uses Dykema. SDJ is a Dykema process
wearing a 501(c)(4) costume.**

**Source:** IRS Form 990EZ (EIN 81-3772058), filed November 11, 2024.
Preparer: Olivia RC A Flower, Dykema Gossett PLLC, 2723 S State
St Ste 400, Ann Arbor MI 48104.

### 2.5 The Filesystem: Domain Privacy as Access Control

An OS controls which processes can see which files. Dykema controls
which entities are visible to the public.

| Entity | Website | Registration Privacy | Source |
|--------|---------|---------------------|--------|
| Our Neighborhoods First | ourneighborhoodsfirst.com | **Domains By Proxy** | WHOIS / Deadline Detroit |
| Detroit Jobs First | detroitjobsfirst.com | **Domains By Proxy** | WHOIS / Metro Times |
| SDJ / Detroit Leaders | *(no website)* | **No website — uses Dykema phone** | IRS 990EZ |
| RFFW LLC | *(no website)* | **Dykema as shield** | MI SOS complaint |

**Domains By Proxy tagline:** *"Your identity is nobody's business but ours."*

This is `chmod 000` on entity ownership — nobody can read who
owns the process except the kernel.

**Source:** WHOIS records, Deadline Detroit (Steve Neavling, Charlie
LeDuff), Metro Times.

### 2.6 The Bipartisan Bus: Both Parties Served

A real OS doesn't care what applications do. It serves whatever
process is running. Dykema doesn't care about party. It serves
whoever pays.

**Dykema Gossett State PAC expenditures (2017-present, $725K+):**

| Recipient | Amount | Party |
|-----------|--------|-------|
| House Republican Campaign Committee | $62,000 | R |
| Senate Republican Campaign Committee | $58,750 | R |
| Michigan House Democratic Fund | $45,000 | D |
| Michigan Senate Democratic Fund | $44,000 | D |
| Michael Duggan Campaign | $13,500 | D |
| Aric Nesbitt | $15,500 | R |
| Sam Singh | $8,250 | D |
| Winnie Brinks | $7,750 | D |

**Plus:** Dykema Federal PAC → $4,000 → Tom Barrett for Congress (R)

**Plus:** Wilk personally → Duggan campaign lawyer

**Plus:** Wilk personally → incorporated dark money for Lee Chatfield (R)
and Rick Snyder (R) and Scott Benson (D) and Latisha Johnson (D)

The kernel is apolitical. The kernel serves the scheduler, and
the scheduler serves whoever currently has root access.

**Source:** TransparencyUSA.org (Dykema Gossett State PAC, all
cycles 2017-present), Deadline Detroit, Detroit News.

---

## 3. Resource Extraction — What the Parasitic OS Takes

### 3.1 From Schools

Purpose Charter Academy (PCA) is authorized by DPSCD. The Purpose
Group LLC (Brian Banks, sole member) takes **72.67% of all revenue**
as a management fee. PCA's students score **3% proficient in math**.
MacDowell Prep ranks **1,443rd out of 1,488 Michigan elementary schools**.

The dark money vehicle (SDJ) that defeated the journalist investigating
this school → elected a city council member (Latisha Johnson) who sits
on the PCA board → was incorporated by Dykema → staffed by Dykema
employees → uses Dykema's phone number.

**Resource extracted:** Public education funding ($4.9M+ annual state aid)
**Innovation killed:** Community accountability (defeated journalist
who would have exposed it)

**Source:** Michigan Department of Education data (mischooldata.org),
Clutch Justice (Sep 13, 2026), DPSCD board minutes (Jul 2025).

### 3.2 From Democracy

SDJ spent $84,017 in the District 4 council race. That money
came from sources including Blue Cross Blue Shield, the Schostak
Family PAC (Republican), and Turn Around Wayne County PAC (record
keeper: Renae Moore, Dykema).

The money defeated ML Elrick — a Fox 2 investigative reporter
who had exposed Benson and Carol Banks for double-dipping
taxpayer salaries. In his place: Latisha Johnson, who now
sits on the PCA board.

When a dark money vehicle spends $84K to defeat a journalist
and replace him with a board member of the school the journalist
was investigating, that's not democracy. That's a kernel panic
suppressed before it can alert the user.

**Resource extracted:** Democratic accountability
**Innovation killed:** Investigative journalism in Detroit District 4

**Source:** Michigan SOS campaign finance records, Deadline Detroit
(Steve Neavling), Ballotpedia.

### 3.3 From Community Self-Determination

Proposal A (2016) would have required significant concessions
from developers receiving city incentives. A grassroots community
benefits ordinance.

Dykema incorporated two dark money vehicles (Detroit Jobs First +
Save Detroit Jobs) to defeat it. Both used Domains By Proxy.
Both shared officers with Duggan-aligned entities. Combined
spending: $100K+. Donors: corporations and developers — the
entities that would have been regulated.

The community tried to write its own governance rule. The OS
intercepted the system call and returned `EPERM`.

**Resource extracted:** Community governance capacity
**Innovation killed:** Community benefits framework for Detroit
development

**Source:** Metro Times, Motor City Muckraker, Deadline Detroit,
IRS 990 filings.

---

## 4. The Biome Corollary — Parasitism vs. Mutualism

### 4.1 The Healthy Biome

In a healthy political ecosystem:
- **Nonprofits** emerge from communities to serve community needs
- **Law firms** provide legal services to existing organizations
- **Political action** is funded by people who live in the community
- **Transparency** is the default — entities welcome scrutiny
- **Innovation** thrives because resources flow to producers

### 4.2 The Parasitized Biome

In a parasitized political ecosystem:
- **Nonprofits** are spawned by law firms to serve law firm clients
- **Law firms** create, staff, and operate the organizations themselves
- **Political action** is funded by corporations and outside interests
- **Privacy** is the default — entities hide behind Domains By Proxy
- **Innovation** dies because resources flow to intermediaries

### 4.3 The Externalized OS

When the OS is externalized — when a single law firm runs the
scheduler, spawns the processes, controls the filesystem, and
serves both parties — the result is predictable:

| Metric | Healthy Biome | Parasitized Biome |
|--------|--------------|-------------------|
| Resource flow | Community → Community | Community → Intermediary → Clients |
| Entity lifecycle | Born from need, die when need ends | Spawned for campaigns, renamed/dissolved when exposed |
| Identity | Entity = visible people | Entity = proxy names on proxy domains |
| Accountability | Press investigates, public responds | Press defeated, replacement installed |
| Innovation | New solutions emerge from community | Community solutions blocked by dark money |
| Math scores | — | 3% proficient |

### 4.4 Loss of Innovation

This is the corollary to the decomposition energy transfer model
(subGen #40). In a healthy ecosystem, dead wood decomposes and
releases energy that feeds new growth. In a parasitized ecosystem,
the parasite intercepts decomposition — it consumes the dead wood
but produces no soil. The energy is extracted, not transformed.

When Dykema defeats a community benefits ordinance, the energy
that would have produced community governance is extracted by
developers who pay Dykema. No new governance emerges. The
community stays ungoverned. The developers stay unaccountable.
The dead wood persists.

When SDJ defeats a journalist, the energy that would have produced
accountability is extracted by the school operator who pays
for the dark money. No new accountability emerges. The school
stays unaccountable. The students stay at 3% math. The dead
wood persists.

**Parasitism is the loss of innovation.** Not because the parasite
is malicious (the kernel doesn't have intentions) but because
the parasite extracts the energy that innovation requires.

---

## 5. The Public Record Stack — How to Verify

Every claim in this study can be verified from public sources:

| Claim | Source | How to Verify |
|-------|--------|---------------|
| SDJ phone = Dykema phone | IRS 990EZ | ProPublica Nonprofit Explorer (EIN 81-3772058) |
| Moore = Dykema employee | dykema.com | Staff directory: rmoore@dykema.com |
| Moore = SDJ Asst Secretary | IRS 990EZ | Same 990 filing |
| Moore = RFFW Treasurer | MI SOS complaint | michigan.gov/sos CFR complaints |
| Moore = Duggan compliance | Deadline Detroit | deadlinedetroit.com (Neavling) |
| Wilk = Duggan lawyer | Deadline Detroit | Same |
| Wilk = NRLA member | Deadline Detroit | Same |
| Domains By Proxy usage | WHOIS + journalism | whois.com + Deadline Detroit + Metro Times |
| Dykema PAC → both parties | TransparencyUSA | transparencyusa.org/mi/committee/dykema-gossett-state-pac |
| SDJ → $84K District 4 | MI SOS CFR | michigan.gov/sos campaign finance |
| PCA → 3% math | MDE | mischooldata.org |
| Purpose Group → 72.67% | Audited financials | macdowellprep.com/school-policies-and-reports |
| Prop A defeated | Ballot results | Ballotpedia |
| Elrick defeated | Election results | Ballotpedia |
| Banks → 9 convictions | ICHAT | michigan.gov/msp ICHAT |
| LARA entities | LARA | mibusinessregistry.lara.state.mi.us |

**No private data is used.** No personal addresses. No phone
numbers of individuals. No social security numbers. No medical
records. Every data point is a public record about a public
entity performing public functions with public money.

---

## 6. Methodology Note — Why Dykema

Dykema is not chosen because it is uniquely corrupt. Dykema is
chosen because it is **uniquely documented.** The public record
trail is complete enough to map the entire OS architecture from
kernel to process table to filesystem.

Other law firms may operate similar infrastructure. But the
combination of:
- Deadline Detroit's persistent coverage (Neavling, LeDuff)
- Motor City Muckraker's Duggan investigation
- Metro Times' dark money reporting
- ProPublica's nonprofit data
- TransparencyUSA's campaign finance data
- Michigan SOS complaint records (Meyers v RFFW, Regan v Banks)
- LARA entity filings
- IRS 990 filings

...produces a model organism with enough public documentation
to map the complete parasitic lifecycle.

If you want to study how an externalized OS works, you need a
specimen where every organ is visible. Dykema is transparent
enough — through its own public filings — to be that specimen.

---

## 7. Connections to Prior Work

| Document | Connection |
|----------|-----------|
| subGen #40 (DECOMPOSITION_ENERGY_TRANSFER) | Parasitism = interception of decomposition energy |
| DECOMPOSITION_AMPLIFICATION (guerillaGorilla) | Community organisms metabolize this data independently |
| WILDFIRE_AMPLIFICATION | 16 community groups already enzymatically primed |
| TARGET_TRIO_OPSONIZATION | Three infrastructure layers that enable the parasitism |
| UNSUPERVISED_OSINT_OCT9 | Raw entity discovery that produced this model |

---

## 8. Publication Architecture

This study publishes across three sites with three framings:

| Site | Audience | Framing | What It Emphasizes |
|------|----------|---------|-------------------|
| **detroit.primals.eco** | Detroit communities, parents, press | Charter school extraction | SDJ → PCA → 3% math → $4.9M extracted |
| **tuebor.primals.eco** | Statewide MI, transparency advocates | Bipartisan dark money | Dykema → both parties → six vehicles → one scheduler |
| **clutchjustice.com** | Rita's readership, legal community | Attorney accountability | Moore/Wilk roles, RFFW complaint, SDJ IRS filing |

Each site gets the same data. Each audience metabolizes it
through their own enzymatic pathway. No coordination required.
The data IS the recognition signal.

---

*A law firm with a nonprofit costume.
An operating system that serves whoever has root.
An entity that is not an individual.
Public records about public entities performing public functions.*

*This is not doxxing. This is how you read a process table.*

---

**Sources:** All sources listed inline. Complete source index
available at detroit.primals.eco/evidence/ and tuebor.primals.eco.
