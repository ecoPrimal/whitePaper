# GPS Platform — Data Manifest

**Purpose**: Complete inventory of every data file required for the GPS sovereign rebuild.
Every source is public. Every file is hashable. No proprietary dependencies.

**Storage target**: biomeGate NVMe array (~500 GB available)
**Fetch policy**: Primary sources only (GEO, not mirrors). BLAKE3 hash on arrival.

---

## Tier 1: Required for Reproduction (~35 GB)

### 1.1 GPS Code + Models (Zenodo)

```powershell
# Create working directory
mkdir C:\Data\gps\zenodo
cd C:\Data\gps\zenodo

# v5 (original deposit, 712.7 MB total)
# Record: https://zenodo.org/records/17653393
# Files: RCL.zip, GPS4Drugs.zip, MolSearch.zip, data_for_GPS_figures.zip
curl -L -o gps_v5_all.zip "https://zenodo.org/records/17653393/files/archive.zip"

# v6 (adds figure_code.zip, 840.3 MB total)
# Record: https://zenodo.org/records/17956238
curl -L -o gps_v6_all.zip "https://zenodo.org/records/17956238/files/archive.zip"
```

| File | MD5 (from Zenodo) | Size (est.) |
|------|-------------------|-------------|
| RCL.zip | TBD (resolve from v5 manifest) | ~40 MB |
| GPS4Drugs.zip | TBD | ~100 MB |
| MolSearch.zip | TBD | ~518 MB |
| data_for_GPS_figures.zip | TBD | ~151 MB |
| figure_code.zip (v6 only) | TBD | ~30 MB |

**MD5 anchors** (from Zenodo, file↔hash mapping to resolve during Phase 0):
```
c612db1387b1375fe6f395da9139f631
4e0aa3c27edb952f9ecc0f0ddf0179a1
73be3c9c3b86a20bcecb059fde9f2fa5
86d3f3a95c324c9479bd8986968f4327
30744d7dcc70490f79a1ce16ff5162de
4b04fc59f0e1ef57c3f24ba8e4891207
a9f1c26b77220fcb9590a06e23c72777
```

### 1.2 GPS GitHub Repository

```powershell
mkdir C:\Data\gps\code
cd C:\Data\gps\code

git clone https://github.com/Bin-Chen-Lab/GPS.git
git clone https://github.com/illidanlab/MolSearch.git
git clone https://github.com/Bin-Chen-Lab/RGES.git
git clone https://github.com/Bin-Chen-Lab/octad.git
```

### 1.3 LINCS L1000 Level 5 — Phase 1 (GSE92742, ~23 GB)

The core training data. 473,647 signatures × 12,328 genes.

```powershell
mkdir C:\Data\gps\lincs
cd C:\Data\gps\lincs

# Level 5 signatures (MODZ — this is what GPS trains on)
curl -L -o GSE92742_Level5_COMPZ_n473647x12328.gctx.gz ^
  "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742_Broad_LINCS_Level5_COMPZ.MODZ_n473647x12328.gctx.gz"

# Metadata (perturbagen info, cell line info)
curl -L -o GSE92742_inst_info.txt.gz ^
  "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742_Broad_LINCS_inst_info.txt.gz"
curl -L -o GSE92742_pert_info.txt.gz ^
  "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742_Broad_LINCS_pert_info.txt.gz"
curl -L -o GSE92742_gene_info.txt.gz ^
  "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742_Broad_LINCS_gene_info.txt.gz"
curl -L -o GSE92742_sig_info.txt.gz ^
  "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742_Broad_LINCS_sig_info.txt.gz"
```

| File | Size | Contents |
|------|------|----------|
| Level5 COMPZ MODZ | 23 GB | 473,647 consensus signatures |
| inst_info | ~100 MB | Instance-level metadata |
| pert_info | ~20 MB | Perturbagen compound/gene info |
| gene_info | ~1 MB | 12,328 gene annotations |
| sig_info | ~50 MB | Signature-level metadata |

### 1.4 LINCS L1000 Level 5 — Phase 2 (GSE70138, ~5 GB)

Extended data. 118,050 additional signatures.

```powershell
cd C:\Data\gps\lincs

curl -L -o GSE70138_Level5_COMPZ_n118050x12328.gctx.gz ^
  "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138_Broad_LINCS_Level5_COMPZ_n118050x12328_2017-03-06.gctx.gz"
```

### 1.5 ChEMBL Transformation Rules (MolSearch dependency, 1.5 GB)

```powershell
mkdir C:\Data\gps\chembl
cd C:\Data\gps\chembl

# From Figshare (referenced by illidanlab/MolSearch README)
curl -L -o chemblDB3.sqlitdb ^
  "https://figshare.com/ndownloader/articles/12912080/versions/1"
```

### 1.6 ZINC Screened Subset (~5 GB)

The specific subset GPS screened. Exact files TBD from GPS code analysis.

```powershell
mkdir C:\Data\gps\zinc
# Exact download commands to be determined during Phase 0
# GPS likely uses a pre-filtered SMILES file or pre-computed fingerprints
# Check GPS4Drugs/data/ for references
```

---

## Tier 2: Required for Full Validation (~14 GB)

### 2.1 OCTAD Database (~6 GB)

19,127 patient tissue samples. Used for cross-validation of disease signatures.

```powershell
mkdir C:\Data\gps\octad
cd C:\Data\gps\octad

# From Bioconductor ExperimentHub
curl -L -o octad.counts.and.tpm.h5 ^
  "https://experimenthub.bioconductor.org/fetch/7327"
```

### 2.2 ChEMBL Full Database (~3 GB)

Compound activity measurements for validation.

```powershell
mkdir C:\Data\gps\chembl_full
cd C:\Data\gps\chembl_full

# Latest ChEMBL SQLite (check version at time of download)
curl -L -o chembl_34.db.gz ^
  "https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_34_sqlite.tar.gz"
```

### 2.3 TCGA Expression Data — HCC + IPF subsets (~2 GB)

```powershell
mkdir C:\Data\gps\tcga
cd C:\Data\gps\tcga

# Use GDC Data Transfer Tool or direct API
# HCC = LIHC project, IPF = not in TCGA (use GEO instead)
# Exact manifest to be generated from GDC portal during Phase 0
```

### 2.4 CCLE (Cancer Cell Line Encyclopedia, ~1 GB)

```powershell
mkdir C:\Data\gps\ccle
cd C:\Data\gps\ccle

# From DepMap portal
curl -L -o CCLE_expression.csv ^
  "https://depmap.org/portal/download/api/download?file_name=CCLE_expression.csv"
```

### 2.5 Enamine HTS Library (subset, ~2 GB)

```powershell
mkdir C:\Data\gps\enamine
# Commercial library — check if GPS used a public subset
# Exact access to be determined during Phase 0 code analysis
```

---

## Tier 3: Full Archaeology (~268 GB)

Only needed if we want to revalidate from raw instrument data.

### 3.1 LINCS L1000 Level 1 — Raw Fluorescence (223 GB)

```powershell
# WARNING: 223 GB download
# Only fetch if revalidating the entire L1000 pipeline from bead-level
cd C:\Data\gps\lincs

curl -L -o GSE70138_Level1_LXB.tar.gz ^
  "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE70nnn/GSE70138/suppl/GSE70138_Broad_LINCS_Level1_LXB_n345976_2017-03-06.tar.gz"
```

### 3.2 LINCS L1000 Level 2-4 (~45 GB combined)

```powershell
# Level 2: raw gene expression (978 genes)
# Level 3: normalized + inferred (12,328 genes)
# Level 4: z-scores per plate
# Only needed for pipeline archaeology
```

---

## NF Extension Data (~5 GB)

### NF Data Portal

```powershell
mkdir C:\Data\gps\nf
cd C:\Data\gps\nf

# NF Data Portal on Synapse
# Requires Synapse account (free, academic)
# Use synapseclient Python package
pip install synapseclient
# Then: synapse get syn26561828 -r  (example — exact IDs from portal)
```

### NF Disease Signatures

| Source | What | Size |
|--------|------|------|
| NF Data Portal | NF1/NF2 tumor expression | ~2 GB |
| GEO NF studies | Supplementary NF profiles | ~1 GB |
| TCGA NF1 subset | Pan-cancer NF1-mutant samples | ~500 MB |

---

## Verification Protocol

### On Download

Every file gets a BLAKE3 hash on arrival:

```powershell
# Using b3sum (install: cargo install b3sum)
b3sum GSE92742_Level5_COMPZ_n473647x12328.gctx.gz >> C:\Data\gps\HASHES.b3
b3sum GPS4Drugs.zip >> C:\Data\gps\HASHES.b3
# ... for every file
```

### Cross-Check Against Zenodo MD5

```powershell
# Verify Zenodo downloads match their published MD5
certutil -hashfile RCL.zip MD5
# Compare against manifest above
```

### guideStone Integration

Once Phase 1 begins, every reproduction step produces a guideStone check:

```
CHECK: rcl_vcap_t1_reproduction
  INPUT_HASH: [BLAKE3 of input L1000 subset]
  OUTPUT_HASH: [BLAKE3 of cleaned profiles]
  MATCH_TARGET: [their published cleaned profiles from Zenodo]
  STATUS: PASS/FAIL
  DELTA: [quantified difference if any]
```

---

## Storage Layout (biomeGate)

```
C:\Data\gps\                          (~350 GB total when full)
├── zenodo\                           (840 MB — GPS artifacts)
│   ├── v5\
│   │   ├── RCL.zip
│   │   ├── GPS4Drugs.zip
│   │   ├── MolSearch.zip
│   │   └── data_for_GPS_figures.zip
│   └── v6\
│       └── figure_code.zip
├── code\                             (~500 MB — all repos)
│   ├── GPS\
│   ├── MolSearch\
│   ├── RGES\
│   └── octad\
├── lincs\                            (~28 GB Tier 1 / ~296 GB with archaeology)
│   ├── GSE92742_Level5_*.gctx.gz
│   ├── GSE70138_Level5_*.gctx.gz
│   └── metadata\
├── chembl\                           (1.5 GB rules + 3 GB full)
│   ├── chemblDB3.sqlitdb
│   └── chembl_34.db
├── zinc\                             (~5 GB)
├── octad\                            (~6 GB)
├── tcga\                             (~2 GB)
├── ccle\                             (~1 GB)
├── nf\                               (~5 GB)
├── HASHES.b3                         (running hash manifest)
└── rebuild\                          (our implementation output)
    ├── rcl\
    ├── gps4drug\
    ├── molsearch\
    └── guidestones\
```

---

## Download Priority Order

Phase 0 archaeology doesn't need everything at once. Download in this order:

| Priority | What | Size | Why First |
|----------|------|------|-----------|
| 1 | Zenodo v6 | 840 MB | See what they shipped. Inventory. |
| 2 | GPS + MolSearch GitHub | 500 MB | Read the code. Map dependencies. |
| 3 | L1000 Level 5 Phase 1 | 23 GB | The training data. Core of everything. |
| 4 | ChEMBL rules | 1.5 GB | MolSearch can't run without this. |
| 5 | L1000 Phase 2 | 5 GB | Extended training. |
| 6 | ChEMBL full | 3 GB | Activity validation. |
| 7 | OCTAD | 6 GB | Cross-validation baseline. |
| 8 | ZINC subset | 5 GB | Screening library (exact subset TBD from code). |
| 9 | TCGA + CCLE | 3 GB | Disease signatures + cell line mapping. |
| 10 | NF Data Portal | 5 GB | Extension target (after base validated). |
| 11 | L1000 Levels 1-4 | 268 GB | Archaeology. Only if revalidating from raw. |

**Start with 1-5. That's ~30 GB and enough to begin reproduction.**

---

## Tools Required for Data Access

| Tool | Purpose | Install |
|------|---------|---------|
| `curl` | HTTP downloads | Built-in (Windows 10+) |
| `b3sum` | BLAKE3 hashing | `cargo install b3sum` |
| `cmapPy` | Read GCTx files | `pip install cmapPy` |
| `h5py` | Read HDF5 (OCTAD) | `pip install h5py` |
| `synapseclient` | NF Data Portal access | `pip install synapseclient` |
| `gdc-client` | TCGA downloads | Download from GDC portal |
| `7z` | Extract archives | `choco install 7zip` |

---

*Every byte traced to source. Every hash recorded on arrival. No trust without verification.
This is what it means to rebuild from true scratch — not from someone's Docker image,
not from someone's conda env, but from the data itself.*
