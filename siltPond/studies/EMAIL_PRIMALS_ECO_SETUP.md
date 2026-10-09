# Email System: *@primals.eco Setup Guide
## October 9, 2026

---

## GOAL

- Send as: `eco.primal@primals.eco`
- Receive at: `*@primals.eco` (catch-all) delivers to one inbox
- Wildcard sender: `anything@primals.eco` for organizational addresses
- Keep ProtonMail encryption and zero-access architecture

## CURRENT STATE

| Check | Status |
|-------|--------|
| Domain: primals.eco | Owned, Cloudflare DNS |
| ProtonMail account | Active (eco.primal@pm.me) |
| MX records | NONE set -- no mail configured |
| SPF record | NONE |
| DKIM records | NONE |
| DMARC record | NONE |
| Existing TXT records | google-site-verification + keyoxide |

## REQUIREMENTS

**ProtonMail paid plan** -- any paid plan supports custom domains:
- Mail Plus ($3.99/mo) -- 1 custom domain, 10 addresses, 15 GB
- Proton Unlimited ($9.99/mo) -- 3 custom domains, 15 addresses, 500 GB
- Proton Business ($6.99/user/mo) -- 3 custom domains, 15 addresses/user

If already on a paid plan (check Settings -> Subscription), skip this.

## STEP-BY-STEP

### Step 1: Add Domain in ProtonMail

1. Log into mail.proton.me
2. Settings -> All settings -> Organization -> Domain names
3. Click "Add domain"
4. Enter: `primals.eco`
5. Proton generates a verification code (e.g., `protonmail-verification=abc123xyz`)

### Step 2: Add Verification TXT Record in Cloudflare

Go to Cloudflare Dashboard -> primals.eco -> DNS -> Records -> Add record:

| Type | Name | Content | TTL |
|------|------|---------|-----|
| TXT | @ | `protonmail-verification=<code from Step 1>` | Auto |

Wait 1-5 minutes, then click "Verify" in ProtonMail.

### Step 3: Create Email Addresses in ProtonMail

BEFORE changing MX records, create these addresses:

| Address | Purpose |
|---------|---------|
| `eco.primal@primals.eco` | Primary send/receive |
| `contact@primals.eco` | Public contact (catch-all target) |
| `hello@primals.eco` | Alternative public |

Optional future addresses (don't count against limit when disabled):
- `signal@primals.eco` -- for signal.primals.eco
- `thesis@primals.eco` -- for thesis.primals.eco
- `tuebor@primals.eco` -- for tuebor.primals.eco

### Step 4: Add MX Records in Cloudflare

Delete any existing MX records, then add:

| Type | Name | Mail Server | Priority | TTL |
|------|------|-------------|----------|-----|
| MX | @ | `mail.protonmail.ch` | 10 | Auto |
| MX | @ | `mailsec.protonmail.ch` | 20 | Auto |

### Step 5: Add SPF Record

| Type | Name | Content | TTL |
|------|------|---------|-----|
| TXT | @ | `v=spf1 include:_spf.protonmail.ch -all` | Auto |

Note: `-all` (hard fail) is recommended. Only ONE SPF record per domain. Do NOT add a second TXT with v=spf1.

### Step 6: Add DKIM Records

Proton provides 3 CNAME records for automatic DKIM key rotation. Get the exact values from ProtonMail Settings -> Domain names -> Edit -> DKIM tab.

| Type | Name | Target | Proxy |
|------|------|--------|-------|
| CNAME | `protonmail._domainkey` | `<value from Proton>` | DNS only (grey cloud) |
| CNAME | `protonmail2._domainkey` | `<value from Proton>` | DNS only (grey cloud) |
| CNAME | `protonmail3._domainkey` | `<value from Proton>` | DNS only (grey cloud) |

**CRITICAL: Grey cloud (DNS only) for DKIM CNAMEs.** Proxied CNAME breaks DKIM verification.

### Step 7: Add DMARC Record

| Type | Name | Content | TTL |
|------|------|---------|-----|
| TXT | `_dmarc` | `v=DMARC1; p=quarantine; rua=mailto:eco.primal@primals.eco` | Auto |

### Step 8: Enable Catch-All

1. Settings -> All settings -> Organization -> Domain names
2. Actions dropdown -> "Set catch-all"
3. Point to: `contact@primals.eco` (or `eco.primal@primals.eco`)

Now `anything@primals.eco` delivers to that inbox.

### Step 9: Verify

Send a test email from a different account to:
- `eco.primal@primals.eco` -- should arrive directly
- `random-test-123@primals.eco` -- should arrive via catch-all
- `tuebor@primals.eco` -- should arrive via catch-all (or direct if created)

Check SPF/DKIM/DMARC with: https://www.mail-tester.com/

---

## WILDCARD SENDING

ProtonMail does NOT support wildcard sending -- you can only send FROM addresses you've explicitly created. But with catch-all on RECEIVE + explicit addresses for SEND, you get:

| Direction | What Works |
|-----------|-----------|
| **Receive** | `*@primals.eco` -- anything arrives via catch-all |
| **Send as** | Only explicitly created addresses (eco.primal@, contact@, hello@, etc.) |

To send as `detroit@primals.eco` or `tuebor@primals.eco`, create those addresses in ProtonMail first. Disabled addresses don't count against your limit.

---

## ESTIMATED TIME

- Cloudflare DNS changes: 5-10 minutes
- ProtonMail domain setup: 10-15 minutes
- DNS propagation: 5-30 minutes (Cloudflare is fast)
- Total: ~30-45 minutes

## WHAT THIS REPLACES

| Before | After |
|--------|-------|
| eco.primal@pm.me | eco.primal@primals.eco |
| No organizational email | contact@primals.eco, hello@primals.eco |
| No catch-all | *@primals.eco catches everything |
| pm.me domain (Proton's) | primals.eco domain (yours) |

eco.primal@pm.me continues to work as an alias. No mail is lost.
