# For Researchers

**How Scientists Use Sovereign Compute for Real Science**

**Date**: May 7, 2026
**Audience**: Bioinformaticians, field scientists, computational researchers,
lab PIs, grad students, research communities (ABG and beyond)

---

## What You Get

### Compute Without a Queue

No Slurm queue. No allocation proposal. No PI signature. No 30-day
scratch purge. You get a configured node — dedicated or shared — with
the hardware shape your workload needs. CPU-heavy alignment? 64-core
EPYC with 256 GB ECC. GPU genomics? RTX 3090 or better. Bulk storage?
76 TB cold or NVMe scratch. The operator configures the node per
project.

### Data Provenance From Day One

Every dataset you fetch — from NCBI, GEO, UniProt, KEGG, PDB, or
anywhere public — gets BLAKE3-hashed at download. The hash is stored
in NestGate (content-addressed storage). The fetch event is recorded
in a rhizoCrypt DAG. Before you run a single analysis, your data
already has a provenance chain anchored to the public repository.

When reviewers ask "where did you get this data?" you don't point at
a Methods section. You point at a hash chain.

### Reproducibility That's Structural

Your analysis pipeline runs through toadStool, which dispatches
workloads with full resource tracking. Inputs, outputs, compute time,
hardware used — all recorded. The complete chain from "NCBI genome
download" to "final figure" is a Merkle tree you can hand to anyone.

They don't have to trust your Methods section. They can re-run the
pipeline and verify the hashes match.

### Attribution That Propagates

sweetGrass braids record who did what: who collected the sample, who
built the pipeline, who ran the analysis, who wrote the paper, who
provided the compute. If someone builds on your work in year 3, the
braid traces back to you automatically. No citation counting. No
h-index games. Structural credit.

---

## How It Works

### 1. You Describe What You Need

Data source (GEO, SRA, NCBI), approximate download size, compute
shape (CPU cores, RAM, GPU), storage type (fast scratch or bulk).

### 2. The Operator Configures a Node

Hardware is physically configured — GPU cards move between machines,
HDDs attach where needed, environments set up. This is not a VM
spinning up in a cloud. It's a physical node with real hardware
dedicated to your workload.

### 3. You Work in JupyterHub

Standard Jupyter environment. Python, R, Rust, whatever your
pipeline needs. Shared workspace visible to all group members.
Individual credentials.

### 4. Provenance Forms Underneath

You don't have to do anything special. The infrastructure BLAKE3-hashes
your downloads, records your compute dispatches, and builds the
provenance DAG. When you're ready to publish, the chain exists.

### 5. You Publish Under scyBorg

Your paper is CC-BY-SA (openly readable, attributable). Your code is
AGPL (openly usable, modifications shared back). Your methods are ORC
(openly applicable). You can still submit to any journal — scyBorg
doesn't prevent that. It ensures the reproducible version exists
alongside the journal PDF.

---

## What It Costs

Nothing. The compute is offered through the ecoPrimals flywheel — a
community-supported model where the infrastructure's metabolic costs
(electricity, hardware, operator time) are covered by supporters who
see value in open sovereign science.

If you want to support the ecosystem in return, contributions are
welcome but never required: monetary support, hardware donations,
or sweat equity (science, documentation, outreach). Every contribution
gets a Loam Certificate — a permanent, provenance-tracked record of
what you gave and what it enabled.

See `gen4/economics/THE_FLYWHEEL.md` for the full economic model.

---

## The scyBorg License

All work on the infrastructure is published under scyBorg:

| License | Covers | What It Means |
|---------|--------|--------------|
| AGPL-3.0 | Code | Anyone can use it; modifications shared back |
| ORC | Methods | System mechanics are unownable |
| CC-BY-SA 4.0 | Docs / papers | Freely shareable with attribution |

**What scyBorg protects you from:**
- The infrastructure operator can't take your work private
- Other group members can't scoop without attribution
- Commercial entities can't extract your methods into closed products
- Nobody can enclose what the community produces

**What scyBorg does NOT restrict:**
- Publishing in any journal (CC-BY-SA allows republication)
- Using what you learn in your career, your lab, your company
- Getting full credit for your contributions
- Building commercial services on top (the code stays open; your service is yours)

scyBorg is mutual protection: everyone bound equally, nobody extracting
disproportionately.

---

## The Foundation

The scientific knowledge layer (`sporeGarden/foundation`) declares what
to validate and where the data lives:

- **Data source manifests** — NCBI accessions, UniProt IDs, KEGG pathways,
  PDB structures, with BLAKE3 hashes and retrieval URLs
- **Validation targets** — Published numerical results with tolerances,
  linked to specific papers and springs
- **Thread organization** — 10 domain threads (whole-cell modeling, plasma
  physics, immunology, environmental genomics, etc.)

Your research contributes to the foundation as **sediment layers**:
validated results with full provenance that strengthen the geological
record over time. See `gen4/foundations/LIVING_GEOLOGY.md` for the
accumulation model.

---

## Current Availability

| Resource | Status |
|----------|--------|
| JupyterHub | Live at lab.primals.eco |
| Dedicated ABG node (ironGate) | i9-14900K, RTX 5070, 96 GB DDR5 |
| Heavy compute (strandGate) | 64-core EPYC, 256 GB ECC, RTX 3090 |
| Cold storage | 76 TB ZFS |
| GPU float pool | 2× RTX 3090, 2× Titan V, 2× MI50 |
| Foundation pipeline | Operational (fetch + validate + provenance) |

Hardware is reconfigurable per project. Don't be shy on requests.

---

## Sovereign Allies

The ecoPrimals ecosystem maintains relationships with organizations
that share the sovereignty principle — entities that resist capture
by external commercial or political pressure:

| Ally | Why Sovereign | Relevance |
|------|--------------|-----------|
| **Valve / Steam** | Privately held, no shareholders to appease. Invested in Linux (Proton, SteamOS), Vulkan, open standards. Won't bend to Microsoft or Apple. | 132M users with GPUs; potential volunteer compute; same Vulkan substrate |
| **System76** | Pure Rust firmware (Pop!_OS, coreboot). AGPL-aligned. Hardware sovereignty. | Potential hardware partner for pre-configured research nodes |
| **BrainChip** | Neuromorphic NPU (AKD1000). Event-driven, 10 mW inference. | Edge compute for field science (autonomous landers, remote monitoring) |
| **NCBI / NIH** | Public data mandate. Federally funded, open access. | Provenance chain anchors; the bedrock of the foundation |

These are not business partnerships. They are structural alignments —
organizations whose incentives don't conflict with open science and
whose platforms can't be arbitrarily revoked.

---

*The queue is empty. The node is configured. The provenance forms
automatically. Bring your science.*
