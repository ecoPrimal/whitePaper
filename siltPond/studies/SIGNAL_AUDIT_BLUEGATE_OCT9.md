# SIGNAL AUDIT: blueGate/nucleus
## October 9, 2026

---

## FINDING: SPLIT TUNNEL — ALL BROWSER TRAFFIC EXITS VIA ISP

### What Was Found

| Interface | Routes | DNS | What Goes Through It |
|-----------|--------|-----|---------------------|
| **northgate-wg0** (WireGuard) | `10.13.37.0/24` ONLY | `10.13.37.1` (golgiBody) | Mesh traffic only — SSH to golgiBody, internal comms |
| **Ethernet 2** (physical) | `0.0.0.0/0` DEFAULT ROUTE | Local router + 1.1.1.1 | **ALL internet traffic** — browser, web searches, git push, everything |

### What This Means

```
blueGate/nucleus
    │
    ├── WireGuard tunnel ──→ golgiBody (10.13.37.0/24)
    │     DNS: 10.13.37.1 ✅ private
    │     Only mesh traffic ✅ contained
    │
    └── Ethernet 2 ──→ ISP router ──→ INTERNET
          DNS: local router + Cloudflare 1.1.1.1
          DEFAULT ROUTE — everything else
          ❌ ISP sees: all DNS queries, all HTTP/HTTPS connections
          ❌ Cloudflare sees: DNS queries (1.1.1.1)
          ❌ Browser fingerprint: exposed to every site visited
```

**The WireGuard tunnel is NOT a full tunnel.** It only routes mesh subnet traffic. All browser activity — web searches, site visits, git operations to GitHub, ProtonMail web access — exits through the physical Ethernet interface to the ISP.

### What the ISP Can See

| Signal | Visible to ISP? | Notes |
|--------|-----------------|-------|
| DNS queries | YES | Which domains you resolve (unless DoH/DoT) |
| HTTPS connection IPs | YES | Which IPs you connect to (can't see content) |
| SNI (Server Name Indication) | YES | Which exact hostname in TLS handshake (unless ECH) |
| Connection timing | YES | When you're active, patterns |
| Git push to GitHub | YES | That you connected to github.com |
| ProtonMail web access | YES | That you connected to mail.proton.me |
| Search queries | NO | Content is encrypted (HTTPS) |
| Email content | NO | ProtonMail E2E encryption |

### What Cloudflare (1.1.1.1) Can See

The secondary DNS resolver on Ethernet 2 is `1.1.1.1` (Cloudflare). Cloudflare sees every DNS query that goes through their resolver. Cloudflare's privacy policy says they don't sell data, but they process it.

---

## RISK ASSESSMENT

| Risk | Severity | Context |
|------|----------|---------|
| ISP sees DNS queries for adversary-related domains | MEDIUM | Research on Barrett, Dykema, etc. visible as DNS queries |
| ISP sees connections to primals.eco sites | LOW | You're the operator — expected |
| ISP sees connections to github.com | LOW | Expected developer behavior |
| Cloudflare DNS sees query patterns | LOW | 1.1.1.1 is privacy-focused |
| Browser fingerprint | MEDIUM | Sites can fingerprint via canvas, WebGL, fonts, etc. |
| WebRTC leak | MEDIUM-HIGH | WebRTC can leak real IP even through VPN — need to verify |
| IPv6 leak | LOW | No IPv6 addresses visible on active adapters |

---

## OPTIONS TO REDUCE SIGNAL

### Option 1: Full WireGuard Tunnel (recommended)

Change WG config to route ALL traffic through golgiBody:

```ini
[Interface]
# existing config...

[Peer]
# existing peer config...
AllowedIPs = 0.0.0.0/0    # <-- change from 10.13.37.0/24 to this
```

**Effect:** ALL internet traffic routes through WG tunnel to golgiBody, exits from golgiBody's IP. ISP only sees encrypted WG traffic to one IP.

**Trade-off:** All traffic goes through DO NYC. Latency increases. Bandwidth limited by golgiBody's pipe. If WG drops, internet drops.

### Option 2: DNS-Only Privacy (minimal change)

Keep split tunnel but encrypt DNS:

1. Set Ethernet 2 DNS to `10.13.37.1` (route DNS through WG even in split mode)
2. OR use DoH (DNS over HTTPS) to 1.1.1.1 or a privacy DNS
3. OR run a local DNS resolver that forwards through WG

**Effect:** DNS queries hidden from ISP. Connection IPs still visible but ISP can't correlate with domain names easily.

**Trade-off:** Minimal performance impact. Doesn't hide connection IPs.

### Option 3: Browser Isolation

Use a separate browser profile or container for research:

1. Firefox with `network.dns.disableIPv6 = true`
2. `media.peerconnection.enabled = false` (disables WebRTC)
3. `privacy.resistFingerprinting = true`
4. Route ONLY that browser through WG or Tor

**Effect:** Research browser is isolated from normal browsing. Fingerprint minimized.

**Trade-off:** Two browser contexts to manage.

### Option 4: Tor for Research (maximum privacy)

Use Tor Browser for any research on adversary-related topics.

**Effect:** ISP sees Tor connection (or bridge if needed). Adversary sites see Tor exit node.

**Trade-off:** Slow. Some sites block Tor. Not needed for all activity.

---

## RECOMMENDED APPROACH

**Layered:**

1. **NOW:** Disable WebRTC in primary browser (`media.peerconnection.enabled = false` in Firefox)
2. **NOW:** Change Ethernet 2 DNS from local router to `10.13.37.1` (WG DNS) or enable DoH
3. **SOON:** Option 3 — dedicated research browser profile through WG
4. **WHEN READY:** Option 1 — full WG tunnel (requires testing, may need killswitch)

The fleet sends signal. We find ways to internalize over time. No rush — hardware goes to sporeGate, LAN to eastGate. blueGate is infra and concept.

---

## IMMEDIATE BROWSER HARDENING

If using Firefox, apply these in `about:config`:

| Setting | Value | Effect |
|---------|-------|--------|
| `media.peerconnection.enabled` | `false` | Disables WebRTC — prevents IP leak |
| `privacy.resistFingerprinting` | `true` | Normalizes fingerprint signals |
| `network.dns.disableIPv6` | `true` | Prevents IPv6 DNS leaks |
| `geo.enabled` | `false` | Disables geolocation API |
| `dom.battery.enabled` | `false` | Prevents battery status fingerprinting |
| `network.http.sendRefererHeader` | `0` | Disables referer header |
| `beacon.enabled` | `false` | Disables beacon API (tracking) |

These are browser-level. They don't fix the network-level split tunnel, but they reduce what sites can extract from the browser.

---

## WHAT'S NOT LEAKING

| Check | Status |
|-------|--------|
| TOPOLOGY_MAP.toml | Purged, not in git |
| Physical addresses | Not in committed files |
| MAC addresses | Not in committed files |
| ISP names | Not in committed files |
| Fleet IPs | In siltPond (private) only |
| Kevin Mok identity -> ecoPrimal bridge | Not on published sites |

The committed file hygiene is clean. The network-level signal is the gap.
