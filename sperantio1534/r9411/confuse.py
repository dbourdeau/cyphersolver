"""Per-occurrence transcription repair for R9412.

For each cipher token, try only the tokens whose SHAPE is confusable with it (the classes below, drawn from
the look-alikes noted on the images), and keep a substitution when it improves the language model by more
than --margin nats. Emulates a human re-checking a doubtful glyph, but bounded: only shape-neighbours, only
big improvements, and a cap on how many tokens may change.

  python kaa4591/r9411/confuse.py TRANSCRIPTION KEYFILE OUT [--margin 2.0] [--cap 0.06]
"""
import argparse, re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm

# shape neighbours only, from the sign inventory: 3 / reversed-3; 9 / gamma; pi / m / m-gamma / small 7;
# delta / lollipop / 6; square / open square; the three cross forms; x / cross; A / triangle; L / tall stroke.
CLASSES = [
    set('3E'), set('9g'), set('nmM7'), set('db6'), set('qc'), set('tPT^'), set('x+'), set('AD'), set('Ll'),
]
NB = {}
for cl in CLASSES:
    for a in cl:
        NB.setdefault(a, set()).update(cl - {a})

ap = argparse.ArgumentParser()
ap.add_argument('file'); ap.add_argument('key'); ap.add_argument('out')
ap.add_argument('--model', default='de-1500s'); ap.add_argument('--margin', type=float, default=2.0)
ap.add_argument('--cap', type=float, default=0.06)
a = ap.parse_args()
M = lm.load(a.model, spaces=False)
KEY = dict(kv.split('=', 1) for kv in open(a.key, encoding='utf8').readline().split())
POLY = {'n': 'bwfu', '4': 'ei', 'E': 'dc', 'H': 'uvkg', 'o': 'sb', 'M': 'mi'}
FIXED = {'α': 'der', 'B': '', '&': 'und', 'Z': 'sch', 'R': 'h', 'K': 'rr', 'Y': 'll', 'S': 'g', 'X': 'x', '%': 'q'}
KEY.update({k: v for k, v in FIXED.items() if k not in KEY})

def val(t, ctx_left='', ctx_right=''):
    if t not in KEY and t not in POLY: raise SystemExit('no key value for token ' + t)
    if t in POLY:
        return max(POLY[t], key=lambda v: M.score_idx(M.encode(ctx_left[-8:] + v + ctx_right[:8])))
    return KEY.get(t, '?').replace('_', '')

LINES = []
for l in open(a.file, encoding='utf8'):
    m = re.match(r'(\d+)\s+(.*)', l.strip())
    if not m: continue
    toks = []
    for part in re.split(r'(\{[^}]*\})', m.group(2)):
        if part.startswith('{'): toks.append(('P', re.sub('[^a-z]', '', part.lower())))
        else: toks += [('C', t) for t in part.split() if t not in (':', '|', '?')]
    LINES.append([m.group(1), toks])

def render(lines):
    out = []
    for _, toks in lines:
        s = ''
        for k, v in toks:
            s += v if k == 'P' else val(v, s, '')
        out.append(s)
    return out

def score_all(lines):
    return sum(M.score_idx(M.encode(t)) for t in render(lines))

base = score_all(LINES)
ntok = sum(1 for _, ts in LINES for k, _ in ts if k == 'C')
budget = int(ntok * a.cap)
changes = []
for li, (n, toks) in enumerate(LINES):
    for ti, (k, t) in enumerate(toks):
        if k != 'C' or t not in NB or len(changes) >= budget: continue
        cur = M.score_idx(M.encode(render([LINES[li]])[0]))
        best, bestv = 0.0, None
        for alt in NB[t]:
            if alt not in KEY and alt not in POLY: continue
            toks[ti] = ('C', alt)
            s = M.score_idx(M.encode(render([LINES[li]])[0]))
            if s - cur > best: best, bestv = s - cur, alt
            toks[ti] = ('C', t)
        if bestv and best > a.margin:
            toks[ti] = ('C', bestv); changes.append((n, ti, t, bestv, round(best, 2)))
print(f'tokens {ntok}  budget {budget}  changes {len(changes)}  score {base:.0f} -> {score_all(LINES):.0f}')
for c in changes: print('  line', c[0], 'pos', c[1], f'{c[2]} -> {c[3]} (+{c[4]})')
with open(a.out, 'w', encoding='utf8') as f:
    for n, toks in LINES:
        f.write(n + ' ' + ' '.join(v if k == 'C' else '{' + v + '}' for k, v in toks) + '\n')
