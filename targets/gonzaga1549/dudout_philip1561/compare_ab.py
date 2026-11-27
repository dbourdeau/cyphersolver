"""Compare two blind shape transcriptions (A, B) line by line; write the agreed line and the open places.

    python3 compare_ab.py <work_dir> <letter> <A files...> -- <B files...>

Agreement is on SHAPE NAMES only: two tokens agree if their first choices are equal, if one first choice is among the
other's alternatives, or if the frozen CROSSWALK-C09.tsv sends both to the same key-table NAME (no value is looked up).
Output: arb/<letter>_DIFF.tsv (one row per open place) and arb/<letter>_PRE.txt (agreed lines, open places as {{A||B}}).
"""
import difflib, sys
from pathlib import Path

W = Path(sys.argv[1]); letter = sys.argv[2]
i = sys.argv.index('--'); A = sys.argv[3:i]; B = sys.argv[i + 1:]
cw = {}
for l in (W / 'CROSSWALK-C09.tsv').read_text().splitlines():
    if l.strip() and not l.startswith('#'):
        p = l.split('\t'); cw[p[0]] = p[1]


def load(files):
    d = {}
    for f in files:
        for l in (W / 'blind' / f).read_text().splitlines():
            if l.strip() and not l.startswith('#'):
                p = l.split(); d[p[0]] = p[1:]
    return d


def alts(t):
    return t.split('|')


def same(a, b):
    if a == b:
        return True
    A_, B_ = alts(a), alts(b)
    if A_[0] in B_ or B_[0] in A_:
        return True
    ca, cb = cw.get(A_[0]), cw.get(B_[0])
    return ca is not None and ca == cb


def key(t):
    return cw.get(alts(t)[0], alts(t)[0])


a, b = load(A), load(B)
(W / 'arb').mkdir(exist_ok=True)
diff = ['line\tpos\tA\tB']
pre = []
tot = agree = 0
for lid in sorted(set(a) | set(b), key=lambda s: (s.split('-')[0], s)):
    ta, tb = a.get(lid, []), b.get(lid, [])
    sm = difflib.SequenceMatcher(None, [key(t) for t in ta], [key(t) for t in tb], autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(i2 - i1):
                ea, eb = ta[i1 + k], tb[j1 + k]
                out.append(alts(ea)[0] if alts(ea)[0] == alts(eb)[0] or alts(ea)[0] in alts(eb) else alts(eb)[0] if alts(eb)[0] in alts(ea) else alts(ea)[0])
                agree += 1; tot += 1
        else:
            sa, sb = ta[i1:i2], tb[j1:j2]
            if op == 'replace' and len(sa) == len(sb):
                for x, y in zip(sa, sb):
                    tot += 1
                    if same(x, y):
                        agree += 1; out.append(alts(x)[0])
                    else:
                        diff.append(f'{lid}\t{len(out)+1}\t{x}\t{y}'); out.append('{{%s||%s}}' % (x, y))
            else:
                tot += max(len(sa), len(sb))
                diff.append(f'{lid}\t{len(out)+1}\t{" ".join(sa) or "-"}\t{" ".join(sb) or "-"}')
                out.append('{{%s||%s}}' % (' '.join(sa) or '-', ' '.join(sb) or '-'))
    pre.append(lid + ' ' + ' '.join(out))
(W / 'arb' / f'{letter}_DIFF.tsv').write_text('\n'.join(diff) + '\n')
(W / 'arb' / f'{letter}_PRE.txt').write_text('\n'.join(pre) + '\n')
print(letter, 'positions', tot, 'agreed', agree, round(agree / tot, 3), 'open places', len(diff) - 1)
