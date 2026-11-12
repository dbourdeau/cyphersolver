# agreement_twelve.py [FOLDER]: token agreement between the first reader's and the blind reader's transcriptions of the twelve
# bare Petkum letters (difflib alignment, unsure mark '~' stripped). Writes agreement_twelve.txt. python3 -I. (b186, 13 Nov 2026)
import sys, os, re, difflib
F = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(F, *a)
IDS = ['petkum_1665-01-06', 'petkum_1665-01-13', 'petkum_1665-01-27', 'petkum_1665-03-03', 'petkum_1665-05-12', 'petkum_1666-03-02',
       'petkum_1666-03-16', 'petkum_1666-03-23', 'petkum_1666-03-30', 'petkum_1666-04-06_king_p2', 'petkum_1666-04-06_biermann', 'petkum_1666-04-27']
def toks(p): return [t.strip() for l in open(p, encoding='utf8') if not l.startswith('#') and '|' in l for r in re.findall(r'<([^>]*)>', l) for t in r.split('.') if t.strip()]
L = ['agreement_twelve.txt: written by scripts/agreement_twelve.py (python3 -I). agreement = tokens equal / first-reader tokens.', '',
     'letter\tfirst\tblind\tequal\tsubst\tdeleted\tinserted\tagreement\tdifferences (first>blind)']
T = [0, 0, 0, 0, 0, 0]
for i in IDS:
    a = toks(P('transcriptions', i + '.txt')); b = toks(P('transcriptions', i + '_blind.txt'))
    sm = difflib.SequenceMatcher(None, [t.rstrip('~') for t in a], [t.rstrip('~') for t in b], autojunk=False); eq = su = de = ins = 0; d = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': eq += i2 - i1
        elif op == 'replace':
            k = min(i2 - i1, j2 - j1); su += k; de += (i2 - i1) - k; ins += (j2 - j1) - k; d.append('%s>%s' % ('.'.join(a[i1:i2]), '.'.join(b[j1:j2])))
        elif op == 'delete': de += i2 - i1; d.append('%s>(none)' % '.'.join(a[i1:i2]))
        else: ins += j2 - j1; d.append('(none)>%s' % '.'.join(b[j1:j2]))
    L.append('%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d/%d = %.2f%%\t%s' % (i, len(a), len(b), eq, su, de, ins, eq, len(a), 100.0 * eq / len(a), '; '.join(d) or '-'))
    for k, v in enumerate((len(a), len(b), eq, su, de, ins)): T[k] += v
L.append('all twelve\t%d\t%d\t%d\t%d\t%d\t%d\t%d/%d = %.2f%%' % (T[0], T[1], T[2], T[3], T[4], T[5], T[2], T[0], 100.0 * T[2] / T[0]))
open(P('agreement_twelve.txt'), 'w', encoding='utf8').write('\n'.join(L) + '\n'); print('\n'.join(L))
