"""Coverage-driven reading of R9412: per-occurrence polyphones, per-line evaluation.

Objective: share of characters that segment into words the period corpus has (lexread.coverage).
Moves: (1) each polyphone occurrence picks its own value; (2) each free sign's global value.
A move is kept only when line coverage improves, so a real word can never be traded for score.

  python kaa4591/r9411/lexopt2.py TRANSCRIPTION KEYFILE OUT [--sweeps 4] [--free a,b,c]
"""
import argparse, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import lexread

ap = argparse.ArgumentParser()
ap.add_argument('file'); ap.add_argument('key'); ap.add_argument('out')
ap.add_argument('--sweeps', type=int, default=4); ap.add_argument('--free', default='')
a = ap.parse_args()

FIXED = {'α': 'der', 'B': '', '&': 'und', 'Z': 'sch', 'R': 'h', 'K': 'rr', 'Y': 'll', 'S': 'g',
         'X': 'x', '%': 'q', 'T': 'g', '^': 'g', 't': 'z', 'P': 'z'}
POLY = {'n': ['b', 'w', 'f', 'u'], '4': ['e', 'i'], 'E': ['d', 'ch'], 'H': ['u', 'v', 'k', 'g'],
        'o': ['s', 'b', ''], 'M': ['m', 'i']}
VALUES = list('abcdefghiklmnoprstuwz') + ['ch', 'sch', 'rr', 'll', 'er', '']
KEY = dict(kv.split('=', 1) for kv in open(a.key, encoding='utf8').readline().split())
KEY.update({k: v for k, v in FIXED.items() if k not in KEY})

LINES = []
for l in open(a.file, encoding='utf8'):
    m = re.match(r'(\d+) (.*)', l.strip())
    if not m: continue
    toks = []
    for part in re.split(r'(\{[^}]*\})', m.group(2)):
        if part.startswith('{'): toks.append(['P', re.sub('[^a-z]', '', part.lower()), None])
        else: toks += [['C', t, (POLY[t][0] if t in POLY else None)] for t in part.split() if t not in (':', '|', '?')]
    LINES.append([m.group(1), toks])

def line_text(toks):
    out, s = [], ''
    for k, v, p in toks:
        if k == 'P': out.append(s); s = ''; continue
        s += (p if p is not None else KEY.get(v, '?')).replace('_', '')
    out.append(s)
    return [x for x in out if x]

def line_cov(toks):
    tot = good = 0
    for part in line_text(toks):
        c, _ = lexread.coverage(part); good += c * len(part); tot += len(part)
    return good, tot

def total():
    g = t = 0
    for _, toks in LINES:
        a_, b_ = line_cov(toks); g += a_; t += b_
    return g / max(t, 1)

print(f'start {total():.4f}', flush=True)
for sweep in range(a.sweeps):
    改 = 0
    for _, toks in LINES:
        cur, _ = line_cov(toks)
        for i, (k, v, p) in enumerate(toks):
            if k != 'C' or v not in POLY: continue
            best, bestv = cur, p
            for cand in POLY[v]:
                if cand == p: continue
                toks[i][2] = cand; g, _ = line_cov(toks)
                if g > best + 1e-9: best, bestv = g, cand
                toks[i][2] = p
            if bestv != p: toks[i][2] = bestv; cur = best; 改 += 1
    free = [t for t in a.free.split(',') if t]
    base = total()
    for t in free:
        if t not in KEY: continue
        old = KEY[t]; best, bestv = base, old
        for v in VALUES:
            if v == old: continue
            KEY[t] = v; c = total()
            if c > best + 1e-9: best, bestv = c, v
            KEY[t] = old
        if bestv != old:
            KEY[t] = bestv; base = best; 改 += 1; print(f'  key {t} -> {bestv!r} {best:.4f}', flush=True)
    print(f'sweep {sweep}: {total():.4f} ({改} moves)', flush=True)
    if not 改: break

with open(a.out, 'w', encoding='utf8') as f:
    f.write(' '.join(f'{k}={v}' for k, v in KEY.items()) + '\n')
    for n, toks in LINES:
        s = ''
        for k, v, p in toks:
            s += v.upper() if k == 'P' else (p if p is not None else KEY.get(v, '?')).replace('_', '')
        f.write(f'{n} {s}\n')
print('final', round(total(), 4))
