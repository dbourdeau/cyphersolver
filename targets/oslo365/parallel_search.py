"""Check the Oslo verso against Kyprianos (July 2026 text CSV).

Pass the local CSV path. No editorial additions or lacunae are crossed.
Only transliterate the shared Greek/Coptic alphabet when explicitly requested.
Line 5 is kept out of the selection of parallel passages.
"""
import csv
import re
import sys
import unicodedata
from collections import defaultdict
from random import Random

patterns = ["γ.......φι", "εωτ.....χ", "λ....τα"]
coptic = dict(zip("ⲁⲃⲅⲇⲉⲍⲏⲑⲓⲕⲗⲙⲛⲝⲟⲡⲣⲥⲧⲩⲫⲭⲯⲱ", "αβγδεζηθικλμνξοπρστυφχψω"))


def segments(line, use_coptic):
    line = unicodedata.normalize("NFD", line.lower()).replace("ς","σ").replace("ϲ","σ")
    line = "".join(c for c in line if not unicodedata.combining(c))
    line = re.sub(r"\[[^\]]*(?:\]|$)|\([^)]*\)|⟨[^⟩]*⟩|\{[^}]*\}", "#", line)
    if use_coptic:
        line = "".join(coptic.get(c,c) for c in line)
    return re.findall(r"[α-ω]+", re.sub(r"[ \t]", "", line))


def search(records, pats):
    hits = defaultdict(list)
    compiled = [re.compile("(?=(" + p + "))") for p in pats]
    for ident, lineno, segment in records:
        for i, pat in enumerate(compiled):
            for match in pat.finditer(segment):
                hits[i].append((ident,lineno,match[1]))
    return hits


def chains(hits, distance):
    result = set()
    for a, b in [(0,1), (1,2), (0,2)]:
        for key, index, _ in hits[a]:
            for other, following, _ in hits[b]:
                if key == other and 0 < following-index <= distance:
                    result.add((key,index,following,a,b))
    return sorted(result)


rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")))
for mapped in (False, True):
    records = [(r["text_id"], n, s) for r in rows
               for n, line in enumerate(r["text"].splitlines(), 1)
               for s in segments(line, mapped) if len(s)>=7]
    hits = search(records, patterns)
    print("Coptic mapping", mapped, "records", len(records), "texts", len({r[0] for r in records}))
    print("Strict counts", [len(hits[i]) for i in range(3)], "pairs within 5", chains(hits,5))
    ordered = chains(hits,20)
    print("Pairs within 20", ordered)
    # Test the prediction downstream only after selecting by lines 2-4.
    fifth = search(records, ["τω....ξ","βωβελιξ"] )
    print("Fifth checks", [fifth[i] for i in range(2)])
    print("Predictions following pairs", [(p,h) for p in ordered for h in fifth[0]+fifth[1]
                                         if h[0]==p[0] and 0<h[1]-p[2]<=20])
    # Let each estimated gap expand or contract by a single sign.
    flex = ["γ.{6,8}φι","εωτ.{4,6}χ","λ.{3,5}τα"]
    fh = search(records, flex)
    print("Flexible counts", [len(fh[i]) for i in range(3)], "pairs", chains(fh,5))
    # Test the opposite arrangement of name strings (retrograde writing).
    back = search(records, [p[::-1] for p in patterns])
    print("Retrograde counts", [len(back[i]) for i in range(3)], "pairs", chains(back,5))
    # Conditional control: permute the fixed letters among their positions.
    rng = Random(365)
    fixed = list("γφιεωτχλτα")
    null = []
    for trial in range(40):
        rng.shuffle(fixed)
        it = iter(fixed)
        scrambled = ["".join(next(it) if c != "." else "." for c in p) for p in patterns]
        null.append(len(chains(search(records,scrambled),5)))
    print("Controls with pairs", sum(n>0 for n in null), "of", len(null))

# Subject-selected corpora; the title and translation select the witnesses
# before any letters are tested. Unordered co-occurrences are reported too.
for label, terms in [
    ("Isis", ["isis"]),
    ("Osiris", ["osiris"]),
    ("Attraction", ["love spell", "attraction", "love charm"]),
    ("Compulsion", ["compel", "compulsion", "constrain"]),
    ("Star", ["constellation", "star"]),
]:
    selected = [r for r in rows if any(t in (r["conventional title"]+" "+r["translation"]).lower()
                                       for t in terms)]
    records = [(r["text_id"],n,s) for r in selected for n,line in enumerate(r["text"].splitlines())
               for s in segments(line,True) if len(s)>=7]
    hits = search(records, patterns)
    print(label,len(selected), [len(hits[i]) for i in range(3)], chains(hits,20))

# Additional hypotheses for extraction from the same formulary. Require
# agreement of all identified letters for an exact candidate.
for label, transform in [
    ("palindrome-name halves reflected", lambda s:s+s[::-1]),
    ("doubled recitation", lambda s:s+s),
    ("one-letter contraction repeated", lambda s:"".join(s[:j] for j in range(len(s),0,-1))),
    ("initial-letter contraction repeated", lambda s:"".join(s[j:] for j in range(len(s)))),
    ("vowel expansion by seven-vowel series", lambda s:"".join("αεηιουω" if c in "αεηιουω" else c for c in s)),
]:
    # Explicit candidate names are those in edited recitations; splitting
    # the entire continuous text at guessed, novel boundaries is avoided.
    names = "χοιθ σαφουθ χενθονευ αφουθ ανουαωθ ιακωβ μαννοχ αραννουθ χαλωαφ κουλιξ βορναθ λουβεινε αρουηρ ουειρε ιτινλοτολ γμοηρ μενδουμβα φθοηρι θερμοηρ φθαω φνουθουηρ βωβελιξ φνουχ μελλανχιω κερδω μελιβευ".split()
    rec = [(n,0,transform(n)) for n in names]
    hits = search(rec,patterns)
    print(label, [sorted({h[0] for h in hits[i]}) for i in range(3)])

# Give each candidate formula the opportunity to place each surviving mask
# across a word boundary. This deliberately permits new combinations, so a
# match would need independent support. The front supplies the ingredients.
for label, joiner in [
    ("two adjoining names", ""),
    ("ei refrain", "ειειει"),
    ("great-named epithet", "ομεγαλωνυμος"),
    ("Iako invocation", "ιακω"),
    ("Iothe invocation", "ιωθη"),
]:
    rec = [(a+" "+b,0,a+joiner+b) for a in names for b in names]
    hits = search(rec, patterns)
    print(label, "individual counts", [len(hits[i]) for i in range(3)],
          "first two supported together", sorted({h[0] for h in hits[0]} & {h[0] for h in hits[1]}))
