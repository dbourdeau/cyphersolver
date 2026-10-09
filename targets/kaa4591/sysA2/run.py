"""Learn a per-letter System A' key by EM and decode it with a word-aware beam.

  python run.py REC [--seed seeds.json] [--pool r9413,r9408] [--it 30] [--beam 1200] [--fix 'E=d/ch,n=w/b']
1. Tokens from sysA2/<rec>.tok (prep.py); runs split at '|' (clear text, F.G. and K code signs).
2. Baum-Welch on a letter-trigram HMM (de-1500s order 3, no spaces), emissions seeded from seeds.json (the
   improved R9407 key carried over by sign shape, augurelio1535/pass2/key.txt, plus the R9410 values);
   --pool adds other letters' tokens to the EM data (shared key assumed).
3. Word-aware beam (de-1500s order 5 with spaces + DTA word unigrams, as augurelio1535/work/wbeam.py) over each
   sign's EM candidates; digraph options (E/+/J = ch, B = rr) and the fixed signs (ʀ = und) added.
Writes <rec>_em.json and <rec>_dec.txt ('Pn.NN decrypt', [clear] and [F.G.]/[K] kept).
"""
import json, math, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..'))
from lang import lm

args = sys.argv[1:]
def opt(name, default):
    if name in args:
        i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
    return default
REC = args[0]
SEEDF = opt('--seed', os.path.join(HERE, 'seeds.json'))
POOL = [p for p in opt('--pool', '').split(',') if p]
IT = int(opt('--it', '30')); BEAM = int(opt('--beam', '1200')); LAM = float(opt('--lam', '0.6'))
OUT = opt('--out', REC)
LANG = opt('--lang', 'de')                          # 'la' for the Latin letter on R9410 ff.246-247
MODEL = 'de-1500s' if LANG == 'de' else 'la'
FIXED = {'ʀ': 'und', 'ꝁ': 'ck', 'ẽ': 'eur', 'Ä': 'auch'} if LANG == 'de' else {}
BREAK = {'ʀ'} if LANG == 'de' else set()                                     # word signs: run boundaries

def read_tok(rec):
    rows = []
    for l in open(os.path.join(HERE, rec + '.tok'), encoding='utf8'):
        m = re.match(r'(\S+) ?(.*)', l.rstrip('\n'))
        if m: rows.append((m.group(1), m.group(2)))
    return rows

def runs_of(rows):
    """yield runs of (line_index, position, sign); clear/code pieces are boundaries"""
    cur = []
    for li, (_, s) in enumerate(rows):
        pos = 0
        for piece in re.split(r'(\[[^\]]*\]|\|F\||\|K\||\|)', s):
            if not piece: continue
            if piece.startswith('[') or piece.startswith('|'):
                if cur: yield cur
                cur = []; continue
            for c in piece:
                if c == ' ': continue
                if c in BREAK:
                    if cur: yield cur
                    cur = []; continue
                cur.append((li, pos, c)); pos += 1
        # page break: lines are joined within a page (words run over line ends)
        if li + 1 < len(rows) and rows[li + 1][0].split('.')[0] != rows[li][0].split('.')[0]:
            if cur: yield cur
            cur = []
    if cur: yield cur

# ---------------- EM ----------------
M3 = lm.load(MODEL, order=3, spaces=False)
L = list(M3.alpha); A = len(L)
T3 = np.exp(M3.lp.reshape(A, A, A))
prior = np.exp(lm.load(MODEL, order=1, spaces=False).lp)[:A]; prior /= prior.sum()
seeds = json.load(open(SEEDF, encoding='utf8')); seeds.pop('_note', None)
rows = read_tok(REC)
seqs = [[c for *_, c in r] for r in runs_of(rows)]
for p in POOL: seqs += [[c for *_, c in r] for r in runs_of(read_tok(p))]
seqs = [s for s in seqs if len(s) >= 4]
signs = sorted({c for s in seqs for c in s}); S = {g: i for i, g in enumerate(signs)}
ALPHA_ = float(opt('--alpha', '0'))
EMONLY = '--emonly' in args
PRI = np.zeros((len(signs), A))                    # P(letter | sign) from the seeds, for the Dirichlet prior
for g in signs:
    sd = seeds.get(g, [])
    if isinstance(sd, dict):
        for c, p in sd.items():
            if len(c) == 1 and c in L: PRI[S[g], L.index(c)] += p
            elif c and c[0] in L: PRI[S[g], L.index(c[0])] += p * 0.5
    else:
        for j, c in enumerate(sd):
            if len(c) == 1 and c in L: PRI[S[g], L.index(c)] += 1.0 if j == 0 else 0.4
            elif c and c[0] in L: PRI[S[g], L.index(c[0])] += 0.3
    if PRI[S[g]].sum(): PRI[S[g]] /= PRI[S[g]].sum()
E = 0.02 + PRI.copy()
if '¿' in S: E[S['¿']] = 1.0
E /= E.sum(0, keepdims=True)
CNT = np.bincount([S[c] for s in seqs for c in s], minlength=len(signs)).astype(float)
UNKROW = S.get('¿')

def em_pass(E):
    num = np.zeros_like(E); ll = 0.0
    for s in seqs:
        o = [S[g] for g in s]; n = len(o)
        em = E[o]                                         # n x A
        al = np.zeros((n, A, A)); sc = np.zeros(n)
        a0 = prior * em[0]; z0 = a0.sum(); a0 /= z0
        a1 = a0[:, None] * prior[None, :] * em[1][None, :]   # first pair: weak bigram (prior)
        z = a1.sum(); al[1] = a1 / z; ll += math.log(z0) + math.log(z)
        for t in range(2, n):
            x = np.einsum('ab,abc->bc', al[t - 1], T3) * em[t][None, :]
            z = x.sum(); al[t] = x / z; ll += math.log(z)
        be = np.ones((A, A)); post = np.zeros((n, A))
        g = al[n - 1] * be; post[n - 1] = g.sum(0) / g.sum()
        for t in range(n - 1, 1, -1):
            # be_{t-1}(a,b) = sum_c T(a,b,c) em_t(c) be_t(b,c)
            be = np.einsum('abc,c,bc->ab', T3, em[t], be); be /= be.sum()
            g = al[t - 1] * be; post[t - 1] = g.sum(0) / g.sum()
        post[0] = a0 / a0.sum() if n < 2 else (al[1].sum(1) / al[1].sum())
        for t in range(n): num[o[t]] += post[t]
    return num, ll

for it in range(IT):
    num, ll = em_pass(E)
    E = num + 1e-3 + ALPHA_ * PRI * np.minimum(CNT, 50)[:, None] / 10.0
    if UNKROW is not None: E[UNKROW] = E.sum(0) / len(signs)
    E /= E.sum(0, keepdims=True)
    if it % 5 == 0 or it == IT - 1: print('em', it, round(ll, 1), flush=True)
Pls = E * prior[None, :]; Pls /= Pls.sum(1, keepdims=True)
key = {}
for g in signs:
    if g == '¿': continue
    key[g] = {L[j]: round(float(Pls[S[g], j]), 3) for j in np.argsort(-Pls[S[g]])[:4] if Pls[S[g], j] > 0.05}
DIGRAPH = {'E': ['ch'], '+': ['ch'], 'J': ['ch'], 'B': ['rr'], 'j': ['ch']}
for g, vs in DIGRAPH.items():
    if g in key:
        mx = max(key[g].values())
        for v in vs: key[g].setdefault(v, mx * 0.25)
json.dump(key, open(os.path.join(HERE, OUT + '_em.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
if EMONLY: sys.exit()

# ---------------- word beam ----------------
M = lm.load(MODEL, spaces=True)
k = M.order; AA = M.A; idx = M.index; SPC = idx[' ']
if LANG == 'de':
    W = json.load(open(os.path.join(HERE, '..', 'r9407', 'de1500_words.json'), encoding='utf8'))
    for f in ['../../augurelio1535/pass2/reading.txt']:
        for l in open(os.path.join(HERE, f), encoding='utf8'):
            if l.startswith('#'): continue
            for w in re.sub(r'\{[^}]*\}|\[[^\]]*\]|\|[^|]*\|', ' ', l.lower()).split()[1:]:
                w = re.sub(r'[^a-z]', '', w.replace('j', 'i').replace('v', 'u'))
                if len(w) > 2: W[w] = W.get(w, 0) + 20
    for w in open(os.path.join(HERE, 'vocab.txt'), encoding='utf8').read().splitlines():
        if w.startswith('#'): continue
        for x in w.split():
            x, _, c = x.partition(':'); W[x] = W.get(x, 0) + int(c or 50)
else:
    from collections import Counter as _C
    W = _C(lm.norm(open(os.path.join(HERE, '..', '..', '..', 'lang', 'corpora', 'la-gutenberg.txt'), encoding='utf8').read(), 'latin').split())
    W = {w: c for w, c in W.items() if c >= 2}
def _n(v): return v if LANG == 'de' else lm.norm(v, 'latin')
NW = sum(W.values()); UNK = math.log(0.05 / NW)
def wlp(w):
    c = W.get(w)
    return math.log(c / NW) if c else UNK - 1.5 * max(0, len(w) - 3)
PFX = {}
for w, c in W.items():
    for i in range(1, len(w) + 1): PFX[w[:i]] = PFX.get(w[:i], 0) + c
def pref(p):
    c = PFX.get(p)
    return math.log(c / NW) if c else UNK - 1.5 * len(p)
CAND = {}
for g, d in key.items():
    mx = max(d.values()); CAND[g] = [(_n(c), -math.log(p / mx)) for c, p in d.items() if _n(c) or not c]
for g, v in FIXED.items(): CAND[g] = [(v, 0.0)]
ALLC = [(c, 3.0) for c in ('abcdefghiklmnoprstuwz' if LANG == 'de' else 'abcdefghilmnopqrstux')]
LPM = M.lp
def lp(ctx, ch):
    if len(ctx) < k - 1: return 0.0
    i = 0
    for c in ctx: i = i * AA + c
    return float(LPM[i * AA + ch])

def decode(signs):
    states = {((SPC,), ''): (0.0, [])}
    for g in signs:
        new = {}
        for (ctx, wd), (s, out) in states.items():
            for cand, cost in CAND.get(g, ALLC):
                base = s - cost; c2 = ctx; w2 = wd
                for ch in cand:
                    x = idx[ch]; base += lp(c2, x); c2 = (c2 + (x,))[-(k - 1):]; w2 += ch
                if len(w2) <= 16:
                    key_ = (c2, w2)
                    if key_ not in new or new[key_][0] < base: new[key_] = (base, out + [cand])
                sc = base + lp(c2, SPC) + LAM * wlp(w2); c3 = (c2 + (SPC,))[-(k - 1):]
                key_ = (c3, '')
                if key_ not in new or new[key_][0] < sc: new[key_] = (sc, out + [cand + ' '])
        states = dict(sorted(new.items(), key=lambda kv: -(kv[1][0] + (LAM * pref(kv[0][1]) if kv[0][1] else 0)))[:BEAM])
    best = max(states.items(), key=lambda kv: kv[1][0] + (LAM * wlp(kv[0][1]) if kv[0][1] else 0))
    return best[1][1]

ROUNDS = int(opt('--rounds', '1'))
from collections import Counter, defaultdict
RUNS = list(runs_of(rows))
for rnd in range(ROUNDS):
    outs = {}; cnt = defaultdict(Counter)
    for r in RUNS:
        o = decode([c for *_, c in r])
        for (li, pos, c), v in zip(r, o): outs[(li, pos)] = v; cnt[c][v.strip()] += 1
    if rnd == ROUNDS - 1: break
    # Viterbi re-estimation: the beam's sign->value counts, smoothed towards the EM key
    for g, c in cnt.items():
        if g == '¿' or g in FIXED: continue
        n = sum(c.values()); em = key.get(g, {})
        d = {v: (c.get(v, 0) + 3 * em.get(v, 0)) / (n + 3) for v in set(c) | set(em)}
        d = {v: p for v, p in d.items() if p >= 0.04 and v}
        if not d: continue
        mx = max(d.values()); CAND[g] = [(v, -math.log(p / mx)) for v, p in d.items()]
        key[g] = {v: round(p, 3) for v, p in sorted(d.items(), key=lambda x: -x[1])}
    print('round', rnd, 'done', flush=True)
json.dump(key, open(os.path.join(HERE, OUT + '_key.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
res = []; lastp = None
for li, (name, s) in enumerate(rows):
    if name.split('.')[0] != lastp: lastp = name.split('.')[0]; res.append(f'== {lastp} ==')
    t = ''; pos = 0
    for piece in re.split(r'(\[[^\]]*\]|\|F\||\|K\||\|)', s):
        if not piece: continue
        if piece.startswith('['): t += ' ' + piece + ' '; continue
        if piece == '|F|': t += ' [F.G.] '; continue
        if piece == '|K|': t += ' [K] '; continue
        if piece == '|': continue
        for c in piece:
            if c == ' ': continue
            if c in BREAK: t += ' ' + FIXED[c] + ' '; continue
            t += outs.get((li, pos), '?'); pos += 1
    res.append(f'{name} ' + re.sub(r' +', ' ', t).strip())
open(os.path.join(HERE, OUT + '_dec.txt'), 'w', encoding='utf8').write('\n'.join(res) + '\n')
print('\n'.join(res[:12]))
