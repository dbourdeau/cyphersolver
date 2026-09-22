"""Homophonic annealer, second generation.

- Sukhotin split restricts each sign to the vowel or the consonant alphabet (can be relaxed with FREECLASS=1).
- coarse pass on an order-3/4 LM, polish on order-5.
- reheats inside each restart.
usage: CT=ct_p3.txt W=3 python solve3.py restarts iters
"""
import sys, os, json, random, math, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
import numpy as np
from solve import load_runs

MODEL = os.environ.get('MODEL', 'fr-1530-despatches')
COARSE = lm.load(MODEL, order=4, spaces=False)
FINE = lm.load(MODEL, order=5, spaces=False)
V = 'aeiou'
C = 'bcdfghlmnpqrstxy'


def sukhotin(runs, signs):
    idx = {s: i for i, s in enumerate(signs)}
    A = np.zeros((len(signs), len(signs)))
    for x in runs:
        for a, b in zip(x, x[1:]):
            A[idx[a], idx[b]] += 1; A[idx[b], idx[a]] += 1
    rho = A.sum(1).copy(); vow = set()
    for _ in range(len(signs)):
        i = int(np.argmax(rho))
        if rho[i] <= 0: break
        vow.add(signs[i]); rho = rho - 2 * A[i]; rho[i] = -1e9
    return vow


def main():
    R, IT = int(sys.argv[1]), int(sys.argv[2])
    runs = [r for r in load_runs() if len(r) >= 5]
    signs = sorted({s for r in runs for s in r})
    si = {s: i for i, s in enumerate(signs)}
    seq = [np.array([si[s] for s in r]) for r in runs]
    cnt = np.zeros(len(signs))
    for r in seq:
        for t in r: cnt[t] += 1
    vow = sukhotin(runs, signs)
    free_class = os.environ.get('FREECLASS')
    cand = [[FINE.encode(c)[0] for c in (V + C if free_class else (V if s in vow else C))] for s in signs]
    occ = [[j for j, r in enumerate(seq) if i in set(r.tolist())] for i in range(len(signs))]
    FR = dict(a=8.2, b=1.0, c=3.2, d=3.8, e=16.5, f=1.1, g=1.0, h=0.8, i=7.2, l=5.6, m=3.0,
              n=7.0, o=5.4, p=2.8, q=1.3, r=6.5, s=8.0, t=7.0, u=6.5, x=0.4, y=0.4)
    N = int(cnt.sum()); tot = sum(FR.values())
    exp = {FINE.encode(c)[0]: FR[c] / tot * N for c in FR}
    W = float(os.environ.get('W', '3'))
    print(len(signs), 'signs', N, 'tokens', len(vow), 'vowel signs', file=sys.stderr)

    def pen(obs):
        return sum((obs.get(a, 0) - e) ** 2 / e for a, e in exp.items())

    best_all = None
    for rs in range(R):
        M = COARSE
        key = np.array([random.choice(c) for c in cand])
        rsc = np.array([M.score_idx(key[r]) for r in seq])
        obs = collections.Counter()
        for i, k in enumerate(key): obs[int(k)] += cnt[i]
        cur = rsc.sum() - W * pen(obs); best = (cur, key.copy())
        for it in range(IT):
            frac = it / IT
            if frac > 0.6 and M is COARSE:
                M = FINE
                rsc = np.array([M.score_idx(key[r]) for r in seq])
                cur = rsc.sum() - W * pen(obs); best = (cur, key.copy())
            T = 2.5 * (1 - frac) + 0.02
            if it % 50000 == 49999: T = 2.0
            i = random.randrange(len(signs)); old = int(key[i]); nv = random.choice(cand[i])
            if nv == old: continue
            key[i] = nv
            js = occ[i]
            ns = np.array([M.score_idx(key[seq[j]]) for j in js])
            obs[old] -= cnt[i]; obs[nv] += cnt[i]
            new = rsc.sum() - rsc[js].sum() + ns.sum() - W * pen(obs)
            if new >= cur or random.random() < math.exp((new - cur) / max(T, 1e-6)):
                cur = new; rsc[js] = ns
                if cur > best[0]: best = (cur, key.copy())
            else:
                key[i] = old; obs[nv] -= cnt[i]; obs[old] += cnt[i]
        print('restart', rs, round(best[0], 1), file=sys.stderr)
        if best_all is None or best[0] > best_all[0]: best_all = best
    key = best_all[1]
    inv = {FINE.encode(c)[0]: c for c in V + C}
    mapping = {s: inv[int(key[i])] for i, s in enumerate(signs)}
    print(json.dumps(mapping, sort_keys=True))
    txt = [''.join(mapping[s] for s in r) for r in runs]
    print('per-char', round(sum(FINE.score(t) for t in txt) / max(1, sum(len(t) for t in txt)), 3))
    for t in txt: print(t)


if __name__ == '__main__':
    main()
