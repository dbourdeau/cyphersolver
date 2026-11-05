"""Held-out power test for one-label-at-a-time value inference on f. 139 (run from the repository root).
All labels with a table value keep it, except one label X; X takes each letter of the pool in turn, the rest of the free labels
sit at their start value. For a matched label X, does the argmax equal its table value (and by what margin)?
Pool 'letters' = 20 letters; pool 'all' adds table syllables."""
import os, sys, collections
sys.path.insert(0, os.getcwd()); sys.path.insert(0, 'targets/tranchedini1446')
import solver2 as S
runs = S.load_runs(); fixed, free = S.build(runs)
mp0 = dict(fixed); mp0.update({t: free[t][0] for t in free}); mp0['?'] = ''
cnt = collections.Counter(t for r in runs for t in r)
def margins(t, pool, base):
    sc = {}
    for v in pool:
        mp = dict(base); mp[t] = v; sc[v] = S.score(runs, mp)
    o = sorted(sc, key=sc.get, reverse=True)
    return o[0], sc[o[0]] - sc[o[1]], o[:3]
for pool_name, pool in (('letters', S.LET), ('all', S.POOL)):
    ok = tot = 0; rows = []
    for t in [x for x, _ in cnt.most_common() if x in fixed and x not in S.WORD and len(fixed[x]) <= 2][:25]:
        b = dict(mp0); b.pop(t)
        best, mg, top3 = margins(t, pool, dict(mp0))
        tot += 1; ok += best == fixed[t]; rows.append((t, fixed[t], best, round(mg * 1000), cnt[t]))
    print(pool_name, ok, '/', tot, rows)
