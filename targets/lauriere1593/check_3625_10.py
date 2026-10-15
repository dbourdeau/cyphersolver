"""Test Nevers key no. 57 (La Verrière's own sheet, fr. 3995 ff. 102-103) on fr. 3625 no. 10 (f. 10r), whose cipher
runs carry the office's interlinear decipherment.

    python targets/champagne1590/check_3625_10.py

Two sets are scored separately:
  * ct_3625_10_blind.txt - five runs transcribed from crops that hide the glosses, fixed before the glosses were read.
    This is the independent test of the key.
  * ct_3625_10_rest.txt  - the other eight runs, transcribed with the glosses in view (weaker; a consistency check).

Score: the number of gloss letters that fall in runs of four or more letters matching the decipherment
(difflib matching blocks). Single-letter agreement is not used: alignment inflates it even for noise (a shuffled
control reached 0.74 on a similar letter). Control: the same signs of each run in shuffled order, 2000 times - the
signs, the key and the glosses stay the same; only the order is destroyed. The key is applied as read from the
sheet; nothing is fitted.

Exit 0 when every set scores above every one of its shuffled controls and at least half the gloss letters.
The run the office left unglossed (U1 in ct_3625_10_rest.txt, added when PR 15 was merged) is deciphered and printed,
not scored.
Contributed by setsunaatto (dbourdeau/cyphersolver issue 13).
"""
import random
import sys
from difflib import SequenceMatcher
from pathlib import Path

HERE = Path(__file__).resolve().parent

# --- Key no. 57, read from f. 103r (canvas 200); see key57.txt -------------------------------------------------------
LETTERS = {  # two signs per letter (header rows of f. 103r)
    "lam": "a", "om": "a", "del": "b", "xi": "b", "mu": "c", "rhoC": "c", "Dh": "d", "Dgrid": "d",
    "ye": "e", "Ep": "e", "Fb": "f", "piF": "f", "varpi": "g", "Gs": "g", "Hq": "h", "c": "h",
    "zig": "i", "yi": "i", "beta": "l", "eps": "l", "xm": "m", "Mh": "m", "onplus": "n", "venus": "n",
    "f": "o", "sigma": "o", "caret": "p", "four": "p", "chi": "q", "tbar": "q", "mcross": "r", "ddag": "r",
    "hash": "s", "pi": "s", "tri": "t", "plus": "t", "Vs": "u", "perp": "u", "theta": "x", "inf": "x",
    "X": "y", "o": "y", "a": "z", "eng": "z",
}
SYL = {}  # 1-72: row + 14 * vowel; v and z rows (15, 16) written with an overbar ("15_")
for r, c in enumerate("b c d f g l j m n p qu r s t".split(), 1):
    for v, vo in enumerate("aeiou"):
        SYL[str(r + 14 * v)] = c + vo
for r, c in ((15, "v"), (16, "z")):
    for v, vo in enumerate("aeiou"):
        SYL[f"{r + 14 * v}_"] = c + vo
DOUBLE = dict(zip(map(str, range(73, 99)),
                  "cc dd ff mm nn pp ll rr ss tt bl uu nt ct st ns ng gl gr pr pl ly cr ch fr fl".split()))
WORDS = {  # 99-353, only those that occur in nos. 10 and 55; each checked on the sheet
    "99": "a", "100": "aux", "101": "au", "103": "aussi", "107": "assemblee", "122": "bien", "141": "catholique",
    "150": "congnoistre", "154": "chose", "159": "donne", "160": "desir", "167": "dessein", "175": "escrit",
    "181": "ennemy", "184": "est", "185": "et", "186": "en", "187": "eu", "190": "emeu", "191": "entendre",
    "196": "force", "197": "faire", "202": "prendre", "203": "fait", "211": "fort", "224": "gens", "234": "hault",
    "246": "jamais", "248": "ilz", "255": "longueur", "262": "luy", "279": "mal", "285": "necessaire", "286": "non",
    "288": "nous", "303": "pouvoir", "304": "pour", "305": "par", "307": "quant", "312": "quoy", "320": "sans",
    "334": "son", "335": "soit", "344": "tout", "345": "veult", "346": "volonte", "347": "vous",
}
NAMES = {  # name signs (f. 103v) and bracket-barred province numbers (f. 103r, right-hand table)
    "ROY": "leroy", "PAPE": "pape", "LORRAINE": "leducdelorraine", "MPONT": "lemarquisdepont", "P29": "lespagne",
    "GONDY": "lecarddegondy", "TOSCANE": "legranducdetoscane",
}


def dec(tok):
    for t in (NAMES, LETTERS, SYL, DOUBLE, WORDS):
        if tok in t:
            return t[tok]
    return "?"


def text(toks):
    return "".join(dec(t) for t in toks)


def load(name, sig_tag):
    sig, gloss = {}, {}
    for line in (HERE / name).read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        k, v = line.split("\t")
        if k[0] == sig_tag:
            sig[k[1:]] = v.split()
        elif k[0] == "G":
            gloss[k[1:]] = v.replace(" ", "")
    return [(k, sig[k], gloss[k]) for k in sorted(sig, key=int)]


def load_unglossed(name, tag="U"):
    rows = []
    for line in (HERE / name).read_text(encoding="utf-8").splitlines():
        if line.startswith(tag) and "\t" in line:
            k, v = line.split("\t")
            rows.append((k[1:], v.split()))
    return rows


def runs(lines, minlen=4):
    n = 0
    for toks, plain in lines:
        for b in SequenceMatcher(None, text(toks), plain, autojunk=False).get_matching_blocks():
            if b.size >= minlen:
                n += b.size
    return n


def score(label, rows, rng):
    lines = [(t, p) for _, t, p in rows]
    r, tot = runs(lines), sum(len(p) for _, p in lines)
    ctrl = [runs([(rng.sample(t, len(t)), p) for t, p in lines]) for _ in range(2000)]
    m = sum(ctrl) / len(ctrl)
    sd = (sum((c - m) ** 2 for c in ctrl) / len(ctrl)) ** 0.5
    ok = r > max(ctrl) and r >= 0.5 * tot
    print(f"{label}: {r} / {tot} gloss letters in runs of >= 4 ({r / tot:.0%}); "
          f"shuffled control {m:.1f} +/- {sd:.1f} (max {max(ctrl)}); Z = {(r - m) / sd:+.1f}; "
          f"controls >= real: {sum(c >= r for c in ctrl)}/2000  [{'pass' if ok else 'FAIL'}]", flush=True)
    return ok


def main():
    blind = load("ct_3625_10_blind.txt", "L")
    rest = load("ct_3625_10_rest.txt", "R")
    for tag, rows in (("L", blind), ("R", rest)):
        for k, t, p in rows:
            print(f"{tag}{k:<2} key   {text(t)}\n    gloss {p}", flush=True)
    for k, t in load_unglossed("ct_3625_10_rest.txt"):
        print(f"U{k:<2} key   {text(t)}\n    (no gloss; not scored)", flush=True)
    print(flush=True)
    rng = random.Random(0)
    ok = score("blind, 5 runs", blind, rng)
    ok &= score("blind, without L1 (seen when the key was first applied)", blind[1:], rng)
    ok &= score("the other 8 runs (not blind)", rest, rng)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
