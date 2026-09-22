"""Learn a polyphonic key P(sign | letter) by Baum-Welch on a letter-trigram HMM (de-1500s, no spaces),
seeded from a candidate file; write the emission table as JSON {sign: {letter: p}}.
  python em.py cands.json out.json trans1.txt [trans2.txt ...]
"""
import re, sys, os, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm

M3 = lm.load('de-1500s', order=3, spaces=False)
L = list(M3.alpha); A = len(L)
lp = M3.lp.reshape(A, A, A)                       # log P(c | a b)
T = np.exp(lp)                                   # trans from state (a,b) -> (b,c)

def tokens(s):
    s = re.sub(r'\{[^}]*\}', '', s).replace('a+', 'B').replace('o-', '%').replace('E+', 'Z').replace('ɔo', 'ɔ').replace('ꝏo', 'ꝏ')
    s = re.sub(r'\[[^\]]*\]', '|', s)
    return re.sub(r'[-.:~?> ]', '', s)

seqs = []
for f in sys.argv[3:]:
    cur = ''
    for l in open(f, encoding='utf8'):
        if l.startswith('=='):
            if cur: seqs.append(cur); cur = ''
            continue
        m = re.match(r'(\d\d) (.*)', l)
        if m: cur += tokens(m.group(2))
    if cur: seqs.append(cur)
seqs = [p for s in seqs for p in s.split('|') if len(p) > 5]
signs = sorted({g for s in seqs for g in s}); S = {g: i for i, g in enumerate(signs)}
C = json.load(open(sys.argv[1], encoding='utf8')); C.pop('_pen', None)
E = np.full((len(signs), A), 0.02)
for g in signs:
    cs = [c for c in C.get(g, []) if len(c) == 1 and c in L]
    for j, c in enumerate(cs): E[S[g], L.index(c)] += 1.0 if j == 0 else 0.4
E /= E.sum(0, keepdims=True)                     # columns: P(sign | letter)

prior = np.exp(lm.load('de-1500s', order=1, spaces=False).lp)
for it in range(int(os.environ.get('IT', 40))):
    num = np.zeros_like(E); tot_ll = 0
    for s in seqs:
        o = [S[g] for g in s]; n = len(o)
        # forward over pair states (a,b): alpha[t][a,b] = P(o_1..t, x_{t-1}=a, x_t=b)
        al = np.zeros((n, A, A))
        a0 = prior * E[o[0]]; a1 = (a0[:, None] * (prior[None, :])) * E[o[1]][None, :]
        al[1] = a1 / a1.sum(); cs = [np.log(a0.sum()), np.log(a1.sum())]
        for t in range(2, n):
            x = np.einsum('ab,abc->bc', al[t - 1], T) * E[o[t]][None, :]
            z = x.sum(); al[t] = x / z; cs.append(np.log(z))
        tot_ll += sum(cs)
        be = np.ones((A, A)); post = np.zeros((n, A))
        post[n - 1] = al[n - 1].sum(0)
        for t in range(n - 1, 1, -1):
            y = T * (E[o[t]] * be.sum(0) if False else (E[o[t]][None, None, :] * be[None, :, :]))
            be = y.sum(2); be /= be.sum()
            g = al[t - 1] * be; post[t - 1] = g.sum(0) / g.sum()
        post[0] = post[1]
        for t in range(n): num[o[t]] += post[t]
    E = num + 1e-3; E /= E.sum(0, keepdims=True)
    print(it, round(tot_ll, 1), flush=True)
# report P(letter | sign)
Pls = (E * prior[None, :]); Pls /= Pls.sum(1, keepdims=True)
out = {g: {L[j]: round(float(Pls[S[g], j]), 3) for j in np.argsort(-Pls[S[g]])[:4] if Pls[S[g], j] > 0.03} for g in signs}
json.dump(out, open(sys.argv[2], 'w', encoding='utf8'), ensure_ascii=False, indent=0)
for g in signs: print(g, out[g])
