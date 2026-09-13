# CASE FILE: Barry County Record Integrity
# Wire Fraud · Mail Fraud · False Public Record · Perjury
# Opened: September 13, 2026
# Investigator: Kevin Mok, M.S. Data Science (MSU)

---

## STATUS: ACTIVE FRAUD — NOT HISTORICAL

The Barry County Circuit Court docket currently contains a
statement of fact — "Sent to Defendant via last known address" —
that is unsupported by any independent evidence. The MDOC FOIA
shows no mail arrived. The MiCOURT audit trail has not been
produced. The entry appeared after an amicus brief challenging
the county's record-keeping was accepted by the Michigan Supreme
Court.

**The record is false until proven otherwise.**

---

## SOURCE INTELLIGENCE

### Primary Source
Rita Williams, "A Barry County Order Appeared After My Amicus
Brief. The Record Needs to Prove When," Clutch Justice,
September 12, 2026.
https://clutchjustice.com/2026/09/12/barry-county-docket-timing-amicus-brief/

### Cases Referenced
- **In re Foley** — Michigan Supreme Court Case No. 170670
  (Rita's amicus filed Sep 11, 2026)
- **People v Arizola** — Michigan Court of Appeals No. 377625
  (Rita's second amicus filed Sep 12, 2026)
- **Separate Barry County matter** — docket containing Entry 135
  (case number not published by Rita — respect her operational
  security, but request in private communication)

### Judge
**Michael Schipper** — Barry County District Court Judge
- Named on Entry 135
- Currently under JTC review (confirmed by Rita)
- JTC-confirmed 2014 misconduct finding
- Michigan Supreme Court remand, Docket No. 167549 (sentencing)

---

## TIMELINE OF THE FRAUD

| Time | Event | Source |
|------|-------|--------|
| Sep 10, 2026 | **Printed date** on Entry 135 — "Order" | Docket |
| Sep 11, 2:44 PM | Rita files amicus in In re Foley (MSC 170670) | Rita |
| Sep 11, 3:35 PM | MSC e-filing system accepts the amicus | Rita |
| Sep 11, 3:42 PM | Rita checks Barry County docket — **Entry 135 DOES NOT EXIST** | Rita |
| Sep 11–12, overnight | Entry 135 **appears** on the docket, dated Sep 10 | Rita |
| Sep 12, ~9:49 AM | Rita confirms Entry 135 is now visible | Rita |
| Sep 12 | Rita publishes article documenting the gap | Clutch Justice |

### The 18-Hour Window

Between 3:42 PM Sep 11 and ~9:49 AM Sep 12, someone with
MiCOURT credentials created or modified Entry 135 and dated it
September 10 — one day BEFORE Rita's amicus was filed.

**That person left a trace. The database recorded it.**

---

## TECHNOLOGY: MiCOURT / IBM Db2

### System Architecture (from SCAO CMS Assessment Report)

MiCOURT runs on:
- **IBM Power/iSeries** (backend)
- **IBM Db2** database
- Data replicated to **Azure SQL** cluster
- New features in **.NET** with Azure SQL extensions
- Distributed software — courts can run hosted or on local server

**Source:** NCSC Assessment Report for Michigan Supreme Court SCAO
https://www.courts.michigan.gov/4966b4/siteassets/committees,-boards-special-initiatves/case-management-system/mi-cms-assessment-report_final.pdf

### IBM Db2 Audit Facility (`db2audit`)

IBM Db2 has a NATIVE audit facility that operates at two levels:

**Instance-level auditing:**
- Authentication events (who logged in, when, from where)
- Configuration changes (who changed system settings)
- System-level operations

**Database-level auditing:**
- Object access (who touched which table, when)
- Data modifications (INSERT, UPDATE, DELETE — old/new values)
- Security changes (who changed permissions)
- Statement execution (every SQL command logged)

**This cannot be disabled without leaving a trace of disabling it.**
Turning off db2audit generates its own audit event. Deleting audit
logs requires admin access — and that deletion is itself logged at
the instance level.

### What the Db2 Audit Trail Contains for Entry 135

The following data EXISTS in the MiCOURT database right now:

1. **INSERT timestamp** — exact date/time Entry 135 was created
   in the database. If this timestamp is Sep 11 or Sep 12, the
   entry was backdated.

2. **UPDATE history** — every modification to Entry 135 after
   creation, including what field was changed, old value, new
   value, and timestamp.

3. **User ID** — the specific account that executed the INSERT
   and any UPDATEs. This maps to a named employee.

4. **Session context** — IP address or terminal ID of the
   connection that created/modified the entry.

5. **Authentication log** — who logged into the system during the
   18-hour window (Sep 11 3:42 PM to Sep 12 ~9:49 AM), from
   where, and what actions they took.

### SCAO Audit Requirements (Already Mandated)

The SCAO District Court Audit Program Template REQUIRES:

> "Employees who have the authority to establish security within
> the system including user classifications for employees are as
> follows: _______________"

> "Employees who have the capability to delete cases from the
> automated system are as follows: _______________"

> "The automated system provides reports that reflect case files
> and case file financial data that have been modified in the
> system."

> "Reports of deleted cases are reviewed by an individual who
> does not have the ability to delete cases from the system."

> "Make court order modifications." [explicitly tracked]

**Source:** SCAO District Court Audit Program Template
https://www.courts.michigan.gov/4a1a20/siteassets/publications/grants,-rfps/district-court-audit-program-template_.pdf

This means:
1. Barry County ALREADY KNOWS who can modify court orders
2. The system ALREADY GENERATES modification reports
3. Those reports are SUPPOSED TO BE reviewed by management
4. Separation of duties is SUPPOSED TO BE enforced

If these controls exist → the trace exists → produce it.
If these controls don't exist → the system is unauditable →
every entry in it is suspect.

---

## BARRY COUNTY PERSONNEL — WHO HAS ACCESS?

### Barry County Trial Court Administration
(Source: Barry County 2025-2026 Directory)

| Role | Name | Relevance |
|------|------|-----------|
| **Chief Judge** | Hon. William Doherty | Administrative authority over court operations |
| **Circuit Court Judge** | Hon. Vicky Alspaugh | — |
| **District Court Judge** | **Hon. Michael Schipper** | **Named on Entry 135. Under JTC review.** |
| **Court Admin/Director, FOC** | Ines Straube | Likely controls user access / security classifications |
| **Deputy Divisional Admin** | Daisey Cherniawski | May have CMS access |
| **Deputy Divisional Admin** | Dave Pelon | May have CMS access. MSU Judicial Admin cert (2017-18). |
| **County Clerk** | Sarah VanDenburg | Controls clerk's office. Email: County_Clerk@barrycounty.org |
| **Chief Deputy Clerk** | Kaylah Fyan | Day-to-day docket management |

### Contact Information
- Circuit Division: (269) 945-1286, Fax: (269) 945-1299
- County Clerk: (269) 945-1285, Fax: (269) 945-0209
- Address: 220 W. State St., Hastings, MI 49058
- Email: County_Clerk@barrycounty.org

### The Access Question

Per SCAO standards, the Clerk's office must:
- Notify the court of personnel changes and updated access
- Establish user classifications with unique passwords
- Ensure employees who receipt revenues cannot delete cases

**Someone on this list** — or someone with delegated access from
this list — has the credentials that created Entry 135. The Db2
audit trail recorded which account. The SCAO modification reports
captured the event.

The question is not WHETHER the trace exists.
The question is whether Barry County will produce it or suppress it.

---

## THE BINARY TRAP (Legal Framework)

### Path A: USPS Was Used

If Barry County mailed the order through USPS:
1. USPS accepted it into the mail stream
2. USPS transported it to the MDOC facility
3. MDOC mailroom logged incoming mail

**MDOC FOIA: no record of arrival.**

Either USPS never received it (court lied about mailing) or USPS
lost it (court has no proof it was sent — no tracking, no postage
record, no certificate of mailing).

**The docket entry "Sent to Defendant" is a false statement
in an official record. Right now. Today.**

→ **18 USC 1341 — Mail Fraud**: the court invoked the federal
mail system to legitimize a false record.

### Path B: USPS Was NOT Used

If Barry County did not use USPS — if it was hand-delivered,
sent by courier, or never sent at all — then it is **not mail**.
It is a flier. An internal document.

1. NO independent third party touched the document
2. NO tracking, no postage, no delivery confirmation
3. The county is the ONLY entity claiming it was sent
4. The county is verifying itself — that is an assertion, not
   verification

**A court record stating a document was sent, when the sending
cannot be independently verified, is functionally perjury by
the state.**

→ **MCL 750.248 — False Public Record**
→ **MCL 750.423 — Perjury**

### Path C Does Not Exist

Either USPS was used or it was not. Both paths terminate in fraud.
The only exit is producing the verification records.

### Wire Fraud (Both Paths)

**18 USC 1343 — Wire Fraud**: MiCOURT operates over interstate
telecommunications infrastructure. Creating a backdated entry IS
the use of interstate wires. Each backdated entry is a separate
count.

### Honest Services Fraud (Both Paths)

**18 USC 1346 — Honest Services**: Judge Schipper is under JTC
review. Authorizing backdated entries while under review deprives
litigants of honest judicial services.

---

## NOTIFICATION SEQUENCE

### Step 1: DEMAND — Barry County Court Administration
**To:** Sarah VanDenburg, County Clerk + Ines Straube, Court Admin
**CC:** Chief Judge William Doherty
**Method:** Certified mail + email to County_Clerk@barrycounty.org

**Demand:** Produce the MiCOURT audit trail for Entry 135:
1. Creation timestamp (date/time of INSERT)
2. Modification history (all UPDATEs with timestamps)
3. User account that created the entry
4. User account(s) that modified the entry
5. IP address / terminal ID of the creating session
6. Public visibility timestamp (when entry appeared on docket)
7. Postage record — USPS receipt, meter stamp, or certificate
8. Address used for mailing
9. MDOC intake record showing receipt
10. SCAO-mandated modification reports for all entries in this
    case for the past 12 months

**Legal basis:**
- MCR 8.119 (register of actions integrity)
- SCAO Records Management Standards §2.4
- SCAO Audit Program Template (modification report requirement)
- Public right to verify official records

### Step 2: USPS OIG Notification
**To:** USPS Office of Inspector General
**Online:** https://www.uspsoig.gov/hotline
**What:** Barry County Circuit Court claims USPS delivered court
documents to an MDOC facility. MDOC FOIA shows no arrival. Either:
- USPS never received the documents (court made false claims
  about using USPS — 18 USC 1341)
- USPS received and lost the documents (USPS accountability)

Request USPS OIG determine whether USPS has any record of
carrying mail from Barry County Circuit Court (220 W. State St.,
Hastings, MI 49058) to the relevant MDOC facility on or around
September 10, 2026.

### Step 3: JTC Supplement — Judge Schipper
**To:** Michigan Judicial Tenure Commission
**What:** Supplement to existing Schipper review:
- New evidence: backdated docket entry appeared after amicus
- MDOC FOIA: no mail arrived
- USPS OIG notification filed (attach)
- Barry County demand letter sent (attach)
- The entry is either authenticated or it is not — verification
  demanded and pending

### Step 4: FBI Detroit / DOJ Public Integrity
**To:** FBI Detroit Field Office + DOJ Public Integrity Section
**What:** Pattern referral:
- Wire fraud — MiCOURT backdating (18 USC 1343)
- Mail fraud — false claims of USPS service (18 USC 1341)
- Honest services fraud — judge under JTC review (18 USC 1346)
- Not a single incident — documented by independent investigative
  journalist across multiple Barry County cases since Dec 2025
- MDOC FOIA proves mail didn't arrive
- Audit trail demand proves the test exists

**Attach:** Complete package — article + demand + USPS OIG +
JTC supplement + Rita's prior Barry County reporting

### Step 5: SCAO Notification
**To:** Michigan Supreme Court State Court Administrative Office
**What:** Barry County's MiCOURT installation may have compromised
audit trail integrity. SCAO has governance authority over all
MiCOURT installations. Request:
- SCAO review of Barry County's compliance with Records
  Management Standards §2.4 (access security)
- SCAO review of Barry County's compliance with Audit Program
  Template (modification reports, separation of duties)
- SCAO-directed extraction of Db2 audit logs for Entry 135
  (if Barry County refuses to produce them)

---

## INVESTIGATION: SOMEONE LEFT A TRACE

### What We Know

1. MiCOURT runs on IBM Db2
2. Db2 has a native audit facility (`db2audit`) that logs
   authentication, object access, modifications, and security
   changes at both instance and database levels
3. SCAO mandates modification reports and separation of duties
4. Barry County has a finite number of people with CMS access
5. Entry 135 was created during a specific 18-hour window
6. The audit log recorded which account did it

### What We Need to Find

1. **The INSERT timestamp** — when was Entry 135 actually created?
   If Sep 11 or 12, the entry was backdated.

2. **The user account** — WHO logged in and created the entry?
   This maps to a named employee on Barry County's access list.

3. **The session metadata** — WHERE did the access come from?
   Was it from the courthouse? From home? From a mobile device?
   After business hours? On a weekend?

4. **The modification history** — was the entry created and then
   modified? Was the date field changed? Was the "sent to
   defendant" notation added after the initial creation?

5. **The postage record** — if USPS was used, there is postage.
   Meter records, certificate of mailing, bulk mail logs. These
   are financial records that the clerk's office must maintain.

6. **The SCAO modification report** — did Barry County's mandated
   modification report capture this entry? If not, why not?
   If so, who reviewed it?

### The Trace They Can't Hide

Even if someone tried to clean the audit trail:

1. **Deleting Db2 audit logs requires admin access** — and that
   deletion generates its own audit event at the instance level

2. **Modifying audit logs changes their file timestamps** — the
   OS metadata (file creation time, modification time) is
   separate from the database and cannot be altered without
   leaving OS-level traces

3. **The Azure SQL replica** — MiCOURT replicates data to Azure
   SQL. The replication timestamp on the Azure side shows when
   the data was replicated. If Entry 135 was replicated on Sep 11
   or 12, the Sep 10 date is contradicted by Microsoft's cloud
   infrastructure logs, which Barry County does not control.

4. **The JDW (Judicial Data Warehouse)** — "receives data from
   CMS applications... uploaded at varying frequencies (weekly or
   daily)." The JDW ingestion timestamp shows when the data
   arrived at the state level. If Entry 135 arrived in the JDW
   on Sep 12 or later, that's an independent state-level record
   that the entry did not exist on Sep 10.

5. **Network logs** — JIS provides network connectivity. The
   state-supplied network is "well-segmented and protected."
   Network authentication logs show when Barry County users
   connected and what they accessed.

6. **Backups** — any enterprise database runs regular backups.
   If the Sep 10 backup does not contain Entry 135, but the
   Sep 11 or Sep 12 backup does, the entry was created after
   Sep 10. Backup integrity is independently verifiable.

### The Five Layers of Evidence

| Layer | System | What It Shows | Who Controls It |
|-------|--------|---------------|-----------------|
| 1 | Db2 audit log | INSERT/UPDATE timestamps, user IDs | Barry County / SCAO |
| 2 | Azure SQL replica | Replication timestamp | Microsoft (subpoena) |
| 3 | JDW ingestion | State-level data arrival time | SCAO (FOIA) |
| 4 | Network auth logs | Connection timestamps, source IPs | SCAO JIS Infrastructure |
| 5 | Database backups | Point-in-time database state | Barry County / SCAO |

**Barry County controls Layer 1 directly.**
**They do not control Layers 2-5.**

Someone sold them the system. Someone has admin credentials.
Someone left a trace. And three of the five layers that recorded
it are outside Barry County's ability to suppress.

---

## FOIA TARGETS

### FOIA 1: Barry County Clerk
**Records requested:**
- MiCOURT user access list (all accounts with create/modify
  permissions for case management entries)
- SCAO-mandated modification reports for the past 12 months
- Mail logs / postage records for all court mailings to MDOC
  facilities in 2026
- Internal policies for creating and dating docket entries

### FOIA 2: SCAO / JIS
**Records requested:**
- JDW ingestion records for the specific Barry County case
  containing Entry 135 (dates of data upload from Barry County)
- Network authentication logs for Barry County MiCOURT access
  during Sep 10-12, 2026
- SCAO audit reports or compliance reviews for Barry County
  court (most recent)
- Any SCAO correspondence with Barry County regarding
  record-keeping compliance

### FOIA 3: MDOC
**Records requested (may already exist via Rita's prior FOIA):**
- Mailroom intake logs for all mail received from Barry County
  Circuit Court in September 2026
- Mail processing policies for legal mail vs. standard mail
- TextBehind digitization logs for the relevant facility

---

## CROSS-PROTECTION (Mode 2: Mutualism)

| Kevin's Action | Effect for Rita |
|---|---|
| USPS OIG notification | Federal record from independent complainant |
| JTC Schipper supplement | Second voice on Schipper's JTC review |
| FBI/DOJ referral | Elevates to federal jurisdiction |
| FOIA to SCAO/JIS | State-level technical records Rita may not have requested |
| Data science expert framework | Technical credibility backing Rita's timeline evidence |

| Rita's Action | Effect for Kevin |
|---|---|
| Clutch Justice publication (Sep 12) | Independent journalist documented the fraud |
| MacDowell article (Sep 13) | Banks intel validated by independent source |
| Prior JTC coverage | Establishes credibility for judicial oversight |
| MDOC FOIA | Proves no mail arrived — the breakthrough evidence |
| Amicus briefs (Foley + Arizola) | Created the conditions that exposed the fraud |

**Neither operator depends on the other.** Both create
independent records. The adversary cannot silence both.

---

## APPLICABILITY TO KEVIN'S OWN CASES

The chain of custody / metadata argument applies EVERYWHERE:

1. **Wayne County 26-108221-DC** (custody) — has Shayla's
   emergency motion been properly served? When was it filed
   vs. when it appeared on the docket?

2. **Ingham County 2026-4349-CZ** (Banks suit) — monitor
   docket entries for backdating or modification after filing.

3. **Any future court interactions** — demand metadata
   verification as a standard practice. If the court can't
   prove its own records are accurate, those records cannot
   be used against you.

**The Barry County case establishes the precedent. Every court
in Michigan uses MiCOURT. If the audit trail can be demanded
in Barry County, it can be demanded everywhere.**

---

## TIMING

| Action | Target Date | Status |
|--------|-------------|--------|
| Case file created | Sep 13 | ✅ DONE |
| Draft demand letter to Barry County | Sep 13-14 | PENDING |
| Draft USPS OIG notification | Sep 14-15 | PENDING |
| Draft JTC Schipper supplement | Sep 15-16 | PENDING |
| Draft FBI/DOJ referral | Sep 16-17 | PENDING |
| Draft SCAO notification | Sep 15-16 | PENDING |
| Prepare FOIA batch (3 targets) | Sep 16-17 | PENDING |
| Coordinate with Rita | Ongoing | PENDING |

**Critical:** Do NOT wait for responses. The fraud is current.
File everything in sequence. Each filing references the prior
one. Silence is evidence.

---

*Case opened September 13, 2026.*
*The record is false until proven otherwise.*
*The burden is on the system, not the citizen.*
