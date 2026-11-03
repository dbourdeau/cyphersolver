"""Settle c. 42r from three blind passes (A, B: whole lines; C: half lines at full size) by majority per aligned sign.
A sign stands if two passes agree; where all three differ, pass A's sign is kept and marked doubtful (?).
Signs present in only one pass are dropped; signs missing in only one pass are kept. Superscripts are not voted on
(they are kept from the base pass). Output: transcription_c42r.txt, validation/settle_log.tsv"""
import sys, difflib
sys.path.insert(0, __import__('os').path.dirname(__file__))
from learn import toks
def rd(f): return dict(l.rstrip('\n').split('\t', 1) for l in open(f, encoding='utf8') if '\t' in l)
A, B, C = rd('validation/passA.txt'), rd('validation/passB.txt'), rd('validation/passC_c0.txt')
def clean(s): return [x for x in toks(s) if not x.startswith('MARK')]
out, log = [], []
for i in range(14):
    n = f'c0L{i:02d}'
    a, b, c = clean(A.get(n, '')), clean(B.get(n, '')), clean(C.get(n, ''))
    if not a: a, b = b, a
    def amap(x):
        m = {}; sm = difflib.SequenceMatcher(None, a, x, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
                for k in range(i2 - i1): m[i1 + k] = x[j1 + k]
            elif op == 'delete':
                for k in range(i1, i2): m[k] = None
            elif op == 'replace':
                for k in range(i1, i2): m[k] = x[j1 + (k - i1)] if j1 + (k - i1) < j2 else None
        return m
    mb, mc = amap(b), amap(c)
    res = []
    for k, s in enumerate(a):
        vb, vc = mb.get(k), mc.get(k)
        if vb is None and vc is None and b and c:
            log.append(f'{n}\t{k}\t{s}\t-\t-\tdropped (only pass A has it)'); continue
        if s == vb or s == vc: res.append(s)
        elif vb is not None and vb == vc: res.append(vb); log.append(f'{n}\t{k}\t{s}\t{vb}\t{vc}\tB and C agree')
        else: res.append(s + '?'); log.append(f'{n}\t{k}\t{s}\t{vb}\t{vc}\tall differ: A kept, doubtful')
    out.append(f'{n}\t' + ' '.join(res))
hdr = ['# Francesco d\'Este to Ferrante Gonzaga, 13 Apr 1546, c. 42r: cipher signs per line (clear words left out).',
       '# Sign names: validation/legend.md. Settled from three blind passes by scripts/settle.py (majority per sign);',
       '# ? = all three passes differ (pass A kept). Superscript digits (6, 4) are not recorded here; see NOTES.']
open('transcription_c42r.txt', 'w', encoding='utf8').write('\n'.join(hdr + out) + '\n')
open('validation/settle_log.tsv', 'w', encoding='utf8').write('line\tpos\tA\tB\tC\tdecision\n' + '\n'.join(log) + '\n')
tot = sum(len(l.split('\t')[1].split()) for l in out); dq = sum(l.count('?') for l in out)
print('signs', tot, 'doubtful', dq, 'log rows', len(log))
