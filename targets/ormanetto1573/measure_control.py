"""Control for measure.py: the same measure with the letter values shuffled (codes kept). Prints the share read for 20 shuffles."""
import random, measure as M, dec_aj as D
base = dict(D.KEY); letters = sorted(set(base.values())); random.seed(7); res = []
for _ in range(20):
    p = letters[:]; random.shuffle(p); mp = dict(zip(letters, p))
    D.KEY.clear(); D.KEY.update({k: mp[v] for k, v in base.items()})
    t, r, per, u = M.run('r116_cipher_v2.txt'); res.append(r / t)
D.KEY.clear(); D.KEY.update(base)
print('shuffled letter keys: mean %.1f%%, max %.1f%% (real key: see measure.py)' % (100*sum(res)/len(res), 100*max(res)))
