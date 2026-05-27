# Project 3: Conformational Energy Landscapes for CAZyme Docking Validation

## Upstream Validation Research Package

**Project Lead**: Alistaire (ABG)
**Timeline**: Semester+
**Core Question**: Can AutoDock Vina molecular docking of monosaccharide ring conformations serve as a computationally cheap surrogate for full conformational energy landscape (FEL) calculations in predicting catalytically competent sugar geometries inside CAZyme active sites?

---

## Reference Paper

**Ardèvol & Rovira 2015**, *JACS* 137:7528–7547
"Reaction Mechanisms in Carbohydrate-Active Enzymes: Glycoside Hydrolases and Glycosyltransferases. Insights from ab Initio QM/MM Dynamic Simulations"
DOI: 10.1021/jacs.5b01156

### Key Concepts from the Paper (esp. Fig 10)

- Glycoside hydrolases (GHs) distort the substrate sugar ring from ground-state chair (⁴C₁) into catalytically competent conformations
- The **catalytic itinerary** = sequence of ring conformations through Michaelis complex → transition state → product
- Fig 10 maps known itineraries onto the Stoddart diagram (Mercator projection of the Cremer-Pople sphere)
- QM/MM metadynamics with Cremer-Pople (θ, φ) as collective variables produces the FEL
- Different GH families follow distinct itineraries (e.g., retaining GHs: ¹S₃ → [⁴H₃]‡ → ⁴C₁; inverting GHs have other paths)

### Alistaire's Hypothesis

Docking with AutoDock Vina (cheap, seconds/pose) should preferentially score conformations along the catalytic itinerary higher (better binding) than non-itinerary conformations, approximating the FEL computed via expensive QM/MM metadynamics (hours to days/system).

---

## Software Stack

### Molecular Docking

| Tool | Source | Version | Purpose |
|------|--------|---------|---------|
| AutoDock Vina | github.com/ccsb-scripps/AutoDock-Vina | v1.2.7 (Feb 2025) | Standard docking |
| Vina-Carb | glycam.org | — | Modified Vina with CHI-energy carbohydrate torsion penalties |
| Open Babel | openbabel.org | — | Format conversion (PDB ↔ PDBQT), ligand preparation |
| MGLTools / AutoDockTools | mgltools.scripps.edu | — | Receptor preparation, grid box definition |

### Ring Conformation Generation

| Tool | Source | Purpose |
|------|--------|---------|
| Cremer-Pople Calculator | enzyme13.bt.a.u-tokyo.ac.jp/CP/ | Online CP parameter calculation from PDB coords |
| Marcello-Sega/sugar-puckering | github.com/Marcello-Sega/sugar-puckering | C code: reconstruct ring atoms from CP coords, GROMACS topologies |
| PLUMED (PUCKERING module) | plumed.org | Calculate/bias CP coordinates in metadynamics; 6-ring (qx,qy,qz) and polar (Q,φ,θ) |
| GLYCAM-Web CP Utility | glycam.org/downloads/software/ | CP trajectory analysis for AMBER |
| Privateer (CCP4) | ccp4i2 | Validate carbohydrate conformations in crystal structures |

### Conformational Energy Landscapes (the "expensive" reference)

| Tool | Source | Purpose |
|------|--------|---------|
| CP2K | cp2k.org | ab initio QM/MM MD (DFT: BLYP/DZVP typical) |
| GROMACS | gromacs.org | Classical MD, enhanced sampling |
| PLUMED | plumed.org | Metadynamics bias (well-tempered), umbrella sampling |
| Gaussian / ORCA | — | QM single-point or optimization in QM/MM |
| AMBER + GLYCAM06 | ambermd.org | Carbohydrate force field for classical simulations |
| GROMOS 45a4 (modified) | see Sega et al. 2010 | Force field with improved puckering FEL for hexopyranoses |

### Structure Sources

| Source | URL | Content |
|--------|-----|---------|
| CAZy Database | cazy.org | GH family classification, links to PDB structures |
| ez-CAZy | (Sci Rep 2025) | 7,000+ biochemically characterized GHs with functional annotations |
| PDB / RCSB | rcsb.org | 3D structures of GH-substrate complexes |
| AlphaFold DB | alphafold.ebi.ac.uk | Predicted structures for GHs without crystal structures |

---

## Datasets

### Input Structures Needed

For each GH family selected:
1. **Representative enzyme structure** with bound substrate/inhibitor (PDB entry)
2. **Monosaccharide ring conformations**: All 38 canonical pyranose conformations on the Stoddart diagram:
   - 2 chairs: ⁴C₁, ¹C₄
   - 6 boats: 1,4B, B₁,₄, 2,5B, B₂,₅, 3,OB, BO,₃
   - 6 skew-boats: ¹S₃, ³S₁, ²Sₒ, ᵒS₂, ¹S₅, ⁵S₁
   - 12 half-chairs: ³H₂, ²H₃, ⁴H₃, ³H₄, ⁵H₄, ⁴H₅, ᵒH₅, ⁵Hₒ, ¹Hₒ, ᵒH₁, ²H₁, ¹H₂
   - 12 envelopes: E₁, ²E, E₃, ⁴E, E₅, ᵒE, ¹E, E₂, ³E, E₄, ⁵E, Eₒ

### Candidate GH Families for Pilot

| Family | Mechanism | Known Itinerary | Example PDB | Substrate |
|--------|-----------|-----------------|-------------|-----------|
| GH1 | Retaining | ⁴C₁ → ⁴H₃ → ⁴C₁ | 1OIF | β-glucoside |
| GH5 | Retaining | ¹S₃ → [⁴H₃]‡ → ⁴C₁ | 4W8B | β-mannan |
| GH10 | Retaining | ¹S₃ → [⁴H₃]‡ → ⁴C₁ | 1E0X | β-xylan |
| GH11 | Retaining | ²Sₒ → [²,⁵B]‡ → ⁵S₁ OR ¹S₃ → [⁴H₃]‡ → ⁴C₁ | 1BCX | β-xylan |
| GH13 | Retaining | ⁴C₁ → [⁴H₃]‡ → ⁴C₁ | 1EA9 | α-amylose |
| GH26 | Retaining | ᵒS₂ → [²,⁵B]‡ → ⁵S₁ | 2QHA | β-mannan |
| GH47 | Inverting | ³S₁ → [³H₄]‡ → ¹C₄ | 1DL2 | α-mannoside |
| GH117 | Inverting | ¹,⁴B → [⁴E]‡ → ¹,⁴B | 4AK5 | β-agarose |

---

## Key Papers (Dependency Chain)

### Foundational

| Paper | Year | Key contribution |
|-------|------|-----------------|
| Cremer & Pople, JACS | 1975 | Puckering coordinates for cyclic molecules |
| Stoddart, *Stereochemistry of Carbohydrates* | 1971 | Stoddart diagram / Mercator projection of CP sphere |
| Ardèvol & Rovira, JACS | 2015 | Review of QM/MM catalytic itineraries in GH/GT families |

### Ring Conformational Free Energy Landscapes

| Paper | Year | System | Method |
|-------|------|--------|--------|
| Sega et al., J Chem Phys | 2010 | All hexopyranoses (α/β) | Metadynamics + umbrella sampling (GROMOS 45a4 modified) |
| Iglesias-Fernández et al., Chem Sci | 2015 | β-xylose complete FEL | ab initio metadynamics (CP2K, BLYP-D3) |
| Spiwok et al., Carbohydr Res | 2010 | β-D-glucopyranose | Metadynamics (GLYCAM06, GROMOS, OPLS) |
| Barnett et al., JACS | 2010 | Various GHs | QM/MM metadynamics for transition states |
| Speciale et al., Front Chem | 2019 | Sucrose / amylosucrase GH13 | QM/MM metadynamics, conformational itinerary |

### Carbohydrate Docking

| Paper | Year | Key contribution |
|-------|------|-----------------|
| Nivedha et al., JCTC | 2016 | Vina-Carb: CHI-energy penalty improves carb docking (55%→74% success) |
| Agirre et al., Struct Biol | 2015 | Privateer: carbohydrate validation in crystal structures |
| Toukach & Egorova, Chem Rev | 2016 | Carbohydrate–protein interactions review |
| Ardá & Jiménez-Barbero, Chem Commun | 2018 | NMR + computational for protein-carbohydrate interactions |

---

## Reproducibility Analysis Plan

### Phase 1: Pilot (1 GH family)

1. Select GH family with well-characterized itinerary (e.g., GH10 β-xylanase, 1E0X)
2. Generate 38 canonical ring conformations of β-xylose using CP_reconstruct from Sega/sugar-puckering
3. Dock all 38 conformations into active site with AutoDock Vina (standard) and Vina-Carb
4. Rank by binding affinity (kcal/mol)
5. Compare ranking with known catalytic itinerary: do itinerary conformations score in top quartile?

### Phase 2: FEL Reference Calculation

1. Set up GROMACS + PLUMED for metadynamics of β-xylose in GH10 active site
2. Use CP (θ, φ) as collective variables in well-tempered metadynamics
3. Compute 2D FEL on Stoddart diagram
4. Compare FEL minima with Vina docking score ranking
5. Quantify correlation (Spearman ρ between FEL depth and Vina score per conformation)

### Phase 3: GH Family Survey

1. Repeat Phase 1 across 5-8 GH families (Table above)
2. Categorize: which families show good docking-FEL correlation? Which fail?
3. Test if retaining vs inverting mechanism affects correlation quality
4. Test if Vina-Carb's CHI corrections improve correlation vs standard Vina

### Phase 4: Ring Generator Validation (Alistaire's tangent)

1. Validate CP_reconstruct outputs against Privateer-validated crystal conformations
2. Compare with PLUMED-computed CP coordinates from MD trajectories
3. Assess whether generated conformations adequately sample the CP sphere

---

## Computational Resource Estimates

| Step | Time/system | GPU? | Parallelizable? |
|------|-------------|------|----------------|
| Vina docking (38 conformations) | ~5 min total | No (CPU) | Yes per conformation |
| Vina-Carb docking (38 conf.) | ~5 min total | No (CPU) | Yes |
| Classical MD setup + equilibration | ~2-4 hours | Yes (GROMACS GPU) | Per system |
| Well-tempered metadynamics (FEL) | ~12-48 hours | Yes | Per system |
| QM/MM metadynamics (reference) | ~5-20 days | Partial | Per system |

Docking is cheap enough to run on any laptop. FEL calculations require HPC — this is the core of Alistaire's argument for why the docking surrogate would be valuable.

---

## Spring-Specific Validation Targets

### hotSpring

- [ ] AutoDock Vina docking of pyranose conformations into GH active sites
- [ ] Vina-Carb comparative docking with CHI-energy corrections
- [ ] Cremer-Pople coordinate generation for all 38 canonical conformations
- [ ] PDB structure preparation (receptor PDBQT, grid box definition)
- [ ] Structure visualization (PyMol / VMD)

### primalSpring

- [ ] GROMACS + PLUMED metadynamics setup with CP collective variables
- [ ] Well-tempered metadynamics FEL calculation
- [ ] Force field comparison (GLYCAM06 vs modified GROMOS 45a4)
- [ ] Convergence assessment (block analysis, FEL difference over time)

### groundSpring

- [ ] Correlation analysis: Vina score vs FEL depth per conformation
- [ ] Statistical framework for docking-FEL agreement
- [ ] Sensitivity analysis: grid box size, exhaustiveness, Vina-Carb parameters
- [ ] Multi-family meta-analysis of docking surrogacy quality

### airSpring

- [ ] Stoddart diagram visualization of docking scores (heatmap on CP sphere)
- [ ] Overlay of docking results with known catalytic itineraries
- [ ] Interactive comparison of FEL vs docking landscapes

---

## Deliverables

### pseudoSpore v1.6.1 — CompChem GuideStone (May 27, 2026)

First formal ABG deliverable. Shipped to Discord as 5.7 MB tarball, 76 files.

**What it delivers:**
- 6 computational modules: free β-D-xylopyranose vs GH10 enzyme-bound (PDB 2D24). 1D theta + 2D Stoddart. Alanine dipeptide + chignolin OPES method controls.
- PLUMED-NEST survey (Module 07): 8 targets, including Grothaus 2022 (plumID:22.028) and Grothaus 2025 (plumID:25.007)
- Exploration roadmap (Module 08): 13 targets across 3 priority tiers
- Full reproducibility: solvated .gro (2,657-atom free xylose, 92,745-atom enzyme), topologies, MDPs, PLUMED inputs with inline index translation
- 71 automated checks PASS. Self-verifying: `./validate`
- Pipeline-generated figures (Ramachandran, 1D FES, Stoddart diagram, enzyme-vs-free comparison)

**Key results:**
- Free xylose: ⁴C₁/boat/¹C₄ basins, barriers 38–53 kJ/mol
- Enzyme-bound: all barriers lowered 1–5 kJ/mol, conformational selection visible in 2D
- Consistent with Iglesias-Fernández 2015: ²S₀ → [²,⁵B]‡ → ⁵S₁ and ¹S₃ → [⁴H₃]‡ → ⁴C₁

**Provenance evolution:**
- Era 1 (v0.6.0–v1.6.0): Hand-authored metadata. v0.6.0 had atom index errors and lyxose contamination caught by Alistaire
- Era 2 (v1.6.1): Pipeline-derived metadata, agentic deploy, every value extracted from authoritative data files
- Era 3 (target v2.0+): NUCLEUS provenance trio signs via `biomeos nucleus ingest`

**Pending domain questions for Alistaire:**
1. Puckering convention: θ=0 → ⁴C₁ (north), θ=π → ¹C₄ (south). Cross-check against Iglesias-Fernández Fig 10?
2. Force field: CHARMM36-jul2022 vs GROMOS 45A4 vs GLYCAM06 for epimer baselines?
3. Convergence: 10 ns metadynamics sufficient for publication, or need 50–200 ns?

**Next (from Module 08 roadmap):**
- Tier 1 (~10 hr): Free lyxose/glucose/mannose/galactose + 2D24 −2/+1 subsites
- Tier 2 (~8 hr): GH11 inverting (1XYN) + 1E0X covalent intermediate
- Tier 3: AutoDock Vina ↔ FEL correlation (the core question)

---

## FOUNDATION Thread Linkage

- **Structural Biology / Computational Chemistry**: Core domain — enzyme mechanism prediction
- **Anderson Framework**: Subtle connection — the enzyme active site is the ultimate bounded 3D micro-niche, where substrate conformation is dictated by the geometry of confinement. Ring distortion during catalysis is geometry-enforced chemistry.
