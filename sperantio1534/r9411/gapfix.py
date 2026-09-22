"""Close the unread spans of R9412 by searching the uncertain signs, span by span.

Method. Render the decrypt with each polyphone occurrence resolved by its n-gram context. Segment the text
against the period lexicon. Every chunk that is NOT a real word is a gap. For each gap, take the tokens that
produced it plus one token either side, and enumerate:
  - every combination of values for the polyphone occurrences in that span (n, 4, E, H, o, M), and
  - one shape-neighbour substitution for any one sign in the span.
A candidate is accepted only when the gap chunk becomes a word of >=4 letters that the corpus has, and the
neighbouring chunks stay words. A search that can only turn non-words into words cannot trade sense for score,
which is how the earlier score-driven repairs went wrong.

  python kaa4591/r9411/gapfix.py TRANSCRIPTION KEYFILE [--apply OUT]
"""
import argparse, itertools, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import lexread
from lang import lm

ap = argparse.ArgumentParser()
ap.add_argument('file'); ap.add_argument('key'); ap.add_argument('--apply', default='')
ap.add_argument('--maxpoly', type=int, default=7)
a = ap.parse_args()
M = lm.load('de-1500s', spaces=False)

FIXED = {'α': 'der', 'B': '', '&': 'und', 'Z': 'sch', 'R': 'h', 'K': 'rr', 'Y': 'll', 'S': 'g',
         'X': 'x', '%': 'q', 'T': 'g', '^': 'g', 't': 'z', 'P': 'z'}
POLY = {'n': ['b', 'w', 'f', 'u'], '4': ['e', 'i'], 'E': ['d', 'ch'], 'H': ['u', 'v', 'k', 'g'],
        'o': ['s', 'b', ''], 'M': ['m', 'i']}
NEIGH = {'3': 'E', 'E': '3', '9': 'g', 'g': '9', 'n': 'm7M', 'm': 'n7M', 'M': 'nm7', '7': 'nmM',
         'd': 'b6', 'b': 'd6', '6': 'db', 'q': 'c', 'c': 'q', 't': 'PT^', 'P': 'tT^', 'T': 'tP^',
         '^': 'tPT', 'x': '+', '+': 'x', 'A': 'D', 'D': 'A', 'L': 'l', 'l': 'L'}
KEY = dict(kv.split('=', 1) for kv in open(a.key, encoding='utf8').readline().split())
KEY.update({k: v for k, v in FIXED.items() if k not in KEY})

LINES = []
for l in open(a.file, encoding='utf8'):
    m = re.match(r'(\d+) (.*)', l.strip())
    if not m: continue
    toks = []
    for part in re.split(r'(\{[^}]*\})', m.group(2)):
        if part.startswith('{'): toks.append(['P', re.sub('[^a-z]', '', part.lower()), None])
        else: toks += [['C', t, None] for t in part.split() if t not in (':', '|', '?')]
    LINES.append([m.group(1), toks])

def val(tok, choice):
    if choice is not None: return choice
    return KEY.get(tok, '?').replace('_', '')

def render(toks):
    """returns text and, for each character, the index of the token that produced it"""
    s, owner = '', []
    for i, (k, v, c) in enumerate(toks):
        piece = v if k == 'P' else val(v, c)
        s += piece; owner += [i] * len(piece)
    return s, owner

# resolve polyphones by n-gram context
for _, toks in LINES:
    for i, (k, v, c) in enumerate(toks):
        if k != 'C' or v not in POLY: continue
        best, bestv = None, POLY[v][0]
        for cand in POLY[v]:
            toks[i][2] = cand; s, _ = render(toks)
            sc = M.score_idx(M.encode(s))
            if best is None or sc > best: best, bestv = sc, cand
        toks[i][2] = bestv

def isword(w, n=4):
    return len(w) >= n and w in lexread.LOGP

report = []
applied = []
for n, toks in LINES:
    text, owner = render(toks)
    if not text: continue
    words = lexread.segment(text)
    pos = 0
    for w in words:
        span = (pos, pos + len(w)); pos += len(w)
        if isword(w) or len(w) < 4: continue
        idx = sorted(set(owner[span[0]:span[1]]))
        if not idx: continue
        lo, hi = max(0, idx[0] - 1), min(len(toks) - 1, idx[-1] + 1)
        polys = [i for i in range(lo, hi + 1) if toks[i][0] == 'C' and toks[i][1] in POLY]
        if len(polys) > a.maxpoly: polys = polys[:a.maxpoly]
        saved = {i: toks[i][2] for i in polys}
        found = []
        combos = list(itertools.product(*[POLY[toks[i][1]] for i in polys])) if polys else [()]
        for combo in combos:
            for i, c in zip(polys, combo): toks[i][2] = c
            for sub in [None] + [(i, alt) for i in range(lo, hi + 1) if toks[i][0] == 'C'
                                 for alt in NEIGH.get(toks[i][1], '')]:
                old = None
                if sub: old = toks[sub[0]][1]; toks[sub[0]][1] = sub[1]
                t2, _ = render(toks)
                for cand in lexread.segment(t2):
                    if isword(cand, 5) and cand not in words:
                        found.append((cand, combo, sub))
                if sub: toks[sub[0]][1] = old
        for i, c in saved.items(): toks[i][2] = c
        if found:
            uniq = sorted({f[0] for f in found}, key=lambda x: -len(x))[:6]
            report.append((n, w, uniq))
            if a.apply:
                # keep the configuration that maximises strict word coverage of this line
                base_cov, _ = lexread.coverage(render(toks)[0])
                best = (base_cov, None, None)
                for cand, combo, sub in found:
                    for i, c in zip(polys, combo): toks[i][2] = c
                    old = None
                    if sub: old = toks[sub[0]][1]; toks[sub[0]][1] = sub[1]
                    cov, _ = lexread.coverage(render(toks)[0])
                    if cov > best[0] + 1e-9: best = (cov, combo, sub)
                    if sub: toks[sub[0]][1] = old
                    for i, c in saved.items(): toks[i][2] = c
                if best[1] is not None:
                    for i, c in zip(polys, best[1]): toks[i][2] = c
                    if best[2]: toks[best[2][0]][1] = best[2][1]
                    applied.append((n, w, round(best[0] - base_cov, 3)))

if a.apply:
    with open(a.apply, 'w', encoding='utf8') as f:
        for n, toks in LINES:
            txt = ''
            for k, v, c in toks:
                txt += v.upper() if k == 'P' else val(v, c)
            f.write(n + ' ' + txt + chr(10))
    print(f'applied {len(applied)} span fixes -> {a.apply}')
print(f'gaps examined: {len(report)}')
for n, w, cands in report:
    print(f'  line {n:>2}  {w:<18} -> {", ".join(cands)}')
