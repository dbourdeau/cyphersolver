# ÉTALONNAGE (Avenant 2 §4) : sur l'apprentissage hors V seulement, clé b contre 200 permutations.
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lm import *
E_SCANS = ['0017', '0062', '0071', '0072', '0080', '0081', '0086', '0087', '0088']
ns = []
for s in E_SCANS:
    for p in read_releve(os.path.join(REL, f'T-{s}.txt')):
        for lid, toks, g in p['lines']: ns += [v for k, v in toks if k == 'n']
Kb = load_key('KEY-W1717b.tsv'); M = LM(); L2 = make_L2()
R = {'groupes_E': len(ns)}
for name, f in (('L1', M.L1), ('L2', L2), ('L3', M.L3)):
    R[name] = {k: round(v, 4) for k, v in stats(f, Kb, ns).items()}
ok = [n for n in ('L1', 'L2', 'L3') if R[n]['gap'] > 0]
best = max(ok, key=lambda n: R[n]['z']) if ok else None
R['retenu'] = best if best and R[best]['z'] >= 4 else None
json.dump(R, open(os.path.join(D, 'ETALONNAGE.json'), 'w'), ensure_ascii=False, indent=1)
print(json.dumps(R, ensure_ascii=False))
