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

def _bloc(m):
    """Un bloc de consensus {A:… | B:…} est UN groupe lu différemment par les deux lectures (correction du
    12 nov. 2026 : il était découpé en plusieurs faux groupes, d'où 481 au lieu de 465 pour le n° 131).
    On le ramène à un seul groupe à candidats : les nombres entre crochets s'il y en a, sinon le nombre lu ;
    les mots en clair cités entre guillemets et les remarques sont écartés."""
    cands = []
    for cote in m.group(1).split(" | "):
        cote = re.sub(r"«[^»]*»|\"[^\"]*\"", " ", re.sub(r"^\s*[AB]:", "", cote))
        alt = re.search(r"\[([^\]]*)\]", cote)
        for n in re.findall(r"\d+", alt.group(1) if alt else cote):
            if n not in cands:
                cands.append(n)
    return "?[" + "|".join(cands) + "]"


surs = total = 0
for l in texte.splitlines():
    l = re.sub(r"\{(A:[^{}]*)\}", _bloc, l)
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
