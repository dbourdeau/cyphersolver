"""dieguez1914: compare the three transcriptions of CMXV.35.3433.1-2 group by group.

  transcription/groups_CMXV.35.3433.1-2.tsv         the settled transcription (first reader, two passes, 25 Nov 2026)
  transcription/groups_CMXV.35.3433.1-2_blind2.tsv  blind reader 2 (images only, 25 Nov 2026)
  transcription/groups_CMXV.35.3433.1-2_blind3.tsv  blind reader 3 (line crops only, 27 Nov 2026)
Run from the repository root:  python targets/dieguez1914/scripts/compare_readings.py
"""
import csv
from pathlib import Path

T = Path(__file__).resolve().parent.parent / 'transcription'


def rows(name):
    lines = [l for l in open(T / name, encoding='utf-8') if not l.startswith('#')]
    return list(csv.DictReader(lines, delimiter='\t'))


def settled():
    out = {}
    for r in rows('groups_CMXV.35.3433.1-2.tsv'):
        if r['kind'] == 'group':
            pg, ln = r['line'].split('.')
            out[(int(pg[1:]), int(ln[1:]), int(r['pos']))] = r['value']
    return out


def blind2():
    out, n = {}, {}
    for r in rows('groups_CMXV.35.3433.1-2_blind2.tsv'):
        g = r['group'].strip()
        if g.startswith('['):
            continue
        k = (int(r['page']), int(r['line']))
        n[k] = n.get(k, 0) + 1
        out[k + (n[k],)] = g
    return out


def blind3():
    out = {}
    for r in rows('groups_CMXV.35.3433.1-2_blind3.tsv'):
        if r['kind'].strip() == 'number':
            out[(int(r['page']), int(r['line']), int(r['pos']))] = r['reading'].strip()
    return out


A, B, C = settled(), blind2(), blind3()
print('groups: settled %d, blind2 %d, blind3 %d' % (len(A), len(B), len(C)))
for name, X in (('blind2', B), ('blind3', C)):
    same = sum(1 for k in A if X.get(k) == A[k])
    print('settled vs %s: %d of %d agree' % (name, same, len(A)))
    for k in sorted(A):
        if X.get(k) != A[k]:
            print('   p%d.L%d group %d: settled %s, %s %s' % (k + (A[k], name, X.get(k))))
