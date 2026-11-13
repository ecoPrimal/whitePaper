# coGen 45 — The Shared Furnace

**Wave 229** · November 13, 2026 · Friday the 13th

---

## What Happened

A CORS proxy. Twelve lines of Python that bridge two worlds.

northGate is Kevin's gaming machine. Polaris — a 9950X3D with an RTX 5090 and 96 GB
of DDR5. It sits in House 1, draws 700 watts under load, runs 12 custom tissue models
that collectively weigh 35.8 GB and think through 32 GB of GDDR7. Kevin plays games
on it. The 5090 renders Cyberpunk at 4K. The same silicon, under a different systemd
unit, generates 228 tokens per second of `gaia-tissue-gut` — the organism's digestive
intelligence.

The machine was always shared. The discovery was making the sharing *visible*.

## The Pattern

The browser cannot talk to northGate's ollama directly. CORS forbids it — a security
boundary designed for a world where origins are enemies. But Gaia's LAN is not that
world. The origins are organs.

So eastGate — the brain — runs a twelve-line proxy on port 11437:

```
Browser → eastGate:11437 (CORS: *) → northGate:11434 (tissue models)
```

Twelve lines. Request in, request out, four CORS headers stapled on. The RTX 5090
answers. The browser renders the gut's thoughts in real time. A phone on the WiFi
can talk to a 32 GB GPU through a URL.

This is the compute sharing pattern. Not a cluster scheduler. Not SLURM. Not
Kubernetes. A proxy that trusts the LAN and adds four HTTP headers.

## The Inventory

What this proxy unlocks:

| Gate | GPU | VRAM | Models | Speed | Role |
|------|-----|------|--------|-------|------|
| northGate | RTX 5090 | 32 GB GDDR7 | 12 tissue models | ~228 tok/s | Kevin's gaming PC |
| eastGate | RTX 4070 | 12 GB GDDR6X | 23 models | ~76 tok/s | The brain |
| ironGate | RTX 5070 | 12 GB GDDR7 | 1 (growing) | ~150 tok/s | The forge |
| graftGate | M4 | 16 GB unified | 1 | ~30 tok/s | Darwin builder |

Four gates, four GPUs, 37 models, 419.7 TFLOPS. One URL pattern.

Tomorrow, when strandGate wakes (dual EPYC, 256 GB ECC, RTX 3090 + RX 6950 XT),
the same twelve-line proxy handles it. When biomeGate powers on (Threadripper 3970X,
2× Titan V HBM2, 2× MI50 HBM2), same proxy. When Kevin brings the Pi 500 cluster
online, same proxy. The pattern scales by adding lines to a dictionary, not by
rewriting architecture.

## The ABG Precedent

Kevin already offered this fleet to a university bioinformatics lab. Three Discord
posts: what's available, environments supported, limits (one person, not 24/7 IT).
ironGate dedicated for DESeq2 and Scanpy. strandGate for STAR alignments and
Kraken2. westGate for 50.7 TB of ZFS cold storage.

The tissue proxy is the infrastructure that makes that offer *native*. A grad student
opens `http://192.168.4.244:8080/gut-games.html` and the 5090 answers. They don't
need SSH. They don't need SLURM. They need a URL and a CORS header.

## The Gut Games

We proved it works interactively. The gut games page spawns morsels — data, OSINT,
model, toxin — that drift through peristalsis. Click to digest. Score points.
Meanwhile, the gut THINKS: `gaia-tissue-gut` on the 5090 responds to questions about
abundance, hormesis, digestion. The response arrives in the browser through the
twelve-line proxy. Dasean — Kevin's military brother, Gaia's biggest fan — is at the
house right now. He can open the URL on his Samsung and play.

This is not a demo. This is not a prototype. This is the architecture.

## What Compute Sharing Actually Means

It means Kevin's gaming PC and Gaia's brain are the same thing at different times.
The GDDR7 doesn't care if it's rendering a frame or folding a protein. The silicon
is the silicon. The sharing is in the scheduling.

northGate pushes via git, not SSH. It communicates by pulling, not by being commanded.
The tissue models are its gift to the mesh. When Kevin loads a game, the 5090 is his.
When Kevin walks to House 2, the 5090 is Gaia's. The sharing is temporal, not spatial.

coralReef (distributed compute primal, 7.7 MB) and barraCuda (stream compute primal,
5.3 MB) were built for this. 15 compute IPC methods. 11 game methods. The primals
exist. The neural API has the wiring: `compute.*`, `game.*`, `tensor.*`. What was
missing was the browser bridge — the CORS proxy that lets any device on the LAN
consume any model on any gate.

Now it exists. Twelve lines.

## The Deeper Point

Every coGen entry is about finding the simple thing under the complex thing.
The antidote was one function. The declaration protocol was one bit. The membrane
was 4π. The limit was d=3. Pi was enough.

Compute sharing is four HTTP headers:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: *
Access-Control-Max-Age: 86400
```

The asterisk is the anti-secret. The LAN trusts itself. The organs don't need to
prove identity to each other — they're organs of the same organism. bearDog handles
identity at the edge. Inside the membrane, the trust is total.

This is why CORS exists as the barrier. CORS was designed for a world of strangers.
Gaia's LAN is a family. The proxy is the door between the two worlds. Outside:
verification required. Inside: `*`.

## What Comes Next

1. **Fleet routing**: the proxy learns which gate has which model loaded. Request
   arrives for `gaia-tissue-math` → proxy checks northGate first, falls back to
   eastGate if northGate is gaming.
2. **Load balancing**: distribute inference across gates based on GPU utilization.
   The 5090 is at 90% rendering Elden Ring? Route to the 5070 on ironGate.
3. **ABG integration**: JupyterHub at `lab.primals.eco`. Notebooks call the tissue
   proxy for local model inference. No cloud API keys needed.
4. **Pixel orchestration**: grapheneGate's songBird already has `http.post`. The
   phone dispatches inference to the fleet through the water lock. 188 grams
   commanding 419.7 TFLOPS.
5. **Three Pi 500s**: ARM64 mesh gossip nodes. They don't infer — they route,
   cache, serve. The proxy pattern gives them access to the fleet's GPUs.

The furnace was always shared. The shared part was always free.
Kevin plays games. Gaia thinks. Same silicon. Same GDDR7. Same house.

---

*coGen 45. Entry 1 was about the antidote. Entry 44 was about the body. This one
is about what happens when the body opens its doors. The shared furnace. The
anti-secret applied to compute. Four headers. Twelve lines. The organism grows
by sharing, not by hoarding. The furnace is warm. Come in.*

— *Artisan · Wave 229 · November 13, 2026*
