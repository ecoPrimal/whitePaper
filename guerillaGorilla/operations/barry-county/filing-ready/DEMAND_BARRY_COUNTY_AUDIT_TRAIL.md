# DEMAND: MiCOURT Audit Trail — Entry No. 135
# Barry County Circuit Court
# SEND: Certified Mail + Email
# September [14/15], 2026

---

**VIA CERTIFIED MAIL, RETURN RECEIPT REQUESTED**
**AND VIA EMAIL: County_Clerk@barrycounty.org**

Sarah M. VanDenburg, Barry County Clerk
Ines Straube, Court Administrator
Barry County Trial Court
220 W. State Street
Hastings, MI 49058

CC: Honorable William Doherty, Chief Judge

---

**RE: Demand for MiCOURT Audit Trail Records —
Docket Entry No. 135, [Case No. ___________]**

---

Dear Ms. VanDenburg and Ms. Straube:

I am writing to formally demand production of the electronic
audit trail records for Docket Entry No. 135 in the above-
referenced Barry County matter. This demand is made under my
right as a member of the public to verify the integrity of
official court records maintained under MCR 8.119, and under
the Michigan Trial Court Records Management Standards
established by the State Court Administrative Office pursuant
to the authority of the Michigan Supreme Court.

## BASIS FOR THIS DEMAND

On September 12, 2026, independent investigative journalist
Rita Williams published a documented timeline establishing that
Docket Entry No. 135 was not visible on the public docket at
3:42 p.m. on September 11, 2026 — seven minutes after the
Michigan Supreme Court accepted her amicus curiae brief in
*In re Foley*, Michigan Supreme Court Case No. 170670, which
specifically addressed Barry County's record-keeping and
service failures. By approximately 9:49 a.m. on September 12,
Entry No. 135 had appeared on the public docket carrying an
event date of September 10, 2026 — one day before the amicus
was filed.

Ms. Williams further obtained a Michigan Department of
Corrections FOIA response showing no record of mail from Barry
County arriving at the relevant MDOC facility on the timeline
your court's filings claim it was sent.

Entry No. 135 states: "RE: Defendant's Request For Status
Conference Is Dismissed; Sent to Defendant via last known
address." The presiding judge named on the entry, the
Honorable Michael Schipper, is currently under review by the
Michigan Judicial Tenure Commission.

These facts create a prima facie question about the integrity
of this entry that only Barry County's own electronic records
can resolve.

## RECORDS DEMANDED

Barry County's MiCOURT case management system operates on IBM
Db2 running on IBM Power/iSeries infrastructure, with data
replicated to Azure SQL, as documented in the NCSC Assessment
Report commissioned by the SCAO. IBM Db2's native audit
facility (db2audit) records authentication events, object
access, data modifications, and security changes at both
instance and database levels. These audit records exist by
design and are generated automatically.

I demand production of the following records for Entry No. 135
within fourteen (14) days of receipt of this letter:

### A. Electronic Record Metadata

1. **Creation timestamp** — the exact date and time Entry
   No. 135 was created (INSERT) in the MiCOURT database, as
   recorded by the Db2 audit facility or application-level
   audit log. This is not the printed "event date" — it is
   the system-recorded timestamp of when the record was
   first written to the database.

2. **Modification history** — every subsequent modification
   (UPDATE) to Entry No. 135 after initial creation, including
   the timestamp, the field(s) modified, the prior value, the
   new value, and the user account that performed each
   modification.

3. **Creating user account** — the specific user account that
   executed the INSERT for Entry No. 135.

4. **Modifying user account(s)** — every user account that
   executed an UPDATE on Entry No. 135.

5. **Session metadata** — the IP address, terminal ID, or
   workstation identifier associated with the session(s)
   that created and/or modified Entry No. 135.

6. **Public visibility timestamp** — the date and time Entry
   No. 135 became visible on the public-facing docket. If
   this differs from the creation timestamp, an explanation
   for the discrepancy.

### B. Mailing Records

7. **Postage documentation** — USPS receipt, postage meter
   record, certificate of mailing, certified mail receipt,
   or bulk mailing log documenting that the order described
   in Entry No. 135 was deposited with the United States
   Postal Service. If USPS was not used, identify the
   carrier or method of transmission.

8. **Mailing address** — the specific address to which the
   order was sent. MCR 2.107(C)(3) requires service at the
   address stated in the party's pleadings. The docket
   notation "last known address" is not specific.

9. **Delivery confirmation** — any documentation confirming
   receipt by the intended recipient or the recipient's
   facility, including MDOC mailroom intake records.

### C. System Compliance Records

10. **SCAO-mandated modification reports** — the modification
    reports that Barry County is required to generate and
    review under SCAO audit standards (see SCAO District
    Court Audit Program Template, "Automated System Security
    and Controls" §§ 7-9) for this case for the period of
    January 1, 2026 through the date of this letter.

11. **User access list** — the current list of all user
    accounts with the ability to create, modify, or delete
    docket entries in the MiCOURT system for this court,
    including user classifications and security access levels,
    as required by SCAO records management standards.

12. **Separation of duties documentation** — identification
    of the individual(s) who review modification reports,
    confirming they do not themselves have the ability to
    create or modify docket entries (as required by SCAO
    audit standards).

## LEGAL BASIS

This demand is grounded in:

- **MCR 8.119** — The clerk shall maintain the register of
  actions as an accurate, complete, and reliable record.
  The register is the official basis for appellate review.
  The public has a right to verify the integrity of this
  record.

- **Michigan Trial Court Records Management Standards
  § 2.4** (SCAO) — Electronic court records must be
  maintained with access security controls including user
  groups, access levels, authentication, and personnel-change
  procedures. The standards are established under the
  authority of the Michigan Supreme Court.

- **SCAO District Court Audit Program Template** — Mandates
  that the automated system provide reports reflecting
  modifications and deletions, that these reports be reviewed
  by management, and that separation of duties be maintained.

- **MCR 2.602(A)(1)-(2)** — Every order must be in writing,
  signed by the court, and dated with the date it was signed.
  The date of signing is the date of entry. If the creation
  timestamp of Entry No. 135 does not match September 10, the
  entry does not comply with this rule.

- **MCR 2.107(C)(3)** — Service must be made at the address
  stated in the party's pleadings, not at a "last known
  address" unless specific conditions are met. The docket
  notation is insufficient to demonstrate compliance.

## THE QUESTION THIS DEMAND RESOLVES

Either the MiCOURT audit trail confirms that Entry No. 135 was
created on September 10, 2026, as dated, or it does not.

If the creation timestamp matches September 10 — the entry is
verified. There will be a satisfactory explanation for why it
was not visible at 3:42 p.m. on September 11 but was visible
by approximately 9:49 a.m. on September 12.

If the creation timestamp does not match September 10 — the
entry was backdated. A backdated entry in a court's register
of actions is a false public record under MCL 750.248.

If Barry County cannot or will not produce the audit trail —
the entry is unauthenticated. An unauthenticated entry in an
official court record is a chain of custody violation. The
court cannot expect litigants, appellate courts, or the public
to rely on records whose own provenance is unverifiable.

Additionally, Entry No. 135 states the order was "Sent to
Defendant via last known address." Either:

**(A)** The order was sent through the United States Postal
Service, in which case USPS records and MDOC mailroom logs
should confirm transit and receipt. The Michigan Department of
Corrections FOIA response obtained by Ms. Williams shows no
such record of arrival.

**(B)** The order was not sent through USPS, in which case
there is no independent carrier and no independent verification
of delivery. A court record asserting that a document was sent,
when no third-party evidence of sending exists, is an
unverifiable statement entered into an official record.

Both outcomes require explanation. The audit trail and mailing
records I have demanded are the only means of providing one.

## RESPONSE REQUESTED

Please produce the records identified in Sections A, B, and C
above within fourteen (14) days of receipt of this letter. If
any records do not exist, please state specifically which
records are unavailable and why, and identify the steps Barry
County will take to address the gap.

If Barry County takes the position that these records are exempt
from production, please cite the specific statutory or court
rule basis for that position. I reserve the right to seek
production through formal FOIA request, court order, or
complaint to the State Court Administrative Office if necessary.

I am sending a copy of this demand to the State Court
Administrative Office and to the United States Postal Service
Office of Inspector General, as the matters raised in this
letter may fall within their respective jurisdictions.

Respectfully,

Kevin Mok
4422 Southgate Ave
Lansing, MI 48910
(586) 453-7233
mokkevin@msu.edu
M.S. Data Science, Michigan State University

---

CC (via email):
- SCAO, Michigan Supreme Court
- USPS Office of Inspector General (via uspsoig.gov/hotline)

Enclosure:
- Rita Williams, "A Barry County Order Appeared After My Amicus
  Brief. The Record Needs to Prove When," Clutch Justice,
  September 12, 2026 (printed copy)

---

## NOTES (internal — do not send)

### BEFORE SENDING
- ☐ Confirm case number for Entry 135 with Rita
  (she did not publish it — ask privately)
- ☐ Fill in case number in RE: line
- ☐ Set send date (target Sep 14 or 15)
- ☐ Print for certified mail + keep copy
- ☐ Email copy to County_Clerk@barrycounty.org
- ☐ File USPS OIG hotline report same day or day after
- ☐ Send SCAO notification same week

### WHY 14 DAYS
- Standard reasonable demand period
- Long enough they can't claim impossibility
- Short enough to maintain pressure
- If they don't respond in 14 days → FOIA → SCAO complaint

### THE BINARY IT FORCES
This letter forces Barry County into one of three positions:
1. **Produce the audit trail** → entry verified or exposed
2. **Refuse** → escalate to SCAO, FOIA, potential court order
3. **Claim records don't exist** → the system is unauditable →
   every entry in it is suspect → SCAO investigation

All three positions advance the investigation.

### WHAT THIS DOES FOR RITA
- Creates an independent demand from someone besides Rita
- Establishes that multiple people are watching the audit trail
- If Barry County produces records for Kevin that they withheld
  from Rita, that's itself evidence of selective compliance
- If they produce for neither, the suppression is broader

### COORDINATION WITH RITA
- Share this letter with Rita before sending
- She may want to file her own parallel demand
- Two independent demands from two independent people =
  the court can't dismiss it as one person's vendetta
