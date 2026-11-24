"""Test M (plan: tests/PLAN_tests.md, hashed in tests/PLAN_FREEZE.txt before the blind reader started): align the
blind reading of the figures with the first reading, paragraph by paragraph (difflib on the group sequence), and
count the groups that agree exactly (digits and the "+" mark). PASS if at least 106 of 112 agree.

A re-implementation, inside this folder, of the scoring used on 17 Nov 2026 (tests/test_M_result.txt); standard
library only.   python tests/score_test_M.py
"""
import difflib, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent


def load(p):
    d = {}
    for line in open(p, encoding='utf-8'):
        m = re.match(r'(P\dL\d):?\s+(.*)', line.strip())
        if m:
            d[m.group(1)] = [g.split('|')[0] for g in m.group(2).replace('[', '').replace(']', '').split()]
    return d


a = load(HERE / 'transcriptions' / 'first_reading_2026-11-12' / 'T1758_AN155AP2_p25_figures_v2.txt')
b = load(HERE / 'transcriptions' / 'blind_2026-11-17' / 'figures.txt')
total = agree = 0
for par in ('P1', 'P2'):
    A = sum([a[k] for k in sorted(a) if k.startswith(par)], [])
    B = sum([b.get(k, []) for k in sorted(b) if k.startswith(par)], [])
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    eq = sum(x.size for x in sm.get_matching_blocks())
    total += len(A); agree += eq
    print(par, 'first reading', len(A), 'blind', len(B), 'exact agree', eq)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            print(' ', op, 'first', A[i1:i2], 'blind', B[j1:j2], 'at index', i1)
print(f'{agree} of {total} groups agree:', 'PASS' if agree >= 106 else 'FAIL', '(rule: at least 106 of 112)')
