"""Language measures for CMXV.35.3492.2-3 under the syllabary card (key.tsv), each against 1,000 permuted cards.

1. W, the frozen plan's measure (plan/PLAN_2026-11-25.md): share of decoded letters covered by the best segmentation
   into words of the repository's Spanish lexicon (lang/lexicons/es.json.gz, count >= 3, two letters or more, ñ -> n)
   plus 14 names (Ornelas, Ávila, Villa, ...). Fit rule: W >= 0.80 and above every control.
2. S, chosen AFTER the plan run had been seen (so an after-the-plan check only): mean per letter of the best
   segmentation score, a word of length L scoring L * log10(its count), an uncovered letter -2.
Controls: the card's 100 values shuffled among its 100 cells, seed 1462, drawn afresh for each measure. (In the
frozen run of 25 Nov the controls for this card came late in one seeded stream shared with the other 15 key
variants, so the control maxima differ: there 0.980, here 0.9688. With this fresh draw the card's W is above every
control and would meet the plan's rule; the registered result is the frozen run's miss.)
With --controls, prints the three best controls under S, segmented, to compare by eye.
Usage: CYPHERSOLVER_REPO=<checkout of dbourdeau/cyphersolver> python3 -I scripts/measures.py [--controls]
"""
import gzip, json, math, os, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
REPO = Path(os.environ.get("CYPHERSOLVER_REPO", HERE.parent.parent))
NAMES = ["ornelas", "avila", "villa", "juarez", "chihuahua", "gonzalez", "garza", "torreon", "carranza", "madero",
         "bonilla", "luque", "ojinaga", "diaz"]
sys.path.insert(0, str(HERE / "scripts"))
import decrypt  # noqa: E402


def lexicon():
    d = json.load(gzip.open(REPO / "lang/lexicons/es.json.gz"))
    f = {}
    for w, c in d.items():
        if c >= 3 and len(w) >= 2:
            w = w.replace("ñ", "n")
            f[w] = max(f.get(w, 0), c)
    for n in NAMES:
        f.setdefault(n, 10)
    return f


def best(text, f, word_score, miss, maxlen=20):
    t = text.replace("ñ", "n")
    n = len(t)
    b = [0.0] + [-1e18] * n
    back = [None] * (n + 1)
    for i in range(1, n + 1):
        b[i], back[i] = b[i - 1] + miss, None
        for j in range(max(0, i - maxlen), i - 1):
            w = t[j:i]
            if w in f:
                v = b[j] + word_score(w, f)
                if v > b[i]:
                    b[i], back[i] = v, j
    seg, i = [], n
    while i > 0:
        if back[i] is None:
            seg.append(t[i - 1].upper()); i -= 1
        else:
            seg.append(t[back[i]:i]); i = back[i]
    return b[n], list(reversed(seg))


def W(text, f):
    return best(text, f, lambda w, f: len(w), 0.0)[0] / len(text)


def S(text, f):
    return best(text, f, lambda w, f: len(w) * math.log10(f[w]), -2.0)[0] / len(text)


def main():
    k = decrypt.key()
    groups = [g for _, gs in decrypt.lines() for g in gs]
    text = "".join(k[g] for g in groups)
    f = lexicon()
    for name, m in (("W (plan measure)", W), ("S (after the plan)", S)):
        rng = random.Random(1462)
        ks, vs = list(k), list(k.values())
        real = m(text, f)
        ctrl = []
        for _ in range(1000):
            rng.shuffle(vs)
            pk = dict(zip(ks, vs))
            ctrl.append(m("".join(pk[g] for g in groups), f))
        print(f"{name}: card {real:.4f}; controls max {max(ctrl):.4f}, mean {sum(ctrl)/len(ctrl):.3f}; "
              f"controls >= card: {sum(c >= real for c in ctrl)} of 1000")
    if "--controls" in sys.argv:
        rng = random.Random(1462)
        ks, vs = list(k), list(k.values())
        res = []
        for _ in range(1000):
            rng.shuffle(vs)
            t = "".join(dict(zip(ks, vs))[g] for g in groups)
            res.append((S(t, f), t))
        res.sort(reverse=True)
        for s, t in res[:3]:
            print(f"control S={s:.3f}:", " ".join(best(t, f, lambda w, f: len(w), 0.0)[1]))
        print("card       :", " ".join(best(text, f, lambda w, f: len(w), 0.0)[1]))


if __name__ == "__main__":
    main()
