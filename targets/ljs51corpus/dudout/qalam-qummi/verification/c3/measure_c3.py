"""Mesure (c3) : clé du vers « pahlavi » (38v l.4) appliquée à l'argot de 37v.12, témoin négatif nommé contre la clé
qummī de c2. Même modèle de langue, même lexique, mêmes 200 témoins que c2 (seed 20261129, même code).
Une seule exécution, après confirmation que le hash de MANIFEST_c3_v1.sha256 est posté. Refuse si RESULT_c3.json existe.
Usage : /usr/bin/python3 -E measure_c3.py <dossier ljs51-qummi>
"""
import sys, os, json, random, time, hashlib
from itertools import product
D = sys.argv[1]
sys.path.insert(0, os.path.join(D, "scripts"))
from qummi_lib import *

OUT = os.path.join(D, "c3", "RESULT_c3.json")
if os.path.exists(OUT):
    sys.exit("RESULT_c3.json existe déjà : refus.")
P3 = json.load(open(os.path.join(D, "c3", "PREREG_c3.json"), encoding="utf-8"))
P2 = json.load(open(os.path.join(D, "gel", "PREREG_c2.json"), encoding="utf-8"))
P1 = json.load(open(os.path.join(D, "gel", "PREREG_c.json"), encoding="utf-8"))
R2 = json.load(open(os.path.join(D, "mesure", "RESULT_c2.json"), encoding="utf-8"))
train = []
for f in P1["corpus_files"]:
    train += read_openiti(os.path.join(P1["corpus_dir"], f))
LM = build_lm(train); lex = build_lexicon(train, P1["lexicon_mincount"])
cant = normalize(open(os.path.join(D, "donnees", "cant_90.txt"), encoding="utf-8").read())
gloss = set()
for ln in open(os.path.join(D, "donnees", "glossaire_38r12_38v2.txt"), encoding="utf-8"):
    if not ln.startswith("#"):
        gloss.update(normalize(ln).split())
FUNC = set("لا ولا ما من في عن على الى ان او و يا با شي قد لم لن ثم بل مع هو هي".split())


def pairs_of(s):
    return [(p[0], p[1]) for p in s.split()]


def involution(pairs):
    m = {c: c for c in ALPHA}
    used = set()
    for a, b in pairs:
        assert a not in used and b not in used, (a, b)
        used |= {a, b}
        m[a], m[b] = b, a
    return m


def run(m, text):
    d = "".join(m.get(c, c) for c in text)
    ws = d.split()
    lexw = [w for w in ws if w in lex]
    full = [w for w in ws if w not in FUNC]
    return {"decoded": d, "ll": score_idx(LM, encode(d)), "lexcov": lexcov(d, lex),
            "lex_words": lexw, "lex_n": len(lexw), "n_words": len(ws),
            "content_lexcov": (sum(w in lex for w in full) / len(full)) if full else 0.0,
            "glossary_hits": [w for w in ws if w in gloss]}


# --- clé de référence : qummī (c2), recalculée
qummi = run(involution(P2["keys"][P2["main_key"]]), cant)

# --- variantes pahlavi (critère) : texte du PREREG_c3, lu tel quel
V = P3["decision_1_emendation_dh_dj"]["variantes_critere"]
pahl = {}
for name, txt in V.items():
    spec = txt.split("(")[0].strip()
    pahl[name] = run(involution(pairs_of(spec)), cant)
    pahl[name]["pairs"] = spec

# --- complétions descriptives de A
specA = V["pahlavi_A_emende_dj"].split("(")[0].strip()
compl = {}
for extra in ["بر فظ", "بف رظ", "بظ رف"]:
    r = run(involution(pairs_of(specA + " " + extra)), cant)
    compl["A+" + extra.replace(" ", "+")] = r

# --- les mêmes 200 témoins que c2 (code identique à measure_c2.py)
rng = random.Random(P2["seed"])
ctrl = []
letters = [c for c in ALPHA if c != "ظ"]
for j in range(P2["controls"]):
    L = letters[:]; rng.shuffle(L)
    pairs = [(L[2 * i], L[2 * i + 1]) for i in range(len(L) // 2)]
    m = {c: c for c in ALPHA}
    for a, b in pairs:
        m[a], m[b] = b, a
    d = "".join(m.get(c, c) for c in cant)
    ctrl.append((score_idx(LM, encode(d)), lexcov(d, lex)))
lls = [c[0] for c in ctrl]; lxs = [c[1] for c in ctrl]
integrity = {
    "qummi_ll_egal_c2": abs(qummi["ll"] - R2["variants"][P2["main_key"]]["ll"]) < 1e-6,
    "qummi_lexcov_egal_c2": abs(qummi["lexcov"] - R2["variants"][P2["main_key"]]["lexcov"]) < 1e-9,
    "temoins_ll_max_egal_c2": abs(max(lls) - R2["controls_ll_max"]) < 1e-6,
    "temoins_lexcov_max_egal_c2": abs(max(lxs) - R2["controls_lexcov_max"]) < 1e-9,
}
for k, r in list(pahl.items()) + list(compl.items()):
    r["rank_ll_vs_200"] = 1 + sum(x >= r["ll"] for x in lls)
    r["rank_lexcov_vs_200"] = 1 + sum(x >= r["lexcov"] for x in lxs)
qummi["rank_ll_vs_200"] = 1 + sum(x >= qummi["ll"] for x in lls)

max_ll = max(r["ll"] for r in pahl.values())
max_lx = max(r["lexcov"] for r in pahl.values())
thr_ll = qummi["ll"] - 39.0
thr_lx = qummi["lexcov"] - 0.20
ok_ll = max_ll <= thr_ll
ok_lx = max_lx <= thr_lx
if ok_ll and ok_lx:
    verdict = "CONFIRMEE"
elif max_ll >= qummi["ll"] or max_lx >= qummi["lexcov"]:
    verdict = "INVERSEE (donc INFIRMEE)"
else:
    verdict = "INFIRMEE"

res = {"prereg_c3_sha256": hashlib.sha256(open(os.path.join(D, "c3", "PREREG_c3.json"), "rb").read()).hexdigest(),
       "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
       "integrite_vs_c2": integrity,
       "undecoded_cant_ll": score_idx(LM, encode(cant)),
       "qummi_reference": qummi,
       "pahlavi_critere": pahl,
       "pahlavi_completions_descriptif": compl,
       "controls_ll_max": max(lls), "controls_ll_mean": sum(lls) / len(lls),
       "controls_lexcov_max": max(lxs), "controls_lexcov_mean": sum(lxs) / len(lxs),
       "seuil_ll": thr_ll, "max_ll_pahlavi": max_ll, "seuil_ll_tenu": ok_ll,
       "seuil_lexcov": thr_lx, "max_lexcov_pahlavi": max_lx, "seuil_lexcov_tenu": ok_lx,
       "verdict_prediction": verdict}
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
