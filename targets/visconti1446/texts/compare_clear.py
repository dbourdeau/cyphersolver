"""Compare independent cipher readings of BnF italien 1584 slips with the contemporary / fair-copy clear texts.

    python texts/compare_clear.py            (from targets/visconti1446)

Pairs: f23 reading and f24 reading vs f25 clear; f72 reading vs f73 clear; f102 reading vs f103 clear.
f24_reading.md is only a note (it defers to f23), so the f24 line-by-line reading f24_plain.txt is used.

Normalisation: lowercase, u=v, i=j=y, accents and punctuation dropped, apostrophes split words, expansions in
round brackets kept as letters, editorial [..] / [?] / [..N..] gaps and editorial notes dropped, letters restored in
square brackets kept, {null} markers dropped, line-break hyphens joined.

Counts: words in the reading (after dropping gaps); words matching the clear text exactly after normalisation;
words matching as spelling variants (same word in another spelling: doubled letters, h, ct/tt, z/c, etc.,
or difflib ratio >= 0.75 inside an aligned replace block). Remaining differences are listed for review.
"""
import difflib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent

PAIRS = [
    ("f23_reading.md", "f25_clear.md"),
    ("f24_plain.txt", "f25_clear.md"),
    ("f72_reading.md", "f73_clear.md"),
    ("f102_reading.md", "f103_clear.md"),
]


def body(path):
    """Text lines of a transcription file, without the heading, notes paragraphs and check-lists."""
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    if path.name.endswith("_clear.md"):
        # transcription lines end with " /" or are the last line(s) of the letter block
        started = False
        for ln in lines:
            if ln.startswith("#") or ln.startswith("(Readings"):
                continue
            if not started:
                if ln.rstrip().endswith("/"):
                    started = True
                else:
                    continue
            if not ln.strip():
                if started and out:
                    break
                continue
            out.append(ln)
    elif path.suffix == ".txt":
        out = [re.sub(r"^L\d+:\s*", "", ln) for ln in lines if ln.strip()]
    else:
        out = [ln for ln in lines if ln.strip() and not ln.startswith("#")]
    text = "\n".join(out)
    text = re.sub(r"-\s*/?\s*\n\s*-?", "", text)  # line-break hyphens (also "Bar- /")
    text = text.replace("/", " ")
    return text


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def tokens(text, clear):
    t = text
    t = re.sub(r"\{[^}]*\}", " ", t)  # {null}
    t = t.replace("**", "")
    if clear:
        t = re.sub(r"\[[^\]]*\]", " ", t)  # all editorial notes in the clear texts
    else:
        t = re.sub(r"\[\.\.[^\]]*\]", " ", t)  # [..] [..16 signs..]
        t = re.sub(r"\[(name sign|closing group)[^\]]*\]", " ", t)
        t = t.replace("[?]", "").replace("?]", "]")
        t = t.replace("[", "").replace("]", "")
    t = t.replace("(", "").replace(")", "")
    t = strip_accents(t.lower()).replace("’", "'")
    t = re.sub(r"[^a-z' ]+", " ", t.replace("\n", " "))
    t = t.replace("'", " ")
    t = t.replace("v", "u").replace("j", "i").replace("y", "i")
    return t.split()


# dialect / spelling pairs of the same word (Lombard chancery vs Tuscanising forms, apocope, date numerals)
CANON = {"e": "et", "a": "ad", "noi": "nui", "uoi": "uui", "par": "pare", "far": "fare", "son": "sono",
         "di": "de", "le": "li", "data": "datum", "dato": "datum", "soa": "sua", "soi": "suoi", "ben": "bene",
         "como": "come", "xxiii": "uintitre", "u": "quinto", "cioe": "zoe", "maiestate": "maiesta",
         "etcetera": "etcetera", "faciti": "facete", "hauiti": "hauete", "haueua": "hauia"}


def skeleton(w):
    """Spelling-insensitive key."""
    w = CANON.get(w, w)
    s = w.replace("h", "")
    s = s.replace("ct", "t").replace("x", "s").replace("z", "c").replace("ti", "ci")
    s = s.replace("q", "c").replace("k", "c")
    s = re.sub(r"(.)\1+", r"\1", s)
    s = s.replace("n", "m") if len(s) > 4 else s
    return s


def variant(a, b):
    if skeleton(a) == skeleton(b):
        return True
    return len(a) > 3 and len(b) > 3 and difflib.SequenceMatcher(None, skeleton(a), skeleton(b)).ratio() >= 0.75


def compare(rname, cname):
    r = tokens(body(HERE / rname), clear=False)
    c = tokens(body(HERE / cname), clear=True)
    sm = difflib.SequenceMatcher(None, [skeleton(w) for w in r], [skeleton(w) for w in c], autojunk=False)
    exact = var = 0
    diffs = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for a, b in zip(r[i1:i2], c[j1:j2]):
                if a == b:
                    exact += 1
                else:
                    var += 1
            continue
        rs, cs = r[i1:i2], c[j1:j2]
        if op == "replace" and len(rs) == len(cs) and all(variant(a, b) for a, b in zip(rs, cs)):
            var += len(rs)
            continue
        # pair off spelling variants inside an uneven block
        rest_r = []
        cs_left = list(cs)
        for a in rs:
            hit = next((k for k, b in enumerate(cs_left) if variant(a, b)), None)
            if hit is None:
                rest_r.append(a)
            else:
                var += 1
                cs_left.pop(hit)
        if rest_r or cs_left:
            ctx = " ".join(c[max(0, j1 - 3):j1])
            diffs.append((op, " ".join(rs) or "-", " ".join(cs) or "-", ctx))
    n = len(r)
    print(f"\n=== {rname} vs {cname}")
    print(f"words in reading: {n}   clear-text words: {len(c)}")
    print(f"exact (normalised) matches: {exact}   spelling variants: {var}")
    print(f"agreement: exact {100*exact/n:.1f}%   exact+variant {100*(exact+var)/n:.1f}%"
          f"   (clear text covered {100*(exact+var)/len(c):.1f}%)")
    print("differences (reading -> clear, after '...'):")
    for op, a, b, ctx in diffs:
        print(f"  [{op}] ...{ctx} | reading: {a} | clear: {b}")
    return n, exact, var


if __name__ == "__main__":
    pairs = PAIRS if len(sys.argv) < 3 else [(sys.argv[1], sys.argv[2])]
    for rn, cn in pairs:
        compare(rn, cn)
