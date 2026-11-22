"""Test necessary repeat constraints for two candidate openings on folio 3b."""
from itertools import combinations, product
from collections import Counter


# Coordinates on the photographed line, in physical left-to-right order.
# A choice with multiple letters describes a possible split within this span.
# U = upright (including hooked), A = upward angle, V = downward angle,
# B = flat-topped enclosure, D = detached marks. Keep this deliberately coarse.
SPANS = [
    (134,("","D")), (194,("U",)), (257,("U",)), (290,("A",)),
    (348,("U",)), (389,("U",)), (454,("A","AA")),
    (548,("U",)), (575,("U",)), (599,("U",)),
    (698,("V",)), (774,("B",)), (819,("U",)), (891,("A",)),
    (955,("V",)), (1012,("UU","UUU")), (1084,("V",)),
    (1121,("","U")), (1150,("B",)), (1200,("U",)), (1261,("","D")),
]
CRIBS = {
    "title, hamza distinguished":"حقيقةالإنجيل",
    "title, plain alif":"حقيقةالانجيل",
    "basmala":"بسماللهالرحمنالرحيم",
}


def signatures(crib):
    return [[i for i,c in enumerate(crib) if c==letter] for letter in set(crib)
            if crib.count(letter)>1]


def incompatibilities(s, groups):
    # Minimum number of positions to discard before every repeated letter
    # can be assigned one consistent coarse shape.
    return sum(len(g)-max(Counter(s[i] for i in g).values()) for g in groups)


def readings():
    return {"".join(v) for v in product(*(options for _,options in SPANS))}


def pairings(positions):
    if not positions:
        yield ()
        return
    first,*rest = positions
    for i,partner in enumerate(rest):
        for tail in pairings(rest[:i]+rest[i+1:]):
            yield ((first,partner),)+tail


def title_control(paths):
    # Conditional null: all arrangements of three disjoint equal-letter pairs.
    # Other letters are singletons. Different letters can share a coarse class.
    windows = {s[i:i+12] for p in paths for s in (p,p[::-1]) for i in range(len(p)-11)}
    masks = [frozenset((i,j) for i,j in combinations(range(12),2) if s[i]==s[j])
             for s in windows]
    passed = total = 0
    for positions in combinations(range(12),6):
        for pairs in pairings(positions):
            total += 1
            passed += any(mask.issuperset(pairs) for mask in masks)
    print("title control:",passed,"of",total,"three-pair patterns fit a window")
    assert total==13860


def detail_check():
    # Subdivide only the clear uprights at three locations on the source crop.
    # 548 descends left of the shaft; 599 and 819 have a top stroke falling right.
    detail = {548:"H",599:"F",819:"F"}
    g = signatures(CRIBS["title, hamza distinguished"])
    surviving = set()
    examples = {}
    for path in product(*(options for _,options in SPANS)):
        t = [(x,c) for (x,_),s in zip(SPANS,path) for c in s]
        for direction,seq in (("LTR",t),("RTL",t[::-1])):
            for i in range(len(seq)-11):
                w = seq[i:i+12]
                if incompatibilities("".join(c for x,c in w),g): continue
                # An unclassified U could be any subtype. Only a directly
                # opposed pair of classified strokes can reject this window.
                violations = [tuple(w[j][0] for j in pair) for pair in g
                              if {"H","F"}=={detail.get(w[j][0]) for j in pair}]
                if not violations:
                    surviving.add(tuple(w))
                else:
                    examples[direction] = violations
    print("opposed detailed forms:",examples,"surviving windows:",len(surviving))


def evaluate():
    paths = readings()
    print("unique segmentations:",len(paths),"lengths:",sorted(set(map(len,paths))))
    for label,crib in CRIBS.items():
        g = signatures(crib)
        assert incompatibilities(crib,g)==0
        for direction in ("LTR","RTL"):
            starts, all_windows = set(),set()
            for path in paths:
                s = path if direction=="LTR" else path[::-1]
                starts.add(s[:len(crib)])
                all_windows.update(s[i:i+len(crib)] for i in range(len(s)-len(crib)+1))
            for where,windows in (("at start",starts),("anywhere",all_windows)):
                counts = Counter(incompatibilities(s,g) for s in windows)
                print(label,direction,where,"windows",len(windows),"minimum",
                      min(counts),"exact",counts[0])
                if counts[0]:
                    print("compatible coarse sequence(s):",
                          sorted(s for s in windows if incompatibilities(s,g)==0))
    title_control(paths)
    detail_check()


if __name__ == "__main__":
    evaluate()
