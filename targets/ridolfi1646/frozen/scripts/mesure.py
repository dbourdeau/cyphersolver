# mesure.py — MESURE UNIQUE sur la page 5 de D.107 (réserve jamais décodée). Ne pas relancer.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hashlib, random, statistics as st
from decode import ROOT, KEY, tokens, lines, dec_tok
from cov import COV, shuffled_key, shuffled_groups

# 1. vérification du gel
for l in open(os.path.join(ROOT, 'FREEZE.sha256')):
    if l.startswith('#') or not l.strip(): continue
    h, f = l.split(None, 1); f = f.strip()
    got = hashlib.sha256(open(os.path.join(ROOT, f), 'rb').read()).hexdigest()
    if got != h: sys.exit('GEL ROMPU : %s' % f)
print('gel verifie (FREEZE.sha256)')

# 2. décodage brut de p5
print('--- decodage brut p5 (cle gelee, aucune correction) ---')
for li, ts in lines(5):
    print('5.%02d\t%s' % (li, '·'.join(dec_tok(t) for t in ts)))

# 3. mesure
T = tokens((5,))
c, n = COV(T)
rk = random.Random(5); RK = [COV(T, shuffled_key(KEY, rk))[0] for _ in range(200)]
rg = random.Random(5); RG = [COV(shuffled_groups(T, rg))[0] for _ in range(200)]
print('p5 : %d groupes, %d lettres decodees' % (len(T), n))
print('COV cle proposee = %.3f' % c)
print('200 cles melangees : max %.3f moy %.3f' % (max(RK), st.mean(RK)))
print('200 melanges des groupes : max %.3f moy %.3f' % (max(RG), st.mean(RG)))
C1 = c >= 0.75; C2 = c >= max(RK) + 0.25; C3 = c >= max(RG) + 0.08
print('C1 COV>=0.75 : %s ; C2 COV>=maxcles+0.25 (%.3f) : %s ; C3 COV>=maxmelanges+0.08 (%.3f) : %s'
      % (C1, max(RK) + 0.25, C2, max(RG) + 0.08, C3))
print('MESURE :', 'VALIDE' if (C1 and C2 and C3) else ('PARTIEL' if C1 and (C2 or C3) else 'ECHEC'))
