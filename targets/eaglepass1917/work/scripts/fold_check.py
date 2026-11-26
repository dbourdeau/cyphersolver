#!/usr/bin/env python3
"""eaglepass1917: check that key.tsv is the keyword alphabet TIRANO + rest, folded on itself (standard library only).
Run from the repository root: python3 -I targets/eaglepass1917/work/scripts/fold_check.py
The search that found no other keyword or construction, and its controls, are summarised in work/runs/fold_test.json."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.path.join(HERE, '..', '..', 'key.tsv')
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def fold(keyword, axis=0):
    seq = []
    for ch in keyword + A:
        if ch not in seq: seq.append(ch)
    pos = {c: i for i, c in enumerate(seq)}
    return ''.join(seq), {c: seq[(axis - pos[c]) % 26] for c in seq}

seq, k = fold("TIRANO")
obs = {}
for line in open(KEY, encoding='utf-8'):
    p = line.rstrip('\n').split('\t')
    if line.startswith('#') or p[0] == 'cipher' or len(p) < 3: continue
    if int(p[2]) > 0: obs[p[0]] = p[1].upper()
agree = sum(1 for c, v in obs.items() if k[c] == v)
print("sequence:", seq)
print("pairs:", ' '.join(sorted({''.join(sorted(c + v)) for c, v in k.items()})))
print(f"observed cipher letters reproduced: {agree} of {len(obs)}")
print("predicted for unseen cipher letters:", {c: k[c].lower() for c in A if c not in obs})
