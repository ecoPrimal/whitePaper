# HBM2 Acquisition Watchlist

**Purpose**: Secondary market HBM2 cards worth acquiring for sovereign compute.
These cards are physically capable but vendor-orphaned — CUDA/ROCm support dropped,
which craters resale price while the silicon remains viable for coralReef's
sovereign compiler pipeline.

**Last Updated**: March 16, 2026

---

## Currently Owned

| Card | Qty | HBM2 | FP64 | BW | Arch | coralReef Target | Status |
|------|-----|------|------|----|------|------------------|--------|
| **Titan V** | 2 | 12 GB each | 7.4 TFLOPS | 653 GB/s | Volta (SM70) | `sm_70` | biomeGate (HBM2 bench) |
| **MI50** | 2 | 16 GB each | 6.6 TFLOPS | 1024 GB/s | Vega 20 (GCN 5.0, gfx906) | `gfx906` | biomeGate (3D printed blowers) |

**Owned totals**: 4 cards, 56 GB HBM2, ~28 TFLOPS FP64, ~$600 invested

---

## Tier 1 — High Priority (Best Value, Vendor-Orphaned)

### AMD Instinct MI60

| Spec | Value |
|------|-------|
| **HBM2** | 32 GB |
| **FP64** | 7.4 TFLOPS |
| **FP32** | 14.75 TFLOPS |
| **BW** | 1024 GB/s |
| **Arch** | Vega 20, 7nm (GCN 5.0, gfx906) |
| **coralReef target** | `gfx906` (same as MI50 — zero new compiler work) |
| **PCIe** | 4.0 x16 |
| **TDP** | 300W |
| **ROCm support** | Dropped. Maintenance ended Q2 2024 (ROCm 5.7 last). |
| **Used price** | ~$550–600 |
| **Cooling** | Passive. 3D printed shrouds available (Cults3D, Printables — MI25/MI50/MI60 compatible, 40mm–120mm fan options) |
| **Why buy** | Double the HBM2 of MI50 (32 vs 16 GB), identical arch so existing gfx906 work applies directly. Same compiler target, twice the memory. Best single purchase on the list. |

### NVIDIA Tesla V100 (16 GB PCIe)

| Spec | Value |
|------|-------|
| **HBM2** | 16 GB |
| **FP64** | 7.0 TFLOPS (PCIe), 7.8 TFLOPS (SXM2) |
| **FP32** | 14.0 TFLOPS (PCIe), 15.7 TFLOPS (SXM2) |
| **BW** | 900 GB/s |
| **Arch** | Volta (SM70) — same as Titan V |
| **coralReef target** | `sm_70` (same as Titan V — zero new compiler work) |
| **PCIe** | 3.0 x16 |
| **TDP** | 250W |
| **CUDA support** | Volta marked "feature-complete and frozen" in CUDA 12.8. R535 LTS driver ends June 2026. |
| **Used price** | ~$380–530 (16 GB PCIe), ~$500–650 (16 GB SXM2 + adapter) |
| **Cooling** | Passive. Extensive 3D printed blower ecosystem (Tindie $17, Printables free STL, GPUmods). SXM2 cards need carrier board + shroud. |
| **Why buy** | Same SM70 as Titan V, so existing compiler work applies. 16 GB version is the sweet spot — cheap, PCIe, fits standard cases. The datacenter V100 that NVIDIA is walking away from. |

### Tesla P100 (16 GB PCIe)

| Spec | Value |
|------|-------|
| **HBM2** | 16 GB |
| **FP64** | 5.3 TFLOPS |
| **FP32** | 10.6 TFLOPS |
| **BW** | 732 GB/s |
| **Arch** | Pascal (SM60) |
| **coralReef target** | `sm_60` (new target, simpler than SM70) |
| **PCIe** | 3.0 x16 |
| **TDP** | 300W |
| **CUDA support** | Pascal marked "feature-complete and frozen" alongside Volta. |
| **Used price** | ~$350–750 (wide range; NEW units at $735) |
| **Cooling** | Passive. Same 3D printed shroud ecosystem as V100 (STKN, GPUmods). |
| **Why buy** | Cheapest HBM2 entry. FP64 is lower than V100/MI60 but still 5.3 TFLOPS. Pascal SM60 is a simpler target than Volta — could be useful as a "coralReef starter" arch. |

---

## Tier 2 — Worth Watching (Higher Price, More Capability)

### NVIDIA Tesla V100 (32 GB PCIe)

| Spec | Value |
|------|-------|
| **HBM2** | 32 GB |
| **FP64** | 7.0 TFLOPS |
| **BW** | 900 GB/s |
| **Arch** | Volta (SM70) |
| **Used price** | ~$890–1,700 (SXM2 cheapest, PCIe premium) |
| **Why watch** | Same arch as Titan V but double HBM2. Price needs to drop below $500 to beat the MI60 on value. SXM2 units at ~$890 are approaching that, but need carrier boards. |

### Quadro GV100

| Spec | Value |
|------|-------|
| **HBM2** | 32 GB |
| **FP64** | 7.4 TFLOPS |
| **BW** | 870 GB/s |
| **Arch** | Volta (SM70) |
| **Used price** | ~$1,750–2,050 |
| **Why watch** | Full GV100 die (same as Titan V), 32 GB, NVLink capable, has active cooling out of the box. But too expensive right now vs MI60 at $550. Watch for price decay. |

### AMD Instinct MI100

| Spec | Value |
|------|-------|
| **HBM2** | 32 GB |
| **FP64** | 11.5 TFLOPS |
| **FP32** | 23.1 TFLOPS |
| **BW** | 1228 GB/s |
| **Arch** | CDNA 1 (gfx908) |
| **coralReef target** | `gfx908` (new target, evolution of gfx906) |
| **PCIe** | 4.0 x16 |
| **TDP** | 300W |
| **ROCm support** | Still supported in ROCm 6.x but will follow MI50/MI60 pattern eventually. |
| **Used price** | ~$1,300 |
| **Why watch** | First GPU to break 10 TFLOPS FP64. CDNA 1 is the natural evolution of gfx906 — compiler work for MI50/MI60 provides a foundation. Price is still too high. When ROCm drops gfx908, expect the MI50/MI60 price crash pattern to repeat. That's the buy signal. |

---

## Vendor Support Timeline (coralReef Opportunity Windows)

| Event | Date | Cards Affected | Price Impact |
|-------|------|----------------|--------------|
| ROCm drops Vega 20 (gfx906) maintenance | Q2 2024 | MI50, MI60 | Already crashed → $300–600 |
| CUDA marks Volta "frozen" | CUDA 12.8 (2025) | Titan V, V100, GV100 | Declining, watch eBay |
| NVIDIA R535 LTS driver EOL | June 2026 | All Volta cards | Expect price drop |
| NVIDIA R570 production driver EOL | Feb 2026 | All Volta cards | Already past → prices softening |
| ROCm drops CDNA 1 (gfx908) | TBD (~2026?) | MI100 | Not yet — watch ROCm release notes |
| CUDA drops Pascal/Volta entirely | TBD (~2027?) | P100, V100, Titan V | Will trigger another crash |

---

## Cooling Solutions

All datacenter cards ship passive (designed for server airflow). Standard desktop
cases need aftermarket cooling. The 3D-printed blower community is mature:

| Source | Cards | Fan Size | Price | Link |
|--------|-------|----------|-------|------|
| **Cults3D** | MI25, MI50, MI60 | 40/80/92/120mm | Free STL | cults3d.com |
| **Printables** | MI50, V100 SXM2 | 60mm (magnetic) | Free STL | printables.com |
| **STKN (Tindie)** | V100/P100 SXM2 | 60mm | $17 pre-built | tindie.com |
| **GPUmods** | Tesla M10–V100s | Blower | ~$30 | gpumods.com |
| **CGTrader** | V100 FHHL | Single fan | $5 STL | cgtrader.com |

Your MI50 blowers already validate this approach — same community, same pattern.

---

## Acquisition Priority

1. **MI60** (~$550) — First buy. Same gfx906 as your MI50s, double HBM2. Zero new compiler work. Blower STLs already exist for MI50/MI60 compatible shrouds.
2. **V100 16GB PCIe** (~$400) — Second buy. Same SM70 as your Titan Vs. PCIe form factor, no carrier board needed. Watch for post-June-2026 R535 EOL price drops.
3. **P100 16GB PCIe** (~$350) — Optional. Cheaper FP64, simpler Pascal target. Good "coralReef starter" arch if you want to validate SM60 before SM70.
4. **MI100** — Hold. Wait for ROCm to drop gfx908 support. When it happens, $1,300 becomes $300–500 overnight. That's 11.5 TFLOPS FP64 for the price of a V100 16GB today.

---

## Running Totals (If All Tier 1 Acquired)

| Metric | Current (Owned) | + MI60 | + V100 16GB | + P100 |
|--------|-----------------|--------|-------------|--------|
| **Cards** | 4 | 5 | 6 | 7 |
| **HBM2 Total** | 56 GB | 88 GB | 104 GB | 120 GB |
| **FP64 Aggregate** | ~28 TFLOPS | ~35.4 TFLOPS | ~42.4 TFLOPS | ~47.7 TFLOPS |
| **Investment** | ~$600 | ~$1,150 | ~$1,550 | ~$1,900 |
| **coralReef Targets** | sm_70, gfx906 | (same) | (same) | + sm_60 |

Seven HBM2 cards, 120 GB aggregate, ~48 TFLOPS FP64, under $2k total.
For reference, a single A100 80GB is $10k+ and delivers 19.5 TFLOPS FP64.
