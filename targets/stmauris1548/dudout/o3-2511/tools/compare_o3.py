"""compare_o3.py (O3) - token agreement A/B with WAINUT compare.py: its load() and its row-by-row SequenceMatcher loop,
unchanged; WAINUT's BMAP (specific to their l2 passes) is NOT applied: names are compared as written (strict)."""
import sys, os, difflib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'o2-2311', 'wainut-scripts'))
from compare import load
A = load(sys.argv[1]); B = load(sys.argv[2])
tot = same = 0; dis = []
for k in A:
    a, b = A[k], B.get(k, [])
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        n = max(i2-i1, j2-j1); tot += n
        if op == "equal": same += n
        else: dis.append((k[0] + ' ' + k[1], i1, j1, op, " ".join(a[i1:i2]), " ".join(b[j1:j2])))
print(f"rows A {len(A)} B {len(B)}; aligned positions {tot}, same {same}, rate {same/tot:.3f}, disagreements {len(dis)}")
for d in dis: print(*d, sep="\t")
