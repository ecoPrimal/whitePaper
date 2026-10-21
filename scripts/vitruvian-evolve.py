#!/usr/bin/env python3
"""vitruvian-evolve.py — feed the catalogue through Shannon + sigmoid
and watch it sort itself into evolutionary body plans.

banana → flatworm → jellyfish → millipede/spider/centipede → vertebrate

Just... see what happens.

Usage: python3 vitruvian-evolve.py [path]
"""

import os, sys, math, json
from collections import Counter, defaultdict
from pathlib import Path

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2

# ═══════════════════════════════════════════════════════════════
# SHANNON ENTROPY — information density of a file
# ═══════════════════════════════════════════════════════════════

def shannon(text):
    """Shannon entropy in bits per word."""
    words = text.lower().split()
    if not words:
        return 0.0
    freq = Counter(words)
    total = len(words)
    h = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            h -= p * math.log2(p)
    return h

def richness(text):
    """Vocabulary richness: unique words / total words."""
    words = text.lower().split()
    if not words:
        return 0.0
    return len(set(words)) / len(words)

# ═══════════════════════════════════════════════════════════════
# SIGMOID — the classification boundary
# smooth transition from 0 to 1
# ═══════════════════════════════════════════════════════════════

def sigmoid(x, midpoint=0.5, steepness=10.0):
    """Standard sigmoid centered at midpoint."""
    z = steepness * (x - midpoint)
    if z > 500: return 1.0
    if z < -500: return 0.0
    return 1.0 / (1.0 + math.exp(-z))

# ═══════════════════════════════════════════════════════════════
# EVOLUTIONARY STAGE CLASSIFIER
#
# Based on file properties:
#   - lines (bulk)
#   - shannon entropy (information density)
#   - richness (vocabulary diversity)
#   - type_count (enums + structs — the skeleton)
#   - function_count (the appendages)
#   - import_count (connections to other organisms)
#
# Stages:
#   BANANA:     single-purpose, low entropy, no types
#   FLATWORM:   has a head (main), bilateral, can regenerate
#   JELLYFISH:  nerve net, no skeleton, radial, event-driven
#   MILLIPEDE:  many segments, paired functions (get/set)
#   SPIDER:     few segments, specialized, exoskeleton (strong types)
#   CENTIPEDE:  many segments, one function each (Unix philosophy)
#   VERTEBRATE: internal skeleton (types inside), soft tissue wrapping
# ═══════════════════════════════════════════════════════════════

def classify_stage(props):
    lines = props.get('lines', 0)
    h = props.get('shannon', 0)
    r = props.get('richness', 0)
    types = props.get('types', 0)
    funcs = props.get('functions', 0)
    imports = props.get('imports', 0)
    lang = props.get('lang', '')

    # sigmoid features
    complexity = sigmoid(h / 12.0, 0.5, 8)       # 0-1 based on entropy
    skeleton = sigmoid(types / 20.0, 0.5, 6)      # 0-1 based on type count
    segmentation = sigmoid(funcs / 10.0, 0.5, 6)  # 0-1 based on function count
    connectivity = sigmoid(imports / 5.0, 0.5, 6)  # 0-1 based on imports

    # composite scores
    invertebrate = complexity * (1 - skeleton)     # complex but no internal skeleton
    vertebrate = complexity * skeleton             # complex WITH internal skeleton

    # classify
    if lines < 20 or h < 2.0:
        return 'banana', 0.0
    if lines < 100 and funcs <= 2 and types == 0:
        return 'flatworm', complexity
    if lang in ('js', 'html') and types == 0:
        if funcs > 10:
            return 'jellyfish', complexity
        return 'flatworm', complexity

    # invertebrate split: millipede vs spider vs centipede vs SPIDER
    if types == 0 or skeleton < 0.3:
        pair_ratio = funcs / max(lines / 50, 1)  # functions per ~50-line segment
        # spider: web-builder — imports/deps create a dependency web,
        # event-driven (callbacks, handlers, async), trap patterns (match/if chains)
        # Like the monkey's honeypot: the web catches, the spider processes
        has_web = imports > 5 and funcs > 3  # many imports = dependency web
        has_trap = complexity > 0.5 and pair_ratio > 0.8 and pair_ratio <= 1.5  # balanced but complex
        if has_web and has_trap:
            return 'spider', invertebrate       # web-builder, trap-setter, event-driven
        elif pair_ratio > 1.5:
            return 'millipede', invertebrate    # many paired functions
        elif funcs > 0 and lines / max(funcs, 1) > 100:
            return 'centipede', invertebrate    # few functions, each long
        else:
            return 'jellyfish', invertebrate    # nerve net, no clear segmentation

    # vertebrate: has internal skeleton (types)
    if vertebrate > 0.3:
        return 'vertebrate', vertebrate

    # default: flatworm (has structure but no clear category)
    return 'flatworm', complexity

# ═══════════════════════════════════════════════════════════════
# FILE SCANNER — extract properties from source files
# ═══════════════════════════════════════════════════════════════

LANG_MAP = {
    '.rs': 'rust', '.js': 'js', '.py': 'python', '.sh': 'shell',
    '.toml': 'toml', '.md': 'markdown', '.html': 'html'
}

SKIP = {'target', '.git', 'node_modules', '__pycache__'}

def scan_file(path):
    """Extract properties from a single file."""
    ext = path.suffix.lower()
    lang = LANG_MAP.get(ext, 'other')
    if lang == 'other':
        return None

    try:
        text = path.read_text(errors='replace')
    except Exception:
        return None

    lines_list = text.splitlines()
    num_lines = len(lines_list)
    if num_lines == 0:
        return None

    h = shannon(text)
    r = richness(text)

    # count language-specific features
    types = 0
    funcs = 0
    imports = 0

    if lang == 'rust':
        for line in lines_list:
            stripped = line.strip()
            if stripped.startswith('pub enum ') or stripped.startswith('enum '):
                types += 1
            elif stripped.startswith('pub struct ') or stripped.startswith('struct '):
                types += 1
            elif stripped.startswith('pub fn ') or stripped.startswith('fn ') or stripped.startswith('pub async fn '):
                funcs += 1
            elif stripped.startswith('use '):
                imports += 1
    elif lang == 'python':
        for line in lines_list:
            stripped = line.strip()
            if stripped.startswith('def '):
                funcs += 1
            elif stripped.startswith('class '):
                types += 1
            elif stripped.startswith('import ') or stripped.startswith('from '):
                imports += 1
    elif lang == 'js':
        for line in lines_list:
            stripped = line.strip()
            if 'function ' in stripped or stripped.startswith('var ') or stripped.startswith('const '):
                funcs += 1
    elif lang == 'shell':
        for line in lines_list:
            stripped = line.strip()
            if '()' in stripped and '{' in stripped:
                funcs += 1
            elif stripped.startswith('source ') or stripped.startswith('. '):
                imports += 1

    return {
        'path': str(path),
        'lang': lang,
        'lines': num_lines,
        'shannon': round(h, 3),
        'richness': round(r, 4),
        'types': types,
        'functions': funcs,
        'imports': imports,
    }

def should_skip(path):
    return any(part in SKIP for part in path.parts)

# ═══════════════════════════════════════════════════════════════
# MAIN — scan, classify, report
# ═══════════════════════════════════════════════════════════════

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    print(f"[vitruvian-evolve] scanning {root.resolve()}...")
    print()

    results = defaultdict(list)
    stage_counts = Counter()
    stage_lines = Counter()
    lang_stage = defaultdict(lambda: Counter())
    total_files = 0
    total_lines = 0

    for path in sorted(root.rglob('*')):
        if not path.is_file() or should_skip(path):
            continue
        props = scan_file(path)
        if props is None:
            continue

        stage, score = classify_stage(props)
        props['stage'] = stage
        props['score'] = round(score, 4)
        results[stage].append(props)
        stage_counts[stage] += 1
        stage_lines[stage] += props['lines']
        lang_stage[props['lang']][stage] += 1
        total_files += 1
        total_lines += props['lines']

    # ─── REPORT ───
    print(f"  TOTAL: {total_files:,} files, {total_lines:,} lines")
    print()

    # evolutionary stage distribution
    ORDER = ['banana', 'flatworm', 'jellyfish', 'centipede', 'millipede', 'spider', 'vertebrate']
    print("  ═══ EVOLUTIONARY STAGE DISTRIBUTION ═══")
    print()
    print(f"  {'STAGE':<12} {'FILES':>7} {'LINES':>12} {'% FILES':>8} {'% LINES':>8}")
    print(f"  {'─'*12} {'─'*7} {'─'*12} {'─'*8} {'─'*8}")
    for stage in ORDER:
        files = stage_counts.get(stage, 0)
        lines = stage_lines.get(stage, 0)
        pf = files / total_files * 100 if total_files else 0
        pl = lines / total_lines * 100 if total_lines else 0
        bar = '█' * int(pl / 2)
        print(f"  {stage:<12} {files:>7,} {lines:>12,} {pf:>7.1f}% {pl:>7.1f}% {bar}")
    print()

    # language × stage cross-table
    langs = ['rust', 'js', 'python', 'shell', 'toml', 'markdown', 'html']
    print("  ═══ LANGUAGE × STAGE (file counts) ═══")
    print()
    header = f"  {'LANG':<10}" + "".join(f"{s:>10}" for s in ORDER)
    print(header)
    print(f"  {'─'*10}" + "─"*10*len(ORDER))
    for lang in langs:
        row = f"  {lang:<10}"
        for stage in ORDER:
            c = lang_stage[lang].get(stage, 0)
            row += f"{c:>10}" if c else f"{'·':>10}"
            
        print(row)
    print()

    # biggest files per stage (the exemplars)
    print("  ═══ EXEMPLARS (biggest file per stage) ═══")
    print()
    for stage in ORDER:
        files = results.get(stage, [])
        if not files:
            continue
        top = sorted(files, key=lambda f: f['lines'], reverse=True)[:3]
        print(f"  {stage.upper()}:")
        for f in top:
            short = f['path'].replace(str(root) + '/', './')
            if len(short) > 60:
                short = '...' + short[-57:]
            print(f"    {f['lines']:>6} lines  H={f['shannon']:>5.1f}  R={f['richness']:.3f}  T={f['types']:>3}  F={f['functions']:>3}  {short}")
        print()

    # the split point: where does invertebrate become vertebrate?
    inv_lines = sum(stage_lines.get(s, 0) for s in ['jellyfish', 'centipede', 'millipede'])
    vert_lines = stage_lines.get('vertebrate', 0)
    ratio = inv_lines / vert_lines if vert_lines else float('inf')
    print(f"  ═══ THE SPLIT ═══")
    print(f"  Invertebrate (jellyfish + centipede + millipede): {inv_lines:>12,} lines")
    print(f"  Vertebrate:                                       {vert_lines:>12,} lines")
    print(f"  Ratio (inv/vert):                                 {ratio:>12.4f}")
    print(f"  π connection:                                     π = {PI:.4f}")
    print(f"  4π:                                               {4*PI:.4f}")
    print()

    # π-stability of stage counts
    print(f"  ═══ π-STABILITY OF STAGE COUNTS ═══")
    print()
    for stage in ORDER:
        n = stage_counts.get(stage, 0)
        if n == 0:
            continue
        divs = sum(1 for i in range(1, n+1) if n % i == 0)
        pi_rem = (n / PI) - int(n / PI)
        is_prime = divs == 2 and n > 1
        label = "PRIME ✓" if is_prime else f"{divs} divisors"
        print(f"  {stage:<12} n={n:>6}  divisors={divs:>3}  π-rem={pi_rem:.4f}  {label}")
    print()

    print("[vitruvian-evolve] done. the organism sorted itself.")

if __name__ == '__main__':
    main()
