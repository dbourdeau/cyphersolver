"""Held-out check of the code table against the clear copy of the 4 Aug 1729 letter (PREREG.md).

The table is rebuilt from every ../transcription/sib*.txt except sib4aug_* (the repo's rule: most common firm
gloss per group). The 4 Aug code lines are read for their group numbers only. Each unit of
transcription/clear_4aug_brackets.tsv is aligned to its code lines; score = tokens that cover exactly their table
value / tokens with a table value. Null: 200 permuted tables, seed 1729.

    python3 -I scripts/check_4aug.py [--target ..]
Writes results/check_4aug_result.json and results/check_4aug_output.txt.
"""
import argparse
import collections
import glob
import json
import os
import random
import re
import unicodedata

TOKEN = re.compile(r'(\d+)(\??)=(\S+)')
GROUP = re.compile(r'(\{?)(\d+)\??=')
ALIAS = {'pourr': 'pour'}
MAXSPAN = 14
SEED = 1729
NSHUF = 200


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.translate(str.maketrans('jvyz', 'iuis'))
    return re.sub(r'[^a-z]', '', s)


def sib_files(target, keep):
    return [p for p in sorted(glob.glob(os.path.join(target, 'transcription', 'sib*.txt'))) if keep(os.path.basename(p))]


def build_table(paths):
    """group -> value, the repo's build_table.py rule (firm glosses preferred, most common value)."""
    seen = collections.defaultdict(list)
    for path in paths:
        for line in open(path, encoding='utf-8'):
            if not line.startswith('L'):
                continue
            rest = re.sub(r'\{[^}]*\}(=\S+)?', ' ', line.split(None, 1)[1])
            for m in TOKEN.finditer(rest):
                value = m.group(3)
                doubtful = bool(m.group(2)) or '?' in value
                seen[int(m.group(1))].append((value.strip('[]').lstrip('?'), doubtful))
    table = {}
    for g, occ in seen.items():
        firm = [v for v, d in occ if not d] or [v for v, _ in occ]
        table[g] = collections.Counter(ALIAS.get(v, v) for v in firm).most_common(1)[0][0]
    return table


def code_lines(target):
    """'sib4aug_60907:L01' -> list of (group, struck) from the 4 Aug files; glosses are not read."""
    out = {}
    for path in sib_files(target, lambda n: n.startswith('sib4aug_')):
        name = os.path.basename(path)[:-4]
        for line in open(path, encoding='utf-8'):
            if line.startswith('L'):
                label, rest = line.split(None, 1)
                out[f'{name}:{label}'] = [(int(m.group(2)), bool(m.group(1))) for m in GROUP.finditer(rest)]
    return out


def units(path):
    rows = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        unit, lines, page, text = line.rstrip('\n').split('\t')
        rows.append((unit, lines.split(','), page, text))
    return rows


def align(tokens, text, table):
    """tokens: list of (group, struck). Returns (matched, valued, per-token flags)."""
    s = norm(text)
    m = len(s)
    kinds = []
    for g, struck in tokens:
        v = None if struck else table.get(g)
        if v is not None and v.strip() == '_':
            kinds.append(('null', None))
        elif v is None:
            kinds.append(('wild', None))
        else:
            kinds.append(('val', norm(v)))
    NEG = -10 ** 9
    dp = [[NEG] * (m + 1) for _ in range(len(kinds) + 1)]
    back = [[None] * (m + 1) for _ in range(len(kinds) + 1)]
    dp[0][0] = 0
    for i, (kind, v) in enumerate(kinds, 1):
        for j in range(m + 1):
            best, arg = NEG, None
            if kind == 'null':
                best, arg = dp[i - 1][j], (j, 0)
            else:
                for k in range(0, min(MAXSPAN, j) + 1):
                    if dp[i - 1][j - k] > best:
                        best, arg = dp[i - 1][j - k], (j - k, 0)
                if kind == 'val' and v and len(v) <= j and s[j - len(v):j] == v and dp[i - 1][j - len(v)] + 1 > best:
                    best, arg = dp[i - 1][j - len(v)] + 1, (j - len(v), 1)
            dp[i][j], back[i][j] = best, arg
    flags, j = [], m
    for i in range(len(kinds), 0, -1):
        if back[i][j] is None:
            return 0, sum(1 for k, _ in kinds if k == 'val'), None
        pj, hit = back[i][j]
        flags.append((kinds[i - 1][0], hit, s[pj:j]))
        j = pj
    flags.reverse()
    return max(dp[-1][m], 0), sum(1 for k, _ in kinds if k == 'val'), flags


def run(table, rows, lines):
    matched = valued = 0
    detail = []
    for unit, names, _, text in rows:
        toks = [t for n in names for t in lines[n]]
        a, b, flags = align(toks, text, table)
        matched += a
        valued += b
        detail.append((unit, toks, a, b, flags))
    return matched, valued, detail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--target', default='..')
    ap.add_argument('--units', default='transcription/clear_4aug_brackets.tsv')
    ap.add_argument('--out', default='results')
    args = ap.parse_args()

    reduced = build_table(sib_files(args.target, lambda n: not n.startswith('sib4aug_')))
    full = build_table(sib_files(args.target, lambda n: True))
    lines = code_lines(args.target)
    rows = units(args.units)

    m, v, detail = run(reduced, rows, lines)
    score = m / v if v else 0.0
    rng = random.Random(SEED)
    groups = [g for g, val in reduced.items() if val != '_']
    values = [reduced[g] for g in groups]
    shuf = []
    for _ in range(NSHUF):
        perm = values[:]
        rng.shuffle(perm)
        t = dict(reduced)
        t.update(zip(groups, perm))
        sm, sv, _ = run(t, rows, lines)
        shuf.append(sm / sv if sv else 0.0)
    best, mean = max(shuf), sum(shuf) / len(shuf)
    fm, fv, fdetail = run(full, rows, lines)
    small = v < 30
    result = {
        'reduced_table_groups': len(reduced), 'full_table_groups': len(full),
        'units': len(rows), 'tokens': sum(len(d[1]) for d in detail),
        'tokens_with_value': v, 'matched': m, 'score': round(score, 4),
        'best_shuffled': round(best, 4), 'mean_shuffled': round(mean, 4), 'margin': round(score - best, 4),
        'pass': (not small) and score >= 0.85 and score - best >= 0.30, 'too_small': small,
        'full_table_check': {'tokens_with_value': fv, 'matched': fm, 'score': round(fm / fv, 4) if fv else None},
        'seed': SEED, 'n_shuffles': NSHUF,
    }
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, 'check_4aug_result.json'), 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=1, ensure_ascii=False)
        f.write('\n')
    with open(os.path.join(args.out, 'check_4aug_output.txt'), 'w', encoding='utf-8') as f:
        f.write('# check_4aug.py: reduced table (no 4 Aug glosses) aligned to the 4 Aug clear text, unit by unit.\n')
        f.write('# per token: group=value(table) -> letters covered, + = exact match, . = no match, ~ = no value, 0 = null\n')
        for (unit, toks, a, b, flags), (_, _, fa, fb, ff) in zip(detail, fdetail):
            f.write(f'\nunit {unit}: reduced {a}/{b}; full table {fa}/{fb}\n')
            for (g, struck), fl in zip(toks, flags or [None] * len(toks)):
                val = '{struck}' if struck else reduced.get(g, '-')
                mark = '~' if fl and fl[0] == 'wild' else '0' if fl and fl[0] == 'null' else '+' if fl and fl[1] else '.'
                f.write(f'  {g}={val} {mark} {fl[2] if fl else "?"}\n')
            misses = [f'{g}={full.get(g)}->{fl[2]}' for (g, _), fl in zip(toks, ff or []) if fl[0] == 'val' and not fl[1]]
            if misses:
                f.write('  full-table misses: ' + ' '.join(misses) + '\n')
    print({k: result[k] for k in ('tokens_with_value', 'matched', 'score', 'best_shuffled', 'mean_shuffled', 'margin', 'pass', 'too_small')})
    print('full table:', result['full_table_check'])


if __name__ == '__main__':
    main()
