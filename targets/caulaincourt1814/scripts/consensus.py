"""Fusionne deux lectures indépendantes d'un même chiffre.

Pour chaque groupe : candidats de A et de B (alternatives entre crochets, ?
comme joker). Accord = intersection non vide. Sortie : une lecture consensus
(groupe sûr si une seule valeur commune, sinon groupe marqué ?[...]), et la
liste des désaccords francs à revoir sur l'image.

Usage : python3 consensus.py lecture_A.txt lecture_B.txt sortie.txt
"""
import difflib
import re
import sys


def lire(chemin):
    lignes = {}
    for l in open(chemin, encoding="utf-8"):
        if re.match(r"\W*(GLOSES|DOUTES|NOTES|DESACCORDS)", l):
            break
        m = re.match(r"\s*(f\d+[rv]?)\s+(L\d+)\s*:\s*(.*)$", l)
        if m:
            lignes[f"{m.group(1)} {m.group(2)}"] = re.findall(r"«[^»]*»|\"[^\"]*\"|\S+", m.group(3))
    return lignes


def candidats(tok):
    tok = tok.lstrip("_")
    alt = re.search(r"\[([\d|]+)\]", tok)
    if alt:
        return set(alt.group(1).split("|"))
    motif = re.sub(r"\[.*", "", tok)
    if "?" in motif:
        return {"~" + motif}          # joker : à résoudre contre l'autre lecture
    return {re.sub(r"\D", "", motif)}


def accorder(ca, cb):
    def joker(c, autres):
        if not c.startswith("~"):
            return {c}
        rx = re.compile("^" + c[1:].replace("?", r"\d") + "$")
        return {a for a in autres if not a.startswith("~") and rx.match(a)} or {c}
    ea = set().union(*[joker(c, cb) for c in ca])
    eb = set().union(*[joker(c, ca) for c in cb])
    return ea & eb, ea, eb


A, B = lire(sys.argv[1]), lire(sys.argv[2])
out, desaccords, n_tot, n_sur = [], [], 0, 0
refs = sorted(set(A) | set(B), key=lambda r: (int(re.sub(r"\D", "", r.split()[0])), r.split()[0][-1], int(r.split()[1][1:])))
for ref in refs:
    a, b = A.get(ref, []), B.get(ref, [])
    ka = [candidats(t) for t in a]
    kb = [candidats(t) for t in b]
    sa = ["/".join(sorted(k)) for k in ka]
    sb = ["/".join(sorted(k)) for k in kb]
    sm = difflib.SequenceMatcher(a=sa, b=sb, autojunk=False)
    # alignement souple : on apparie position par position dans les blocs de même longueur
    toks = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
            for i, j in zip(range(i1, i2), range(j1, j2)):
                commun, ea, eb = accorder(ka[i], kb[j])
                n_tot += 1
                commun = {c for c in commun if not c.startswith("~")}
                if len(commun) == 1:
                    toks.append(next(iter(commun)))
                    n_sur += 1
                else:
                    tout = sorted(c.lstrip("~") for c in (commun or (ea | eb)))
                    toks.append("?[" + "|".join(tout) + "]")
                    if not commun:
                        desaccords.append(f"{ref} groupe {len(toks)} : A={a[i]} B={b[j]}")
        else:
            n_tot += max(i2 - i1, j2 - j1)
            toks.append("{A:" + " ".join(a[i1:i2]) + " | B:" + " ".join(b[j1:j2]) + "}")
            desaccords.append(f"{ref} groupes {len(toks)} : A={' '.join(a[i1:i2]) or '∅'} B={' '.join(b[j1:j2]) or '∅'}")
    out.append(f"{ref}: " + " ".join(toks))

with open(sys.argv[3], "w", encoding="utf-8") as f:
    f.write(f"# consensus de {sys.argv[1]} et {sys.argv[2]}\n")
    f.write("\n".join(out) + "\n\nDESACCORDS\n" + "\n".join(desaccords) + "\n")
print(f"{n_tot} groupes, {n_sur} sûrs ({100 * n_sur / max(1, n_tot):.1f} %), {len(desaccords)} désaccords francs")
