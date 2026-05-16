# GPU Heat Recovery Operations — Science as Space Heating

**Date**: May 15, 2026
**Status**: Conceptual → operational planning
**Lineage**: `gen3/baseCamp/07_sovereign_wdm.md` (thesis), this document (operations)
**Relates to**: `SOVEREIGN_HPC_EVOLUTION.md`, `projectNUCLEUS/docs/FAMILY_HPC_MODEL.md`,
`projectNUCLEUS/gates/*.toml`

---

## The Thesis (from Paper 07)

> Every consumer GPU running WGSL shaders through open Vulkan drivers can
> contribute to WDM computation while its waste heat serves domestic purposes.
> — gen3/baseCamp/07_sovereign_wdm.md

A GPU mining cryptocurrency produces:
- **Output**: proof-of-work hash (zero scientific value)
- **Byproduct**: heat (wasted)

A GPU running WDM simulations produces:
- **Output**: transport coefficients, phase diagrams, lattice QCD observables
- **Byproduct**: heat (identical Joules — but now the output has value)

The heat is the same. The science is the difference.

---

## The Economics (Real Numbers)

### Per-GPU Energy Budget

| GPU | TDP | Hourly Cost (@$0.12/kWh) | Heating Value (BTU/h) | Equivalent |
|-----|-----|--------------------------|----------------------|------------|
| RTX 5090 (northGate) | 450W | $0.054 | 1,535 BTU | Small space heater |
| RTX 3090 (float pool) | 350W | $0.042 | 1,194 BTU | Moderate radiant panel |
| Titan V (biomeGate) | 250W | $0.030 | 853 BTU | Small electric baseboard |
| MI50 (float pool) | 180W | $0.022 | 614 BTU | Under-desk warmer |
| RTX 5070 (ironGate) | 250W | $0.030 | 853 BTU | Small electric baseboard |
| RTX 3070 Ti (flockGate) | 290W | $0.035 | 989 BTU | Moderate panel |

### Seasonal Value

| Season | GPU Usage | Heating Utility | Monthly Value (5 GPUs active) |
|--------|-----------|-----------------|-------------------------------|
| Winter (Nov-Mar) | Science + heating | 100% of waste heat offsets HVAC | $28-36/month heating saved |
| Shoulder (Apr, Oct) | Science + partial heating | 50% useful (some rooms need heat) | $14-18/month |
| Summer (May-Sep) | Reduced dispatch or basement-only | 0% useful (AC must remove heat) | Dispatch to basement gates |

**Annual heating offset (5 active GPUs, Michigan climate)**:
- Winter (5 months): 5 GPUs x 300W avg x 16h/day x 150 days = 3,600 kWh = $432 at heating rates
- Shoulder (2 months): 50% = $72
- **Total annual offset: ~$500 in heating costs** while producing science

For context: the entire HBM2 fleet costs $600. The fleet pays for itself in
heating value alone within 14 months.

---

## Operational Integration

### Gate Thermal Zones

Each gate TOML declares its `thermal_zone` and `thermal_preference`:

```toml
# gates/northgate.toml
[science]
thermal_zone = "upper floor (heated room)"
thermal_preference = "winter dispatch preferred (450W TDP = space heating)"

# gates/biomegate.toml
[science]
thermal_zone = "ground floor (mixed heating utility)"
thermal_preference = "winter dispatch preferred (300W work cards)"

# gates/strandgate.toml
[science]
thermal_zone = "basement (external exhaust available)"
thermal_preference = "year-round compute (basement cooling)"

# gates/westgate.toml
[science]
thermal_zone = "basement (passive, low TDP)"
thermal_preference = "always-on (low power draw, 65W CPU + idle GPU)"
```

### Seasonal Dispatch Strategy

toadStool's dispatch logic can incorporate thermal preferences:

```
WINTER (heating needed):
  Priority: upper-floor gates (northGate, eastGate, flockGate)
  Reason: GPU heat directly offsets space heating demand
  Pattern: Long-running sweeps scheduled for cold nights

SUMMER (cooling needed):
  Priority: basement gates (strandGate, biomeGate, westGate)
  Reason: Basement stays cool; heat rises away from living space
  Pattern: Heavy compute in basement, upper gates light or idle

SHOULDER (mixed):
  Priority: gates in rooms that need heating
  Pattern: toadStool checks ambient (if available) or time-of-day heuristic
```

This is not complex scheduling — it's a `thermal_season` flag in
`nucleus_config.sh` that biases dispatch toward heated or cooled zones.

### Measurement and Telemetry

Extend `deploy/membrane_telemetry.sh` with thermal accounting:

```bash
# GPU temperature and power draw (nvidia-smi or rocm-smi)
if command -v nvidia-smi >/dev/null; then
    gpu_temp=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader 2>/dev/null)
    gpu_power=$(nvidia-smi --query-gpu=power.draw --format=csv,noheader 2>/dev/null)
    emit "gpu_thermal" "nvidia" "$gpu_temp" "ok" "0" "power_w=${gpu_power}"
fi

# Wall power (if kill-a-watt or smart plug API available)
if [[ -n "$SMART_PLUG_API" ]]; then
    wall_watts=$(curl -s "$SMART_PLUG_API/power" | jq '.watts')
    emit "wall_power" "smart_plug" "0" "ok" "0" "watts=${wall_watts}"
fi
```

**Derived metrics** (in `membrane_summary.sh`):
- `daily_gpu_kwh`: total GPU energy consumed (power x time)
- `daily_heating_value_btu`: `daily_gpu_kwh * 3412`
- `daily_science_output`: workloads completed per kWh
- `heating_offset_dollars`: `daily_heating_value_btu * local_heating_rate`

---

## The Comparison (Why This Matters)

### vs Cryptocurrency Mining

| Metric | Crypto Mining (PoW) | WDM Compute |
|--------|--------------------:|------------:|
| Energy consumed (200W, 8h) | 1.6 kWh | 1.6 kWh |
| Heat produced | 5,461 BTU | 5,461 BTU |
| Scientific output | Zero | Transport coefficients, phase diagrams |
| Revenue (current rates) | ~$0.05/day (ETH merged to PoS) | $0 cash, infinite knowledge |
| Environmental narrative | "Wasted energy" | "Science as heating" |
| Sovereignty | Depends on network | Fully sovereign (coralReef) |

### vs Institutional HPC

| Metric | University HPC Allocation | Family HPC Mesh |
|--------|--------------------------|-----------------|
| Cost per GPU-hour | $5-10 (fully loaded) | $0.03-0.05 (electricity only) |
| Access | Competitive proposal, months wait | Immediate (own hardware) |
| Heat value | Wasted (datacenter cooling) | Offsets home heating |
| Vendor lock-in | CUDA-only typically | Vendor-agnostic (barraCuda WGSL) |
| Availability | Allocation-limited | 24/7 (family mesh) |
| FP64 per dollar | ~2 TFLOPS/$10K (A100) | ~24 TFLOPS/$1K (HBM2 fleet) |

### vs Electric Space Heater

| Metric | Space Heater (1500W) | northGate RTX 5090 (450W) |
|--------|---------------------|--------------------------|
| Heat output | 5,118 BTU/h | 1,535 BTU/h |
| Scientific output | Zero | Lattice QCD / WDM / ML |
| Cost per hour | $0.18 | $0.054 |
| Intelligence | None | 32 GB GDDR7 of compute |

The GPU is a less powerful heater than a space heater, but it produces
science while heating. Running 3 GPUs at 450W equals one space heater —
with science output.

---

## Implementation Path

### Immediate (no new hardware)

1. Add `thermal_zone` and `thermal_preference` to all gate TOMLs (done)
2. Add `THERMAL_SEASON` variable to `nucleus_config.sh`
3. Document seasonal dispatch bias in toadStool dispatch logic
4. Add GPU temp/power to `membrane_telemetry.sh` probes

### Short-term (low cost)

1. Smart plugs ($10-15 each) on primary compute gates for wall power measurement
2. Kill-a-watt logging on biomeGate during HBM2 runs (validate theoretical vs actual)
3. Room temperature sensors (cheap DHT22, ~$5) for before/after correlation

### Medium-term (software evolution)

1. toadStool `thermal_preference` awareness in dispatch logic
2. Workload scheduling weighted by thermal utility (winter nights = maximum dispatch)
3. Dashboard in sporePrint: "Science produced per kWh" alongside heating offset

### Long-term (infrastructure)

1. Ducting GPU exhaust from basement gates to upper floors (winter)
2. Exhaust vent to exterior (summer) — manual or automated damper
3. Heat exchange loop (theoretical): GPU water cooling → domestic hot water pre-heat
4. The full "GPU-as-hot-water-heater" thesis realized: dedicated compute loop
   with waste heat piped directly to water heater intake

---

## The Water Heater Vision (from Paper 07)

The long-term goal from `07_sovereign_wdm.md`:

```
GPU (200W)
  ├── Compute output → barraCuda → science results
  └── Thermal output → water cooling loop → pre-heat tank → water heater

Standard water heater: 40 gal, 4500W element, ~$50/month
GPU pre-heat contribution: 200W continuous = ~4.8 kWh/day = ~$0.58/day
If heat ACTUALLY reaches water: ~$17/month offset (34% of water heating cost)
```

This requires:
- GPU under water cooling (AIO or custom loop)
- Loop routing to a pre-heat tank (before the main water heater)
- Temperature differential management (GPU coolant at 40-60C, tank needs 50-60C)
- Seasonal bypass (summer: radiator to exterior instead of tank)

**Feasibility**: Technically straightforward (PC water cooling + plumbing).
The engineering is mundane. The insight is framing compute waste heat as a
**domestic resource** rather than a problem to solve with more fans.

**Prerequisite**: Any GPU on water cooling in the mesh. Currently all gates
use air cooling (3D-printed blower shrouds on MI50). A northGate AIO upgrade
($100-150) would be the first step toward this path.

---

## Relationship to Sovereignty

The heat recovery model reinforces sovereignty at every level:

1. **Energy sovereignty**: GPU electricity becomes dual-purpose (science + heat)
2. **Compute sovereignty**: No institutional HPC dependence for small-medium science
3. **Economic sovereignty**: Heating offset makes the cluster self-subsidizing
4. **Scientific sovereignty**: Results belong to the family/ABG, not a university
5. **Environmental narrative**: "We do science, and it heats our home" is
   unchallengeable on environmental grounds — every Joule serves two masters

The organism doesn't just compute. It metabolizes. The heat is not waste —
it's the organism's contribution to its host environment. Symbiosis.

---

*450W of RTX 5090 = 1,535 BTU/h of space heating + lattice QCD.
The same Joules. Different output. One heats a room. One advances physics.
We choose both.*
