"""DESCRIPTIF, fait APRÈS la mesure c3 (non décisif). Attestation des mots du décodage qummī (c2) dans Lisān al-ʿArab
et Tāj al-ʿarūs (OpenITI). Comptes de jetons normalisés (qummi_lib.normalize), forme exacte puis forme sans préfixe
(و ب ف ل ال وال بال) ; quelques contextes pour les formes rares.
Usage : /usr/bin/python3 -E attestations_post_c3.py <dossier ljs51-qummi> <dossier corpus>
"""
import sys, os, json, re
from collections import Counter
D, CORP = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(D, "scripts"))
from qummi_lib import normalize
R = json.load(open(os.path.join(D, "c3", "RESULT_c3.json"), encoding="utf-8"))
dec = R["qummi_reference"]["decoded"].split()
cant = normalize(open(os.path.join(D, "donnees", "cant_90.txt"), encoding="utf-8").read()).split()
DICTS = {"Lisan": "0711IbnManzurIfriqi.LisanCarab.Shamela0001687-ara1.mARkdown",
         "Taj": "1205MurtadaZabidi.TajCarus.Shamela0007030-ara1"}
PREF = ["وبال", "وال", "بال", "فال", "ال", "و", "ب", "ف", "ل"]
def strip(w):
    for p in PREF:
        if w.startswith(p) and len(w) - len(p) >= 2:
            return w[len(p):]
    return w
texts, counts = {}, {}
for k, f in DICTS.items():
    t = []
    for ln in open(os.path.join(CORP, f), encoding="utf-8"):
        if not ln.startswith("#META"):
            t.append(normalize(ln))
    texts[k] = " ".join(t)
    counts[k] = Counter(texts[k].split())
def ctx(k, w, n=2, width=60):
    out = []
    for m in re.finditer(r"(?<!\S)" + re.escape(w) + r"(?!\S)", texts[k]):
        out.append(texts[k][max(0, m.start() - width):m.end() + width])
        if len(out) >= n: break
    return out
rows = []
for i, (c, w) in enumerate(zip(cant, dec), 1):
    s = strip(w)
    r = {"n": i, "argot": c, "decode_qummi": w, "forme_sans_prefixe": s,
         "argot_Lisan": counts["Lisan"][c], "argot_Taj": counts["Taj"][c]}
    for k in DICTS:
        r[k] = counts[k][w]
        r[k + "_sans_prefixe"] = counts[k][s] if s != w else None
        r[k + "_contextes"] = ctx(k, w) if 0 < counts[k][w] <= 50 else []
    rows.append(r)
json.dump(rows, open(os.path.join(D, "c3", "ATTESTATIONS_post_c3.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for r in rows:
    print(r["n"], r["argot"], "->", r["decode_qummi"], "| Lisan", r["Lisan"], r["Lisan_sans_prefixe"], "| Taj", r["Taj"], r["Taj_sans_prefixe"], "| argot L/T", r["argot_Lisan"], r["argot_Taj"])
