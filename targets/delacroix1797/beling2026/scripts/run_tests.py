#!/usr/bin/env python3
"""Tests 1, 2a and 2b of TEST_PLAN.md.

usage: run_tests.py CIPHER TESTTEXT TURNER OUTDIR [NPROC]
TESTTEXT: plain text file, one sentence per line (already final text).
"""
import json
import os
import random
import re
import sys
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import align_em as A

# eight fixed start settings: (mean-length scale, alpha, null weight)
CONF = [(1.0, 0.3, 0.02), (0.85, 0.3, 0.02), (1.15, 0.3, 0.02), (1.0, 1.0, 0.02),
        (1.0, 0.1, 0.02), (1.0, 0.3, 0.005), (1.3, 0.3, 0.02), (0.7, 0.3, 0.02)]

FR = set("le la les de des du et que qui dans pour par sur avec vous nous il elle est sont ont a au aux un une ce cette ces ne pas plus je me mon ma mes son sa ses leur leurs en y se si mais ou comme tout tous etre avoir fait ete citoyen ministre gouvernement republique".split())


def turner_sentences(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    raw = re.sub(r"-\s*\n\s*", "", raw)
    sents = []
    for p in re.split(r"\n\s*\n", raw):
        p = " ".join(p.split())
        ws = A.normalise(p)
        if len(ws) < 25:
            continue
        if sum(1 for w in ws if w in FR) / len(ws) < 0.32:
            continue
        for s in re.split(r"(?<=[.;:!?])\s+", p):
            w = [x for x in A.normalise(s) if not x.isdigit()]
            if len(w) >= 4:
                sents.append(w)
    return sents


def flat(sl):
    return [w for s in sl for w in s]


# ---------- Test 2a ----------

def cipher_repeat_pairs(cipher, nmin=3):
    """Maximal exact repeats of nmin or more groups: list of (i, j, n)."""
    n = len(cipher)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if cipher[i] != cipher[j]:
                continue
            if i > 0 and cipher[i - 1] == cipher[j - 1]:
                continue  # not maximal on the left
            L = 0
            while j + L < n and i + L < j and cipher[i + L] == cipher[j + L]:
                L += 1
            if L >= nmin:
                pairs.append((i, j, L))
    return pairs


def repeat_score(cipher, words, pairs, tol=0.06):
    text = "".join(words)
    N = len(text)
    ntok = len(cipher)
    w = tol * N
    supported = 0
    detail = []
    for (i, j, n) in pairs:
        need = 2 * n
        pi = (i + n / 2.0) * N / ntok
        pj = (j + n / 2.0) * N / ntok
        a0, a1 = max(0, int(pi - w - need)), min(N, int(pi + w + need))
        b0, b1 = max(0, int(pj - w - need)), min(N, int(pj + w + need))
        found = None
        seen = {}
        for a in range(a0, a1 - need + 1):
            centre = a + need / 2.0
            if abs(centre - pi) <= w:
                seen.setdefault(text[a:a + need], a)
        for b in range(b0, b1 - need + 1):
            centre = b + need / 2.0
            if abs(centre - pj) <= w and text[b:b + need] in seen:
                a = seen[text[b:b + need]]
                if b >= a + need:      # two distinct, non-overlapping occurrences
                    found = (a, b)
                    break
        if found:
            supported += 1
            a, b = found
            # extend for the report
            e = need
            while b + e < N and a + e < b and text[a + e] == text[b + e]:
                e += 1
            s = 0
            while a - s - 1 >= 0 and text[a - s - 1] == text[b - s - 1] and a - s - 1 >= 0 and b - s - 1 >= a + e:
                s += 1
            detail.append((i, j, n, text[a - s:a + e]))
        else:
            detail.append((i, j, n, None))
    return supported / max(len(pairs), 1), detail


# ---------- Test 2b ----------

def fit_one(job):
    name, cipher, words, ci = job
    mu, al, pn = CONF[ci]
    A.P_NULL = pn
    r = A.fit(cipher, words, alpha=al, mu_scale=mu)
    if r is None:
        return name, ci, None
    return name, ci, {"S_tok": r["S_tok"], "S_let": r["S_let"], "loglik": r["loglik"],
                      "spans": r["spans"], "chunks": r["chunks"]}


def main():
    cipher_path, text_path, turner_path, outdir = sys.argv[1:5]
    nproc = int(sys.argv[5]) if len(sys.argv) > 5 else 14
    os.makedirs(outdir, exist_ok=True)
    cipher = A.read_cipher(cipher_path)
    sents = [A.normalise(l) for l in open(text_path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    sents = [s for s in sents if s]
    words = flat(sents)
    N = sum(map(len, words))
    rng = random.Random(1797)
    out = {"n_groups": len(cipher), "n_types": len(set(cipher)), "words": len(words), "letters": N}

    # Test 1
    lpg, gpw = N / len(cipher), len(cipher) / len(words)
    out["test1"] = {"letters_per_group": lpg, "groups_per_word": gpw,
                    "pass": bool(2.0 <= lpg <= 6.0 and 1.0 <= gpw <= 2.5)}
    print("TEST 1", json.dumps(out["test1"]), flush=True)

    # controls
    units = sents if len(sents) >= 8 else [words[i:i + 12] for i in range(0, len(words), 12)]
    tsents = turner_sentences(turner_path)

    def shuffled():
        u = units[:]
        rng.shuffle(u)
        return flat(u)

    def turner():
        s0 = rng.randrange(0, len(tsents) - 400)
        o, k = [], s0
        while sum(map(len, o)) < N:
            o.extend(tsents[k])
            k += 1
        return o

    # Test 2a
    pairs = cipher_repeat_pairs(cipher)
    R, detail = repeat_score(cipher, words, pairs)
    ctrl_R = [repeat_score(cipher, shuffled(), pairs)[0] for _ in range(100)] + \
             [repeat_score(cipher, turner(), pairs)[0] for _ in range(100)]
    out["test2a"] = {"pairs": len(pairs), "R": R, "control_max": max(ctrl_R),
                     "control_mean": sum(ctrl_R) / len(ctrl_R),
                     "control_shuffled_max": max(ctrl_R[:100]), "control_turner_max": max(ctrl_R[100:]),
                     "pass": bool(R >= 0.60 and R > max(ctrl_R)),
                     "detail": detail, "controls": ctrl_R}
    print("TEST 2a", json.dumps({k: v for k, v in out["test2a"].items() if k not in ("detail", "controls")}), flush=True)
    for d in detail:
        print("   pair", d, cipher[d[0]:d[0] + d[2]], flush=True)

    # Test 2b (DRY_RUN=1 in the environment shrinks the controls, for checking the script only)
    nctl = 3 if os.environ.get("DRY_RUN") else 40
    jobs = [("real", cipher, words, ci) for ci in range(len(CONF))]
    for c in range(nctl):
        w = shuffled()
        jobs += [("shuf%02d" % c, cipher, w, ci) for ci in range(len(CONF))]
    for c in range(nctl):
        w = turner()
        jobs += [("turn%02d" % c, cipher, w, ci) for ci in range(len(CONF))]
    res = {}
    with Pool(nproc) as pool:
        for name, ci, r in pool.imap_unordered(fit_one, jobs, chunksize=1):
            res.setdefault(name, {})[ci] = r
            if name == "real":
                print("   real conf", ci, None if r is None else round(r["S_tok"], 3), flush=True)
    best = {}
    for name, d in res.items():
        vals = [(v["S_tok"], ci) for ci, v in d.items() if v]
        best[name] = max(vals) if vals else (0.0, -1)
    S, ci_best = best["real"]
    ctrl = sorted(v[0] for k, v in best.items() if k != "real")
    out["test2b"] = {"S": S, "best_conf": ci_best, "per_conf": {ci: (v["S_tok"] if v else None) for ci, v in res["real"].items()},
                     "control_max": ctrl[-1], "control_mean": sum(ctrl) / len(ctrl), "controls": ctrl,
                     "control_shuffled_max": max(v[0] for k, v in best.items() if k.startswith("shuf")),
                     "control_turner_max": max(v[0] for k, v in best.items() if k.startswith("turn")),
                     "pass": bool(S >= 0.50 and S > ctrl[-1])}
    print("TEST 2b", json.dumps({k: v for k, v in out["test2b"].items() if k != "controls"}), flush=True)
    json.dump(out, open(os.path.join(outdir, "tests_1_2.json"), "w"), indent=1)
    r = res["real"][ci_best]
    json.dump({"conf": ci_best, "cipher": cipher, "words": words, "spans": r["spans"], "chunks": r["chunks"]},
              open(os.path.join(outdir, "alignment_full.json"), "w"), indent=1)
    v = out["test1"]["pass"] and out["test2b"]["pass"]
    print("VERDICT:", "PASS" if v else ("NOT SETTLED" if out["test2a"]["pass"] else "MISS"), flush=True)


if __name__ == "__main__":
    main()
