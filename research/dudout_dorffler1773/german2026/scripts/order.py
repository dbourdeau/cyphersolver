"""Fill gaps in the word lists using their alphabetical order. Fit half only; the test half is scored once.

The word list (146-249) and the names list (250 and up) of TABLE-C04 are alphabetical: 89% and 99% of
entry pairs are in order. So a missing number must sort between its known neighbours. Candidates come from
the plain German of the letters themselves (no decryptions) and the decryptions of the fit half. Among the
candidates reproduced whole at least as often as the median established entry, a number gets the one that
best matches the fit-half decrypts it sits under. The test half and its
shuffled-key control are scored after every choice is made.

  python3 analysis/order.py check  KEY.json   # entries that break the alphabetical order
  python3 analysis/order.py fill   KEY.json   # -> data/key_order.json, data/order_changes.tsv
"""
import collections, json, os, random, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as P
import p5
from common import norm

LISTS = [(146, 249), (250, 999)]


def anchors(key, lo, hi):
    """Longest run of entries in alphabetical order (C04 entries that break the order are not anchors)."""
    items = sorted((int(n), norm(v)) for n, v in key.items() if n.isdigit() and lo <= int(n) <= hi and norm(v))
    best = [[it] for it in items]
    for i in range(len(items)):
        for j in range(i):
            if items[j][1] <= items[i][1] and len(best[j]) + 1 > len(best[i]):
                best[i] = best[j] + [items[i]]
    return max(best, key=len) if best else []


def window(n, anc):
    lo = max((a for a in anc if a[0] < n), default=None)
    hi = min((a for a in anc if a[0] > n), default=None)
    return (lo[1] if lo else ""), (hi[1] if hi else "~"), lo, hi


def vocabulary(lines, fit_pairs):
    words = collections.Counter()
    for r in lines:
        if r["tag"] == "L":  # plain German around the numbers: unsupervised, no decryptions
            for w in re.findall(r"[^\W\d_]{2,}", r["text"]):
                words[norm(w)] += 1
    fit_halves = {p["half"] for p in fit_pairs}
    for r in lines:
        if r["tag"] == "G" and r["half"] in fit_halves:
            for w in re.findall(r"[^\W\d_]{2,}", r["text"]):
                words[norm(w)] += 1
    for w in open(os.path.join(P.D, "bourdeau", "LEXICON.txt")):
        if norm(w):
            words[norm(w)] += 1
    return {w for w, c in words.items() if len(w) >= 2}


def covered(key, pairs, n):
    """Share of the places n occurs where its whole value sits inside a matched stretch (3+ letters)
    of the decrypt. A long wrong word picks up scattered partial matches; it is rarely covered whole."""
    import difflib
    hit = tot = 0
    for p in pairs:
        pieces = [norm(key.get(x, "")) for x in p["nums"]]
        dec = "".join(pieces)
        blocks = [b for b in difflib.SequenceMatcher(None, p["gloss"], dec, autojunk=False).get_matching_blocks() if b.size >= 3]
        pos = 0
        for x, pc in zip(p["nums"], pieces):
            if x == n:
                tot += 1
                hit += any(b.b <= pos and pos + len(pc) <= b.b + b.size for b in blocks)
            pos += len(pc)
    return hit / max(tot, 1)


def reference(key, fit, min_uses=30):
    """Median coverage of the established entries (30+ fit-half uses). Each number is scored against the
    decrypts over its own line and the line before, so even a correct entry sits near 0.33, not 1."""
    import statistics
    uses = collections.Counter(x for p in fit for x in p["nums"])
    return statistics.median(covered(key, [p for p in fit if n in p["nums"]], n)
                             for n in key if n.isdigit() and uses[n] >= min_uses)


def check(path):
    key = p5.load_key(path)
    for lo, hi in LISTS:
        anc = {a[0] for a in anchors(key, lo, hi)}
        bad = [(int(n), v) for n, v in key.items() if n.isdigit() and lo <= int(n) <= hi and norm(v) and int(n) not in anc]
        print("%d-%d: %d entries, %d in order, out of order: %s" % (
            lo, hi, len(anc) + len(bad), len(anc), sorted(bad)))


def fill(path, min_uses=3):
    key = p5.load_key(path)
    lines = p5.load_lines()
    pairs = p5.gloss_pairs(lines)
    fit = [p for p in pairs if p5.fold(p["half"]) == "fit"]
    test = [p for p in pairs if p5.fold(p["half"]) == "test"]
    vocab = vocabulary(lines, fit)
    cnt = collections.Counter(n for r in lines if r["tag"] == "L" for n in p5.nums_of(r) if n.isdigit())
    new, log = dict(key), []
    ref = reference(key, fit)
    print("reference coverage of established entries: %.2f" % ref)
    for lo, hi in LISTS:
        anc = anchors(key, lo, hi)
        for n in sorted((int(x) for x in cnt if x.isdigit() and not x.startswith("0") and lo <= int(x) <= hi
                         and x not in key and cnt[x] >= min_uses and not (len(x) == 4 and x.startswith("16")))):
            a, b, la, ha = window(n, anc)
            cands = sorted(w for w in vocab if a < w < b)
            mine = [p for p in fit if str(n) in p["nums"]]
            if not cands or len(mine) < 2:
                continue
            base = p5.gloss_score(new, mine)
            best, bc, bs = None, 0.0, base
            for w in cands:
                new[str(n)] = w
                c = covered(new, mine, str(n))
                if c < ref:
                    continue
                s = p5.gloss_score(new, mine)
                if s > bs:
                    best, bc, bs = w, c, s
            if best:
                new[str(n)] = best
                log.append((n, la and la[1], best, ha and ha[1], cnt[str(n)], len(mine), round(bc, 2), round(base, 3), round(bs, 3)))
            else:
                del new[str(n)]
    rng = random.Random(4)
    def rep(name, k):
        ctl = [p5.gloss_score(p5.shuffled(k, rng), test) for _ in range(200)]
        print("%-22s fit %.3f | test %d decrypts %.3f | shuffled mean %.3f max %.3f" % (
            name, p5.gloss_score(k, fit), len(test), p5.gloss_score(k, test), sum(ctl) / len(ctl), max(ctl)))
    rep(os.path.basename(path), key)
    rep("+ order fill", new)
    json.dump(dict(sorted(new.items(), key=lambda kv: int(kv[0])),
                   _source="%s + alphabetical-order fills chosen on the fit half, analysis/order.py" % os.path.basename(path)),
              open(os.path.join(P.D, "key_order.json"), "w"), ensure_ascii=False, indent=0)
    with open(os.path.join(P.D, "order_changes.tsv"), "w") as o:
        o.write("number\tafter\tnew\tbefore\tuses\tfit_pairs\tcovered\tfit_local_before\tfit_local_after\n")
        for row in log:
            o.write("\t".join(map(str, row)) + "\n")
    print("%d fills -> data/key_order.json, data/order_changes.tsv" % len(log))


if __name__ == "__main__":
    {"check": check, "fill": fill}[sys.argv[1]](sys.argv[2])
