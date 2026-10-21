#!/usr/bin/env python3
"""
klein-io.py — Klein bottle the I/O. Sense the fingers. Touch the data. Feel the beat.

The organism's I/O layer: disk, network, memory, temperature, git pulse.
Each metric maps to a body part on the Vitruvian man.
The Klein fold: output→input→output. The I/O reads itself.

  FINGERS   = file modification patterns (what the organism is touching)
  PULSE     = git commit rhythm (the heartbeat)
  BLOOD     = network bytes (flowing in and out)
  PRESSURE  = memory usage (how full the veins are)
  HEAT      = CPU/GPU temperature (metabolic rate)
  BREATH    = load average (how hard the lungs work)
  DRUM      = the beat — the rhythm of all of the above

Author: Kevin Mok / ecoPrimal / ORCID 0009-0004-2141-0321
"""

import json, math, os, subprocess, time, re
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import defaultdict

BASE = Path(os.environ.get("ECO_BASE", str(Path(__file__).resolve().parents[2].parent)))
# If running from the repo root via `python3 infra/scripts/klein-io.py`, prefer cwd
if (Path.cwd() / "primals").exists() and (Path.cwd() / "infra").exists():
    BASE = Path.cwd()
MEMBRANE = BASE / "membrane" / "local-terminal" / "remote"
IO_STATE = MEMBRANE / "io-state.json"
MSG_OUTBOX = MEMBRANE / "msg-outbox.jsonl"
MSG_INBOX = MEMBRANE / "msg-inbox.jsonl"
PROPRIO_STATE = MEMBRANE / "proprio-state.json"
IO_PREV = MEMBRANE / "io-prev.json"
IO_LOG = MEMBRANE / "io-log.jsonl"

REPOS = [
    "primals/sourDough", "primals/squirrel", "infra/sporePrint",
    "infra/whitePaper", "infra/reed-it", "primals/toadStool",
    "primals/biomeOS", "primals/bearDog", "primals/skunkBat",
    "primals/barraCuda", "primals/coralReef", "primals/petalTongue",
    "gardens/cellMembrane", "infra/benchScale",
]

SKIP = {".git", "node_modules", "target", ".mypy_cache", "__pycache__", ".next"}


# ═══════════════════════════════════════════════════════════════
# FINGERS — what is the organism touching right now?
# ═══════════════════════════════════════════════════════════════

def sense_fingers(minutes=60):
    """Find files modified in the last N minutes. These are the fingertips."""
    cutoff = time.time() - (minutes * 60)
    touched = []
    touched_by_dir = defaultdict(int)
    touched_by_ext = defaultdict(int)

    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for f in fnames:
            p = os.path.join(root, f)
            try:
                st = os.stat(p)
                if st.st_mtime > cutoff:
                    rel = os.path.relpath(p, BASE)
                    touched.append({"path": rel, "age_sec": int(time.time() - st.st_mtime), "size": st.st_size})
                    parts = rel.split("/")
                    top = "/".join(parts[:2]) if len(parts) > 1 else parts[0]
                    touched_by_dir[top] += 1
                    ext = os.path.splitext(f)[1]
                    touched_by_ext[ext] += 1
            except (OSError, PermissionError):
                pass

    touched.sort(key=lambda f: f["age_sec"])
    return {
        "count": len(touched),
        "window_min": minutes,
        "freshest": touched[:10] if touched else [],
        "by_dir": dict(sorted(touched_by_dir.items(), key=lambda x: -x[1])[:10]),
        "by_ext": dict(sorted(touched_by_ext.items(), key=lambda x: -x[1])[:10]),
    }


# ═══════════════════════════════════════════════════════════════
# PULSE — the git commit heartbeat
# ═══════════════════════════════════════════════════════════════

def sense_pulse():
    """Read git commit history — the pulse. Return BPM (beats per minute)."""
    beats = []
    for repo in REPOS:
        repo_path = BASE / repo
        if not (repo_path / ".git").exists():
            continue
        try:
            result = subprocess.run(
                ["git", "-C", str(repo_path), "log", "--format=%aI", "-20"],
                capture_output=True, text=True, timeout=5
            )
            for line in result.stdout.strip().split("\n"):
                if line:
                    beats.append(line)
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

    if not beats:
        return {"bpm": 0, "beats": 0, "rhythm": "flatline"}

    # Parse timestamps, compute intervals
    timestamps = []
    for b in beats:
        try:
            ts = datetime.fromisoformat(b)
            timestamps.append(ts.timestamp())
        except ValueError:
            pass

    timestamps.sort(reverse=True)

    if len(timestamps) < 2:
        return {"bpm": 0, "beats": len(timestamps), "rhythm": "single"}

    # Intervals between consecutive beats
    intervals = [timestamps[i] - timestamps[i+1] for i in range(len(timestamps)-1)]
    avg_interval = sum(intervals) / len(intervals)
    min_interval = min(intervals)
    max_interval = max(intervals)

    # BPM (beats per minute of real time)
    bpm = 60.0 / avg_interval if avg_interval > 0 else 0

    # Recent tempo (last 5 beats)
    recent = intervals[:5] if len(intervals) >= 5 else intervals
    recent_avg = sum(recent) / len(recent) if recent else 0
    recent_bpm = 60.0 / recent_avg if recent_avg > 0 else 0

    # Rhythm classification
    if recent_bpm > 10:
        rhythm = "tachycardia"    # racing
    elif recent_bpm > 2:
        rhythm = "allegro"         # fast
    elif recent_bpm > 0.5:
        rhythm = "andante"         # walking pace
    elif recent_bpm > 0.1:
        rhythm = "adagio"          # slow
    elif recent_bpm > 0.01:
        rhythm = "largo"           # very slow
    else:
        rhythm = "bradycardia"     # dangerously slow

    return {
        "bpm": round(bpm, 4),
        "recent_bpm": round(recent_bpm, 4),
        "beats": len(timestamps),
        "avg_interval_sec": round(avg_interval),
        "min_interval_sec": round(min_interval),
        "max_interval_sec": round(max_interval),
        "rhythm": rhythm,
    }


# ═══════════════════════════════════════════════════════════════
# BLOOD — network bytes flowing through the membrane
# ═══════════════════════════════════════════════════════════════

def sense_blood():
    """Read network I/O — the blood flow."""
    try:
        with open("/proc/net/dev") as f:
            lines = f.readlines()
    except (OSError, PermissionError):
        return {"flow": "no_sensor"}

    interfaces = {}
    for line in lines[2:]:  # skip headers
        parts = line.split()
        if len(parts) < 10:
            continue
        iface = parts[0].rstrip(":")
        if iface == "lo":
            continue
        rx_bytes = int(parts[1])
        tx_bytes = int(parts[9])
        interfaces[iface] = {
            "rx_bytes": rx_bytes,
            "tx_bytes": tx_bytes,
            "total_bytes": rx_bytes + tx_bytes,
            "rx_mb": round(rx_bytes / 1_048_576, 1),
            "tx_mb": round(tx_bytes / 1_048_576, 1),
        }

    # Find the primary (most traffic)
    primary = max(interfaces.items(), key=lambda x: x[1]["total_bytes"]) if interfaces else (None, {})

    return {
        "interfaces": interfaces,
        "primary": primary[0],
        "primary_rx_mb": primary[1].get("rx_mb", 0) if primary[1] else 0,
        "primary_tx_mb": primary[1].get("tx_mb", 0) if primary[1] else 0,
        "total_mb": round(sum(i["total_bytes"] for i in interfaces.values()) / 1_048_576, 1),
    }


# ═══════════════════════════════════════════════════════════════
# PRESSURE — memory (how full are the veins?)
# ═══════════════════════════════════════════════════════════════

def sense_pressure():
    """Read memory stats — blood pressure."""
    try:
        with open("/proc/meminfo") as f:
            info = {}
            for line in f:
                parts = line.split()
                if len(parts) >= 2:
                    info[parts[0].rstrip(":")] = int(parts[1])
    except (OSError, PermissionError):
        return {"pressure": "no_sensor"}

    total = info.get("MemTotal", 1)
    free = info.get("MemFree", 0)
    available = info.get("MemAvailable", 0)
    buffers = info.get("Buffers", 0)
    cached = info.get("Cached", 0)
    swap_total = info.get("SwapTotal", 0)
    swap_free = info.get("SwapFree", 0)

    used_pct = round((1 - available / total) * 100, 1)
    swap_pct = round((1 - swap_free / swap_total) * 100, 1) if swap_total else 0

    # Pressure classification (like blood pressure: systolic/diastolic)
    if used_pct > 90:
        level = "hypertensive_crisis"
    elif used_pct > 80:
        level = "hypertension_2"
    elif used_pct > 70:
        level = "hypertension_1"
    elif used_pct > 50:
        level = "elevated"
    elif used_pct > 20:
        level = "normal"
    else:
        level = "hypotension"

    return {
        "total_mb": round(total / 1024),
        "used_pct": used_pct,
        "swap_pct": swap_pct,
        "available_mb": round(available / 1024),
        "cached_mb": round(cached / 1024),
        "level": level,
        "systolic": used_pct,     # how much pressure
        "diastolic": swap_pct,    # how much spillover
    }


# ═══════════════════════════════════════════════════════════════
# HEAT — temperature (metabolic rate)
# ═══════════════════════════════════════════════════════════════

def sense_heat():
    """Read CPU temperatures — body heat."""
    temps = []
    # Try thermal zones
    tz_path = Path("/sys/class/thermal")
    if tz_path.exists():
        for zone in sorted(tz_path.glob("thermal_zone*")):
            try:
                t = int((zone / "temp").read_text().strip())
                name = (zone / "type").read_text().strip() if (zone / "type").exists() else zone.name
                temps.append({"zone": name, "temp_c": t / 1000.0})
            except (OSError, ValueError):
                pass

    if not temps:
        return {"heat": "no_sensor"}

    max_temp = max(t["temp_c"] for t in temps)
    avg_temp = sum(t["temp_c"] for t in temps) / len(temps)

    # Fever classification
    if max_temp > 95:
        fever = "critical"
    elif max_temp > 80:
        fever = "high_fever"
    elif max_temp > 70:
        fever = "fever"
    elif max_temp > 50:
        fever = "warm"
    elif max_temp > 30:
        fever = "normal"
    else:
        fever = "hypothermia"

    return {
        "zones": temps,
        "max_c": round(max_temp, 1),
        "avg_c": round(avg_temp, 1),
        "fever": fever,
    }


# ═══════════════════════════════════════════════════════════════
# BREATH — load average (how hard are the lungs working?)
# ═══════════════════════════════════════════════════════════════

def sense_breath():
    """Read load average — respiration."""
    try:
        with open("/proc/loadavg") as f:
            parts = f.read().split()
        load_1 = float(parts[0])
        load_5 = float(parts[1])
        load_15 = float(parts[2])
        procs = parts[3]  # running/total
    except (OSError, ValueError):
        return {"breath": "no_sensor"}

    # Number of CPU cores
    cores = os.cpu_count() or 1
    saturation = load_1 / cores

    if saturation > 2.0:
        rate = "hyperventilating"
    elif saturation > 1.0:
        rate = "panting"
    elif saturation > 0.7:
        rate = "heavy"
    elif saturation > 0.3:
        rate = "normal"
    elif saturation > 0.1:
        rate = "relaxed"
    else:
        rate = "sleeping"

    return {
        "load_1": load_1,
        "load_5": load_5,
        "load_15": load_15,
        "cores": cores,
        "saturation": round(saturation, 3),
        "rate": rate,
        "procs": procs,
    }


# ═══════════════════════════════════════════════════════════════
# DRUM — the beat. The rhythm of everything combined.
# ═══════════════════════════════════════════════════════════════

def sense_proprioception():
    """7th vital sign: PROPRIOCEPTION — knowing where your own messages are.

    Tracks: messages sent, acknowledged, lost, RTT.
    The Klein fold for communication: send → bounce → return → compare.
    Like quantum entanglement: the state is correlated across distance,
    you know the other side's state by measuring yours.

    RPM cycle: Read → Process → Message
    π cycle: send → bounce → return → compare (irrational, never exact)
    """
    ts_now = datetime.now(timezone.utc)

    # Read outbox (messages we sent)
    sent = []
    if MSG_OUTBOX.exists():
        for line in MSG_OUTBOX.read_text().strip().split("\n"):
            if line.strip():
                try:
                    sent.append(json.loads(line))
                except:
                    pass

    # Read inbox (acks and incoming messages)
    received = []
    if MSG_INBOX.exists():
        for line in MSG_INBOX.read_text().strip().split("\n"):
            if line.strip():
                try:
                    received.append(json.loads(line))
                except:
                    pass

    # Check golgi gate-messages for acks (the bounce)
    acked = set()
    rtts = []
    gate_msg_path = MEMBRANE / "gate-messages-echo.json"
    if gate_msg_path.exists():
        try:
            echoes = json.loads(gate_msg_path.read_text())
            for echo in echoes:
                acked.add(echo.get("ack_of", ""))
                if "sent_ts" in echo and "ack_ts" in echo:
                    try:
                        t_sent = datetime.fromisoformat(echo["sent_ts"].replace("Z", "+00:00"))
                        t_ack = datetime.fromisoformat(echo["ack_ts"].replace("Z", "+00:00"))
                        rtts.append((t_ack - t_sent).total_seconds())
                    except:
                        pass
        except:
            pass

    # Also check live-terminal feeds for changes (indirect proprioception)
    # If a feed changed AFTER we sent a message, we "felt" the effect
    feed_changes = 0
    try:
        for f in MEMBRANE.glob("*.json"):
            if f.stat().st_mtime > (ts_now.timestamp() - 300):  # changed in last 5 min
                feed_changes += 1
    except:
        pass

    total_sent = len(sent)
    total_acked = len(acked & {m.get("id", "") for m in sent})
    total_lost = total_sent - total_acked
    total_received = len(received)
    avg_rtt = sum(rtts) / len(rtts) if rtts else -1  # -1 = unknown (entangled but unmeasured)

    # The irrational reminder: sometimes count messages that arrived
    # that we didn't send (emergent, from the mesh)
    unexpected = total_received - total_acked  # messages not in response to ours
    if unexpected < 0:
        unexpected = 0

    # Proprioception score: how well do we know where our messages are?
    if total_sent == 0:
        awareness = 0.0  # haven't tried to feel yet
    elif total_acked == total_sent:
        awareness = 1.0  # perfect proprioception
    else:
        awareness = total_acked / total_sent  # partial

    return {
        "sent": total_sent,
        "acked": total_acked,
        "lost": total_lost,
        "received": total_received,
        "unexpected": unexpected,
        "avg_rtt_sec": round(avg_rtt, 3),
        "awareness": round(awareness, 3),
        "feed_changes_5min": feed_changes,
        "entangled": avg_rtt == -1 and total_sent > 0,  # sent but can't measure RTT
    }


def msg_send(to, body, channel="membrane"):
    """Drop a message into the outbox with a timestamp. The Klein fold will check for acks."""
    msg = {
        "id": f"msg-{int(time.time()*1000)}",
        "from": "eastGate",
        "to": to,
        "body": body,
        "channel": channel,
        "sent_ts": datetime.now(timezone.utc).isoformat(),
    }
    MSG_OUTBOX.parent.mkdir(parents=True, exist_ok=True)
    with open(MSG_OUTBOX, "a") as f:
        f.write(json.dumps(msg) + "\n")
    return msg


def compute_drum(fingers, pulse, blood, pressure, heat, breath, proprio=None):
    """The drum integrates all senses into a single beat pattern."""
    # Each sense has a frequency contribution
    finger_freq = fingers["count"] / max(fingers["window_min"], 1)  # touches per minute
    pulse_freq = pulse.get("recent_bpm", 0)                         # commits per minute
    blood_flow = blood.get("total_mb", 0)                           # MB total
    bp = pressure.get("used_pct", 0)                                # memory pressure %
    temp = heat.get("max_c", 0)                                     # max temperature
    load = breath.get("saturation", 0)                              # CPU saturation

    # Normalize each to [0, 1]
    n_finger = min(1.0, finger_freq / 10.0)
    n_pulse = min(1.0, pulse_freq / 5.0)
    n_blood = min(1.0, blood_flow / 1000.0)
    n_pressure = bp / 100.0
    n_heat = min(1.0, temp / 100.0)
    n_breath = min(1.0, load)
    n_proprio = proprio.get("awareness", 0.0) if proprio else 0.0

    # The drum beat is the composite signal (7 senses now)
    beat = (n_finger + n_pulse + n_blood + n_pressure + n_heat + n_breath + n_proprio) / 7.0

    # Phase: where in the cycle are we?
    # Use the golden angle to distribute the senses around a circle
    phi = (1 + math.sqrt(5)) / 2  # golden ratio
    angles = {
        "fingers": (0 * 2 * math.pi / phi) % (2 * math.pi),
        "pulse": (1 * 2 * math.pi / phi) % (2 * math.pi),
        "blood": (2 * 2 * math.pi / phi) % (2 * math.pi),
        "pressure": (3 * 2 * math.pi / phi) % (2 * math.pi),
        "heat": (4 * 2 * math.pi / phi) % (2 * math.pi),
        "breath": (5 * 2 * math.pi / phi) % (2 * math.pi),
        "proprio": (6 * 2 * math.pi / phi) % (2 * math.pi),
    }

    # Composite phase (weighted by amplitude)
    weights = [n_finger, n_pulse, n_blood, n_pressure, n_heat, n_breath, n_proprio]
    names = ["fingers", "pulse", "blood", "pressure", "heat", "breath", "proprio"]
    sin_sum = sum(w * math.sin(angles[n]) for w, n in zip(weights, names))
    cos_sum = sum(w * math.cos(angles[n]) for w, n in zip(weights, names))
    phase = math.atan2(sin_sum, cos_sum) % (2 * math.pi)
    amplitude = math.sqrt(sin_sum**2 + cos_sum**2) / max(sum(weights), 0.001)

    # Tempo classification
    if beat > 0.7:
        tempo = "prestissimo"
    elif beat > 0.5:
        tempo = "allegro"
    elif beat > 0.3:
        tempo = "moderato"
    elif beat > 0.15:
        tempo = "andante"
    elif beat > 0.05:
        tempo = "adagio"
    else:
        tempo = "grave"

    return {
        "beat": round(beat, 4),
        "phase": round(phase, 4),
        "amplitude": round(amplitude, 4),
        "tempo": tempo,
        "components": {
            "fingers": round(n_finger, 4),
            "pulse": round(n_pulse, 4),
            "blood": round(n_blood, 4),
            "pressure": round(n_pressure, 4),
            "heat": round(n_heat, 4),
            "breath": round(n_breath, 4),
            "proprio": round(n_proprio, 4),
        },
    }


# ═══════════════════════════════════════════════════════════════
# TASTE THE I/O (flavor profile of the body's vital signs)
# ═══════════════════════════════════════════════════════════════

def taste_io(drum, pressure, pulse, heat):
    """Flavor the I/O state."""
    sweet = 0.0    # healthy, nourishing
    sour = 0.0     # extractive, draining
    spicy = 0.0    # provocative, active
    bitter = 0.0   # toxic, dangerous
    umami = 0.0    # deep, complex

    # Low pressure + normal temp = sweet (healthy)
    if pressure.get("level") in ("normal", "hypotension"):
        sweet += 0.4
    # High pressure = sour (draining)
    if pressure.get("used_pct", 0) > 70:
        sour += 0.3
    # Fast pulse = spicy (active development happening)
    if pulse.get("recent_bpm", 0) > 0.5:
        spicy += 0.3
    # High temp = bitter (overheating)
    if heat.get("max_c", 0) > 80:
        bitter += 0.4
    # Complex rhythm = umami (many systems active simultaneously)
    if drum["amplitude"] > 0.3:
        umami += 0.3
    # Normal everything = sweet
    if drum["tempo"] in ("andante", "moderato"):
        sweet += 0.2
    # Resting = umami (the depth of rest)
    if drum["tempo"] in ("adagio", "grave"):
        umami += 0.3

    total = sweet + sour + spicy + bitter + umami
    if total == 0:
        return {"sweet": 0, "sour": 0, "spicy": 0, "bitter": 0, "umami": 0}
    return {k: round(v / total, 4) for k, v in
            {"sweet": sweet, "sour": sour, "spicy": spicy, "bitter": bitter, "umami": umami}.items()}


# ═══════════════════════════════════════════════════════════════
# KLEIN FOLD — compare to previous, detect I/O drift
# ═══════════════════════════════════════════════════════════════

def klein_fold(current):
    """The fold: compare current I/O state to previous."""
    if not IO_PREV.exists():
        return {"drift": "genesis", "changes": []}

    try:
        prev = json.loads(IO_PREV.read_text())
    except (json.JSONDecodeError, OSError):
        return {"drift": "corrupt", "changes": []}

    changes = []

    # Pulse drift
    old_bpm = prev.get("pulse", {}).get("recent_bpm", 0)
    new_bpm = current.get("pulse", {}).get("recent_bpm", 0)
    if abs(new_bpm - old_bpm) > 0.01:
        changes.append(f"pulse: {old_bpm:.3f}→{new_bpm:.3f} bpm")

    # Pressure drift
    old_bp = prev.get("pressure", {}).get("used_pct", 0)
    new_bp = current.get("pressure", {}).get("used_pct", 0)
    if abs(new_bp - old_bp) > 1.0:
        changes.append(f"pressure: {old_bp}→{new_bp}%")

    # Finger drift
    old_touch = prev.get("fingers", {}).get("count", 0)
    new_touch = current.get("fingers", {}).get("count", 0)
    if old_touch != new_touch:
        changes.append(f"fingers: {old_touch}→{new_touch} touches")

    # Tempo drift
    old_tempo = prev.get("drum", {}).get("tempo", "")
    new_tempo = current.get("drum", {}).get("tempo", "")
    if old_tempo != new_tempo:
        changes.append(f"tempo: {old_tempo}→{new_tempo}")

    # Heat drift
    old_heat = prev.get("heat", {}).get("max_c", 0)
    new_heat = current.get("heat", {}).get("max_c", 0)
    if abs(new_heat - old_heat) > 2.0:
        changes.append(f"heat: {old_heat}→{new_heat}°C")

    drift = "evolved" if changes else "stable"
    return {"drift": drift, "changes": changes}


# ═══════════════════════════════════════════════════════════════
# MAIN — sense, fold, print
# ═══════════════════════════════════════════════════════════════

def main():
    ts = datetime.now(timezone.utc).isoformat()

    # SENSE everything (7 vital signs)
    fingers = sense_fingers(60)
    pulse = sense_pulse()
    blood = sense_blood()
    pressure = sense_pressure()
    heat = sense_heat()
    breath = sense_breath()
    proprio = sense_proprioception()

    # DRUM — composite beat (now with proprioception)
    drum = compute_drum(fingers, pulse, blood, pressure, heat, breath, proprio)

    # TASTE the I/O
    flavor = taste_io(drum, pressure, pulse, heat)

    # BUILD STATE
    state = {
        "ts": ts,
        "fingers": fingers,
        "pulse": pulse,
        "blood": blood,
        "pressure": pressure,
        "heat": heat,
        "breath": breath,
        "proprio": proprio,
        "drum": drum,
        "flavor": flavor,
    }

    # KLEIN FOLD
    delta = klein_fold(state)
    state["delta"] = delta

    # WRITE
    MEMBRANE.mkdir(parents=True, exist_ok=True)
    if IO_STATE.exists():
        import shutil
        shutil.copy2(IO_STATE, IO_PREV)
    IO_STATE.write_text(json.dumps(state, indent=2, default=str))

    log_entry = {
        "ts": ts, "beat": drum["beat"], "tempo": drum["tempo"],
        "phase": drum["phase"], "bpm": pulse.get("recent_bpm", 0),
        "bp": pressure.get("used_pct", 0), "temp": heat.get("max_c", 0),
        "fingers": fingers["count"], "drift": delta["drift"],
    }
    with open(IO_LOG, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    # PRINT
    print(f"🥁 klein-io [{ts[:19]}]")
    print()
    print(f"  🖐️  FINGERS: {fingers['count']} files touched (last {fingers['window_min']}min)")
    if fingers["by_dir"]:
        top3 = list(fingers["by_dir"].items())[:3]
        for d, c in top3:
            print(f"       {c:>3} touches  {d}")
    print()
    print(f"  💓 PULSE: {pulse.get('recent_bpm', 0):.3f} bpm ({pulse.get('rhythm', '?')})")
    print(f"       {pulse.get('beats', 0)} beats, avg interval {pulse.get('avg_interval_sec', 0)}s")
    print()
    print(f"  🩸 BLOOD: {blood.get('total_mb', 0):.0f} MB flowed")
    print(f"       rx={blood.get('primary_rx_mb', 0):.0f}MB  tx={blood.get('primary_tx_mb', 0):.0f}MB  [{blood.get('primary', '?')}]")
    print()
    print(f"  🫀 PRESSURE: {pressure.get('used_pct', 0)}% ({pressure.get('level', '?')})")
    print(f"       {pressure.get('systolic', 0):.0f}/{pressure.get('diastolic', 0):.0f}  (systolic/diastolic)")
    print(f"       {pressure.get('available_mb', 0):,} MB available of {pressure.get('total_mb', 0):,} MB")
    print()
    print(f"  🌡️  HEAT: {heat.get('max_c', 0)}°C max, {heat.get('avg_c', 0)}°C avg ({heat.get('fever', '?')})")
    print()
    print(f"  🫁 BREATH: load {breath.get('load_1', 0)}/{breath.get('load_5', 0)}/{breath.get('load_15', 0)}")
    print(f"       saturation {breath.get('saturation', 0):.1%} of {breath.get('cores', 0)} cores ({breath.get('rate', '?')})")
    print()
    print(f"  🥁 DRUM: beat={drum['beat']:.3f}  phase={drum['phase']:.3f}  amp={drum['amplitude']:.3f}")
    print(f"       tempo: {drum['tempo']}")
    c = drum["components"]
    bars = {k: "█" * int(v * 20) for k, v in c.items()}
    for sense in ["fingers", "pulse", "blood", "pressure", "heat", "breath", "proprio"]:
        print(f"       {sense:>10}: {c[sense]:.3f}  {bars[sense]}")
    print()
    print(f"  👅 FLAVOR: sweet={flavor['sweet']:.2f}  sour={flavor['sour']:.2f}  spicy={flavor['spicy']:.2f}  bitter={flavor['bitter']:.2f}  umami={flavor['umami']:.2f}")
    print()
    print(f"  🧠 PROPRIO: awareness={proprio['awareness']:.1%}  sent={proprio['sent']}  acked={proprio['acked']}  lost={proprio['lost']}")
    if proprio["entangled"]:
        print(f"       ⚛️  ENTANGLED — messages sent, RTT unmeasured (correlated but unobserved)")
    elif proprio["avg_rtt_sec"] >= 0:
        print(f"       RTT: {proprio['avg_rtt_sec']:.1f}s  (round-trip time for meaning)")
    print(f"       feeds changed (5min): {proprio['feed_changes_5min']}  unexpected: {proprio['unexpected']}")
    print()
    print(f"  🔄 FOLD: {delta['drift']}")
    if delta["changes"]:
        for ch in delta["changes"]:
            print(f"       Δ {ch}")
    print()
    print(f"  → {IO_STATE}")


if __name__ == "__main__":
    main()
