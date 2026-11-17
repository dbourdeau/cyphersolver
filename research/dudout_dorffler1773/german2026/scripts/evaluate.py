"""Score a key against the clerk's decryptions: test half, fit half, fresh lines, each volume, with a shuffled-key control.

  CIPHER_DATA=transcription python3 scripts/evaluate.py ../table/TABLE-C04.json [more keys or TSVs of additions]
A .tsv argument (number, C04, new, ...) is applied on top of the first key.
Split, chosen by M. German before any key change: fit = 19/102 plus even pages elsewhere; test = odd pages outside 19/102.
Measure: share of decryption letters reproduced in order by the decoding, runs of 3+ letters only.
Harder controls (test half and fresh lines), 200 draws each: values shuffled only among numbers of the same kind
(letters 14-65, syllables 66-145, words and names 146+), and each decryption scored against the numbers of a
different cipher line (any line in the set, or a line of the same page-half).
"""
import csv, os, random, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p5
from common import norm


def kind(n):
    n = int(n)
    return "letter" if n <= 65 else "syllable" if n <= 145 else "word"


def shuffled_within_kind(key, rng):
    groups = {}
    for k in key:
        groups.setdefault(kind(k) if k.isdigit() else k, []).append(k)
    out = {}
    for ks in groups.values():
        vs = [key[k] for k in ks]
        rng.shuffle(vs)
        out.update(zip(ks, vs))
    return out


def wrong_lines(ps, rng, same_half):
    """Each decryption paired with the numbers of another line, never its own. A half with one line borrows from the set."""
    out = list(ps)
    groups = {}
    for i, p in enumerate(ps):
        groups.setdefault(p["half"] if same_half else "", []).append(i)
    for ix in groups.values():
        if len(ix) == 1:
            out[ix[0]] = dict(ps[ix[0]], nums=ps[rng.choice([j for j in range(len(ps)) if j != ix[0]])]["nums"])
            continue
        shift = rng.randrange(1, len(ix))
        rot = ix[shift:] + ix[:shift]       # the order inside a half is kept, so this pairs with a neighbouring line
        if not same_half:
            rng.shuffle(rot)                # any line in the set; a fixed point is replaced below
        for a, b in zip(ix, rot):
            out[a] = dict(ps[a], nums=ps[b]["nums"])
    return out


def main(args):
    base = p5.load_key(args[0])
    keys = [(os.path.basename(args[0]), base)]
    for a in args[1:]:
        if a.endswith(".tsv"):
            add = {r[0]: norm(r[2]) for r in list(csv.reader(open(a), delimiter="\t"))[1:] if r}
            keys.append(("+ " + os.path.basename(a), {**base, **add}))
        else:
            keys.append((os.path.basename(a), p5.load_key(a)))
    pairs = p5.gloss_pairs(p5.load_lines())
    sets = [("test half", [p for p in pairs if p5.fold(p["half"]) == "test"]),
            ("fit half", [p for p in pairs if p5.fold(p["half"]) == "fit"]),
            ("fresh lines", [p for p in pairs if p["half"].split("/")[0] not in p5.TRAIN_VOLS and p["half"][:-1] not in p5.SPENT])]
    for v in sorted({p["half"].split("/")[0] for p in pairs}):
        sets.append((v, [p for p in pairs if p["half"].startswith(v)]))
    rng = random.Random(21)
    for name, ps in sets:
        for kn, k in keys:
            ctl = [p5.gloss_score(p5.shuffled(k, rng), ps) for _ in range(200)]
            print("%-16s %-28s %.3f | shuffled mean %.3f, best of 200 %.3f | %d lines, %d letters" % (
                name, kn, p5.gloss_score(k, ps), sum(ctl) / 200, max(ctl), len(ps), sum(len(p["gloss"]) for p in ps)))
    print("\nharder controls (200 draws each): mean, best")
    for name, ps in sets[:3:2]:
        for kn, k in keys:
            c = [p5.gloss_score(shuffled_within_kind(k, rng), ps) for _ in range(200)]
            w = [p5.gloss_score(k, wrong_lines(ps, rng, False)) for _ in range(200)]
            h = [p5.gloss_score(k, wrong_lines(ps, rng, True)) for _ in range(200)]
            print("%-12s %-28s same-kind shuffle %.3f, %.3f | wrong line, any %.3f, %.3f | wrong line, same page-half %.3f, %.3f" % (
                name, kn, sum(c) / 200, max(c), sum(w) / 200, max(w), sum(h) / 200, max(h)))


if __name__ == "__main__":
    main(sys.argv[1:])
