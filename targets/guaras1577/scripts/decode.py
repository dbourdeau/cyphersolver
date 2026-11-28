"""Print the decode of every cipher line with the frozen key (run from targets/guaras1577, TSPLIT=1).
Dotted numbers stay as [#NN]; a sign with no value prints as '?'. No word division is added."""
import json, os, sys
os.environ.setdefault('TSPLIT', '1'); sys.path.insert(0, 'scripts')
import build_key as B
key = json.load(open('verification/key_1577_v1.json'))['key']
for lab in sorted(B.L, key=lambda x: (x[:2], int(x[3:]))):
    print(lab, ''.join(f'[{t}]' if t.startswith('#') else key.get(t, '?') for t in B.L[lab]))
