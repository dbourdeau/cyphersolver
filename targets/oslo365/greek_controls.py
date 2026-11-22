"""Control for accidental matches in running Greek outside ritual formularies."""
import re
import sys
import unicodedata
from collections import Counter

pats = [re.compile(p) for p in ("γ.......φι","εωτ.....χ","λ....τα","τω....ξ")]
for path in sys.argv[1:]:
    sentences = []
    sent = []
    with open(path,encoding="utf8") as f:
        for line in f:
            if not line.strip():
                if sent:
                    sentences.append(sent)
                sent = []
            else:
                fields = line.split("\t")
                if len(fields)<4 or not fields[0].isdigit():
                    continue
                word = unicodedata.normalize("NFD",fields[1].lower()).replace("ς","σ")
                word = "".join(c for c in word if not unicodedata.combining(c))
                sent.append(word if re.fullmatch("[α-ω]+",word) else "#")
    if sent:
        sentences.append(sent)
    print(path, len(sentences), "sentences")
    hits = [set() for _ in pats]
    for i,p in enumerate(pats):
        whole, tails, continuous = Counter(),Counter(),Counter()
        for j,words in enumerate(sentences):
            for word in words:
                if p.fullmatch(word):
                    whole[word]+=1
                match = re.search(p.pattern+"$",word)
                if match and "#" not in match[0]:
                    tails[word]+=1
            for part in "".join(words).split("#"):
                for m in p.finditer(part):
                    continuous[m[0]]+=1
                    hits[i].add(j)
        print(p.pattern, "whole",sum(whole.values()), "tails",sum(tails.values()),
              "running",sum(continuous.values()),"examples",continuous.most_common(3))
    # Same sentence only, so switching works cannot generate a positive.
    print("Sentences containing 2,3,4 masks",len(set.intersection(*hits[:3])))
