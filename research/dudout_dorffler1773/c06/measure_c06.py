"""C06 measure (Dorffler, catalogue 1773): share of the clerk's letters reproduced by the decode.

    python3 -I measure_c06.py TABLE.json T-cipher.txt G-gloss.txt [TABLE2.json ...]

Metric = M. German's "clerk's letters" measure (cyphersolver PR #742, scripts/p5.py, functions norm,
local_match, gloss_score, shuffled), re-implemented here unchanged in substance:
  - letters only, lower case, umlauts folded, ss for sharp s (norm);
  - for each gloss line: the letters it shares, IN ORDER, with the decode of the cipher line directly
    under it plus the next cipher line of the same half-page, counting only matching runs of >= 3 letters
    (difflib.SequenceMatcher, autojunk off);
  - S = sum of matched letters / sum of gloss letters, over every gloss line of >= 4 letters.
It ignores word boundaries entirely (lesson of C05).
Controls: 200 tables = the first table with its values shuffled among its numbers, random.Random(20261117).
Only the FIRST table decides. Further tables are printed for information only.

T-cipher.txt: lines "<id> n.n.n ..." where <id> = <img><L|R>-<NN>[a-z]; '?' = unreadable group (no value).
G-gloss.txt : lines "<id> text" where <id> is the cipher line directly UNDER the gloss; '[?]' = illegible.
"""
import difflib
import json
import random
import sys
import unicodedata


def norm(text):
    t = text.lower().replace("ß", "ss").replace("ÿ", "y").replace("ſ", "s")
    t = unicodedata.normalize("NFKD", t)
    return "".join(ch for ch in t if "a" <= ch <= "z")


def load_key(path):
    return {k: v for k, v in json.load(open(path, encoding="utf-8")).items() if not k.startswith("_")}


def read_ids(path):
    out = []
    for l in open(path, encoding="utf-8"):
        l = l.rstrip("\n")
        if not l.strip() or l.startswith("#"):
            continue
        i, _, rest = l.partition(" ")
        out.append((i, rest.strip()))
    return out


def pairs_of(tpath, gpath):
    cipher = read_ids(tpath)
    order = [i for i, _ in cipher]
    nums = {i: [g for g in s.replace(" ", ".").split(".") if g] for i, s in cipher}
    half = lambda i: i.split("-")[0]
    pairs = []
    for gid, gtext in read_ids(gpath):
        if gid not in nums:
            sys.exit("gloss id without cipher line: " + gid)
        k = order.index(gid)
        ids = [gid] + [j for j in order[k + 1:k + 2] if half(j) == half(gid)]
        ns = [n for j in ids for n in nums[j] if n.isdigit()]
        g = norm(gtext.replace("[?]", ""))
        if len(g) >= 4 and ns:
            pairs.append({"id": gid, "gloss": g, "nums": ns})
    return pairs


def local_match(gloss, dec):
    if not dec:
        return 0
    sm = difflib.SequenceMatcher(None, gloss, dec, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3)


def gloss_score(key, pairs):
    hit = tot = 0
    for p in pairs:
        dec = "".join(norm(key.get(n, "")) for n in p["nums"])
        hit += local_match(p["gloss"], dec)
        tot += len(p["gloss"])
    return hit / max(tot, 1)


def shuffled(key, rng):
    ks = list(key)
    vs = [key[k] for k in ks]
    rng.shuffle(vs)
    return dict(zip(ks, vs))


def main(a):
    tabs, tpath, gpath = [a[0]] + a[3:], a[1], a[2]
    pairs = pairs_of(tpath, gpath)
    ngroups = sum(len([g for g in s.replace(" ", ".").split(".") if g]) for _, s in read_ids(tpath))
    print("pairs %d | gloss letters %d | groups in scored pairs %d | cipher groups in file %d" % (
        len(pairs), sum(len(p["gloss"]) for p in pairs), sum(len(p["nums"]) for p in pairs), ngroups))
    for j, t in enumerate(tabs):
        key = load_key(t)
        s = gloss_score(key, pairs)
        rng = random.Random(20261117)
        ctl = sorted(gloss_score(shuffled(key, rng), pairs) for _ in range(200))
        tag = "DECIDES" if j == 0 else "info only"
        print("%-16s S = %.4f | controls (200) mean %.4f p99 %.4f max %.4f | margin %+.4f | %s" % (
            t.split("/")[-1], s, sum(ctl) / 200, ctl[197], ctl[-1], s - ctl[-1], tag))
        if j == 0:
            print("PASS" if (s >= THRESH and s >= ctl[-1] + MARGIN) else "FAIL",
                  "(rule: S >= %.2f AND S >= max(controls) + %.2f)" % (THRESH, MARGIN))
    for p in pairs:
        key = load_key(tabs[0])
        dec = "".join(norm(key.get(n, "")) for n in p["nums"])
        print("%-10s %.2f  G=%s\n%-10s       D=%s" % (p["id"], local_match(p["gloss"], dec) / len(p["gloss"]), p["gloss"], "", dec))


THRESH = 0.70
MARGIN = 0.30

if __name__ == "__main__":
    main(sys.argv[1:])
