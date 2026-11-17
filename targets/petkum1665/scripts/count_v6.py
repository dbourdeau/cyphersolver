# count_v6.py [FOLDER]: what key_v6.tsv (key_v5.tsv + nine values of Brice Dudout's key T2 seen under a gloss, 88 corrected;
# integration of PR #622, 14 Nov 2026) changes, letter by letter, for every letter that has a word division (units/*.seg).
# Label rule copied from scripts/count_twelve.py lab(): N if any token is not in the key (incl. '~'), is tier C, or the note
# starts with '!N'; E if any value is longer than three letters, is 'et', or is tier G; else S. strict = S/(S+E+N).
# Writes counts_v6.txt. Standard library only; run with python3 -I.
import sys, os, re, glob, collections
F = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(F, *a)
def load(p):
    k = {}
    for l in open(p, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        x = l.rstrip('\n').split('\t'); k[x[0]] = (x[1], x[2])
    return k
K = {'v5': load(P('key_v5.tsv')), 'v6': load(P('key_v6.tsv'))}
TWELVE = ['petkum_1665-01-06', 'petkum_1665-01-13', 'petkum_1665-01-27', 'petkum_1665-03-03', 'petkum_1665-05-12', 'petkum_1666-03-02',
          'petkum_1666-03-16', 'petkum_1666-03-23', 'petkum_1666-03-30', 'petkum_1666-04-06_king_p2', 'petkum_1666-04-06_biermann', 'petkum_1666-04-27']
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
NEW = sorted((t for t in K['v6'] if t not in K['v5']), key=int)
L = ['counts_v6.txt: written by scripts/count_v6.py (python3 -I). Strict = S/(S+E+N), the rule of scripts/count_twelve.py.',
     'v6 = key_v5.tsv + %d values of key T2 (%s) and 88 corrected to le Roy d\'Espagne. Code words count E, never S,' % (len(NEW), ', '.join(NEW)),
     'so a new code value can move a unit from N to E and cannot raise a strict share.', '',
     'letter\treader\tS v5\tE v5\tN v5\tS v6\tE v6\tN v6\tunits\tstrict v5\tstrict v6\tunits moved N to E (token: value)']
moved_all = collections.Counter()
for seg in sorted(glob.glob(P('units', '*.seg'))):
    i = os.path.basename(seg)[:-4]; rd = 'blind' if i.endswith('_blind') else 'first'; base = i[:-6] if rd == 'blind' else i
    rows = readseg(seg); c5 = collections.Counter(); c6 = collections.Counter(); mv = []
    for t, u, n in rows:
        a, b = lab(t, n, K['v5']), lab(t, n, K['v6']); c5[a] += 1; c6[b] += 1
        if a != b:
            mv.append('%s>%s %s' % (a, b, ', '.join('%s: %s' % (x, K['v6'][x][0]) for x in t if x in NEW))); moved_all.update(x for x in t if x in NEW)
    n = sum(c5.values())
    L.append('%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%.2f%%\t%.2f%%\t%s%s' % (base, rd, c5['S'], c5['E'], c5['N'], c6['S'], c6['E'], c6['N'], n,
             100.0 * c5['S'] / n, 100.0 * c6['S'] / n, '; '.join(mv) or '-', '\t[one of the twelve]' if base in TWELVE else ''))
L += ['', 'T2 values met in these word divisions: ' + (', '.join('%s x%d' % (k, v) for k, v in sorted(moved_all.items(), key=lambda kv: int(kv[0]))) or 'none')]
# code numbers with no value under v6, over every frozen transcription (first readers)
unk = collections.Counter()
for tx in sorted(glob.glob(P('transcriptions', '*.txt'))):
    if '_blind' in tx: continue
    for l in open(tx, encoding='utf8'):
        if l.startswith('#') or '|' not in l: continue
        for r in re.findall(r'<([^>]*)>', l):
            for t in r.split('.'):
                t = t.strip().rstrip('~')
                if t.isdigit() and t not in K['v6']: unk[t] += 1
L += ['', 'Code numbers with no value in key_v6.tsv, over the first-reader transcriptions (occurrences): ' + ', '.join('%s x%d' % (k, v) for k, v in sorted(unk.items(), key=lambda kv: int(kv[0])))]
open(P('counts_v6.txt'), 'w', encoding='utf8').write('\n'.join(L) + '\n'); print('\n'.join(L))
