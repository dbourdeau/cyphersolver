# One run of TEST_PLAN_verify.md. Usage (from this folder): python -I run_verify.py
import csv, json, random, string, os
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = "RALLYTOTHEFRONT"
CLAIM = ("EXACTLYHOWLONGYOUWILLHOLDTHECITY" "RUNNINGOFTHETRAINSDEPENDS"
         "HOLDONUNTILNINEOCLOCKTOMORROW" "ADDITIONALTRAINSTHERE")
assert len(CLAIM) == 107
KNOWN = ["COMPLETEVICTORY", "COMERETRIBUTION", "MANCHESTERBLUFF", "OURNAVYOURPRIDE"]
SPLITS = {11: 6, 16: 2, 21: 4}   # line-end joins: split after this many letters (G25)

WORDS = set()
for w in open("/usr/share/dict/words", encoding="utf-8"):
    w = w.strip()
    if w.isalpha():
        WORDS.add(w.lower())

def load(name):
    rows = list(csv.DictReader(open(os.path.join(HERE, name, "transcription.tsv"), encoding="utf-8"), delimiter="\t"))
    groups = {}
    for r in rows:
        groups.setdefault(int(r["group"]), []).append(r)
    g22 = [[r for r in sorted(groups[g], key=lambda r: int(r["pos"]))] for g in sorted(groups)]
    return g22

def g25_of(g22):
    out = []
    for i, g in enumerate(g22, 1):
        if i in SPLITS:
            out += [g[:SPLITS[i]], g[SPLITS[i]:]]
        else:
            out.append(g)
    return out

def dec(text, key, off=0):
    return "".join(chr((ord(c) - ord(key[(i + off) % len(key)])) % 26 + 65) for i, c in enumerate(text))

def score(groups, key, off=0):
    flat = "".join(r["first"] for g in groups for r in g)
    p = dec(flat, key, off)
    n = 0; i = 0; words = []
    for g in groups:
        w = p[i:i + len(g)]; i += len(g); words.append(w)
        n += w.lower() in WORDS
    return n, words

rng = random.Random(20261115)
pool = sorted(w.upper() for w in WORDS if 2 <= len(w) <= 8)
rkeys = []
while len(rkeys) < 400:
    s = ""
    while len(s) < 15:
        s += rng.choice(pool)
    rkeys.append(s[:15])

res = {"key": KEY, "helpers": {}}
lines = []
for h in ["helperA", "helperB"]:
    g22 = load(h); g25 = g25_of(g22)
    assert len(g22) == 22 and len(g25) == 25, (h, len(g22), len(g25))
    flat = [r for g in g22 for r in g]
    assert len(flat) == 107, (h, len(flat))
    out = {}
    for lab, G in [("G22", g22), ("G25", g25)]:
        n, words = score(G, KEY)
        rnd = [score(G, k)[0] for k in rkeys]
        kn = {f"{k}@{o}": score(G, k, o)[0] for k in KNOWN for o in range(len(k))}
        out[lab] = {"words": n, "of": len(G), "plain_groups": words,
                    "random_max": max(rnd), "random_mean": sum(rnd) / len(rnd),
                    "random_hist": {str(v): rnd.count(v) for v in sorted(set(rnd))},
                    "known_max": max(kn.values()), "known_max_at": max(kn, key=kn.get),
                    "known_offset0": {k: kn[f"{k}@0"] for k in KNOWN}}
    # letter changes
    ct = "".join(r["first"] for r in flat)
    pt = dec(ct, KEY)
    ch = []
    for i, (r, a, b) in enumerate(zip(flat, pt, CLAIM)):
        if a != b:
            need = chr((ord(b) - 65 + ord(KEY[i % 15]) - 65) % 26 + 65)
            alts = [x.strip() for x in r["alts"].split(",") if x.strip()]
            ch.append({"cipher_pos": i + 1, "group": int(r["group"]), "pos": int(r["pos"]), "read": r["first"],
                       "alts": r["alts"], "conf": r["conf"], "gives": a, "claim": b, "needs": need,
                       "need_in_alts": need in alts, "note": r["note"]})
    out["plain"] = pt
    out["changes"] = ch
    res["helpers"][h] = out

def passes():
    ok = True; why = []
    for lab, mark in [("G25", 17), ("G22", 15)]:
        for h in res["helpers"]:
            d = res["helpers"][h][lab]
            if d["words"] < mark:
                ok = False; why.append(f"{h} {lab} {d['words']} < {mark}")
        low = min(res["helpers"][h][lab]["words"] for h in res["helpers"])
        cmax = max(max(res["helpers"][h][lab]["random_max"], res["helpers"][h][lab]["known_max"]) for h in res["helpers"])
        if not cmax < low:
            ok = False; why.append(f"{lab}: a control scored {cmax}, not below {low}")
    return ok, why
ok, why = passes()
res["PASS"] = ok; res["miss_reasons"] = why
json.dump(res, open(os.path.join(HERE, "results_verify.json"), "w"), indent=1)

for h, d in res["helpers"].items():
    lines.append(f"== {h}")
    lines.append("plain: " + d["plain"])
    for lab in ["G22", "G25"]:
        x = d[lab]
        lines.append(f"{lab}: words {x['words']}/{x['of']}; random keys max {x['random_max']} mean {x['random_mean']:.2f}; "
                     f"known keys max {x['known_max']} ({x['known_max_at']}); offset 0 {x['known_offset0']}")
        lines.append("   " + " ".join(x["plain_groups"]))
    nin = sum(c["need_in_alts"] for c in d["changes"])
    lines.append(f"letter changes: {len(d['changes'])}; needed letter among helper's alternatives: {nin}; not: {len(d['changes'])-nin}")
    for c in d["changes"]:
        lines.append(f"   pos {c['cipher_pos']:3d} g{c['group']}.{c['pos']} read {c['read']} alts [{c['alts']}] {c['conf']} -> gives {c['gives']}, claim {c['claim']} needs {c['needs']}  in alts: {c['need_in_alts']}  | {c['note']}")
lines.append(f"PASS: {ok}  {why}")
open(os.path.join(HERE, "results_verify.txt"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
