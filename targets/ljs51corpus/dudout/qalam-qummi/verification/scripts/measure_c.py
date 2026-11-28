"""Mesure UNIQUE (c) de ljs51-qummi — à ne lancer qu'après confirmation que l'empreinte du gel est postée (#1023).

Usage : /usr/bin/python3 -E measure_c.py <dossier ljs51-qummi>
Écrit mesure/RESULT_c.json et mesure/RESULT_c.md ; refuse si RESULT_c.json existe.
"""
import sys, os, json, random, time, hashlib
D = sys.argv[1]
sys.path.insert(0, os.path.join(D, "scripts"))
from qummi_lib import *

OUT = os.path.join(D, "mesure", "RESULT_c.json")
if os.path.exists(OUT):
    sys.exit("RESULT_c.json existe déjà : mesure unique, refus.")

P = json.load(open(os.path.join(D, "gel", "PREREG_c.json"), encoding="utf-8"))
CORP = P["corpus_dir"]
train = []
for f in P["corpus_files"]:
    train += read_openiti(os.path.join(CORP, f))
LM = build_lm(train); lex = build_lexicon(train, P["lexicon_mincount"])

cant = normalize(open(os.path.join(D, "donnees", "cant_90.txt"), encoding="utf-8").read())
assert len(cant.replace(" ", "")) == 90, len(cant)
rng = random.Random(P["seed"])
it, rs = P["anneal"]["iters"], P["anneal"]["restarts"]

t0 = time.time()
s_real, k_real = anneal(LM, encode(cant), rng, iters=it, restarts=rs)
dec_real = decode(encode(cant), k_real)
real = {"ll": s_real, "decoded": dec_real, "lexcov": lexcov(dec_real, lex),
        "key": {SYMS[i]: SYMS[int(k_real[i])] for i in sorted(set(int(x) for x in encode(cant))) if SYMS[i] != " "}}

ctrls = []
for j in range(P["controls"]):
    ct = shuffled_control(cant, rng)
    s, k = anneal(LM, encode(ct), rng, iters=it, restarts=rs)
    d = decode(encode(ct), k)
    ctrls.append({"ll": s, "lexcov": lexcov(d, lex), "decoded": d})

lls = [c["ll"] for c in ctrls]; lxs = [c["lexcov"] for c in ctrls]
mean = sum(lls) / len(lls); sd = (sum((x - mean) ** 2 for x in lls) / len(lls)) ** 0.5
rank = 1 + sum(x >= s_real for x in lls)

# H2 : tables explicites tirées de 38v l.4 / l.6 (lectures gelées) — rapportées, non décisives
H2 = {}
L4 = P["l4_letters"]; L6 = P["l6_letters"]
ABJ = [c for c in ABJAD if c != "ظ"]; HIJ = [c for c in ALPHA if c != "ظ"]
tables = {
    "l6->l4 (position)": table_key(L6, L4), "l4->l6 (position)": table_key(L4, L6),
    "l6dedup->abjad": table_key(dedup(L6), ABJ), "abjad->l6dedup": table_key(ABJ, dedup(L6)),
    "l6dedup->hija": table_key(dedup(L6), HIJ), "hija->l6dedup": table_key(HIJ, dedup(L6)),
    "l4dedup->abjad": table_key(dedup(L4), ABJ), "abjad->l4dedup": table_key(ABJ, dedup(L4)),
    "l4dedup->hija": table_key(dedup(L4), HIJ), "hija->l4dedup": table_key(HIJ, dedup(L4)),
}
for name, m in tables.items():
    d = apply_table(cant, m)
    ok = "·" not in d.replace(" ", "")
    H2[name] = {"decoded": d, "complete": ok,
                "ll": score_idx(LM, encode(d)) if ok else None, "lexcov": lexcov(d, lex)}

C = P["criterion"]
passed = (s_real >= max(lls)) and (real["lexcov"] >= C["lexcov_min"]) and (real["lexcov"] >= max(lxs) if C.get("lexcov_vs_best_control") else True)
res = {"prereg_sha256": hashlib.sha256(open(os.path.join(D, "gel", "PREREG_c.json"), "rb").read()).hexdigest(),
       "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "seconds": round(time.time() - t0, 1),
       "real": real, "controls_ll_max": max(lls), "controls_ll_mean": mean, "controls_ll_sd": sd,
       "z": (s_real - mean) / sd if sd else None, "rank_of_real": rank, "n_controls": len(lls),
       "controls_lexcov_max": max(lxs), "controls_lexcov_mean": sum(lxs) / len(lxs),
       "controls_lexcov_ge_070": sum(x >= 0.70 for x in lxs),
       "best_control_decoded": ctrls[lls.index(max(lls))]["decoded"],
       "H2_tables": H2, "verdict_criterion": "PASS (sous réserve du mètre)" if passed else "FAIL"}
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ("H2_tables",)}, ensure_ascii=False, indent=1))
for n, h in H2.items():
    print(n, round(h["lexcov"], 2), h["ll"], h["decoded"])
