"""Build the blind arbitration list (no values): each A/B disagreement with agreed context tokens."""
import sys, os, difflib, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'o2-2311', 'wainut-scripts'))
from compare import load
A = load('passe-A/transcription_passA.txt'); B = load('passe-B/transcription_passB.txt')
items = []
for k in A:
    a, b = A[k], B[k]
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal': continue
        items.append(dict(id='D%02d' % (len(items) + 1), row='%s %s' % k, sign_number=i1 + 1, row_length=len(a),
                          before=' '.join(a[max(0, i1 - 3):i1]), after=' '.join(a[i2:i2 + 3]),
                          A=' '.join(a[i1:i2]), B=' '.join(b[j1:j2])))
json.dump(items, open('ARBITRAGE/disputes.json', 'w'), indent=1, ensure_ascii=False)
print(len(items))
