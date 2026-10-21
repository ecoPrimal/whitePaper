#!/usr/bin/env python3
"""
chipmunk-journey.py — The Traveling Chipmunk

A graph-walking observer that visits every endpoint in the membrane,
measures distances (latency), builds an adjacency matrix, and finds
the nearest-neighbor tour. Then reports what it learned.

Named for Dijkstra, Bellman-Ford, Held-Karp, and every pioneer
who taught us that the shortest path through a graph is the one
you actually walk.

The traveling salesman doesn't solve TSP optimally.
The traveling salesman LEARNS THE GRAPH by walking it.
That's the point. The solution is the journey.
"""

import json
import time
import urllib.request
import urllib.error
import socket
import sys
import os
from datetime import datetime, timezone
from collections import defaultdict

# The graph — every touchable node in the membrane
NODES = {
    "primals.eco": {
        "url": "https://primals.eco/",
        "type": "cis",
        "feeds": [
            "/api/was.json",
            "/chipmunk.json",
            "/dashboard.json",
            "/membrane.json",
            "/negentropy.json",
            "/now.json",
            "/topology.json",
            "/scan_sweep_sort.json",
            "/five-o-five",
        ],
    },
    "hud.primals.eco": {
        "url": "https://hud.primals.eco/",
        "type": "cis-alias",
        "feeds": [],
    },
    "golgi-direct": {
        "url": "http://157.230.3.183/",
        "type": "trans",
        "feeds": [
            "/was.json",
            "/campfire.json",
            "/chipmunk.json",
        ],
    },
    "sporeprint-golgi": {
        "url": "http://157.230.3.183/",
        "host": "sporeprint.primals.eco",
        "type": "trans-sporeprint",
        "feeds": ["/atom.xml", "/llms.txt"],
    },
    "nestgate-golgi": {
        "url": "http://157.230.3.183/",
        "host": "nestgate.io",
        "type": "klein-touchpoint",
        "feeds": ["/campfire.json", "/chipmunk.json"],
    },
    "ntfy-membrane": {
        "url": "https://ntfy.sh/primals-membrane/json?poll=1&since=30m",
        "type": "neutrino",
        "feeds": [],
    },
    "ntfy-inbox": {
        "url": "https://ntfy.sh/primals-membrane-inbox/json?poll=1&since=30m",
        "type": "neutrino-inbox",
        "feeds": [],
    },
    "github-hud": {
        "url": "https://api.github.com/repos/ecoPrimal/hud/commits?per_page=1",
        "type": "nucleus",
        "feeds": [],
    },
    "github-sporeprint": {
        "url": "https://api.github.com/repos/ecoPrimal/sporePrint/commits?per_page=1",
        "type": "nucleus",
        "feeds": [],
    },
}


def visit(name, node):
    """Visit a node. Measure latency. Check feeds. Return observations."""
    url = node["url"]
    host = node.get("host")
    obs = {
        "node": name,
        "type": node["type"],
        "url": url,
        "latency_ms": None,
        "status": None,
        "alive": False,
        "feeds_checked": 0,
        "feeds_alive": 0,
        "feed_results": {},
        "error": None,
    }

    headers = {"User-Agent": "chipmunk/1.0 (traveling-salesman)"}
    if host:
        headers["Host"] = host

    try:
        req = urllib.request.Request(url, headers=headers)
        t0 = time.monotonic()
        with urllib.request.urlopen(req, timeout=8) as resp:
            t1 = time.monotonic()
            obs["latency_ms"] = round((t1 - t0) * 1000, 1)
            obs["status"] = resp.status
            obs["alive"] = resp.status == 200
            resp.read()
    except urllib.error.HTTPError as e:
        obs["status"] = e.code
        obs["error"] = str(e)
    except Exception as e:
        obs["error"] = str(e)[:120]

    # Check feeds
    base = url.rstrip("/")
    for feed_path in node.get("feeds", []):
        feed_url = base + feed_path
        freq = {"path": feed_path, "alive": False, "latency_ms": None}
        try:
            req = urllib.request.Request(feed_url, headers=headers)
            t0 = time.monotonic()
            with urllib.request.urlopen(req, timeout=8) as resp:
                t1 = time.monotonic()
                freq["latency_ms"] = round((t1 - t0) * 1000, 1)
                freq["alive"] = resp.status == 200
                body = resp.read()
                # Try to parse JSON for health info
                if feed_path.endswith(".json"):
                    try:
                        data = json.loads(body)
                        freq["has_data"] = bool(data)
                        if isinstance(data, dict):
                            freq["keys"] = list(data.keys())[:8]
                    except:
                        freq["has_data"] = len(body) > 0
        except Exception as e:
            freq["error"] = str(e)[:80]

        obs["feed_results"][feed_path] = freq
        obs["feeds_checked"] += 1
        if freq["alive"]:
            obs["feeds_alive"] += 1

    return obs


def nearest_neighbor_tour(distances, start):
    """
    Classic nearest-neighbor TSP heuristic.
    Dijkstra showed us shortest paths. This finds a greedy tour.
    Not optimal, but it LEARNS the graph by walking it.
    """
    nodes = list(distances.keys())
    if start not in nodes:
        return nodes, float("inf")

    unvisited = set(nodes)
    tour = [start]
    unvisited.remove(start)
    total = 0.0

    current = start
    while unvisited:
        # Find nearest unvisited
        best = None
        best_dist = float("inf")
        for n in unvisited:
            d = distances.get(current, {}).get(n, float("inf"))
            if d < best_dist:
                best_dist = d
                best = n
        if best is None:
            break
        tour.append(best)
        total += best_dist
        unvisited.remove(best)
        current = best

    # Return to start
    total += distances.get(current, {}).get(start, 0)
    tour.append(start)
    return tour, round(total, 1)


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"🐿️  chipmunk journey — {ts}")
    print(f"   visiting {len(NODES)} nodes in the membrane graph")
    print()

    observations = {}
    distances = defaultdict(dict)

    # Phase 1: Visit every node (Dijkstra's exploration)
    for name, node in NODES.items():
        print(f"  → {name}", end="", flush=True)
        obs = visit(name, node)
        observations[name] = obs

        status = "✅" if obs["alive"] else "❌"
        lat = f"{obs['latency_ms']}ms" if obs["latency_ms"] else "timeout"
        feeds = f"{obs['feeds_alive']}/{obs['feeds_checked']}" if obs["feeds_checked"] else "-"
        print(f"  {status} {lat}  feeds: {feeds}")

    # Phase 2: Build adjacency matrix (latency as distance)
    alive_nodes = [n for n, o in observations.items() if o["alive"]]
    for a in alive_nodes:
        for b in alive_nodes:
            if a != b:
                la = observations[a]["latency_ms"] or 9999
                lb = observations[b]["latency_ms"] or 9999
                distances[a][b] = (la + lb) / 2  # symmetric approx

    # Phase 3: Nearest-neighbor tour (the traveling salesman walks)
    if alive_nodes:
        start = "golgi-direct" if "golgi-direct" in alive_nodes else alive_nodes[0]
        tour, total_cost = nearest_neighbor_tour(distances, start)
    else:
        tour, total_cost = [], 0

    # Phase 4: Report
    print()
    print("  ═══ GRAPH STATE ═══")
    total_nodes = len(NODES)
    alive_count = len(alive_nodes)
    total_feeds = sum(o["feeds_checked"] for o in observations.values())
    alive_feeds = sum(o["feeds_alive"] for o in observations.values())
    print(f"  nodes: {alive_count}/{total_nodes} alive")
    print(f"  feeds: {alive_feeds}/{total_feeds} responding")
    print(f"  tour:  {' → '.join(tour)}")
    print(f"  cost:  {total_cost}ms (nearest-neighbor)")
    print()

    # Phase 5: Dijkstra insight
    if alive_nodes:
        fastest = min(alive_nodes, key=lambda n: observations[n]["latency_ms"] or 9999)
        slowest = max(alive_nodes, key=lambda n: observations[n]["latency_ms"] or 0)
        print(f"  fastest: {fastest} ({observations[fastest]['latency_ms']}ms)")
        print(f"  slowest: {slowest} ({observations[slowest]['latency_ms']}ms)")

    # Save journey state
    journey = {
        "ts": ts,
        "nodes_total": total_nodes,
        "nodes_alive": alive_count,
        "feeds_total": total_feeds,
        "feeds_alive": alive_feeds,
        "tour": tour,
        "tour_cost_ms": total_cost,
        "observations": {
            n: {
                "type": o["type"],
                "alive": o["alive"],
                "latency_ms": o["latency_ms"],
                "feeds": f"{o['feeds_alive']}/{o['feeds_checked']}",
            }
            for n, o in observations.items()
        },
    }

    # Write to known locations
    for path in [
        os.path.expanduser("~/Development/ecoPrimals/membrane/local-terminal/remote/journey.json"),
        os.path.expanduser("~/Development/membrane/local-terminal/remote/journey.json"),
    ]:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                json.dump(journey, f, indent=2)
        except:
            pass

    print()
    print("  the traveling chipmunk doesn't solve TSP.")
    print("  the traveling chipmunk LEARNS THE GRAPH by walking it.")
    print(f"  🐿️  journey complete — {alive_count} nodes, {alive_feeds} feeds, {total_cost}ms tour")

    return journey


if __name__ == "__main__":
    main()
