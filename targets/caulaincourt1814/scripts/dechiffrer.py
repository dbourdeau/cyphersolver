"""Applique une table reconstruite à un texte chiffré.

Usage : python3 dechiffrer.py table.tsv chiffre.txt [seuil_occurrences]
Pour chaque ligne : les valeurs séparées par « · ». Valeur sûre : vue au moins
`seuil` fois (défaut 2) avec une probabilité EM >= 0,6 ; douteuse : suivie de « ? » ;
inconnue : [nombre]. Les lectures incertaines du chiffre sont toutes essayées.
"""
import csv
import re
import sys

table = {}
for r in list(csv.reader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))[1:]:
    table[int(r[0])] = (r[1], int(r[2]), float(r[4]))
seuil = int(sys.argv[3]) if len(sys.argv) > 3 else 2

texte = open(sys.argv[2], encoding="utf-8").read()
if "\nCHIFFRE" in texte:
    texte = texte[texte.index("\nCHIFFRE"):]
texte = re.split(r"\n(GLOSES|DOUTES|NOTES|DESACCORDS)", texte)[0]

surs = total = 0
for l in texte.splitlines():
    m = re.match(r"\s*(f\d+[rv]?)\s+(L\d+)\s*:\s*(.*)$", l)
    if not m:
        continue
    sortie = []
    for tok in re.findall(r"«[^»]*»|\"[^\"]*\"|\S+", m.group(3)):
        if tok[0] in "«\"":
            sortie.append(tok)
            continue
        alt = re.search(r"\[([\d|]+)\]", tok)
        d = re.sub(r"\D", "", re.sub(r"\[.*", "", tok.lstrip("_")))
        cands = [int(x) for x in alt.group(1).split("|") if x] if alt else ([int(d)] if d else [])
        total += 1
        best = max((table[n] + (n,) for n in cands if n in table), key=lambda t: (t[1] >= seuil and t[2] >= 0.6, t[1]), default=None)
        if best is None:
            sortie.append(f"[{'|'.join(map(str, cands)) or '?'}]")
        else:
            v = "∅" if best[0] == "(nulle)" else best[0]
            if best[1] >= seuil and best[2] >= 0.6:
                surs += 1
                sortie.append(v)
            else:
                sortie.append(v + "?")
    print(f"{m.group(1)} {m.group(2)}: " + " · ".join(sortie))
print(f"\n{surs}/{total} groupes à valeur sûre", file=sys.stderr)
