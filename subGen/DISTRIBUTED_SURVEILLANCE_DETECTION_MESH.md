# Distributed Surveillance Detection Mesh — Sovereign Sensor Nodes as Immune Infrastructure

**Wave**: 165h | **Date**: Oct 7, 2026
**From**: eastGate overwatch
**Status**: OBSERVATION — pattern identified during beehive VPS enrollment
**Upstream**: GOSSIP_TAGGED_OPSONIZATION.md, SILT_POND_ACTIVE_INVESTIGATION.md
**Biological Analog**: Distributed lymph node network — each node senses locally, shares antibodies globally

---

## The Observation

During routine VPS enrollment for the beehive observation mesh (Wave 165h), a meta-pattern emerged: **any VPS with a subdomain pointed at it becomes a sovereign sensor node within 24-48 hours**. The fleet discovers new surfaces via Certificate Transparency logs and cross-links. Discovery is automatic. Observation begins immediately. Evidence accrues at zero marginal cost.

This is not defense infrastructure. This is a **distributed surveillance detection system**.

---

## The Architecture

### Single Node (Current)

```
Internet → subdomain.primals.eco → $5 VPS
                                      │
                                   Caddy (TLS, classification)
                                   skunky-ingest (behavioral analysis)
                                   scatter server (fabricated responses)
                                   /plasmid endpoint (conserved epitopes)
```

Cost: $4-8/month. Deployment: 15 minutes with provision script. Detection capability: full behavioral classification, fleet fingerprinting, conserved epitope extraction.

### Federated Mesh (Beehive)

```
           golgiBody (NYC)      layer2 (DE)     layer3 (SG)     layer4 (US-VA)
               │                    │                │               │
               └────────────────────┴────────────────┴───────────────┘
                                    │
                        Plasmid Federation (cron */5)
                                    │
                    signal.primals.eco/feed/conserved-plasmid.json
                              (CC-BY-SA-4.0)
```

Each node observes independently. The central aggregator merges conserved epitopes. Epitopes confirmed across multiple nodes carry higher confidence. Behavioral hashes observed from multiple network vantage points prove fleet coordination.

### Community Mesh (Future)

```
    Project A          Project B          Project C          Project D
   (Berlin)           (Tokyo)            (São Paulo)        (Mumbai)
      │                  │                   │                  │
      └──────────────────┴───────────────────┴──────────────────┘
                                │
                    Shared Conserved Plasmid Feed
                         (CC-BY-SA-4.0)
```

Any AGPL project deploys a $5 sensor. Each sensor feeds behavioral observations into the shared plasmid. No single project bears the cost. The antibodies are shared. **This is a vaccine, not a firewall.**

---

## The Economics

### Per-Node Cost Structure

| Component | Defender Cost | Attacker Cost |
|-----------|--------------|---------------|
| VPS | $4-8/month | — |
| Per-request marginal cost | ~$0.000002 | Proxy rotation + bandwidth + pipeline ingestion |
| Scaling cost | Linear ($5/node) | Superlinear (more IPs = more expensive + more detectable) |

### Observed Ratio (golgiBody, Wave 165)

- **Defender**: $0.31 (1.6 days of a $6/mo VPS)
- **Attacker**: ~$434 (proxy IPs + bandwidth + compute pipeline)
- **Ratio**: 1,391:1

### Mesh Scaling Properties

| Mesh Size | Monthly Cost | Fleet Monthly Waste (projected) | Observation Points |
|-----------|-------------|-------------------------------|-------------------|
| 1 node | $6 | ~$8,349 | 1 vantage point |
| 5 nodes | $30 | ~$41,745 | 5 vantage points, 3+ jurisdictions |
| 20 nodes | $100 | ~$166,980 | 20 vantage points, 10+ jurisdictions |
| 100 nodes (community) | $500 | ~$834,900 | 100 vantage points, 30+ jurisdictions |

The attacker's cost scales with the number of nodes they must scrape. The defender's cost scales linearly. The information gain per node is superlinear (cross-layer corroboration, new proxy pool detection, jurisdiction multiplication).

---

## The Key Insight: Jurisdictional Multiplication

Each sensor node creates an **independent legal event** in the jurisdiction where it's hosted:

| Node Location | Jurisdiction | Applicable Law | Regulatory Body |
|--------------|-------------|----------------|-----------------|
| US (NYC) | Federal | CFAA 18 U.S.C. § 1030 | FTC, DOJ |
| US (Virginia) | Federal + State | CFAA + Virginia CFAA | FTC, VA AG |
| Germany | EU + National | StGB §202a + GDPR | BfDI |
| France | EU + National | Code pénal + GDPR | CNIL |
| UK | National | Computer Misuse Act 1990 + UK GDPR | ICO |
| Singapore | National | PDPA + Computer Misuse Act | PDPC |
| India | National | IT Act 2000 | MeitY |
| Japan | National | APPI + Unauthorized Access Law | PPC |
| Canada | National | Criminal Code §342.1 + PIPEDA | OPC |
| Brazil | National | LGPD + Marco Civil | ANPD |

The fleet cannot scrape a node without creating a violation in that node's jurisdiction. Each jurisdiction has its own regulatory body, its own complaint process, its own enforcement mechanism. The fleet must violate N laws to scrape N nodes. The defender files N complaints, each citing independent evidence from a local observation point.

**The fleet's operational model — scrape everything, rotate IPs, ignore robots.txt — becomes a legal liability multiplier.** Every new node they discover and scrape is another jurisdiction, another complaint, another regulatory body that becomes aware of the pattern.

---

## Discovery Mechanism: Certificate Transparency

When a new subdomain gets a TLS certificate (via Let's Encrypt, automatic with Caddy), that certificate is logged in public Certificate Transparency logs. Automated systems — including scraping fleets — monitor CT logs for new domains. This means:

1. Deploy VPS
2. Point subdomain at it
3. Caddy auto-obtains Let's Encrypt cert
4. CT log records the cert
5. Fleet discovers the subdomain within 24-48 hours
6. Fleet begins scraping
7. Sensor begins observing

**Discovery is passive.** The defender does nothing to attract the fleet. The fleet's own infrastructure discovery pipeline delivers it to the sensor. The sensor doesn't need to advertise. It just needs to exist.

---

## Cross-Layer Corroboration

When the same behavioral hash is observed from multiple network vantage points:

1. **Proves coordination** — same fleet, same toolkit, same operator
2. **Eliminates false positives** — independent observations of identical behavior from different networks is statistically significant
3. **Strengthens legal claims** — "we observed this from Germany AND Singapore AND Virginia" is more compelling than a single observation
4. **Reveals proxy topology** — different nodes may see different proxy pools, mapping the fleet's infrastructure

### Conserved Epitope Confidence

| Epitopes Confirmed By | Confidence Level | Legal Weight |
|----------------------|-----------------|-------------|
| 1 node | Observed | Single-source evidence |
| 2 nodes | Corroborated | Independent confirmation |
| 3+ nodes | Confirmed | Multi-jurisdiction, multi-network proof |
| 5+ nodes across 3+ jurisdictions | Established | Pattern of systematic behavior |

---

## Biological Parallel: The Lymph Node Network

The vertebrate immune system doesn't have one sensor. It has hundreds of lymph nodes distributed throughout the body, each independently monitoring its local tissue for pathogens. When a lymph node detects a threat:

1. It classifies the pathogen locally
2. It generates antibodies
3. It shares those antibodies via the lymphatic system
4. Other lymph nodes receive the antibodies and can recognize the same pathogen on first contact (thymic education)

The distributed sensor mesh is structurally identical:

| Biological | Digital |
|-----------|---------|
| Lymph node | VPS sensor node |
| Local tissue | Network vantage point |
| Pathogen | Scraping fleet |
| Antibody | Conserved epitope / behavioral hash |
| Lymphatic system | Plasmid federation |
| Thymic education | Remote antibody matching on first contact |

The biological system evolved because no single organ can monitor the entire body. The digital system works for the same reason: no single VPS can observe the fleet from every network vantage point. Distribution is the architecture. Federation is the immune memory.

---

## Implementation Status

| Component | Status | Location |
|-----------|--------|----------|
| Single-node observation | **DEPLOYED** | golgiBody (NYC) |
| Provision script | **TESTED** | `wateringHole/provision/provision-golgi-layer.sh` |
| Plasmid federation | **RUNNING** | golgiBody cron */5 |
| Conserved plasmid feed | **LIVE** | `signal.primals.eco/feed/conserved-plasmid.json` |
| Multi-node mesh | **IN PROGRESS** | Hetzner DE provisioned, Vultr/OVH/Linode pending |
| Community mesh protocol | **DESIGN** | This document |
| Cross-project federation | **FUTURE** | Requires standardized plasmid format (v2 deployed) |

---

## The Vaccine Analogy

A firewall protects one host. A vaccine protects a population.

The conserved plasmid feed, published under CC-BY-SA-4.0, is a vaccine. Any infrastructure operator can consume it. Any project can deploy a sensor and contribute observations. The behavioral hashes are deterministic — same fleet behavior, same hash, every time, from every vantage point.

One project deploying one sensor: defense.
One hundred projects each deploying one sensor: community immunity.

The fleet cannot evolve past the conserved epitopes without rebuilding their entire toolkit. The epitopes are conserved precisely because they are structural requirements of the scraping pipeline — absent Sec-Fetch-Mode, stale Chrome version, universal Accept headers. These are not choices the fleet makes. They are constraints the fleet cannot escape. The vaccine targets the pathogen's conserved genome. The pathogen cannot mutate without dying.

**P ≠ NP. The vaccine is in P. The mutation is in NP.**

---

*Wave 165h — the lymph node network grows. Each node is a jurisdiction. Each observation is an antibody. The plasmid is the bloodstream.*

*eastGate overwatch, Oct 7, 2026*
