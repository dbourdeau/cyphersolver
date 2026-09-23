"""Homophonic substitution annealer for the Harley 1582 ff. 263-264 memoir cipher.

Reads ct_p*.txt (signs column), drops dot tokens ':' and numbers '#nn' (kept as segment breaks),
maps every sign to one letter, scores with the shared French LM (no spaces).
usage: python solve.py [restarts] [iters] [fixed.json]
"""
import sys, os, glob, json, random, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
M = lm.load('fr-1530-despatches', order=5, spaces=False)


def load_runs():
    runs = []
    for fn in sorted(glob.glob(os.path.join(HERE, os.environ.get('CT','ct_p*.txt')))):
        for line in open(fn, encoding='utf-8', errors='replace'):
            if line.startswith('#') or '|' not in line:
                continue
            parts = [p.strip() for p in line.split('|')]
            if len(parts) < 3:
                continue
            seg = []
            for t in ' : '.join(parts[2::2]).replace('/', ' ').split():
                t = t.rstrip('?')
                if t in (':', '.', '..', ':2', ':3', ':4', '::'):
                    seg.append('DOT'); continue
                if not t or t.startswith('#') or t == '-':
                    if seg: runs.append(seg); seg = []
                    continue
                seg.append(t.split('/')[0])
            if seg: runs.append(seg)
    return runs


LET = 'abcdefghilmnopqrstuxyz'


def main():
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    IT = int(sys.argv[2]) if len(sys.argv) > 2 else 60000
    fixed = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}
    runs = load_runs()
    signs = sorted({s for r in runs for s in r})
    si = {s: i for i, s in enumerate(signs)}
    seq = [np.array([si[s] for s in r]) for r in runs if len(r) >= 2]
    print(len(signs), 'signs,', sum(len(r) for r in seq), 'tokens in', len(seq), 'runs', file=sys.stderr)
    alpha = [M.encode(c)[0] for c in LET]
    free = [i for i, s in enumerate(signs) if s not in fixed]

    FR = dict(a=8.2,b=1.0,c=3.2,d=3.8,e=16.5,f=1.1,g=1.0,h=0.8,i=7.2,l=5.6,m=3.0,n=7.0,o=5.4,p=2.8,q=1.3,r=6.5,s=8.0,t=7.0,u=6.5,x=0.4,y=0.4,z=0.2)
    tot = sum(FR.values()); N = sum(len(r) for r in seq)
    exp = {M.encode(c)[0]: FR[c] / tot * N for c in LET}
    cnt = np.zeros(len(signs)); 
    for r in seq:
        for t in r: cnt[t] += 1
    W = float(os.environ.get('W', '2'))

    def score(key):
        lp = sum(M.score_idx(key[r]) for r in seq)
        obs = {}
        for i, k in enumerate(key): obs[int(k)] = obs.get(int(k), 0) + cnt[i]
        pen = sum((obs.get(a, 0) - e) ** 2 / e for a, e in exp.items())
        return lp - W * pen

    occ = [[j for j, r in enumerate(seq) if i in set(r.tolist())] for i in range(len(signs))]

    def pen_of(obs):
        return sum((obs.get(a, 0) - e) ** 2 / e for a, e in exp.items())

    best_all = None
    for rs in range(R):
        key = np.array([M.encode(fixed[s])[0] if s in fixed else random.choice(alpha) for s in signs])
        rsc = np.array([M.score_idx(key[r]) for r in seq])
        obs = {}
        for i, k in enumerate(key): obs[int(k)] = obs.get(int(k), 0) + cnt[i]
        cur = rsc.sum() - W * pen_of(obs); best = (cur, key.copy())
        for it in range(IT):
            T = 3.0 * (1 - it / IT) + 0.05
            i = random.choice(free); old = int(key[i]); nv = random.choice(alpha)
            if nv == old: continue
            key[i] = nv
            js = occ[i]; ns = np.array([M.score_idx(key[seq[j]]) for j in js])
            obs[old] -= cnt[i]; obs[nv] = obs.get(nv, 0) + cnt[i]
            new = rsc.sum() - rsc[js].sum() + ns.sum() - W * pen_of(obs)
            if new >= cur or random.random() < math.exp((new - cur) / T):
                cur = new; rsc[js] = ns
                if cur > best[0]: best = (cur, key.copy())
            else:
                key[i] = old; obs[nv] -= cnt[i]; obs[old] += cnt[i]
        print('restart', rs, round(best[0], 1), file=sys.stderr)
        if best_all is None or best[0] > best_all[0]: best_all = best
    key = best_all[1]
    inv = {M.encode(c)[0]: c for c in LET}
    mapping = {s: inv[int(key[i])] for i, s in enumerate(signs)}
    print(json.dumps(mapping, sort_keys=True))
    for r in runs:
        print(''.join(mapping[s] for s in r))


if __name__ == '__main__':
    main()
