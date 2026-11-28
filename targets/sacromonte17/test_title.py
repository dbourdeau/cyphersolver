"""Check a candidate title against one explicit visual segmentation of LP17 2a."""

# Left to right. R lumps every mainly upright shaft together. T includes open
# and closed triangular forms. B is an upper box, D a cluster of detached marks.
GROUPS = [(245,"R"),(315,"D"),(393,"R"),(430,"R"),(479,"R"),(512,"R"),
          (599,"T"),(660,"B"),(723,"B"),(773,"R"),(855,"T"),(978,"R"),(1114,"D")]


def tests():
    observed = "".join(kind for _, kind in GROUPS)
    # Removing one observation also covers merging a pair and retaining either
    # constituent's class. Try an unrestricted new class for a merged pair too.
    candidates = {observed[:i]+observed[i+1:] for i in range(len(observed))}
    candidates.update(observed[:i]+"?"+observed[i+2:] for i in range(len(observed)-1))
    for title in ("حقيقةالانجيل","حقيقةالإنجيل"):
        assert len(title) == 12
        for direction in ("ltr","rtl"):
            results = []
            for candidate in candidates:
                s = candidate if direction=="ltr" else candidate[::-1]
                mismatches = sum(len(set(s[i] for i,c in enumerate(title)
                                         if c==letter and s[i]!="?"))>1 for letter in set(title))
                results.append(mismatches)
            print(ascii(title), direction, "minimum incompatible repeated letters",min(results))


if __name__ == "__main__":
    tests()
