"""Held-out test of the syllabary card (K-SYL, CMXV.16.1557.1 scan 3) on CMXV.33.3233.1 (PLAN_2026-11-26.md, step H).

Reads the card from key.tsv (Daniel Jalkut's transcription), as is, row digit then column digit (RC). Decodes the hashed group transcription, compares with the hashed period
decipherment by the plan's measure A, and runs 1,000 permuted cards (seed 1462).
Usage: python3 -I scripts/heldout_test.py
"""
import random, re, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def load_card():
    card = {}
    for line in (HERE / "key.tsv").read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or line.startswith("group	"):
            continue
        g, v = line.split("	")[:2]
        card[g] = v
    assert len(card) == 100
    return card


def read_tsv(name):
    out = []
    for line in (HERE / "heldout" / name).read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#") or line.startswith("stretch\t"):
            continue
        out.append(line.split("\t"))
    return out


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = re.sub(r"[^a-zñ]", "", s)
    s = s.replace("h", "").replace("v", "b").replace("k", "c").replace("ll", "l").replace("rr", "r")
    return s


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def measure(card, stretches, period):
    dec = "".join(card.get(g, "?") for s in stretches for g in s)
    ref = norm("".join(period))
    d = norm(dec)
    return 1 - lev(d, ref) / len(ref), dec


def main():
    card = load_card()
    groups = read_tsv("Ha_3233_groups.tsv")
    period = dict((r[0], r[1]) for r in read_tsv("Ha_3233_period_decipherment.tsv"))
    stretches = [r[2].split() for r in groups]
    texts = [period[r[0]] for r in groups]
    a, dec = measure(card, stretches, texts)
    print("H-a CMXV.33.3233.1, K-SYL RC as is")
    for r, s in zip(groups, stretches):
        print(f"  {r[0]}: {' '.join(card[g] for g in s)}   | period: {period[r[0]]}")
    print(f"A = {a:.3f} (normalised decode length {len(norm(dec))}, period text length {len(norm(''.join(texts)))})")
    rng = random.Random(1462)
    keys = sorted(card)
    vals = [card[k] for k in keys]
    ctrl = []
    for _ in range(1000):
        rng.shuffle(vals)
        ctrl.append(measure(dict(zip(keys, vals)), stretches, texts)[0])
    ctrl.sort()
    print(f"controls: max {ctrl[-1]:.3f}, mean {sum(ctrl)/len(ctrl):.3f}, n >= A: {sum(c >= a for c in ctrl)}")
    verdict = "PASS" if (a >= 0.80 and a > ctrl[-1]) else "MISS"
    print("verdict:", verdict)


if __name__ == "__main__":
    main()


def siblings():
    """The card on the two Villa telegrams of CMXV.33.3231 (no period text; not measurable under the plan)."""
    card = load_card()
    for r in read_tsv("Hb_3231_groups.tsv"):
        print(f"{r[0]} with the card: {' '.join(card[g] for g in r[2].split())}")


if __name__ == "__main__":
    siblings()
