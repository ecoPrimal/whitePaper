# northGate Onboarding — Hobby System + Future Mesh Node

**Gate**: northGate
**Host**: tamison / mokke
**OS**: Windows (consumer-grade)
**GPU**: RTX 5090
**Role**: Personal gaming system. Stays personal.
**Network**: CRS310 backbone (hub 1), alongside eastGate and sporeGate
**Priority**: P3

---

## Current Scope

### 1. Sovereign RustDesk Relay (DONE — Jun 16)

Config applied to `%APPDATA%\RustDesk\config\RustDesk2.toml`:

```toml
rendezvous_server = '157.230.3.183:21116'

[options]
relay-server = '157.230.3.183'
custom-rendezvous-server = '157.230.3.183'
key = 'utlNOAWUDdV+Q+ifG3zHrQ5HU0FtQnOTHiAnu6prV7Q='
```

**Status**: Config pushed. Relay reachable (port 21116 open, ~90ms to golgi).
Connection to remote gates depends on those gates also being online and registered
to the sovereign relay. northGate is on `192.168.1.x`; other gates are on
`192.168.4.x` — all cross-subnet traffic routes through golgi WAN relay.

### 2. Enable Windows OpenSSH Server (when convenient)

Settings → Optional Features → Add Feature → OpenSSH Server

Or from PowerShell (admin):
```powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic
```

### 3. Stay on Backbone

northGate sits on CRS310 hub 1 with eastGate and sporeGate. No special
network config needed — standard DHCP consumer deployment.

---

## Future Scope (P3 — after NUCLEUS covalent is proven on Linux gates)

- Join the sovereign mesh as an idle-compute node
- RTX 5090 available for toadStool/barraCuda GPU workloads
- Same pattern as any Steam gaming computer: mesh node when idle, gaming when active
- Requires NUCLEUS Windows port (not yet built)

Linux gates (sporeGate, eastGate) prove the patterns first. northGate benefits
from proven deployments rather than being an experiment ground.

---

## Network Info

| Gate | IP | Subnet | Role |
|------|----|--------|------|
| sporeGate | 192.168.4.1 | .4.x | Router/gateway |
| eastGate | 192.168.4.244 | .4.x | Overwatch tower |
| fieldGate | 192.168.4.36 | .4.x | NUC canary |
| northGate | 192.168.1.115 | .1.x | Gaming/hobby (this machine) |
| golgi VPS | 157.230.3.183 | WAN | RustDesk relay + Forgejo |

---

## What northGate Is Not

- Not an experiment ground for unproven NUCLEUS patterns
- Not a Linux gate — all NUCLEUS primals target Linux first
- Not expected to run `membrane` or `gate.bootstrap` until Windows port exists
- Not on the same subnet as the other gates (WAN relay for remote access)
