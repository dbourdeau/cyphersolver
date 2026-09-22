"""Hill-climb the R9412 key against word coverage (lexread), not against an n-gram score.

  python kaa4591/r9411/lexopt.py TRANSCRIPTION KEYFILE OUT [--sweeps 3] [--free 3,E,H,n,o,M,f,r,I,F,O,Q,a,+]

For every sign in --free (plus the polyphones, resolved per line), try each candidate value and keep it when
the share of characters that segment into real period words goes up. A substitution that turns a word into a
non-word can never be accepted, which is how the n-gram repairs went wrong.
"""
import argparse, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import lexread

ap = argparse.ArgumentParser()
ap.add_argument('file'); ap.add_argument('key'); ap.add_argument('out')
ap.add_argument('--sweeps', type=int, default=3)
ap.add_argument('--free', default='')
a = ap.parse_args()

KEY = dict(kv.split('=', 1) for kv in open(a.key, encoding='utf8').readline().split())
for _k, _v in [] : pass
FIXED = {'α': 'der', 'B': '', '&': 'und', 'Z': 'sch', 'R': 'h', 'K': 'rr', 'Y': 'll', 'S': 'g', 'X': 'x', '%': 'q', 'T': 'g', '^': 'g', 't': 'z', 'P': 'z'}
POLY = {'n': ['b', 'w', 'f', 'u'], '4': ['e', 'i'], 'E': ['d', 'ch'], 'H': ['u', 'v', 'k', 'g'],
        'o': ['s', 'b', ''], 'M': ['m', 'i']}
KEY.update({k: v for k, v in FIXED.items() if k not in KEY})
VALUES = list('abcdefghiklmnoprstuwz') + ['ch', 'sch', 'rr', 'll', 'er', '']

LINES = []
for l in open(a.file, encoding='utf8'):
    m = re.match(r'(\d+) (.*)', l.strip())
    if not m: continue
    toks = []
    for part in re.split(r'(\{[^}]*\})', m.group(2)):
        if part.startswith('{'): toks.append(('P', re.sub('[^a-z]', '', part.lower())))
        else: toks += [('C', t) for t in part.split() if t not in (':', '|', '?')]
    LINES.append((m.group(1), toks))

def render(key, poly):
    out = []
    for _, toks in LINES:
        s = ''
        for k, v in toks:
            if k == 'P': out.append(s); s = ''; continue
            s += poly.get(v, key.get(v, '?')).replace('_', '')
        out.append(s)
    return [x for x in out if x]

def cov(key, poly):
    tot = good = 0
    for part in render(key, poly):
        c, _ = lexread.coverage(part)
        good += c * len(part); tot += len(part)
    return good / max(tot, 1)

poly = {t: v[0] for t, v in POLY.items()}
for t in POLY:
    if t in KEY: poly[t] = KEY[t] if KEY[t] in POLY[t] else POLY[t][0]
base = cov(KEY, poly)
print(f'start coverage {base:.4f}', flush=True)
free = [t for t in (a.free.split(',') if a.free else []) if t]
for sweep in range(a.sweeps):
    improved = False
    for t in list(POLY):
        for v in POLY[t]:
            old = poly[t]
            if v == old: continue
            poly[t] = v; c = cov(KEY, poly)
            if c > base + 1e-6: base = c; improved = True; print(f'  poly {t} -> {v!r} {c:.4f}', flush=True)
            else: poly[t] = old
    for t in free:
        if t not in KEY: continue
        old = KEY[t]
        for v in VALUES:
            if v == old: continue
            KEY[t] = v; c = cov(KEY, poly)
            if c > base + 1e-6: base = c; old = v; improved = True; print(f'  key  {t} -> {v!r} {c:.4f}', flush=True)
            else: KEY[t] = old
    print(f'sweep {sweep}: {base:.4f}', flush=True)
    if not improved: break

open(a.out, 'w', encoding='utf8').write(' '.join(f'{k}={v}' for k, v in KEY.items()) + '\n' +
                                        '\n'.join(f'{n} {t}' for n, t in zip([l[0] for l in LINES], render(KEY, poly))) + '\n')
print('final coverage', round(base, 4))
