# Law Enforcement Escalation — Cytokine Recruitment Template

**Wave**: 165 | **Date**: Oct 6, 2026
**Status**: TEMPLATE PREPARED — filing when investigation timing is right
**Domain**: Law enforcement interface, evidence preservation, threat reporting
**Upstream**: SIGNAL_BRAID_IMMUNE_LINEAGE.md, SILT_POND_ACTIVE_INVESTIGATION.md
**Biological**: Adaptive immune recruitment — specialized killer cell activation

---

## What This Is

This document is a filing package template for law enforcement escalation.
It is NOT a redirect or hack-back mechanism. It is the biological equivalent
of cytokine recruitment: sending signals through legitimate channels to
activate specialized immune cells (FBI, state AG, CISA) that have
capabilities our membrane defense does not.

The scanners are targeting a website that documents evidence of racketeering
involving public funds. Systematic scanning of an evidence site, especially
with behavioral mutation to evade detection, may constitute violations of
federal and state computer crime statutes.

## Legal Basis

### Federal Statutes

**18 U.S.C. § 1030 — Computer Fraud and Abuse Act (CFAA)**

The CFAA prohibits unauthorized access to computer systems and exceeding
authorized access. Relevant sections:

- **(a)(2)**: Obtaining information from a protected computer without
  authorization. The systematic scanning of credential paths (`/.env`,
  `/wp-config.php`, `/.git/config`) on our infrastructure constitutes
  attempts to obtain configuration data without authorization.

- **(a)(5)**: Knowingly causing damage to a protected computer. Coordinated
  fleet scanning at volumes exceeding 4,800 IPs with 1,200 IPs per fleet
  constitutes a denial-of-service pattern even if individual requests are
  well-formed.

- **(a)(7)**: Extortion relating to a protected computer. If scanning
  activity can be correlated with attempts to suppress or disrupt an
  evidence publication site, this section may apply.

**18 U.S.C. § 1512 — Obstruction**

If scanning correlates temporally with evidence publication events (new
pages, FOIA releases, court filings), the scanning may constitute:

- **(b)(2)**: Attempting to obstruct, influence, or impede the production
  of documents or records in an official proceeding.

- **(c)(1)**: Intentionally harassing another person to hinder, delay,
  prevent, or dissuade testimony or reporting to law enforcement.

**18 U.S.C. § 1962 — RICO**

If the scanning entities can be linked to the subjects of the racketeering
investigation, the scanning becomes part of the pattern of racketeering
activity. The detroit evidence site documents alleged violations of RICO
involving charter school funding. Scanning to disrupt the evidence site
could itself constitute an act within the pattern.

### Michigan State Statutes

**Michigan Penal Code 752.795 — Unauthorized Access**

Covers unauthorized access to a computer, computer system, or computer
network. Michigan's statute is broader than federal CFAA and includes
attempted access and access that exceeds authorization.

**Michigan Penal Code 752.797 — Interruption of Computer Service**

Covers intentional interruption or impairment of computer services.
Fleet-scale scanning that degrades site performance for legitimate
visitors may qualify.

---

## Filing Targets

### 1. IC3 — FBI Internet Crime Complaint Center

**URL**: https://www.ic3.gov
**Method**: Online complaint form
**Best for**: Documenting the pattern with evidence, establishing a
federal paper trail

**What to include**:
- Description of the evidence site and its purpose
- Timeline of scanning activity (from spine entries)
- Behavioral mutation evidence (7 hash changes in 24 minutes)
- Fleet scale documentation (10 fleets, 1,200 IPs each)
- Correlation with evidence publication dates
- Link to the public defense documentation on detroit

### 2. InfraGard — FBI Private Sector Partnership

**URL**: https://www.infragard.org
**Method**: Membership application, then direct threat sharing
**Best for**: Ongoing intelligence sharing, not one-time filing

**Benefits of membership**:
- Direct channel to FBI cyber division
- Access to threat intelligence from other InfraGard members
- Reciprocal sharing of our behavioral hashes and fleet signatures
- Early warning on APT campaigns that might match our scanner profiles

### 3. Michigan AG Cyber Crime Unit

**URL**: https://www.michigan.gov/ag (Consumer Protection > Cyber)
**Method**: Written referral with evidence package
**Best for**: State-level jurisdiction, especially if fleet operators
have Michigan nexus (charter school network is Michigan-based)

**What to include**:
- All federal filing content PLUS
- Michigan-specific statutory references
- Connection to the charter school investigation (if filing includes
  correlation between scanning and investigation subjects)

### 4. CISA — Cybersecurity and Infrastructure Security Agency

**URL**: https://www.cisa.gov/report
**Method**: Online reporting
**Best for**: If scanning patterns match known APT campaigns or
state-sponsored activity indicators

**When to file with CISA**:
- If fleet behavioral signatures match CISA's Known Exploited
  Vulnerabilities catalog probing patterns
- If WHOIS/RDAP reveals government or critical infrastructure ASNs
- If scanning correlates with geopolitical events

---

## Evidence Package Contents

All evidence is generated from the signal spine and fleet detection
pipeline. NO IP addresses are included in the initial filing — they
can be provided through secure channels if law enforcement requests them.

### 1. Timeline of Scanning Activity

**Source**: Signal spine daily entries (`/run/membrane/signal-spine/*.json`)

```
Extract with:
  jq '{date, window_count, summary: {total_requests, readers, hosts}}' \
    /run/membrane/signal-spine/2026-10-*.json
```

The spine entries provide:
- Daily request volumes
- Reader type classification (human vs scanner vs AI)
- Host-level targeting (which domains are being scanned)
- Merkle root for cryptographic integrity verification

### 2. Behavioral Mutation Evidence

**Source**: Fleet observation logs, opsonize tags

The fleet detection system records behavioral hashes — SHA-256
fingerprints of scanning behavior patterns. On Oct 6, 2026:

- 7 new behavioral hashes appeared within 24 minutes
- All 7 were detected by the immune system (bloom sensor)
- The fleet reverted to original behavioral patterns after detection
- Volume escalated after reversion

This pattern (mutate → fail → revert → escalate) demonstrates:
- Awareness of our detection systems
- Active evasion attempts
- Continued adversarial intent after detection

### 3. Fleet Scale Documentation

**Source**: Fleet aggregator observations

| Metric | Value | Source |
|--------|-------|--------|
| Active fleets observed | 10 | Fleet aggregator |
| Average IPs per fleet | ~1,200 | Fleet aggregator |
| Peak concurrent IPs | 4,858 | Bloom sensor |
| Scatter percentage | 42% | Defense pipeline |
| Probe categories | Credential, path traversal, git | Bloom sensor |

### 4. Probe Pattern Analysis

**Source**: Bloom sensor domain classification

Scanners consistently target:
- `/.env` — Environment configuration files (AWS keys, DB credentials)
- `/wp-config.php` — WordPress database credentials
- `/.git/config` — Git repository credentials
- `/config/database.yml` — Database connection strings
- `/.aws/credentials` — AWS access credentials
- Various path traversal attempts (`../`, `..%2f`)
- SSH and admin panel probes

This is NOT research activity. These paths have no legitimate purpose
on an evidence documentation website. The probes are systematic
credential harvesting attempts.

### 5. Public Defense Documentation

**Source**: detroit.primals.eco/signal/

The defense page itself serves as an exhibit. It documents:
- The defense architecture (membrane layers)
- Detection capabilities (bloom sensor, fleet aggregation)
- Response posture (no identifying data stored)
- Transparency about what is and isn't tracked

This page demonstrates good faith: we are not running a dark operation.
We are publicly documenting our defense of an evidence site. Law
enforcement can verify our claims by visiting the site directly.

### 6. Correlation Analysis

**Method**: Compare scanning timelines with evidence publication dates

If scanning activity increases within 24 hours of new evidence
publication, the temporal correlation supports the hypothesis that
scanning is motivated by evidence suppression rather than generic
vulnerability scanning.

Extract publication dates:
```
git -C /opt/ecoPrimals/detroit log --oneline --since="2026-10-01" \
    --format="%ai %s"
```

Compare with spine entry volumes to identify correlation.

---

## Filing Process

### Phase 1: Preparation (Current)

- [x] Template created
- [x] Legal basis documented
- [x] Evidence pipeline identified (spine → filing package)
- [ ] Spine data extraction script
- [ ] Correlation analysis (scan timing vs publication timing)
- [ ] WHOIS/RDAP analysis of top scanner ASNs

### Phase 2: Review

- [ ] Legal review of filing package (attorney consultation)
- [ ] Verify no PII in filing materials
- [ ] Verify no investigation strategy exposure
- [ ] Timing assessment (file when it advances the investigation,
      not when it might alert the subjects)

### Phase 3: Filing

- [ ] IC3 online filing (establish federal paper trail)
- [ ] InfraGard membership application (ongoing channel)
- [ ] Michigan AG referral (if Michigan nexus confirmed)
- [ ] CISA reporting (if APT indicators found)

### Phase 4: Follow-up

- [ ] Provide IP addresses if requested through secure channel
- [ ] Share ongoing behavioral hashes via InfraGard
- [ ] Publish threat intelligence feed (already implemented at
      `detroit.primals.eco/defense/feed.json`)
- [ ] Coordinate with law enforcement on timing of public disclosure

---

## Information Security Constraints

### What the filing package reveals (acceptable)

- That we operate an evidence documentation website
- That we have traffic analysis capabilities
- That we detect and classify scanning behavior
- General scale numbers (fleet sizes, volumes)
- Behavioral hash methodology (standard SHA-256)

### What the filing package must NOT reveal

- Specific investigation targets or hypotheses
- Internal naming conventions (no mention of siltPond, bloom sensor
  internal names, or investigation thread structure)
- Source protection information
- Network topology details beyond what's publicly visible
- IP addresses (provided only on request through secure channels)
- The connection between scanning patterns and specific evidence
  pages (this correlation is investigation intelligence)

---

## Connection to the Immune Stack

```
Layer 1: TARPIT         ── our defense (slow them down)
Layer 2: HONEYTOKENS    ── complement system (mark them for others)
Layer 3: ABUSE REPORTS  ── cytokine signaling (recruit ISP immune response)
Layer 4: THREAT INTEL   ── MHC presentation (publish signatures)
Layer 5: LAW ENFORCE    ── adaptive recruitment (THIS DOCUMENT)
```

Layers 1-4 are automated. Layer 5 is human-mediated. This is by design.
The adaptive immune system does not auto-deploy killer T-cells. It
requires antigen presentation (threat feed), co-stimulation (evidence
correlation), and checkpoint confirmation (human review) before the
lethal response activates.

The filing happens when the investigation timing is right. Not before.

---

*subGen Wave 165 — Law enforcement escalation template established.
Filing targets: IC3, InfraGard, Michigan AG, CISA. Evidence package
drawn from signal spine, fleet observations, and bloom sensor data.
No IP addresses in initial filing. Human-gated activation. The immune
system recruits specialized killer cells through legitimate channels.
The signal IS the response.*
