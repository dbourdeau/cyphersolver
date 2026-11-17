"""Score a key against the clerk's decryptions: test half, fit half, fresh lines, each volume, with a shuffled-key control.

  CIPHER_DATA=transcription python3 scripts/evaluate.py ../table/TABLE-C04.json [more keys or TSVs of additions]
A .tsv argument (number, C04, new, ...) is applied on top of the first key.
Split, chosen by M. German before any key change: fit = 19/102 plus even pages elsewhere; test = odd pages outside 19/102.
Measure: share of decryption letters reproduced in order by the decoding, runs of 3+ letters only.
"""
import csv, os, random, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p5
from common import norm


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


if __name__ == "__main__":
    main(sys.argv[1:])
