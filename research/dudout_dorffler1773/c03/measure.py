# -*- coding: utf-8 -*-
"""C03 dorffler-1686 — the SINGLE measure of PREREG-C03.md (frozen with it; do not edit after the PREREG hash).
Usage: python3 -I measure.py TABLE.json T476-cipher.txt G476-gloss.txt
- TABLE.json: {"<group>": "<plaintext string>", ...}; "" = null. A value may also be a list: the first item is used.
- T476-cipher.txt: blocks '@<id> ...' followed by 'C g g g ...' lines (other lines ignored). Groups: digits, with
  optional marks (dots ':' or '"'), '?' = unreadable, '?+' = lost groups.
- G476-gloss.txt: the same block ids, followed by 'G words ...' lines. A block with no G line is unglossed: excluded.
Score S = 1 - sum_b lev(D_b, G_b) / sum_b max(|D_b|, |G_b|) over glossed blocks b, after normalisation.
Controls: 500 tables = the frozen table with its values permuted at random among its keys (seed 20261112).
Pass (PREREG): S >= 0.75 AND S >= max(controls) + 0.30."""
import json, random, re, sys

def norm(s):
    s = s.lower()
    for a, b in (('ä', 'a'), ('ö', 'o'), ('ü', 'u'), ('ß', 'ss'), ('æ', 'ae'), ('ſ', 's')):
        s = s.replace(a, b)
    s = re.sub(r'[^a-z]', '', s)
    for a, b in (('j', 'i'), ('y', 'i'), ('v', 'u'), ('dt', 't'), ('th', 't'), ('ck', 'k'), ('tz', 'z'), ('c', 'k')):
        s = s.replace(a, b)
    return re.sub(r'(.)\1+', r'\1', s)

def lev(a, b):
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

def blocks(path, tag):
    out, cur = {}, None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('@'):
            cur = line[1:].split()[0]; out.setdefault(cur, [])
        elif line.startswith(tag + ' ') and cur:
            out[cur] += line[2:].split()
    return out

def decode(groups, table):
    s = []
    for g in groups:
        k = re.sub(r'[^0-9]', '', g)
        v = table.get(k) if k and '?' not in g else None
        if isinstance(v, list):
            v = v[0] if v else ''
        s.append('#' if v is None else norm(v))
    return ''.join(s)

def score(table, C, G):
    num = den = 0
    for b, words in G.items():
        if not words or b not in C:
            continue
        d, g = decode(C[b], table), norm(''.join(words))
        num += lev(d, g); den += max(len(d), len(g))
    return 1 - num / den if den else float('nan')

if __name__ == '__main__':
    table = {str(k): v for k, v in json.load(open(sys.argv[1], encoding='utf-8')).items() if not str(k).startswith('_')}
    C, G = blocks(sys.argv[2], 'C'), blocks(sys.argv[3], 'G')
    used = [b for b in G if G[b] and b in C]
    S = score(table, C, G)
    rng = random.Random(20261112); keys = sorted(table); vals = [table[k] for k in keys]; ctl = []
    for _ in range(500):
        rng.shuffle(vals); ctl.append(score(dict(zip(keys, vals)), C, G))
    ctl.sort(); mx = ctl[-1]
    ok = S >= 0.75 and S >= mx + 0.30
    print(json.dumps({'blocks_used': used, 'S': round(S, 4), 'ctl_max': round(mx, 4), 'ctl_median': round(ctl[250], 4),
                      'ctl_p99': round(ctl[494], 4), 'rank_above_all': S > mx, 'PASS': ok}, ensure_ascii=False))
