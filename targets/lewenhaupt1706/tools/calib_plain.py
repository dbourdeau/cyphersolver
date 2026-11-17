"""N du clair authentique de L1 (déchiffrement d'époque 293, ajusté) et de ce clair bruité ; aussi held-out à faible bruit."""
import sys, os, json, random, statistics as st, re
sys.path.insert(0, os.path.dirname(__file__))
from ngram import LM, norm
from score2 import U
lm = LM(open('corpus_train.txt').read()); R = json.load(open('calib_UR.json'))['R']
N = lambda s: (sum(lm.ll(s)[0] for _ in [0]) / len(s) - U) / (R - U)
pl = ''.join(l for l in open('../../transcr/L1_plain_v2.txt', encoding='utf-8') if not l.startswith('#'))
pl = norm(re.sub(r'\(\?\)', '', pl)); print('L1 clair authentique : %d lettres N = %.3f' % (len(pl), N(pl)))
rng = random.Random(7); pool = open('corpus_heldout.txt').read().replace('\n', '')
for p in (0.02, 0.05, 0.08, 0.1, 0.15):
    v = [N(''.join(c if rng.random() > p else rng.choice(pool) for c in pl)) for _ in range(20)]
    print('L1 clair bruité p=%.2f : moy %.3f min %.3f max %.3f' % (p, st.mean(v), min(v), max(v)))
ho = [l for l in open('corpus_heldout.txt').read().split('\n') if l]
for p in (0.02, 0.05):
    v = [N(''.join(c if rng.random() > p else rng.choice(pool) for c in h)) for h in ho[:40]]
    print('held-out bruité p=%.2f : moy %.3f' % (p, st.mean(v)))
