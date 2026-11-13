# count_twelve.py [FOLDER]: per-letter strict counts for the twelve bare Petkum letters (first reader and blind reader),
# with key.tsv (KEY_v3, as decoded and filed in our log), key_v4.tsv and key_v5.tsv. Writes counts_twelve.txt and units/*.ledger.tsv.
# Label rule = scripts/count_v4.py label() (copied): N if any token not in the key (incl. '~'), tier C or '!N'; E if any value longer
# than three letters, 'et', or tier G; else S. strict = S/(S+E+N). Flattened .seg tokens are asserted equal to the frozen transcription.
# Standard library only; run with python3 -I. (b186, 13 Nov 2026)
import sys, os, re, collections
F = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(F, *a)
def load(p):
    k = {}
    for l in open(p, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        x = l.rstrip('\n').split('\t'); k[x[0]] = (x[1], x[2])
    return k
K = {'v3': load(P('key.tsv')), 'v4': load(P('key_v4.tsv')), 'v5': load(P('key_v5.tsv'))}
IDS = ['petkum_1665-01-06', 'petkum_1665-01-13', 'petkum_1665-01-27', 'petkum_1665-03-03', 'petkum_1665-05-12', 'petkum_1666-03-02',
       'petkum_1666-03-16', 'petkum_1666-03-23', 'petkum_1666-03-30', 'petkum_1666-04-06_king_p2', 'petkum_1666-04-06_biermann', 'petkum_1666-04-27']
def flat(tx): return [t.strip() for l in open(tx, encoding='utf8') if not l.startswith('#') and '|' in l for r in re.findall(r'<([^>]*)>', l) for t in r.split('.') if t.strip()]
def readseg(p):
    rows = []
    for l in open(p, encoding='utf8'):
        if not l.strip(): continue
        x = l.rstrip('\n').split(' ', 2); rows.append((x[0].split('.'), x[1] if len(x) > 1 else '', x[2] if len(x) > 2 else ''))
    return rows
def lab(toks, note, KEY):
    if any(t not in KEY for t in toks): return 'N'
    if any(KEY[t][1] == 'C' for t in toks): return 'N'
    if note.startswith('!N'): return 'N'
    if any(len(KEY[t][0]) > 3 or KEY[t][0] == 'et' or KEY[t][1] == 'G' for t in toks): return 'E'
    return 'S'
def pct(s, n): return '%d/%d = %.2f%%' % (s, n, 100.0 * s / n)
L = ['counts_twelve.txt: written by scripts/count_twelve.py (python3 -I). Strict = S/(S+E+N).',
     'v3 = key.tsv (KEY_v3, md5 ddc02e4a; the key these letters were first decoded with, 12 Nov 2026, as in our log); v4 = key_v4.tsv (maintainer, 13 Nov);',
     'v5 = key_v5.tsv (b186; decoded after the key update; not held-out for leaves used to build v5). Units = the first reader\'s word division; the blind',
     'reader\'s file carries the same units mapped onto the blind tokens.', '', 'letter\treader\tkey\tS\tE\tN\tunits\tstrict']
tot = collections.defaultdict(collections.Counter); per = collections.defaultdict(list)
for i in IDS:
    for suf, rd in (('', 'first'), ('_blind', 'blind')):
        rows = readseg(P('units', i + suf + '.seg'))
        assert [t for r in rows for t in r[0]] == flat(P('transcriptions', i + suf + '.txt')), 'seg/transcription mismatch ' + i + suf
        led = ['# ledger: %s, %s reader. label per key (v3 = key.tsv, v4 = key_v4.tsv, v5 = key_v5.tsv)' % (i, rd), '# tokens\tunit\tnote\tlabel_v3\tlabel_v4\tlabel_v5']
        for t, u, n in rows: led.append('\t'.join(['.'.join(t), u, n] + [lab(t, n, K[k]) for k in ('v3', 'v4', 'v5')]))
        open(P('units', i + suf + '.ledger.tsv'), 'w', encoding='utf8').write('\n'.join(led) + '\n')
        for k in ('v3', 'v4', 'v5'):
            c = collections.Counter(lab(t, n, K[k]) for t, u, n in rows); n = sum(c.values()); tot[(rd, k)] += c; per[(rd, k)].append(c['S'])
            L.append('%s\t%s\t%s\t%d\t%d\t%d\t%d\t%d/(%d+%d+%d) = %s' % (i, rd, k, c['S'], c['E'], c['N'], n, c['S'], c['S'], c['E'], c['N'], pct(c['S'], n)))
L.append('')
for rd in ('first', 'blind'):
    for k in ('v3', 'v4', 'v5'):
        c = tot[(rd, k)]; n = sum(c.values())
        L.append('pool of the twelve, %s reader, %s (information only; use the per-letter figures): S %s = %d; E %d; N %d; units %d; strict %s' % (rd, k, ' + '.join(map(str, per[(rd, k)])), c['S'], c['E'], c['N'], n, pct(c['S'], n)))
open(P('counts_twelve.txt'), 'w', encoding='utf8').write('\n'.join(L) + '\n'); print('\n'.join(L))
