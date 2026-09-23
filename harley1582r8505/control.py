"""Control: encipher real French with a 50-sign homophonic key of the same shape as R8505,
then run the same annealer. Tells solver weakness apart from transcription noise.

usage: python control.py [tokens] [restarts] [iters] [noise]
noise = fraction of signs randomly replaced, to imitate transcription error.
"""
import sys, os, random, math, json, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
import numpy as np

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3600
R = int(sys.argv[2]) if len(sys.argv) > 2 else 8
IT = int(sys.argv[3]) if len(sys.argv) > 3 else 400000
NOISE = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0

COARSE = lm.load('fr-1530-despatches', order=4, spaces=False)
FINE = lm.load('fr-1530-despatches', order=5, spaces=False)

# plaintext: a chunk of the corpus itself is too easy to find; use a held-out slice of the raw corpus
corp = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lang', 'corpora',
                         'fr-henri4.txt'), encoding='utf-8', errors='replace').read()
plain = lm.norm(corp, 'early').replace(' ', '')
start = len(plain) // 3
plain = plain[start:start + N]

FR = dict(a=8.2, b=1.0, c=3.2, d=3.8, e=16.5, f=1.1, g=1.0, h=0.8, i=7.2, l=5.6, m=3.0,
          n=7.0, o=5.4, p=2.8, q=1.3, r=6.5, s=8.0, t=7.0, u=6.5, x=0.4, y=0.4)
NSIGN = 50
# homophones roughly proportional to letter frequency, as a 16th-c. clerk would build them
letters = sorted(FR)
share = {c: max(1, round(FR[c] / sum(FR.values()) * NSIGN)) for c in letters}
key = {}
i = 0
for c in letters:
    for _ in range(share[c]):
        key.setdefault(f's{i}', c); i += 1
signs_of = collections.defaultdict(list)
for s, c in key.items(): signs_of[c].append(s)
ct = [random.choice(signs_of[c]) for c in plain if c in signs_of]
if NOISE:
    allsigns = list(key)
    ct = [random.choice(allsigns) if random.random() < NOISE else s for s in ct]
print(f'control: {len(ct)} tokens, {len(key)} signs, noise {NOISE}', file=sys.stderr)

# same search as solve3.py
runs = [ct[i:i + 60] for i in range(0, len(ct), 60)]
signs = sorted(set(ct)); si = {s: i for i, s in enumerate(signs)}
seq = [np.array([si[s] for s in r]) for r in runs]
cnt = np.zeros(len(signs))
for r in seq:
    for t in r: cnt[t] += 1
A = np.zeros((len(signs), len(signs)))
for r in runs:
    for a, b in zip(r, r[1:]):
        A[si[a], si[b]] += 1; A[si[b], si[a]] += 1
rho = A.sum(1).copy(); vow = set()
for _ in range(len(signs)):
    j = int(np.argmax(rho))
    if rho[j] <= 0: break
    vow.add(signs[j]); rho = rho - 2 * A[j]; rho[j] = -1e9
V, C = 'aeiou', 'bcdfghlmnpqrstxy'
cand = [[FINE.encode(c)[0] for c in (V if s in vow else C)] for s in signs]
occ = [[j for j, r in enumerate(seq) if i in set(r.tolist())] for i in range(len(signs))]
exp = {FINE.encode(c)[0]: FR[c] / sum(FR.values()) * len(ct) for c in FR}
W = float(os.environ.get('W', '3'))
T0 = float(os.environ.get('T0', '2.5')); TEND = float(os.environ.get('TEND', '0.02'))
if os.environ.get('FREECLASS'):
    cand = [[FINE.encode(c)[0] for c in (V + C)] for s in signs]
true = {s: key[s] for s in signs}


def pen(obs):
    return sum((obs.get(a, 0) - e) ** 2 / e for a, e in exp.items())


best_all = None
for rs in range(R):
    M = COARSE
    k = np.array([random.choice(c) for c in cand])
    rsc = np.array([M.score_idx(k[r]) for r in seq])
    obs = collections.Counter()
    for i, v in enumerate(k): obs[int(v)] += cnt[i]
    cur = rsc.sum() - W * pen(obs); best = (cur, k.copy())
    for it in range(IT):
        frac = it / IT
        if frac > 0.6 and M is COARSE:
            M = FINE; rsc = np.array([M.score_idx(k[r]) for r in seq])
            cur = rsc.sum() - W * pen(obs); best = (cur, k.copy())
        T = T0 * (1 - frac) + TEND
        if it % 50000 == 49999: T = T0 * 0.5
        i = random.randrange(len(signs)); old = int(k[i]); nv = random.choice(cand[i])
        if nv == old: continue
        k[i] = nv; js = occ[i]
        ns = np.array([M.score_idx(k[seq[j]]) for j in js])
        obs[old] -= cnt[i]; obs[nv] += cnt[i]
        new = rsc.sum() - rsc[js].sum() + ns.sum() - W * pen(obs)
        if new >= cur or random.random() < math.exp((new - cur) / max(T, 1e-6)):
            cur = new; rsc[js] = ns
            if cur > best[0]: best = (cur, k.copy())
        else:
            k[i] = old; obs[nv] -= cnt[i]; obs[old] += cnt[i]
    print('restart', rs, round(best[0], 1), file=sys.stderr)
    if best_all is None or best[0] > best_all[0]: best_all = best

k = best_all[1]
inv = {FINE.encode(c)[0]: c for c in V + C}
got = {s: inv[int(k[i])] for i, s in enumerate(signs)}
right = sum(1 for s in signs if got[s] == true[s])
dec = ''.join(got[s] for s in ct)
ref = ''.join(true[s] for s in ct)
charok = sum(1 for a, b in zip(dec, ref) if a == b) / len(ref)
print(f'signs correct {right}/{len(signs)}  characters correct {charok:.3f}')
print('plain :', ref[:120])
print('solved:', dec[:120])
