"""H3: each run of digits is the jummal sum of a whole word (wordfreq vocabulary + colophon names)."""
import math, re, sys, heapq
from wordfreq import top_n_list, word_frequency
sys.path.insert(0, '.')
from wordsum import AB, VOC
def norm(w): return re.sub('[ً-ْـ]', '', w)
V = {}
for w in top_n_list('ar', 40000):
    n = norm(w)
    if len(n) < 2 or any(c not in AB for c in n): continue
    V.setdefault(str(sum(AB[c] for c in n)), []).append((word_frequency(w, 'ar'), n))
for w in VOC: V.setdefault(str(sum(AB.get(c,0) for c in w)), []).append((1e-3, w))
for k in V: V[k] = sorted(set(V[k]), reverse=True)[:8]
def best(s, K=30):
    beams = {0: [(0.0, [])]}
    for i in range(len(s)):
        for sc, ws in beams.get(i, []):
            for L in range(1, 5):
                t = s[i:i+L]
                if len(t) < L or t not in V or t[0] == '0': continue
                beams.setdefault(i+L, []).append((sc + math.log10(V[t][0][0]) + 1.5*L, ws+[t]))
        for j in beams: beams[j] = heapq.nlargest(K, beams[j], key=lambda x: x[0])
    return beams.get(len(s), [])
LTR = "71589217218921518421924"
for sc, ws in best(LTR)[:12]:
    print("%.1f" % sc, ' | '.join(t + ':' + '/'.join(w for f, w in V[t][:5]) for t in ws))
