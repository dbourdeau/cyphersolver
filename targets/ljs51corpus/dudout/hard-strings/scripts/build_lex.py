"""Lexique de mots (formes normalisees, comptes) tire de textes OpenITI deja recoltes (SPOF_2).
Ibn Nubata (calibration) exclu. Ecrit lex.tsv (mot\tcompte), formes de 2 a 12 lettres."""
import sys, os, collections
sys.path.insert(0, "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-aveugle/scripts")
from common import words, strip_meta, CORPUS, CALIB
FILES = sys.argv[2].split(',')
out = sys.argv[1]
cnt = collections.Counter()
for f in FILES:
    assert CALIB not in f
    t = strip_meta(open(CORPUS + f, encoding='utf8', errors='ignore').read())
    for w in words(t):
        if 1 <= len(w) <= 12: cnt[w] += 1
with open(out, 'w') as g:
    for w, c in cnt.most_common(): g.write(f"{w}\t{c}\n")
print(len(cnt), "formes", sum(cnt.values()), "mots")
