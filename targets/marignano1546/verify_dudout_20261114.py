"""Independent check of marignano1546 (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).
Reads only key.tsv, transcription_c13r.txt and reading_marked_c13r.txt (not scripts/decode.py or check_marks.py).
usage: python3 verify_dudout_20261114.py targets/marignano1546
"""
import sys, re, unicodedata, collections
T = sys.argv[1] if len(sys.argv) > 1 else '.'
key = collections.defaultdict(set)
for l in open(f'{T}/key.tsv', encoding='utf8'):
    if l.startswith('#') or l.startswith('sign\t') or not l.strip(): continue
    s, v = l.split('\t')[:2]
    for x in v.split('|'): key[s].add(x)
def strip(c): return ''.join(ch for ch in unicodedata.normalize('NFD', c.lower()) if ch.isalpha())
# transcription: per line, list of (sign, doubtful)
tr = {}
for l in open(f'{T}/transcription_c13r.txt', encoding='utf8'):
    if not re.match(r'M\d\d\t', l): continue
    lid, body = l.rstrip('\n').split('\t', 1)
    body = re.sub(r"\[[^\]]*\]", ' ', body)          # clear words
    toks = [t for t in re.split(r'[\s,/.:]+', body) if t]
    tr[lid] = [(t.rstrip('?'), t.endswith('?')) for t in toks]
# reading: tokens -> list of (letter or None for null, kind)
def units(r):
    r = re.sub(r'<<[^>]*>>', ' ', r)
    out = []; i = 0
    while i < len(r):
        c = r[i]
        if r.startswith('[eti', i):
            j = r.index(']', i); out.append(('[V. Ecc.a]', 'code')); i = j + 1; continue
        if c == '{':
            j = r.index('}', i); m = r[i+1:j]; i = j + 1
            if m == '-': out.append((None, 'null'))
            elif m.startswith('+'): out.append((strip(m[1:]), 'nosign'))
            elif m.startswith('?'): out.append((strip(m[1:]), 'doubt'))
            elif '/' in m: a, b = m.split('/'); out.append((strip(a), 'against:' + b))
            continue
        if c.isalpha():
            out.append((strip(c), 'plain'))
        i += 1
    return out
rd = {}
for l in open(f'{T}/reading_marked_c13r.txt', encoding='utf8'):
    if re.match(r'M\d\d\t', l):
        lid, body = l.rstrip('\n').split('\t', 1); rd[lid] = units(body)
tot = ok = 0; issues = []; two = collections.Counter(); picks = collections.defaultdict(collections.Counter)
for lid in sorted(tr):
    sig = list(tr[lid]); us = [u for u in rd[lid] if u[1] != 'nosign']
    if len(sig) != len(us):
        issues.append(f'{lid}: {len(sig)} signs vs {len(us)} reading units'); continue
    for (s, d), (let, kind) in zip(sig, us):
        tot += 1; vals = key.get(s)
        if vals is None: issues.append(f'{lid}: sign {s} not in key'); continue
        if kind == 'null':
            good = 'null' in vals
        elif kind == 'code':
            good = let in vals
        elif kind.startswith('against'):
            good = False
        else:
            good = let in vals
        if len(vals) > 1: two[s] += 1; picks[s][let] += 1
        if good: ok += 1
        else: issues.append(f'{lid}: sign {s}{"?" if d else ""} = {sorted(vals)} but reading has {let!r} ({kind})')
print(f'sign units {tot}; reading letter is a key value of its sign: {ok} ({ok/tot:.1%})')
for x in issues: print('  ', x)
print('two-valued sign names and the letters picked:')
for s in sorted(picks): print('  ', s, sorted(key[s]), dict(picks[s]))
