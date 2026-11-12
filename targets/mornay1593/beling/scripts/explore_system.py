"""Exploratory (not pre-registered): structure of the 1595-99 Duplessis/Lomenie figures.

Pools every passage of the repo's lomenie1595.txt and duplessis1597.txt (transcription/repo/), the Duplessis passages of
v7v8_figures.tsv and v9v12_figures.tsv, and the vol. 8 name code (v8_namecode.tsv). Prints, per source and pooled:
number ranges, the x10 codes and their positions, the commonest figures, repeated runs of 2-6 figures with where they
occur, and the first figure of each passage. No key is assumed. Usage, from beling/: python3 -I scripts/explore_system.py
"""
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def toks(field):
    return [t.strip('.,') for t in field.split() if t.strip('.,')]


def load():
    src = []  # (source, id, groups) ; groups keep editor letters as non-digits
    for name, gfield, keep in [('lomenie1595.txt', 2, 'LD'), ('duplessis1597.txt', 2, 'CW')]:
        for line in (HERE / 'transcription/repo' / name).read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#') or '|' not in line:
                continue
            f = [x.strip() for x in line.split('|')]
            if f[0][0] in keep:
                tag = 'Lomenie 1595' if f[0][0] == 'L' else 'Duplessis to wife 1595' if f[0] == 'D1' else \
                      'Duplessis to Cargroy Jan 1597' if f[0][0] == 'C' else 'Duplessis to wife Jan 1597'
                src.append((tag, f[0], toks(f[gfield])))
    for name, tag in [('v7v8_figures.tsv', 'Duplessis to wife 1597-98'), ('v9v12_figures.tsv', 'Duplessis to wife 1599')]:
        for line in (HERE / 'transcription' / name).read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#'):
                continue
            f = line.split('\t')
            if f[1] == 'Duplessis':
                src.append((tag, f[0], toks(f[6])))
    for line in (HERE / 'transcription/v8_namecode.tsv').read_text(encoding='utf-8').splitlines():
        if line.strip() and not line.startswith('#'):
            f = line.split('\t')
            if f[0] != 'N02':  # N02 = round 1 M8, already in v7v8
                src.append(('Duplessis to wife 1597-98', f[0], toks(f[4])))
    return src


def main():
    src = load()
    out = []
    bysrc = defaultdict(list)
    for tag, pid, gs in src:
        bysrc[tag].append((pid, gs))
    out.append('# Exploratory structure of the 1595-99 Duplessis/Lomenie figures (not pre-registered)\n')
    allnums = []
    for tag, items in bysrc.items():
        nums = [int(g) for _, gs in items for g in gs if g.isdigit()]
        allnums += nums
        x10 = [n for n in nums if n >= 200 and n % 10 == 0]
        big = [n for n in nums if n >= 200 and n % 10 != 0]
        out.append(f'## {tag}: {len(items)} passages, {len(nums)} groups, {len(set(nums))} distinct')
        out.append(f'   range {min(nums)}-{max(nums)}; <=130: {sum(1 for n in nums if n <= 130)}; 131-199: '
                   f'{sum(1 for n in nums if 131 <= n <= 199)}; >=200 ending 0: {len(x10)} {sorted(Counter(x10).items())}; '
                   f'>=200 other: {sorted(big)}')
        out.append('   commonest: ' + ', '.join(f'{k}x{v}' for k, v in Counter(nums).most_common(12)))
    out.append(f'\n## Pooled: {len(allnums)} groups, {len(set(allnums))} distinct')
    c = Counter(allnums)
    out.append('   commonest: ' + ', '.join(f'{k}x{v}' for k, v in c.most_common(25)))
    singles = sorted(k for k, v in c.items() if v == 1)
    out.append(f'   seen once: {len(singles)} figures')
    # x10 codes by position in passage
    pos = defaultdict(Counter)
    for tag, pid, gs in src:
        d = [g for g in gs if g.isdigit()]
        for i, g in enumerate(d):
            n = int(g)
            if n >= 200 and n % 10 == 0:
                p = 'alone' if len(d) == 1 else 'first' if i == 0 else 'last' if i == len(d) - 1 else 'inner'
                pos[n][p] += 1
    out.append('\n## x10 codes (>=200) by position in their passage')
    for n in sorted(pos):
        out.append(f'   {n}: ' + ', '.join(f'{k} {v}' for k, v in sorted(pos[n].items())))
    # repeated runs
    out.append('\n## Repeated runs of 2-6 figures (passages where they occur)')
    seen = defaultdict(set)
    for tag, pid, gs in src:
        d = [g for g in gs if g.isdigit()]
        for L in range(2, 7):
            for i in range(len(d) - L + 1):
                seen[tuple(d[i:i + L])].add(pid)
    rep = {k: v for k, v in seen.items() if len(v) >= 2}
    # keep maximal runs only
    keep = []
    for k, v in sorted(rep.items(), key=lambda kv: (-len(kv[0]), kv[0])):
        if any(len(k2) > len(k) and v2 >= v and any(k2[i:i + len(k)] == k for i in range(len(k2) - len(k) + 1)) for k2, v2 in keep):
            continue
        keep.append((k, v))
    for k, v in keep:
        out.append(f'   {" ".join(k)}: ' + ', '.join(sorted(v)))
    out.append('\n## First figure of each passage of 2+ groups (source: figure)')
    firsts = Counter()
    for tag, pid, gs in src:
        d = [g for g in gs if g.isdigit()]
        if len(d) >= 2:
            firsts[d[0]] += 1
    out.append('   ' + ', '.join(f'{k}x{v}' for k, v in firsts.most_common(15)))
    (HERE / 'results/explore_system.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
