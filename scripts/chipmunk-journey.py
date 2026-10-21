#!/usr/bin/env python3
"""
chipmunk-journey.py — The Traveling Salesman of the Membrane

A chipmunk walks the graph. At each node it checks every endpoint,
measures latency, records what it finds, and picks the next node
using shortest-unvisited (Dijkstra-greedy, nearest-neighbor TSP).

The chipmunk doesn't solve TSP optimally — it learns the graph
by walking it. Each journey is a story. The stories accumulate
into a map. The map is never complete (halting problem), but
the coverage improves (equidistribution, Weyl 1916).

Graph science foundations:
  - Dijkstra (1959): shortest path, single source
  - Bellman-Ford (1958): shortest path with negative edges
  - TSP (Dantzig, Fulkerson, Johnson 1954): visit all, return
  - Euler (1736): Königsberg bridges — can you walk every edge?
  - Hamilton (1857): can you visit every node exactly once?
  
The chipmunk's journey is Hamiltonian (visit every node) with
Dijkstra ordering (nearest unvisited next). It's the nearest-
neighbor heuristic for TSP — not optimal, but fast, and it
LEARNS the distances by actually walking them.

Marathon runner's problem: TSP is "what's the shortest route
that visits every checkpoint?" The marathon runner asks the
same question. CompSci rediscovered what runners always knew:
you can't optimize a route you haven't run. Run it first.
Map it second. Optimize it third. The chipmunk runs.
"""

import json
import time
import subprocess
import sys
from datetime import datetime, timezone

NODES = [
    {
        "id": "primals.eco",
        "type": "cis",
        "endpoints": [
            {"path": "/", "expect": 200, "label": "HUD"},
            {"path": "/api/was.json", "expect": 200, "label": "was.json"},
            {"path": "/five-o-five", "expect": 200, "label": "5/O/5"},
            {"path": "/water", "expect": 200, "label": "watering hole"},
            {"path": "/chipmunk.json", "expect": 200, "label": "chipmunk feed"},
            {"path": "/dashboard.json", "expect": 200, "label": "dashboard"},
            {"path": "/negentropy.json", "expect": 200, "label": "negentropy"},
            {"path": "/topology.json", "expect": 200, "label": "topology"},
            {"path": "/now.json", "expect": 200, "label": "now"},
            {"path": "/membrane.json", "expect": 200, "label": "membrane"},
        ],
        "base": "https://primals.eco",
    },
    {
        "id": "golgi-direct",
        "type": "trans",
        "endpoints": [
            {"path": "/", "expect": 200, "label": "Klein Gate"},
            {"path": "/was.json", "expect": 200, "label": "was.json (inner)"},
        ],
        "base": "http://157.230.3.183",
    },
    {
        "id": "sporeprint",
        "type": "trans",
        "endpoints": [
            {"path": "/", "expect": 200, "label": "sporePrint"},
        ],
        "base": "http://157.230.3.183",
        "host": "sporeprint.primals.eco",
    },
    {
        "id": "nestgate-connect",
        "type": "klein",
        "endpoints": [
            {"path": "/", "expect": 200, "label": "connect page"},
            {"path": "/campfire.json", "expect": 200, "label": "campfire"},
            {"path": "/chipmunk.json", "expect": 200, "label": "chipmunk"},
        ],
        "base": "http://157.230.3.183",
        "host": "nestgate.io",
    },
    {
        "id": "nucleus",
        "type": "nucleus",
        "endpoints": [
            {"path": "/", "expect": 200, "label": "nucleus connect"},
            {"path": "/campfire.json", "expect": 200, "label": "campfire (nucleus)"},
        ],
        "base": "http://137.184.197.151",
    },
    {
        "id": "ntfy-membrane",
        "type": "neutrino",
        "endpoints": [
            {"path": "/primals-membrane/json?poll=1&since=10m", "expect": 200, "label": "membrane channel"},
            {"path": "/primals-membrane-inbox/json?poll=1&since=10m", "expect": 200, "label": "inbox channel"},
        ],
        "base": "https://ntfy.sh",
    },
    {
        "id": "github-hud",
        "type": "nucleus",
        "endpoints": [
            {"path": "/repos/ecoPrimal/hud/commits?per_page=1", "expect": 200, "label": "hud commits"},
            {"path": "/repos/ecoPrimal/sporePrint/commits?per_page=1", "expect": 200, "label": "sporePrint commits"},
        ],
        "base": "https://api.github.com",
        "headers": {"Accept": "application/vnd.github.v3+json"},
    },
]


def check_endpoint(base, path, expect, host=None, headers=None):
    """Visit one endpoint. Return (status, latency_ms, snippet)."""
    url = base + path
    cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}|%{time_total}", 
           "--connect-timeout", "5", "--max-time", "10", url]
    if host:
        cmd.extend(["-H", f"Host: {host}"])
    if headers:
        for k, v in headers.items():
            cmd.extend(["-H", f"{k}: {v}"])
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        parts = result.stdout.strip().split("|")
        status = int(parts[0]) if parts[0].isdigit() else 0
        latency = float(parts[1]) * 1000 if len(parts) > 1 else 0
        return status, round(latency, 1), "ok" if status == expect else f"expected {expect}"
    except Exception as e:
        return 0, 0, str(e)[:60]


def dijkstra_nearest(visited, distances):
    """Pick the nearest unvisited node (greedy TSP nearest-neighbor)."""
    unvisited = [n for n in distances if n not in visited]
    if not unvisited:
        return None
    return min(unvisited, key=lambda n: distances.get(n, float("inf")))


def run_journey():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"🐿️ chipmunk journey starting at {ts}")
    print(f"   nodes: {len(NODES)}")
    print(f"   strategy: nearest-neighbor TSP (Dijkstra-greedy)")
    print()

    journal = []
    visited = set()
    distances = {}  # node_id -> measured latency to first endpoint
    total_checks = 0
    total_ok = 0
    route = []

    # First pass: measure distances (latency to each node's first endpoint)
    print("═══ MEASURING DISTANCES (Dijkstra phase) ═══")
    for node in NODES:
        ep = node["endpoints"][0]
        status, latency, note = check_endpoint(
            node["base"], ep["path"], ep["expect"],
            host=node.get("host"), headers=node.get("headers")
        )
        distances[node["id"]] = latency if status > 0 else 99999
        print(f"  {node['id']:20} → {latency:7.1f}ms {'✅' if status == ep['expect'] else '❌'}")

    print()
    print("═══ WALKING THE GRAPH (TSP nearest-neighbor) ═══")

    # Walk: always visit nearest unvisited node
    current = None
    while len(visited) < len(NODES):
        next_id = dijkstra_nearest(visited, distances)
        if next_id is None:
            break

        node = next(n for n in NODES if n["id"] == next_id)
        visited.add(next_id)
        route.append(next_id)
        
        print(f"\n  ┌─ visiting: {next_id} ({node['type']})")
        print(f"  │  base: {node['base']}")

        node_results = []
        for ep in node["endpoints"]:
            status, latency, note = check_endpoint(
                node["base"], ep["path"], ep["expect"],
                host=node.get("host"), headers=node.get("headers")
            )
            ok = status == ep["expect"]
            total_checks += 1
            if ok:
                total_ok += 1
            symbol = "✅" if ok else "❌"
            print(f"  │  {symbol} {ep['label']:25} → {status} ({latency:.0f}ms) {note if not ok else ''}")
            node_results.append({
                "label": ep["label"],
                "path": ep["path"],
                "status": status,
                "latency_ms": latency,
                "ok": ok,
            })

        journal.append({
            "node": next_id,
            "type": node["type"],
            "distance_ms": distances[next_id],
            "endpoints": node_results,
            "all_ok": all(r["ok"] for r in node_results),
        })
        print(f"  └─ {'all green ✅' if journal[-1]['all_ok'] else 'ISSUES FOUND ⚠️'}")

    # Summary
    print()
    print("═══ JOURNEY COMPLETE ═══")
    print(f"  route: {' → '.join(route)}")
    print(f"  nodes visited: {len(visited)}/{len(NODES)}")
    print(f"  checks: {total_ok}/{total_checks} ok ({100*total_ok/total_checks:.0f}%)")
    
    total_distance = sum(distances[nid] for nid in route if nid in distances)
    print(f"  total distance: {total_distance:.0f}ms")
    print(f"  avg per node: {total_distance/len(route):.0f}ms")

    # Euler check: can we walk every EDGE?
    edge_count = sum(len(n["endpoints"]) for n in NODES)
    print(f"  edges (endpoints): {edge_count}")
    print(f"  Euler circuit: {'possible' if all(len(n['endpoints']) % 2 == 0 for n in NODES) else 'not possible (odd-degree nodes)'}")

    # Hamilton check: did we visit every NODE exactly once?
    print(f"  Hamilton path: {'✅ yes' if len(visited) == len(NODES) else '❌ no'}")

    # π remainder of the journey
    import math
    pi_rem = (total_checks * math.pi) % 1
    print(f"  π remainder of journey: {pi_rem:.6f}")

    # Write journey state
    state = {
        "ts": ts,
        "strategy": "nearest-neighbor TSP (Dijkstra-greedy)",
        "route": route,
        "nodes_visited": len(visited),
        "nodes_total": len(NODES),
        "checks_ok": total_ok,
        "checks_total": total_checks,
        "health_pct": round(100 * total_ok / total_checks, 1),
        "total_distance_ms": round(total_distance, 1),
        "pi_remainder": round(pi_rem, 6),
        "journal": journal,
        "graph_science": {
            "dijkstra_1959": "shortest path, single source — used for distance measurement",
            "tsp_dantzig_1954": "visit all nodes, minimize total distance — the route",
            "euler_1736": "Königsberg bridges — can you walk every edge?",
            "hamilton_1857": "can you visit every node exactly once?",
            "nearest_neighbor": "greedy heuristic — always go to closest unvisited",
            "marathon": "you can't optimize a route you haven't run. run first. map second.",
        },
    }

    out_path = "/home/eastgate/Development/ecoPrimals/membrane/local-terminal/remote/chipmunk-journey.json"
    with open(out_path, "w") as f:
        json.dump(state, f, indent=2)
    print(f"\n  journal written: {out_path}")

    return state


if __name__ == "__main__":
    run_journey()
