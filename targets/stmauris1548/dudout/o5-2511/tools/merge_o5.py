"""merge_o5.py (PREREG-O5 §4, 25/11/2026) - fusion des passes aveugles A et B de la portion Q (cc. 6v-8v), AVANT tout décodage.
= merge_o4.py (8491108d...) rendu générique : nombre de désaccords lu dans ARBITRAGE.tsv (plus de 104 en dur), en-tête calculé.
Positions d'accord : le jeton commun. Positions disputées (même ordre que compare_o4.py) : choix de ARBITRAGE.tsv
(A -> jetons de A, B -> jetons de B, neither -> NIL répété max(len A, len B)). Les noms propres aux passes gardent leur
préfixe tA-... / tB-... (aucune lettre). Ponctuation et '?' retirés exactement comme compare.load. Compte ensuite (noms
seulement, colonne 1 de key.tsv, aucune valeur lue) les jetons dont le nom est un nom de clé (règle de taille du §3).
Lancer depuis o5-2511/ : python3 -I tools/merge_o5.py"""
import sys, os, re, difflib, csv, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'o2-2311', 'wainut-scripts'))
from compare import load
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def pref(rows, X): return {k: [('t%s-%s' % (X, t) if re.match(r't(\d|\?)', t) else t) for t in r] for k, r in rows.items()}
PA, PB = 'passe-A/transcription_passA.txt', 'passe-B/transcription_passB.txt'
A = pref(load(PA), 'A'); B = pref(load(PB), 'B')
assert list(A) == list(B), 'les deux passes n\'ont pas les mêmes lignes'
arb = [r for r in csv.DictReader(open('ARBITRAGE/ARBITRAGE.tsv', encoding='utf-8'), delimiter='\t')]
n = 0; out = []; cnt = {'A': 0, 'B': 0, 'neither': 0}; tot = same = 0
for k in A:
    a, b = A[k], B[k]; toks = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        m = max(i2 - i1, j2 - j1); tot += m
        if op == 'equal': toks += a[i1:i2]; same += m; continue
        r = arb[n]; n += 1
        assert r['id'] == 'D%03d' % n and r['row'] == '%s %s' % k and r['A'] == ' '.join(a[i1:i2]) and r['B'] == ' '.join(b[j1:j2]), r
        c = r['choice'].strip(); cnt[c] += 1
        toks += a[i1:i2] if c == 'A' else b[j1:j2] if c == 'B' else ['NIL'] * m
    out.append('%s %s: %s' % (k[0], k[1], ' '.join(toks)))
assert n == len(arb), 'ARBITRAGE.tsv ne couvre pas exactement les désaccords (%d / %d)' % (n, len(arb))
names = {l.split('\t')[0] for l in open('../o2-2311/wainut-key.tsv', encoding='utf-8') if l.strip() and not l.startswith('# ')}
allt = [t for l in out for t in l.split(': ', 1)[1].split()]
nk = sum(1 for t in allt if t in names)
pages = []
for k in A:
    if k[0] not in pages: pages.append(k[0])
span = ' + '.join('%s L01-L%02d' % (p, max(int(k[1][1:]) for k in A if k[0] == p)) for p in pages)
hdr = ('# transcription_1548-03-12_Q_merged.txt - PREREG-O5, 12 mars 1548, %s.\n'
       '# Passe aveugle A (%s) + passe aveugle B (%s), accord %.3f (%d/%d), %d désaccords arbitrés à l\'aveugle par l\'agent C\n'
       '# (A %d, B %d, neither %d -> NIL). tA-.. / tB-.. = formes propres aux transcripteurs (aucune lettre). tools/merge_o5.py.\n'
       % (span, sha(PA)[:8] + '...', sha(PB)[:8] + '...', same / tot, same, tot, n, cnt['A'], cnt['B'], cnt['neither']))
open('transcription_1548-03-12_Q_merged.txt', 'w', encoding='utf-8').write(hdr + '\n'.join(out) + '\n')
print(len(out), 'lignes', len(allt), 'jetons ;', 'jetons à nom de clé', nk, '; arbitrage', cnt)
print('noms hors clé, hors t, hors NIL (pour name_step_o5.py) :', sorted({t for t in allt if t not in names and not t.startswith('t') and t != 'NIL' and not t.endswith('_')}))
