"""Compare our transcription of the six coded sections (../transcription_six_sections.txt) group by group
with Brice Dudout's files (../../dudout/texts/*_transcription.txt) and the project's
(../../everett1825_transcription.txt), and print the agreement counts.

    python targets/everett1825/beling/scripts/compare.py            # counts per section
    python targets/everett1825/beling/scripts/compare.py --list     # also every differing or unmatched group

Python standard library only; runs from any folder. Alignment: per section, difflib.SequenceMatcher on the
numbers (marks ignored), autojunk off; a 'replace' block of equal length is compared position by position,
an unequal one would be reported as ambiguous (there are none).
"""
import difflib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.normpath(os.path.join(HERE, "..", ".."))
OURS = os.path.join(TARGET, "beling", "transcription_six_sections.txt")


def number(tok):
    m = re.match(r"-?(\d+)", tok)
    return m.group(1) if m else None


def read_ours():
    secs = {}
    for line in open(OURS, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        sec, loc, groups = line.rstrip("\n").split("\t")
        for pos, tok in enumerate(groups.split(), 1):
            secs.setdefault(sec, []).append((f"{loc}.{pos}", tok, number(tok)))
    return secs


def read_dudout(page):
    out = []
    path = os.path.join(TARGET, "dudout", "texts", f"{page}_transcription.txt")
    rows = [l for l in open(path, encoding="utf-8") if not l.startswith("#")]
    for li, l in enumerate(rows, 1):
        pos = 0
        for tok in l.split():
            if number(tok):
                pos += 1
                out.append((f"{page}.L{li}.{pos}", tok, number(tok)))
    return out


def read_project(passages):
    out, lineno = [], {}
    for l in open(os.path.join(TARGET, "everett1825_transcription.txt"), encoding="utf-8"):
        if not (l[:1] in "ABC" and l[1:2] == " "):
            continue
        t = l.split()
        lineno[t[0]] = li = lineno.get(t[0], 0) + 1
        if t[0] not in passages:
            continue
        for pos, g in enumerate([x for x in t[1:] if number(x)], 1):
            out.append((f"{t[0]}.L{li}.{pos}", g, number(g)))
    return out


def main():
    listing = "--list" in sys.argv
    ours = read_ours()
    p01, p03 = read_dudout("p01_0112"), read_dudout("p03_0113")
    dudout = {
        "S1": p01[:6], "S2": p01[6:],
        "S3": read_dudout("p02_0113") + p03[:38],
        "S4": p03[38:] + read_dudout("p04_0114") + read_dudout("p05_0114") + read_dudout("p06_0115"),
        "S6": read_dudout("p17_0120") + read_dudout("p18_0121"),
    }
    project = {"S5": read_project("A"), "S6": read_project("BC")}
    print("section\tcompared_with\tours\ttheirs\tin_both\tagree\tdiffer\tonly_ours\tonly_theirs\tambiguous")
    total = dict(both=0, agree=0, differ=0, only_ours=0, only_theirs=0)
    rows = []
    for who, other in (("Dudout", dudout), ("project", project)):
        for sec in sorted(other):
            mine, theirs = ours[sec], other[sec]
            c = dict(both=0, agree=0, differ=0, only_ours=0, only_theirs=0, ambiguous=0)
            sm = difflib.SequenceMatcher(None, [x[2] for x in mine], [x[2] for x in theirs], autojunk=False)
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
                    for k in range(i2 - i1):
                        m, t = mine[i1 + k], theirs[j1 + k]
                        c["both"] += 1
                        if m[2] == t[2]:
                            c["agree"] += 1
                        else:
                            c["differ"] += 1
                            rows.append((sec, who, "differ", m[0], m[1], t[0], t[1]))
                else:
                    if op == "replace":
                        c["ambiguous"] += 1
                    for m in mine[i1:i2]:
                        c["only_ours"] += 1
                        rows.append((sec, who, "only ours", m[0], m[1], "", ""))
                    for t in theirs[j1:j2]:
                        c["only_theirs"] += 1
                        rows.append((sec, who, "only theirs", "", "", t[0], t[1]))
            print("\t".join(map(str, [sec, who, len(mine), len(theirs), c["both"], c["agree"], c["differ"],
                                      c["only_ours"], c["only_theirs"], c["ambiguous"]])))
            if who == "Dudout":
                for k in total:
                    total[k] += c[k]
    print("Dudout, sections 1-4 and 6:", ", ".join(f"{k} {v}" for k, v in total.items()))
    print("ours, all six sections:", sum(len(v) for v in ours.values()), "groups")
    if listing:
        print("\nsection\tcompared_with\tkind\tour_locus\tour_group\ttheir_locus\ttheir_group")
        for r in rows:
            print("\t".join(r))


if __name__ == "__main__":
    main()
