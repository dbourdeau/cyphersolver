"""name_step_o5.py (PREREG-O5 §5, 25/11/2026) - étape de nommage DÉCLARÉE D'AVANCE (leçon d'O4, point 4).
Tout jeton de la fusion gelée qui n'est ni un nom de clé (colonne 1 de key.tsv), ni NIL, ni un nom de transcripteur (t...),
ni un signe barré (..._) - typiquement un composé base + marque haute de SIGNS.md / SHAPES-KEY-NAMES.md sans ligne dans
key.tsv (en O4 : 13, @2, N6o, mx3) - est renommé tS-<nom> (aucune lettre). Rien d'autre n'est changé. Ne lit que les NOMS
de la clé, jamais une valeur. La fusion gelée n'est pas modifiée : écrit une copie *_named.txt et journalise les renommages.
Lancer depuis o5-2511/ : python3 -I tools/name_step_o5.py"""
import re, collections
SRC, DST = 'transcription_1548-03-12_Q_merged.txt', 'transcription_1548-03-12_Q_merged_named.txt'
names = {l.split('\t')[0] for l in open('../o2-2311/wainut-key.tsv', encoding='utf-8') if l.strip() and not l.startswith('# ')}
assert not any(k.startswith('t') or k == 'NIL' for k in names)
def bad(x): return not (x in names or x == 'NIL' or x.startswith('t') or x.endswith('_'))
src = open(SRC, encoding='utf-8').read().split('\n')
out = []; ren = collections.Counter()
for l in src:
    m = re.match(r'^(\d[rv] L\d\d: )(.*)$', l)
    if not m: out.append(l); continue
    t = m.group(2).split()
    for x in t:
        if bad(x): ren[x] += 1
    out.append(m.group(1) + ' '.join('tS-' + x if bad(x) else x for x in t))
log = ', '.join('%s x%d' % kv for kv in sorted(ren.items())) or 'aucun'
out.insert(3, '# Étape de nommage (PREREG-O5 §5, tools/name_step_o5.py) : %d jetons sans ligne dans key.tsv renommés tS-<nom> (%s) ; rien d\'autre changé.' % (sum(ren.values()), log))
open(DST, 'w', encoding='utf-8').write('\n'.join(out))
print(sum(ren.values()), 'jetons renommés :', log)
