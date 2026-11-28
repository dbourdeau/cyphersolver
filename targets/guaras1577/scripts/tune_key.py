"""Tune each sign's value on the build lines only: for every sign, try its four most frequent aligned values and keep
the one that gives the best in-sample per-sign score (part 1 + part 2), two passes. Writes build/key_1577_final.json.
Metric normalisation as in the protocol: PLAN.md 2.2 plus the two OCR classes c=e and l=t."""
import json, os, sys
sys.path.insert(0, 'scripts')
os.environ.setdefault('TSPLIT', '1')
from build_key import p1, p2, U
import measure_lib as M
TR = {'y': 'i', 'f': 's', 'e': 'c', 't': 'l'}
f = lambda x: ''.join(TR.get(c, c) for c in x)
K = json.load(open('build/key_1577.json'))
key = {s: v['plain'] for s, v in K['key'].items() if '+' not in s}
cands = {s: [v['plain']] + list(v['others'])[:3] for s, v in K['key'].items() if '+' not in s and v['aligned'] >= 3}
U2 = [u if len(u) > 1 else f(u) for u in U]; sp = K['plain_spans_used']
parts = [([t for _, _, t in p1], U2[sp['part1'][0]:sp['part1'][1]]), ([t for _, _, t in p2], U2[sp['part2'][0]:sp['part2'][1]])]
def total(k):
    k2 = {s: f(v) for s, v in k.items()}; r = s_ = 0
    for toks, ref in parts:
        a, b, _ = M.score(toks, k2, ref); r += a; s_ += b
    return r / s_
best = total(key); print('start', round(best, 4))
for rnd in range(2):
    for s in sorted(cands, key=lambda x: -K['key'][x]['aligned']):
        for v in cands[s]:
            if v == key[s]: continue
            old = key[s]; key[s] = v; sc = total(key)
            if sc > best + 1e-9: best = sc; print(rnd, s, old, '->', v, round(sc, 4))
            else: key[s] = old
json.dump({'_about': K['_about'] + ' Values tuned on build lines only (scripts/tune_key.py).', 'key': key,
           'codes': K['codes'], 'heldout_reference_units': K['heldout_reference_units'],
           'plain_spans_used': K['plain_spans_used'], 'in_sample_score': round(best, 4)},
          open('build/key_1577_final.json', 'w'), indent=1, ensure_ascii=False)
