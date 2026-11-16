"""Verifier's stricter variants of the first agent's held-out test. Imports their scripts read-only.
Usage: python3 -I stricter_heldout.py <their scripts dir>"""
import sys, itertools
sys.path.insert(0, sys.argv[1])
import os
import poly, multishift as ms
segs, labels = poly.read_ct(os.path.join(sys.argv[1], '..', 'transcription', 'pass1.txt'))
A = [s for l, s in zip(labels, segs) if l.split('.')[0] in {f'A{i}' for i in range(1, 10)}]
B = [s for l, s in zip(labels, segs) if l.split('.')[0] not in {f'A{i}' for i in range(1, 10)}]
print('first part', sum(map(len, A)), 'second part', sum(map(len, B)))
def sc(part, shifts): return ms.run(part, shifts)[0]
for name, tr, te in [('choose on first 350, score last 301', A, B), ('choose on last 301, score first 350', B, A)]:
    print('==', name)
    # V1: base 7 fixed; choose the two extra shifts on training among all 253 pairs; rank on test among all pairs
    pairs = [p for p in itertools.combinations(range(24), 2) if 7 not in p and 0 not in p]
    trs = {p: sc(tr, (7,) + p) for p in pairs}
    tes = {p: sc(te, (7,) + p) for p in pairs}
    best = max(trs, key=trs.get)
    rank = 1 + sum(v > tes[best] for v in tes.values())
    print(f' base 7 alone: train {sc(tr,(7,)):.4f} test {sc(te,(7,)):.4f}')
    print(f' extra pair chosen on train: {best} train {trs[best]:.4f}; on test {tes[best]:.4f}, rank {rank} of {len(pairs)} pairs; test best {max(tes,key=tes.get)} {max(tes.values()):.4f}; test median {sorted(tes.values())[len(tes)//2]:.4f}')
    print('  top 5 train:', sorted(trs, key=trs.get, reverse=True)[:5])
    print('  top 5 test :', sorted(tes, key=tes.get, reverse=True)[:5])
    # V2: whole triple (base included) chosen on training among all 2024 triples
    trip = list(itertools.combinations(range(24), 3))
    t3 = {t: sc(tr, t) for t in trip}
    b3 = max(t3, key=t3.get)
    e3 = {t: sc(te, t) for t in trip}
    print(f' triple chosen blind on train: {b3}; test score {e3[b3]:.4f}, rank {1+sum(v>e3[b3] for v in e3.values())} of 2024; best test triple {max(e3,key=e3.get)}')
    sys.stdout.flush()
