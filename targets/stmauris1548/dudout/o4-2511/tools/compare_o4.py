"""compare_o4.py (O4) - token agreement A/B (PREREG-O4 §3): WAINUT compare.load + its row-by-row SequenceMatcher loop,
no BMAP (names compared as written). Before comparing, each pass's transcriber names t... are prefixed tA-... / tB-...
(a t1 of A is not assumed to be a t1 of B), so every t position is a disagreement. Also writes ARBITRAGE/disputes.json
(no values): disputed positions with context. Run from o4-2511/."""
import sys, os, re, difflib, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'o2-2311', 'wainut-scripts'))
from compare import load
def pref(rows, X): return {k: [('t%s-%s' % (X, t) if re.match(r't(\d|\?)', t) else t) for t in r] for k, r in rows.items()}
A = pref(load('passe-A/transcription_passA.txt'), 'A'); B = pref(load('passe-B/transcription_passB.txt'), 'B')
assert list(A) == list(B), 'row sets differ'
tot = same = 0; dis = []
for k in A:
    a, b = A[k], B[k]
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        n = max(i2 - i1, j2 - j1); tot += n
        if op == 'equal': same += n; continue
        dis.append(dict(id='D%03d' % (len(dis) + 1), row='%s %s' % k, sign_number=i1 + 1, row_length_A=len(a), op=op,
                        before=' '.join(a[max(0, i1 - 3):i1]), after=' '.join(a[i2:i2 + 3]), A=' '.join(a[i1:i2]), B=' '.join(b[j1:j2])))
print(f"rows A {len(A)} B {len(B)}; tokens A {sum(map(len,A.values()))} B {sum(map(len,B.values()))}; aligned positions {tot}, same {same}, rate {same/tot:.3f}, disagreements {len(dis)}")
for d in dis: print(d['id'], d['row'], d['sign_number'], d['op'], d['A'] or '-', d['B'] or '-', sep='\t')
if len(sys.argv) > 1: json.dump(dis, open('ARBITRAGE/disputes.json', 'w'), indent=1, ensure_ascii=False)
