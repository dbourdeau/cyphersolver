"""Word-aware beam decode: letter 5-gram (de-1500s, spaces) + word-unigram bonus LAM*log p(word) at each break.
Candidates per sign from a key JSON {sign: {value: p}} (or lists). Pruned to BEAM states.
  LAM=0.6 BEAM=3000 python wbeam.py key.json transcription.txt out.txt
"""
import re, sys, os, json, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm
M = lm.load('de-1500s', spaces=True)
k = M.order; A = M.A; idx = M.index; SPC = idx[' ']
W = json.load(open(os.path.join(os.path.dirname(__file__), 'de1500_words.json')))
N = sum(W.values()); LAM = float(os.environ.get('LAM', 0.6)); BEAM = int(os.environ.get('BEAM', 3000))
UNK = math.log(0.05 / N)
def wlp(w):
    c = W.get(w)
    return math.log(c / N) if c else UNK + (-1.5 * max(0, len(w) - 3))
P = {}
for w, c in W.items():
    for i in range(1, len(w) + 1): P[w[:i]] = P.get(w[:i], 0) + c
def PREF(p):
    c = P.get(p)
    return math.log(c / N) if c else UNK - 1.5 * len(p)
K = json.load(open(sys.argv[1], encoding='utf8')); K.pop('_pen', None)
CAND = {}
for g, v in K.items():
    if isinstance(v, dict):
        mx = max(v.values()); CAND[g] = [(c, -math.log(p / mx)) for c, p in v.items()]
    else:
        CAND[g] = [(c, 0.0 if j == 0 else 1.0) for j, c in enumerate(v)]
ALL = [(c, 3.0) for c in 'abcdefghiklmnoprstuwz']

def lp(ctx, ch):
    if len(ctx) < k - 1: return 0.0
    i = 0
    for c in ctx: i = i * A + c
    return float(M.lp[i * A + ch])

def decode(signs):
    states = {((SPC,), ''): (0.0, [])}
    for g in signs:
        new = {}
        for (ctx, wd), (s, out) in states.items():
            for cand, cost in CAND.get(g, ALL):
                for brk in (False, True):
                    sc = s - cost; c2 = ctx; w2 = wd
                    for ch in cand:
                        x = idx[ch]; sc += lp(c2, x); c2 = (c2 + (x,))[-(k - 1):]; w2 += ch
                    o = cand
                    if brk:
                        sc += lp(c2, SPC) + LAM * wlp(w2); c2 = (c2 + (SPC,))[-(k - 1):]; w2 = ''; o = cand + ' '
                    if len(w2) > 16: continue
                    key = (c2, w2)
                    if key not in new or new[key][0] < sc: new[key] = (sc, out + [o])
        states = dict(sorted(new.items(), key=lambda kv: -(kv[1][0] + (LAM * PREF(kv[0][1]) if kv[0][1] else 0)))[:BEAM])
    best = max(states.items(), key=lambda kv: kv[1][0] + (LAM * wlp(kv[0][1]) if kv[0][1] else 0))
    return best[1][1]

def tokens(s):
    s = re.sub(r'\{[^}]*\}', '', s).replace('a+', 'B').replace('o-', '%').replace('E+', 'Z').replace('ɔo', 'ɔ').replace('ꝏo', 'ꝏ')
    return re.sub(r'[-.:~?> ]', '', s)

lines = []
for l in open(sys.argv[2], encoding='utf8'):
    if l.startswith('=='): lines.append((l.strip(), None)); continue
    m = re.match(r'(\d\d) (.*)', l)
    if m: lines.append((m.group(1), tokens(m.group(2))))
res = []; buf = []; ALN = []
def flush():
    if not buf: return
    spans = [(no, re.split(r'(\[[^\]]*\])', s)) for no, s in buf]
    # decode each clear-text-delimited run separately
    outs = {}
    runs = []; cur = []
    for li, (no, parts) in enumerate(spans):
        for pi, p in enumerate(parts):
            if p.startswith('['): runs.append(cur); cur = []
            else: cur += [(li, pi, j, g) for j, g in enumerate(p)]
    runs.append(cur)
    for r in runs:
        if not r: continue
        o = decode([g for *_, g in r])
        for (li, pi, j, g), v in zip(r, o): outs[(li, pi, j)] = v; ALN.append((g, v))
    for li, (no, parts) in enumerate(spans):
        t = ''
        for pi, p in enumerate(parts):
            t += p if p.startswith('[') else ''.join(outs[(li, pi, j)] for j in range(len(p)))
        res.append(f'{no} {t}')
    buf.clear()
for no, s in lines:
    if s is None: flush(); res.append(no)
    else: buf.append((no, s))
flush()
txt = '\n'.join(res)
if len(sys.argv) > 3:
    open(sys.argv[3], 'w', encoding='utf8').write(txt + '\n')
    json.dump(ALN, open(sys.argv[3] + '.aln.json', 'w', encoding='utf8'))
print(txt)
