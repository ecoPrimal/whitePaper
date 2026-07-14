# Composition Routing Pattern — Live Data Compositions via Drawbridge

**Wave 138a — July 14, 2026**

---

## What This Document Is

This describes how protoKarya projects and other live compositions
register as drawbridge capabilities, receive public subdomains via
wildcard DNS, and cross-feed each other through the sovereign data
mesh. This is the gen5 deployment model: compositions are not static
artifacts — they are live services that consume primal capabilities,
ingest external data through drawbridge weak bonds, and expose their
results as new capabilities for other compositions to consume.

---

## The Pattern

Every live composition follows the same arc:

```
1. Data enters through drawbridge weak bonds
   (USGS, ArcGIS, NF Data Portal, LINCS, PubMed, etc.)

2. Data lands in NestGate CAS
   (content-addressed, BLAKE3 integrity, Loam Certificate provenance)

3. Primals process the data
   (barracuda math, helixVision expression, healthSpring PK)

4. Composition exposes results as drawbridge capabilities
   (capability.call from any mesh node)

5. Other compositions consume those capabilities
   (cross-feeding: footPrint GIS → NF spatial, tideGlass compounds → healthSpring)

6. Public face via *.primals.eco wildcard DNS
   (Caddy routing on golgi — no Cloudflare changes needed)
```

### Why This Matters for gen5

gen4 proved primals disappear into products. gen5 proves compositions
disappear into collaborator workflows. The collaborator never sees
NestGate, bearDog, or songBird. They see a GIS tool, a drug screening
platform, or a JupyterHub notebook. The composition is the interface.
The drawbridge is the data ingestion point. The mesh is the coordination
layer. The CAS is the provenance backbone.

---

## Architecture

```
                    *.primals.eco (Cloudflare wildcard → golgi)
                              │
                        Caddy (golgi)
                    ┌─────────┼─────────┐
                    │         │         │
           footprint/    tideglass     lab/
           (GIS SPA)    (reversal)    (JupyterHub)
                    │         │         │
              ┌─────┴─────────┴─────────┴─────┐
              │        songBird mesh           │
              │      drawbridge routing        │
              │      capability.call()         │
              └─────┬─────────┬─────────┬─────┘
                    │         │         │
              nestGate    barracuda   ironGate
              (CAS)       (math)     (GPU/compute)
                    │
              ┌─────┴─────────────────────────┐
              │     External Data Sources      │
              │  (drawbridge weak bonds)       │
              │                                │
              │  USGS  ArcGIS  NF Portal       │
              │  LINCS  PubMed  Pluto.bio      │
              │  NCBI  UniProt  ChEMBL         │
              └────────────────────────────────┘
```

### Data Flow

External data enters through **drawbridge weak bonds** — the lowest
trust level in the K-Derm bonding model. The drawbridge mediates
between the hostile internet and the sovereign interior:

1. **Weak bond**: HTTP/HTTPS fetch from external API (zero trust)
2. **Content-addressed storage**: Data lands in NestGate CAS with BLAKE3 hash
3. **Provenance**: Loam Certificate minted with source attribution (sweetGrass braid)
4. **Capability exposure**: Processed results registered as drawbridge capabilities
5. **Mesh availability**: Any gate can `capability.call` the result

Bond escalation follows the standard K-Derm path. External data
starts as weak (untrusted fetch), becomes ionic (verified hash),
and can reach metallic (validated by spring scenarios) or covalent
(incorporated into permanent provenance chain) over time.

---

## Composition Catalog

### Live (Wave 138a)

| Composition | Subdomain | Data Sources | Capabilities Exposed |
|------------|-----------|-------------|---------------------|
| **footPrint** | `primals.eco/footprint/` | USGS, OpenStreetMap, ArcGIS, custom tile servers | `gis.render`, `gis.layers`, `gis.search` |
| **JupyterHub** | `lab.primals.eco` | User notebooks, conda environments | `jupyter` (via drawbridge routes) |
| **sporePrint** | `primals.eco` | Markdown content, Zola static gen | `content.serve` |
| **TOPO-VIS** | `live.primals.eco` | songBird mesh state, gate topology | `topo.visualize` |

### Planned

| Composition | Subdomain | Data Sources | Capabilities |
|------------|-----------|-------------|-------------|
| **tideGlass** | `tideglass.primals.eco` | LINCS L1000, GEO, ChEMBL, NF Data Portal | `gps.screen`, `gps.reverse`, `compound.search` |
| **helixVision** | `helix.primals.eco` | GEO, SRA, Synapse, collaborator uploads | `expression.de`, `pathway.enrich`, `variant.impact` |
| **initioChem** | `chem.primals.eco` | PDB, AlphaFold, PubChem | `fel.landscape`, `structure.predict` |

### Private (primal.eco — inner membrane)

| Composition | Subdomain | Data Sources | Trust Level |
|------------|-----------|-------------|-------------|
| **Private footPrint** | `footprint.primal.eco` | Personal GIS data, property measurements | Full trust — Loam Certificate provenance |
| **Ceremony endpoints** | `ceremony.primal.eco` | SoloKey entropy, Pixel StrongBox | Covalent — hardware-backed |
| **Personal sporePrint** | `primal.eco` | Personal blog, private notes | Full trust — sovereign DNS |

---

## Cross-Feeding

The power of the pattern is that compositions consume each other's
capabilities without knowing which primal provides them:

```
footPrint GIS layers
  → NF tumor localization (Gonzales)
  → Environmental sampling sites (ABG eDNA)
  → Ecosystem topology visualization

tideGlass compound screening
  → healthSpring MATRIX scoring (drug repurposing)
  → NF Data Portal hits → footPrint spatial overlay

JupyterHub compute
  → ABG RNA-seq pipelines (kallisto, salmon, STAR)
  → Gonzales NF mining notebooks
  → Any collaborator's analysis
```

The same NestGate CAS holds all the data. The same songBird mesh
routes all the requests. The same bearDog signs all the sessions.
Different compositions, same sovereign infrastructure.

---

## Adding a New Composition

1. **Create the project** in `protoKarya` org (or wherever appropriate)
2. **Define drawbridge routes** in the composition's config:
   ```
   SONGBIRD_DRAWBRIDGE_ROUTES=/api=myproject
   SONGBIRD_PROXY_ROUTES=myproject=http://localhost:PORT
   ```
3. **Add a Caddy block** to `provision-golgi.sh`:
   ```caddy
   myproject.primals.eco {
       import security_headers
       reverse_proxy localhost:PORT
   }
   ```
4. **Register data sources** as drawbridge weak bonds in the composition's manifest
5. **Wire NestGate** for content-addressed storage of ingested data
6. **Expose capabilities** via songBird — other compositions can now `capability.call`

No Cloudflare changes needed. Wildcard `*.primals.eco` handles DNS.
Caddy handles TLS (ACME on-demand). The composition is live.

---

## Relationship to Other Patterns

| Pattern | Relationship |
|---------|-------------|
| **K-Derm Diderm** | Compositions live in the outer membrane (`primals.eco`) or inner membrane (`primal.eco`). Trust level determined by domain. |
| **Drawbridge** | Universal data ingestion point. External APIs enter as weak bonds. Compositions register their capabilities via drawbridge routes. |
| **Provenance Trio** | All ingested data gets rhizoCrypt DAG → loamSpine spine → sweetGrass braid. |
| **Novel Ferment Transcripts** | Composition outputs are NFTs — history-bound artifacts with full provenance. |
| **Pre-Grant Pipeline** | gen5 collaborators consume compositions to produce preliminary data at zero cost. |
| **Universal Substrate** | Compositions deploy on any architecture that runs a NUCLEUS. |

---

## Biological Analogy

Compositions are **organelles** — specialized structures within the
cell that perform specific functions. footPrint is the spatial
perception organelle. tideGlass is the pharmacological screening
organelle. JupyterHub is the general compute organelle. They all
share the cell's infrastructure (CAS, mesh, crypto) but serve
different functions. When a new function is needed, a new organelle
differentiates from the same primal substrate.

The drawbridge is the **transporter protein** — it selectively imports
molecules (data) from outside the cell, transforms them into the
cell's internal format (content-addressed CAS entries), and makes
them available to any organelle that needs them.

---

*Compositions are the gen5 delivery mechanism. Primals are invisible.
Compositions are what collaborators touch. The drawbridge feeds them.
The mesh connects them. The CAS remembers everything.*
