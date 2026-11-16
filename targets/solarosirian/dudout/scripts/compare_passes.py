# -*- coding: utf-8 -*-
"""C13 — alignement passe 1 / passe 2 par unité (A, B, C, F), difflib ; D comparé en nombre seulement."""
import json, difflib, sys
p1 = json.load(open(sys.argv[1], encoding='utf-8'))['signs']
p2 = json.load(open(sys.argv[2], encoding='utf-8'))['units']
U1 = {}
for s in p1: U1.setdefault(s['unit'], []).append(s)
U2 = {u['unit']: u['signs'] for u in p2}
tot = agree = 0; out = []
for u, ss in U1.items():
    if u[0] == 'D' or u not in U2: continue
    a = [s['code'] for s in ss]; b = [s['code'] for s in U2[u]]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            agree += i2 - i1
        else:
            out.append(f"{u}: {op} p1[{i1}:{i2}]={a[i1:i2]} (ids {ss[i1]['id'] if i1<len(ss) else '-'}) | p2={b[j1:j2]}")
    tot += len(a)
print(f'A-C,F : {agree}/{tot} signes de la passe 1 identiques et alignés ({agree/tot:.1%})')
print('\n'.join(out))
d1 = sum(1 for s in p1 if s['zone'] == 'D'); d2 = sum(len(v) for k, v in U2.items() if k.startswith('D'))
print(f'D : passe 1 {d1} signes, passe 2 {d2} signes')
