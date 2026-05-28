# Public Data Systems — The Provenance Substrate for gen5

**Date**: May 28, 2026
**Status**: Active — catalog established, provenance format mapping in progress
**License**: scyBorg triple — AGPL-3.0-or-later (code), ORC (system mechanics), CC-BY-SA 4.0 (this document)
**Lineage**: gen3/baseCamp (scattered data source references) → gen4/foundations (sporeGarden/foundation 100+ anchors) → gen5 (this document)

---

## Why This Document Exists

gen3 scattered data source references across 28 baseCamp papers. gen4 consolidated them into `sporeGarden/foundation` with 100+ public data source anchors and `fetch_sources.sh`. gen5 needs something different: a unified catalog of public data systems mapped to provenance format, ingestion status, spring alignment, and collaborator demand.

The difference: gen4 cataloged data sources for internal validation. gen5 catalogs data systems for external science production — where the data comes from, how it enters the provenance chain, what springs consume it, and which collaborators need it.

---

## The Trust Hierarchy

Not all data systems are equal. The ecosystem distinguishes three tiers of trust based on how close the data is to the original measurement or deposition.

### Tier 1 — Primary Sources (Trust After Hash)

Primary sources are the authoritative repositories where experimentalists deposit raw or minimally processed data. NCBI, PDB, UniProt, PhysioNet — these are the bedrock. When we fetch from a primary source and the BLAKE3 hash matches, we trust the data because the provenance chain starts at the instrument.

**Policy**: Fetch, hash, consume. The data is what the depositor said it is. Validation checks confirm our processing, not their data.

| Examples | Why primary |
|----------|------------|
| NCBI SRA / GenBank / Protein | Depositor-submitted sequences with accession provenance |
| RCSB PDB | Experimentally determined structures, deposition-validated |
| UniProt | Curated protein annotations from primary literature |
| PhysioNet | Clinician-deposited biosignal recordings |
| NOAA GHCND | Instrument-measured weather observations |
| Dryad / Zenodo | Author-deposited datasets tied to publications via DOI |

### Tier 2 — Secondary Sources (Revalidate Before Trust)

Secondary sources curate, transform, or aggregate primary data. They are highly valuable — often more usable than the raw primary data — but they introduce interpretation. Someone chose what to include, how to process, what metadata to attach. We consume them for targets and context, but we go back to the underlying primary data and revalidate before we trust the conclusions.

**PLUMED-NEST is the canonical example.** It hosts published PLUMED input files for enhanced sampling simulations — curated, peer-reviewed, tied to specific papers via `plumID`. But the PLUMED inputs encode parameter choices (collective variables, bias heights, temperatures, force fields) that are the author's interpretation. The ecosystem ingests PLUMED-NEST entries (8 targets in pseudoSpore Module 07, 2 PASS, 6 profiled), but the underlying trajectories and force field parameters get revalidated through hotSpring before the results enter a pseudoSpore.

**Policy**: Ingest for targets and context. Revalidate the underlying data through spring checks before incorporating into artifacts. Trust the curation, verify the science.

| Examples | Why secondary | What we revalidate |
|----------|--------------|-------------------|
| **PLUMED-NEST** | Published enhanced sampling inputs — author parameter choices | Force field params, CV definitions, convergence, against primary PDB/trajectory data |
| **CAZy / ez-CAZy** | Curated GH family classification — expert annotation | Structural assignments against PDB, sequence against UniProt |
| **MalariaGEN Pf6** | Curated *P. falciparum* genomic variation — consortium processing | Variant calls against raw SRA reads |
| **TCGA / GEO** | Cancer transcriptomics — platform-specific normalization | Expression quantification against raw FASTQ |
| **ChEMBL** | Bioactivity aggregated from literature — manual extraction | Dose-response curves against original papers |
| **MANA SODA** | Cross-validation benchmark datasets — consortium assembly | Processing results against raw instrument files |
| **AlphaFold DB** | Predicted structures — computational, not experimental | Predictions against PDB experimental structures where available |
| **MassBank** | Reference mass spectra — curated from instruments | Spectral matching against raw instrument data when available |
| **KEGG** | Pathway maps — expert-curated biological interpretation | Pathway membership against primary literature |
| **BRENDA** | Enzyme kinetics — literature-extracted parameters | Kinetic constants against original publications |

### Tier 3 — Derived Sources (Target Only)

Derived sources are analyses, models, or predictions built on primary/secondary data. They are targets for validation, not inputs for trust. When a paper claims a result, we reproduce it — the claim is the target, the primary data is the input, and the spring check is the arbiter.

**Policy**: Use as validation targets. Never consume derived claims as input without reproduction.

| Examples | Why derived | How we use it |
|----------|------------|---------------|
| Published paper figures | Author's analysis of their data | Reproduce the figure from the primary data |
| TNMplot | Pre-computed tumor vs normal expression | Verify against TCGA/GTEx raw data |
| Pathway enrichment databases | Pre-computed gene set enrichments | Recompute enrichment from expression data |
| Force field parameter sets (CHARMM, AMBER, OPLS, GLYCAM) | Fitted to QM/experimental data | Validate FEL against published benchmarks |

### The Revalidation Pipeline

```
Secondary/Derived source (claim)
    → Identify underlying primary data
    → Fetch primary data (Tier 1 provenance)
    → Reproduce the secondary source's result through spring checks
    → If checks pass: result enters ecosystem as validated
    → If checks fail: flag discrepancy, investigate, document
    → Never propagate unvalidated secondary claims into pseudoSpores
```

---

## The Catalog

### Drug Discovery & Pharmacology

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|
| **PubChem BioAssay** | Dose-response, IC50, EC50 | 1.5M+ assays, 115M+ compounds | JSON/SDF/CSV REST API | ncbi.nlm.nih.gov/pcassay | healthSpring | Gonzales (NF, AD) | Partial (healthSpring Exp) |
| **ChEMBL 34** | Bioactivity, 15K targets | 2.4M compounds, 20M activities (~2 GB) | PostgreSQL dump, REST API | ebi.ac.uk/chembl | healthSpring | Gonzales (NF) | Planned |
| **BindingDB** | Binding affinities (Kd/Ki) | 2.8M affinities (~1 GB) | TSV download | bindingdb.org | healthSpring | Gonzales (ADDRC) | Planned |
| **DrugBank** | Drugs, targets, ADMET, PK | 14K+ drugs | XML (academic license) | drugbank.com | healthSpring | Gonzales | Planned |
| **FDA Orange Book** | Approved products, TE | Regulatory | Web | fda.gov/drugs | healthSpring | — | Not started |
| **ZINC20** | Purchasable compounds | 1.4B compounds | SMILES/SDF | zinc20.docking.org | healthSpring | — | Not started |
| **ADDRC Library** | Screening compounds | 8K compounds | CSV (Lisabeth access) | MSU internal | healthSpring | Gonzales (ADDRC) | Requires lab access |

### Analytical Chemistry & PFAS

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|
| **NIST PFAS Reference Data** | Untargeted PFAS reference spectra | Standard set | Varies | nist.gov/programs-projects/pfas | wetSpring T2 | Jones | Planned (Jones rec.) |
| **EPA Method 1633A** | Targeted analysis of 40 PFAS, QC specs | Regulatory standard | PDF → structured | epa.gov (Method 1633A) | wetSpring T2 | Jones | Planned (Jones rec.) |
| **MassBank** | Reference mass spectra | 90K+ spectra | MSP/JSON | massbank.eu | wetSpring T2 | Jones | Active (9/9 checks) |
| **MANA SODA** | Cross-validation datasets for metabolomics | Benchmark suite | Various | sites.google.com/metabolomicsna.org/soda | wetSpring T2 | Jones | Planned (Jones rec.) |
| **Proteowizard msConvert** | LC-MS format conversion (RAW → mzML) | Tool | Binary | proteowizard.sourceforge.io | wetSpring T2 | Jones | Reference tool |

### Genomics & Microbiome

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|
| **NCBI SRA** | 16S, shotgun metagenomes | Millions of runs | FASTQ | ncbi.nlm.nih.gov/sra | wetSpring | ABG, Gonzales | Active (multiple BioProjects) |
| **NCBI BioProject** | Sequencing study metadata | Study-level | XML/JSON | ncbi.nlm.nih.gov/bioproject | wetSpring | ABG | Active |
| **NCBI GenBank** | Reference genomes | Genome assemblies | FASTA/GenBank | ncbi.nlm.nih.gov/genbank | wetSpring | ABG (REL606) | Active |
| **NCBI Protein** | Protein sequences | Millions | FASTA | ncbi.nlm.nih.gov/protein | wetSpring | ABG (QS genes) | Active |
| **UniProt** | Protein sequences + annotations | 250M+ entries | FASTA/XML/RDF | uniprot.org | wetSpring, hotSpring | ABG | Active |
| **KEGG** | Pathways, reactions, compounds | 500+ pathways | REST API | genome.jp/kegg | wetSpring | ABG (WCM) | Active |
| **HMP Phase II** | Healthy human gut microbiome | ~4,700 samples | FASTQ | hmpdacc.org | wetSpring | — | Planned |
| **Earth Microbiome Project** | 14 biomes, global | ~30K samples | BIOM/FASTQ | earthmicrobiome.org | wetSpring | — | Planned (Tier 2) |

### Protein Structure & Prediction

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|
| **RCSB PDB** | Experimental protein structures | 220K+ structures | PDB/mmCIF | rcsb.org | hotSpring, neuralSpring | ABG, Gonzales (NF1) | Active |
| **AlphaFold DB** | Predicted protein structures | 200M+ structures | PDB/mmCIF | alphafold.ebi.ac.uk | neuralSpring (coralForge) | Gonzales (NF1 variants) | Planned |
| **UniRef90** | MSA sequences for structure prediction | ~100 GB | FASTA | uniprot.org | neuralSpring (coralForge) | — | Planned |
| **PDB70** | MSA for homology search | ~15 GB | HHsearch format | — | neuralSpring (coralForge) | — | Planned |

### Neurofibromatosis (NF) — gen5 Priority

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|
| **NF Data Portal (Synapse)** | Gene expression, genomic variants, drug screening, clinical | Multi-dataset | Synapse API | synapse.org (CTF) | wetSpring, healthSpring | **Gonzales** | Not started |
| **Pluto.bio NF Datasets** | Gene expression, pathway analysis | ~108M data points, 12 datasets | Web platform | pluto.bio | wetSpring | **Gonzales** | Not started |
| **CTF Foundation Datasets** | Curated NF research data | Foundation-curated | Varies | ctf.org | wetSpring, healthSpring | **Gonzales** | Not started |

### LTEE & Microbial Evolution

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|
| **Dryad (Wiser 2013)** | LTEE fitness trajectories | Time-series | CSV | doi:10.5061/dryad.0hc2m | wetSpring | Barrick | Active (lithoSpore) |
| **NCBI PRJNA294072** | LTEE genomes (Tenaillon 2016) | 264 genomes | FASTQ | ncbi.nlm.nih.gov/bioproject | wetSpring | Barrick | Active (lithoSpore) |
| **NCBI PRJNA380528** | LTEE allele frequencies (Good 2017) | Population genomics | VCF | ncbi.nlm.nih.gov/bioproject | wetSpring | Barrick | Active (lithoSpore) |

### Tissue & Expression Atlases

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|
| **GTEx** | Expression across 54 tissues | Multi-tissue | TSV/API | gtexportal.org | wetSpring | Gonzales (cross-tissue) | Planned |
| **Human Protein Atlas** | Tissue expression + histology | Proteome-wide | Web API | proteinatlas.org | wetSpring | Gonzales | Planned |
| **Cell x Gene (CZI)** | scRNA-seq atlases | Multi-tissue | H5AD | cellxgene.cziscience.com | wetSpring | Gonzales | Planned |
| **Tabula Sapiens / Muris** | Human + mouse sc atlases | Full organism | H5AD | tabula-sapiens-portal.ds.czbiohub.org | wetSpring | — | Planned |

### Biosignal & Clinical

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|
| **PhysioNet MIT-BIH** | Annotated ECG | 48 recordings | WFDB | physionet.org | healthSpring | — | Active |
| **PhysioNet MIMIC-III** | ICU records + biosignals | 40K+ patients | CSV (credentialed) | physionet.org | healthSpring | — | Partial |
| **PhysioNet PTB-XL** | 12-lead ECG | 21,799 records | WFDB | physionet.org | healthSpring | — | Planned |

### Environmental & Agriculture

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|
| **Open-Meteo ERA5** | Weather reanalysis | Global, hourly | REST API / CSV | open-meteo.com | airSpring | — | Active (100 MI stations) |
| **USDA Web Soil Survey** | Soil properties | US national | API | websoilsurvey.nrcs.usda.gov | airSpring | — | Active |
| **EPA STORET** | Water quality | US national | API | epa.gov/waterdata | wetSpring | — | Planned |
| **AmeriFlux** | Eddy covariance flux data | 500+ sites | CSV | ameriflux.lbl.gov | airSpring | — | Planned |

### Physics & Computational Chemistry

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **BRENDA** | Enzyme kinetics | 6M+ entries | Web/SOAP | brenda-enzymes.org | hotSpring | ABG (WCM) | Active | T2 — literature-extracted |
| **EcoCyc** | E. coli metabolism | Genome-scale | API | ecocyc.org | hotSpring | ABG (WCM) | Active | T2 — curated |
| **NIST TECRdb** | Thermodynamics of enzyme reactions | Standard | Web | — | hotSpring | ABG | Active | T1 — NIST reference |
| **FPEOS (Militzer)** | EOS tables for H, He, C at WDM | Dense matter | Open C++/Python | Berkeley | hotSpring | Murillo, Chuna | Planned | T1 — first-principles |

### Simulation Repositories & Enhanced Sampling (Secondary — Revalidate)

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **PLUMED-NEST** | Published PLUMED input files for enhanced sampling | 198 projects, 1,212 protocol examples (plumID) | PLUMED input + reference data + GitHub/Zenodo archives | plumed-nest.org | hotSpring | ABG (Alistaire) | Active — 8 targets ingested via `nest-validate`, 2 PASS, 6 profiled. plumIDs: 24.020, 24.029, 24.017, 20.000, 22.028, 25.007, 25.012, 22.039 | **T2** — author parameter choices, revalidate CVs/convergence/force fields against PDB primary data |
| **CAZy Database** | GH/GT family classification | All characterized CAZymes | Web | cazy.org | hotSpring | ABG (Alistaire) | Active | T2 — expert annotation, verify against PDB |
| **ez-CAZy** | Biochemically characterized GHs | 7,000+ GHs with functional annotations | Web (Sci Rep 2025) | — | hotSpring | ABG (Alistaire) | Active | T2 — curated subset of CAZy |
| **GROMACS** | MD simulation engine (Tier 0 ground truth) | Industry standard | Binary + source | gromacs.org | hotSpring | ABG, Eaves | Reference tool | T1 — parity target for barraCuda |
| **PLUMED** | Enhanced sampling / metadynamics | Plugin ecosystem | Source | plumed.org | hotSpring | ABG (Alistaire) | Reference tool | T1 — established CV framework |

### Cancer Genomics & Transcriptomics (ABG Project 2)

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **TCGA** | Cancer RNA-seq, WGS, clinical | 33 cancer types, 11K+ patients | BAM/FASTQ/counts | portal.gdc.cancer.gov | wetSpring, healthSpring | ABG (Mark) | Planned | T2 — consortium processing |
| **GEO** | Gene expression omnibus | 4M+ samples | SOFT/MINiML/supplementary | ncbi.nlm.nih.gov/geo | wetSpring | ABG (Mark, bake3011) | Active (metadata mining) | T1 — depositor-submitted |
| **COSMIC** | Somatic mutations in cancer | 40M+ mutations | TSV (academic) | cancer.sanger.ac.uk/cosmic | healthSpring | ABG (Mark) | Planned | T2 — curated from literature |
| **CPTAC** | Cancer proteomics | Multi-cancer | mzML/mzIdentML | proteomics.cancer.gov | healthSpring | ABG (Mark) | Planned | T1 — depositor-submitted |
| **ProteomeXchange** | Proteomics data sharing | 30K+ datasets | Various | proteomecentral.proteomexchange.org | healthSpring | ABG (Mark) | Planned | T1 — depositor-submitted |
| **TNMplot** | Tumor vs normal expression (pre-computed) | TCGA + GTEx | Web | tnmplot.com | wetSpring | ABG (Mark) | Survey | **T3** — derived, verify against TCGA/GTEx |

### Malaria Genomics (ABG Project 1)

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **MalariaGEN Pf6** | *P. falciparum* genomic variation | 7K+ samples, global | VCF/HDF5 | malariagen.net/pf6 | wetSpring, groundSpring | ABG (Tamison) | Planned | T2 — consortium processing, revalidate against raw reads |
| **PlasmoDB** | Plasmodium genomics and functional data | Genome-scale | GFF/FASTA/API | plasmodb.org | wetSpring | ABG (Tamison) | Planned | T2 — curated |
| **ENA** | European Nucleotide Archive (NCBI mirror) | Millions of runs | FASTQ | ebi.ac.uk/ena | wetSpring | ABG (Tamison) | Active (via NCBI) | T1 — depositor-submitted |

### Salmon Genomics (ABG Project 4)

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **SalmoBase** | Salmonid reference genomes and annotations | Multi-species | FASTA/GFF | salmobase.org | wetSpring | ABG (bake3011) | Planned | T2 — curated assemblies |
| **Aqua-FAANG** | Aquaculture functional annotation | Multi-species | BED/BigWig | aqua-faang.eu | wetSpring | ABG (bake3011) | Planned | T2 — consortium |
| **GEO (salmon-specific)** | RNA-seq: GSE166686, GSE269132, GSE166760, SRP124522 | 4+ datasets | FASTQ/counts | ncbi.nlm.nih.gov/geo | wetSpring | ABG (bake3011) | Planned | T1 — depositor-submitted |

### Lattice QCD & Gauge Configurations (Chuna)

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **ILDG** | International Lattice Data Grid — gauge configurations | Community archive | ILDG/LIME binary + QCDml 2.0 | ildg.net | hotSpring | Chuna (Bazavov) | Planned — MILC interop | T1 — community-standard archive |
| **MILC configurations** | Lattice QCD gauge fields (Bazavov group production) | LANL/FNAL HPC | MILC binary | — | hotSpring | Chuna (Bazavov) | Planned — format conversion | T1 — primary production |

### Seismology & Geophysics

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **IRIS FDSN** | Seismic station geometry, event catalogs | Global | FDSN web services | iris.edu | groundSpring | — | Active (Exp 032) | T1 — instrument network |

### Weather, Hydrology & Long-Term Ecology

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **NOAA GHCND** | Daily weather observations | Global, historical | CSV/API | ncdc.noaa.gov | groundSpring, airSpring | — | Active (ET₀ validation) | T1 — instrument observations |
| **USGS Streamflow** | River discharge, stage | US national | API | waterdata.usgs.gov | airSpring | — | Planned (Red Cedar River) | T1 — gauge measurements |
| **Tara Oceans** | Marine metagenomics | 243 stations, global | FASTQ | oceans.taraexpeditions.org | wetSpring | — | Planned (Tier 2) | T1 — expedition-collected |
| **KBS LTER** | 30+ year no-till temporal ecology | Michigan | CSV/API | lter.kbs.msu.edu | airSpring, wetSpring | — | Planned (Tier 2) | T1 — long-term ecological |
| **ADREC** | Anaerobic digester time-series | Collaboration | Custom | MSU internal | wetSpring | — | Planned | Requires access |

### Taxonomy & Reference Databases

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **SILVA 138.1** | 16S/18S/23S rRNA reference taxonomy | ~500K sequences | FASTA/TSV (QIIME2 .qza) | arb-silva.de | wetSpring | — | Active — classifier loaded in `validation_helpers.rs` | T1 — curated reference |
| **RDP Trainset 9** | 16S classifier training set | Standard | FASTA/TAX | via Zenodo 800651 | wetSpring | — | Active (Galaxy mothur tutorial) | T1 — reference |
| **GTDB** | Genome Taxonomy Database | 400K+ genomes | FASTA | gtdb.ecogenomic.org | wetSpring | — | Planned (NestGate need flagged) | T1 — genome-based taxonomy |

### PFAS & Environmental Chemistry (Expanded — Codebase-Verified)

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **EPA CompTox Dashboard** | PFAS Master List structures | ~14K PFAS | SMILES/SDF | comptox.epa.gov/dashboard | wetSpring T2 | Jones | Active (manual download noted) | T1 — EPA reference |
| **EPA UCMR 5** | National drinking water PFAS | National survey | ZIP/CSV | epa.gov (UCMR5) | wetSpring T2 | — | Planned (Exp041) | T1 — EPA monitoring |
| **EPA PFOS Surface Water** | Surface water PFAS concentrations | DOI-keyed | CSV | pasteur.epa.gov (DOI 10.23719/1522855) | wetSpring T2 | — | Scripted download | T1 — EPA measurement |
| **Michigan EGLE PFAS** | Surface water sampling, ArcGIS | 3,383 samples | GeoJSON/CSV | gis-egle.hub.arcgis.com | wetSpring T2 | — | Active (Exp008) | T1 — state monitoring |
| **NORMAN SusDat** | PFAS suspect screening list | Cross-ref | Web | norman-network.com/nds/SusDat | wetSpring T2 | Jones | Documented | T2 — community curation |
| **Jones/Zenodo PFAS Library** | 175 PFAS compounds | Reference library | mzML/MSP | zenodo.org/record/14341321 | wetSpring T2 | Jones | Active (Exp018) | T1 — depositor data |

### Drug Repurposing & Knowledge Graphs

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **repoDB** | Drug-disease associations matrix | 1,571 drugs × 1,209 diseases | CSV | — | wetSpring | — | Active (Exp160, NMF) | T2 — curated from literature |
| **ROBOKOP KG** | Biomedical knowledge graph | Large-scale | TransE embeddings | robokop.renci.org | wetSpring | — | Planned (Exp161) | T2 — computational |
| **MONDO / Disease Ontology** | Disease classification | Standard | OWL/JSON | mondo.monarchinitiative.org | healthSpring | Gonzales | Planned | T1 — community standard |
| **OMIM / Orphanet** | Rare disease ontologies | Curated | Web/API | omim.org / orpha.net | healthSpring | Gonzales (NF) | Planned | T2 — curated |
| **Reactome** | Biological pathway database | 2,700+ pathways | REST API | reactome.org | healthSpring | Gonzales | Planned | T2 — curated |

### Agriculture & Soil (Codebase-Verified)

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **USDA NASS Quick Stats** | Agricultural statistics, crop yields | US national | REST API | quickstats.nass.usda.gov | airSpring | — | Active — Rust `NassProvider`, API key required | T1 — USDA official |
| **USDA SCAN** | In-situ soil moisture profiles | Station network | API | wcc.sc.egov.usda.gov | airSpring | — | Active (Exp 026 Richards θ(t)) | T1 — instrument data |
| **AmeriFlux / FLUXNET** | Eddy covariance ET gold standard | 500+ sites | CSV | ameriflux.lbl.gov | airSpring | — | Active (Exp 030, `validate_ameriflux`) | T1 — instrument data |
| **NASA SMAP** | Satellite soil moisture | Global | HDF5 | smap.jpl.nasa.gov | airSpring | — | Planned (Tier 3) | T1 — satellite |
| **ERA5-Land (Copernicus CDS)** | High-res land reanalysis | Global, ~3 TB | NetCDF/GRIB | cds.climate.copernicus.eu | airSpring | — | Planned (Tier 3) | T1 — reanalysis |

### Deep-Sea & Specialty Repositories

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **MBL darchive** | Sogin rare biosphere amplicon | Historical | FASTA | darchive.mblwhoilibrary.org | wetSpring | — | Active (Exp051) | T1 — depositor |
| **MG-RAST** | Metagenomic analysis server | Community | Web | mg-rast.org | wetSpring | — | Planned (Exp051-056) | T2 — processed |
| **Figshare** | Sulfur-cycling phylogenomics | DOI-keyed | CSV/FASTA | figshare.com | wetSpring | — | Active (Exp053) | T1 — depositor |
| **OSF** | Phosphorus phylogenomics | DOI-keyed | CSV | osf.io | wetSpring | — | Active (Exp054) | T1 — depositor |

### Phylogenetics & Evolution

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **Dryad (SATe-II alignments)** | 16S alignments + Newick trees | Reference | Alignment/Newick | datadryad.org | wetSpring | — | Active (Exp019) | T1 — depositor |
| **PhyNetPy (Rice)** | 1,284 gene trees | Benchmark | Newick | github.com/NakhlehLab | wetSpring | — | Active (Exp019) | T1 — published code |
| **LTEE-Ecoli mutation database** | Long-term evolution mutations | Comprehensive | Web | barricklab.org/ltee | wetSpring | Barrick | Planned | T2 — lab-curated |

### Nuclear Physics & Dense Matter

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **AME2020** | Atomic mass evaluation | Nuclear binding energies | JSON (selected) | — | hotSpring | Murillo | Active (control/surrogate/) | T1 — IAEA reference |
| **Sarkas** (Murillo group) | Yukawa plasma simulation | Reference code | Python | github.com/murillo-group/sarkas | hotSpring | Murillo | Active (cloned control) | T1 — author code |
| **TTM** (Murillo group) | Transport theory models | Reference code | Python | github.com/murillo-group | hotSpring | Murillo | Active (cloned control) | T1 — author code |

### Gaming & Creative Data (esotericWebb Domain)

| System | Data Types | Scale | Format | URL | Spring(s) | Collaborator(s) | Ingestion | Trust |
|--------|-----------|-------|--------|-----|-----------|-----------------|-----------|-------|
| **MTG card/rulings via NestGate** | Card database, rulings, historical errata | Complete | loamSpine certs | via NestGate | ludoSpring | — | Planned (NestGate provider) | T1 — official data |
| **Pathfinder 2e / FATE / Cairn / Cypher** | TTRPG rulesets (ORC/CC-BY) | Complete rulesets | loamSpine certificates | — | ludoSpring | — | Active (exp045 ruleset control) | T1 — ORC/CC-BY licensed |
| **Veloren / Fish Folk / A/B Street** | Game telemetry adapters | External games | Log parsing | Open source repos | ludoSpring | — | Active (exp027-029) | T1 — open source |

---

## Synapse as a Challenge Platform

Synapse (synapse.org) is not just a data repository — it hosts **scientific challenges** (DREAM Challenges, BraTS, CTF NF challenges) that provide structured benchmarking for computational methods in translational medicine and systems biology.

This is relevant to gen5 because:

1. **NF challenges exist on Synapse** — CTF-sponsored computational challenges for NF research. These are not Kaggle competitions. They are domain-science benchmarks with curated datasets, standardized evaluation, and foundation oversight.
2. **The challenge infrastructure** (Evaluation Queues, Docker submission, leaderboard) maps directly to the pseudoSpore validation pattern — self-contained, reproducible, provenance-tracked.
3. **DREAM Challenges** (Dialogue for Reverse Engineering Assessments and Methods) have been running since 2006 — real computational biology benchmarks that advance the field.

See `gen5/thesis/SCIENTIFIC_CHALLENGES.md` for the full thesis on how scientific challenges fit the gen5 evolution.

---

## Provenance Format Mapping

Every public data system enters the ecosystem through a provenance chain. The path differs by trust tier:

### Tier 1 (Primary) — Direct Provenance

```
Primary source (NCBI, PDB, PhysioNet)
    → Fetch (fetch_sources.sh / API client / NestGate NCBILiveProvider)
    → BLAKE3 content hash (NestGate)
    → Provenance vertex (rhizoCrypt DAG)
    → Attribution (sweetGrass braid)
    → Spring consumption (domain validation)
    → Product composition (gen4 tool)
    → pseudoSpore packaging (gen5 artifact)
```

### Tier 2 (Secondary) — Revalidation Required

```
Secondary source (PLUMED-NEST, CAZy, TCGA, ChEMBL, MalariaGEN)
    → Fetch secondary curation (targets, metadata, parameter choices)
    → Identify underlying primary data (PDB IDs, SRA accessions, raw instrument files)
    → Fetch PRIMARY data through Tier 1 pipeline
    → Reproduce secondary source's result through spring checks
    → If PASS: validated result enters provenance chain
    → If FAIL: discrepancy documented, secondary claim NOT propagated
    → BLAKE3 hash on primary data (not secondary curation)
    → pseudoSpore contains validated result, cites both sources
```

### Tier 3 (Derived) — Target Only

```
Derived source (published figures, pre-computed analyses, TNMplot)
    → Extract the claim (numerical value, figure, ranking)
    → Identify primary data the claim was derived from
    → Reproduce the claim from primary data through spring checks
    → Claim becomes a validation check: PASS/FAIL
    → Primary data enters provenance chain; derived claim is the test, not the input
```

### Ingestion Status Key

| Status | Meaning |
|--------|---------|
| **Active** | Data fetched, hashed, consumed by springs, validation checks passing |
| **Partial** | Some datasets ingested, not complete coverage |
| **Planned** | Data source identified, ingestion pipeline designed but not built |
| **Not started** | Data source identified, no engineering work yet |
| **Requires lab access** | Data exists but needs institutional credentials or PI authorization |
| **Survey** | Source identified, relevance confirmed, no ingestion plan yet |
| **Reference tool** | Not a data source — a tool the ecosystem uses or validates against |

---

## What gen5 Changes About Data Ingestion

gen3/gen4 fetched public data to reproduce published results. gen5 fetches public data to produce **new results** for external collaborators. The shift:

| gen4 Ingestion | gen5 Ingestion |
|---------------|---------------|
| Reproduce known results | Produce unknown results |
| Accession → fetch → validate against paper | Portal → fetch → analyze for collaborator's question |
| One BioProject at a time | Entire portal catalogs (NF Data Portal, MANA SODA) |
| Internal consumption | Collaborator-facing artifacts |
| Spring validation only | Spring validation + product composition + pseudoSpore |

### Priority Data Systems for gen5 (by collaborator demand)

**Tier A — Active collaborator, immediate need:**

1. **NF Data Portal / Synapse** (T2) — Gonzales NF project (first gen5 instance)
2. **NIST PFAS Reference Data** (T1) — Jones/blueFish (emeritus consulting)
3. **EPA Method 1633A** (T1) — Jones/blueFish (QC compliance gap)
4. **MANA SODA** (T2) — Jones/blueFish (cross-validation benchmarks)
5. **PubChem / ChEMBL** (T1/T2) — Gonzales drug repurposing (MATRIX scoring)
6. **PLUMED-NEST** (T2) — ABG/Alistaire (8 targets ingested, expanding)
7. **TCGA + GEO** (T2/T1) — ABG/Mark PTP cancer metastasis project

**Tier B — Contacted collaborator, near-term:**

8. **ILDG / MILC** (T1) — Chuna/Bazavov QCD configurations
9. **LTEE datasets (Dryad, PRJNA×2)** (T1) — Barrick lithoSpore expansion
10. **CTF Challenge Datasets** — Synapse scientific challenges (Gonzales alignment)

**Tier C — Ecosystem expansion:**

11. **EMP / Tara Oceans / HMP** (T1) — wetSpring global microbiome coverage
12. **SalmoBase / Aqua-FAANG** (T2) — ABG/bake3011 salmon project
13. **MalariaGEN Pf6** (T2) — ABG/Tamison CQ resistance project

---

## Catalog Statistics

| Category | Systems | Active | Planned | Not Started |
|----------|---------|--------|---------|-------------|
| Drug Discovery & Pharmacology | 7 | 1 | 4 | 2 |
| Analytical Chemistry & PFAS (original) | 5 | 1 | 3 | 1 |
| PFAS & Env. Chemistry (expanded) | 6 | 4 | 2 | 0 |
| Genomics & Microbiome | 8 | 5 | 3 | 0 |
| Taxonomy & Reference DBs | 3 | 2 | 1 | 0 |
| Protein Structure & Prediction | 4 | 1 | 3 | 0 |
| Neurofibromatosis | 3 | 0 | 0 | 3 |
| LTEE & Microbial Evolution | 3 | 3 | 0 | 0 |
| Tissue & Expression Atlases | 4 | 0 | 4 | 0 |
| Biosignal & Clinical | 3 | 1 | 1 | 1 |
| Environmental & Agriculture (original) | 4 | 2 | 2 | 0 |
| Agriculture & Soil (expanded) | 5 | 3 | 2 | 0 |
| Physics & Comp. Chemistry | 4 | 3 | 1 | 0 |
| Simulation & Enhanced Sampling | 5 | 2 | 0 | 0 |
| Cancer Genomics (ABG) | 6 | 1 | 4 | 1 |
| Malaria Genomics (ABG) | 3 | 1 | 2 | 0 |
| Salmon Genomics (ABG) | 3 | 0 | 3 | 0 |
| Drug Repurposing & Knowledge Graphs | 5 | 1 | 4 | 0 |
| Lattice QCD (Chuna) | 2 | 0 | 2 | 0 |
| Seismology | 1 | 1 | 0 | 0 |
| Weather/Hydrology/Ecology | 5 | 2 | 3 | 0 |
| Deep-Sea & Specialty | 4 | 3 | 1 | 0 |
| Phylogenetics & Evolution | 3 | 2 | 1 | 0 |
| Nuclear Physics & Dense Matter | 3 | 3 | 0 | 0 |
| Gaming & Creative | 3 | 2 | 1 | 0 |
| **Total** | **~110** | **~44** | **~46** | **~8** |

### By Trust Tier

| Tier | Count | Meaning |
|------|-------|---------|
| T1 — Primary | ~62 | Fetch, hash, consume |
| T2 — Secondary | ~38 | Revalidate before trust |
| T3 — Derived | ~5 | Target only |
| Reference tools | ~5 | GROMACS, PLUMED, msConvert, etc. |

### Codebase Verification

The spring profiles reveal that many systems previously marked "planned" are actually **wired in Rust code** with live NestGate providers:

| System | Previous Status | Codebase Status | Spring | Evidence |
|--------|----------------|----------------|--------|----------|
| NCBI E-utilities | Active | **Rust `NCBILiveProvider` + IPC handlers** | wetSpring, groundSpring, healthSpring, airSpring | `entrez.rs`, `efetch.rs`, `science.rs` |
| ChEMBL | Planned | **Rust IPC handler + manifest pin** | wetSpring, healthSpring | `data_fetch.rs`, `manifest.toml` |
| PubChem | Planned | **Rust IPC handler** | wetSpring | `data_fetch.rs` |
| Open-Meteo ERA5 | Active | **Rust `OpenMeteoProvider`** | airSpring, groundSpring, neuralSpring | `open_meteo.rs`, `open_meteo.py` |
| NOAA GHCND | Active | **NestGate `data.noaa_ghcnd`** | groundSpring | `pipeline_config.toml`, Exp 029 |
| IRIS FDSN | Active | **NestGate `data.iris_stations/events`** | groundSpring | `validate_iris_seismic.rs`, Exp 032 |
| USDA NASS | Not listed | **Rust `NassProvider`** | airSpring | `usda_nass.rs` |
| SILVA 138.1 | Not listed | **Loaded in Rust classifier** | wetSpring | `validation_helpers.rs` |
| PhysioNet/WFDB | Active | **Rust WFDB parser** | healthSpring | `wfdb.rs`, `integration_wfdb.rs` |
| MassBank | Active (9/9) | **Scripted download + Rust validation** | wetSpring | `download_data.sh`, Exp018/042/111 |
| PLUMED-NEST | Active (8 targets) | **`nest-validate` CLI + 8 plumID ingestions** | hotSpring | `control/plumed_nest/`, ingest.sh |
| AmeriFlux | Not listed | **Rust `validate_ameriflux`** | airSpring | Exp 030 |

---

## Spring × Data System Coverage Matrix

The eight springs that built baseCamp each consume different slices of the public data landscape. This matrix maps **codebase-verified** external data consumption (not planned, not documented — actually wired in Rust or Python with live fetch/parse code).

### Active NestGate Providers (Rust IPC)

| Provider Capability | Spring(s) | External Endpoint |
|---------------------|-----------|-------------------|
| `science.ncbi_fetch` | wetSpring, healthSpring, groundSpring, airSpring | NCBI E-utilities (ESearch/EFetch/SRA) |
| `data.fetch.chembl` | wetSpring, healthSpring | EBI ChEMBL activity API |
| `data.fetch.pubchem` | wetSpring | PubChem PUG REST |
| `data.noaa_ghcnd` | groundSpring | NOAA Climate Data Online |
| `data.iris_stations` / `data.iris_events` | groundSpring | IRIS FDSN Web Services |
| `data.weather` (Open-Meteo) | airSpring, groundSpring, neuralSpring | Open-Meteo ERA5 Archive API |

### Spring Profiles

**wetSpring** — Sovereign analytical biology. Most data-intensive spring.
- Live Rust providers: NCBI (Entrez, SRA, EFetch), ChEMBL, PubChem
- Scripted downloads: MassBank, SILVA, EPA CompTox, Jones/Zenodo PFAS, Dryad, EMP/Qiita
- Accessions consumed: 30+ BioProjects (PRJNA/PRJEB), CP000819.1, SRP001569, CHEMBL2103874
- Validation experiments: 380+ numbered experiments
- Data formats: FASTQ, FASTA, mzML, mzXML, MS2, SAM/BAM, BIOM, GenBank, taxonomy TSV

**hotSpring** — Sovereign computational physics & chemistry.
- GROMACS 2026.0 + PLUMED 2.9.2 control tier
- PLUMED-NEST: 8 plumID targets (24.020, 24.029, 24.017, 20.000, 22.028, 25.007, 25.012, 22.039)
- PDB structures: 2D24 (primary), 1XYN, 1QWN, 3QR3, 8CEL, 2QHA
- Force fields: CHARMM36, CHARMM22*, AMBER99SB-ILDN
- Nuclear physics: AME2020 binding energies, Sarkas/TTM (Murillo group)
- 229 numbered experiments, 22 GuideStone modules (~420 ns simulation)

**healthSpring** — Sovereign pharmacology & biosignals.
- Live Rust providers: ChEMBL (JAK panel, IC50/Ki/EC50), NCBI (GEO, SRA, PubMed)
- WFDB parser: MIT-BIH Arrhythmia Database (format 212/16)
- Manifest pins: GSE28680, HMP reference, QS gene matrix
- Planned: PhysioNet MIMIC-III/IV, PTB Diagnostic ECG, DrugBank, FDA FAERS

**groundSpring** — Sovereign environmental science.
- Live NestGate: NOAA GHCND (Exp 029), IRIS FDSN (Exp 032), NCBI SRA (Exp 030)
- Open-Meteo ERA5: Observation gap analysis (Exp 002)
- 29 core + 5 LTEE benchmark JSON files in `control/`
- Planned: KBS LTER, EMP, USGS

**airSpring** — Sovereign agriculture & weather.
- Rust providers: Open-Meteo ERA5 (`OpenMeteoProvider`), USDA NASS (`NassProvider`)
- Active validation: AmeriFlux/FLUXNET (eddy covariance ET₀), USDA SCAN (soil moisture)
- FAO-56 Penman-Monteith: digitized reference values (not API)
- Planned: ERA5-Land (CDS, ~3 TB), NASA SMAP, KBS LTER

**neuralSpring** — Sovereign ML & structure prediction.
- coralForge: AlphaFold2/3 sovereign reimplementation (synthetic baselines, no live PDB fetch yet)
- Training data: MNIST, Open-Meteo ERA5, PINNs/DeepONet GitHub repos
- HuggingFace: GPT-2 safetensors for weight spectral analysis
- NestGate deploy config: `providers = ["ncbi", "zenodo", "pdb"]` (wired, not yet live)
- Performance baselines: Kokkos, Polybench, cuBLAS

**ludoSpring** — Sovereign game engine & narrative.
- loamSpine certificates: Pathfinder 2e, FATE Core, Cairn, Cypher (ORC/CC-BY rulesets)
- External game adapters: Veloren, Fish Folk, A/B Street (telemetry parsing)
- Planned: MTG card DB via NestGate, NCBI QS gene cross-spring coupling
- No Scryfall/EDHREC — card data routes through NestGate + loamSpine certs

**primalSpring** — Sovereign infrastructure orchestrator.
- plasmidBin: 13 NUCLEUS primals bootstrapped via GitHub Releases + BLAKE3 checksums
- Foundation sediment: 12 NCBI/Dryad accessions in thread config TOML
- NestGate: `storage.store/retrieve`, `storage.fetch_external`, `content.put`
- Cross-spring: validates all other springs' NestGate data flows via composition graphs

### Data Flow Architecture

```
External APIs → Songbird Tower (HTTPS) → NestGate (content-addressed cache)
                                          ↓
                                    Spring Rust code
                                          ↓
                              barracuda GPU / metalForge Tower
                                          ↓
                              rhizoCrypt provenance DAG
                                          ↓
                              sweetGrass attribution
                                          ↓
                              pseudoSpore / guideStone artifact
```

Every external data system, regardless of trust tier, enters the ecosystem through the same pipeline: fetch → BLAKE3 hash → NestGate store → spring validation → provenance chain. The trust tier determines what happens *after* storage: T1 data flows directly to analysis, T2 data gets revalidated against underlying sources, T3 data becomes a reproduction target.

---

## Cross-References

- `gen4/foundations/README.md` — `sporeGarden/foundation` with 100+ anchors
- `attsi/non-anon/contact/gonzales/onboarding/DATA_SOURCES_AND_INTEGRATION.md` — the gen4-era full catalog
- `attsi/non-anon/contact/gonzales/onboarding/PRE_GRANT_PIPELINE.md` — open data scale rationale
- `gen3/baseCamp/EXTENSION_PLAN.md` — NCBI accession tiers with size estimates
- `gen5/thesis/SCIENTIFIC_CHALLENGES.md` — Synapse/DREAM challenge thesis
- `gen5/collaborators/JONES_BLUEFISH.md` — Jones data dump and PFAS data systems
- `gen5/collaborators/GONZALES_NF.md` — NF Data Portal and CTF datasets
- `attsi/non-anon/contact/ABG/ABG_PROJECTS_MAY2026.md` — ABG project data source mapping
- `attsi/non-anon/contact/ABG/projects/03_cazyme_landscapes/RESEARCH.md` — PLUMED-NEST survey (plumID references)
- `attsi/non-anon/contact/chuna/README.md` — ILDG/MILC interop for QCD
- `attsi/non-anon/contact/barrick/` — LTEE data provenance
- `gen4/architecture/GUIDESTONE_LTEE.md` — LTEE-specific dataset inventory

---

*gen3 fetched data to prove the instruments work. gen4 organized it into a geological record. gen5 fetches data because a collaborator has a question the ecosystem hasn't answered yet — and the provenance chain that started at a public API endpoint ends in someone else's science. But not all endpoints are equal. Primary sources get hashed and consumed. Secondary sources get revalidated. Derived sources get reproduced. The trust hierarchy is not bureaucracy — it is the difference between a provenance chain that proves something and one that merely claims it.*
