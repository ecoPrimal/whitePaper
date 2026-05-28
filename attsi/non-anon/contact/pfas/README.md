# PFAS Research Team — Contact Notes

**Team**: MSU PFAS Research Lab / Murphy Lab
**Kevin's role**: Former Research Specialist (Oct 2024–laid off Oct 2025)
**Domain**: Environmental chemistry, PFAS detection, mass spectrometry, EPA SOPs

---

## Team Members

### A. Daniel Jones, PhD
- **Title**: Professor Emeritus, Biochemistry & Molecular Biology, MSU (retired May 2026)
- **Location**: Rancho Cordova, CA (was always remote PI for PFAS project)
- **URL**: https://www.canr.msu.edu/news/center-for-pfas-research-faculty-spotlight-a-daniel-jones
- **Email**: jonesar4@msu.edu
- **Phone**: (517) 898-0504
- **Domain**: Analytical chemistry, mass spectrometry, PFAS detection, metabolomics, lipidomics
- **Relationship**: Former employer (remote PI). Replied May 27, 2026 with technical resources and retirement announcement.
- **wetSpring connection**: Track 2 blueFish — FindPFAS (17/17), EPA PFAS ML (14/14), MassBank spectral (9/9), 40/40 checks total

### Cheryl Murphy, PhD
- **Title**: Professor / PI, Department of Fisheries and Wildlife, MSU
- **Email**: camurphy@msu.edu
- **Phone**: (517) 432-7771
- **Domain**: PFAS Research Lab supervisor/PI
- **Relationship**: Supervisor at PFAS Research Lab

### Sima Kumar
- **Title**: Research Assistant III, Murphy Lab, Department of Fisheries and Wildlife
- **URL**: https://www.canr.msu.edu/people/sima-kumar/
- **Relationship**: Peer (RA III in Murphy Lab)

---

## Status

- Kevin was laid off Oct 2025. This is reaching back to former colleagues.
- wetSpring Track 2 has 40/40 checks reproducing PFAS detection papers
- Project blueFish is the intended product: sovereign PFAS data pipeline replacing Chromeleon and vendor-locked analytical software
- Email drafted May 2026 (`email_spore_may2026.md`) — pseudoSpore attached as example
- **New lab manager**: Dr. Aswin Kumar Ilango (started recently, replacing Jones as on-site lead)

## Dan Jones Response — May 27, 2026

Jones replied same day. Now **Professor Emeritus** (retired). Provided three technical resources:

### 1. NIST Reference Data for Untargeted PFAS
- URL: https://www.nist.gov/programs-projects/and-polyfluoroalkyl-substances-pfas/research/reference-data-and-tools/
- **blueFish target**: Ingest NIST reference spectra as validation baseline for untargeted analysis

### 2. EPA Method 1633A (Targeted Analysis of 40 PFAS)
- URL: https://www.epa.gov/system/files/documents/2024-12/method-1633a-december-5-2024-508-compliant.pdf
- **Jones's domain insight**: Most labs (including commercial) don't actually perform all QC checks — particularly **ion abundance ratios**. No published data exists to evaluate QC compliance beyond single-letter qualifiers in lab reports.
- **LOQ reporting problem**: State labs report measurements below LOQ as equal to LOQ (not "< LOQ") because they can't verify lower values. Jones personally corrected Grayling MI water reports — levels not as bad as reported.
- **blueFish target**: Implement full 1633A QC checks including ion abundance ratios. Automated QC compliance verification that commercial labs aren't doing. This is the gap.

### 3. LC/MS File Conversion (Chromeleon → Open Formats)
- Chromeleon Console exports to .mzML or .CDF
- **Proteowizard msConvert**: https://proteowizard.sourceforge.io/ — the standard converter
- **blueFish target**: Sovereign mzML/CDF ingestion, bypassing Chromeleon entirely for downstream analysis

### Jones's Assessment of Open-Source Tools
- **MZmine** (https://github.com/mzmine) — unacceptable failure rates
- **MS-DIAL** (https://zenodo.org/records/12589462) — same
- **XCMS** (https://sneumann.github.io/xcms/) — same
- **Progenesis QI** (Nonlinear Dynamics) — had good graphical evaluation, now **obsolete**
- **The gap**: No open-source tool gives acceptable failure rates AND graphical evaluation of feature detection/measurement quality
- **blueFish opportunity**: Fill exactly this gap — low failure rate + visual QC + sovereign + validated

## Strategy

Jones is now emeritus and willing to engage. Ask for ongoing consulting/review. He knows where the bodies are buried (QC compliance, LOQ reporting, tool failure rates). His expertise validates blueFish design decisions.

Sima and Cheryl are the on-campus contacts. Dr. Aswin Kumar Ilango is the new lab manager — potential new contact.

Connection to Chuna: Jones is in California, Chuna is heading to LANL. Both are remote collaborators in different domains.
