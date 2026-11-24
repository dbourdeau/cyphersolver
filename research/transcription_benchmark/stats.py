"""Check 2: confidence intervals and paired comparisons between models.

Hierarchical bootstrap: resample the ten documents with replacement, and within each drawn document resample its three
passes with replacement (per model; passes are not paired across models, documents are). The statistic is the pooled
error rate (total edits / total reference signs). Differences between models use the same document draws, so they are
paired by document. Also a sign test over documents (how many of the ten documents have the lower three-pass mean).

Usage:
  python stats.py                 # raw scores: scores.json (Sonnet), scores_opus.json, scores_fable.json
  python stats.py --adjudicated   # adjudication/summary.json (edits against the adjudicated reference)
Writes stats.json or stats_adjudicated.json next to this file.
"""
import argparse
import collections
import json
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ALNUM = {"carpio_R1009", "carpio_R1010", "ferdinand_R1889", "ferdinand_R1890"}
SUBSETS = {"all": lambda d: True, "digit-only": lambda d: d not in ALNUM, "letter-and-digit": lambda d: d in ALNUM}


def load(adjudicated):
    """model -> doc -> list of (edits, ref_len) per pass"""
    data = collections.defaultdict(lambda: collections.defaultdict(list))
    if adjudicated:
        for r in json.load(open(os.path.join(HERE, "adjudication", "summary.json")))["rows"]:
            data[r["model"]][r["doc"]].append((r["edits_adj"], r["adj_len"]))
    else:
        for model, f in (("sonnet", "scores.json"), ("opus", "scores_opus.json"), ("fable", "scores_fable.json")):
            for r in json.load(open(os.path.join(HERE, f))):
                data[model][r["doc"]].append((r["edits"], r["ref_digits"]))
    return data


def pooled(rows):
    return sum(e for e, _ in rows) / sum(n for _, n in rows)


def sign_test(wins, n):
    """two-sided exact binomial p for wins out of n at p=0.5"""
    k = max(wins, n - wins)
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n)


def main(adjudicated, B=10000, seed=20261119):
    data = load(adjudicated)
    models = [m for m in ("sonnet", "opus", "fable") if m in data]
    rng = random.Random(seed)
    out = {}
    for sub, keep in SUBSETS.items():
        docs = sorted(d for d in data[models[0]] if keep(d))
        point = {m: pooled([r for d in docs for r in data[m][d]]) for m in models}
        boots = {m: [] for m in models}
        for _ in range(B):
            draw = [rng.choice(docs) for _ in docs]
            for m in models:
                rows = []
                for d in draw:
                    ps = data[m][d]
                    rows += [rng.choice(ps) for _ in ps]
                boots[m].append(pooled(rows))
        res = {"documents": len(docs), "models": {}}
        for m in models:
            b = sorted(boots[m])
            res["models"][m] = {"pooled": round(point[m], 4), "ci95": [round(b[int(0.025 * B)], 4), round(b[int(0.975 * B)], 4)]}
        res["pairs"] = {}
        for i, a in enumerate(models):
            for c in models[i + 1:]:
                diff = sorted(x - y for x, y in zip(boots[a], boots[c]))
                p = 2 * min(sum(1 for x in diff if x <= 0), sum(1 for x in diff if x >= 0)) / B
                means = {m: {d: pooled(data[m][d]) for d in docs} for m in (a, c)}
                wins = sum(1 for d in docs if means[c][d] < means[a][d])
                res["pairs"][f"{a} - {c}"] = {"diff": round(point[a] - point[c], 4),
                                              "ci95": [round(diff[int(0.025 * B)], 4), round(diff[int(0.975 * B)], 4)],
                                              "bootstrap_p": round(min(1.0, p), 4),
                                              f"docs_where_{c}_lower": f"{wins} of {len(docs)}",
                                              "sign_test_p": round(sign_test(wins, len(docs)), 4)}
        out[sub] = res
        print(f"== {sub} ({len(docs)} documents)")
        for m in models:
            r = res["models"][m]
            print(f"  {m:7s} {100 * r['pooled']:5.2f}%  95% CI {100 * r['ci95'][0]:5.2f} - {100 * r['ci95'][1]:5.2f}")
        for k, r in res["pairs"].items():
            print(f"  {k:16s} diff {100 * r['diff']:+5.2f} pts  CI {100 * r['ci95'][0]:+5.2f} to {100 * r['ci95'][1]:+5.2f}"
                  f"  boot p {r['bootstrap_p']:.3f}  {[v for kk, v in r.items() if kk.startswith('docs_')][0]}  sign p {r['sign_test_p']:.3f}")
    json.dump(out, open(os.path.join(HERE, "stats_adjudicated.json" if adjudicated else "stats.json"), "w"), indent=1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--adjudicated", action="store_true")
    main(ap.parse_args().adjudicated)
