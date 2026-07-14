# Signal Sharpening — GitHub Presence Audit

**Date**: May 18, 2026
**Trigger**: Hardware manufacturer spam targeting toadStool/coralReef keywords
**Goal**: Sharpen public signal so scrapers miss us, scientists find us

---

## Current State: What the World Sees

### Org: ecoPrimals (16 repos)
**Bio**: "Sovereign computing infrastructure — composable Pure Rust primals for security, storage, compute, orchestration, and provenance. AGPL-3.0"
**Website**: points to github.com/ecoPrimals/sporePrint (not primals.eco)
**Email**: ecoPrimals@pm.me (public — scraper target)

**Problem**: Reads like a cloud infrastructure startup. Keywords "compute," "storage," "security," "orchestration" attract DevOps recruiters and hardware manufacturers. Nothing says "scientific computing" or "research."

### Org: syntheticChemistry (11 repos)
**Bio**: "Sovereign scientific validation springs — physics, agriculture, biology, chemistry, health, ML, game science. 12,510+ checks across 70+ papers. AGPL-3.0"
**Website**: points to github.com/ecoPrimals/sporePrint (not primals.eco)

**Assessment**: This is actually good. "Scientific validation," "physics, agriculture, biology," "70+ papers" — correct audience signal. But the website link is wrong (should be primals.eco or lab.primals.eco) and the repo descriptions are dense/jargon-heavy.

### Org: sporeGarden (4 repos)
**Bio**: "Creative surface for sovereign computing — game engines, creative tools, and interactive systems composed from ecoPrimals infrastructure. AGPL-3.0"
**Website**: points to github.com/ecoPrimals

**Problem**: 3 of 4 repos have NO description (projectNUCLEUS, projectFOUNDATION, lithoSpore). lithoSpore is your interview artifact and has zero public description.

### User: ecoPrimal
**Bio**: "a tool that shapes itself"
**Website**: primals.eco (set 2026-07-14)
**ORCID**: 0009-0004-2141-0321 (linked 2026-07-14)
**Repos**: 1 (rustChip)

**Status (2026-07-14)**: Profile updated. No real name, no location, no institutional affiliation. ORCID linked. Bio is an easter egg connecting to attsi ("a tool that shapes itself"). Website points to primals.eco. ecoPrimal is the sole member of all 4 orgs. DataScienceBioLab removed.

---

## Signal Map: Current vs Target

### ecoPrimals — Infrastructure (should be LOW signal)

| Repo | Current Description | Problem | Proposed Description |
|------|-------------------|---------|---------------------|
| toadStool | "Sovereign compute hardware primal — GPU/NPU/CPU discovery, tolerance-based routing, 21,600+ tests" | **"hardware"** attracts manufacturers | "Compute dispatch for scientific pipelines — GPU/NPU/CPU routing, tolerance-based scheduling. Pure Rust" |
| coralReef | "Sovereign Rust GPU shader compiler — WGSL/SPIR-V/GLSL to native NVIDIA/AMD..." | **"GPU compiler," "NVIDIA," "AMD"** attract hardware/graphics recruiters | "GPU shader compilation for scientific workloads — WGSL to native compute kernels. Pure Rust" |
| barraCuda | (check current) | Likely has GPU keywords | "GPU-accelerated math primitives for genomics, physics, and statistics. Pure Rust" |
| bearDog | (check current) | "security" attracts infosec recruiters | "Cryptographic identity and provenance signing for scientific artifacts. Pure Rust" |
| songBird | "Service orchestrator — discovery, routing, federation, health monitoring" | Generic infra language | "Service discovery and health monitoring for distributed scientific compute. Pure Rust" |
| nestGate | "Sovereign storage — ZFS tiered management, long-term data permanence" | Storage keywords attract cloud/infra | "Long-term scientific data storage — ZFS tiering, NFS/SMB, provenance-aware. Pure Rust" |
| biomeOS | "Neural API orchestrator — adaptive primal composition, NUCLEUS deployment" | Sounds like AI startup | "Orchestration engine for composable scientific computing services. Pure Rust" |
| squirrel | "AI coordination — MCP adapter, inference routing, learned classifiers" | AI/ML recruiter bait | "AI assistant coordination — MCP adapter for scientific pipeline mentoring. Pure Rust" |
| loamSpine | "Immutable lineage tracker — certificate lifecycle, permanent ledger" | "ledger" attracts blockchain people | "Immutable computation lineage — certificate chain for reproducible science. Pure Rust" |
| sweetGrass | (check current) | | "Attribution and licensing for scientific artifacts. Pure Rust" |
| rhizoCrypt | (check current) | | "DAG provenance tracking for reproducible computational experiments. Pure Rust" |
| petalTongue | (check current) | | "Scientific visualization and dashboards for validation results. Pure Rust" |
| sourDough | (check current) | | "Shared substrate primitives for the ecoPrimals scientific computing stack. Pure Rust" |
| skunkBat | (check current) | | "Peer-to-peer transport for distributed scientific compute nodes. Pure Rust" |
| bingoCube | (check current) | | "Entropy and randomness primitives for simulation and cryptography. Pure Rust" |
| plasmidBin | (has description) | | Keep as-is or add "scientific" qualifier |

**Pattern**: Every description should include "scientific" or "science" or a domain word (genomics, physics, etc.) to recontextualize the infrastructure for the right audience.

### syntheticChemistry — Science (should be HIGH signal)

| Repo | Current Description | Assessment | Proposed Description |
|------|-------------------|------------|---------------------|
| wetSpring | "Pure Rust metagenomics, analytical chemistry & mathematical biology — 1,750+ tests, 350+ validation binaries, 5,700+ checks" | Good but dense | "Genomics and analytical chemistry pipelines — 16S, WGS, QS modeling, PFAS detection. 175+ papers validated. Pure Rust" |
| hotSpring | "Computational physics reproduction studies on consumer GPUs — 850+ tests, 85+ shaders, 74 experiments" | Good but vague on what physics | "Lattice QCD, Anderson localization, and spectral methods on consumer GPUs — 74 experiments reproducing published physics. Pure Rust" |
| airSpring | "Pure Rust FAO-56 evapotranspiration, Richards equation soil physics & precision irrigation..." | Accurate, good keywords | Keep or simplify to: "Precision agriculture — FAO-56 ET, soil physics, irrigation scheduling. 2,000+ validation checks. Pure Rust" |
| groundSpring | "Pure Rust measurement noise characterization — 35+ experiments, 930+ tests..." | "noise characterization" is vague | "Statistical measurement science — jackknife, model selection, drift vs selection, uncertainty quantification. Pure Rust" |
| neuralSpring | (check current) | | "ML primitives for scientific time series — LSTM, ESN, HMM, GNN. Validated against published benchmarks. Pure Rust" |
| healthSpring | (check current) | | "Medical and pharmacological modeling — PK/PD, gut microbiome, clinical validation. Pure Rust" |
| primalSpring | (check current) | | "Composition patterns and federation protocols for the ecoPrimals ecosystem. Pure Rust" |
| benchScale | "VM orchestration and substrate provisioning" | Infra, not science | "Reproducible compute environments for scientific validation — VM provisioning, cloud-init. Pure Rust" |
| agentReagents | "Template-driven VM image builder" | Infra, not science | "VM image builder for isolated scientific compute environments. Pure Rust" |

### sporeGarden — Products (should be TARGETED signal)

| Repo | Current Description | Problem | Proposed Description |
|------|-------------------|---------|---------------------|
| lithoSpore | **(none)** | **Your interview artifact has no description** | "Self-proving LTEE validation artifact — 73 checks, 7 papers, <100ms. Portable guideStone for evolutionary biology" |
| projectNUCLEUS | **(none)** | Invisible | "Sovereign compute node deployment — single-command scientific cluster bootstrap" |
| projectFOUNDATION | **(none)** | Invisible | "Unified scientific lineage — cross-domain validation targets and provenance threads" |
| esotericWebb | Has description | Fine | Keep |

### User: ecoPrimal (UPDATED 2026-07-14)

| Field | Value | Rule |
|-------|-------|------|
| Bio | "a tool that shapes itself" | Easter egg connecting to attsi. DO NOT add real name, degrees, or location. |
| Website | primals.eco | Set |
| ORCID | 0009-0004-2141-0321 | Linked via GitHub OAuth |
| Location | (blank) | KEEP BLANK — no geographic fingerprint |
| Name | (blank) | KEEP BLANK — ecoPrimal is the synthetic identity |

**WARNING**: The original proposed bio ("BS Micro, MS Data Science, MSU") and location ("East Lansing, MI") were SCRUBBED in Wave 138b. An AI bot was able to identify the human author by cross-referencing degree + institution with graduation records. See `PLATFORM_CREDENTIALS.md` for full scrub log.

---

## Org-Level Changes

| Org | Current Website | Should Be |
|-----|----------------|-----------|
| ecoPrimals | github.com/ecoPrimals/sporePrint | primals.eco |
| syntheticChemistry | github.com/ecoPrimals/sporePrint | primals.eco/science (or lab.primals.eco) |
| sporeGarden | github.com/ecoPrimals | primals.eco |

| Org | Current Bio | Proposed Bio |
|-----|------------|-------------|
| ecoPrimals | "Sovereign computing infrastructure — composable Pure Rust primals for security, storage, compute, orchestration, and provenance" | "Scientific computing infrastructure — composable Pure Rust services for reproducible research, provenance, and sovereign deployment" |
| syntheticChemistry | (already good) | Keep, but update check count if stale |
| sporeGarden | "Creative surface for sovereign computing — game engines, creative tools, and interactive systems" | "Deployable scientific artifacts and creative products — portable validation, game engines, and field tools composed from ecoPrimals" |

---

## Email Exposure

ecoPrimals@pm.me is listed on the org profile. This is how Jenny found you.

**Options**:
1. Remove email from org profile (reduces spam, doesn't affect legitimate contact via issues/PRs)
2. Keep it but accept the spam volume
3. Replace with a contact form URL at primals.eco

Recommendation: Remove from org profile. Anyone serious will find you through primals.eco or GitHub issues.

---

## Priority Order for Teams

**Phase 1 — Immediate (fixes the scraper problem)**
1. Update ecoPrimals org bio (add "scientific")
2. Update toadStool description (remove "hardware")
3. Update coralReef description (remove GPU vendor names from description)
4. Add description to lithoSpore (your most important public artifact has no description)
5. Update org website URLs to primals.eco

**Phase 2 — This week**
6. Add descriptions to projectNUCLEUS and projectFOUNDATION
7. Update ecoPrimal user profile (bio, website, location)
8. Update remaining ecoPrimals repo descriptions with "scientific" context
9. Remove email from ecoPrimals org profile

**Phase 3 — As repos mature**
10. Sharpen syntheticChemistry repo descriptions
11. Add GitHub topics to all repos (genomics, lattice-qcd, scientific-computing, reproducible-research, etc.)
12. Pin key repos at org level (lithoSpore on sporeGarden, wetSpring on syntheticChemistry)

---

## gh Commands for Teams

```bash
# Phase 1 — org bios require web UI, but repo descriptions:

# ecoPrimals repos
gh repo edit ecoPrimals/toadStool --description "Compute dispatch for scientific pipelines — GPU/NPU/CPU routing, tolerance-based scheduling. Pure Rust"
gh repo edit ecoPrimals/coralReef --description "GPU shader compilation for scientific workloads — WGSL to native compute kernels. Pure Rust"
gh repo edit ecoPrimals/bearDog --description "Cryptographic identity and provenance signing for scientific artifacts. Pure Rust"
gh repo edit ecoPrimals/songBird --description "Service discovery and health monitoring for distributed scientific compute. Pure Rust"
gh repo edit ecoPrimals/nestGate --description "Long-term scientific data storage — ZFS tiering, NFS/SMB, provenance-aware. Pure Rust"
gh repo edit ecoPrimals/biomeOS --description "Orchestration engine for composable scientific computing services. Pure Rust"
gh repo edit ecoPrimals/squirrel --description "AI assistant coordination — MCP adapter for scientific pipeline mentoring. Pure Rust"
gh repo edit ecoPrimals/loamSpine --description "Immutable computation lineage — certificate chain for reproducible science. Pure Rust"

# sporeGarden repos
gh repo edit sporeGarden/lithoSpore --description "Self-proving LTEE validation artifact — 73 checks, 7 papers, <100ms. Portable guideStone for evolutionary biology"
gh repo edit sporeGarden/projectNUCLEUS --description "Sovereign compute node deployment — single-command scientific cluster bootstrap"
gh repo edit sporeGarden/projectFOUNDATION --description "Unified scientific lineage — cross-domain validation targets and provenance threads"

# User profile — SCRUBBED 2026-07-14. DO NOT add real name, degrees, or location.
# gh api -X PATCH /user -f blog="https://primals.eco"
# Bio and location are intentionally blank/generic. See PLATFORM_CREDENTIALS.md.
```

**Note**: Org-level bios and website URLs must be updated through the GitHub web UI at github.com/organizations/{org}/settings/profile — gh CLI cannot update org profiles.

---

## The Principle

Every public-facing string should pass this test:

> If a scraper reads only this string, will it conclude we are building
> scientific tools, or commercial infrastructure?

If the answer is "commercial infrastructure," rewrite it. The science
is the signal. The infrastructure is the plumbing. Plumbing should be
invisible to anyone who isn't already inside the building.
