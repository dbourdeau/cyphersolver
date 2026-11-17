"""Calibration de la métrique n-grammes AVANT gel (n'utilise pas L3).
usage: calib.py <key.json> <workdir>"""
import sys, os, json, random, statistics as st, time
sys.path.insert(0, os.path.dirname(__file__))
from ngram import LM, ALPHA
from score2 import *
key = json.load(open(sys.argv[1], encoding='utf-8')); W = sys.argv[2]
t0 = time.time(); lm = LM(open(os.path.join(W, 'corpus_train.txt')).read())
ho = [l for l in open(os.path.join(W, 'corpus_heldout.txt')).read().split('\n') if l]
Ls = [score(lm, [h]) for h in ho]; R = st.mean(Ls)
print('train s', round(time.time()-t0), 'U', round(U, 3), 'R(held-out moyen)', round(R, 3), 'min', round(min(Ls), 3), 'max', round(max(Ls), 3))
N = lambda L: (L - U) / (R - U)
rng = random.Random(1)
print('held-out N : min %.3f moy %.3f' % (min(map(N, Ls)), st.mean(map(N, Ls))))
rnd = ''.join(rng.choice(ALPHA) for _ in range(2000)); print('aléatoire uniforme N %.3f' % N(score(lm, [rnd])))
sh = list(ho[0]); rng.shuffle(sh); print('held-out mélangé (unigrammes) N %.3f' % N(score(lm, [''.join(sh)])))
# bruit : remplacer une part p des lettres d'un texte authentique par des lettres tirées selon les fréquences
pool = ''.join(ho)
for p in (0.1, 0.2, 0.3, 0.4, 0.5):
    vals = []
    for h in ho[:30]:
        s = ''.join(c if rng.random() > p else rng.choice(pool) for c in h); vals.append(N(score(lm, [s])))
    print('held-out bruité p=%.1f : N moy %.3f min %.3f' % (p, st.mean(vals), min(vals)))
T = '../transcr/'; H = '../../transcr/'
sets = {'L1a(286-287)': [H+'A_286_p1.txt', H+'A_287_p1.txt'], 'L1b(289-290)': [H+'A_289_p1.txt', H+'A_290_p1.txt'],
        'L1c(292-293)': [H+'A_292_p1.txt', H+'A_293_p1.txt'], 'L2(295-297)': [H+'A_295_p1.txt', H+'A_296L_p1.txt', H+'A_296R_p1.txt', T+'A_297_p1.txt'],
        'L4(310-311)': [H+'H/A_310_p1.txt', H+'H/A_311L_p1.txt', H+'H/A_311R_p1.txt']}
ctr = permuted_keys(key, 200, 20261117)
for name, fs in sets.items():
    fs = [os.path.join(W, f) for f in fs]; runs = read_runs(fs); ng = sum(map(len, runs)); unk = sum(1 for r in runs for c in r if c not in key)
    sK = N(score(lm, decode(runs, key))); cs = [N(score(lm, decode(runs, k))) for k in ctr]
    print('%-14s groupes %4d inconnus %.2f  N(K) %.3f  témoins moy %.3f max %.3f' % (name, ng, unk/ng, sK, st.mean(cs), max(cs)))
json.dump({'U': U, 'R': R}, open(os.path.join(W, 'calib_UR.json'), 'w'))
