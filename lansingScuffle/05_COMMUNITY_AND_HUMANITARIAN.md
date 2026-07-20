# Community and Humanitarian — Preparing Rooms for People Who Need Them

**Date**: Jul 20, 2026
**Status**: Concept — service model projected from SOVEREIGN_PALLET + THE_MANY_ROOMS
**Lineage**: gen3/atlasHugged/09_THE_MANY_ROOMS → gen5/products/SOVEREIGN_PALLET → gen4/knome/ → 00_THE_SCUFFLE
**Wave**: 150

---

## Thesis

> Someone goes ahead. Into territory that is not yet habitable.
> The preparer does not own the house. The work is not creation. It is
> preparation.
> — 09_THE_MANY_ROOMS.md

> The highest charity is the charity that ends the need for charity.
> A loan. A partnership. A job. A tool. A skill.
> — Maimonides, Level 8 tzedakah (via THE_MANY_ROOMS)

Community is structural, not decorative. Hot water for the unhoused is
not charity bolted onto a tech project — it is architecture. The
building's thermal system produces hot water as a natural byproduct of
computation. The building's mesh produces connectivity as a natural
byproduct of networking. The building's science produces mentoring
opportunities as a natural byproduct of research.

The humanitarian and community services described here are not a
separate project. They are what the building's energy loop, network,
and science pipeline produce when designed correctly.

---

## Humanitarian Services — No Credentials Required

These services are extracellular: they face outward, they require no
membership, no ID, no credentials. They are always available.

### Hot Water Station

| Attribute | Specification |
|-----------|--------------|
| Source | GPU waste heat → sand storage → water heater |
| Temperature | 40-50°C (comfortable, safe for hand-washing and hygiene) |
| Availability | 24/7 |
| Access | Street-accessible, no entry requirements |
| Uses | Hand-washing, hygiene, container fill, cooking prep |
| Capacity | ~1,500 liters/hour at 30 kW GPU heat (see 02_THERMAL_SOVEREIGNTY) |

From SOVEREIGN_PALLET: "phones are housing applications, benefits, jobs,
family." A person who can wash their hands, clean their face, and fill a
thermos with hot water has dignity. Dignity is not a luxury.

### Phone Charging

| Attribute | Specification |
|-----------|--------------|
| Ports | 12+ USB-A/C ports, outdoor-rated enclosure |
| Power | Solar + grid (always available) |
| Availability | 24/7 |
| Security | Locked cable loops (prevent theft of charging cables) |
| Notes | No personal data collection. No app required. Plug in, charge, leave. |

A dead phone is a disconnection from housing applications, benefits
offices, job callbacks, family, and emergency services. Charging is
infrastructure, not a favor.

### Open WiFi

| Attribute | Specification |
|-----------|--------------|
| SSID | Open (no password, no captive portal) |
| AP | Mesh AP in humanitarian zone, fed by building backbone |
| Bandwidth | Shared, rate-limited per client (~10 Mbps) |
| Data collection | None. No DNS logging. No session tracking. |
| Availability | 24/7 |

From THE_NEW_CITY: "Ethics as architecture: there is no mechanism for
exploitation." The WiFi does not harvest data. It does not require an
email address. It does not show ads. It provides connectivity.

### Warming Center (Winter)

| Attribute | Specification |
|-----------|--------------|
| Heat source | Sand battery discharge (see 02_THERMAL_SOVEREIGNTY) |
| Capacity | 20-50 people (benches, not beds — daytime warming) |
| Hours | Extended hours during cold weather events |
| Services | Hot water, charging, WiFi, seating, restroom access |
| Requirements | None. Walk in. |

Michigan winters are dangerous. A warming center powered by sand
batteries that charged all summer from GPU heat is the thermal
sovereignty thesis applied to the most vulnerable population.

### Community Kitchen

| Attribute | Specification |
|-----------|--------------|
| Equipment | Commercial range/oven, refrigeration, prep surfaces |
| Food source | Rooftop gardens (primary) + community food donations |
| Availability | Scheduled hours (lunch, dinner) |
| Access | Low-barrier (walk in, eat) |
| Model | Community-operated, volunteer-staffed |

Food from the roof goes to the kitchen. The kitchen feeds the community.
The community gardens on the roof. The loop closes.

---

## Sovereign Identity for the Unhoused

From SOVEREIGN_PALLET — the biometric identity model:

```
Person approaches station
    → biometric enrollment (fingerprint/palm vein/voice)
    → biometric hash = encryption key (never stored as biometric)
    → encrypted data blob stored in mesh (replicated across gates)
    → ANY station in the mesh can retrieve their data
    → ONLY the person can decrypt their data
```

| Current Problem | Sovereign Solution |
|----------------|-------------------|
| Paper SSN cards get lost/stolen/swept | Biometric key — the person IS the credential |
| Every sweep restarts all applications | Data replicates across mesh — survives destruction |
| Service providers can't verify without ID | Biometric at any station → verified identity |
| Centralized databases = honeypot targets | Distributed, encrypted, no single point of compromise |
| "The system lost my paperwork" | The person holds the data. The system doesn't store it. |

Implementation uses bearDog encrypted identity — the same cryptographic
identity system used by the rest of the ecosystem. An unhoused person's
data gets the same cryptographic protections as a faculty collaborator's
research dataset. No second-class identities.

---

## Community Services — Membership-Based

These services are outer membrane: they face the community but require
some form of membership, reservation, or training.

### K-NOME Mentoring Rooms

From gen4/knome/ — massively parallel mentoring:

| Attribute | Specification |
|-----------|--------------|
| Rooms | 2-4 mentoring rooms, each with workstation + display |
| Model | K-NOME: one human mentors multiple AI conversations in parallel |
| Access | Scheduled sessions, open enrollment |
| Target | Anyone curious — high school students, career changers, retirees |
| Tools | Cursor IDE, RustDesk access to compute gates, AGPL tools |

K-NOME's core insight: the human never typed code. The conversation is
the interface. A domain expert can tend parallel AI conversations
producing validated tools without writing code. The mentoring rooms
teach this methodology — and every mentoring session is itself a
contribution to the ecosystem (sweetGrass attributed).

From THE_MANY_ROOMS: "The highest charity is the charity that ends the
need for charity." K-NOME doesn't teach people to use tools. It teaches
people to build tools — and that skill propagates.

### Makerspace

| Attribute | Specification |
|-----------|--------------|
| Equipment | 3D printers (FDM + resin), CNC router, laser cutter, electronics bench, soldering |
| Access | Community membership ($25-50/month) or day pass |
| Safety | Orientation required for power tools |
| Projects | Personal, community, ecosystem (sensor enclosures, pallet housing, etc.) |

The makerspace serves both the community and the ecosystem. Community
members build personal projects. The ecosystem builds sensor enclosures
for airSpring, cases for NUCs, mounting brackets for mesh antennas.

### Co-Working Space

| Attribute | Specification |
|-----------|--------------|
| Desks | Hot desks (drop-in) and reserved desks |
| Access | Community membership |
| Network | Building backbone, not the open WiFi |
| Use | Remote workers, freelancers, students, ABG members |

### Event Space

| Attribute | Specification |
|-----------|--------------|
| Capacity | 50-100 people |
| Uses | ABG meetings, community science talks, art shows, film screenings |
| AV | Projector, sound system, streaming capability |
| Access | Reservation (community and external) |

### ABG Citizen Science

The Autonomous Biology Group moves from Discord to physical space:

- Weekly meetings in the event space
- Hands-on bench work in the wet lab
- Compute access through K-NOME rooms
- Results published through the ecosystem's provenance chain
- Community members doing real science, not volunteer theater

---

## Integration with Building Systems

Every community service connects to the building's infrastructure:

| Service | Energy | Network | Science |
|---------|--------|---------|---------|
| Hot water station | GPU heat → sand → water | — | — |
| Phone charging | Solar + grid | — | — |
| Open WiFi | — | Mesh AP (humanitarian) | — |
| Warming center | Sand battery discharge | — | — |
| Community kitchen | Grid (cooking) | — | Rooftop garden data → airSpring |
| K-NOME rooms | Grid (workstations) | Building backbone | sweetGrass attributed |
| Makerspace | Grid (tools) | Building backbone | Ecosystem hardware production |
| Co-working | Grid (desks) | Building backbone | — |
| Event space | Grid (AV) | Building backbone + streaming | ABG publications |

---

## Implementation Phases

| Phase | Community Services |
|-------|-------------------|
| **Year 1** (beachhead) | Open WiFi AP in suite. Phone charging station (USB hub). Hot water pilot (electric, not GPU-heated yet). |
| **Year 2** (expansion) | K-NOME mentoring room (1). Makerspace pilot (3D printer + electronics). ABG physical meetings. GPU hot water connection. |
| **Year 3** (operations) | Full K-NOME suite (3 rooms). Makerspace expanded. Warming center operational. Community kitchen from rooftop produce. |
| **Year 4-5** (campus) | Full event space. Co-working. Sovereign identity station. All humanitarian services GPU-heated and 24/7. |

---

## References

| Document | Contribution |
|----------|-------------|
| `gen3/atlasHugged/09_THE_MANY_ROOMS.md` | Preparing rooms philosophy, Maimonides Level 8, Samaritan structural lesson |
| `gen3/atlasHugged/03_THE_NEW_CITY.md` | Architecture as ethics — no mechanism for exploitation |
| `gen5/products/SOVEREIGN_PALLET.md` | Biometric identity model, humanitarian services at pallet scale |
| `gen4/knome/` | K-NOME mentoring methodology — massively parallel, conversation-only |
| `gen4/knome/MASSIVELY_PARALLEL_MENTORING.md` | How K-NOME runs at scale |
| `gen3/baseCamp/19_games_at_home_distributed_human_computation.md` | Community compute as Games@Home |
