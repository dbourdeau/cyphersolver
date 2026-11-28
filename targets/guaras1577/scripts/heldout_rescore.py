"""Re-score the frozen key on the held-out lines without writing anything (cold check, 28 Nov 2026, after the test):
the protocol's metric, then the same metric without the OCR classes c=e and l=t, then with nothing merged. Run from
targets/guaras1577 after scripts/fetch_kervyn.py. The registered result is verification/RESULT_v1.json only."""
import json, os, sys
os.environ['TSPLIT'] = '1'; sys.path.insert(0, 'scripts')
import build_key as B, measure_lib as M
from kervyn_units import units
P = json.load(open('verification/PROTOCOL_v1.json'))
raw = json.load(open('verification/key_1577_v1.json'))['key']
U = units(); j0, j1 = P['reference_units']
toks = [t for lab in sorted(B.L) if lab in B.HELDOUT for t in B.L[lab]]
for name, TR in (('protocol (y=i f=s c=e l=t)', {'y': 'i', 'f': 's', 'e': 'c', 't': 'l'}),
                 ('without the OCR classes (y=i f=s)', {'y': 'i', 'f': 's'}), ('nothing merged', {})):
    f = lambda x: ''.join(TR.get(c, c) for c in x)
    key = {s: f(v) for s, v in raw.items()}; ref = [u if len(u) > 1 else f(u) for u in U[j0:j1]]
    r, s, h = M.score(toks, key, ref); c = M.controls(toks, key, ref, 200, 1577)
    m = sum(c) / len(c); sd = (sum((x - m) ** 2 for x in c) / len(c)) ** .5
    print(f'{name}: {r} of {s} ({r / s:.3f}), best control {max(c):.3f}, mean {m:.3f}, z {(r / s - m) / sd:.2f}')
