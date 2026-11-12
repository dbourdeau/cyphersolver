# count_v4.py [FOLDER]: recount the word-division (.seg) letters with key_v4.tsv, next to the key v3 count of scripts/count.py.
# Same rule as count.py; the new tier G rows are code words (count E, never S); tier A3 rows (PF=f, Q=b, 242=he) are spelled values.
# Letters whose labels are the reader's own (units.tsv: 30 Nov 1665, Paulmyer) are NOT relabelled here; their figures stay as filed (a floor).
# Writes counts_v4.txt. Standard library only; run with python3 -I.
import sys, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.dirname(HERE)
P = lambda *a: os.path.join(F, *a)
def load(path):
    k = {}
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        p = l.rstrip('\n').split('\t'); k[p[0]] = (p[1], p[2])
    return k
K3, K4 = load(P('key.tsv')), load(P('key_v4.tsv'))
def flat(tx): return [t.strip() for l in open(tx, encoding='utf8') if not l.startswith('#') and '|' in l for r in re.findall(r'<([^>]*)>', l) for t in r.split('.') if t.strip()]
def label(seg, tx, KEY):
    c = collections.Counter(); rows = []; fl = []
    for l in open(seg, encoding='utf8'):
        if not l.strip(): continue
        p = l.rstrip('\n').split(' ', 2); toks = p[0].split('.'); fl += toks
        if any(t not in KEY for t in toks): lab = 'N'
        elif any(KEY[t][1] == 'C' for t in toks): lab = 'N'
        elif len(p) > 2 and p[2].startswith('!N'): lab = 'N'
        elif any(len(KEY[t][0]) > 3 or KEY[t][0] == 'et' or KEY[t][1] == 'G' for t in toks): lab = 'E'
        else: lab = 'S'
        c[lab] += 1; rows.append((p[0], p[1], lab))
    assert fl == flat(tx)
    return c, rows
def pct(a, b): return '%d/%d = %.2f%%' % (a, b, 100.0 * a / b)
L = ['counts_v4.txt: written by scripts/count_v4.py (python3 -I). key v3 = key.tsv, key v4 = key_v4.tsv.', '']
tot3 = collections.Counter(); tot4 = collections.Counter()
for suf, name in (('', 'first reader'), ('_blind', 'blind reader')):
    L.append('Letters on the word division (.seg), ' + name)
    for d in ['1665-03-24', '1665-04-28', '1665-06-23', '1665-09-17', '1665-11-23', '1665-12-10', '1666-01-18', '1666-04-06', '1666-04-13']:
        sg = P('units', 'petkum_%s%s.seg' % (d, suf)); tx = P('transcriptions', 'petkum_%s%s.txt' % (d, suf))
        if not os.path.exists(sg): continue
        c3, r3 = label(sg, tx, K3); c4, r4 = label(sg, tx, K4); n = sum(c3.values())
        ch = ['%s %s->%s' % (a[1], a[2], b[2]) for a, b in zip(r3, r4) if a[2] != b[2]]
        L.append('  %s%s: v3 %s ; v4 %s ; N->S/E: %s' % (d, suf, pct(c3['S'], n), pct(c4['S'], n), '; '.join(ch) or 'none'))
        if not suf: tot3 += c3; tot4 += c4
    L.append('')
n = sum(tot3.values())
L.append('Nine first-reader letters pooled (information only, not a headline): v3 %s, v4 %s' % (pct(tot3['S'], n), pct(tot4['S'], n)))
L.append('v4 E: %d (v3 E: %d); v4 N: %d (v3 N: %d)' % (tot4['E'], tot3['E'], tot4['N'], tot3['N']))
open(P('counts_v4.txt'), 'w', encoding='utf8').write('\n'.join(L) + '\n'); print('\n'.join(L))
