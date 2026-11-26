"""Join attested Geniza word pairs and test one bijection across both faces."""
import sys
from collections import Counter, defaultdict
from pathlib import Path
from zipfile import ZipFile

from corpus_check import normalize
from crib_check import R11, R12


def extend(key, signs, word):
    result = key.copy()
    for s, c in zip(signs, word, strict=True):
        if s in result:
            if result[s] != c:
                return None
        elif c in result.values():
            return None
        else:
            result[s] = c
    return result


def token(raw):
    if any(c in raw for c in "[].…"):
        return ""
    return normalize(raw)


def run(path):
    freq, pairs = Counter(), Counter()
    definite, before_kama = Counter(), Counter()
    seen = set()
    with ZipFile(path) as z:
        for name in sorted(z.namelist()):
            if not name.endswith("_transcription.txt"):
                continue
            doc = Path(name).parent.name
            if doc in seen or doc == "9097":
                continue
            raw = z.read(name).decode("utf-8-sig")
            words = [token(w) for w in raw.split()]
            if words.count("אללה") < 2:
                continue
            seen.add(doc)
            definite.update({w[len(prefix):] for w in words for prefix in ("אל","ואל")
                             if w.startswith(prefix) and len(w[len(prefix):]) == 5})
            before_kama.update({x for x,y in zip(words,words[1:]) if len(x)==4 and y=="כמא"})
            freq.update({w for w in words if len(w) in (2,4,5)})
            pairs.update({(x,y) for x,y in zip(words,words[1:])
                          if (len(x),len(y)) in ((5,2),(2,4),(4,2),(2,5))})
    print("documents",len(seen))
    for direction in (1,-1):
        lengths = (5,2,4)[::direction]
        left, right = defaultdict(list), defaultdict(list)
        for x,y in pairs:
            if (len(x),len(y)) == lengths[:2]:
                left[y].append(x)
            if (len(x),len(y)) == lengths[1:]:
                right[x].append(y)
        front = defaultdict(list)
        for w in freq:
            if len(w)==5 and len(set(w))==5:
                oriented = w[::direction]
                front[oriented[0],oriented[-1]].append(w)
        for penultimate, final in ((8,8),(8,-2),(-2,8)):
            signs = [1,60,100,400,40,1,100,1,-1,penultimate,final][::direction]
            matches = []
            verso_hits = 0
            for y in left.keys() & right.keys():
                for x in left[y]:
                    for z in right[y]:
                        back = extend({},signs,x+y+z)
                        if back is None:
                            continue
                        verso_hits += 1
                        for f in front[back[400],back[40]]:
                            key = extend(back,R11[::direction],f)
                            if key is None:
                                continue
                            for c in "אבגדהוזחטיכלמנסעפצקרשת":
                                if c in key.values():
                                    continue
                                key[10] = c
                                g = "".join(key[s] for s in R12[::direction])
                                del key[10]
                                if g in freq:
                                    matches.append((min(freq[f],freq[g],pairs[x,y],pairs[y,z]),
                                                    f,g,x,y,z))
            print(direction,penultimate,final,"back triples",verso_hits,"joint readings",len(matches))
            contextual = [m for m in matches if definite[m[1]] and before_kama[m[2]]]
            print("both recto contexts",len(contextual))
            for m in sorted(contextual,reverse=True)[:3]:
                print("context",*m)
            for result in sorted(matches,reverse=True)[:4]:
                print(*result)


if __name__ == "__main__":
    run(sys.argv[1])
