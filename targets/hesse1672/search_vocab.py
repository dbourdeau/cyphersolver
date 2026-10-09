"""Escalation: align the open signs 28 83 117 20 66 [37 104] against every word of the period corpora
(DTA 1630-1670, 1720-1770, 1470-1610) of the form er..., ver..., ir..., ex..., ent... (participles).
Cost per sign: 0 if the key-255 value, 1 if an alphabet neighbour in the table (column slip) or a digit
look-alike value, 1 for a syllable sign in place of the 'bb' sign, 2 otherwise; insertions/deletions 2."""
import os, re, sys, collections
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from decrypt import NUM
C = os.path.join(here, '..', '..', 'lang', 'corpora')
def norm(w): return w.lower().replace('j','i').replace('v','u').replace('ä','a').replace('ö','o').replace('ü','u').replace('ß','ss').replace('ſ','s')
cnt = collections.Counter()
for fn in ('de-dta-1630-1670.txt', 'de-dta-1720-1770.txt', 'de-dta-1470-1610.txt'):
    p = os.path.join(C, fn)
    if os.path.exists(p):
        cnt.update(norm(w) for w in re.findall(r"[A-Za-zÄÖÜäöüßſ]+", open(p, encoding='utf-8', errors='ignore').read()))
ALPHA = 'abcdefghiklmnopqrstuwxyz'
def neigh(c):
    i = ALPHA.find(c); return {ALPHA[j] for j in (i-1, i+1) if 0 <= j < len(ALPHA)}
LOOK = {'1':'17','7':'172','2':'27','3':'358','5':'538','8':'8360','6':'608','0':'06','4':'49','9':'94'}
def look(tok):
    out=set()
    for i,ch in enumerate(tok):
        for a in LOOK.get(ch,ch):
            n=int(tok[:i]+a+tok[i+1:])
            if n in NUM: out.add(NUM[n])
    return out
SIG = [('28','e'),('83','r'),('117','t'),('20','a'),('66','d'),('37','i'),('104','n')]
SYL = ['au','mm','ch','st','tt','ll','ff']
def unit_cost(k, u):
    tok, v = SIG[k]
    if u == v: return 0
    if len(u) == 1 and (u in neigh(v) or u in look(tok)): return 1
    if k == 4 and u in SYL: return 1
    return 2 if len(u) == 1 else 9
def align(word, ksig):
    # DP over signs vs word letters, each sign emits 1 letter or (sign 4) a syllable
    INF = 99; n = len(word); D = [[INF]*(n+1) for _ in range(ksig+1)]; D[0][0] = 0
    for i in range(ksig+1):
        for j in range(n+1):
            if D[i][j] >= INF: continue
            if i < ksig:
                for L in (1, 2, 3):
                    if j+L <= n: D[i+1][j+L] = min(D[i+1][j+L], D[i][j] + unit_cost(i, word[j:j+L]))
                D[i+1][j] = min(D[i+1][j], D[i][j] + 2)
            if j < n: D[i][j+1] = min(D[i][j+1], D[i][j] + 2)
    return D[ksig][n]
res = []
for w, c in cnt.items():
    if c < 2 or not re.match(r'^(er|uer|ir|ex|ent|ert)', w) or not 4 <= len(w) <= 11: continue
    res.append((align(w, 5), -c, w, 5))
    res.append((align(w, 7), -c, w, 7))
res.sort()
for r in res[:40]: print(r[0], -r[1], r[2], 'signs:', r[3])
