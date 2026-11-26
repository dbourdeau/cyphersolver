#!/usr/bin/env python3
"""Plan alternative A1 (PLAN.md), run late on 23 Nov 2026 after the review: keyword-mixed alphabets.
Keywords = MURCIELAGO + every corpus word of 5-15 letters seen >= 3 times. Alphabet = keyword without repeats
+ remaining letters in order. Two directions, 26 offsets each:
  dir1: cipher = MIX[(std_index(plain)+s) % 26]   (mixed alphabet as cipher row)
  dir2: plain  = MIX[(std_index(cipher)+s) % 26]  (mixed alphabet as plain row)
Scored with the same 4-gram model; also counts agreement with the recovered key.
Run: python3 -I with numpy on the path, e.g.
  PYTHONPATH=$(python3 -c 'import site;print(site.getusersitepackages())') python3 -I keyword_test.py <scripts dir>
"""
import sys, json
sys.path.insert(0, sys.argv[1])
from solve import *
from run_controls import cipher, T1P

REC = dict(zip("BCDEFGLMNOPQRSTUVWXYZ", "USQPMLGFWVEDYCTBONARI"))  # recovered key, cipher -> plain

def mixed(w):
    seen = []
    for ch in w + A:
        if ch not in seen: seen.append(ch)
    return ''.join(seen)

if __name__ == '__main__':
    lp, wl, n, wc = build_model()
    c = cipher(T1P); ci = to_int(c)
    words = sorted({w for w, k in wc.items() if 5 <= len(w) <= 15 and k >= 3} | {'MURCIELAGO'})
    best = []
    for w in words:
        M = mixed(w)
        for s in range(26):
            k1 = [0] * 26   # dir1 inverse: cipher letter -> plain
            for p in range(26): k1[A.index(M[(p + s) % 26])] = p
            k2 = [A.index(M[(x + s) % 26]) for x in range(26)]
            for d, k in (('dir1', k1), ('dir2', k2)):
                karr = np.array(k)
                sc = score_int(karr[ci], lp)
                agree = sum(1 for cc, pp in REC.items() if A[k[A.index(cc)]] == pp)
                best.append((sc, w, s, d, agree, ''.join(A[v] for v in karr[ci])))
    best.sort(key=lambda x: -x[0])
    maxagree = max(best, key=lambda x: x[4])
    out = dict(n_keywords=len(words), n_alphabets=len(best), free_solve_T1_score=-2490.93,
               top10=[dict(score=round(b[0], 2), keyword=b[1], offset=b[2], direction=b[3], agree_with_recovered_of_21=b[4], dec=b[5][:60]) for b in best[:10]],
               max_agreement=dict(score=round(maxagree[0], 2), keyword=maxagree[1], offset=maxagree[2], direction=maxagree[3], agree=maxagree[4], dec=maxagree[5][:60]))
    json.dump(out, open(OUT + '/runs/keyword_test.json', 'w'), indent=1, ensure_ascii=False)
    print(json.dumps(out, indent=1, ensure_ascii=False))
