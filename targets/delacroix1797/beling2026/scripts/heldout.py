#!/usr/bin/env python3
"""Test 3 of TEST_PLAN.md: table from the training part, scored on the held-out part.

usage: heldout.py train   CIPHER ALIGNMENT_FULL.json N_TRAIN OUTDIR [NPROC]
       heldout.py score   CIPHER ALIGNMENT_FULL.json N_TRAIN OUTDIR
"""
import hashlib
import json
import os
import random
import sys
from multiprocessing import Pool

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import align_em as A
from run_tests import CONF

K = A.K


def words_split(words, letter_pos):
    """Split the word list at a letter position (moved to the nearest word boundary at or after it)."""
    pos = 0
    for w_i, w in enumerate(words):
        if pos >= letter_pos:
            return words[:w_i], words[w_i:]
        pos += len(w)
    return words, []


def fit_one(job):
    cipher, words, ci = job
    mu, al, pn = CONF[ci]
    A.P_NULL = pn
    r = A.fit(cipher, words, alpha=al, mu_scale=mu)
    return ci, (None if r is None else {"S_tok": r["S_tok"], "chunks": r["chunks"]})


def table_supported(cipher, chunks):
    by = {}
    for g, c in zip(cipher, chunks):
        by.setdefault(g, []).append(c)
    tab = {}
    for g, cs in by.items():
        cnt = {}
        for c in cs:
            if c:
                cnt[c] = cnt.get(c, 0) + 1
        if not cnt:
            continue
        c, m = sorted(cnt.items(), key=lambda kv: (-kv[1], -len(kv[0]), kv[0]))[0]
        if m >= 2:
            tab[g] = {"chunk": c, "support": m, "seen": len(cs)}
    return tab


def embed_score(cipher, text, table):
    """Place the groups on the text in order so that the number of LETTERS
    covered by table chunks standing at their place is as large as possible
    (any group may otherwise take 0..K letters). Returns (letters, hits)."""
    N = len(text)
    NEG = -10 ** 9
    V = np.full(N + 1, NEG, dtype=np.int64)
    Hn = np.zeros(N + 1, dtype=np.int64)
    V[0] = 0
    match_cache = {}
    for g in cipher:
        best = V.copy()                       # takes 0 letters
        bh = Hn.copy()
        for k in range(1, K + 1):
            better = V[:N + 1 - k] > best[k:]
            best[k:] = np.where(better, V[:N + 1 - k], best[k:])
            bh[k:] = np.where(better, Hn[:N + 1 - k], bh[k:])
        if g in table:
            c = table[g]
            L = len(c)
            m = match_cache.get(c)
            if m is None:
                m = np.array([text.startswith(c, j) for j in range(N + 1)])
                match_cache[c] = m
            cand = np.where(m[:N + 1 - L], V[:N + 1 - L] + L, NEG)
            better = cand > best[L:]
            best[L:] = np.where(better, cand, best[L:])
            bh[L:] = np.where(better, Hn[:N + 1 - L] + 1, bh[L:])
        V, Hn = best, bh
    if V[N] <= NEG // 2:
        return None
    return int(V[N]), int(Hn[N])


def main():
    mode, cipher_path, align_path, n_train, outdir = sys.argv[1:6]
    n_train = int(n_train)
    cipher = A.read_cipher(cipher_path)
    full = json.load(open(align_path))
    words = full["words"]
    boundary = full["spans"][n_train - 1][1]
    w_train, w_held = words_split(words, boundary)
    c_train, c_held = cipher[:n_train], cipher[n_train:]
    tpath = os.path.join(outdir, "table_train_frozen.json")
    if mode == "train":
        nproc = int(sys.argv[6]) if len(sys.argv) > 6 else 8
        with Pool(nproc) as pool:
            res = dict(pool.map(fit_one, [(c_train, w_train, ci) for ci in range(len(CONF))]))
        ci = max((v["S_tok"], k) for k, v in res.items() if v)[1]
        tab = table_supported(c_train, res[ci]["chunks"])
        json.dump({"conf": ci, "S_train": res[ci]["S_tok"], "n_train": n_train, "boundary_letter": boundary,
                   "train_words": len(w_train), "table": {str(g): v for g, v in sorted(tab.items())},
                   "train_chunks": res[ci]["chunks"]}, open(tpath, "w"), indent=1)
        h = hashlib.sha256(open(tpath, "rb").read()).hexdigest()
        open(tpath + ".sha256", "w").write(h + "  table_train_frozen.json\n")
        print("table entries", len(tab), "S_train", res[ci]["S_tok"], "sha256", h)
        return
    tabj = json.load(open(tpath))
    table = {int(g): v["chunk"] for g, v in tabj["table"].items()}
    text = "".join(w_held)
    predicted = sum(1 for g in c_held if g in table)
    letters, hits = embed_score(c_held, text, table)
    rng = random.Random(649)
    ctrl = []
    gs, cs = list(table.keys()), list(table.values())
    for _ in range(200):
        sh = cs[:]
        rng.shuffle(sh)
        ctrl.append(embed_score(c_held, text, dict(zip(gs, sh)))[0] / max(len(text), 1))
    ctrl.sort()
    HL = letters / max(len(text), 1)
    H = hits / max(predicted, 1)
    p99 = ctrl[int(0.99 * len(ctrl)) - 1]
    mean = sum(ctrl) / len(ctrl)
    out = {"held_tokens": len(c_held), "held_letters": len(text), "table_entries": len(table),
           "predicted_tokens": predicted, "hits": hits, "H_tokens": H, "letters_covered": letters, "H_letters": HL,
           "control_p99": p99, "control_max": ctrl[-1], "control_mean": mean,
           "pass": bool(predicted >= 40 and H >= 0.70 and HL > p99 and HL >= 2 * mean)}
    json.dump(out, open(os.path.join(outdir, "test3_heldout.json"), "w"), indent=1)
    print("TEST 3", json.dumps(out))


if __name__ == "__main__":
    main()
