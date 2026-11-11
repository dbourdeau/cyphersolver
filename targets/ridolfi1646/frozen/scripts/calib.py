# calib.py — calibration AVANT mesure, sur p. 1-4 SEULEMENT (la page 5 n'est jamais lue ici).
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import random, statistics as st
from decode import tokens
from cov import COV, shuffled_key, shuffled_groups, KEY
T = tokens((1, 2, 3, 4))
c, n = COV(T); rng = random.Random(1646)
R = [COV(T, shuffled_key(KEY, rng))[0] for _ in range(200)]
print('p1-4 in-sample : COV cle proposee %.3f (%d lettres) ; 200 cles melangees max %.3f moy %.3f' % (c, n, max(R), st.mean(R)))
L = 99; rows = []
for s in range(0, len(T) - L + 1, 24):
    w = T[s:s + L]; r = random.Random(s)
    cw = COV(w)[0]
    mk = max(COV(w, shuffled_key(KEY, r))[0] for _ in range(200))
    mg = max(COV(shuffled_groups(w, r))[0] for _ in range(200))
    rows.append((s, cw, mk, mg, cw - max(mk, mg)))
cs = sorted(r[1] for r in rows); ms = [max(r[2], r[3]) for r in rows]; gaps = sorted(r[4] for r in rows)
print('fenetres de %d groupes (pas 24) : %d cas' % (L, len(rows)))
print('  COV cle proposee : min %.3f p10 %.3f mediane %.3f max %.3f' % (cs[0], cs[len(cs) // 10], st.median(cs), cs[-1]))
print('  max temoin (200 cles + 200 melanges) : mediane %.3f max %.3f' % (st.median(ms), max(ms)))
print('  ecart COV - max temoin : min %.3f p10 %.3f mediane %.3f' % (gaps[0], gaps[len(gaps) // 10], st.median(gaps)))
for r in rows: print('  start %4d COV %.3f maxcle %.3f maxmel %.3f ecart %.3f' % r)
