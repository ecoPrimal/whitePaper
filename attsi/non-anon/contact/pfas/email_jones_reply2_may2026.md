# Email: Jones Second Reply — MANA SODA + MRM Details — May 28, 2026

**From**: Dan Jones
**To**: Kevin Mok
**Subject**: Re: What I've been building — congratulations, and a question
**Date**: May 28, 2026

---

Kevin,

I would be glad to review, but since I have limited access to data sets and proprietary software these days, you might do well to connect with the MANA SODA group (focused on metabolomics; info at https://sites.google.com/metabolomicsna.org/soda/home), as they provide an assortment of resources including datasets and software that you may find useful.

Most of the open source tools don't give you information that allows for data quality review. MANA SODA was set up to encourage people to apply different processing software on common datasets to facilitate this (though most people don't want to go to that much effort).

At present, most PFAS analyses are targeted (multiple reaction monitoring, or MRM) analyses, so analysis of a single sample involves generation of about 100 different chromatograms (two each for most analytes, plus one each for the extracted and non-extracted internal standards). Each of the analyte chromatograms will have one (sometimes more) peaks integrated and reported (Ehab has been exporting these into a grand consolidated spreadsheet), so setting up all of the processing (peak integration) can be quite tedious compared to untargeted analyses.

I'm glad you found your time in the PFAS lab useful — we enjoyed having you as a team member and hope the coming months bring you great opportunities and experiences.

Best wishes,
Dan

---

## Extracted Intel

| Item | Value | blueFish Action |
|------|-------|-----------------|
| Consulting willingness | "I would be glad to review" | Confirmed — informal consulting relationship |
| Data access | "limited access to data sets and proprietary software" | Not a data source; architecture/QC advisor only |
| MANA SODA | metabolomics cross-validation consortium | Contact for benchmark datasets |
| MRM chromatograms/sample | ~100 (2/analyte + internal standards) | Architecture: batch 100 chromatograms per sample |
| Peak integration per chromatogram | 1+ peaks | Feature detection must handle multi-peak |
| Current export workflow | "grand consolidated spreadsheet" (Ehab) | Match output format for lab compatibility |
| Setup tedium | "quite tedious compared to untargeted" | Template-driven method setup is the product differentiator |
| Data quality review gap | "Most open source tools don't give you information for data quality review" | Visual QC is the primary feature gap to fill |
