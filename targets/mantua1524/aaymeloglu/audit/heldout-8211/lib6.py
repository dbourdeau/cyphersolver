"""Shared loader / decoder for the anneal6 round.

Units: cipher signs with selected pairs merged (MERGE, overridable by env MERGE='mi,oo,...').
Reserved control lines (RESERVED.md) are dropped unless include_reserved=True.
"""
import csv, os, json, collections, itertools

HERE = '/Users/aaymeloglu/.claude-assistant/research/unsolved-ciphers/mantua-1524/'
FILES = ['transcription.tsv', 'transcription-68r.tsv', 'transcription-198r.tsv']
DEFAULT_MERGE = 'mi,oo,cc,dd,bb,lo,no,pa,la,bo,mo,gr,g1,bu'  # io dropped (broke 'i oo'); la, bo, mo, gr, g1 added 2026-11-15, see DECISIONS.md
RESERVE = {('68r', '20'), ('68r', '21'), ('68r', '22'), ('68r', '23')}
CODE = {'BOX', 'IZ', 'H', 'CROSS', 'C@'}


def merges():
    spec = os.environ.get('MERGE', DEFAULT_MERGE)
    return [(p[0], p[1:]) if len(p) == 2 else tuple(p.split('+')) for p in spec.split(',') if p]


def signs(text):
    return [x.split('{')[0].rstrip('?') for x in text.split() if x != '.']


def units(text, merge=None):
    merge = merges() if merge is None else merge
    t = signs(text)
    m, i = [], 0
    while i < len(t):
        if i + 1 < len(t) and (t[i], t[i + 1]) in merge:
            m.append(t[i] + t[i + 1]); i += 2
        else:
            m.append(t[i]); i += 1
    return m


def rows(include_reserved=False):
    for f in FILES:
        for r in csv.DictReader((l for l in open(HERE + f) if not l.startswith('#')), delimiter='\t'):
            if not include_reserved and (r['leaf'], r['line']) in RESERVE:
                continue
            yield r


def runs(include_reserved=False, skip_code=True, raised=False):
    out = []
    for r in rows(include_reserved):
        if r['kind'] != 'cipher' and not (raised and r['kind'] == 'raised'):
            continue
        u = units(r['text'])
        if skip_code:
            u = [x for x in u if x not in CODE]
        if u:
            out.append(u)
    return out


def load_key(path):
    k = json.load(open(path))
    if isinstance(k, list):
        k = k[0]['map']
    out = {}
    for s, v in k.items():
        if s.startswith('_'):
            continue  # metadata (_about, _merges)
        v = v.get('value') if isinstance(v, dict) else v
        if v:
            out[s] = v  # null = no reading; dec() then shows [sign]
    return out


def dec(us, key, upper=True):
    s = ''.join(key.get(x, '[' + x + ']') if x not in CODE else '[' + x + ']' for x in us)
    return s.upper() if upper else s
