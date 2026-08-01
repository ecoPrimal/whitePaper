# Sovereign Identity Garden — Biometric-Anchored Identity for People Who Have Nothing

**Status**: CONCEPT | **Wave**: 155n | **Date**: Aug 1, 2026
**Garden**: Proposed — application layer on primal infrastructure
**Motivation**: We make tools for humanity because we can, and because the need is real.

---

## The Problem

An unhoused person in America interacts with an average of 7-12 agencies per
year: shelters, clinics, courts, social services, food banks, VA offices,
substance abuse programs, mental health providers. At each one, they fill out
the same intake paperwork. Name. Date of birth. Social Security number. Medical
history. Substance use. Mental health status. Criminal record. Emergency
contacts. Housing history.

Every time, from memory, to a stranger, into a system they don't control.

Then their camp gets swept. Their bag with their SSN card, their birth
certificate, their medication list — gone. Or they're arrested and their
belongings are discarded. Or they're hospitalized and discharged with nothing.

Now they start over. Stand in line at the Social Security office to replace
the card. Request a birth certificate from a county office in another state,
mailed to what address? Prove you're you so you can get a new card that proves
you're you. Circular. Punishing. Designed for people with addresses, filing
cabinets, and time.

Every agency that collected their data now has it in a database. HMIS (Homeless
Management Information System) aggregates it federally. Thousands of case
workers across the country access it. Names, SSNs, domestic violence history,
substance use, mental health diagnoses — the most sensitive data about the most
vulnerable people, in one place.

It is a honeypot. And the people in it are the least equipped to survive a
breach.

---

## The Insight

Every existing identity system is anchored to something losable:

| Anchor | Failure Mode |
|---|---|
| SSN card | Paper. Destroyed in camp sweep. |
| Driver's license | Costs money. Expires. Confiscated during arrest. |
| Birth certificate | Single copy. Locked in a county office across the country. |
| Phone | Stolen. Dead battery. Confiscated by police. |
| Address | The thing they don't have. |
| Medical records | Locked in a hospital portal they can't log into. |
| Agency database | They can't see it, can't control it, can't delete it. |

**The person's body is the only thing they always have.**

A fingerprint survives a camp sweep. A face survives an arrest. An iris pattern
survives a winter. These are not losable. They are not confiscatable. They are
not forgettable.

**The person IS the credential.**

---

## The Architecture

This garden uses existing primal capabilities. No new primals are required —
only an application layer that orchestrates them into a sovereign identity
workflow.

### Identity Creation (First Contact)

```
1. Person arrives at a participating agency
2. Device (tablet, phone) runs bearDog with biometric sensor
3. Person provides biometric (fingerprint, face, iris)
4. bearDog generates a key pair in hardware security:
   - iOS: Secure Enclave (Face ID / Touch ID)
   - Android: StrongBox HSM (Titan M2 on Pixel)
   - Desktop: SoloKey FIDO2 (fallback)
5. Private key NEVER leaves the hardware module
6. Public key becomes the person's identity anchor
7. No account. No username. No password. No SSN required.
```

### Data Capture (Intake)

```
1. Social worker captures intake data on device
2. Data is immediately encrypted with person's public key (rhizoCrypt)
3. Social worker's device retains ONLY:
   - Encrypted blob (unreadable without biometric)
   - Attestation hashes (verifiable without decryption)
   - Provenance record (who captured, when, where, under what authority)
4. Social worker NEVER has persistent access to cleartext
5. Encrypted data syncs to participating nest (when connectivity available)
6. loamSpine records full data lineage
```

### Attestation (Zero-Knowledge Verification)

The critical innovation: agencies don't need raw data. They need answers.

| What the agency asks | What they receive | What they DON'T see |
|---|---|---|
| "Is this the same person from January?" | Yes (biometric match) | Nothing else |
| "Do they have a valid SSN?" | Yes (sweetGrass attestation) | The SSN itself |
| "Do they have documented medical needs?" | Yes + category (sweetGrass) | Diagnoses, medications, history |
| "Were they at Shelter X last month?" | Yes + dates (sweetGrass) | Why they were there |
| "Are they a veteran?" | Yes (sweetGrass, VA-signed attestation) | Service record, discharge status |
| "Do they have a substance use history?" | Only if person consents to disclose | Everything, by default |

Each attestation is a signed, verifiable statement WITHOUT the underlying data.
The shelter knows "this person has documented medical needs" without knowing
what those needs are. The clinic knows "this person was at the shelter last
week" without knowing which shelter or why.

### Selective Disclosure (Person-Controlled)

```
1. Person arrives at new agency
2. Authenticates with biometrics (bearDog)
3. Device shows their attestation summary:
   "You have 12 verified attestations across 4 agencies"
4. New agency requests specific information
5. Person sees EXACTLY what's being requested:
   "City Clinic wants to see: Medical needs, Allergies, Current medications"
6. Person APPROVES or DENIES each item
7. Approved items are decrypted WITH THEIR BIOMETRIC and shared
8. Denied items remain sealed
9. Disclosure event is recorded in loamSpine (who saw what, when, why)
```

The person controls their own data with their own body. No one accesses
anything without them physically present and consenting.

### Cross-Agency Verification (No Central Database)

```
Agency A (shelter):
  - Captures intake, encrypts to person's key
  - Generates attestations: "has_id", "has_medical_needs", "was_here_jan_15"

Agency B (clinic):
  - Person authenticates with biometrics
  - Sees attestations from Agency A (verified, not raw data)
  - Person consents to share medical info
  - Clinic captures additional medical data, encrypts to same key
  - Generates new attestations: "under_treatment", "medication_prescribed"

Agency C (court):
  - Person authenticates
  - Court sees attestation: "in_shelter_program" (from A), "under_treatment" (from B)
  - Court does NOT see medical details, shelter intake, SSN
  - Sufficient for compliance verification
```

No central database. No HMIS feed. Each agency holds only encrypted blobs
and attestation hashes. A breach at any single agency exposes nothing useful —
encrypted data without keys.

---

## Primal Mapping

| Primal | Role in Sovereign Identity |
|---|---|
| **bearDog** | Biometric key generation (FIDO2), authentication, hardware-backed key storage. The root of trust. `beardog.fido2.register`, `beardog.fido2.authenticate`. |
| **rhizoCrypt** | Encryption of captured data to person's public key. Selective decryption on consent. |
| **sweetGrass** | Attestation generation and verification. Zero-knowledge proofs. Cross-agency attestation chains. |
| **loamSpine** | Data lineage. Who captured what, when, on which device, under what authority. Audit trail for disclosure events. |
| **songBird** | Service discovery and IPC. Local-first — primals on the phone communicate without internet. Works in shelters with no WiFi. |
| **biomeOS** | Orchestration. Manages the intake workflow, coordinates primals, handles lifecycle. |
| **skunkBat** | Threat detection. Monitors for anomalous access patterns, potential data exfiltration, unauthorized disclosure attempts. |
| **BTSP** | Trust establishment between devices. Social worker's phone ↔ shelter terminal. Bond-type enforcement: intake worker gets different trust level than case manager. |

### Bond Types (Trust Spectrum)

The bonding model (G8 Plasmodium) maps directly to social services trust levels:

| Bond Type | Who | Access Level | Duration |
|---|---|---|---|
| **Ionic** (weak, temporary) | Intake worker at walk-in shelter | Identity verification only. "Is this person?" | Session. Dissolves when person leaves. |
| **Covalent** (strong, persistent) | Assigned case manager | Full attestation access. Selective disclosure by consent. | Ongoing. Maintained across visits. |
| **Metallic** (institutional) | Agency ↔ Agency | Attestation verification only. Never raw data. | Persistent between participating agencies. |
| **Hydrogen** (minimal, bridging) | Court, law enforcement | Compliance attestations only. "In program? Under treatment?" | Request-response. No persistent access. |

---

## First Deployment: Gate-Connected Hardware (Phase 0), then grapheneGate

Before mobile deployment, existing gates provide cameras, sensors, and
hardware entropy for early identity prototyping. Phone deploy is late-stage.

### Phase 0 — Gate-First (existing hardware)

```
USB cameras on eastGate/ironGate/westGate for facial capture + liveness.
Hardware RNG from existing gate silicon for key generation entropy.
bearDog FIDO2 with SoloKey USB (already working) for key ceremonies.
rhizoCrypt encrypts captures. sweetGrass generates attestations.
No phone required. Gates already run full NUCLEUS.

Validates:
  - Camera capture → bearDog key gen → rhizoCrypt encrypt → sweetGrass attest
  - Full flow on commodity gate hardware
  - Liveness detection on standard USB cameras
  - Provenance chain via loamSpine
```

### Phase 1 — grapheneGate (Pixel 8a) — Mobile Anchor

| Component | Capability |
|---|---|
| **SoC** | Google Tensor G3 |
| **HSM** | Titan M2 (StrongBox) — hardware-backed key generation, tamper-resistant |
| **Camera** | 64 MP main + 13 MP ultrawide — liveness detection, document scanning, facial capture |
| **Fingerprint** | Under-display optical sensor |
| **OS** | GrapheneOS — hardened Android, no Google services, full user control |
| **Primals** | Tower 3/3 already running (bearDog, songBird, skunkBat) |
| **IPC** | TCP (13/13 primals), `BindMode::Auto` abstract sockets |
| **Status** | Live in ecosystem manifest as `grapheneGate` |

### Why grapheneGate First

1. **Already running primals.** Tower is live. bearDog IPC works. No deployment
   gap — this is the first device that can demonstrate the full flow.

2. **Titan M2 is a real HSM.** Not a software keystore — a physically separate
   chip that performs cryptographic operations in hardware. Keys generated
   inside Titan M2 cannot be extracted, even by the OS. This is the same
   security model as a bank's HSM, in a $350 phone.

3. **Camera + biometrics on one device.** Fingerprint sensor for authentication,
   camera for liveness detection and facial capture, all feeding into bearDog.
   The social worker holds one device and gets everything.

4. **GrapheneOS = no data leakage.** No Google services phoning home. No Play
   Store analytics. No carrier bloatware. The phone runs exactly what we tell
   it to and nothing else. This matters when handling DV survivor data.

5. **Personal anchor.** Before multi-agency deployment, grapheneGate can serve
   as a personal anchor device — a prototype where one operator (you) can test
   the full identity creation → data capture → attestation → verification
   flow end-to-end.

### Deployment Path

```
PHASE 0 — Gate-connected capture (now):
  USB cameras + SoloKey FIDO2 on existing NUCLEUS gates.
  Validates full flow without phone hardware.
  Gate silicon provides hardware entropy.

PHASE 1 — grapheneGate mobile anchor:
  grapheneGate as a single-device mobile prototype.
  bearDog generates key pair via Titan M2.
  Camera captures test biometric + document scans.
  rhizoCrypt encrypts to person's key.
  sweetGrass generates attestations.
  All local, all IPC, no network required.

PHASE 2 — Two-device proof (Mac Mini M4 acquired):
  grapheneGate (field device) ↔ appleGate (back office)
  BTSP establishes trust between devices.
  Attestations sync over LAN/WAN.
  Proves cross-platform: Android field capture, macOS verification.

PHASE 3 — Multi-agency simulation:
  Multiple devices (grapheneGate + appleGate + existing gates)
  simulate shelter → clinic → court flow.
  Each device is a different "agency."
  Person authenticates at each, attestations flow, raw data stays sealed.
```

---

## Encryption Genetics — Identity as Living Cryptographic DNA

This is where the architecture goes deeper than encryption. Each interaction
doesn't just encrypt data — it EVOLVES the identity's genetic signature.

### The Concept

In ecoPrimals, every gate has a genetic lineage tracked by mitoBeacon. The
lineage records the gate's history: what hardware it runs on, what operator
enrolled it, what primals it hosts, what interactions it's had. The genetics
are cumulative — each event mutates the signature, making the gate's identity
progressively richer and harder to impersonate.

Apply this to a person's sovereign identity:

```
INITIAL SEED (first contact):
  biometric_hash = bearDog.fido2.register(fingerprint)
  device_genetics = mitoBeacon.genetics(grapheneGate)
  operator_genetics = mitoBeacon.genetics(social_worker_bond)
  timestamp = now()
  
  identity_seed = hash(
    biometric_hash,
    device_genetics,
    operator_genetics,
    timestamp
  )

FIRST MUTATION (intake data captured):
  intake_data = encrypt(form_data, person_public_key)
  photo = encrypt(camera_capture, person_public_key)
  liveness = liveness_proof(camera_frames)
  
  identity_gen1 = hash(
    identity_seed,
    hash(intake_data),
    hash(photo),
    liveness_proof,
    device_genetics,        // WHICH device captured this
    operator_genetics,      // WHO captured it
    timestamp               // WHEN
  )

SECOND MUTATION (clinic visit, different device, different operator):
  identity_gen2 = hash(
    identity_gen1,          // carries ALL prior history
    hash(medical_data),
    hash(new_photo),
    new_liveness_proof,
    clinic_device_genetics, // different device = different genetics
    clinic_operator_bond,   // different operator = different bond type
    timestamp
  )

...and so on. Each interaction is a generation.
```

### What This Achieves

**The identity becomes unforgeable through accumulation.** A forger would need
to reproduce not just a biometric match, but the entire chain of interactions:
every device's hardware genetics, every operator's bond signature, every
timestamp, every liveness proof. Each generation adds entropy. By the tenth
interaction, the genetic signature contains cryptographic material from ten
different devices, ten different operators, ten different timestamps, and ten
different liveness proofs.

**The identity strengthens with use.** A freshly created identity (gen 0) has
one biometric hash and one device signature. An identity with 50 interactions
across 12 agencies over 2 years has 50 generations of accumulated genetics.
The longer a person uses the system, the more cryptographically robust their
identity becomes. Usage IS security.

**Each data entry enriches the genetics.** When a social worker captures a name,
the hash of that encrypted name becomes part of the genetic chain. When the
camera captures a photo, the photo's hash is woven in. When a liveness proof
is generated (proving a real person was present, not a printed photo), that
proof becomes genetic material. Nothing is wasted — every interaction makes
the identity stronger.

**Device genetics provide provenance.** Each capture event includes the
mitoBeacon genetics of the device that performed it. This means the identity's
genetic chain records not just WHAT was captured, but on WHAT silicon. If a
device is later compromised, you can identify exactly which genetic mutations
came from that device and flag them — without invalidating the entire identity.

### Defense in Depth Through Genetics

```
LAYER 1 — Biometric Root
  Person's fingerprint/face → hardware key pair (Titan M2 / Secure Enclave)
  Cannot be extracted. Cannot be forged without the person's body.

LAYER 2 — Encryption Envelope
  All data encrypted to person's public key (rhizoCrypt)
  Encrypted at rest, in transit, everywhere. No cleartext persists.

LAYER 3 — Genetic Chain
  Every interaction hashes into the identity genetics.
  Cumulative, irreversible. History cannot be rewritten.
  A forger must reproduce the entire chain, not just one link.

LAYER 4 — Device Entanglement
  Each genetic mutation includes the capturing device's mitoBeacon signature.
  The identity is entangled with the hardware that touched it.
  Provenance is embedded in the cryptographic structure, not logged in a database.

LAYER 5 — Operator Bond Signatures
  Each mutation includes the operator's bond type and signature.
  An intake worker's ionic bond produces different genetic material than
  a case manager's covalent bond. Bond type is part of the genetics.

LAYER 6 — Liveness Proofs
  Camera captures prove a real person was present at each interaction.
  Liveness data (blink detection, depth mapping, micro-expression) is
  hashed into the genetics. Replay attacks fail because each liveness
  proof is temporally unique.

LAYER 7 — Temporal Entropy
  Timestamps are part of every genetic mutation.
  The identity exists in time. You can't manufacture a 2-year interaction
  history retroactively — each timestamp is bound to the genetic state
  that preceded it.
```

Seven layers. Each strengthens the others. Compromising one layer does not
compromise the identity — the remaining six layers hold. This is what
defense in depth means when your genetics carry the full history.

### Live Images and Biometrics in the Genetic Chain

The camera on grapheneGate captures more than a photo. Each capture event
produces:

| Capture | What Gets Mixed Into Genetics | Why |
|---|---|---|
| **Facial photo** | Hash of encrypted image | Visual identity, cross-references with future captures |
| **Liveness proof** | Blink sequence, depth map hash | Proves real person, not printed photo or screen |
| **Ambient context** | Light level, orientation, approximate location hash | Unique environmental fingerprint per interaction |
| **Document scan** | Hash of encrypted document image | If they have an ID today, capture it before it's lost |
| **Fingerprint template** | Biometric template hash (from Titan M2) | Hardware-verified, tamper-resistant |
| **Voice sample** (future) | Voiceprint hash | Additional biometric factor, captures naturally during intake |

Each of these is encrypted (the raw data is sealed), but the HASH of each
becomes genetic material. The genetics carry proof that real captures happened
on real devices with real people, without containing the sensitive data itself.

---

## Why This Requires ecoPrimals (Not Just "an App")

A conventional app could encrypt data. What it can't do:

1. **Hardware-rooted biometric keys** — bearDog uses FIDO2 / Secure Enclave /
   StrongBox. The private key literally cannot be extracted from the chip. This
   isn't software encryption that can be reverse-engineered. It's silicon.

2. **Zero-knowledge attestations** — sweetGrass generates verifiable statements
   about encrypted data without exposing it. An app can encrypt; it can't prove
   properties of encrypted data to third parties.

3. **Provenance that survives device loss** — loamSpine tracks data lineage
   across devices and agencies. When a phone is lost, the provenance chain is
   intact on the mesh. The identity reconstructs on any new device with a
   biometric sensor.

4. **Local-first operation** — songBird IPC means the phone works without
   internet. Critical in shelters, camps, rural areas, places where connectivity
   is not guaranteed. Data syncs when available; operates independently always.

5. **Trust enforcement at the protocol level** — BTSP doesn't trust the
   application to enforce access control. Trust is established at the handshake
   layer, before any data flows. A compromised app can't escalate its own bond
   type.

6. **Threat detection** — skunkBat monitors for a case worker running bulk
   queries, for access patterns that don't match intake workflows, for devices
   that appear in locations they shouldn't be. The system watches its own
   watchers.

---

## What Needs to Evolve

### Phase 1 — grapheneGate (Android, Now)

| Component | Current State | What's Needed |
|---|---|---|
| **bearDog biometrics** | FIDO2 ceremony, SoloKey USB | Android StrongBox (Titan M2) integration, fingerprint template hashing, camera-based liveness |
| **bearDog key derivation** | Ed25519 from FIDO2 | Biometric → deterministic key pair via StrongBox. Key must be reproducible from same biometric on any device with same HSM protocol. |
| **mitoBeacon genetics** | Gate-level genetics exist | Extend to identity genetics: each interaction mutates a person's genetic chain with device + operator + data hashes |
| **Camera pipeline** | Not integrated with primals | bearDog captures (photo, liveness, document scan) → rhizoCrypt encrypt → hash into genetics chain |
| **sweetGrass attestations** | Provenance attestation chains | Zero-knowledge proof generation for selective property verification |
| **Intake UX** | No application layer exists | Garden: Android app (Kotlin) calling primals via songBird IPC |

### Phase 2 — iOS (Mac Mini M4 Acquired)

| Component | Current State | What's Needed |
|---|---|---|
| **iOS primals** | Not built | Swift/Rust FFI. bearDog → Secure Enclave, songBird → Darwin IPC, full Tower on iOS. |
| **Face ID / Touch ID** | Not integrated | bearDog uses iOS biometric APIs → Secure Enclave key generation |
| **Cross-platform identity** | Single-device only | Same biometric + same identity genetics must verify across Android and iOS devices |

### Phase 3 — Multi-Agency

| Component | Current State | What's Needed |
|---|---|---|
| **Offline sync** | songBird local IPC works | Conflict resolution for attestations captured offline at multiple agencies |
| **Agency onboarding** | Single-operator ecosystem | Multi-operator enrollment: agencies run their own gates with shared attestation verification |
| **Genetic chain verification** | Not implemented | Any agency device can verify a person's genetic chain without access to the raw data in it |

---

## The Silicon Deism Connection

This garden is WHY silicon deism matters. If the identity system only runs on
one vendor's hardware, or one cloud provider, or one operating system — then
it's not sovereign. It's just a different landlord.

An unhoused person might authenticate at:
- A shelter's Android tablet ($200)
- A clinic's iPad ($400)
- A social worker's iPhone ($800)
- A library's Linux desktop ($0)
- A VA office's Windows terminal ($500)

The primals must run on ALL of them. Same identity, same attestations, same
zero-knowledge proofs, regardless of the silicon underneath. That's not an
abstract architectural goal — it's the difference between a system that works
for everyone and a system that works for people who can afford the right phone.

---

## Who This Is For

This garden serves people who:
- Have lost every physical document they own, possibly multiple times
- Cannot maintain a phone, an email address, or a mailing address
- Interact with 7-12 agencies per year, repeating the same intake each time
- Have sensitive data (DV history, mental health, substance use) that is
  currently stored in centralized databases they cannot monitor or control
- Are the least equipped to survive an identity theft or data breach
- Deserve the same cryptographic protection as a Fortune 500 CEO's data

We make tools for humanity because we can, and because the need is real.

---

*subGen Wave 155n — Sovereign Identity Garden. Biometric-anchored identity for
unhoused populations. Encryption genetics: each interaction mutates the identity's
cryptographic DNA — device genetics, operator bonds, liveness proofs, data hashes
accumulate into an unforgeable chain. Seven-layer defense in depth. First deploy
on grapheneGate (Pixel 8a, Titan M2, camera, fingerprint). Phase 2 on iOS via
Mac Mini M4. Person IS the credential. No central database. No honeypot. Identity
strengthens with use. We make tools for humanity because we can, and because the
need is real.*
