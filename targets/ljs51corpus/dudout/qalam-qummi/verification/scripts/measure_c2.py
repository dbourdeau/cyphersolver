"""Mesure (c2) : clé réciproque du qalam qummī d'Ibn al-Durayhim (via Qalqashandī, Ṣubḥ 9:230) appliquée à l'argot.
Une seule exécution, après confirmation que le hash du MANIFEST_c2 est posté. Refuse si RESULT_c2.json existe.
Usage : /usr/bin/python3 -E measure_c2.py <dossier ljs51-qummi>
"""
import sys, os, json, random, time, hashlib
D = sys.argv[1]
sys.path.insert(0, os.path.join(D, "scripts"))
from qummi_lib import *

OUT = os.path.join(D, "mesure", "RESULT_c2.json")
if os.path.exists(OUT):
    sys.exit("RESULT_c2.json existe déjà : refus.")
P = json.load(open(os.path.join(D, "gel", "PREREG_c2.json"), encoding="utf-8"))
P1 = json.load(open(os.path.join(D, "gel", "PREREG_c.json"), encoding="utf-8"))
train = []
for f in P1["corpus_files"]:
    train += read_openiti(os.path.join(P1["corpus_dir"], f))
LM = build_lm(train); lex = build_lexicon(train, P1["lexicon_mincount"])
cant = normalize(open(os.path.join(D, "donnees", "cant_90.txt"), encoding="utf-8").read())


def involution(pairs):
    m = {c: c for c in ALPHA}
    for a, b in pairs:
        m[a], m[b] = b, a
    return m


def run(m, text):
    d = "".join(m.get(c, c) for c in text)
    return d, score_idx(LM, encode(d)), lexcov(d, lex)


variants = {}
for name, pairs in P["keys"].items():
    d, ll, lx = run(involution(pairs), cant)
    variants[name] = {"decoded": d, "ll": ll, "lexcov": lx}

rng = random.Random(P["seed"])
ctrl = []
letters = [c for c in ALPHA if c != "ظ"]
for j in range(P["controls"]):
    L = letters[:]; rng.shuffle(L)
    pairs = [(L[2 * i], L[2 * i + 1]) for i in range(len(L) // 2)]
    d, ll, lx = run(involution(pairs), cant)
    ctrl.append((ll, lx, d))
lls = [c[0] for c in ctrl]; lxs = [c[1] for c in ctrl]
main = variants[P["main_key"]]
passed = main["ll"] >= max(lls) and main["lexcov"] >= P["criterion"]["lexcov_min"] and main["lexcov"] >= max(lxs)
res = {"prereg_c2_sha256": hashlib.sha256(open(os.path.join(D, "gel", "PREREG_c2.json"), "rb").read()).hexdigest(),
       "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "variants": variants,
       "controls_ll_max": max(lls), "controls_ll_mean": sum(lls) / len(lls),
       "rank_main_ll": 1 + sum(x >= main["ll"] for x in lls),
       "controls_lexcov_max": max(lxs), "controls_lexcov_mean": sum(lxs) / len(lxs),
       "rank_main_lexcov": 1 + sum(x >= main["lexcov"] for x in lxs),
       "best_control": ctrl[lls.index(max(lls))][2],
       "verdict_criterion": "PASS (couche arabe)" if passed else "FAIL (pas de vers arabe ordinaire sous la clé qummī)"}
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
