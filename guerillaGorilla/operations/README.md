# guerillaGorilla — Operations

Active deployments of the guerillaGorilla framework.

Each subdirectory is an independent case/campaign.
bluegate-tenancy (Banks/Smith) is the original case validation
and lives in its own repo. Operations here are NEW deployments.

---

## Active Operations

### barry-county/ — Wire & Mail Fraud (Opened Sep 13, 2026)

**Target:** Barry County Circuit Court record manipulation
**Mode:** Cross-protection Mode 2 (Kevin Mok ↔ Rita Williams)
**Judge:** Michael Schipper (under JTC review)
**Core evidence:** Backdated docket entry + MDOC FOIA showing
no mail arrival
**Tech stack target:** MiCOURT (IBM Db2 / Power iSeries)
**Status:** Case file built, demand letter drafted

```
barry-county/
├── case/
│   ├── CASE_FILE_BARRY_COUNTY_SEP13.md    ← full investigative file
│   └── RITA_BARRY_COUNTY_SUPPORT_SEP13.md ← framework + binary trap
├── filing-ready/
│   └── DEMAND_BARRY_COUNTY_AUDIT_TRAIL.md ← 14-day demand letter
└── evidence/
    └── (pending — screenshots, FOIA responses, audit trail)
```

---

## Structure Convention

Each operation follows:

```
operation-name/
├── case/          ← investigative files, analysis, strategy
├── filing-ready/  ← letters, complaints, notifications ready to send
└── evidence/      ← screenshots, FOIA responses, documents
```

---

*guerillaGorilla operations directory.*
*The gorilla walks where the framework says to walk.*
