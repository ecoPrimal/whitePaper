# Platform Credentials — ecoPrimal Identity Web

**Last Updated**: 2026-07-14 (Wave 138b)
**Security Model**: This file lives in `whitePaper` (private repo). Secrets are NOT stored here — only platform URIs, handles, and fingerprints. Secrets live in your head or in hardware (SoloKey).

---

## Identity Architecture

Two synthetic voices, one mind:

| Voice | Handle | Register | Platforms |
|-------|--------|----------|-----------|
| **ecoPrimal** | ecoPrimal | Technical — code, thesis, architecture | GitHub, ORCID, Forgejo, crates.io, Zenodo, Keyoxide, primals.eco |
| **attsi** | attsi | Philosophical — essays, concepts, outreach | Medium, primals.eco/philosophy, primals.eco/story |

**Locke/Demosthenes model**: Both voices are publicly connected via the sporePrint site (`identity.json`, `llms.txt`). The connection is an easter egg, not a secret. Each voice stands independently on its own evidence.

**What is NOT connected**: The human behind both voices. The Kevin Mok → ecoPrimal chain has been severed in sporePrint content (Wave 138b). See "Scrub Log" below.

---

## Platform Accounts

### ecoPrimal (Technical Voice)

| Platform | Handle / URI | Status | Notes |
|----------|-------------|--------|-------|
| **GitHub** | [github.com/ecoPrimal](https://github.com/ecoPrimal) | Active | Bio: "a tool that shapes itself". ORCID linked. No name/location. |
| **ORCID** | [0009-0004-2141-0321](https://orcid.org/0009-0004-2141-0321) | Active | Name: ecoPrimal. Email: ecoPrimal@pm.me. Keywords + websites populated. |
| **Keyoxide** | `aspe:keyoxide.org:LE2B7C7QUIRLE5OP3TUA5ADXL4` | Active | ASPe profile. Hashed proof available. Secret key stored securely (password in head). |
| **Forgejo** | [git.primals.eco](https://git.primals.eco) | Active | Self-hosted. Mirror of GitHub repos. |
| **crates.io** | ecoPrimal | Token generated | Token name: `ecoPrimal-publish`. Scopes: publish-new, publish-update. 90-day expiry (Oct 12, 2026). `cargo login` done on eastGate. |
| **Zenodo** | ecoPrimal (via GitHub OAuth) | Authorized | All 4 orgs granted. Enable repos in Settings → GitHub to mint DOIs on release. |
| **Email** | eco.primal@pm.me | Active | ProtonMail. Used for ORCID, GitHub, contact page. |

### attsi (Philosophical Voice)

| Platform | Handle / URI | Status | Notes |
|----------|-------------|--------|-------|
| **Medium** | (not yet created) | Planned | Handle: `attsi`. Bio: "a tool that shapes itself — philosopher synthetic intelligence" |
| **primals.eco** | /philosophy/, /story/ | Active | 12 atlasHugged essays + 3 story essays. CC-BY-SA 4.0. |

### GitHub Organizations

| Org | URL | Role | ecoPrimal visible? |
|-----|-----|------|--------------------|
| ecoPrimals | github.com/ecoPrimals | Infrastructure (17 primals + tooling) | Sole member |
| syntheticChemistry | github.com/syntheticChemistry | Science (8 springs) | Sole member |
| sporeGarden | github.com/sporeGarden | Products | Sole member |
| protoKarya | github.com/protoKarya | External | Sole member |

**DataScienceBioLab removed** from ecoPrimals and syntheticChemistry (2026-07-14).

---

## Keyoxide Identity Claims

Add these via Manual Input on the Keyoxide profile:

| Claim | Verification Method |
|-------|-------------------|
| `https://primals.eco/.well-known/aspe` | File served at that path (deployed via sporePrint) |
| `https://github.com/ecoPrimal` | Create gist `keyoxide.md` with fingerprint |
| `dns:primals.eco` | TXT record: `aspe:keyoxide.org:LE2B7C7QUIRLE5OP3TUA5ADXL4` |

**Keyoxide fingerprint**: `LE2B7C7QUIRLE5OP3TUA5ADXL4`
**Keyoxide URI**: `aspe:keyoxide.org:LE2B7C7QUIRLE5OP3TUA5ADXL4`
**Keyoxide URL**: `https://keyoxide.org/aspe:keyoxide.org:LE2B7C7QUIRLE5OP3TUA5ADXL4`

---

## Scrub Log (2026-07-14)

Changes made to sporePrint content to sever Kevin Mok → ecoPrimal identification chain:

### Removed from sporePrint
- "Submitted to Michigan State University" + degree program names (CMSE, MMG)
- "BS Microbiology, MS Data Science (Michigan State University)"
- All "MSU Genomics Core, RTSF" references implying personal access
- Specific coursework names (Medical Microbiology, Virology, Molecular Pathogenesis)
- Personal anecdotes (partner, rottweilers at retirement home)
- "physically housed at Michigan State University" (LTEE)
- "MSU's LTEE frozen library"
- "the author" → "the builder" in thesis voice

### Kept in sporePrint
- Researcher MSU affiliations (Murillo, Waters, Dong, etc.) — public facts about their work
- "bench microbiology background" / "data science" as generic skill descriptors
- ecoPrimal as the developer identity
- MSU_ASSET_ACCELERATION.md (institutional outreach doc — flags MSU by design)

### Removed from GitHub
- DataScienceBioLab from ecoPrimals org membership
- DataScienceBioLab from syntheticChemistry org membership

---

## Single Source of Truth

The canonical identity template lives in `sporePrint/config.toml` under `[extra.identity]`. All sporePrint templates, JSON-LD, llms.txt, and identity.json read from it. Update config.toml → rebuild → everything propagates.

Machine-readable: `https://primals.eco/identity.json`

---

## Token Rotation Schedule

| Token | Location | Expires | Rotate Via |
|-------|----------|---------|-----------|
| crates.io | eastGate (`~/.cargo/credentials.toml`) | Oct 12, 2026 | crates.io → Settings → API Tokens → Generate |
| Keyoxide | In your head | Never | Password-based. Secret key stored securely. |
| GitHub (gh CLI) | eastGate | Indefinite (PAT) | `gh auth refresh` |
| Zenodo | OAuth via GitHub | Follows GitHub session | Re-authorize at zenodo.org |

**golgi deployment**: crates.io token needs to be provisioned on golgi when CI publishing is set up. Use `CARGO_REGISTRY_TOKEN` env var in systemd service.
