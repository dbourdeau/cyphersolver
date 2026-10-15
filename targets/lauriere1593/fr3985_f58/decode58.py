"""Decode fr. 3985 f. 58 (La Verriere to Nevers, Poissy, 12 Aug 1593) with Nevers key no. 57.

    python targets/champagne1590/fr3985_f58/decode58.py

Key: ../check_3625_10.py tables (alphabet, syllables, doubles, names) plus the full word list read off f. 103r for
this letter (words57.tsv). Prints each run: the decipherment group by group, and the office's gloss.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import check_3625_10 as k  # noqa: E402

WORDS = {}
for line in (HERE / "words57.tsv").read_text(encoding="utf-8").splitlines():
    if not line or line.startswith("#"):
        continue
    num, val = line.split("\t", 1)
    WORDS.setdefault(num, val.split(" / ")[0].split(" (")[0].rstrip("?"))
WORDS["320"] = "religion"  # both values on the sheet; context decides (see reading.md)
NAMES = dict(k.NAMES)
NAMES.update({"NAME:Conty": "[prince de Conty]", "NAME:Montmorency": "[M. de Montmorency]",
              "NAME:CardBourbon": "[Cardinal de Bourbon]", "PAPE": "[Pape]"})
SLIPS = {}  # signs written that the context and gloss correct; see reading.md


def dec(tok):
    if tok.startswith("{"):
        return tok
    if re.fullmatch(r"v\d+", tok):
        return k.SYL[tok[1:] + "_"]
    if tok in NAMES:
        return NAMES[tok]
    if tok in k.LETTERS:
        return k.LETTERS[tok]
    if tok.endswith("_"):
        if tok in WORDS:
            return WORDS[tok]
        if tok in k.SYL:
            return k.SYL[tok]
        return "[" + WORDS.get(tok, tok) + "]"
    if tok in k.SYL:
        return k.SYL[tok]
    if tok in k.DOUBLE:
        return k.DOUBLE[tok]
    if tok in WORDS:
        return "<" + WORDS[tok] + ">"
    return "?"


def runs():
    out = []
    for line in (HERE / "ct.txt").read_text(encoding="utf-8").splitlines():
        if line[:1] in "AB" and "\t" in line:
            tag, sig = line.split("\t")
            out.append((tag, sig.split()))
    return out


# Reading of each run, and the 0-based indices (clear-text braces excluded) of cipher tokens NOT read as sense.
# A token counts as read when its key value (or a slip correction listed in reading.md) gives a word of the reading.
# Reading of each run, and the 0-based indices (clear-text braces excluded) of cipher tokens NOT read as sense.
# A token counts as read when its key value (or a slip correction listed in reading.md) gives a word of the reading.
# Pass 2, 3 Oct 2026 (lossless PNG regions, enhancement, name panel f. 103v): see reading.md.
READING = {
    "A1": "pour le fait du [prince de Conty] qui",
    "A2": "desire de ritirer, mais il ne s[ai]t a qui le confier, estre-nt (estant) la personne qui luy est de",
    "A3": "plus d'importance. Ma[d]ame d'Angoulesme est port[ee] du tout a la maison de [M. de Montmorency] et le pr[i]nci",
    "A4": "pall apuy qu'il ayi(t), soi(t) des catholiques, soit de ceux de la religion, soi(t) de c[est]e maison",
    "A5": "s'il y aveoit quelque remuemant. [Vo]la pourquoy",
    "A6": "il desiree faire eleoction d'ung [fi]delle serviteur et [340] le lieu ou il le pourra",
    "A7": "mettre (et point) l'oter, instruire, gagnet monsieur de la Trimoule pour ne donner",
    "A8": "aucung soub[s] son a ceux de la religion (estans tous) de nature defians",
    "B1": "a [Espagnols] [?] [Pape]",
    "B2": "[?]",
    "B3": "lettre[s] [du] [Pape] pour atanter a la",
    "B4": "[?] [duc de Lorraine]",
    "B5": "personne de [Cardinal de Bourbon]",
}
OPEN = {
    "A2": [13, 14],             # two signs inside s..t (sait): a blot and a 2-shaped sign that is no a or i sign
    "A4": [30, 31, 32],         # the three middle signs of c...e (ceste): '1 5 4' shapes, no key value gives -est-
    "A6": [24],                 # 340 'taboure' on the sheet (office: 'tabour'): no sense in 'et [340] le lieu'
    "B1": [2],                  # the sign after the Espagnols number (gloss 'aux Esp... au Pape')
    "B2": [0, 1, 2],            # 6 lam 340: 'la a/p taboure', gloss 'la plu...': no sense
    "B4": [0, 1, 2],            # 28 25 202 'te que font' before [duc de Lorraine]: no sense; 303 struck
}


def main():
    total = read = 0
    plain = []
    for tag, toks in runs():
        ct = [t for t in toks if not t.startswith("{")]
        n_open = len(OPEN.get(tag, []))
        total += len(ct)
        read += len(ct) - n_open
        print(f"{tag} ({len(ct) - n_open}/{len(ct)} read)")
        print("   key :", " ".join(dec(t) for t in toks))
        print("   read:", READING[tag])
        if tag.startswith("A"):
            plain.append(re.sub(r"\[[^]]*\]|\([^)]*\)", "", READING[tag]))
    print(f"\ncipher tokens {total}; read as sense {read} ({read / total:.1%}); open {total - read}")
    try:
        sys.path.insert(0, str(HERE.parents[2]))
        from lang import lm
        text = " ".join(plain)
        m = lm.load("fr-1600-letters")
        print("fr-1600-letters per-char, run A reading:", round(m.per_char(lm.norm(text, "early")), 3))
        print("best_language:", [(round(a, 3), b) for a, b in lm.best_language(text)[:3]])
    except Exception as e:  # the LM is a check, not part of the count
        print("LM check skipped:", e)


if __name__ == "__main__":
    main()
