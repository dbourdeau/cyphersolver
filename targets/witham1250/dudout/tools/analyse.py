# -*- coding: utf-8 -*-
"""Formula fit and family alignment for the Alphen / Witham inscriptions.
Run: python3 -I analyse.py   (stdlib only; seed fixed)"""
import random, sys, os, collections, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import TARGETS, SIBLINGS, CONTROLS, FORMULAS, UNITS

random.seed(20261111)
N_NULL = 1000

def norm(s):
    return s.upper().replace("U", "V").replace("J", "I").replace("Y", "V").replace("W", "VV")

# ---------- 1. letter -> word statistics from the formula corpus ----------
def initial_stats():
    st = collections.defaultdict(collections.Counter)
    for f in FORMULAS.values():
        for w in f.split():
            st[w[0].upper()][w] += 1
    return st

# ---------- 2. formula runs ----------
def word_tokens(word):
    """possible letter strings standing for `word`: its initial, or a contraction unit"""
    out = {word[0]}
    for u, ws in UNITS.items():
        if word in ws:
            out.add(u)
    return out

def runs_in(s, formula, allow_ch=True):
    """all maximal contiguous runs: s[i:k] == concatenation of tokens of formula words j..j+m-1.
    Returns list of (i, k, j, m, words)."""
    s = s.lower()
    words = formula.split()
    toks = [ {t for t in word_tokens(w) if allow_ch or t != "ch"} for w in words ]
    res = []
    for i in range(len(s)):
        for j in range(len(words)):
            # DFS for longest
            best = None
            stack = [(i, j, [])]
            while stack:
                p, q, acc = stack.pop()
                if acc and (best is None or p - i > best[0] or (p - i == best[0] and len(acc) < len(best[1]))):
                    best = (p - i, list(acc))
                if q >= len(words):
                    continue
                for t in toks[q]:
                    if s.startswith(t, p):
                        stack.append((p + len(t), q + 1, acc + [words[q]]))
            if best and best[0] >= 2:
                res.append((i, i + best[0], j, len(best[1]), best[1]))
    return res

def best_runs(s, allow_ch=True, mirror=False):
    out = []
    for name, f in FORMULAS.items():
        for r in runs_in(s, f, allow_ch):
            out.append((r[1] - r[0], name, r))
        if mirror:
            rs = s[::-1]
            for r in runs_in(rs, f, allow_ch):
                out.append((r[1] - r[0], name + "(mirror)", r))
    out.sort(key=lambda x: -x[0])
    return out

def coverage(s, allow_ch=True, minlen=3):
    """letters covered by the union of runs of length >= minlen (any formula)"""
    cov = [False] * len(s)
    for L, name, r in best_runs(s, allow_ch):
        if L >= minlen:
            for p in range(r[0], r[1]):
                cov[p] = True
    return sum(cov)

def maxrun(s, allow_ch=True):
    b = best_runs(s, allow_ch)
    return b[0][0] if b else 0

def shuffled(s):
    l = list(s); random.shuffle(l); return "".join(l)

def null_test(s, stat, n=N_NULL):
    obs = stat(s)
    ge = sum(1 for _ in range(n) if stat(shuffled(s)) >= obs)
    return obs, (ge + 1) / (n + 1)

# ---------- 3. family alignment ----------
def lcsubstr(a, b):
    best = 0
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0] * (len(b) + 1)
        for j, y in enumerate(b):
            if x == y:
                cur[j + 1] = prev[j] + 1
                best = max(best, cur[j + 1])
        prev = cur
    return best

def lcsubstr_str(a, b):
    best, end = 0, 0
    prev = [0] * (len(b) + 1)
    for i, x in enumerate(a):
        cur = [0] * (len(b) + 1)
        for j, y in enumerate(b):
            if x == y:
                cur[j + 1] = prev[j] + 1
                if cur[j + 1] > best:
                    best, end = cur[j + 1], i + 1
        prev = cur
    return a[end - best:end]

def grams(s, n=3):
    return {s[i:i + n] for i in range(len(s) - n + 1)}

def family_stat(s, pool):
    """number of distinct trigrams of s found in any pool string"""
    pg = set().union(*[grams(p) for p in pool])
    return len(grams(s) & pg)

def main():
    rep = {}
    print("== 1. initial-letter statistics (formula corpus, %d texts, %d words)" %
          (len(FORMULAS), sum(len(f.split()) for f in FORMULAS.values())))
    st = initial_stats()
    for L in "NDXOCHWRVIBESMTFZ":
        c = st.get(L, collections.Counter())
        tot = sum(c.values())
        top = ", ".join("%s %d" % (w, k) for w, k in c.most_common(5))
        print("  %s  n=%3d  %s" % (L, tot, top))
    rep["initials"] = {L: dict(st[L].most_common(6)) for L in sorted(st)}

    print("\n== 2. formula runs (contiguous; letter = initial or nomen-sacrum contraction)")
    for t in ["witham_BL", "witham_new", "alphen_A", "alphen_B"]:
        s = TARGETS[t]
        b = best_runs(s, mirror=True)
        print("\n  %s  %s" % (t, s))
        seen = set()
        for L, name, r in b:
            key = (r[0], r[1], name)
            if L < 3 or key in seen:
                continue
            seen.add(key)
            print("    len %d  pos %d-%d  %-22s %s" % (L, r[0], r[1], name, " ".join(r[4])))
        for stat_name, fn in [("max run", maxrun), ("coverage>=3", coverage)]:
            obs, p = null_test(s, fn)
            print("    %s: obs %d / %d letters; p(shuffled >= obs) = %.3f" % (stat_name, obs, len(s), p))
            rep.setdefault(t, {})[stat_name] = {"obs": obs, "len": len(s), "p": round(p, 4)}
        obs, p = null_test(s, lambda x: maxrun(x, allow_ch=False))
        print("    max run without CH unit: obs %d; p = %.3f" % (obs, p))
        rep[t]["max run noCH"] = {"obs": obs, "p": round(p, 4)}

    print("\n== 3. family alignment (Witham vs published siblings; shuffle null n=%d)" % N_NULL)
    pool_main = [v[0] for k, v in SIBLINGS.items() if not k.endswith("*")]
    for t in ["witham_BL", "witham_new"]:
        s = TARGETS[t]
        print("\n  %s %s" % (t, s))
        for k, (v, src) in SIBLINGS.items():
            l = lcsubstr(s, v)
            if l >= 3:
                print("    %-14s LCSubstr %d '%s'" % (k, l, lcsubstr_str(s, v)))
        obs, p = null_test(s, lambda x: family_stat(x, pool_main))
        print("    distinct trigrams shared with sibling pool: %d; p(shuffled >= obs) = %.4f" % (obs, p))
        obs2, p2 = null_test(s, lambda x: max(lcsubstr(x, v) for v in pool_main))
        print("    longest common substring with any sibling: %d; p = %.4f" % (obs2, p2))
        rep.setdefault(t, {})["family_trigrams"] = {"obs": obs, "p": round(p, 4)}
        rep[t]["family_lcs"] = {"obs": obs2, "p": round(p2, 4)}
    print("\n  controls (same test):")
    for k, v in list(CONTROLS.items()) + [("alphen_A", TARGETS["alphen_A"]), ("alphen_B", TARGETS["alphen_B"])]:
        obs, p = null_test(v, lambda x: family_stat(x, pool_main), n=2000)
        print("    %-10s %-42s trigrams %2d p=%.4f" % (k, v, obs, p))
    json.dump(rep, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "RESULTS.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
