"""Mechanical reconciliation of the two blind-ish transcriptions of catalogue 2857.

  python3 -I reconcile2857.py <transcription_A.txt> <transcription_B.txt> <adjudications.tsv|-> <out_reconciled.txt>

Steps (fixed): (1) strip '?', '/', '.' tokens and the CLEAR marker; (2) apply the CLASS rules below to reader B (sign
classes settled by comparing shapes with George Lasry's own leaf, BnF Esp. 318 f. 122r, before any decoding);
(3) align each line token by token (difflib); (4) agreements are kept; each disagreement is listed, and is settled only
by an entry in the adjudication file (line, A-index, value, reason); a disagreement without an entry becomes '#'
(a hole). Alternatives written 'Kxx/Kyy' count as the first one for the alignment.
"""
import sys, difflib, re

CLASS_B = {'N01': 'K23',   # T with two dots = Lasry's "T:" (leaf f.122r l.2: same form)
           'K08': 'K11',   # closed o joined to a 7 = Lasry's "7o" (leaf f.122r l.2 end: "=. 7o np C."), not "np"
           'N02': 'K42'}   # stem + colon + o: B's own note, K42 with a stray colon


def load(path, classmap=None):
    out = {}
    for line in open(path, encoding='utf8'):
        m = re.match(r'(L\d):\s*(.*)', line)
        if not m:
            continue
        toks = []
        for t in m.group(2).split():
            if t in ('/', '.', ':', 'CLEAR'):
                continue
            t = t.rstrip('?').split('/')[0]
            if classmap:
                t = classmap.get(t, t)
            toks.append(t)
        out.setdefault(m.group(1), toks)   # first occurrence only (later 'L8:' lines are notes)
    return out


def main():
    A, B = load(sys.argv[1]), load(sys.argv[2], CLASS_B)
    adj = {}
    if sys.argv[3] != '-':
        for row in open(sys.argv[3], encoding='utf8'):
            if row.startswith('#') or not row.strip():
                continue
            ln, ia, val, why = row.rstrip('\n').split('\t')
            adj[(ln, int(ia))] = (val, why)
    rec, agree, total, report = {}, 0, 0, []
    for ln in sorted(A):
        a, b = A[ln], B.get(ln, [])
        sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
        res = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                res += a[i1:i2]; agree += i2 - i1; total += i2 - i1
                continue
            n = max(i2 - i1, j2 - j1)
            for k in range(n):
                ia = i1 + k if i1 + k < i2 else None
                ta = a[ia] if ia is not None else '-'
                tb = b[j1 + k] if j1 + k < j2 else '-'
                total += 1
                key = (ln, ia if ia is not None else -1 - (j1 + k))
                if key in adj:
                    val, why = adj[key]
                else:
                    val, why = '#', 'unsettled: hole'
                report.append(f'{ln}\tA{key[1]}\tA={ta}\tB={tb}\t-> {val}\t{why}')
                if val != 'DROP':
                    res.append(val)
        rec[ln] = res
    with open(sys.argv[4], 'w', encoding='utf8') as f:
        f.write('# reconciled transcription of catalogue 2857 (reconcile2857.py); # = hole\n')
        for ln in sorted(rec):
            f.write(f'{ln}: ' + ' '.join(rec[ln]) + '\n')
    print(f'positions {total}, agreeing after class rules {agree} ({agree / total:.1%}), disagreements {total - agree}')
    print('\n'.join(report))


if __name__ == '__main__':
    main()
